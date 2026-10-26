# Arquitectura integrada de Spotty, v7

La imagen principal es el nuevo grafo integrado que Luis pidió puntuar: actores, servicios lógicos, decisiones y almacenamiento. Los servicios pertenecen al mismo backend modular; no se propone un despliegue por caja. C representa la misma BD lógica de control y O el mismo almacenamiento lógico de objetos, aunque se dibujen varios accesos. El control legacy marcado como alias es el mismo Control de trabajo central.

Los requerimientos, personas y REDALE conservan el contenido de la iteración 6; cambia la representación visual. Las condiciones se revalidan dentro del guardado atómico, tanto para un final único como para la publicación P-7.

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

**RF3 — Corrección.** Coordinación clasifica el trabajo según curso y perfil: Programación, Arquitectura o IA. Lo coloca en su cola correspondiente. Un minion compatible toma el trabajo, prepara la versión de imagen fijada, inicia un sandbox y registra el intento. El minion de confianza recoge la salida y envía eventos y resultado al **backend central**, que invoca su **Control de trabajo**. Este módulo registra las transiciones en la misma BD que consulta mobile y acepta el final con la validación transaccional descrita en RF6; el código del alumno no escribe directamente en la BD de control ni recibe credenciales del sistema.

**RF4 — Actualización de estados.** Coordinación genera estados de recepción, cola, falta de capacidad y reintento; los minions de confianza reportan ejecución, salida e incidencias. El Control de trabajo del backend central valida el trabajo y el intento, registra el cambio en la misma BD que consulta mobile y conserva su fecha y revisión. Un evento de un intento obsoleto no puede sobrescribir un final aceptado.

La app autenticada consulta automáticamente por entregaId cada 30 segundos mientras está activa la pantalla de seguimiento, y de inmediato al abrirla o reconectar. Resultados y notas comprueba que la entrega sea del alumno, consulta la BD mediante su Circuit Breaker y devuelve entregaId, estado de corrección, fecha y revisión del estado, y estado de la nota. La app actualiza la pantalla con esa respuesta y descarta una respuesta de revisión anterior a la que ya muestra. El objetivo extremo a extremo es el de RNF5; el sondeo por sí solo no acredita su cumplimiento.

Si no existe capacidad Spot, coordinación guarda «Esperando capacidad» y el circuito de consulta sigue operando sin depender de un minion libre. Si falla la red o la BD, la app distingue el último estado conocido de una consulta exitosa nueva y muestra el aviso de actualización fallida. No interpreta una pérdida de conexión como finalización de la corrección. La nota se incluye únicamente después de la publicación de RF5.

**RF5 — Revisión y publicación de la nota.** El docente autenticado selecciona entregaId de uno de sus cursos. Resultados y notas valida el acceso, recupera de la BD las referencias y los intentos, obtiene de objetos el archivo original, la salida y los errores, y los devuelve al desktop para su revisión. Los intentos fallidos u obsoletos permanecen identificados como historial; no reemplazan el resultado final aceptado.

Tras revisar, el docente envía una solicitud de publicación con entregaId, nota e identificador de solicitud. El backend comprueba rol, curso y resultado aceptado, valida la nota según la configuración del curso y guarda la nota, el docente responsable, la solicitud y la fecha de publicación. Solo confirma «Nota publicada» después de completar ese guardado. Una corrección automática lista sigue pendiente de publicación docente.

Repetir la misma solicitud devuelve la publicación existente. Ante un fallo definitivo de guardado, la respuesta indica que la nota no se publicó. Si se pierde el acuse o hay un timeout con resultado desconocido, el desktop consulta o reintenta el mismo identificador en vez de asumir éxito o crear una solicitud distinta. La siguiente consulta automática mobile puede recuperar la nota publicada desde la misma BD. El plazo de dos días se verifica con esa publicación durable y disponible, conservando el supuesto de cómputo desde el cierre.

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
| Nota | Resultado, docente, valor, solicitud de publicación y fecha de publicación | Confirmar únicamente tras guardar; reconocer la repetición de la misma solicitud y medir el plazo de entrega de notas. |
| Evento de estado | Trabajo, intento si aplica, estado, fecha, revisión y causa | Registrar las transiciones y devolver a mobile un estado durable con fecha y revisión, sin sobrescribir un final con un intento obsoleto. |

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

La capacidad IA es un **bottleneck candidato**, por las duraciones GPU y la posible escasez del caso. También se señalan como **bottlenecks candidatos** la preparación de imágenes de 3–5 GB y la RAM del host. Se medirán duración de descarga y arranque, picos de memoria, rechazos por límites y edad de colas antes de confirmar el diagnóstico. Se validan estas hipótesis con pruebas; las etiquetas no sustituyen las mediciones.

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

**FF1 — Integridad y confiabilidad.** Indicadores: entregas confirmadas que se pierden, resultados finales duplicados por trabajo y notas duplicadas por la misma solicitud de publicación. Rúbrica aceptable: **cero pérdidas y cero duplicados**. Prueba propuesta: interrumpir minions antes y después de guardar salida, reencolar trabajos, finalizar concurrentemente el mismo trabajo desde dos intentos y repetir solicitudes de finalización. Añadir pérdida del acuse después de guardar una nota y reintentar la misma solicitud; comprobar que se devuelve la publicación existente y se rechazan intentos obsoletos.

**FF2 — Aislamiento y seguridad.** Indicadores: accesos del sandbox a credenciales o datos ajenos, y afectación de otro pool bajo la carga de prueba. Rúbrica aceptable: **cero accesos prohibidos y continuidad del otro pool**. Prueba: código que supera memoria o tiempo o intenta acceder fuera de su entorno. Registrar la causa y detener únicamente la ejecución infractora en el escenario definido.

**FF3 — Requerimiento de plazo.** Indicador: entregas sin nota publicada cuando vence su fecha límite, incluyendo las que continúan en espera. Rúbrica aceptable: **cero notas fuera del máximo de dos días**, usando el supuesto de cómputo de R. Prueba: cierres escalonados, colas acumuladas, interrupciones y escasez de GPU. Registrar el incumplimiento si ocurre; no excluir del indicador los trabajos que nunca llegaron a terminar.

**FF4 — Contención del fallo de dependencias.** Indicadores: llamadas enviadas a BD o laptop mientras su circuito está abierto y confirmaciones o notas aceptadas sin persistencia durable. Rúbrica: cero llamadas de negocio mientras esté abierto, salvo la prueba de recuperación controlada, y cero confirmaciones o publicaciones sin guardado completo. Prueba propuesta: inyectar caída o latencia superior al timeout de cada dependencia; comprobar apertura, respuesta de espera o indisponibilidad, recuperación controlada y conservación de trabajos y finales únicos. No se declara una ejecución real de esta prueba.

**FF5 — Frescura del estado visible.** Indicador: demora desde que coordinación o un minion genera una transición hasta que la pantalla mobile activa refleja ese estado o uno posterior. Rúbrica propuesta: **hasta 60 segundos** en los escenarios normales definidos, incluidos espera de capacidad y reintento. Prueba propuesta: generar transiciones identificadas y registrar su presentación con 311 y 3110 pantallas de seguimiento activas, sondeo cada 30 segundos y conectividad operativa. Medir también la recuperación de una consulta fallida y comprobar que la app distingue información previa de una actualización exitosa. Estas son pruebas de arquitectura pendientes, no resultados medidos.

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
