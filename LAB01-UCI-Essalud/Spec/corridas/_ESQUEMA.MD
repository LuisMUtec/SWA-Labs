# Esquema de una corrida

Una corrida es una medición completa de `Requirements/ReqFunc.MD` contra la rúbrica de
`Spec/Eval-Spec.MD`: una sola pasada sobre un estado congelado del repositorio, con un veredicto al
final. Este documento fija qué deja escrito, dónde y qué puede tocar.

## Por qué el resultado no cabe en un archivo

El resultado de una corrida tiene cuatro lectores con necesidades incompatibles:

| Lector | Qué necesita | Vida útil |
|---|---|---|
| Quien revisa el entregable | una página: veredicto, dimensiones, brechas | la corrida actual |
| Quien corrige `ReqFunc.MD` | la evidencia entera, diffeable contra la corrida anterior | la corrida actual |
| Quien pregunta si el trabajo avanza | una fila por corrida, comparable | todas las corridas |
| El control de aritmética | los puntajes como números, no como prosa | la corrida actual |

Un solo documento sirve mal a los cuatro: el resumen queda sepultado bajo la evidencia, la evidencia
no se puede diffear, la historia se sobrescribe en cada corrida y los números no se pueden verificar.

## Estructura

```
Spec/
  Eval-Spec.MD                          rúbrica — solo lectura durante la corrida
  Eval-Report.MD                        resumen de la corrida actual, 1–2 páginas
  HISTORIAL.MD                          append-only, una fila por corrida
  corridas/
    _ESQUEMA.MD                         este documento
    <AAAA-MM-DD>-<etiqueta>/
      corrida.json                      cabecera y puntajes, legibles por script
      controles.txt                     salida literal de verificar.sh y su código de salida
      bloqueos.MD                       lo que la corrida no pudo corregir; se omite si no hubo
      veredicto-rodrigo.MD
      veredicto-milagros.MD
      veredicto-carmen.MD
      veredicto-anibal.MD
      diagnostico.MD                    las tablas de evidencia de Eval-Spec §Salida
```

La etiqueta del directorio es la de la rama de trabajo sin su prefijo: la rama `eval/agentes-estandar`
corriendo el 13 de agosto de 2026 produce `2026-08-13-agentes-estandar`.

**Una corrida mide una vez.** No itera ni corrige `ReqFunc.MD`: emite su veredicto y termina. La
corrección de los requerimientos es trabajo de otra rama, con su propia revisión, y se comprueba con
una corrida posterior. Medir y corregir en la misma ejecución destruye la medición, porque quien
corrige conoce la vara.

**No hay tope de corridas.** `Spec/corridas/` guarda un directorio por cada una y `HISTORIAL.MD` una
fila por cada una, sin límite: el número de veces que vale la pena reevaluar los requerimientos no lo
decide este esquema.

**Un veredicto por archivo** es lo que hace comparable una corrida con la siguiente. `git diff` entre
dos directorios de corrida muestra exactamente qué RF pasó de `Ambiguo` a `Sirve` y para qué persona,
que es lo que una mejora tiene que poder atribuir a un cambio concreto. Dentro de un documento único,
ese diff es ilegible.

## Qué puede tocar una corrida

Puede crear o modificar exclusivamente:

- `Spec/corridas/‹id-de-esta-corrida›/` y todo lo que va dentro.
- `Spec/Eval-Report.MD`.
- `Spec/HISTORIAL.MD`, **solo agregando su fila**.
- La aparición del porcentaje en la línea «Resultado del agente» de `README.md`, y nada más de esa
  línea.

Todo lo demás es de solo lectura: `Personas/*`, `Agents/*`, `Requirements/*`, `docs/*`,
`Spec/Eval-Spec.MD`, este esquema, los directorios de corridas anteriores y `scripts/*`. La única
excepción es la comprobación de conformidad de [`../../Agents/README.md`](../../Agents/README.md), que
ocurre antes de leer un RF y puede corregir un agente desviado; terminada esa comprobación, `Agents/*`
vuelve a ser de solo lectura.

`scripts/guardia-diff.sh` comprueba esta lista y se ejecuta como control E4. Lo que quede fuera y aun
así haga falta corregir se registra en `bloqueos.MD` y se reporta; no se corrige a escondidas.

## Cabecera de reproducibilidad

Encabeza `Eval-Report.MD` y se repite, campo por campo, en `corrida.json`. Sin ella un porcentaje no
significa nada: la rúbrica está versionada y cambia, de modo que un 82 % medido contra `Eval-Spec` de
ayer y un 82 % medido contra el de hoy no son el mismo número.

```yaml
corrida:     2026-08-13-agentes-estandar
fecha:       2026-08-13
rama:        eval/agentes-estandar
modelo:      claude-opus-5
evaluado:    Requirements/ReqFunc.MD @ <sha>
rúbrica:     Spec/Eval-Spec.MD @ <sha>
personas:    Personas/ @ <sha>
agentes:     Agents/ @ <sha>
```

`instrumento_modificado` merece un renglón propio. Si la comprobación de conformidad corrigió un
agente de persona, el instrumento de medición cambió y **esa corrida no es comparable con las
anteriores**. El campo lo deja dicho en lugar de dejarlo deducir.

## corrida.json

Lo consume `scripts/verificar-puntaje.sh`, que recomputa los puntajes y revalida el veredicto. Los
nombres de campo son los de la rúbrica, para que el control se lea junto a `Eval-Spec.MD` sin traducir
nada.

| Campo | Tipo | Qué contiene |
|---|---|---|
| `corrida` | texto | identificador del directorio |
| `fecha` | texto | `AAAA-MM-DD` |
| `rama` | texto | rama de trabajo |
| `modelo` | texto | modelo que ejecutó la corrida |
| `commits` | objeto | `requerimientos`, `rubrica`, `personas`, `agentes` |
| `instrumento_modificado` | booleano | la comprobación de conformidad tocó algún agente |
| `glosario` | booleano | el repositorio tiene glosario — mientras sea `false`, D5 ≤ 80 |
| `iteraciones` | lista | **exactamente una entrada**: la medición de esta corrida |
| `resultado` | objeto | cierre: debe coincidir con esa entrada |

`iteraciones` conserva forma de lista para que la cardinalidad sea comprobable: C1 falla si trae más
de una entrada, y así «una corrida mide una vez» deja de ser una regla que alguien deba recordar.

La entrada de `iteraciones`:

| Campo | Tipo | Qué contiene |
|---|---|---|
| `n` | entero | siempre `1` |
| `personas` | objeto | `rodrigo`, `milagros`, `carmen`, `anibal` |
| `dimensiones` | objeto | `D1` a `D6`, cada una de 0 a 100 |
| `d2_problemas` | objeto | `P1`, `P2`, `P3`, cada uno 0, 50 o 100 |
| `d3_rf` | objeto | `conformes` y `total` |
| `tensiones_sin_decidir` | entero | de las cinco de `Personas/README.md` |
| `prioridad_uniforme` | booleano | todos los RF comparten prioridad |
| `controles_pasan` | booleano | `verificar.sh` salió con código 0 |
| `global` | número | puntaje global declarado |
| `veredicto` | texto | `PASSED` o `FAILED` |

Cada persona dentro de `personas`:

| Campo | Tipo | Qué contiene |
|---|---|---|
| `tareas` | número | Σ de sus seis tareas críticas, de 0 a 30 |
| `estorba_fuera` | entero | `X_p`: RF marcados **Estorba** que no trazan a sus tareas |
| `flujo` | número | 0, 2 o 4 |
| `puntaje` | número | el declarado, de 0 a 10 — el control lo recomputa |
| `percibida` | número | cobertura percibida autoinformada, de 0 a 100 |
| `tareas_en_cero` | entero | cuántas de sus seis tareas quedaron en 0 |

`puntaje` se declara y además se recomputa. Que un número derivable se escriba a mano es
deliberado: si el declarado y el recomputado difieren, el control lo dice, y esa diferencia es
exactamente el error que se busca atrapar.

### Esqueleto

Los `null` no son opcionales por omisión: marcan que este archivo es una plantilla y no una corrida.
`verificar-puntaje.sh` ignora todo archivo cuyo nombre empiece por `_`.

```json
{
  "corrida": "<AAAA-MM-DD>-<etiqueta>",
  "fecha": "<AAAA-MM-DD>",
  "rama": "<rama de trabajo>",
  "modelo": "<modelo>",
  "commits": {
    "requerimientos": "<sha>",
    "rubrica": "<sha>",
    "personas": "<sha>",
    "agentes": "<sha>"
  },
  "instrumento_modificado": null,
  "glosario": null,
  "iteraciones": [
    {
      "n": 1,
      "personas": {
        "rodrigo":  { "tareas": null, "estorba_fuera": null, "flujo": null, "puntaje": null, "percibida": null, "tareas_en_cero": null },
        "milagros": { "tareas": null, "estorba_fuera": null, "flujo": null, "puntaje": null, "percibida": null, "tareas_en_cero": null },
        "carmen":   { "tareas": null, "estorba_fuera": null, "flujo": null, "puntaje": null, "percibida": null, "tareas_en_cero": null },
        "anibal":   { "tareas": null, "estorba_fuera": null, "flujo": null, "puntaje": null, "percibida": null, "tareas_en_cero": null }
      },
      "dimensiones": { "D1": null, "D2": null, "D3": null, "D4": null, "D5": null, "D6": null },
      "d2_problemas": { "P1": null, "P2": null, "P3": null },
      "d3_rf": { "conformes": null, "total": null },
      "tensiones_sin_decidir": null,
      "prioridad_uniforme": null,
      "controles_pasan": null,
      "global": null,
      "veredicto": "<PASSED|FAILED>"
    }
  ],
  "resultado": {
    "global": null,
    "veredicto": "<PASSED|FAILED>",
    "promedio_personas": null,
    "brechas_abiertas": null
  }
}
```

## Qué verifica el control C1

`scripts/verificar-puntaje.sh` no juzga la evaluación: comprueba que los números declarados sean
consistentes entre sí y con las reglas duras de `Spec/Eval-Spec.MD`. Catorce comprobaciones:

1. Rangos: dimensiones de 0 a 100, puntajes de persona de 0 a 10, `flujo` en {0, 2, 4}, problemas de
   D2 en {0, 50, 100}.
2. `Puntaje_p = máx(0, tareas − 2 × estorba_fuera) / 5 + flujo`.
3. `D1 = promedio de los cuatro puntajes × 10`.
4. `D2 = (P1 + P2 + P3) / 3`.
5. `D3 = conformes / total × 100`.
6. `Global = D1×0,30 + D2×0,25 + D3×0,20 + D4×0,10 + D5×0,10 + D6×0,05`.
7. D5 ≤ 80 mientras `glosario` sea `false`.
8. D5 ≤ 40 si las cuatro percibidas alcanzan 90 y alguna tensión queda sin decidir.
9. D2 ≤ 60 si algún problema crítico queda sin resolver.
10. D1 ≤ 50 si alguna persona tiene sus seis tareas en 0.
11. D6 ≤ 60 si todos los RF comparten prioridad.
12. El veredicto declarado coincide con el que producen las cinco condiciones de `Eval-Spec`, y el
    cierre coincide con la medición.
13. El porcentaje que `README.md` publica coincide con el de la última corrida, y ninguna corrida
    dejó `Eval-Report.MD` sin su `corrida.json` —omitirlo bastaría para esquivar el control—.
14. `iteraciones` trae exactamente una entrada: la corrida midió una vez y no iteró.

Hasta aquí, esas reglas las aplicaba el mismo agente que quería aprobar. El control las vuelve
mecánicas.

## Qué no verifica

Que `tareas` valga 22 y no 18 lo decide la evidencia de `diagnostico.MD`, y ningún script la lee. C1
atrapa la aritmética y las reglas duras; no atrapa un insumo mal juzgado. Un C1 en verde dice que las
cuentas cierran, no que la evaluación sea correcta.

Tampoco vigila todo el protocolo. Comprueba que la corrida no haya iterado, pero no puede ver si las
cuatro evaluaciones se produjeron realmente aisladas ni cuántas corridas vale la pena ejecutar: eso lo
decide `Spec/Eval-Spec.MD`, y ningún script lo cuenta.
