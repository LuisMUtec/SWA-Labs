# Alumno

## Acceso y objetivo
Accede desde una aplicación mobile para consultar el estado de sus entregables. En esta propuesta también envía código o archivos desde mobile; el enunciado no especifica el canal de envío.

## Interacciones de la propuesta
- Envía una entrega y recibe confirmación cuando el archivo completo y su registro quedan guardados.
- Puede reanudar una carga interrumpida, según RF2.
- Consulta únicamente sus entregas y sus estados: recibida, en espera, en ejecución, reintento, espera por capacidad o finalizada.

## Necesidades recogidas en el avance
- No perder una entrega confirmada cuando se interrumpe un worker Spot.
- Poder seguir el estado aunque falte capacidad CPU o GPU.
- Que su código se ejecute aislado de las otras entregas y que los reintentos no generen resultados finales duplicados.

Fuente: RF1, RF2, RF4, RF6, RNF3, RNF4 y el diseño del avance REDALE.
