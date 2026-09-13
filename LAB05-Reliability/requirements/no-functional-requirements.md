# Requerimientos no funcionales — Genius-x

Estos requerimientos salen del enunciado del Lab 5 y de lo que explicamos en la parte 5 del README.

| ID | Requerimiento no funcional |
|---|---|
| NFR-01 | **Volumen.** El sistema debe soportar 10,000 incidentes por semana, o más en los picos de la primera semana de cada mes. |
| NFR-02 | **Usuarios.** El sistema debe soportar de 50 a 100 ingenieros usando la plataforma. |
| NFR-03 | **SLA por tipo de incidente.** Los Customer escalations se responden en máximo 1 día y los Engineering escalations en máximo 3 días. Para los Support escalations asumimos 2 días porque el enunciado no lo indica. |
| NFR-04 | **LLM sin punto único de falla.** Debe haber más de una instancia del LLM detrás de un load balancer que revisa el /health de cada una. Si una instancia se cae, las demás siguen respondiendo. |
| NFR-05 | **Tolerancia a fallos del LLM.** Si el LLM falla muchas veces seguidas, un circuit breaker corta los pedidos por un tiempo para que se recupere. Mientras tanto las preguntas comunes se responden con las respuestas guardadas y lo demás espera en la cola. |
| NFR-06 | **Recuperación de la base de datos.** La base de datos debe tener backups frecuentes y una réplica, para poder recuperarla si se borra o se daña. |
| NFR-07 | **Acciones controladas.** El MCP de base de datos por defecto solo permite leer. Ninguna escritura se ejecuta sin la aprobación de un ingeniero. |
| NFR-08 | **Respuestas consistentes.** Una misma pregunta común debe tener siempre la misma respuesta. |
| NFR-09 | **Datos actualizados.** El estado que muestra el sistema debe ser el actual. Si se usa caché, debe tener un TTL corto y limpiarse apenas el incidente cambia de estado. |
| NFR-10 | **Latencia mínima para decisiones críticas.** Las decisiones críticas deben tener la menor latencia posible. Se mide con el P95 y el P99 del tiempo de respuesta. |
| NFR-11 | **Disponibilidad y reliability medibles.** Se mide la availability con 2xx / (2xx + 5xx), la reliability con 2xx / (2xx + 4xx + 5xx) y cuántos issues vencen su SLA. |
| NFR-12 | **Slack no bloquea el sistema.** Si Slack no responde, el resto del sistema debe seguir funcionando. |
