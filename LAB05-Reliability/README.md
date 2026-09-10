# Lab 05 - Reliability: Genius-x

## Alcance (borrador)

- Genius-x administra un backlog único de incidentes originados por clientes, soporte o ingeniería.
- Los usuarios directos son soporte e ingenieros.
- Quien reporta un ticket consulta su estado; el rol resolutor usa herramientas adicionales según su autorización.
- La base de datos de incidentes es la fuente de verdad para el estado y cierre del ticket.
- El LLM recopila información en modo de solo lectura y propone un plan.
- Una operación crítica requiere aprobación humana explícita y debe quedar registrada junto con su resultado.

## Happy path de resolución (en revisión)

1. Soporte o ingeniería registra un ticket en la plataforma interna de issues.
2. El LLM recopila información y propone un plan de resolución.
3. Un ingeniero autorizado revisa y aprueba el plan.
4. Las operaciones críticas requieren autorización explícita antes de ejecutarse.
5. El resultado se registra en el ticket y el reportante consulta su estado actualizado.
6. La persona autorizada confirma el cierre y se notifica al reportante.

## Pendientes

- Definir el rol aprobador y el ejecutor de las operaciones críticas.
- Precisar la supervisión: auditoría, notificaciones o ambas.
- Definir la clasificación de complejidad y su relación con los SLA.
- Diseñar la respuesta de Genius-x durante picos o fallas del LLM.
