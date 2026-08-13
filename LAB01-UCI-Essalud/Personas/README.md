# Personas / Usuarios Modelo

Cuatro personas modelo, derivadas de los usuarios directos identificados en el
[README principal](../README.md#2-usuarios--clientes-del-sistema). Cada una ancla al menos uno de los
problemas críticos del caso. Base para nuevas personas: [`_TEMPLATE.md`](_TEMPLATE.md).

Las cuatro son personal clínico. La justificación de los usuarios directos que no se modelan —entre
ellos el coordinador de TI de red— está en la sección 2.5 del README principal.

| Persona | Archivo | Rol | Problema que ancla | Responsable |
|---|---|---|---|---|
| Rodrigo Salazar | [Rodrigo.MD](Rodrigo.MD) | Médico internista rotante | P1 — Rotación de doctor | |
| Milagros Chávez | [Milagros.MD](Milagros.MD) | Enfermera asistencial UCI, turno noche | P2 — Medianoche · P3 — Tiempo real | |
| Carmen Rojas | [Carmen.MD](Carmen.MD) | Jefa de UCI / coordinadora de turnos | P1 · Horarios sin cruces | |
| Aníbal Quispe | [Anibal.MD](Anibal.MD) | Intensivista de guardia localizable | P2 — Medianoche (receptor) | |

## Cobertura de los problemas críticos

| Problema | Personas involucradas | Ángulo de cada una |
|---|---|---|
| **P1** Rotación de doctor | Rodrigo, Carmen | Rodrigo consume y produce el handoff; Carmen verifica que se cumpla |
| **P2** Medianoche | Milagros, Aníbal | Milagros origina el escalamiento; Aníbal lo recibe fuera del hospital |
| **P3** Tiempo real | Milagros, Aníbal | Milagros depende de la entrega inmediata; Aníbal, del acuse que la cierra |

## Tensiones

Estos conflictos son deliberados: los requerimientos tienen que resolverlos, no ignorarlos. Un
conjunto de requerimientos que deja conforme a las cuatro personas a la vez probablemente esquivó
alguna de estas tensiones en lugar de decidirla.

| Tensión | Entre | En qué consiste |
|---|---|---|
| Velocidad frente a completitud del registro | Rodrigo ↔ Carmen | Rodrigo registra en el mínimo tiempo posible; Carmen necesita un registro completo y auditable |
| Sensibilidad del escalamiento | Milagros ↔ Aníbal | Milagros escala rápido y ante la duda; Aníbal deja de responder si todo le llega como crítico |
| Autonomía de intercambio de turnos | Rodrigo ↔ Carmen | Rodrigo pacta cambios con sus colegas; Carmen responde por la cobertura y necesita aprobarlos |
| Adopción voluntaria | Carmen ↔ Rodrigo, Milagros | Si el sistema estorba, el equipo vuelve al Excel y al WhatsApp, y el registro se degrada |
| Movilidad frente a control de datos | Aníbal ↔ Ley N.° 29733 | Aníbal opera desde su celular personal; la norma restringe la exposición de datos sensibles |
