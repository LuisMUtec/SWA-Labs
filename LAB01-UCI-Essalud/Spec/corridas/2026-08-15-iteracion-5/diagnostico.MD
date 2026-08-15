# Diagnóstico — corrida 2026-08-15-iteracion-5

Evidencia de la agregación. Insumos: los cuatro veredictos de este mismo directorio,
`Requirements/ReqFunc.MD` @ `be8c4ed`, `Personas/*` @ `6340172`, `Agents/*` @ `34877c7` y la rúbrica
`Spec/Eval-Spec.MD` @ `b492237`.

Vocabulario de veredicto: **S** Sirve · **I** Indiferente · **E** Estorba · **A** Ambiguo.
La columna «Efecto en D1» cita la tarea crítica que el RF traza según la matriz de trazabilidad de
`ReqFunc.MD` —`R1`…`R6` Rodrigo, `M1`…`M6` Milagros, `C1`…`C6` Carmen, `A1`…`A6` Aníbal— y anota
`X_p` cuando un veredicto **Estorba** cae fuera de las seis tareas de esa persona y por tanto resta
2 puntos.

## Veredictos agregados

| RF | Rodrigo | Milagros | Carmen | Aníbal | Efecto en D1 |
|---|---|---|---|---|---|
| RF-TUR-01 | S | I | S | A | C2 |
| RF-TUR-02 | A | I | S | I | C2 |
| RF-TUR-03 | I | I | S | I | C4 |
| RF-TUR-04 | S | S | S | S | C1 |
| RF-TUR-05 | S | I | S | S | C4 |
| RF-TUR-06 | S | I | E | I | C3 — Estorba dentro de la tarea, no cuenta en X_C |
| RF-TUR-07 | I | I | S | I | C2 |
| RF-TUR-08 | S | S | S | S | — no traza a ninguna tarea crítica |
| RF-TUR-09 | I | I | A | I | C1 (Ambiguo de Carmen) |
| RF-TUR-10 | I | I | S | I | C1 |
| RF-TUR-11 | I | I | S | I | C1 |
| RF-TUR-12 | I | I | S | I | C3 |
| RF-TUR-13 | S | I | S | I | C3 |
| RF-TUR-14 | I | I | S | I | — |
| RF-TUR-15 | I | I | S | I | — |
| RF-TUR-16 | I | I | I | I | — |
| RF-TUR-17 | E | I | S | I | C3 — **X_R** (fuera de las tareas de Rodrigo) |
| RF-TUR-18 | I | I | S | I | C4 |
| RF-TUR-19 | I | I | S | I | C4 |
| RF-TUR-20 | S | I | S | I | C4 |
| RF-TUR-21 | I | I | S | I | C3 |
| RF-TUR-22 | I | I | S | I | C3 |
| RF-TUR-23 | I | I | S | I | — |
| RF-TUR-24 | I | I | S | I | — |
| RF-TUR-25 | I | I | S | I | C4 |
| RF-TUR-26 | S | I | S | S | C4 |
| RF-TUR-27 | S | S | S | S | C1 |
| RF-TUR-28 | I | E | S | I | C1 — **X_M** |
| RF-TUR-29 | I | I | S | I | C3 |
| RF-TUR-30 | I | I | S | I | C3 |
| RF-TUR-31 | E | I | S | I | C3 — **X_R** |
| RF-TUR-32 | S | I | S | I | C3 |
| RF-TUR-33 | S | I | S | I | C3 |
| RF-TUR-34 | I | I | S | I | C3 |
| RF-TUR-35 | S | I | S | I | C4 |
| RF-TUR-36 | I | I | S | I | C4 |
| RF-TUR-37 | I | I | S | I | C4 |
| RF-TUR-38 | I | I | S | I | C4 |
| RF-TUR-39 | I | I | S | I | C4 |
| RF-TUR-40 | I | I | S | I | C4 |
| RF-TUR-41 | I | I | S | I | C4 |
| RF-TUR-42 | S | S | S | S | R6, C2 |
| RF-TUR-43 | S | I | I | I | C4 |
| RF-DIA-01 | S | I | S | S | R6 |
| RF-DIA-02 | S | I | I | I | R1, R2 |
| RF-DIA-03 | S | I | I | I | R1 |
| RF-DIA-04 | S | I | S | I | R6 |
| RF-DIA-05 | A | I | I | S | R2 (Ambiguo de Rodrigo) |
| RF-DIA-06 | S | S | I | I | R4 |
| RF-DIA-07 | S | I | S | S | R2, R3 |
| RF-DIA-08 | I | S | I | I | M6 |
| RF-DIA-09 | S | I | S | I | R1 |
| RF-DIA-10 | S | I | S | I | R1, R2 |
| RF-DIA-11 | I | S | I | I | M6 |
| RF-DIA-12 | S | I | A | I | R6, C5 (Ambiguo de Carmen) |
| RF-DIA-13 | S | I | I | S | R2, R3 |
| RF-DIA-14 | S | I | I | S | R2, R3 |
| RF-DIA-15 | S | I | I | I | R2, R3 |
| RF-DIA-16 | S | I | I | I | R3 |
| RF-DIA-17 | S | I | I | I | R1 |
| RF-DIA-18 | S | S | S | I | R1 |
| RF-DIA-19 | I | S | S | I | M6 |
| RF-DIA-20 | S | I | S | I | R6 |
| RF-DIA-21 | S | I | I | I | R2 |
| RF-DIA-22 | S | S | I | I | R4 |
| RF-DIA-23 | S | S | I | S | R2 |
| RF-DIA-24 | E | I | S | I | R6, C5 — Estorba dentro de R6, no cuenta en X_R |
| RF-DIA-25 | I | S | I | I | M6 |
| RF-DIA-26 | I | S | I | I | M6 |
| RF-DIA-27 | I | S | S | I | M6 |
| RF-DIA-28 | S | S | S | A | R1 (Ambiguo de Aníbal, fuera de sus tareas) |
| RF-DIA-29 | S | S | A | S | R1, M2 (Ambiguo de Carmen) |
| RF-DIA-30 | I | S | S | I | M6 |
| RF-DIA-31 | S | I | S | I | R6 |
| RF-ESC-01 | S | S | I | S | M2 |
| RF-ESC-02 | S | S | I | S | — |
| RF-ESC-03 | S | S | I | S | A1 |
| RF-ESC-04 | S | S | I | S | A2 |
| RF-ESC-05 | I | S | I | I | — |
| RF-ESC-06 | S | S | I | S | M2 |
| RF-ESC-07 | S | S | S | S | A5 |
| RF-ESC-08 | S | S | S | S | M3 |
| RF-ESC-09 | I | S | S | S | — |
| RF-ESC-10 | S | I | I | S | — |
| RF-ESC-11 | S | S | I | S | M2 |
| RF-ESC-12 | S | S | I | S | A2 |
| RF-ESC-13 | S | A | I | A | M4 (Ambiguo de Milagros y de Aníbal) |
| RF-ESC-14 | I | S | I | S | A2 |
| RF-ESC-15 | I | S | I | S | M2 |
| RF-ESC-16 | S | E | I | S | A1 — **X_M** |
| RF-ESC-17 | S | S | I | S | A5 |
| RF-ESC-18 | I | S | I | S | — |
| RF-ESC-19 | S | I | I | S | A2 |
| RF-ESC-20 | I | S | I | S | M2 |
| RF-ESC-21 | S | S | I | S | M2 |
| RF-ESC-22 | I | S | I | S | M2 |
| RF-ESC-23 | S | S | S | S | M2 |
| RF-ESC-24 | S | I | I | S | A1 |
| RF-ESC-25 | S | S | I | E | M2 — **X_A** |
| RF-ESC-26 | I | I | S | I | C2 |
| RF-ESC-27 | S | S | S | S | M2, M3 |
| RF-ESC-28 | I | S | I | S | M4 |
| RF-ESC-29 | S | S | I | E | R5 — **X_A** |
| RF-ESC-30 | S | S | S | E | A5, C2 — Estorba dentro de A5, no cuenta en X_A |
| RF-ESC-31 | I | I | S | E | C2 — **X_A** |
| RF-REG-01 | I | S | I | S | M1 |
| RF-REG-02 | I | S | I | S | M1 |
| RF-REG-03 | S | S | I | S | M4 |
| RF-REG-04 | I | S | I | S | M4 |
| RF-REG-05 | I | S | I | S | M5 |
| RF-REG-06 | S | I | I | S | R5 |
| RF-REG-07 | S | S | I | S | A4 |
| RF-REG-08 | S | I | I | S | A3 |
| RF-REG-09 | S | S | I | S | A4 |
| RF-REG-10 | S | I | I | I | R5 |
| RF-IAM-01 | S | S | S | S | R3 |
| RF-IAM-02 | E | E | S | S | A4 — **X_R**, **X_M** |
| RF-IAM-03 | I | I | S | I | — |
| RF-IAM-04 | S | I | I | S | A1 |
| RF-IAM-05 | S | I | I | S | A1, A4 |
| RF-IAM-06 | A | I | S | I | — (Ambiguo de Rodrigo, fuera de sus tareas) |
| RF-IAM-07 | S | I | I | S | A1, A4 |
| RF-IAM-08 | S | S | I | S | A1, A4 |
| RF-IAM-09 | S | S | I | S | R3, A4 |
| RF-SUP-01 | A | I | S | I | C5 (Ambiguo de Rodrigo, fuera de sus tareas) |
| RF-SUP-02 | I | I | S | I | C6 |
| RF-SUP-03 | I | A | I | A | A6 (Ambiguo de Milagros y de Aníbal) |
| RF-SUP-04 | I | I | I | I | — |
| RF-SUP-05 | I | I | S | I | C6 |

Recuento por persona, coincidente con las precondiciones verificadas:

| Persona | Sirve | Indiferente | Estorba | Ambiguo | Total |
|---|---:|---:|---:|---:|---:|
| Rodrigo | 69 | 52 | 4 | 4 | 129 |
| Milagros | 51 | 73 | 3 | 2 | 129 |
| Carmen | 67 | 58 | 1 | 3 | 129 |
| Aníbal | 53 | 68 | 4 | 4 | 129 |

Catorce RF no figuran en ninguna fila de tareas críticas de la matriz de trazabilidad —RF-TUR-08,
RF-TUR-14, RF-TUR-15, RF-TUR-16, RF-TUR-23, RF-TUR-24, RF-ESC-02, RF-ESC-05, RF-ESC-09, RF-ESC-10,
RF-ESC-18, RF-IAM-03, RF-IAM-06 y RF-SUP-04—. No son huérfanos: todos declaran persona y problema
existentes, y sirven criterios de éxito o restricciones normativas. Se anota porque explica por qué
un RF con veredicto Sirve puede no sumar en D1.

## Daño fuera de tarea — `X_p`

| Persona | RF marcados Estorba | Cuentan en `X_p` | No cuentan | `X_p` |
|---|---|---|---|---:|
| Rodrigo | RF-TUR-17, RF-TUR-31, RF-DIA-24, RF-IAM-02 | RF-TUR-17, RF-TUR-31 y RF-IAM-02: ninguno figura en las seis filas de Rodrigo de la matriz de trazabilidad | RF-DIA-24 traza a su tarea 6 «Cerrar y firmar la entrega de turno» | 3 |
| Milagros | RF-TUR-28, RF-ESC-16, RF-IAM-02 | los tres: ninguno figura en sus seis filas | — | 3 |
| Carmen | RF-TUR-06 | — | RF-TUR-06 traza a su tarea 3 «Aprobar o rechazar intercambios y permisos» | 0 |
| Aníbal | RF-ESC-25, RF-ESC-29, RF-ESC-30, RF-ESC-31 | RF-ESC-25 (traza a M2), RF-ESC-29 (traza a R5) y RF-ESC-31 (traza a C2): ninguno figura en sus seis filas | RF-ESC-30 traza a su tarea 5 «Marcarse temporalmente indisponible y delegar» | 3 |

RF-IAM-02 merece nota. Rodrigo y Milagros describen su daño dentro de su tarea de registro, pero la
matriz de trazabilidad de `ReqFunc.MD` no lo lista en ninguna de sus filas: solo lo traza a la tarea 4
de Aníbal. Ante la duda se penaliza y se cuenta como daño fuera de tarea para ambos.

## Matriz de cobertura

| Persona | Tarea crítica | RF que la cubre | Veredicto | Puntos | Estado |
|---|---|---|---|---:|---|
| Rodrigo | Recibir el handoff estructurado de todas las camas asignadas | RF-DIA-02, 03, 09, 10, 17, 18, 28, 29 | ocho Sirve | 3 | Incompleta — el contenido declarado en RF-DIA-02 no es exigible: ningún RF obliga a registrar la decisión y su fundamento, y RF-DIA-01 condiciona el cierre solo al diagnóstico. Su criterio «el handoff incluye decisiones y su justificación» queda a merced del turno saliente |
| Rodrigo | Consultar la evolución y el diagnóstico del turno anterior | RF-DIA-02, 05, 07, 10, 13, 14, 15, 21, 23 | ocho Sirve, RF-DIA-05 Ambiguo | 3 | Incompleta — el estado completo de la cama se obtiene, pero el criterio «ver qué cambió desde su último contacto» cuelga entero de RF-DIA-05, que el agente marcó Ambiguo |
| Rodrigo | Registrar nota de evolución y diagnóstico por paciente | RF-DIA-07, 13, 14, 15, 16, RF-IAM-01, RF-IAM-09 | siete Sirve | 3 | Incompleta — RF-IAM-02 (Estorba) le rechaza el registro sobre una cama ajena sin escalamiento de por medio, que es su necesidad no cubierta declarada, y ahí vuelve al papel |
| Rodrigo | Marcar pacientes inestables o con pendientes críticos | RF-DIA-06, RF-DIA-22 | dos Sirve | 5 | Cubierta — marca vigente que sobrevive al cambio de turno y consulta de las camas marcadas de la unidad; el agente la declara la mejor resuelta y ningún RF implicado se contradice |
| Rodrigo | Consultar resultados de laboratorio e imágenes | RF-REG-06, RF-REG-10, RF-ESC-29 | tres Sirve | 3 | Incompleta — todo se declara «del episodio»: los resultados anteriores al episodio o producidos en otra sede de la Red no llegan, y esa es la frustración que la tarea existe para resolver |
| Rodrigo | Cerrar y firmar la entrega de turno | RF-DIA-01, 04, 12, 20, 31, RF-TUR-42 (Sirve) y RF-DIA-24 (Estorba) | seis Sirve, uno Estorba | 3 | Incompleta — firma, bloqueo y composición sin transcripción están, pero RF-DIA-24 convierte en advertencia a la jefatura la noche en que no alcanza a cerrar, y el agente lo rechaza expresamente |
| Milagros | Registrar signos vitales y balance por paciente | RF-REG-01, RF-REG-02 | dos Sirve | 5 | Cubierta — registro junto a la cama con autoría e instante, preservado sin pérdida ni duplicación durante la desconexión, y reutilizado en su entrega por RF-DIA-08 |
| Milagros | Escalar un deterioro clínico al médico responsable | RF-ESC-01, 06, 11, 15, 20, 21, 22, 23, 25, 27, RF-DIA-29 | once Sirve | 5 | Cubierta — emite junto a la cama, sin clasificar, con contexto adjunto, cadena compuesta y avance automático; el umbral de 30 s pertenece a `ReqNoFunc.MD` y no se reclama aquí |
| Milagros | Consultar quién está de guardia y su estado de disponibilidad | RF-ESC-08, RF-ESC-27 | dos Sirve | 3 | Incompleta — «disponible» es el estado residual de RF-ESC-08: el médico ocupado que nadie registró le figura disponible, que es exactamente el Dr. Paredes de su escenario |
| Milagros | Ver y confirmar indicaciones médicas vigentes | RF-REG-03, RF-REG-04, RF-ESC-28 (Sirve) y RF-ESC-13 (Ambiguo) | tres Sirve, uno Ambiguo | 3 | Incompleta — la indicación nueva la alcanza junto a la cama, pero el resto de los cambios se reúne en RF-ESC-13, que no declara si la alcanza o si debe ir a consultarla a la estación |
| Milagros | Registrar eventos y administración de medicamentos | RF-REG-05 | Sirve | 3 | Incompleta — RF-IAM-02 le rechaza el registro sobre la cama de la colega que cubre, y un registro rechazado a las 03:00 termina en el papel que la tarea existe para eliminar |
| Milagros | Recibir y entregar el turno de enfermería | RF-DIA-08, 11, 19, 25, 26, 27, 30 | siete Sirve | 3 | Incompleta — enfermería no tiene equivalente de RF-DIA-17: nada declara qué recibe cuando la saliente concluyó sin entrega cerrada |
| Carmen | Elaborar y publicar la programación mensual de turnos | RF-TUR-04, 10, 11, 27, 28 (Sirve) y RF-TUR-09 (Ambiguo) | cinco Sirve, uno Ambiguo | 3 | Incompleta — RF-TUR-09 presupone «las franjas de cobertura requeridas» y ningún enunciado declara su origen ni le permite definirlas: el mes empieza en un dato que el documento no constituye |
| Carmen | Validar que no existan cruces ni franjas descubiertas | RF-TUR-01, 02, 07, 42, RF-ESC-26, 30, 31 | siete Sirve | 3 | Incompleta — el rechazo del cruce y la vista de siete días cumplen sus dos criterios duros, pero todo depende de que ella consulte: cuando un permiso, una ausencia o un retiro de rotante descubren una franja, ningún RF la avisa |
| Carmen | Aprobar o rechazar intercambios y permisos | RF-TUR-12, 13, 17, 21, 22, 29, 30, 31, 32, 33, 34 (Sirve) y RF-TUR-06 (Estorba) | once Sirve, uno Estorba | 3 | Incompleta — el permiso está resuelto de punta a punta; el intercambio amparado se consuma sobre su programación vigente sin su resolución y RF-TUR-34 solo se lo cuenta después |
| Carmen | Reasignar cobertura ante una ausencia imprevista | RF-TUR-03, 05, 18, 19, 20, 25, 26, 35, 36, 37, 38, 39, 40, 41 (Sirve) y RF-TUR-43 (Indiferente) | catorce Sirve | 3 | Incompleta — la cadena entera termina en que el candidato acepte; ningún RF le permite asignar directamente sobre la programación vigente cuando nadie acepta y la guardia empieza en horas |
| Carmen | Monitorear cumplimiento y completitud de entregas de turno | RF-DIA-24, RF-SUP-01 (Sirve) y RF-DIA-12 (Ambiguo) | dos Sirve, uno Ambiguo | 3 | Incompleta — obtiene el turno concluido sin entrega y el detalle del periodo, pero RF-DIA-12 no declara a quién presenta las camas sin diagnóstico |
| Carmen | Generar indicadores de cobertura para la Dirección de Red | RF-SUP-02, RF-SUP-05 | dos Sirve | 3 | Incompleta — cobertura y cumplimiento salen sin transcripción; la trazabilidad de la documentación clínica, tercer indicador que la Red le exige, hay que armarla entre RF-SUP-01 y RF-IAM-03, y ningún RF declara que ella pueda consultar ese registro |
| Aníbal | Recibir la alerta de escalamiento con contexto clínico adjunto | RF-ESC-03, 16, 24, RF-IAM-04, 05, 07, 08 | siete Sirve | 3 | Incompleta — el paquete de contexto es exactamente el que hoy consigue en once minutos, pero su restricción de selectividad no queda servida: RF-ESC-25 le entrega toda duda con el plazo del deterioro inmediato y RF-ESC-24 lo distingue recién en el aviso |
| Aníbal | Confirmar recepción y tomar el caso | RF-ESC-04, 12, 14, 19 | cuatro Sirve | 5 | Cubierta — acuse y toma con autoría e instante, devueltos a quien escaló junto a la cama; el «un toque» que falta es esfuerzo de interacción y pertenece a `ReqNoFunc.MD` |
| Aníbal | Consultar tendencia de signos, ventilación y última evolución | RF-REG-08 (más RF-REG-01, 02, 03, 06, RF-DIA-05, 23) | Sirve | 5 | Cubierta — seis horas con la extensión efectiva declarada, los cinco parámetros del ventilador y la última evolución, más lo que cambió desde su último contacto |
| Aníbal | Registrar la indicación dada de forma remota | RF-REG-07, 09, RF-IAM-02, 05, 07, 08, 09 | siete Sirve | 3 | Incompleta — la indicación queda con hora, autoría y sin PC, incluso sobre cama ajena por toma del caso; no está declarado que pueda registrar a distancia la decisión clínica fundamentada, incluida la de no acudir |
| Aníbal | Marcarse temporalmente indisponible y delegar | RF-ESC-07, 17 (Sirve) y RF-ESC-30 (Estorba) | dos Sirve, uno Estorba | 3 | Incompleta — RF-ESC-07 no admite declararse indisponible sin delegado, RF-ESC-30 puede dejarlo sin delegado admisible y RF-ESC-31 permite que la jefatura termine su delegación sin que ningún RF declare que se le avisa |
| Aníbal | Revisar en la mañana lo ocurrido durante la noche | RF-SUP-03 | Ambiguo | 1 | Aparente — es el único RF que la traza y quedó Ambiguo; con el glosario, el «ámbito de responsabilidad» de un médico de guardia localizable sin asignación médica, delegación ni jefatura resulta vacío |

Σ tareas: Rodrigo 20 · Milagros 22 · Carmen 18 · Aníbal 20. Tareas en 0: ninguna, en ninguna persona.

## Recorrido del escenario clave y claridad del flujo

| Persona | Paso decisivo | Fundamento | Flujo |
|---|---|---|---:|
| Rodrigo | Paso 5 — el saliente iba con retraso y no cerró la entrega | RF-DIA-17 declara la ausencia y RF-DIA-24 advierte a la jefatura; ninguno devuelve el contexto de la cama 6, y ningún otro RF declara vía para obtenerlo sin llamar al médico que ya se fue. El escenario de la persona es exactamente ese: «Nada de eso está en la nota». Hay un paso que ningún RF sostiene | **0** |
| Milagros | Pasos 13 y 15 — el ajuste de soporte posterior a la toma del caso, y la revisión de su propio escalamiento | Se apoyan en RF-ESC-13 y RF-SUP-03, ambos Ambiguo. La madrugada entera —desaturación, escalamiento, cadena, acuse, toma, indicación, ejecución— se sostiene en RF marcados Sirve y no se interrumpe | **2** |
| Carmen | Paso 9 — la solicitud vence o la lista se agota sin que nadie acepte | RF-TUR-11 asigna solo dentro de una propuesta y RF-TUR-35 exige la aceptación del candidato. El escenario obliga a cubrir una guardia que empieza en 27 horas; agotada la lista, ningún RF sostiene el paso siguiente y la coordinadora vuelve al teléfono. Hay un paso que ningún RF sostiene | **0** |
| Aníbal | Paso 15 — la revisión matutina de las dos sedes | Se apoya únicamente en RF-SUP-03, Ambiguo. Los pasos 1 a 14 —emisión, cadena, aviso sin identificación, verificación en el celular, contexto, acuse, toma, indicación a distancia, confirmación y cierre— se sostienen en RF Sirve. El paso 3 avanza apoyado en RF-ESC-25 (Estorba), pero avanza | **2** |

Los dos ceros se declaran con fundamento y no por eco del agente. En ambos casos el corte no está en
una rama exótica: en Rodrigo es el estado que su propia persona describe —el saliente que entrega en
ocho minutos en el pasillo—, y en Carmen es la rama que `RF-TUR-39` declara expresamente y que su
escenario, con la guardia a 27 horas, vuelve inmediata.

## Aritmética de D1

```
Puntaje_p = máx(0, Σ tareas_p − 2 × X_p) / 5 + Flujo_p

Rodrigo   Σ tareas = 3 + 3 + 3 + 5 + 3 + 3 = 20   X = 3   Flujo = 0
          máx(0, 20 − 2×3) = 14 ;  14 / 5 = 2,8 ;  2,8 + 0 = 2,8

Milagros  Σ tareas = 5 + 5 + 3 + 3 + 3 + 3 = 22   X = 3   Flujo = 2
          máx(0, 22 − 2×3) = 16 ;  16 / 5 = 3,2 ;  3,2 + 2 = 5,2

Carmen    Σ tareas = 3 + 3 + 3 + 3 + 3 + 3 = 18   X = 0   Flujo = 0
          máx(0, 18 − 2×0) = 18 ;  18 / 5 = 3,6 ;  3,6 + 0 = 3,6

Aníbal    Σ tareas = 3 + 5 + 5 + 3 + 3 + 1 = 20   X = 3   Flujo = 2
          máx(0, 20 − 2×3) = 14 ;  14 / 5 = 2,8 ;  2,8 + 2 = 4,8

promedio  = (2,8 + 5,2 + 3,6 + 4,8) / 4 = 16,4 / 4 = 4,1
D1        = 4,1 × 10 = 41,0
```

Ninguna persona tiene sus seis tareas en 0, de modo que el techo de 50 sobre D1 no se activa.

## Cobertura de P1, P2 y P3

| Problema | RF asociados | Comportamiento que lo resuelve | Puntos |
|---|---|---|---:|
| P1 — Rotación de doctor | RF-DIA-01, 02, 03, 04, 07, 09, 10, 12, 17, 20, 24, 31, RF-SUP-01 | El cierre de la entrega queda impedido si falta el diagnóstico de alguna cama asignada (RF-DIA-01), la entrega se compone sin transcripción (RF-DIA-31), se presenta al entrante sin depender del saliente (RF-DIA-10) y las camas sin diagnóstico se señalan antes de aceptar (RF-DIA-03). **Queda un tramo sin RF que lo cubra**: un turno puede concluir sin cerrar su entrega —RF-DIA-01 impide el cierre, no la conclusión—, y entonces RF-DIA-17 solo declara la ausencia y RF-DIA-24 solo advierte a la jefatura. El diagnóstico del médico previo no está garantizado antes del cambio de turno, que es el enunciado literal de P1 | **50** |
| P2 — Medianoche | RF-ESC-01, 02, 03, 06, 07, 08, 09, 11, 12, 15, 17, 20, 21, 23, 25, 27, 30, 31, RF-IAM-04, 05, 07, 08, RF-REG-07, 08, 09 | Contacto: el escalamiento alcanza al responsable clínico vigente y no al del rol publicado (RF-ESC-01, 27), con la cadena compuesta desde la programación vigente (RF-ESC-23), emitido junto a la cama (RF-ESC-20) y preservado sin conexión (RF-ESC-21), con el contexto ya armado (RF-ESC-03). Indisponibilidad: la cadena avanza sola por falta de acuse (RF-ESC-02), la delegación se activa y se restituye (RF-ESC-07, 17) y la cadena agotada termina en la jefatura (RF-ESC-09). Ningún tramo queda sin RF: los defectos que los agentes señalan —delegado inadmisible, revocación sin aviso— son refinamientos dentro de un camino resuelto, y se registran como brechas | **100** |
| P3 — Actualizaciones en tiempo real | RF-ESC-08, 13, 16, 22, 28, 29, RF-REG-01, 02, 03, 04, 05 | El alcance sin consulta previa está declarado para exactamente dos hechos —la indicación nueva (RF-ESC-28) y el resultado crítico (RF-ESC-29)— y para el cambio de estado del escalamiento hacia quien lo emitió (RF-ESC-22); el registro a pie de cama se preserva durante la desconexión (RF-REG-02). **Queda un tramo sin RF que lo cubra**: los demás cambios de una cama se reúnen en la actualización informativa de RF-ESC-13, que dice «dirigida a» y no declara si alcanza o si debe consultarse —dos agentes independientes lo marcaron Ambiguo por esa razón—, y RF-ESC-29 no alcanza al médico con toma del caso vigente. El «aviso a múltiples médicos y enfermeras» queda indeterminado justo fuera de los dos hechos privilegiados | **50** |

```
D2 = (50 + 100 + 50) / 3 = 200 / 3 = 66,7
```

Ningún problema queda en 0, de modo que el techo de 60 sobre D2 no se activa.

## Verificabilidad y forma (D3)

Se inventariaron los 129 RF contra las ocho condiciones. Los controles M1, M2, M3 y E2 devuelven
vacío: ningún enunciado carece del auxiliar DEBE, ninguno tiene por sujeto a una persona, ninguno
nombra mecanismo o producto y ninguno omite prioridad, persona, problema o criterios. Los plazos que
los enunciados invocan —«dentro del plazo definido para la severidad»— se declaran remitidos a
`ReqNoFunc.MD` y, conforme al alcance de la rúbrica, no se puntúan aquí.

Dos RF resultan no conformes, ambos por la condición 8:

```
D3 = 127 / 129 × 100 = 98,4
```

### Requerimientos mal formados

| ID | Condición de D3 incumplida | Corrección propuesta |
|---|---|---|
| RF-DIA-12 | 8 — el criterio amplía el contrato del enunciado. El enunciado ordena «presentar exactamente las camas … que carecen de diagnóstico» sin declarar destinatario, y su CA-1 lo fija en el médico saliente. El disparador es impersonal («se bloquea un intento de cierre»), de modo que el destinatario no se deduce: lo agrega el criterio | Declarar el destinatario en el enunciado —al médico saliente y a la jefatura de la unidad, si ambos lo requieren— y dejar que el criterio lo demuestre en lugar de constituirlo |
| RF-DIA-29 | 8 — el criterio amplía el contrato del enunciado. El enunciado es ubicuo y solo ordena «mantener una sola asignación médica vigente»; su CA-1 decide cuál de las dos sobrevive —la del segundo declarante— y esa regla no está en el enunciado. La ambigüedad la reportó el agente de Carmen antes que la auditoría | Enunciar la regla de resolución en el propio enunciado —rechazar la segunda declaración, o desplazar la primera avisando al desplazado— y conservar el criterio como demostración |

### Requerimientos mal ubicados

| ID | Por qué no es funcional | Documento que le corresponde |
|---|---|---|
| — | Ningún RF del documento se limita a enunciar un umbral sin comportamiento. Los cuatro RNF que las matrices de cierre citan —`RNF-USA-01`, `RNF-USA-02`, `RNF-SEG-03`, `RNF-DIS-01/02`— se citan como referencia cruzada y viven en su documento | — |

### Requerimientos huérfanos

| ID | Por qué no traza a nadie |
|---|---|
| — | Los 129 RF declaran persona y problema, y las cuatro personas y los tres problemas existen |

## Trazabilidad (D4)

```
Tramo de 70 — RF con persona y problema existentes: 129 / 129 → 70 × 1,000 = 70,0
Tramo de 30 — tareas críticas con al menos 1 punto en D1: 24 / 24 → 30 × 1,000 = 30,0
Matrices internas desfasadas respecto del cuerpo: 0 filas → 0 descuentos

D4 = 70,0 + 30,0 − 0 = 100,0
```

Se cotejaron fila por fila las siete matrices internas: trazabilidad (24 filas), cobertura de
criterios de éxito (23), cobertura de problemas críticos (3), cobertura de las preguntas del
enunciado (6), requerimientos de origen normativo (4), decisión de tensiones (5) y distribución de
prioridad (3). Las tres filas de problemas críticos coinciden RF por RF con el campo `Problema` del
cuerpo —83 en P1, 42 en P2 y 11 en P3—, y la distribución de prioridad coincide con el conteo del
cuerpo: 63 MUST, 64 SHOULD y 2 COULD sobre 129. Las 24 filas de trazabilidad citan tareas con el
texto literal de `Personas/*.MD` y RF cuyo campo `Persona` comprende a la persona de la fila.

## Consistencia y tensiones decididas (D5)

### Tensiones sin decidir

| Tensión | Por qué ningún RF la resuelve |
|---|---|
| — | Ninguna. Las cinco de `Personas/README.md` se deciden en un RF, y en cuatro de ellas la decisión cuesta un veredicto Estorba a la persona que perdió el punto en disputa, que es la señal de que se decidió en lugar de esquivarse |

| Tensión | RF que la decide | Puntos |
|---|---|---:|
| Velocidad frente a completitud del registro | RF-DIA-01 y RF-DIA-20 exigen del cierre exactamente el diagnóstico de cada cama y ningún otro dato; RF-DIA-31 compone el resto sin transcripción; RF-DIA-24 traslada a la jefatura el turno que concluye sin cerrar. Rodrigo marca RF-DIA-24 Estorba: ese es el costo que la decisión le cobra | 12 |
| Sensibilidad del escalamiento | RF-ESC-11 y RF-ESC-25 deciden en favor de Milagros —escala sin clasificar y la duda recibe cadena y plazo del deterioro inmediato— y la selectividad se preserva en la presentación (RF-ESC-16, RF-ESC-24). Aníbal marca RF-ESC-25 Estorba y Milagros marca RF-ESC-16 Estorba: la decisión duele en ambos extremos | 12 |
| Autonomía de intercambio de turnos | RF-TUR-13 y RF-TUR-06 admiten la autorización reutilizable; RF-TUR-31 y RF-TUR-32 dejan el intercambio no amparado pendiente de resolución. Rodrigo marca RF-TUR-17 y RF-TUR-31 Estorba, Carmen marca RF-TUR-06 Estorba | 12 |
| Adopción voluntaria | RF-TUR-08 fija la programación vigente como única fuente editable y RF-TUR-28 y RF-TUR-16 conceden la copia impresa declarándola reflejo no editable y archivo no operativo. Milagros marca RF-TUR-28 Estorba | 12 |
| Movilidad frente a control de datos | RF-IAM-04, 05, 07 y 08 y RF-REG-07 admiten el dispositivo personal, limitan lo visible antes de la identificación y recuperan la identidad verificada en el propio celular | 12 |

### Contradicciones, duplicados encubiertos y vocabulario

Seis hallazgos independientes, con lo que el tramo de 40 queda en su piso.

| # | Hallazgo | Evidencia |
|---|---|---|
| 1 | **Contradicción RF-DIA-18 ↔ RF-DIA-28.** RF-DIA-18 cierra el contrato: «registrar **exactamente** esas camas como su asignación médica vigente durante esa franja». RF-DIA-28 agrega a esa misma asignación toda cama con episodio abierto sin responsable. Un contrato cerrado y otro que lo amplía sobre el mismo objeto | auditoría; riesgo 1 de veredicto-rodrigo |
| 2 | **Contradicción RF-DIA-18 ↔ RF-DIA-29.** RF-DIA-18 garantiza la asignación «durante esa franja» y la CA-1 de RF-DIA-29 la desplaza a mitad de franja cuando otro médico declara la misma cama, sin que ningún RF avise al desplazado | auditoría; veredicto-carmen (Ambiguo); riesgo 2 de veredicto-rodrigo |
| 3 | **Doble constitución de la responsabilidad clínica.** RF-ESC-27 la constituye desde la asignación médica y la delegación; RF-IAM-06 la constituye y la extingue desde lo que la Red comunica, a nivel de unidad y no de cama, y su CA-2 la retira desde el instante comunicado, contra la garantía de RF-TUR-42. El glosario nombra la responsabilidad clínica vigente desde el profesional y respecto de una cama | auditoría; riesgo 5 de veredicto-rodrigo |
| 4 | **Vocabulario inconsistente de la entrega de un aviso clínico.** RF-ESC-22, 28 y 29 dicen «alcanzar … sin que deban consultarlo»; RF-ESC-13 dice «dirigida a» y su CA-2 la muestra al consultar los avisos pendientes. La misma familia de avisos se entrega con dos vocabularios y el glosario no arbitra entre ellos | auditoría; veredicto-milagros y veredicto-anibal, ambos Ambiguo sobre RF-ESC-13 |
| 5 | **RF-SUP-03 contra el glosario.** Declara persona Aníbal y la matriz lo hace único cubridor de su tarea 6, pero su contrato depende del «ámbito de responsabilidad», que el glosario compone con asignaciones, delegaciones y jefatura: un médico de guardia localizable —«turno médico sin asignación médica de camas»— no tiene ninguna de las tres | auditoría; veredicto-anibal y veredicto-milagros |
| 6 | **RF-TUR-01 contra la modalidad de la persona Aníbal.** El glosario define la guardia localizable como un turno médico; RF-TUR-01 rechaza toda asignación que solape otro turno vigente del mismo profesional en cualquier sede, de modo que la cobertura simultánea de dos UCIs que `Personas/Anibal.MD` declara vigente quedaría rechazada. RF-ESC-08 admite en cambio el estado «con cobertura simultánea de otro servicio» | auditoría; veredicto-anibal (Ambiguo) |

```
D5 = 60 (cinco tensiones × 12) + máx(0, 40 − 6 × 10) = 60 + 0 = 60,0
```

El repositorio tiene glosario (`docs/GLOSARIO.md`, 66 términos), de modo que el techo de 80 no
aplica. Ninguna cobertura percibida alcanza el 90 %, de modo que el techo de 40 por conformidad
unánime tampoco se activa.

## Priorización (D6)

Distribución declarada y verificada en el cuerpo: 63 MUST, 64 SHOULD, 2 COULD. Ningún RF sin
prioridad ni con prioridad fuera del vocabulario, de modo que no hay descuentos de 10. La prioridad
no es uniforme.

Tres MUST no superan la reserva: su ausencia no dejaría sin resolver un problema crítico ni
descubierta una tarea crítica.

| MUST | Por qué no está reservado |
|---|---|
| RF-DIA-15 — estado de información a la familia | Ninguna tarea crítica consiste en registrarlo; es un componente del contrato de RF-DIA-02 y su ausencia deja la tarea 1 de Rodrigo incompleta, no descubierta. P1 no depende de él |
| RF-DIA-25 — apertura de un pendiente de cuidado | Ninguna de las seis tareas de Milagros consiste en abrir pendientes; su tarea 6 sigue cubierta por RF-DIA-08, RF-DIA-11 y RF-DIA-27. Su gemelo RF-DIA-26 es SHOULD |
| RF-ESC-15 — registro de la emisión de un escalamiento | Es evidencia posterior: sin él se escala igual, se alcanza igual y la cadena avanza igual. Rodrigo y Carmen lo marcan Indiferente por eso mismo, y la auditoría de escalamientos que lo consume es COULD (RF-SUP-04) |

```
D6 = 100 − 0 × 10 − 3 × 5 = 100 − 15 = 85,0
```

En el sentido contrario, RF-DIA-17 es SHOULD siendo el único enunciado que distingue una entrega
ausente de una vieja, justo en el paso donde se corta el recorrido de Rodrigo. La rúbrica solo
penaliza el MUST no reservado, de modo que esto no descuenta; se registra como brecha.

## Contrastes cruzados

### Discrepancias entre agente y cómputo

| Persona | Δ | Qué falla: el agente o las tareas críticas |
|---|---:|---|
| Rodrigo | 78 − 28 = **50** | El agente. Su tabla de veredictos y su recorrido detectan el corte del paso 5, el Ambiguo de RF-DIA-05 y siete necesidades no cubiertas, pero su autoinforme del 78 % no descuenta nada de eso: puntúa la impresión de un documento que le sirve, no el estado de sus seis tareas. Sus tareas críticas están bien enunciadas |
| Milagros | 80 − 52 = **28** | El agente, con matiz. Declara «queda cubierta» cinco veces y a renglón seguido nombra la reserva que la deja incompleta —el estado residual «disponible», RF-IAM-02, RF-ESC-13, la entrega de enfermería no cerrada—. La percibida recoge el «cubierta» y no la reserva |
| Carmen | 75 − 36 = **39** | El agente. Es la evaluación más generosa en veredictos —67 Sirve— y a la vez la que declara un corte de flujo y siete necesidades no cubiertas. Un recorrido que se interrumpe en la tarea crítica más urgente de la persona no admite un 75 % de cobertura percibida |
| Aníbal | 80 − 48 = **32** | El agente. Declara su tarea 5 «la peor servida», su tarea 6 pendiente de una decisión que ningún RF toma y cuatro RF Estorba, tres de ellos fuera de sus tareas; el 80 % no refleja ninguno de esos descuentos |

Las cuatro desviaciones superan el umbral de 20 puntos y en las cuatro prevalece el valor computado.
Que las cuatro sean del mismo signo —percibida por encima de computada— es en sí un hallazgo: los
agentes describen la falla con precisión y luego la olvidan al puntuarse.

### Conformidad unánime

No aplica. Las coberturas percibidas son 78, 80, 75 y 80: ninguna alcanza el 90 % y, además, las
cinco tensiones están decididas. El techo de 40 sobre D5 no se activa.

### Necesidad no cubierta sin brecha

Las veinticinco necesidades no cubiertas que los agentes declaran —siete de Rodrigo, cuatro de
Milagros, siete de Carmen y siete de Aníbal— figuran en la tabla de brechas, salvo las que la
auditoría refuta por escrito:

| Necesidad declarada | Refutación |
|---|---|
| Rodrigo — «Definición de qué constituye mi último contacto con una cama» | `docs/GLOSARIO.md` la fija: «Último contacto: instante del registro o de la consulta más reciente de un profesional sobre una cama dentro del episodio en curso; a falta de contacto anterior, es la apertura del episodio». RF-DIA-05 CA-2 aplica esa segunda mitad. La lectura que vacía su diferencial es la correcta, pero no es una ambigüedad: es una decisión declarada que le resulta adversa, y como tal se registra en la brecha 16 |
| Rodrigo — «RF-SUP-01 habla de cada dato obligatorio ausente sin decir cuáles son» | El glosario define «Dato obligatorio de la entrega médica … es uno solo: el diagnóstico de ese turno de esa cama». La puerta por la que temía que se colara una ficha exhaustiva está cerrada por escrito |
| Aníbal — riesgo de que iniciar su bloque de localizable lo convierta en responsable de las camas huérfanas (RF-DIA-28) | El glosario define la guardia localizable como «turno médico sin asignación médica de camas» y la CA-2 de RF-DIA-01 contempla expresamente al médico de guardia localizable «sin asignación médica vigente de camas». No hereda camas huérfanas |
| Carmen — riesgo de que RF-ESC-09 la alcance fuera de horario sin poder delegar su posición de jefatura | El glosario declara que la responsabilidad de la jefatura «admite delegación activa» y la CA-2 de RF-ESC-09 alcanza al delegado de la jefatura; RF-ESC-07 es el acto por el que lo declara. Refutada |

## Brechas encontradas

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| 1 | Rodrigo · P1 | Ningún RF obliga a registrar la decisión clínica y su fundamento: RF-DIA-02 promete presentarlos y RF-DIA-01 condiciona el cierre solo al diagnóstico, de modo que el handoff puede cerrar en regla sin un solo porqué | veredicto-rodrigo | Alta |
| 2 | Rodrigo · P1 | Un turno que concluye sin cerrar su entrega no deja vía declarada para recuperar el contexto de la cama: RF-DIA-17 declara la ausencia y RF-DIA-24 advierte a la jefatura. Es el corte del recorrido de Rodrigo y el tramo que baja P1 a 50 | veredicto-rodrigo · auditoría | Alta |
| 3 | Milagros | Enfermería no tiene equivalente de RF-DIA-17: nada declara qué recibe la entrante cuando la saliente concluyó sin entrega cerrada, y RF-DIA-11 se apoya en «la última entrega cerrada» | veredicto-milagros | Alta |
| 4 | Carmen | Ningún RF permite asignar directamente a un profesional a una franja de la programación vigente: RF-TUR-11 opera solo sobre una propuesta y RF-TUR-35 exige la aceptación del candidato. Es el corte del recorrido de Carmen | veredicto-carmen | Alta |
| 5 | Carmen | RF-TUR-09 presupone «las franjas de cobertura requeridas» de la unidad y ningún RF declara su origen ni permite definirlas | veredicto-carmen | Alta |
| 6 | Aníbal · Milagros | El «ámbito de responsabilidad» de RF-SUP-03 no queda constituido para un médico de guardia localizable ni para una enfermera con asignación de cuidado: la única tarea que ese RF cubre queda sin alcance | veredicto-anibal · veredicto-milagros · auditoría | Alta |
| 7 | Aníbal · P2 | RF-ESC-07 solo admite declararse indisponible indicando delegado y RF-ESC-30 puede dejar sin delegado admisible: no hay enunciado para la indisponibilidad genuina sin delegado | veredicto-anibal | Alta |
| 8 | Aníbal · P2 | Ningún RF declara que se comunique al titular el vencimiento de su delegación ni su revocación por la jefatura (RF-ESC-31): puede volver a encabezar la cadena sin saberlo | veredicto-anibal | Alta |
| 9 | Aníbal · P3 | RF-ESC-29 alcanza al responsable clínico vigente y a enfermería, pero no al médico con toma del caso vigente que está manejando la cama a distancia | veredicto-anibal | Alta |
| 10 | Milagros · Aníbal · P3 | RF-ESC-13 no declara si la actualización informativa alcanza sin consulta previa o espera a ser consultada. Dos agentes independientes lo marcaron Ambiguo; es el tramo que baja P3 a 50 | veredicto-milagros · veredicto-anibal | Alta |
| 11 | Rodrigo · Milagros | RF-IAM-02 rechaza el registro sobre una cama fuera de la asignación propia sin escalamiento de por medio: el médico llamado a una cama ajena y la enfermera que cubre a su colega vuelven al papel | veredicto-rodrigo · veredicto-milagros | Alta |
| 12 | Rodrigo · Carmen | RF-DIA-18 declara la asignación médica «exactamente» y RF-DIA-28 le agrega toda cama huérfana de la unidad; combinado con RF-DIA-01, el rotante entra a una UCI ajena y sale debiendo diez diagnósticos | auditoría · veredicto-rodrigo · veredicto-carmen | Alta |
| 13 | Rodrigo · Carmen | RF-DIA-29 no decide en el enunciado qué ocurre ante una segunda declaración sobre la misma cama; su criterio desplaza al primer médico y ningún RF le avisa | auditoría · veredicto-carmen | Alta |
| 14 | Rodrigo | RF-IAM-06 constituye y extingue la responsabilidad clínica del rotante por una vía distinta de RF-ESC-27 y contra la garantía de RF-TUR-42: la primera noche puede llegar sin poder registrar | auditoría · veredicto-rodrigo | Alta |
| 15 | Aníbal | RF-TUR-01, leído con el glosario, rechazaría la modalidad de guardia localizable simultánea en dos sedes que `Personas/Anibal.MD` declara vigente | veredicto-anibal · auditoría | Alta |
| 16 | Rodrigo | El diferencial de RF-DIA-05 se vacía en cuanto Rodrigo consulta la cama una vez: el glosario cuenta la consulta como contacto, de modo que a las 23:40 no obtiene las tres semanas sino lo ocurrido desde su vistazo de las 19:05 | veredicto-rodrigo · auditoría | Alta |
| 17 | Carmen | RF-DIA-12 no declara a quién presenta las camas sin diagnóstico cuando el cierre se bloquea | veredicto-carmen · auditoría | Media |
| 18 | Rodrigo | Los resultados de laboratorio e imágenes anteriores al episodio o producidos en otra sede de la Red no llegan: todo se declara «del episodio» | veredicto-rodrigo | Media |
| 19 | Rodrigo | Los pendientes de cuidado que enfermería abre (RF-DIA-25) no figuran ni en el contenido de la entrega médica (RF-DIA-02) ni en el estado clínico de la cama (RF-DIA-21) | veredicto-rodrigo | Media |
| 20 | Rodrigo | La entrega se enuncia en singular —«el turno inmediatamente anterior»— y no declara cómo se compone cuando ese turno lo cubrieron dos médicos con camas repartidas | veredicto-rodrigo | Media |
| 21 | Carmen | Ningún RF avisa a la coordinadora cuando una franja queda descubierta por un hecho que ella no inició, en particular el retiro de un rotante que decide la Red (RF-TUR-24) | veredicto-carmen | Media |
| 22 | Carmen | No hay vía declarada para modificar la programación vigente fuera de los tres caminos existentes —intercambio, ausencia y solicitud de cobertura— | veredicto-carmen | Media |
| 23 | Carmen | No hay vía declarada para retirar una propuesta o una programación publicada que resultó equivocada | veredicto-carmen | Media |
| 24 | Carmen | Ningún RF le presenta las horas acumuladas del mes de un profesional antes de asignarle un turno, dato que su escenario le exige | veredicto-carmen | Media |
| 25 | Carmen | RF-TUR-02 y RF-TUR-03 dan por disponibles las reglas de jornada y descanso sin que ningún RF declare su origen; RF-TUR-03 excluye al profesional que no las tenga y puede vaciar la lista de candidatos | veredicto-carmen | Media |
| 26 | Carmen | Ningún RF declara que la jefatura pueda consultar el registro de accesos de RF-IAM-03, que es la trazabilidad que la Red le exige acreditar | veredicto-carmen | Media |
| 27 | Carmen | RF-DIA-27 cierra la entrega de enfermería sin ninguna exigencia de completitud, a diferencia de la médica, y la Red no distingue estamento al pedirle cumplimiento | veredicto-carmen | Media |
| 28 | Milagros | Ningún RF la alcanza junto a la cama cuando cambia el responsable clínico vigente de sus camas durante el turno: RF-ESC-08 exige consulta y RF-ESC-26 avisa a la jefatura | veredicto-milagros | Media |
| 29 | Milagros | «Disponible» es el estado residual de RF-ESC-08: el médico ocupado que nadie registró figura disponible, igual que hoy en el papel de la pared | veredicto-milagros | Media |
| 30 | Milagros | RF-ESC-16 ordena la severidad por confirmar por debajo de todo deterioro inmediato, y son precisamente los escalamientos que ella emite sin tiempo para clasificar | veredicto-milagros | Media |
| 31 | Aníbal | RF-ESC-25 le entrega toda duda no clasificada con el plazo del deterioro inmediato; la selectividad queda entregada a la etiqueta del aviso y no al plazo | veredicto-anibal | Media |
| 32 | Aníbal | Ningún RF declara que pueda registrar a distancia y desde su dispositivo la decisión clínica fundamentada, incluida la de no acudir | veredicto-anibal | Media |
| 33 | Aníbal | RF-ESC-07 y RF-ESC-17 mencionan la revocación anticipada, pero el único acto de revocación declarado es el de la jefatura (RF-ESC-31): el titular no puede revocar su propia delegación | veredicto-anibal | Media |
| 34 | Rodrigo · P1 | RF-DIA-17 es SHOULD siendo el único enunciado que distingue una entrega ausente de una vieja, justo donde se corta su recorrido | auditoría | Media |
| 35 | Aníbal | Ningún RF declara hasta cuándo conserva acceso al episodio que atendió después del cierre de RF-ESC-19, que es lo que su revisión matutina necesita | veredicto-anibal | Baja |
| 36 | Rodrigo | RF-DIA-06 admite que cualquier profesional retire la marca de inestabilidad, sin exigir responsabilidad sobre esa cama | veredicto-rodrigo | Baja |
| 37 | Milagros | RF-TUR-28 devuelve a la unidad una copia impresa de la programación, que es el objeto que a las 02:15 la mandó a llamar al Dr. Paredes; declarar su instante de generación no impide leerla con prisa | veredicto-milagros | Baja |
| 38 | Rodrigo | Las copias imprimibles de RF-TUR-16 y RF-TUR-28 solo las obtiene la coordinadora: la salida del rotante ante la fricción no es una copia oficial sino su cuaderno | veredicto-rodrigo | Baja |
| 39 | Documento | Tres MUST sin reserva —RF-DIA-15, RF-DIA-25 y RF-ESC-15—: su ausencia no dejaría un problema crítico sin resolver ni una tarea crítica descubierta | auditoría | Baja |

39 brechas abiertas.

## Evaluaciones de agente ausentes o inválidas

| Persona | Qué falta |
|---|---|
| — | Ninguna. Las cuatro evaluaciones emiten veredicto para los 129 RF, en el mismo orden de identificadores del cuerpo, con vocabulario cerrado y sin omisiones ni valores fuera de {Sirve, Indiferente, Estorba, Ambiguo} |

## Cálculo global

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 41,0 | 0,30 | 12,300 |
| D2 Cobertura de problemas críticos | 66,7 | 0,25 | 16,675 |
| D3 Verificabilidad y forma | 98,4 | 0,20 | 19,680 |
| D4 Trazabilidad | 100,0 | 0,10 | 10,000 |
| D5 Consistencia y tensiones | 60,0 | 0,10 | 6,000 |
| D6 Priorización | 85,0 | 0,05 | 4,250 |
| **Global** | | | **68,905 → 68,9** |

## Veredicto

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 68,9 % | no |
| 2 | D1 | ≥ 80,0 | 41,0 | no |
| 3 | Persona más baja | ≥ 7,0/10 | 2,8 (Rodrigo) | no |
| 4 | D2 | ≥ 80,0 | 66,7 | no |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | sí |

Cuatro de las cinco condiciones fallan: **FAILED**.
