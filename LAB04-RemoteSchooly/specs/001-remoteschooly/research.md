# Research: decisiones técnicas de RemoteSchooly

## 1. Nodo local y cliente web offline

**Decision**: servir el material desde un nodo escolar y conservar en el navegador solo la carcasa y
el estado de sesión necesarios; los paquetes completos permanecen en el almacén local del nodo.

**Rationale**: la especificación de [Service Workers de W3C](https://www.w3.org/TR/service-workers/)
define eventos de red y almacenamiento de respuestas para aplicaciones offline. Eso resuelve la
interfaz del alumno, pero un caché por navegador no es una unidad administrable para toda la escuela.
El nodo local agrega una copia verificable compartida y evita descargar el mismo paquete por alumno.

**Alternatives considered**:

- Solo PWA por dispositivo: multiplica descargas y hace imposible que Julio vea una copia escolar.
- Aplicación nativa obligatoria: eleva instalación y soporte sin que el caso exija capacidades nativas.
- Solo centro en Lima: no funciona cuando el enlace externo cae durante la clase.

## 2. Reanudación con HTTP y huellas

**Decision**: descargar recursos inmutables por rango de bytes, conservar el validador de versión y
verificar cada recurso contra una huella SHA-256 del manifiesto antes de activarlo.

**Rationale**: [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) define `Range` y la respuesta
`206 Partial Content`, suficientes para reanudar una representación estable. La huella impide que
bytes de versiones distintas formen un archivo que parezca completo.

**Alternatives considered**:

- Reiniciar el archivo: desperdicia la ventana de conexión y contradice `FR-021`.
- Protocolo propietario de sincronización: añade una superficie nueva sin necesidad.
- Validar solo tamaño: dos contenidos distintos pueden tener el mismo tamaño.

## 3. Paquete inmutable y activación atómica local

**Decision**: el manifiesto referencia recursos por huella; el Sync Agent guarda una versión parcial
fuera del directorio activo y cambia el puntero local solo cuando todos los recursos pasan.

**Rationale**: separa transferencia de publicación local. La última versión completa continúa
sirviendo mientras llega la nueva y `Listo` se vuelve una propiedad calculable, no un botón humano.

**Alternatives considered**:

- Sobrescribir la versión activa: expone una semana mezclada durante cada actualización.
- Copiar paquetes ZIP enteros: simplifica el primer caso, pero impide deduplicar recursos idénticos.

## 4. Aplicación central modular, no flota de microservicios

**Decision**: los componentes centrales son límites lógicos dentro de una aplicación modular y
trabajadores asíncronos. Almacenamiento de objetos y proveedor de IA permanecen externos.

**Rationale**: el enunciado no entrega escala ni exige disponibilidad total. Una topología de muchos
servicios agregaría despliegue, redes y fallas que ningún requisito paga. Los límites lógicos permiten
separar más adelante solo el cuello de botella que se mida.

**Alternatives considered**:

- Microservicio por caja: arquitectura prematura sin volumen.
- Monolito sin módulos: oculta fronteras de permisos, tokens y publicación.

## 5. Reducción de tokens

**Decision**: la métrica primaria usa tokens de entrada más salida reportados por el proveedor, por
unidad aprobada. El gateway reduce solicitudes mediante reutilización exacta/semántica confirmada por
la docente, selección de contexto y límites de salida. Registra caché y precio por separado.

**Rationale**: la [API de Usage de OpenAI](https://platform.openai.com/docs/api-reference/usage)
distingue tokens de entrada, salida y entrada cacheada. Como la entrada reportada puede incluir
tokens cacheados, atribuir el 40 % únicamente a prompt caching sería confundir costo con volumen. Una
reutilización que evita la llamada y un contexto menor sí reducen los tokens comparables.

**Alternatives considered**:

- Medir dólares: cambia con precios y modelos sin cambiar uso.
- Medir tokens totales del mes: premia publicar menos.
- Contar caché como cero siempre: contradice proveedores que siguen reportándola dentro de entrada.
- Publicación automática de IA: reduce revisión, no tokens, y viola `FR-007`.

## 6. Privacidad y telemetría

**Decision**: el AI Gateway acepta solo fuentes de autoría y metadatos del curso; el pipeline de
avance estudiantil termina en agregados separados para Gobierno. La sede informa además la fecha de
último contacto.

**Rationale**: son dos flujos con dueños distintos. Unirlos facilita enviar accidentalmente una
respuesta de alumno al proveedor o al tablero. La fecha de contacto impide convertir ausencia de
datos en un estado de entrega falso.

**Alternatives considered**:

- Lago de datos único para todo: mayor superficie y permisos difíciles de demostrar.
- Telemetría solo cuando hay error: el silencio sería indistinguible de éxito.

## 7. Alcance de confiabilidad

**Decision**: incluir integridad, idempotencia, reanudación y operación offline; diferir replicas
activas, failover automático y multi-región.

**Rationale**: los primeros cuatro mecanismos producen correctitud observable exigida por el caso.
Los segundos persiguen disponibilidad, explícitamente postergada por el enunciado.

**Alternatives considered**:

- Quitar toda confiabilidad: un paquete parcial podría aparecer listo.
- Diseñar producción nacional completa: finge cifras y desvía el laboratorio.
