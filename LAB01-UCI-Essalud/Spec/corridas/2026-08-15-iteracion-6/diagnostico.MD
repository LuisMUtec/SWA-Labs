# Diagnóstico — corrida 2026-08-15-iteracion-6

Evidencia de la agregación. `ReqFunc.MD` @ `4b277e9`, rúbrica `Spec/Eval-Spec.MD` @ `b492237`,
146 requerimientos funcionales, cuatro evaluaciones de persona presentes y completas.

## Precondiciones

| Comprobación | Resultado |
|---|---|
| Cuatro evaluaciones presentes | sí — `veredicto-{rodrigo,milagros,carmen,anibal}.MD` |
| Veredicto para los 146 RF vigentes | sí, en las cuatro, mismo conjunto y orden de IDs |
| Vocabulario cerrado (Sirve/Indiferente/Estorba/Ambiguo) | sí, sin veredictos inválidos |
| Distribución | Rodrigo 55/83/5/3 · Milagros 60/82/2/2 · Carmen 75/64/3/4 · Aníbal 60/82/2/2 |

D1 es computable. Ninguna evaluación se sustituye por juicio propio.

## Reglas de derivación aplicadas

Para que las 24 tareas se puntúen con una sola vara y el puntaje se derive en lugar de juzgarse dos
veces, se aplican estas reglas, iguales para las cuatro personas:

- **5** — todos los RF de la fila de esa tarea en la matriz de trazabilidad son Sirve o Indiferente, y
  el agente no declara comportamiento faltante ni criterio de éxito relacionado incumplido.
- **3** — al menos un RF Sirve la aborda, y ocurre una de dos: el agente declara comportamiento
  faltante o un criterio de éxito relacionado incumplido, o un RF implicado en la tarea recibió
  Estorba o Ambiguo.
- **1** — los únicos RF que la trazan son Ambiguo, o la cobertura se apoya en una capacidad que
  ningún enunciado declara.
- **0** — ningún RF la traza, o el único que la traza recibió Estorba.

Ninguna tarea de esta corrida cae en 1 ni en 0: las 24 tienen al menos un RF Sirve que las aborda.
Todas las rebajas a 3 citan una declaración escrita del agente correspondiente.

## Veredictos agregados

Un RF **Estorba** que no traza a ninguna de las seis tareas de esa persona suma a `X_p` y resta 2. Un
RF **Estorba** que sí traza a una de sus tareas no suma a `X_p`: baja esa tarea a 3.

| RF | Rodrigo | Milagros | Carmen | Aníbal | Efecto en D1 |
|---|---|---|---|---|---|
| RF-TUR-01 | Indiferente | Indiferente | Sirve | Sirve | — |
| RF-TUR-02 | Indiferente | Indiferente | Ambiguo | Indiferente | Ambiguo de Carmen |
| RF-TUR-03 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-04 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-TUR-05 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-TUR-06 | Sirve | Indiferente | Estorba | Indiferente | Estorba en tarea de Carmen: baja su tarea a 3 |
| RF-TUR-07 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-08 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-TUR-09 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-10 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-11 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-12 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-13 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-14 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-15 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-16 | Indiferente | Indiferente | Ambiguo | Indiferente | Ambiguo de Carmen |
| RF-TUR-17 | Estorba | Indiferente | Sirve | Indiferente | X_R +1 (−2) |
| RF-TUR-18 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-19 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-20 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-21 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-22 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-23 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-24 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-25 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-26 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-TUR-27 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-TUR-28 | Indiferente | Estorba | Sirve | Indiferente | X_M +1 (−2) |
| RF-TUR-29 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-30 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-31 | Estorba | Indiferente | Sirve | Indiferente | X_R +1 (−2) |
| RF-TUR-32 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-33 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-34 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-35 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-36 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-37 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-38 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-39 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-40 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-41 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-42 | Sirve | Sirve | Sirve | Indiferente | — |
| RF-TUR-43 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-44 | Estorba | Indiferente | Sirve | Indiferente | X_R +1 (−2) |
| RF-TUR-45 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-46 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-DIA-01 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-DIA-02 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-03 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-04 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-05 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-DIA-06 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-DIA-07 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-DIA-08 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-09 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-10 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-11 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-12 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-13 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-DIA-14 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-DIA-15 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-16 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-17 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-18 | Sirve | Sirve | Sirve | Indiferente | — |
| RF-DIA-19 | Indiferente | Ambiguo | Indiferente | Indiferente | Ambiguo de Milagros |
| RF-DIA-20 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-21 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-22 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-DIA-23 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-DIA-24 | Estorba | Indiferente | Sirve | Indiferente | Estorba en tarea de Rodrigo: baja su tarea a 3 |
| RF-DIA-25 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-26 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-27 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-28 | Sirve | Sirve | Sirve | Sirve | — |
| RF-DIA-29 | Sirve | Sirve | Estorba | Indiferente | X_C +1 (−2) |
| RF-DIA-30 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-31 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-32 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-33 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-34 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-35 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-36 | Sirve | Estorba | Sirve | Indiferente | X_M +1 (−2) |
| RF-ESC-01 | Sirve | Sirve | Sirve | Sirve | — |
| RF-ESC-02 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-03 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-04 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-05 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-06 | Indiferente | Sirve | Indiferente | Ambiguo | Ambiguo de Aníbal |
| RF-ESC-07 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-08 | Indiferente | Sirve | Sirve | Ambiguo | Ambiguo de Aníbal |
| RF-ESC-09 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-10 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-ESC-11 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-12 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-13 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-ESC-14 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-15 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-16 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-17 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-18 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-19 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-20 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-21 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-22 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-23 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-24 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-25 | Indiferente | Sirve | Indiferente | Estorba | X_A +1 (−2) |
| RF-ESC-26 | Indiferente | Indiferente | Ambiguo | Indiferente | Ambiguo de Carmen |
| RF-ESC-27 | Sirve | Sirve | Sirve | Sirve | — |
| RF-ESC-28 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-29 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-30 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-31 | Indiferente | Indiferente | Sirve | Estorba | Estorba en tarea de Aníbal: baja su tarea a 3 |
| RF-ESC-32 | Indiferente | Sirve | Estorba | Sirve | X_C +1 (−2) |
| RF-ESC-33 | Indiferente | Indiferente | Sirve | Sirve | — |
| RF-ESC-34 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-ESC-35 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-36 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-01 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-02 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-03 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-REG-04 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-05 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-06 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-REG-07 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-08 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-REG-09 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-REG-10 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-REG-11 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-REG-12 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-IAM-01 | Ambiguo | Sirve | Sirve | Sirve | Ambiguo de Rodrigo |
| RF-IAM-02 | Ambiguo | Ambiguo | Sirve | Sirve | Ambiguo de Rodrigo; Ambiguo de Milagros |
| RF-IAM-03 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-IAM-04 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-IAM-05 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-IAM-06 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-IAM-07 | Ambiguo | Indiferente | Indiferente | Sirve | Ambiguo de Rodrigo |
| RF-IAM-08 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-IAM-09 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-IAM-10 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-SUP-01 | Estorba | Indiferente | Sirve | Indiferente | X_R +1 (−2) |
| RF-SUP-02 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-SUP-03 | Indiferente | Sirve | Ambiguo | Sirve | Ambiguo de Carmen |
| RF-SUP-04 | Indiferente | Indiferente | Indiferente | Indiferente | — |
| RF-SUP-05 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-SUP-06 | Indiferente | Indiferente | Sirve | Indiferente | — |

## Daño fuera de tarea — `X_p`

| Persona | RF Estorba | Traza a una de sus seis tareas | Cuenta en `X_p` |
|---|---|---|:---:|
| Rodrigo | RF-TUR-17 | no | sí |
| Rodrigo | RF-TUR-31 | no (traza a la tarea 3 de Carmen) | sí |
| Rodrigo | RF-TUR-44 | no (traza a la tarea 4 de Carmen) | sí |
| Rodrigo | RF-DIA-24 | **sí** — tarea 6 «Cerrar y firmar la entrega de turno» | no |
| Rodrigo | RF-SUP-01 | no (traza a la tarea 5 de Carmen) | sí |
| Milagros | RF-TUR-28 | no | sí |
| Milagros | RF-DIA-36 | no (traza a la tarea 4 de Carmen) | sí |
| Carmen | RF-TUR-06 | **sí** — tarea 3 «Aprobar o rechazar intercambios y permisos» | no |
| Carmen | RF-DIA-29 | no (traza a las tareas 1 y 2 de Rodrigo y a la 2 de Milagros) | sí |
| Carmen | RF-ESC-32 | no (traza a la tarea 3 de Milagros y a la 5 de Aníbal) | sí |
| Aníbal | RF-ESC-25 | no (traza a la tarea 2 de Milagros) | sí |
| Aníbal | RF-ESC-31 | **sí** — tarea 5 «Marcarse temporalmente indisponible y delegar» | no |

`X_Rodrigo = 4` · `X_Milagros = 2` · `X_Carmen = 2` · `X_Aníbal = 1`.

## Matriz de cobertura

| Persona | Tarea crítica | RF que la cubre | Veredicto | Puntos | Estado |
|---|---|---|---|---:|---|
| Rodrigo | 1. Recibir el handoff estructurado de todas las camas asignadas | RF-DIA-02, 03, 09, 10, 17, 18, 28, 29, 32, 35 | todos Sirve | 3 | Incompleta — el agente declara que ningún RF arma la vista de la unidad completa priorizada: RF-DIA-02 entrega cama por cama y RF-DIA-22 sólo las marcadas. Cae su criterio «entender diez camas en ≤ 15 min usando solo el sistema» |
| Rodrigo | 2. Consultar la evolución y el diagnóstico del turno anterior | RF-DIA-02, 05, 07, 10, 13, 14, 15, 21, 23 | todos Sirve | 3 | Incompleta — RF-DIA-13 crea el fundamento y RF-DIA-02 lo entrega, pero ningún RF lo vuelve exigible; RF-DIA-02 CA-4 admite entregarlo declarado no registrado. Cae su criterio «el handoff incluye decisiones y su justificación» |
| Rodrigo | 3. Registrar nota de evolución y diagnóstico por paciente | RF-DIA-07, 13, 14, 15, 16, RF-IAM-01, 02, 09, 10 | Sirve, salvo RF-IAM-01 y RF-IAM-02 **Ambiguo** | 3 | Incompleta — el acto de escribir la nota no lo abarata ningún RF y la atribución en la PC compartida se apoya en dos Ambiguos |
| Rodrigo | 4. Marcar pacientes inestables o con pendientes críticos | RF-DIA-06, RF-DIA-22 | ambos Sirve | 3 | Incompleta — RF-DIA-06 deja que cualquier profesional retire la marca y ningún RF avisa de la retirada. El propio agente declara que la tarea 5 es «la única de mis seis que sale completa» |
| Rodrigo | 5. Consultar resultados de laboratorio e imágenes | RF-REG-06, 10, 12, RF-ESC-29 | todos Sirve | 5 | Cubierta — declarada completa y sin apoyo en ningún Ambiguo |
| Rodrigo | 6. Cerrar y firmar la entrega de turno | RF-DIA-01, 04, 12, 20, 24, 31, 34, RF-TUR-42 | Sirve, salvo RF-DIA-24 **Estorba** | 3 | Incompleta — RF-DIA-24 y RF-SUP-01 convierten el turno no cerrado en un reporte a la jefatura sin devolverle un minuto |
| Milagros | 1. Registrar signos vitales y balance por paciente | RF-REG-01, RF-REG-02 | ambos Sirve | 5 | Cubierta — declarada «de punta a punta»; el costo por toque es RNF y no se reclama aquí |
| Milagros | 2. Escalar un deterioro clínico al médico responsable | RF-ESC-01, 06, 11, 15, 20, 21, 22, 23, 25, 27, 35, RF-DIA-29 | todos Sirve | 3 | Incompleta — no puede escalar sobre la cama de su colega sin relevo declarado previo (RF-IAM-02, **Ambiguo**), y su persona documenta que cubren diez camas entre dos |
| Milagros | 3. Consultar quién está de guardia y su estado de disponibilidad | RF-ESC-08, 27, 32, 35 | todos Sirve | 3 | Incompleta — RF-DIA-28 CA-2 excluye la guardia localizable: en una noche cubierta sólo por un localizable ninguna cama tiene responsable clínico vigente y RF-ESC-08 no tiene a quién presentar |
| Milagros | 4. Ver y confirmar indicaciones médicas vigentes | RF-REG-03, 04, RF-ESC-13, 28, 36 | Sirve, salvo RF-ESC-13 Indiferente | 3 | Incompleta — RF-ESC-28 sólo declara la indicación nueva; la suspensión o el cambio de una vigente no la alcanza junto a la cama |
| Milagros | 5. Registrar eventos y administración de medicamentos | RF-REG-05, RF-IAM-02, RF-IAM-10 | Sirve, salvo RF-IAM-02 **Ambiguo** | 3 | Incompleta — el registro sobre la cama de la colega exige un relevo que ella no puede declarar en el momento |
| Milagros | 6. Recibir y entregar el turno de enfermería | RF-DIA-08, 11, 19, 25, 26, 27, 30, 33 | Sirve, salvo RF-DIA-19 **Ambiguo** | 3 | Incompleta — RF-DIA-08 y RF-DIA-11 enumeran «exactamente» cinco componentes y dejan fuera el escalamiento abierto y las indicaciones vigentes |
| Carmen | 1. Elaborar y publicar la programación mensual de turnos | RF-TUR-04, 09, 10, 11, 27, 28, 46 | todos Sirve | 3 | Incompleta — la publicación «sin infracciones» depende del control de horas y ese control se apoya en RF-TUR-02, que ella marcó **Ambiguo** |
| Carmen | 2. Validar que no existan cruces ni franjas descubiertas | RF-TUR-01, 02, 07, 42, 45, RF-ESC-26, 30, 31, 33 | Sirve, salvo RF-TUR-02 y RF-ESC-26 **Ambiguo** | 3 | Incompleta — dos guardias localizables simultáneas en sedes distintas no se rechazan, y la indisponibilidad sin delegado (RF-ESC-32, Estorba) deja la franja figurando cubierta |
| Carmen | 3. Aprobar o rechazar intercambios y permisos | RF-TUR-06, 12, 13, 17, 21, 22, 29, 30, 31, 32, 33, 34 | Sirve, salvo RF-TUR-06 **Estorba** | 3 | Incompleta — RF-TUR-06 aplica a su programación un intercambio sin resolución suya; RF-TUR-34 avisa después del hecho |
| Carmen | 4. Reasignar cobertura ante una ausencia imprevista | RF-TUR-03, 05, 18, 19, 20, 25, 26, 35, 36, 37, 38, 39, 40, 41, 43, 44, RF-DIA-36 | todos Sirve | 3 | Incompleta — el filtro de horas del mes no queda firme (RF-TUR-02) y la aceptación que sí produciría cruce no tiene respuesta declarada (RF-TUR-35) |
| Carmen | 5. Monitorear cumplimiento y completitud de entregas de turno | RF-DIA-12, 24, RF-SUP-01 | todos Sirve | 5 | Cubierta — el agente la declara «la tarea que sale de esta iteración más entera» |
| Carmen | 6. Generar indicadores de cobertura para la Dirección de Red | RF-SUP-02, RF-SUP-05 | ambos Sirve | 5 | Cubierta — su criterio «los indicadores salen sin trabajo manual» queda satisfecho; el Ambiguo de RF-SUP-03 recae sobre otra consulta |
| Aníbal | 1. Recibir la alerta de escalamiento con contexto clínico adjunto | RF-ESC-03, 16, 24, RF-IAM-04, 05, 07, 08 | todos Sirve | 3 | Incompleta — el agente declara sin cubrir la constitución y vigencia de sus medios de contacto, que RF-TUR-05 y RF-TUR-26 invocan y ningún RF constituye; es por donde hoy se pierde la llamada que sí importaba |
| Aníbal | 2. Confirmar recepción y tomar el caso | RF-ESC-04, 12, 14, 19 | todos Sirve | 5 | Cubierta — «la mitad que le corresponde a este documento está entera»; el esfuerzo de un toque es RNF |
| Aníbal | 3. Consultar tendencia de signos, ventilación y última evolución | RF-REG-08, RF-DIA-05 | ambos Sirve | 3 | Incompleta — sin registro previo suyo sobre esa cama, RF-DIA-05 computa el diferencial desde la apertura del episodio: tres semanas de cambios no son un resumen |
| Aníbal | 4. Registrar la indicación dada de forma remota | RF-REG-07, 09, 11, RF-IAM-02, 05, 07, 08, 09 | todos Sirve | 5 | Cubierta — «el circuito está completo de punta a punta»; es su tarea mejor cubierta |
| Aníbal | 5. Marcarse temporalmente indisponible y delegar | RF-ESC-07, 17, 30, 31, 32, 34, 35 | Sirve, salvo RF-ESC-31 **Estorba**; RF-ESC-08 **Ambiguo** la sostiene | 3 | Incompleta — la mitad «marcarme indisponible» sólo existe cuando no indica delegado (RF-ESC-32) |
| Aníbal | 6. Revisar en la mañana lo ocurrido durante la noche | RF-SUP-03 | Sirve | 5 | Cubierta — el CA-1 de RF-SUP-03 describe su caso exacto |

Σ por persona: **Rodrigo 20/30 · Milagros 20/30 · Carmen 22/30 · Aníbal 24/30**. Ninguna tarea en 0.

## Escenarios clave y claridad del flujo

| Persona | Recorrido | Paso decisivo | Flujo |
|---|---|---|---:|
| Rodrigo | Completo, doce pasos, sin corte | **Paso 11** — registra su decisión en la PC de la estación apoyado en RF-IAM-01 y RF-IAM-02, ambos **Ambiguo**; RF-IAM-07 roza el mismo paso | **2** |
| Milagros | **Se corta en el paso 8** | **Paso 8** — necesita saber si el médico baja. RF-REG-11 incorpora la decisión al episodio y ningún RF la hace llegar a quien escaló: RF-ESC-14 cubre destinatario, acuse y toma; RF-ESC-22 se dispara con el cambio de estado de atención, cuyos valores cerrados (emitido, alcanzado, acusado, tomado, cerrado, agotado) no comprenden esa decisión | **0** |
| Carmen | Completo, catorce pasos, sin corte | **Paso 5** — el filtro de horas del mes se sostiene en RF-TUR-02, **Ambiguo**: ningún RF constituye el vínculo laboral ni las reglas de jornada del personal de planta | **2** |
| Aníbal | Completo, trece pasos, sin corte | **Paso 2** — la composición de la cadena se apoya en RF-ESC-06, **Ambiguo**, que aplica «la cadena de esa severidad» mientras RF-ESC-23 la compone sin mirarla. La variante de indisponibilidad se apoya además en RF-ESC-08 | **2** |

**El corte de Milagros se confirma, no se rebaja.** Contra los RF: el glosario cierra el estado de
atención de un escalamiento en exactamente seis valores y ninguno es la decisión de acudir; RF-ESC-14
enumera «exactamente» destinatario, acuse y toma; RF-ESC-22 se dispara con el cambio de ese estado
cerrado; RF-ESC-13 entrega la actualización informativa a la consulta del responsable clínico y no a
quien escaló, y sólo comprende soporte ventilatorio, vasoactivo y traslado. Ningún RF hace llegar a la
enfermera la decisión de acudir. La regla de la rúbrica —un agente puede bajar D1, nunca subirla—
impide además elevar un corte que el agente declaró. Flujo 0.

## Cómputo de D1 — cada operación

```
Rodrigo   Σ tareas = 3 + 3 + 3 + 3 + 5 + 3 = 20 ;  X = 4
          máx(0, 20 − 2×4) / 5 + 2 = máx(0, 12) / 5 + 2 = 2,4 + 2      = 4,4
Milagros  Σ tareas = 5 + 3 + 3 + 3 + 3 + 3 = 20 ;  X = 2
          máx(0, 20 − 2×2) / 5 + 0 = máx(0, 16) / 5 + 0 = 3,2 + 0      = 3,2
Carmen    Σ tareas = 3 + 3 + 3 + 3 + 5 + 5 = 22 ;  X = 2
          máx(0, 22 − 2×2) / 5 + 2 = máx(0, 18) / 5 + 2 = 3,6 + 2      = 5,6
Aníbal    Σ tareas = 3 + 5 + 3 + 5 + 3 + 5 = 24 ;  X = 1
          máx(0, 24 − 2×1) / 5 + 2 = máx(0, 22) / 5 + 2 = 4,4 + 2      = 6,4

promedio = (4,4 + 3,2 + 5,6 + 6,4) / 4 = 19,6 / 4 = 4,9
D1       = 4,9 × 10                                                    = 49,0
```

Techo duro comprobado: ninguna persona tiene sus seis tareas en 0, de modo que el límite D1 ≤ 50 no
se activa. El valor cae por debajo por cómputo, no por techo.

## Discrepancias entre agente y cómputo

| Persona | Computado ×10 | Percibida | Δ | Qué falla: el agente o las tareas críticas |
|---|---:|---:|---:|---|
| Rodrigo | 44 | 78 | **34** | El agente. Marca Sirve 55 RF y describe con precisión cinco necesidades sin cubrir, pero al declarar su cobertura no descuenta ni los cuatro Estorba fuera de tarea ni los dos Ambiguos que sostienen el paso en que deja su decisión escrita |
| Milagros | 32 | 80 | **48** | El agente. Declara ella misma que su escenario se corta en el paso 8 y que cuatro de sus seis tareas quedan incompletas, y aun así se autoinforma 80 %. La percibida mide el alivio frente al papel, no la cobertura del escenario |
| Carmen | 56 | 82 | **26** | El agente. Su cobertura percibida recoge que 75 de 146 RF le sirven; el cómputo pesa que dos de sus tres Estorba caen fuera de sus tareas y que cuatro de sus seis tareas se apoyan en un Ambiguo o en un Estorba |
| Aníbal | 64 | 80 | 16 | Sin discrepancia reportable (≤ 20). Es el único autoinforme calibrado de la corrida |

En los tres casos prevalece el valor computado. Ninguna cobertura percibida alcanza el 90 %, de modo
que el contraste de conformidad unánime no se activa y D5 no queda limitada a 40.

## Cobertura de P1, P2 y P3

| Problema | RF asociados | Comportamiento que lo resuelve | Puntos |
|---|---|---|---:|
| **P1** — Rotación de doctor: el diagnóstico del médico previo debe estar disponible antes del cambio de turno | RF-DIA-07, 13, 14, 15, 16 (producción); RF-DIA-31 (composición); RF-DIA-01, 12, 20, 34 (completitud y cierre); RF-DIA-02, 03, 09, 10 (entrega al entrante); RF-DIA-17, 32 (borde: turno concluido sin cerrar); RF-DIA-18, 28 (a quién se entrega); RF-DIA-24, RF-SUP-01 (control) | Cerrado de extremo a extremo: el diagnóstico se registra versionado con autoría, la entrega se compone sin transcripción, el cierre queda impedido si falta el diagnóstico de alguna cama asignada, el entrante la recibe sin depender del saliente, el borde del turno no cerrado tiene respuesta declarada y lo incumplido llega a la jefatura | **100** |
| **P2** — Medianoche: contactar rápido al médico encargado y manejar su indisponibilidad | RF-ESC-01, 02, 03, 04, 06, 07, 09, 11, 12, 20, 21, 23, 25, 27, 30, 31, 32, 33, 34, 35; RF-IAM-04, 05, 07, 08; RF-REG-07, 11 | El contacto está resuelto: cadena compuesta de la programación vigente, contexto adjunto cerrado, avance automático sin intervención de quien escaló y acuse trazable. **La indisponibilidad queda a medias**: quien se declara indisponible sigue siendo responsable clínico vigente (RF-ESC-27) y encabezando la cadena (RF-ESC-23), de modo que el escalamiento le quema un plazo entero; la indisponibilidad con delegado no se registra como estado, aunque RF-ESC-08 lo enumere; la cadena termina en la jefatura sin comportamiento declarado si ella tampoco acusa; y una noche cubierta sólo por guardia localizable no tiene responsable clínico vigente que encabece la cadena | **50** |
| **P3** — Tiempo real: avisos a múltiples médicos y enfermeras, y persistencia del diagnóstico con disponibilidad permanente | RF-ESC-13, 16, 22, 28, 29, 36; RF-REG-01, 02, 03, 04, 05; RF-DIA-07 y RF-ESC-21 (persistencia) | Los tres hechos que alcanzan sin consulta previa —indicación nueva, resultado crítico y actualización informativa a enfermería— están declarados con destinatarios múltiples, y la persistencia sin pérdida ni duplicación cubre la desconexión. **Queda un tramo sin RF**: la suspensión o el cambio de una indicación vigente no alcanza junto a la cama a quien la ejecuta —RF-ESC-28 sólo declara la indicación nueva—, la decisión de acudir no alcanza a quien escaló, y nada declara que la enfermera vea junto a la cama que su escalamiento emitido sin conexión todavía no salió | **50** |

`D2 = (100 + 50 + 50) / 3 = 200 / 3 = 66,7`

Ningún problema queda en 0, de modo que el techo D2 ≤ 60 no se activa.

## Requerimientos mal formados

Las ocho condiciones se inventariaron sobre los 146 RF. Los controles mecánicos M1, M2 y M3 devuelven
vacío, de modo que no hay hallazgo automático de las condiciones 1, 3, 4 y 5. Las condiciones 1, 2, 3,
6 y 7 se comprobaron además sobre el texto completo: los 146 enunciados abren con un patrón EARS
admitido y llevan «el sistema DEBE»; ninguno acumula dos DEBE; los tres enunciados con punto y coma
—RF-ESC-03, RF-REG-08 y RF-SUP-03— lo usan para separar los ítems de una sola enumeración y no una
segunda respuesta; los 146 llevan al menos un criterio y los 187 criterios traen exactamente un par
Cuando/Entonces.

| ID | Condición de D3 incumplida | Corrección propuesta |
|---|---|---|
| RF-TUR-16 | 5 — nombra el medio de salida: «copia imprimible» y «archivo histórico» son el soporte, no la garantía | Enunciar la garantía que la persona necesita —un reflejo no editable y no operativo de las asignaciones de un periodo cerrado— y dejar el soporte fuera del enunciado |
| RF-TUR-28 | 5 — «copia imprimible» nombra el medio | Igual que el anterior: el enunciado ya declara «condición de reflejo no editable de la programación vigente», que es la garantía; el adjetivo del soporte sobra |
| RF-ESC-09 | 8 — el criterio amplía el contrato: el enunciado alcanza a «la jefatura vigente de la unidad» y CA-2 entrega al «delegado de esa jefatura», figura que el enunciado no declara | O el enunciado declara que la delegación activa de la jefatura desplaza el alcance, o CA-2 se retira |

`D3 = 143 / 146 × 100 = 97,9`

## Requerimientos huérfanos

| ID | Por qué no traza a nadie |
|---|---|
| — | Ninguno. Los 146 RF declaran persona y problema, las cuatro personas citadas existen y los tres problemas citados existen |

## Requerimientos mal ubicados

| ID | Por qué no es funcional | Documento que le corresponde |
|---|---|---|
| — | Ninguno. Todos los enunciados declaran comportamiento; los plazos se remiten a `ReqNoFunc.MD` sin fijar umbrales aquí | — |

## Trazabilidad — D4

| Tramo | Cálculo | Puntos |
|---|---|---:|
| RF con persona y problema, ambos existentes | 146 / 146 × 70 | 70,0 |
| Tareas críticas con al menos 1 punto en D1 | 24 / 24 × 30 | 30,0 |
| Filas de matriz interna que no coinciden con el cuerpo | 0 × (−10) | 0,0 |

Las matrices se verificaron contra el cuerpo, no se dieron por buenas: las 24 filas de la matriz de
trazabilidad citan sólo RF cuyo campo `Persona` declara a esa persona; las tres filas de cobertura de
problemas críticos coinciden exactamente con los RF cuyo campo `Problema` declara ese problema —94,
48 y 12 identificadores, sin sobrantes ni faltantes—; las 23 filas de cobertura de criterios de éxito
corresponden una a una con los criterios de las cuatro personas; y la distribución de prioridad
declara 63 MUST, 81 SHOULD y 2 COULD, que es lo que el documento contiene.

`D4 = 70 + 30 − 0 = 100,0`

## Tensiones sin decidir

| Tensión | Por qué ningún RF la resuelve |
|---|---|
| — | Ninguna. Las cinco están decididas en un RF |

| Tensión | RF que la decide | Comprobación |
|---|---|---|
| Velocidad frente a completitud del registro | RF-DIA-01, 31, 34 | El cierre exige un solo dato por cama y lo demás se compone sin transcripción; el señalamiento previo a la firma no condiciona el cierre. Rodrigo escribe que «la tensión quedó decidida de mi lado y lo reconozco»; Carmen la acepta con RF-DIA-31 y RF-DIA-12 como mitigación. **12** |
| Sensibilidad del escalamiento | RF-ESC-11, 25, 16, 24 | Se escala sin clasificar y lo no clasificado corre con el plazo del deterioro inmediato; la selectividad se preserva en la presentación. La decisión es explícita aunque Aníbal la marque Estorba: perder un lado de una tensión decidida no es una tensión sin decidir. **12** |
| Autonomía de intercambio de turnos | RF-TUR-06, 13, 17, 31, 32, 33, 34 | La autonomía se concede por autorización previa de alcance y periodo, y lo no cubierto espera resolución expresa. Los dos lados marcan Estorba en extremos opuestos —Rodrigo RF-TUR-31 y RF-TUR-17, Carmen RF-TUR-06—, que es la firma de una tensión decidida y no esquivada. **12** |
| Adopción voluntaria | RF-TUR-08, 16, 27, 28 | El sistema es la única fuente editable y la copia imprimible se concede declarando su instante y su condición. Decide exactamente el conflicto enunciado —el Excel y el WhatsApp—, aunque Milagros marque RF-TUR-28 Estorba porque el papel vuelve a la pared. **12** |
| Movilidad frente a control de datos | RF-REG-07, 11, RF-IAM-04, 05, 07, 08 | Se admite el dispositivo personal; antes de identificarse el aviso expone sólo sede, unidad, cama, severidad y motivo, y la identidad verificada habilita contexto y registro sin repetirse. **12** |

## Consistencia — D5

Primer tramo: **60 / 60** — las cinco tensiones decididas, 12 cada una.

Segundo tramo: **0 / 40** — diez hallazgos independientes, resta 10 cada uno, con piso 0.

| # | Hallazgo | Tipo |
|---|---|---|
| 1 | RF-DIA-02, RF-DIA-05, RF-ESC-29, RF-ESC-31 y RF-IAM-02 conservan un bloque «*Cambio:*» que narra cómo se llegó al enunciado vigente y cita la evaluación —«cierra la brecha 1», «el Estorba de Aníbal que hoy cuenta en `X_A`»—. Rompe CONVENCIONES §2 «cero lápidas» y §10 «el documento registra el estado vigente», e invierte la frontera: el requerimiento pasa a hablar de la rúbrica que lo mide | Rastro de historial en el cuerpo |
| 2 | RF-DIA-05 remite a «`## GLOSARIO`», sección que `ReqFunc.MD` no contiene: referencia rota | Referencia portante |
| 3 | RF-ESC-06 aplica «la cadena y el plazo de acuse de esa severidad» mientras RF-ESC-23 compone la cadena sin mirar la severidad. Dos RF dicen cosas distintas sobre el mismo objeto | Contradicción |
| 4 | RF-ESC-08 presenta el estado «indisponible declarado» y RF-ESC-32 sólo lo constituye para el caso sin delegado: la pantalla enumera un valor que ningún RF produce en el otro caso | Contrato apoyado en un estado no constituido |
| 5 | RF-TUR-02 y RF-TUR-03 se apoyan en el vínculo laboral y las reglas de jornada del profesional, y RF-IAM-06 sólo los constituye para el rotante que comunica la Red | Contrato apoyado en un dato no constituido |
| 6 | RF-TUR-16 se apoya en un «periodo cerrado» que ningún RF constituye y que el glosario no define | Contrato apoyado en un concepto no definido |
| 7 | RF-ESC-26 se apoya en una «resolución de la jefatura» sobre delegaciones que ningún RF constituye | Contrato apoyado en un acto no constituido |
| 8 | RF-IAM-01 y RF-IAM-07 presuponen identidad verificada en el equipo compartido, y RF-IAM-08 sólo declara cómo se establece en el dispositivo personal | Contrato apoyado en una capacidad no declarada |
| 9 | RF-DIA-28 CA-2 excluye la guardia localizable de la absorción de camas sin responsable, mientras RF-ESC-01, RF-ESC-08 y RF-ESC-23 presuponen que existe responsable clínico vigente | Contradicción |
| 10 | La enumeración del contenido clínico de una cama se repite en RF-DIA-02, RF-DIA-21, RF-DIA-31 y RF-DIA-32: cuatro copias de la misma lista que hay que corregir por separado hasta contradecirse | Duplicado encubierto |

`D5 = 60 + 0 = 60,0`

El repositorio tiene glosario —`docs/GLOSARIO.md`, 74 términos—, de modo que el techo D5 ≤ 80 no
aplica. No hay RNF alojado dentro de `ReqFunc.MD`.

## Priorización — D6

- RF sin prioridad o con prioridad fuera de MUST/SHOULD/COULD: **0** → resta 0.
- Distribución 63 MUST / 81 SHOULD / 2 COULD: hay gradiente, `prioridad_uniforme` es `false` y el
  techo D6 ≤ 60 no se activa.
- MUST no reservados: **2** → resta 10.

| ID | Por qué su ausencia no deja un problema sin resolver ni una tarea descubierta |
|---|---|
| RF-TUR-44 | La tarea 4 de Carmen conserva su camino completo sin él: RF-TUR-03 presenta candidatos, RF-TUR-20 les dirige la solicitud y RF-TUR-35 los asigna al aceptar. RF-TUR-44 es el atajo del caso urgente, no la cobertura de la tarea, y ninguno de P1, P2 y P3 depende de él. SHOULD |
| RF-DIA-32 | RF-DIA-21 ya presenta al médico, durante su turno y sobre las camas de su asignación, el diagnóstico vigente, las decisiones con su fundamento, el esquema con su día, los pendientes críticos y el estado de la información a la familia. RF-DIA-32 añade el alcance al turno anterior y la declaración de lo no registrado, que es refuerzo y no la única cobertura de la tarea 1 de Rodrigo. SHOULD |

`D6 = 100 − 0 − 10 = 90,0`

## Contrastes cruzados

| Contraste | Resultado |
|---|---|
| Discrepancia percibido/computado | Tres personas por encima de 20 puntos: Rodrigo 34, Milagros 48, Carmen 26. En las tres falla el agente y no el enunciado de sus tareas críticas: las tareas están escritas como acciones observables y se dejaron trazar sin ambigüedad. Prevalece el valor computado |
| Conformidad unánime | No se activa. Las cuatro coberturas percibidas son 78, 80, 82 y 80, ninguna alcanza el 90 %, y además ninguna tensión queda sin decidir. D5 no queda limitada a 40 |
| Necesidad no cubierta sin brecha | Las 21 necesidades que los cuatro agentes declaran aparecen en la tabla de brechas: 5 de Rodrigo, 6 de Milagros, 7 de Carmen y 3 de Aníbal. Ninguna queda silenciada ni refutada |

## Evaluaciones de agente ausentes o inválidas

| Persona | Qué falta |
|---|---|
| — | Ninguna. Las cuatro evaluaciones están presentes, completas y con vocabulario cerrado |

## Cálculo global

```
D1  49,0 × 0,30 = 14,700
D2  66,7 × 0,25 = 16,675
D3  97,9 × 0,20 = 19,580
D4 100,0 × 0,10 = 10,000
D5  60,0 × 0,10 =  6,000
D6  90,0 × 0,05 =  4,500
                  ───────
Global          = 71,455 → 71,5 %
```

| # | Condición de PASSED | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 71,5 % | no |
| 2 | D1 | ≥ 80,0 | 49,0 | no |
| 3 | Persona más baja | ≥ 7,0/10 | 3,2 (Milagros) | no |
| 4 | D2 | ≥ 80,0 | 66,7 | no |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | sí |

**Veredicto: FAILED** — cumple una de las cinco condiciones.

## Brechas encontradas

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| 1 | Milagros · P3 | La decisión de acudir o de no acudir se incorpora al episodio por RF-REG-11 y ningún RF la hace llegar a quien escaló. Corta su escenario clave en el paso 8 | veredicto-milagros | Alta |
| 2 | Milagros · P3 | La suspensión o el cambio de una indicación vigente no la alcanza junto a la cama: RF-ESC-28 sólo declara la indicación nueva. Puede seguir administrando lo suspendido | veredicto-milagros · auditoría | Alta |
| 3 | Milagros · P2 | RF-DIA-28 CA-2 excluye la guardia localizable: una noche cubierta sólo por un localizable deja las camas sin responsable clínico vigente, y RF-ESC-01, RF-ESC-08 y RF-ESC-23 lo presuponen | veredicto-milagros · auditoría | Alta |
| 4 | P2 · Milagros, Carmen, Aníbal | La indisponibilidad declarada no altera la cadena: por RF-ESC-27 el declarado indisponible sigue siendo responsable clínico vigente y por RF-ESC-23 la encabeza, de modo que el escalamiento le quema un plazo entero antes de que RF-ESC-02 avance | auditoría · veredicto-milagros | Alta |
| 5 | Aníbal · P2 | No existe indisponibilidad registrada cuando sí se indica delegado: RF-ESC-32 sólo cubre el caso sin delegado, RF-ESC-08 enumera un estado que nadie constituye para ese caso y RF-ESC-31 devuelve al titular a la cabeza de la cadena sin que pueda responder | veredicto-anibal | Alta |
| 6 | Carmen · P2 | La indisponibilidad declarada sin delegado no devuelve la franja a la vista de descubiertas de RF-TUR-07 ni la habilita para la asignación de RF-TUR-44: sabe que hay un problema por RF-ESC-33 y no tiene camino para resolverlo | veredicto-carmen | Alta |
| 7 | P2 | RF-ESC-09 termina la cadena en la jefatura de la unidad y ningún RF declara qué ocurre si ella tampoco acusa | veredicto-milagros · auditoría | Alta |
| 8 | Aníbal · P2 | RF-ESC-06 aplica la cadena de la severidad registrada y RF-ESC-23 compone la cadena sin mirar la severidad: de esa diferencia depende que una consulta diferible lo despierte | veredicto-anibal · auditoría | Alta |
| 9 | Rodrigo · P1 | La atribución del registro en la PC compartida de la estación no la declara ningún RF: RF-IAM-08 sólo constituye la identidad verificada en el dispositivo personal y RF-IAM-01 y RF-IAM-07 la presuponen en el equipo compartido | veredicto-rodrigo | Alta |
| 10 | Milagros · P2 | No puede registrar ni escalar sobre la cama de su colega sin un relevo declarado previo: RF-IAM-02 y RF-IAM-10 exigen un acto anterior de quien tiene la asignación, y de noche cubren diez camas entre dos | veredicto-milagros | Alta |
| 11 | Milagros · P3 | Nada la alcanza junto a la cama cuando la cama que cuida se queda sin responsable clínico vigente: RF-DIA-36 lo produce y RF-TUR-45 avisa a la jefatura | veredicto-milagros | Alta |
| 12 | Carmen · P1 | El vínculo laboral y las reglas de jornada y descanso del personal de planta no los constituye ningún RF: RF-IAM-06 sólo cubre al rotante, y de ese dato dependen RF-TUR-02 y el filtro de candidatos de RF-TUR-03 | veredicto-carmen | Alta |
| 13 | ReqFunc.MD | Cinco RF conservan un bloque «*Cambio:*» que narra la historia de la iteración y cita la evaluación; RF-DIA-05 remite además a una sección `## GLOSARIO` inexistente en el documento | auditoría | Alta |
| 14 | Rodrigo · P1 | Ningún RF arma la vista de la unidad completa priorizada al inicio del turno: RF-DIA-02 entrega cama por cama y RF-DIA-22 sólo las marcadas. Su criterio de las diez camas en quince minutos no se sostiene | veredicto-rodrigo | Media |
| 15 | Rodrigo · P1 | El fundamento de la decisión clínica no es exigible: RF-DIA-01 exige sólo el diagnóstico y RF-DIA-34 señala sin condicionar el cierre, de modo que una cama puede entregarse con el porqué vacío | veredicto-rodrigo | Media |
| 16 | Rodrigo | Ningún RF avisa cuando otro profesional retira una marca de inestabilidad o de pendiente crítico: puede pasar por una cama creyéndola marcada | veredicto-rodrigo | Media |
| 17 | Rodrigo | No existe diferencial de unidad desde su último turno en ella: RF-DIA-05 lo computa por cama y él llega a diez camas después de tres semanas | veredicto-rodrigo | Baja |
| 18 | Milagros | La entrega de enfermería no comprende los escalamientos abiertos ni las indicaciones vigentes: RF-DIA-08 y RF-DIA-11 enumeran «exactamente» otros cinco componentes | veredicto-milagros | Media |
| 19 | Carmen · P1 | Ningún RF avisa a la jefatura cuando un médico desplaza a otro de una cama: RF-DIA-29 lo permite y RF-DIA-35 avisa sólo al desplazado | veredicto-carmen | Media |
| 20 | Carmen · P1 | La aceptación de una solicitud de cobertura cuya asignación sí produciría un cruce no tiene respuesta declarada: RF-TUR-35 sólo cubre el caso sin cruce y nada dice que ella se entere de que la franja sigue descubierta | veredicto-carmen | Media |
| 21 | Carmen · P1 | El «periodo cerrado» que RF-TUR-16 presupone no lo constituye ningún RF ni lo define el glosario | veredicto-carmen · auditoría | Media |
| 22 | Carmen · P2 | La «resolución de la jefatura» sobre una delegación que RF-ESC-26 presupone no la constituye ningún RF | veredicto-carmen · auditoría | Media |
| 23 | Carmen · P1 | Dos guardias localizables simultáneas en sedes distintas no constituyen cruce y RF-TUR-01 no las rechaza, siendo la doble asignación entre sedes por la que ella responde | veredicto-carmen | Media |
| 24 | Aníbal · P2 | La selectividad del escalamiento se resuelve sólo en la presentación: RF-ESC-25 iguala el plazo hacia arriba y su restricción documentada dice que si todo llega como crítico deja de responder a todo | veredicto-anibal | Media |
| 25 | Aníbal · P2 | La constitución y la vigencia de sus medios de contacto no las declara ningún RF: RF-TUR-05 y RF-TUR-26 los invocan y es por donde hoy se pierde la llamada que sí importaba | veredicto-anibal | Media |
| 26 | Aníbal · P2 | RF-DIA-05 computa el diferencial desde la apertura del episodio cuando no hay registro previo suyo: tres semanas de cambios a las 03:20 con señal débil no son un resumen | veredicto-anibal | Media |
| 27 | ReqFunc.MD · D3 | RF-TUR-16 y RF-TUR-28 nombran el medio de salida —«copia imprimible», «archivo histórico»— en lugar de la garantía | auditoría | Media |
| 28 | ReqFunc.MD · D3 | RF-ESC-09 CA-2 amplía el contrato: el enunciado alcanza a la jefatura y el criterio entrega al delegado de esa jefatura | auditoría | Media |
| 29 | ReqFunc.MD · D5 | La enumeración del contenido clínico de una cama se repite en RF-DIA-02, RF-DIA-21, RF-DIA-31 y RF-DIA-32, y la segunda declaración sobre la misma cama se resuelve en RF-DIA-29 para la asignación médica y no en RF-DIA-19 para la de cuidado de enfermería | auditoría · veredicto-milagros | Media |
| 30 | ReqFunc.MD · D6 | Dos MUST no reservados: RF-TUR-44 y RF-DIA-32 | auditoría | Baja |
