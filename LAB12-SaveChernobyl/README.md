# Save Chernobyl para el evaluador del curso

Paquete del Lab 12 (Reliability Patterns, Fault Tolerance, Legacy Migration, Scalability) armado para el minions archi evaluator. Contiene la **propuesta inicial del equipo** tal como llegó el 29 de octubre de 2026, sin correcciones, para tener una referencia de evaluación antes de iterar.

- `requerimientos/`: enunciado original del lab (con su diagrama as-is) y los requisitos funcionales, no funcionales y restricciones extraídos de él.
- `users/`: el operador de planta, único usuario humano del sistema.
- `Listado_Diagramas/`: el diagrama final (`Diagrama Final.png`, con su fuente `.excalidraw`) y los criterios hipotéticos de escalabilidad (`README.md`), que es el segundo entregable del lab.

El diagrama tiene tres iteraciones en una sola lámina: as-is con actores, SPOF y failure scenarios sobre el as-is, y to-be con reliability, fault tolerance y coexistencia con el legacy (reactor 1 migrado; 2 y 3 siguen en legacy).

Repositorio: `LuisMUtec/SWA-Labs`, rama `lab12/chernobyl-evaluacion`, carpeta `LAB12-SaveChernobyl`. El evaluador recibe `path: "LAB12-SaveChernobyl"` y los nombres relativos `requerimientos`, `users` y `Listado_Diagramas`. La imagen principal se llama `Diagrama Final.png`, como exige el servicio. Cada evaluación registra el commit exacto enviado.

Pendiente: TEAM e INTEGRANTES en la cabecera del diagrama y en el PDF de criterios.
