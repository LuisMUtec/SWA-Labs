# Requerimientos funcionales de Genius-x

Estos requerimientos salen de lo que explicamos en el README (partes 3, 4 y 5) y del enunciado del Lab 5.

| ID | Requerimiento funcional |
|---|---|
| FR-01 | **Registro de issues por tipo.** El sistema debe recibir issues de tipo Customer, Support y Engineering, y guardar de qué tipo es cada uno. |
| FR-02 | **Puntaje de urgencia.** Cada variable recibe un puntaje del 1 al 10. Customer y Support usan el SLA, la categoría del cliente y el tipo de mercado. Engineering usa el SLA y el sistema afectado. |
| FR-03 | **Cola por urgencia.** Customer siempre se atiende antes que Support y Engineering. Después, la cola ordena los issues por su puntaje. |
| FR-04 | **Clasificación por complejidad.** El LLM debe clasificar cada issue como de complejidad Alta, Media o Baja. |
| FR-05 | **Embudo para complejidad Alta.** Antes de crear el plan, un issue de complejidad Alta debe pasar por un embudo que revisa palabras clave potencialmente destructivas. |
| FR-06 | **Plan para Alta y Media.** Para los issues de complejidad Alta y Media, el LLM debe crear un plan.md con las acciones que propone. |
| FR-07 | **Human in the loop.** Media necesita una aprobación y Alta necesita dos en paralelo. Si el issue es urgente, se avisa al ingeniero de guardia y, si no responde en 5 minutos, a uno de respaldo. Nada se ejecuta sin las aprobaciones necesarias. |
| FR-08 | **Solo lectura para Baja.** Los issues de complejidad Baja solo pueden hacer consultas de lectura y el LLM responde directamente. |
| FR-09 | **Respuestas guardadas.** Si la pregunta es común, el sistema debe usar la respuesta guardada antes de llamar al LLM. |
| FR-10 | **Estado actual del incidente.** Primero se revisa la caché. Si no tiene un estado vigente, se lee la BD. Cuando el estado cambia, se limpia la caché. |
| FR-11 | **Base de conocimiento.** Cada vez que se cierra un incidente, el sistema debe guardar cómo se resolvió, y el LLM debe consultar esa información antes de responder. |
| FR-12 | **Límite de sesiones por rol.** El sistema debe limitar cuántas sesiones puede tener abiertas cada ingeniero según su rol, y no debe dejarle abrir más cuando llega a su límite. |
| FR-13 | **Avisos por Slack.** El sistema debe enviar avisos por Slack. Si Slack no responde, los avisos se guardan y se envían cuando vuelva. |
