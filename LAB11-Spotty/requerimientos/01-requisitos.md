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
