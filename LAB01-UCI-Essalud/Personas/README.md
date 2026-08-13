# Personas / Usuarios Modelo

Cinco personas modelo, derivadas de los usuarios directos identificados en el
[README principal](../README.md#2-usuarios--clientes-del-sistema). Cada una ancla al menos uno de los
problemas críticos del caso. Base para nuevas personas: [`_TEMPLATE.md`](_TEMPLATE.md).

| Persona | Archivo | Rol | Problema que ancla | Responsable |
|---|---|---|---|---|
| Rodrigo Salazar | [Rodrigo.MD](Rodrigo.MD) | Médico internista rotante | P1 — Rotación de doctor | |
| Milagros Chávez | [Milagros.MD](Milagros.MD) | Enfermera asistencial UCI, turno noche | P2 — Medianoche · P3 — Tiempo real | |
| Carmen Rojas | [Carmen.MD](Carmen.MD) | Jefa de UCI / coordinadora de turnos | P1 · Horarios sin cruces | |
| Aníbal Quispe | [Anibal.MD](Anibal.MD) | Intensivista de guardia localizable | P2 — Medianoche (receptor) | |
| Katherine Ttito | [Katherine.MD](Katherine.MD) | Coordinadora de TI de Red Asistencial | P3 · Metas de rendimiento y escalamiento | |

## Cobertura de los problemas críticos

| Problema | Personas involucradas | Ángulo de cada una |
|---|---|---|
| **P1** Rotación de doctor | Rodrigo, Carmen | Rodrigo consume y produce el handoff; Carmen verifica que se cumpla |
| **P2** Medianoche | Milagros, Aníbal | Milagros origina el escalamiento; Aníbal lo recibe fuera del hospital |
| **P3** Tiempo real | Milagros, Katherine | Milagros depende de la entrega inmediata; Katherine la sostiene a escala |
| **Metas de rendimiento** | Katherine, Milagros | Katherine responde por el SLA; Milagros lo percibe a pie de cama |

## Tensiones entre personas

Estos conflictos son deliberados: los requerimientos tienen que resolverlos, no ignorarlos.

| Tensión | Entre | En qué consiste |
|---|---|---|
| Velocidad vs. completitud del registro | Rodrigo ↔ Carmen | Rodrigo quiere registrar en el mínimo tiempo; Carmen necesita que el registro sea completo y auditable |
| Sensibilidad del escalamiento | Milagros ↔ Aníbal | Milagros quiere escalar rápido y ante la duda; Aníbal deja de responder si todo le llega como crítico |
| Movilidad vs. control de datos | Aníbal ↔ Katherine | Aníbal necesita su celular personal; Katherine responde por la protección de datos sensibles |
| Riqueza funcional vs. parque tecnológico | Rodrigo/Milagros ↔ Katherine | La interfaz útil a pie de cama choca con PCs antiguas y conectividad intermitente |
| Adopción voluntaria | Carmen ↔ todos | Si el sistema estorba, el equipo vuelve al Excel y al WhatsApp, y la data se degrada |
