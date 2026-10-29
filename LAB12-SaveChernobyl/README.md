# Save Chernobyl para el evaluador del curso

Paquete del Lab 12 (Reliability Patterns, Fault Tolerance, Legacy Migration, Scalability) armado para el minions archi evaluator.

- `requerimientos/`: enunciado original del lab (con su diagrama as-is) y los requisitos funcionales, no funcionales y restricciones extraídos de él.
- `users/`: el operador de planta, único usuario humano del sistema.
- `Listado_Diagramas/`: el diagrama final (`Diagrama Final.png`, con su fuente `.excalidraw`) y los criterios hipotéticos de escalabilidad (`README.md`), que es el segundo entregable del lab.
- `scripts/`: `build_final.py` genera el `.excalidraw` con la librería `xlib.py`; `render_chrome.py` lo pasa a SVG y PNG con Chrome headless (`render_x.py` hace el SVG). Para la entrega al profesor conviene abrir el `.excalidraw` en excalidraw.com y exportar el PNG desde ahí, que usa la Excalifont real.

## Versiones del diagrama

**v1 (commit `de0e1c6`, 29 oct):** la propuesta inicial del equipo tal como llegó, sin correcciones. Tres iteraciones en una sola lámina de 3790×3585 px: as-is con actores, SPOF y failure scenarios sobre el as-is, y to-be con reliability, fault tolerance y coexistencia con el legacy. Sirve de línea base.

**v2 (lámina actual):** misma arquitectura, una sola lámina solo con el to-be (iteración 3), 3080×1793 px y fuentes de 15 a 18 px en vez de 12 a 14. Cambios respecto a v1:

- Etiquetas literales de patrón sobre cada caja: `<< Strangler >>`, `<< Side-car >>`, `<< Cache-Aside >>`, `<< Replicas >>`, `<< Sharding >>`, `<< Circuit Breaker >>`.
- SPOF y Bottleneck marcados en la misma lámina con su mitigación: Main Controller legacy = SPOF (Circuit Breaker + Retry en el router, Main nuevo en parallel run); Log DB = Bottleneck (cola asíncrona + Read Replica + Cache-Aside).
- Login / Auth Service, User Registration Service y Users DB para que el operador se autentique y quede identificado en la trazabilidad («quién prendió o apagó qué»).
- Alert Service replicado (en v1 era una caja sola).
- Los flujos alternos, la leyenda y el resumen de patrones pasan a bloques de texto al pie.

Repositorio: `LuisMUtec/SWA-Labs`, rama `lab12/chernobyl-evaluacion`, carpeta `LAB12-SaveChernobyl`. El evaluador recibe `path: "LAB12-SaveChernobyl"` y los nombres relativos `requerimientos`, `users` y `Listado_Diagramas`. La imagen principal se llama `Diagrama Final.png`, como exige el servicio. Cada evaluación registra el commit exacto enviado.

Pendiente: TEAM e INTEGRANTES en la cabecera del diagrama y en el PDF de criterios.

## Primera evaluación del profesor (línea base)

Corrida del 29 de octubre de 2026 sobre el commit `de0e1c60e166ab86018d98c90253e78a0edf866a`: **5.0/10** («Ok but can be improved»).

| Minion | Peso | Puntaje | Qué dijo |
|---|---|---|---|
| Security | 1 | 0/10 | No encuentra un componente nombrado Login/Auth ni uno de creación de usuarios. El API Gateway dice «auth, rate limit» pero no cuenta como Login Service. |
| Reliability | 3 | 10/10 | Encontró SPOF y bottleneck etiquetados en la iteración 2 y Circuit Breaker, Cache y Retry en la 3. |
| Scalability | 4 | 0/10 | Dice que ningún elemento está etiquetado con Strangler, Side-car, Cache-Aside, BFF, Replicas o Sharding. |
| Spec | 2 | 10/10 | Operador presente; RF1, RF3 y RF5 con camino completo. |
| E2E | — | ✅ ✅ | Critical path y happy path presentes. |

Lectura del resultado: el evaluador trabaja sobre una versión reducida de la imagen. La lámina mide 3790×3585 px y el texto de la iteración 3 es pequeño, así que inventa nombres de nodos («Auth Controller», «Sensor Handler», «Decision Engine», «Expense Repository Protected») y no lee las etiquetas que sí existen («Strangler Router (Facade)», «Side-car», «Cache aside», «Read Replica», «replica (failover)», «Sharding por reactor»). Para la siguiente iteración: etiquetas de patrón grandes y literales sobre cada caja, un Login/Auth Service y un registro de usuarios nombrados como tales, y una lámina por iteración o solo la iteración 3 como `Diagrama Final.png`.

- [Informe completo](evaluaciones/2026-10-29/resultado.md)
- [Solicitud usada](evaluaciones/2026-10-29/solicitud.json)
- [Registro de la corrida](evaluaciones/2026-10-29/registro.json)
