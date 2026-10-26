# Spotty — requerimientos y arquitectura para revisión

**Estado:** borrador pendiente de aprobación de Luis; esta es una rama de prueba, no una entrega en Canvas.

## Actualización funcional

- RF4: consulta y actualización automática de estados propios en mobile, con fecha y revisión. Se propone consultar cada 30 segundos con la pantalla activa; el objetivo normal extremo a extremo es hasta 60 segundos. Se definen desconexión, recuperación y estados sin capacidad/reintento.
- RF5: revisión conjunta de entrega original, resultado y errores/intententos; publicación de nota con validación de acceso y confirmación tras persistir. Una solicitud repetida devuelve la publicación guardada; una confirmación perdida se recupera sin otra nota.
- RNF5, criterios CA4.1–CA5.4, escenarios de carga de consultas y fitness functions actualizados. RF6, RF7, restricciones y el plazo máximo de dos días se conservan.

## Archivos para revisar

- [Requerimientos y criterios](requerimientos/01-requisitos.md)
- [REDALE completo](REDALE.md)
- [Lámina principal](Listado_Diagramas/Diagrama%20Final.png)
- [Excalidraw principal](Listado_Diagramas/Diagrama%20Final.excalidraw)
- [Cuatro vistas detalladas](material_revision/Spotty-detallado.excalidraw)
- [Detalle de RF4 y RF5](material_revision/02-requerimientos.png)
- [Comparación de criterios y diagrama](revision-funcional.md)

## Resultado automático actual

**9.6/10**: security 10, reliability 10, scalability 10 y spec 8. Critical Path y Happy Path: reconocidos. [Informe completo](evaluaciones/iteracion-6-panel/resultado.md).

El evaluador todavía marca RF4 y RF5 como parciales; no se declara una aprobación total. Algunas observaciones no coinciden con elementos explícitos del dibujo, como la rama de P-7 existente. La comparación por criterio documenta dónde revisar cada punto; la interpretación final corresponde a la revisión humana.

Las pruebas de ejecución, frescura bajo carga y recuperación de pérdida de acuse siguen siendo propuestas de validación, no resultados medidos. El Circuit Breaker no elimina los SPOF ni garantiza el plazo bajo escasez prolongada de GPU.

## Historial conservado

- Primer Excalidraw: [2.3/10](evaluaciones/prueba-excalidraw/resultado.md).
- Iteración 2: [7.1/10](evaluaciones/iteracion-2/resultado.md).
- Iteración 3: [9.6/10](evaluaciones/iteracion-3/resultado.md).
- Iteración 4: [9.6/10](evaluaciones/iteracion-4/resultado.md).
- Iteración 5: [9.6/10](evaluaciones/iteracion-5/resultado.md).
- Requisitos completados, imagen conjunta: [6.9/10](evaluaciones/iteracion-6/resultado.md).
- Lámina principal: [9.4/10](evaluaciones/iteracion-6-legible/resultado.md), [9.2/10](evaluaciones/iteracion-6-cierre/resultado.md), [9.2/10](evaluaciones/iteracion-6-retornos/resultado.md), [9.4/10](evaluaciones/iteracion-6-publicacion/resultado.md), [9.6/10](evaluaciones/iteracion-6-panel/resultado.md).

Commit evaluado: `9f65f517ac21af776e9ca46d95b58a8b4c7dbf69`. Los hashes del manifiesto corresponden a los archivos de ese ref, antes de añadir el informe posterior.
