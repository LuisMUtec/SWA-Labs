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
