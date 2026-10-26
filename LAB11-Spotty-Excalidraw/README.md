# Spotty — arquitectura integrada v7

Borrador enviado al minion por solicitud de Luis. La entrega final sigue pendiente de aprobación. Se utiliza la rama de prueba lab11/spotty-prueba-excalidraw.

- [Diagrama actual](Listado_Diagramas/Diagrama%20Final.png)
- [Excalidraw editable](Listado_Diagramas/Diagrama%20Final.excalidraw)
- [SVG para ampliar](material_revision/Spotty-integrado-v7.svg)
- [Requerimientos y criterios](requerimientos/01-requisitos.md)
- [REDALE](REDALE.md)
- [Historial de evaluaciones](evaluaciones)

Se conservan los requerimientos, restricciones y supuestos del documento previo. Los servicios del dibujo son componentes lógicos; C y O son alias de los mismos almacenamientos. Esta variante tiene una arquitectura integrada con ramas de éxito/error, consultas mobile, pools de minions/sandboxes, capacidad, interrupciones y publicación docente.

Evaluación de v7: **5.1/10** — [informe completo](evaluaciones/arquitectura-integrada-v7/resultado.md). Seguridad 5, confiabilidad 10, escalabilidad 0 y requerimientos 8. Happy Path reconocido; Critical Path no reconocido. Las notas anteriores pertenecen a otros diagramas y no se atribuyen a esta variante.

Commit exacto evaluado: `4eead9a221e6f81bfc5bba63ccdbcc4282d6e1ba`. El informe original se conserva sin corregir sus interpretaciones. Pasó por alto Registro de usuarios, Strangler y la leyenda del camino crítico, que están presentes en la imagen; esta discrepancia no cambia el puntaje reportado ni acredita una aprobación automática.
