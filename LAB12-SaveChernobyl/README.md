# Save Chernobyl para el evaluador del curso

Paquete del Lab 12 (Reliability Patterns, Fault Tolerance, Legacy Migration, Scalability) armado para el minions archi evaluator. Contiene la **propuesta inicial del equipo** tal como llegó el 29 de octubre de 2026, sin correcciones, para tener una referencia de evaluación antes de iterar.

- `requerimientos/`: enunciado original del lab (con su diagrama as-is) y los requisitos funcionales, no funcionales y restricciones extraídos de él.
- `users/`: el operador de planta, único usuario humano del sistema.
- `Listado_Diagramas/`: el diagrama final (`Diagrama Final.png`, con su fuente `.excalidraw`) y los criterios hipotéticos de escalabilidad (`README.md`), que es el segundo entregable del lab.

El diagrama tiene tres iteraciones en una sola lámina: as-is con actores, SPOF y failure scenarios sobre el as-is, y to-be con reliability, fault tolerance y coexistencia con el legacy (reactor 1 migrado; 2 y 3 siguen en legacy).

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
