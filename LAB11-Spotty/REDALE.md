# Spotty Análisis REDALE

Versión de trabajo consolidada al 22 de octubre de 2026. Las seis partes se revisaron por separado durante la conversación. Esta copia incorpora la corrección posterior de los cierres escalonados. El diagrama evolutivo se conserva como borrador para revisión antes del cierre de los dos PDFs solicitados.

**Fuente de verdad:** laboratorio de Canvas de la semana 11 y material teórico de las semanas 1 a 11. Los valores de matrícula, peso de archivos, memoria, horarios y objetivos internos se presentan como supuestos ilustrativos, no como datos del caso.

# R — Requerimientos del caso Spotty

## Problema y usuarios

La universidad corrige actualmente las entregas de Arquitectura con sandboxes y workers en una laptop. Necesita extender el servicio a otros cursos y absorber muchas entregas próximas al cierre.

El **docente usa la aplicación desktop** para consultar correcciones y gestionar las notas. El **alumno usa la aplicación mobile** para enviar código u otras tareas y consultar su estado. El envío desde mobile es una **decisión de diseño solicitada para esta propuesta**: el enunciado menciona expresamente la consulta de estado, pero no especifica desde dónde se envía la entrega.

## Requisitos funcionales

| ID | Requisito |
|---|---|
| RF1 | Permitir que el alumno envíe desde mobile código o archivos de una tarea y reciba una confirmación cuando la entrega haya quedado guardada. |
| RF2 | Permitir reanudar una carga interrumpida, especialmente para archivos grandes de IA o conexiones móviles inestables. |
| RF3 | Corregir tres clases de trabajo: pruebas unitarias/código de Programación, diagramas/código de Arquitectura y modelos/ejecuciones GPU de IA. |
| RF4 | Mostrar al alumno el estado de su entrega, incluidas espera, ejecución, reintento, demora por falta de capacidad y finalización. |
| RF5 | Permitir al docente consultar desde desktop la entrega, el resultado y los errores de corrección para gestionar la nota. |
| RF6 | Los reintentos de una corrección no deben generar resultados finales duplicados. |
| RF7 | Mantener operativo el corrector existente durante la incorporación del sistema nuevo. |

## Requisitos no funcionales

| ID | Calidad que debe protegerse | Criterio propuesto para evaluar el diseño |
|---|---|---|
| RNF1 | **Plazo de entrega de notas** | Los docentes deben entregar las notas en un máximo de **dos días**. La espera, preparación del entorno, ejecución, reintentos y revisión docente deben caber dentro de ese plazo; terminar la corrección automática no basta para acreditar su cumplimiento. |
| RNF2 | **Escalabilidad** | Soportar el pico de entregas de los últimos 30 minutos y aumentar por separado los workers de Programación, Arquitectura e IA según el atraso de cada cola. |
| RNF3 | **Aislamiento y seguridad** | Ejecutar cada entrega no confiable en un sandbox independiente, con límites de CPU, memoria, tiempo y almacenamiento, sin acceso a credenciales del sistema. |
| RNF4 | **Durabilidad y consistencia** | No perder una entrega ya confirmada al alumno. Si Spot interrumpe un worker, el trabajo podrá repetirse sin publicar dos correcciones finales. |
| RNF5 | **Continuidad del estado** | Reflejar en mobile un cambio de estado en **hasta 60 segundos** en operación normal, incluso cuando la corrección espere o sea reintentada. |
| RNF6 | **Uso justo de recursos** | Un curso con muchos alumnos no debe impedir indefinidamente que se corrijan entregas de otros cursos. |
| RNF7 | **Observabilidad** | Medir entregas recibidas, tiempo en cola, duración total, uso de memoria, interrupciones Spot, falta de capacidad y trabajos en riesgo de incumplir el plazo. |

## Plazo de notas y objetivo interno

**Requisito del caso:** el máximo de **dos días** corresponde a la entrega de las notas por el docente. Incluye la espera por recursos, preparación de imágenes, ejecución, reintentos, revisión docente y entrega de la nota.

**Supuesto para medir el plazo:** para los cálculos de esta propuesta interpretamos los dos días como **48 horas desde el cierre de cada tarea**. El enunciado no especifica desde qué evento se cuentan; este punto debe confirmarse antes de fijar una condición definitiva de aceptación.

**Objetivo interno propuesto:** completar el **99 % de las correcciones automáticas en 36 horas desde el cierre**, cuando haya capacidad Spot suficiente, para reservar 12 horas a la revisión docente y entrega de notas. Este objetivo no exime al resto de las entregas del plazo máximo del caso.

**Riesgo de cumplimiento:** una escasez prolongada de Spot puede impedir entregar las notas dentro del plazo. Conservar los trabajos, mostrar la espera y emitir alertas protege la continuidad y permite actuar, pero no equivale a cumplir el plazo ni lo amplía.

## Restricciones del caso

| ID | Restricción | Condición del caso |
|---|---|---|
| RC1 | **Uso de AWS Spot** | Solo se aprobó AWS Spot para los sandboxes/workers de la ampliación. El enunciado no prescribe el alojamiento del backend, las colas o la base de datos. |
| RC2 | **Ejecución en sandbox** | Cada ejecución procesa código no confiable de un alumno dentro de un sandbox. El aislamiento debe contemplar código ineficiente o con consumo excesivo de memoria. |
| RC3 | **Canales de acceso** | Los docentes acceden desde desktop y los alumnos consultan el estado de sus entregables desde una app mobile. El envío desde mobile sigue siendo una decisión de esta propuesta. |
| RC4 | **Capacidad GPU** | Las correcciones de IA que requieren GPU deben ejecutarse con recursos GPU compatibles. |

## Características de la carga y del entorno

**Situación inicial:** el corrector existente atiende únicamente Arquitectura mediante workers y sandboxes en una laptop local. La ampliación debe atender también Programación e IA.

| Tipo de curso | Trabajos corregidos | P99 de ejecución indicado |
|---|---|---|
| Programación | Pruebas unitarias y código | **1 minuto** |
| Arquitectura | Diagramas y código | **10 minutos** |
| IA | Modelos y ejecuciones con GPU | **40 minutos o más** |

Estos P99 describen tiempos de ejecución; no incluyen toda la espera ni la revisión docente y no son límites máximos para cada trabajo individual.

- **Imágenes por curso:** cada curso tiene su propia imagen base de **3–5 GB**. Ese tamaño corresponde al entorno de ejecución, no al archivo que entrega el alumno.
- **Picos de llegada:** el uso no es constante; casi todas las entregas llegan en los **últimos 30 minutos antes del cierre de su tarea**. El enunciado no fija un porcentaje exacto ni indica que todos los cursos cierren simultáneamente.
- **Demanda desigual:** algunos cursos tienen más alumnos y generan mayor demanda; no debe asumirse una carga uniforme entre cursos.
- **Consumo de recursos:** deben considerarse la memoria y las ejecuciones ineficientes de los alumnos, además del tiempo de procesamiento y la GPU cuando corresponda.
- **Interrupción y escasez de Spot:** AWS puede reclamar una instancia con **dos minutos de aviso** o no tener capacidad Spot del tipo solicitado; el caso indica que las GPU son las más escasas.

## Supuestos cuantitativos iniciales

El enunciado no proporciona matrícula ni tamaños de archivo. Para poder estimar en la siguiente etapa, usaremos este **escenario ilustrativo**, sin presentarlo como dato de Canvas:

| Tipo | Cursos y demanda supuestos | Entregas por cierre | Archivo por entrega | Memoria por ejecución |
|---|---|---:|---:|---:|
| Programación | 8 cursos de 120 alumnos y 4 muy demandados de 300 | 2160 | 1–10 MB | 0,5–2 GB de RAM |
| Arquitectura | 5 cursos de 100 alumnos y 1 muy demandado de 250 | 750 | 5–30 MB | 2–4 GB de RAM |
| IA | 1 curso de 60 alumnos y 1 muy demandado de 140 | 200 | 50–500 MB | 16–32 GB de RAM y 12–24 GB de memoria GPU |

En total, el ejemplo considera **20 cursos y 3110 entregas** en la jornada ilustrativa. Cada tarea puede cerrar a una hora distinta. Interpretaremos «casi todas en los últimos 30 minutos» como **90 % de las entregas de cada tarea**, no como 3110 entregas simultáneas. Los cursos muy demandados tienen más alumnos dentro de cada categoría; no se supone una carga uniforme.

Para probar el comportamiento ante falta de Spot usaremos escenarios de **6 horas sin capacidad CPU**, **24 horas sin GPU** y un caso extremo de **48 horas sin GPU**. Son pruebas de resistencia propuestas, **no pronósticos sobre AWS**. Si la capacidad GPU falta durante demasiado tiempo, el plazo de notas no puede garantizarse únicamente con workers Spot.

# E — Estimar la carga y los recursos

## 1. Qué estamos estimando

Tomamos el escenario aprobado de **20 cursos y una entrega por alumno**, con **3110 entregas en total**. Es una jornada ilustrativa de alta demanda, no una matrícula informada por Canvas. Cada tarea tiene su propia hora de cierre.

| Cierre ilustrativo | Programación | Arquitectura | IA | Total |
|---|---:|---:|---:|---:|
| 18:00 | 240 | 100 | 60 | 400 |
| 20:00 | 660 | 350 | 0 | 1010 |
| 22:00 | 540 | 200 | 0 | 740 |
| 23:59 | 720 | 100 | 140 | 960 |
| **Total de la jornada** | **2160** | **750** | **200** | **3110** |

En cada cierre suponemos que el **90 %** llega durante sus últimos 30 minutos. Por cantidad de solicitudes, el mayor pico es el de **20:00**: aproximadamente **909 entregas en media hora**, o **0,51 entregas por segundo en promedio**. Los trabajos recibidos a distintas horas pueden seguir ejecutándose cuando llega el cierre siguiente; por eso hay que observar también la acumulación en las colas.

## 2. Tamaño supuesto de una entrega

Los tamaños corresponden a **lo que sube el alumno**, no a la imagen base del curso.

| Tipo | Ejemplo concreto de entregable | Rango supuesto | Tamaño usado en el cálculo |
|---|---|---:|---:|
| Programación | ZIP con archivos fuente, configuración y pruebas unitarias | 1–10 MB | 5 MB |
| Arquitectura | Diagramas en PDF o formato editable, documento y código de apoyo | 5–30 MB | 15 MB |
| IA | Notebook, scripts, configuración y pesos de un modelo de curso | 50–500 MB | 200 MB |

Con una entrega por alumno, el volumen ilustrativo es **10,8 GB** de Programación, **11,25 GB** de Arquitectura y **40 GB** de IA: **62,05 GB** en la jornada, antes de resultados, versiones o copias de seguridad.

El cierre de **23:59** concentra menos entregas que el de 20:00, pero más datos porque incluye IA: unos **29,79 GB en 30 minutos**, equivalentes a **132 Mb/s de subida promedio**. Como el ritmo dentro de esa media hora no será uniforme, usaremos **300 Mb/s como capacidad inicial de referencia** para la ruta de carga y comprobaremos el valor con pruebas. Las cargas mobile grandes deberán poder reanudarse.

Cada uno de los 20 cursos tiene además una **imagen base de 3–5 GB**: guardar una versión por curso requiere **60–100 GB**. Esa cifra es separada de los archivos de los alumnos. Cuando un worker descarga una imagen que aún no tiene, consume tiempo y red adicionales; el número de copias dependerá de cuántos hosts la necesiten.

## 3. Trabajo de corrección

Para un cálculo preliminar usamos los P99 del caso como tiempo de referencia por trabajo: **1 minuto** en Programación y **10 minutos** en Arquitectura. Para IA adoptamos **60 minutos como supuesto**, ya que el caso indica **40 minutos o más**. Añadimos un **25 % de margen ilustrativo** para preparación y reintentos.

**Workers simultáneos estimados = redondear hacia arriba[(entregas × minutos por trabajo × 1,25) ÷ 2160 minutos].** Los 2160 minutos representan el objetivo interno propuesto de **36 horas** descrito en R, separado del máximo de dos días para entregar las notas.

| Tipo | Trabajo estimado, incluido el margen | Workers simultáneos preliminares |
|---|---:|---:|
| Programación | 45 horas de CPU | 2 CPU |
| Arquitectura | 156,25 horas de CPU | 5 CPU |
| IA, suponiendo 60 min por trabajo | 250 horas de GPU | 7 GPU |

Estas cifras dimensionan **una jornada intensa completa**, aunque sus cierres estén escalonados. Son un primer cálculo, no una garantía: faltan mediciones reales de duración, memoria, descarga de imágenes y capacidad Spot. Si los cierres se reparten entre varios días, la capacidad necesaria puede bajar.

IA es especialmente sensible a la duración real: con trabajos de **40, 60 o 90 minutos**, el mismo cálculo pide respectivamente **5, 7 u 11 workers GPU**. Además, el curso de IA muy demandado reúne **140 de las 200 entregas de IA**; necesitará una política que evite dejar sin atención al otro curso.

## 4. Prueba de estrés: falta de GPU Spot

El aviso de recuperación de **dos minutos** no permite terminar un trabajo GPU de 40 minutos o más. La arquitectura tendrá que conservar su estado y repetirlo o retomarlo cuando sea posible.

Para medir la escasez, suponemos como prueba extrema que **los 200 trabajos de IA ya están pendientes** y no hay GPU Spot durante **24 horas desde un cierre de referencia**. Si después solo aparecen los **7 GPU** del cálculo inicial, procesar las 250 horas de trabajo tomaría otras **35,7 horas**: unas **59,7 horas desde ese cierre**. Con el supuesto de cómputo del plazo definido en R, la corrección automática ya excedería las 48 horas y faltaría además la revisión docente. Harían falta alrededor de **11 GPU disponibles durante las 24 horas restantes** solo para completar esa carga de ejecución antes de 48 horas; esa cifra no acredita la entrega de notas a tiempo ni conserva el objetivo interno de 36 horas. AWS Spot puede no ofrecer esa capacidad.

El diseño debe **mostrar la espera y alertar temprano al docente** cuando la proyección de corrección y revisión ponga en riesgo el plazo de notas. Si no se entregan las notas dentro del máximo de dos días, se registra un incumplimiento; informar la demora no amplía ese plazo.

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
