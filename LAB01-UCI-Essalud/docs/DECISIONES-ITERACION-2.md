# Decisiones de la iteración 2

Este registro cierra las cuestiones que condicionaban la segunda iteración de requerimientos. Las
decisiones se aplican en `Requirements/` y se conservan aquí con su fundamento para no resolverlas
de forma implícita.

## D-01 — Jornada de profesionales rotantes

Cada profesional se valida contra las reglas de jornada y descanso asociadas a su vínculo laboral
vigente. Los rotantes asignados por la Red no heredan por defecto el régimen del personal de planta:
la Red debe suministrar sus reglas aplicables y sus horas realizadas en cualquier sede.

**Consecuencia:** una asignación se rechaza cuando infringe las reglas asociadas al profesional; si
esas reglas no están disponibles, el profesional no se presenta como candidato elegible.

## D-02 — Unidad de la meta de 10 M

La meta de 10 M se interpreta como **10 millones de unidades UCI federadas registradas**, no como 10
millones de hospitales físicos peruanos. Una unidad federada es una unidad lógica con identidad,
camas y programación propias, adscrita a una sede. La ventana de cambio de turno conserva el supuesto
de 2 % de actividad concurrente: 200 000 unidades.

## D-03 — Atención del derecho de acceso

La solicitud de acceso del titular se registra y se deriva al responsable institucional de datos
personales. El plazo máximo de respuesta es de 20 días contados desde el día siguiente de la
presentación. Puede ampliarse una sola vez, como máximo por otros 20 días, cuando exista justificación
comunicada dentro del plazo inicial.

**Fuente:** [Decreto Supremo N.° 016-2024-JUS](https://cdn.www.gob.pe/uploads/document/file/7568330/6426760-decreto-supremo-n-016-2024-jus-reglamento-de-la-ley-n-29733-ley-de-proteccion-de-datos-personales-publicado-nov-2024.pdf), artículos 69.2 y 71.

## D-04 — Intercambio con RENHICE

La línea base técnica es la guía CorePE v0.1 publicada por MINSA, basada en HL7 FHIR R4 e IPS Perú.
Como la guía está publicada como borrador, cada intercambio registra la versión del perfil y los
catálogos empleados. Cuando MINSA publique una versión posterior exigible, esa versión reemplaza la
línea base sin cambiar el significado de los conceptos del dominio.

**Fuentes:** Ley N.° 30024, su reglamento, la Directiva Administrativa N.° 266-MINSA/2019/OGTI y la
[guía de implementación CorePE publicada por MINSA](https://dyaku.minsa.gob.pe/guides/index.html).

## D-05 — Adopción del sistema

La programación y el registro clínico conservados por el sistema son la fuente oficial. La salida
imprimible es una vista de consulta y no una segunda fuente editable. Las tareas críticas deben poder
completarse sin transcribir nuevamente información ya registrada y dentro de los umbrales de
usabilidad de `Requirements/ReqNoFunc.MD`.

## D-06 — Forma de las iteraciones

Una corrida mide una sola versión confirmada de los requerimientos y no los corrige. Cada resultado
se archiva. Si no alcanza 100 %, la corrección ocurre en una nueva versión y se mide mediante otra
corrida, sin modificar la evidencia anterior.
