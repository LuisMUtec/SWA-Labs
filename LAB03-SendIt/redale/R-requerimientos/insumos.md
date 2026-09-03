# R — Insumos del backlog

> ### ⚠ Los identificadores de este archivo son los de la ronda 01 y **no** son los del backlog
>
> Este documento se escribió antes de la primera corrida del EVAL y **nunca se renumeró**. Su
> `RF-11`, su `RF-15` y su `RF-17` no son los del [backlog](backlog.md): allá esos números dicen
> otra cosa, y dos de ellos están retirados. Leerlo como si compartiera numeración produce
> exactamente la **deriva semántica** que la tabla de identificadores retirados del backlog declara
> como la lección de la iteración 05.
>
> **Qué conserva su valor:** el razonamiento —de dónde sale cada necesidad, qué se descartó y por
> qué—, que es para lo que el backlog lo cita. **Qué no:** ningún identificador `RF-nn` ni `RNF-nn`
> de este archivo resuelve contra el backlog vigente. La tabla `BR` → `RF` del final está en la
> misma condición. La correspondencia autorizada es la del propio backlog y la de la trazabilidad
> de [`L`](../L-listar-componentes/README.md).
>
> Los `[CLARIFY]` que aparezcan más abajo están **cerrados en el backlog** como supuestos declarados.
>
> Lo encontró el agregador en la **ronda 16**, dieciséis rondas después de escribirse; el aviso más
> viejo que decía la mitad de esto se retiró en la **18**, porque dejar los dos era la corrección
> entrando sin barrer lo que ya lo decía — el defecto de esta serie, dentro de la corrección del
> hallazgo más viejo de la serie.


**Esto no es el entregable.** El artefacto que el enunciado puntúa es el
[backlog](backlog.md), que se escribe a partir de estos insumos.

Lo que hay acá es el razonamiento previo — el que un backlog de solo títulos no puede cargar.
La restricción del enunciado dice dos cosas, y la segunda vale cualquiera sea el formato:

> *"Los requerimientos deben ser mostrados en formato backlog. **No necesitan describirlos,
> sino colocar un título claro y entendible.**"*

Estos veinticuatro enunciados **sí** los describen, así que no pueden ser el entregable. Su
valor es otro: son de donde salieron las dieciséis reglas de
[`business-rules.md`](../../business-rules.md), y son el banco del que se sacarán los títulos
del backlog cuando el profesor lo habilite —convertirlos al formato de
[D-06](../../docs/DECISIONES.md#d-06--el-backlog-adopta-el-formato-literal-del-profesor),
`el sistema [verbo en futuro] [capacidad] - <Persona>`, es mecánico—.

**No los puntúa el [EVAL](../../evals/README.md).** El EVAL puntúa el backlog.

## Encuadre

Las tres preguntas con las que el material abre el paso `R`.

| Pregunta | Respuesta |
|---|---|
| **¿Cuál es el problema?** | Una persona necesita entregar dinero en un país y que otra lo reciba en otro, sin que ninguna de las dos tenga cuenta bancaria. Entre la entrega y el cobro el dinero no está con ninguna: está con SendIt, que lo debe (BR-01). Ese intervalo es todo el problema. |
| **¿Para quién lo resolvemos?** | Para los tres de abajo. El usuario modelo es **la emisora**: es quien paga, quien elige el servicio y de quien el dinero sigue siendo hasta que alguien lo cobra. Los otros dos existen porque sin ellos su operación no cierra. |
| **¿Cuáles son las limitaciones?** | Las dos que el enunciado marca como críticas: **seguridad**, porque el efectivo se entrega a un desconocido en una ventanilla ajena, y **consistencia de datos**, porque un giro pagado dos veces es dinero perdido, no un registro sucio. A eso se suma que el negocio es transfronterizo y por lo tanto multirregulador. |

## Usuario modelo

`[ASSUMPTION: SendIt opera el modelo Western Union —red de agentes físicos, efectivo contra
efectivo, sin cuenta bancaria obligatoria en ninguna punta—, según indicación del profesor.]`

| Persona | Rol en la remesa | Archivo |
|---|---|---|
| **Rosa Quispe** | Emisora — entrega el efectivo y designa a quién llega. **Usuario modelo.** | [`Rosa.MD`](../../personas/Rosa.MD) |
| **Elena Quispe** | Receptora — cobra en el país destino. No es clienta de SendIt. | [`Elena.MD`](../../personas/Elena.MD) |
| **Kevin Ramos** | Operario — atiende la ventanilla del agente. Encarna la seguridad. | [`Operario.MD`](../../personas/Operario.MD) |

Las reglas que estos requerimientos ejercen están en
[`business-rules.md`](../../business-rules.md). Cada `RF` enuncia el efecto de su regla y la
cita; ninguna cita es portante.

---

## Requerimientos funcionales

### Creación del giro

- **RF-01** — El sistema no crea un giro mientras el emisor no esté identificado contra un
  documento oficial vigente, y no registra la recepción del efectivo antes de esa
  identificación. · *Rosa, Kevin · BR-03*
- **RF-02** — El sistema exige un único receptor designado y un único país destino por giro, y
  rechaza la creación si falta cualquiera de los dos. · *Rosa · BR-02*
- **RF-03** — El sistema informa al emisor el monto exacto que el receptor cobrará en la
  moneda destino **antes** de que el emisor entregue el efectivo. · *Rosa · BR-07*
- **RF-04** — El sistema conserva ese monto sin recalcularlo durante toda la vida del giro,
  cualquiera sea el tiempo transcurrido hasta el cobro. · *Rosa, Elena · BR-07*
- **RF-05** — El sistema rechaza la creación de un giro que haga al emisor superar su límite
  por operación o su acumulado en la ventana vigente, contados sobre su identidad y no sobre
  el punto de atención. · *Rosa, Kevin · BR-04*
- **RF-06** — El sistema emite un código de seguimiento por giro y lo entrega únicamente al
  emisor; no lo transmite al receptor por ningún canal propio. · *Rosa · BR-08*
- **RF-07** — El sistema exige la autorización de un segundo rol antes de dar por creado un
  giro que supere el umbral reforzado, y hasta obtenerla no habilita la recepción del
  efectivo. · *Kevin · BR-05*

### Cumplimiento

- **RF-08** — El sistema contrasta a emisor y receptor contra las listas de sanciones vigentes
  antes de aceptar el efectivo y antes de autorizar el pago. · *Kevin · BR-06*
- **RF-09** — Ante una coincidencia de sanciones el sistema deja el giro retenido —ni pagable
  ni cancelado— y lo deriva a un rol distinto del operario que lo atendió. · *Kevin · BR-06*

### Pago

- **RF-10** — El sistema autoriza el pago solo cuando quien se presenta exhibe el código del
  giro **y** un documento cuya identidad coincide con la del receptor designado; rechaza si
  falta cualquiera de los dos. · *Elena, Kevin · BR-09*
- **RF-11** — El sistema rechaza todo intento de pago sobre un giro ya pagado, en cualquier
  punto de atención y país de la red. · *Elena, Kevin · BR-10*
- **RF-12** — El sistema no habilita el pago de un giro cuyos fondos de origen no estén
  confirmados. · *Kevin · BR-11*
- **RF-13** — Cuando rechaza un pago, el sistema entrega al operario el motivo del rechazo y
  la acción que corresponde ofrecer a quien está en la ventanilla, sin exponer datos del giro
  que el rechazo no requiere. · *Elena, Kevin · BR-16*
- **RF-14** — El sistema entrega al receptor el monto en moneda destino fijado al crearse el
  giro, sin diferencia. · *Elena · BR-07*

### Interrupción y consistencia

- **RF-15** — Ante una interrupción durante una operación, el sistema deja el giro en un
  estado único y legible —creado o no creado, pagado o no pagado— y nunca en un estado
  intermedio que el operario deba interpretar. · *Kevin · BR-10, BR-11*
- **RF-16** — El sistema trata todo reintento de una creación o de un pago interrumpidos como
  la misma operación, de modo que reintentar no produzca un segundo giro ni un segundo
  pago. · *Kevin · BR-10*

### Cancelación y prescripción

- **RF-17** — El sistema permite al emisor cancelar su giro mientras no esté pagado, y le
  devuelve el monto entregado. · *Rosa · BR-12*
- **RF-18** — El sistema rechaza toda cancelación pedida por el receptor, y toda cancelación
  sobre un giro ya pagado. · *Rosa, Elena · BR-12*
- **RF-19** — Cumplido el plazo de prescripción sin que el giro se cobre, el sistema lo deja
  no pagable y pone su monto a disposición del emisor. · *Rosa · BR-14*

### Consulta

- **RF-20** — El sistema permite al emisor consultar el estado de sus propios giros
  —pendiente, retenido, pagado, cancelado o prescrito— sin depender del receptor. ·
  *Rosa · BR-01*

### Registro y privilegio

- **RF-21** — El sistema asocia cada acto sobre un giro —creación, autorización, pago,
  cancelación, corrección— a la identidad de quien lo ejecutó. · *Kevin · BR-15*
- **RF-22** — El sistema no permite modificar ni eliminar el registro de un acto ya
  ejecutado. · *Kevin · BR-15*
- **RF-23** — El sistema registra la corrección de un giro pagado como un movimiento nuevo y
  conserva intacto el registro del giro original. · *Kevin · BR-13*
- **RF-24** — El sistema limita lo que el operario ve a los datos de la operación que está
  atendiendo: no le expone el historial del emisor ni del receptor, ni el código completo de
  giros que no está pagando. · *Kevin · BR-16*

---

## Requerimientos no funcionales

El enunciado nombra dos como críticos —**seguridad** y **consistencia de datos**— y no da
ninguna cifra. Los umbrales de abajo son nuestros y van marcados; son además las entradas que
el paso [`E`](../E-estimar/README.md) va a consumir.

- **RNF-01 — Consistencia del dinero.** Ningún giro queda pagado dos veces ni con dos montos
  distintos, aun ante caída de un punto de atención o pérdida de conexión durante la
  operación. **Medida:** cero doble pagos y cero giros huérfanos en la conciliación
  diaria. · *BR-10, BR-11*
- **RNF-02 — Confidencialidad.** Los datos de identidad y el código de giro viajan y se
  conservan cifrados, y no son legibles por quien administra la infraestructura. · *BR-08,
  BR-16*
- **RNF-03 — No repudio.** El registro de actos es inalterable y conservado por el plazo que
  exija el regulador de cada país de origen. `[CLARIFY: el plazo lo fija cada regulador; sin
  él no se puede dimensionar el almacenamiento en el paso E.]` · *BR-15*
- **RNF-04 — Tiempo de atención en ventanilla.** Una operación de envío o de cobro se
  completa en menos de `[ASSUMPTION: 3 minutos]` desde que el operario empieza a registrarla,
  sin contar el tiempo de verificación del documento. · *Kevin*
- **RNF-05 — Disponibilidad para cobro.** Un giro fondeado queda disponible para cobro en el
  país destino en menos de `[ASSUMPTION: 15 minutos]` desde su creación. · *Rosa, Elena*
- **RNF-06 — Disponibilidad de la red.** `[ASSUMPTION: 99.9 % mensual]`, medida sobre la
  capacidad de crear y de pagar giros, no sobre la consulta. · *Kevin*
- **RNF-07 — Recuperación.** Ante caída de un punto de atención, el estado de los giros que
  estaba atendiendo se recupera en menos de `[ASSUMPTION: 5 minutos]` y sin intervención del
  operario. · *Kevin · BR-10*
- **RNF-08 — Alcance multipaís y multimoneda.** El sistema opera con más de un país de origen
  y más de una moneda destino desde el primer día. `[CLARIFY: cuántos corredores país-a-país
  al lanzamiento, y cuáles. Determina la estimación de carga del paso E.]` · *BR-02*

---

## Supuestos y ambigüedades

El enunciado deja casi todo el dominio abierto. Lo indefinido se marca, nunca se rellena en
silencio.

| Marca | Dónde | Qué depende de resolverla |
|---|---|---|
| `[ASSUMPTION]` modelo Western Union | Usuario modelo · `business-rules.md` | Todo. Sin red de agentes no existe el operario y la mitad del catálogo pierde sentido |
| `[ASSUMPTION]` umbral de límites (BR-04) y umbral reforzado (BR-05) | RF-05, RF-07 | El punto exacto en que la operación exige dos personas |
| `[CLARIFY]` plazo de prescripción (BR-14) | RF-19 | Cuándo cierra el pasivo y vuelve el dinero al emisor |
| `[CLARIFY]` plazo de conservación del registro | RNF-03 | El dimensionamiento de almacenamiento del paso `E` |
| `[CLARIFY]` corredores país-a-país al lanzamiento | RNF-08 | La estimación de carga entera del paso `E` |
| `[ASSUMPTION]` umbrales de RNF-04 a RNF-07 | RNF | Las tres cuentas del paso `E`: servidores, almacenamiento y ancho de banda |

## Trazabilidad

Las dieciséis reglas de [`business-rules.md`](../../business-rules.md) están citadas por al
menos un `RF`. Ningún `RF` existe sin una persona que lo pida y una regla que lo gobierne.

| Regla | La ejercen |
|---|---|
| BR-01 | RF-20 |
| BR-02 | RF-02, RNF-08 |
| BR-03 | RF-01 |
| BR-04 | RF-05 |
| BR-05 | RF-07 |
| BR-06 | RF-08, RF-09 |
| BR-07 | RF-03, RF-04, RF-14 |
| BR-08 | RF-06, RNF-02 |
| BR-09 | RF-10 |
| BR-10 | RF-11, RF-15, RF-16, RNF-01, RNF-07 |
| BR-11 | RF-12, RF-15, RNF-01 |
| BR-12 | RF-17, RF-18 |
| BR-13 | RF-23 |
| BR-14 | RF-19 |
| BR-15 | RF-21, RF-22, RNF-03 |
| BR-16 | RF-13, RF-24, RNF-02 |
