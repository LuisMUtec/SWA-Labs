# D — Diseñar el servicio

## Tipo de arquitectura elegido

Proponemos un **backend modular con corrección asíncrona**. La aplicación responde cuando una entrega queda guardada, mientras la corrección continúa en segundo plano. Así, una ejecución de IA de 40 minutos o más no mantiene abierta la solicitud del alumno.

El backend atiende las dos aplicaciones con permisos diferentes: **mobile** permite al alumno enviar una tarea y consultar su estado; **desktop** permite al docente consultar entregas, correcciones e incidencias para gestionar las notas. No necesitamos crear un servicio distinto por cada pantalla.

## Recorrido de una entrega nueva

1. El alumno inicia el envío desde mobile. El backend crea un identificador de entrega y permite subir el archivo directamente a un almacenamiento duradero. Una carga incompleta puede reanudarse.
2. Solo cuando el archivo termina de guardarse, el sistema confirma **«Entrega recibida»** y registra curso, alumno, tarea y hora. No se envía a corregir un archivo parcial.
3. Un planificador clasifica el trabajo como **Programación**, **Arquitectura** o **IA** y lo coloca en su cola correspondiente. Dentro de cada tipo considera el tiempo de espera y evita que un curso muy demandado ocupe indefinidamente toda la capacidad.
4. Un worker Spot compatible toma el trabajo. Descarga la imagen base del curso, prepara un **sandbox nuevo para esa ejecución** y aplica los límites de memoria, CPU/GPU, tiempo y almacenamiento.
5. El worker guarda el resultado y los registros necesarios. El sistema actualiza el estado una sola vez como resultado final. El docente lo consulta desde desktop y el alumno ve el estado actualizado desde mobile.

Los archivos de los alumnos y los resultados se guardan en **almacenamiento de objetos**; una **base de datos** conserva identificadores, estados y referencias a esos archivos. Las **colas duraderas** conservan los trabajos pendientes. El diagrama podrá usar S3, una base de datos y SQS como ejemplos concretos de estas funciones, sin presentar esa elección como una exigencia textual del lab.

## Estados visibles

| Estado interno | Mensaje comprensible para el alumno |
|---|---|
| Archivo aún en carga | «Subiendo entrega» |
| Archivo guardado y trabajo registrado | «Entrega recibida» |
| Trabajo pendiente o sin instancia compatible | «En espera»; si la demora es relevante, «Esperando capacidad para corregir» |
| Imagen y sandbox en preparación, o corrección ejecutándose | «Corrección en curso» |
| Worker interrumpido y trabajo devuelto a la cola | «La corrección se reanudará» |
| Resultado guardado | «Corrección lista» |
| Fallo que requiere intervención | «Requiere revisión» |

El docente verá además el motivo técnico, los intentos y el riesgo de exceder el plazo. Un aviso de falta de GPU **no se mostrará como si la tarea ya estuviera corregida**.

## Transición desde la laptop existente

Un **enrutador por curso y tarea** decidirá si una entrega va al corrector *legacy* o al nuevo. Un adaptador pequeño permitirá enviar al sistema actual los trabajos que todavía le corresponden y registrar su estado y resultado en la vista común. Moveremos cursos al sistema nuevo por etapas y comprobaremos su comportamiento antes de cambiar el siguiente.

La laptop solo podrá ser respaldo de los trabajos que **realmente sabe corregir**. No la dibujaremos como alternativa para modelos GPU ni para todos los nuevos cursos. Esta transición gradual aplica el patrón *Strangler* explicado en semana 11.

## Qué ocurre si falla un worker

El trabajo conserva su identificador aunque cambie de worker. Ante el aviso Spot de dos minutos, el worker deja de aceptar tareas nuevas e intenta guardar un avance **solo si esa corrección lo permite**. Si no es posible, el trabajo vuelve a la cola y se ejecuta de nuevo. El sistema registra los intentos y acepta **un solo resultado final**.

Si no existe capacidad Spot compatible —sobre todo GPU—, el trabajo permanece guardado y en espera; se informa la demora al alumno y se alerta al docente cuando el plazo corre riesgo. Un trabajo GPU no se trasladará automáticamente a un worker CPU suponiendo que dará el mismo resultado.

# A — Armar el modelo de datos

Usaremos una **base de datos relacional** para los registros de entregas, trabajos y notas. Los archivos del alumno, resultados y registros extensos se guardarán en almacenamiento de objetos. Cada curso tendrá su imagen base en un registro de imágenes; no guardaremos esos archivos de 3–5 GB dentro de una tabla.

| Registro | Datos principales | Para qué sirve |
|---|---|---|
| **Curso** | ID, nombre, tipo de corrección, versión de imagen base, perfil de recursos, ruta *legacy* o nueva | Configurar cómo se corrigen sus tareas y permitir la migración por curso. |
| **Tarea** | ID, curso, fecha y hora de cierre, plazo de notas | Registrar el cierre y la fecha límite de entrega de notas. Con el supuesto de cómputo definido en R, esa fecha límite es 48 horas después del cierre de la tarea. |
| **Acceso al curso** | Usuario, curso, rol de alumno o docente | Asegurar que el alumno vea sus entregas y el docente gestione únicamente sus cursos. |
| **Entrega** | ID, tarea, alumno, versión, ubicación y tamaño del archivo, comprobante de integridad, hora de recepción | Identificar el archivo que quedó guardado. Una nueva entrega del mismo alumno crea una nueva versión. |
| **Trabajo** | ID, entrega, tipo CPU/GPU, estado, curso, plazo, versión exacta de la imagen, referencia *legacy* si aplica | Seguir la corrección aunque cambie de worker o se interrumpa. Guardar la versión de imagen evita que un reintento use un entorno distinto. |
| **Intento** | Trabajo, número de intento, worker, inicio, fin, causa de interrupción, avance guardado si existe | Distinguir una corrección de sus ejecuciones y diagnosticar fallas Spot. |
| **Resultado** | Trabajo, ubicación de corrección y registros, puntaje sugerido si corresponde, fecha de finalización | Conservar **un único resultado final por trabajo**. El puntaje automático no sustituye necesariamente la revisión docente. |
| **Nota** | Resultado, docente, nota final, fecha de publicación | Registrar la decisión del docente y comprobar el plazo de dos días. |
| **Evento de estado** | Trabajo, estado, hora y motivo | Reconstruir lo ocurrido y mostrar un estado actualizado en mobile. |

## Relaciones principales

Un **curso** tiene muchas **tareas**; una tarea recibe muchas **entregas**. Cada versión de una entrega genera **un trabajo de corrección**. Un trabajo puede tener **varios intentos**, pero como máximo **un resultado final**. El docente puede publicar una **nota** a partir de ese resultado. Los eventos conservan el historial de cambios de estado.

## Reglas para evitar pérdidas y duplicados

- La app mobile recibe «Entrega recibida» **solo después** de que el archivo esté completo y su registro se haya guardado.
- Si la conexión móvil repite la misma solicitud, un identificador de solicitud permite reconocerla sin crear otra entrega por accidente. Una nueva versión enviada voluntariamente sí queda registrada aparte.
- Si un worker Spot desaparece, se crea otro **intento del mismo trabajo**. Ningún intento adicional puede crear una segunda nota o sobrescribir un resultado final ya aceptado.
- El registro **Trabajo** es la referencia durable de lo pendiente. Si falla el envío a la cola, un proceso de conciliación puede volver a anunciar los trabajos que siguen «en cola».
- Cada trabajo guarda su **curso y fecha límite**; estos datos permiten planificar con justicia cuando un curso muy demandado acumula muchas entregas.

# L — Listar los componentes

La solución tendrá un **backend de control modular** y workers separados para ejecutar correcciones. «Modular» significa que en el diagrama distinguiremos funciones; no implica desplegar un microservicio por cada caja.

| Etapa | Componente | Responsabilidad |
|---|---|---|
| **0 — Actual** | Laptop, sandboxes y workers existentes | Corregir las entregas de Arquitectura que hoy soporta el sistema. Es la base de la transición. |
| **1 — Transición** | App mobile del alumno | Enviar archivos, reanudar cargas y consultar el estado de sus propias entregas. |
| **1 — Transición** | App desktop del docente | Consultar entregas, resultados, incidencias y notas de sus cursos. |
| **1 — Transición** | Backend de control y enrutador | Autenticar, confirmar entregas y dirigir cada trabajo por **curso y tarea** al sistema *legacy* o al nuevo. También responde las consultas de estado. |
| **1 — Transición** | Adaptador *legacy* | Conectar la laptop con el registro común de entregas y resultados sin sustituir de golpe su corrector. |
| **1 — Transición** | Almacenamiento de objetos y base de datos | Guardar archivos y resultados por un lado; relaciones, estados, intentos y notas por otro. |
| **2 — CPU Spot** | Planificador y colas duraderas de Programación y Arquitectura | Mantener trabajos pendientes separados, asignarlos según espera y plazo, y evitar que un curso grande ocupe toda la capacidad. |
| **2 — CPU Spot** | Registro de imágenes por curso | Conservar las imágenes base de 3–5 GB y su versión. Un reintento usa la misma versión que el primer intento. |
| **2 — CPU Spot** | Workers CPU Spot y sandboxes | Corregir Programación y Arquitectura con perfiles y límites distintos. Cada trabajo ejecuta código no confiable en un sandbox propio. |
| **3 — GPU y operación completa** | Cola y workers GPU Spot | Ejecutar trabajos de IA sin bloquear las colas CPU. |
| **3 — GPU y operación completa** | Conciliación, monitoreo y alertas | Detectar trabajos atascados, interrupciones Spot, falta de capacidad, uso de memoria y riesgo de exceder el plazo. |

S3 para objetos, SQS para colas, un registro de imágenes y EC2 Spot para ejecución son **opciones concretas para rotular el diagrama**. El dato obligatorio del caso es que los **sandboxes/workers usen Spot**; el enunciado no prescribe productos para los demás componentes.

## Conexiones que deben verse en la arquitectura final

1. **Envío:** mobile → backend → archivo guardado y entrega registrada → confirmación al alumno.
2. **Corrección nueva:** planificador → cola del tipo correspondiente → worker Spot → imagen del curso → sandbox → resultado guardado.
3. **Consulta:** mobile → backend → estado; desktop → backend → entrega, resultado e incidencias.
4. **Transición:** enrutador → adaptador → laptop para los trabajos que aún siguen en *legacy*; su resultado regresa al registro común.
5. **Interrupción Spot:** aviso al worker → dejar de tomar trabajos → guardar avance si es posible → registrar intento → devolver el trabajo pendiente a su cola.
6. **Sin capacidad Spot:** el trabajo permanece guardado y en espera; monitoreo alerta al docente si su plazo está en riesgo.

La laptop **solo sirve como alternativa para trabajos que ya puede corregir**. Una ejecución GPU de IA no se redirigirá allí cuando falten instancias Spot.

## Caminos críticos y puntos a vigilar

Para **confirmar una entrega**, deben funcionar la app, el backend, el almacenamiento del archivo y el registro de la entrega. La corrección puede esperar; la confirmación nunca debe depender de que ya exista un worker.

Para **terminar una corrección**, el camino pasa por planificador, cola, capacidad Spot compatible, imagen, sandbox y almacenamiento del resultado. Sus posibles cuellos de botella son la espera por GPU, la memoria, la descarga de imágenes y los cursos con muchos trabajos. La laptop es además un punto único de falla mientras un curso dependa exclusivamente de ella.

El diagrama mostrará estas conexiones en una **línea superior de etapas 0→1→2→3** y ampliará abajo la **arquitectura final completa**, con flechas distintas para el flujo normal, la consulta mobile y las fallas.

# E — Escalar la arquitectura

## Cuándo y qué escalar

El sistema no aumentará todos sus componentes a la vez. Medirá, por tipo de corrección y por curso, **trabajos pendientes, edad de la cola, duración estimada, memoria usada y tiempo restante hasta el plazo**. Los cierres de tareas ocurren a distintas horas: cada cálculo incluirá el trabajo que sigue pendiente de cierres anteriores.

El planificador estimará periódicamente:

**Workers necesarios ≈ horas de trabajo pendiente ÷ horas disponibles hasta el objetivo interno**, redondeando hacia arriba y añadiendo el margen del 25 % usado en E — Estimar.

Escalará **por separado** los pools Spot de Programación, Arquitectura e IA. Como referencia para la jornada intensa estimada, el cálculo preliminar dio **2 workers CPU de Programación, 5 CPU de Arquitectura y 7 GPU de IA**. Es una solicitud de capacidad, no una afirmación de que AWS Spot la tendrá disponible.

## Preparación para cada cierre

Las fechas de las tareas permiten anticipar la demanda. Antes de un cierre conocido, el sistema solicita capacidad Spot compatible y prepara **solo las imágenes de los cursos que tendrán trabajos próximos**. Una imagen base descargada en un host puede reutilizarse allí, pero su copia local se perderá si AWS recupera ese host. Fuera de los periodos de carga, los workers terminan los trabajos activos y la capacidad se reduce para controlar el costo.

Dentro de cada pool, los cursos se atienden por turnos; los trabajos con plazo más cercano reciben prioridad. Un curso muy demandado puede recibir más capacidad cuando hay trabajadores libres, pero no debe ocuparlos todos mientras otros cursos compatibles esperan.

## Si AWS avisa que recuperará una instancia en dos minutos

1. El worker **deja de aceptar trabajos nuevos**.
2. Registra qué intento estaba ejecutando y trata de guardar un avance **si ese programa admite un punto de recuperación que quepa en el tiempo disponible**.
3. Si el resultado no quedó guardado como final, el trabajo vuelve a su cola. El siguiente worker usa la **misma versión de imagen** y retoma el avance disponible o ejecuta nuevamente la corrección.
4. El alumno ve que la corrección sigue pendiente; el docente puede consultar la interrupción. El identificador del trabajo evita publicar dos resultados finales.

Los **dos minutos son un aviso, no tiempo suficiente para terminar** una corrección GPU de 40 minutos o más. Un error repetible por exceder memoria o tiempo se distingue de una interrupción Spot: no se reintentará indefinidamente con el mismo límite. Tras intentos automáticos acotados, se marcará para revisión del docente.

## Si no hay capacidad Spot compatible

El archivo, el trabajo y su estado permanecen guardados. El sistema intenta obtener **otros tipos de instancia Spot compatibles y otras zonas disponibles**; una ejecución GPU no pasa a CPU por el solo hecho de faltar GPU. Si sigue sin haber capacidad, se muestra «Esperando capacidad» y se recalcula la fecha probable de término. Se alerta al docente desde que la proyección de corrección rebasa el objetivo interno de **36 horas** o, considerando la revisión docente, pone en riesgo la entrega de notas dentro de **48 horas** bajo el supuesto de R. La espera y la alerta no amplían el plazo del caso.

El escenario de E — Estimar muestra el riesgo: con **200 trabajos de IA de 60 minutos**, el margen supuesto eleva la carga a **250 horas GPU**. Si faltan GPU durante **24 horas desde el cierre de referencia** y todos esos trabajos están pendientes, los **7 GPU** inicialmente previstos tardarían otras **35,7 horas**: alrededor de **59,7 horas desde ese cierre**, sin incluir la revisión docente. Harían falta aproximadamente **11 GPU durante las 24 horas restantes** solo para completar la ejecución antes de 48 horas; aún debe caber la revisión y entrega de notas. La escasez prolongada de Spot es un **riesgo de incumplimiento del plazo**, no una excepción al requisito.

## Cómo comprobaremos el diseño

| Prueba de arquitectura | Resultado esperado |
|---|---|
| Simular muchas entregas en los 30 minutos anteriores a **distintos** cierres | Se conservan todas las entregas confirmadas y crece el pool que tiene trabajo pendiente. |
| Interrumpir un worker durante una corrección | El trabajo permanece registrado, se reintenta y se publica como máximo un resultado final. |
| Mantener GPU Spot sin capacidad durante 24 horas | Los trabajos muestran espera, se actualiza la proyección de corrección y revisión, y se alerta al docente si peligra el plazo de notas; la alerta no cuenta como entrega de notas. |
| Ejecutar código que excede memoria o tiempo | El sandbox detiene esa ejecución sin afectar otras entregas. |
| Consultar estados desde mobile durante el pico | El alumno ve el estado de su propia entrega; objetivo normal de actualización: **hasta 60 segundos**. |
| Comprobar la entrega de notas desde el cierre de cada tarea | Con el supuesto de R, se verifica que la entrega de la nota ocurra dentro de 48 horas. Se cuentan espera, corrección, reintentos y revisión; una alerta o un resultado automático no acreditan por sí solos el cumplimiento. |

Los tableros mostrarán tiempo de espera y tiempo total **P50, P95 y P99**, trabajos por curso, interrupciones Spot, falta de capacidad, uso de CPU/RAM/GPU y demora al preparar imágenes. Estas mediciones permitirán identificar el cuello de botella real antes de aumentar componentes adicionales.

## Fuentes del curso consultadas

- Laboratorio: `Arquitectura.2026.II-LAB.12.docx`, archivo 4951716 de Canvas.
- Teoría: materiales de semanas 1, 2, 3, 5, 6, 7, 10 y 11 descargados de Canvas para la revisión; las referencias directas de REDALE y migración gradual proceden de semanas 3 y 11.
- Diagrama editable: ocho escenas `.excalidraw` incluidas en este paquete; versión vectorial reunida en `Diagrama_evolutivo_Spotty_Excalidraw_profesional_borrador.pdf`.
