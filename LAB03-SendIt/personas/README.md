# Personas / usuarios modelo

Tres personas, derivadas del enunciado del [Caso de Estudio #3](../docs/LAB-03-ARQ-2026.2.md). El
enunciado no nombra a ninguna, así que las tres están en `status: proto` y toda afirmación inventada
va marcada con `[ASSUMPTION: ...]`. Base para una persona nueva: [`_TEMPLATE.MD`](_TEMPLATE.MD).

| Persona | Archivo | Rol | Qué ancla |
|---|---|---|---|
| **Rosa Quispe** | [`Rosa.MD`](Rosa.MD) | Remitente en Estados Unidos — **usuario modelo** | Que el envío llegue por el monto y en la fecha prometidos |
| Elena Quispe | [`Elena.MD`](Elena.MD) | Destinataria en Huanta, cobra en efectivo | Que el último tramo, el que no tiene pantalla, también cierre |
| Marco Salas | [`Marco.MD`](Marco.MD) | Oficial de cumplimiento de SendIt | La **seguridad** del enunciado, y la retención que pone a prueba la **consistencia** |

## El usuario modelo

> Hint del enunciado: *identifique correctamente quién es el usuario modelo.*

**Es Rosa.** Ella decide usar SendIt o abandonarlo, ella paga, y es la única de las tres que elige
libremente: Elena recibe por donde Rosa mandó y Marco trabaja dentro de la empresa. Un backlog que
resuelve el día de Marco y no el de Rosa describe una casa de cambio con buen cumplimiento y sin
clientes.

Elegirla no la vuelve la única. Es el usuario modelo, no el único usuario, y las otras dos existen
porque **el problema de Rosa no se puede resolver dentro de la pantalla de Rosa**: la promesa que
ella necesita —tantos soles, tal día— la cumple o la rompe Elena en la bodega de Huanta, y la
suspende o la libera Marco.

## Cobertura de las dos exigencias del enunciado

| Exigencia | Quién la ancla | Ángulo |
|---|---|---|
| **Seguridad** | Marco (dueño), Rosa y Elena (la sufren) | Marco tamiza y retiene; Rosa vive la retención sin explicación; Elena vive la verificación de identidad del lado donde no hay a quién pedirle ayuda |
| **Consistencia de datos** | Las tres | Rosa: el monto que vio es el que llegó, y no paga dos veces. Elena: no cobra dos veces ni cobra lo devuelto. Marco: una operación no puede figurar retenida y pagada a la vez |

La consistencia no es de nadie en exclusiva y por eso no tiene una persona propia: es la costura
entre las tres. La rúbrica la puntúa aparte, en [D3](../evals/README.md), justamente porque ninguna
persona la ve entera.

## Usuarios que no se modelan, y por qué

| Actor | Por qué no es persona | Dónde aparece igual |
|---|---|---|
| **Tesorería / liquidez del corredor** | Su problema —prefinanciar el corredor, cerrar la posición de cambio— es de la empresa, no del envío. Modelarlo agregaría una cuarta persona cuyo día se resuelve sin tocar el de Rosa | La tasa fijada al pagar, que Rosa exige, es una decisión de exposición cambiaria: se registra en [`D`](../redale/D-disenar-servicio/) |
| **Agente pagador (el bodeguero)** | No es usuario de SendIt sino de la red pagadora, un tercero. Darle voz de persona haría creer que el diseño puede mandarle | Es la frontera de sistemas que produce el peor defecto de consistencia del caso; aparece en el flujo de Elena y en el de Marco |
| **Soporte al cliente** | Existe hoy porque el sistema no informa. Modelarlo como persona vuelve requisito al síntoma | Cada vez que Rosa «tiene que llamar», eso es un defecto del backlog, no un caso de uso |

## Tensiones

Estos conflictos son deliberados. El backlog tiene que **decidirlos**, no esquivarlos. Un conjunto
de requerimientos que deja conformes a las tres personas a la vez probablemente evitó decidir alguna
de estas — y eso lo cobra [D4](../evals/README.md).

| # | Tensión | Entre | En qué consiste |
|---|---|---|---|
| T1 | Control frente a rapidez | Rosa ↔ Marco | Cada verificación que Marco necesita es tiempo que Rosa espera. Marco quiere tamizar antes de comprometer el dinero; Rosa quiere una promesa firme al pagar |
| T2 | Explicación frente a reserva | Rosa ↔ Marco | Rosa exige saber por qué se detuvo su dinero. Marco tiene **prohibido** decírselo cuando hay un reporte de por medio. No se resuelve redactando mejor un mensaje: hay que decidir qué se le dice a Rosa cuando no se le puede decir nada |
| T3 | Verificación de identidad frente a lo que Elena tiene | Elena ↔ Marco | Marco necesita saber quién cobra. Elena tiene un DNI vencido y una foto de hace veinte años, y está del lado donde no hay a quién reclamar |
| T4 | Certeza del monto frente a exposición cambiaria | Rosa ↔ la empresa | Rosa necesita que el monto en soles se fije al pagar. Fijarlo deja a SendIt cargando el movimiento del tipo de cambio hasta que Elena cobre — que puede ser nunca |
| T5 | El canal de Rosa frente al canal de Elena | Rosa ↔ Elena | Rosa opera en una aplicación; Elena solo tiene llamada y mensaje de texto. Todo aviso que dependa de una pantalla deja a Elena afuera, y Elena es quien tiene que decidir si viaja |
| T6 | Cerrar el envío frente a cerrarlo de verdad | Rosa ↔ Elena | Para el sistema es cómodo dar por terminado el envío cuando el dinero llegó al agente. Para Rosa y Elena, termina cuando Elena contó los billetes. Entre esos dos momentos vive el defecto que nadie ve |

## Cómo se usan

Cada persona tiene un agente que la representa en el [EVAL](../evals/README.md) y vive en
[`.claude/agents/`](../.claude/agents/). El agente lee **su** archivo de persona y el
[backlog](../redale/R-requerimientos/backlog.md), y nada más: ni las otras personas, ni los
veredictos ajenos, ni el historial.

**Regla de asimetría:** un agente de persona solo puede **restar** de D1, nunca sumar. Su función es
detectar la falla, no certificar el acierto.
