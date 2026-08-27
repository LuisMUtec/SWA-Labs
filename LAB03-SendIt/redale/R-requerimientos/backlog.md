# R — Requerimientos (backlog)

**Formato exigido por el enunciado:** backlog. Solo el título, claro y entendible — no se
describen. Este documento es **la única entrada puntuada por el [EVAL](../../evals/README.md)**.

Cada ítem sigue el formato del [ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md) fijado en
[D-06](../../docs/DECISIONES.md): *el sistema [verbo en futuro] [capacidad] - `<Persona>`*. El
razonamiento que un título no puede cargar vive en [`insumos.md`](insumos.md); las reglas que cada
ítem ejerce, en [`business-rules.md`](../../business-rules.md).

## Usuario modelo

> Hint del enunciado: *identifique correctamente quién es el usuario modelo.*

| Persona | Rol en la remesa | Archivo |
|---|---|---|
| **Rosa Quispe** — *usuario modelo* | Emisora. Entrega el efectivo y designa a quién llega. Es de quien el dinero sigue siendo hasta que alguien lo cobra | [`Rosa.MD`](../../personas/Rosa.MD) |
| Elena Quispe | Receptora en el país destino. **No es clienta de SendIt** | [`Elena.MD`](../../personas/Elena.MD) |
| Kevin Ramos | Operario de la ventanilla del agente. Encarna la seguridad — es el vector, no el guardián | [`Operario.MD`](../../personas/Operario.MD) |

## Preguntas de encuadre

| Pregunta | Respuesta |
|---|---|
| **¿Cuál es el problema?** | Una persona necesita entregar dinero en un país y que otra lo reciba en otro, **sin que ninguna de las dos tenga cuenta bancaria**. Entre la entrega y el cobro el dinero no está con ninguna: está con SendIt, que lo debe (BR-01). Ese intervalo es todo el problema |
| **¿Para quién lo resolvemos?** | Para Rosa, que paga y elige el servicio. Elena y Kevin existen porque sin ellos su operación no cierra |
| **¿Cuáles son las limitaciones?** | Las dos del enunciado: **seguridad**, porque el efectivo se entrega a un desconocido en una ventanilla ajena, y **consistencia de datos**, porque un giro pagado dos veces es dinero perdido, no un registro sucio. A eso se suma que el negocio es transfronterizo y por tanto **multirregulador** |

---

## Funcionales

### Creación del giro

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-01 | el sistema identificará al emisor contra un documento oficial vigente antes de crear un giro - Rosa | Rosa | BR-03 | P0 |
| RF-02 | el sistema entregará al receptor su dinero en efectivo, sin exigirle cuenta bancaria - Elena | Elena | BR-09 | P0 |
| RF-79 | el sistema dará el giro por creado en el momento en que registra la recepción del efectivo - Kevin | Kevin | BR-03 | P0 |
| RF-03 | el sistema exigirá un único receptor designado por giro - Rosa | Rosa | BR-02 | P0 |
| RF-04 | el sistema exigirá un único país destino por giro - Rosa | Rosa | BR-02 | P0 |
| RF-63 | el sistema permitirá al emisor elegir el punto de atención donde cobrará el receptor, entre los disponibles en el país destino - Rosa | Rosa | BR-11 | P0 |
| RF-05 | el sistema informará al emisor el monto exacto en moneda destino antes de que entregue el efectivo - Rosa | Rosa | BR-07 | P0 |
| RF-06 | el sistema conservará ese monto sin recalcularlo durante toda la vida del giro - Rosa | Rosa | BR-07 | P0 |
| RF-07 | el sistema producirá y fechará la cotización de la que sale ese monto - Rosa | Rosa | BR-07 | P0 |
| RF-08 | el sistema rechazará, antes de registrar la recepción del efectivo, el giro que haga al emisor superar su límite por operación - Rosa | Rosa | BR-04 | P0 |
| RF-09 | el sistema rechazará, antes de registrar la recepción del efectivo, el giro que haga al emisor superar su acumulado en la ventana vigente - Rosa | Rosa | BR-04 | P0 |
| RF-10 | el sistema contará esos límites sobre la identidad del emisor y no sobre el punto de atención - Kevin | Kevin | BR-04 | P0 |
| RF-11 | el sistema entregará el código de seguimiento del giro únicamente al emisor - Rosa | Rosa | BR-08 | P0 |
| RF-94 | el sistema volverá a entregar el código únicamente al emisor que lo perdió, tras identificarlo de nuevo - Rosa | Rosa | BR-08 | P1 |
| RF-12 | el sistema comprobará la respuesta del desafío sin mostrarla a quien atiende el mostrador - Kevin | Kevin | BR-08 | P0 |
| RF-13 | el sistema exigirá, antes de registrar la recepción del efectivo, la autorización de un segundo rol para un giro sobre el umbral reforzado - Kevin | Kevin | BR-05 | P0 |
| RF-14 | el sistema avisará al emisor que su devolución está disponible y en qué punto retirarla - Rosa | Rosa | BR-12 | P0 |

### La frontera

Este bloque existe por una sola razón: **el giro cruza un país.** Si dejara de cruzarlo, **ninguno
de sus ítems tendría sentido** — y esa prueba se corre cada ronda, no se declara. La
[iteración 01](../../evals/iterations/2026-08-26-01.md) mostró que un backlog sin este bloque
describe un transmisor de dinero doméstico con un campo de moneda; la
[03](../../evals/iterations/2026-08-26-03.md) encontró que dos de sus ítems **sobrevivían a una red
doméstica** y estaban archivados bajo el rasgo equivocado: la liquidación con el agente pertenece al
efectivo y el aviso al receptor pertenece al canal. Los dos se mudaron a **Pago**.

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-15 | el sistema aplicará a un mismo giro las reglas del regulador de origen y las del regulador de destino - Kevin | Kevin | BR-17 | P0 |
| RF-16 | el sistema rechazará el giro cuando los dos reguladores impongan condiciones incompatibles, en vez de elegir una - Kevin | Kevin | BR-17 | P0 |
| RF-17 | el sistema reportará a la autoridad de origen el giro que supere su umbral de reporte transfronterizo - Kevin | Kevin | BR-06 | P0 |
| RF-18 | el sistema conservará el registro de un giro por el plazo más largo de los dos países que lo tocaron - Kevin | Kevin | BR-15 | P1 |
| RF-19 | el sistema informará al emisor que un país destino no puede atenderse antes de que entregue el efectivo - Rosa | Rosa | BR-15 | P0 |
| RF-20 | el sistema exigirá efectivo disponible en el corredor de destino antes de dar un giro por fondeado - Kevin | Kevin | BR-11 | P0 |
| RF-21 | el sistema informará al emisor en qué moneda cobrará el receptor, con su nombre y no solo su cifra - Rosa | Rosa | BR-07 | P1 |
| RF-22 | el sistema aplicará el umbral de reporte de cada país sobre el giro completo y no sobre su tramo local - Kevin | Kevin | BR-06 | P0 |
| RF-23 | el sistema impedirá que un giro rechazado por el regulador de destino se cree en el de origen - Kevin | Kevin | BR-17 | P2 |

### Cumplimiento

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-26 | el sistema contrastará a emisor y receptor contra las listas de sanciones antes de aceptar el efectivo - Kevin | Kevin | BR-06 | P0 |
| RF-27 | el sistema contrastará al receptor contra las listas vigentes al momento de autorizar el pago - Kevin | Kevin | BR-06 | P0 |
| RF-97 | el sistema volverá a tamizar los giros aún no pagados cuando cambia una lista de sanciones - Kevin | Kevin | BR-06 | P1 |
| RF-28 | el sistema separará una coincidencia exacta de sanciones de una coincidencia por homonimia - Kevin | Kevin | BR-06 | P0 |
| RF-78 | el sistema resolverá la coincidencia por homonimia en un plazo más corto que la coincidencia exacta - Kevin | Kevin | BR-06 | P1 |
| RF-29 | el sistema dejará retenido el giro con coincidencia de sanciones, ni pagable ni cancelable - Kevin | Kevin | BR-06 | P0 |
| RF-30 | el sistema derivará el giro retenido a un rol distinto del operario que lo atendió - Kevin | Kevin | BR-06 | P0 |
| RF-31 | el sistema exigirá que toda retención lleve el plazo del regulador más estricto de los dos países del giro - Kevin | Kevin | BR-06 | P0 |
| RF-32 | el sistema devolverá al emisor el monto del giro cuya retención venció sin haber sido liberada - Kevin | Kevin | BR-06 | P0 |
| RF-71 | el sistema devolverá siempre en efectivo - Rosa | Rosa | BR-12 | P0 |
| RF-88 | el sistema devolverá siempre en la moneda que el emisor entregó - Rosa | Rosa | BR-12 | P0 |
| RF-72 | el sistema devolverá en el punto de atención que el emisor elija - Rosa | Rosa | BR-12 | P0 |
| RF-73 | el sistema informará al emisor el plazo de una eventual devolución antes de que entregue el efectivo - Rosa | Rosa | BR-12 | P0 |
| RF-96 | el sistema informará al emisor cuánto puede durar como máximo una revisión, antes de que entregue el efectivo - Rosa | Rosa | BR-06 | P0 |
| RF-89 | el sistema mantendrá disponible la devolución no retirada hasta el plazo de prescripción del giro - Rosa | Rosa | BR-12 | P2 |
| RF-74 | el sistema devolverá también la comisión cobrada cuando el giro no llegó a pagarse - Rosa | Rosa | BR-12 | P0 |
| RF-33 | el sistema permitirá liberar un giro retenido únicamente al rol de cumplimiento - Kevin | Kevin | BR-06 | P0 |
| RF-87 | el sistema registrará el motivo de cada liberación de un giro retenido - Kevin | Kevin | BR-06 | P1 |
| RF-58 | el sistema contará cuántos giros cobró un mismo receptor en la ventana vigente - Kevin | Kevin | BR-04 | P0 |
| RF-93 | el sistema retendrá el giro cuyo receptor superó su acumulado de cobros de la ventana - Kevin | Kevin | BR-04 | P0 |

### Pago

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-34 | el sistema exigirá el código del giro para autorizar un pago - Elena | Elena | BR-09 | P0 |
| RF-85 | el sistema exigirá un documento de identidad cuyo titular coincida con el receptor designado - Elena | Elena | BR-09 | P0 |
| RF-86 | el sistema exigirá que el documento del receptor esté vigente - Elena | Elena | BR-09 | P0 |
| RF-68 | el sistema exigirá al emisor registrar al crear el giro una pregunta y su respuesta - Rosa | Rosa | BR-09 | P0 |
| RF-101 | el sistema no transmitirá al receptor la respuesta del desafío por ningún canal propio - Rosa | Rosa | BR-08 | P0 |
| RF-102 | el sistema impedirá que el punto de atención cobre al receptor por recibir su dinero - Elena | Elena | BR-01 | P0 |
| RF-69 | el sistema ofrecerá el desafío como vía de cobro a quien no tiene documento vigente - Elena | Elena | BR-09 | P0 |
| RF-82 | el sistema limitará a un número acotado los intentos de responder el desafío, y devolverá al emisor el giro cuyos intentos se agotaron - Kevin | Kevin | BR-09 | P0 |
| RF-83 | el sistema caducará la respuesta del desafío junto con el giro que la lleva - Kevin | Kevin | BR-09 | P0 |
| RF-84 | el sistema decidirá qué diferencias de escritura cuentan como coincidencia de titular, y no el operario - Kevin | Kevin | BR-09 | P0 |
| RF-35 | el sistema rechazará todo intento de pago sobre un giro ya pagado, en cualquier punto de la red - Elena | Elena | BR-10 | P0 |
| RF-36 | el sistema no habilitará el pago de un giro cuyos fondos de origen no estén confirmados - Kevin | Kevin | BR-11 | P0 |
| RF-24 | el sistema liquidará con el agente el efectivo que puso de su caja, en el plazo acordado con él - Kevin | Kevin | BR-01 | P0 |
| RF-37 | el sistema avisará al receptor por llamada o mensaje de texto si su giro quedó retenido - Elena | Elena | BR-06 | P0 |
| RF-38 | el sistema impedirá entregar al receptor un monto distinto del fijado al crear el giro - Elena | Elena | BR-13 | P0 |
| RF-59 | el sistema responderá ante el emisor y el receptor por toda diferencia entre el monto fijado y el entregado, y la resolverá con el agente por separado - Elena | Elena | BR-13 | P0 |
| RF-60 | el sistema informará al emisor y al receptor, cada uno por su canal, toda diferencia registrada sobre el giro - Elena | Elena | BR-13 | P1 |
| RF-90 | el sistema permitirá al receptor declarar por llamada o mensaje de texto que el dinero recibido no coincide con el informado - Elena | Elena | BR-13 | P0 |
| RF-91 | el sistema ofrecerá al emisor otro punto de atención cercano al elegido cuando ese no puede pagar, y no lo cambiará sin su respuesta - Rosa | Rosa | BR-11 | P0 |
| RF-39 | el sistema no dejará ningún giro rechazado ni retenido sin una salida que el operario pueda ofrecer en el mostrador - Kevin | Kevin | BR-16 | P0 |
| RF-40 | el sistema omitirá al operario el motivo de un rechazo cuando revelarlo esté prohibido - Kevin | Kevin | BR-16 | P0 |
| RF-25 | el sistema avisará al receptor que hay un giro a su nombre por llamada o mensaje de texto - Elena | Elena | BR-11 | P0 |
| RF-41 | el sistema informará al receptor por llamada o mensaje de texto, antes de que viaje, el monto que cobrará - Elena | Elena | BR-11 | P0 |
| RF-75 | el sistema informará al receptor por llamada o mensaje de texto, antes de que viaje, si el punto elegido puede pagarle hoy - Elena | Elena | BR-11 | P0 |
| RF-76 | el sistema registrará el efectivo que cada punto de atención declara al abrir y al cerrar su caja - Kevin | Kevin | BR-11 | P0 |
| RF-92 | el sistema informará al operario el efectivo disponible en su punto antes de habilitarle un pago - Kevin | Kevin | BR-11 | P0 |
| RF-95 | el sistema descontará del efectivo del punto cada pago que autoriza, sin esperar al cierre de caja - Kevin | Kevin | BR-11 | P0 |
| RF-77 | el sistema informará al emisor la fecha desde la cual el giro estará disponible para cobro, antes de que entregue el efectivo - Rosa | Rosa | BR-11 | P0 |

### Interrupción y consistencia

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-42 | el sistema dejará el giro, ante una interrupción, en un estado único que el operario puede leer y retomar - Kevin | Kevin | BR-10 | P0 |
| RF-43 | el sistema tratará todo reintento de una creación interrumpida como la misma operación - Kevin | Kevin | BR-10 | P0 |
| RF-44 | el sistema tratará todo reintento de un pago interrumpido como la misma operación - Kevin | Kevin | BR-10 | P0 |
| RF-45 | el sistema impedirá que un punto sin conexión pague un giro que el centro ya retuvo, canceló o dio por pagado en otro punto - Kevin | Kevin | BR-10 | P0 |
| RF-100 | el sistema acotará por monto y por antigüedad lo que un punto sin conexión puede pagar - Kevin | Kevin | BR-10 | P0 |

### Cancelación y prescripción

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-46 | el sistema permitirá al emisor cancelar su giro mientras el dinero no esté a disposición del receptor - Rosa | Rosa | BR-12 | P0 |
| RF-47 | el sistema devolverá al emisor el monto entregado al cancelar - Rosa | Rosa | BR-12 | P0 |
| RF-48 | el sistema admitirá la cancelación de un giro únicamente del emisor que lo creó - Rosa | Rosa | BR-12 | P0 |
| RF-62 | el sistema rechazará todo intento de pago sobre un giro ya cancelado y devuelto al emisor - Elena | Elena | BR-12 | P0 |
| RF-49 | el sistema dejará no pagable el giro cuyo plazo de prescripción venció - Rosa | Rosa | BR-14 | P0 |
| RF-50 | el sistema devolverá al emisor el monto del giro prescrito - Rosa | Rosa | BR-14 | P0 |
| RF-51 | el sistema avisará al emisor antes de que su giro prescriba - Rosa | Rosa | BR-14 | P1 |

### Consulta

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-52 | el sistema permitirá al emisor consultar el estado de sus giros sin depender del receptor - Rosa | Rosa | BR-01 | P0 |
| RF-53 | el sistema distinguirá al emisor el giro disponible para cobro del que todavía no lo está - Rosa | Rosa | BR-01 | P0 |
| RF-64 | el sistema dará el giro por cerrado en el momento en que el receptor recibe el dinero - Elena | Elena | BR-10 | P0 |
| RF-65 | el sistema avisará al emisor que su giro fue cobrado - Rosa | Rosa | BR-01 | P0 |
| RF-66 | el sistema mostrará al emisor que su giro está retenido y hasta qué fecha - Rosa | Rosa | BR-06 | P0 |
| RF-67 | el sistema avisará al emisor cuando su giro pase a estar retenido - Rosa | Rosa | BR-06 | P0 |

### Registro y privilegio

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-54 | el sistema asociará cada acto sobre un giro a la identidad de quien lo ejecutó - Kevin | Kevin | BR-15 | P0 |
| RF-55 | el sistema impedirá modificar o eliminar el registro de un acto ya ejecutado - Kevin | Kevin | BR-15 | P0 |
| RF-56 | el sistema registrará la corrección del **monto** de un giro pagado como un movimiento nuevo - Kevin | Kevin | BR-13 | P1 |
| RF-70 | el sistema impedirá alterar el receptor designado de un giro después de creado - Rosa | Rosa | BR-09 | P0 |
| RF-61 | el sistema exigirá la autorización de un segundo rol para corregir el monto de un giro pagado - Kevin | Kevin | BR-13 | P0 |
| RF-57 | el sistema limitará lo que el operario ve a los datos de la operación que está atendiendo, excluida la respuesta del desafío - Kevin | Kevin | BR-16 | P0 |
| RF-80 | el sistema conservará la evidencia de la identificación del emisor y del receptor de cada giro - Kevin | Kevin | BR-15 | P0 |
| RF-98 | el sistema conservará constancia de cada aviso que envió por el canal del receptor - Elena | Elena | BR-15 | P1 |
| RF-99 | el sistema descartará la evidencia de identificación de un emisor que no llegó a crear un giro - Kevin | Kevin | BR-15 | P1 |
| RF-81 | el sistema suprimirá a pedido los datos personales de quien los entregó, y de nadie más - Rosa | Rosa | BR-15 | P2 |

---

## No funcionales

El enunciado nombra dos como críticos —**seguridad** y **consistencia de datos**— y no da ninguna
cifra. Para la consistencia la medida correcta no es un número sino un **invariante**: algo que
nunca puede ser falso, y que por lo tanto se comprueba en cualquier momento.

### Seguridad

| ID | Título | Medida | Regla | Prioridad |
|---|---|---|---|---|
| RNF-01 | el sistema mantendrá ilegibles los datos de identidad para quien administre la infraestructura | Nadie que tenga acceso al almacenamiento reconstruye un documento de identidad | BR-08, BR-16 | P0 |
| RNF-15 | el sistema mantendrá ilegible el código de seguimiento para quien administre la infraestructura | El sistema puede comprobar un código sin poder mostrarlo | BR-08 | P0 |
| RNF-17 | el sistema mantendrá ilegible la respuesta del desafío para quien administre la infraestructura | El sistema puede comprobar una respuesta sin poder mostrarla | BR-08 | P0 |
| RNF-02 | el sistema impedirá que una misma identidad ejerza dos roles de un mismo giro | Ninguna identidad aparece dos veces en la cadena crear → autorizar → pagar → liberar → corregir de un mismo giro | BR-05 | P0 |
| RNF-03 | el sistema conservará inalterable el registro de actos | Ningún acto registrado se modifica ni se borra, cualquiera sea quien lo pida — y esa conservación prevalece sobre toda supresión | BR-15 | P0 |
| RNF-04 | el sistema dejará traza de todo acceso a datos de identidad | Todo acceso tiene autor, momento y giro; ninguno es anónimo | BR-16 | P1 |

### Consistencia de datos

| ID | Título | Invariante | Regla | Prioridad |
|---|---|---|---|---|
| RNF-05 | el sistema impedirá que un giro quede pagado dos veces | Ningún giro registra dos entregas al receptor, en ningún punto y en ningún momento | BR-10, BR-11 | P0 |
| RNF-16 | el sistema impedirá que un giro quede pagado con un monto distinto del que se le informó al emisor | Ninguna entrega registrada difiere de la cifra que el emisor vio antes de entregar su efectivo | BR-07, BR-13 | P0 |
| RNF-06 | el sistema mantendrá un solo estado del giro entre el centro y el punto de atención | Dos lugares del sistema nunca afirman a la vez que un giro está retenido y disponible para cobro | BR-10 | P0 |
| RNF-13 | el sistema impedirá que un giro quede devuelto y cobrado a la vez | Ningún giro figura simultáneamente devuelto al emisor y entregado al receptor, en ningún punto y en ningún momento | BR-12 | P0 |
| RNF-07 | el sistema conservará la suma del dinero en toda operación | Lo que sale de una cuenta entra en otra; ningún movimiento deja el total distinto | BR-01 | P0 |
| RNF-08 | el sistema recuperará el estado de los giros de un punto caído sin intervención del operario | Un punto que vuelve no necesita que nadie le diga qué pasó mientras no estaba | BR-10 | P1 |

### Servicio

| ID | Título | Medida | Prioridad |
|---|---|---|---|
| RNF-09 | el sistema resolverá en un tiempo acotado todo lo que no dependa de una persona ni de un sistema ajenos | `[ASSUMPTION: menos de 3 minutos]` desde que alguien llega al mostrador, incluida la verificación del documento. Una espera por un segundo rol o por una lista externa se mide aparte, y su suma no se descuenta de este techo | P1 |
| RNF-10 | el sistema dejará un giro fondeado disponible para cobro en el destino en un tiempo acotado | `[ASSUMPTION: menos de 15 minutos]` desde su creación | P0 |
| RNF-11 | el sistema sostendrá la capacidad de crear y de pagar giros | `[ASSUMPTION: 99,9 % mensual]`, medida sobre crear y pagar, no sobre consultar | P1 |
| RNF-12 | el sistema operará con más de un país de origen desde el primer día | Ninguna cifra ni regla del sistema supone un solo país de origen. Los corredores concretos los fija el supuesto único de la tabla de abajo | P0 |
| RNF-14 | el sistema operará con más de una moneda destino desde el primer día | Ninguna cifra del sistema supone una sola moneda de destino | P0 |

---

## Las seis tensiones, y dónde quedan decididas

| Tensión | Entre | Cómo se decide | Ítem |
|---|---|---|---|
| **T1** Control ↔ rapidez | Rosa ↔ Kevin | **A favor del control, con precio acotado.** El tamizaje corre *antes* de aceptar el efectivo, de modo que se detiene en vez de revertir; a cambio, toda retención nace con plazo y se resuelve sola al vencerlo | RF-26 · RF-31 · RF-32 |
| **T2** Explicación ↔ reserva | Rosa ↔ Kevin | **Se decide en la altitud correcta, y en los dos mostradores.** Cuando revelar el motivo está prohibido, el operario recibe **la acción y no el motivo** — atiende sin saber y sin poder deducir. Y del lado de Rosa: ve **que** está retenido y **hasta cuándo**, nunca por qué | RF-39 · RF-40 · RF-66 · RF-67 |
| **T3** Identidad del receptor | Elena ↔ Kevin | **Se parte, como T5.** La regla dura queda: el documento tiene que estar **vigente** (RF-86), y **qué cuenta como coincidencia lo decide el sistema, no el operario** (RF-84). Pero la tensión *era* el documento vencido, y ahora tiene salida: el emisor registra un desafío al crear el giro (RF-68) y el receptor cobra respondiéndolo (RF-69), con intentos acotados y devolución al agotarlos (RF-82), caducidad (RF-83), y **la respuesta comprobada sin mostrarse a nadie** (RF-12, RF-57, RNF-17). Elena no queda fuera, y nadie cobra sin ser verificado | RF-86 · RF-84 · RF-68 · RF-69 · RF-82 · RF-12 · RNF-17 |
| **T4** Certeza del monto ↔ exposición cambiaria | Rosa ↔ la empresa | **A favor de Rosa.** El monto de destino se fija al crear el giro y no se recalcula nunca, con una cotización que el sistema produce y fecha. La empresa carga el movimiento | RF-05 · RF-06 · RF-07 |
| **T5** El canal de Rosa ↔ el de Elena | Rosa ↔ Elena | **Se parte en dos, que es lo que la iteración 02 mostró que faltaba.** El **código** es un secreto: solo Rosa lo transmite, y eso hace ejecutable la cancelación. El **aviso** no lo es: llega a Elena por llamada o mensaje de texto, sin exigirle pantalla. Fusionar las dos cosas dejaba su flujo sin arrancar | RF-11 · RF-25 · RF-41 · RF-75 |
| **T6** Cerrar ↔ cerrar de verdad | Rosa ↔ Elena | **A favor de Elena, ahora con ítem que lo diga.** El giro cierra en el momento en que el receptor recibe el dinero, no al fondearse ni al quedar disponible. Y el límite de la cancelación se corre para que Rosa no pueda anular con Elena en la ventanilla: no es «mientras no esté pagado» sino **mientras el dinero no esté a disposición del receptor** | RF-64 · RF-65 · RF-46 |

## Reparto de prioridad

| | P0 | P1 | P2 |
|---|---|---|---|
| Funcionales | 88 | 11 | 3 |
| No funcionales | 13 | 4 | 0 |

## Supuestos y ambigüedades

| Marca | Dónde | Estado |
|---|---|---|
| `[ASSUMPTION: modelo Western Union — red de agentes, efectivo contra efectivo, sin cuenta bancaria en ninguna punta]` | Todo el backlog | Vigente — indicación del profesor |
| `[ASSUMPTION: umbral de límites (BR-04) y umbral reforzado (BR-05)]` | RF-08 · RF-09 · RF-13 | Vigente |
| `[ASSUMPTION: umbrales de servicio de RNF-09 a RNF-11]` | RNF-09 · RNF-10 · RNF-11 | Vigente — los consume el paso `E` |
| `[ASSUMPTION: el plazo de prescripción es el que fije el regulador del país de origen; a falta de norma expresa, 12 meses desde la creación]` | RF-49 · RF-50 · RF-51 · BR-14 | **Cerrada** — alineada con BR-14, que lo fija por jurisdicción |
| `[ASSUMPTION: la conservación es el plazo más largo de los dos reguladores del giro, con un piso de 5 años]` | RNF-03 · RF-18 | **Cerrada** en la iteración 03 — el paso `E` ya puede dimensionar |
| `[ASSUMPTION: dos corredores al lanzamiento — Estados Unidos → Perú y Estados Unidos → México]` | RNF-12 · RNF-14 | **Cerrada** — dos monedas destino, para no romper RNF-14 |
| `[ASSUMPTION: la retención dura lo que fije el regulador más estricto de los dos países; a falta de norma expresa, 72 horas]` | RF-31 · RF-32 | **Cerrada** — sin techo global, para no contradecir a RF-31 |
