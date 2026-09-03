# Decisiones de arquitectura

Cada decisión registra contexto, elección y costo. El historial de cambios vive en Git.

## D-01 — Se conservan exactamente los cuatro usuarios indicados

**Contexto.** Gobierno, Alumnos, Profesores de Lima y Profesores de Provincia ven fallas distintas.

**Decisión.** Los cuatro tienen persona, recorrido, permisos y un punto propio en D1 del EVAL.

**Consecuencia.** La costura completa queda visible. A cambio, ningún rol técnico adicional gana voz
en la rúbrica; operación y soporte aparecen como componentes o reglas, no como personas.

## D-02 — La sede tiene un nodo local

**Contexto.** Una aplicación alojada únicamente en Lima vuelve a depender de Internet durante cada
clase, que es justamente la restricción del caso.

**Decisión.** Cada sede opera un nodo local que sincroniza durante ventanas de conexión y sirve el
paquete por Wi-Fi/LAN mientras el enlace externo está caído.

**Consecuencia.** La clase deja de depender del enlace. El costo es administrar almacenamiento,
identidades cacheadas y actualizaciones en equipos remotos.

## D-03 — Los paquetes son inmutables y los recursos son direccionables por contenido

**Contexto.** Reanudar y reutilizar archivos exige saber si dos fragmentos son realmente iguales.

**Decisión.** Cada publicación crea un manifiesto inmutable; cada recurso se identifica por su huella.

**Consecuencia.** Se puede verificar integridad, deduplicar y reanudar. Corregir un recurso exige una
nueva versión; no existe edición silenciosa de un paquete publicado.

## D-04 — Toda IA pasa por una única frontera medible

**Contexto.** Si cada pantalla llama al proveedor por su cuenta, no existe consumo completo ni una
política común.

**Decisión.** Un AI Gateway aplica presupuesto, contexto máximo, salida máxima, reutilización y
medición antes de delegar al proveedor externo.

**Consecuencia.** El 40 % se vuelve auditable. El gateway es una dependencia central de la ayuda de
IA, pero no de la autoría manual ni de la publicación ya revisada.

## D-05 — El 40 % usa una comparación pareada y normalizada

**Contexto.** El gasto total baja si se publica menos o cambia el precio aunque el uso sea igual.

**Decisión.** Se compara entrada + salida por unidad aprobada sobre las mismas tareas y la misma
rúbrica; se versionan línea base y política.

**Consecuencia.** La cifra resiste cambios de volumen y precio. Exige mantener un corpus de
comparación y repetirlo cuando cambie materialmente el flujo de autoría.

## D-06 — Correctitud de entrega no equivale a alta disponibilidad

**Contexto.** El enunciado posterga 100 % de disponibilidad y mecanismos avanzados de confiabilidad,
pero exige que los cursos lleguen correctamente.

**Decisión.** Se incluyen manifiesto, huellas, reanudación, última versión completa y bandeja local;
se excluyen multi-región, quorum, réplica activa-activa y failover automático.

**Consecuencia.** El diseño cumple el problema sin fingir una operación de producción. Una caída
central puede retrasar la próxima sincronización, pero no corrompe un paquete ya listo.

## D-07 — Spec Kit mantiene una spec viva

**Contexto.** A diferencia del LAB03, este enunciado no obliga a un backlog de títulos sin descripción.

**Decisión.** `specs/001-remoteschooly/spec.md` es la única fuente de verdad de comportamiento;
plan, datos, contratos, EVAL y arquitectura derivan de ella.

**Consecuencia.** Las fases oficiales `specify`, `plan`, `tasks` y `analyze` tienen artefactos reales.
Duplicar requisitos en otro backlog queda prohibido.

## D-08 — El diagrama tiene tres iteraciones top-down

**Contexto.** El laboratorio declara top-down design y puntúa los happy paths.

**Decisión.** La iteración 1 muestra actores y sistema; la 2 abre centro y sede; la 3 abre servicios,
datos, proveedor de IA, sincronización y recorridos numerados.

**Consecuencia.** Cada paso agrega únicamente lo que el anterior no podía explicar. Mantener tres
diagramas cuesta, pero vuelve visible el razonamiento y no solo el resultado final.
