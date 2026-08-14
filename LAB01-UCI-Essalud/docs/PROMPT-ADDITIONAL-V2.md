# Prompt de ejecución — Evaluación de requerimientos funcionales

Trabajas dentro del repositorio:

`LuisMUtec/SWA-LAB01-UCI-Essalud`

Proyecto: Arquitectura de Software, UTEC 2026-II.  
Dominio: sistema de gestión de UCI de Essalud.

## Objetivo

Evaluar `Requirements/ReqFunc.MD` desde las cuatro personas modelo y emitir el porcentaje de calidad
que indica si los requerimientos las satisfacen:

1. Comprobar que los cuatro agentes de persona derivan de su persona.
2. Evaluar los requerimientos funcionales desde cada una de las cuatro perspectivas.
3. Calcular el porcentaje global con la rúbrica de `Spec/Eval-Spec.MD`.
4. Documentar iteraciones reales.
5. Corregir únicamente los requerimientos funcionales cuando el resultado sea `FAILED`.
6. Detenerse al obtener `PASSED` o después de tres iteraciones.
7. No hacer commit, push ni pull request sin autorización explícita.

La evaluación se realiza sobre el estado actual del repositorio. No se reutiliza ningún puntaje
previo ni ilustrativo.

---

## 1. Precedencia de las fuentes

Cuando exista una duda, aplica este orden:

1. `Personas/Rodrigo.MD`, `Personas/Milagros.MD`, `Personas/Carmen.MD` y `Personas/Anibal.MD`.

   Son la única fuente válida de tareas críticas, criterios de éxito, contexto, frustraciones,
   escenario clave y restricciones de cada persona.

2. `Personas/README.md`.

   Es la fuente de las tensiones entre personas y de las decisiones que deben reflejarse en los
   requerimientos.

3. `Spec/Eval-Spec.MD`.

   Fija la rúbrica D1–D6, los pesos, la escala de puntaje por persona, las reglas duras, las cinco
   condiciones del veredicto y el formato del diagnóstico. **Este prompt no redeclara ninguna de esas
   cifras**: si una discrepancia aparece, manda `Eval-Spec`.

4. `docs/CONVENCIONES.md`.

   Fija la forma de RF, criterios de aceptación, trazabilidad, prioridad y separación RF/RNF.

No edites ninguna de estas fuentes para elevar el puntaje. Son la vara con la que se mide, y una vara
que se ajusta para alcanzar el número deja de medir.

---

## 2. Alcance de la evaluación

Se evalúa exclusivamente:

`Requirements/ReqFunc.MD`

`Requirements/ReqNoFunc.MD` no suma ni resta en el porcentaje. Si una afirmación no funcional aparece
dentro de `ReqFunc.MD`, repórtala como requerimiento mal ubicado.

Utiliza únicamente estos cuatro agentes como agentes de persona:

- `Agents/agent-rodrigo.MD`
- `Agents/agent-milagros.MD`
- `Agents/agent-carmen.MD`
- `Agents/agent-anibal.MD`

`Agents/README.md` y `Agents/_TEMPLATE.md` no son personas ni fuentes de necesidades.

No consultes fuentes externas. El repositorio es la única fuente de verdad.

---

## 3. Preparación Git

Ejecuta desde la raíz:

```bash
scripts/preparar-git.sh eval/additional-v2 main
```

El script comprueba que no haya cambios locales, actualiza `main` solo por fast-forward, verifica que
la rama de trabajo no exista ni localmente ni en `origin`, y la crea. Ante cualquier condición que
obligaría a descartar, sobrescribir o esconder trabajo, aborta con el motivo y no toca nada.

**Si el script aborta, detente y reporta su mensaje.** No resuelvas a mano lo que el script se negó a
hacer: no ejecutes `stash`, `reset`, `checkout -f` ni reescribas historia.

No hagas commit, push, merge ni pull request durante esta ejecución.

Emite:

`✅ Preparación Git completada`

---

## 4. Archivos editables

Puedes crear o modificar exclusivamente:

- `Requirements/ReqFunc.MD`
- `Spec/Eval-Report.MD`
- `Spec/corridas/‹id-de-esta-corrida›/` y todo lo que va dentro
- `Spec/HISTORIAL.MD`, **solo agregando la fila de esta corrida**
- La aparición final del porcentaje en la línea «Resultado del agente» de `README.md`.

El identificador de la corrida es la fecha y la etiqueta de la rama:
`Spec/corridas/2026-08-13-additional-v2/`. No hay límite de corridas: cada una escribe su propio
directorio y no toca los de las anteriores. `Spec/corridas/_ESQUEMA.MD` fija qué va dentro y es de
solo lectura, como el resto de la vara.

Y, **solo durante el Paso 0** y solo sobre lo que la comprobación declare no conforme:

- `Agents/agent-rodrigo.MD`
- `Agents/agent-milagros.MD`
- `Agents/agent-carmen.MD`
- `Agents/agent-anibal.MD`
- `Agents/README.md`

Terminado el Paso 0, `Agents/*` queda de solo lectura durante el resto de la ejecución.

Todos los demás archivos son de solo lectura, incluidos `Personas/*`, `docs/*`, `Spec/Eval-Spec.MD`,
`Spec/corridas/_ESQUEMA.MD`, los directorios de corridas anteriores, `Requirements/ReqNoFunc.MD`,
`Agents/_TEMPLATE.md`, `scripts/*` y `.claude/*`.

En `README.md` reemplaza solamente el marcador final `**__ %**` de la línea «Resultado del agente».
Conserva literalmente el resto de esa línea, incluso su formato actual. No aproveches la edición para
corregir enlaces ni otros contenidos.

No añadas dependencias, configuración, workflows, plantillas ni archivos distintos de los enumerados.
La única carpeta que creas es la de tu corrida. `scripts/guardia-diff.sh` comprueba esta lista y se
ejecuta como control E4.

---

## 5. Paso 0 — Comprobación de los agentes de persona

Este paso se ejecuta **una sola vez**, antes de la primera iteración. No se repite en las iteraciones
siguientes: el ciclo del §6 vuelve a leer los agentes, nunca a rehacerlos.

Los agentes son el instrumento de medición. Si cambian entre una iteración y la siguiente, el `Delta`
del reporte deja de ser atribuible a las correcciones de `ReqFunc.MD`: no se sabría si mejoró el
requerimiento o se ablandó el evaluador.

Los cuatro agentes ya existen. Antes de evaluar, verifica que cada uno siga siendo fiel a su persona:

- Su identidad, contexto, necesidades, tareas, restricciones, frustraciones, escenario clave y
  criterios de éxito derivan únicamente de su archivo `Personas/<Nombre>.MD`.
- No contiene ninguna tarea, necesidad, restricción o preferencia que la persona no documente.
- No contiene información de otra persona.
- No convierte un RNF en necesidad personal.
- Declara que una ambigüedad se penaliza y nunca se interpreta de forma favorable.
- Declara que el alcance evaluado es únicamente `ReqFunc.MD`.

Verifica además que existan exactamente cuatro agentes de persona, que `Agents/README.md` enlace cada
uno con su persona y que no queden filas pendientes.

Corrige en el agente lo que se desvíe de su persona. **Si una necesidad legítima falta en la persona,
no la agregues al agente**: `Personas/*` es de solo lectura, así que repórtalo como bloqueado.

Interviene solo sobre la desviación concreta que detectes. No reescribas un agente que ya cumple, no
retoques su redacción y no ajustes ningún agente en función de los RF que va a evaluar.

Los agentes mencionan archivar su corrida en `Agents/Veredictos/`. Esa carpeta no se crea: en esta
ejecución los veredictos viven dentro de `Spec/Eval-Report.MD`.

Emite:

`✅ Paso 0 completado — cuatro agentes verificados`

Informa qué archivos tocaste. Si no tocaste ninguno, dilo explícitamente.

Desde aquí y hasta el final de la ejecución, `Agents/*` es de solo lectura. Si una iteración posterior
necesitara cambiar un agente, detente y repórtalo según el §10.

---

## 6. Ciclo de evaluación

Ejecuta como máximo tres iteraciones.

Cada iteración relee desde disco todos los insumos. No reutilices veredictos, matrices ni puntajes de
una iteración anterior.

Cada iteración contiene las fases A, B y C. La fase D se ejecuta únicamente cuando el resultado sea
`FAILED` y todavía quede otra iteración disponible.

### Fase A — Evaluación independiente por persona

Realiza cuatro evaluaciones independientes: Rodrigo, Milagros, Carmen y Aníbal.

Adopta íntegramente el agente correspondiente y recorre todos los RF, sin omitir ningún ID. Para cada
uno asigna exactamente uno de estos veredictos:

- **Sirve:** aporta de forma explícita a una tarea, criterio de éxito o escenario de la persona.
- **Indiferente:** no afecta de forma relevante a esa persona.
- **Estorba:** introduce un conflicto, riesgo o fricción con su trabajo.
- **Ambiguo:** admite más de una interpretación o depende de una capacidad que el enunciado no declara.

Justifica cada veredicto en una sola frase, anclada al trabajo cotidiano de la persona.

Reglas:

- No atribuyas al RF capacidades implícitas.
- No uses los criterios de aceptación para ampliar el comportamiento que el enunciado no declara.
- Si admite más de una lectura, es `Ambiguo`.
- Recorre las seis tareas críticas de la persona una por una y contrasta sus criterios de éxito.
- Recorre su escenario clave de extremo a extremo encadenando RF. Si el flujo se interrumpe o se
  sostiene en un RF ambiguo, identifica el paso exacto.
- Declara tu cobertura percibida como porcentaje. Es un autoinforme: no la calcules a partir de la
  rúbrica ni la ajustes después para que coincida con el puntaje computado. Su valor está justamente
  en poder diferir.
- No redactes soluciones ni RF nuevos en esta fase.

En esta fase **no se calcula ningún puntaje**. El agente juzga; el agregador computa. Cada evaluación
entrega su tabla de veredictos, sus necesidades no cubiertas, sus riesgos, el recorrido de su
escenario y su cobertura percibida.

Emite:

`✅ Fase A completada — cuatro evaluaciones independientes`

### Fase B — Agregación mediante Eval-Spec

Aplica `Spec/Eval-Spec.MD` sobre los RF y sobre las cuatro evaluaciones de la fase A. La rúbrica, la
escala de puntaje por persona, las fórmulas de D1 a D6, los pesos y las reglas duras están todas allí:
síguelas al pie de la letra y no las reinterpretes.

Construye primero estas cuatro evidencias:

1. Matriz de las 24 tareas críticas: persona × tarea → RF → veredicto → puntos.
2. Matriz de P1, P2 y P3: problema → RF → comportamiento que lo resuelve → puntos.
3. Inventario de todos los RF: ID → las ocho condiciones de D3 → resultado.
4. Matriz de las cinco tensiones de `Personas/README.md`: tensión → RF que la decide → estado.

Después computa D1 a D6, aplica los pesos y muestra cada operación. Ante la duda se penaliza.

Emite:

`✅ Fase B completada — porcentaje global calculado`

### Fase C — Veredicto

Aplica las cinco condiciones de `Spec/Eval-Spec.MD`, sección «Veredicto», y presenta la tabla de
condición contra umbral. La quinta exige que los ocho controles de la sección 8 devuelvan vacío.

Falla una sola condición y el resultado es `FAILED`. No redondees un valor hacia arriba para atravesar
un umbral.

Emite una de estas líneas:

`✅ Fase C completada — ITERACION #N: PASSED`

o:

`✅ Fase C completada — ITERACION #N: FAILED`

### Fase D — Corrección controlada

Ejecuta esta fase solamente si la iteración fue `FAILED`, no se realizaron todavía tres iteraciones y
la corrección cabe dentro de los archivos editables.

Modifica exclusivamente `Requirements/ReqFunc.MD`.

Prioriza:

1. Tareas críticas sin cobertura.
2. P1, P2 o P3 incompletos.
3. RF ambiguos, no atómicos o mal formados.
4. Trazabilidad incompleta.
5. Tensiones sin decidir.
6. Priorización injustificada.

La escala de D1 dice qué tipo de corrección corresponde: una tarea en **3** pide comportamiento que
falta y se corrige agregándolo; una tarea en **1** pide un enunciado que solo admita una lectura y se
corrige reescribiendo. No confundas una con otra.

Cada cambio debe:

- Trazar a una brecha concreta de la iteración anterior.
- Mantener un solo patrón EARS y una sola respuesta.
- Usar al sistema como sujeto del `DEBE`.
- Declarar comportamiento observable, no interfaz, navegación, tecnología ni mecanismo.
- Incluir criterios de aceptación deterministas que no amplíen el contrato del enunciado.
- Declarar persona, problema y prioridad.
- Mantener actualizadas todas las matrices y resúmenes internos.
- Usar `[ACLARAR: pregunta concreta]` o `[SUPUESTO: enunciado]` cuando falte información.

Al agregar un RF: no renumeres los existentes, usa el siguiente número disponible dentro de su área y
actualiza conteos, distribución de prioridades y matrices.

Al dividir un RF no atómico: conserva el ID original para una de las respuestas, crea un ID nuevo para
la otra, ajusta su trazabilidad con evidencia y no elimines comportamiento en silencio.

Prohibido:

- Modificar personas, agentes, convenciones, `Eval-Spec`, scripts o RNF.
- Suavizar criterios de evaluación.
- Inventar necesidades.
- Añadir RF genéricos para elevar D1.
- Añadir comportamiento que no responda a una brecha identificada.
- Eliminar un RF para ocultar una contradicción.
- Modificar los puntajes manualmente.

Registra el diff conceptual: ID agregado, modificado o dividido; brecha exacta que corrige; persona,
tarea o problema beneficiado; efecto esperado en la siguiente iteración.

Emite:

`✅ Fase D completada — correcciones preparadas para ITERACION #N+1`

Después, relee todos los archivos y comienza una evaluación nueva.

---

## 7. Controles obligatorios

Ejecuta desde la raíz, antes de declarar `PASSED`:

```bash
scripts/verificar.sh --sin-agentes
```

Son nueve controles en tres familias: los cuatro mecánicos de `docs/CONVENCIONES.md`, sección 11;
cuatro estructurales —identificadores duplicados, campos obligatorios de cada RF, matrices que citen
IDs inexistentes y archivos de solo lectura tocados—; y uno de cómputo, C1, que recomputa los
puntajes declarados en `corrida.json`. El script sale con código 0 cuando los nueve pasan y 1 cuando
alguno falla, con el detalle de las líneas culpables.

C1 comprueba que `Puntaje_p`, D1, D2, D3 y el global salgan de sus fórmulas, que los techos duros de
`Eval-Spec` se respeten, que el veredicto declarado sea el que producen las cinco condiciones y que el
porcentaje del README sea el de la última corrida. Hasta ahora esas reglas las aplicabas tú, que eres
además quien quiere aprobar. Puedes ejecutarlo por separado mientras trabajas:

```bash
scripts/verificar-puntaje.sh
```

Si C1 contradice un número tuyo, corrige el número. La fórmula, el techo y el umbral no se tocan.

C1 aparece como `OMITE` mientras no exista ningún `corrida.json`. **Un control omitido no es un
control cumplido**: la condición 5 del veredicto exige los nueve, así que no hay `PASSED` sin el JSON
de la corrida escrito.

`--sin-agentes` retira `Agents/*` de la lista de editables, y por eso acompaña a toda ejecución
posterior al Paso 0: hace cumplir por control lo que el §4 exige por regla. Durante el Paso 0, y solo
entonces, se ejecuta sin el flag.

El skill `verificar-requerimientos` documenta qué detecta cada control, qué significa una falla y
dónde vive su corrección. Consúltalo antes de interpretar un hallazgo.

**Ningún puntaje se declara `PASSED` con un control en rojo**, por alto que sea el porcentaje. Si la
corrección de un hallazgo exige tocar un archivo de solo lectura, repórtala como bloqueada.

Guarda la salida literal del script, con su código de salida, en
`Spec/corridas/‹id›/controles.txt`.

---

## 8. Entregables de la corrida

La salida no cabe en un archivo. `Spec/corridas/_ESQUEMA.MD` explica por qué y fija la estructura;
`Spec/Eval-Spec.MD`, sección «Salida», fija los contenidos. Esto es lo que produces:

```
Spec/
  Eval-Report.MD                        resumen de esta corrida, 1–2 páginas
  HISTORIAL.MD                          una fila más, la de esta corrida
  corridas/‹AAAA-MM-DD›-‹etiqueta›/
    corrida.json                        cabecera y puntajes, para el control C1
    controles.txt                       salida literal de verificar.sh y su código de salida
    bloqueos.MD                         lo que el §10 impidió corregir; omítelo si no hubo
    iteracion-N/
      veredicto-rodrigo.MD
      veredicto-milagros.MD
      veredicto-carmen.MD
      veredicto-anibal.MD
      diagnostico.MD
```

### El resumen

`Spec/Eval-Report.MD` sigue el formato de `Eval-Spec.MD` §Salida → «Resumen». Empieza por la cabecera
de reproducibilidad —los SHA de lo evaluado, de la rúbrica, de las personas y de los agentes— y
sigue con veredicto, dimensiones, puntajes por persona, brechas y acciones. **No pegues aquí la
evidencia**: enlázala.

Los SHA se obtienen del repositorio, no se inventan:

```bash
git log -1 --format=%h -- Requirements/ReqFunc.MD
git log -1 --format=%h -- Spec/Eval-Spec.MD
```

Encabezado:

```markdown
# Reporte de Evaluación de Requerimientos Funcionales
## Sistema de Gestión UCI — Essalud
```

### La evidencia

Cada iteración escribe su propio directorio `iteracion-N/`. Los cuatro veredictos van en archivos
separados, uno por persona, cada uno con:

- Tabla completa ID → veredicto → justificación.
- Tareas y criterios no cubiertos.
- Recorrido del escenario.
- Cobertura percibida declarada.

Y `diagnostico.MD` lleva el resto de las tablas del formato «Evidencia»: veredictos agregados, matriz
de cobertura, cobertura de P1–P3, discrepancias, tensiones sin decidir, requerimientos huérfanos, mal
formados y mal ubicados, y evaluaciones ausentes o inválidas.

**No reescribas `iteracion-1/` al ejecutar la iteración 2.** Cada iteración es un directorio nuevo:
esa separación es lo que permite diffearlas, y un diff entre iteraciones es la única evidencia de que
una corrección cerró la brecha que decía cerrar.

### Los números

`corrida.json` según `Spec/corridas/_ESQUEMA.MD`. Escríbelo antes de ejecutar los controles: C1 lo
lee, y sin él la condición 5 del veredicto no se cumple.

### El historial

Al cerrar la corrida agrega **una** fila a `Spec/HISTORIAL.MD` con los valores de la última
iteración. No edites filas anteriores ni las reordenes.

### Entre iteraciones

En las iteraciones posteriores a la primera, `diagnostico.MD` comienza con:

```markdown
### Cambios respecto a la iteración anterior

| ID | Cambio | Brecha cerrada |
|---|---|---|
```

Y termina con:

```markdown
### Delta
```

Explica qué dimensión cambió, cuánto cambió y qué evidencia produjo el cambio. No atribuyas una mejora
a una corrección que no afecte esa dimensión.

Cierre de `Spec/Eval-Report.MD`:

```markdown
## Resultado final: __ %

- Iteraciones ejecutadas: N
- Veredicto final: PASSED / FAILED
- Promedio final de personas: _/10
- Puntaje global final: _ %
- Brechas abiertas: N
```

El resultado final debe coincidir con la última iteración, con el bloque `resultado` de
`corrida.json` y con la fila de `HISTORIAL.MD`. C1 comprueba las dos primeras coincidencias.

---

## 9. Actualización del README

Cuando termine la última iteración, actualiza exclusivamente el marcador `**__ %**` de la línea final
«Resultado del agente» en `README.md`.

Usa el porcentaje global de la última iteración, incluso si el resultado final es `FAILED`. C1
compara ese número con el que `corrida.json` declara en `resultado.global`: un README que se queda
con el porcentaje de una corrida anterior publica un valor que ya nadie sostiene.

No modifiques ninguna otra parte del README.

Emite:

`✅ Entregables de la corrida escritos y resultado de README.md actualizado`

---

## 10. Condiciones de parada

Detente y solicita autorización antes de:

- Eliminar un RF existente.
- Mover contenido entre `ReqFunc.MD` y `ReqNoFunc.MD`.
- Modificar un archivo de solo lectura.
- Crear un archivo no autorizado.
- Cambiar una persona, tarea crítica o criterio de éxito.
- Cambiar `Eval-Spec`, la rúbrica, las convenciones, el esquema de corrida o los scripts.
- Reescribir el directorio de una corrida anterior o una fila ya escrita de `HISTORIAL.MD`.
- Hacer commit, push, merge o pull request.

Si una corrección necesaria depende de cualquiera de esas acciones, repórtala como bloqueada y
regístrala en `Spec/corridas/‹id›/bloqueos.MD`. No la sustituyas por una solución inventada.

Si la tercera iteración sigue en `FAILED`: conserva los tres directorios `iteracion-N/`, documenta
todas las brechas restantes en el resumen, agrega igual la fila al historial, actualiza el README con
el porcentaje real y detente. Nunca fuerces `PASSED`.

---

## 11. Reporte final en la conversación

Al terminar informa:

- Rama creada y directorio de la corrida.
- Número de iteraciones y resultado de cada una.
- Puntajes individuales finales y promedio.
- D1–D6 finales y porcentaje global.
- `PASSED` o `FAILED`, con la tabla de las cinco condiciones.
- RF agregados, modificados o divididos.
- Archivos creados y modificados.
- Salida de `scripts/verificar.sh`, con el estado de C1.
- Brechas todavía abiertas y bloqueos registrados.
- Fila agregada a `Spec/HISTORIAL.MD`.
- Estado de Git.

No hagas commit ni subas cambios. Termina preguntando si se autoriza crear el commit y el pull
request.
