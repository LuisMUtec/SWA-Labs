# Requerimientos Funcionales

Sistema de Gestión de UCI — Essalud

Forma y verificación: [`docs/CONVENCIONES.md`](../docs/CONVENCIONES.md), secciones 5, 6 y 9.
Este documento es el único insumo de requerimientos que puntúa [`Spec/Eval-Spec.MD`](../Spec/Eval-Spec.MD).
Los términos del dominio se emplean con el significado fijado en [`docs/GLOSARIO.md`](../docs/GLOSARIO.md).

## Convenciones

- **ID:** `RF-‹área›-‹n›`
- **Enunciado:** un patrón EARS con el auxiliar DEBE y el sistema como sujeto.
- **Prioridad:** MUST / SHOULD / COULD. MUST se reserva a lo que, ausente, deja sin resolver un
  problema crítico o deja a una persona sin su tarea crítica.
- **Trazabilidad:** persona que lo motiva y problema crítico al que responde.
- **Criterios de aceptación:** un par Cuando/Entonces por criterio, actor en tercera persona.

| Área | Prefijo |
|---|---|
| Gestión de turnos | `RF-TUR` |
| Diagnósticos y entrega de turno | `RF-DIA` |
| Escalamiento y disponibilidad del médico | `RF-ESC` |
| Registro clínico a pie de cama | `RF-REG` |
| Identidad y accesos | `RF-IAM` |
| Supervisión de la unidad | `RF-SUP` |

Patrones EARS admitidos: ubicuo, de estado (MIENTRAS), de evento (CUANDO), de opción (DONDE),
de borde (SI … ENTONCES) y complejo.

Los plazos que un enunciado invoca —«dentro del plazo definido para la severidad»— se fijan en
[`ReqNoFunc.MD`](ReqNoFunc.MD). El comportamiento pertenece a este documento; el umbral, al otro.

---

## RF-TUR — Gestión de turnos

### RF-TUR-01 — Rechazo de asignación con cruce en la red

**Enunciado:** SI una asignación solapa otro turno vigente del mismo profesional en cualquier sede, ENTONCES el sistema DEBE rechazarla indicando el turno con el que solapa.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional asignado el sábado de 19:00 a 07:00 en la sede A, cuando la coordinadora intenta asignarlo en la misma franja de la sede B, entonces la asignación se rechaza indicando el turno de la sede A.
---

### RF-TUR-02 — Rechazo de asignación fuera de la jornada aplicable

**Enunciado:** SI una asignación infringe una regla de jornada o descanso asociada al vínculo laboral vigente del profesional, ENTONCES el sistema DEBE rechazarla indicando la regla infringida.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional de planta que alcanzó el máximo de horas de su régimen, cuando la coordinadora intenta asignarle otro turno, entonces la asignación se rechaza indicando el máximo aplicable.
- **CA-2** — Dado un rotante con reglas de jornada suministradas por la Red, cuando una asignación infringe su descanso mínimo, entonces la asignación se rechaza indicando la regla del rotante.

---

### RF-TUR-03 — Candidatos elegibles ordenados por rotación

**Enunciado:** CUANDO la coordinadora solicita cobertura para una franja, el sistema DEBE presentar en el orden de rotación vigente de la unidad los profesionales sin solapamiento en ninguna sede de la Red, sin permiso vigente que alcance la franja y con reglas laborales disponibles que permitan la asignación.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una franja descubierta y un profesional con permiso vigente que la abarca, cuando la coordinadora solicita candidatos, entonces ese profesional no figura entre los presentados.
- **CA-2** — Dados dos profesionales elegibles a los que el orden de rotación vigente de la unidad asigna precedencia al segundo, cuando la coordinadora solicita candidatos, entonces el segundo figura antes que el primero.

---

### RF-TUR-04 — Programación vigente única

**Enunciado:** El sistema DEBE mantener una sola programación vigente por unidad y periodo.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una programación vigente, cuando se publica una modificación válida, entonces la modificación pasa a ser la única programación vigente del periodo.
---

### RF-TUR-05 — Aviso de un cambio de programación

**Enunciado:** CUANDO cambia una asignación de la programación vigente, el sistema DEBE avisar a cada profesional incorporado, retirado o trasladado por el cambio.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada la sustitución del profesional de una guardia, cuando se publica el cambio, entonces el profesional retirado y el incorporado reciben el aviso.
- **CA-2** — Dado un cambio que no modifica la asignación de un profesional, cuando se publica, entonces ese profesional no recibe el aviso.

---

### RF-TUR-06 — Intercambio con autorización previa vigente

**Enunciado:** CUANDO dos profesionales proponen un intercambio sin infracciones cubierto por una autorización previa vigente de la coordinadora para ambas asignaciones, el sistema DEBE aplicarlo a la programación vigente sin exigir otra resolución individual.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un intercambio sin infracciones cubierto por una autorización previa vigente de la coordinadora para ambas asignaciones, cuando los dos profesionales lo proponen, entonces la programación vigente incorpora el intercambio sin esperar otra resolución individual.

---

### RF-TUR-07 — Franjas sin responsable asignado

**Enunciado:** CUANDO la coordinadora consulta la cobertura de una unidad para un horizonte, el sistema DEBE presentar las franjas sin profesional asignado con su sede y unidad.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una franja nocturna sin profesional durante los próximos siete días, cuando la coordinadora consulta ese horizonte, entonces la franja figura con su sede y unidad.
- **CA-2** — Dado un horizonte con todas sus franjas asignadas, cuando la coordinadora consulta la cobertura, entonces no se presenta ninguna franja descubierta.

---

### RF-TUR-08 — Programación como fuente oficial

**Enunciado:** El sistema DEBE conservar la programación vigente como única fuente editable de asignaciones de la unidad.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen, Rodrigo, Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una copia imprimible de la programación, cuando una asignación cambia, entonces la copia no puede modificar ni reemplazar la programación vigente.

---

### RF-TUR-09 — Elaboración de la programación mensual

**Enunciado:** CUANDO la coordinadora inicia la programación mensual de una unidad, el sistema DEBE crear una propuesta con todas las franjas de cobertura requeridas para el periodo.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un mes con cobertura de 24 horas, cuando la coordinadora inicia su programación, entonces la propuesta contiene todas las franjas requeridas del mes.

---

### RF-TUR-10 — Publicación de la programación

**Enunciado:** CUANDO la coordinadora publica una propuesta completa y sin infracciones, el sistema DEBE convertirla en la programación vigente de la unidad.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una propuesta con todas las franjas asignadas y sin infracciones, cuando la coordinadora la publica, entonces pasa a ser la programación vigente.
---

### RF-TUR-11 — Asignación de un profesional a una franja

**Enunciado:** CUANDO la coordinadora selecciona un candidato elegible para una franja, el sistema DEBE registrar su asignación en la propuesta de programación.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una franja descubierta y un candidato elegible, cuando la coordinadora lo selecciona, entonces queda asignado a esa franja en la propuesta.

---

### RF-TUR-12 — Resolución de permisos

**Enunciado:** CUANDO la coordinadora aprueba o rechaza una solicitud de permiso, el sistema DEBE registrar la resolución con su autoría, motivo e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una solicitud de permiso pendiente, cuando la coordinadora la aprueba, entonces la resolución aprobada queda registrada con autoría, motivo e instante.
- **CA-2** — Dada una solicitud de permiso pendiente, cuando la coordinadora la rechaza, entonces la resolución rechazada queda registrada con autoría, motivo e instante.

---

### RF-TUR-13 — Aprobación de una autorización reutilizable de intercambio

**Enunciado:** CUANDO la coordinadora aprueba una autorización reutilizable para intercambios de un alcance y periodo definidos, el sistema DEBE registrarla como vigente para ese alcance y periodo.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una propuesta de autorización reutilizable para intercambios de guardias nocturnas de una unidad durante un mes, cuando la coordinadora la aprueba, entonces la autorización queda vigente para ese alcance y periodo.

---

### RF-TUR-14 — Historial de cambios de programación

**Enunciado:** CUANDO cambia la programación vigente, el sistema DEBE conservar la versión desplazada con la autoría y el instante del cambio.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una programación vigente, cuando un cambio la desplaza, entonces la versión desplazada permanece conservada con la autoría y el instante del cambio.

---

### RF-TUR-15 — Confirmación de lectura de un cambio de programación

**Enunciado:** CUANDO un profesional consulta el detalle de un cambio de programación que lo afecta, el sistema DEBE registrar la confirmación de lectura con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional afectado por un cambio de programación, cuando consulta el detalle del cambio, entonces la confirmación de lectura queda registrada con su autoría e instante.

---

### RF-TUR-16 — Copia histórica de una programación cerrada

**Enunciado:** CUANDO la coordinadora obtiene una copia imprimible de un periodo cerrado, el sistema DEBE generarla como archivo histórico identificando unidad, periodo, instante de generación y su condición no operativa.

| Campo | Valor |
|---|---|
| Prioridad | COULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una programación de un periodo cerrado, cuando la coordinadora obtiene su copia imprimible, entonces la copia coincide con sus asignaciones e identifica unidad, periodo, instante de generación y su condición no operativa.

---

### RF-TUR-17 — Rechazo de una autorización reutilizable de intercambio

**Enunciado:** CUANDO la coordinadora rechaza una autorización reutilizable propuesta para intercambios, el sistema DEBE registrar el rechazo con su alcance, periodo, motivo, autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una autorización reutilizable propuesta para intercambios de guardias nocturnas, cuando la coordinadora la rechaza, entonces el rechazo queda registrado con alcance, periodo, motivo, autoría e instante.

---

### RF-TUR-18 — Registro de una ausencia imprevista

**Enunciado:** CUANDO la coordinadora registra la ausencia imprevista de un profesional, el sistema DEBE conservar al profesional, el intervalo afectado, el motivo, la autoría y el instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una guardia vigente y el descanso médico imprevisto del profesional asignado, cuando la coordinadora registra la ausencia, entonces quedan conservados el profesional, el intervalo afectado, el motivo, la autoría y el instante.

---

### RF-TUR-19 — Retiro de la asignación de un profesional ausente

**Enunciado:** CUANDO se registra una ausencia imprevista que alcanza una asignación vigente, el sistema DEBE retirar al profesional ausente de esa asignación durante el intervalo afectado.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional asignado a la guardia del sábado y una ausencia que cubre esa guardia, cuando se registra la ausencia, entonces el profesional queda retirado de esa asignación durante el intervalo afectado.

---

### RF-TUR-20 — Solicitud de cobertura al candidato seleccionado

*Corrección de coherencia exigida por la brecha 20: si la asignación pasa a producirse con la
aceptación del candidato (`RF-TUR-35`), el enunciado anterior —«asignarlo directamente»— abría un
segundo camino a la misma asignación y contradecía al nuevo. Este bloque conserva el disparador
original y traslada su respuesta al acto que faltaba.*

**Enunciado:** CUANDO la coordinadora selecciona un candidato elegible para una franja descubierta de la programación vigente, el sistema DEBE dirigirle una solicitud de cobertura con exactamente la sede, la unidad y el intervalo de esa franja.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una guardia vigente descubierta por una ausencia y un candidato elegible, cuando la coordinadora lo selecciona, entonces el candidato recibe la solicitud de cobertura con la sede, la unidad y el intervalo de esa guardia.

---

### RF-TUR-21 — Vigencia de un permiso aprobado

**Enunciado:** CUANDO la coordinadora aprueba una solicitud de permiso, el sistema DEBE registrar el permiso como vigente durante todo el intervalo autorizado desde el instante de la aprobación.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una solicitud de permiso para el sábado presentada por un profesional, cuando la coordinadora la aprueba el viernes, entonces el permiso figura vigente para todo su intervalo desde ese instante.

---

### RF-TUR-22 — Asignaciones alcanzadas por un permiso aprobado

**Enunciado:** CUANDO entra en vigencia un permiso aprobado que alcanza una asignación vigente, el sistema DEBE retirar al profesional de esa asignación durante el intervalo autorizado.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un permiso aprobado que cubre una guardia asignada, cuando comienza su vigencia, entonces el profesional queda retirado de esa asignación durante el intervalo autorizado.

---

### RF-TUR-23 — Elegibilidad del profesional rotante

**Enunciado:** CUANDO la Red comunica el alta o el retiro de un profesional rotante, el sistema DEBE actualizar su elegibilidad para el periodo efectivo comunicado.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un rotante retirado por la Red desde el viernes, cuando la Red comunica el retiro, entonces su elegibilidad deja de estar vigente desde ese día.

---

### RF-TUR-24 — Asignaciones de un rotante retirado

**Enunciado:** CUANDO la Red comunica el retiro de un profesional rotante desde un instante efectivo que alcanza asignaciones vigentes, el sistema DEBE retirarlo de esas asignaciones desde ese instante.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un rotante con una guardia asignada el sábado, cuando la Red comunica su retiro desde el viernes, entonces queda retirado de esa guardia desde el instante efectivo.

---

### RF-TUR-25 — Confirmaciones pendientes de un cambio urgente

**Enunciado:** CUANDO la coordinadora consulta un cambio urgente publicado, el sistema DEBE presentar a cada profesional afectado con su confirmación de lectura o su estado pendiente.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un cambio urgente que afecta a dos profesionales y solo uno lo consultó, cuando la coordinadora revisa el cambio, entonces obtiene al primero con su confirmación de lectura y al segundo con estado pendiente.

---

### RF-TUR-26 — Reiteración de un cambio urgente sin confirmar

**Enunciado:** SI un profesional no confirma la lectura de un cambio urgente dentro del plazo definido, ENTONCES el sistema DEBE reiterarle el aviso por los medios de contacto vigentes.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional afectado por un cambio urgente sin confirmación de lectura, cuando vence el plazo definido, entonces recibe otra vez el aviso por sus medios de contacto vigentes.

---

### RF-TUR-27 — Consulta de la programación vigente

**Enunciado:** CUANDO un profesional consulta la programación de una unidad para un periodo, el sistema DEBE presentar las asignaciones de la programación vigente de esa unidad en ese periodo con exactamente la franja, el profesional asignado y la sede.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una unidad con programación vigente publicada para el mes en curso, cuando la coordinadora consulta ese periodo, entonces obtiene sus asignaciones con la franja, el profesional asignado y la sede.
- **CA-2** — Dada una programación vigente que reemplazó a la anterior durante el mes, cuando un profesional de la unidad consulta ese periodo, entonces obtiene las asignaciones de la programación vigente.

---

### RF-TUR-28 — Copia imprimible de la programación vigente

**Enunciado:** CUANDO la coordinadora solicita una copia imprimible de la programación vigente, el sistema DEBE entregarla con exactamente la unidad, el periodo, las asignaciones vigentes en el instante de su generación, ese instante y su condición de reflejo no editable de la programación vigente.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada la programación vigente del mes en curso, cuando la coordinadora solicita su copia imprimible, entonces obtiene una copia con la unidad, el periodo y las asignaciones vigentes en el instante de su generación.
- **CA-2** — Dada una copia imprimible ya obtenida y una programación vigente modificada después, cuando la coordinadora solicita otra copia, entonces obtiene una copia que declara su propio instante de generación y su condición de reflejo no editable.

---

### RF-TUR-29 — Presentación de una solicitud de permiso

**Enunciado:** CUANDO un profesional presenta una solicitud de permiso, el sistema DEBE registrarla como pendiente de resolución con exactamente el profesional solicitante, el intervalo solicitado, el motivo y el instante de presentación.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional asignado a la unidad, cuando presenta una solicitud de permiso para el sábado, entonces la solicitud queda pendiente de resolución con el solicitante, el intervalo solicitado, el motivo y el instante de presentación.

---

### RF-TUR-30 — Solicitudes de permiso pendientes de resolución

**Enunciado:** CUANDO la coordinadora consulta las solicitudes de permiso pendientes de resolución de su unidad, el sistema DEBE presentarlas con exactamente el profesional solicitante, el intervalo solicitado, el motivo y el instante de presentación.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dadas dos solicitudes de permiso pendientes de resolución y una ya resuelta en la misma unidad, cuando la coordinadora consulta las pendientes, entonces obtiene las dos pendientes con el solicitante, el intervalo solicitado, el motivo y el instante de presentación.

---

### RF-TUR-31 — Propuesta de intercambio sin autorización previa

**Enunciado:** CUANDO dos profesionales proponen un intercambio de sus asignaciones que ninguna autorización previa vigente cubre, el sistema DEBE registrarlo como pendiente de resolución de la coordinadora con exactamente las dos asignaciones, los dos profesionales y el instante de la propuesta.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dados dos profesionales con guardias asignadas y sin autorización previa vigente que cubra su intercambio, cuando ambos lo proponen, entonces el intercambio queda pendiente de resolución de la coordinadora con las dos asignaciones, los dos profesionales y el instante de la propuesta.

---

### RF-TUR-32 — Aprobación de un intercambio propuesto

**Enunciado:** CUANDO la coordinadora aprueba un intercambio pendiente de resolución y sin infracciones, el sistema DEBE incorporarlo a la programación vigente.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un intercambio pendiente de resolución entre dos guardias asignadas y sin infracciones, cuando la coordinadora lo aprueba, entonces la programación vigente incorpora el intercambio.

---

### RF-TUR-33 — Rechazo de un intercambio propuesto

**Enunciado:** CUANDO la coordinadora rechaza un intercambio pendiente de resolución, el sistema DEBE avisar a los dos profesionales proponentes con exactamente las dos asignaciones, el motivo y el instante del rechazo.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un intercambio pendiente de resolución propuesto por dos profesionales, cuando la coordinadora lo rechaza, entonces ambos proponentes reciben el aviso con las dos asignaciones, el motivo y el instante del rechazo.

---

### RF-TUR-34 — Aviso del intercambio aplicado sin resolución individual

**Enunciado:** CUANDO un intercambio cubierto por una autorización previa vigente se incorpora a la programación vigente, el sistema DEBE avisar a la coordinadora de la unidad con exactamente las dos asignaciones intercambiadas, los dos profesionales y la autorización que lo amparó.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un intercambio amparado por una autorización previa vigente de la coordinadora, cuando los dos profesionales lo proponen, entonces la coordinadora recibe el aviso con las dos asignaciones intercambiadas, los dos profesionales y la autorización que lo amparó.

---

### RF-TUR-35 — Asignación tras la aceptación de la cobertura

**Enunciado:** CUANDO el candidato acepta una solicitud de cobertura, el sistema DEBE asignarlo a la franja de esa solicitud en la programación vigente.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un candidato con una solicitud de cobertura para la guardia del sábado, cuando la acepta, entonces queda asignado a esa guardia en la programación vigente.

---

### RF-TUR-36 — Rechazo de la cobertura solicitada

**Enunciado:** CUANDO el candidato rechaza una solicitud de cobertura, el sistema DEBE avisar a la coordinadora con exactamente el candidato, la franja y el instante del rechazo.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un candidato con una solicitud de cobertura para la guardia del sábado, cuando la rechaza, entonces la coordinadora recibe el aviso con el candidato, esa guardia y el instante del rechazo.

---

### RF-TUR-37 — Franja sin ningún profesional elegible

**Enunciado:** SI ningún profesional resulta elegible para la franja cuya cobertura solicita la coordinadora, ENTONCES el sistema DEBE presentarle, por cada profesional evaluado, la condición de elegibilidad que lo excluyó.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una franja para la que un profesional queda excluido por permiso vigente y el otro por solapamiento en otra sede, cuando la coordinadora solicita su cobertura, entonces obtiene por cada profesional evaluado la condición que lo excluyó.

---

### RF-TUR-38 — Condición de urgencia de un cambio de programación

**Enunciado:** CUANDO se incorpora a la programación vigente un cambio que alcanza una franja cuyo inicio queda dentro del horizonte definido para la urgencia, el sistema DEBE registrarlo como cambio urgente.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una guardia cuyo inicio queda dentro del horizonte definido para la urgencia, cuando la coordinadora publica un cambio que la alcanza, entonces el cambio queda registrado como cambio urgente.
- **CA-2** — Dada una guardia cuyo inicio queda fuera del horizonte definido para la urgencia, cuando la coordinadora publica un cambio que la alcanza, entonces el cambio no queda registrado como cambio urgente.

---

### RF-TUR-39 — Vencimiento de una solicitud de cobertura sin respuesta

**Enunciado:** SI el candidato no acepta ni rechaza una solicitud de cobertura dentro del plazo definido, ENTONCES el sistema DEBE dejarla sin efecto.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un candidato con una solicitud de cobertura para la guardia del sábado, cuando vence el plazo definido sin que la acepte ni la rechace, entonces la solicitud queda sin efecto.
- **CA-2** — Dada una solicitud de cobertura que quedó sin efecto por vencimiento, cuando el candidato la acepta después, entonces no queda asignado a esa guardia.

---

### RF-TUR-40 — Aviso del vencimiento de una solicitud de cobertura

**Enunciado:** CUANDO una solicitud de cobertura queda sin efecto por vencimiento del plazo definido, el sistema DEBE avisar a la coordinadora con exactamente el candidato, la franja y el instante del vencimiento.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una solicitud de cobertura para la guardia del sábado que venció sin respuesta, cuando queda sin efecto, entonces la coordinadora recibe el aviso con el candidato, esa guardia y el instante del vencimiento.

---

### RF-TUR-41 — Orden de rotación vigente de la unidad

**Enunciado:** CUANDO la coordinadora define el orden de rotación de los profesionales de su unidad para un periodo, el sistema DEBE registrarlo como el orden de rotación vigente de esa unidad en ese periodo.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una unidad sin orden de rotación definido para el mes, cuando la coordinadora define el orden de sus profesionales, entonces ese orden queda vigente para la unidad en ese periodo.
- **CA-2** — Dado un orden de rotación vigente para el mes y otro que la coordinadora define después para el mismo periodo, cuando lo define, entonces el orden vigente de esa unidad en ese periodo es el segundo.

---

## RF-DIA — Diagnósticos y entrega de turno

### RF-DIA-01 — Bloqueo del cierre de turno sin diagnóstico vigente

**Enunciado:** SI un turno médico con asignación médica vigente finaliza con alguna de esas camas sin diagnóstico vigente, ENTONCES el sistema DEBE impedir el cierre de su entrega.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Carmen, Aníbal |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un médico con cuatro camas de asignación médica vigente y diagnóstico vigente en tres de ellas, cuando ese médico intenta cerrar su entrega de turno, entonces la entrega no queda cerrada.
- **CA-2** — Dado un médico de guardia localizable sin asignación médica vigente de camas, cuando su turno finaliza, entonces el cierre de su entrega no queda impedido.

---

### RF-DIA-02 — Contenido de la entrega médica

**Enunciado:** CUANDO un médico inicia un turno, el sistema DEBE presentar por cada cama asignada exactamente el diagnóstico vigente, las decisiones clínicas previas con su fundamento, el esquema terapéutico vigente con su día de tratamiento, los pendientes críticos y el estado de la información a la familia.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una cama cuyo turno anterior decidió no escalar el soporte ventilatorio y registró su fundamento, cuando el médico entrante inicia el turno, entonces esa decisión y su fundamento figuran en la entrega de esa cama.
- **CA-2** — Dada una cama en el tercer día de un antimicrobiano, cuando el médico entrante inicia el turno, entonces el esquema y su tercer día figuran en la entrega.
- **CA-3** — Dada una cama con un cultivo pendiente y la familia aún no informada, cuando el médico entrante inicia el turno, entonces ambos estados figuran en los campos correspondientes de la entrega.

---

### RF-DIA-03 — Señalamiento de camas sin diagnóstico previo

**Enunciado:** SI una cama asignada carece de diagnóstico del turno anterior, ENTONCES el sistema DEBE señalarla antes de la aceptación de la entrega médica.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una cama sin diagnóstico previo, cuando el médico entrante recibe la entrega, entonces esa cama aparece señalada antes de cualquier aceptación.
- **CA-2** — Dada una entrega cuyas camas tienen diagnóstico previo, cuando el médico entrante la recibe, entonces ninguna aparece señalada por ausencia de diagnóstico.

---

### RF-DIA-04 — Firma de la entrega con autoría e instante

**Enunciado:** CUANDO el médico saliente firma la entrega, el sistema DEBE registrar la firma con la identidad verificada del médico y el instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una entrega de turno completa, cuando el médico saliente la firma, entonces la firma queda registrada con la identidad verificada del médico y el instante.

---

### RF-DIA-05 — Cambios desde el último contacto del profesional

**Enunciado:** CUANDO un médico consulta una cama, el sistema DEBE presentar exactamente los cambios de diagnóstico, esquema terapéutico, soporte ventilatorio, soporte vasoactivo, resultados de laboratorio y pendientes ocurridos desde el último contacto de ese médico con esa cama.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un médico cuyo último contacto con una cama ocurrió tres semanas antes, cuando ese médico consulta esa cama, entonces obtiene exactamente los cambios de diagnóstico, esquema terapéutico, soporte ventilatorio, soporte vasoactivo, resultados de laboratorio y pendientes ocurridos desde ese contacto.
- **CA-2** — Dado un médico sin ningún contacto anterior con una cama cuyo episodio se abrió tres semanas antes, cuando ese médico consulta esa cama, entonces obtiene exactamente los cambios de diagnóstico, esquema terapéutico, soporte ventilatorio, soporte vasoactivo, resultados de laboratorio y pendientes ocurridos desde la apertura de ese episodio.

---

### RF-DIA-06 — Marca de inestabilidad y pendiente crítico

**Enunciado:** CUANDO un profesional marca una cama como inestable o con pendiente crítico, el sistema DEBE mantener esa marca vigente sobre la cama hasta que un profesional la retire con su autoría.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una cama que el médico del turno anterior marcó como inestable, cuando la enfermera de turno consulta esa cama, entonces la marca figura vigente.
- **CA-2** — Dada una cama marcada como inestable, cuando una profesional de enfermería retira la marca, entonces la marca deja de figurar vigente con la autoría de esa enfermera.

---

### RF-DIA-07 — Registro de evolución y diagnóstico

**Enunciado:** CUANDO un médico registra una nota de evolución y un diagnóstico para un episodio, el sistema DEBE incorporarlos como una nueva versión con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio abierto, cuando el médico registra su nota y diagnóstico, entonces ambos quedan incorporados como una nueva versión con la autoría e instante del médico.
---

### RF-DIA-08 — Entrega de turno de enfermería

**Enunciado:** CUANDO una profesional de enfermería concluye su turno, el sistema DEBE componer su entrega reutilizando sin transcripción exactamente los pendientes de cuidado abiertos, los eventos, la medicación administrada, los signos vitales y el balance hídrico ya registrados durante el turno.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una enfermera con pendientes de cuidado, eventos, medicación, signos vitales y balance hídrico registrados durante su turno, cuando concluye el turno, entonces su entrega queda compuesta con esos datos ya registrados sin transcribirlos.

---

### RF-DIA-09 — Aceptación de la entrega médica

**Enunciado:** CUANDO el médico entrante acepta una entrega recibida, el sistema DEBE registrar la aceptación con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una entrega recibida por el médico entrante, cuando la acepta, entonces la aceptación queda registrada con su autoría e instante.

---

### RF-DIA-10 — Disponibilidad de la entrega médica

**Enunciado:** CUANDO el médico entrante inicia su turno y existe una entrega cerrada del turno inmediatamente anterior, el sistema DEBE presentarle esa entrega de cada cama asignada sin depender de la presencia del médico saliente.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una entrega cerrada del turno inmediatamente anterior y el médico saliente ausente, cuando el entrante inicia su turno, entonces obtiene esa entrega de cada cama asignada.

---

### RF-DIA-11 — Recepción de la entrega de enfermería

**Enunciado:** CUANDO una profesional de enfermería inicia su turno, el sistema DEBE presentarle exactamente los pendientes de cuidado abiertos, los eventos, la medicación administrada, los signos vitales y el balance hídrico de la última entrega cerrada de las camas de su asignación de cuidado de enfermería vigente, reutilizando los registros existentes sin transcripción.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una entrega de enfermería cerrada del turno anterior, cuando la enfermera entrante inicia su turno, entonces obtiene sus pendientes de cuidado abiertos, eventos, medicación administrada, signos vitales y balance hídrico sin transcribirlos.

---

### RF-DIA-12 — Causa de un cierre de entrega bloqueado

**Enunciado:** CUANDO se bloquea un intento de cierre de entrega médica, el sistema DEBE presentar cada cama que lo impide con el dato obligatorio ausente.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una entrega con dos camas sin diagnóstico vigente, cuando se bloquea su intento de cierre, entonces ambas camas se presentan con el diagnóstico como dato obligatorio ausente.

---

### RF-DIA-13 — Registro de una decisión clínica fundamentada

**Enunciado:** CUANDO un médico registra una decisión clínica para un episodio, el sistema DEBE incorporarla con su fundamento, autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Aníbal |
| Problema | P1, P2 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio en el que el médico decide no escalar el soporte ventilatorio, cuando registra la decisión, entonces queda incorporada con su fundamento, autoría e instante.

---

### RF-DIA-14 — Registro del esquema terapéutico y su día

**Enunciado:** CUANDO un médico registra o modifica un esquema terapéutico, el sistema DEBE incorporarlo con su fecha de inicio, día de tratamiento, autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un antimicrobiano iniciado dos días antes, cuando el médico registra el esquema vigente, entonces queda incorporado con la fecha de inicio, el tercer día de tratamiento, la autoría y el instante.

---

### RF-DIA-15 — Registro del estado de información a la familia

**Enunciado:** CUANDO un médico registra el estado de información a la familia de un episodio, el sistema DEBE incorporarlo con el estado comunicado o pendiente, el motivo, la autoría y el instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio cuya familia aún no fue informada, cuando el médico registra ese estado, entonces queda incorporado como pendiente con el motivo, la autoría y el instante.

---

### RF-DIA-16 — Registro del plan clínico

**Enunciado:** CUANDO un médico registra el plan clínico de un episodio, el sistema DEBE incorporarlo con las acciones previstas, su horizonte, la autoría y el instante.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio que requiere reevaluación en seis horas, cuando el médico registra el plan, entonces queda incorporado con la acción prevista, el horizonte de seis horas, la autoría y el instante.

---

### RF-DIA-17 — Ausencia de entrega del turno inmediatamente anterior

**Enunciado:** SI el turno inmediatamente anterior concluyó sin una entrega cerrada, ENTONCES el sistema DEBE presentar al médico entrante un estado de entrega ausente que diferencie expresamente cualquier entrega más antigua.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un turno concluido sin entrega cerrada y una entrega de un turno anterior, cuando el médico entrante inicia su turno, entonces obtiene el estado de entrega ausente con la entrega antigua identificada expresamente como no vigente.

---

### RF-DIA-18 — Asignación médica de camas para un turno

**Enunciado:** CUANDO la coordinadora asigna camas de una unidad a un profesional médico con asignación vigente para una franja, el sistema DEBE registrar esas camas como asignación médica vigente de ese profesional durante ese turno.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una unidad de diez camas y un médico con asignación vigente para la guardia nocturna, cuando la coordinadora le asigna cuatro de esas camas, entonces esas cuatro figuran como su asignación médica vigente durante esa guardia.

---

### RF-DIA-19 — Asignación de cuidado de enfermería de camas para un turno

**Enunciado:** CUANDO la coordinadora asigna camas de una unidad a una profesional de enfermería con asignación vigente para una franja, el sistema DEBE registrar esas camas como asignación de cuidado de enfermería vigente de esa profesional durante ese turno.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una unidad de diez camas y una enfermera con asignación vigente para el turno noche, cuando la coordinadora le asigna tres de esas camas, entonces esas tres figuran como su asignación de cuidado de enfermería vigente durante ese turno.

---

### RF-DIA-20 — Cierre de la entrega médica

**Enunciado:** CUANDO el médico saliente firma una entrega cuyas camas cuentan todas con diagnóstico vigente, el sistema DEBE registrar esa entrega como entrega cerrada de su turno.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un médico con cuatro camas asignadas y diagnóstico vigente en las cuatro, cuando ese médico firma su entrega, entonces la entrega figura como entrega cerrada de su turno.

---

### RF-DIA-21 — Consulta del fundamento clínico de una cama durante el turno

**Enunciado:** MIENTRAS un turno médico está en curso, CUANDO el médico consulta una cama de su asignación médica vigente, el sistema DEBE presentar exactamente las decisiones clínicas registradas con su fundamento, el esquema terapéutico vigente con su día de tratamiento y el estado de la información a la familia de esa cama.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una cama en el tercer día de un antimicrobiano, cuyo turno diurno decidió no escalar el soporte ventilatorio y cuya familia aún no fue informada, cuando el médico de guardia consulta esa cama a mitad de su turno, entonces obtiene exactamente esa decisión con su fundamento, el esquema con su tercer día y el estado pendiente de la información a la familia.

---

### RF-DIA-22 — Consulta de las camas marcadas de una unidad

**Enunciado:** CUANDO un profesional consulta las camas marcadas de una unidad, el sistema DEBE presentar exactamente las camas de esa unidad con marca vigente de inestabilidad o de pendiente crítico.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una unidad con dos camas marcadas como inestables y ocho sin marca, cuando el médico de guardia consulta las camas marcadas de esa unidad a mitad de su turno, entonces obtiene exactamente esas dos.

---

### RF-DIA-23 — Presentación al médico del cuidado registrado por enfermería

**Enunciado:** CUANDO un médico consulta una cama de su asignación médica vigente, el sistema DEBE presentar exactamente los eventos clínicos y la medicación administrada que enfermería registró sobre esa cama durante el turno en curso.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo, Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una cama sobre la que la enfermera de turno registró un episodio de hipotensión y dos dosis administradas, cuando el médico de guardia consulta esa cama, entonces obtiene exactamente ese evento y esas dos administraciones.

---

### RF-DIA-24 — Turno concluido sin entrega cerrada

**Enunciado:** SI un turno médico concluye sin que su entrega quede cerrada, ENTONCES el sistema DEBE advertir a la jefatura de la unidad identificando ese turno y cada cama sin diagnóstico vigente.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un turno médico con una cama sin diagnóstico vigente cuyo intento de cierre quedó impedido, cuando ese turno concluye, entonces la jefatura de la unidad queda advertida con ese turno y esa cama identificados.

---

### RF-DIA-25 — Apertura de un pendiente de cuidado de enfermería

**Enunciado:** CUANDO una profesional de enfermería registra un pendiente de cuidado sobre una cama de su asignación de cuidado de enfermería vigente, el sistema DEBE incorporarlo al episodio como pendiente abierto con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con episodio abierto, cuando la enfermera de turno registra sobre ella un pendiente de curación, entonces ese pendiente integra el episodio como abierto con su autoría e instante.

---

### RF-DIA-26 — Resolución de un pendiente de cuidado de enfermería

**Enunciado:** CUANDO una profesional de enfermería da por resuelto un pendiente de cuidado abierto, el sistema DEBE registrarlo como pendiente resuelto con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un pendiente de curación abierto sobre una cama, cuando la enfermera de turno lo da por resuelto, entonces ese pendiente figura como resuelto con su autoría e instante.

---

### RF-DIA-27 — Cierre de la entrega de enfermería

**Enunciado:** CUANDO una profesional de enfermería firma su entrega de turno, el sistema DEBE registrar el cierre de esa entrega con su identidad verificada y el instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una entrega de enfermería compuesta al concluir el turno, cuando la enfermera saliente la firma, entonces el cierre de esa entrega queda registrado con su identidad verificada y el instante.

---

## RF-ESC — Escalamiento y disponibilidad del médico

### RF-ESC-01 — Escalamiento al responsable clínico vigente

**Enunciado:** CUANDO un profesional de enfermería escala un deterioro clínico de una cama, el sistema DEBE alcanzar al responsable clínico vigente de esa cama.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con responsable clínico vigente, cuando la enfermera escala un deterioro de esa cama, entonces ese responsable queda alcanzado.
- **CA-2** — Dada una cama cuyo responsable clínico difiere del publicado en la programación inicial del mes, cuando la enfermera escala un deterioro de esa cama, entonces queda alcanzado el responsable vigente en ese instante.

---

### RF-ESC-02 — Escalamiento automático por falta de acuse

**Enunciado:** SI el destinatario alcanzado no acusa recibo dentro del plazo definido para la severidad del escalamiento, ENTONCES el sistema DEBE alcanzar al siguiente integrante de la cadena sin intervención de quien escaló.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento emitido al responsable clínico vigente, cuando transcurre el plazo de acuse de esa severidad sin que él acuse, entonces el siguiente integrante de la cadena queda alcanzado sin que la enfermera realice acción alguna.
- **CA-2** — Dado un escalamiento emitido, cuando el destinatario acusa dentro del plazo, entonces ningún integrante posterior de la cadena queda alcanzado.

---

### RF-ESC-03 — Contexto clínico adjunto al escalamiento

**Enunciado:** CUANDO el sistema emite un escalamiento, el sistema DEBE adjuntar exactamente la identificación inequívoca del paciente; la sede, unidad, cama y episodio; el motivo; seis horas de signos vitales; el balance hídrico; el soporte vasoactivo con dosis; el modo, frecuencia, volumen corriente, PEEP y FiO2 del ventilador; el esquema antimicrobiano con su día; los resultados de laboratorio de las últimas seis horas incluido el lactato más reciente; la última evolución; y la última decisión médica con su fundamento.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio con vasopresor en curso, cuando el sistema emite un escalamiento de esa cama, entonces el escalamiento incluye ese vasopresor con su dosis.
- **CA-2** — Dada una cama con ventilación mecánica, una decisión diurna fundamentada y un lactato reciente, cuando se emite un escalamiento, entonces incluye la identificación inequívoca del paciente, los cinco parámetros ventilatorios, la decisión con su fundamento y el lactato.

---

### RF-ESC-04 — Registro del acuse de recibo

**Enunciado:** CUANDO el destinatario de un escalamiento acusa recibo, el sistema DEBE registrar el acuse con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento emitido, cuando el médico alcanzado acusa recibo, entonces el acuse queda registrado con su autoría e instante.

---

### RF-ESC-05 — Estado de la cadena mientras el escalamiento sigue abierto

**Enunciado:** MIENTRAS un escalamiento permanece sin acuse, el sistema DEBE presentar a quien escaló el integrante de la cadena alcanzado en ese momento.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento sin acuse que ya alcanzó al segundo integrante de la cadena, cuando la enfermera consulta ese escalamiento, entonces obtiene la identidad del segundo integrante como destinatario en curso.

---

### RF-ESC-06 — Cadena y plazo de la severidad registrada

**Enunciado:** CUANDO una profesional de enfermería emite un escalamiento con severidad registrada, el sistema DEBE aplicarle la cadena y el plazo de acuse de esa severidad.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento clasificado como deterioro inmediato y otro como consulta diferible sobre la misma cama, cuando la enfermera emite ambos, entonces cada uno obtiene la cadena y el plazo de acuse de su severidad.

---

### RF-ESC-07 — Indisponibilidad temporal y delegación

**Enunciado:** CUANDO un médico se declara temporalmente indisponible e indica un delegado y un instante de término, el sistema DEBE activar la delegación en la cadena durante el intervalo declarado o hasta su revocación anticipada.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico de guardia que declara indisponibilidad hasta las 05:00 e indica un delegado, cuando confirma la declaración, entonces la delegación queda activa hasta las 05:00 o hasta una revocación anterior.

---

### RF-ESC-08 — Consulta de la cobertura clínica vigente

**Enunciado:** CUANDO un profesional consulta la cobertura clínica de una unidad, el sistema DEBE presentar por cada cama al responsable vigente, su estado exacto —el primero que corresponda entre indisponible declarado, ocupado en otro caso abierto, con cobertura simultánea de otro servicio y disponible— y su delegado activo.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P2, P3 |

**Criterios de aceptación**

- **CA-1** — Dado un responsable clínico vigente a quien la programación vigente asigna además a otro servicio en la misma franja y sin caso abierto registrado, cuando la enfermera consulta la cobertura de esa unidad, entonces obtiene a ese profesional con cobertura simultánea de otro servicio.
- **CA-2** — Dado un responsable clínico que tomó otro caso aún abierto, cuando la enfermera consulta la cobertura de esa unidad, entonces obtiene a ese profesional como ocupado en otro caso abierto y al delegado activo si existe.
- **CA-3** — Dada una unidad cuya programación cambió durante el turno en curso, cuando la enfermera consulta la cobertura, entonces obtiene el responsable resultante de ese cambio.

---

### RF-ESC-09 — Agotamiento de la cadena de escalamiento

**Enunciado:** SI un escalamiento agota su cadena sin obtener acuse, ENTONCES el sistema DEBE alcanzar a la jefatura vigente de la unidad.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros, Carmen |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento que alcanzó a todos los integrantes de su cadena sin acuse, cuando vence el plazo del último integrante, entonces la jefatura vigente de la unidad queda alcanzada.
- **CA-2** — Dada una jefatura de unidad con delegación activa, cuando vence el plazo del último integrante de una cadena sin acuse, entonces queda alcanzado el delegado de esa jefatura.

---

### RF-ESC-10 — Aviso al integrante que no acusó

**Enunciado:** CUANDO el sistema alcanza al siguiente integrante de la cadena por falta de acuse, el sistema DEBE informar de ese avance al integrante que no acusó.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico que no acusó un escalamiento dentro de su plazo, cuando el sistema alcanza al siguiente integrante, entonces ese médico queda informado de que el escalamiento avanzó en la cadena.

---

### RF-ESC-11 — Escalamiento ante duda de severidad

**Enunciado:** SI una profesional de enfermería emite un escalamiento sin determinar su severidad, ENTONCES el sistema DEBE asignarle el estado severidad por confirmar.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una enfermera que detecta deterioro pero no puede clasificarlo, cuando emite el escalamiento, entonces queda con severidad por confirmar.

---

### RF-ESC-12 — Toma del caso

**Enunciado:** CUANDO un médico que acusó un escalamiento asume su respuesta clínica, el sistema DEBE registrar la toma del caso con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal, Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento acusado por un médico, cuando ese médico toma el caso, entonces la toma queda registrada con su autoría e instante.

---

### RF-ESC-13 — Actualización clínica a múltiples destinatarios

**Enunciado:** CUANDO se registra sobre una cama un deterioro confirmado, una indicación médica nueva, un cambio de soporte ventilatorio o vasoactivo, un resultado crítico o un traslado, el sistema DEBE incorporarlo a una única actualización informativa de esa cama, dirigida al responsable médico vigente y a las profesionales de enfermería asignadas, que aguarda la consulta de sus destinatarios.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Milagros, Aníbal |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con una actualización informativa pendiente por un cambio de soporte ventilatorio, cuando el responsable clínico vigente registra una indicación nueva sobre esa cama, entonces esa indicación queda incorporada a esa misma actualización informativa.
- **CA-2** — Dado un médico de guardia localizable destinatario de la actualización informativa de una cama, cuando esa actualización se produce durante la madrugada, entonces la obtiene al consultar sus avisos pendientes.

---

### RF-ESC-14 — Acuse visible para quien escaló

**Enunciado:** CUANDO cambia el estado de atención de un escalamiento, el sistema DEBE presentar a quien lo emitió el destinatario alcanzado, el acuse con su instante y la toma del caso con su instante cuando exista.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento emitido por una enfermera que fue acusado y tomado por un médico, cuando cambia su estado de atención, entonces ella obtiene la identidad del médico y los instantes del acuse y de la toma.

---

### RF-ESC-15 — Registro de la emisión de un escalamiento

**Enunciado:** CUANDO el sistema emite un escalamiento, el sistema DEBE registrar el episodio, el emisor, el destinatario, la severidad y el instante de emisión.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un deterioro escalado por una enfermera al responsable vigente, cuando el sistema emite el escalamiento, entonces quedan registrados el episodio, la enfermera, el responsable, la severidad y el instante de emisión.

---

### RF-ESC-16 — Priorización de avisos clínicos

**Enunciado:** CUANDO un destinatario tiene varios avisos clínicos pendientes, el sistema DEBE presentarlos agrupados por cama y ordenados primero por deterioro inmediato, después por severidad por confirmar, después por consulta diferible y al final por actualización informativa.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros, Aníbal |
| Problema | P2, P3 |

**Criterios de aceptación**

- **CA-1** — Dados un deterioro inmediato, una severidad por confirmar, una consulta diferible y tres actualizaciones informativas de una misma cama, cuando el médico consulta sus avisos pendientes, entonces los obtiene agrupados por cama y en ese orden de prioridad.

---

### RF-ESC-17 — Retorno del titular después de una delegación

**Enunciado:** CUANDO una delegación vence o es revocada, el sistema DEBE restaurar el orden de la cadena vigente anterior a esa delegación.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal, Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una delegación que vence a las 05:00, cuando llega ese instante, entonces la cadena recupera el orden vigente anterior a la delegación.

---

### RF-ESC-18 — Registro del agotamiento de una cadena

**Enunciado:** CUANDO un escalamiento agota su cadena sin obtener acuse, el sistema DEBE registrar el agotamiento con los integrantes alcanzados y el instante.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros, Carmen, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento sin acuse después de alcanzar a todos los integrantes, cuando vence el plazo del último integrante, entonces el agotamiento queda registrado con los integrantes alcanzados y el instante.

---

### RF-ESC-19 — Cierre de la atención de un escalamiento

**Enunciado:** CUANDO el médico que tomó un caso concluye su respuesta clínica, el sistema DEBE registrar el cierre con el desenlace, la autoría y el instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal, Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento cuyo caso tomó un médico, cuando ese médico concluye su respuesta clínica, entonces el cierre queda registrado con el desenlace, la autoría y el instante.

---

### RF-ESC-20 — Emisión de un escalamiento junto a la cama

**Enunciado:** CUANDO una profesional de enfermería declara junto a una cama un deterioro o una consulta que requiere respuesta, el sistema DEBE emitir el escalamiento de esa cama sin exigirle apartarse de ella.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con episodio abierto y la enfermera de turno a su lado, cuando ella declara un deterioro de esa cama, entonces el escalamiento de esa cama queda emitido sin que ella se aparte de la cama.

---

### RF-ESC-21 — Escalamiento emitido sin conexión

**Enunciado:** SI una profesional de enfermería emite un escalamiento sin conexión, ENTONCES el sistema DEBE preservarlo con su instante de emisión, sin pérdida ni duplicación, hasta alcanzar a su destinatario.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una enfermera que emite un escalamiento mientras la unidad se encuentra sin conexión, cuando la conexión se restablece, entonces ese escalamiento alcanza a su destinatario una sola vez con el instante en que fue emitido.

---

### RF-ESC-22 — Alcance junto a la cama de quien emitió el escalamiento

**Enunciado:** CUANDO cambia el estado de atención de un escalamiento, el sistema DEBE alcanzar junto a la cama a la profesional de enfermería que lo emitió, sin que ella deba consultarlo.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros |
| Problema | P2, P3 |

**Criterios de aceptación**

- **CA-1** — Dada una enfermera que emitió un escalamiento y permanece junto a la cama, cuando el médico alcanzado acusa recibo, entonces ella queda alcanzada junto a esa cama sin haber consultado el escalamiento.

---

### RF-ESC-23 — Composición de la cadena de escalamiento de una cama

**Enunciado:** CUANDO una profesional de enfermería emite un escalamiento de una cama, el sistema DEBE componer su cadena con exactamente el responsable clínico vigente de esa cama en primer lugar y, a continuación, los demás profesionales médicos que la programación vigente asigna a esa unidad en la franja del escalamiento.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Carmen |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una cama cuyo responsable clínico vigente es el internista de guardia y una unidad con un intensivista asignado por la programación vigente a esa misma franja, cuando la enfermera emite un escalamiento de esa cama, entonces la cadena queda compuesta por ese internista en primer lugar y por ese intensivista a continuación.
- **CA-2** — Dada una cama cuyo responsable clínico vigente lo es por una delegación activa, cuando la enfermera emite un escalamiento de esa cama, entonces la cadena queda encabezada por ese delegado.

---

### RF-ESC-24 — Severidad identificada en el aviso entregado

**Enunciado:** El sistema DEBE identificar en el propio aviso clínico entregado a un destinatario exactamente si corresponde a un deterioro inmediato, a una consulta diferible, a una severidad por confirmar o a una actualización informativa.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal, Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento con severidad por confirmar dirigido al médico de guardia localizable, cuando ese médico recibe el aviso, entonces el aviso recibido lo identifica como severidad por confirmar.
- **CA-2** — Dada una actualización informativa de una cama dirigida a ese mismo médico, cuando ese médico la recibe, entonces el aviso recibido la identifica como actualización informativa.

---

### RF-ESC-25 — Cadena y plazo de un escalamiento con severidad por confirmar

**Enunciado:** SI un escalamiento tiene la severidad por confirmar, ENTONCES el sistema DEBE aplicarle la cadena y el plazo de acuse del deterioro inmediato.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una enfermera que emite un escalamiento sin determinar su severidad, cuando ese escalamiento queda con severidad por confirmar, entonces obtiene la cadena y el plazo de acuse del deterioro inmediato.

---

### RF-ESC-26 — Aviso a la jefatura de una delegación activada sin su resolución

**Enunciado:** CUANDO un médico activa una delegación sobre una unidad sin resolución de su jefatura, el sistema DEBE informar de esa delegación a la jefatura de esa unidad.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico de guardia que declara indisponibilidad e indica un delegado sin resolución de la jefatura, cuando la delegación queda activa, entonces la jefatura de esa unidad queda informada de esa delegación.

---

## RF-REG — Registro clínico a pie de cama

### RF-REG-01 — Registro de signos vitales y balance

**Enunciado:** CUANDO una profesional de enfermería registra signos vitales o balance hídrico junto a la cama, el sistema DEBE incorporarlos al episodio con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con episodio abierto, cuando la enfermera registra los signos vitales, entonces esos signos integran el estado vigente del episodio con su autoría e instante.
---

### RF-REG-02 — Registro sin pérdida durante una desconexión

**Enunciado:** SI un registro a pie de cama se produce sin conexión, ENTONCES el sistema DEBE preservarlo sin pérdida ni duplicación y en el orden en que fue tomado hasta incorporarlo al episodio después del restablecimiento.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una enfermera que registra signos vitales sin conexión, cuando la conexión se restablece, entonces ese registro figura una sola vez en el episodio con el instante en que fue tomado.
- **CA-2** — Dada una enfermera que registra dos observaciones sucesivas sin conexión, cuando la conexión se restablece, entonces ambas figuran en el episodio en el orden en que fueron tomadas.

---

### RF-REG-03 — Consulta de indicaciones vigentes

**Enunciado:** CUANDO un profesional consulta las indicaciones médicas de una cama, el sistema DEBE presentar exactamente las vigentes, cada una con su autor y su instante de emisión.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una cama cuya indicación fue sustituida por otra, cuando la enfermera consulta las indicaciones de esa cama, entonces obtiene únicamente la vigente.
- **CA-2** — Dada una indicación vigente, cuando la enfermera la consulta, entonces obtiene su autor y su instante de emisión.

---

### RF-REG-04 — Confirmación de ejecución de una indicación

**Enunciado:** CUANDO un profesional de enfermería confirma la ejecución de una indicación, el sistema DEBE registrar la confirmación con su autoría y su instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una indicación vigente, cuando la enfermera confirma su ejecución, entonces la confirmación queda registrada con su autoría e instante.

---

### RF-REG-05 — Registro de eventos y medicación administrada

**Enunciado:** CUANDO una profesional de enfermería registra un evento clínico o la administración de un medicamento junto a la cama, el sistema DEBE incorporarlo al episodio con su autoría y su instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con episodio abierto, cuando la enfermera registra junto a ella la administración de un medicamento, entonces esa administración integra el episodio con su autoría e instante.

---

### RF-REG-06 — Resultados de laboratorio e imágenes del episodio

**Enunciado:** CUANDO un profesional consulta una cama, el sistema DEBE presentar los resultados de laboratorio e imágenes disponibles del episodio.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio con resultados de laboratorio disponibles, cuando el médico consulta esa cama, entonces obtiene esos resultados.

---

### RF-REG-07 — Registro de indicación a distancia

**Enunciado:** CUANDO el responsable clínico vigente de una cama, su delegado activo o el profesional médico con toma del caso vigente sobre ella registra una indicación a distancia desde un dispositivo personal con identidad verificada, el sistema DEBE incorporarla a la cama con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado el responsable clínico vigente de una cama con identidad verificada en su dispositivo personal, cuando registra una indicación a distancia, entonces la indicación integra las vigentes de esa cama con su autoría e instante.
- **CA-2** — Dado un médico alcanzado como segundo integrante de la cadena que acusó y tomó el caso de una cama sin ser su responsable clínico vigente ni su delegado activo, cuando registra una indicación a distancia desde su dispositivo personal con identidad verificada, entonces la indicación integra las vigentes de esa cama con su autoría e instante.

---

### RF-REG-08 — Resumen de la evolución de la cama

**Enunciado:** CUANDO un médico consulta la evolución de una cama, el sistema DEBE presentar la tendencia disponible de hasta seis horas con la extensión efectiva de ese periodo declarada, los parámetros ventilatorios vigentes y la última evolución registrada.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con seis horas de registros y ventilación mecánica, cuando el médico consulta su evolución, entonces obtiene la tendencia, el modo, frecuencia, volumen corriente, PEEP y FiO2, y la última evolución.
- **CA-2** — Dada una cama con dos horas de registros, cuando el médico consulta su evolución, entonces obtiene esas dos horas con la extensión del periodo declarada.

---

### RF-REG-09 — Devolución de la confirmación de ejecución al autor de la indicación

**Enunciado:** CUANDO un profesional de enfermería confirma la ejecución de una indicación, el sistema DEBE presentar esa confirmación con su autoría e instante al autor de la indicación.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una indicación registrada a distancia por un médico y ejecutada junto a la cama, cuando la enfermera de turno confirma su ejecución, entonces ese médico obtiene la confirmación con la autoría y el instante de ella.

---

### RF-REG-10 — Señalamiento de estudios solicitados sin resultado

**Enunciado:** CUANDO un profesional consulta una cama, el sistema DEBE señalar los estudios del episodio solicitados aún sin resultado.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio con un cultivo solicitado y aún sin resultado, cuando el médico consulta esa cama, entonces ese estudio figura como solicitado sin resultado.

---

## RF-IAM — Identidad y accesos

### RF-IAM-01 — Atribución del registro a su autor

**Enunciado:** CUANDO un profesional produce un registro clínico, el sistema DEBE atribuirlo a la identidad verificada de ese profesional.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dados dos médicos que utilizan sucesivamente un equipo compartido, cuando el segundo produce un registro clínico tras verificar su identidad, entonces el registro queda atribuido al segundo.
---

### RF-IAM-02 — Restricción del registro al ámbito de responsabilidad

**Enunciado:** SI un profesional carece de responsabilidad clínica vigente, delegación activa, responsabilidad de jefatura, asignación médica vigente, asignación de cuidado de enfermería vigente y toma del caso vigente sobre una cama, ENTONCES el sistema DEBE rechazar su registro sobre esa cama.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo, Carmen, Aníbal |
| Problema | P1, P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico sin responsabilidad clínica vigente, delegación, jefatura, asignación médica ni toma del caso vigente, cuando intenta registrar sobre una cama, entonces el registro se rechaza.
- **CA-2** — Dada una enfermera sin asignación de cuidado vigente sobre una cama, cuando intenta registrar sobre esa cama, entonces el registro se rechaza.

---

### RF-IAM-03 — Trazabilidad de acceso a datos clínicos

**Enunciado:** El sistema DEBE registrar cada consulta y cada modificación de datos clínicos con el profesional que la realiza, el episodio alcanzado y su instante.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional que consulta el episodio de una cama, cuando esa consulta concluye, entonces quedan registrados el profesional, el episodio alcanzado y el instante.
---

### RF-IAM-04 — Aviso de escalamiento antes de la identificación del destinatario

**Enunciado:** MIENTRAS el destinatario de un escalamiento no se ha identificado con identidad verificada vigente ante el dispositivo no institucional en el que recibe el aviso, el sistema DEBE presentar en ese aviso exactamente la sede, la unidad, la cama, la severidad y el motivo.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico que recibe un escalamiento en un dispositivo no institucional en el que no tiene identidad verificada vigente, cuando llega el aviso, entonces obtiene la sede, la unidad, la cama, la severidad y el motivo sin el nombre ni el documento de identidad del paciente.
- **CA-2** — Dado un médico con identidad verificada vigente en su celular personal ante el cual todavía no se ha identificado, cuando llega el aviso de un escalamiento, entonces obtiene la sede, la unidad, la cama, la severidad y el motivo sin el nombre ni el documento de identidad del paciente.

---

### RF-IAM-05 — Reutilización de identidad verificada en dispositivo personal

**Enunciado:** DONDE el destinatario emplea un dispositivo personal con identidad verificada vigente, el sistema DEBE presentar el contexto clínico sin exigir una nueva verificación para cada escalamiento.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico con identidad verificada vigente en su dispositivo personal, cuando abre un escalamiento recibido, entonces obtiene el contexto clínico sin realizar otra verificación.

---

### RF-IAM-06 — Responsabilidad clínica de un profesional rotante

**Enunciado:** CUANDO la Red comunica el alta o el retiro de un profesional rotante con su periodo efectivo, el sistema DEBE actualizar su responsabilidad clínica en las unidades comunicadas para ese periodo.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional rotante cuya alta rige desde el lunes, cuando la Red comunica esa alta con su periodo efectivo, entonces su responsabilidad clínica figura vigente en las unidades comunicadas desde el lunes.
- **CA-2** — Dado un profesional rotante cuyo retiro rige desde el viernes, cuando la Red comunica ese retiro con su periodo efectivo, entonces su responsabilidad clínica deja de figurar vigente en las unidades comunicadas desde el viernes.

---

### RF-IAM-07 — Restricción del contexto sin identidad verificada

**Enunciado:** SI un destinatario carece de identidad verificada vigente en el dispositivo empleado, ENTONCES el sistema DEBE impedirle consultar el contexto clínico del escalamiento.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal, Rodrigo |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico sin identidad verificada vigente en su dispositivo personal, cuando intenta consultar el contexto clínico, entonces el contexto no se presenta.

---

### RF-IAM-08 — Verificación de identidad en el dispositivo personal

**Enunciado:** CUANDO un profesional verifica su identidad en el dispositivo personal en el que recibe los avisos clínicos, el sistema DEBE dejar su identidad verificada vigente en ese mismo dispositivo exigiéndole únicamente ese dispositivo y la conectividad de que disponga.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal, Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico de guardia localizable en su domicilio, sin identidad verificada vigente, con señal débil y sin más equipo que su celular personal, cuando verifica su identidad en ese celular, entonces su identidad verificada queda vigente en ese celular.

---

### RF-IAM-09 — Registro habilitado por la toma del caso

**Enunciado:** MIENTRAS un médico conserva la toma del caso de un escalamiento de una cama, el sistema DEBE admitir sus registros clínicos sobre esa cama.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal, Rodrigo |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico alcanzado como segundo integrante de la cadena, que acusó y tomó el caso de una cama sobre la que no tiene responsabilidad clínica vigente ni delegación activa, cuando registra su indicación sobre esa cama, entonces ese registro es admitido.

---

## RF-SUP — Supervisión de la unidad

### RF-SUP-01 — Cumplimiento y completitud de las entregas de turno

**Enunciado:** CUANDO el coordinador consulta el cumplimiento de entregas de turno de una unidad en un periodo, el sistema DEBE presentar exactamente las entregas cerradas, los turnos concluidos sin entrega cerrada y los intentos bloqueados con cada cama y dato obligatorio ausente.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una unidad con un turno concluido sin entrega cerrada, cuando la coordinadora consulta el cumplimiento de ese periodo, entonces ese turno figura entre los concluidos sin entrega cerrada.
- **CA-2** — Dado un intento bloqueado por una cama sin diagnóstico vigente, cuando la coordinadora consulta el cumplimiento de ese periodo, entonces obtiene el intento con la cama y el diagnóstico como dato obligatorio ausente.

---

### RF-SUP-02 — Indicadores de cobertura de la red

**Enunciado:** El sistema DEBE producir los indicadores de cobertura de turnos y de cumplimiento de entrega de las unidades de una red a partir de los registros vigentes, sin transcripción manual.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una red de tres unidades con los turnos y las entregas de un periodo registrados, cuando concluye ese periodo, entonces los indicadores de cobertura de turnos y de cumplimiento de entrega de las tres unidades quedan producidos a partir de esos registros sin que la coordinadora transcriba dato alguno.

---

### RF-SUP-03 — Revisión de la actividad en el ámbito de responsabilidad

**Enunciado:** CUANDO un profesional consulta la actividad de un periodo en su ámbito de responsabilidad, el sistema DEBE presentar exactamente los eventos clínicos; los escalamientos con severidad, cadena alcanzada, acuses, tomas de caso y desenlace; las indicaciones registradas a distancia; y los ingresos y egresos ocurridos en las unidades que ese ámbito comprendía en ese periodo.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico cuyo ámbito de responsabilidad de la noche anterior comprendía dos unidades de sedes distintas, cada una con un evento, un escalamiento con su recorrido y desenlace, una indicación a distancia, un ingreso y un egreso, cuando ese médico consulta la actividad de esa noche, entonces obtiene exactamente esos elementos de ambas unidades.

---

### RF-SUP-04 — Auditoría de un escalamiento

**Enunciado:** CUANDO el coordinador audita un escalamiento, el sistema DEBE presentar exactamente: su instante de emisión, su severidad, los integrantes alcanzados en orden, los acuses con su autoría e instante, y su desenlace.

| Campo | Valor |
|---|---|
| Prioridad | COULD |
| Persona | Carmen |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento que recorrió dos integrantes antes de ser acusado, cuando la coordinadora lo audita, entonces obtiene ambos integrantes en el orden en que fueron alcanzados y el acuse del segundo.

---

### RF-SUP-05 — Entrega de los indicadores de cobertura

**Enunciado:** CUANDO la coordinadora solicita los indicadores de cobertura de una red para un periodo, el sistema DEBE entregarle exactamente las franjas descubiertas y las entregas cerradas de cada unidad de esa red en ese periodo.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una red de tres unidades con sus indicadores de un periodo producidos, cuando la coordinadora los solicita, entonces obtiene las franjas descubiertas y las entregas cerradas de las tres unidades.

---

## Matriz de trazabilidad

Cada tarea crítica de cada persona traza a al menos un RF. Las filas sin RF son brechas abiertas.

| Persona | Tarea crítica | RF que la cubre |
|---|---|---|
| Rodrigo | Recibir el handoff estructurado de todas las camas asignadas | RF-DIA-02, RF-DIA-03, RF-DIA-09, RF-DIA-10, RF-DIA-17, RF-DIA-18 |
| Rodrigo | Consultar la evolución y el diagnóstico del turno anterior | RF-DIA-02, RF-DIA-05, RF-DIA-07, RF-DIA-10, RF-DIA-13, RF-DIA-14, RF-DIA-15, RF-DIA-21, RF-DIA-23 |
| Rodrigo | Registrar nota de evolución y diagnóstico por paciente | RF-DIA-07, RF-DIA-13, RF-DIA-14, RF-DIA-15, RF-DIA-16, RF-IAM-01, RF-IAM-09 |
| Rodrigo | Marcar pacientes inestables o con pendientes críticos | RF-DIA-06, RF-DIA-22 |
| Rodrigo | Consultar resultados de laboratorio e imágenes | RF-REG-06, RF-REG-10 |
| Rodrigo | Cerrar y firmar la entrega de turno | RF-DIA-01, RF-DIA-04, RF-DIA-12, RF-DIA-20, RF-DIA-24 |
| Milagros | Registrar signos vitales y balance por paciente | RF-REG-01, RF-REG-02 |
| Milagros | Escalar un deterioro clínico al médico responsable | RF-ESC-01, RF-ESC-06, RF-ESC-11, RF-ESC-15, RF-ESC-20, RF-ESC-21, RF-ESC-22, RF-ESC-23, RF-ESC-25 |
| Milagros | Consultar quién está de guardia y su estado de disponibilidad | RF-ESC-08 |
| Milagros | Ver y confirmar indicaciones médicas vigentes | RF-REG-03, RF-REG-04, RF-ESC-13 |
| Milagros | Registrar eventos y administración de medicamentos | RF-REG-05 |
| Milagros | Recibir y entregar el turno de enfermería | RF-DIA-08, RF-DIA-11, RF-DIA-19, RF-DIA-25, RF-DIA-26, RF-DIA-27 |
| Carmen | Elaborar y publicar la programación mensual de turnos | RF-TUR-04, RF-TUR-09, RF-TUR-10, RF-TUR-11, RF-TUR-27, RF-TUR-28 |
| Carmen | Validar que no existan cruces ni franjas descubiertas | RF-TUR-01, RF-TUR-02, RF-TUR-07, RF-ESC-26 |
| Carmen | Aprobar o rechazar intercambios y permisos | RF-TUR-06, RF-TUR-12, RF-TUR-13, RF-TUR-17, RF-TUR-21, RF-TUR-22, RF-TUR-29, RF-TUR-30, RF-TUR-31, RF-TUR-32, RF-TUR-33, RF-TUR-34 |
| Carmen | Reasignar cobertura ante una ausencia imprevista | RF-TUR-03, RF-TUR-05, RF-TUR-18, RF-TUR-19, RF-TUR-20, RF-TUR-25, RF-TUR-26, RF-TUR-35, RF-TUR-36, RF-TUR-37, RF-TUR-38, RF-TUR-39, RF-TUR-40, RF-TUR-41 |
| Carmen | Monitorear cumplimiento y completitud de entregas de turno | RF-DIA-12, RF-DIA-24, RF-SUP-01 |
| Carmen | Generar indicadores de cobertura para la Dirección de Red | RF-SUP-02, RF-SUP-05 |
| Aníbal | Recibir la alerta de escalamiento con contexto clínico adjunto | RF-ESC-03, RF-ESC-16, RF-ESC-24, RF-IAM-04, RF-IAM-05, RF-IAM-07, RF-IAM-08 |
| Aníbal | Confirmar recepción y tomar el caso | RF-ESC-04, RF-ESC-12, RF-ESC-14, RF-ESC-19 |
| Aníbal | Consultar tendencia de signos, ventilación y última evolución | RF-REG-08 |
| Aníbal | Registrar la indicación dada de forma remota | RF-REG-07, RF-REG-09, RF-IAM-02, RF-IAM-05, RF-IAM-07, RF-IAM-08, RF-IAM-09 |
| Aníbal | Marcarse temporalmente indisponible y delegar | RF-ESC-07, RF-ESC-17 |
| Aníbal | Revisar en la mañana lo ocurrido durante la noche | RF-SUP-03 |

## Cobertura de criterios de éxito

| Persona | Criterio de éxito | RF que lo satisface |
|---|---|---|
| Rodrigo | Entender el estado de las camas empleando solo el sistema | RF-DIA-02, RF-DIA-05, RF-DIA-10, RF-DIA-17, RF-DIA-18, RF-DIA-21, RF-DIA-22, RF-REG-10 |
| Rodrigo | El handoff incluye decisiones y su justificación | RF-DIA-02, RF-DIA-13, RF-DIA-21 |
| Rodrigo | Ninguna cama llega sin diagnóstico; si falta, el sistema lo señala | RF-DIA-01, RF-DIA-03, RF-DIA-12, RF-DIA-20, RF-DIA-24 |
| Rodrigo | Registrar la nota de evolución cuesta menos que escribirla a mano | RF-DIA-07, `RNF-USA-01` |
| Rodrigo | Ver qué cambió desde su último contacto con el paciente | RF-DIA-05, RF-DIA-23 |
| Milagros | Escalar un deterioro en el mínimo de pasos | RF-ESC-01, RF-ESC-11, RF-ESC-20, RF-ESC-21, RF-ESC-25, `RNF-USA-02` |
| Milagros | Ver quién está de guardia en este momento | RF-ESC-08, RF-ESC-12, RF-ESC-17, RF-ESC-23 |
| Milagros | Recibir confirmación visible de que el médico vio la alerta | RF-ESC-04, RF-ESC-14, RF-ESC-22 |
| Milagros | Si nadie responde, el sistema escala sin que ella intervenga | RF-ESC-02, RF-ESC-09, RF-ESC-23, RF-ESC-25 |
| Milagros | Registrar a pie de cama, sin caminar hasta la estación | RF-REG-01, RF-REG-02, RF-REG-05, RF-ESC-20, RF-ESC-22 |
| Milagros | Dejar de transcribir del papel al sistema | RF-REG-05, RF-DIA-08, RF-DIA-11, RF-DIA-25, RF-DIA-26, RF-DIA-27 |
| Carmen | El sistema impide guardar una asignación con cruce | RF-TUR-01 |
| Carmen | Cubrir una ausencia imprevista toma minutos | RF-TUR-03, RF-TUR-18, RF-TUR-19, RF-TUR-20, RF-TUR-25, RF-TUR-35, RF-TUR-36, RF-TUR-37, RF-TUR-38, RF-TUR-39, RF-TUR-40, RF-TUR-41 |
| Carmen | Una sola versión vigente del rol, con historial de cambios | RF-TUR-04, RF-TUR-08, RF-TUR-14, RF-TUR-27, RF-TUR-28, RF-TUR-32, RF-TUR-34 |
| Carmen | Ver qué franjas de los próximos días están descubiertas | RF-TUR-07 |
| Carmen | Saber qué entregas se cerraron sin diagnóstico registrado | RF-DIA-12, RF-DIA-24, RF-SUP-01 |
| Carmen | Los indicadores salen del sistema sin trabajo manual | RF-SUP-02, RF-SUP-05 |
| Aníbal | La alerta incluye el contexto clínico mínimo sin pedirlo | RF-DIA-13, RF-ESC-03, RF-ESC-24, RF-IAM-04 |
| Aníbal | Decidir si acude, con el contexto ya recibido | RF-ESC-03, RF-ESC-16, RF-ESC-24, RF-REG-08, RF-IAM-08 |
| Aníbal | Confirmar recepción y que quien escaló lo vea de inmediato | RF-ESC-04, RF-ESC-14 |
| Aníbal | Registrar su indicación remota con hora y autoría | RF-REG-07, RF-REG-09, RF-IAM-05, RF-IAM-07, RF-IAM-08, RF-IAM-09 |
| Aníbal | Si no responde, el sistema escala solo y él se entera | RF-ESC-02, RF-ESC-10, RF-ESC-25 |
| Aníbal | Revisar en un solo lugar lo ocurrido en la noche | RF-SUP-03 |

## Cobertura de problemas críticos

Cada fila enumera los RF cuyo campo `Problema` declara ese problema crítico. La enumeración es
explícita —sin rangos— porque un rango encubre a los RF intermedios que declaran otro problema.

| Problema | RF que lo resuelve |
|---|---|
| P1 — Rotación de doctor | RF-TUR-01, RF-TUR-02, RF-TUR-03, RF-TUR-04, RF-TUR-05, RF-TUR-06, RF-TUR-07, RF-TUR-08, RF-TUR-09, RF-TUR-10, RF-TUR-11, RF-TUR-12, RF-TUR-13, RF-TUR-14, RF-TUR-15, RF-TUR-16, RF-TUR-17, RF-TUR-18, RF-TUR-19, RF-TUR-20, RF-TUR-21, RF-TUR-22, RF-TUR-23, RF-TUR-24, RF-TUR-25, RF-TUR-26, RF-TUR-27, RF-TUR-28, RF-TUR-29, RF-TUR-30, RF-TUR-31, RF-TUR-32, RF-TUR-33, RF-TUR-34, RF-TUR-35, RF-TUR-36, RF-TUR-37, RF-TUR-38, RF-TUR-39, RF-TUR-40, RF-TUR-41, RF-DIA-01, RF-DIA-02, RF-DIA-03, RF-DIA-04, RF-DIA-05, RF-DIA-06, RF-DIA-07, RF-DIA-08, RF-DIA-09, RF-DIA-10, RF-DIA-11, RF-DIA-12, RF-DIA-13, RF-DIA-14, RF-DIA-15, RF-DIA-16, RF-DIA-17, RF-DIA-18, RF-DIA-19, RF-DIA-20, RF-DIA-21, RF-DIA-22, RF-DIA-23, RF-DIA-24, RF-DIA-25, RF-DIA-26, RF-DIA-27, RF-REG-06, RF-REG-10, RF-IAM-01, RF-IAM-02, RF-IAM-03, RF-IAM-06, RF-SUP-01, RF-SUP-02, RF-SUP-05 |
| P2 — Medianoche | RF-DIA-13, RF-ESC-01, RF-ESC-02, RF-ESC-03, RF-ESC-04, RF-ESC-05, RF-ESC-06, RF-ESC-07, RF-ESC-08, RF-ESC-09, RF-ESC-10, RF-ESC-11, RF-ESC-12, RF-ESC-14, RF-ESC-15, RF-ESC-16, RF-ESC-17, RF-ESC-18, RF-ESC-19, RF-ESC-20, RF-ESC-21, RF-ESC-22, RF-ESC-23, RF-ESC-24, RF-ESC-25, RF-ESC-26, RF-REG-07, RF-REG-08, RF-REG-09, RF-IAM-02, RF-IAM-04, RF-IAM-05, RF-IAM-07, RF-IAM-08, RF-IAM-09, RF-SUP-03, RF-SUP-04 |
| P3 — Actualizaciones en tiempo real | RF-ESC-08, RF-ESC-13, RF-ESC-16, RF-ESC-22, RF-REG-01, RF-REG-02, RF-REG-03, RF-REG-04, RF-REG-05 |

## Cobertura de las preguntas del enunciado

| Pregunta del caso | RF que la responde |
|---|---|
| Qué ocurre si un paciente se agrava en el turno noche | RF-ESC-01, RF-ESC-06, RF-ESC-11, RF-ESC-15, RF-ESC-16, RF-ESC-20, RF-ESC-21, RF-ESC-22, RF-ESC-23, RF-ESC-24, RF-ESC-25 |
| Cómo se contacta rápidamente al médico encargado | RF-ESC-01, RF-ESC-08, RF-ESC-20, RF-ESC-21, RF-ESC-23 |
| Qué ocurre si el médico no está disponible | RF-ESC-02, RF-ESC-07, RF-ESC-09, RF-ESC-10, RF-ESC-17, RF-ESC-18, RF-ESC-26 |
| Cómo se avisa a varios médicos y enfermeras | RF-ESC-13, RF-ESC-16, RF-ESC-22, RF-ESC-23, RF-ESC-24 |
| Con qué garantía se conserva el diagnóstico | RF-DIA-01, RF-DIA-07, RF-DIA-20, RF-DIA-24, `RNF-SEG-03` |
| Cómo se sostiene su disponibilidad permanente | RF-DIA-10, RF-DIA-17, RF-REG-02, RF-ESC-21, `RNF-DIS-01`, `RNF-DIS-02` |

## Requerimientos de origen normativo

Estos RF no nacen de una tarea crítica sino de las restricciones externas declaradas en la sección 2.4
del [`README.md`](../README.md). Trazan igualmente a la persona sobre cuya operación recaen.

| Restricción externa | RF que la observa |
|---|---|
| Ley N.° 29733 — trazabilidad del acceso a datos de salud | RF-IAM-03 |
| Ley N.° 29733 — acceso limitado al ámbito de responsabilidad | RF-IAM-02, RF-IAM-09 |
| Ley N.° 29733 — exposición de datos fuera del entorno institucional | RF-IAM-04, RF-IAM-05, RF-IAM-07, RF-IAM-08 |
| SUSALUD — atribución cierta del registro clínico | RF-DIA-04, RF-DIA-07, RF-DIA-27, RF-IAM-01 |

## Decisión de tensiones

Cada tensión documentada en [`Personas/README.md`](../Personas/README.md) se decide en un RF. Una
tensión sin RF que la resuelva es una brecha de consistencia.

| Tensión | RF que la decide | Decisión adoptada |
|---|---|---|
| Velocidad frente a completitud del registro | RF-DIA-01, RF-DIA-07, RF-DIA-08, RF-DIA-13, RF-DIA-14, RF-DIA-15, RF-DIA-16, RF-DIA-20, RF-DIA-24 | El cierre exige el diagnóstico vigente de cada cama asignada y nada más; los demás componentes se registran una sola vez para su reutilización, evitando que completitud signifique reingreso. El turno que concluye sin entrega cerrada no se resuelve exigiéndole más al médico, sino advirtiendo a la jefatura con cada cama sin diagnóstico. |
| Sensibilidad del escalamiento | RF-ESC-06, RF-ESC-11, RF-ESC-13, RF-ESC-16, RF-ESC-24, RF-ESC-25 | La enfermera escala sin clasificar: el escalamiento sin severidad determinada queda en severidad por confirmar y recibe la cadena y el plazo de acuse del deterioro inmediato. La selectividad se preserva en la presentación y no en el plazo: los avisos se ordenan en cuatro clases —deterioro inmediato, severidad por confirmar, consulta diferible y actualización informativa—, y el propio aviso entregado identifica a cuál corresponde, de modo que el médico distingue urgencia real de consulta rutinaria antes de abrirlo. |
| Autonomía de intercambio de turnos | RF-TUR-06, RF-TUR-13, RF-TUR-17, RF-TUR-31, RF-TUR-32, RF-TUR-33, RF-TUR-34 | La coordinadora aprueba o rechaza autorizaciones reutilizables por alcance y periodo; los intercambios cubiertos se aplican sin una resolución individual adicional y se le avisan con la autorización que los amparó. El intercambio que ninguna autorización cubre queda pendiente de su resolución expresa, y su aprobación o su rechazo llega a los dos proponentes. |
| Adopción voluntaria | RF-TUR-08, RF-TUR-16, RF-TUR-27, RF-TUR-28 | El sistema es la única fuente editable de asignaciones. La copia imprimible deja de limitarse a periodos cerrados: la de la programación vigente se entrega como reflejo no editable con el instante de su generación, y la de un periodo cerrado se identifica además como archivo histórico de condición no operativa. |
| Movilidad frente a control de datos | RF-REG-07, RF-IAM-04, RF-IAM-05, RF-IAM-07, RF-IAM-08 | Se admite el dispositivo personal. Mientras el destinatario no se ha identificado ante él, el aviso expone solo sede, unidad, cama, severidad y motivo; la identidad verificada se recupera en el propio dispositivo con la conectividad de que se disponga, sin exigir equipo institucional, y mientras está vigente permite leer el contexto clínico y registrar sin repetir la verificación en cada alerta. |

## Distribución de prioridad

| Prioridad | Cantidad | Proporción | Criterio aplicado |
|---|---|---|---|
| MUST | 60 | 50.8 % | Es la única cobertura de una tarea crítica, o su ausencia deja sin resolver un problema crítico |
| SHOULD | 56 | 47.5 % | Sostiene un criterio de éxito, o refuerza una tarea crítica que ya tiene cobertura MUST |
| COULD | 2 | 1.7 % | Preserva una práctica vigente del equipo sin condicionar la operación clínica |
