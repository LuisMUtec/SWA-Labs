# Personas / usuarios modelo

Tres personas, derivadas del enunciado del [Caso de Estudio #3](../docs/LAB-03-ARQ-2026.2.md). El
enunciado no nombra a ninguna, así que las tres están en `status: proto` y toda afirmación inventada
va marcada con `[ASSUMPTION: ...]`. Base para una persona nueva: [`_TEMPLATE.MD`](_TEMPLATE.MD).

| Persona | Archivo | Rol | Qué ancla |
|---|---|---|---|
| **Rosa Quispe** | [`Rosa.MD`](Rosa.MD) | Remitente en Estados Unidos — **usuario modelo** | Que el envío llegue por el monto y en la fecha prometidos |
| Elena Quispe | [`Elena.MD`](Elena.MD) | Destinataria en Huanta, cobra en efectivo | Que el último tramo, el que no tiene pantalla, también cierre |
| Kevin Ramos | [`Operario.MD`](Operario.MD) | Operario de la ventanilla de un agente de la red | La **seguridad** del enunciado —es el vector, no el guardián— y la operación cortada, que pone a prueba la **consistencia** |

## El usuario modelo

> Hint del enunciado: *identifique correctamente quién es el usuario modelo.*

**Es Rosa.** Ella decide usar SendIt o abandonarlo, ella paga, y es la única de las tres que elige
libremente: Elena recibe por donde Rosa mandó y Kevin atiende el mostrador donde Rosa llega. Un
backlog que resuelve el día de Kevin y no el de Rosa describe una red de agentes muy bien
controlada y sin clientes.

Elegirla no la vuelve la única. Es el usuario modelo, no el único usuario, y las otras dos existen
porque **el problema de Rosa no se puede resolver dentro de la pantalla de Rosa**: la promesa que
ella necesita —tantos soles, tal día— la cumple o la rompe Elena en la bodega de Huanta, y la
sostiene o la pierde Kevin en el mostrador, que es donde el efectivo cambia de manos dos veces.

## Cobertura de las dos exigencias del enunciado

| Exigencia | Quién la ancla | Ángulo |
|---|---|---|
| **Seguridad** | Kevin (el vector), Rosa y Elena (la sufren) | Kevin está solo, con efectivo, y puede crear giros y pagarlos: todo mecanismo que no lo contemple protege la puerta equivocada. Rosa vive la retención sin explicación; Elena vive la verificación de identidad del lado donde no hay a quién pedirle ayuda |
| **Consistencia de datos** | Las tres | Rosa: el monto que vio es el que llegó, y no paga dos veces. Elena: no cobra dos veces ni cobra lo devuelto. Kevin: una operación cortada a la mitad queda en un estado único y legible, y reintentarla no duplica nada |

La consistencia no es de nadie en exclusiva y por eso no tiene una persona propia: es la costura
entre las tres. La rúbrica la puntúa aparte, en [D3](../evals/README.md), justamente porque ninguna
persona la ve entera.

## Usuarios que no se modelan, y por qué

| Actor | Por qué no es persona | Dónde aparece igual |
|---|---|---|
| **Tesorería / liquidez del corredor** | Su problema —prefinanciar el corredor, cerrar la posición de cambio— es de la empresa, no del envío. Modelarlo agregaría una cuarta persona cuyo día se resuelve sin tocar el de Rosa | La tasa fijada al pagar, que Rosa exige, es una decisión de exposición cambiaria: se registra en [`D`](../redale/D-disenar-servicio/) |
| **Oficial de cumplimiento** | El tamizaje, la retención y el reporte son responsabilidad del sistema y obligación del negocio, no el día de una persona más. Bajo el modelo Western Union la tercera voz le corresponde al mostrador: es ahí donde el efectivo cambia de manos y donde la seguridad se rompe | Las reglas de cumplimiento están en [`business-rules.md`](../business-rules.md) —BR-04, BR-06, BR-15— y la retención sin explicación se sufre en las tensiones T1 y T2 |
| **Tesorería del corredor pagador** | Quién repone el efectivo de la caja de Kevin y cuándo es un problema de la empresa, no del envío | Aparece como el límite de efectivo que Kevin no controla, y en [`D`](../redale/D-disenar-servicio/) |
| **Soporte al cliente** | Existe hoy porque el sistema no informa. Modelarlo como persona vuelve requisito al síntoma | Cada vez que Rosa «tiene que llamar», eso es un defecto del backlog, no un caso de uso |

## Tensiones

Estos conflictos son deliberados. El backlog tiene que **decidirlos**, no esquivarlos. Un conjunto
de requerimientos que deja conformes a las tres personas a la vez probablemente evitó decidir alguna
de estas — y eso lo cobra [D4](../evals/README.md).

| # | Tensión | Entre | En qué consiste |
|---|---|---|---|
| T1 | Control frente a rapidez | Rosa ↔ Kevin | Cada verificación que Kevin hace es tiempo que Rosa espera con la cola detrás. El control tiene que ocurrir **antes** de que Kevin toque el efectivo; Rosa quiere salir de la ventanilla con su código y una promesa firme |
| T2 | Explicación frente a reserva | Rosa ↔ Kevin | Rosa exige saber por qué se detuvo su dinero. Kevin es la cara de SendIt frente a ella y tiene **prohibido** decírselo cuando hay un reporte de por medio — y ni siquiera es él quien decidió. No se resuelve redactando mejor un mensaje: hay que decidir qué dice Kevin cuando no puede decir nada |
| T3 | Verificación de identidad frente a lo que Elena tiene | Elena ↔ Kevin | Kevin necesita saber quién cobra, y responde con el efectivo de su patrón si se equivoca. Elena tiene un DNI vencido y una foto de hace veinte años, y está del lado donde no hay a quién reclamar. La decisión de pagar o no recae sobre Kevin, que es quien menos debería estar decidiéndola |
| T4 | Certeza del monto frente a exposición cambiaria | Rosa ↔ la empresa | Rosa necesita que el monto en soles se fije al pagar. Fijarlo deja a SendIt cargando el movimiento del tipo de cambio hasta que Elena cobre — que puede ser nunca |
| T5 | El canal de Rosa frente al canal de Elena | Rosa ↔ Elena | Rosa origina en la ventanilla y consulta desde su teléfono; Elena solo tiene llamada y mensaje de texto, y el código se lo pasa Rosa, no SendIt. Todo aviso que dependa de una pantalla deja a Elena afuera, y Elena es quien tiene que decidir si viaja |
| T6 | Cerrar el envío frente a cerrarlo de verdad | Rosa ↔ Elena | Para el sistema es cómodo dar por terminado el envío cuando el dinero llegó al agente. Para Rosa y Elena, termina cuando Elena contó los billetes. Entre esos dos momentos vive el defecto que nadie ve |
| T7 | El código perdido | Rosa ↔ Elena | Rosa **nunca debe** poder recuperar el código por un canal de SendIt, porque eso lo volvería obtenible por quien se haga pasar por ella. Y Elena **no puede cobrar sin él**. Entre las dos cosas no hay término medio: o el secreto se puede reponer y deja de serlo, o el dinero queda atrapado hasta prescribir. La descubrió el EVAL en la iteración 07, después de que dos rondas la revirtieran en direcciones opuestas, cada una por un punto entero de D3 |

## Cómo se usan

Cada persona tiene un agente que la representa en el [EVAL](../evals/README.md) y vive en
[`.claude/agents/`](../.claude/agents/). El agente lee **su** archivo de persona y el
[backlog](../redale/R-requerimientos/backlog.md), y nada más —tampoco
[`business-rules.md`](../business-rules.md), porque una persona sufre los efectos de las reglas y
no conoce el catálogo—: ni las otras personas, ni los
veredictos ajenos, ni el historial.

**Regla de asimetría:** un agente de persona solo puede **restar** de D1, nunca sumar. Su función es
detectar la falla, no certificar el acierto.
