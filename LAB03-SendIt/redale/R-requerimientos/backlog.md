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
| RF-02 | el sistema rechazará registrar la recepción del efectivo antes de identificar al emisor - Kevin | Kevin | BR-03 | P0 |
| RF-03 | el sistema exigirá un único receptor designado por giro - Rosa | Rosa | BR-02 | P0 |
| RF-04 | el sistema exigirá un único país destino por giro - Rosa | Rosa | BR-02 | P0 |
| RF-05 | el sistema informará al emisor el monto exacto en moneda destino antes de que entregue el efectivo - Rosa | Rosa | BR-07 | P0 |
| RF-06 | el sistema conservará ese monto sin recalcularlo durante toda la vida del giro - Rosa | Rosa | BR-07 | P0 |
| RF-07 | el sistema producirá y fechará la cotización de la que sale ese monto - Rosa | Rosa | BR-07 | P0 |
| RF-08 | el sistema rechazará el giro que haga al emisor superar su límite por operación - Rosa | Rosa | BR-04 | P0 |
| RF-09 | el sistema rechazará el giro que haga al emisor superar su acumulado en la ventana vigente - Rosa | Rosa | BR-04 | P0 |
| RF-10 | el sistema contará esos límites sobre la identidad del emisor y no sobre el punto de atención - Kevin | Kevin | BR-04 | P0 |
| RF-11 | el sistema entregará el código de seguimiento del giro únicamente al emisor - Rosa | Rosa | BR-08 | P0 |
| RF-12 | el sistema no transmitirá el código al receptor por ningún canal propio - Rosa | Rosa | BR-08 | P0 |
| RF-13 | el sistema exigirá la autorización de un segundo rol antes de crear un giro sobre el umbral reforzado - Kevin | Kevin | BR-05 | P0 |
| RF-14 | el sistema no habilitará la recepción del efectivo mientras esa autorización no exista - Kevin | Kevin | BR-05 | P0 |

### La frontera

Este bloque existe por una sola razón: **el envío cruza un país.** Si dejara de cruzarlo, ninguno de
estos once ítems tendría sentido. La [iteración 01 del EVAL](../../evals/iterations/2026-08-26-01.md)
mostró que un backlog sin este bloque describe un transmisor de dinero doméstico con un campo de
moneda.

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-15 | el sistema aplicará a un mismo giro las reglas del regulador de origen y las del regulador de destino - Kevin | Kevin | BR-02 | P0 |
| RF-16 | el sistema rechazará el giro cuando los dos reguladores impongan condiciones incompatibles, en vez de elegir una - Kevin | Kevin | BR-02 | P0 |
| RF-17 | el sistema reportará a la autoridad de origen el giro que supere su umbral de reporte transfronterizo - Kevin | Kevin | BR-06 | P0 |
| RF-18 | el sistema conservará el registro de un giro por el plazo más largo de los dos países que lo tocaron - Kevin | Kevin | BR-15 | P1 |
| RF-19 | el sistema informará al emisor que un país destino no puede atenderse antes de que entregue el efectivo - Rosa | Rosa | BR-02 | P0 |
| RF-20 | el sistema exigirá efectivo disponible en el corredor de destino antes de dar un giro por fondeado - Kevin | Kevin | BR-11 | P0 |
| RF-21 | el sistema informará al emisor en qué moneda cobrará el receptor, con su nombre y no solo su cifra - Rosa | Rosa | BR-07 | P1 |
| RF-22 | el sistema aplicará el umbral de reporte de cada país sobre el giro completo y no sobre su tramo local - Kevin | Kevin | BR-06 | P0 |
| RF-23 | el sistema impedirá que un giro rechazado por el regulador de destino se cree en el de origen - Kevin | Kevin | BR-02 | P0 |
| RF-24 | el sistema contará el acumulado del emisor sumando los corredores, no por corredor - Kevin | Kevin | BR-04 | P0 |
| RF-25 | el sistema conservará el horario de atención del destino como condición de disponibilidad del giro - Elena | Elena | BR-11 | P1 |

### Cumplimiento

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-26 | el sistema contrastará a emisor y receptor contra las listas de sanciones antes de aceptar el efectivo - Kevin | Kevin | BR-06 | P0 |
| RF-27 | el sistema contrastará al receptor contra las listas vigentes al momento de autorizar el pago - Kevin | Kevin | BR-06 | P0 |
| RF-28 | el sistema separará una coincidencia exacta de sanciones de una coincidencia por homonimia - Kevin | Kevin | BR-06 | P0 |
| RF-29 | el sistema dejará retenido el giro con coincidencia de sanciones, ni pagable ni cancelable - Kevin | Kevin | BR-06 | P0 |
| RF-30 | el sistema derivará el giro retenido a un rol distinto del operario que lo atendió - Kevin | Kevin | BR-06 | P0 |
| RF-31 | el sistema exigirá que toda retención lleve un plazo desde que empieza - Kevin | Kevin | BR-06 | P0 |
| RF-32 | el sistema resolverá por sí solo la retención cuyo plazo venció - Kevin | Kevin | BR-06 | P0 |
| RF-33 | el sistema permitirá liberar un giro retenido dejando registrado el motivo - Kevin | Kevin | BR-06 | P0 |

### Pago

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-34 | el sistema autorizará el pago solo contra el código del giro y un documento que coincida con el receptor designado - Elena | Elena | BR-09 | P0 |
| RF-35 | el sistema rechazará todo intento de pago sobre un giro ya pagado, en cualquier punto de la red - Elena | Elena | BR-10 | P0 |
| RF-36 | el sistema no habilitará el pago de un giro cuyos fondos de origen no estén confirmados - Kevin | Kevin | BR-11 | P0 |
| RF-37 | el sistema entregará al receptor el monto en moneda destino fijado al crearse el giro - Elena | Elena | BR-07 | P0 |
| RF-38 | el sistema registrará la diferencia cuando el monto entregado no coincida con el fijado - Elena | Elena | BR-13 | P0 |
| RF-39 | el sistema entregará al operario la acción que corresponde ofrecer ante un rechazo - Kevin | Kevin | BR-16 | P0 |
| RF-40 | el sistema omitirá al operario el motivo de un rechazo cuando revelarlo esté prohibido, sin omitirle la acción - Kevin | Kevin | BR-16 | P0 |
| RF-41 | el sistema informará al receptor si el punto de atención puede pagarle antes de que viaje - Elena | Elena | BR-11 | P0 |

### Interrupción y consistencia

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-42 | el sistema dejará el giro en un estado único y legible ante una interrupción - Kevin | Kevin | BR-10 | P0 |
| RF-43 | el sistema tratará todo reintento de una creación interrumpida como la misma operación - Kevin | Kevin | BR-10 | P0 |
| RF-44 | el sistema tratará todo reintento de un pago interrumpido como la misma operación - Kevin | Kevin | BR-10 | P0 |
| RF-45 | el sistema impedirá que un punto sin conexión pague un giro que el centro ya retuvo - Kevin | Kevin | BR-10 | P0 |

### Cancelación y prescripción

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-46 | el sistema permitirá al emisor cancelar su giro mientras no esté pagado - Rosa | Rosa | BR-12 | P0 |
| RF-47 | el sistema devolverá al emisor el monto entregado al cancelar - Rosa | Rosa | BR-12 | P0 |
| RF-48 | el sistema rechazará toda cancelación pedida por el receptor - Elena | Elena | BR-12 | P0 |
| RF-49 | el sistema dejará no pagable el giro cuyo plazo de prescripción venció - Rosa | Rosa | BR-14 | P1 |
| RF-50 | el sistema pondrá a disposición del emisor el monto del giro prescrito - Rosa | Rosa | BR-14 | P1 |
| RF-51 | el sistema avisará al emisor antes de que su giro prescriba - Rosa | Rosa | BR-14 | P1 |

### Consulta

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-52 | el sistema permitirá al emisor consultar el estado de sus giros sin depender del receptor - Rosa | Rosa | BR-01 | P0 |
| RF-53 | el sistema distinguirá al emisor el giro disponible para cobro del que todavía no lo está - Rosa | Rosa | BR-01 | P0 |

### Registro y privilegio

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-54 | el sistema asociará cada acto sobre un giro a la identidad de quien lo ejecutó - Kevin | Kevin | BR-15 | P0 |
| RF-55 | el sistema impedirá modificar o eliminar el registro de un acto ya ejecutado - Kevin | Kevin | BR-15 | P0 |
| RF-56 | el sistema registrará la corrección de un giro pagado como un movimiento nuevo - Kevin | Kevin | BR-13 | P1 |
| RF-57 | el sistema limitará lo que el operario ve a los datos de la operación que está atendiendo - Kevin | Kevin | BR-16 | P0 |

---

## No funcionales

El enunciado nombra dos como críticos —**seguridad** y **consistencia de datos**— y no da ninguna
cifra. Para la consistencia la medida correcta no es un número sino un **invariante**: algo que
nunca puede ser falso, y que por lo tanto se comprueba en cualquier momento.

### Seguridad

| ID | Título | Medida | Regla | Prioridad |
|---|---|---|---|---|
| RNF-01 | el sistema mantendrá ilegibles los datos de identidad y el código para quien administre la infraestructura | Quien tiene el almacenamiento y no la clave no reconstruye un documento ni un código | BR-08, BR-16 | P0 |
| RNF-02 | el sistema impedirá que un mismo rol cree un giro sobre el umbral reforzado y lo autorice | Ninguna identidad aparece como creadora y autorizadora del mismo giro (RF-13) | BR-05 | P0 |
| RNF-03 | el sistema conservará el registro de actos inalterable por el plazo que exija cada regulador | `[CLARIFY: el plazo lo fija cada regulador]` — hasta resolverlo, no se borra | BR-15 | P0 |
| RNF-04 | el sistema dejará traza de todo acceso a datos de identidad | Todo acceso tiene autor, momento y giro; ninguno es anónimo | BR-16 | P1 |

### Consistencia de datos

| ID | Título | Invariante | Regla | Prioridad |
|---|---|---|---|---|
| RNF-05 | el sistema impedirá que un giro quede pagado dos veces o con dos montos distintos | Cero doble pagos y cero giros huérfanos en la conciliación diaria | BR-10, BR-11 | P0 |
| RNF-06 | el sistema mantendrá un solo estado del giro entre el centro y el punto de atención | Dos lugares del sistema nunca afirman a la vez que un giro está retenido y disponible para cobro | BR-10 | P0 |
| RNF-07 | el sistema conservará la suma del dinero en toda operación | Lo que sale de una cuenta entra en otra; ningún movimiento deja el total distinto | BR-01 | P0 |
| RNF-08 | el sistema recuperará el estado de los giros de un punto caído sin intervención del operario | Un punto que vuelve no necesita que nadie le diga qué pasó mientras no estaba | BR-10 | P1 |

### Servicio

| ID | Título | Medida | Prioridad |
|---|---|---|---|
| RNF-09 | el sistema completará una operación de ventanilla en un tiempo acotado | `[ASSUMPTION: menos de 3 minutos]` desde que el operario empieza a registrarla, sin contar la verificación del documento | P1 |
| RNF-10 | el sistema dejará un giro fondeado disponible para cobro en el destino en un tiempo acotado | `[ASSUMPTION: menos de 15 minutos]` desde su creación | P0 |
| RNF-11 | el sistema sostendrá la capacidad de crear y de pagar giros | `[ASSUMPTION: 99,9 % mensual]`, medida sobre crear y pagar, no sobre consultar | P1 |
| RNF-12 | el sistema operará con más de un país de origen y más de una moneda destino desde el primer día | `[CLARIFY: cuántos corredores al lanzamiento, y cuáles]` | P0 |

---

## Las seis tensiones, y dónde quedan decididas

| Tensión | Entre | Cómo se decide | Ítem |
|---|---|---|---|
| **T1** Control ↔ rapidez | Rosa ↔ Kevin | **A favor del control, con precio acotado.** El tamizaje corre *antes* de aceptar el efectivo, de modo que se detiene en vez de revertir; a cambio, toda retención nace con plazo y se resuelve sola al vencerlo | RF-26 · RF-31 · RF-32 |
| **T2** Explicación ↔ reserva | Rosa ↔ Kevin | **Se decide en la altitud correcta: qué se le muestra a quien está en la ventanilla.** No es cuestión de redactar mejor un mensaje. Cuando revelar el motivo está prohibido, el operario recibe **la acción y no el motivo** — puede atender sin saber, y sin poder deducir | RF-39 · RF-40 |
| **T3** Identidad del receptor | Elena ↔ Kevin | **A favor del control, y se dice el costo.** Se exige el código *y* un documento que coincida; Elena sin documento válido no cobra. La decisión no es cómoda y no se disfraza | RF-34 |
| **T4** Certeza del monto ↔ exposición cambiaria | Rosa ↔ la empresa | **A favor de Rosa.** El monto de destino se fija al crear el giro y no se recalcula nunca, con una cotización que el sistema produce y fecha. La empresa carga el movimiento | RF-05 · RF-06 · RF-07 |
| **T5** El canal de Rosa ↔ el de Elena | Rosa ↔ Elena | **Rosa transmite el código por su cuenta.** El sistema no se lo da a Elena por ningún canal propio, y eso es lo que hace ejecutable la cancelación de RF-46 | RF-11 · RF-12 |
| **T6** Cerrar ↔ cerrar de verdad | Rosa ↔ Elena | **A favor de Elena.** El giro no cierra por fondearse ni por estar disponible: cierra cuando alguien cobró, y hasta entonces Rosa puede cancelarlo y recuperar su dinero | RF-46 · RF-53 |

## Reparto de prioridad

| | P0 | P1 | P2 |
|---|---|---|---|
| Funcionales | 50 | 7 | 0 |
| No funcionales | 8 | 4 | 0 |

## Supuestos y ambigüedades

| Marca | Dónde | Estado |
|---|---|---|
| `[ASSUMPTION: modelo Western Union — red de agentes, efectivo contra efectivo, sin cuenta bancaria en ninguna punta]` | Todo el backlog | Vigente — indicación del profesor |
| `[ASSUMPTION: umbral de límites (BR-04) y umbral reforzado (BR-05)]` | RF-08 · RF-09 · RF-13 | Vigente |
| `[ASSUMPTION: umbrales de servicio de RNF-09 a RNF-11]` | RNF-09 · RNF-10 · RNF-11 | Vigente — los consume el paso `E` |
| `[CLARIFY: plazo de prescripción de un giro no cobrado]` | RF-49 · RF-50 · RF-51 | **Abierta** — sin él, RF-49 no es verificable |
| `[CLARIFY: plazo de conservación del registro por regulador]` | RNF-03 · RF-18 | **Abierta** — determina el almacenamiento del paso `E` |
| `[CLARIFY: cuántos corredores al lanzamiento, y cuáles]` | RNF-12 | **Abierta** — determina la estimación de carga entera del paso `E` |
| `[CLARIFY: plazo máximo de una retención antes de resolverse sola]` | RF-31 · RF-32 | **Abierta** — sin número, la retención no tiene terminador comprobable |
