# Requerimientos Funcionales

Sistema de Gestión de UCI — Essalud

Forma y verificación: [`docs/CONVENCIONES.md`](../docs/CONVENCIONES.md), secciones 5, 6 y 9.
Este documento es el único insumo de requerimientos que puntúa [`Spec/Eval-Spec.MD`](../Spec/Eval-Spec.MD).

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

---

## RF-DIA — Diagnósticos y entrega de turno

### RF-DIA-01 — ‹título›

**Enunciado:** CUANDO ‹disparador›, el sistema DEBE ‹respuesta›.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado ‹estado›, cuando ‹disparador›, entonces ‹resultado observable›.

---

## RF-ESC — Escalamiento y disponibilidad del médico

### RF-ESC-01 — ‹título›

**Enunciado:** SI ‹condición no deseada›, ENTONCES el sistema DEBE ‹respuesta›.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado ‹estado›, cuando ‹disparador›, entonces ‹resultado observable›.

---

## RF-TUR — Gestión de turnos

### RF-TUR-01 — ‹título›

**Enunciado:** SI ‹condición no deseada›, ENTONCES el sistema DEBE ‹respuesta›.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado ‹estado›, cuando ‹disparador›, entonces ‹resultado observable›.

---

## Matriz de trazabilidad

Cada tarea crítica de cada persona traza a al menos un RF. Las filas sin RF son brechas abiertas.

| Persona | Tarea crítica | RF que la cubre |
|---|---|---|
| Rodrigo | Recibir el handoff estructurado de todas las camas asignadas | |
| Rodrigo | Consultar la evolución y el diagnóstico del turno anterior | |
| Rodrigo | Registrar nota de evolución y diagnóstico por paciente | |
| Rodrigo | Marcar pacientes inestables o con pendientes críticos | |
| Rodrigo | Consultar resultados de laboratorio e imágenes | |
| Rodrigo | Cerrar y firmar la entrega de turno | |
| Milagros | Registrar signos vitales y balance por paciente | |
| Milagros | Escalar un deterioro clínico al médico responsable | |
| Milagros | Consultar quién está de guardia y su estado de disponibilidad | |
| Milagros | Ver y confirmar indicaciones médicas vigentes | |
| Milagros | Registrar eventos y administración de medicamentos | |
| Milagros | Recibir y entregar el turno de enfermería | |
| Carmen | Elaborar y publicar la programación mensual de turnos | |
| Carmen | Validar que no existan cruces ni franjas descubiertas | |
| Carmen | Aprobar o rechazar intercambios y permisos | |
| Carmen | Reasignar cobertura ante una ausencia imprevista | |
| Carmen | Monitorear cumplimiento y completitud de entregas de turno | |
| Carmen | Generar indicadores de cobertura para la Dirección de Red | |
| Aníbal | Recibir la alerta de escalamiento con contexto clínico adjunto | |
| Aníbal | Confirmar recepción y tomar el caso | |
| Aníbal | Consultar tendencia de signos, ventilación y última evolución | |
| Aníbal | Registrar la indicación dada de forma remota | |
| Aníbal | Marcarse temporalmente indisponible y delegar | |
| Aníbal | Revisar en la mañana lo ocurrido durante la noche | |

## Cobertura de problemas críticos

| Problema | RF que lo resuelve |
|---|---|
| P1 — Rotación de doctor | |
| P2 — Medianoche | |
| P3 — Actualizaciones en tiempo real | |

## Decisión de tensiones

Cada tensión documentada en [`Personas/README.md`](../Personas/README.md) se decide en un RF. Una
tensión sin RF que la resuelva es una brecha de consistencia.

| Tensión | RF que la decide |
|---|---|
| Velocidad frente a completitud del registro | |
| Sensibilidad del escalamiento | |
| Autonomía de intercambio de turnos | |
| Adopción voluntaria | |
| Movilidad frente a control de datos | |
