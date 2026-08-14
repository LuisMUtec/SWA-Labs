# Prompt de ejecución — Additional V2

Trabajas dentro del repositorio:

`LuisMUtec/SWA-LAB01-UCI-Essalud`

Proyecto: Arquitectura de Software, UTEC 2026-II.  
Dominio: sistema de gestión de UCI de Essalud.

## Objetivo

Ejecutar de forma completa y auditable la sección **Additional** de
`docs/V2-LAB-01-ARQ-2026.2.md`:

1. Crear un agente evaluador por cada persona.
2. Evaluar `Requirements/ReqFunc.MD` desde las cuatro personas.
3. Calcular el porcentaje global mediante `Spec/Eval-Spec.MD`.
4. Documentar iteraciones reales.
5. Corregir únicamente los requerimientos funcionales cuando el resultado sea `FAILED`.
6. Detenerse al obtener `PASSED` o después de tres iteraciones.
7. No hacer commit, push ni pull request sin autorización explícita.

No copies los puntajes ilustrativos de la V2. Debes realizar una evaluación nueva sobre el estado actual del repositorio.

---

## 1. Precedencia de las fuentes

Cuando exista una duda, aplica este orden:

1. `Personas/Rodrigo.MD`, `Personas/Milagros.MD`, `Personas/Carmen.MD` y `Personas/Anibal.MD`.

   Son la única fuente válida de tareas críticas, criterios de éxito, contexto, frustraciones y restricciones de cada persona.

2. `Personas/README.md`.

   Es la fuente de las tensiones entre personas y decisiones que deben reflejarse en los requerimientos.

3. `Spec/Eval-Spec.MD`.

   Fija la rúbrica global D1–D6, los pesos, las reglas duras y el formato del diagnóstico.

4. `docs/CONVENCIONES.md`.

   Fija la forma de RF, criterios de aceptación, trazabilidad, prioridad, separación RF/RNF y los controles mecánicos.

5. `docs/V2-LAB-01-ARQ-2026.2.md`.

   Exige el puntaje por persona, el reporte y las iteraciones. Sus tablas de Roberto y Pablo son ejemplos del enunciado, no resultados del proyecto.

No edites ninguna de estas fuentes para elevar el puntaje.

> **Importante:** los promedios mostrados como ejemplo en la V2 son matemáticamente inconsistentes. No los copies ni los uses como fórmula. Los puntajes y promedios de esta ejecución deben calcularse desde cero.

---

## 2. Alcance de la evaluación

Se evalúa exclusivamente:

`Requirements/ReqFunc.MD`

`Requirements/ReqNoFunc.MD` no suma ni resta en el porcentaje. Si una afirmación no funcional aparece dentro de `ReqFunc.MD`, repórtala como requerimiento mal ubicado.

Utiliza únicamente estos cuatro agentes como agentes de persona:

- `Agents/agent-rodrigo.MD`
- `Agents/agent-milagros.MD`
- `Agents/agent-carmen.MD`
- `Agents/agent-anibal.MD`

`Agents/README.md` y `Agents/_TEMPLATE.md` no son personas ni fuentes de necesidades.

No consultes fuentes externas. El repositorio es la única fuente de verdad.

---

## 3. Preparación Git

Antes de modificar archivos:

1. Comprueba que el repositorio no tenga cambios locales.
2. Ejecuta `fetch` de `origin`.
3. Cambia a `main`.
4. Actualiza `main` exclusivamente mediante fast-forward desde `origin/main`.
5. Confirma que `main` queda limpio y sincronizado.
6. Crea la rama:

   `eval/additional-v2`

Si existen cambios locales, `main` no puede actualizarse mediante fast-forward o la rama ya existe, detente y repórtalo. No descartes, sobrescribas ni escondas cambios.

No hagas commit, push, merge ni pull request durante esta ejecución.

Emite:

`✅ Preparación Git completada`

---

## 4. Archivos editables

Puedes crear o modificar exclusivamente:

- `Agents/agent-rodrigo.MD`
- `Agents/agent-milagros.MD`
- `Agents/agent-carmen.MD`
- `Agents/agent-anibal.MD`
- `Agents/README.md`
- `Requirements/ReqFunc.MD`
- `Spec/Eval-Report.MD`
- La aparición final del porcentaje en la línea “Resultado del agente” de `README.md`.

Todos los demás archivos son de solo lectura, incluidos:

- `Personas/*`
- `docs/*`
- `Spec/Eval-Spec.MD`
- `Requirements/ReqNoFunc.MD`
- `Agents/_TEMPLATE.md`

En `README.md` reemplaza solamente el marcador final `**__ %**` de la línea “Resultado del agente”. Conserva literalmente el resto de esa línea, incluso su formato actual. No aproveches la edición para corregir enlaces ni otros contenidos.

No añadas dependencias, scripts, configuración, workflows, plantillas, carpetas ni archivos distintos de los enumerados.

---

## 5. Paso 0 — Creación de los agentes

Crea los cuatro archivos `Agents/agent-<nombre>.MD` usando la estructura de `Agents/_TEMPLATE.md`.

Para cada agente:

- Deriva identidad, contexto, necesidades, tareas, restricciones, frustraciones, escenario clave y criterios de éxito únicamente de su archivo `Personas/<Nombre>.MD`.
- No introduzcas ninguna tarea, necesidad, restricción o preferencia que la persona no documente.
- No copies información de otra persona.
- No conviertas RNF en necesidades personales.
- Declara que una ambigüedad se penaliza y nunca se interpreta de forma favorable.
- Declara que el alcance evaluado es únicamente `ReqFunc.MD`.
- Mantén el nombre del archivo en minúsculas y sin tilde: `agent-anibal.MD`.

Actualiza `Agents/README.md` para sustituir la fila pendiente por las cuatro filas reales, enlazando cada agente con su persona.

Después, verifica:

- Existen exactamente cuatro agentes de persona.
- Cada uno enlaza a la persona correcta.
- No queda la fila `_(pendiente)_`.
- Ningún agente contiene necesidades ajenas a su persona.

Emite:

`✅ 4 agentes creados y Agents/README.md actualizado`

---

## 6. Ciclo de evaluación

Ejecuta como máximo tres iteraciones.

Cada iteración debe releer desde disco todos los insumos. No reutilices veredictos, matrices ni puntajes de una iteración anterior.

Cada iteración contiene las fases A, B y C. La fase D se ejecuta únicamente cuando el resultado sea `FAILED` y todavía quede otra iteración disponible.

### Fase A — Evaluación independiente por persona

Realiza cuatro evaluaciones independientes:

1. Rodrigo.
2. Milagros.
3. Carmen.
4. Aníbal.

Adopta íntegramente el agente correspondiente y recorre todos los RF, sin omitir ningún ID.

Para cada RF asigna exactamente uno de estos veredictos:

- **Sirve:** aporta de forma explícita a una tarea, criterio de éxito o escenario de la persona.
- **Indiferente:** no afecta de forma relevante a esa persona.
- **Estorba:** introduce un conflicto, riesgo o fricción con su trabajo.
- **Ambiguo:** admite más de una interpretación o depende de una capacidad que el enunciado no declara.

Justifica cada veredicto en una sola frase, anclada al trabajo cotidiano de la persona.

Reglas:

- No atribuyas al RF capacidades implícitas.
- No uses criterios de aceptación para ampliar el comportamiento que el enunciado del RF no declara.
- Si admite más de una lectura, es `Ambiguo`.
- Un RF ambiguo nunca puede contar como cobertura total.
- Un RF marcado `Estorba` no cuenta como cobertura de la tarea afectada.
- Recorre las seis tareas críticas de la persona una por una.
- Contrasta también sus criterios de éxito.
- Recorre su escenario clave de extremo a extremo encadenando RF.
- Si el flujo se interrumpe, identifica el paso exacto.
- No redactes soluciones ni RF nuevos en esta fase.

---

## 7. Fórmula del puntaje por persona

La puntuación individual usa la intención de la rúbrica adicional `5/1/0 + 4`, normalizada a 10 puntos.

### A. Cobertura de necesidades: máximo 6 puntos

Evalúa cada una de las seis tareas críticas:

- **5 puntos internos:** cobertura total.
- **1 punto interno:** cobertura parcial o dependiente de un RF ambiguo.
- **0 puntos internos:** sin cobertura o cubierta únicamente por un RF que `Estorba`.

Una tarea solo es cobertura total cuando:

- Al menos un RF declara explícitamente el comportamiento necesario.
- El conjunto de RF cubre la tarea completa.
- Se satisfacen los criterios de éxito relacionados.
- No hay contradicción entre los RF usados.

Calcula:

```text
Cobertura de necesidades =
suma de puntos internos de las seis tareas / 5
```

El resultado queda entre 0 y 6.

### B. Claridad del flujo: máximo 4 puntos

- **4 puntos:** el escenario clave puede recorrerse completo, en orden, con RF explícitos y sin saltos ni interpretaciones favorables.
- **0 puntos:** el flujo se interrumpe, depende de comportamiento no declarado o contiene un salto ambiguo.

### C. Puntaje individual

```text
Puntaje de persona =
Cobertura de necesidades + Claridad del flujo
```

Máximo: 10.

```text
Cobertura percibida = Puntaje de persona × 10 %
```

Muestra los cálculos. Redondea el puntaje individual a un decimal.

El promedio de la iteración es la media aritmética de los cuatro puntajes individuales mostrados. Redondea una sola vez, al final, a un decimal.

Emite:

`✅ Fase A completada — cuatro evaluaciones independientes`

### Fase B — Agregación mediante Eval-Spec

Aplica `Spec/Eval-Spec.MD` sobre los RF y sobre las cuatro evaluaciones de la fase A.

Construye primero estas evidencias:

1. Matriz de las 24 tareas críticas: persona × tarea → RF → estado.
2. Matriz de P1, P2 y P3: problema → RF → comportamiento que lo resuelve → estado.
3. Inventario de todos los RF: ID → forma EARS → respuesta atómica → sujeto del DEBE → criterios de aceptación → trazabilidad → prioridad → resultado.
4. Matriz de las cinco tensiones de `Personas/README.md`: tensión → RF que la decide → estado.

Puntúa las dimensiones así:

#### D1 — Cobertura de personas

- Usa los valores internos `5/1/0` de las 24 tareas.
- `D1 = suma obtenida / 120 × 100`.
- Un RF `Ambiguo` permite como máximo cobertura parcial.
- Un RF `Estorba` no cubre la tarea afectada.
- Aplica las reglas duras de `Eval-Spec`.

#### D2 — Problemas críticos

Para P1, P2 y P3 asigna:

- **100:** resuelto de extremo a extremo por RF explícitos.
- **50:** parcialmente resuelto.
- **0:** solo nombrado o no resuelto.

D2 es el promedio de los tres valores.

Si algún problema obtiene 0, aplica el límite de `Eval-Spec`: D2 no puede superar 60.

#### D3 — Verificabilidad y forma

Un RF es conforme únicamente si cumple simultáneamente:

- Un patrón EARS identificable.
- Una sola respuesta.
- El sistema es el sujeto del `DEBE`.
- Declara garantía y no mecanismo.
- No contiene interfaz ni tecnología.
- Tiene criterios de aceptación.
- Cada criterio contiene un solo par Cuando/Entonces.
- Los criterios no amplían el contrato del enunciado.

`D3 = RF conformes / total de RF × 100`.

No declares conforme un RF que falle cualquiera de estas condiciones.

#### D4 — Trazabilidad

Calcula:

- **70 %:** proporción de RF que trazan correctamente a persona y problema.
- **30 %:** proporción de las 24 tareas con al menos cobertura parcial.

Las matrices internas de `ReqFunc.MD` deben coincidir con el cuerpo. Una matriz desactualizada cuenta como defecto de trazabilidad.

#### D5 — Consistencia

- 60 puntos corresponden a las cinco tensiones: 12 puntos por cada tensión decidida explícitamente por RF.
- 40 puntos corresponden a ausencia de contradicciones, duplicados encubiertos y uso inconsistente del vocabulario.
- Resta 10 de esos 40 puntos por cada contradicción, duplicado o inconsistencia independiente, sin bajar de 0.

El repositorio no contiene actualmente un glosario separado. No inventes uno ni modifiques `docs`. Decláralo como limitación de la evaluación y, mientras falte, D5 no puede superar 80.

#### D6 — Priorización

Empieza en 100 y aplica:

- Resta 10 por cada RF sin prioridad o con prioridad inválida.
- Resta 5 por cada MUST cuya ausencia no deje descubierto un problema crítico o una tarea crítica.
- Si todos los RF usan la misma prioridad, D6 no puede superar 60.
- El mínimo es 0.

#### Cálculo global

```text
Global =
D1×0.30 + D2×0.25 + D3×0.20 +
D4×0.10 + D5×0.10 + D6×0.05
```

Muestra cada dimensión, peso y aporte. Utiliza un decimal como máximo y verifica que la suma de los aportes coincida con el resultado global.

Ante la duda se penaliza. Un puntaje alto debe estar respaldado por evidencia trazable.

Emite:

`✅ Fase B completada — porcentaje global calculado`

### Fase C — Veredicto

La iteración obtiene `PASSED` únicamente si cumple simultáneamente:

1. Puntaje global ≥ 80.0 %.
2. Promedio de las cuatro personas ≥ 8.0/10.
3. Ninguna persona < 7.0/10.
4. D2 ≥ 80.0.
5. Los cuatro controles mecánicos de `docs/CONVENCIONES.md` devuelven vacío.

Si falla una sola condición, el resultado es `FAILED`.

No redondees un valor hacia arriba para atravesar un umbral.

Emite una de estas líneas:

`✅ Fase C completada — ITERACION #N: PASSED`

o:

`✅ Fase C completada — ITERACION #N: FAILED`

### Fase D — Corrección controlada

Ejecuta esta fase solamente si:

- La iteración fue `FAILED`.
- Todavía no se realizaron tres iteraciones.
- La corrección cabe dentro de los archivos editables.

Modifica exclusivamente `Requirements/ReqFunc.MD`.

Prioriza:

1. Tareas críticas sin cobertura.
2. P1, P2 o P3 incompletos.
3. RF ambiguos, no atómicos o mal formados.
4. Trazabilidad incompleta.
5. Tensiones sin decidir.
6. Priorización injustificada.

Cada cambio debe:

- Trazar a una brecha concreta de la iteración anterior.
- Mantener un solo patrón EARS.
- Contener una sola respuesta.
- Usar al sistema como sujeto del `DEBE`.
- Declarar comportamiento observable.
- Evitar interfaz, navegación, tecnología y mecanismos.
- Incluir criterios de aceptación deterministas.
- Declarar persona, problema y prioridad.
- Mantener actualizadas todas las matrices y resúmenes internos.
- Usar `[ACLARAR: pregunta concreta]` o `[SUPUESTO: enunciado]` cuando falte información.

Al agregar un RF:

- No renumeres RF existentes.
- Usa el siguiente número disponible dentro del área correspondiente.
- Actualiza conteos, distribución de prioridades y matrices.

Al dividir un RF no atómico:

- Conserva el ID original para una de las respuestas.
- Crea un ID nuevo para la otra.
- Conserva o ajusta su trazabilidad con evidencia.
- No elimines silenciosamente comportamiento existente.

Prohibido:

- Modificar personas, agentes, convenciones, Eval-Spec o RNF.
- Suavizar criterios de evaluación.
- Inventar necesidades.
- Añadir RF genéricos para elevar D1.
- Añadir comportamiento que no responda a una brecha identificada.
- Eliminar un RF para ocultar una contradicción.
- Modificar los puntajes manualmente.

Registra el diff conceptual:

- ID agregado, modificado o dividido.
- Brecha exacta que corrige.
- Persona, tarea o problema beneficiado.
- Efecto esperado en la siguiente iteración.

Emite:

`✅ Fase D completada — correcciones preparadas para ITERACION #N+1`

Después, relee todos los archivos y comienza una evaluación nueva.

---

## 8. Controles obligatorios

Ejecuta estos cuatro controles desde la raíz antes de declarar `PASSED`:

```bash
grep -nE "^\*\*Enunciado:\*\*" Requirements/ReqFunc.MD | grep -v "DEBE"

grep -nEi "el médico DEBE|la enfermera DEBE|el coordinador DEBE|el hospital DEBE|el equipo DEBE" Requirements/*.MD

grep -nEi "kafka|redis|websocket|microservicio|kubernetes|base de datos|caché|endpoint|push" Requirements/*.MD

grep -nE "~~|\(Decidido|\(Refinado|\(Corregido|versión anterior|por ahora" README.md Requirements/*.MD Personas/*.MD
```

Los cuatro deben devolver vacío.

También verifica:

- No hay IDs de RF duplicados.
- Cada RF tiene enunciado, prioridad, persona, problema y al menos un criterio de aceptación.
- Las matrices internas de `ReqFunc.MD` solo referencian IDs existentes.
- `git diff --name-only` contiene exclusivamente archivos editables.
- No se modificó ningún archivo de solo lectura.

Incluye el resultado literal de estos controles en `Eval-Report.MD`.

---

## 9. Entregable — Spec/Eval-Report.MD

Crea `Spec/Eval-Report.MD`.

Encabezado:

```markdown
# Reporte de Evaluación de Requerimientos Funcionales
## Sistema de Gestión UCI — Essalud
```

Incluye una sección por iteración con esta estructura:

```markdown
## ITERACION #N

### Evaluación de Rodrigo

Tabla completa ID → veredicto → justificación.
Tareas y criterios no cubiertos.
Recorrido del escenario.
Cálculo del puntaje.

### Evaluación de Milagros

Mismo contenido.

### Evaluación de Carmen

Mismo contenido.

### Evaluación de Aníbal

Mismo contenido.

### Puntajes por persona

| Persona | Necesidades /6 | Flujo /4 | Score |
|---|---:|---:|---:|
| Rodrigo | | | _/10 |
| Milagros | | | _/10 |
| Carmen | | | _/10 |
| Aníbal | | | _/10 |
| PROMEDIO | | | _/10 — PASSED / FAILED |

### Puntaje global: __ %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Cobertura de personas | | 30 % | |
| D2 Cobertura de problemas críticos | | 25 % | |
| D3 Verificabilidad y forma | | 20 % | |
| D4 Trazabilidad | | 10 % | |
| D5 Consistencia | | 10 % | |
| D6 Priorización | | 5 % | |

### Veredicto
### Matriz de cobertura
### Cobertura de P1, P2 y P3
### Brechas encontradas
### Tensiones sin decidir
### Requerimientos huérfanos
### Requerimientos mal formados
### Requerimientos mal ubicados
### Acciones recomendadas (priorizadas)
### Controles de convenciones
```

En las iteraciones posteriores a la primera, comienza además con:

```markdown
### Cambios respecto a la iteración anterior

| ID | Cambio | Brecha cerrada |
|---|---|---|
```

Y termina con:

```markdown
### Delta
```

Explica qué dimensión cambió, cuánto cambió y qué evidencia produjo el cambio. No atribuyas una mejora a una corrección que no afecte esa dimensión.

Cierre del documento:

```markdown
## Resultado final: __ %

- Iteraciones ejecutadas: N
- Veredicto final: PASSED / FAILED
- Promedio final de personas: _/10
- Puntaje global final: _ %
- Brechas abiertas: N
```

El resultado final debe coincidir con la última iteración.

---

## 10. Actualización del README

Cuando termine la última iteración, actualiza exclusivamente el marcador `**__ %**` de la línea final “Resultado del agente” en `README.md`.

Usa el porcentaje global de la última iteración, incluso si el resultado final es `FAILED`.

No modifiques ninguna otra parte del README.

Emite:

`✅ Eval-Report.MD creado y resultado de README.md actualizado`

---

## 11. Condiciones de parada

Detente y solicita autorización antes de:

- Eliminar un RF existente.
- Mover contenido entre `ReqFunc.MD` y `ReqNoFunc.MD`.
- Modificar un archivo de solo lectura.
- Crear un archivo no autorizado.
- Cambiar una persona, tarea crítica o criterio de éxito.
- Cambiar Eval-Spec, la rúbrica o las convenciones.
- Hacer commit, push, merge o pull request.

Si una corrección necesaria depende de cualquiera de esas acciones, repórtala como bloqueada y no la sustituyas por una solución inventada.

Si la tercera iteración sigue en `FAILED`:

- Conserva las tres iteraciones en `Eval-Report.MD`.
- Documenta todas las brechas restantes.
- Actualiza README con el porcentaje real.
- Detente.
- Nunca fuerces `PASSED`.

---

## 12. Reporte final en la conversación

Al terminar informa:

- Rama creada.
- Número de iteraciones.
- Resultado de cada iteración.
- Puntajes individuales finales.
- Promedio final.
- D1–D6 finales.
- Porcentaje global.
- `PASSED` o `FAILED`.
- RF agregados, modificados o divididos.
- Archivos creados y modificados.
- Resultado de los cuatro controles.
- Brechas todavía abiertas.
- Estado de Git.

No hagas commit ni subas cambios. Termina preguntando si se autoriza crear el commit y el pull request.
