# Spotty Arquitectura para la corrección académica

Spotty amplía el corrector académico de una laptop para recibir entregas de varios cursos, corregirlas con minions Spot y permitir que el docente revise y entregue las notas dentro del plazo del caso.

**Propuesta:** backend modular con corrección asíncrona, recursos separados por tipo de trabajo, estado durable y transición gradual desde el corrector existente.

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

## Tipo de arquitectura y módulos

Proponemos un **backend modular con corrección asíncrona**. El alumno recibe confirmación cuando el archivo completo y su registro quedan guardados; la corrección continúa en segundo plano. El resultado automático se entrega al docente, quien revisa y publica la nota.

El backend agrupa cuatro responsabilidades: **Identidad**, **Entregas**, **Coordinación de corrección** y **Resultados y notas**. Son módulos lógicos; las cajas no obligan a desplegar un microservicio por función. Los minions que ejecutan código de alumnos se despliegan separados del backend, en instancias Spot compatibles.

La división sigue el método de las demostraciones Top-Down: empezar por usuarios y requerimientos, seguir los datos y descomponer las responsabilidades necesarias. El diagrama principal identifica el tipo de arquitectura y el recorrido crítico de negocio.

## Identidad y acceso

El **Login Service** valida identidad y cuenta habilitada. Todas las operaciones de entrega, consulta y publicación comprueban el rol y la pertenencia al curso. El alumno consulta sus propias entregas; el docente revisa y publica las notas de sus cursos.

El módulo de **Registro de usuarios** crea o habilita cuentas y asigna rol y cursos. Se propone un **alta institucional autorizada**: el alumno no puede otorgarse el rol de docente. Esta forma de alta es una decisión del diseño que debe acordarse con la universidad; el enunciado no exige registro público ni especifica un proveedor de identidad.

Esta separación hace explícitos los controles que antes se resumían como «API + auth». Se apoya en el Login Service que el profesor dibuja en Top-Down II `[05:03]` y en la agrupación de autenticación y autorización del módulo de seguridad de semana 7.

## Recorridos por requerimiento

**RF1 — Envío y confirmación.** El alumno autenticado inicia el envío con un identificador de solicitud. Entregas registra la intención, recibe o coordina la carga y verifica que el archivo esté completo. Guarda el registro de entrega y el trabajo pendiente; solo entonces devuelve **«Entrega recibida» y entregaId** al alumno. Repetir la misma solicitud no crea otra entrega accidental. Una nueva versión enviada voluntariamente se registra como otra versión.

Si el archivo se guardó pero falla el registro, no se confirma la recepción. Si el registro ya existe y falla el anuncio a la cola, el trabajo durable permite a la conciliación volver a anunciarlo. La confirmación no depende de que ya haya un minion libre.

**RF3 — Corrección.** Coordinación clasifica el trabajo según curso y perfil: Programación, Arquitectura o IA. Lo coloca en su cola correspondiente. Un minion compatible toma el trabajo, prepara la versión de imagen fijada, inicia un sandbox y registra el intento. El minion de confianza recoge la salida y publica el resultado; el código del alumno no escribe directamente en la BD de control ni recibe credenciales del sistema.

**RF4 — Consulta y estados.** El alumno consulta entregaId. Resultados y notas comprueba el acceso, lee el estado durable y responde a la app. El recorrido cubre recibida, en cola, esperando capacidad, ejecutando, reintentando, resultado listo y requiere revisión. El objetivo de actualización normal de 60 segundos sigue siendo un objetivo propuesto, como se declaró en R.

**RF5 — Revisión y nota.** El docente autenticado consulta las entregas de sus cursos, obtiene resultado y errores, revisa la corrección y solicita publicar la nota. El sistema guarda la nota y confirma su publicación. El plazo se verifica con la entrega de la nota; un resultado automático disponible todavía no completa ese recorrido.

**RF6 — Final único.** Cada trabajo conserva jobId y registra sus intentos. La aceptación del resultado comprueba de forma transaccional que el intento sigue vigente y que el trabajo aún no tiene un final aceptado. Un intento obsoleto o una finalización repetida se rechazan sin sobrescribir el resultado ni crear otra nota. Los archivos de salida se identifican por trabajo e intento.

## Instancia Spot, minion y sandbox

La **instancia Spot** es el host reemplazable. El **minion** es el proceso de confianza que obtiene trabajos, prepara el entorno y supervisa la ejecución. El **sandbox** es el entorno aislado donde corre el código no confiable del alumno; se crea uno nuevo para cada ejecución.

Como punto de partida se propone **un minion activo y un sandbox simultáneo por instancia Spot**. Al terminar una tarea, el host puede atender otra con un sandbox nuevo. Esta elección facilita atribuir recursos y recuperar fallos, con el costo de capacidad ociosa cuando una tarea usa poco del host. La concurrencia se ajustará después de medir; no es una regla universal del curso.

| Perfil | Recursos ilustrativos del avance | Configuración de ejecución |
|---|---|---|
| Programación | 0,5–2 GB de RAM por trabajo | Cuota CPU, memoria máxima y tiempo límite definidos por curso. |
| Arquitectura | 2–4 GB de RAM por trabajo | Cuota CPU, memoria máxima y tiempo límite definidos por curso. |
| IA | 16–32 GB RAM y 12–24 GB de memoria GPU | GPU compatible, cuota CPU, memoria y tiempo límite definidos por curso. |

Los rangos son los supuestos de R. El perfil debe concretar sus límites antes de ejecutar un curso y el host debe reservar recursos para el sistema y el minion. Los P99 del enunciado sirven de referencia de duración; **no se convierten automáticamente en timeouts** ni en máximos válidos para todas las entregas.

El trabajo fija la imagen del curso y su versión. El gestor prepara las imágenes de 3–5 GB antes de los cierres previstos. El minion reutiliza la copia local mientras exista el host; si Spot lo retira, otro host vuelve a preparar esa imagen.

## Planificación y aislamiento de la carga

Las colas y pools de Programación, Arquitectura e IA conservan recursos de ejecución separados. Esta partición aplica **Bulkhead** al cómputo: un trabajo GPU largo o una ejecución que agota su cuota no consume los recursos reservados al pool CPU. La separación debe comprobarse con pruebas de carga e interrupción.

Dentro de cada pool, la planificación combina **turnos por curso** y prioridad de los trabajos con menor holgura hasta su fecha límite. Un curso muy demandado puede aprovechar capacidad libre, pero se conserva una oportunidad de asignación para los demás cursos compatibles en la ronda. «Cupo por curso» significa turno de servicio; no promete una máquina simultánea por curso cuando hay menos máquinas que cursos pendientes.

El gestor de capacidad solicita instancias Spot según atraso, perfiles y plazo, considera tipos y zonas compatibles y mide la capacidad realmente obtenida. El backend y los datos durables conservan la recepción y consulta mientras los trabajos esperan capacidad de ejecución.

## Transición con Strangler

Durante la migración, el **Strangler Router** decide por curso y tarea entre el adaptador legacy y la coordinación nueva. Primero se valida el nuevo recorrido para un subconjunto y después se amplía su uso. La laptop sigue atendiendo únicamente lo que realmente sabe corregir.

El adaptador normaliza el estado y el resultado legacy hacia el registro común. Si se revierte una ruta, solo se hace para trabajos que el corrector legacy siga soportando. La laptop no sustituye una ejecución GPU.

Cuando la migración termina se retira esa ruta. El clasificador P/A/IA del objetivo final **no es el Strangler Router**: clasificar trabajos por recursos y decidir legacy/nuevo son responsabilidades diferentes. Las láminas principal y de transición distinguen ambas etapas.

## Respuestas ante fallos

Si Spot anuncia una interrupción, el minion deja de aceptar trabajos e intenta guardar avance solo cuando el programa lo admite y alcanza el tiempo. Si no hay final durable, el trabajo conserva su identificador y vuelve a la cola para otro intento. La asignación temporal y la señal de vida permiten detectar una desaparición sin aviso.

Se propone inicialmente un **máximo de tres intentos automáticos en total por trabajo**, configurable por curso. Es un parámetro de esta propuesta que debe validarse. Un fallo repetible de memoria o tiempo se registra y pasa a revisión; no se repite indefinidamente con el mismo perfil.

Si no hay Spot compatible, el trabajo queda en espera durable, se intenta obtener capacidad compatible en otros tipos o zonas y se actualiza la proyección del plazo. La falta prolongada de GPU puede hacer incumplir los dos días; informar la espera y alertar al docente no amplía el plazo.

## Protecciones de dependencias y riesgos residuales

Esta iteración añade **Circuit Breaker** en dos límites concretos: el acceso del backend a la BD de control y las llamadas del adaptador a la laptop legacy. Cada circuito observa su dependencia; sus umbrales, timeout y período de recuperación son configurables y se ajustarán mediante pruebas. No se fijan cifras del caso que el enunciado no proporciona.

El **circuito de BD** corta nuevas llamadas cuando la dependencia falla o tarda demasiado y permite una prueba controlada de recuperación. Si la BD no permite completar el registro durable, no se confirma una nueva entrega ni se publica una nota. Una consulta responde indisponibilidad temporal en lugar de inventar un estado. Si el minion ya guardó una salida en objetos y falta aceptar el final, el trabajo conserva su identificador y permanece pendiente hasta completar la aceptación durable; no se reconoce su terminación ni se crea otro final por reintentar. El código del alumno no accede directamente a la BD.

El **circuito del adaptador legacy** evita seguir enviando llamadas a la única laptop cuando falla o responde fuera de su timeout. El trabajo y su estado permanecen registrados; se informa y se reintenta según la política acotada cuando corresponda. Solo puede cambiarse la ruta a una implementación compatible ya validada. No existe una sustitución de GPU mediante la laptop.

La laptop es un **SPOF del recorrido legacy**. La BD es un **SPOF si el despliegue usa una sola instancia**, condición que el dibujo deja explícita. Los circuitos contienen la cascada de fallos; **no recuperan los datos ni eliminan esos SPOF**. El backend y las demás dependencias también necesitan una decisión de recuperación antes de producción; esta lámina no acredita redundancia ni un SLA.

La capacidad GPU Spot se identifica como **bottleneck candidato**, por la escasez y duración de trabajos del enunciado. Se contrastará con capacidad obtenida, edad de cola, duración y preparación del entorno. Circuit Breaker no crea capacidad GPU ni garantiza el plazo de notas. Los pools separados y la planificación por curso conservan sus funciones de aislamiento y reparto.

La justificación procede de SWA 5.1 [62:44] (Circuit Breaker y límite de su efecto), SWA 6.1 [19:49] (identificar la dependencia y ubicar su protección), Top-Down II [34:09] (dependencias lentas o caídas) y SWA 11.1 [89:12–94:54] (diagnóstico y patrón mínimo).

# A — Armar el modelo de datos

La BD relacional conserva identidad, cursos, entregas, trabajos, intentos y notas. Los archivos de alumnos, resultados y avances recuperables se conservan en almacenamiento de objetos; las imágenes base permanecen en un registro de imágenes. El sandbox no tiene acceso directo a la BD de control.

| Registro | Datos principales | Regla o responsabilidad |
|---|---|---|
| Usuario | ID institucional, habilitación y roles | Alta institucional autorizada; el alumno no se asigna rol docente. |
| Acceso al curso | Usuario, curso, rol | Limitar consultas y publicación a entregas propias o cursos autorizados. |
| Curso y perfil | Tipo CPU/GPU, imagen y versión, límites de recursos y tiempo | Elegir un host compatible y fijar el entorno de corrección. |
| Tarea | Curso, cierre y fecha límite de notas | Con el supuesto de R, fecha límite igual a cierre más 48 horas. |
| Entrega | Alumno, tarea, versión, solicitud y referencia al archivo completo | Reconocer reenvíos de la misma solicitud sin duplicar la entrega. |
| Trabajo | Entrega, perfil, plazo, estado e intento vigente | Ser la referencia durable de lo pendiente; final único por trabajo. |
| Intento | Trabajo, minion, inicio, señal de vida, asignación y causa de salida | Detectar interrupciones y rechazar finales de intentos obsoletos. |
| Resultado | Trabajo, intento aceptado y referencias a salida y errores | Guardar como máximo un resultado final aceptado por trabajo. |
| Nota | Resultado, docente, valor y fecha de publicación | Conservar la revisión y medir la entrega de notas dentro del plazo. |
| Evento de estado | Trabajo, estado, fecha y causa | Mostrar y reconstruir espera, ejecución, reintento y finalización. |

Una tarea recibe entregas; cada versión genera un trabajo; un trabajo admite varios intentos y como máximo un final aceptado. Una revisión docente produce la nota. El historial de intentos no se confunde con versiones nuevas que el alumno envía deliberadamente.

# L — Listar los componentes

| Componente | Responsabilidad |
|---|---|
| App del alumno | Enviar una entrega, recibir confirmación y consultar su estado. |
| Desktop del docente | Revisar resultados y errores, y publicar notas de sus cursos. |
| Login Service | Autenticar cuentas habilitadas. |
| Registro de usuarios | Alta institucional y asignación autorizada de roles y cursos. |
| Entregas | Registrar solicitudes, comprobar archivos completos y confirmar recepción. |
| Resultados y notas | Responder estados y resultados, controlar permisos y confirmar publicación. |
| Coordinación | Clasificar, planificar por plazo y turnos, y conciliar trabajos pendientes. |
| Control de trabajo | Supervisar intento vigente, señales de vida, reintentos y final único. |
| Gestor Spot | Solicitar y reducir capacidad compatible según perfiles, atraso y plazos. |
| Colas y pools P/A/IA | Separar trabajo pendiente y recursos CPU/GPU mediante Bulkhead. |
| Minion y sandbox | Supervisar desde el proceso de confianza y ejecutar el código aislado. |
| Registro y copia local de imágenes | Conservar versiones de 3–5 GB y preparar el entorno del curso. |
| Objetos y BD | Conservar archivos, resultados, identidad, trabajos, estados y notas. |
| Circuit Breaker de BD y del adaptador legacy | Cortar llamadas ante falla o timeout; recuperación controlada sin confirmar datos no guardados. |
| Strangler Router y adaptador | Conservar el recorrido legacy durante la migración y unificar resultados. |
| Monitoreo y alertas | Medir esperas, recursos, interrupciones, capacidad obtenida y riesgo de plazo. |

## Recorrido crítico y puntos de falla

El **camino crítico de negocio** se representa como envío y guardado durable, coordinación, cola compatible, minion y sandbox, resultado durable, revisión docente y publicación de nota. La confirmación inicial y las consultas también tienen recorridos de retorno explícitos. La lámina principal diferencia los pasos de ese camino de las consultas y confirmaciones.

La laptop es un **SPOF del recorrido legacy** mientras sea su única ejecución. En el objetivo nuevo, backend, planificador y BD son **riesgos de SPOF si el despliegue elige una única instancia**; dibujar un módulo lógico no acredita redundancia. Antes del despliegue se debe decidir su recuperación o redundancia según los requisitos. Esta revisión no atribuye un SLA 24/7 al caso Spotty.

La capacidad IA es un **bottleneck candidato**, por las duraciones GPU y la posible escasez del caso. También deben medirse preparación de imágenes, memoria, edad de colas y acceso a datos. Se validan estas hipótesis con pruebas; las etiquetas no sustituyen las mediciones.

# E — Escalar la arquitectura

## Cuándo y qué ampliar

Se miden trabajos pendientes y su edad, carga por curso, duración por perfil, uso de memoria, tiempo para preparar imágenes y holgura hasta la entrega de notas. Se conserva el atraso de cierres anteriores al recibir el siguiente pico. El gestor solicita capacidad antes de los cierres conocidos y ajusta cada pool de forma separada.

La estimación inicial del avance corresponde a **2 slots de Programación, 5 de Arquitectura y 7 de IA**. Con la propuesta de una ejecución por host serían esas cantidades de minions e instancias simultáneas solicitadas. Los slots CPU no son un conteo de cores; la capacidad real depende de la instancia y del perfil medido. Spot puede ofrecer menos capacidad que la solicitada.

La fórmula preliminar sigue siendo horas de trabajo pendiente, incluido el margen, divididas entre horas disponibles hasta el objetivo interno. Las duraciones asumidas y el margen deben contrastarse con mediciones. El objetivo interno de corrección de 36 horas es distinto del máximo de dos días para entregar notas.

## Trade-offs de la propuesta

Una ejecución simultánea por host facilita el aislamiento y reemplazo, con posible capacidad ociosa. Los pools separados limitan el impacto de una clase de trabajo, pero pueden dejar recursos libres en un pool mientras otro espera. La planificación por turnos protege a cursos pequeños y debe medirse frente a las tareas urgentes.

Se conservan **Strangler, Bulkhead y Retry** por migración, aislamiento y fallos de ejecución. Esta iteración concreta además **Circuit Breaker** en el acceso a la BD y a la laptop legacy para contener fallos de esas dependencias, con los límites descritos en D. BFF, Cache-Aside, réplicas y sharding requieren un diagnóstico adicional antes de incorporarse. La selección sigue la regla de la semana 11 de aplicar el patrón mínimo necesario.

## Límite ante escasez de GPU

El escenario ilustrativo conserva **200 trabajos de IA de 60 minutos** y un margen que eleva el trabajo a **250 horas GPU**. Si faltan GPU durante 24 horas desde el cierre de referencia, siete GPU tardarían después otras 35,7 horas: 59,7 horas desde el cierre, sin revisión docente.

Once GPU durante las 24 horas restantes alcanzarían solo para completar esa ejecución antes de 48 horas; todavía debe caber la revisión y publicación de notas. Por ello la escasez prolongada se registra como riesgo de incumplimiento. La espera durable y las alertas protegen la entrega, pero no demuestran que se entregarán las notas a tiempo.

## Fitness functions

Cada función identifica una dimensión, un indicador y una rúbrica. Su ejecución queda asociada a pruebas de arquitectura con una carga y un conjunto de entregas definidos. No se declara que estas pruebas hayan sido ejecutadas sobre una implementación de Spotty.

**FF1 — Integridad y confiabilidad.** Indicadores: entregas confirmadas que se pierden y resultados finales duplicados por trabajo. Rúbrica aceptable: **cero pérdidas y cero duplicados**. Prueba: interrumpir minions antes y después de guardar salida, reencolar trabajos y repetir solicitudes de finalización; comprobar los registros durables y rechazar intentos obsoletos.

**FF2 — Aislamiento y seguridad.** Indicadores: accesos del sandbox a credenciales o datos ajenos, y afectación de otro pool bajo la carga de prueba. Rúbrica aceptable: **cero accesos prohibidos y continuidad del otro pool**. Prueba: código que supera memoria o tiempo o intenta acceder fuera de su entorno. Registrar la causa y detener únicamente la ejecución infractora en el escenario definido.

**FF3 — Requerimiento de plazo.** Indicador: entregas sin nota publicada cuando vence su fecha límite, incluyendo las que continúan en espera. Rúbrica aceptable: **cero notas fuera del máximo de dos días**, usando el supuesto de cómputo de R. Prueba: cierres escalonados, colas acumuladas, interrupciones y escasez de GPU. Registrar el incumplimiento si ocurre; no excluir del indicador los trabajos que nunca llegaron a terminar.

**FF4 — Contención del fallo de dependencias.** Indicadores: llamadas enviadas a BD o laptop mientras su circuito está abierto y confirmaciones o notas aceptadas sin persistencia durable. Rúbrica: cero llamadas de negocio mientras esté abierto, salvo la prueba de recuperación controlada, y cero confirmaciones o publicaciones sin guardado completo. Prueba propuesta: inyectar caída o latencia superior al timeout de cada dependencia; comprobar apertura, respuesta de espera o indisponibilidad, recuperación controlada y conservación de trabajos y finales únicos. No se declara una ejecución real de esta prueba.

El objetivo interno de **99 % de correcciones automáticas en 36 horas desde el cierre** se mide adicionalmente y no sustituye FF3. La modularidad se representa mediante responsabilidades e interfaces claras entre identidad, entregas, coordinación y resultados; las dependencias se revisan cuando cambien esos módulos.

## Fuentes del curso y trazabilidad

| Fuente del profesor | Criterio aplicado |
|---|---|
| Enunciado Spotty, Arquitectura.2026.II-LAB.12.docx | Spot, sandbox, GPU, memoria, imágenes de curso, picos y máximo de dos días para las notas. |
| Top-Down I, `[03:59]`, `[05:48]` y `[15:33]–[18:33]` | Definir problema y usuarios; relacionar estimaciones con recursos y disponibilidad. |
| Top-Down II, `[02:07]`, `[05:03]`, `[06:49]` y `[10:56]` | Representar requerimientos, Login Service, datos por interacción y respuestas alternativas. |
| Top-Down II, `[30:29]` y `[34:09]–[38:13]` | Control de estados frente a repetición y comportamiento ante dependencias fallidas o lentas. |
| SWA 5.1 [62:44], [87:19] y SWA 6.1 [19:49] | Circuit Breaker ante dependencia fallida o lenta; protección junto al SPOF y uso de patrones en los laboratorios. |
| Semana 6, diapositivas 30–32 | Confiabilidad, Bulkhead y Retry; entregables con tipo de arquitectura, camino crítico y fitness functions. |
| Semana 7, diapositivas 24–36, 41 y 65 | Funciones automatizables, dimensiones e indicadores; modularidad y recorrido crítico. |
| Semana 11, diapositivas 13–23 y 59–62 | Strangler para la transición; identificar el bottleneck y elegir el patrón mínimo necesario. |

El alta institucional, una ejecución por host y el límite inicial de tres intentos son decisiones propuestas para concretar este diseño. Los tamaños, matrículas y objetivos internos conservan su condición de supuestos del avance; no se atribuyen como cifras del enunciado o reglas generales del profesor.
