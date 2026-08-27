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
| **Entrega a L** | Los servicios que el diagrama dibuja como cajas, las fronteras con terceros que el diagrama dibuja como externas, y la frontera con el **punto de atención** —que corre el software de SendIt sobre el mostrador de un agente afiliado, paga con el efectivo de la caja del agente y obliga a liquidárselo después (`RF-24`)—: es a la vez frontera contable y extremo que puede quedarse sin conexión |
| **Queda inválido si E cambia** | La justificación de escala. Si el número de servidores cruza un orden de magnitud, la opción de arquitectura deja de estar sostenida por su cálculo aunque siga siendo defendible por otra razón — y esa otra razón hay que escribirla |
| **Queda inválido si R cambia** | La decisión cuyo requerimiento desapareció, y toda la fila de la tabla de endpoints que lo servía |

---

## Lo que este paso registra y el backlog no puede contener

El backlog **enuncia la garantía**; este paso **elige el mecanismo**. La frontera es operativa, no
estilística: un requerimiento que nombra un mecanismo se verifica contra la implementación en vez de
contra el efecto, y sobrevive a su propia obsolescencia.

| El backlog dice | Este paso decide |
|---|---|
| `RF-35` — «el sistema rechazará todo intento de pago sobre un giro ya pagado, en cualquier punto de la red» | Clave de idempotencia: quién la genera, cuándo se persiste, cuánto vive, qué devuelve el reintento (`RF-43`, `RF-44`) |
| `RF-06` — «el sistema conservará ese monto sin recalcularlo durante toda la vida del giro» | Cuánto vive la cotización que `RF-07` fecha, y quién absorbe el movimiento cambiario hasta que el receptor cobra |
| `RNF-06` — «el sistema mantendrá un solo estado del giro entre el centro y el punto de atención» | Qué puede hacer un punto sin conexión, cuál lado manda mientras dura, y cómo se resuelve la divergencia al reconectar (`RNF-08`) |
| `RF-55` — «el sistema impedirá modificar o eliminar el registro de un acto ya ejecutado» | Registro por adición frente a actualización en el sitio |
| `RF-12` — «el sistema comprobará la respuesta del desafío sin mostrarla a quien atiende el mostrador», con el invariante de `RNF-17`: «El sistema puede comprobar una respuesta sin poder mostrarla, en los dos lados del mostrador» | Con qué transformación se guarda la respuesta que `RF-68` le pide al emisor, dónde corre la comparación que `RF-69` habilita, cómo se cuentan los intentos de `RF-82` y qué caduca con el giro por `RF-83` |

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
elige monolito 3-tier con el argumento de que su aplicación no tiene conexiones hacia afuera — no
está transcrito literal en este repositorio, así que se usa como criterio y no como cita. SendIt es
lo contrario de ese caso: tiene
al menos cinco conexiones hacia afuera —verificación del documento oficial (`RF-01`), listas de
sanciones (`RF-26`, `RF-27`), proveedor de tipo de cambio (`RF-07`), la autoridad de origen a la que
reporta (`RF-17`) y el canal de llamada o mensaje de texto por el que se avisa al receptor
(`RF-25`)—, y cada una falla, tarda o miente por su cuenta. Y tiene además un **extremo que puede
quedar incomunicado**: el punto de atención corre el software de SendIt sobre el mostrador de un
agente afiliado, está en una plaza de Huanta y puede perder la conexión con los billetes del agente
en la caja. El criterio del material apunta en la otra dirección; si la decisión final es igualmente
monolito, tiene que apoyarse en otro argumento y decir cuál —y tiene que decir qué corre en el
mostrador cuando el centro no está, sabiendo que `RF-45` ya le prohíbe pagar lo que el centro
retuvo, canceló o dio por pagado en otro punto.

Preguntas que la tabla tiene que responder, no esquivar:

- ¿Qué se aísla porque falla distinto? Un tercero lento no puede arrastrar consigo el camino del
  pago.
- ¿Qué **no** se separa porque separarlo rompe una transacción? Partir el registro contable en dos
  servicios convierte una escritura atómica en un problema distribuido creado por el diseño.
- ¿El puesto desde el que se resuelven las retenciones y el mostrador del operario son el mismo
  sistema? `RF-30` deriva el giro retenido a un rol distinto del que lo atendió, `RF-33` reserva la
  liberación al rol de cumplimiento y `RF-87` obliga a que deje su motivo escrito, `RNF-02` prohíbe
  que una misma identidad ejerza dos roles del mismo giro y `RF-57` limita al operario a la
  operación que está atendiendo. Separar los dos puestos —o no separarlos— es el mecanismo de esas
  exigencias, no una preferencia de despliegue.

## 2. Tipo de persistencia

| Familia de dato | Necesidad dominante | SQL / NoSQL / objetos / otro | Por qué | Decisión |
|---|---|---|---|---|
| Registro contable del dinero | — | — | — | — |
| Giro y su estado | — | — | — | — |
| Código de seguimiento (`RF-11`, `RNF-15`) | — | — | — | — |
| Respuesta del desafío y sus intentos (`RF-68`, `RF-12`, `RF-82`, `RNF-17`) | — | — | — | — |
| Acumulado del emisor en la ventana vigente (`RF-09`, `RF-10`) | — | — | — | — |
| Acumulado de cobros del receptor en la ventana vigente (`RF-58`, `RF-93`) | — | — | — | — |
| Identidad de personas | — | — | — | — |
| Binarios de identidad (imágenes) — evidencia que `RF-80` obliga a conservar | — | — | — | — |
| Resultado de tamizaje | — | — | — | — |
| Traza de auditoría | — | — | — | — |
| Cotizaciones de tipo de cambio | — | — | — | — |
| Catálogo de puntos de atención y efectivo disponible en el corredor (`RF-20`, `RF-63`) | — | — | — | — |
| Efectivo que cada punto declara al abrir y al cerrar su caja (`RF-76`, `RF-92`) | — | — | — | — |
| Devolución pendiente de retiro y su plazo (`RF-14`, `RF-89`) | — | — | — | — |
| Declaración de diferencia hecha por el receptor en el mostrador (`RF-90`, `RF-59`) | — | — | — | — |
| Estado que el punto sostiene mientras opera sin conexión | — | — | — | — |

La decisión es **por familia de dato, no global**. El propio material lo hace así en su ejemplo
—NoSQL para las imágenes, SQL para la metadata de usuario—, y aquí la diferencia es más marcada: el
mismo giro tiene una parte que exige integridad transaccional estricta y otra que es un binario de
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

Las capacidades que este caso obliga a exponer —sin decidir aún su verbo ni su forma— y el ítem del
que cada una cuelga. **Cada una traza a un ítem del backlog o no existe**, y la tabla vacía de arriba
se llena contra esta:

| Capacidad obligada | Traza a | Llamador |
|---|---|---|
| Cotizar e informar el monto en moneda destino antes del efectivo | `RF-05`, `RF-07`, `RF-21` | Ventanilla de origen |
| Informar antes del efectivo lo que el emisor tiene que saber: desde cuándo se cobra, el plazo de una eventual devolución y si el país destino se puede atender | `RF-77`, `RF-73`, `RF-19` | Ventanilla de origen |
| Elegir el punto de atención donde cobrará el receptor | `RF-63` | Ventanilla de origen, por el emisor |
| Crear el giro y entregar el código únicamente al emisor | `RF-11`, `RNF-15` | Ventanilla de origen |
| Registrar la pregunta del desafío y su respuesta al crear el giro | `RF-68`, `RNF-17` | Ventanilla de origen, por el emisor |
| Registrar la recepción del efectivo, que es lo que da el giro por creado | `RF-79`, `RF-08`, `RF-09`, `RF-20` | Ventanilla de origen |
| Pedir y otorgar la segunda autorización | `RF-13`, `RF-61` | Segundo rol, nunca el mismo operario |
| Avisar al receptor por llamada o mensaje de texto | `RF-25`, `RF-41`, `RF-60`, `RF-75` | Proceso interno hacia el canal de Elena |
| Reportar a la autoridad de origen | `RF-17`, `RF-22` | Proceso interno hacia la autoridad |
| Listar y decidir giros retenidos | `RF-29`, `RF-30` | Rol de cumplimiento |
| Liberar una retención dejando registrado el motivo | `RF-33`, `RF-87` | Rol de cumplimiento, distinto del que atendió |
| Contar los cobros del receptor en la ventana y retener al superarla | `RF-58`, `RF-93` | Proceso interno hacia el rol de cumplimiento |
| Autorizar el pago hacia el punto contra las listas vigentes | `RF-27`, `RF-36` | Centro → punto de atención |
| Informar al operario el efectivo de su punto antes de habilitarle un pago | `RF-92` | Centro → punto de atención |
| Declarar el efectivo del punto al abrir y al cerrar la caja | `RF-76` | Punto de atención → centro |
| Comprobar la respuesta del desafío sin mostrarla, con intentos acotados | `RF-12`, `RF-69`, `RF-82`, `RF-83`, `RF-86`, `RNF-17` | Punto de atención → centro. **Nunca devuelve la respuesta: devuelve el veredicto** |
| Confirmar el cobro desde el mostrador, en efectivo y por el monto fijado | `RF-34`, `RF-85`, `RF-02`, `RF-38`, `RF-64`, `RF-65` | Punto de atención → centro |
| Cobrar en otro punto del país destino cuando el elegido no puede pagar | `RF-91` | Punto de atención → centro |
| Registrar la declaración del receptor de que el dinero no coincide | `RF-90`, `RF-59` | Punto de atención → centro, por el receptor |
| Sincronizar un punto que estuvo sin conexión | `RF-45`, `RNF-08` | Punto de atención → centro |
| Consultar el estado de los giros propios | `RF-52`, `RF-53`, `RF-66` | Emisor |
| Cancelar y devolver | `RF-46`, `RF-47`, `RF-62` | Emisor, nunca el receptor (`RF-48`) |
| Avisar la devolución disponible y dónde retirarla | `RF-14`, `RF-72` | Proceso interno hacia el emisor |
| Retirar la devolución en efectivo, en la moneda entregada, con su comisión | `RF-71`, `RF-88`, `RF-74`, `RF-89` | Punto de atención elegido por el emisor → centro |
| Vencer una retención y devolver | `RF-31`, `RF-32` | Proceso interno |
| Prescribir y poner el monto a disposición del emisor | `RF-49`, `RF-50`, `RF-51` | Proceso interno |
| Liquidar con el agente el efectivo que puso de su caja | `RF-24` | Proceso interno hacia el agente |
| Suprimir a pedido los datos personales de quien los entregó | `RF-81` | Emisor → proceso interno, acotado por lo que `RF-55` obliga a conservar |

---

## Decisiones que este caso obliga y no se pueden posponer

Seis. No están resueltas y no se resuelven aquí: se enuncian con su tensión para que la iteración
que las cierre sepa qué estaba en juego. Posponerlas no las deja abiertas — las resuelve por
omisión, y por omisión siempre salen mal.

### (a) Dónde vive la verdad del dinero

**Pregunta.** ¿El saldo de una operación es un campo que se actualiza, o el resultado de sumar
movimientos que solo se agregan?

**La tensión.** Un campo `estado` o `saldo` se lee rápido y no tiene historia: el valor anterior
desapareció cuando se sobrescribió. Un registro contable de partida doble —cada movimiento con su
contrapartida, cada asiento sumando cero— tiene historia completa y es reconstruible, pero obliga a
que **todo** hecho del giro se exprese como asiento, incluidos los que no parecen contables: la
retención (`RF-29`), el vencimiento de su plazo sin liberación (`RF-32`), la devolución por
cancelación (`RF-47`) y la prescripción (`RF-50`).

**Por qué no es un detalle de implementación.** La consistencia que el enunciado exige *—«estamos
hablando de dinero»—* es exactamente la invariante contable: el dinero no se crea ni se destruye, se
mueve entre cuentas, y toda diferencia tiene una contrapartida con nombre. Elegir un campo mutable
no es elegir una representación más simple de la misma cosa: es renunciar a poder demostrar que la
suma cuadra —que es literalmente el invariante de `RNF-07`: «Lo que sale de una cuenta entra en
otra». Nadie puede auditar un campo que se sobrescribió, y `RF-55` prohíbe modificar el registro de
un acto ya ejecutado mientras `RNF-03` obliga a que siga íntegro por el plazo más largo de los dos
reguladores del giro (`BR-15`).

**Qué queda decidido al responderla.** Si existe un libro de movimientos y cuáles son sus cuentas
—el efectivo que entregó el emisor, la obligación de SendIt frente al receptor mientras nadie cobra
(`BR-01`), la caja del agente que pone el efectivo en destino y que hay que liquidarle (`RF-24`), y
la diferencia de cambio—; si el estado del giro se deriva de los movimientos o se guarda aparte; y
si se guarda aparte, cuál de los dos manda cuando difieren. **Se propaga a** `A` (entidades y su
mutabilidad) y a `L` (el componente que escribe el libro).

### (b) Idempotencia

**Pregunta.** Rosa entrega el efectivo en la ventanilla, la operación se corta, Kevin vuelve a
entrar y ve la pantalla de registro otra vez. `RF-43` obliga a tratar ese reintento como la misma
operación. ¿Quién genera la clave que lo identifica —el cliente antes de mandar, o el servidor al
recibir— y qué devuelve el sistema cuando llega el segundo intento?

**La tensión.** Si la clave la genera el servidor, un reintento del cliente es un intento nuevo y
Rosa entrega un giro y le cobran dos; `RF-43` lo prohíbe. Si la genera el cliente, hay que
persistirla **antes** de mover un centavo, decidir cuánto vive, y decidir qué se responde al
reintento: devolver el resultado original es lo correcto y es distinto de devolver un error, porque
un error hace que Rosa lo intente por tercera vez.

**Y hay un segundo lado que se olvida.** La idempotencia de la **creación** protege al emisor
(`RF-43`). El **pago** es el otro lado y lo ejecuta el mostrador de un agente que puede estar sin
conexión, con una autorización que bajó antes: `RF-44` obliga a tratar el reintento de un pago
interrumpido como la misma operación, `RF-35` rechaza todo segundo pago **en cualquier punto de la
red**, y `RF-62` lo rechaza sobre un giro ya cancelado y devuelto. El software es el mismo, así que
la clave puede ser una sola — pero el lugar donde se comprueba no lo es: si la comprobación vive
únicamente en el centro, un punto desconectado no la puede hacer, y si vive en el punto, dos puntos
desconectados no se ven entre sí. Es la misma frontera que (c), vista desde el reintento.

**Qué queda decidido.** El alcance (¿solo el pago? ¿también cancelar y devolver —`RF-46`, `RF-47`—,
o liberar una retención, que `RF-33` obliga a registrar con motivo?), el generador de la clave, su
ventana de vida, la respuesta al reintento, y qué pasa cuando llega un reintento con la misma clave
y **distinto** contenido.

### (c) La frontera entre el centro y el punto de atención

**Lo que `RF-45` ya cerró, y este documento tenía abierto de más.** El ítem es P0 y no admite lectura
intermedia: *«el sistema impedirá que un punto sin conexión pague un giro que el centro ya retuvo,
canceló o dio por pagado en otro punto»*. Eso elimina dos de las tres respuestas que aquí figuraban
—pagar siempre y dejar que el centro absorba la divergencia al reconectar, y pagar cualquier giro
que caiga dentro de la ventana de una autorización previa sin mirar nada más—: las dos pagan
exactamente el giro que `RF-45` protege. No son opciones caras; son opciones prohibidas.

**La pregunta que queda es más chica y más precisa.** ¿Qué hace el punto sin conexión con un giro
sobre el que **no pesa ninguna de esas tres condiciones**? Y antes de eso, la parte difícil: **cómo
sabe que no pesa.** La ausencia de una orden no viaja por una línea caída, y una retención nace en
el centro (`RF-29`) sin preguntarle al punto si está conectado. Prohibir el pago de lo retenido es
barato de enunciar y caro de comprobar sin línea.

**La tensión.** El mostrador corre el software de SendIt, pero el efectivo es del agente y SendIt se
lo liquida después (`RF-24`): hay frontera contable, y aun así del otro lado la orden del centro se
acata sin discutirla. Lo que falta cuando cae la línea no es acuerdo, es **conexión** — el centro no
puede impedir un pago y el punto no puede saber que lo prohibieron. Cualquier respuesta elige a quién
dejar sin servicio: al receptor, que viajó cuarenta minutos en combi, o a quien ordenó detener.

| Opción sobre el giro sin condición en contra | Qué supone | Dónde se rompe en este caso |
|---|---|---|
| El punto no paga sin confirmación en línea del centro | Que la conexión sea la condición de operar | Una caída de línea cierra el punto. Elena viajó, hizo la cola y vuelve con las manos vacías por un motivo que no tiene nada que ver con ella — y el sistema cumple `RF-45` y `RNF-06` por el método de no pagarle a nadie, después de que `RF-41` y `RF-75` le prometieran antes de viajar que ese punto podía pagarle. La salida que `RF-91` le da —cobrar en otro punto del país destino— exige línea para trasladar el giro, que es justo lo que falta |
| El punto paga contra la autorización que el centro ya le bajó, con caducidad corta y tope de monto, y trata como no pagable todo giro cuya ausencia de retención no pueda sostener con lo que tiene local | Que la autorización caduque sola, que el tope acote el daño y que lo no demostrable se rechace en vez de pagarse | Hay que fijar caducidad y tope, y el backlog no los da: `RNF-09` acota el mostrador y `RNF-10` la disponibilidad, ninguno la vida de una autorización fuera de línea. El techo no es negociable: `RNF-06` no admite ventana |
| El centro le empuja al punto las prohibiciones antes de la caída —retenidos, cancelados, pagados en otro punto— y el punto paga lo demás | Que la lista de prohibiciones viaje antes que la caída | Se rompe con la retención que nace mientras el punto está caído: `RF-29` no espera a que vuelva. No elimina la ventana, la desplaza al último empujón hecho — y hay que decir cuánto puede durar ese desfase |

**El caso de Huanta, que hoy es lo que el backlog prohíbe.** Se ordenó detener un giro cuando la
autorización ya había bajado al punto, que llevaba desde la mañana sin conexión. El centro decía
«retenido»; el mostrador decía «disponible para cobro»; Elena cobró. Eso **ya no es un precedente
que el diseño tolere**: es la conducta que `RF-45` prohíbe y el estado que `RNF-06` declara
imposible —*«Dos lugares del sistema nunca afirman a la vez que un giro está retenido y disponible
para cobro»*—. Lo que el caso sigue aportando es el costo, no la licencia: lo que no se le pudo
explicar al auditor no fue la decisión, fue que dos registros del mismo sistema afirmaran dos hechos
incompatibles sobre el mismo dinero. El diseño no tiene que justificar ese desenlace; tiene que
volverlo inalcanzable y decir, en la misma frase, quién se queda sin cobrar mientras tanto.

**Qué queda decidido.** Qué se le permite hacer a un punto sin conexión sobre un giro sin condición
en contra, hasta qué monto y por cuánto tiempo; con qué evidencia local sostiene que no pesa ninguna
de las tres condiciones de `RF-45`; cuál de los dos lados manda mientras dura; cómo se detecta y se
salda la divergencia al reconectar **sin que el operario tenga que contarla**, que es lo que `RNF-08`
exige; qué ve el emisor en ese intervalo (`RF-52`, `RF-53`, `RF-66`); y cuánto puede tardar el punto
en enterarse de una retención sin que `RNF-06` deje de ser alcanzable — el invariante no admite
ventana, así que lo que se fija no es una tolerancia sino el mecanismo que la lleva a cero.

### (d) Cuándo se fija el tipo de cambio

**Pregunta.** El *cuándo* ya está cerrado por el backlog: la tasa se fija **al crear el giro**. Lo
que queda abierto es cuánto vive una cotización antes de que el giro se cree, y quién carga el
movimiento cambiario entre que Rosa entrega el efectivo y Elena cobra.

**La tensión (T4 del conjunto de personas).** Rosa necesita prometerle una cifra a su madre antes de
pagar, y su señal de éxito dice que el número que vio es el que Elena cuenta. Fijarlo deja a SendIt
cargando la exposición cambiaria hasta que Elena cobre — que puede ser en tres días, o nunca, porque
la combi pasa cuando pasa. No fijarlo traslada esa exposición a la persona que menos puede
absorberla, y reproduce exactamente el caso que Elena ya vivió: treinta soles menos, «por el
cambio», explicados por un mostrador que no produjo esa diferencia y no la tiene a la vista. El
backlog ya cerró ese hueco por tres lados —`RF-38` impide entregar un monto distinto del fijado,
`RF-59` obliga a atribuir toda diferencia a un responsable nombrado y `RF-60` se la informa al
receptor—; lo que falta es el mecanismo que hace que quien atiende tenga qué contestar.

**El backlog no deja abierto el momento, y conviene citarlo bien.** `RF-05` obliga a informar el
monto exacto en moneda destino **antes de que el emisor entregue el efectivo**, `RF-06` lo conserva
«sin recalcularlo durante toda la vida del giro» y `RF-07` produce y fecha la cotización de la que
sale (`BR-07`). La tasa se fija **al crear el giro**, no al pagar. Lo que este paso elige es el
mecanismo con el que se sostiene esa promesa —cotización con vencimiento previo a la creación,
cobertura, o margen que la absorbe— y qué pasa cuando el mercado se mueve y Elena todavía no llegó.

**Qué queda decidido.** Cuánto vive una cotización antes de crear el giro; qué se hace con el giro
ya creado cuando esa cotización queda lejos del mercado, dado que `RF-06` no permite recalcularla;
en qué moneda y a qué valor se devuelve el giro cancelado (`RF-47`), el que venció retenido
(`RF-32`) y el prescrito (`RF-50`); y dónde se registra la diferencia de cambio, que es una cuenta
del libro de (a) y no un ajuste silencioso.

### (e) Dónde corre el tamizaje respecto del momento en que el dinero se compromete

**Pregunta.** El contraste contra listas y el análisis de patrón, ¿corren en el camino del pago
—bloqueando a Rosa hasta que resuelvan— o después de aceptar el dinero?

**La tensión (T1).** Kevin lo dice sin ambigüedad: el control tiene que correr antes de que él
toque el efectivo, porque si corre después la herramienta ya no es detener sino **revertir**. Sobre
los puntos el sistema sí manda mientras haya línea —el mostrador del agente corre el software de
SendIt y un pago puede detenerse antes de que el efectivo salga de la caja—; lo único que la orden
no alcanza es el punto sin conexión que ya recibió la autorización, que es la frontera de (c) y lo
que `RF-45` obliga a cerrar. `RF-26` fija el momento: el tamizaje corre antes de aceptar el
efectivo. Pero
tamizar antes es tiempo que Rosa espera, y Rosa necesita una promesa firme al pagar, no un «en
proceso» de seis días.

**Y hay un caso que rompe cualquier respuesta simple.** Las listas se actualizan sin aviso, y una
lista nueva puede alcanzar a un giro ya aprobado con la anterior. `RF-27` ya lo decide en un
sentido: al receptor se lo contrasta contra las listas **vigentes al momento de autorizar el pago**,
no contra las de la creación. Ese segundo tamizaje corre por definición **después**. De modo que la
pregunta no es «antes o después» sino **qué se compromete en cada punto de la secuencia**.

**La secuencia que hay que desagregar.** Identificar y tamizar antes de tocar el efectivo (`RF-01`,
`RF-26`), aceptar el efectivo en la ventanilla de origen (`RF-02`), dar el giro por fondeado con
efectivo disponible en el corredor de destino (`RF-20`, `RF-36`), autorizar el pago contra las
listas vigentes (`RF-27`), y entregarle el efectivo al receptor contra código, documento y —cuando
el documento no está vigente— desafío (`RF-34`, `RF-85`, `RF-86`, `RF-69`, `RF-64`) son **cinco
momentos distintos**, no uno. Cada control se ancla a uno de ellos, y el punto de no retorno
—el último momento en que detener todavía es no-hacer en vez de deshacer— hay que nombrarlo
explícitamente. Con un punto que puede quedar sin conexión, ese punto de no retorno **se cruza sin
que el centro se entere**: entre el cuarto momento y el quinto puede no haber ninguna señal de
vuelta.

**Qué queda decidido.** Qué control corre en cuál momento; cuál es el punto de no retorno; qué pasa
con un tamizaje posterior a ese punto; y qué ve Rosa mientras su giro está retenido, dado que a
Kevin —la cara de SendIt frente a ella— `RF-40` le **omite el motivo** cuando revelarlo está
prohibido y `RF-39` solo le entrega la acción que corresponde ofrecer, mientras a ella `RF-66` le
muestra que el giro está retenido y hasta qué fecha y `RF-67` le avisa cuando pasa a estarlo (T2).
Esa última no se resuelve redactando mejor un mensaje: hay que decidir qué mecanismo hace que el
hecho y el plazo lleguen sin que el motivo se pueda deducir.

### (f) Dónde vive la respuesta del desafío y quién la compara

**Pregunta.** `RF-68` obliga al emisor a registrar, al crear el giro, una pregunta y su respuesta.
`RF-69` deja cobrar con un documento no vigente a quien la responde correctamente, y `RF-86`
convierte esa respuesta en la única excepción a la vigencia que `RF-85` exige sobre el titular. La
pregunta de diseño no es dónde poner el campo: es **quién tiene la respuesta en las manos y en qué
forma**, cuando `RF-12` prohíbe mostrársela a quien atiende el mostrador y `RNF-17` extiende la
prohibición a quien administra la infraestructura — «El sistema puede comprobar una respuesta sin
poder mostrarla, en los dos lados del mostrador».

**Por qué no es un campo más.** Un campo se guarda y se lee; esto se guarda y **no se puede leer**,
ni por el operario que lo teclea ni por quien tiene acceso al almacenamiento. Eso obliga a decidir
tres cosas que ninguna tabla vacía resuelve sola: con qué transformación entra el dato (y por tanto
qué se pierde para siempre), **dónde corre la comparación** —en el mostrador, que puede estar sin
conexión, o en el centro, que entonces recibe por la línea lo que Elena dijo—, y qué viaja de vuelta
por esa línea, que tiene que ser un veredicto y nunca el valor.

**Y hay un lado que el código de seguimiento no tiene.** El código lo genera el sistema; la
respuesta la elige Rosa, en el mostrador, delante de Kevin, y se la transmite a Elena por el mismo
canal que SendIt no controla. Es un **secreto compartido entre dos personas** que el sistema solo
arbitra: no puede regenerarlo, no puede recordárselo a nadie y no puede aceptar que se adivine —de
ahí `RF-82`, que acota los intentos, y `RF-83`, que la caduca junto con el giro. Contar intentos
fallidos es a su vez un dato sobre el secreto, y hay que decir dónde vive y quién lo ve, sabiendo
que `RF-57` limita al operario a la operación que atiende.

**Qué queda decidido al responderla.** La forma en que se persiste la respuesta y si es reversible;
el lado del mostrador donde ocurre la comparación y qué pasa con `RF-69` cuando ese lado está sin
conexión (es la frontera de (c) otra vez, ahora sobre un secreto en vez de sobre un estado); cuántos
intentos son «acotados» y qué queda del giro al agotarlos; y si la caducidad de `RF-83` borra el
dato o solo lo deja inservible. **Se propaga a** `A` (la entidad que lo guarda y su trato en la
tabla de datos personales) y a `L` (el componente que compara, que es el único que toca el valor).

---

## Resumen de propagación

| Decisión | Se propaga a | Qué queda inválido si se reabre |
|---|---|---|
| (a) Verdad del dinero | `A`, `L` | El modelo de datos completo del giro y del movimiento; el componente que escribe el libro |
| (b) Idempotencia | `A`, `L`, API | La tabla de endpoints; la entidad que persiste la clave |
| (c) Frontera entre el centro y el punto de atención | `A`, `L`, `E` (escalar) | El estado del giro y el que el punto sostiene sin conexión; el componente que sincroniza el punto al reconectar; el tramo en que la divergencia deja de ser manejable a mano |
| (d) Tipo de cambio | `A`, `L` | La entidad de cotización y la cuenta de diferencia de cambio |
| (e) Momento del tamizaje | `A`, `L`, `E` (estimar) | La carga del camino del pago; el orden de los componentes en el diagrama |
| (f) Dónde vive y quién compara la respuesta del desafío | `A`, `L` | La entidad que la guarda y su fila en la tabla de datos personales; el componente que la compara; el flujo de pago con documento no vigente (`RF-69`, `RF-86`) |

---

## Nota sobre las dos clases de iteración

La **iteración del diseño** —el mismo diagrama de componentes, dibujado otra vez y más abierto, que
es la que exige el enunciado ([ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md))— y la
**iteración del EVAL** no son lo mismo y [`ITERACIONES.md`](../ITERACIONES.md) las lleva en tablas
separadas. Este paso alimenta la primera: los servicios que aquí se nombren son las cajas que
[`L`](../L-listar-componentes/README.md) abre en su segunda pasada. Y lo afecta la segunda: un ítem
nuevo en el backlog puede reabrir cualquiera de las seis decisiones de arriba.
