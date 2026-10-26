# Spotty — borrador para revisión

La entrega final sigue pendiente de aprobación de Luis. Esta rama conserva las iteraciones contra el minion del profesor.

El archivo .excalidraw contiene cuatro vistas editables: arquitectura general e identidad; camino crítico y consultas RF4/RF5; minions y control central de estados/finales; transición Strangler. Los requisitos, restricciones y estimaciones se conservan.

## Historial

- Original: 1.6/10.
- Primer Excalidraw: 2.3/10 — [informe](evaluaciones/prueba-excalidraw/resultado.md).
- Iteración 2: 7.1/10 — [informe](evaluaciones/iteracion-2/resultado.md).
- Iteración 3: 9.6/10 — [informe](evaluaciones/iteracion-3/resultado.md).
- Iteración 4: 9.6/10, Critical Path y Happy Path reconocidos — [informe](evaluaciones/iteracion-4/resultado.md).
- Iteración 5: **9.6/10**, Critical Path y Happy Path reconocidos — [informe](evaluaciones/iteracion-5/resultado.md).

Los Circuit Breaker contienen la cascada de fallos y no eliminan por sí solos los SPOF. Los cuellos de botella son candidatos que se deben medir. El minion revisa el dibujo; las pruebas de ejecución, concurrencia, carga y cumplimiento del plazo siguen pendientes de una implementación.

## Resultado actual y revisión pendiente

Security 10/10, reliability 10/10, scalability 10/10 y spec 8/10. El informe conserva las observaciones sobre RF4 (actualización de estado mobile) y RF5 (revisión/publicación docente). Deben revisarse junto al dibujo y el REDALE antes de aprobar la entrega; el resultado automático no se presenta como conformidad total.

Commit evaluado: `fc7bb7ebed8cf1e777bd1daff80484c7eecd728e`. El manifiesto contiene los hashes de los archivos en ese commit. Los informes posteriores no alteran la entrada de esa evaluación.

## Actualización de requerimientos: iteración 6

RF4 y RF5 tienen redacción y criterios de aceptación explícitos. RNF5 define el objetivo extremo a extremo de 60 segundos con la pantalla activa y conectividad operativa. El sondeo propuesto cada 30 segundos añade escenarios de 10.4 y 103.7 consultas/s para 311 y 3110 pantallas activas. Las estimaciones previas, RF6, RF7 y las restricciones se conservan. Se completan los retornos de datos y la publicación de notas en el dibujo; se proponen pruebas de frescura e idempotencia con pérdida de acuse.

Evaluación de la iteración 6 con imagen conjunta: **6.9/10** — [informe](evaluaciones/iteracion-6/resultado.md). La entrega final sigue pendiente de aprobación de Luis.

### Presentación legible de la misma iteración

Se conserva el contenido de RF4 y RF5 y se cambia la lámina principal a una vista de 2000×2460 con letras mayores y recorridos continuos de evento a mobile y de revisión a publicación docente. Las cuatro vistas detalladas están en [material_revision](material_revision). Primera comprobación de la lámina legible: **9.4/10**, RF5 reconocido como completo — [informe](evaluaciones/iteracion-6-legible/resultado.md).

Se explicitan dentro de los componentes RF4 la emisión del evento al cambiar de estado y el temporizador de consulta mobile de 30 segundos. Los requisitos y usuarios permanecen iguales. Verificación anterior: **9.2/10** — [informe](evaluaciones/iteracion-6-cierre/resultado.md). Se conservan sus observaciones.

La presentación actual ancla y etiqueta los retornos de datos a las apps, y conecta la revisión del docente con su acción de publicar. Los requisitos y criterios no cambian. Comprobación anterior: **9.2/10** — [informe](evaluaciones/iteracion-6-retornos/resultado.md).

La lámina actual muestra un estado con fecha en la pantalla mobile y el presupuesto temporal de RNF5; en publicación presenta la transacción por P-7 y las respuestas numeradas BD → backend → docente. Son ejemplos del diseño, no mediciones ni una implementación ejecutada. Verificación: pendiente.
