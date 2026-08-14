---
name: verificar-requerimientos
description: Ejecuta los controles de forma y estructura sobre los entregables del caso UCI Essalud e interpreta sus hallazgos. Úsalo antes de declarar PASSED una iteración de evaluación, después de editar Requirements/ReqFunc.MD o los agentes de persona, y cuando haya que comprobar que una corrida no tocó archivos de solo lectura. También prepara la rama de trabajo de una corrida.
allowed-tools: Bash, Read, Grep
---

# Verificación de requerimientos

Nueve controles mecánicos sobre los entregables, más la preparación de la rama. Todos viven en
`scripts/` y se ejecutan desde la raíz del repositorio.

```bash
scripts/preparar-git.sh [rama] [base]   # deja la rama de trabajo lista; aborta en vez de forzar
scripts/verificar.sh                    # los nueve controles, con detalle de cada falla
scripts/verificar.sh --sin-agentes      # igual, pero Agents/* deja de ser editable
scripts/guardia-diff.sh                 # solo la comprobación de archivos editables
scripts/verificar-puntaje.sh            # solo la aritmética del puntaje de las corridas
```

`verificar.sh` sale con código 0 cuando los nueve pasan y 1 cuando alguno falla. **Ningún puntaje se
declara `PASSED` con un control en rojo**, por alto que sea el porcentaje.

`--sin-agentes` cambia una sola cosa: retira los cuatro agentes de persona y su índice de la lista de
editables. Se usa **desde la primera iteración en adelante**. Los agentes solo se corrigen durante el
Paso 0; a partir de ahí son el instrumento de medición, y si cambian entre una iteración y la
siguiente ya no se sabe si mejoró el requerimiento o se ablandó el evaluador.

## Qué verifica cada control

Los cuatro primeros buscan texto que no debería existir: aciertan cuando no encuentran nada.

| Control | Falla cuando | Dónde vive la corrección |
|---|---|---|
| **M1** Enunciado sin DEBE | Un RF se enuncia sin el auxiliar DEBE | Reescribir el enunciado con un patrón EARS |
| **M2** Sujeto distinto del sistema | El sujeto del DEBE es una persona | El actor va en el disparador; quien debe es el sistema |
| **M3** Mecanismo o producto nombrado | El RF condiciona sobre la solución en vez de sobre la garantía | Reformular como garantía; la decisión técnica se registra en `docs/` |
| **M4** Lápidas o rastro de historial | El cuerpo conserva lo descartado, tachado o comentado | Borrarlo: su lector es `git log` |
| **E1** Identificadores duplicados | Dos RF comparten ID | Renumerar el nuevo, nunca el existente |
| **E2** Campos obligatorios | Un RF no declara enunciado, prioridad, persona, problema o algún criterio | Completar el campo, no suprimir el RF |
| **E3** Matrices citan IDs inexistentes | Una matriz de cierre referencia un RF que ya no está | Actualizar la matriz junto con el cuerpo |
| **E4** Archivos de solo lectura | La corrida tocó algo fuera de la lista de editables | Revertir el archivo; si la corrección vive ahí, reportarla como bloqueada |
| **C1** Aritmética del puntaje | Un puntaje declarado no sale de su fórmula, un techo duro se supera, el veredicto no es el que dan las cinco condiciones, o el README publica otro porcentaje | Corregir el número en `corrida.json` y en el resumen; nunca la fórmula |

M1 a M4 son los controles de [`docs/CONVENCIONES.md`](../../../docs/CONVENCIONES.md), sección 11.
E4 delega en `guardia-diff.sh` y C1 en `verificar-puntaje.sh`.

C1 lee los `Spec/corridas/*/corrida.json` que existan —sin límite de corridas— y recomputa lo que
declaran: `Puntaje_p`, D1, D2, D3, el global ponderado, los cinco techos duros de la rúbrica y las
cinco condiciones del veredicto. Hasta que existió, esas reglas las aplicaba el mismo agente que
quería aprobar.

Aparece como `OMITE` mientras no haya ningún `corrida.json`. **Omitido no es cumplido**: la condición
5 del veredicto exige los nueve controles, de modo que una corrida sin su JSON no llega a `PASSED`.
Escribir el reporte y no el JSON tampoco sirve de atajo — C1 lo detecta y falla.

## Qué no verifica

Un control en verde no dice que el requerimiento sea bueno: dice que no incurre en el defecto que ese
control sabe detectar. Ninguno de los nueve juzga si el comportamiento enunciado le sirve a una
persona, si P1, P2 y P3 quedan resueltos, si una tensión está decidida o si la prioridad es realista.
Eso lo puntúa [`Spec/Eval-Spec.MD`](../../../Spec/Eval-Spec.MD) y no se sustituye por un grep.

C1 tampoco es una excepción: comprueba que las cuentas cierren, no que los insumos sean correctos.
Que una tarea crítica valga 5 y no 3 lo decide la evidencia del diagnóstico, y ningún script la lee.
Un C1 en verde sobre puntajes mal juzgados sigue siendo verde.

En particular, **M3 acierta por coincidencia de palabra**. Una mención legítima —«push» dentro de una
cita del enunciado, por ejemplo— aparece como hallazgo. Se resuelve reformulando o desplazando la
frase, nunca relajando el patrón del script: el control se ajusta a los documentos, no al revés.

## Interpretación de los hallazgos

Cada falla imprime las líneas culpables con su número, de modo que el hallazgo se corrige donde está.
Recorre los controles en orden y no encadenes correcciones: mover una afirmación de documento suele
romper la coherencia de otro, así que se vuelve a ejecutar el script completo después de cada tanda.

Cuando un control falla y la corrección exige tocar un archivo de solo lectura —una persona, las
convenciones, la definición del evaluador, los requerimientos no funcionales—, **detente y repórtalo
como bloqueado**. Son la vara con la que se mide; una vara que se ajusta para alcanzar el número deja
de medir.

## Preparación de la rama

`preparar-git.sh` comprueba que no haya cambios locales, actualiza la base solo por fast-forward,
confirma que la rama de trabajo no exista ni aquí ni en `origin`, y la crea. Ante cualquier condición
que obligaría a descartar o esconder trabajo, aborta con el motivo y no toca nada: no ejecuta `stash`,
`reset` ni `checkout -f`, y no reescribe historia. Los archivos sin seguimiento se anuncian pero no
bloquean.

El resultado literal de los controles, con su código de salida, se guarda en
`Spec/corridas/‹id›/controles.txt`. [`Spec/corridas/_ESQUEMA.MD`](../../../Spec/corridas/_ESQUEMA.MD)
fija el resto de lo que una corrida deja escrito.
