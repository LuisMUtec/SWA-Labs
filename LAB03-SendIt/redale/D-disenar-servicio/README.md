# D — Diseñar el servicio

> Paso 3 de [R.E.D.A.L.E.](../README.md) · anterior: [**E** — Estimar](../E-estimar/README.md) ·
> siguiente: [**A** — Armar el modelo de datos](../A-armar-modelo-datos/README.md) · bitácora:
> [`ITERACIONES.md`](../ITERACIONES.md)

**Estado: andamiaje.** Ninguna decisión de este documento está tomada. Las tablas de decisión están
vacías y las preguntas abiertas siguen abiertas: se cierran contra el backlog ya evaluado.

Qué construimos y cómo. El material pide tres salidas: **arquitectura high-level** (3-tier, MVC,
monolito, servicios), **tipo de persistencia** (SQL, NoSQL, mixta) y **diseño de la API** (los
endpoints). Aquí se define el alcance y las expectativas de la arquitectura.

---

## Contrato con los pasos vecinos

| | |
|---|---|
| **Consume de E** | El orden de magnitud: cuántos servidores, cuánto almacenamiento y de qué tipo, cuánto ancho de banda y con qué asimetría. Y los supuestos declarados, porque una arquitectura elegida bajo un supuesto que se retira queda sin fundamento |
| **Consume de R** | Las garantías enunciadas en el backlog. Cada decisión de este paso es el **mecanismo** de una garantía; una decisión que no responde a ninguna garantía es preferencia técnica |
| **Entrega a A** | El tipo de persistencia por familia de dato, que es lo que `A` convierte en entidades y motores; y las decisiones de consistencia, que deciden si un dato se actualiza en el sitio o se agrega |
| **Entrega a L** | Los servicios que el diagrama dibuja como cajas, y las fronteras con terceros que el diagrama dibuja como externas |
| **Queda inválido si E cambia** | La justificación de escala. Si el número de servidores cruza un orden de magnitud, la opción de arquitectura deja de estar sostenida por su cálculo aunque siga siendo defendible por otra razón — y esa otra razón hay que escribirla |
| **Queda inválido si R cambia** | La decisión cuyo requerimiento desapareció, y toda la fila de la tabla de endpoints que lo servía |

---

## Lo que este paso registra y el backlog no puede contener

El backlog **enuncia la garantía**; este paso **elige el mecanismo**. La frontera es operativa, no
estilística: un requerimiento que nombra un mecanismo se verifica contra la implementación en vez de
contra el efecto, y sobrevive a su propia obsolescencia.

| El backlog dice | Este paso decide |
|---|---|
| «El sistema no cobrará dos veces el mismo envío» | Clave de idempotencia: quién la genera, cuándo se persiste, cuánto vive, qué devuelve el reintento |
| «El monto en soles que el remitente vio antes de pagar es el que se entrega» | Cuándo se fija la tasa, cuánto vive la cotización y quién absorbe el movimiento |
| «Una operación nunca figura en dos estados incompatibles» | Transacción distribuida, saga con compensación o conciliación — y cuál registro manda mientras diverge |
| «La decisión de cumplimiento y su evidencia no se pueden alterar» | Registro por adición frente a actualización en el sitio |

Toda decisión técnica desplazada desde el backlog aterriza **aquí**, no se suprime.

---

## 1. Arquitectura high-level

| Opción | A favor | En contra | Decisión |
|---|---|---|---|
| Monolito 3-tier | — | — | — |
| Monolito modular | — | — | — |
| Servicios | — | — | — |
| MVC (como organización interna) | — | — | — |
| Mixta — núcleo monolítico + servicios en la frontera | — | — | — |

**El criterio del propio material no se cumple aquí, y hay que decirlo.** El ejemplo del material
elige monolito con este argumento literal: *«la arquitectura elegida será 3-tier y en monolito ya
que encontramos que la aplicación no tendrá conexión hacia afuera»*. SendIt es lo contrario: tiene
al menos cinco conexiones hacia afuera —verificación de identidad, listas de sanciones, proveedor de
tipo de cambio, red pagadora en destino, y la autoridad a la que reporta cumplimiento—, y cada una
falla, tarda o miente por su cuenta. El criterio del material apunta en la otra dirección; si la
decisión final es igualmente monolito, tiene que apoyarse en otro argumento y decir cuál.

Preguntas que la tabla tiene que responder, no esquivar:

- ¿Qué se aísla porque falla distinto? Un tercero lento no puede arrastrar consigo el camino del
  pago.
- ¿Qué **no** se separa porque separarlo rompe una transacción? Partir el registro contable en dos
  servicios convierte una escritura atómica en un problema distribuido creado por el diseño.
- ¿La consola de cumplimiento y la aplicación del remitente son el mismo sistema? Tienen usuarios,
  ritmos, permisos y obligaciones de auditoría distintos.

## 2. Tipo de persistencia

| Familia de dato | Necesidad dominante | SQL / NoSQL / objetos / otro | Por qué | Decisión |
|---|---|---|---|---|
| Registro contable del dinero | — | — | — | — |
| Envío y su estado | — | — | — | — |
| Identidad de personas | — | — | — | — |
| Binarios de identidad (imágenes) | — | — | — | — |
| Resultado de tamizaje | — | — | — | — |
| Traza de auditoría | — | — | — | — |
| Cotizaciones de tipo de cambio | — | — | — | — |
| Catálogo de agentes y disponibilidad de efectivo | — | — | — | — |

La decisión es **por familia de dato, no global**. El propio material lo hace así en su ejemplo
—NoSQL para las imágenes, SQL para la metadata de usuario—, y aquí la diferencia es más marcada: el
mismo envío tiene una parte que exige integridad transaccional estricta y otra que es un binario de
megabytes que nunca se consulta salvo por auditoría.

## 3. Diseño de la API

| Método | Ruta | Quién la usa | Qué garantiza |
|---|---|---|---|
| — | — | — | — |

Los ejemplos del material listan rutas desnudas (`/tweet`, `/timeline`, `/user`, `/invoice`). Aquí
la tabla lleva dos columnas más y las dos son obligatorias:

- **Quién la usa** — la aplicación de Rosa, el canal de Elena, la consola de Marco, la red pagadora,
  o un proceso interno. Una ruta sin llamador identificado es una superficie de ataque sin dueño, y
  el enunciado dice que la seguridad es muy importante.
- **Qué garantiza** — y en particular, si es idempotente. **Un endpoint que mueve dinero y no
  declara su comportamiento ante el reintento es un defecto**, no una omisión de documentación.

Las rutas que este caso obliga a cubrir, sin decidir aún su forma: cotizar, confirmar el pago,
consultar estado, listar y decidir casos de cumplimiento, recibir la confirmación de cobro desde la
red pagadora, y devolver. Cada una traza a un ítem del backlog o no existe.

---

## Decisiones que este caso obliga y no se pueden posponer

Cinco. No están resueltas y no se resuelven aquí: se enuncian con su tensión para que la iteración
que las cierre sepa qué estaba en juego. Posponerlas no las deja abiertas — las resuelve por
omisión, y por omisión siempre salen mal.

### (a) Dónde vive la verdad del dinero

**Pregunta.** ¿El saldo de una operación es un campo que se actualiza, o el resultado de sumar
movimientos que solo se agregan?

**La tensión.** Un campo `estado` o `saldo` se lee rápido y no tiene historia: el valor anterior
desapareció cuando se sobrescribió. Un registro contable de partida doble —cada movimiento con su
contrapartida, cada asiento sumando cero— tiene historia completa y es reconstruible, pero obliga a
que **todo** hecho del envío se exprese como asiento, incluidos los que no parecen contables: la
retención de Marco, el vencimiento de un plazo, la devolución.

**Por qué no es un detalle de implementación.** La consistencia que el enunciado exige *—«estamos
hablando de dinero»—* es exactamente la invariante contable: el dinero no se crea ni se destruye, se
mueve entre cuentas, y toda diferencia tiene una contrapartida con nombre. Elegir un campo mutable
no es elegir una representación más simple de la misma cosa: es renunciar a poder demostrar que la
suma cuadra. Marco no puede auditar un campo que se sobrescribió, y su señal de éxito dice que un
año después su decisión y su evidencia siguen siendo recuperables.

**Qué queda decidido al responderla.** Si existe un libro de movimientos y cuáles son sus cuentas
(remitente, cuenta de tránsito de SendIt, cuenta con la red pagadora, comisión, diferencia de
cambio); si el estado del envío se deriva de los movimientos o se guarda aparte; y si se guarda
aparte, cuál de los dos manda cuando difieren. **Se propaga a** `A` (entidades y su mutabilidad) y a
`L` (el componente que escribe el libro).

### (b) Idempotencia

**Pregunta.** Rosa paga, se le cierra la app, vuelve a entrar y ve la pantalla de pago otra vez.
¿Quién genera la clave que identifica ese intento —el cliente antes de mandar, o el servidor al
recibir— y qué devuelve el sistema cuando llega el segundo intento?

**La tensión.** Si la clave la genera el servidor, un reintento del cliente es un intento nuevo y
Rosa paga dos veces; su señal de éxito lo prohíbe explícitamente. Si la genera el cliente, hay que
persistirla **antes** de mover un centavo, decidir cuánto vive, y decidir qué se responde al
reintento: devolver el resultado original es lo correcto y es distinto de devolver un error, porque
un error hace que Rosa lo intente por tercera vez.

**Y hay un segundo lado que se olvida.** La idempotencia del cobro a Rosa protege a Rosa. **El pago
a Elena lo ejecuta un tercero**, y la señal de éxito de Elena dice que nunca cobra dos veces el
mismo envío ni uno ya devuelto. Esa garantía no se consigue con la misma clave ni en el mismo
sistema.

**Qué queda decidido.** El alcance (¿solo el pago? ¿también cancelar, devolver, liberar una
retención?), el generador de la clave, su ventana de vida, la respuesta al reintento, y qué pasa
cuando llega un reintento con la misma clave y **distinto** contenido.

### (c) La frontera con la red pagadora

**Pregunta.** Una operación cruza a un tercero que tiene su propio registro contable y no participa
de nuestra transacción. ¿Transacción distribuida, saga con compensación, o conciliación?

**La tensión.** Las tres tienen un costo y ninguna elimina la divergencia; eligen **quién la
absorbe**.

| Opción | Qué supone | Dónde se rompe en este caso |
|---|---|---|
| Transacción distribuida | Que el tercero participe del protocolo y ceda control | La red pagadora no lo hace, y bloquear un recurso ajeno durante un viaje en combi no es viable |
| Saga con compensación | Que todo paso tenga inverso | «Se le entregó efectivo a Elena» **no tiene inverso**. La compensación de un pago consumado es una deuda, no una reversión |
| Conciliación | Que la divergencia sea temporal, detectable y acotada | Hay que decidir cuánto puede durar, quién manda mientras dura, y qué ve Rosa en ese intervalo |

**El caso concreto está documentado.** Marco tuvo dos días una operación que su sistema declaraba
retenida y el del pagador declaraba disponible para cobro. Elena cobró. Lo que no pudo explicarle al
auditor no fue su decisión: fue por qué sus propios registros afirmaban dos hechos incompatibles
sobre el mismo dinero.

**Qué queda decidido.** Cuál es el registro autoritativo durante la divergencia; la ventana máxima
tolerada; el mecanismo de detección y su periodicidad; qué estado ve Rosa mientras tanto; y qué
ocurre cuando la conciliación encuentra una diferencia que ya no se puede deshacer.

### (d) Cuándo se fija el tipo de cambio

**Pregunta.** ¿La tasa se fija al cotizar, al pagar, o al entregar? ¿Cuánto vive una cotización? Y
entre que Rosa paga y Elena cobra, ¿quién carga el movimiento?

**La tensión (T4 del conjunto de personas).** Rosa necesita prometerle una cifra a su madre antes de
pagar, y su señal de éxito dice que el número que vio es el que Elena cuenta. Fijarlo deja a SendIt
cargando la exposición cambiaria hasta que Elena cobre — que puede ser en tres días, o nunca, porque
la combi pasa cuando pasa. No fijarlo traslada esa exposición a la persona que menos puede
absorberla, y reproduce exactamente el caso que Elena ya vivió: treinta soles menos, «por el
cambio», sin nadie a quien preguntarle.

**Que la tasa se fije al pagar no lo decide este paso: lo exige el backlog.** Lo que este paso elige
es el mecanismo con el que se sostiene la promesa —cotización con vencimiento, cobertura, o margen
que la absorbe— y qué pasa cuando el vencimiento llega antes que Elena.

**Qué queda decidido.** La duración de la cotización; qué ocurre al vencer con el envío ya pagado;
en qué moneda y a qué valor se devuelve un envío que no se completó; y dónde se registra la
diferencia de cambio, que es una cuenta del libro de (a) y no un ajuste silencioso.

### (e) Dónde corre el tamizaje respecto del momento en que el dinero se compromete

**Pregunta.** El contraste contra listas y el análisis de patrón, ¿corren en el camino del pago
—bloqueando a Rosa hasta que resuelvan— o después de aceptar el dinero?

**La tensión (T1).** Marco lo dice sin ambigüedad: hoy el control corre después de aceptar, así que
su herramienta no es detener sino **revertir**, y revertir cruza la frontera de (c), donde él ya no
manda. Su señal de éxito exige que ninguna decisión suya se tome sobre dinero que ya salió. Pero
tamizar antes es tiempo que Rosa espera, y Rosa necesita una promesa firme al pagar, no un «en
proceso» de seis días.

**Y hay un caso que rompe cualquier respuesta simple.** Las listas se actualizan sin aviso, y una
lista nueva puede alcanzar a un envío ya aprobado con la lista anterior. Ese re-tamizaje corre por
definición **después**. De modo que la pregunta no es «antes o después» sino **qué se compromete en
cada punto de la secuencia**.

**La secuencia que hay que desagregar.** Autorizar el cobro a Rosa, capturar el cobro, acreditar en
la cuenta de tránsito, poner el dinero a disposición en el agente, y entregarlo a Elena son **cinco
momentos distintos**, no uno. Cada control se ancla a uno de ellos, y el punto de no retorno —el
último momento en que detener todavía es no-hacer en vez de deshacer— hay que nombrarlo
explícitamente.

**Qué queda decidido.** Qué control corre en cuál momento; cuál es el punto de no retorno; qué pasa
con un re-tamizaje posterior a ese punto; y qué ve Rosa mientras un envío está retenido, dado que
Marco tiene **prohibido** decirle el motivo cuando hay un reporte de por medio (T2). Esa última no
se resuelve redactando mejor un mensaje: hay que decidir qué se le dice cuando no se le puede decir
nada.

---

## Resumen de propagación

| Decisión | Se propaga a | Qué queda inválido si se reabre |
|---|---|---|
| (a) Verdad del dinero | `A`, `L` | El modelo de datos completo del envío y del movimiento; el componente que escribe el libro |
| (b) Idempotencia | `A`, `L`, API | La tabla de endpoints; la entidad que persiste la clave |
| (c) Frontera con el pagador | `A`, `L`, `E` (escalar) | El estado del envío; el componente de conciliación; el tramo en que la divergencia deja de ser manejable a mano |
| (d) Tipo de cambio | `A`, `L` | La entidad de cotización y la cuenta de diferencia de cambio |
| (e) Momento del tamizaje | `A`, `L`, `E` (estimar) | La carga del camino del pago; el orden de los componentes en el diagrama |

---

## Nota sobre las dos clases de iteración

La **iteración del diseño** —el mismo diagrama de componentes, dibujado otra vez y más abierto, que
es la que exige el enunciado ([ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md))— y la
**iteración del EVAL** no son lo mismo y [`ITERACIONES.md`](../ITERACIONES.md) las lleva en tablas
separadas. Este paso alimenta la primera: los servicios que aquí se nombren son las cajas que
[`L`](../L-listar-componentes/README.md) abre en su segunda pasada. Y lo afecta la segunda: un ítem
nuevo en el backlog puede reabrir cualquiera de las cinco decisiones de arriba.
