# A — Armar el modelo de datos

> Paso 4 de [R.E.D.A.L.E.](../README.md) · anterior:
> [**D** — Diseñar el servicio](../D-disenar-servicio/README.md) · siguiente:
> [**L** — Listar los componentes](../L-listar-componentes/README.md) · bitácora:
> [`ITERACIONES.md`](../ITERACIONES.md)

**Estado: andamiaje.** No hay campos definidos ni motores elegidos. Las entidades están **nombradas
y sin campos** a propósito: nombrarlas es reconocer que el dominio las tiene; darles campos es
decidir, y eso se hace contra el backlog ya evaluado.

El material pide cuatro cosas: **tablas**, **campos**, **opciones de base de datos** y **otros tipos
de almacenamiento** (archivos, caché, almacenamiento de objetos, sistemas de archivos distribuidos).

---

## Contrato con los pasos vecinos

| | |
|---|---|
| **Consume de D** | El tipo de persistencia por familia de dato, y —sobre todo— las seis decisiones abiertas de `D`. Cuatro de ellas *son* decisiones de modelo de datos disfrazadas de arquitectura: dónde vive la verdad del dinero decide si hay tabla de movimientos; la idempotencia decide si hay entidad de clave de intento; el momento del tamizaje decide qué estados existen; y dónde vive la respuesta del desafío decide si hay entidad para un secreto que nadie puede leer |
| **Consume de E** | El volumen por tipo de dato y los años de retención, que deciden qué entidad puede vivir en una fila y cuál necesita almacenamiento de objetos |
| **Entrega a L** | Las bases de datos del diagrama. En el ejemplo de clase hay **varias `BD`, no una sola**: cada grupo de servicios tiene la suya, y cuál es cuál se decide acá |
| **Queda inválido si D cambia** | La entidad cuyo mecanismo se reeligió. Reabrir (a) borra o crea la tabla de movimientos; reabrir (c) cambia los estados del giro y lo que el punto de atención sostiene sin conexión; reabrir (e) cambia qué se guarda y en qué momento |
| **Queda inválido si E cambia** | La elección de motor que se justificó por volumen, y la política de retención por entidad |

---

## 1. Entidades candidatas

Nombradas, no definidas. Cada una existe porque alguien del conjunto de personas la necesita; una
entidad sin persona que la exija es un huérfano y se borra o se le busca el requerimiento que faltó
en `R`.

| Entidad candidata | Por qué es candidata |
|---|---|
| **Emisor** | Rosa. Entrega el efectivo y tiene que ser identificable contra un documento oficial vigente antes de que el dinero se mueva (`RF-01`, `RF-02`) |
| **Receptor** | Elena. No es un campo del giro: es una persona con identidad propia, que se verifica y que cobra contra código y documento (`RF-34`, `RF-85`). Modelarla como texto dentro del giro hace imposible reconocer que dos giros van a la misma persona, que es justo lo que el tamizaje necesita ver (`RF-26`, `RF-27`) y lo que `RF-58` obliga a contar |
| **Giro** | La operación completa, de extremo a extremo. Su cierre no es «despachado» ni «disponible»: es el momento en que el receptor recibe el dinero (`RF-64`, tensión T6) |
| **Código de seguimiento** | El objeto que este modelo introduce y el anterior no tenía. `RF-11` lo entrega **únicamente al emisor**, y `RNF-15` exige que quede ilegible incluso para quien administra la infraestructura: no es un identificador público del giro, es el secreto que vuelve ejecutable la cancelación (`BR-08`) |
| **Desafío** | La pregunta y la respuesta que `RF-68` obliga al emisor a registrar al crear el giro, y contra las que el receptor cobra cuando su documento no está vigente (`RF-69`, `RF-86`). No es un campo del giro y no puede serlo: `RF-12` prohíbe mostrárselo a quien atiende y `RNF-17` a quien administra el almacenamiento, `RF-82` acota los intentos —que son un dato aparte y sobre el mismo secreto— y `RF-83` lo caduca con el giro |
| **Devolución** | El camino de vuelta del dinero, con estado y plazo propios: nace de la cancelación (`RF-47`), de la retención vencida (`RF-32`) o de la prescripción (`RF-50`); es siempre en efectivo (`RF-71`) y en la moneda que el emisor entregó (`RF-88`); se retira en el punto que el emisor elija (`RF-72`), se le avisa dónde (`RF-14`), incluye la comisión cuando el giro no llegó a pagarse (`RF-74`) y queda disponible hasta la prescripción si nadie la retira (`RF-89`). Un estado más del giro no sostiene un plazo propio ni un punto de retiro distinto del de cobro |
| **Caja del punto de atención** | El efectivo que cada punto declara al abrir y al cerrar (`RF-76`), y que `RF-92` obliga a poner delante del operario antes de habilitarle un pago. Es un saldo por punto y por jornada, no el efectivo del corredor que `RF-20` exige antes de dar un giro por fondeado: dos cifras distintas que hoy nada distingue |
| **Declaración de diferencia del receptor** | La voz de Elena en el mostrador: `RF-90` la deja declarar que el dinero recibido no coincide con el informado. Es un hecho asentado por quien no es usuaria del sistema, contra un monto que `RF-38` declara intocable y una diferencia que `RF-59` atribuye al punto donde se entregó el dinero. Sin entidad, esa declaración solo existe si el operario la escribe — y es sobre él que se declara |
| **Acumulado de cobros del receptor** | `RF-58` cuenta cuántos giros cobró un mismo receptor en la ventana vigente y `RF-93` retiene el giro de quien la superó. Es el espejo del acumulado del emisor, pero sobre una persona que **no es clienta de SendIt** y de la que solo existe lo que el mostrador capturó: el contador decide una retención, así que su identidad tiene que resolverse igual entre giros |
| **Supresión** | La solicitud de `RF-81`: borrar los datos personales de quien los entregó, de nadie más, y salvo los que el registro de actos debe conservar (`RF-55`, `RNF-03`). Es un acto con solicitante, alcance, momento y resultado — y es él mismo un acto que la traza registra. Sin entidad no hay forma de demostrar qué se borró ni de defender por qué algo no |
| **Acumulado del emisor** | `RF-08` rechaza el giro que supere el límite por operación y `RF-09` el que supere el acumulado de la ventana vigente; `RF-10` obliga a contarlos **sobre la identidad del emisor y no sobre el punto de atención**. Un contador que vive dentro de la fila del punto no puede cumplir eso |
| **Segunda autorización** | El acto de un segundo rol, con su identidad y su momento: `RF-13` la exige **antes** de crear un giro sobre el umbral reforzado —y `RF-79` da el giro por creado al registrar la recepción del efectivo, así que la autorización tiene que existir antes de ese instante— y `RF-61` la exige para corregir un giro pagado. `RNF-02` obliga a poder compararla con las demás identidades del mismo giro |
| **Prescripción** | El plazo del giro no cobrado y su terminador: `RF-49` lo deja no pagable, `RF-50` pone el monto a disposición del emisor y `RF-51` avisa antes de que ocurra. Un plazo que nadie hace vencer no vence |
| **Jurisdicción** | Los dos reguladores que tocan un mismo giro: `RF-15` aplica las reglas de los dos, `RF-31` toma el plazo de retención del más estricto y `RF-18` el de conservación del más largo. Sin entidad, esos plazos quedan como constantes globales — que es exactamente lo que `RNF-03` prohíbe al exigir que se calculen por giro |
| **Movimiento contable** | El asiento. Existe si `D`(a) decide que la verdad del dinero es una suma de movimientos y no un campo |
| **Tasa aplicada / cotización** | La promesa de cuánto cobra el receptor en moneda destino. `RF-07` obliga a producirla y fecharla y `RF-06` a no recalcularla nunca: tiene momento de emisión, vencimiento y valor propios, no es un número dentro del giro |
| **Verificación de identidad** | El acto de haber comprobado quién es alguien, con su evidencia, su momento y su resultado. Distinto de la persona verificada |
| **Caso de cumplimiento** | El expediente de cumplimiento: la coincidencia, la evidencia, la decisión, el plazo y su vencimiento |
| **Traza de auditoría** | Quién vio qué, quién decidió qué, cuándo. Crece con las lecturas, no solo con las escrituras |

Faltan por decidir, y hay que decidirlas: si el **punto de atención** es entidad del modelo —con el
efectivo que declara al abrir y al cerrar (`RF-76`, `RF-92`), su estado de conexión y el momento de
su última sincronización— o solo un identificador dentro del giro, sabiendo que `RF-63` deja que el
emisor lo elija y que por tanto tiene que ser listable **antes** de que el giro exista, y que
`RF-91` deja cobrar en otro punto del país destino cuando el elegido no puede pagar —de modo que el
punto no puede ser un campo inmutable del giro—; si el **agente** —el negocio afiliado
dueño del efectivo que se paga, y a quien `RF-24` obliga a liquidarle lo que puso de su caja— es una
entidad distinta del punto que opera; si **el operario** es un usuario con identidad propia o
únicamente un dato en la traza, cuando `RF-54` ata cada acto a la identidad de quien lo ejecutó y
`RF-30` y `RNF-02` obligan a compararla con los demás roles del mismo giro; si la **clave de
idempotencia** es entidad propia (`RF-43`, `RF-44`); y si el **aviso al receptor** se guarda como
prueba de haber avisado, que ahora no depende de una sola exigencia: `RF-25` obliga a avisarle por
llamada o mensaje de texto, `RF-41` a informarle antes de que viaje el monto y si el punto puede
pagarle, y `RF-60` a informarle toda diferencia registrada sobre su giro. El punto corre el software
de SendIt, así que lo que no esté modelado no lo tiene nadie más; pero el efectivo y el local son
del agente, y esa frontera es de `RF-24` y no se puede modelar como si no existiera.

### Campos

Una sección por entidad. Vacías.

| Entidad | Campos | Clave | Relaciones |
|---|---|---|---|
| Emisor | — | — | — |
| Receptor | — | — | — |
| Giro | — | — | — |
| Código de seguimiento | — | — | — |
| Desafío | — | — | — |
| Devolución | — | — | — |
| Caja del punto de atención | — | — | — |
| Declaración de diferencia del receptor | — | — | — |
| Acumulado del emisor | — | — | — |
| Acumulado de cobros del receptor | — | — | — |
| Segunda autorización | — | — | — |
| Prescripción | — | — | — |
| Jurisdicción | — | — | — |
| Movimiento contable | — | — | — |
| Tasa aplicada | — | — | — |
| Verificación de identidad | — | — | — |
| Caso de cumplimiento | — | — | — |
| Supresión | — | — | — |
| Traza de auditoría | — | — | — |

## 2. Elección de motor por entidad

| Entidad | Necesidad dominante | Motor | Por qué | Decisión |
|---|---|---|---|---|
| — | — | — | — | — |

La elección es **por entidad**, no global — el material lo hace así en su ejemplo, con NoSQL para
imágenes y SQL para metadata. El criterio no es la preferencia sino qué garantía necesita cada dato:
integridad transaccional, capacidad de agregar sin bloquear, o volumen barato de solo escritura.

## 3. Otros almacenamientos

| Necesidad | Qué guarda | Opción | Por qué | Decisión |
|---|---|---|---|---|
| Almacenamiento de objetos | Binarios de identidad —la evidencia que `RF-80` obliga a conservar de emisor y receptor—, evidencia adjunta de un caso | — | — | — |
| Caché | — | — | — | — |
| Sistema de archivos distribuido | — | — | — | — |
| Archivos planos / exportación | Reportes a la autoridad de origen (`RF-17`), liquidación con cada agente (`RF-24`) | — | — | — |
| Almacén local del punto de atención | Lo que el mostrador tiene que sostener sin conexión: las autorizaciones ya bajadas, las prohibiciones que `RF-45` le obliga a respetar, los pagos hechos y no informados, el efectivo declarado al abrir y al cerrar (`RF-76`, `RF-92`) y —si la comparación del desafío corre ahí— algo derivado de una respuesta que `RNF-17` prohíbe que sea legible en el local de un tercero | — | — | — |

**Un aviso sobre la caché en este dominio.** Cachear es servir un dato que puede estar viejo. El
monto que Rosa vio, el estado de un giro retenido que `RF-66` le muestra y el resultado de un
tamizaje son exactamente los datos que no toleran estar viejos, y son los que más se consultan. Lo que se cachee y lo que no se
decide aquí y hay que justificarlo por dato, no por capa.

---

## 4. Datos personales y su trato

| Dato | ¿Se guarda? | En claro / cifrado / tokenizado / hash / no se guarda | Quién puede leerlo | Bajo qué condición | Por qué así |
|---|---|---|---|---|---|
| Documento de identidad del emisor | — | — | — | — | — |
| Imagen del documento (`RF-80`) | — | — | — | — | — |
| Documento de identidad del receptor (`RF-85`, `RF-86`) | — | — | — | — | — |
| Código de seguimiento del giro (`RNF-15`) | — | — | — | — | — |
| Pregunta del desafío (`RF-68`) | — | — | — | — | — |
| Respuesta del desafío (`RF-12`, `RNF-17`) | — | — | — | — | — |
| Intentos fallidos del desafío (`RF-82`) | — | — | — | — | — |
| Domicilio | — | — | — | — | — |
| Teléfono de Elena (`RF-25`, `RF-41`, `RF-60`) | — | — | — | — | — |
| Resultado de tamizaje y su coincidencia | — | — | — | — | — |
| Existencia de un reporte a la autoridad | — | — | — | — | — |

**Por qué esto es decisión de modelo de datos y no de infraestructura.** Cifrar el disco protege
contra el robo del disco. No protege contra la consulta legítima que no debía ocurrir — y `RF-57`
limita al operario **a los datos de la operación que está atendiendo**, mientras `RNF-01` exige que
los datos de identidad queden ilegibles para quien administra la infraestructura, `RNF-15` lo mismo
del código de seguimiento, `RNF-17` lo mismo de la respuesta del desafío —y además frente a quien
atiende el mostrador (`RF-12`)— y `RNF-04` que todo
acceso a datos de identidad deje autor, momento y giro. Esas garantías se cumplen decidiendo
dónde vive el dato, detrás de qué referencia, con qué llave y con qué registro de acceso: es la
forma de las tablas, no la configuración del servidor.

Cuatro consecuencias concretas que la tabla tiene que resolver:

- **Sacar el documento y el código de la fila cambia la forma de la entidad.** `RNF-01` exige que
  los datos de identidad queden ilegibles para quien administra la infraestructura, y `RNF-15` lo
  mismo del código de seguimiento. Si cualquiera de los dos se guarda detrás de una referencia —con
  otra llave y otro control de acceso— deja de ser un campo del emisor o del giro y pasa a ser una
  relación con otro almacén: una tabla más y una frontera más. Y el código tiene una exigencia que
  el documento no tiene: `RF-11` lo entrega solo al emisor y `RF-34` obliga a exigirlo para
  autorizar el pago, así que el modelo tiene que permitir **comprobarlo en el mostrador sin poder
  mostrarlo** (`RNF-15`) — comparación sin lectura, que es una forma de tabla y no una regla de
  pantalla.
- **La respuesta del desafío es un secreto compartido, y ahí está el problema de modelado más duro
  de este paso.** `RF-68` obliga al emisor a registrarla al crear el giro y `RF-69` deja cobrar con
  un documento no vigente a quien la responde, que es la única excepción a la vigencia que `RF-86`
  admite: hay que guardarla, no es opcional. Y a la vez `RF-12` prohíbe mostrarla a quien atiende y
  `RNF-17` a quien administra la infraestructura — **en los dos lados del mostrador**. La tensión no
  se resuelve aquí y se enuncia entera: guardar el valor lo hace legible para alguien; no guardarlo
  hace imposible comprobarlo; guardar solo algo derivado de él obliga a decidir qué diferencias de
  escritura cuentan como acierto —la misma pregunta que `RF-84` ya le quitó al operario sobre el
  nombre del titular— y esa decisión, una vez tomada, no se puede revisar sobre un dato que nadie
  puede leer. Se suma que `RF-82` obliga a contar los intentos fallidos: un contador es un dato
  **sobre** el secreto, y decidir dónde vive y quién lo ve es parte de la misma pregunta, con
  `RF-57` acotando al operario a la operación que atiende. Y `RF-83` lo caduca junto con el giro,
  lo que obliga a decir si caducar es borrar o dejar inservible. Colisiona de frente con `RNF-01`,
  `RNF-15` y `RNF-17` porque es el único de los tres secretos que **una persona eligió y otra tiene
  que recordar**: el sistema no puede regenerarlo ni recordárselo a nadie. Es `D`(f), y aquí se
  materializa en si hay entidad propia, con qué llave y con qué control de acceso.
- **Del reporte a la autoridad, lo que se oculta es el motivo, no el hecho.** Ningún ítem declara
  secreta la existencia del reporte; lo que el backlog decide es más fino y hay que modelarlo así.
  Al operario: `RF-39` le entrega **la acción** que corresponde ofrecer ante un rechazo y `RF-40` le
  **omite el motivo** cuando revelarlo está prohibido. Al emisor: `RF-66` le muestra **que** su giro
  está retenido y **hasta qué fecha**, y `RF-67` le avisa cuando pasa a estarlo. Motivo y hecho son
  entonces dos datos con lectores distintos —no una fila que se muestra u oculta entera—, y el
  modelo tiene que permitir servir el segundo sin que el primero se deduzca. `RF-57` acota quién
  llega al motivo y `RNF-04` obliga a que ese acceso quede trazado. Ocultarlo en la interfaz no
  basta (tensión T2).
- **El dato del receptor lo captura el mostrador de un agente, y ahí hay una frontera contable.**
  Elena se identifica ante un punto de atención que corre el software de SendIt, pero el efectivo
  que se le entrega sale de la caja del agente y SendIt se lo liquida después (`RF-24`): sí hay un
  tercero, y la custodia del dato y la del dinero no caen del mismo lado. Eso cierra una cosa y abre
  tres. Cierra: el registro es de SendIt, porque el software lo es. Abre: **qué se le exige a Elena
  lo decide la regla de este lado** —código (`RF-34`), documento del titular designado (`RF-85`) y
  vigencia salvo desafío respondido (`RF-86`, `RF-69`)—, y quien la atiende no puede saltarla aunque
  sepa que es ella, ni decidir por su cuenta si el nombre coincide (`RF-84`)
  —eso es T3, y con `RF-57` limitando lo que ve, tiene todavía menos margen—; **qué queda
  escrito en el equipo del local del agente** mientras el punto opera sin conexión, dónde vive
  mientras tanto y quién puede leerlo después; y **qué parte del asiento es del agente y cuál de
  SendIt**, cuando la liquidación de `RF-24` y la conservación de `RF-18` piden cosas distintas del
  mismo hecho. Qué de ese dato puede ver el emisor no lo decide ningún ítem todavía: ni se lo
  concede ni se lo niega, y eso es un hueco para `R`, no una licencia para este paso.

---

## 5. Qué es inmutable y qué no

No hace falta invocar a nadie: lo exige el backlog y con ítems que se pueden contar. `RF-55` impide
modificar o eliminar el registro de un acto ya ejecutado; `RF-54` ata cada acto a la identidad de
quien lo ejecutó; `RF-33` obliga a que toda liberación de una retención deje registrado su motivo;
`RF-56` obliga a que la corrección de un giro pagado sea un movimiento **nuevo** y `RF-61` a que
lleve la autorización de un segundo rol; y `RNF-03` conserva todo eso inalterable por el plazo más
largo de los dos reguladores del giro, calculado **por giro y no por política global** (`BR-15`,
`RF-18`).

**Un modelo donde todo se actualiza en el sitio no puede darle eso.** Un `UPDATE` no deja rastro del
valor anterior; una fila de estado que pasa de `retenido` a `liberado` no dice quién, cuándo, ni con
qué a la vista — y `RF-54` pide exactamente esas tres cosas. El problema es más agudo de lo que
parece: se decide mirando un dato que **después cambia**, y el backlog lo asume explícitamente al
obligar a contrastar al receptor contra las listas **vigentes al momento de autorizar el pago**
(`RF-27`) y no contra las de la creación (`RF-26`). Guardar un puntero al dato no basta: hay que
guardar el valor que tenía en el momento de decidir.

| Dato | ¿Se actualiza en el sitio o solo se agrega? | Quién lo exige | Decisión |
|---|---|---|---|
| Estado del giro | — | — | — |
| Código de seguimiento | — | — | — |
| Respuesta del desafío y su cuenta de intentos (`RF-82`, `RF-83`) | — | — | — |
| Punto de atención donde se cobra (`RF-63`, `RF-91`) | — | — | — |
| Estado de la devolución y su plazo (`RF-14`, `RF-89`) | — | — | — |
| Efectivo declarado por el punto al abrir y al cerrar (`RF-76`) | — | — | — |
| Declaración de diferencia del receptor (`RF-90`) | — | — | — |
| Movimiento contable | — | — | — |
| Decisión de cumplimiento | — | — | — |
| Evidencia sobre la que se decidió | — | — | — |
| Versión de la lista consultada | — | — | — |
| Cotización emitida | — | — | — |
| Datos de contacto del emisor | — | — | — |

**La pregunta de fondo, planteada y sin responder:** ¿el giro es una fila que cambia de estado, o
una secuencia de hechos de la que el estado se deriva? Las dos formas sostienen la consulta que
`RF-52` y `RF-53` le deben a Rosa. Solo una sostiene una auditoría. Y si conviven —hechos para lo
que se audita, fila mutable para lo que se consulta— hay que decidir cuál manda cuando difieren, que
es la misma pregunta que `D`(a) dejó abierta.

**Y hay un tercer lector que no aparece en el material: el punto de atención que estuvo sin
conexión.** Una fila que cambia de estado no se fusiona con la que el punto trae al reconectar —una
de las dos pisa a la otra y la que pierde desaparece sin dejar rastro, que es lo que `RF-55`
prohíbe—. Una secuencia de hechos sí se fusiona, al precio de admitir que dos hechos contradictorios
sobre el mismo giro convivan en el registro hasta que alguien decida cuál vale — y `RNF-06` no
tolera que esa convivencia sea observable como estado, ni `RNF-08` que resolverla dependa del
operario. Cuál de esos dos precios se paga es `D`(c), y aquí se materializa en la forma de las
tablas.

---

## 6. Retención

Dos obligaciones caen sobre el mismo registro y **ninguna anula a la otra**: el cliente puede exigir
que se borren sus datos, y la regulación obliga a conservar la operación durante años — `RF-18` por
el plazo más largo de los **dos** países que tocaron el giro y `RNF-03` calculado por giro y no por
política global. **Las dos tienen ítem, y la asimetría que esta sección registraba ya no existe:**
`RF-81` suprime a pedido los datos personales de quien los entregó, y le pone dos límites que son
exactamente lo que el modelo tiene que poder ejecutar — **de nadie más**, así que hay que saber cuál
de las dos personas de un giro entregó cada dato, cuando el receptor no es cliente y sus datos los
capturó el mostrador; y **salvo los que el registro de actos debe conservar**, que es la frontera de
`RF-55` y `RNF-03`. Un derecho de supresión con excepción nombrada no se cumple con una política: se
cumple si la fila del dato personal se puede borrar sin arrastrar el asiento, y no se cumple si no.
Lo que sigue abierto no es si la obligación existe, es **quién ejecuta cada plazo** y qué queda en
pie después.

La columna de plazo se apoya en el supuesto ya cerrado del backlog —*conservación = el plazo más
largo de los dos reguladores del giro, con un piso de cinco años*—; si `E` lo reabre, esta tabla se
rehace entera.

| Dato | Plazo de conservación | ¿Se borra a pedido del cliente? | Qué lo obliga | Qué se rompe si se borra |
|---|---|---|---|---|
| Registro del giro | El más largo de los dos reguladores, piso de 5 años | No mientras corra el plazo — es la operación, no el dato personal | `RF-18`, `RNF-03`, `BR-15` | El reporte a la autoridad (`RF-17`) queda sin respaldo y el giro deja de ser demostrable ante cualquiera de los dos reguladores |
| Movimiento contable | El del giro que lo originó | No — `RF-81` lo excluye por vía de `RF-55` | `RF-55`, `RNF-03`, `RNF-07` | La prueba de que la suma cuadra: sin asiento no se demuestra `RNF-07`, y el pasivo de `BR-01` queda sin contrapartida |
| Imagen del documento de identidad (`RF-80`) | El del giro. Es el dato voluminoso y el primer candidato a archivo frío al vencerlo | No mientras corra el plazo; al vencerlo se decide si se borra o se anonimiza — y esa decisión sigue abierta | `RF-80`, `RF-18`, `RNF-01` | La evidencia de que la identificación de `RF-01` y `RF-85` ocurrió. Queda la afirmación de que se verificó, sin nada detrás |
| Pregunta y respuesta del desafío | Caduca con el giro (`RF-83`) — más corto que todo lo demás de esta tabla | Se extingue sola; borrarla antes deja a `RF-69` sin salida | `RF-83`, `RNF-17` | Nada del asiento. Pero si caduca antes de que el receptor llegue, el documento no vigente deja de poder cobrarse y `RF-86` vuelve a cerrar la puerta que `RF-69` abrió |
| Resultado de tamizaje | El del giro | No — sostiene la decisión, no la identidad | `RF-26`, `RF-27`, `RNF-03` | La defensa de por qué se retuvo o se dejó pasar. `RF-27` decide contra listas **vigentes al momento del pago**: sin el valor guardado, esa decisión no se puede reconstruir |
| Caso de cumplimiento | El del giro, con su plazo de retención propio (`RF-31`) vencido adentro | No | `RF-29`, `RF-33`, `RF-87`, `RNF-03` | El motivo de la liberación que `RF-87` obliga a registrar, y con él la trazabilidad de quién dejó salir el dinero |
| Declaración de diferencia del receptor (`RF-90`) | El del giro | No — es un acto, y los actos no se borran | `RF-90`, `RF-59`, `RF-55` | La única versión de los hechos que no escribió el punto al que `RF-59` le atribuye la diferencia |
| Traza de auditoría | El del giro, inalterable (`RNF-03`) | No — es la excepción que `RF-81` nombra | `RF-54`, `RF-55`, `RNF-03`, `RNF-04` | El no repudio entero, y también la prueba de que la supresión pedida se ejecutó |
| Solicitud de supresión y su alcance (`RF-81`) | El del registro de actos | No — es el acto que demuestra el borrado | `RF-81`, `RF-54`, `RF-55` | La capacidad de demostrarle a quien lo pidió qué se borró, y de defender ante el regulador por qué algo no |
| Datos de contacto | Mientras el giro esté vivo y queden avisos pendientes | **Sí — es el caso claro de `RF-81`**, y el que prueba si el modelo sabe borrar sin romper nada | `RF-25`, `RF-41`, `RF-60`, `RF-75`, `RF-81` | Los avisos pendientes se quedan sin destino: la devolución disponible (`RF-14`), el aviso previo a la prescripción (`RF-51`) y el de giro cobrado (`RF-65`). El asiento no se toca |
| Cotizaciones no ejecutadas | Sin giro no hay regulador que las reclame: plazo corto, por decidir | Sí, si quedaron atadas a una persona | `RF-07` | Nada del registro contable — salvo que la cotización sea la que `RF-06` congeló en un giro creado, y entonces ya no es «no ejecutada» |

**Lo que esta tabla decide sin que lo parezca.** Si el nombre y el documento de Rosa viven **dentro**
de la fila del giro, borrar a Rosa destruye el asiento contable y con él la posibilidad de demostrar
que la suma cuadra, que es el invariante de `RNF-07`. Si viven **detrás de una referencia**, se
puede borrar la identidad y dejar en pie la operación. Es decir: **la convivencia entre el derecho
de supresión y la obligación de conservación se resuelve en el diseño de las tablas, y solo ahí.**
Ninguna política escrita en un documento la resuelve si el modelo no la permite — y `RF-81` ya no
deja tratarla como hipótesis: la excepción que nombra («salvo los que el registro de actos debe
conservar») es una frontera entre dos tablas, no una cláusula. Queda abierto, y es de este paso, si
el receptor entra en esa referencia: sus datos los entregó él en el mostrador, así que `RF-81` lo
alcanza, pero de él el modelo tiene además el contador de cobros de `RF-58`, que decide retenciones
sobre giros que no son suyos.

Falta decidir además qué pasa al vencer el plazo: ¿se borra, se anonimiza, se archiva en frío? Y
quién ejecuta ese vencimiento, porque un plazo que nadie hace vencer no vence. Es el mismo mecanismo
que le hace falta a la retención que caduca sin liberarse (`RF-31`, `RF-32`), al giro que prescribe
(`RF-49`, `RF-50`), a la respuesta del desafío que caduca con él (`RF-83`), a la devolución que
nadie retira (`RF-89`) y a la supresión pedida (`RF-81`): seis plazos distintos, un solo ejecutor
por decidir — y `RF-81` es el único de los seis que además tiene que **dejar en pie** una parte del
registro mientras borra la otra.

---

## Qué invalida este modelo

| Si cambia… | Se rehace |
|---|---|
| `D`(a) verdad del dinero | Movimiento contable, estado del giro, y la sección 5 completa |
| `D`(b) idempotencia | La entidad que persiste la clave de intento y su ventana de vida |
| `D`(c) frontera entre el centro y el punto de atención | Los estados del giro, el estado que el punto sostiene sin conexión, y qué se guarda de lo que informa al reconectar |
| `D`(d) tipo de cambio | Tasa aplicada, su vencimiento, y la cuenta de diferencia de cambio |
| `D`(e) momento del tamizaje | Verificación de identidad, caso de cumplimiento, y el orden de los estados |
| `D`(f) dónde vive y quién compara la respuesta del desafío | La entidad **Desafío**, su llave, su control de acceso y su fila en la tabla de datos personales; y qué del secreto sostiene el punto de atención sin conexión |
| Los años de retención en `E` | La sección 6 y la elección de motor de las entidades voluminosas |

---

## Nota sobre las dos clases de iteración

[`ITERACIONES.md`](../ITERACIONES.md) registra dos cosas distintas y no se fusionan: la **iteración
del diseño** —el mismo diagrama de componentes dibujado otra vez y más abierto, que es la que exige
el enunciado ([ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md))— y la **iteración del EVAL**,
que cambia una decisión del backlog. Este paso las alimenta a las dos: las bases de datos que aquí
se decidan son las `BD` que el diagrama dibuja, y un ítem nuevo del backlog puede agregar una
entidad que nadie había nombrado.
