# Revisión funcional de RF4 y RF5

Esta comparación documenta la propuesta y su representación; no sustituye las pruebas de una implementación. El último minion dio 9.6/10 y mantuvo requerimientos en 8/10. La entrega final requiere la revisión de Luis.

| Criterio | Representación en la lámina principal | Validación pendiente |
|---|---|---|
| CA4.1: origen y persistencia del estado | `principal-event-source` → `principal-work-control` → `principal-state-db`. Se declara emitir al cambiar estado; se guarda con el trabajo e intento correspondientes. | Inyectar transiciones reales y comprobar persistencia y rechazo de intentos obsoletos. |
| CA4.2: consulta automática y pantalla | `principal-state-mobile`, `principal-mobile-poll` y `principal-mobile-update`: consulta cada 30 s, lectura mediante `principal-state-query` y retorno «Mostrar». El panel muestra E-104, Reintentando y fecha como ejemplo. | Medir hasta 60 s desde la transición con pantalla activa; el presupuesto 30 + 30 s es propuesto. |
| CA4.3: consulta fallida y recuperación | El REDALE y la vista detallada `02-requerimientos.png` especifican último dato con fecha/aviso y consulta inmediata al abrir o reconectar. | Prueba de red caída y recuperación, sin simular una actualización exitosa. |
| CA5.1: original, resultado y errores | `principal-review-store` → `principal-review-service` → `principal-review-teacher`. La respuesta ligada a la flecha enumera original, resultado, errores e intentos; el panel desktop muestra los cuatro accesos. | Probar autorización por curso y acceso a los artefactos de una entrega. |
| CA5.2: guardar antes de confirmar | `principal-note-save` (1. Solicitud P-7) → `principal-publish-store` → `principal-note-saved` (2. Nota persistida) → `principal-publish-response` (3. Nota publicada). Se valida rol, curso y final aceptado. | Inyectar fallo definitivo de guardado y comprobar que no se devuelve éxito. |
| CA5.3: repetición y pérdida de confirmación | `principal-publish-store` contiene la transacción: «P-7 existe: leer publicación»; «No existe: guardar nota + fecha»; «Devolver publicación persistida». La política indica consultar/reintentar P-7 si se pierde el acuse. | Repetir P-7 concurrentemente y perder el acuse después del commit; comprobar una sola nota y recuperación de la misma publicación. |
| CA5.4: nota visible después de publicar | La respuesta de RF4 incluye nota solo si publicada; la sección de publicación devuelve el dato persistido a la misma BD que se consulta desde mobile. | Comprobar que una nota en revisión no se muestre publicada y que la publicación se vuelva consultable dentro del objetivo definido. |

## Observaciones automáticas y revisión humana

El último informe afirma que no se especifica cómo se consulta una P-7 existente. Esa rama figura literalmente en `principal-publish-store-label`. También cuestiona conexiones del recorrido RF4 que están representadas por las flechas y etiquetas anteriores. La discrepancia debe revisarse mirando el dibujo y sus elementos; no se interpreta como prueba de ejecución ni se descarta el informe completo.

Las corridas previas reconocieron por separado RF4 y RF5 como completos, mientras otras los calificaron de parciales. Se conservan todas con el commit de entrada para no elegir solo una nota favorable.

## Base del curso

Top-Down II [02:07] exige representar los recorridos; [06:49] usa datos concretos en conexiones; [10:56] incluye resultados alternativos; [30:29] trata repetición y estado, y [34:09] dependencias lentas o fallidas. El sondeo de 30 segundos, el presupuesto temporal y la publicación idempotente son decisiones propuestas para concretar los requisitos, no cifras ni algoritmos atribuidos al profesor.
