# Ingeniero de soporte

## Quién es

Es un ingeniero del área de soporte. Atiende los incidentes que reportan los clientes y los escalamientos que soporte ya revisó antes. Es quien más usa Genius en el día a día.

## Qué hace en Genius

- Atiende customer escalations y support escalations.
- Le pregunta al LLM por el estado de los incidentes.
- Le da instrucciones al LLM para resolver un escalamiento.

## Necesidades del sistema

- Ver el estado real de un incidente y no uno que ya cambió hace horas.
- Recibir la misma respuesta cuando hace una pregunta común.
- Que el LLM le responda también en la primera semana del mes, cuando hay más incidentes.
- Que los customer escalations se atiendan dentro del SLA de 1 día.
- Que ninguna instrucción suya termine en una acción destructiva sin que alguien la apruebe.

## Problemas que tiene hoy

- Genius a veces le muestra como abierto un incidente que ya se cerró hace horas.
- El LLM le responde distinto a la misma pregunta.
- Un ingeniero de soporte le dio instrucciones al LLM para un escalamiento de un cliente y el LLM borró la base de datos.
