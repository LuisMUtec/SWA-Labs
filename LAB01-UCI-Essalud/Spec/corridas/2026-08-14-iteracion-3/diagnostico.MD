# Diagnóstico — corrida 2026-08-14-iteracion-3

Evidencia de la agregación. Rúbrica aplicada: `Spec/Eval-Spec.MD` @ `b492237`.
Evaluado: `Requirements/ReqFunc.MD` @ `f50cf90`. Personas @ `6340172`. Agentes @ `34877c7`.

Las cuatro evaluaciones de persona son insumo inmutable y viven junto a este documento. Este
diagnóstico no las reinterpreta: las cruza con la matriz de trazabilidad de `ReqFunc.MD` y con las
escalas de la rúbrica.

---

## Criterio de lectura aplicado

Dos decisiones de método gobiernan todo lo que sigue. Se declaran antes de los números para que el
lector pueda recomputar con otra lectura si la considera mejor fundada.

1. **La traza RF → tarea crítica sale de la «Matriz de trazabilidad» de `ReqFunc.MD`**, no del relato
   del agente. Es la fuente que el paso 2 del procedimiento de agregación nombra, y es la única
   reproducible: un RF traza a una tarea si figura en la fila de esa tarea. Esto gobierna tanto la
   matriz de cobertura como el cómputo de `X_p`.
2. **Escala de puntos aplicada de forma uniforme a las 24 tareas:**
   - **5** cuando el agente no declara ninguna carencia sobre la tarea;
   - **3** cuando el agente declara comportamiento o criterio de éxito faltante, pero los verbos
     propios de la tarea están declarados por RF que él marcó *Sirve*;
   - **1** cuando los RF que cargan los verbos de la tarea son *Ambiguo*, o cuando la cobertura se
     apoya en una capacidad que ningún enunciado declara;
   - **0** cuando ningún RF la traza o el único que la traza recibió *Estorba*.

Ante la duda se penaliza. Un agente puede bajar D1, nunca subirla: donde el agente declaró una grieta,
la grieta se computa; donde declaró satisfacción, se verificó contra el enunciado antes de aceptarla.

---

## Veredictos agregados

Los 81 RF por las cuatro personas. La columna **Efecto en D1** usa la notación `‹inicial de la
persona›T‹n›` para «traza a la tarea *n* de esa persona» y `X_‹inicial› −2` para «Estorba fuera de sus
seis tareas». `—` significa que el RF no interviene en ninguna tarea crítica ni en ningún `X_p`.

| RF | Rodrigo | Milagros | Carmen | Aníbal | Efecto en D1 |
|---|---|---|---|---|---|
| RF-TUR-01 | Indiferente | Indiferente | Sirve | Ambiguo | CT2 |
| RF-TUR-02 | Indiferente | Indiferente | Sirve | Indiferente | CT2 |
| RF-TUR-03 | Indiferente | Indiferente | Sirve | Indiferente | CT4 |
| RF-TUR-04 | Indiferente | Sirve | Sirve | Sirve | CT1 |
| RF-TUR-05 | Sirve | Indiferente | Sirve | Sirve | CT4 |
| RF-TUR-06 | Sirve | Indiferente | Estorba | Indiferente | CT3 |
| RF-TUR-07 | Indiferente | Indiferente | Sirve | Indiferente | CT2 |
| RF-TUR-08 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-TUR-09 | Indiferente | Indiferente | Ambiguo | Indiferente | CT1 |
| RF-TUR-10 | Indiferente | Indiferente | Ambiguo | Indiferente | CT1 |
| RF-TUR-11 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-12 | Indiferente | Indiferente | Sirve | Indiferente | CT3 |
| RF-TUR-13 | Sirve | Indiferente | Sirve | Indiferente | CT3 |
| RF-TUR-14 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-15 | Indiferente | Estorba | Sirve | Indiferente | X_M −2 |
| RF-TUR-16 | Indiferente | Indiferente | Estorba | Indiferente | X_C −2 |
| RF-TUR-17 | Indiferente | Indiferente | Sirve | Indiferente | CT3 |
| RF-TUR-18 | Indiferente | Indiferente | Sirve | Indiferente | CT4 |
| RF-TUR-19 | Indiferente | Indiferente | Sirve | Indiferente | CT4 |
| RF-TUR-20 | Indiferente | Indiferente | Sirve | Indiferente | CT4 |
| RF-TUR-21 | Indiferente | Indiferente | Ambiguo | Indiferente | — |
| RF-TUR-22 | Indiferente | Indiferente | Ambiguo | Indiferente | — |
| RF-TUR-23 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-24 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-25 | Indiferente | Indiferente | Ambiguo | Indiferente | CT4 |
| RF-TUR-26 | Indiferente | Indiferente | Ambiguo | Indiferente | CT4 |
| RF-DIA-01 | Sirve | Indiferente | Sirve | Ambiguo | RT6 |
| RF-DIA-02 | Sirve | Indiferente | Sirve | Indiferente | RT1/T2 |
| RF-DIA-03 | Sirve | Indiferente | Sirve | Indiferente | RT1 |
| RF-DIA-04 | Sirve | Indiferente | Sirve | Indiferente | RT6 |
| RF-DIA-05 | Sirve | Indiferente | Indiferente | Sirve | RT2 |
| RF-DIA-06 | Sirve | Ambiguo | Indiferente | Indiferente | RT4 |
| RF-DIA-07 | Sirve | Indiferente | Sirve | Sirve | RT2/T3 |
| RF-DIA-08 | Indiferente | Sirve | Indiferente | Indiferente | MT6 |
| RF-DIA-09 | Sirve | Indiferente | Sirve | Indiferente | RT1 |
| RF-DIA-10 | Sirve | Indiferente | Sirve | Indiferente | RT1/T2 |
| RF-DIA-11 | Indiferente | Sirve | Indiferente | Indiferente | MT6 |
| RF-DIA-12 | Sirve | Indiferente | Sirve | Indiferente | RT6; CT5 |
| RF-DIA-13 | Sirve | Indiferente | Indiferente | Sirve | RT2/T3 |
| RF-DIA-14 | Sirve | Indiferente | Indiferente | Sirve | RT2/T3 |
| RF-DIA-15 | Sirve | Indiferente | Indiferente | Indiferente | RT2/T3 |
| RF-DIA-16 | Sirve | Indiferente | Indiferente | Indiferente | RT3 |
| RF-DIA-17 | Sirve | Indiferente | Sirve | Indiferente | RT1 |
| RF-ESC-01 | Indiferente | Sirve | Indiferente | Sirve | MT2 |
| RF-ESC-02 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-03 | Sirve | Ambiguo | Indiferente | Sirve | AT1 |
| RF-ESC-04 | Indiferente | Sirve | Indiferente | Sirve | AT2 |
| RF-ESC-05 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-06 | Indiferente | Sirve | Indiferente | Sirve | MT2 |
| RF-ESC-07 | Indiferente | Sirve | Estorba | Sirve | X_C −2; AT5 |
| RF-ESC-08 | Indiferente | Sirve | Indiferente | Sirve | MT3 |
| RF-ESC-09 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-10 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-ESC-11 | Indiferente | Sirve | Indiferente | Estorba | MT2; X_A −2 |
| RF-ESC-12 | Indiferente | Sirve | Indiferente | Sirve | AT2 |
| RF-ESC-13 | Ambiguo | Sirve | Indiferente | Ambiguo | — |
| RF-ESC-14 | Indiferente | Sirve | Indiferente | Sirve | AT2 |
| RF-ESC-15 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-16 | Sirve | Estorba | Indiferente | Sirve | X_M −2; AT1 |
| RF-ESC-17 | Indiferente | Sirve | Indiferente | Sirve | AT5 |
| RF-ESC-18 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-19 | Indiferente | Sirve | Indiferente | Sirve | AT2 |
| RF-REG-01 | Indiferente | Sirve | Indiferente | Sirve | MT1 |
| RF-REG-02 | Indiferente | Sirve | Indiferente | Sirve | MT1 |
| RF-REG-03 | Sirve | Sirve | Indiferente | Sirve | MT4 |
| RF-REG-04 | Indiferente | Sirve | Indiferente | Indiferente | MT4 |
| RF-REG-05 | Indiferente | Sirve | Indiferente | Sirve | MT5 |
| RF-REG-06 | Sirve | Indiferente | Indiferente | Sirve | RT5 |
| RF-REG-07 | Indiferente | Sirve | Indiferente | Sirve | AT4 |
| RF-REG-08 | Sirve | Indiferente | Indiferente | Sirve | AT3 |
| RF-IAM-01 | Ambiguo | Sirve | Sirve | Sirve | RT3 |
| RF-IAM-02 | Estorba | Ambiguo | Indiferente | Ambiguo | X_R −2; AT4 |
| RF-IAM-03 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-IAM-04 | Indiferente | Indiferente | Indiferente | Ambiguo | AT1 |
| RF-IAM-05 | Indiferente | Sirve | Indiferente | Sirve | AT1/T4 |
| RF-IAM-06 | Sirve | Sirve | Sirve | Indiferente | — |
| RF-IAM-07 | Indiferente | Estorba | Indiferente | Ambiguo | X_M −2; AT1/T4 |
| RF-SUP-01 | Indiferente | Ambiguo | Sirve | Indiferente | CT5 |
| RF-SUP-02 | Indiferente | Indiferente | Sirve | Indiferente | CT6 |
| RF-SUP-03 | Sirve | Sirve | Indiferente | Sirve | AT6 |
| RF-SUP-04 | Indiferente | Sirve | Sirve | Indiferente | — |

**Recuento por persona:** Rodrigo 25 Sirve / 53 Indiferente / 1 Estorba / 2 Ambiguo · Milagros
31 / 43 / 3 / 4 · Carmen 35 / 37 / 3 / 6 · Aníbal 33 / 41 / 1 / 6. Los cuatro emitieron veredicto para
los 81 RF con vocabulario cerrado.

**Dato que la tabla deja ver y ninguna evaluación individual podía ver:** 24 de los 81 RF no
intervienen en ninguna tarea crítica de ninguna persona (columna `—`). Diecisiete de esos 24 son MUST.
No son huérfanos —todos declaran persona y problema— pero sostienen la programación como aparato
administrativo, no como cobertura de una tarea declarada.

---

## Matriz de cobertura

Veinticuatro filas: seis tareas críticas por persona, textuales de `Personas/*.MD`. La columna
**Veredicto** es el del agente de esa persona sobre los RF de la fila de la matriz de trazabilidad de
`ReqFunc.MD`.

| Persona | Tarea crítica | RF que la cubre | Veredicto | Puntos | Estado |
|---|---|---|---:|---:|---|
| Rodrigo | 1. Recibir el handoff estructurado de todas las camas asignadas | RF-DIA-02, RF-DIA-03, RF-DIA-09, RF-DIA-10, RF-DIA-17 | 5 × Sirve | 3 | Incompleta |
| Rodrigo | 2. Consultar la evolución y el diagnóstico del turno anterior | RF-DIA-02, RF-DIA-05, RF-DIA-07, RF-DIA-10, RF-DIA-13, RF-DIA-14, RF-DIA-15 | 7 × Sirve | 3 | Incompleta |
| Rodrigo | 3. Registrar nota de evolución y diagnóstico por paciente | RF-DIA-07, RF-DIA-13, RF-DIA-14, RF-DIA-15, RF-DIA-16, RF-IAM-01 | 5 × Sirve, 1 × Ambiguo | 3 | Incompleta |
| Rodrigo | 4. Marcar pacientes inestables o con pendientes críticos | RF-DIA-06 | Sirve | 3 | Incompleta |
| Rodrigo | 5. Consultar resultados de laboratorio e imágenes | RF-REG-06 | Sirve | 5 | Cubierta |
| Rodrigo | 6. Cerrar y firmar la entrega de turno | RF-DIA-01, RF-DIA-04, RF-DIA-12 | 3 × Sirve | 3 | Incompleta |
| Milagros | 1. Registrar signos vitales y balance por paciente | RF-REG-01, RF-REG-02 | 2 × Sirve | 3 | Incompleta |
| Milagros | 2. Escalar un deterioro clínico al médico responsable | RF-ESC-01, RF-ESC-06, RF-ESC-11 | 3 × Sirve | 3 | Incompleta |
| Milagros | 3. Consultar quién está de guardia y su estado de disponibilidad | RF-ESC-08 | Sirve | 3 | Incompleta |
| Milagros | 4. Ver y confirmar indicaciones médicas vigentes | RF-REG-03, RF-REG-04 | 2 × Sirve | 3 | Incompleta |
| Milagros | 5. Registrar eventos y administración de medicamentos | RF-REG-05 | Sirve | 3 | Incompleta |
| Milagros | 6. Recibir y entregar el turno de enfermería | RF-DIA-08, RF-DIA-11 | 2 × Sirve | 1 | Aparente |
| Carmen | 1. Elaborar y publicar la programación mensual de turnos | RF-TUR-04, RF-TUR-09, RF-TUR-10 | 1 × Sirve, 2 × Ambiguo | 1 | Aparente |
| Carmen | 2. Validar que no existan cruces ni franjas descubiertas | RF-TUR-01, RF-TUR-02, RF-TUR-07 | 3 × Sirve | 3 | Incompleta |
| Carmen | 3. Aprobar o rechazar intercambios y permisos | RF-TUR-06, RF-TUR-12, RF-TUR-13, RF-TUR-17 | 3 × Sirve, 1 × Estorba | 1 | Aparente |
| Carmen | 4. Reasignar cobertura ante una ausencia imprevista | RF-TUR-03, RF-TUR-05, RF-TUR-18, RF-TUR-19, RF-TUR-20, RF-TUR-25, RF-TUR-26 | 5 × Sirve, 2 × Ambiguo | 3 | Incompleta |
| Carmen | 5. Monitorear cumplimiento y completitud de entregas de turno | RF-DIA-12, RF-SUP-01 | 2 × Sirve | 3 | Incompleta |
| Carmen | 6. Generar indicadores de cobertura para la Dirección de Red | RF-SUP-02 | Sirve | 3 | Incompleta |
| Aníbal | 1. Recibir la alerta de escalamiento con contexto clínico adjunto | RF-ESC-03, RF-ESC-16, RF-IAM-04, RF-IAM-05, RF-IAM-07 | 3 × Sirve, 2 × Ambiguo | 3 | Incompleta |
| Aníbal | 2. Confirmar recepción y tomar el caso | RF-ESC-04, RF-ESC-12, RF-ESC-14, RF-ESC-19 | 4 × Sirve | 5 | Cubierta |
| Aníbal | 3. Consultar tendencia de signos, ventilación y última evolución | RF-REG-08 | Sirve | 3 | Incompleta |
| Aníbal | 4. Registrar la indicación dada de forma remota | RF-REG-07, RF-IAM-02, RF-IAM-05, RF-IAM-07 | 2 × Sirve, 2 × Ambiguo | 3 | Incompleta |
| Aníbal | 5. Marcarse temporalmente indisponible y delegar | RF-ESC-07, RF-ESC-17 | 2 × Sirve | 5 | Cubierta |
| Aníbal | 6. Revisar en la mañana lo ocurrido durante la noche | RF-SUP-03 | Sirve | 3 | Incompleta |

**Ninguna tarea quedó en 0.** Las 24 trazan a al menos un RF y ninguna depende de un único RF marcado
*Estorba*. `tareas_en_cero = 0` para las cuatro personas, de modo que el techo «D1 ≤ 50 si una persona
tiene sus seis tareas en 0» no se activa.

### Por qué cada tarea no llegó a 5

| Tarea | Carencia que impide el 5 | Declarada por |
|---|---|---|
| Rodrigo 1 | Ningún RF declara el acto por el que las camas quedan asignadas al médico; RF-DIA-02 y RF-DIA-10 arrancan de «cada cama asignada» y dan ese estado por existente | veredicto-rodrigo |
| Rodrigo 2 | RF-DIA-05 solo cubre camas con registro propio previo; en una rotación son la minoría, y su criterio «ver qué cambió» queda sin respuesta para el resto | veredicto-rodrigo |
| Rodrigo 3 | RF-IAM-01 (Ambiguo) no declara la atribución en PC compartida con sesión ajena abierta, que es su restricción más dura | veredicto-rodrigo |
| Rodrigo 4 | RF-DIA-06 ancla la marca a la entrega de turno; ningún RF declara una vista de las camas marcadas durante las doce horas, y la tarea es continua | veredicto-rodrigo |
| Rodrigo 5 | — | — |
| Rodrigo 6 | El bloqueo de RF-DIA-01 impide cerrar pero no produce el diagnóstico ausente; ningún RF declara qué ocurre cuando el turno termina bloqueado | veredicto-rodrigo |
| Milagros 1 | RF-IAM-02 puede rechazar su registro sobre camas que cubre de hecho; ningún RF declara quién crea la asignación de cuidado de enfermería | veredicto-milagros |
| Milagros 2 | Ningún RF declara desde dónde emite el escalamiento; RF-ESC-03 exige un bloque de contexto sin declarar qué ocurre si falta un dato | veredicto-milagros |
| Milagros 3 | El estado «disponible» de RF-ESC-08 no refleja al médico ocupado en otro servicio sin caso abierto registrado, que es su escenario literal | veredicto-milagros |
| Milagros 4 | Ningún RF le avisa de una indicación nueva: RF-ESC-13 no la incluye en su lista de disparadores | veredicto-milagros |
| Milagros 5 | Mismo rechazo de RF-IAM-02 sobre camas cubiertas sin asignación formal | veredicto-milagros |
| Milagros 6 | RF-DIA-08 y RF-DIA-11 consumen «pendientes de cuidado abiertos» que ningún RF declara cómo se abren o cierran; la entrega no incluye signos vitales ni balance y no tiene cierre ni firma | veredicto-milagros |
| Carmen 1 | RF-TUR-09 y RF-TUR-10 —los dos verbos de la tarea— quedaron Ambiguo, y ningún RF declara que alguien consulte la programación vigente | veredicto-carmen |
| Carmen 2 | RF-TUR-22 admite leerse como que el retiro por permiso ocurre al comenzar la vigencia: la franja aparece descubierta con el turno ya empezado | veredicto-carmen |
| Carmen 3 | Ningún RF declara la presentación de una solicitud ni una bandeja de pendientes: resuelve algo cuya llegada el documento no describe. RF-TUR-06 (Estorba) aplica el intercambio sin su resolución y sin avisarle | veredicto-carmen |
| Carmen 4 | Ningún RF declara que el candidato acepte antes de quedar asignado; RF-TUR-25 y RF-TUR-26 descansan en un «cambio urgente» que nadie define | veredicto-carmen |
| Carmen 5 | Solo el diagnóstico bloquea el cierre: una entrega sin decisión fundamentada, sin esquema y sin estado de familia figura como cumplida en su reporte | veredicto-carmen |
| Carmen 6 | RF-SUP-02 declara que el sistema produce los indicadores, no que ella pueda llevárselos en un formato entregable a la Dirección | veredicto-carmen |
| Aníbal 1 | RF-IAM-04 solo gobierna el caso sin identidad verificada, que no es su estado habitual; su restricción de pantalla de bloqueo queda sin RF | veredicto-anibal |
| Aníbal 2 | — | — |
| Aníbal 3 | RF-REG-08 no incluye balance hídrico, lactato ni dosis de vasopresor, que sí están en RF-ESC-03: fuera de un escalamiento le faltan tres de las seis cosas que pregunta | veredicto-anibal |
| Aníbal 4 | RF-REG-07 nombra al responsable vigente y al delegado, no al integrante que llega por avance de cadena; RF-IAM-02 (Ambiguo) puede rechazarle el registro en esa noche | veredicto-anibal |
| Aníbal 5 | — | — |
| Aníbal 6 | RF-SUP-03 está enunciado por unidad y él cubre dos sedes: su «un solo lugar» son dos consultas | veredicto-anibal |

---

## Daño fuera de tarea — `X_p`

`X_p` cuenta los RF marcados **Estorba** por esa persona que no figuran en ninguna de las seis filas de
su matriz de trazabilidad. Los ocho veredictos *Estorba* del conjunto, uno por uno:

| RF | Persona que lo marca | ¿Traza a alguna de sus seis tareas? | ¿Cuenta en `X_p`? |
|---|---|---|---|
| RF-IAM-02 | Rodrigo | No figura en ninguna fila de Rodrigo (aparece en Aníbal 4) | **Sí** — X_Rodrigo |
| RF-TUR-15 | Milagros | No figura en ninguna fila de la matriz, de ninguna persona | **Sí** — X_Milagros |
| RF-ESC-16 | Milagros | No figura en ninguna fila de Milagros (aparece en Aníbal 1) | **Sí** — X_Milagros |
| RF-IAM-07 | Milagros | No figura en ninguna fila de Milagros (aparece en Aníbal 1 y 4) | **Sí** — X_Milagros |
| RF-TUR-06 | Carmen | **Sí**: fila «Aprobar o rechazar intercambios y permisos» | No — su daño ya está descontado dentro de la tarea 3, puntuada 1 |
| RF-TUR-16 | Carmen | No figura en ninguna fila de Carmen | **Sí** — X_Carmen |
| RF-ESC-07 | Carmen | No figura en ninguna fila de Carmen (aparece en Aníbal 5) | **Sí** — X_Carmen |
| RF-ESC-11 | Aníbal | No figura en ninguna fila de Aníbal (aparece en Milagros 2) | **Sí** — X_Aníbal |

`X_Rodrigo = 1` · `X_Milagros = 3` · `X_Carmen = 2` · `X_Aníbal = 1`.

Tres de estos siete —RF-IAM-02 para Rodrigo, RF-ESC-16 para Milagros, RF-ESC-11 para Aníbal— fueron
además invocados por el propio agente dentro del análisis de una tarea, aunque la matriz de
`ReqFunc.MD` no los liste allí. Bajo la lectura alternativa —contar la traza que el agente declara en
su relato y no la que la matriz publica— `X_Rodrigo = 0`, `X_Milagros = 2`, `X_Aníbal = 0`, y D1
subiría de 29,0 a 32,0. Se adopta la lectura de la matriz por ser la fuente que el procedimiento
nombra y la única reproducible; ninguna de las dos lecturas altera el veredicto.

---

## Recorrido del escenario clave y claridad del flujo

Se recorrió el escenario de cada persona contra los RF, tomando como punto de partida el recorrido que
el agente declaró. Los cuatro recorridos llegan lejos —el tramo medio del escalamiento y el contenido
de la entrega médica están encadenados— y los cuatro se apoyan en al menos un paso que ningún
enunciado sostiene.

| Persona | Paso exacto que ningún RF sostiene | Verificación contra el enunciado | Flujo |
|---|---|---|---:|
| Rodrigo | Paso 9 — 23:40, la cama 6 se descompensa y necesita el esquema con su día, la decisión con su fundamento y el estado de la familia | RF-DIA-02 dispara al **iniciar el turno**; RF-REG-08 entrega tendencia, ventilatorios y última evolución, no la decisión fundamentada ni el esquema con su día; RF-DIA-05 exige registro propio previo; RF-ESC-03 solo actúa si alguien escala. **Confirmado: no hay consulta a demanda de ese bloque** | **0** |
| Milagros | Paso 2 — decide y emite el escalamiento; y paso 12 — la indicación remota llega sin aviso | Ningún RF declara el acto de emisión ni desde qué dispositivo; RF-ESC-01 lo toma como disparador ya ocurrido. RF-ESC-13 enumera deterioro, cambio de soporte, resultado crítico y traslado: la indicación nueva no está. **Confirmado** | **0** |
| Carmen | Paso 5 — asigna al reemplazo y sigue llamando por teléfono para saber si vendrá; y el cierre, sin rol vigente consultable ni copia imprimible del mes en curso | Entre RF-TUR-03 y RF-TUR-20 no hay ningún enunciado de aceptación del candidato; RF-TUR-16 solo cubre periodos cerrados y ningún RF declara la consulta del rol vigente. **Confirmado** | **0** |
| Aníbal | Paso 10 — quiere saber si la indicación que dio a distancia fue ejecutada | RF-REG-04 registra la confirmación de la enfermera y ningún enunciado la devuelve a quien indicó. **Confirmado: el ciclo de la indicación remota queda abierto** | **0** |

Los apoyos en *Ambiguo* —RF-IAM-01 en el paso 10 de Rodrigo, RF-ESC-03 en el paso 4 de Milagros,
RF-TUR-21 y RF-TUR-25/26 en Carmen, RF-IAM-04 y RF-IAM-07 en Aníbal— habrían bastado por sí solos para
bajar el flujo a 2. La interrupción los subsume: la escala no acumula.

---

## Aritmética de D1

```
Rodrigo   tareas = 3+3+3+3+5+3 = 20    X = 1
          máx(0, 20 − 2×1)/5 + 0 = 18/5 + 0 = 3,6 + 0 = 3,6

Milagros  tareas = 3+3+3+3+3+1 = 16    X = 3
          máx(0, 16 − 2×3)/5 + 0 = 10/5 + 0 = 2,0 + 0 = 2,0

Carmen    tareas = 1+3+1+3+3+3 = 14    X = 2
          máx(0, 14 − 2×2)/5 + 0 = 10/5 + 0 = 2,0 + 0 = 2,0

Aníbal    tareas = 3+5+3+3+5+3 = 22    X = 1
          máx(0, 22 − 2×1)/5 + 0 = 20/5 + 0 = 4,0 + 0 = 4,0

promedio  = (3,6 + 2,0 + 2,0 + 4,0) / 4 = 11,6 / 4 = 2,9
D1        = 2,9 × 10 = 29,0
```

El redondeo a un decimal se aplicó una sola vez, al cierre de cada puntaje individual; los cuatro
resultaron exactos.

---

## Cobertura de P1, P2 y P3

| Problema | RF asociados | Comportamiento que lo resuelve | Tramo sin RF | Puntos |
|---|---|---|---|---:|
| **P1 — Rotación de doctor**: el diagnóstico del médico previo debe estar disponible antes del cambio de turno | RF-DIA-01, RF-DIA-02, RF-DIA-03, RF-DIA-04, RF-DIA-07, RF-DIA-09, RF-DIA-10, RF-DIA-12, RF-DIA-17 | El diagnóstico se registra versionado con autoría (RF-DIA-07); su ausencia bloquea el cierre (RF-DIA-01) y el bloqueo se explica cama por cama (RF-DIA-12); la entrega se presenta al entrante sin depender del saliente (RF-DIA-10) con contenido fijado (RF-DIA-02); la cama sin diagnóstico se señala antes de aceptar (RF-DIA-03) y la entrega ausente se distingue de una vieja (RF-DIA-17) | **Ningún RF declara qué acto produce una «entrega confirmada»**, que es la condición de la que dependen RF-DIA-10 y RF-DIA-17; ni **cómo quedan asignadas las camas a un médico**, presupuesto de RF-DIA-01, RF-DIA-02 y RF-DIA-10. Y el bloqueo de RF-DIA-01 no produce el diagnóstico que falta: el turno puede terminar igual, con el entrante recibiendo «entrega ausente» | **50** |
| **P2 — Medianoche**: contactar rápido al médico encargado y manejar su indisponibilidad | RF-ESC-01 a RF-ESC-19, RF-REG-07, RF-REG-08, RF-IAM-02, RF-IAM-04, RF-IAM-05, RF-IAM-07, RF-SUP-03, RF-SUP-04 | El aviso alcanza al responsable vigente y no al del rol impreso (RF-ESC-01); sin acuse avanza solo (RF-ESC-02), llega a la jefatura al agotarse (RF-ESC-09) y queda registrado (RF-ESC-18); la indisponibilidad se declara con delegado y vencimiento (RF-ESC-07, RF-ESC-17); el contexto va adjunto (RF-ESC-03) y la indicación remota se registra con autoría (RF-REG-07) | **Ningún RF declara el acto de emisión del escalamiento** —desde qué dispositivo, con qué disparador— ni **qué ocurre con un escalamiento emitido sin conexión**, en una unidad cuyo WiFi es intermitente y sin soporte de TI de noche. **RF-IAM-07 impide el contexto sin identidad verificada vigente y ningún RF declara cómo se recupera esa identidad a las 03:20**: el flujo vuelve al teléfono, que es la falla que P2 nombra | **50** |
| **P3 — Actualizaciones en tiempo real**: notificación a múltiples médicos y enfermeras, y persistencia del diagnóstico con disponibilidad permanente | RF-ESC-08, RF-ESC-13, RF-ESC-16, RF-REG-01 a RF-REG-05 | La actualización agrupada por cama alcanza al responsable médico y a las enfermeras asignadas (RF-ESC-13); los avisos pendientes se ordenan por severidad (RF-ESC-16); el registro a pie de cama se preserva sin pérdida ni duplicación durante una desconexión (RF-REG-02) | **RF-ESC-13 es el único enunciado que responde «cómo se avisa a varios» y dos de sus tres personas destinatarias lo marcaron Ambiguo** (Rodrigo: aviso por cambio o agrupado por cama; Aníbal: si interrumpe o espera). Su lista de disparadores **excluye la indicación médica nueva**, que es donde se corta el flujo de Milagros. Y ningún RF declara **por qué medio llega lo que el sistema «presenta»** a una enfermera con doble guante en una unidad con alarmas constantes | **50** |

```
D2 = (50 + 50 + 50) / 3 = 50,0
```

Ningún problema quedó en 0 —los tres tienen RF que declaran comportamiento y no solo lo nombran—, de
modo que el techo «D2 ≤ 60 si algún problema queda sin resolver» no se activa. El resultado queda
igualmente por debajo de él.

---

## Requerimientos mal formados

Inventario de los 81 RF contra las ocho condiciones de D3. Las condiciones 1, 3, 4, 5 y 6 se
verificaron además mecánicamente: los controles M1, M2, M3 y E2 devuelven vacío, y el reparto de
patrones EARS es 62 CUANDO, 12 SI…ENTONCES, 4 ubicuos, 2 DONDE y 1 MIENTRAS — los 81 con patrón
identificable. La condición 7 se verificó sobre los 102 criterios de aceptación: ninguno contiene más
de un par Cuando/Entonces.

| ID | Condición de D3 incumplida | Corrección propuesta |
|---|---|---|
| RF-ESC-06 | **2 — una sola respuesta.** «aplicarle la cadena y el plazo de acuse de su severidad registrada **o los del deterioro inmediato si** la severidad está por confirmar» son dos reglas: una de evento y una de borde pegadas por una condición | Partir en dos: `CUANDO un profesional emite un escalamiento con severidad registrada, el sistema DEBE aplicarle la cadena y el plazo de acuse de esa severidad` y `SI un escalamiento tiene la severidad por confirmar, ENTONCES el sistema DEBE aplicarle la cadena y el plazo del deterioro inmediato` |
| RF-REG-06 | **2 — una sola respuesta.** «DEBE presentar los resultados … **y señalar** los estudios solicitados aún sin resultado» son dos respuestas con dos objetos distintos | Partir en dos RF: uno para la presentación de resultados disponibles y otro para el señalamiento de estudios solicitados sin resultado |
| RF-REG-02 | **8 — el criterio amplía el contrato.** El enunciado garantiza «sin pérdida ni duplicación»; CA-2 exige además que las observaciones figuren «en el orden en que fueron tomadas», que es una garantía distinta y no declarada | Incorporar la preservación del orden al enunciado, o retirar CA-2 y dejarlo como criterio del RF que declare el orden |
| RF-REG-08 | **8 — el criterio amplía el contrato.** El enunciado promete «la tendencia disponible de hasta seis horas»; CA-2 exige que el sistema entregue esas horas «con la extensión del periodo declarada», obligación que el enunciado no contiene | Añadir al enunciado la declaración de la extensión efectiva del periodo presentado |
| RF-SUP-02 | **8 — el criterio amplía el contrato.** El enunciado obliga a *producir* los indicadores; CA-1 demuestra que la coordinadora *obtiene* franjas descubiertas y entregas cerradas «sin ingresar dato alguno». La obtención no está en el contrato, y es exactamente la carencia que Carmen declara | Declarar en el enunciado la entrega de los indicadores a quien los solicita, con su contenido cerrado |

```
D3 = 76 / 81 × 100 = 93,8
```

Observaciones que **no** se contaron como incumplimiento porque no corresponden a ninguna de las ocho
condiciones, y que quedan registradas para quien corrija: RF-TUR-16 usa como disparador el propio acto
que constituye su respuesta («CUANDO la coordinadora **obtiene** una copia …, el sistema DEBE
**generarla**»); RF-ESC-03 y RF-ESC-15 toman como disparador un acto interno del sistema («CUANDO el
sistema emite un escalamiento») sin que ningún RF declare ese acto; y RF-TUR-06 y RF-TUR-16 recopian su
enunciado en el criterio en lugar de demostrarlo, contra `docs/CONVENCIONES.md` §6.

---

## Requerimientos mal ubicados

| ID | Por qué no es funcional | Documento que le corresponde |
|---|---|---|
| — | Ninguno | — |

Ningún RF se limita a enunciar un umbral. Los enunciados que invocan un plazo —RF-TUR-26, RF-ESC-02,
RF-ESC-06— declaran comportamiento y remiten el umbral a `ReqNoFunc.MD`, que es exactamente el reparto
que `Spec/Eval-Spec.MD` §Alcance exige. No hay RNF alojado dentro de `ReqFunc.MD`, de modo que el
segundo tramo de D5 no recibe descuento por ese concepto.

---

## Requerimientos huérfanos

| ID | Por qué no traza a nadie |
|---|---|
| — | Ninguno |

Los 81 declaran persona y problema, y las cuatro personas y los tres problemas citados existen. La
proporción del primer tramo de D4 es 81/81.

Sí queda registrado un hallazgo que la tabla de huérfanos no captura: **24 RF no figuran en ninguna
fila de la matriz de trazabilidad**, es decir, declaran persona y problema pero no cubren ninguna tarea
crítica de nadie — RF-TUR-08, RF-TUR-11, RF-TUR-14, RF-TUR-15, RF-TUR-16, RF-TUR-21, RF-TUR-22,
RF-TUR-23, RF-TUR-24, RF-ESC-02, RF-ESC-05, RF-ESC-09, RF-ESC-10, RF-ESC-13, RF-ESC-15, RF-ESC-18,
RF-IAM-03, RF-IAM-06, RF-SUP-04 y los que solo aparecen en matrices de criterios. Diecisiete de ellos
son MUST. No resta en D4, cuya fórmula es explícita, pero es la evidencia que alimenta el descuento de
D6.

---

## Aritmética de D4

```
Tramo 1 — RF que declaran persona y problema existentes:  81/81 × 70 = 70,0
Tramo 2 — tareas críticas con al menos 1 punto en D1:     24/24 × 30 = 30,0
Tramo 3 — filas de matriz interna desfasadas del cuerpo:        1 × (−10) = −10,0

D4 = 70,0 + 30,0 − 10,0 = 90,0
```

**Fila desfasada.** En «Cobertura de problemas críticos», la fila **P2** declara «RF-ESC-01 a
RF-ESC-19», rango que incluye a RF-ESC-13, cuyo cuerpo declara **P3** y no P2; y omite a **RF-DIA-13**,
cuyo cuerpo declara «P1, P2». Dos discrepancias en una sola fila: −10.

Las demás matrices internas coinciden con el cuerpo: las 24 filas de trazabilidad citan RF cuya
`Persona` incluye a la persona de la fila; las 23 filas de criterios de éxito corresponden a los cinco
o seis criterios que cada persona declara; la fila P1 y la fila P3 de cobertura de problemas coinciden
exactamente con los cuerpos; los cinco `RNF-` citados existen en `ReqNoFunc.MD`; y la distribución de
prioridad —60 MUST (74,1 %), 19 SHOULD (23,5 %), 2 COULD (2,5 %)— coincide con el recuento del cuerpo.

---

## Tensiones sin decidir

| Tensión | Por qué ningún RF la resuelve |
|---|---|
| — | Ninguna. Las cinco están decididas explícitamente |

`tensiones_sin_decidir = 0`. El detalle de la decisión y de lo que cada una cuesta:

| Tensión | RF que la decide | Decisión y evidencia de que no fue esquivada |
|---|---|---|
| Velocidad frente a completitud del registro | RF-DIA-01 con RF-DIA-07 y RF-DIA-13 a RF-DIA-16 | El cierre exige el diagnóstico y nada más; el resto se registra una vez para reutilizarse. Rodrigo acepta el límite («no me obliga a llenar campos exhaustivos»); Carmen sostiene su objeción («una entrega cerrada con el mínimo no es una entrega cumplida para la Red»). Hay un lado que pierde: la tensión se decidió |
| Sensibilidad del escalamiento | RF-ESC-06, RF-ESC-11, RF-ESC-16 | La enfermera escala sin clasificar; la duda toma plazo inmediato pero se presenta detrás del deterioro confirmado. **Milagros marca RF-ESC-16 Estorba y Aníbal marca RF-ESC-11 Estorba**: cada uno paga el precio del otro, que es la firma de una tensión decidida y no esquivada |
| Autonomía de intercambio de turnos | RF-TUR-06, RF-TUR-13, RF-TUR-17 | La coordinadora autoriza por alcance y periodo; dentro de ese alcance el intercambio corre solo. Carmen marca RF-TUR-06 Estorba porque nada le avisa. La decisión existe, pero **solo gobierna los intercambios cubiertos**: los demás no tienen camino declarado (brecha 18) |
| Adopción voluntaria | RF-TUR-08, RF-TUR-16 | El sistema es la única fuente editable y las copias se limitan a periodos cerrados y no operativos. Carmen marca RF-TUR-16 Estorba: la decisión es explícita y va contra su práctica. Cuenta como decidida, y su consecuencia —la foto del Excel sobrevive porque el rol vigente no se puede consultar ni imprimir— encabeza las brechas (15 y 16) |
| Movilidad frente a control de datos | RF-REG-07, RF-IAM-04, RF-IAM-05, RF-IAM-07 | Se admite el dispositivo personal, el aviso previo expone solo contexto operativo y la identidad vigente evita reverificar. Milagros marca RF-IAM-07 Estorba y Aníbal lo marca Ambiguo: la decisión existe y su costo está identificado (brecha 25) |

---

## Aritmética de D5

```
Tramo 1 — tensiones decididas:            5 × 12 = 60,0
Tramo 2 — 40 − 10 × hallazgos (piso 0):   40 − 10 × 5 = −10 → 0,0

D5 = 60,0 + 0,0 = 60,0
```

Hallazgos independientes del segundo tramo:

| # | Hallazgo | Tipo | Evidencia |
|---|---|---|---|
| 1 | Cuatro términos circulan sin decidir alrededor de la entrega médica: **firma** (RF-DIA-04), **aceptación** (RF-DIA-09), **cierre** (RF-DIA-01, RF-SUP-01) y **entrega confirmada** (RF-DIA-10, RF-DIA-17). Ningún RF ni el glosario declaran qué acto produce una entrega confirmada, y de eso depende que el entrante reciba o no la entrega | Vocabulario inconsistente | auditoría + veredicto-rodrigo |
| 2 | **«Cambio urgente»** (RF-TUR-25, RF-TUR-26) no está definido en el glosario ni en ningún RF, y ningún enunciado declara quién lo clasifica; RF-TUR-05 habla del mismo hecho como «cambio de programación» | Terminología acuñada fuera del glosario | auditoría + veredicto-carmen |
| 3 | **RF-TUR-03 y RF-TUR-21 declaran dos veces la misma exclusión** por permiso: RF-TUR-03 ya presenta solo candidatos «sin permiso vigente». La copia ya divergió — RF-TUR-21 la ata a la entrada en vigencia del permiso, y de ahí sale el Ambiguo de Carmen sobre si un permiso aprobado el jueves excluye al profesional el viernes | Duplicado encubierto que ya produjo contradicción | auditoría |
| 4 | **RF-DIA-06 enuncia «un profesional»** y su CA-2 solo demuestra a «un médico» retirando la marca; el contrato no se deja leer de una sola manera y por eso Milagros lo marcó Ambiguo | Contradicción entre enunciado y criterio | auditoría + veredicto-milagros |
| 5 | **Tres verbos para el mismo acto de la Red sobre un rotante**: «comunica el alta o retiro» (RF-TUR-23), «asigna o retira» (RF-IAM-06) y «retira … desde un instante» (RF-TUR-24), con enunciados casi idénticos y objetos distintos (elegibilidad frente a responsabilidad clínica). Un lector no puede distinguirlos por su redacción | Vocabulario inconsistente | auditoría |

Con cinco hallazgos el segundo tramo cae por debajo de 0 y se aplica el piso: 0.

**Techos verificados.** El repositorio tiene glosario (`docs/GLOSARIO.md`), de modo que el techo D5 ≤ 80
no aplica. El techo de conformidad unánime tampoco: exige que **las cuatro** coberturas percibidas
alcancen 90 y aquí son 70, 70, 70 y 78. Se deja constancia expresa porque la comprobación forma parte
de los contrastes cruzados.

---

## Aritmética de D6

```
Base                                                        100
− 10 por RF sin prioridad o fuera de MUST/SHOULD/COULD:  0 × (−10) =   0
−  5 por MUST no justificado:                            4 × (−5)  = −20

D6 = 100 − 20 = 80,0
```

Los 81 declaran prioridad dentro del vocabulario admitido: 60 MUST, 19 SHOULD, 2 COULD.
`prioridad_uniforme = false`, de modo que el techo D6 ≤ 60 no aplica.

| MUST sin justificación | Por qué su ausencia no dejaría un problema sin resolver ni una tarea descubierta |
|---|---|
| RF-TUR-08 | La unicidad de la programación ya la garantiza RF-TUR-04. No figura en ninguna fila de tarea crítica; su aporte —negar autoridad a la copia— decide una tensión, que no es el criterio de MUST |
| RF-TUR-21 | RF-TUR-03 ya excluye de los candidatos a quien tiene permiso vigente. Es la mitad duplicada del hallazgo 3 de D5: suprimirlo no descubre ninguna tarea |
| RF-TUR-25 | La reasignación de Carmen queda cubierta por RF-TUR-03, RF-TUR-05, RF-TUR-18, RF-TUR-19 y RF-TUR-20. Consultar confirmaciones pendientes no sostiene ninguna tarea por sí solo, y descansa en el «cambio urgente» que nadie define. Nótese el gradiente invertido: la consulta es MUST y la reiteración que sí actúa (RF-TUR-26) es SHOULD |
| RF-DIA-16 | La tarea crítica de Rodrigo es «registrar nota de evolución y diagnóstico», que RF-DIA-07 cubre entero. El plan clínico no figura en el contrato de la entrega (RF-DIA-02) ni en el del escalamiento (RF-ESC-03): su ausencia no descubre ninguna tarea declarada |

**Gradiente inverso que no descuenta pero sí se reporta.** Cinco coberturas únicas de tarea crítica o
de criterio de éxito están en SHOULD mientras el documento reserva 60 MUST para el resto: RF-DIA-05
—único enunciado que responde un criterio de éxito de Rodrigo—, RF-DIA-08 —mitad de salida de la tarea
6 de Milagros, frente a RF-DIA-11 que es MUST—, RF-REG-08 —cobertura única de la tarea 3 de Aníbal—,
RF-SUP-02 —cobertura única de la tarea 6 de Carmen— y RF-SUP-03 —cobertura única de la tarea 6 de
Aníbal—. A ello se suma RF-DIA-15 (SHOULD), que produce un dato que el contrato MUST de RF-DIA-02
obliga a presentar. La prioridad está asignada, pero no en el eje que la convención declara.

---

## Discrepancias entre agente y cómputo

| Persona | Computado ×10 | Percibida | Δ | Qué falla: el agente o las tareas críticas |
|---|---:|---:|---:|---|
| Rodrigo | 36 | 70 | **34** | El agente. Su cuerpo sostiene el cómputo —declara seis necesidades no cubiertas y un corte de flujo en el paso 9— y su titular no lo refleja. Las tareas críticas de `Personas/Rodrigo.MD` están bien enunciadas: son observables y con frecuencia y criticidad |
| Milagros | 20 | 70 | **50** | El agente. Declara ocho necesidades no cubiertas, un paso inicial que ningún RF declara y un corte en el paso 12, y aun así informa 70 %. La percibida parece contar los RF que le sirven (31 Sirve) y no la cobertura de sus seis tareas |
| Carmen | 20 | 70 | **50** | El agente. Es quien más necesidades no cubiertas declara —once— y quien más Ambiguos emite —seis, dos de ellos sobre los verbos de su tarea 1—, y su titular coincide con el de las otras dos |
| Aníbal | 40 | 78 | **38** | El agente. Su percibida es la más alta y su evidencia la más consistente con ella: es el único con dos tareas en 5. Aun así declara siete necesidades no cubiertas y un paso sin ningún RF |

Las cuatro desviaciones superan el umbral de 20 puntos y las cuatro apuntan en la misma dirección: la
cobertura percibida está por encima de la computada. La coincidencia de las cuatro lecturas
—producidas en aislamiento— es lo que permite descartar la hipótesis contraria: si las tareas críticas
estuvieran mal enunciadas, la desviación se concentraría en una o dos personas y no en las cuatro con
el mismo signo. **Prevalece el valor computado.** El autoinforme mide qué proporción de los RF le
sirven al agente; la rúbrica mide si sus seis tareas quedan cubiertas y si su escenario se recorre
entero, que no es lo mismo: 31 veredictos *Sirve* conviven con una tarea *Aparente* y un flujo
interrumpido.

---

## Contraste de conformidad unánime

`Personas/README.md` advierte que un conjunto que deja conforme a las cuatro personas probablemente
esquivó una tensión. La comprobación **no se activa** —exige las cuatro percibidas en 90 o más, y son
70, 70, 70 y 78— y su hipótesis tampoco se cumple: ninguna de las cuatro está conforme, las cinco
tensiones están decididas y en tres de ellas hay una persona que marca *Estorba* el RF que decide en
contra de su lado. El techo D5 ≤ 40 no aplica.

---

## Evaluaciones de agente ausentes o inválidas

| Persona | Qué falta |
|---|---|
| — | Nada |

Las cuatro evaluaciones existen, cada una con 81 filas, el mismo conjunto y orden de IDs que
`ReqFunc.MD` y vocabulario cerrado. Ninguna omite un RF y ninguna emite un veredicto fuera de {Sirve,
Indiferente, Estorba, Ambiguo}. D1 es computable.

---

## Contraste de necesidad no cubierta sin brecha

Las cuatro evaluaciones declaran 32 necesidades no cubiertas. Las 32 figuran en la tabla de brechas
—filas 1 a 31, con la fusión de la necesidad de Rodrigo sobre la asignación de camas y la de Carmen
sobre el reparto de camas entre médicos en una sola fila—. Una sola queda **refutada por escrito**:

| Necesidad declarada | Por qué no genera brecha |
|---|---|
| Rodrigo: «tiempos, cantidad de clics e igualdad de la interfaz entre las tres sedes» | El propio agente la excluye («eso pertenece a `ReqNoFunc.MD` y no lo reclamo como carencia mía») y `Spec/Eval-Spec.MD` §Alcance confirma que los atributos de calidad no se puntúan aquí. Se refuta sin descuento |

---

## Brechas

Severidad: **Crítica** cuando interrumpe un escenario clave o deja un problema del enunciado sin
tramo; **Alta** cuando deja una tarea crítica incompleta o devuelve a la persona al procedimiento
manual; **Media** cuando degrada la evidencia o el mantenimiento del documento; **Baja** cuando es un
defecto de forma sin consecuencia operativa.

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---:|---|---|---|---|
| 1 | Rodrigo, Carmen · P1 | Ningún RF declara cómo se asignan las camas a un médico en un turno. RF-DIA-01, RF-DIA-02, RF-DIA-10 y RF-IAM-02 dan ese estado por existente; la programación asigna franjas, no camas | veredicto-rodrigo, veredicto-carmen, auditoría | Crítica |
| 2 | Rodrigo · P1 | No hay consulta a demanda, en medio del turno, de la decisión clínica con su fundamento, el esquema con su día y el estado de la familia. RF-DIA-02 solo dispara al iniciar el turno y RF-ESC-03 solo si alguien escala | veredicto-rodrigo | Crítica |
| 3 | Rodrigo | RF-DIA-05 solo cubre camas sobre las que el médico produjo un registro previo; en una rotación real la mayoría de las camas quedan fuera | veredicto-rodrigo | Alta |
| 4 | Rodrigo | Ninguna vista de las camas marcadas como inestables durante el turno: RF-DIA-06 ancla la marca a la entrega | veredicto-rodrigo | Media |
| 5 | Rodrigo | Lo que enfermería administró y los eventos que registró no se presentan al médico: RF-REG-05 los registra y RF-DIA-08 y RF-DIA-11 los llevan solo a la entrega de enfermería | veredicto-rodrigo | Media |
| 6 | Rodrigo, Carmen · P1 | Ningún RF declara qué ocurre con la entrega cuando RF-DIA-01 la bloquea y el turno termina igual | veredicto-rodrigo | Alta |
| 7 | Milagros · P2 | Ningún RF declara el acto de emisión del escalamiento: desde qué dispositivo y con qué disparador. RF-ESC-01 lo toma como hecho ya ocurrido | veredicto-milagros, auditoría | Crítica |
| 8 | Milagros · P2 | Ningún RF declara qué ocurre con un escalamiento emitido sin conexión; RF-REG-02 protege el registro, no el aviso | veredicto-milagros | Alta |
| 9 | Milagros · P3 | Ningún RF declara por qué medio le llega lo que el sistema «presenta» en RF-ESC-05 y RF-ESC-14, con doble guante y alarmas constantes | veredicto-milagros | Alta |
| 10 | Milagros | Ningún RF declara cómo se crea, se mantiene o se cierra un pendiente de cuidado de enfermería, del que dependen RF-DIA-08 y RF-DIA-11 | veredicto-milagros | Alta |
| 11 | Milagros | Ningún RF declara quién asigna las camas de cuidado de enfermería, de lo que dependen el rechazo de RF-IAM-02 y el destinatario de RF-ESC-13 | veredicto-milagros | Alta |
| 12 | Milagros | La entrega de enfermería no tiene cierre ni firma equivalentes a los del médico y no incluye los signos vitales ni el balance registrados toda la noche | veredicto-milagros | Alta |
| 13 | Milagros · P3 | Ningún RF avisa de una indicación médica nueva sobre sus camas, incluida la registrada a distancia por RF-REG-07: la lista de RF-ESC-13 no la contempla | veredicto-milagros, auditoría | Crítica |
| 14 | Milagros · P2 | El estado «disponible» de RF-ESC-08 no refleja al médico que atiende una emergencia en otro servicio sin caso abierto registrado, que es su escenario literal | veredicto-milagros | Alta |
| 15 | Carmen · P1 | Ningún RF declara que alguien pueda consultar la programación vigente. Hay unicidad, historial, huecos y avisos, y nada que declare la consulta del rol | veredicto-carmen | Crítica |
| 16 | Carmen | No hay copia imprimible del rol vigente: RF-TUR-16 solo cubre periodos cerrados y marcados no operativos. Con 15, la foto del Excel por WhatsApp sobrevive | veredicto-carmen | Alta |
| 17 | Carmen | Ningún RF declara la presentación de una solicitud de permiso ni una bandeja de pendientes; RF-TUR-12 resuelve algo cuya llegada el documento no describe | veredicto-carmen | Alta |
| 18 | Carmen, Rodrigo | No hay camino declarado para el intercambio que no está cubierto por una autorización previa, que es la mayoría de los que se pactan | veredicto-carmen | Alta |
| 19 | Carmen | Ni RF-TUR-06 ni RF-ESC-07 declaran aviso a la jefatura de lo que se aplicó sin su resolución, y por esa cobertura responde ella | veredicto-carmen | Alta |
| 20 | Carmen | Ningún RF declara que el candidato acepte o rechace la cobertura antes de quedar asignado: el escenario clave vuelve al teléfono | veredicto-carmen | Alta |
| 21 | Carmen | Ningún RF declara el paso siguiente cuando RF-TUR-03 devuelve una lista de candidatos vacía | veredicto-carmen | Media |
| 22 | Carmen | RF-TUR-03 presenta candidatos «en orden de rotación» sin que ningún RF ni el glosario declaren quién define esa rotación | veredicto-carmen, auditoría | Media |
| 23 | Carmen, Milagros · P2 | Ningún RF declara quién compone la cadena de escalamiento ni si sale de la programación; RF-ESC-09 pone a la jefatura en su extremo sin límite ni delegación declarados | veredicto-carmen | Alta |
| 24 | Carmen | RF-SUP-02 produce los indicadores y ningún enunciado declara cómo se entregan a la Dirección de Red | veredicto-carmen, auditoría | Media |
| 25 | Aníbal, Milagros · P2 | Ningún RF declara cómo se obtiene o renueva la identidad verificada vigente en el celular personal a las 03:20 con señal débil. RF-IAM-05 y RF-IAM-07 la dan por existente, y sin ella el flujo vuelve al teléfono | veredicto-anibal, veredicto-milagros | Crítica |
| 26 | Aníbal | Ningún RF declara qué se muestra en la pantalla de bloqueo cuando sí hay identidad verificada vigente, que es su estado normal y el único que RF-IAM-04 no gobierna | veredicto-anibal | Alta |
| 27 | Aníbal, Rodrigo · P2 | RF-IAM-02 no declara si tomar un caso por avance de la cadena habilita a registrar sobre esa cama; RF-REG-07 solo nombra al responsable vigente y al delegado | veredicto-anibal, veredicto-rodrigo, veredicto-milagros | Crítica |
| 28 | Aníbal | Ningún RF devuelve a quien indicó a distancia la confirmación de ejecución que RF-REG-04 registra: el ciclo queda abierto y se cierra por teléfono | veredicto-anibal | Alta |
| 29 | Aníbal | RF-SUP-03 está enunciado por unidad y él cubre dos sedes: su revisión matinal «en un solo lugar» son dos consultas | veredicto-anibal | Media |
| 30 | Aníbal · P2 | El aviso no distingue en su teléfono la duda no clasificada del deterioro confirmado; RF-ESC-16 solo ordena una lista de pendientes | veredicto-anibal | Alta |
| 31 | Aníbal | Ningún RF declara si la guardia localizable es un turno médico con camas asignadas a efectos de RF-DIA-01, y por lo tanto si a las 08:00 se le bloqueará un cierre por camas que nunca vio | veredicto-anibal | Alta |
| 32 | P1 | Ningún RF declara qué acto produce una «entrega confirmada», condición de la que dependen RF-DIA-10 y RF-DIA-17, mientras el documento usa firma, aceptación, cierre y entrega confirmada como cuatro términos distintos | auditoría, veredicto-rodrigo | Crítica |
| 33 | Carmen | «Cambio urgente» no está definido ni en el glosario ni en ningún RF, y de él dependen RF-TUR-25 y RF-TUR-26 | auditoría, veredicto-carmen | Alta |
| 34 | Carmen | RF-TUR-03 y RF-TUR-21 declaran dos veces la exclusión por permiso, y las dos copias ya divergen en el instante desde el que rige | auditoría | Alta |
| 35 | Milagros | RF-DIA-06 enuncia «un profesional» y su criterio solo demuestra «un médico»: el contrato admite dos lecturas | auditoría, veredicto-milagros | Media |
| 36 | Documento | RF-TUR-23, RF-TUR-24 e RF-IAM-06 usan tres redacciones casi idénticas para el mismo acto de la Red con objetos distintos | auditoría | Baja |
| 37 | Documento | La fila P2 de «Cobertura de problemas críticos» incluye RF-ESC-13 (que declara P3) y omite RF-DIA-13 (que declara P2) | auditoría | Media |
| 38 | Documento | RF-ESC-06 enuncia dos respuestas: la cadena de la severidad registrada y la del deterioro inmediato cuando está por confirmar | auditoría | Media |
| 39 | Documento | RF-REG-06 enuncia dos respuestas: presentar resultados y señalar estudios solicitados sin resultado | auditoría | Media |
| 40 | Documento | RF-REG-02 CA-2 exige preservar el orden, garantía que el enunciado no declara | auditoría | Baja |
| 41 | Documento | RF-REG-08 CA-2 exige declarar la extensión del periodo, obligación que el enunciado no contiene | auditoría | Baja |
| 42 | Carmen | RF-SUP-02 CA-1 demuestra una obtención de indicadores que el enunciado no promete | auditoría, veredicto-carmen | Media |
| 43 | Documento | Cuatro MUST no justificados —RF-TUR-08, RF-TUR-21, RF-TUR-25, RF-DIA-16— cuya ausencia no dejaría un problema sin resolver ni una tarea descubierta | auditoría | Media |
| 44 | Rodrigo, Milagros, Carmen, Aníbal | Cinco coberturas únicas de tarea crítica o de criterio de éxito están en SHOULD —RF-DIA-05, RF-DIA-08, RF-REG-08, RF-SUP-02, RF-SUP-03— y RF-DIA-15 (SHOULD) alimenta el contrato MUST de RF-DIA-02 | auditoría, veredicto-rodrigo, veredicto-milagros, veredicto-carmen, veredicto-anibal | Alta |

**Brechas abiertas: 44.** Ninguna proviene de un control mecánico: los ocho controles de forma y
estructura devuelven vacío, de modo que no hay filas con origen `control-‹id›`. Ese es exactamente el
límite que `docs/CONVENCIONES.md` §11 anuncia: un control en verde dice que el documento no incurre en
el defecto que ese control sabe detectar, no que el requerimiento sirva.

---

## Cálculo global

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 29,0 | 30 % | 8,70 |
| D2 Cobertura de problemas críticos | 50,0 | 25 % | 12,50 |
| D3 Verificabilidad y forma | 93,8 | 20 % | 18,76 |
| D4 Trazabilidad | 90,0 | 10 % | 9,00 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,00 |
| D6 Priorización | 80,0 | 5 % | 4,00 |
| **Suma de aportes** | | | **58,96** |

```
Global = 29,0×0,30 + 50,0×0,25 + 93,8×0,20 + 90,0×0,10 + 60,0×0,10 + 80,0×0,05
       = 8,70 + 12,50 + 18,76 + 9,00 + 6,00 + 4,00
       = 58,96  →  59,0
```

## Veredicto

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 59,0 % | ✗ |
| 2 | D1 | ≥ 80,0 | 29,0 | ✗ |
| 3 | Persona más baja | ≥ 7,0/10 | 2,0 (Milagros y Carmen) | ✗ |
| 4 | D2 | ≥ 80,0 | 50,0 | ✗ |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | ✓ |

**FAILED.** Cuatro de las cinco condiciones no se cumplen.

## Bloqueos

Ninguna corrección necesaria cayó fuera de lo editable por esta corrida: las 44 brechas se corrigen en
`Requirements/ReqFunc.MD`, que es de solo lectura durante la medición por diseño y cuya corrección
pertenece a otra rama y a una corrida posterior. No se crea `bloqueos.MD`.
