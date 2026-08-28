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
| RF-01 | el sistema identificará al emisor contra un documento oficial vigente antes de recibir su efectivo - Rosa | Rosa | BR-03 | P0 |
| RF-225 | el sistema resolverá con un segundo rol, y no con el criterio del operario, la duda sobre si la fotografía del documento corresponde al emisor - Kevin | Kevin | BR-03 | P0 |
| RF-02 | el sistema entregará al receptor su dinero en efectivo, sin exigirle cuenta bancaria - Elena | Elena | BR-01 | P0 |
| RF-79 | el sistema dará el giro por creado en el momento en que registra la recepción del efectivo - Kevin | Kevin | BR-03 | P0 |
| RF-03 | el sistema exigirá un único receptor designado por giro - Rosa | Rosa | BR-02 | P0 |
| RF-04 | el sistema exigirá un único país destino por giro - Rosa | Rosa | BR-02 | P0 |
| RF-63 | el sistema permitirá al emisor elegir el punto de atención donde cobrará el receptor, entre los disponibles en el país destino - Rosa | Rosa | BR-02 | P0 |
| RF-05 | el sistema informará al emisor el monto exacto en moneda destino antes de que entregue el efectivo - Rosa | Rosa | BR-07 | P0 |
| RF-06 | el sistema conservará sin recalcularlo, durante toda la vida del giro, el monto en moneda destino que informó al emisor - Rosa | Rosa | BR-07 | P0 |
| RF-07 | el sistema producirá y fechará la cotización de la que sale el monto en moneda destino - Rosa | Rosa | BR-07 | P0 |
| RF-157 | el sistema producirá y fechará la comisión que aplica a cada giro - Rosa | Rosa | BR-07 | P0 |
| RF-158 | el sistema producirá y fechará el margen que aplica sobre la cotización - Rosa | Rosa | BR-07 | P0 |
| RF-201 | el sistema dejará de ofrecer al emisor la cotización que no se ejecutó dentro de `[ASSUMPTION: 10 minutos]` de producida - Rosa | Rosa | BR-07 | P0 |
| RF-209 | el sistema conservará para el giro que espera la autorización de un segundo rol la cotización que se le informó al emisor antes de pedirla - Rosa | Rosa | BR-07 | P0 |
| RF-08 | el sistema rechazará, antes de que el operario reciba el efectivo, el giro que haga al emisor superar su límite por operación - Rosa | Rosa | BR-04 | P0 |
| RF-09 | el sistema rechazará, antes de que el operario reciba el efectivo, el giro que haga al emisor superar su acumulado en la ventana vigente `[ASSUMPTION: la ventana es de 30 días corridos]` - Rosa | Rosa | BR-04 | P0 |
| RF-10 | el sistema contará el límite por operación y el acumulado sobre la identidad del emisor y no sobre el punto de atención - Kevin | Kevin | BR-04 | P0 |
| RF-11 | el sistema hará llegar el código de seguimiento al emisor por llamada o mensaje de texto al teléfono que él registró - Rosa | Rosa | BR-08 | P0 |
| RF-125 | el sistema confirmará al operario que el código salió hacia el emisor, sin mostrárselo - Kevin | Kevin | BR-08 | P0 |
| RF-114 | el sistema recibirá la respuesta del desafío del propio receptor `[CLARIFY: por qué medio la introduce quien no tiene teléfono con pantalla]` - Elena | Elena | BR-09 | P0 |
| RF-94 | el sistema no volverá a entregar un código ya emitido, ni siquiera al emisor que lo perdió - Rosa | Rosa | BR-08 | P0 |
| RF-189 | el sistema tendrá por llegado el aviso cuyo canal no reporta fallo dentro de `[ASSUMPTION: 15 minutos]` del despacho - Rosa | Rosa | BR-15 | P0 |
| RF-217 | el sistema tendrá por no llegado el código de seguimiento cuyo canal no reporta entrega - Rosa | Rosa | BR-08 | P0 |
| RF-149 | el sistema dejará no pagable el giro del que no tiene constancia de que el código llegó a su emisor - Kevin | Kevin | BR-08 | P0 |
| RF-173 | el sistema volverá pagable el giro no pagable por falta de constancia cuando la constancia llega - Kevin | Kevin | BR-08 | P0 |
| RF-174 | el sistema devolverá al emisor el giro que sigue sin constancia del código a las `[ASSUMPTION: 72 horas]` de emitido - Rosa | Rosa | BR-12 | P0 |
| RF-117 | el sistema permitirá rehacer al mismo receptor el giro que se canceló o se devolvió sin haberse pagado - Rosa | Rosa | BR-12 | P0 |
| RF-134 | el sistema conservará en el giro rehecho la cotización que fijó el giro cancelado - Rosa | Rosa | BR-07 | P0 |
| RF-135 | el sistema no volverá a cobrar la comisión del giro rehecho - Rosa | Rosa | BR-07 | P0 |
| RF-123 | el sistema volverá a correr sobre el giro rehecho los mismos controles que sobre uno nuevo, incluida la identificación del emisor contra su documento - Kevin | Kevin | BR-06 | P0 |
| RF-13 | el sistema exigirá la autorización de un segundo rol antes de que el operario reciba el efectivo de un giro sobre el umbral reforzado - Kevin | Kevin | BR-05 | P0 |
| RF-191 | el sistema rechazará, antes de que el operario reciba el efectivo, el giro cuya autorización de segundo rol no llega en `[ASSUMPTION: 10 minutos]` - Kevin | Kevin | BR-05 | P0 |
| RF-14 | el sistema avisará al emisor por llamada o mensaje de texto que su devolución está disponible y en qué punto retirarla - Rosa | Rosa | BR-12 | P0 |

### La frontera

Este bloque existe por una sola razón: **el giro cruza un país.** La prueba se corre cada ronda y
**la ronda 16 la corrió en serio, con un resultado incómodo**: `RF-140` y `RF-161` —registrar la
fecha de nacimiento «cuando el reporte a una autoridad la exige»— **sobreviven palabra por palabra a
una red doméstica**, y llevaban catorce rondas bajo un encabezado que afirmaba que ninguno lo hacía.
Se quedan, porque el reporte transfronterizo los necesita; lo que se retira es la afirmación de que
todo el bloque muere, que era falsa. Es el mismo defecto que la
[iteración 03](../../evals/iterations/2026-08-26-03.md) encontró acá y que la 15 volvió a encontrar. La
[iteración 01](../../evals/iterations/2026-08-26-01.md) mostró que un backlog sin este bloque
describe un transmisor de dinero doméstico con un campo de moneda; la
[03](../../evals/iterations/2026-08-26-03.md) encontró que dos de sus ítems **sobrevivían a una red
doméstica** y estaban archivados bajo el rasgo equivocado: la liquidación con el agente pertenece al
efectivo y el aviso al receptor pertenece al canal. Los dos se mudaron a **Pago**.

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-16 | el sistema rechazará el giro cuando los dos reguladores impongan condiciones incompatibles, en vez de elegir una - Kevin | Kevin | BR-17 | P0 |
| RF-17 | el sistema reportará a la autoridad de origen el giro que supere su umbral de reporte transfronterizo `[ASSUMPTION: USD 10 000 por operación, o el que fije cada regulador si es menor]` - Kevin | Kevin | BR-17 | P0 |
| RF-139 | el sistema reportará a la autoridad del país de destino el giro que supere el umbral de reporte de esa jurisdicción - Kevin | Kevin | BR-17 | P0 |
| RF-185 | el sistema reportará a cada autoridad dentro del plazo que fija esa jurisdicción, y no del más largo de los dos - Kevin | Kevin | BR-17 | P0 |
| RF-140 | el sistema registrará la fecha de nacimiento del emisor cuando el reporte a una autoridad la exige - Kevin | Kevin | BR-17 | P0 |
| RF-161 | el sistema registrará la fecha de nacimiento del receptor cuando el reporte a una autoridad la exige - Kevin | Kevin | BR-17 | P0 |
| RF-18 | el sistema conservará el registro de un giro por el plazo más largo de los dos países que lo tocaron - Kevin | Kevin | BR-17 | P1 |
| RF-19 | el sistema informará al emisor que un país destino no puede atenderse antes de que entregue el efectivo - Rosa | Rosa | BR-02 | P0 |
| RF-20 | el sistema exigirá efectivo disponible en el corredor de destino antes de dar un giro por fondeado - Kevin | Kevin | BR-11 | P0 |
| RF-22 | el sistema aplicará el umbral de reporte de cada país sobre el giro completo y no sobre su tramo local - Kevin | Kevin | BR-17 | P0 |
| RF-23 | el sistema impedirá que un giro rechazado por el regulador de destino se cree en el de origen - Kevin | Kevin | BR-17 | P2 |

### Cumplimiento

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-26 | el sistema contrastará al emisor contra las listas de sanciones antes de aceptar el efectivo - Kevin | Kevin | BR-06 | P0 |
| RF-167 | el sistema rechazará la creación de un giro mientras no pueda contrastar a las dos puntas contra listas vigentes - Kevin | Kevin | BR-06 | P0 |
| RF-177 | el sistema rechazará, antes de aceptar el efectivo, el giro cuya consulta a una lista externa no responde en `[ASSUMPTION: 60 segundos]` - Kevin | Kevin | BR-06 | P0 |
| RF-186 | el sistema tratará como no vigente la copia de una lista de sanciones que no se actualizó en `[ASSUMPTION: 24 horas]` - Kevin | Kevin | BR-06 | P0 |
| RF-119 | el sistema contrastará al receptor designado contra las listas de sanciones antes de aceptar el efectivo - Kevin | Kevin | BR-06 | P0 |
| RF-27 | el sistema contrastará al receptor contra las listas vigentes al momento de autorizar el pago - Kevin | Kevin | BR-06 | P0 |
| RF-97 | el sistema volverá a tamizar los giros aún no pagados cuando cambia una lista de sanciones - Kevin | Kevin | BR-06 | P1 |
| RF-28 | el sistema separará una coincidencia exacta de sanciones de una coincidencia por homonimia - Kevin | Kevin | BR-06 | P0 |
| RF-78 | el sistema resolverá la coincidencia por homonimia en `[ASSUMPTION: 24 horas]`, plazo más corto que el de la coincidencia exacta - Kevin | Kevin | BR-06 | P1 |
| RF-29 | el sistema retendrá el giro con coincidencia de sanciones - Kevin | Kevin | BR-06 | P0 |
| RF-220 | el sistema dejará no pagable todo giro retenido - Kevin | Kevin | BR-06 | P0 |
| RF-182 | el sistema dejará no cancelable todo giro retenido - Kevin | Kevin | BR-06 | P0 |
| RF-213 | el sistema volverá cancelable el giro cuya retención terminó sin devolución - Rosa | Rosa | BR-06 | P0 |
| RF-30 | el sistema derivará el giro retenido a un rol distinto del operario que lo atendió - Kevin | Kevin | BR-06 | P0 |
| RF-31 | el sistema exigirá que toda retención lleve el plazo del regulador más estricto de los dos países del giro - Kevin | Kevin | BR-06 | P0 |
| RF-32 | el sistema devolverá al emisor el monto del giro cuya retención venció sin liberarse - Kevin | Kevin | BR-06 | P0 |
| RF-106 | el sistema avisará al receptor por llamada o mensaje de texto cuando un giro se devuelva al emisor - Elena | Elena | BR-12 | P0 |
| RF-71 | el sistema devolverá siempre en efectivo - Rosa | Rosa | BR-12 | P0 |
| RF-203 | el sistema exigirá el documento oficial vigente del emisor antes de entregarle en el mostrador el efectivo de una devolución - Kevin | Kevin | BR-12 | P0 |
| RF-88 | el sistema devolverá siempre en la moneda que el emisor entregó - Rosa | Rosa | BR-12 | P0 |
| RF-72 | el sistema devolverá en el punto de atención que el emisor elija, y a falta de elección en aquel donde entregó el efectivo - Rosa | Rosa | BR-12 | P0 |
| RF-207 | el sistema identificará contra los datos que registró al crear el giro, antes de admitirla, la elección del punto de devolución hecha fuera del mostrador - Rosa | Rosa | BR-12 | P0 |
| RF-73 | el sistema informará al emisor el plazo de una eventual devolución antes de que entregue el efectivo - Rosa | Rosa | BR-12 | P0 |
| RF-96 | el sistema informará al emisor, antes de que entregue el efectivo, cuánto puede durar como máximo la retención de su giro - Rosa | Rosa | BR-06 | P0 |
| RF-115 | el sistema informará al emisor, antes de que entregue el efectivo, dentro de cuánto le avisará si su giro queda retenido - Rosa | Rosa | BR-06 | P0 |
| RF-133 | el sistema no dejará pasar más de `[ASSUMPTION: 1 hora]` entre la retención de un giro y el aviso a su emisor - Rosa | Rosa | BR-06 | P0 |
| RF-89 | el sistema mantendrá disponible la devolución no retirada durante `[ASSUMPTION: 12 meses]` contados desde que quedó disponible - Rosa | Rosa | BR-12 | P2 |
| RF-137 | el sistema dará por prescrita la devolución que nadie retiró al vencer su plazo de disponibilidad - Rosa | Rosa | BR-14 | P2 |
| RF-74 | el sistema devolverá también la comisión cobrada cuando el giro no llegó a pagarse - Rosa | Rosa | BR-12 | P0 |
| RF-33 | el sistema permitirá liberar un giro retenido únicamente al rol de cumplimiento - Kevin | Kevin | BR-06 | P0 |
| RF-87 | el sistema registrará el motivo de cada liberación de un giro retenido - Kevin | Kevin | BR-06 | P1 |
| RF-163 | el sistema mostrará al rol de cumplimiento el motivo con que se liberó cada giro retenido - Kevin | Kevin | BR-06 | P1 |
| RF-127 | el sistema avisará al emisor por llamada o mensaje de texto cuando su giro deja de estar retenido - Rosa | Rosa | BR-06 | P0 |
| RF-93 | el sistema rechazará, antes de que el operario reciba el efectivo, el giro cuyo receptor superó su acumulado de cobros en la ventana `[ASSUMPTION: 30 días corridos]` - Kevin | Kevin | BR-04 | P0 |
| RF-159 | el sistema fijará por jurisdicción de destino el acumulado de cobros que un receptor no puede superar en la ventana - Kevin | Kevin | BR-04 | P0 |

### Pago

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-34 | el sistema exigirá el código del giro para autorizar un pago - Elena | Elena | BR-09 | P0 |
| RF-147 | el sistema recibirá el código del giro del propio receptor `[CLARIFY: por qué medio lo introduce quien no tiene teléfono con pantalla]` - Elena | Elena | BR-08 | P0 |
| RF-85 | el sistema exigirá un documento de identidad cuyo titular coincida con el receptor designado - Elena | Elena | BR-09 | P0 |
| RF-86 | el sistema exigirá que el documento del receptor esté vigente - Elena | Elena | BR-09 | P0 |
| RF-68 | el sistema exigirá al emisor registrar al crear el giro una pregunta acordada con el receptor, y su respuesta - Rosa | Rosa | BR-09 | P0 |
| RF-101 | el sistema no transmitirá a nadie la respuesta del desafío, ni siquiera a quien registró la pregunta - Rosa | Rosa | BR-09 | P0 |
| RF-102 | el sistema impedirá que el punto de atención cobre al receptor por recibir su dinero - Elena | Elena | BR-01 | P0 |
| RF-69 | el sistema entregará al receptor por llamada o mensaje de texto la pregunta del desafío cuando no tiene documento vigente - Elena | Elena | BR-09 | P0 |
| RF-122 | el sistema autorizará el pago con documento vencido cuando el receptor responde correctamente el desafío - Elena | Elena | BR-09 | P0 |
| RF-222 | el sistema autorizará con documento vencido la entrega de una reposición cuando el receptor responde correctamente el desafío - Elena | Elena | BR-13 | P0 |
| RF-82 | el sistema limitará a `[ASSUMPTION: 3]` los intentos de responder el desafío de un giro - Kevin | Kevin | BR-09 | P0 |
| RF-103 | el sistema devolverá al emisor el giro cuyos intentos de desafío se agotaron y cuya identificación por el rol de cumplimiento no prosperó - Kevin | Kevin | BR-09 | P0 |
| RF-212 | el sistema derivará al rol de cumplimiento la identificación del receptor cuyos intentos de desafío se agotaron, antes de devolver el giro - Elena | Elena | BR-09 | P0 |
| RF-218 | el sistema habilitará el pago del giro cuyo receptor identificó el rol de cumplimiento contra los datos que el emisor registró, tras agotarse los intentos - Elena | Elena | BR-09 | P0 |
| RF-219 | el sistema resolverá dentro de `[ASSUMPTION: 24 horas]` la identificación derivada al rol de cumplimiento - Elena | Elena | BR-09 | P0 |
| RF-223 | el sistema devolverá al emisor el giro cuya identificación derivada venció sin resolverse - Elena | Elena | BR-12 | P0 |
| RF-83 | el sistema caducará la respuesta del desafío junto con el giro que la lleva - Kevin | Kevin | BR-09 | P0 |
| RF-84 | el sistema decidirá qué diferencias de escritura cuentan como coincidencia de titular, y no el operario - Kevin | Kevin | BR-09 | P0 |
| RF-148 | el sistema resolverá con el desafío, y no con el criterio del operario, la duda sobre si la fotografía del documento corresponde al receptor - Elena | Elena | BR-09 | P0 |
| RF-36 | el sistema no habilitará el pago de un giro cuyos fondos de origen no estén confirmados - Kevin | Kevin | BR-11 | P0 |
| RF-24 | el sistema liquidará con el agente el efectivo que puso de su caja, en el plazo acordado con él `[ASSUMPTION: al cierre del día hábil siguiente]` - Kevin | Kevin | BR-01 | P0 |
| RF-37 | el sistema avisará al receptor por llamada o mensaje de texto si su giro quedó retenido - Elena | Elena | BR-06 | P0 |
| RF-59 | el sistema repondrá al emisor o al receptor, según a quién le faltó, toda diferencia comprobada entre el monto fijado y el entregado - Elena | Elena | BR-13 | P0 |
| RF-154 | el sistema decidirá en un rol ajeno al punto donde ocurrió si una diferencia declarada queda comprobada - Kevin | Kevin | BR-13 | P0 |
| RF-193 | el sistema decidirá toda diferencia declarada dentro de `[ASSUMPTION: 5 días hábiles en la jurisdicción del punto donde se originó]` - Elena | Elena | BR-13 | P0 |
| RF-194 | el sistema repondrá la diferencia cuyo plazo de decisión venció sin decidirse - Elena | Elena | BR-13 | P0 |
| RF-214 | el sistema no repondrá por una diferencia más que lo que el giro fijó menos lo que la evidencia de entrega acredita - Kevin | Kevin | BR-13 | P0 |
| RF-155 | el sistema pagará al receptor en efectivo, en el punto donde cobró, la diferencia repuesta a su favor - Elena | Elena | BR-13 | P0 |
| RF-204 | el sistema exigirá el documento oficial vigente del receptor designado antes de entregarle en el mostrador el efectivo de una reposición - Elena | Elena | BR-13 | P0 |
| RF-156 | el sistema avisará al receptor por llamada o mensaje de texto que su reposición está disponible y en qué punto retirarla - Elena | Elena | BR-13 | P0 |
| RF-175 | el sistema mantendrá disponible la reposición no retirada durante `[ASSUMPTION: 12 meses]` contados desde que quedó disponible - Elena | Elena | BR-13 | P2 |
| RF-176 | el sistema dará por prescrita la reposición que nadie retiró al vencer su plazo de disponibilidad - Elena | Elena | BR-14 | P2 |
| RF-104 | el sistema no aplicará a la liquidación del agente ningún descuento por diferencia que no le haya informado antes - Kevin | Kevin | BR-13 | P0 |
| RF-195 | el sistema acompañará con la evidencia que lo sustenta todo descuento por diferencia que informe al agente - Kevin | Kevin | BR-13 | P0 |
| RF-143 | el sistema descontará de la liquidación del agente la diferencia repuesta que se originó en su punto - Kevin | Kevin | BR-13 | P0 |
| RF-145 | el sistema admitirá del agente una objeción a un descuento por diferencia antes de aplicarlo a su liquidación - Kevin | Kevin | BR-13 | P0 |
| RF-153 | el sistema resolverá toda objeción del agente a un descuento por diferencia dentro de `[ASSUMPTION: 5 días hábiles en la jurisdicción del punto donde se originó la diferencia]` - Kevin | Kevin | BR-13 | P0 |
| RF-184 | el sistema aplicará el descuento objetado cuyo plazo de resolución venció sin resolverse - Kevin | Kevin | BR-13 | P0 |
| RF-60 | el sistema informará al emisor por llamada o mensaje de texto toda diferencia registrada sobre el giro - Rosa | Rosa | BR-13 | P1 |
| RF-121 | el sistema informará al receptor por llamada o mensaje de texto toda diferencia registrada sobre el giro - Elena | Elena | BR-13 | P1 |
| RF-90 | el sistema permitirá al receptor declarar por llamada o mensaje de texto que el dinero recibido no coincide con el informado - Elena | Elena | BR-13 | P0 |
| RF-166 | el sistema admitirá del receptor, en el mostrador donde cobró y contra su documento, la declaración de que el dinero recibido no coincide con el informado - Elena | Elena | BR-13 | P0 |
| RF-91 | el sistema ofrecerá al emisor por llamada o mensaje de texto otro punto de atención del mismo distrito que el elegido cuando ese se queda sin efectivo para pagar - Rosa | Rosa | BR-02 | P0 |
| RF-129 | el sistema devolverá al emisor el giro para el que no queda ningún punto de atención con efectivo para pagarlo en el distrito elegido - Rosa | Rosa | BR-12 | P0 |
| RF-105 | el sistema no cambiará el punto de atención elegido sin la respuesta del emisor, salvo el cambio que el receptor solicitó y el emisor dejó vencer - Rosa | Rosa | BR-02 | P0 |
| RF-208 | el sistema identificará contra los datos que registró al crear el giro, antes de admitirla, la respuesta del emisor a un cambio de punto hecha fuera del mostrador - Rosa | Rosa | BR-02 | P0 |
| RF-187 | el sistema admitirá del receptor designado la solicitud de cambio de punto de atención - Elena | Elena | BR-02 | P0 |
| RF-192 | el sistema informará al emisor, al ofrecerle un cambio de punto de atención, si la solicitud la originó el receptor - Rosa | Rosa | BR-02 | P0 |
| RF-111 | el sistema devolverá al emisor el giro cuyo punto se quedó sin efectivo para pagar, cuya respuesta no llega dentro del plazo y para el que el receptor no solicitó otro punto - Rosa | Rosa | BR-12 | P0 |
| RF-211 | el sistema cambiará al punto que el receptor solicitó el giro cuyo emisor no respondió dentro del plazo, en vez de devolverlo - Elena | Elena | BR-02 | P0 |
| RF-164 | el sistema devolverá al emisor el giro cuyo punto se quedó sin efectivo para pagar y cuyo cambio de punto el emisor rechazó - Rosa | Rosa | BR-12 | P0 |
| RF-116 | el sistema informará al emisor por llamada o mensaje de texto, al ofrecerle otro punto de atención, dentro de cuánto debe responder - Rosa | Rosa | BR-11 | P0 |
| RF-183 | el sistema no dará al emisor menos de `[ASSUMPTION: 24 horas]` para responder a un cambio de punto de atención - Rosa | Rosa | BR-11 | P0 |
| RF-39 | el sistema asociará al menos una acción ofrecible a todo giro rechazado - Kevin | Kevin | BR-16 | P0 |
| RF-151 | el sistema asociará al menos una acción ofrecible a todo giro no pagable - Kevin | Kevin | BR-16 | P0 |
| RF-152 | el sistema asociará al giro cuyo motivo de rechazo está prohibido revelar una acción ofrecible que no permita deducirlo - Kevin | Kevin | BR-16 | P0 |
| RF-171 | el sistema asociará al giro cuyo motivo de retención está prohibido revelar una acción ofrecible que no permita deducirlo - Kevin | Kevin | BR-16 | P0 |
| RF-130 | el sistema mostrará al operario la acción ofrecible del giro que tiene delante - Kevin | Kevin | BR-16 | P0 |
| RF-221 | el sistema mostrará al operario en qué estado quedó la operación que acaba de cerrar - Kevin | Kevin | BR-16 | P0 |
| RF-40 | el sistema omitirá al operario el motivo de un rechazo cuando revelarlo esté prohibido - Kevin | Kevin | BR-16 | P0 |
| RF-170 | el sistema omitirá al operario el motivo de una retención cuando revelarlo esté prohibido - Kevin | Kevin | BR-16 | P0 |
| RF-25 | el sistema avisará al receptor que hay un giro a su nombre por llamada o mensaje de texto - Elena | Elena | BR-09 | P0 |
| RF-210 | el sistema no avisará al receptor que hay un giro a su nombre antes de tener constancia de que el código llegó al emisor - Elena | Elena | BR-08 | P0 |
| RF-41 | el sistema informará al receptor por llamada o mensaje de texto, antes de que viaje, el monto que cobrará - Elena | Elena | BR-09 | P0 |
| RF-199 | el sistema informará al receptor por llamada o mensaje de texto, antes de que viaje, en qué punto de atención puede cobrar - Elena | Elena | BR-11 | P0 |
| RF-75 | el sistema informará al receptor por llamada o mensaje de texto si el punto elegido tiene efectivo para pagarle - Elena | Elena | BR-11 | P0 |
| RF-109 | el sistema volverá a avisar al receptor por llamada o mensaje de texto si el punto elegido se queda sin efectivo para pagarle - Elena | Elena | BR-11 | P0 |
| RF-124 | el sistema informará al receptor por llamada o mensaje de texto a qué otro punto de atención puede ir, una vez que el cambio de punto queda en firme - Elena | Elena | BR-11 | P0 |
| RF-76 | el sistema registrará el efectivo que cada punto de atención declara al abrir y al cerrar su caja - Kevin | Kevin | BR-01 | P0 |
| RF-92 | el sistema informará al operario el efectivo disponible en su punto antes de habilitarle un pago o una devolución - Kevin | Kevin | BR-01 | P0 |
| RF-95 | el sistema descontará del efectivo del punto cada pago y cada devolución que autoriza, sin esperar al cierre de caja - Kevin | Kevin | BR-01 | P0 |
| RF-141 | el sistema informará al agente cada cierre de caja de sus puntos en que el efectivo declarado difiere del esperado - Kevin | Kevin | BR-01 | P1 |
| RF-77 | el sistema informará al emisor la fecha desde la cual el giro estará disponible para cobro, antes de que entregue el efectivo - Rosa | Rosa | BR-07 | P0 |
| RF-136 | el sistema informará al emisor la comisión que se le cobra por el giro, antes de que entregue el efectivo - Rosa | Rosa | BR-07 | P0 |
| RF-142 | el sistema informará al emisor el margen que se aplica sobre la cotización, antes de que entregue el efectivo - Rosa | Rosa | BR-07 | P0 |

### Interrupción y consistencia

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-42 | el sistema dejará el giro interrumpido en un estado único que el operario puede leer y retomar - Kevin | Kevin | BR-10 | P0 |
| RF-118 | el sistema dejará el efectivo ya recibido sin giro creado en un estado único que el operario puede leer y retomar - Kevin | Kevin | BR-10 | P0 |
| RF-138 | el sistema devolverá al emisor el efectivo en custodia que nadie retomó al vencer `[ASSUMPTION: 72 horas]` - Kevin | Kevin | BR-12 | P0 |
| RF-43 | el sistema tratará todo reintento de una creación interrumpida como la misma operación - Kevin | Kevin | BR-10 | P0 |
| RF-44 | el sistema tratará todo reintento de un pago interrumpido como la misma operación - Kevin | Kevin | BR-10 | P0 |
| RF-100 | el sistema impedirá que un punto sin conexión autorice un pago que no puede comprobar contra el centro - Kevin | Kevin | BR-10 | P0 |
| RF-144 | el sistema dejará el pago cuya confirmación no llegó del punto al centro en un estado único que el operario puede leer y retomar - Kevin | Kevin | BR-10 | P0 |
| RF-146 | el sistema resolverá contra el registro del centro el pago cuya confirmación no llegó, sin intervención del operario - Kevin | Kevin | BR-10 | P0 |

### Cancelación y prescripción

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-46 | el sistema permitirá al emisor cancelar su giro mientras el receptor no lo haya cobrado - Rosa | Rosa | BR-12 | P0 |
| RF-47 | el sistema devolverá al emisor, al cancelar, el efectivo que entregó por el giro - Rosa | Rosa | BR-12 | P0 |
| RF-48 | el sistema admitirá la cancelación de un giro únicamente del emisor que lo creó - Rosa | Rosa | BR-12 | P0 |
| RF-206 | el sistema identificará contra los datos que registró al crear el giro, antes de admitirla, la cancelación pedida fuera del mostrador - Rosa | Rosa | BR-12 | P0 |
| RF-49 | el sistema dejará no pagable el giro cuyo plazo de prescripción venció - Rosa | Rosa | BR-14 | P0 |
| RF-50 | el sistema devolverá al emisor el monto del giro prescrito - Rosa | Rosa | BR-14 | P0 |
| RF-51 | el sistema avisará al emisor por llamada o mensaje de texto antes de que el giro prescriba - Rosa | Rosa | BR-14 | P1 |
| RF-120 | el sistema avisará al receptor por llamada o mensaje de texto antes de que el giro prescriba - Elena | Elena | BR-14 | P1 |

### Consulta

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-52 | el sistema permitirá al emisor consultar por llamada o mensaje de texto el estado de sus giros sin depender del receptor - Rosa | Rosa | BR-01 | P0 |
| RF-205 | el sistema identificará contra los datos que registró al crear el giro, antes de responderle, a quien consulta fuera del mostrador el estado de sus giros como emisor - Rosa | Rosa | BR-09 | P0 |
| RF-128 | el sistema permitirá al receptor consultar por llamada o mensaje de texto el estado de los giros a su nombre sin depender del emisor - Elena | Elena | BR-01 | P0 |
| RF-178 | el sistema confirmará al receptor designado, por llamada o mensaje de texto, si el código que dice tener corresponde a un giro a su nombre, sin decirle cuál es - Elena | Elena | BR-09 | P0 |
| RF-179 | el sistema limitará a `[ASSUMPTION: 3]` los intentos de comprobar un código contra un mismo giro - Elena | Elena | BR-09 | P0 |
| RF-180 | el sistema identificará contra los datos que el emisor registró, antes de responderle, a quien consulta fuera del mostrador el estado de un giro a su nombre - Elena | Elena | BR-09 | P0 |
| RF-196 | el sistema identificará contra los datos que el emisor registró, antes de admitirla, la declaración de diferencia hecha fuera del mostrador - Elena | Elena | BR-09 | P0 |
| RF-197 | el sistema identificará contra los datos que el emisor registró, antes de responderle, a quien comprueba un código fuera del mostrador - Elena | Elena | BR-09 | P0 |
| RF-198 | el sistema identificará contra los datos que el emisor registró, antes de admitirla, la solicitud de cambio de punto hecha fuera del mostrador - Elena | Elena | BR-09 | P0 |
| RF-53 | el sistema distinguirá al emisor el giro disponible para cobro del que todavía no lo está - Rosa | Rosa | BR-01 | P0 |
| RF-64 | el sistema dará el giro por cerrado en el momento en que el receptor recibe el dinero - Elena | Elena | BR-10 | P0 |
| RF-65 | el sistema avisará al emisor por llamada o mensaje de texto que su giro fue cobrado - Rosa | Rosa | BR-01 | P0 |
| RF-66 | el sistema mostrará al emisor que su giro está retenido y hasta qué fecha - Rosa | Rosa | BR-06 | P0 |
| RF-67 | el sistema avisará al emisor por llamada o mensaje de texto cuando su giro pase a estar retenido - Rosa | Rosa | BR-06 | P0 |
| RF-172 | el sistema avisará al emisor por llamada o mensaje de texto cuando su giro quede no pagable - Rosa | Rosa | BR-08 | P0 |
| RF-190 | el sistema avisará al receptor por llamada o mensaje de texto cuando el giro a su nombre quede no pagable - Elena | Elena | BR-08 | P0 |
| RF-200 | el sistema informará al operario que registró la recepción del efectivo que ese giro quedó no pagable, sin mostrarle ningún otro dato de la operación - Kevin | Kevin | BR-08 | P0 |

### Registro y privilegio

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-54 | el sistema asociará cada acto sobre un giro a la identidad de quien lo ejecutó - Kevin | Kevin | BR-15 | P0 |
| RF-56 | el sistema registrará la corrección del **monto** de un giro pagado como un movimiento nuevo - Kevin | Kevin | BR-13 | P1 |
| RF-70 | el sistema impedirá alterar el receptor designado de un giro después de creado - Rosa | Rosa | BR-09 | P0 |
| RF-61 | el sistema exigirá la autorización de un segundo rol para corregir el monto de un giro pagado - Kevin | Kevin | BR-13 | P0 |
| RF-57 | el sistema limitará lo que el operario ve a los datos de la operación que está atendiendo, excluida la respuesta del desafío - Kevin | Kevin | BR-16 | P0 |
| RF-80 | el sistema conservará la evidencia de la identificación del emisor de cada giro - Kevin | Kevin | BR-15 | P1 |
| RF-160 | el sistema conservará la evidencia de la identificación del receptor de cada giro - Kevin | Kevin | BR-15 | P1 |
| RF-168 | el sistema conservará la evidencia, firmada por el receptor, del monto que recibió en efectivo - Kevin | Kevin | BR-15 | P0 |
| RF-98 | el sistema conservará constancia de cada aviso enviado - Elena | Elena | BR-15 | P0 |
| RF-162 | el sistema mostrará la constancia de un aviso únicamente a su destinatario - Elena | Elena | BR-15 | P0 |
| RF-224 | el sistema mostrará la constancia de un aviso únicamente por el canal por el que lo despachó - Elena | Elena | BR-15 | P0 |
| RF-131 | el sistema registrará el resultado que el canal reporta sobre cada aviso - Elena | Elena | BR-15 | P0 |
| RF-132 | el sistema tratará como no avisado a quien no tenga constancia de que el aviso llegó - Elena | Elena | BR-15 | P1 |
| RF-202 | el sistema volverá a despachar por llamada o mensaje de texto el aviso que el canal reporta como no entregado y el que el destinatario dice no haber recibido - Elena | Elena | BR-15 | P0 |
| RF-169 | el sistema no descartará ningún aviso, cualquiera sea la causa - Elena | Elena | BR-15 | P0 |
| RF-188 | el sistema entregará primero el aviso sujeto a un plazo cuando la capacidad del canal no alcanza para todos - Elena | Elena | BR-15 | P1 |
| RF-99 | el sistema descartará a los `[ASSUMPTION: 3 días]` la evidencia de identificación de un emisor que no llegó a crear un giro - Rosa | Rosa | BR-16 | P2 |
| RF-81 | el sistema suprimirá a pedido los datos personales de quien los entregó, y de nadie más - Rosa | Rosa | BR-16 | P2 |
| RF-215 | el sistema identificará contra los datos que registró, antes de admitirla, la supresión de datos personales pedida fuera del mostrador - Rosa | Rosa | BR-16 | P2 |
| RF-226 | el sistema exigirá el documento oficial vigente de quien pide en el mostrador cancelar un giro o suprimir sus datos personales - Kevin | Kevin | BR-16 | P0 |

---

## No funcionales

El enunciado nombra dos como críticos —**seguridad** y **consistencia de datos**— y no da ninguna
cifra. Para la consistencia la medida correcta no es un número sino un **invariante**: algo que
nunca puede ser falso, y que por lo tanto se comprueba en cualquier momento.

### Seguridad

| ID | Título | Medida | Regla | Prioridad |
|---|---|---|---|---|
| RNF-01 | el sistema mantendrá ilegibles los datos de identidad para quien administre la infraestructura | Nadie que tenga acceso al almacenamiento reconstruye un documento de identidad | BR-08, BR-16 | P0 |
| RNF-15 | el sistema mantendrá ilegible el código de seguimiento para quien administre la infraestructura y para quien atiende el mostrador | Ni quien administra la infraestructura ni quien atiende el mostrador reconstruye un código: el sistema lo comprueba sin mostrárselo a ninguno de los dos | BR-08 | P0 |
| RNF-17 | el sistema mantendrá ilegible la respuesta del desafío para quien administre la infraestructura y para quien atiende el mostrador | Ni quien administra la infraestructura ni quien atiende el mostrador reconstruye una respuesta: el sistema la comprueba sin mostrársela a ninguno de los dos | BR-08 | P0 |
| RNF-02 | el sistema impedirá que una misma identidad ejerza dos roles sobre un giro | Ninguna identidad aparece dos veces en la cadena crear → autorizar → pagar → liberar → corregir de un mismo giro | BR-05 | P0 |
| RNF-18 | el sistema impedirá que quien atiende un mostrador inicie una corrección sobre un giro pagado | Ninguna identidad que opere un mostrador inicia la corrección del monto de un giro ya pagado, en ningún punto y en ningún momento | BR-05 | P0 |
| RNF-03 | el sistema conservará inalterable el registro de actos | Ningún acto registrado se modifica ni se borra, cualquiera sea quien lo pida — y esa conservación prevalece sobre toda supresión | BR-15 | P0 |
| RNF-04 | el sistema dejará traza de todo acceso a datos de identidad | Todo acceso tiene autor, momento y giro; ninguno es anónimo | BR-16 | P1 |

### Consistencia de datos

| ID | Título | Invariante | Regla | Prioridad |
|---|---|---|---|---|
| RNF-05 | el sistema impedirá que un giro quede pagado dos veces | Ningún giro registra dos entregas al receptor, en ningún punto y en ningún momento | BR-10, BR-11 | P0 |
| RNF-16 | el sistema impedirá que un giro quede pagado con un monto distinto del que se le informó al emisor | Ningún giro se registra como entregado por una cifra distinta de la que el emisor vio antes de entregar su efectivo. El invariante habla del registro; la diferencia entre lo registrado y lo que el receptor contó a mano la remedian RF-59 y RF-194 | BR-07, BR-13 | P0 |
| RNF-06 | el sistema mantendrá un solo estado del giro entre el centro y el punto de atención | Dos lugares del sistema nunca afirman a la vez que un giro está retenido y disponible para cobro | BR-10 | P0 |
| RNF-13 | el sistema impedirá que un giro quede devuelto y cobrado a la vez | Ningún giro figura simultáneamente devuelto al emisor y entregado al receptor, en ningún punto y en ningún momento | BR-12 | P0 |
| RNF-19 | el sistema impedirá que un giro quede devuelto y pagable a la vez | Ningún giro figura simultáneamente devuelto al emisor y habilitado para que el receptor lo cobre, en ningún punto y en ningún momento | BR-12 | P0 |
| RNF-07 | el sistema conservará la suma del dinero en toda operación | Lo que sale de una cuenta entra en otra; ningún movimiento deja el total distinto | BR-01 | P0 |
| RNF-08 | el sistema recuperará el estado de los giros de un punto caído sin intervención del operario | Un punto que vuelve no necesita que nadie le diga qué pasó mientras no estaba | BR-10 | P1 |

### Servicio

| ID | Título | Medida | Prioridad |
|---|---|---|---|
| RNF-09 | el sistema resolverá en un tiempo acotado la parte de una atención que solo depende de él | `[ASSUMPTION: menos de 3 minutos]` desde que alguien llega al mostrador, incluida la verificación del documento contra el sistema, **y `[ASSUMPTION: menos de 14 minutos]` sumándole las esperas de RNF-20 y RF-177 cuando las dos ocurren**, que es la suma de los tres y no una cifra aparte. No se mide contra una disponibilidad: son plazos | P0 |
| RNF-20 | el sistema resolverá en un tiempo acotado la espera por la autorización de un segundo rol | `[ASSUMPTION: 10 minutos]` desde que la autorización se solicita, con la persona esperando en el mostrador. RF-191 dice qué pasa al vencerlo | P0 |
| RNF-10 | el sistema dejará un giro fondeado disponible para cobro en el destino en un tiempo acotado | `[ASSUMPTION: menos de 15 minutos]` desde su creación | P0 |
| RNF-11 | el sistema sostendrá la capacidad de crear y de pagar giros | `[ASSUMPTION: 99,9 % mensual]`, medida sobre crear y pagar, no sobre consultar | P1 |
| RNF-12 | el sistema no supondrá un solo país de origen en ninguna cifra ni en ninguna regla | Ninguna cifra ni regla del sistema queda falsa al agregar un país de origen, y agregarlo no exige reescribir ninguna. Los corredores concretos del lanzamiento los fija el supuesto único de la tabla de abajo | P0 |
| RNF-14 | el sistema operará con más de una moneda destino desde el primer día | Ninguna cifra del sistema supone una sola moneda de destino | P0 |

---

## Las siete tensiones, y dónde quedan decididas

| Tensión | Entre | Cómo se decide | Ítem |
|---|---|---|---|
| **T1** Control ↔ rapidez | Rosa ↔ Kevin | **A favor del control, con precio acotado — y desde la ronda 13 el precio está acotado de verdad.** El tamizaje corre *antes* de aceptar el efectivo, de modo que se detiene en vez de revertir; a cambio, toda retención nace con plazo y se resuelve sola al vencerlo. Y desde la ronda 14 **los tres plazos que ocurren con la persona delante están partidos y los tres tienen final**: la atención en `RNF-09`, el segundo rol en `RNF-20` con `RF-191` diciendo qué pasa al vencerlo, y la lista externa en `RF-177`. Ninguno se mide ya contra una disponibilidad | RF-26 · RF-31 · RF-32 · RNF-09 · RNF-20 · RF-191 · RF-177 |
| **T2** Explicación ↔ reserva | Rosa ↔ Kevin | **Se decide en los dos mostradores, y la reserva de la ronda 11 queda cerrada.** Cuando revelar el motivo está prohibido, el operario recibe **una salida concreta que ofrecer, no la razón** (RF-39, RF-40) y esa salida **no permite deducir el motivo** (RF-152): atiende sin saber y sin poder deducir. **La ronda 13 cerró el agujero que partir RF-39 destapó:** lo que RF-40 y RF-152 decidían solo para el *rechazo* lo deciden ahora también para la *retención* —RF-170 y RF-171—, que es el estado que puede tener un reporte detrás y el que T2 existe para gobernar. Y del lado de Rosa: ve **que** está retenido y **hasta cuándo**, nunca por qué, y sabe de antemano dentro de cuánto le avisarán (RF-66, RF-67, RF-115) | RF-39 · RF-40 · RF-170 · RF-152 · RF-171 · RF-66 · RF-67 · RF-115 |
| **T3** Identidad del receptor | Elena ↔ Kevin | **Se parte, como T5, y sus tres ejes quedan decididos.** La regla dura queda en un título solo, desde que la ronda 13 lo partió: el documento tiene que estar **vigente** (RF-86), y la única excepción vive entera en su propio título (RF-122); **qué cuenta como coincidencia de escritura lo decide el sistema, no el operario** (RF-84); y **la duda sobre la fotografía tampoco la decide el operario, la resuelve el desafío** (RF-148). La salida al documento vencido es el mismo desafío: el emisor registra una pregunta **acordada con el receptor** (RF-68), el sistema le entrega la pregunta por su canal (RF-69) y **autoriza el pago cuando la responde** (RF-122), sin transmitir la respuesta a nadie (RF-101) y comprobándola sin mostrarla ni a la infraestructura ni al mostrador (RF-114, RNF-17), con intentos acotados (RF-82) | RF-86 · RF-84 · RF-148 · RF-68 · RF-69 · RF-122 · RF-101 · RF-114 · RNF-17 · RF-82 |
| **T4** Certeza del monto ↔ exposición cambiaria | Rosa ↔ la empresa | **A favor de Rosa.** El monto de destino se fija al crear el giro y no se recalcula nunca, con una cotización que el sistema produce y fecha. La empresa carga el movimiento | RF-05 · RF-06 · RF-07 |
| **T5** El canal de Rosa ↔ el de Elena | Rosa ↔ Elena | **Se parte en dos, y el secreto tiene decidido quién lo mueve en los dos extremos — no por qué medio lo introduce Elena, que sigue sin título y ella lo reporta cada ronda.** El **código** llega **solo al emisor**, por llamada o mensaje de texto al teléfono que él registró (RF-11), y ni quien atiende el mostrador puede leerlo o transcribirlo (RNF-15, que desde la ronda 16 lo dice solo, sin RF-113 repitiendo su mitad) ni el sistema lo reemite (RF-94): al receptor se lo pasa Rosa, nunca el sistema. En el mostrador **lo introduce el propio receptor, sin que quien atiende pueda leerlo ni digitarlo** (RF-147), igual que la respuesta del desafío (RF-114). Para que el operario no quede mudo, RF-125 le confirma que el código salió sin mostrárselo, y el giro del que no hay constancia de que llegó queda **no pagable con acción ofrecible** (RF-149, RF-151) en vez de quedar mudo — y desde la ronda 14 ese estado **viaja a las dos puntas y no a una**: RF-172 se lo avisa al emisor, RF-190 al receptor y RF-200 al operario que recibió el efectivo, cada uno por su canal — y **desde la ronda 16 el que *nace* no pagable tampoco se anuncia como cobrable**: RF-210 impide que RF-25 salga antes de la constancia, con la constancia por fin producida (RF-189), RF-173 lo revierte si la constancia llega y RF-174 le pone fondo a las 72 horas. Del lado de Elena, RF-178 le deja comprobar antes de viajar si el código que le dictaron sirve, con intentos acotados (RF-179) y contra su identidad (RF-197), **sin que el sistema se lo diga nunca**. La **respuesta del desafío** es lo único que el sistema no transmite a nadie (RF-101). Todo lo demás —aviso, monto, disponibilidad, pregunta del desafío, mala noticia— viaja **por llamada o mensaje de texto a los dos**, porque ninguno origina desde una aplicación | RF-11 · RF-147 · RF-125 · RF-149 · RF-210 · RNF-15 · RF-94 · RF-101 · RF-25 · RF-41 · RF-69 · RF-14 · RF-65 · RF-67 |
| **T6** Cerrar ↔ cerrar de verdad | Rosa ↔ Elena | **A favor de Elena, ahora con ítem que lo diga.** El giro cierra en el momento en que el receptor recibe el dinero, no al fondearse ni al quedar disponible. Y el límite de la cancelación se corre para que Rosa no pueda anular con Elena en la ventanilla: no es «mientras no esté pagado» sino **mientras el dinero no esté a disposición del receptor** — un solo borde y un solo título, desde que RF-110 se retiró por decir lo mismo que RF-46 | RF-64 · RF-65 · RF-46 |
| **T7** El código perdido | Rosa ↔ Elena | **A favor del secreto, con salida, y sin que la salida cueste dos veces.** El código no se reemite nunca (RF-94) — es el «nunca debe» de Rosa y RNF-15 lo hace imposible. Lo que se decide es la salida que faltaba: el emisor **cancela** el giro mientras nadie lo haya cobrado (RF-46) y **lo rehace al mismo receptor** (RF-117), conservando la cotización (RF-134) y **sin volver a pagar comisión** (RF-135, ahora P0 como el rehacer que la necesita). El dinero deja de quedar atrapado hasta prescribir, y el secreto sigue siendo secreto | RF-94 · RF-46 · RF-117 · RF-134 · RF-135 · RNF-15 |

## Reparto de prioridad

| | P0 | P1 | P2 |
|---|---|---|---|
| Funcionales | 184 | 15 | 8 |
| No funcionales | 17 | 3 | 0 |

## Disciplina de alcance

> **Regla de escritura, en vigor desde la ronda 14.** Cada título nuevo **muere en una transferencia
> doméstica entre dos cuentas de banco en la misma moneda**, o lleva escrito por qué no. La razón no
> es estética: el [EVAL](../../evals/README.md) mide en D2 la fracción del backlog que deja de tener
> sentido si el envío no cruza una frontera, y esa fracción bajó tres rondas seguidas —61,3 %,
> 54,9 %, 53,1 %— **sin que nadie empeorara un ítem**. Cayó porque el backlog creció por su mitad
> genérica.
>
> **La ronda 14 declaró que sus «diez» títulos morían los diez. Eran nueve y morían cinco.** La
> corrección de la afirmación es parte de la regla: una disciplina que se autocertifica sin contar no
> es una disciplina. El conteo auditado por el EVAL fue **5 de 9 = 55,6 %**, contra 33 % en la
> ronda 13 — la regla funcionó donde se aplicó y se mintió donde no.
>
> **Ronda 15 — siete títulos nuevos, contados de verdad. Mueren seis:** `RF-196`, `RF-197` y
> `RF-198` dicen «fuera del mostrador», y el mostrador existe porque el último tramo se paga en
> efectivo; `RF-199` nombra el punto de atención; `RF-200` nombra al operario que recibió el
> efectivo; `RF-201` nombra la cotización, que solo existe porque el giro cruza una moneda.
>
> **Uno sobrevive, y la razón se escribe en vez de negarse:** `RF-202` —volver a despachar el aviso
> que el canal reporta como no entregado— vale igual para un giro doméstico. Entra porque `A:139`
> ya lo ejecutaba sin título, y **la regla de dirección obliga a escribirlo arriba antes que a
> tolerarlo abajo**: un huérfano declarado cuesta menos que una decisión sin requerimiento.
>
> **Ronda 16 — once títulos, mueren diez.** `RF-203`, `RF-204`, `RF-205`, `RF-206`, `RF-207` y
> `RF-208` nombran el mostrador o el punto de atención; `RF-209` la cotización; `RF-210` el código;
> `RF-211` el punto de atención; `RF-212` al receptor en el mostrador de destino. **Sobrevive
> `RF-213`** —volver cancelable el giro cuya retención terminó—: una retención por sanciones existe
> igual en una red doméstica, y el título entra porque `RF-182` abría un estado que nada cerraba.
>
> **Ronda 17 — seis títulos nuevos, mueren los seis.** `RF-214` nombra la evidencia de entrega en el
> mostrador; `RF-215` la supresión pedida fuera del mostrador; `RF-217` el código de seguimiento;
> `RF-218` y `RF-219` la identificación del receptor en el mostrador de destino; `RF-220` el giro
> retenido en la ventanilla. **100 %.** El párrafo anterior de esta sección contaba nueve metiendo
> `RF-213` —ya contado en la ronda 16— y dos **ediciones**, `RF-162` y `RF-194`, que la regla no
> llama títulos nuevos. Lo corrigió el EVAL de la ronda 17 y se recuenta acá, que es donde la regla
> vive: **una disciplina que se autocertifica sin contar no es una disciplina**, y ésta ya cometió
> ese error una vez.
>
> **Ronda 18 — seis títulos nuevos, mueren los seis.** `RF-221` («al operario»), `RF-222` (la
> reposición en el mostrador), `RF-223` (devolver al emisor), `RF-224` (el canal de voz), `RF-225`
> (la fotografía del documento en la ventanilla) y `RF-226` (el documento en el mostrador). **100 %
> por segunda ronda consecutiva.**

## Supuestos y ambigüedades

| Marca | Dónde | Estado |
|---|---|---|
| `[ASSUMPTION: modelo Western Union — red de agentes, efectivo contra efectivo, sin cuenta bancaria en ninguna punta]` | Todo el backlog | Vigente — indicación del profesor |
| `[ASSUMPTION: umbral de límites (BR-04) y umbral reforzado (BR-05)]` | RF-08 · RF-09 · RF-13 | Vigente |
| `[ASSUMPTION: umbrales de servicio de RNF-09 a RNF-11]` | RNF-09 · RNF-10 · RNF-11 | Vigente — los consume el paso `E` |
| `[ASSUMPTION: el plazo de prescripción es el que fije el regulador del país de origen; a falta de norma expresa, 12 meses desde la creación]` | RF-49 · RF-50 · RF-51 · BR-14 | **Cerrada** — alineada con BR-14, que lo fija por jurisdicción |
| `[ASSUMPTION: la conservación es el plazo más largo de los dos reguladores del giro, con un piso de 5 años]` | RNF-03 · RF-18 | **Cerrada** en la iteración 03 — el paso `E` ya puede dimensionar |
| `[ASSUMPTION: dos corredores al lanzamiento — Estados Unidos → Perú y Estados Unidos → México]` | RNF-12 · RNF-14 | **Cerrada** — dos monedas destino, para no romper RNF-14 |
| `[ASSUMPTION: la retención dura lo que fije el regulador más estricto de los dos países; a falta de norma expresa, 72 horas]` | RF-31 · RF-32 · RF-96 | **Cerrada** — es el máximo que RF-96 promete informar |
| `[ASSUMPTION: umbral de reporte transfronterizo — USD 10 000 por operación, o el que fije cada regulador si es menor]` | RF-17 · RF-22 · RF-139 | **Cerrada en la iteración 11** — era una cifra sin productor que `E` había inventado |
| `[ASSUMPTION: la ventana del acumulado es de 30 días corridos]` | RF-09 · RF-93 | **Cerrada en la iteración 11** |
| `[ASSUMPTION: la homonimia se resuelve en 24 horas; 3 intentos de desafío; 3 días para descartar la identificación sin giro; 72 horas de custodia; 24 horas de piso para responder un cambio de punto; liquidación al cierre del día hábil siguiente]` | RF-78 · RF-82 · RF-99 · RF-116 · RF-138 · RF-24 | **Cerradas en la iteración 11** — las seis cifras que la ronda 10 encontró sin productor |
| `[ASSUMPTION: la objeción del agente se resuelve en 5 días hábiles de la jurisdicción del punto donde se originó la diferencia]` | RF-153 · RF-184 | **Abierta en la ronda 12, desambiguada en la 13** — «hábiles de cuál de los dos países» era la ambigüedad, y RF-184 dice qué pasa al vencer |
| `[ASSUMPTION: la consulta a una lista externa responde en 60 segundos o el giro no se crea]` | RNF-09 · RF-177 | **Abierta en la ronda 13** — era la única espera con la persona delante y remitía a RNF-11, que mide disponibilidad y no tiempo |
| `[ASSUMPTION: una copia de lista de sanciones con más de 24 horas no está vigente]` | RF-167 · RF-186 | **Abierta en la ronda 13** — la cifra la inventaba `D` y la consumían `E` y `E-escalar` |
| `[ASSUMPTION: 72 horas sin constancia del código devuelven el giro; 3 intentos de comprobar un código; la reposición no retirada dura 12 meses]` | RF-174 · RF-179 · RF-175 · RF-176 | **Abiertas en la ronda 13** — los tres terminadores que faltaban |
| `[ASSUMPTION: el código se tiene por llegado si el canal no reporta fallo en 15 minutos]` | RF-189 | **Abierta en la ronda 14** — era la cifra sin productor de la que colgaban RF-149, RF-173 y RF-174 |
| `[ASSUMPTION: el segundo rol autoriza en 10 minutos o el giro se rechaza]` | RNF-20 · RF-191 | **Abierta en la ronda 14** — el único de los tres plazos de RNF-09 que había quedado sin final |
| `[ASSUMPTION: la cotización no ejecutada deja de ofrecerse a los 10 minutos, salvo la del giro que espera un segundo rol]` | RF-201 · RF-209 | **Abierta en la ronda 15, cerrada en la 16** — los dos relojes de diez minutos chocaban sobre la misma persona en el mostrador |
| `[ASSUMPTION: el reintento de un aviso solo procede si el fallo se reporta dentro de los 15 minutos del despacho]` | RF-189 · RF-202 | **Abierta en la ronda 16** — sin la ventana, un aviso podía ser a la vez llegado y no entregado |
| `[ASSUMPTION: el silencio del canal vale como entrega para todo aviso salvo el que lleva el código]` | RF-189 · RF-217 | **Abierta en la ronda 17** — era la reserva de Rosa: su teléfono está en la cartera y el canal no se queja |
| `[ASSUMPTION: la identificación derivada al rol de cumplimiento se resuelve en 24 horas, y al vencer el giro se devuelve]` | RF-212 · RF-218 · RF-219 · RF-223 | **Abierta en la ronda 17, terminada en la 18** |
| `[ASSUMPTION: toda diferencia declarada se decide en 5 días hábiles de la jurisdicción del punto donde se originó]` | RF-193 · RF-194 | **Abierta en la ronda 14** — el mismo reloj que RF-153 y RF-184 le habían dado al agente y no a la receptora |
| `[ASSUMPTION: la devolución no retirada queda disponible 12 meses desde que quedó disponible, y no hasta la prescripción del giro que la originó]` | RF-89 · RF-137 | **Abierta en la ronda 12** — cierra la devolución que nacía vencida |
| `[ASSUMPTION: la comisión y el margen los fija el sistema y quedan fechados, como la cotización]` | RF-157 · RF-158 | **Abierta en la ronda 12** — eran las dos cifras con lectores y sin productor |

## Identificadores retirados

Un identificador retirado **no se reutiliza**: su número queda muerto. La iteración 05 aprendió por
qué —reusar `RF-02`, `RF-12`, `RF-14`, `RF-37` y `RF-58` produjo una deriva semántica que ningún
`grep` delata, porque el puntero sigue resolviendo a un ítem que dice otra cosa. Los `BR-nn` nunca
cometieron ese error.

| ID | Por qué se retira | Qué lo cubre ahora |
|---|---|---|
| `RF-35` | Duplicado encubierto: decía como comportamiento lo que un invariante ya decía | RNF-05 — «ningún giro registra dos entregas al receptor, en ningún punto y en ningún momento» |
| `RF-62` | Duplicado encubierto: decía como comportamiento lo que un invariante ya decía | RNF-13 — «ningún giro figura simultáneamente devuelto al emisor y entregado al receptor» |
| `RF-55` | Duplicado encubierto: decía como comportamiento lo que un invariante ya decía | RNF-03 — «ningún acto registrado se modifica ni se borra» |
| `RF-38` | Duplicado encubierto: decía como comportamiento lo que un invariante ya decía | RNF-16 — «ninguna entrega difiere de la cifra que el emisor vio antes de entregar su efectivo» |
| `RF-45` | Duplicado encubierto, **por el mismo criterio con que se retiraron los cuatro de arriba** | RNF-05, RNF-06 y RNF-13 — los tres invariantes que ya prohíben pagar, retener y devolver a la vez |
| `RF-58` | Duplicado encubierto: contar el acumulado del receptor está contenido en retenerlo por superarlo, y estaba un escalón de prioridad por debajo | RF-93 |
| `RF-107` | Duplicado encubierto: caso particular de avisar al receptor toda devolución, porque RF-47 hace de la cancelación una devolución | RF-106 vía RF-47 |
| `RF-21` | Duplicado encubierto: caso particular de informar el monto **en moneda destino**, y estaba dos escalones de prioridad por debajo | RF-05 |
| `RF-112` | Duplicado encubierto: no volver a consultar un código está contenido en no poder leerlo | RNF-15 |
| `RF-12` | Duplicado encubierto: comprobar sin mostrar al mostrador está contenido en recibirla del receptor sin que el mostrador pueda leerla, una vez que RNF-17 se extendió al mostrador | RF-114 y RNF-17 |
| `RF-110` | Duplicado encubierto: caso particular de cancelar, con el mismo borde palabra por palabra desde que T6 lo alineó | RF-46 |
| `RF-15` | **Título comodín**, por las tres pruebas de la rúbrica: «aplicar las reglas de los dos reguladores» nombra un área y ningún sistema concreto lo incumple. Lo que decía en serio lo dicen los que nombran el hecho | RF-16 · RF-17 · RF-139 · RF-185 · RF-22 · RF-31 · RF-23 |
| `RF-113` | Duplicado encubierto: «impedirá que quien atiende el mostrador lea o transcriba el código» es, palabra por palabra, la mitad del invariante de `RNF-15`. Es el mismo criterio con que se retiraron `RF-35`, `RF-38`, `RF-45`, `RF-55` y `RF-62` | RNF-15 |
| `RF-126` | Duplicado encubierto: identificar al receptor remoto antes de atenderlo, dicho dos veces por dos disparadores distintos, desde que la ronda 15 escribió un título por disparador | RF-180 · RF-196 · RF-197 · RF-198 |
| `RF-181` | **Número muerto por error de numeración, no por retiro.** Nunca se asignó a ningún título: la ronda 13 saltó de `RF-180` a `RF-182`. Se declara acá porque la tabla existe para que no queden números muertos sin declarar | — |
| `RF-150` | Duplicado encubierto: desde que `RF-220` deja no pagable a **todo** giro retenido, asociar acción ofrecible al retenido es un caso particular de asociarla al no pagable. Mismo criterio con que se retiraron `RF-58`, `RF-112` y `RF-165` | RF-151 vía RF-220 |
| `RF-216` | **Nunca se asignó a ningún título.** La ronda 17 saltó de `RF-215` a `RF-217` y lo declaró en la prosa de «Disciplina de alcance» en vez de acá, que es donde esta tabla promete que estará | — |
| `RF-165` | Duplicado encubierto: dar de baja los cobros anteriores a la ventana está contenido en contar «en la ventana», por el mismo criterio con que se retiraron `RF-58` y `RF-112` | RF-93 |
| `RF-108` | Duplicado encubierto: caso particular de avisar al receptor — y además anunciaba una devolución que ningún título ordena: un cambio de lista **retiene** (RF-29) y la devolución la produce el vencimiento de la retención (RF-32) | RF-37 y RF-106 |
