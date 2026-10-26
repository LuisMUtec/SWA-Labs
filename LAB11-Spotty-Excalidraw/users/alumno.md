# Alumno

## Acceso y objetivo
Accede desde una aplicación mobile para consultar el estado de sus entregables. En esta propuesta también envía código o archivos desde mobile; el enunciado no especifica el canal de envío.

## Interacciones de la propuesta
- Envía una entrega y recibe confirmación cuando el archivo completo y su registro quedan guardados.
- Puede reanudar una carga interrumpida, según RF2.
- Consulta únicamente sus entregas y sus estados: recibida, en espera, en ejecución, reintento, espera por capacidad o finalizada.
- La pantalla de seguimiento consulta automáticamente cada 30 segundos (decisión propuesta) y se actualiza con el estado recibido. El objetivo normal es hasta 60 segundos desde la transición.
- Si falla una consulta, distingue el último estado conocido de una actualización exitosa y vuelve a consultar al reconectar.
- La consulta devuelve la nota únicamente cuando el docente ya la publicó.

## Necesidades recogidas en el avance
- No perder una entrega confirmada cuando se interrumpe un worker Spot.
- Poder seguir el estado aunque falte capacidad CPU o GPU.
- Que su código se ejecute aislado de las otras entregas y que los reintentos no generen resultados finales duplicados.

Fuente: RF1, RF2, RF4, RF6, RNF3, RNF4 y el diseño del avance REDALE.
