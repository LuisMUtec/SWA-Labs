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
| **Entrega a L** | Los servicios que el diagrama dibuja como cajas, las fronteras con terceros que el diagrama dibuja como externas, y la frontera interna con el punto de pago —que no es externa y falla igual de fuerte, porque puede quedarse sin conexión |
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
| «El estado del envío es uno solo entre el centro y el punto de pago, incluso sin conexión» | Qué puede hacer un mostrador desconectado, cuál lado manda mientras dura, y cómo se resuelve la divergencia al reconectar |
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
al menos cuatro conexiones hacia afuera —verificación de identidad, listas de sanciones, proveedor de
tipo de cambio, y la autoridad a la que reporta cumplimiento—, y cada una falla, tarda o miente por
su cuenta. Y tiene además una parte **propia que puede quedar incomunicada**: el punto de pago corre
sobre el sistema de SendIt, pero está en una plaza de Huanta y puede perder la conexión con billetes
en la caja. El criterio del material apunta en la otra dirección; si la decisión final es igualmente
monolito, tiene que apoyarse en otro argumento y decir cuál —y tiene que decir qué corre en el
mostrador cuando el centro no está.

Preguntas que la tabla tiene que responder, no esquivar:

- ¿Qué se aísla porque falla distinto? Un tercero lento no puede arrastrar consigo el camino del
  pago.
- ¿Qué **no** se separa porque separarlo rompe una transacción? Partir el registro contable en dos
  servicios convierte una escritura atómica en un problema distribuido creado por el diseño.
- ¿La consola de cumplimiento y el punto de venta del mostrador son el mismo sistema? Tienen usuarios,
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
| Catálogo de puntos de pago y disponibilidad de efectivo | — | — | — | — |
| Estado que el mostrador sostiene mientras opera sin conexión | — | — | — | — |

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

- **Quién la usa** — la ventanilla donde Rosa origina, el canal de Elena, el mostrador de Kevin, o
  un proceso interno. Una ruta sin llamador identificado es una superficie de ataque sin dueño, y
  el enunciado dice que la seguridad es muy importante.
- **Qué garantiza** — y en particular, si es idempotente. **Un endpoint que mueve dinero y no
  declara su comportamiento ante el reintento es un defecto**, no una omisión de documentación.

Las rutas que este caso obliga a cubrir, sin decidir aún su forma: cotizar, confirmar el pago,
consultar estado, listar y decidir casos de cumplimiento, autorizar el pago hacia el punto, recibir
la confirmación de cobro desde el mostrador, sincronizar un punto que estuvo sin conexión, y
devolver. Cada una traza a un ítem del backlog o no existe.

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
la retención de cumplimiento, el vencimiento de un plazo, la devolución.

**Por qué no es un detalle de implementación.** La consistencia que el enunciado exige *—«estamos
hablando de dinero»—* es exactamente la invariante contable: el dinero no se crea ni se destruye, se
mueve entre cuentas, y toda diferencia tiene una contrapartida con nombre. Elegir un campo mutable
no es elegir una representación más simple de la misma cosa: es renunciar a poder demostrar que la
suma cuadra. Nadie puede auditar un campo que se sobrescribió, y `BR-15` exige que un
año después su decisión y su evidencia siguen siendo recuperables.

**Qué queda decidido al responderla.** Si existe un libro de movimientos y cuáles son sus cuentas
(remitente, cuenta de tránsito de SendIt, caja del punto de pago, comisión, diferencia de
cambio); si el estado del envío se deriva de los movimientos o se guarda aparte; y si se guarda
aparte, cuál de los dos manda cuando difieren. **Se propaga a** `A` (entidades y su mutabilidad) y a
`L` (el componente que escribe el libro).

### (b) Idempotencia

**Pregunta.** Rosa paga en la ventanilla, la operación se corta, Kevin vuelve a entrar y ve la pantalla de registro otra vez.
¿Quién genera la clave que identifica ese intento —el cliente antes de mandar, o el servidor al
recibir— y qué devuelve el sistema cuando llega el segundo intento?

**La tensión.** Si la clave la genera el servidor, un reintento del cliente es un intento nuevo y
Rosa paga dos veces; su señal de éxito lo prohíbe explícitamente. Si la genera el cliente, hay que
persistirla **antes** de mover un centavo, decidir cuánto vive, y decidir qué se responde al
reintento: devolver el resultado original es lo correcto y es distinto de devolver un error, porque
un error hace que Rosa lo intente por tercera vez.

**Y hay un segundo lado que se olvida.** La idempotencia del cobro a Rosa protege a Rosa. **El pago
a Elena lo ejecuta un mostrador propio que puede estar sin conexión**, con una autorización que bajó
antes, y la señal de éxito de Elena dice que nunca cobra dos veces el mismo envío ni uno ya
devuelto. Es el mismo sistema, así que la clave puede ser una sola — pero el lugar donde se
comprueba no lo es: si la comprobación vive únicamente en el centro, un mostrador desconectado no la
puede hacer, y si vive en el mostrador, dos mostradores desconectados no se ven entre sí.

**Qué queda decidido.** El alcance (¿solo el pago? ¿también cancelar, devolver, liberar una
retención?), el generador de la clave, su ventana de vida, la respuesta al reintento, y qué pasa
cuando llega un reintento con la misma clave y **distinto** contenido.

### (c) La frontera entre el centro y el mostrador

**Pregunta.** El punto de pago es de SendIt y corre sobre el sistema de SendIt, pero está en una
plaza de Huanta y puede perder la conexión con billetes en la caja y una autorización previa que
dice «paga». **¿Qué hace el mostrador mientras dura eso?**

**La tensión.** No es una negociación con un tercero: la contabilidad es una sola y del otro lado la
orden del centro se acata sin discutirla. Lo que falta no es acuerdo, es **conexión** — y sin ella el
centro no puede impedir un pago ni el mostrador puede saber que lo prohibieron. Cualquier respuesta
elige a quién dejar sin servicio: a Elena, que viajó cuarenta minutos en combi, o a quien ordenó
detener.

| Opción | Qué supone | Dónde se rompe en este caso |
|---|---|---|
| El mostrador no paga sin confirmación en línea del centro | Que la conexión sea la condición de operar | Una caída de línea cierra el punto. Elena viajó, hizo la cola y vuelve con las manos vacías por un motivo que no tiene nada que ver con ella — y el sistema queda cumpliendo el invariante por el método de no pagarle a nadie |
| El mostrador paga con la autorización previa, acotado por ventana y monto | Que la autorización caduque sola y que el límite absorba el daño de lo que se pague de más | Hay que fijar la ventana y el límite sin dato: son exactamente el `[CLARIFY]` que RNF-08 dejó abierto. Y un envío puede caer dentro de la ventana y aun así ser el que Marco ordenó detener |
| El mostrador paga siempre y el centro absorbe la divergencia al reconectar | Que todo pago sea un hecho que se agrega y nunca se contradice | «Se le entregó efectivo a Elena» **no tiene inverso**: deshacer un pago consumado es una deuda, no una reversión. El invariante de RNF-08 se rompe por diseño y hay que decir durante cuánto |

**El caso concreto está documentado.** Se ordenó detener un envío cuando la autorización ya había
bajado al punto de Huanta, que llevaba desde la mañana sin conexión. El centro decía «retenido»; el
mostrador decía «disponible para cobro». Elena cobró. Lo que no se le pudo explicar al auditor no
fue la decisión: fue por qué **los registros propios** —los dos propios, no uno propio y uno ajeno—
afirmaban dos hechos incompatibles sobre el mismo dinero.

**Qué queda decidido.** Qué se le permite hacer a un mostrador sin conexión y hasta qué monto y por
cuánto tiempo; cuál de los dos lados manda mientras dura; cómo se detecta la divergencia al
reconectar y qué se hace con un pago que el centro había ordenado detener; qué estado ve Rosa en
ese intervalo; y —lo que RNF-08 dejó marcado— cuál es la **ventana máxima** en que un envío puede
figurar detenido en el centro y disponible en el mostrador sin que el invariante deje de ser
alcanzable.

### (d) Cuándo se fija el tipo de cambio

**Pregunta.** ¿La tasa se fija al cotizar, al pagar, o al entregar? ¿Cuánto vive una cotización? Y
entre que Rosa paga y Elena cobra, ¿quién carga el movimiento?

**La tensión (T4 del conjunto de personas).** Rosa necesita prometerle una cifra a su madre antes de
pagar, y su señal de éxito dice que el número que vio es el que Elena cuenta. Fijarlo deja a SendIt
cargando la exposición cambiaria hasta que Elena cobre — que puede ser en tres días, o nunca, porque
la combi pasa cuando pasa. No fijarlo traslada esa exposición a la persona que menos puede
absorberla, y reproduce exactamente el caso que Elena ya vivió: treinta soles menos, «por el
cambio», explicados por un mostrador que no produjo esa diferencia y no la tiene a la vista. Ahora
hay a quién reclamarle; lo que falta es que quien atiende tenga qué contestar.

**Que la tasa se fije al pagar no lo decide este paso: lo exige el backlog.** Lo que este paso elige
es el mecanismo con el que se sostiene la promesa —cotización con vencimiento, cobertura, o margen
que la absorbe— y qué pasa cuando el vencimiento llega antes que Elena.

**Qué queda decidido.** La duración de la cotización; qué ocurre al vencer con el envío ya pagado;
en qué moneda y a qué valor se devuelve un envío que no se completó; y dónde se registra la
diferencia de cambio, que es una cuenta del libro de (a) y no un ajuste silencioso.

### (e) Dónde corre el tamizaje respecto del momento en que el dinero se compromete

**Pregunta.** El contraste contra listas y el análisis de patrón, ¿corren en el camino del pago
—bloqueando a Rosa hasta que resuelvan— o después de aceptar el dinero?

**La tensión (T1).** Kevin lo dice sin ambigüedad: el control tiene que correr antes de que él
toque el efectivo, porque si corre después la herramienta ya no es detener sino **revertir**. Sobre
los puntos el negocio sí manda —son propios y corren su sistema, y puede pararse un pago antes de
que el mostrador lo entregue—; lo único que la orden no alcanza es el punto sin conexión que ya
recibió la autorización, que es la frontera de (c). Su señal de éxito exige que ninguna decisión se
tome sobre dinero que ya salió. Pero
tamizar antes es tiempo que Rosa espera, y Rosa necesita una promesa firme al pagar, no un «en
proceso» de seis días.

**Y hay un caso que rompe cualquier respuesta simple.** Las listas se actualizan sin aviso, y una
lista nueva puede alcanzar a un envío ya aprobado con la lista anterior. Ese re-tamizaje corre por
definición **después**. De modo que la pregunta no es «antes o después» sino **qué se compromete en
cada punto de la secuencia**.

**La secuencia que hay que desagregar.** Autorizar el cobro a Rosa, capturar el cobro, acreditar en
la cuenta de tránsito, bajar la autorización al punto de pago, y entregarle el efectivo a Elena son
**cinco momentos distintos**, no uno. Cada control se ancla a uno de ellos, y el punto de no retorno
—el último momento en que detener todavía es no-hacer en vez de deshacer— hay que nombrarlo
explícitamente. Con un punto que puede quedar sin conexión, ese punto de no retorno **se cruza sin
que el centro se entere**: entre el cuarto momento y el quinto puede no haber ninguna señal de
vuelta.

**Qué queda decidido.** Qué control corre en cuál momento; cuál es el punto de no retorno; qué pasa
con un re-tamizaje posterior a ese punto; y qué ve Rosa mientras un envío está retenido, dado que
Kevin, que es la cara de SendIt frente a ella, tiene **prohibido** decirle el motivo cuando hay un reporte de por medio (T2). Esa última no
se resuelve redactando mejor un mensaje: hay que decidir qué se le dice cuando no se le puede decir
nada.

---

## Resumen de propagación

| Decisión | Se propaga a | Qué queda inválido si se reabre |
|---|---|---|
| (a) Verdad del dinero | `A`, `L` | El modelo de datos completo del envío y del movimiento; el componente que escribe el libro |
| (b) Idempotencia | `A`, `L`, API | La tabla de endpoints; la entidad que persiste la clave |
| (c) Frontera entre el centro y el mostrador | `A`, `L`, `E` (escalar) | El estado del envío y el que el mostrador sostiene sin conexión; el componente que sincroniza el punto al reconectar; el tramo en que la divergencia deja de ser manejable a mano |
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
