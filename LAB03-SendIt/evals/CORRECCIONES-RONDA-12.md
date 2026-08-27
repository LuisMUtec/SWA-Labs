# Correcciones pendientes — ronda 12

**Estado: no aplicadas.** El trabajo se detuvo al cerrar la [iteración 11](iterations/2026-08-27-11.md)
con **6,61 / 10**, por instrucción explícita. Este archivo existe para que la ronda 12 empiece donde
la 11 terminó y no haya que volver a derivar nada.

El backlog vigente es `redale/R-requerimientos/backlog.md` con **138 RF + 17 RNF = 155 ítems**,
congelado en `b33944b`; la propagación aguas abajo, en `97c7f6b`.

## Aritmética del gate

| Escenario | D1 | D2 | D3 | D4 | Total |
|---|---|---|---|---|---|
| Hoy (ronda 11) | 1,5 | 3,0 | 1,5 | 0,61 | **6,61** |
| Con los bloques 1–3 | 3,0 | 3,0 | 2,0 | ≈1,0 | **≈ 9,0** |
| Con los ocho bloques | 3,0 | 3,0 | 2,0 | ≈1,7 | **≈ 9,7** |

**Los bloques 1 y 2 son dieciséis ediciones de título y mueven 1,5 puntos de D1 y 0,5 de D3.**

---

## Bloque 1 — la entrada del secreto · +0,5 D3 y −1,0 de las deducciones de D1

El hallazgo central de la ronda 11, y el que dos personas encontraron por separado.

`RF-34` exige el código para autorizar el pago. `RF-113` y `RNF-15` prohíben a quien atiende el
mostrador leerlo o transcribirlo. **No existe para el código el equivalente de `RF-114`**, que sí dice,
para el desafío, que la respuesta *«la pone el propio receptor, sin que quien atiende pueda leerla ni
digitarla»*.

- **Escribir el título que falta:** quién introduce el código en el pago y por dónde, sin que quien
  atiende pueda leerlo ni digitarlo.
- **Corregir `L:548`**, que hoy describe el `Terminal del Cliente` como *«donde el emisor lee su
  código»* — contradice a `RF-11`.
- **Corregir `D:813`**, que afirma que el secreto *«entra y sale por un dispositivo orientado al
  cliente»* citando `RF-114`, que solo cubre el desafío.

> **La lección de esta ronda, escrita para no repetirla:** la ronda 10 reparó el hueco del mostrador
> por el lado de la **salida** porque ahí se vio el síntoma. La decisión que lo gobierna es *por dónde
> se mueve el secreto en un mostrador donde el operario no puede tocarlo*, y tiene **dos extremos**.
> Reparar un extremo y no el par es la clase «reparación en la altitud equivocada» aplicada a la
> corrección anterior — cuarta ronda consecutiva con esta clase.

## Bloque 2 — el canal de los cuatro huérfanos · la edición más barata del informe

La misma edición cuatro veces: agregar **«por llamada o mensaje de texto»**.

| ID | Por qué importa |
|---|---|
| `RF-91` | Rosa ya salió del mostrador cuando el punto deja de poder pagar |
| `RF-116` | **Es el aviso sobre el que corre el plazo de 24 h** que, vencido, le devuelve el giro por `RF-111`. Rosa: *«no es un plazo, es un sorteo»* |
| `RF-128` | Elena: *«el único comodín de canal que me queda, y está justo en el ítem que se llama sin depender del emisor»* |
| `RF-109` | Hoy su canal solo existe si se lee `RF-75` — referencia portante |

## Bloque 3 — las tres inversiones de prioridad

| Cambio | Por qué |
|---|---|
| `RF-135` → **P0** | Hoy P1 bajo `RF-110`/`RF-117` en P0: puede existir el rehacer sin la exención de comisión, y Rosa paga dos veces por el mismo envío |
| `RF-145` → **P0** | La objeción del agente es P1 y el descuento sobre su caja (`RF-143`) es P0. **Es la misma inversión que la ronda 10 cobró en `RF-104`, reaparecida un eslabón más abajo** |
| `RF-142` → **P0** | El margen informado por debajo de la comisión informada, en la misma pantalla |

Y **un título que resuelva la objeción de `RF-145` con plazo**: hoy se admite y nada la termina, y
`D:244` dice *«mientras la objeción vive, el descuento no entra en ninguna corrida»* — bloquea
`RF-143` indefinidamente.

## Bloque 4 — la cadena del dinero repuesto

- **Qué es «comprobada» en `RF-59`, y quién comprueba.** La ronda 11 cambió «informar no es autorizar»
  por «comprobar sin decir quién comprueba».
- **Ruta de cobro de la reposición al receptor.** Hoy `RF-59` la asienta y nada la paga: `RF-71`/`RF-72`
  son devoluciones al emisor, `RF-121` informa la diferencia y no que hay dinero esperando.
- **Un título que ordene la devolución que `RF-108` anuncia.** `RF-108` avisa que el giro «será
  devuelto» y ningún título la ordena.

## Bloque 5 — los productores que faltan

- **Quién fija la comisión**, con la forma de `RF-07`. Hoy tiene **cuatro lectores y ningún productor**:
  `RF-136` la informa, `RF-47` la incluye, `RF-74` la devuelve, `RF-135` no la recobra.
- **Quién fija el margen cambiario.** `RF-142` le dio lector, no productor.
- **El umbral del acumulado del receptor** de `RF-93` — abierto desde la ronda 10.

## Bloque 6 — forma: cinco duplicados y tres no atómicos

- **Retirar** `RF-112` (⊂ `RF-113` ⊂ `RNF-15`), `RF-12` (⊂ `RF-114`), `RF-110` (⊂ `RF-46` desde que T6
  alineó el borde), `RF-108` (⊂ `RF-106`). Sin reusar los números.
- **Quitar el solape** de `RF-47` con `RF-74`.
- **Partir** `RNF-02` (dos prohibiciones), `RF-39` (tres estados), `RF-80`/`RF-140` (emisor **y**
  receptor).
- **Extender `RNF-17` al mostrador**, como se hizo con su gemelo `RNF-15`.
- **Quitar los demostrativos** de `RF-06` («ese monto») y `RF-10` («esos límites»).

## Bloque 7 — los catorce comportamientos inventados aguas abajo

El bloque más grande de D4. Para cada uno: **o se escribe el título, o se saca la decisión.** Por
prioridad: el **recibo firmado digitalizado** y el **comprobante de domicilio** de `E-estimar` (el
segundo es dato personal bajo `RNF-01` y `RF-81`), la declaración de diferencia **por mostrador** en
`L:408`/`L:544` contra `RF-90`, el *«deja de crear giros»* de `D:634`, y el **diferimiento de avisos**
de `E-escalar:185`.

## Bloque 8 — cuatro ramas sin salida

- **El emisor que responde que no** a la oferta de otro punto: `RF-111` no aplica, `RF-105` impide
  cambiar, `RF-129` solo cubre que no quede ninguno. El giro queda en un punto que no puede pagar.
- **La devolución que nace vencida:** `RF-50` la crea al prescribir el giro y `RF-89` la mantiene
  disponible «hasta el plazo de prescripción del giro».
- **La custodia sin emisor identificado:** `RF-138` devuelve «al emisor» y `RF-01` lo identifica «antes
  de crear un giro» — hay una ventana sin emisor a quien devolver.
- **La baja del acumulado por identidad de receptor** — el único dato del sistema que nace y nada cierra.

---

## Además, y no es del backlog

- **`docs/ENTREGA.md` está desactualizado**: dice 118 ítems en doce lugares, 32 endpoints, 30
  entidades, trazabilidad 118/118, y su serie del EVAL llega a la iteración 07. Hoy son **155 ítems,
  40 rutas para 47 capacidades, 34 entidades, 155/155 y once corridas**. Hay que refrescarlo y
  regenerar el PDF con `scripts/entrega-a-pdf.sh`.
- **Contradicción `A`↔`D` que no es clase de la rúbrica pero es el defecto más grave del rebarrido:**
  `A:120` declara **cinco cuentas contables** y `D:358-365` ejecuta **ocho**. Resultado literal: la
  retención de `RF-29` y toda devolución **no se pueden asentar**, y `RNF-07` queda sin forma de
  comprobarse.
- **La fracción específica de remesa cayó de 72,3 % a 61,3 %** porque 11 de los 18 ítems nuevos
  sobreviven a una transferencia doméstica. No cuesta puntos hoy. **Si el patrón se repite dos rondas
  más, D2 baja sin que nadie haya empeorado un ítem.**
