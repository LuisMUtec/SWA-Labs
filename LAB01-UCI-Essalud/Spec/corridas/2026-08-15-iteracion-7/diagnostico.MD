# Diagnóstico — corrida 2026-08-15-iteracion-7

`Requirements/ReqFunc.MD` @ `c923c7f` · rúbrica `Spec/Eval-Spec.MD` @ `b492237` · modelo
claude-opus-5 · instrumento no modificado · glosario presente.

## Precondiciones

Las cuatro evaluaciones están presentes, cada una con un veredicto para los 163 RF vigentes, en el
mismo conjunto y el mismo orden de identificadores, y con vocabulario cerrado. No hay omisiones ni
veredictos inválidos, de modo que D1 es computable.

| Persona | Sirve | Indiferente | Estorba | Ambiguo | Total | Percibida |
|---|---:|---:|---:|---:|---:|---:|
| Rodrigo | 41 | 116 | 2 | 4 | 163 | 75 |
| Milagros | 71 | 88 | 2 | 2 | 163 | 85 |
| Carmen | 77 | 80 | 1 | 5 | 163 | 80 |
| Aníbal | 71 | 89 | 1 | 2 | 163 | 85 |

## Veredictos agregados

`S` Sirve · `I` Indiferente · `E` Estorba · `A` Ambiguo. La columna **Efecto en D1** cita la tarea
crítica a la que el RF traza según la matriz de trazabilidad de `ReqFunc.MD` —`R1`–`R6` Rodrigo,
`M1`–`M6` Milagros, `C1`–`C6` Carmen, `A1`–`A6` Aníbal— y marca `X_p` cuando un **Estorba** cae fuera
de las seis tareas de quien lo emitió y por tanto resta 2 puntos.

| RF | Rodrigo | Milagros | Carmen | Aníbal | Efecto en D1 |
|---|:--:|:--:|:--:|:--:|---|
| RF-TUR-01 | I | I | S | S | C2 |
| RF-TUR-02 | I | I | S | I | C2 |
| RF-TUR-03 | I | I | S | I | C4 |
| RF-TUR-04 | I | S | S | S | C1 |
| RF-TUR-05 | I | I | S | S | C4 |
| RF-TUR-06 | S | I | S | I | C3 |
| RF-TUR-07 | I | I | S | I | C2 |
| RF-TUR-08 | I | S | S | I | — |
| RF-TUR-09 | I | I | S | I | C1 |
| RF-TUR-10 | I | I | S | I | C1 |
| RF-TUR-11 | I | I | S | I | C1 |
| RF-TUR-12 | I | I | S | I | C3 |
| RF-TUR-13 | S | I | A | I | C3 |
| RF-TUR-14 | I | I | S | I | — |
| RF-TUR-15 | E | I | S | I | **X_Rodrigo** |
| RF-TUR-16 | I | I | I | I | — |
| RF-TUR-17 | I | I | S | I | C3 |
| RF-TUR-18 | I | I | S | I | C4 |
| RF-TUR-19 | I | S | S | I | C4 |
| RF-TUR-20 | I | I | S | I | C4 |
| RF-TUR-21 | I | I | S | I | C3 |
| RF-TUR-22 | I | I | S | I | C3 |
| RF-TUR-23 | I | I | S | I | — |
| RF-TUR-24 | I | I | S | I | — |
| RF-TUR-25 | I | I | S | I | C4 |
| RF-TUR-26 | I | I | S | S | C4 |
| RF-TUR-27 | I | S | S | S | C1 |
| RF-TUR-28 | I | I | S | I | C1 |
| RF-TUR-29 | I | I | S | I | C3 |
| RF-TUR-30 | I | I | S | I | C3 |
| RF-TUR-31 | E | I | S | I | C3 · **X_Rodrigo** |
| RF-TUR-32 | I | I | S | I | C3 |
| RF-TUR-33 | I | I | S | I | C3 |
| RF-TUR-34 | I | I | S | I | C3 |
| RF-TUR-35 | I | I | S | I | C4 |
| RF-TUR-36 | I | I | S | I | C4 |
| RF-TUR-37 | I | I | S | I | C4 |
| RF-TUR-38 | I | I | S | I | C4 |
| RF-TUR-39 | I | I | S | I | C4 |
| RF-TUR-40 | I | I | S | I | C4 |
| RF-TUR-41 | I | S | S | S | C4 |
| RF-TUR-42 | S | S | S | I | R6 · C2 |
| RF-TUR-43 | I | I | S | I | C4 |
| RF-TUR-44 | I | I | S | I | C4 |
| RF-TUR-45 | I | I | S | I | C2 |
| RF-TUR-46 | I | I | S | I | C1 |
| RF-DIA-01 | S | I | S | S | R6 |
| RF-DIA-02 | S | I | I | I | R1 · R2 |
| RF-DIA-03 | S | I | I | I | R1 |
| RF-DIA-04 | S | I | S | I | R6 |
| RF-DIA-05 | S | I | I | S | R2 · A3 |
| RF-DIA-06 | S | S | I | I | R4 |
| RF-DIA-07 | S | I | S | S | R2 · R3 |
| RF-DIA-08 | I | S | I | I | M6 |
| RF-DIA-09 | S | I | I | I | R1 |
| RF-DIA-10 | S | I | I | I | R1 · R2 |
| RF-DIA-11 | I | S | I | I | M6 |
| RF-DIA-12 | S | I | S | I | R6 · C5 |
| RF-DIA-13 | S | I | I | S | R2 · R3 |
| RF-DIA-14 | S | I | I | S | R2 · R3 |
| RF-DIA-15 | S | I | I | I | R2 · R3 |
| RF-DIA-16 | S | I | I | I | R3 |
| RF-DIA-17 | S | I | I | I | R1 |
| RF-DIA-18 | S | S | S | I | R1 |
| RF-DIA-19 | I | S | I | I | M6 |
| RF-DIA-20 | S | I | S | I | R6 |
| RF-DIA-21 | S | I | I | I | R2 |
| RF-DIA-22 | S | S | I | I | R4 |
| RF-DIA-23 | S | S | I | S | R2 |
| RF-DIA-24 | S | I | S | I | R6 · C5 |
| RF-DIA-25 | I | S | I | I | M6 |
| RF-DIA-26 | I | S | I | I | M6 |
| RF-DIA-27 | I | S | I | I | M6 |
| RF-DIA-28 | S | I | S | S | R1 |
| RF-DIA-29 | S | S | S | I | R1 · M2 |
| RF-DIA-30 | I | **E** | I | I | M6 — Estorba dentro de tarea: no suma a `X_Milagros` |
| RF-DIA-31 | S | I | S | I | R6 |
| RF-DIA-32 | S | I | I | I | R1 |
| RF-DIA-33 | I | S | I | I | M6 |
| RF-DIA-34 | S | I | S | I | R6 |
| RF-DIA-35 | S | I | I | I | R1 |
| RF-DIA-36 | I | S | S | I | C4 |
| RF-DIA-37 | I | **E** | I | I | M6 — Estorba dentro de tarea: no suma a `X_Milagros` |
| RF-DIA-38 | I | S | I | I | M6 |
| RF-DIA-39 | S | I | I | I | R1 |
| RF-DIA-40 | S | I | S | S | R2 · R3 |
| RF-DIA-41 | S | S | I | I | R4 |
| RF-ESC-01 | I | S | S | S | M2 |
| RF-ESC-02 | I | S | I | S | — |
| RF-ESC-03 | S | S | I | S | A1 |
| RF-ESC-04 | I | S | I | S | A2 |
| RF-ESC-05 | I | S | I | I | — |
| RF-ESC-06 | I | S | I | S | M2 |
| RF-ESC-07 | I | S | S | S | A5 |
| RF-ESC-08 | A | S | A | I | M3 |
| RF-ESC-09 | I | S | A | A | — |
| RF-ESC-10 | I | I | I | S | — |
| RF-ESC-11 | I | S | I | S | M2 |
| RF-ESC-12 | I | S | I | S | A2 |
| RF-ESC-13 | I | S | I | S | M4 |
| RF-ESC-14 | I | S | I | S | A2 |
| RF-ESC-15 | I | S | I | S | M2 |
| RF-ESC-16 | I | A | I | S | A1 |
| RF-ESC-17 | I | S | I | S | A5 |
| RF-ESC-18 | I | S | S | S | — |
| RF-ESC-19 | I | S | I | S | A2 |
| RF-ESC-20 | I | S | I | S | M2 |
| RF-ESC-21 | I | S | I | S | M2 |
| RF-ESC-22 | I | S | I | S | M2 |
| RF-ESC-23 | I | S | A | S | M2 |
| RF-ESC-24 | I | I | I | S | A1 |
| RF-ESC-25 | A | S | I | **E** | M2 · **X_Aníbal** |
| RF-ESC-26 | I | I | S | S | C2 |
| RF-ESC-27 | I | S | I | S | M2 · M3 |
| RF-ESC-28 | I | S | I | S | M4 |
| RF-ESC-29 | S | S | I | S | R5 |
| RF-ESC-30 | I | S | S | S | C2 · A5 |
| RF-ESC-31 | I | I | S | I | C2 · A5 |
| RF-ESC-32 | I | S | S | S | M3 · A5 |
| RF-ESC-33 | I | I | S | S | C2 |
| RF-ESC-34 | I | I | S | S | A5 |
| RF-ESC-35 | I | S | I | S | M2 · M3 · A5 |
| RF-ESC-36 | I | S | I | I | M4 |
| RF-ESC-37 | I | S | I | S | M2 · A4 |
| RF-ESC-38 | I | S | I | S | M4 |
| RF-ESC-39 | I | S | I | S | M2 |
| RF-ESC-40 | I | S | I | S | M2 · A5 |
| RF-ESC-41 | I | S | I | I | M3 |
| RF-ESC-42 | I | I | S | S | A5 |
| RF-ESC-43 | I | S | **E** | S | M2 · M3 · **X_Carmen** |
| RF-REG-01 | I | S | I | S | M1 |
| RF-REG-02 | I | S | I | S | M1 |
| RF-REG-03 | S | S | I | S | M4 |
| RF-REG-04 | I | S | I | S | M4 |
| RF-REG-05 | I | S | I | S | M5 |
| RF-REG-06 | S | I | I | S | R5 |
| RF-REG-07 | I | S | I | S | A4 |
| RF-REG-08 | S | I | I | S | A3 |
| RF-REG-09 | I | I | I | S | A4 |
| RF-REG-10 | A | I | I | S | R5 |
| RF-REG-11 | I | S | I | S | A4 |
| RF-REG-12 | S | I | I | I | R5 |
| RF-REG-13 | I | S | I | A | M4 · A4 |
| RF-IAM-01 | A | S | S | S | R3 |
| RF-IAM-02 | S | S | S | S | R3 · M5 · A4 |
| RF-IAM-03 | I | I | S | I | — |
| RF-IAM-04 | I | I | I | S | A1 |
| RF-IAM-05 | I | I | I | S | A1 · A4 |
| RF-IAM-06 | I | I | S | I | — |
| RF-IAM-07 | I | I | I | S | A1 · A4 |
| RF-IAM-08 | I | A | I | S | A1 · A4 |
| RF-IAM-09 | I | I | I | S | R3 · A4 |
| RF-IAM-10 | I | S | I | I | R3 · M5 |
| RF-IAM-11 | I | S | S | S | A1 |
| RF-IAM-12 | I | I | I | S | A1 |
| RF-IAM-13 | I | I | S | I | C1 · C4 |
| RF-IAM-14 | S | S | S | I | R3 · M5 |
| RF-SUP-01 | I | I | S | I | R6 · C5 |
| RF-SUP-02 | I | I | S | I | C6 |
| RF-SUP-03 | I | S | I | S | A6 |
| RF-SUP-04 | I | S | I | I | — |
| RF-SUP-05 | I | I | A | I | C6 |
| RF-SUP-06 | I | I | S | I | — |

## Matriz de cobertura

Cada tarea se puntúa contra el texto literal de `Personas/*.MD`, la matriz de trazabilidad de
`ReqFunc.MD` y el veredicto del agente de esa persona. **5** cubierta, **3** incompleta, **1**
aparente, **0** descubierta.

| Persona | Tarea crítica | RF que la cubre | Veredicto | Puntos | Estado |
|---|---|---|---|---:|---|
| Rodrigo | 1 · Recibir el handoff estructurado de todas las camas asignadas | RF-DIA-02, 03, 09, 10, 17, 18, 28, 29, 32, 35, 39 | Sirve (11/11) | 3 | Incompleta — el criterio de éxito «el handoff incluye no solo datos, sino decisiones y su justificación» no queda satisfecho: la CA-4 de RF-DIA-02 declara la decisión «no registrada» y ningún enunciado obliga al saliente a producirla |
| Rodrigo | 2 · Consultar la evolución y el diagnóstico del turno anterior | RF-DIA-02, 05, 07, 10, 13, 14, 15, 21, 23, 40 | Sirve (10/10) | 3 | Incompleta — RF-DIA-05 resuelve «qué cambió desde su último contacto» al pie de la letra, pero las dos preguntas que su escenario declara —por qué no se escaló el soporte y si la familia fue informada— pueden llegar vacías; la garantía que la persona exige es que ese contexto **exista** |
| Rodrigo | 3 · Registrar nota de evolución y diagnóstico por paciente | RF-DIA-07, 13, 14, 15, 16, 40; RF-IAM-01, 02, 09, 10, 14 | Sirve salvo RF-IAM-01 (Ambiguo) | 3 | Incompleta — el acto de registrar está declarado entero; la atribución en la PC compartida descansa en RF-IAM-01, que no exige verificar identidad antes de escribir, y esa es una restricción explícita de la persona |
| Rodrigo | 4 · Marcar pacientes inestables o con pendientes críticos | RF-DIA-06, 22, 41 | Sirve (3/3) | 5 | Cubierta — la marca permanece vigente, se consulta por unidad y el retiro se avisa a quien la dejó; ningún RF implicado contradice a otro |
| Rodrigo | 5 · Consultar resultados de laboratorio e imágenes | RF-REG-06, 12; RF-ESC-29; RF-REG-10 (Ambiguo) | Sirve 3, Ambiguo 1 | 3 | Incompleta — lo que ya tiene resultado está resuelto y RF-REG-12 ataca su frustración de repetir exámenes; el cultivo pendiente de su escenario se apoya en RF-REG-10, cuyo señalamiento ningún acto de solicitud alimenta |
| Rodrigo | 6 · Cerrar y firmar la entrega de turno | RF-DIA-01, 04, 12, 20, 24, 31, 34; RF-TUR-42; RF-SUP-01 | Sirve (8/9, SUP-01 Indiferente) | 5 | Cubierta — el cierre exige el diagnóstico y nada más, RF-DIA-12 dice qué falta, RF-DIA-31 evita el reingreso y RF-TUR-42 le conserva la guardia para poder cerrar |
| Milagros | 1 · Registrar signos vitales y balance por paciente | RF-REG-01, 02 | Sirve (2/2) | 3 | Incompleta — «junto a la cama» está declarado con todas las letras y la desconexión está cubierta; falta el dispositivo con el que verifica su identidad para que RF-IAM-01 pueda atribuirle el registro (RF-IAM-08, Ambiguo) |
| Milagros | 2 · Escalar un deterioro clínico al médico responsable | RF-ESC-01, 06, 11, 15, 20, 21, 22, 23, 25, 27, 35, 37, 39, 40, 43; RF-DIA-29 | Sirve (16/16) | 5 | Cubierta — declara el deterioro sin apartarse, sin clasificar y sin costo de plazo; la cadena avanza sola y termina en la jefatura vigente. Es la única tarea de las 24 que llega entera |
| Milagros | 3 · Consultar quién está de guardia y su estado de disponibilidad | RF-ESC-08, 27, 32, 35, 41, 43 | Sirve (6/6) | 3 | Incompleta — obtiene el responsable vigente por cama con su estado exacto, pero RF-ESC-08 no declara que la consulta pueda hacerse junto a la cama, y es la consulta que hace ante cada escalamiento |
| Milagros | 4 · Ver y confirmar indicaciones médicas vigentes | RF-REG-03, 04, 13; RF-ESC-13, 28, 36, 38 | Sirve (7/7) | 3 | Incompleta — la indicación nueva y la suspensión la alcanzan junto a la cama, pero RF-REG-03 y RF-REG-04 no declaran dónde se consulta ni dónde se confirma, y hoy eso es la PC de la estación |
| Milagros | 5 · Registrar eventos y administración de medicamentos | RF-REG-05; RF-IAM-02, 10, 14 | Sirve (4/4) | 3 | Incompleta — arrastra la misma dependencia de la tarea 1: el dispositivo de registro junto a la cama no está declarado |
| Milagros | 6 · Recibir y entregar el turno de enfermería | RF-DIA-08, 11, 19, 25, 26, 27, 33, 38; RF-DIA-30 y RF-DIA-37 (**Estorba**) | Sirve 8, Estorba 2 | 3 | Incompleta — la entrega se compone y se recibe sin transcripción, pero dos RF de la propia fila le hacen daño: uno la carga sin límite con las camas huérfanas y el otro deja cada cama en manos de la última que la declara |
| Carmen | 1 · Elaborar y publicar la programación mensual de turnos | RF-TUR-04, 09, 10, 11, 27, 28, 46; RF-IAM-13 | Sirve (8/8) | 3 | Incompleta — una sola versión vigente con historial, sí; falta el formato imprimible que su restricción exige y el acto de corregir una asignación de la programación vigente fuera de urgencia |
| Carmen | 2 · Validar que no existan cruces ni franjas descubiertas | RF-TUR-01, 02, 07, 42, 45; RF-ESC-26, 30, 31, 33 | Sirve (9/9) | 3 | Incompleta — RF-TUR-01 impide guardar el cruce entre sedes al pie de la letra, pero RF-TUR-02 es SHOULD y solo actúa si hay un vínculo laboral registrado: sin él no hay tope que infringir, y ella responde ante la Red por ese tope |
| Carmen | 3 · Aprobar o rechazar intercambios y permisos | RF-TUR-06, 12, 17, 21, 22, 29, 30, 31, 32, 33, 34; RF-TUR-13 (Ambiguo) | Sirve 11, Ambiguo 1 | 3 | Incompleta — el camino individual está entero; el previo depende de acotar la autorización y RF-TUR-13 no declara qué compone un alcance |
| Carmen | 4 · Reasignar cobertura ante una ausencia imprevista | RF-TUR-03, 05, 18, 19, 20, 25, 26, 35, 36, 37, 38, 39, 40, 41, 43, 44; RF-DIA-36; RF-IAM-13 | Sirve (18/18) | 3 | Incompleta — es la parte mejor resuelta del documento y aun así RF-TUR-03 enumera exactamente tres condiciones de exclusión y la ausencia imprevista no está entre ellas: el profesional que acaba de retirar vuelve a figurarle como candidato |
| Carmen | 5 · Monitorear cumplimiento y completitud de entregas de turno | RF-DIA-12, 24; RF-SUP-01 | Sirve (3/3) | 5 | Cubierta — su criterio «saber qué entregas se cerraron sin diagnóstico» queda resuelto por partida doble, con el bloqueo y con el consolidado, sin cargarle transcripción a Rodrigo |
| Carmen | 6 · Generar indicadores de cobertura para la Dirección de Red | RF-SUP-02; RF-SUP-05 (Ambiguo) | Sirve 1, Ambiguo 1 | 3 | Incompleta — RF-SUP-02 declara la producción sin transcripción manual, pero lo único que le **entrega** algo son franjas descubiertas y entregas cerradas, que por glosario son el insumo del indicador y no el indicador |
| Aníbal | 1 · Recibir la alerta de escalamiento con contexto clínico adjunto | RF-ESC-03, 16, 24; RF-IAM-04, 05, 07, 08, 11, 12 | Sirve 8, Ambiguo 1 (RF-ESC-16 lo marcó Milagros, no él) | 5 | Cubierta — RF-ESC-03 enumera los seis datos que hoy arranca a preguntas y declara no registrado lo que falte; RF-IAM-04 respeta su restricción de celular personal |
| Aníbal | 2 · Confirmar recepción y tomar el caso | RF-ESC-04, 12, 14, 19 | Sirve (4/4) | 5 | Cubierta — el acuse y la toma quedan registrados y quien escaló los ve de inmediato; el costo del gesto pertenece a `ReqNoFunc.MD` y el propio agente no lo reclama aquí |
| Aníbal | 3 · Consultar tendencia de signos, ventilación y última evolución | RF-REG-08; RF-DIA-05 | Sirve (2/2) | 3 | Incompleta — obtiene las seis horas, los cinco parámetros y la última evolución, pero el esquema antimicrobiano con su día solo viaja en el paquete del escalamiento: RF-DIA-21 lo condiciona a una asignación médica que un localizable nunca tiene |
| Aníbal | 4 · Registrar la indicación dada de forma remota | RF-REG-07, 09, 11; RF-ESC-37; RF-IAM-02, 05, 07, 08, 09; RF-REG-13 (Ambiguo) | Sirve 9, Ambiguo 1 | 3 | Incompleta — indicar y decidir a distancia están declarados con el dispositivo personal; suspender lo que él mismo indicó, no |
| Aníbal | 5 · Marcarse temporalmente indisponible y delegar | RF-ESC-07, 17, 30, 31, 32, 34, 35, 40, 42 | Sirve (9/9) | 5 | Cubierta — puede declararse indisponible aun sin delegado admisible, la declaración desvía la cadena de verdad, el delegado inadmisible se rechaza y la terminación se le informa |
| Aníbal | 6 · Revisar en la mañana lo ocurrido durante la noche | RF-SUP-03 | Sirve (1/1) | 5 | Cubierta — su CA-1 describe literalmente al localizable sin camas con dos unidades en sedes distintas, y «ámbito de responsabilidad» está definido en `docs/GLOSARIO.md`, contra lo que supone el agente |

### Daño fuera de tarea — `X_p`

| Persona | RF marcados Estorba | Traza a una de sus seis tareas | Cuenta en `X_p` | `X_p` |
|---|---|---|---|---:|
| Rodrigo | RF-TUR-15 | no (no figura en ninguna fila de Rodrigo) | **sí** | |
| Rodrigo | RF-TUR-31 | figura en C3, no en ninguna fila de Rodrigo | **sí** | **2** |
| Milagros | RF-DIA-30 | sí, M6 | no | |
| Milagros | RF-DIA-37 | sí, M6 | no | **0** |
| Carmen | RF-ESC-43 | no (sus filas no lo citan; traza a M2 y M3) | **sí** | **1** |
| Aníbal | RF-ESC-25 | no (sus filas no lo citan; traza a M2) | **sí** | **1** |

Los dos Estorba de Milagros caen **dentro** de su tarea 6 y por eso no restan 2 puntos cada uno: ya
pagan en la puntuación de esa tarea, que queda en 3. Contarlos otra vez en `X_p` sería cobrar dos
veces el mismo daño.

## Recorrido del escenario clave y claridad del flujo

Escala: **4** completo y con cada paso en un RF explícito; **2** completo con al menos un paso apoyado
en un RF que ese agente marcó Ambiguo; **0** interrumpido.

| Persona | Recorrido | Paso exacto que lo baja | Flujo |
|---|---|---|---:|
| Rodrigo | 19:00–07:00, Almenara, 15 pasos, sin cortes | Paso 1: la atribución de todo lo que escriba descansa en **RF-IAM-01** (Ambiguo) y nada le impide saltarse la verificación. Paso 10: el cultivo pendiente se apoya en **RF-REG-10** (Ambiguo). Los pasos 11 y 12 no se cortan pero llegan vacíos: RF-DIA-02 CA-4 declara la decisión y el estado de la familia «no registrados» | **2** |
| Milagros | 19:00–03:00, cama 3, de la declaración del deterioro al cierre de la atención, sin cortes | Paso de las 02:15 y de las 02:22: para que RF-IAM-01 atribuya el escalamiento y el registro a su identidad, tiene que estar verificada en el equipo que usa junto a la cama, y el único enunciado que habla de eso es **RF-IAM-08** (Ambiguo). Salvedad añadida en el paso de las 02:15: RF-ESC-08 no declara que la cobertura pueda consultarse junto a la cama | **2** |
| Carmen | Viernes 15:40 a domingo, 13 pasos, sin cortes | Paso 12: la cadena de la madrugada se apoya en **RF-ESC-23** y **RF-ESC-09**, los dos Ambiguo para ella. Paso 4: fuga declarada —RF-TUR-03 no filtra la ausencia imprevista—, que no corta el recorrido porque los candidatos igual se presentan. Paso 8: **no es un 0**. Su corte es condicional y depende del horizonte de urgencia, que `Eval-Spec` §Alcance asigna expresamente al umbral de `ReqNoFunc.MD`: RF-TUR-44 sostiene el paso como comportamiento, y un RF que se apoya en un umbral ajeno se juzga por su comportamiento, no por el umbral. El flujo no queda sin RF en ningún paso | **2** |
| Aníbal | 03:20, hospital B, 14 pasos, sin cortes | Paso 12: la suspensión de la infusión se apoya en **RF-REG-13** (Ambiguo), que constituye el acto sin declarar el dispositivo personal. Segunda dependencia en la rama de no contestar: **RF-ESC-09** (Ambiguo) | **2** |

Ninguno de los cuatro recorridos alcanza 4 y ninguno cae a 0. Lo que impide el 4 es siempre el mismo
tipo de enunciado: un acto que el documento constituye sin declarar dónde o con qué se ejecuta
—RF-IAM-01 y RF-IAM-08 para la identidad, RF-REG-13 para la suspensión—, o un objeto que un RF invoca
y ningún otro constituye —RF-REG-10 para la solicitud del estudio, RF-ESC-09 para la delegación de la
jefatura—, o un orden que se declara existente sin declararlo determinado —RF-ESC-23—.

## Cómputo de D1

```
Rodrigo   Σ tareas = 3 + 3 + 3 + 5 + 3 + 5 = 22 ;  X = 2 ;  Flujo = 2
          Puntaje = máx(0, 22 − 2×2) / 5 + 2 = 18 / 5 + 2 = 3,6 + 2 = 5,6

Milagros  Σ tareas = 3 + 5 + 3 + 3 + 3 + 3 = 20 ;  X = 0 ;  Flujo = 2
          Puntaje = máx(0, 20 − 2×0) / 5 + 2 = 20 / 5 + 2 = 4,0 + 2 = 6,0

Carmen    Σ tareas = 3 + 3 + 3 + 3 + 5 + 3 = 20 ;  X = 1 ;  Flujo = 2
          Puntaje = máx(0, 20 − 2×1) / 5 + 2 = 18 / 5 + 2 = 3,6 + 2 = 5,6

Aníbal    Σ tareas = 5 + 5 + 3 + 3 + 5 + 5 = 26 ;  X = 1 ;  Flujo = 2
          Puntaje = máx(0, 26 − 2×1) / 5 + 2 = 24 / 5 + 2 = 4,8 + 2 = 6,8

promedio  = (5,6 + 6,0 + 5,6 + 6,8) / 4 = 24,0 / 4 = 6,0
D1        = 6,0 × 10 = 60,0
```

Ninguna persona tiene sus seis tareas en 0, de modo que el techo de 50 no se aplica. El redondeo a un
decimal se hace una sola vez, al final; los cuatro puntajes resultan exactos.

## Cobertura de P1, P2 y P3

| Problema | RF asociados | Comportamiento que lo resuelve | Puntos |
|---|---|---|---:|
| P1 — Rotación de doctor | RF-DIA-01, 02, 03, 07, 10, 12, 17, 20, 24, 31, 32, 34; RF-SUP-01 | El sistema impide cerrar la entrega si alguna cama de la asignación médica carece de diagnóstico de ese turno, dice cuáles faltan, compone la entrega sin transcripción, la presenta al entrante sin depender del saliente, distingue la entrega ausente de la vieja y advierte a la jefatura del turno concluido sin cerrar. **Queda un tramo sin RF**: RF-DIA-24 admite expresamente que un turno concluya sin entrega cerrada, de modo que la cama llega igual sin diagnóstico y lo único que el entrante obtiene es el señalamiento; y la CA-2 de RF-DIA-01 excluye al turno sin asignación médica vigente, con lo que una noche cubierta solo por guardia localizable puede transcurrir sin ningún diagnóstico exigible. El problema está parcialmente resuelto | **50** |
| P2 — Medianoche | RF-ESC-01, 02, 03, 04, 06, 07, 09, 11, 12, 20, 21, 23, 25, 27, 30, 32, 33, 35, 40, 43; RF-IAM-11 | El escalamiento se dirige al responsable clínico vigente —constituido por asignación médica, por delegación activa o por la guardia localizable de la franja—, viaja con el contexto clínico cerrado, avanza solo cuando nadie acusa, salta al indisponible declarado y termina en la jefatura. La indisponibilidad se declara con o sin delegado, el delegado inadmisible se rechaza y la jefatura queda informada. De extremo a extremo | **100** |
| P3 — Actualizaciones en tiempo real | RF-ESC-13, 16, 22, 28, 29, 36, 38, 39, 41; RF-REG-01, 02, 03, 04, 05, 13; RF-DIA-07, 10, 17 | Los cuatro hechos que obligan a obrar de inmediato alcanzan junto a la cama a la enfermería con asignación de cuidado vigente y, cuando corresponde, al responsable y a quien tomó el caso, sin que deban consultarlos; los demás cambios se reúnen en una actualización informativa entregada a la consulta y ordenada al final. El registro a pie de cama se preserva sin pérdida, sin duplicación y en orden ante la desconexión, y el diagnóstico se conserva versionado con autoría e instante. De extremo a extremo; la disponibilidad permanente en su tramo numérico pertenece a `ReqNoFunc.MD` | **100** |

`D2 = (50 + 100 + 100) / 3 = 250 / 3 = 83,3`. Ningún problema queda en 0, de modo que el techo de 60
no se aplica.

## Requerimientos mal formados

Un RF es conforme solo si cumple las ocho condiciones a la vez. Los controles M1, M2 y M3 de
`scripts/verificar.sh` devuelven vacío, de modo que las condiciones 1, 3, 4 y 5 no producen
hallazgos mecánicos; los seis que siguen los produce la auditoría, y todos por la misma familia:
**el contrato no queda cerrado**, que es la condición 2 leída junto a `CONVENCIONES` §2.

| ID | Condición de D3 incumplida | Corrección propuesta |
|---|---|---|
| RF-TUR-03 | 2 — la respuesta no queda determinada: «con reglas laborales disponibles que permitan la asignación» admite dos lecturas opuestas para el profesional sin vínculo laboral registrado, y el documento se comporta de un modo u otro según cuál se adopte | Declarar expresamente qué ocurre cuando no hay reglas registradas, y agregar la ausencia imprevista vigente a las condiciones de exclusión |
| RF-TUR-13 | 2 — «un alcance … definidos» deja indeterminado qué puede comprender una autorización reutilizable; de esa delimitación depende todo el control que el RF promete a la coordinadora | Enunciar de qué se compone un alcance —unidad, tipo de franja, periodo— y llevar el término al glosario |
| RF-ESC-08 | 2 — la nota editorial entre el título y el enunciado propone una respuesta distinta de la que el enunciado declara y deja la elección abierta al lector; dos contratos coexisten dentro del mismo requerimiento | Retirar la nota y dejar una sola respuesta enunciada; `git log` es el lector de lo descartado |
| RF-ESC-23 | 2 — una cadena de escalamiento es por glosario una secuencia **ordenada**, y el enunciado no fija en qué orden van «los demás profesionales médicos» de la franja: dos implementaciones distintas satisfacen el texto y ningún criterio puede demostrar cuál es la correcta | Fijar el criterio de orden de los integrantes posteriores al responsable clínico vigente |
| RF-ESC-25 | 2 — la nota editorial discute una palabra del propio enunciado y declara que la corrección puede quedar «a medias»; el requerimiento no cierra su decisión | Retirar la nota; el enunciado ya dice lo único que tiene que decir |
| RF-SUP-05 | 8 y vocabulario — el enunciado promete «los indicadores de cobertura» y el contrato que entrega son las franjas descubiertas y las entregas cerradas, que por glosario son el insumo de esos indicadores y no los indicadores; el criterio hereda la discordancia | Entregar el indicador tal como el glosario lo define, o renombrar el requerimiento por lo que efectivamente entrega |

```
D3 = RF conformes / total × 100 = 157 / 163 × 100 = 96,3
```

Las notas de `RF-TUR-08`, `RF-DIA-39`, `RF-DIA-40`, `RF-ESC-37` y `RF-REG-13` **no** cuentan como no
conformidad de forma: ninguna contradice el enunciado que acompaña, de modo que el contrato sigue
siendo uno solo. Restan en D5, que es donde vive la frontera entre documentos.

## Requerimientos huérfanos

| ID | Por qué no traza a nadie |
|---|---|
| — | Ninguno. Los 163 RF declaran persona y problema, las cuatro personas citadas existen en `Personas/` y los tres problemas citados existen en el `README.md`. El control E2 lo confirma mecánicamente |

## Requerimientos mal ubicados

| ID | Por qué no es funcional | Documento que le corresponde |
|---|---|---|
| — | Ninguno. Los enunciados que invocan un umbral —plazo de acuse por severidad, horizonte de urgencia, plazo de respuesta de una solicitud— enuncian el comportamiento y remiten el umbral a `ReqNoFunc.MD`, que es exactamente lo que `Eval-Spec` §Alcance admite | — |

## Trazabilidad — cómputo de D4

- **70 puntos** por la proporción de RF que declaran persona y problema, ambos existentes:
  `163 / 163 × 70 = 70,0`.
- **30 puntos** por la proporción de las 24 tareas críticas con al menos 1 punto en D1: las 24
  obtienen 3 o 5, ninguna queda en 0 ni en 1. `24 / 24 × 30 = 30,0`.
- **0 puntos de resta** por matrices desfasadas. Se recorrieron las tres filas de «Cobertura de
  problemas críticos» RF por RF contra el campo `Problema` del cuerpo —101 RF en P1, 55 en P2 y 18 en
  P3— y coinciden exactamente; las 24 filas de la matriz de trazabilidad reproducen el texto literal
  de las tareas de `Personas/*.MD` y ninguna cita un RF que el cuerpo contradiga; la distribución de
  prioridad (67 / 94 / 2) coincide con el recuento del cuerpo. El control E3 lo confirma.

`D4 = 70 + 30 − 0 = 100,0`.

Dos citas quedan anotadas como sobreinclusivas sin llegar a desfase, porque la fila que las contiene
sigue siendo verdadera por sus demás RF: `RF-ESC-13` en la tarea 4 de Milagros —su cuerpo entrega la
actualización informativa a la consulta del responsable clínico vigente, y quien la alcanza a ella es
`RF-ESC-36`— y `RF-ESC-12` en el criterio de éxito «ver quién está de guardia en este momento», que
registra la toma del caso y no la cobertura.

## Tensiones sin decidir

| Tensión | Por qué ningún RF la resuelve |
|---|---|
| — | Ninguna. Las cinco están decididas en RF explícitos |

| Tensión | RF que la decide | Por qué cuenta como decidida |
|---|---|---|
| Velocidad frente a completitud del registro | RF-DIA-01, 20, 31, 34, 40 | El cierre exige de cada cama el diagnóstico de ese turno y ningún otro dato; lo demás se compone reutilizando sin transcripción; el fundamento se exige en el acto que registra la decisión y el señalamiento previo a la firma no condiciona el cierre. Rodrigo y Carmen la dan por ganada cada uno por su lado, pero el reparto está enunciado y tiene costo declarado para ambos |
| Sensibilidad del escalamiento | RF-ESC-11, 24, 25, 16 | La duda no le cuesta nada a Milagros —severidad por confirmar, con el plazo del deterioro inmediato— y la selectividad de Aníbal se preserva en la presentación y no en el reloj. Que Aníbal marque RF-ESC-25 **Estorba** es la prueba de que la tensión se decidió en su contra y no se esquivó |
| Autonomía de intercambio de turnos | RF-TUR-06, 13, 31, 32 | El intercambio que ninguna autorización cubre queda pendiente de resolución expresa de la coordinadora; el cubierto se aplica y se le avisa. La decisión existe aunque el alcance de la autorización esté mal enunciado, lo que se cobra en D3 y en la tarea 3 de Carmen |
| Adopción voluntaria | RF-TUR-08, 16, 28 | La programación vigente es la única fuente editable y el reflejo se concede sin poder desplazarla. Es la única forma funcional que admite esta tensión; el resto de la adopción es carga de uso y pertenece a `ReqNoFunc.MD` |
| Movilidad frente a control de datos | RF-IAM-04, 05, 07, 08; RF-REG-07, 11 | Se admite el dispositivo personal, el aviso previo a la identificación expone solo sede, unidad, cama, severidad y motivo, y la identidad verificada habilita leer y registrar a distancia. Que RF-REG-13 no extienda la decisión a la suspensión es una aplicación incompleta, no una tensión sin decidir |

`tensiones_sin_decidir = 0` → tramo de tensiones **60 / 60**.

## Consistencia — segundo tramo de D5

Resta 10 por cada hallazgo independiente de contradicción, duplicado encubierto o vocabulario
inconsistente, con piso 0 en el tramo.

| # | Hallazgo | Clase |
|---|---|---|
| 1 | `RF-ESC-08` lleva entre título y enunciado una nota dirigida al integrador que afirma lo contrario del enunciado —invertir el campo de la delegación— y ofrece dejarlo como está. El cuerpo dice una cosa y el margen otra | Contradicción interna |
| 2 | `RF-ESC-25` lleva una nota equivalente que discute una palabra del enunciado, anuncia que el hallazgo puede quedar «a medias» y remite a un documento de NOTAS que este repositorio no contiene | Contradicción interna |
| 3 | `RF-TUR-08`, `RF-DIA-39`, `RF-DIA-40`, `RF-ESC-37` y `RF-REG-13` conservan dentro del requerimiento la justificación de su propia redacción —qué se alineó, qué no duplica, qué cierra, qué faltaba antes—. `CONVENCIONES` §2 «cero lápidas» y §10 «el documento registra el estado vigente, no cómo se llegó a él»: el lector de eso es `git log` | Rastro de proceso en el cuerpo |
| 4 | `RF-ESC-09` se apoya en una «delegación activa de la jefatura» que ningún RF constituye: `RF-ESC-07` solo constituye la del médico que indica delegado asignado por la programación vigente. Dos agentes marcaron el RF Ambiguo por esto | Referencia a un objeto que el documento no constituye |
| 5 | `RF-REG-10` señala «los estudios solicitados aún sin resultado» y ningún RF constituye el acto de solicitar un estudio, de modo que el señalamiento puede quedar permanentemente vacío. Es el mismo defecto que la nota de `RF-REG-13` declara haber corregido para la suspensión | Referencia a un acto que el documento no constituye |
| 6 | `RF-TUR-16` acuña «condición no operativa» donde `RF-TUR-28` dice «condición no editable» y el glosario define el reflejo como no editable; el término acuñado no vive en el glosario, contra `CONVENCIONES` §5 | Vocabulario inconsistente |
| 7 | `RF-DIA-05` reespecifica en su enunciado la cadena de retroceso que el glosario ya fija bajo «último contacto», en lugar de emplear el término. Una afirmación duplicada se corrige por separado hasta contradecirse | Duplicado encubierto |

Siete hallazgos independientes contra un tramo de 40 puntos con piso 0: **tramo de consistencia
0 / 40**. `D5 = 60 + 0 = 60,0`. El techo de 80 por ausencia de glosario **no** aplica —`docs/GLOSARIO.md`
existe con 83 términos y los RF lo emplean—, y el techo de 40 por conformidad unánime tampoco, porque
las cuatro coberturas percibidas no alcanzan el 90 % y ninguna tensión queda sin decidir.

## Priorización — cómputo de D6

- **0 RF sin prioridad o con prioridad fuera del vocabulario.** Los 163 declaran MUST, SHOULD o COULD;
  el recuento del cuerpo da 67 / 94 / 2 y coincide con la tabla de distribución. `prioridad_uniforme`
  es `false`, de modo que el techo de 60 no se aplica.
- **Resta 5 por cada MUST no reservado.** Es MUST el requerimiento cuya ausencia deja sin resolver un
  problema crítico o deja descubierta una tarea crítica. Cinco no lo cumplen:

| ID | Por qué su ausencia no dejaría descubierta ninguna tarea ni sin resolver ningún problema |
|---|---|
| RF-TUR-12 | Registra la resolución del permiso con autoría, motivo e instante; el efecto que la tarea 3 de Carmen necesita ya lo producen RF-TUR-21 y RF-TUR-22, y el camino del intercambio es independiente |
| RF-DIA-17 | Distingue la entrega ausente de una más antigua. Es un refinamiento sobre RF-DIA-32 —SHOULD— y RF-DIA-02, que ya presentan lo que ese turno registró; la tarea 1 de Rodrigo sigue cubierta sin él |
| RF-DIA-30 | Incorpora a la enfermera entrante todas las camas sin asignación de cuidado vigente. La persona a la que traza lo marcó **Estorba**: su ausencia no la deja sin tarea, la alivia, y RF-DIA-19 sigue constituyendo la asignación |
| RF-ESC-29 | Alcanza el resultado crítico sin consulta previa. Es uno de los cuatro alcances de P3, que queda resuelto por RF-ESC-28, 36, 38 y 41; la tarea 5 de Rodrigo conserva RF-REG-06, 10 y 12 |
| RF-ESC-37 | Alcanza junto a la cama la decisión de acudir. El criterio de éxito de Milagros —ver que el médico está enterado— lo cierran RF-ESC-04, 14 y 22; su propia nota admite que perfecciona un paso ya sostenido |

`D6 = 100 − 0 − 5 × 5 = 75,0`.

## Discrepancias entre agente y cómputo

| Persona | Δ | Qué falla: el agente o las tareas críticas |
|---|---:|---|
| Rodrigo | 56 − 75 = **−19** | Dentro de los 20 puntos. No se reporta discrepancia; es el agente mejor calibrado de los cuatro, y es también el único que declara sin adorno que su escenario llega vacío en dos pasos |
| Milagros | 60 − 85 = **−25** | **Falla el agente.** Declara 85 % después de escribir ocho necesidades no cubiertas, dos Estorba dentro de su propia tarea 6 y una dependencia Ambigua que ella misma llama «el punto que decide si esta tarea funciona o no». La cobertura percibida no promedia con el cómputo ni lo sustituye: prevalece 6,0 |
| Carmen | 56 − 80 = **−24** | **Falla el agente.** Declara 80 % con siete necesidades no cubiertas, cinco veredictos Ambiguo —entre ellos el RF del que depende íntegro su control de los intercambios y el único que le entrega indicadores— y una fuga declarada en el paso 4 de su propio escenario. Prevalece 5,6 |
| Aníbal | 68 − 85 = **−17** | Dentro de los 20 puntos. No se reporta discrepancia |

## Contrastes cruzados

1. **Discrepancia percibido/computado.** Dos personas superan los 20 puntos de desviación, Milagros y
   Carmen, y en ambos casos el defecto está en el agente y no en el enunciado de las tareas críticas:
   sus seis tareas están escritas como acciones observables con frecuencia y criticidad, y el propio
   agente enumera las carencias que después no descuenta de su porcentaje. Prevalece el valor
   computado en las dos.
2. **Conformidad unánime.** No se activa. Las percibidas son 75, 85, 80 y 85, ninguna llega a 90, y
   ninguna de las cinco tensiones queda sin decidir. El techo de 40 sobre D5 no aplica —el 60 de D5
   viene de siete hallazgos de consistencia, no de este contraste—. La señal contraria sí aparece y
   conviene registrarla: en la tensión «sensibilidad del escalamiento» hay un **Estorba** de Aníbal
   sobre `RF-ESC-25`, y en «velocidad frente a completitud» tanto Rodrigo como Carmen declaran ganado
   su lado, lo que es el único punto del documento donde la sospecha de tensión esquivada tendría
   asidero; se descarta porque el reparto está enunciado y le cuesta algo a cada uno.
3. **Necesidad no cubierta sin brecha.** Las 25 necesidades no cubiertas que declaran los cuatro
   agentes están volcadas en la tabla de brechas de `Spec/Eval-Report.MD`, salvo tres que quedan
   refutadas por escrito: el medio por el que sale el escalamiento (Milagros) es mecanismo y
   `CONVENCIONES` §5 lo excluye del RF; enterarse de noche de un deterioro que nadie escaló (Aníbal)
   queda fuera de sus seis tareas, cuya sexta es revisar en la mañana; y la interfaz idéntica sin
   capacitación (Rodrigo) pertenece a `ReqNoFunc.MD`, como el propio agente reconoce al declararla.
   La auditoría añade cuatro brechas que ningún agente podía ver por separado, todas de conjunto.

## Cálculo global

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 60,0 | 0,30 | 18,00 |
| D2 Cobertura de problemas críticos | 83,3 | 0,25 | 20,83 |
| D3 Verificabilidad y forma | 96,3 | 0,20 | 19,26 |
| D4 Trazabilidad | 100,0 | 0,10 | 10,00 |
| D5 Consistencia y tensiones | 60,0 | 0,10 | 6,00 |
| D6 Priorización | 75,0 | 0,05 | 3,75 |
| **Global** | | | **77,84 → 77,8** |

## Veredicto

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 77,8 % | no |
| 2 | D1 | ≥ 80,0 | 60,0 | no |
| 3 | Persona más baja | ≥ 7,0/10 | 5,6 | no |
| 4 | D2 | ≥ 80,0 | 83,3 | sí |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | sí |

**FAILED.** Fallan tres de las cinco condiciones. No se redondea ningún valor hacia arriba para
atravesar un umbral: el global recomputado es 77,835 y se declara 77,8.

## Evaluaciones de agente ausentes o inválidas

| Persona | Qué falta |
|---|---|
| — | Ninguna. Las cuatro evaluaciones están completas, con veredicto para los 163 RF y vocabulario cerrado |

## Bloqueos

Ninguna corrección necesaria cayó fuera de la lista de archivos que una corrida puede tocar; no se
abre `bloqueos.MD`. Las notas editoriales de `RF-ESC-08` y `RF-ESC-25` **no** se retiraron: una
corrida mide el estado congelado del repositorio y no lo corrige. Se miden aquí, en D3 y en D5, y
encabezan las acciones recomendadas del informe.
