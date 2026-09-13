# EVAL de requisitos de RemoteSchooly

Este aparato puntúa únicamente [`specs/001-remoteschooly/spec.md`](../specs/001-remoteschooly/spec.md).
Los diagramas no suman ni corrigen el puntaje. El gate del laboratorio es **mayor a 8**; este
repositorio adopta la condición conservadora **≥ 8.0/10** y exige además los cuatro veredictos.

## Entradas

| Entrada | Quién la lee | Para qué |
|---|---|---|
| `specs/001-remoteschooly/spec.md` | Todos | Única fuente de comportamiento y métricas |
| Una persona de `personas/` | Su evaluador | Juzgar el recorrido desde esa posición |
| `personas/README.md` | Agregador | Comprobar las siete tensiones |
| `docs/LAB-04-ARQ-2026.2.md` | Agregador | Contrastar el ajuste literal al problema |
| `.specify/memory/constitution.md` | Agregador | Aplicar los gates no negociables |

## Rúbrica — 10 puntos

| Dimensión | Puntos | Qué mide |
|---|---:|---|
| D1. Cuatro personas | 4 | Un punto por recorrido completo, incluido su fallo principal; los evaluadores solo restan |
| D2. Ajuste al caso | 2 | Internet limitado y entrega semanal (0,75), Lima → regiones y uso offline local (0,75), ahorro comparable ≥ 40 % (0,50) |
| D3. Verificabilidad | 2 | Requisitos observables y atómicos (1), criterios medibles con casos de falla (1) |
| D4. Coherencia y alcance | 2 | Propietario, permiso, tensión, supuesto y trazabilidad sin contradicción ni mecanismo disfrazado |

**Condiciones de aprobación**:

1. Total ≥ 8.0/10.
2. Están presentes los cuatro veredictos de persona.
3. D2 no es menor a 1.5/2; un sistema educativo genérico no puede aprobar.
4. El ahorro de tokens tiene línea base, normalización y control de calidad; si falta cualquiera,
   D2 no supera 1.5 y D3 no supera 1.5.

## D1 — regla de asimetría

Cada evaluador lee la spec y solo su persona. Empieza con un punto y puede restar:

| Veredicto | Resta | Condición |
|---|---:|---|
| `Funciona` | 0 | Todos los pasos y el fallo principal tienen requisitos citables |
| `Funciona con reservas` | 0,5 | El recorrido cierra, pero una decisión queda parcial o ambigua |
| `No funciona` | 1 | Falta un paso, no se cubre el fallo principal o se viola un permiso |

Una cita inexistente o un veredicto sin citas vale `No funciona`. Un evaluador no agrega necesidades
nuevas ni negocia con otros roles: señala dónde su propio día se corta.

## D2 — ajuste al problema

El agregador aplica tres pruebas contrafácticas:

1. Si Internet fuera estable, ¿qué requisitos dejarían de ser necesarios? Deben existir requisitos
   de reanudación, integridad, última versión completa y uso offline.
2. Si el contenido naciera en cada sede, ¿qué requisitos dejarían de ser necesarios? Deben existir
   publicación desde Lima, asignación, sincronización y telemetría de regreso.
3. Si el gasto de tokens no importara, ¿qué requisitos dejarían de ser necesarios? Deben existir
   medición, línea base comparable, calidad constante y meta de 40 %.

Nombrar el rasgo sin cambiar ningún comportamiento da cero en ese rasgo.

## D3 — verificabilidad

Un requisito aprueba si alguien puede construir evidencia que lo confirme o refute sin adivinar la
intención. Las palabras `rápido`, `seguro`, `eficiente`, `correcto` o `optimizado` no cuentan sin
medida, estado o invariante. Los criterios de éxito deben probar también interrupción, corrupción,
duplicado y privacidad, no solo el camino feliz.

## D4 — coherencia y alcance

D4 empieza en 2 y resta 0,25 por hallazgo, con piso 0:

- requisito sin dueño o sin permiso compatible;
- duplicado encubierto o dos resultados separables bajo un solo identificador;
- tensión de `personas/README.md` sin decisión;
- supuesto presentado como hecho o `[CLARIFY]` sin resolver;
- decisión de arquitectura escrita dentro de un requisito de comportamiento;
- criterio de éxito sin requisitos que lo produzcan;
- contradicción con una regla de negocio o con la constitución.

**Techos duros**: si dos tensiones quedan abiertas, D4 ≤ 1; si hay un componente del plan sin
requisito, D4 ≤ 1,5; si todos los requisitos tienen la misma prioridad o ninguna, D4 ≤ 1,5.

## Protocolo de una corrida

1. Fijar el SHA o la huella exacta de la spec antes de evaluar.
2. Ejecutar los cuatro evaluadores por separado con su par de archivos permitido.
3. Ejecutar el agregador con los cuatro veredictos, el enunciado, tensiones y constitución.
4. Verificar aritmética, citas y condiciones de aprobación.
5. Guardar el resultado inmutable en `evals/iterations/` y agregar una fila a `HISTORY.md`.
6. Si no aprueba, corregir la spec en otro commit y abrir una corrida nueva; nunca reescribir una
   corrida anterior.
