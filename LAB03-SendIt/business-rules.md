# Reglas de negocio — SendIt

El cuerpo de reglas que obedece el negocio de remesas. Las reglas no son proceso ni son
requerimientos: valen en todos los flujos y sobreviven a cualquier lista de requerimientos.
Cuando los requerimientos del paso `R` queden satisfechos y desaparezcan, estas reglas recién
estarán empezando.

**Este documento enuncia** qué permite, prohíbe y exige el negocio.
**No enuncia** qué hace el sistema —eso es
[`redale/R-requerimientos/backlog.md`](redale/R-requerimientos/backlog.md)— ni
quiénes son los usuarios —eso es [`personas/`](personas/).

## Convenciones

- **Una regla por entrada.** Una sola cosa, verdadera o falsa, modificable por su cuenta.
- **Los identificadores son estables.** `BR-nn` se asigna una vez y no se renumera ni se
  reutiliza, aunque la regla se reescriba. Los huecos en la numeración son normales.
- **Lenguaje de negocio, sin mecanismo.** Una regla dice qué hace el negocio, nunca cómo lo
  implementa un sistema.
- **Toda regla declara su fuente.** O viene del enunciado, o es nuestra — y si es nuestra
  lleva `[ASSUMPTION: …]`. El enunciado solo fija dos cosas (seguridad y consistencia de
  datos), así que casi todas las reglas de acá son nuestras. Una regla inventada y sin marcar
  es un defecto.
- **Citadas, no copiadas.** Los requerimientos enuncian el efecto de la regla y citan el
  identificador —*"el sistema rechaza un segundo cobro del mismo giro (BR-10)"*— para que
  ninguna referencia sea portante.

Ordenadas por identificador.

---

## El modelo: red de agentes con efectivo

`[ASSUMPTION: SendIt opera el modelo Western Union —red de agentes físicos, efectivo contra
efectivo, sin cuenta bancaria obligatoria de ninguna de las dos puntas— y no un monedero
digital ni una transferencia banco a banco. Esta decisión antecede a todo el catálogo: fija
que el operario de ventanilla exista, que el receptor no tenga relación previa con SendIt, y
que la identificación ocurra en persona y no por medios remotos.]`

---

## Catálogo

### BR-01 — SendIt nunca es dueño del dinero, solo lo debe

El dinero que el emisor entrega no es ingreso de SendIt: es una obligación de pago frente al
receptor designado, hasta que se paga, se devuelve o prescribe.

- **Por qué:** es lo que separa una remesa de una venta. Todo el resto del catálogo —la
  irrevocabilidad, el reverso, la prescripción— se sigue de que el dinero es de alguien más.
- **Fuente:** enunciado — "estamos hablando de dinero".
- **Afecta:** contabilidad, cancelación, prescripción, quiebra.

### BR-02 — Un giro tiene exactamente un emisor, un receptor designado y un país destino

El emisor designa a una única persona y un único país al momento de entregar el efectivo. No
existen giros a múltiples receptores ni a un receptor indeterminado.

- **Por qué:** el tamizado de sanciones (BR-06) y la identificación del receptor (BR-09) no
  tienen contra qué correr si el destinatario no está determinado desde el origen.
- **Fuente:** enunciado — "mandar remesas a personas en diferentes países".
- **Afecta:** creación del giro, cumplimiento, pago.

### BR-03 — El emisor se identifica antes de que SendIt acepte el efectivo

Ningún giro se crea con un emisor no identificado. La identificación ocurre antes de recibir
el dinero, no después.

- **Por qué:** después de aceptar el efectivo, rechazar al emisor obliga a devolverlo, y la
  devolución es justamente el movimiento que el lavado de activos busca provocar.
- **Fuente:** enunciado — "el tema de seguridad es muy importante" ·
  `[ASSUMPTION: la identificación es presencial contra documento oficial vigente.]`
- **Afecta:** creación del giro, cumplimiento, seguridad.

### BR-04 — Todo giro tiene un límite por operación, un acumulado por emisor y un acumulado por receptor

Un emisor no puede superar un monto por giro ni un monto acumulado en una ventana de tiempo,
contados sobre su identidad y no sobre el punto de atención.

- **Por qué:** el límite por operación sin acumulado se evade partiendo el monto en giros
  chicos —*structuring*—, que es la forma más común de fraccionamiento en remesas.
- **Fuente:** `[ASSUMPTION: los umbrales concretos los fija el regulador de cada país de
  origen; el negocio exige que existan, no fija su valor.]`
- **Afecta:** creación del giro, cumplimiento, seguridad.

### BR-05 — Por encima de cierto monto, un giro exige una segunda autorización

Ningún operario puede completar por sí solo un giro que supere el umbral reforzado: hace
falta la autorización de un segundo rol.

- **Por qué:** el operario de ventanilla es el vector de fraude más barato de la red — está
  solo, en efectivo, y con acceso a crear y a pagar. Partir la operación entre dos personas
  es el control que no depende de confiar en ninguna.
- **Fuente:** `[ASSUMPTION: nuestra, derivada del hint del enunciado sobre "diseñar
  correctamente el/los mecanismo(s) de seguridad".]`
- **Afecta:** creación del giro, pago, seguridad.

### BR-06 — Emisor y receptor se tamizan contra listas de sanciones antes de mover dinero

Las dos puntas se contrastan contra las listas de personas y entidades sancionadas antes de
aceptar el efectivo y antes de pagarlo. Una coincidencia detiene el giro; no lo cancela.

- **Por qué:** una coincidencia con lista de sanciones no es un error del cliente ni una
  decisión del operario: es una retención que debe resolver un tercero. Cancelar
  automáticamente devolvería fondos que quizá no deben devolverse.
- **Fuente:** `[ASSUMPTION: nuestra; ninguna operación de remesas transfronteriza opera sin
  esto, pero el enunciado no lo menciona.]`
- **Afecta:** creación del giro, pago, cumplimiento.

### BR-07 — El tipo de cambio se fija al crear el giro y no se recalcula

El monto que el receptor cobrará en la moneda destino queda determinado en el momento en que
el emisor entrega el efectivo, y no cambia después, cualquiera sea el tiempo hasta el cobro.

- **Por qué:** consistencia de datos en el sentido que exige el enunciado. Si el monto se
  recalcula al cobrar, ni el emisor ni el receptor pueden saber cuánto se está mandando, y la
  diferencia la absorbe siempre la punta más débil.
- **Fuente:** enunciado — "la consistencia de datos ya que estamos hablando de dinero".
- **Afecta:** creación del giro, pago, contabilidad.

### BR-08 — El giro se identifica por un código que solo el emisor puede transmitir

Cada giro recibe un código de seguimiento. SendIt lo entrega al emisor, y es el emisor quien
decide comunicárselo al receptor. SendIt no se lo entrega al receptor por su cuenta.

- **Por qué:** es lo que convierte al emisor en el titular de la operación. Si SendIt pudiera
  darle el código al receptor, el emisor perdería el control de un dinero que todavía es suyo
  (BR-01) y la cancelación (BR-12) sería inejecutable.
- **Fuente:** `[ASSUMPTION: nuestra, modelo Western Union.]`
- **Afecta:** creación del giro, pago, cancelación, seguridad.

### BR-09 — El receptor cobra contra código **y** documento. Cuando el documento no está vigente, el tercer factor es el desafío que el emisor registró al crear el giro: el receptor cobra contra código, documento y respuesta

El pago exige que quien se presenta exhiba el código del giro y un documento de identidad
que coincida con el receptor designado por el emisor. Ninguna de las dos cosas basta sola.

- **Por qué:** el código viaja por canales que SendIt no controla —mensajes, llamadas— y se
  intercepta. El documento sin código permitiría cobrar cualquier giro dirigido a esa
  persona. El fraude necesita las dos, y obtenerlas cuesta.
- **Fuente:** enunciado — seguridad · `[ASSUMPTION: el modelo de dos factores es nuestro.]`
- **Afecta:** pago, seguridad.

### BR-10 — Un giro se paga una sola vez

Una vez pagado, un giro no puede volver a pagarse, en ninguna ventanilla, en ningún país,
por ningún medio.

- **Por qué:** es la regla de consistencia central del negocio. Un doble pago no es un dato
  inconsistente: es dinero que SendIt perdió y no puede recuperar.
- **Fuente:** enunciado — "la consistencia de datos ya que estamos hablando de dinero".
- **Afecta:** pago, conciliación.

### BR-11 — Ningún giro se paga sin que los fondos estén confirmados en el origen

El receptor no cobra hasta que SendIt tiene confirmado que el efectivo del emisor ingresó.
La disponibilidad para cobrar no se anticipa a la confirmación.

- **Por qué:** si el pago se adelanta a la confirmación, la red paga giros que nunca se
  fondearon y el agente de origen se vuelve un punto de fuga.
- **Fuente:** enunciado — consistencia de datos.
- **Afecta:** pago, liquidación entre agentes.

### BR-12 — El emisor puede cancelar mientras el dinero no esté a disposición del receptor, y solo él

Hasta que el giro se paga, el emisor puede cancelarlo y recuperar su dinero. Después del
pago, no. El receptor nunca puede cancelar.

- **Por qué:** se sigue de BR-01: el dinero es del emisor hasta que se entrega. Y de BR-10:
  después del pago no hay nada que devolver.
- **Fuente:** `[ASSUMPTION: nuestra. El costo de la operación puede no ser reembolsable; eso
  no lo decide esta regla.]`
- **Afecta:** cancelación, pago.

### BR-13 — Un giro pagado se corrige con un movimiento nuevo, nunca borrando el anterior

Un error sobre un giro ya pagado se resuelve registrando un movimiento compensatorio. El
registro del giro original no se altera ni se elimina.

- **Por qué:** es lo que hace auditable el sistema. Un registro que se puede editar después
  del hecho no prueba nada, y el no repudio (BR-15) se apoya en que no se pueda.
- **Fuente:** `[ASSUMPTION: nuestra, principio contable de partida doble.]`
- **Afecta:** corrección, auditoría, contabilidad.

### BR-14 — Un giro no cobrado prescribe y el dinero vuelve al emisor

Pasado un plazo sin que el receptor cobre, el giro deja de ser pagable y el monto queda a
disposición del emisor.

- **Por qué:** BR-01 dice que el dinero es una obligación. Sin plazo, la obligación es
  perpetua y el pasivo nunca cierra.
- **Fuente:** `[ASSUMPTION: el plazo lo fija el regulador del país de origen; a falta de norma expresa, 12 meses desde la creación del giro]`
- **Afecta:** pago, contabilidad, cancelación.

### BR-15 — Toda operación queda registrada con quién la hizo, y ese registro no se altera

Cada acto sobre un giro —creación, autorización, pago, cancelación, corrección— queda
asociado a la identidad de quien lo ejecutó, y ese registro no se modifica ni se borra.

- **Por qué:** sin no repudio, BR-05 no sirve de nada: la segunda autorización solo es un
  control si después se puede probar quién autorizó qué.
- **Fuente:** enunciado — seguridad · `[ASSUMPTION: la inalterabilidad es nuestra.]`
- **Afecta:** todos los flujos, auditoría, seguridad.

### BR-16 — El operario ve lo que necesita para atender, no el giro completo

Un operario accede a los datos necesarios para la operación que está atendiendo. No accede
al historial del emisor ni del receptor más allá de eso, ni al código completo de giros que
no está pagando.

- **Por qué:** limita el daño de un operario comprometido, que es el escenario que BR-05
  y BR-09 ya asumen posible. Un control de fraude que le da al posible defraudador todos los
  datos no es un control.
- **Fuente:** `[ASSUMPTION: nuestra, mínimo privilegio.]`
- **Afecta:** pago, seguridad, privacidad.

## BR-17 — Un giro transfronterizo obedece a los dos reguladores, y cuando chocan no se elige uno

Un giro cruza dos jurisdicciones y queda sujeto a las dos a la vez: la del país de origen y la del
país de destino. Ninguna desplaza a la otra.

De ahí se sigue lo que hace difícil el caso: **cuando las dos imponen condiciones incompatibles, el
giro no se crea.** Elegir una sería decidir por cuenta propia cuál regulador se incumple.

`[ASSUMPTION: la regla se deduce de que el negocio es transfronterizo y multirregulador, que el
enunciado marca como limitación. Ninguna norma concreta se cita.]`
