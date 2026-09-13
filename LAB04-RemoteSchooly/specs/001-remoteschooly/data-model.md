# Data Model: RemoteSchooly

El modelo es lógico. No prescribe motor, nombres SQL ni particiones.

## Actor

| Campo | Regla |
|---|---|
| `actor_id` | Identificador estable |
| `role` | Gobierno, Alumno, ProfesorLima o ProfesorProvincia |
| `site_ids` | Sedes autorizadas; vacío para roles centrales cuando aplique |
| `course_ids` | Cursos autorizados |
| `status` | Activo o revocado |

Un equipo compartido cambia de actor activo; nunca hereda los permisos de la sesión anterior.

## Site

| Campo | Regla |
|---|---|
| `site_id` | Identificador estable de sede |
| `name`, `region` | Etiquetas de operación |
| `timezone` | Interpreta semana y vigencia |
| `storage_budget_bytes` | Límite configurable del nodo |
| `last_seen_at` | Última telemetría confirmada |
| `freshness_threshold` | Umbral para mostrar `sin reporte reciente` |

## Course y CourseWeek

- **Course**: `course_id`, área, grado, audiencia, docentes responsables, estado.
- **CourseWeek**: `course_week_id`, curso, número/intervalo, vigencia y estado editorial.

Una combinación curso + semana + audiencia es la identidad pedagógica previa a una publicación.

## MaterialUnit

| Campo | Regla |
|---|---|
| `unit_id`, `version` | Identidad inmutable de la revisión |
| `course_week_id` | Semana a la que pertenece |
| `author_id` | Profesor de Lima |
| `source_ids` | Fuentes aprobadas usadas |
| `approval_status` | Draft, InReview, Approved o Rejected |
| `approved_by`, `approved_at` | Obligatorios en `Approved` |
| `quality_score`, `rubric_version` | Comparación base/optimizada |
| `ai_usage_ids` | Cero o más solicitudes; vacío si fue manual |

## Package y Manifest

### Package

`package_id`, `course_week_id`, audiencia, versión, vigencia, `manifest_id`, publicación, revocación.

Estados centrales:

```text
Draft -> Approved -> Published -> Revoked
```

No se edita `Published`; una corrección crea otra versión.

### ManifestEntry

`manifest_id`, `resource_hash`, nombre lógico, tipo, tamaño, obligatorio, variante de consumo y
objetivo pedagógico. Si un recurso obligatorio es audiovisual, otra entrada con el mismo objetivo se
marca como variante de bajo consumo.

## Assignment

`assignment_id`, paquete, sede, curso, vigencia y estado. BR-01 impide dos asignaciones activas para
la misma identidad de semana.

## SitePackageState

| Estado | Condición |
|---|---|
| `Assigned` | La sede conoce la asignación; aún no inicia |
| `Syncing` | Hay recursos o fragmentos pendientes |
| `Incomplete` | La sesión cerró con ausencia, corrupción o espacio insuficiente |
| `Ready` | Todas las entradas obligatorias de una versión pasaron |
| `Revoked` | La sede recibió la revocación |

La activación cambia el puntero `active_package_id` de una vez. El directorio parcial nunca es activo.

## SyncSession y ChunkReceipt

- **SyncSession**: sesión, sede, paquete, manifiesto, bytes totales/verificados, inicio, último intento,
  estado y error accionable.
- **ChunkReceipt**: recurso, rango, validador de versión, huella parcial y confirmación local.

Un rango solo se reutiliza si pertenece al mismo recurso y validador. Cambiar el manifiesto invalida
fragmentos que no resuelvan a la misma huella de contenido.

## StudentProgress y LocalOutboxItem

- **StudentProgress**: `progress_id` idempotente, alumno, curso, semana, actividad, resultado,
  `occurred_at`, estado de confirmación.
- **LocalOutboxItem**: secuencia local, tipo, carga cifrada, intentos, último error y confirmación.

Estados:

```text
PendingLocal -> Sent -> Confirmed
                    \-> PendingLocal (reintento con el mismo progress_id)
```

## AIUsageRecord

`usage_id`, docente, curso, tarea, unidad, política, modelo lógico, input, output, cached input
reportado, reutilizado sin llamada, fecha, resultado y motivo de rechazo. Nunca contiene datos de
alumnos.

## TokenBaseline y TokenComparison

- **TokenBaseline**: versión, corpus, tareas, fuentes, rúbrica, umbral de calidad y consumo por unidad.
- **TokenComparison**: línea base, política optimizada, unidades comparables, tokens base/optimizados,
  ahorro calculado y diferencia de calidad.

Una comparación es publicable solo si las tareas, fuentes y rúbrica coinciden y ambas variantes
superan el mismo umbral de calidad.

## TokenBudget y BudgetException

- **TokenBudget**: programa/curso/periodo, límite, consumo y estado.
- **BudgetException**: actor gubernamental, motivo, límite adicional, vigencia y auditoría.

## AuditEvent

Evento append-only con actor, rol, acción, objeto, fecha, resultado y razón. Incluye publicación,
revocación, asignación, excepción y transición de paquete; no almacena contenido personal.
