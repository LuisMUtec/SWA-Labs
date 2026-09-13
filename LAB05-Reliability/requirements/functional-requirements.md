# Requerimientos funcionales de Genius-x

Estos requerimientos salen de lo que explicamos en el README (partes 3, 4 y 5) y del enunciado del Lab 5.

| ID | Requerimiento funcional |
|---|---|
| FR-01 | **Registro de issues por tipo.** El sistema debe recibir issues de tipo Customer, Support y Engineering, y guardar de qué tipo es cada uno. |
| FR-02 | **Puntaje de urgencia.** El sistema debe calcular un puntaje de urgencia para cada issue con las variables de su tipo. Customer usa el tiempo que falta para vencer el SLA, la categoría del cliente y el tipo de mercado. Support usa las mismas variables más lo que ya hizo soporte. Engineering usa el tiempo que falta para vencer el SLA, la relevancia según rol y el sistema afectado. |
| FR-03 | **Cola por urgencia.** Los issues deben entrar a una cola ordenada por su puntaje, para que primero se atiendan los que están por vencer su SLA. |
| FR-04 | **Clasificación por complejidad.** El LLM debe clasificar cada issue como de complejidad Alta, Media o Baja. |
| FR-05 | **Embudo para complejidad Alta.** Antes de crear el plan, un issue de complejidad Alta debe pasar por un embudo que revisa palabras clave potencialmente destructivas. |
| FR-06 | **Plan para Alta y Media.** Para los issues de complejidad Alta y Media, el LLM debe crear un plan.md con las acciones que propone. |
| FR-07 | **Human in the loop.** Ningún plan.md se ejecuta sin la aprobación de un ingeniero. Un issue de complejidad Alta necesita más aprobación humana que uno de complejidad Media. |
| FR-08 | **Solo lectura para Baja.** Los issues de complejidad Baja solo pueden hacer consultas de lectura y el LLM responde directamente. |
| FR-09 | **Respuestas guardadas.** Si la pregunta es común, el sistema debe responder con la respuesta ya guardada para que siempre sea la misma. |
| FR-10 | **Estado actual del incidente.** Cuando se pregunta por un incidente, el sistema debe leer su estado actual de la base de datos. |
| FR-11 | **Base de conocimiento.** Cada vez que se cierra un incidente, el sistema debe guardar cómo se resolvió, y el LLM debe consultar esa información antes de responder. |
| FR-12 | **Límite de sesiones por rol.** El sistema debe limitar cuántas sesiones puede tener abiertas cada ingeniero según su rol, y no debe dejarle abrir más cuando llega a su límite. |
| FR-13 | **Avisos por Slack.** El sistema debe enviar avisos por Slack. Si Slack no responde, los avisos se guardan y se envían cuando vuelva. |
