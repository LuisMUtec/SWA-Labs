# Feature Specification: RemoteSchooly

**Feature Branch**: `main`

**Created**: 2026-09-02

**Status**: Ready for architecture

**Input**: Educación semanal para pueblos remotos del Perú con Internet limitado, materiales
producidos en Lima y una reducción demostrable de al menos 40 % en el consumo de tokens de IA.

## User Scenarios & Testing

### User Story 1 - Publicar una semana de curso con gasto de IA controlado (Priority: P1)

Una profesora de Lima prepara un paquete semanal, decide cuándo usar IA, revisa el resultado y
publica únicamente material aprobado. El uso de IA queda medido contra una línea base comparable,
sin impedir que la docente escriba o edite manualmente.

**Why this priority**: Sin material correcto y aprobado no existe nada que distribuir. Además, la
reducción de tokens del 40 % es la única meta cuantitativa explícita del enunciado.

**Independent Test**: Con un conjunto fijo de tareas y fuentes, una docente completa el mismo
material con la ruta base y la ruta optimizada. Ambas salidas aprueban la misma rúbrica; la segunda
consume al menos 40 % menos tokens de entrada más salida por unidad aprobada.

**Acceptance Scenarios**:

1. **Given** una docente con fuentes aprobadas y presupuesto disponible, **When** solicita ayuda de
   IA y aprueba el resultado, **Then** el consumo queda atribuido a la tarea y el contenido aún
   requiere aprobación humana antes de publicarse.
2. **Given** una tarea equivalente a contenido ya aprobado, **When** la docente intenta generarlo de
   nuevo, **Then** puede reutilizar o adaptar ese resultado sin pagar una generación completa nueva.
3. **Given** que el servicio de IA no está disponible o se agotó el presupuesto, **When** la docente
   edita el material, **Then** puede terminarlo y publicarlo sin IA.

---

### User Story 2 - Recibir el paquete semanal con Internet intermitente (Priority: P1)

Un profesor de provincia sincroniza los cursos asignados cuando existe conexión. Si el enlace se
corta, conserva lo ya verificado y continúa después. Solo ve el paquete como listo cuando está
completo y coincide con la versión publicada desde Lima.

**Why this priority**: Es la condición que distingue al caso de una plataforma educativa web
convencional y la que permite que la clase ocurra en una localidad remota.

**Independent Test**: Se transfiere un paquete conocido, se corta el enlace al 10 %, 50 % y 90 %, y
se reanuda. En los tres casos el resultado final es idéntico al original y nunca aparece listo un
paquete parcial.

**Acceptance Scenarios**:

1. **Given** un paquete semanal asignado y una conexión inestable, **When** la sincronización se
   interrumpe, **Then** el progreso verificado se conserva y la próxima sesión continúa desde allí.
2. **Given** una transferencia completa, **When** un archivo no coincide con el manifiesto,
   **Then** el paquete permanece no disponible y el profesor ve qué debe recuperarse.
3. **Given** una versión anterior completa y una nueva aún parcial, **When** empieza la clase,
   **Then** la versión anterior sigue utilizable hasta que la nueva esté verificada.

---

### User Story 3 - Aprender sin depender de Internet (Priority: P2)

Un alumno accede desde la red local de su escuela al material semanal ya sincronizado, aun cuando
el enlace externo está caído. Su avance se conserva localmente y se envía al centro cuando vuelve
la conexión, sin duplicar entregas.

**Why this priority**: La entrega técnica solo tiene valor si termina en una experiencia de clase
utilizable para el alumno.

**Independent Test**: Con Internet desconectado y un paquete listo en la escuela, un alumno abre
todos los recursos obligatorios, completa una actividad y luego sincroniza su avance una sola vez al
restablecer la conexión.

**Acceptance Scenarios**:

1. **Given** un paquete listo en la escuela y sin Internet, **When** el alumno entra a la red local,
   **Then** puede abrir los recursos obligatorios de la semana.
2. **Given** una actividad terminada sin Internet, **When** vuelve la conexión, **Then** el avance se
   registra una vez aunque el envío se reintente.
3. **Given** que el dispositivo del alumno no puede reproducir un recurso pesado, **When** consulta
   la lección, **Then** existe una alternativa de bajo consumo que conserva el objetivo pedagógico.

---

### User Story 4 - Gobernar cobertura y presupuesto sin invadir contenido personal (Priority: P3)

El Gobierno configura escuelas, asignaciones y presupuestos; observa qué semana llegó correctamente
a cada sede y si el ahorro de tokens cumple la meta. Solo recibe datos agregados de participación y
nunca los prompts ni las respuestas personales de alumnos.

**Why this priority**: El Gobierno encarga y financia el programa, pero su supervisión no debe
convertirse en acceso irrestricto a datos educativos o de autoría.

**Independent Test**: Con escuelas en estados asignado, sincronizando, listo y con error, el tablero
muestra la cobertura correcta, el ahorro normalizado y las excepciones de presupuesto, sin exponer
prompts, respuestas de alumnos ni contenido de actividades individuales.

**Acceptance Scenarios**:

1. **Given** varias escuelas con estados distintos, **When** el Gobierno consulta una semana,
   **Then** ve la cobertura por sede, curso y versión, incluida la causa accionable de cada error.
2. **Given** consumo de IA registrado, **When** consulta el indicador, **Then** ve el ahorro contra la
   línea base y la calidad de las unidades comparadas.
3. **Given** actividad estudiantil sincronizada, **When** consulta participación, **Then** recibe
   agregados y no contenido personal.

### Edge Cases

- El enlace cambia repetidamente entre conectado y desconectado durante un archivo grande.
- Llega primero una versión nueva del manifiesto y después fragmentos de una versión anterior.
- El almacenamiento de la sede se llena durante la sincronización.
- Lima revoca una versión mientras una sede está desconectada.
- Dos docentes publican para el mismo curso, semana y sede.
- Una misma actividad offline se reenvía después de varios reinicios del nodo local.
- Un resultado de IA viene vacío, excede el límite de salida o no cita las fuentes usadas.
- La docente modifica manualmente un resultado reutilizado y crea una nueva unidad aprobada.
- Una escuela pasa varios días sin conexión y acumula telemetría de más de una semana.
- Varios alumnos comparten dispositivo y deben conservar sesiones y avances separados.

## Requirements

### Functional Requirements

#### Identidad y autoridad

- **FR-001**: El sistema MUST aplicar permisos distintos para Gobierno, Alumno, Profesor de Lima y
  Profesor de Provincia, y MUST rechazar cualquier acción fuera del rol activo.
- **FR-002**: El Gobierno MUST poder registrar sedes, cursos, semanas, asignaciones y presupuestos
  de tokens sin editar el contenido pedagógico.
- **FR-003**: El Profesor de Lima MUST poder crear, editar, revisar y aprobar material sin usar IA.
- **FR-004**: El Profesor de Provincia MUST acceder solo a los paquetes asignados a sus sedes y
  cursos.
- **FR-005**: El Alumno MUST acceder solo a los cursos y al avance que le correspondan.

#### Autoría, IA y publicación

- **FR-006**: Toda ayuda de IA ofrecida por la plataforma MUST requerir una acción explícita del
  Profesor de Lima y MUST permanecer separada de la publicación.
- **FR-007**: Ningún resultado de IA MUST publicarse sin aprobación humana registrada.
- **FR-008**: Toda solicitud de IA de la plataforma MUST registrar tokens de entrada, tokens de
  salida, tokens reutilizados, docente, curso, tarea, unidad de material, fecha y versión de la
  política de consumo.
- **FR-009**: Antes de enviar una solicitud de IA, el Profesor de Lima MUST conocer su presupuesto
  restante y el límite aplicable de entrada y salida.
- **FR-010**: El sistema MUST ofrecer reutilizar una unidad previamente aprobada cuando la intención
  y las fuentes coincidan, dejando la decisión final a la docente.
- **FR-011**: El Profesor de Lima MUST poder aceptar, editar, rechazar o regenerar una propuesta de
  IA y registrar el resultado que finalmente fue aprobado.
- **FR-012**: El sistema MUST impedir que datos personales o respuestas de alumnos formen parte de
  una solicitud de IA.
- **FR-013**: El sistema MUST mantener una línea base versionada de tokens para un conjunto fijo de
  tareas y MUST comparar la ruta optimizada contra las mismas tareas y la misma rúbrica de calidad.
- **FR-014**: El ahorro de tokens MUST calcularse como `1 - tokens_optimizados / tokens_base`, usando
  entrada más salida por unidad aprobada; cambios de precio o de cantidad publicada MUST quedar fuera.
- **FR-015**: El sistema MUST alertar al Profesor de Lima y al Gobierno cuando el ahorro acumulado
  comparable sea menor a 40 %, sin bloquear la autoría manual.
- **FR-016**: Solo una versión aprobada del material MUST poder convertirse en paquete semanal.

#### Paquete semanal y sincronización

- **FR-017**: Cada publicación MUST producir un paquete inmutable identificado por curso, semana,
  audiencia, versión y fecha de vigencia.
- **FR-018**: Cada paquete MUST incluir un manifiesto con la lista completa de recursos obligatorios,
  tamaño, versión y huella verificable de cada recurso.
- **FR-019**: El sistema MUST impedir dos versiones activas para la misma combinación de curso,
  semana, audiencia y sede.
- **FR-020**: El Profesor de Provincia MUST poder iniciar o programar la sincronización de sus
  paquetes asignados cuando exista conexión.
- **FR-021**: Una transferencia interrumpida MUST conservar cada fragmento ya verificado y MUST
  continuar desde el último fragmento válido.
- **FR-022**: Una nueva versión MUST reutilizar los recursos idénticos ya verificados en la sede en
  lugar de transferirlos otra vez.
- **FR-023**: Un paquete MUST aparecer como `Listo` solo después de verificar todos los recursos
  obligatorios contra el manifiesto de la misma versión.
- **FR-024**: Un recurso ausente o corrupto MUST mantener el paquete en `Incompleto` y MUST indicar
  qué recurso debe recuperarse.
- **FR-025**: La última versión completa MUST seguir disponible mientras su reemplazo esté parcial,
  salvo que haya sido revocada explícitamente.
- **FR-026**: El Profesor de Provincia MUST ver versión, semana, vigencia, tamaño, progreso y estado
  de cada paquete asignado.
- **FR-027**: Una revocación MUST propagarse en la siguiente conexión y MUST impedir nuevas aperturas
  de esa versión después de recibida.
- **FR-028**: La falta de conexión externa MUST NOT borrar paquetes completos ni avances locales.

#### Clase y progreso offline

- **FR-029**: El Profesor de Provincia MUST poder abrir y presentar un paquete `Listo` desde la red
  local de la sede sin conexión a Internet.
- **FR-030**: El Alumno MUST poder abrir los recursos obligatorios de un paquete `Listo` desde la red
  local de la sede sin conexión a Internet.
- **FR-031**: Cada recurso audiovisual obligatorio MUST incluir una alternativa de bajo consumo que
  conserve el mismo objetivo pedagógico.
- **FR-032**: El Alumno MUST poder guardar localmente avance y entregas mientras no exista conexión.
- **FR-033**: El sistema MUST mantener los avances pendientes en una bandeja local hasta recibir
  confirmación del centro.
- **FR-034**: Reenviar una misma entrega MUST producir un solo registro de avance en el centro.
- **FR-035**: El Profesor de Provincia MUST poder distinguir alumnos sincronizados, pendientes y con
  error sin ver respuestas de cursos ajenos.

#### Gobierno, medición y auditoría

- **FR-036**: El Gobierno MUST ver por sede, curso y semana los estados `Asignado`, `Sincronizando`,
  `Listo`, `Incompleto` y `Revocado`, con la última actualización recibida.
- **FR-037**: El Gobierno MUST ver tokens base, tokens optimizados, ahorro porcentual, cantidad de
  unidades comparables y resultado de calidad por periodo.
- **FR-038**: El Gobierno MUST administrar presupuestos y excepciones de tokens por programa, curso
  y periodo, y toda excepción MUST dejar actor, motivo y vigencia.
- **FR-039**: El Gobierno MUST recibir participación estudiantil agregada por sede, curso y semana,
  sin prompts, respuestas individuales ni contenido de entregas.
- **FR-040**: El sistema MUST auditar publicación, revocación, asignación, cambio de presupuesto y
  transición de estado del paquete con actor y fecha.
- **FR-041**: Toda afirmación de cobertura del Gobierno MUST distinguir `sin reporte reciente` de
  `no entregado`; la ausencia de telemetría MUST NOT contarse como fracaso confirmado.

### Key Entities

- **Actor**: identidad, rol activo, sedes y cursos autorizados.
- **Sede**: escuela remota, zona horaria, capacidad local y último contacto conocido.
- **Curso**: área, grado, audiencia, docente responsable y calendario.
- **Semana de curso**: intervalo pedagógico que agrupa material y asignaciones.
- **Unidad de material**: contenido revisable con fuentes, versión, estado de aprobación y autoría.
- **Paquete semanal**: versión inmutable asignable a sedes.
- **Manifiesto**: inventario verificable de todos los recursos de un paquete.
- **Asignación**: relación entre paquete, sede, curso y vigencia.
- **Sesión de sincronización**: estado por recurso y fragmento, última confirmación y error.
- **Avance**: progreso o entrega de un alumno con identificador idempotente y estado de sincronización.
- **Registro de uso de IA**: tokens y contexto de una tarea de autoría, sin datos de alumnos.
- **Línea base de tokens**: conjunto versionado de tareas, fuentes, calidad y consumo comparable.
- **Presupuesto de tokens**: límite, consumo, periodo y excepciones autorizadas.
- **Evento de auditoría**: actor, acción, objeto, momento y resultado.

## Success Criteria

### Measurable Outcomes

- **SC-001**: El 100 % de los paquetes que figuren como `Listo` coincide con su manifiesto y no
  contiene recursos obligatorios ausentes o corruptos.
- **SC-002**: Una transferencia cortada al 10 %, 50 % o 90 % se reanuda sin empezar desde cero y
  termina con el mismo contenido que la versión publicada.
- **SC-003**: Profesores de Provincia y alumnos completan sus recorridos principales con el enlace
  de Internet desconectado después de que el paquete fue sincronizado.
- **SC-004**: La ruta optimizada usa al menos 40 % menos tokens de entrada más salida por unidad
  aprobada que la línea base, sobre el mismo conjunto de tareas y sin reducir el resultado de calidad.
- **SC-005**: El 100 % de las solicitudes de IA originadas en la plataforma aparece en el registro de
  consumo o queda rechazada antes de llegar al proveedor.
- **SC-006**: El tablero del Gobierno distingue correctamente los cinco estados de entrega y no
  presenta sedes sin reporte reciente como entregas fallidas.
- **SC-007**: Ninguna vista gubernamental contiene prompts, respuestas individuales de alumnos ni
  contenido de entregas.
- **SC-008**: Los cuatro caminos felices están representados en el diagrama final y cada requisito
  tiene al menos un componente responsable en la matriz de trazabilidad.
- **SC-009**: El EVAL de requisitos alcanza al menos 8.0/10 con los cuatro veredictos de persona y
  todas las citas resolviendo a requisitos existentes.

## Assumptions

- [ASSUMPTION: Cada sede dispone de al menos un equipo administrado por el profesor —portátil o
  mini-PC— con almacenamiento local y una red Wi-Fi/LAN utilizable dentro de la escuela.]
- [ASSUMPTION: Los paquetes se publican semanalmente y se asignan por curso, grado y sede.]
- [ASSUMPTION: El conjunto de comparación de IA contiene al menos 30 unidades aprobadas y conserva
  tareas, fuentes y rúbrica entre la línea base y la variante optimizada.]
- [ASSUMPTION: La calidad pedagógica la aprueba un Profesor de Lima con una rúbrica común; el sistema
  no reemplaza ese juicio.]
- [ASSUMPTION: La primera versión no incluye videollamadas, clases en vivo ni edición colaborativa en
  tiempo real, porque contradicen la restricción de conectividad del caso.]
- [ASSUMPTION: La primera versión no promete 100 % de disponibilidad ni despliegue multi-región;
  sí promete integridad del paquete que marque como listo.]
- [ASSUMPTION: El canal principal del alumno es la red local de la escuela; guardar material en su
  dispositivo es una conveniencia, no una precondición para enseñar.]
