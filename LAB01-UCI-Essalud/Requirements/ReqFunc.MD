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
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional de planta que alcanzó el máximo de horas de su régimen, cuando la coordinadora intenta asignarle otro turno, entonces la asignación se rechaza indicando el máximo aplicable.
- **CA-2** — Dado un rotante con reglas de jornada suministradas por la Red, cuando una asignación infringe su descanso mínimo, entonces la asignación se rechaza indicando la regla del rotante.

---

### RF-TUR-03 — Candidatos elegibles ordenados por rotación

**Enunciado:** CUANDO la coordinadora solicita cobertura para una franja, el sistema DEBE presentar en orden de rotación los profesionales sin solapamiento en ninguna sede de la Red, sin permiso vigente y con reglas laborales disponibles que permitan la asignación.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una franja descubierta y un profesional con permiso que la abarca, cuando la coordinadora solicita candidatos, entonces ese profesional no figura entre los presentados.
- **CA-2** — Dados dos profesionales elegibles cuya rotación asigna precedencia al segundo, cuando la coordinadora solicita candidatos, entonces el segundo figura antes que el primero.

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
| Prioridad | MUST |
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
| Prioridad | MUST |
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
| Prioridad | MUST |
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

### RF-TUR-20 — Sustitución urgente en la programación vigente

**Enunciado:** CUANDO la coordinadora selecciona un candidato elegible para una franja descubierta de la programación vigente, el sistema DEBE asignarlo directamente a esa franja vigente.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una guardia vigente descubierta por una ausencia y un candidato elegible, cuando la coordinadora lo selecciona, entonces el candidato queda asignado directamente a esa guardia vigente.

---

### RF-TUR-21 — Elegibilidad después de aprobar un permiso

**Enunciado:** CUANDO entra en vigencia un permiso aprobado, el sistema DEBE excluir al profesional de los candidatos elegibles durante el intervalo autorizado.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un permiso aprobado para el sábado, cuando comienza su vigencia, entonces el profesional no figura entre los candidatos elegibles durante ese intervalo.

---

### RF-TUR-22 — Asignaciones alcanzadas por un permiso aprobado

**Enunciado:** CUANDO entra en vigencia un permiso aprobado que alcanza una asignación vigente, el sistema DEBE retirar al profesional de esa asignación durante el intervalo autorizado.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un permiso aprobado que cubre una guardia asignada, cuando comienza su vigencia, entonces el profesional queda retirado de esa asignación durante el intervalo autorizado.

---

### RF-TUR-23 — Elegibilidad del profesional rotante

**Enunciado:** CUANDO la Red comunica el alta o retiro de un profesional rotante, el sistema DEBE actualizar su elegibilidad para el periodo efectivo comunicado.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un rotante retirado por la Red desde el viernes, cuando se recibe la comunicación, entonces su elegibilidad deja de estar vigente desde ese día.

---

### RF-TUR-24 — Asignaciones de un rotante retirado

**Enunciado:** CUANDO la Red retira a un profesional rotante desde un instante que alcanza asignaciones vigentes, el sistema DEBE retirar al profesional de esas asignaciones desde ese instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un rotante retirado desde el viernes con una guardia asignada el sábado, cuando se recibe la comunicación, entonces queda retirado de esa guardia desde el instante efectivo.

---

### RF-TUR-25 — Confirmaciones pendientes de un cambio urgente

**Enunciado:** CUANDO la coordinadora consulta un cambio urgente publicado, el sistema DEBE presentar a cada profesional afectado con su confirmación de lectura o su estado pendiente.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
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

## RF-DIA — Diagnósticos y entrega de turno

### RF-DIA-01 — Bloqueo del cierre de turno sin diagnóstico vigente

**Enunciado:** SI un turno médico finaliza con alguna cama asignada sin diagnóstico vigente, ENTONCES el sistema DEBE impedir el cierre de la entrega.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un médico con cuatro camas asignadas y diagnóstico vigente en tres de ellas, cuando ese médico intenta cerrar su entrega de turno, entonces la entrega no queda cerrada.

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

**Enunciado:** CUANDO un médico consulta una cama sobre la que produjo un registro clínico previo, el sistema DEBE presentar exactamente los cambios de diagnóstico, esquema terapéutico, soporte ventilatorio, soporte vasoactivo, resultados de laboratorio y pendientes ocurridos desde ese último registro propio.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un médico cuyo último registro clínico propio sobre una cama ocurrió tres semanas antes, cuando ese médico consulta esa cama, entonces obtiene exactamente los cambios de diagnóstico, esquema terapéutico, soporte ventilatorio, soporte vasoactivo, resultados de laboratorio y pendientes ocurridos desde ese registro.

---

### RF-DIA-06 — Marca de inestabilidad y pendiente crítico

**Enunciado:** CUANDO un profesional marca una cama como inestable o con pendiente crítico, el sistema DEBE mantener esa marca en la entrega de turno de esa cama hasta que un profesional la retire con su autoría.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una cama marcada como inestable en el turno anterior, cuando el médico entrante recibe la entrega de esa unidad, entonces esa cama figura marcada como inestable.
- **CA-2** — Dada una cama marcada como inestable, cuando un médico retira la marca, entonces la retirada queda registrada con su autoría y la cama deja de figurar marcada.

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

**Enunciado:** CUANDO una profesional de enfermería concluye su turno, el sistema DEBE componer su entrega reutilizando sin transcripción los pendientes de cuidado abiertos, los eventos y la medicación ya registrados durante el turno.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una enfermera con pendientes, eventos y medicación registrados durante su turno, cuando concluye el turno, entonces su entrega queda compuesta con esos datos ya registrados sin transcribirlos.

---

### RF-DIA-09 — Aceptación de la entrega médica

**Enunciado:** CUANDO el médico entrante acepta una entrega recibida, el sistema DEBE registrar la aceptación con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una entrega recibida por el médico entrante, cuando la acepta, entonces la aceptación queda registrada con su autoría e instante.

---

### RF-DIA-10 — Disponibilidad de la entrega médica

**Enunciado:** CUANDO el médico entrante inicia su turno y existe una entrega confirmada del turno inmediatamente anterior, el sistema DEBE presentarle esa entrega de cada cama asignada sin depender de la presencia del médico saliente.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una entrega confirmada del turno inmediatamente anterior y el médico saliente ausente, cuando el entrante inicia su turno, entonces obtiene esa entrega de cada cama asignada.

---

### RF-DIA-11 — Recepción de la entrega de enfermería

**Enunciado:** CUANDO una profesional de enfermería inicia su turno, el sistema DEBE presentarle los pendientes, eventos y medicación de la última entrega de sus camas asignadas reutilizando los registros existentes sin transcripción.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una entrega de enfermería registrada, cuando la enfermera entrante inicia su turno, entonces obtiene sus pendientes, eventos y medicación sin transcribirlos.

---

### RF-DIA-12 — Causa de un cierre de entrega bloqueado

**Enunciado:** CUANDO se bloquea un intento de cierre de entrega médica, el sistema DEBE presentar cada cama que lo impide con el dato obligatorio ausente.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
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
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio cuya familia aún no fue informada, cuando el médico registra ese estado, entonces queda incorporado como pendiente con el motivo, la autoría y el instante.

---

### RF-DIA-16 — Registro del plan clínico

**Enunciado:** CUANDO un médico registra el plan clínico de un episodio, el sistema DEBE incorporarlo con las acciones previstas, su horizonte, la autoría y el instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio que requiere reevaluación en seis horas, cuando el médico registra el plan, entonces queda incorporado con la acción prevista, el horizonte de seis horas, la autoría y el instante.

---

### RF-DIA-17 — Ausencia de entrega del turno inmediatamente anterior

**Enunciado:** SI el turno inmediatamente anterior concluyó sin una entrega confirmada, ENTONCES el sistema DEBE presentar al médico entrante un estado de entrega ausente que diferencie expresamente cualquier entrega más antigua.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un turno concluido sin entrega confirmada y una entrega de un turno anterior, cuando el médico entrante inicia su turno, entonces obtiene el estado de entrega ausente con la entrega antigua identificada expresamente como no vigente.

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

### RF-ESC-06 — Cadena según la severidad

**Enunciado:** CUANDO un profesional emite un escalamiento, el sistema DEBE aplicarle la cadena y el plazo de acuse de su severidad registrada o los del deterioro inmediato si la severidad está por confirmar.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento clasificado como deterioro inmediato y otro como consulta diferible sobre la misma cama, cuando ambos se emiten, entonces cada uno aplica la cadena y el plazo de su severidad.
- **CA-2** — Dado un escalamiento con severidad por confirmar, cuando se emite, entonces aplica la cadena y el plazo del deterioro inmediato.

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

**Enunciado:** CUANDO un profesional consulta la cobertura clínica de una unidad, el sistema DEBE presentar por cada cama al responsable vigente, su estado exacto entre disponible, indisponible declarado u ocupado en otro caso abierto, y su delegado activo.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P2, P3 |

**Criterios de aceptación**

- **CA-1** — Dado un responsable clínico que tomó otro caso aún abierto, cuando la enfermera consulta la cobertura de esa unidad, entonces obtiene a ese profesional como ocupado en otro caso abierto y al delegado activo si existe.
- **CA-2** — Dada una unidad cuya programación cambió durante el turno en curso, cuando la enfermera consulta la cobertura, entonces obtiene el responsable resultante de ese cambio.

---

### RF-ESC-09 — Agotamiento de la cadena de escalamiento

**Enunciado:** SI un escalamiento agota su cadena sin obtener acuse, ENTONCES el sistema DEBE alcanzar a la jefatura de la unidad.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros, Carmen |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento que alcanzó a todos los integrantes de su cadena sin acuse, cuando vence el plazo del último integrante, entonces la jefatura de la unidad queda alcanzada.

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

**Enunciado:** CUANDO se registra un deterioro confirmado, un cambio de soporte ventilatorio o vasoactivo, un resultado crítico o un traslado de cama, el sistema DEBE emitir una única actualización informativa agrupada por cama al responsable médico vigente y a las profesionales de enfermería asignadas.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Milagros, Aníbal |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dado un cambio del soporte ventilatorio de una cama, cuando queda registrado, entonces el responsable médico y las enfermeras asignadas reciben una actualización informativa agrupada por esa cama.

---

### RF-ESC-14 — Acuse visible para quien escaló

**Enunciado:** CUANDO cambia el estado de atención de un escalamiento, el sistema DEBE presentar a quien lo emitió el destinatario alcanzado, el acuse con su instante y la toma del caso con su instante cuando exista.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
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

**Enunciado:** CUANDO un destinatario tiene varios avisos clínicos pendientes, el sistema DEBE presentarlos agrupados por cama y ordenados primero por deterioro confirmado, después por severidad por confirmar y al final por actualización informativa.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2, P3 |

**Criterios de aceptación**

- **CA-1** — Dados un deterioro confirmado, una severidad por confirmar y tres actualizaciones informativas de una misma cama, cuando el médico consulta sus avisos pendientes, entonces los obtiene agrupados por cama y en ese orden de prioridad.

---

### RF-ESC-17 — Retorno del titular después de una delegación

**Enunciado:** CUANDO una delegación vence o es revocada, el sistema DEBE restaurar el orden de la cadena vigente anterior a esa delegación.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
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

**Enunciado:** SI un registro a pie de cama se produce sin conexión, ENTONCES el sistema DEBE preservarlo sin pérdida ni duplicación hasta incorporarlo al episodio después del restablecimiento.

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
| Prioridad | SHOULD |
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

**Enunciado:** CUANDO un profesional consulta una cama, el sistema DEBE presentar los resultados de laboratorio e imágenes disponibles del episodio y señalar los estudios solicitados aún sin resultado.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio con un cultivo solicitado y aún sin resultado, cuando el médico consulta esa cama, entonces ese estudio figura como solicitado sin resultado.
- **CA-2** — Dado un episodio con resultados de laboratorio disponibles, cuando el médico consulta esa cama, entonces obtiene esos resultados.

---

### RF-REG-07 — Registro de indicación a distancia

**Enunciado:** CUANDO el responsable clínico vigente o su delegado activo registra una indicación a distancia desde un dispositivo personal con identidad verificada, el sistema DEBE incorporarla a la cama con su autoría e instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico que tomó un caso y conserva la responsabilidad vigente en un dispositivo personal con identidad verificada, cuando registra una indicación a distancia, entonces la indicación integra las vigentes con su autoría e instante.

---

### RF-REG-08 — Resumen de la evolución de la cama

**Enunciado:** CUANDO un médico consulta la evolución de una cama, el sistema DEBE presentar la tendencia disponible de hasta seis horas, los parámetros ventilatorios vigentes y la última evolución registrada.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con seis horas de registros y ventilación mecánica, cuando el médico consulta su evolución, entonces obtiene la tendencia, el modo, frecuencia, volumen corriente, PEEP y FiO2, y la última evolución.
- **CA-2** — Dada una cama con dos horas de registros, cuando el médico consulta su evolución, entonces obtiene esas dos horas con la extensión del periodo declarada.

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

**Enunciado:** SI un profesional carece de responsabilidad clínica vigente, delegación activa, responsabilidad de jefatura, asignación médica vigente o asignación de cuidado de enfermería vigente sobre una cama, ENTONCES el sistema DEBE rechazar su registro sobre esa cama.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo, Carmen, Aníbal |
| Problema | P1, P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico sin responsabilidad clínica vigente, delegación, jefatura ni asignación médica, cuando intenta registrar sobre una cama, entonces el registro se rechaza.
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

### RF-IAM-04 — Aviso protegido en dispositivo no institucional

**Enunciado:** DONDE el destinatario recibe un escalamiento en un dispositivo no institucional sin identidad verificada, el sistema DEBE presentar únicamente sede, unidad, cama, severidad y motivo sin datos identificatorios del paciente.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico que recibe un escalamiento en un dispositivo no institucional sin identidad verificada, cuando llega el aviso, entonces obtiene únicamente sede, unidad, cama, severidad y motivo sin nombre ni documento de identidad del paciente.

---

### RF-IAM-05 — Reutilización de identidad verificada en dispositivo personal

**Enunciado:** DONDE el destinatario emplea un dispositivo personal con identidad verificada vigente, el sistema DEBE presentar el contexto clínico sin exigir una nueva verificación para cada escalamiento.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico con identidad verificada vigente en su dispositivo personal, cuando abre un escalamiento recibido, entonces obtiene el contexto clínico sin realizar otra verificación.

---

### RF-IAM-06 — Vigencia de la asignación de un rotante

**Enunciado:** CUANDO la Red asigna o retira a un profesional rotante, el sistema DEBE actualizar su responsabilidad clínica para el periodo efectivo comunicado.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un rotante asignado por la Red desde el lunes, cuando inicia ese periodo, entonces su responsabilidad clínica figura vigente en las unidades comunicadas.
- **CA-2** — Dado un rotante retirado por la Red desde el viernes, cuando inicia ese periodo, entonces su responsabilidad deja de figurar vigente en las unidades comunicadas.

---

### RF-IAM-07 — Restricción del contexto sin identidad verificada

**Enunciado:** SI un destinatario carece de identidad verificada vigente en el dispositivo empleado, ENTONCES el sistema DEBE impedirle consultar el contexto clínico del escalamiento.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal, Rodrigo |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico sin identidad verificada vigente en su dispositivo personal, cuando intenta consultar el contexto clínico, entonces el contexto no se presenta.

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
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una red con tres unidades y sus turnos registrados en un periodo, cuando la coordinadora obtiene los indicadores de cobertura de ese periodo, entonces obtiene las franjas descubiertas y las entregas cerradas de las tres unidades sin ingresar dato alguno.

---

### RF-SUP-03 — Revisión de la actividad de la unidad en un periodo

**Enunciado:** CUANDO un profesional consulta la actividad de una unidad en un periodo, el sistema DEBE presentar exactamente los eventos clínicos; los escalamientos con severidad, cadena alcanzada, acuses, tomas de caso y desenlace; las indicaciones registradas a distancia; y los ingresos y egresos ocurridos.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una unidad con un evento, dos escalamientos con sus recorridos y desenlaces, una indicación a distancia, un ingreso y un egreso durante la noche, cuando el médico consulta la actividad de esa noche, entonces obtiene exactamente esos elementos en un solo resultado.

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

## Matriz de trazabilidad

Cada tarea crítica de cada persona traza a al menos un RF. Las filas sin RF son brechas abiertas.

| Persona | Tarea crítica | RF que la cubre |
|---|---|---|
| Rodrigo | Recibir el handoff estructurado de todas las camas asignadas | RF-DIA-02, RF-DIA-03, RF-DIA-09, RF-DIA-10, RF-DIA-17 |
| Rodrigo | Consultar la evolución y el diagnóstico del turno anterior | RF-DIA-02, RF-DIA-05, RF-DIA-07, RF-DIA-10, RF-DIA-13, RF-DIA-14, RF-DIA-15 |
| Rodrigo | Registrar nota de evolución y diagnóstico por paciente | RF-DIA-07, RF-DIA-13, RF-DIA-14, RF-DIA-15, RF-DIA-16, RF-IAM-01 |
| Rodrigo | Marcar pacientes inestables o con pendientes críticos | RF-DIA-06 |
| Rodrigo | Consultar resultados de laboratorio e imágenes | RF-REG-06 |
| Rodrigo | Cerrar y firmar la entrega de turno | RF-DIA-01, RF-DIA-04, RF-DIA-12 |
| Milagros | Registrar signos vitales y balance por paciente | RF-REG-01, RF-REG-02 |
| Milagros | Escalar un deterioro clínico al médico responsable | RF-ESC-01, RF-ESC-06, RF-ESC-11 |
| Milagros | Consultar quién está de guardia y su estado de disponibilidad | RF-ESC-08 |
| Milagros | Ver y confirmar indicaciones médicas vigentes | RF-REG-03, RF-REG-04 |
| Milagros | Registrar eventos y administración de medicamentos | RF-REG-05 |
| Milagros | Recibir y entregar el turno de enfermería | RF-DIA-08, RF-DIA-11 |
| Carmen | Elaborar y publicar la programación mensual de turnos | RF-TUR-04, RF-TUR-09, RF-TUR-10 |
| Carmen | Validar que no existan cruces ni franjas descubiertas | RF-TUR-01, RF-TUR-02, RF-TUR-07 |
| Carmen | Aprobar o rechazar intercambios y permisos | RF-TUR-06, RF-TUR-12, RF-TUR-13, RF-TUR-17 |
| Carmen | Reasignar cobertura ante una ausencia imprevista | RF-TUR-03, RF-TUR-05, RF-TUR-18, RF-TUR-19, RF-TUR-20, RF-TUR-25, RF-TUR-26 |
| Carmen | Monitorear cumplimiento y completitud de entregas de turno | RF-DIA-12, RF-SUP-01 |
| Carmen | Generar indicadores de cobertura para la Dirección de Red | RF-SUP-02 |
| Aníbal | Recibir la alerta de escalamiento con contexto clínico adjunto | RF-ESC-03, RF-ESC-16, RF-IAM-04, RF-IAM-05, RF-IAM-07 |
| Aníbal | Confirmar recepción y tomar el caso | RF-ESC-04, RF-ESC-12, RF-ESC-14, RF-ESC-19 |
| Aníbal | Consultar tendencia de signos, ventilación y última evolución | RF-REG-08 |
| Aníbal | Registrar la indicación dada de forma remota | RF-REG-07, RF-IAM-02, RF-IAM-05, RF-IAM-07 |
| Aníbal | Marcarse temporalmente indisponible y delegar | RF-ESC-07, RF-ESC-17 |
| Aníbal | Revisar en la mañana lo ocurrido durante la noche | RF-SUP-03 |

## Cobertura de criterios de éxito

| Persona | Criterio de éxito | RF que lo satisface |
|---|---|---|
| Rodrigo | Entender el estado de las camas empleando solo el sistema | RF-DIA-02, RF-DIA-05, RF-DIA-10, RF-DIA-17 |
| Rodrigo | El handoff incluye decisiones y su justificación | RF-DIA-02, RF-DIA-13 |
| Rodrigo | Ninguna cama llega sin diagnóstico; si falta, el sistema lo señala | RF-DIA-01, RF-DIA-03, RF-DIA-12 |
| Rodrigo | Registrar la nota de evolución cuesta menos que escribirla a mano | RF-DIA-07, `RNF-USA-01` |
| Rodrigo | Ver qué cambió desde su último contacto con el paciente | RF-DIA-05 |
| Milagros | Escalar un deterioro en el mínimo de pasos | RF-ESC-01, RF-ESC-11, `RNF-USA-02` |
| Milagros | Ver quién está de guardia en este momento | RF-ESC-08, RF-ESC-12, RF-ESC-17 |
| Milagros | Recibir confirmación visible de que el médico vio la alerta | RF-ESC-04, RF-ESC-14 |
| Milagros | Si nadie responde, el sistema escala sin que ella intervenga | RF-ESC-02, RF-ESC-09 |
| Milagros | Registrar a pie de cama, sin caminar hasta la estación | RF-REG-01, RF-REG-02, RF-REG-05 |
| Milagros | Dejar de transcribir del papel al sistema | RF-REG-05, RF-DIA-08, RF-DIA-11 |
| Carmen | El sistema impide guardar una asignación con cruce | RF-TUR-01 |
| Carmen | Cubrir una ausencia imprevista toma minutos | RF-TUR-03, RF-TUR-18, RF-TUR-19, RF-TUR-20, RF-TUR-25 |
| Carmen | Una sola versión vigente del rol, con historial de cambios | RF-TUR-04, RF-TUR-14 |
| Carmen | Ver qué franjas de los próximos días están descubiertas | RF-TUR-07 |
| Carmen | Saber qué entregas se cerraron sin diagnóstico registrado | RF-DIA-12, RF-SUP-01 |
| Carmen | Los indicadores salen del sistema sin trabajo manual | RF-SUP-02 |
| Aníbal | La alerta incluye el contexto clínico mínimo sin pedirlo | RF-DIA-13, RF-DIA-14, RF-ESC-03 |
| Aníbal | Decidir si acude, con el contexto ya recibido | RF-ESC-03, RF-REG-08 |
| Aníbal | Confirmar recepción y que quien escaló lo vea de inmediato | RF-ESC-04, RF-ESC-14 |
| Aníbal | Registrar su indicación remota con hora y autoría | RF-REG-07, RF-IAM-05, RF-IAM-07 |
| Aníbal | Si no responde, el sistema escala solo y él se entera | RF-ESC-02, RF-ESC-10 |
| Aníbal | Revisar en un solo lugar lo ocurrido en la noche | RF-SUP-03 |

## Cobertura de problemas críticos

| Problema | RF que lo resuelve |
|---|---|
| P1 — Rotación de doctor | RF-TUR-01 a RF-TUR-26; RF-DIA-01 a RF-DIA-17; RF-REG-06; RF-IAM-01, RF-IAM-02, RF-IAM-03, RF-IAM-06; RF-SUP-01, RF-SUP-02 |
| P2 — Medianoche | RF-ESC-01 a RF-ESC-19; RF-REG-07, RF-REG-08; RF-IAM-02, RF-IAM-04, RF-IAM-05, RF-IAM-07; RF-SUP-03, RF-SUP-04 |
| P3 — Actualizaciones en tiempo real | RF-ESC-08, RF-ESC-13, RF-ESC-16; RF-REG-01 a RF-REG-05 |

## Cobertura de las preguntas del enunciado

| Pregunta del caso | RF que la responde |
|---|---|
| Qué ocurre si un paciente se agrava en el turno noche | RF-ESC-01, RF-ESC-06, RF-ESC-11, RF-ESC-15, RF-ESC-16 |
| Cómo se contacta rápidamente al médico encargado | RF-ESC-01, RF-ESC-08 |
| Qué ocurre si el médico no está disponible | RF-ESC-02, RF-ESC-07, RF-ESC-09, RF-ESC-17, RF-ESC-18 |
| Cómo se avisa a varios médicos y enfermeras | RF-ESC-13 |
| Con qué garantía se conserva el diagnóstico | RF-DIA-07, `RNF-SEG-03` |
| Cómo se sostiene su disponibilidad permanente | RF-DIA-10, RF-REG-02, `RNF-DIS-01`, `RNF-DIS-02` |

## Requerimientos de origen normativo

Estos RF no nacen de una tarea crítica sino de las restricciones externas declaradas en la sección 2.4
del [`README.md`](../README.md). Trazan igualmente a la persona sobre cuya operación recaen.

| Restricción externa | RF que la observa |
|---|---|
| Ley N.° 29733 — trazabilidad del acceso a datos de salud | RF-IAM-03 |
| Ley N.° 29733 — acceso limitado al ámbito de responsabilidad | RF-IAM-02 |
| Ley N.° 29733 — exposición de datos fuera del entorno institucional | RF-IAM-04, RF-IAM-05, RF-IAM-07 |
| SUSALUD — atribución cierta del registro clínico | RF-IAM-01, RF-DIA-07 |

## Decisión de tensiones

Cada tensión documentada en [`Personas/README.md`](../Personas/README.md) se decide en un RF. Una
tensión sin RF que la resuelva es una brecha de consistencia.

| Tensión | RF que la decide | Decisión adoptada |
|---|---|---|
| Velocidad frente a completitud del registro | RF-DIA-01, RF-DIA-07, RF-DIA-13 a RF-DIA-16 | El cierre exige el diagnóstico mínimo y los demás componentes se registran una sola vez para su reutilización, evitando que completitud signifique reingreso. |
| Sensibilidad del escalamiento | RF-ESC-06, RF-ESC-11, RF-ESC-16 | La enfermera puede escalar sin clasificar; la duda obtiene plazo inmediato pero se presenta distinta y detrás del deterioro confirmado para preservar la respuesta selectiva. |
| Autonomía de intercambio de turnos | RF-TUR-06, RF-TUR-13, RF-TUR-17 | La coordinadora aprueba o rechaza autorizaciones reutilizables por alcance y periodo; los intercambios cubiertos se aplican sin una resolución individual adicional. |
| Adopción voluntaria | RF-TUR-08, RF-TUR-16 | El sistema es la única fuente editable y las copias se limitan a periodos cerrados con condición histórica no operativa. |
| Movilidad frente a control de datos | RF-REG-07, RF-IAM-04, RF-IAM-05, RF-IAM-07 | Se admite el dispositivo personal, el aviso previo expone solo contexto operativo y una identidad verificada vigente permite leer y registrar sin repetir la verificación en cada alerta. |

## Distribución de prioridad

| Prioridad | Cantidad | Proporción | Criterio aplicado |
|---|---|---|---|
| MUST | 60 | 74.1 % | Es la única cobertura de una tarea crítica, o su ausencia deja sin resolver un problema crítico |
| SHOULD | 19 | 23.5 % | Sostiene un criterio de éxito, o refuerza una tarea crítica que ya tiene cobertura MUST |
| COULD | 2 | 2.5 % | Preserva una práctica vigente del equipo sin condicionar la operación clínica |
