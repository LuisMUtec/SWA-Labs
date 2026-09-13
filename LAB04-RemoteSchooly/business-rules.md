# Reglas de negocio

Las reglas describen invariantes del programa y conservan identificadores estables.

| ID | Regla |
|---|---|
| BR-01 | Una combinación curso + semana + audiencia + sede tiene como máximo una versión activa. |
| BR-02 | Solo una unidad aprobada por un Profesor de Lima puede formar parte de un paquete publicado. |
| BR-03 | Un paquete es `Listo` si y solo si todos los recursos obligatorios coinciden con el manifiesto de esa misma versión. |
| BR-04 | Una versión parcial no sustituye a la última versión completa. |
| BR-05 | El identificador de una entrega de alumno es estable entre reintentos; confirmarlo dos veces no crea dos avances. |
| BR-06 | Datos personales y respuestas de alumnos no ingresan a solicitudes de IA. |
| BR-07 | La métrica primaria suma tokens de entrada y salida por unidad aprobada; precio, modelo y volumen publicado se reportan aparte. |
| BR-08 | Línea base y variante optimizada usan las mismas tareas, fuentes y umbral de calidad. |
| BR-09 | Una solicitud de IA originada en la plataforma se mide o se rechaza antes del proveedor; no existe una tercera salida. |
| BR-10 | Gobierno recibe participación agregada; prompts y entregas individuales quedan fuera de su vista. |
| BR-11 | Un Profesor de Provincia solo sincroniza paquetes asignados a su sede y curso. |
| BR-12 | Una revocación impide nuevas aperturas después de que la sede la recibe; no se afirma efecto retroactivo mientras estuvo desconectada. |
| BR-13 | La última comunicación de una sede siempre se muestra junto a su estado; silencio no significa entrega fallida. |
| BR-14 | La caída de Internet no elimina contenido completo ni trabajo local pendiente. |
| BR-15 | Un recurso audiovisual obligatorio tiene una alternativa de bajo consumo con el mismo objetivo pedagógico. |
