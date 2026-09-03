# Diagnóstico — corrida 2026-08-14-iteracion-4

Evidencia completa de la agregación. Los cuatro veredictos de persona son insumo inmutable y viven
en archivos propios junto a este documento.

## Precondiciones

| Persona | Filas | Sirve | Indiferente | Estorba | Ambiguo | Vocabulario | Percibida |
|---|---:|---:|---:|---:|---:|---|---:|
| Rodrigo | 118 | 27 | 82 | 4 | 5 | cerrado | 70 |
| Milagros | 118 | 44 | 68 | 3 | 3 | cerrado | 78 |
| Carmen | 118 | 59 | 49 | 5 | 5 | cerrado | 70 |
| Aníbal | 118 | 46 | 65 | 4 | 3 | cerrado | 80 |

Las cuatro evaluaciones existen, emiten veredicto para los 118 RF vigentes de `ReqFunc.MD`, en el
mismo orden de identificadores del cuerpo, y no usan ningún término fuera de Sirve / Indiferente /
Estorba / Ambiguo. D1 es computable.

## Criterios de derivación aplicados

Tres reglas de lectura, fijadas antes de puntuar y aplicadas sin excepción, para que la escala no se
decida caso por caso:

1. **La relación «traza» es la de la matriz de trazabilidad de `ReqFunc.MD`.** Es la declaración que
   el propio documento hace de qué RF cubre qué tarea, y es la que `X_p` necesita para distinguir el
   daño dentro del ámbito de la tarea del daño fuera de él.
2. **Se penaliza la incompletitud directa del comportamiento que la tarea necesita, no la dependencia
   de segundo orden.** Una carencia se cobra en la tarea cuyo RF la contiene, no en cada tarea que
   más abajo la hereda; de otro modo un solo enunciado faltante anularía el documento entero.
3. **Un 3 dice que falta comportamiento y se corrige agregándolo; un 1 dice que el enunciado no se
   deja leer de una sola manera y se corrige reescribiendo.** El vacío de «responsable clínico
   vigente» es comportamiento faltante y puntúa 3; una tarea sostenida por un único RF que su agente
   marcó Ambiguo puntúa 1.

## Veredictos agregados

| RF | Rodrigo | Milagros | Carmen | Aníbal | Efecto en D1 |
|---|---|---|---|---|---|
| RF-TUR-01 | Indiferente | Indiferente | Sirve | Ambiguo | traza C2 |
| RF-TUR-02 | Indiferente | Indiferente | Ambiguo | Indiferente | traza C2; Ambiguo en tarea (C) |
| RF-TUR-03 | Indiferente | Indiferente | Sirve | Indiferente | traza C4 |
| RF-TUR-04 | Indiferente | Indiferente | Sirve | Sirve | traza C1 |
| RF-TUR-05 | Indiferente | Indiferente | Sirve | Sirve | traza C4 |
| RF-TUR-06 | Sirve | Indiferente | Estorba | Indiferente | traza C3; Estorba dentro de tarea (C) |
| RF-TUR-07 | Indiferente | Indiferente | Sirve | Indiferente | traza C2 |
| RF-TUR-08 | Indiferente | Sirve | Sirve | Indiferente | sin efecto: no traza a ninguna tarea crítica |
| RF-TUR-09 | Indiferente | Indiferente | Ambiguo | Indiferente | traza C1; Ambiguo en tarea (C) |
| RF-TUR-10 | Indiferente | Indiferente | Sirve | Indiferente | traza C1 |
| RF-TUR-11 | Indiferente | Indiferente | Sirve | Indiferente | traza C1 |
| RF-TUR-12 | Indiferente | Indiferente | Sirve | Indiferente | traza C3 |
| RF-TUR-13 | Sirve | Indiferente | Ambiguo | Indiferente | traza C3; Ambiguo en tarea (C) |
| RF-TUR-14 | Indiferente | Indiferente | Sirve | Indiferente | sin efecto: no traza a ninguna tarea crítica |
| RF-TUR-15 | Indiferente | Indiferente | Sirve | Indiferente | sin efecto: no traza a ninguna tarea crítica |
| RF-TUR-16 | Indiferente | Indiferente | Sirve | Indiferente | sin efecto: no traza a ninguna tarea crítica |
| RF-TUR-17 | Ambiguo | Indiferente | Sirve | Indiferente | traza C3 |
| RF-TUR-18 | Indiferente | Indiferente | Sirve | Indiferente | traza C4 |
| RF-TUR-19 | Indiferente | Indiferente | Sirve | Indiferente | traza C4 |
| RF-TUR-20 | Indiferente | Indiferente | Sirve | Indiferente | traza C4 |
| RF-TUR-21 | Indiferente | Indiferente | Sirve | Indiferente | traza C3 |
| RF-TUR-22 | Indiferente | Indiferente | Sirve | Indiferente | traza C3 |
| RF-TUR-23 | Indiferente | Indiferente | Sirve | Indiferente | sin efecto: no traza a ninguna tarea crítica |
| RF-TUR-24 | Estorba | Indiferente | Sirve | Indiferente | X_R −2 |
| RF-TUR-25 | Indiferente | Indiferente | Sirve | Indiferente | traza C4 |
| RF-TUR-26 | Indiferente | Indiferente | Sirve | Estorba | traza C4; X_A −2 |
| RF-TUR-27 | Indiferente | Sirve | Sirve | Sirve | traza C1 |
| RF-TUR-28 | Indiferente | Estorba | Sirve | Indiferente | traza C1; X_M −2 |
| RF-TUR-29 | Indiferente | Indiferente | Sirve | Indiferente | traza C3 |
| RF-TUR-30 | Indiferente | Indiferente | Sirve | Indiferente | traza C3 |
| RF-TUR-31 | Estorba | Indiferente | Sirve | Indiferente | traza C3; X_R −2 |
| RF-TUR-32 | Indiferente | Indiferente | Sirve | Indiferente | traza C3 |
| RF-TUR-33 | Indiferente | Indiferente | Sirve | Indiferente | traza C3 |
| RF-TUR-34 | Indiferente | Indiferente | Sirve | Indiferente | traza C3 |
| RF-TUR-35 | Indiferente | Indiferente | Ambiguo | Indiferente | traza C4; Ambiguo en tarea (C) |
| RF-TUR-36 | Indiferente | Indiferente | Sirve | Indiferente | traza C4 |
| RF-TUR-37 | Indiferente | Indiferente | Sirve | Indiferente | traza C4 |
| RF-TUR-38 | Indiferente | Indiferente | Sirve | Indiferente | traza C4 |
| RF-TUR-39 | Estorba | Indiferente | Estorba | Indiferente | traza C4; X_R −2; Estorba dentro de tarea (C) |
| RF-TUR-40 | Indiferente | Indiferente | Sirve | Indiferente | traza C4 |
| RF-TUR-41 | Indiferente | Indiferente | Sirve | Indiferente | traza C4 |
| RF-DIA-01 | Sirve | Indiferente | Sirve | Sirve | traza R6 |
| RF-DIA-02 | Sirve | Indiferente | Sirve | Indiferente | traza R1, R2 |
| RF-DIA-03 | Sirve | Indiferente | Sirve | Indiferente | traza R1 |
| RF-DIA-04 | Sirve | Indiferente | Sirve | Indiferente | traza R6 |
| RF-DIA-05 | Sirve | Indiferente | Indiferente | Sirve | traza R2 |
| RF-DIA-06 | Sirve | Sirve | Indiferente | Indiferente | traza R4 |
| RF-DIA-07 | Sirve | Indiferente | Sirve | Sirve | traza R2, R3 |
| RF-DIA-08 | Indiferente | Sirve | Indiferente | Indiferente | traza M6 |
| RF-DIA-09 | Sirve | Indiferente | Sirve | Indiferente | traza R1 |
| RF-DIA-10 | Sirve | Indiferente | Sirve | Indiferente | traza R1, R2 |
| RF-DIA-11 | Indiferente | Sirve | Indiferente | Indiferente | traza M6 |
| RF-DIA-12 | Ambiguo | Indiferente | Sirve | Indiferente | traza R6, C5; Ambiguo en tarea (R) |
| RF-DIA-13 | Sirve | Indiferente | Indiferente | Sirve | traza R2, R3 |
| RF-DIA-14 | Sirve | Indiferente | Indiferente | Sirve | traza R2, R3 |
| RF-DIA-15 | Sirve | Indiferente | Indiferente | Indiferente | traza R2, R3 |
| RF-DIA-16 | Sirve | Indiferente | Indiferente | Indiferente | traza R3 |
| RF-DIA-17 | Sirve | Indiferente | Indiferente | Indiferente | traza R1 |
| RF-DIA-18 | Sirve | Ambiguo | Estorba | Indiferente | traza R1; X_C −2 |
| RF-DIA-19 | Indiferente | Sirve | Estorba | Indiferente | traza M6; X_C −2 |
| RF-DIA-20 | Sirve | Indiferente | Sirve | Indiferente | traza R6 |
| RF-DIA-21 | Sirve | Indiferente | Indiferente | Indiferente | traza R2 |
| RF-DIA-22 | Sirve | Sirve | Indiferente | Indiferente | traza R4 |
| RF-DIA-23 | Ambiguo | Sirve | Indiferente | Estorba | traza R2; Ambiguo en tarea (R); X_A −2 |
| RF-DIA-24 | Indiferente | Indiferente | Sirve | Indiferente | traza R6, C5 |
| RF-DIA-25 | Indiferente | Sirve | Indiferente | Indiferente | traza M6 |
| RF-DIA-26 | Indiferente | Sirve | Indiferente | Indiferente | traza M6 |
| RF-DIA-27 | Indiferente | Sirve | Indiferente | Indiferente | traza M6 |
| RF-ESC-01 | Ambiguo | Sirve | Ambiguo | Sirve | traza M2 |
| RF-ESC-02 | Indiferente | Sirve | Indiferente | Sirve | sin efecto: no traza a ninguna tarea crítica |
| RF-ESC-03 | Sirve | Ambiguo | Indiferente | Sirve | traza A1 |
| RF-ESC-04 | Indiferente | Sirve | Indiferente | Sirve | traza A2 |
| RF-ESC-05 | Indiferente | Sirve | Indiferente | Indiferente | sin efecto: no traza a ninguna tarea crítica |
| RF-ESC-06 | Indiferente | Sirve | Indiferente | Sirve | traza M2 |
| RF-ESC-07 | Indiferente | Sirve | Estorba | Sirve | traza A5; X_C −2 |
| RF-ESC-08 | Indiferente | Sirve | Sirve | Sirve | traza M3 |
| RF-ESC-09 | Indiferente | Sirve | Sirve | Sirve | sin efecto: no traza a ninguna tarea crítica |
| RF-ESC-10 | Indiferente | Indiferente | Indiferente | Sirve | sin efecto: no traza a ninguna tarea crítica |
| RF-ESC-11 | Indiferente | Sirve | Indiferente | Sirve | traza M2 |
| RF-ESC-12 | Indiferente | Sirve | Indiferente | Sirve | traza A2 |
| RF-ESC-13 | Ambiguo | Estorba | Indiferente | Ambiguo | traza M4; Estorba dentro de tarea (M) |
| RF-ESC-14 | Indiferente | Sirve | Indiferente | Sirve | traza A2 |
| RF-ESC-15 | Indiferente | Sirve | Indiferente | Sirve | traza M2 |
| RF-ESC-16 | Indiferente | Sirve | Indiferente | Sirve | traza A1 |
| RF-ESC-17 | Indiferente | Sirve | Indiferente | Sirve | traza A5 |
| RF-ESC-18 | Indiferente | Sirve | Sirve | Sirve | sin efecto: no traza a ninguna tarea crítica |
| RF-ESC-19 | Indiferente | Sirve | Indiferente | Sirve | traza A2 |
| RF-ESC-20 | Indiferente | Sirve | Indiferente | Sirve | traza M2 |
| RF-ESC-21 | Indiferente | Sirve | Indiferente | Sirve | traza M2 |
| RF-ESC-22 | Indiferente | Sirve | Indiferente | Sirve | traza M2 |
| RF-ESC-23 | Indiferente | Sirve | Sirve | Sirve | traza M2 |
| RF-ESC-24 | Indiferente | Indiferente | Indiferente | Sirve | traza A1 |
| RF-ESC-25 | Indiferente | Sirve | Indiferente | Estorba | traza M2; X_A −2 |
| RF-ESC-26 | Indiferente | Indiferente | Sirve | Indiferente | traza C2 |
| RF-REG-01 | Indiferente | Sirve | Indiferente | Sirve | traza M1 |
| RF-REG-02 | Indiferente | Sirve | Indiferente | Sirve | traza M1 |
| RF-REG-03 | Sirve | Sirve | Indiferente | Sirve | traza M4 |
| RF-REG-04 | Indiferente | Sirve | Indiferente | Sirve | traza M4 |
| RF-REG-05 | Indiferente | Sirve | Indiferente | Sirve | traza M5 |
| RF-REG-06 | Sirve | Indiferente | Indiferente | Sirve | traza R5 |
| RF-REG-07 | Indiferente | Sirve | Indiferente | Sirve | traza A4 |
| RF-REG-08 | Sirve | Indiferente | Indiferente | Ambiguo | traza A3; Ambiguo en tarea (A) |
| RF-REG-09 | Indiferente | Sirve | Indiferente | Sirve | traza A4 |
| RF-REG-10 | Sirve | Indiferente | Indiferente | Sirve | traza R5 |
| RF-IAM-01 | Sirve | Sirve | Sirve | Sirve | traza R3 |
| RF-IAM-02 | Estorba | Estorba | Sirve | Sirve | traza A4; X_R −2; X_M −2 |
| RF-IAM-03 | Indiferente | Indiferente | Sirve | Indiferente | sin efecto: no traza a ninguna tarea crítica |
| RF-IAM-04 | Indiferente | Indiferente | Indiferente | Sirve | traza A1 |
| RF-IAM-05 | Indiferente | Indiferente | Indiferente | Sirve | traza A1, A4 |
| RF-IAM-06 | Sirve | Sirve | Sirve | Indiferente | sin efecto: no traza a ninguna tarea crítica |
| RF-IAM-07 | Indiferente | Indiferente | Indiferente | Estorba | traza A1, A4; Estorba dentro de tarea (A) |
| RF-IAM-08 | Indiferente | Sirve | Sirve | Sirve | traza A1, A4 |
| RF-IAM-09 | Indiferente | Sirve | Indiferente | Sirve | traza R3, A4 |
| RF-SUP-01 | Indiferente | Indiferente | Sirve | Indiferente | traza C5 |
| RF-SUP-02 | Indiferente | Indiferente | Sirve | Indiferente | traza C6 |
| RF-SUP-03 | Indiferente | Ambiguo | Indiferente | Sirve | traza A6 |
| RF-SUP-04 | Indiferente | Sirve | Sirve | Indiferente | sin efecto: no traza a ninguna tarea crítica |
| RF-SUP-05 | Indiferente | Indiferente | Sirve | Indiferente | traza C6 |

## Matriz de cobertura

| Persona | Tarea crítica | RF que la cubre | Veredicto | Puntos | Estado |
|---|---|---|---|---:|---|
| Rodrigo | 1. Recibir el handoff estructurado de todas las camas asignadas | RF-DIA-02, RF-DIA-03, RF-DIA-09, RF-DIA-10, RF-DIA-17, RF-DIA-18 | 6 Sirve | 3 | Incompleta |
| Rodrigo | 2. Consultar la evolución y el diagnóstico del turno anterior | RF-DIA-02, RF-DIA-05, RF-DIA-07, RF-DIA-10, RF-DIA-13, RF-DIA-14, RF-DIA-15, RF-DIA-21 Sirve; RF-DIA-23 Ambiguo | 8 Sirve, 1 Ambiguo | 3 | Incompleta |
| Rodrigo | 3. Registrar nota de evolución y diagnóstico por paciente | RF-DIA-07, RF-DIA-13, RF-DIA-14, RF-DIA-15, RF-DIA-16, RF-IAM-01 Sirve; RF-IAM-09 Indiferente | 6 Sirve | 3 | Incompleta |
| Rodrigo | 4. Marcar pacientes inestables o con pendientes críticos | RF-DIA-06, RF-DIA-22 | 2 Sirve | 5 | Cubierta |
| Rodrigo | 5. Consultar resultados de laboratorio e imágenes | RF-REG-06, RF-REG-10 | 2 Sirve | 3 | Incompleta |
| Rodrigo | 6. Cerrar y firmar la entrega de turno | RF-DIA-01, RF-DIA-04, RF-DIA-20 Sirve; RF-DIA-12 Ambiguo; RF-DIA-24 Indiferente | 3 Sirve, 1 Ambiguo | 3 | Incompleta |
| Milagros | 1. Registrar signos vitales y balance por paciente | RF-REG-01, RF-REG-02 | 2 Sirve | 3 | Incompleta |
| Milagros | 2. Escalar un deterioro clínico al médico responsable | RF-ESC-01, RF-ESC-06, RF-ESC-11, RF-ESC-15, RF-ESC-20, RF-ESC-21, RF-ESC-22, RF-ESC-23, RF-ESC-25 | 9 Sirve | 3 | Incompleta |
| Milagros | 3. Consultar quién está de guardia y su estado de disponibilidad | RF-ESC-08 | 1 Sirve | 3 | Incompleta |
| Milagros | 4. Ver y confirmar indicaciones médicas vigentes | RF-REG-03, RF-REG-04 Sirve; RF-ESC-13 Estorba | 2 Sirve, 1 Estorba | 3 | Incompleta |
| Milagros | 5. Registrar eventos y administración de medicamentos | RF-REG-05 | 1 Sirve | 5 | Cubierta |
| Milagros | 6. Recibir y entregar el turno de enfermería | RF-DIA-08, RF-DIA-11, RF-DIA-19, RF-DIA-25, RF-DIA-26, RF-DIA-27 | 6 Sirve | 3 | Incompleta |
| Carmen | 1. Elaborar y publicar la programación mensual de turnos | RF-TUR-04, RF-TUR-10, RF-TUR-11, RF-TUR-27, RF-TUR-28 Sirve; RF-TUR-09 Ambiguo | 5 Sirve, 1 Ambiguo | 3 | Incompleta |
| Carmen | 2. Validar que no existan cruces ni franjas descubiertas | RF-TUR-01, RF-TUR-07, RF-ESC-26 Sirve; RF-TUR-02 Ambiguo | 3 Sirve, 1 Ambiguo | 3 | Incompleta |
| Carmen | 3. Aprobar o rechazar intercambios y permisos | RF-TUR-12, RF-TUR-17, RF-TUR-21, RF-TUR-22, RF-TUR-29, RF-TUR-30, RF-TUR-31, RF-TUR-32, RF-TUR-33, RF-TUR-34 Sirve; RF-TUR-13 Ambiguo; RF-TUR-06 Estorba | 10 Sirve, 1 Ambiguo, 1 Estorba | 3 | Incompleta |
| Carmen | 4. Reasignar cobertura ante una ausencia imprevista | RF-TUR-03, RF-TUR-05, RF-TUR-18, RF-TUR-19, RF-TUR-20, RF-TUR-25, RF-TUR-26, RF-TUR-36, RF-TUR-37, RF-TUR-38, RF-TUR-40, RF-TUR-41 Sirve; RF-TUR-35 Ambiguo; RF-TUR-39 Estorba | 12 Sirve, 1 Ambiguo, 1 Estorba | 3 | Incompleta |
| Carmen | 5. Monitorear cumplimiento y completitud de entregas de turno | RF-DIA-12, RF-DIA-24, RF-SUP-01 | 3 Sirve | 3 | Incompleta |
| Carmen | 6. Generar indicadores de cobertura para la Dirección de Red | RF-SUP-02, RF-SUP-05 | 2 Sirve | 5 | Cubierta |
| Aníbal | 1. Recibir la alerta de escalamiento con contexto clínico adjunto | RF-ESC-03, RF-ESC-16, RF-ESC-24, RF-IAM-04, RF-IAM-05, RF-IAM-08 Sirve; RF-IAM-07 Estorba | 6 Sirve, 1 Estorba | 3 | Incompleta |
| Aníbal | 2. Confirmar recepción y tomar el caso | RF-ESC-04, RF-ESC-12, RF-ESC-14, RF-ESC-19 | 4 Sirve | 3 | Incompleta |
| Aníbal | 3. Consultar tendencia de signos, ventilación y última evolución | RF-REG-08 | 1 Ambiguo | 1 | Aparente |
| Aníbal | 4. Registrar la indicación dada de forma remota | RF-REG-07, RF-REG-09, RF-IAM-02, RF-IAM-05, RF-IAM-08, RF-IAM-09 Sirve; RF-IAM-07 Estorba | 6 Sirve, 1 Estorba | 5 | Cubierta |
| Aníbal | 5. Marcarse temporalmente indisponible y delegar | RF-ESC-07, RF-ESC-17 | 2 Sirve | 3 | Incompleta |
| Aníbal | 6. Revisar en la mañana lo ocurrido durante la noche | RF-SUP-03 | 1 Sirve | 5 | Cubierta |

### Por qué cada tarea no llegó a 5

**Rodrigo 1 — 3.** Los seis RF son Sirve y declaran el acto, pero RF-DIA-02 declara la presentación
**por cada cama asignada** y ningún enunciado declara una vista agregada de la asignación completa:
el criterio de éxito «entender el estado de las 10 camas en ≤ 15 minutos usando solo el sistema»
queda sin RF que lo satisfaga. Falta comportamiento, no claridad.

**Rodrigo 2 — 3.** El delta desde su último contacto lo cubre RF-DIA-05, pero el aporte de
enfermería entra por RF-DIA-23, cuyo «turno en curso» el agente marcó Ambiguo: a las 19:00 no puede
asegurar que vea lo que enfermería registró en la tarde.

**Rodrigo 3 — 3.** Los cinco actos de registro están declarados y atribuidos, pero ningún enunciado
declara para la entrega médica lo que RF-DIA-08 y RF-DIA-11 declaran para enfermería —componerla
reutilizando sin transcripción lo ya registrado—, de modo que el criterio «registrar cuesta menos
que escribirlo a mano» queda sin cobertura.

**Rodrigo 4 — 5.** RF-DIA-06 declara la marca, su persistencia por encima del cambio de turno y su
retiro con autoría; RF-DIA-22 declara la lista de camas marcadas. El comportamiento que la tarea
necesita está completo y ningún RF implicado contradice a otro. El alcance permisivo de «un
profesional» que retira la marca es contrato declarado, no comportamiento ausente; se registra como
brecha de severidad media.

**Rodrigo 5 — 3.** La consulta está declarada, pero RF-REG-06 presenta los resultados «disponibles»
y ningún RF declara cómo el resultado de un estudio entra al episodio: la pantalla puede estar vacía
sin que ningún enunciado quede incumplido. El glosario lo afirma en la entrada «Estudio», pero el
glosario define y no regula.

**Rodrigo 6 — 3.** El cierre, la firma y el bloqueo están declarados por RF Sirve, pero la causa del
bloqueo llega por RF-DIA-12, marcado Ambiguo: «el dato obligatorio ausente» no está enumerado en
ningún enunciado y de esa lista depende que cerrar cueste dos minutos o veinte.

**Milagros 1 — 3.** RF-REG-01 y RF-REG-02 declaran el registro y su preservación sin conexión, pero
RF-IAM-02 rechaza su registro sobre una cama fuera de su asignación de cuidado y ningún enunciado
prevé el relevo entre las dos enfermeras del turno, que es la situación normal de la unidad.

**Milagros 2 — 3.** Los nueve RF son Sirve y la emisión junto a la cama queda declarada en dos
actos, pero la cadena que RF-ESC-23 encabeza con «el responsable clínico vigente» carece de un RF
que declare cómo una cama adquiere ese responsable: falta el primer eslabón. Se suma RF-ESC-03, que
no declara qué ocurre cuando el contexto obligatorio todavía no existe.

**Milagros 3 — 3.** RF-ESC-08 es Sirve y su CA-3 satisface literalmente el criterio «ver quién está
de guardia en este momento», pero todo su contenido es «el responsable vigente por cada cama», y las
únicas vías declaradas para constituirlo son la delegación de RF-ESC-07 y la comunicación de la Red
de RF-IAM-06. Falta la vía ordinaria.

**Milagros 4 — 3.** Ver y confirmar están declarados por RF-REG-03 y RF-REG-04, pero la mitad de la
tarea que exige que la indicación nueva la alcance a ella descansa en RF-ESC-13, que el agente marcó
Estorba porque la actualización «aguarda la consulta de sus destinatarios».

**Milagros 5 — 5.** RF-REG-05 declara el comportamiento completo —evento y medicación incorporados
al episodio junto a la cama con autoría e instante—, los criterios relacionados «registrar a pie de
cama» y «dejar de transcribir» quedan satisfechos con RF-REG-02 y RF-DIA-08, y el agente no declara
ninguna carencia sobre esta tarea.

**Milagros 6 — 3.** Recibir y entregar están declarados sin transcripción, pero RF-DIA-11 se apoya en
«la última entrega cerrada» y no existe para enfermería el equivalente de RF-DIA-17: si el turno
anterior concluyó sin cerrar, nada le advierte ni le diferencia una entrega más antigua.

**Carmen 1 — 3.** RF-TUR-09, que crea la propuesta, quedó Ambiguo: ningún enunciado declara quién
define cuántas franjas y cuántos profesionales requiere la unidad, y sin ese patrón la «propuesta
completa» de RF-TUR-10 no tiene contra qué medirse.

**Carmen 2 — 3.** El criterio «el sistema impide en vez de advertir» lo cumple RF-TUR-01 de manera
literal, pero la mitad laboral de la validación descansa en RF-TUR-02, Ambiguo: ningún RF declara de
dónde salen las reglas de jornada y descanso ni el vínculo laboral vigente, y respetar el régimen
laboral es restricción explícita de la persona.

**Carmen 3 — 3.** Permisos e intercambios sin autorización están cubiertos de punta a punta, pero
RF-TUR-06 aplica un intercambio a la programación vigente sin su resolución y el «alcance» de la
autorización de RF-TUR-13 no está declarado en ningún enunciado: la tarea puede vaciarse sin que
ningún RF quede incumplido.

**Carmen 4 — 3.** El paso central quedó Ambiguo: RF-TUR-35 obliga a asignar al candidato que acepta
sin declarar si se revalida la elegibilidad, y RF-TUR-39 puede dejar la solicitud sin efecto sin que
ningún RF le dé una vía para cerrar la franja por autoridad cuando la guardia empieza en horas.

**Carmen 5 — 3.** RF-SUP-01 entrega más de lo que el criterio pedía, pero quedan fuera del
monitoreo la aceptación de la entrega por el médico entrante —que RF-DIA-09 registra y RF-SUP-01 no
reporta— y el cumplimiento de las entregas de enfermería, que también son entregas de turno de su
unidad.

**Carmen 6 — 5.** RF-SUP-02 declara la producción de los indicadores a partir de los registros
vigentes y sin transcripción manual, que es su criterio de éxito con todas las letras, y RF-SUP-05 su
entrega. El riesgo de adopción que el agente señala es una condición sobre la calidad del dato, no
comportamiento ausente, y la indefinición de «franjas requeridas» se cobra en su tarea 1, donde el
enunciado que la contiene vive.

**Aníbal 1 — 3.** RF-ESC-03 enumera el paquete completo y la tarea queda cubierta en lo esencial,
pero la medicación administrada durante el turno en curso no está en esa lista y RF-DIA-23 la
condiciona a una asignación médica vigente que un localizable nunca tiene; además RF-IAM-07 puede
dejarlo sin ningún contexto y ningún RF declara un piso de información para decidir.

**Aníbal 2 — 3.** El acuse y la toma quedan registrados y devueltos a quien escaló, pero ningún
enunciado declara si puede acusar recibo desde el propio aviso de RF-IAM-04 antes de identificarse o
si RF-IAM-07 se lo impide, que con señal débil es la diferencia entre un toque y tres minutos.

**Aníbal 3 — 1.** La matriz de trazabilidad le asigna un único RF, RF-REG-08, y su agente lo marcó
Ambiguo porque el enunciado no declara de qué es «la tendencia disponible de hasta seis horas». Es
el caso literal de cobertura aparente: los únicos RF que trazan la tarea son Ambiguo. El glosario sí
define «Tendencia», pero el veredicto del agente es insumo inmutable y un agente puede bajar D1.

**Aníbal 4 — 5.** RF-REG-07 admite el dispositivo personal, su CA-2 y RF-IAM-09 lo habilitan sobre
una cama que no es suya cuando tomó el caso, RF-IAM-01 lo atribuye y RF-REG-09 le devuelve la
confirmación de ejecución. El agente declara cerrada su frustración y no señala carencia.

**Aníbal 5 — 3.** RF-ESC-07 y RF-ESC-17 declaran la delegación y su retorno, pero ningún enunciado
declara que el delegado se entere de que quedó delegado —RF-ESC-26 informa a la jefatura— ni qué
ocurre con un caso ya acusado si la indisponibilidad se declara en el medio.

**Aníbal 6 — 5.** RF-SUP-03 declara exactamente los seis contenidos que la tarea necesita y los
entrega para las unidades que su ámbito comprendía en el periodo, que en su caso son dos sedes. Su
criterio de éxito queda satisfecho literalmente. Que la tarea penda de un solo RF es fragilidad de
diseño, no comportamiento ausente; se registra como brecha.

## Daño fuera de tarea — X_p

| Persona | RF marcados Estorba | Cuentan en X_p | No cuentan y por qué | X_p |
|---|---|---|---:|---:|
| Rodrigo | RF-TUR-24, RF-TUR-31, RF-TUR-39, RF-IAM-02 | los cuatro | — | 4 |
| Milagros | RF-TUR-28, RF-ESC-13, RF-IAM-02 | RF-TUR-28, RF-IAM-02 | RF-ESC-13 traza su tarea 4 en la matriz: su daño ya se cobró bajando esa tarea a 3 | 2 |
| Carmen | RF-TUR-06, RF-TUR-39, RF-DIA-18, RF-DIA-19, RF-ESC-07 | RF-DIA-18, RF-DIA-19, RF-ESC-07 | RF-TUR-06 traza su tarea 3 y RF-TUR-39 su tarea 4: cobrados dentro de esas tareas | 3 |
| Aníbal | RF-TUR-26, RF-DIA-23, RF-ESC-25, RF-IAM-07 | RF-TUR-26, RF-DIA-23, RF-ESC-25 | RF-IAM-07 traza sus tareas 1 y 4: cobrado dentro de ellas | 3 |

Detalle de los que cuentan:

- **Rodrigo.** RF-TUR-24 permite que un retiro comunicado por la Red con instante efectivo lo alcance
  en plena guardia. RF-TUR-31 convierte en pendiente de resolución el cambio que pactó de palabra.
  RF-TUR-39 puede vencer una solicitud mientras atiende a un paciente inestable sin avisarle a él.
  RF-IAM-02 le rechaza la nota sobre el paciente que tiene delante si nadie registró su asignación
  médica; ninguno de los cuatro figura en ninguna de las seis filas de Rodrigo de la matriz de
  trazabilidad.
- **Milagros.** RF-TUR-28 devuelve a la pared la copia impresa que la manda a llamar al médico
  equivocado. RF-IAM-02 le rechaza el registro sobre la cama de su colega cuando la cubre.
- **Carmen.** RF-DIA-18 y RF-DIA-19 le cargan la distribución de camas de cada turno de las 24 horas
  desde un horario administrativo de 08:00 a 16:00. RF-ESC-07 deja que un médico cambie de manos la
  cobertura clínica de su unidad sin su resolución y sin exigir que el delegado esté asignado a ella.
- **Aníbal.** RF-TUR-26 le reitera avisos de programación por sus medios de contacto fuera del
  esquema de severidad clínica. RF-DIA-23 le niega los eventos y la medicación del turno en curso por
  falta de una asignación médica que un localizable nunca tiene. RF-ESC-25 le entrega toda duda con
  la urgencia máxima, que es el mecanismo por el que deja de responder a todo.

## Recorrido del escenario clave y claridad del flujo

| Persona | ¿Se recorre entero? | Pasos sostenidos en Ambiguo | Puntos |
|---|---|---|---:|
| Rodrigo | Sí, en la trayectoria declarada | 8 (RF-ESC-01), 10 (RF-DIA-23), 12 (RF-DIA-12) | 2 |
| Milagros | Sí | 3 (RF-DIA-18), 5 (RF-ESC-03) | 2 |
| Carmen | Sí, en la trayectoria declarada | 6 (RF-TUR-35) | 2 |
| Aníbal | Sí | 7 (RF-REG-08) | 2 |

**Rodrigo — 2, no 0.** El agente declara que el flujo «puede cortarse en el paso 11 por RF-IAM-02 si
el paso 1 (RF-DIA-18) no ocurrió». La escala reserva el 0 para el recorrido en que «hay un paso que
ningún RF sostiene». El paso 1 sí lo sostiene un RF explícito y Sirve —RF-DIA-18—; lo que falta es
la vía alterna cuando ese acto no se ejecutó, que es comportamiento ausente y no un paso huérfano.
El recorrido se completa en su trayectoria declarada apoyado en tres Ambiguo. Se puntúa 2 y la
ausencia de vía alterna se registra como brecha de severidad crítica.

**Carmen — 2, no 0.** El agente declara que «el flujo también se corta por una rama»: si se agotan
los candidatos, ningún RF le deja cerrar la franja por autoridad. Esa rama no es la trayectoria del
escenario clave, que termina con el candidato aceptando, el cambio publicado y la confirmación de
lectura perseguida. En la trayectoria declarada todos los pasos se sostienen en RF explícitos, y el
paso central (6) descansa en RF-TUR-35, Ambiguo. El paso 12 descansa en RF-DIA-18, marcado Estorba,
que ya se cobró en `X_Carmen`. Se puntúa 2 y la rama sin salida se registra como brecha crítica.

**Milagros — 2.** El agente declara el recorrido completo con dos apoyos ambiguos, RF-DIA-18 en el
paso 3 y RF-ESC-03 en el paso 5, ambos dentro de los primeros treinta segundos.

**Aníbal — 2.** El agente declara el recorrido completo y sin corte, con un apoyo ambiguo en el paso
7 (RF-REG-08). RF-IAM-07 en el paso 5 y RF-DIA-23 en el paso 7 son Estorba, ya cobrados en `X_Aníbal`.

## Aritmética de D1

```
Puntaje_p = máx(0, Σ tareas_p − 2 × X_p) / 5 + Flujo_p

Rodrigo   Σ = 3+3+3+5+3+3 = 20   X = 4   máx(0, 20 − 8)  = 12   12/5 = 2,4   + 2 = 4,4
Milagros  Σ = 3+3+3+3+5+3 = 20   X = 2   máx(0, 20 − 4)  = 16   16/5 = 3,2   + 2 = 5,2
Carmen    Σ = 3+3+3+3+3+5 = 20   X = 3   máx(0, 20 − 6)  = 14   14/5 = 2,8   + 2 = 4,8
Aníbal    Σ = 3+3+1+5+3+5 = 20   X = 3   máx(0, 20 − 6)  = 14   14/5 = 2,8   + 2 = 4,8

promedio  = (4,4 + 5,2 + 4,8 + 4,8) / 4 = 19,2 / 4 = 4,8
D1        = 4,8 × 10 = 48,0
```

Ninguna persona tiene sus seis tareas en 0, de modo que el techo de 50 sobre D1 no se activa; el
valor computado queda por debajo de él por sí solo.

## Cobertura de P1, P2 y P3

| Problema | RF asociados | Comportamiento que lo resuelve | Tramo sin RF | Puntos |
|---|---|---|---|---:|
| P1 — Rotación de doctor | RF-DIA-01, RF-DIA-02, RF-DIA-03, RF-DIA-04, RF-DIA-07, RF-DIA-10, RF-DIA-12, RF-DIA-17, RF-DIA-18, RF-DIA-20, RF-DIA-24 | RF-DIA-01 impide cerrar la entrega con alguna cama sin diagnóstico vigente; RF-DIA-07 versiona el diagnóstico con autoría e instante; RF-DIA-20 registra la entrega cerrada; RF-DIA-02 y RF-DIA-10 la presentan al entrante sin depender del saliente; RF-DIA-03 señala la cama sin diagnóstico antes de aceptar; RF-DIA-17 y RF-DIA-24 cubren el turno que concluyó sin cerrar | Toda la cadena cuelga de la asignación médica vigente que solo RF-DIA-18 produce y que el enunciado pone en la coordinadora, cuya jornada es 08:00–16:00; ningún RF declara qué ocurre cuando esa asignación no existe a las 19:00 de un sábado, y sin ella RF-DIA-01 no tiene camas sobre las que exigir diagnóstico, RF-DIA-02 no tiene qué presentar y RF-IAM-02 rechaza el registro del entrante. Además RF-DIA-01 exige «diagnóstico vigente» y RF-DIA-03 señala la falta de «diagnóstico del turno anterior»: un diagnóstico de anteayer satisface el bloqueo sin que nadie haya evaluado esa cama en el turno que acaba | 50 |
| P2 — Medianoche | RF-ESC-01, RF-ESC-02, RF-ESC-03, RF-ESC-04, RF-ESC-06, RF-ESC-07, RF-ESC-08, RF-ESC-09, RF-ESC-12, RF-ESC-17, RF-ESC-20, RF-ESC-21, RF-ESC-23, RF-ESC-25, RF-REG-07, RF-IAM-04, RF-IAM-05, RF-IAM-08, RF-IAM-09 | RF-ESC-20 emite junto a la cama; RF-ESC-23 compone la cadena; RF-ESC-01 alcanza al responsable; RF-ESC-02 avanza sola sin acuse y RF-ESC-09 termina en la jefatura; RF-ESC-07 y RF-ESC-17 declaran y revierten la indisponibilidad; RF-ESC-03 adjunta el contexto; RF-IAM-04, RF-IAM-05 y RF-IAM-08 lo resuelven en el celular personal; RF-REG-07 y RF-IAM-09 registran la indicación a distancia | Ningún RF declara el acto por el que una cama adquiere su responsable clínico vigente. RF-ESC-01 es MUST y su respuesta entera es «alcanzar al responsable clínico vigente de esa cama»; RF-ESC-23 lo pone en primer lugar de la cadena; RF-IAM-02 enumera «responsabilidad clínica vigente» y «asignación médica vigente» como condiciones distintas, y las únicas vías declaradas son la delegación de RF-ESC-07 y la comunicación de la Red de RF-IAM-06. Tres de los cuatro agentes lo declaran por separado | 50 |
| P3 — Actualizaciones en tiempo real | RF-ESC-13, RF-ESC-16, RF-ESC-22, RF-REG-01, RF-REG-02, RF-REG-03, RF-REG-04, RF-REG-05, RF-ESC-08 | RF-REG-01, RF-REG-02 y RF-REG-05 incorporan el registro a pie de cama y lo preservan sin pérdida ni duplicación durante una desconexión; RF-ESC-22 alcanza junto a la cama a quien emitió el escalamiento; RF-ESC-16 ordena los avisos pendientes en cuatro clases | El tramo «notificaciones a múltiples médicos y enfermeras» tiene un solo RF, RF-ESC-13, y su enunciado declara expresamente que la actualización **aguarda la consulta de sus destinatarios**: no alcanza a nadie, espera. Milagros lo marcó Estorba y Rodrigo y Aníbal, Ambiguo. RF-ESC-22 solo alcanza a la enfermera que emitió el escalamiento, y ningún RF declara el alcance proactivo de una indicación nueva o un resultado crítico a los demás destinatarios | 50 |

```
D2 = (50 + 50 + 50) / 3 = 50,0
```

Ningún problema queda en 0, de modo que el techo de 60 sobre D2 no se activa.

## Requerimientos mal formados

| ID | Condición de D3 incumplida | Corrección propuesta |
|---|---|---|
| RF-TUR-16 | 8 — el criterio amplía el contrato | CA-1 exige que «la copia coincide con sus asignaciones», fidelidad que el enunciado no declara y que su RF gemelo RF-TUR-28 sí pone en el enunciado. Trasladar la fidelidad al enunciado: «…DEBE generarla como archivo histórico con exactamente las asignaciones de ese periodo, la unidad, el periodo, el instante de generación y su condición no operativa». |
| RF-TUR-39 | 8 — el criterio amplía el contrato | CA-2 decide, dentro del criterio, que una aceptación posterior al vencimiento no produce asignación; el enunciado solo dice «dejarla sin efecto» y RF-TUR-35 ordena asignar a todo candidato que acepta, sin excepción. Llevar la condición al enunciado de RF-TUR-35 —«CUANDO el candidato acepta una solicitud de cobertura vigente…»— y dejar CA-2 como demostración. |
| RF-DIA-02 | 5 — nombra estructura de datos | CA-3 sitúa el resultado «en los campos correspondientes de la entrega». Reformular: «…entonces ambos estados figuran en la entrega de esa cama». |

Los 115 RF restantes cumplen las ocho condiciones a la vez. Verificación de las condiciones
mecanizables sobre los 118: patrón EARS identificable en todos (91 de evento, 17 de borde, 5
ubicuos, 3 de estado, 1 de opción, 1 complejo); sujeto del DEBE «el sistema» en los 118 y un solo
DEBE por enunciado; al menos un criterio de aceptación en los 118; exactamente un par
Cuando/Entonces en cada uno de sus criterios; ningún mecanismo, producto ni topología nombrado —los
términos `dispositivo personal`, `dispositivo no institucional` y `copia imprimible` están definidos
en `docs/GLOSARIO.md` o son restricciones declaradas de las personas, y los parámetros ventilatorios
de RF-ESC-03 y RF-REG-08 son contenido clínico y no estructura de la solución—.

```
D3 = 115 / 118 × 100 = 97,4576… → 97,5
```

## Requerimientos huérfanos

| ID | Por qué no traza a nadie |
|---|---|
| — | Ninguno. Los 118 RF declaran persona y problema, las cuatro personas citadas existen en `Personas/` y los tres problemas citados existen en `README.md`. |

## Requerimientos mal ubicados

| ID | Por qué no es funcional | Documento que le corresponde |
|---|---|---|
| — | Ninguno. Ningún RF de `ReqFunc.MD` enuncia solo un umbral: los que se apoyan en una garantía de calidad —RF-ESC-02, RF-ESC-21, RF-REG-02, RF-TUR-26, RF-TUR-39— declaran el comportamiento y delegan el plazo a `ReqNoFunc.MD`, como el propio encabezado del documento anuncia. |

## Trazabilidad — D4

**Tramo de 70 puntos.** 118 de 118 RF declaran persona y problema, ambos existentes:
70 × 118/118 = **70,0**.

**Tramo de 30 puntos.** 24 de 24 tareas críticas obtuvieron al menos 1 punto en D1 —la más baja es
la tarea 3 de Aníbal, con 1—: 30 × 24/24 = **30,0**.

**Matrices internas contrastadas contra el cuerpo.**

| Matriz | Filas | Resultado |
|---|---:|---|
| Matriz de trazabilidad | 24 | Coincide. Cada RF citado existe y su campo `Persona` incluye a la persona de la fila |
| Cobertura de criterios de éxito | 23 | Una fila desfasada |
| Cobertura de problemas críticos | 3 | Coincide exactamente: P1 lista 77 RF y 77 declaran P1; P2 lista 37 y 37 lo declaran; P3 lista 9 y 9 lo declaran |
| Cobertura de las preguntas del enunciado | 6 | Coincide. Los RF citados existen y su enunciado responde la pregunta; las cinco referencias `RNF-*` existen en `ReqNoFunc.MD` |
| Requerimientos de origen normativo | 4 | Coincide |
| Decisión de tensiones | 5 | Una fila desfasada |
| Distribución de prioridad | 3 | Coincide: 60 MUST (50,8 %), 56 SHOULD (47,5 %), 2 COULD (1,7 %) sobre 118 |

**Filas desfasadas (−10 cada una):**

1. *Decisión de tensiones*, fila «Velocidad frente a completitud del registro». Afirma que «los demás
   componentes se registran una sola vez para su reutilización, evitando que completitud signifique
   reingreso». El cuerpo declara esa reutilización sin transcripción únicamente para enfermería
   (RF-DIA-08 y RF-DIA-11); ningún RF declara que la entrega médica se componga con lo que el médico
   ya registró durante el turno. La fila además cita RF-DIA-08, cuyo campo `Persona` es Milagros, como
   decisión de una tensión que es Rodrigo ↔ Carmen.
2. *Cobertura de criterios de éxito*, fila «Rodrigo · Registrar la nota de evolución cuesta menos que
   escribirla a mano → RF-DIA-07, `RNF-USA-01`». RF-DIA-07 declara la incorporación de la nota y el
   diagnóstico como nueva versión con autoría e instante y nada más: el cuerpo no sostiene comparación
   alguna de esfuerzo, y el propio agente de Rodrigo declara ese criterio sin cobertura.

```
D4 = 70,0 + 30,0 − 10 − 10 = 80,0
```

## Consistencia y tensiones — D5

**Tramo de 60 puntos — las cinco tensiones de `Personas/README.md`.**

| Tensión | ¿Decidida? | RF que la decide | Decisión |
|---|---|---|---|
| Velocidad frente a completitud del registro | Sí | RF-DIA-01, RF-DIA-20 | El cierre exige el diagnóstico vigente de cada cama asignada y nada más; ningún otro dato bloquea |
| Sensibilidad del escalamiento | Sí | RF-ESC-11, RF-ESC-25, RF-ESC-16, RF-ESC-24 | La enfermera escala sin clasificar y la duda recibe cadena y plazo de deterioro inmediato; la selectividad se preserva en la presentación, no en el plazo. Aníbal marca RF-ESC-25 Estorba: la tensión está decidida en su contra, que es decidirla |
| Autonomía de intercambio de turnos | Sí | RF-TUR-13, RF-TUR-06, RF-TUR-31, RF-TUR-32 | La coordinadora autoriza por alcance y periodo; lo cubierto se aplica sin resolución individual y lo no cubierto queda pendiente de la suya. Carmen marca RF-TUR-06 Estorba: decidida en su contra |
| Adopción voluntaria | Sí | RF-TUR-08, RF-TUR-28, RF-DIA-08, RF-DIA-11 | El sistema es la única fuente editable y la copia imprimible se concede como reflejo no editable; el registro de enfermería se reutiliza sin transcripción. El lado de Rodrigo queda sin decidir y se registra como brecha |
| Movilidad frente a control de datos | Sí | RF-IAM-04, RF-IAM-08, RF-IAM-05, RF-IAM-07 | Se admite el dispositivo personal; antes de identificarse el aviso expone solo sede, unidad, cama, severidad y motivo, y la identidad se recupera en el propio dispositivo |

5 × 12 = **60,0**. `tensiones_sin_decidir` = 0.

**Tramo de 40 puntos — hallazgos independientes (−10 cada uno, piso 0).**

| # | Clase | Hallazgo |
|---:|---|---|
| 1 | Contradicción | RF-TUR-35 (MUST) obliga a asignar a todo candidato que acepta una solicitud de cobertura, sin condición; RF-TUR-39 CA-2 declara que una aceptación posterior al vencimiento no produce asignación |
| 2 | Contradicción | RF-TUR-35 obliga a asignar al candidato que acepta y RF-TUR-01 (MUST) obliga a rechazar toda asignación que solape otro turno vigente en cualquier sede: si el candidato tomó otro turno mientras la solicitud esperaba, los dos mandan lo contrario y ningún enunciado declara cuál prevalece |
| 3 | Vocabulario inconsistente | RF-DIA-01 bloquea por «diagnóstico vigente» y RF-DIA-03 señala la falta de «diagnóstico del turno anterior»; el glosario define solo el primero y sin ancla temporal al turno, de modo que las dos expresiones no denotan lo mismo y el bloqueo puede satisfacerse con un diagnóstico de días atrás |
| 4 | Vocabulario inconsistente | RF-IAM-02 enumera «responsabilidad clínica vigente» y «asignación médica vigente» como condiciones distintas, mientras el glosario define «responsable clínico vigente» como quien responde «según la programación o una delegación activa» —es decir, derivándolo de lo mismo que produce la asignación médica—. RF-ESC-01, RF-ESC-08 y RF-ESC-23 dependen del término y ningún RF lo constituye |
| 5 | Duplicado encubierto | RF-DIA-02 y RF-DIA-21 declaran el mismo contenido para el mismo lector en momentos contiguos, y ya divergieron: RF-DIA-21 omite el diagnóstico vigente y los pendientes críticos que RF-DIA-02 incluye. Es exactamente la deriva que `docs/CONVENCIONES.md` §2 anticipa para dos copias de una regla |
| 6 | Vocabulario inconsistente | RF-ESC-11 asigna «el **estado** severidad por confirmar», pero el glosario declara que el estado de atención de un escalamiento tiene «exactamente los valores emitido, alcanzado, acusado, tomado, cerrado y agotado», y enumera «severidad por confirmar» entre los tres valores de **severidad**. El mismo término nombra dos categorías distintas |
| 7 | Historial en el cuerpo | RF-TUR-20 conserva dentro del requerimiento un párrafo que narra la corrección y cita el enunciado descartado —«el enunciado anterior —«asignarlo directamente»—»—, contra `docs/CONVENCIONES.md` §2 «Cero lápidas» y §10. El control M4 no lo detecta porque su patrón no cubre esa redacción |
| 8 | Historial en el cuerpo | La matriz «Decisión de tensiones», fila «Adopción voluntaria», redacta la decisión como cambio de estado —«La copia imprimible **deja de limitarse** a periodos cerrados»— en lugar de enunciar el estado vigente |

Ocho hallazgos independientes × 10 = 80 sobre un tramo de 40: el tramo queda en su piso, **0**. A
partir del cuarto hallazgo el tramo ya estaba agotado, de modo que el puntaje no depende de si el
séptimo y el octavo se cuentan por separado.

```
D5 = 60,0 + 0,0 = 60,0
```

El repositorio tiene glosario (`docs/GLOSARIO.md`, 59 términos), así que el techo de 80 no aplica. El
techo de 40 por conformidad unánime tampoco: exige que las cuatro coberturas percibidas alcancen 90
y las declaradas son 70, 78, 70 y 80.

## Priorización — D6

Los 118 RF declaran prioridad y los 118 la declaran dentro de MUST / SHOULD / COULD: **0 descuentos**
por el primer concepto. La distribución es 60 / 56 / 2, de modo que `prioridad_uniforme` es false y
el techo de 60 no aplica.

**MUST cuya ausencia no dejaría sin resolver un problema crítico ni descubierta una tarea crítica
(−5 cada uno):**

| ID | Por qué no merece MUST |
|---|---|
| RF-DIA-03 | Señala la cama sin diagnóstico previo antes de aceptar. Sostiene el criterio de éxito de Rodrigo, pero su ausencia no deja descubierta la tarea 1 —que conservan RF-DIA-02, RF-DIA-09, RF-DIA-10, RF-DIA-17 y RF-DIA-18— ni deja P1 sin resolver, porque RF-DIA-01 ya impide cerrar sin diagnóstico. Por el criterio que el propio `ReqFunc.MD` declara para SHOULD —«sostiene un criterio de éxito»— corresponde SHOULD |
| RF-DIA-05 | Presenta los cambios desde el último contacto. Sostiene el criterio de éxito de Rodrigo «ver qué cambió sin releer todo el historial», pero la tarea 2 conserva otros ocho RF y P1 queda resuelto sin él |
| RF-ESC-19 | Registra el cierre de la atención con su desenlace. La tarea 2 de Aníbal es «confirmar recepción y tomar el caso» y la cubren RF-ESC-04, RF-ESC-12 y RF-ESC-14; P2 es contactar rápido y manejar la indisponibilidad, y el desenlace no interviene en ninguna de las dos cosas |

Los 57 MUST restantes quedan justificados por una de tres vías: son la única cobertura declarada de
una tarea crítica en la matriz de trazabilidad (RF-ESC-08, RF-REG-05, RF-REG-08, RF-SUP-03,
RF-SUP-01, RF-ESC-13); su respuesta es el acto que la tarea crítica nombra literalmente y ningún otro
RF lo declara (RF-TUR-01, RF-TUR-03, RF-TUR-07, RF-TUR-09, RF-TUR-10, RF-TUR-11, RF-TUR-12,
RF-TUR-18, RF-TUR-20, RF-TUR-32, RF-TUR-35, RF-DIA-04, RF-DIA-06, RF-DIA-08, RF-DIA-11, RF-ESC-03,
RF-ESC-04, RF-ESC-07, RF-ESC-12, RF-ESC-20, RF-REG-03, RF-REG-04, RF-REG-06, RF-REG-07, RF-SUP-02);
o son un eslabón sin el cual la cadena que resuelve P1, P2 o P3 se rompe, incluida la producción de
un contenido que otro MUST declara en su contrato cerrado (RF-TUR-04, RF-TUR-19, RF-TUR-29,
RF-TUR-31, RF-DIA-01, RF-DIA-02, RF-DIA-07, RF-DIA-13, RF-DIA-14, RF-DIA-15, RF-DIA-18, RF-DIA-19,
RF-DIA-20, RF-DIA-25, RF-DIA-27, RF-ESC-01, RF-ESC-02, RF-ESC-06, RF-ESC-11, RF-ESC-15, RF-ESC-21,
RF-ESC-23, RF-ESC-25, RF-REG-01, RF-REG-02, RF-IAM-08).

```
D6 = 100 − 5 × 3 = 85,0
```

## Discrepancias entre agente y cómputo

| Persona | Computado ×10 | Percibida | Δ | Qué falla: el agente o las tareas críticas |
|---|---:|---:|---:|---|
| Rodrigo | 44 | 70 | 26 | El agente. Su análisis por tarea es riguroso —declara sin cobertura tres de sus cinco criterios de éxito— pero su autoinforme no descuenta ni esas carencias ni los cuatro RF que marcó Estorba fuera de sus tareas. La percibida mide el documento que le gustaría tener, no el que evaluó |
| Milagros | 52 | 78 | 26 | El agente. Declara seis necesidades no cubiertas, dos de ellas en los primeros treinta segundos de su escenario, y aun así se autoinforma en 78 |
| Carmen | 48 | 70 | 22 | El agente. Es la persona con más RF marcados Sirve —59 de 118— y aun así ninguna de sus seis tareas llega a 5 salvo la última: la abundancia de RF que le sirven no equivale a tareas resueltas, y la percibida confunde ambas cosas |
| Aníbal | 48 | 80 | 32 | El agente, con el mayor desvío de los cuatro. Declara «la tarea está cubierta» sobre su tarea 1 y en el mismo párrafo enumera lo que falta; su tarea 3 pende de un único RF que él mismo marcó Ambiguo |

Las cuatro desviaciones superan el umbral de 20 puntos y las cuatro apuntan en la misma dirección.
Eso no es ruido de un agente: es un sesgo del instrumento. La cobertura percibida se declara al final
del documento, después de haber enumerado necesidades no cubiertas y riesgos, y ninguno de los cuatro
agentes la deriva de lo que acaba de escribir. Prevalece el valor computado en los cuatro casos.

## Tensiones sin decidir

| Tensión | Por qué ningún RF la resuelve |
|---|---|
| — | Ninguna. Las cinco tensiones de `Personas/README.md` se deciden en al menos un RF. Se registra, como brecha y no como tensión sin decidir, que la decisión de «Adopción voluntaria» cubre el lado de la programación y el de enfermería y deja sin decidir el del registro médico de Rodrigo |

## Evaluaciones de agente ausentes o inválidas

| Persona | Qué falta |
|---|---|
| — | Ninguna. Las cuatro evaluaciones están presentes, completas y con vocabulario cerrado |

## Contrastes cruzados

1. **Discrepancia percibido/computado.** Aplica a las cuatro personas; ver la tabla anterior. Prevalece
   el valor computado.
2. **Conformidad unánime.** No aplica. Exige que las cuatro coberturas percibidas alcancen o superen
   el 90 %; las declaradas son 70, 78, 70 y 80. Además `tensiones_sin_decidir` es 0. El techo de 40
   sobre D5 no se activa por esta vía.
3. **Necesidad no cubierta sin brecha.** Las 25 necesidades no cubiertas que los cuatro agentes
   declaran están recogidas en la tabla de brechas —tres de ellas son la misma necesidad declarada por
   tres agentes distintos y se consolidan en la brecha 1—. Ninguna queda silenciada y ninguna se
   refuta.

## Brechas encontradas

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---:|---|---|---|---|
| 1 | Milagros, Carmen, Rodrigo · P2 | Ningún RF declara el acto por el que una cama adquiere su responsable clínico vigente. RF-ESC-01, RF-ESC-08 y RF-ESC-23 lo presuponen; RF-IAM-02 lo enumera aparte de la asignación médica; las únicas vías declaradas son la delegación de RF-ESC-07 y la comunicación de la Red de RF-IAM-06 | `veredicto-milagros`, `veredicto-carmen`, `veredicto-rodrigo` | Crítica |
| 2 | Rodrigo, Carmen · P1 | RF-DIA-18 y RF-DIA-19 ponen la asignación de camas de cada turno en la coordinadora, cuya jornada es 08:00–16:00, y ningún RF declara qué ocurre cuando esa asignación no existe al inicio de un turno nocturno o de fin de semana | `veredicto-carmen`, `veredicto-rodrigo`, `auditoría` | Crítica |
| 3 | Milagros, Aníbal, Rodrigo · P3 | Ningún RF alcanza proactivamente a médicos y enfermeras ante una indicación nueva o un resultado crítico: RF-ESC-13, único RF de ese tramo, declara que la actualización aguarda la consulta de sus destinatarios | `veredicto-milagros`, `veredicto-anibal`, `auditoría` | Crítica |
| 4 | Carmen · P1 | Ningún RF permite asignar a un profesional a una franja descubierta sin su aceptación: si nadie acepta y la guardia empieza en horas, no queda vía dentro del sistema | `veredicto-carmen` | Crítica |
| 5 | Carmen · P1 | RF-TUR-35 obliga a asignar a todo candidato que acepta y RF-TUR-39 CA-2 niega la asignación tras el vencimiento; ningún enunciado declara cuál prevalece | `auditoría`, `veredicto-carmen` | Alta |
| 6 | Carmen · P1 | RF-TUR-35 obliga a asignar y RF-TUR-01 obliga a rechazar la asignación que solape otro turno vigente en cualquier sede; el conflicto no está resuelto en ningún enunciado | `auditoría`, `veredicto-carmen` | Alta |
| 7 | Rodrigo · P1 | Ningún RF declara una vista agregada de la asignación médica completa: RF-DIA-02 presenta por cama y el criterio de las diez camas en quince minutos queda sin cobertura | `veredicto-rodrigo` | Alta |
| 8 | Rodrigo · P1 | Ningún RF declara que la entrega médica se componga reutilizando sin transcripción lo ya registrado durante el turno, como RF-DIA-08 y RF-DIA-11 sí declaran para enfermería | `veredicto-rodrigo` | Alta |
| 9 | Rodrigo · P1 | Ningún RF declara cómo el resultado de un estudio se incorpora al episodio: RF-REG-06 solo presenta los «disponibles» | `veredicto-rodrigo` | Alta |
| 10 | Rodrigo · P1 | Ningún RF declara la verificación de identidad en el equipo compartido de la estación de enfermería; RF-IAM-08 solo cubre el dispositivo personal | `veredicto-rodrigo` | Media |
| 11 | Rodrigo · P1 | El vencimiento de una solicitud de cobertura solo se avisa a la coordinadora (RF-TUR-40): el candidato puede aceptarla tarde creyéndose cubriendo una guardia que no tiene | `veredicto-rodrigo` | Media |
| 12 | Milagros · P3 | RF-IAM-02 rechaza su registro sobre una cama fuera de su asignación de cuidado y ningún RF prevé el relevo entre las dos enfermeras del turno | `veredicto-milagros` | Alta |
| 13 | Milagros · P2 | Nada le advierte que su escalamiento emitido sin conexión todavía no ha salido: RF-ESC-21 lo preserva pero no la informa | `veredicto-milagros` | Media |
| 14 | Milagros · P1 | No existe para enfermería el equivalente de RF-DIA-17: si el turno anterior no cerró su entrega, nada se lo advierte ni le diferencia una entrega más antigua | `veredicto-milagros` | Media |
| 15 | Milagros · P2 | Ningún RF le da vía propia para consultar el respaldo de lo que avisó: RF-SUP-04 lo entrega al coordinador y RF-SUP-03 no declara si su asignación de cuidado cuenta como ámbito de responsabilidad | `veredicto-milagros` | Media |
| 16 | Carmen · P1 | Ningún RF declara quién define el patrón de cobertura requerido de la unidad —cuántas franjas y cuántos profesionales por franja—, del que dependen RF-TUR-09, RF-TUR-10, RF-TUR-07 y el indicador de cobertura | `veredicto-carmen` | Alta |
| 17 | Carmen · P1 | Ningún RF declara de dónde salen las reglas de jornada y descanso ni el vínculo laboral vigente que RF-TUR-02 y RF-TUR-03 invocan, siendo el régimen laboral una restricción explícita de la persona | `veredicto-carmen` | Alta |
| 18 | Carmen · P1 | Ningún RF le avisa cuando el retiro de un rotante comunicado por la Red (RF-TUR-24) deja una franja descubierta; RF-TUR-07 se lo muestra solo si consulta | `veredicto-carmen` | Media |
| 19 | Carmen · P1 | RF-SUP-01 no reporta las entregas cerradas que el médico entrante nunca aceptó, aunque RF-DIA-09 registre esa aceptación | `veredicto-carmen` | Media |
| 20 | Carmen · P1 | Ningún RF le da visibilidad sobre el cumplimiento de las entregas de enfermería, que también son entregas de turno de su unidad | `veredicto-carmen` | Media |
| 21 | Aníbal · P2 | Ningún RF declara que el delegado nombrado en RF-ESC-07 se entere de su delegación o pueda aceptarla; RF-ESC-26 informa a la jefatura | `veredicto-anibal` | Alta |
| 22 | Aníbal · P2 | RF-DIA-23 condiciona los eventos y la medicación del turno en curso a una asignación médica vigente que un médico de guardia localizable nunca tiene | `veredicto-anibal` | Alta |
| 23 | Aníbal · P2 | RF-TUR-26 invoca «los medios de contacto vigentes» y ningún RF declara cómo se mantienen vigentes, que es exactamente el número viejo por el que nadie lo ubicó | `veredicto-anibal` | Media |
| 24 | Aníbal · P2 | Ningún RF declara si el acuse de recibo puede darse desde el propio aviso de RF-IAM-04 antes de verificar identidad o si RF-IAM-07 lo impide | `veredicto-anibal` | Alta |
| 25 | Aníbal · P2 | Ningún RF declara un piso de información con el que decidir ir o no ir cuando la identidad verificada no está vigente y la señal no alcanza para recuperarla | `veredicto-anibal` | Alta |
| 26 | Aníbal · P2 | El balance hídrico que RF-ESC-03 adjunta no declara su periodo, y lo que la decisión de madrugada necesita es el del día | `veredicto-anibal` | Media |
| 27 | Rodrigo, Milagros · P1 | RF-DIA-06 permite que «un profesional» retire una marca de inestabilidad sin acotar sobre qué camas, de modo que un pendiente crítico puede desaparecer sin que quien lo dejó se entere | `veredicto-rodrigo` | Media |
| 28 | Milagros · P2 | RF-ESC-03 no declara qué ocurre cuando parte del contexto obligatorio todavía no existe: leído como condición de salida, convierte el escalamiento en un formulario | `veredicto-milagros` | Alta |
| 29 | Rodrigo · P1 | El «turno en curso» de RF-DIA-23 no distingue el turno médico del turno de enfermería | `veredicto-rodrigo` | Media |
| 30 | Rodrigo · P1 | RF-DIA-12 no enumera los datos obligatorios cuya ausencia bloquea el cierre, y de esa lista depende que cerrar el turno cueste dos minutos o veinte | `veredicto-rodrigo` | Media |
| 31 | Carmen · P1 | RF-TUR-13 no declara qué puede ser un «alcance» de la autorización reutilizable, y de su amplitud depende cuánta cobertura queda entregada por adelantado | `veredicto-carmen` | Alta |
| 32 | Rodrigo, Carmen · P1 | «Diagnóstico vigente» (RF-DIA-01) y «diagnóstico del turno anterior» (RF-DIA-03) no denotan lo mismo y el glosario solo define el primero, sin ancla temporal al turno | `auditoría`, `veredicto-rodrigo` | Alta |
| 33 | Rodrigo · P1 | RF-DIA-02 y RF-DIA-21 duplican el mismo contenido para el mismo lector y ya divergieron: RF-DIA-21 omite el diagnóstico vigente y los pendientes críticos | `auditoría` | Media |
| 34 | Milagros, Aníbal · P2 | «Severidad por confirmar» se usa como estado del escalamiento en RF-ESC-11 y como valor de severidad en el glosario, que además declara cerrados y distintos ambos conjuntos de valores | `auditoría` | Media |
| 35 | Carmen · P1 | RF-TUR-16 CA-1 exige que la copia coincida con las asignaciones del periodo, fidelidad que el enunciado no declara | `auditoría` | Baja |
| 36 | Rodrigo · P1 | RF-DIA-02 CA-3 sitúa el resultado «en los campos correspondientes de la entrega», nombrando estructura de datos en lugar de comportamiento observable | `auditoría` | Baja |
| 37 | Carmen · P1 | RF-TUR-20 conserva dentro del requerimiento un párrafo que narra su corrección y cita el enunciado descartado | `auditoría` | Baja |
| 38 | Carmen · P1 | La fila «Adopción voluntaria» de la matriz de tensiones redacta la decisión como cambio de estado —«deja de limitarse»— en lugar del estado vigente | `auditoría` | Baja |
| 39 | Rodrigo, Carmen · P1 | La decisión de la tensión «Velocidad frente a completitud» promete que los componentes se registran una vez para su reutilización; el cuerpo solo lo declara para enfermería, y la fila cita RF-DIA-08, cuya persona es Milagros, para una tensión Rodrigo ↔ Carmen | `auditoría` | Alta |
| 40 | Rodrigo · P1 | La matriz de criterios de éxito declara satisfecho «registrar la nota cuesta menos que a mano» con RF-DIA-07, que solo declara la incorporación de la nota con autoría e instante | `auditoría` | Media |
| 41 | — | Tres MUST no reservados: RF-DIA-03 y RF-DIA-05 sostienen criterios de éxito y RF-ESC-19 refuerza una tarea ya cubierta | `auditoría` | Baja |
| 42 | Aníbal · P2 | Sus tareas 3 y 6 penden de un único RF cada una —RF-REG-08 y RF-SUP-03—, y la primera además de un término que su enunciado no fija | `veredicto-anibal` | Media |
| 43 | Rodrigo, Carmen · P1 | La tensión «Adopción voluntaria» se decide para la programación y para el registro de enfermería, y queda sin decidir para el registro médico: cinco actos separados por cama sin reutilización declarada | `auditoría` | Alta |
| 44 | Instrumento | Las cuatro coberturas percibidas superan lo computado en más de 20 puntos (26, 26, 22 y 32): los agentes no derivan su autoinforme de las carencias que acaban de enumerar | `auditoría` | Media |

**Brechas abiertas: 44** — 4 críticas, 16 altas, 16 medias, 5 bajas, y la 41 y la 44 sobre el
instrumento y la prioridad.

## Cálculo global

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 48,0 | 30 % | 14,40 |
| D2 Cobertura de problemas críticos | 50,0 | 25 % | 12,50 |
| D3 Verificabilidad y forma | 97,5 | 20 % | 19,50 |
| D4 Trazabilidad | 80,0 | 10 % | 8,00 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,00 |
| D6 Priorización | 85,0 | 5 % | 4,25 |
| **Suma** | | | **64,65** |

```
Global = 48,0×0,30 + 50,0×0,25 + 97,5×0,20 + 80,0×0,10 + 60,0×0,10 + 85,0×0,05
       = 14,40 + 12,50 + 19,50 + 8,00 + 6,00 + 4,25
       = 64,65 → 64,7
```

## Veredicto

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 64,7 % | no |
| 2 | D1 | ≥ 80,0 | 48,0 | no |
| 3 | Persona más baja | ≥ 7,0/10 | 4,4 (Rodrigo) | no |
| 4 | D2 | ≥ 80,0 | 50,0 | no |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | sí |

Cuatro de las cinco condiciones fallan. **FAILED.**
