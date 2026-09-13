# Ingeniero del área de ingeniería

## Quién es

Es un ingeniero del área de ingeniería. Reporta incidentes para su propia área o para otras áreas y también resuelve los que le llegan. Puede ser practicante, analista, senior o lead, y según su rol cambia la relevancia de lo que reporta y cuántas sesiones puede abrir.

## Qué hace en Genius

- Registra engineering escalations.
- Usa el LLM para hacer consultas a la base de datos y pruebas E2E.
- Revisa y aprueba los plan.md que propone el LLM en el human in the loop.

## Necesidades del sistema

- Que los engineering escalations se atiendan dentro del SLA de 3 días.
- Revisar y aprobar un plan.md antes de que se ejecute cualquier cambio.
- Que el LLM use lo aprendido en incidentes anteriores y no responda con data pasada.
- Poder abrir las sesiones que necesita según su rol, sin que otros saturen el LLM.
- Que el sistema siga funcionando aunque una instancia del LLM se caiga.

## Problemas que tiene hoy

- Hay quejas de que el LLM no aprende y da respuestas erróneas o con data pasada.
- En la primera semana del mes el LLM tiende a no responder o responde mal.
- Hoy el LLM puede ejecutar acciones en la base de datos sin que nadie las revise.
