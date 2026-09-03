# Decisiones

Registro de las decisiones que gobiernan el resto del repositorio. Cada entrada tiene cuatro partes
—**contexto → opciones → decisión → consecuencias**— y ninguna ceremonia más: no hay estado, ni fecha
de revisión, ni decisiones superadas conservadas tachadas. El historial está en `git log`.

**Qué entra acá.** Una decisión se registra cuando cambiar de opinión obliga a reescribir más de un
documento. Lo que se decide dentro de un paso de [R.E.D.A.L.E.](../redale/README.md) —una cifra, una
ruta, una tabla— se registra en ese paso y se rige por su contrato con los vecinos.

**Las consecuencias se escriben en los dos sentidos.** Una decisión que solo enumera lo que gana no
se decidió: se justificó. Lo que cuesta va escrito con el mismo cuidado que lo que rinde.

| # | Decisión | Qué gobierna |
|---|---|---|
| [D-01](#d-01--spec-kit-es-la-autoridad-y-el-backlog-es-su-proyección) | Spec Kit es la autoridad y el backlog es su proyección | Quién manda sobre qué debe hacer el sistema |
| [D-02](#d-02--el-formato-del-backlog-sale-de-la-clase-no-del-enunciado) | El formato del backlog sale de la clase, no del enunciado | La forma de cada ítem |
| [D-03](#d-03--el-mandante-del-gobierno-entra-como-persona-con-agente) | El mandante del gobierno entra como persona con agente | Quién juzga D1 |
| [D-04](#d-04--la-autora-en-la-central-no-es-el-docente-que-dicta-en-el-pueblo) | La autora en la central no es el docente que dicta en el pueblo | El encuadre del problema |
| [D-05](#d-05--el-backlog-tiene-techo-declarado-26-rf--7-rnf) | El backlog tiene techo declarado: ~26 RF + ~7 RNF | El tamaño del entregable |
| [D-06](#d-06--d1-se-reparte-075--4-y-las-deducciones-se-reescalan) | D1 se reparte 0,75 × 4 y las deducciones se reescalan | La aritmética del EVAL |
| [D-07](#d-07--el-40--se-mide-por-semana-curso-publicada-contra-una-línea-base-declarada) | El −40 % se mide por semana-curso publicada contra una línea base declarada | La única cifra dura del caso |

---

## D-01 — Spec Kit es la autoridad, y el backlog es su proyección

**Contexto.** El repositorio hereda del [Caso #3](../../LAB03-SendIt/) un `.specify/` completo y diez
skills `speckit-*`. Allá se decidió instalarlo como harness **inerte**: corría una sola skill
—`/speckit-constitution`— y el backlog conservaba toda la autoridad. El resultado documentado de esa
elección fue que `insumos.md`, el único documento aguas arriba del backlog, congeló sus
identificadores en la ronda 01 y pasó dieciséis rondas contradiciendo al documento que lo citaba.

El profesor nunca pidió Spec Kit: no aparece en el enunciado ni en la clase. Es andamiaje propio, y
por eso mismo la pregunta de qué papel le toca es una decisión y no un dato.

**Opciones.**

| Opción | Qué resuelve | Por qué no |
|---|---|---|
| Harness inerte, como el Caso #3 | Cero fricción; el backlog manda solo | Deja el razonamiento suelto en un `insumos.md` sin disciplina de numeración — el defecto ya observado |
| Sacar Spec Kit del repositorio | Menos ruido | Se pierde la constitución, que `evals/README.md` declara como entrada del agregador para D2 |
| **Spec Kit gobierna** | — | — |

**Decisión.** **`specs/001-remoteschooly/spec.md` es donde se autorizan los requerimientos**, y
`redale/R-requerimientos/backlog.md` es su **proyección** al formato que el profesor exige. La
cadena de autoridad es:

```
constitution.md  →  spec.md  →  backlog.md  →  E · D · A · L
   principios     la autoridad   la proyección    aguas abajo
```

**Regla de dirección: nada sube.** Si el EVAL encuentra un hueco, la corrección se hace en `spec.md`
y se reproyecta al backlog. Corregir solo el backlog es exactamente la deriva del Caso #3.

`insumos.md` cambia de papel: deja de ser razonamiento suelto y pasa a ser **la tabla de
trazabilidad `FR ↔ RF` y `SC ↔ RNF`**. Con el mapeo explícito, renumerar es mecánico.

Quedan vivas `/speckit-constitution`, `/speckit-specify` y `/speckit-clarify` —esta última ahora sí
corre, porque hay un `spec.md`—. `/speckit-plan`, `/speckit-tasks` e `/speckit-implement` producen
código y este lab no produce código; `/speckit-analyze` exige los tres archivos. Quedan fuera **por
decisión declarada, no por olvido**.

**Consecuencias.**

- **El razonamiento tiene por fin un documento con forma.** Los Given/When/Then, los edge cases y los
  criterios medibles viven donde la plantilla los pide, y no comprimidos en un título sin descripción.
- **Un `RF` sin su `FR` es un huérfano detectable**, y un `FR` sin su `RF` es un requerimiento que el
  profesor nunca va a ver. Las dos faltas son ahora verificables con un `grep`.
- **Cuesta un documento más que mantener en sincronía.** Toda corrección pasa a ser doble: spec y
  proyección. Si en alguna ronda se corrige solo el backlog, la trazabilidad miente y el defecto es
  peor que no haber tenido spec, porque hay un documento que dice lo contrario con autoridad.
- **El EVAL sigue puntuando el backlog y nada más.** El spec no se entrega ni se puntúa: es
  infraestructura de autoría. Un lector que espere que el spec sea el entregable se confunde, y esta
  entrada existe para que no lo haga.
- **Se aleja del uso normal de Spec Kit**, que apunta a producir código. Acá el ciclo se corta después
  de `clarify` y eso deja seis skills sin usar en el repositorio.

---

## D-02 — El formato del backlog sale de la clase, no del enunciado

**Contexto.** El enunciado del Caso #3 traía una restricción explícita: *"los requerimientos deben ser
mostrados en formato backlog. No necesitan describirlos, sino colocar un título claro y entendible"*.
**El enunciado del Caso #4 no la repite.** Su sección de entregables dice solo *"Requirements Eval"*.

El silencio admite dos lecturas, y son incompatibles.

**Opciones.**

| Lectura | Qué implica | Por qué no |
|---|---|---|
| El silencio libera el formato | Se puede volver a EARS, o a historias de usuario | La rúbrica sigue pagando *"Requerimientos — 3 ptos"* y quien la aplica es el mismo profesor que dictó el formato en clase |
| Historia de usuario | *Como X quiero Y para Z* | Es una descripción, que es justo lo que el formato prohíbe |
| **El formato lo fija la clase** | — | — |

**Decisión.** Se adopta **`el sistema [verbo en futuro] [capacidad] - <Persona>`**, el formato literal
del [ejemplo de clase](EJEMPLO-CLASE-TOP-DOWN.md), porque el profesor lo dictó en voz en la sesión del
2026-08-25 (`clases/SWA 3.1/`):

> `[15:00]` *"sobre los requerimientos nada más a partir de ahora… **no puede ser una lista, un
> backlog**"* · `[76:52]` *"mapean requerimientos, **es un backlog**, por si acaso, un backlog"*

De la misma sesión sale el criterio de los no funcionales, que `evals/README.md` cobra en D3:

> `[11:49]` *"los no funcionales son todas **las limitaciones técnicas del sistema**: el sistema
> soportará máximo un megabyte de archivo de texto"* — y la regla que se destila: no *"el sistema
> imprimirá archivos"* sino *"el sistema imprimirá **PDF de máximo 5 MB**"*.

**Consecuencias.**

- **La fuente del formato queda citada y fechada**, así que la elección es auditable y no un hábito
  arrastrado de casos anteriores.
- **Un RNF sin número no es un RNF para este profesor.** Eso convierte «cada no funcional lleva medida
  o no entra» en una regla operativa y no en una intención.
- **Se asume un riesgo:** si el silencio del enunciado del #4 era deliberado y el profesor esperaba
  otro formato, este caso lo va a ignorar. Se acepta porque el costo del error es bajo —un backlog de
  títulos se lee igual de bien— y el de acertar es alto.
- **El repositorio arrastra un documento más:** [`EJEMPLO-CLASE-TOP-DOWN.md`](EJEMPLO-CLASE-TOP-DOWN.md),
  traído del Caso #3 y readaptado, porque sin él la decisión no tiene dónde apoyarse.

---

## D-03 — El mandante del gobierno entra como persona, con agente

**Contexto.** El enunciado nombra tres posiciones sin darles nombre —el alumno, el profesor que
enseña, el profesor que genera material con IA— y una cuarta que aparece dos veces sin figura: **"el
gobierno de Perú"**, que encarga el programa, y **"una central de Lima"**, de donde salen los
materiales. La segunda exigencia del caso —bajar el gasto de tokens **al menos 40 %**— es del
gobierno, no de ninguna de las tres posiciones nombradas.

Ahí está el problema: **quien causa el gasto no es quien lo sufre.** La autora quema tokens; la
factura le llega a otro. Si ese otro no está en el modelo, la única cifra dura del caso queda sin
dueño y D3 la mide contra nadie.

**Opciones.**

| Opción | Qué gana | Qué cuesta |
|---|---|---|
| Restricción del caso, no persona | D1 queda en 1 pt × 3, más simple | El −40 % no tiene quién lo reclame; se vuelve un número flotando en un RNF |
| Persona sin voto en D1 | Entra el ángulo sin abrir un cuarto frente de deducciones | Una persona que no puede reclamar no es una persona, es una nota al pie |
| **Cuarta persona con agente** | — | — |

**Decisión.** Entra **`personas/Aurelio.MD`**, coordinador del programa en la central, que responde
ante el gobierno por el presupuesto y por la cobertura de las regiones. Tiene archivo, agente propio
y **voto en D1**. Ver [`D-06`](#d-06--d1-se-reparte-075--4-y-las-deducciones-se-reescalan) para la
aritmética que esto obliga.

**Consecuencias.**

- **El −40 % adquiere un dueño que puede reclamar.** Un backlog que declara la cifra pero no da a
  nadie manera de verificarla ahora falla D1 y no solo D3.
- **Aparece la tensión que faltaba:** cobertura de la región más lejana ↔ presupuesto finito. Es la
  que obliga al backlog a decidir qué pasa cuando llegar a todos cuesta más de lo que hay.
- **Cuesta una cuarta superficie de deducción en D1.** Cuatro veredictos en lugar de tres, y el gate
  sigue en 8. Es la parte cara de la decisión y se acepta a sabiendas.
- **Cuesta la aritmética de la rúbrica**, que hay que enmendar antes de puntuar nada.

---

## D-04 — La autora en la central no es el docente que dicta en el pueblo

**Contexto.** El enunciado dice que *"los materiales vienen desde una central de Lima"* y, aparte,
que *"los profesores que generan los materiales de curso usan demasiado la IA"*. No dice si los que
generan son los mismos que dictan. `personas/README.md` lo deja anotado como decisión del caso y no
como dato.

**Opciones.**

| Opción | Qué gana | Por qué no |
|---|---|---|
| Un solo docente-autor | Tres personas y D1 en 1 pt exacto; backlog más chico | El enunciado dice que el material **viene** de la central: un docente del pueblo generando desde el pueblo contradice la premisa del enlace limitado, que es todo el caso |
| **Personas distintas** | — | — |

**Decisión.** **Marisol** produce en la central de Lima; **Rómulo** dicta en el pueblo. Son personas
distintas, con archivos y agentes distintos.

**Consecuencias.**

- **Sostiene la premisa del enunciado.** El material atraviesa el enlace porque se produce de un lado
  y se consume del otro. Fusionarlos borraría la distancia, que es el problema.
- **Da la tensión que D4 exige decidida:** Marisol corrige el material tarde, Rómulo ya tiene la
  semana congelada y en camino. Alguien tiene que perder, y el backlog tiene que decir quién.
- **Cuesta una persona más y un flujo más que cubrir de extremo a extremo**, incluido su «cuando sale
  mal». Junto con [`D-03`](#d-03--el-mandante-del-gobierno-entra-como-persona-con-agente) es lo que
  fuerza a subir el techo del backlog en [`D-05`](#d-05--el-backlog-tiene-techo-declarado-26-rf--7-rnf).

---

## D-05 — El backlog tiene techo declarado: ~26 RF + ~7 RNF

**Contexto.** El 2026-09-02 el profesor abrió tres issues sobre el Caso #1
(`LuisMUtec/SWA-LAB01-UCI-Essalud` [#15](https://github.com/LuisMUtec/SWA-LAB01-UCI-Essalud/issues/15),
[#16](https://github.com/LuisMUtec/SWA-LAB01-UCI-Essalud/issues/16),
[#17](https://github.com/LuisMUtec/SWA-LAB01-UCI-Essalud/issues/17)) que dicen lo mismo tres veces:

> *"194 requerimientos es inmanejable para cualquier proyecto. Y el sistema no debería ser tan
> complejo"* · *"los requerimientos no funcionales están demasiado genéricos y **parecen demasiado
> ajustados para que sean evaluados/leídos por una IA más que una persona**"* · *"lo interesante es
> que a pesar de tener 194 requerimientos no se cumplan los EVAL y los usuarios no tengan sus
> necesidades cubiertas"*

El Caso #1 tenía 3 412 líneas de requerimientos funcionales. El Caso #3 llegó a **236 ítems** —más
todavía—, pero se entregó el 2026-08-28 y la retroalimentación llegó cinco días después. **Este es el
primer caso donde se puede aplicar.**

**Opciones.**

| Opción | Por qué no |
|---|---|
| Sin techo, medir solo por cobertura | Es fiel al principio, pero sin freno declarado es exactamente como el #1 llegó a 194 y el #3 a 236: nadie decide agregar de más, se llega de a un ítem por vez |
| ~20 RF + ~6 RNF | Deja poco margen con cuatro flujos que cubrir de extremo a extremo, cada uno con su «cuando sale mal» |
| **~26 RF + ~7 RNF** | — |

**Decisión.** Techo de **~26 funcionales y ~7 no funcionales**. El backlog se mide por **cobertura de
los flujos de las personas, no por volumen**, y el techo existe para que la cobertura sea lo que
decida y no la inercia. Un título que no cierra un paso del flujo de alguien no entra.

**Consecuencias.**

- **Es un orden de magnitud menos que el Caso #1**, y responde a las tres issues con una regla
  operativa en lugar de una intención.
- **Obliga a que los títulos sirvan a más de un flujo**, que es lo que un backlog bien escrito hace de
  todos modos.
- **El techo puede quedar corto.** Si en alguna ronda un agente encuentra un paso descubierto y la
  única forma de cubrirlo es pasarse, **se pasa y se anota acá**: el techo es un freno declarado, no
  un límite que valga más que la cobertura. Lo que no se puede es pasarse en silencio.
- **Se pierde granularidad frente al Caso #3.** Habrá comportamientos que allá eran tres títulos y acá
  son uno. Eso empuja detalle hacia `spec.md`, que es donde [`D-01`](#d-01--spec-kit-es-la-autoridad-y-el-backlog-es-su-proyección)
  quiere que viva.

---

## D-06 — D1 se reparte 0,75 × 4 y las deducciones se reescalan

**Contexto.** `evals/README.md` fija D1 en 3 puntos, *"1 pt por persona, solo deducciones"*, con una
escala de veredictos calibrada para esa unidad: `Funciona con reservas` resta 0,5 y `No funciona`
resta 1. La rúbrica se escribió suponiendo tres personas.
[`D-03`](#d-03--el-mandante-del-gobierno-entra-como-persona-con-agente) mete una cuarta.

Dejar la escala como está tiene una consecuencia aritmética que no es cosmética: con cuatro personas
a 0,75, un solo `No funciona` de −1 **costaría más de lo que la persona entera vale**. D1 dejaría de
medir la satisfacción de las personas y pasaría a medir cuántas objetaron.

**Opciones.**

| Opción | Por qué no |
|---|---|
| Dejar 1 pt × 3 y que Aurelio no vote | Contradice [`D-03`](#d-03--el-mandante-del-gobierno-entra-como-persona-con-agente): una persona sin voto no reclama |
| Repartir 0,75 × 4 sin tocar las deducciones | Un veredicto podría restar más de lo que su emisor vale; D1 deja de medir lo que dice medir |
| **Repartir y reescalar en proporción** | — |

**Decisión.** D1 sigue valiendo **3**, repartido **0,75 por persona**, y las deducciones se reescalan
por el mismo factor:

| Veredicto | Antes | Ahora |
|---|---|---|
| `Funciona` | 0 | 0 |
| `Funciona con reservas` | −0,5 | **−0,375** |
| `No funciona` | −1 | **−0,75** |

`evals/README.md` permite enmendar una dimensión que **no mide lo que dice medir**, con dos
condiciones que acá se cumplen: la enmienda se escribe **antes de conocer el puntaje que produciría**
—no se ha corrido ninguna ronda— y se registra en esta bitácora. **No se toca nada más de la rúbrica,
y nunca para alcanzar el gate.**

**Consecuencias.**

- **La proporción se conserva:** un `No funciona` sigue costando la persona entera, y uno con reservas
  la mitad. La dimensión mide lo mismo que antes con una persona más.
- **El gate se vuelve más difícil, no más fácil.** Cuatro lectores independientes buscando huecos
  encuentran más que tres, y el umbral sigue en 8. La enmienda no compra puntos.
- **Los puntajes de D1 dejan de ser enteros o medios.** Los informes van a mostrar cifras como 2,625,
  que se leen peor. Es el precio de que la aritmética sea honesta.
- **Cuesta tocar `evals/README.md`**, el documento que en principio no se toca. Queda como precedente
  incómodo: la próxima enmienda tiene que justificarse contra esta.

---

## D-07 — El −40 % se mide por semana-curso publicada, contra una línea base declarada

**Contexto.** *"Reducir el uso de gasto de tokens en al menos un 40 %"* es la única cifra dura del
caso, y el enunciado no dice **40 % de qué**. Sin unidad y sin línea base, el número no es
verificable: cualquier sistema puede declararlo cumplido y ninguno puede ser acusado de incumplirlo.
D3 lo cobra como *exigencia sin medida*.

Hay además un conflicto de forma. El agregador exige títulos **sin mecanismo** —regla que el profesor
dicta también para el diagrama, `[113:48]` *"acá no pongo Java, acá no pongo Amazon, Azure, acá no
pongo Postgres"*— pero el ahorro de tokens lo producen mecanismos.

**Opciones.**

| Formulación | Por qué no |
|---|---|
| *"el sistema mostrará a la autora el costo de una generación **antes** de ejecutarla"* | El costo no se conoce antes: lo que se paga es la salida, y todavía no está escrita. Ningún sistema puede cumplirlo, así que **no es negable** |
| *"el sistema reutilizará un material ya generado **equivalente**"* | «Equivalente» no admite una sola lectura —¿equivalente en qué?— y quien decida la equivalencia es el mecanismo que el título esconde. En un caso educativo, además, dar por buena la reutilización sin decir bajo qué criterio es una decisión pedagógica que el backlog no puede tomar de contrabando |
| *"el gasto de tokens bajará 40 %"*, a secas | Es el resultado sin nada que lo produzca: una cifra sin productor |
| **Unidad declarada + comportamientos observables** | — |

**Decisión.** **La unidad es la semana-curso publicada**, y la línea base es el consumo de tokens por
semana-curso del periodo inmediatamente anterior a la medición, declarado como `[ASSUMPTION: ...]` con
su justificación a la vista. Se elige esa unidad porque es la única que el propio enunciado ya trata
como átomo del sistema —*"los materiales para la semana"*— y porque normaliza: bajar el gasto total
cerrando cursos no cuenta como ahorro.

El resultado agregado vive como `SC-nnn` en el spec y como **RNF con medida** en el backlog. Lo que lo
produce se enuncia como **comportamiento observable, negable y sin tecnología**:

- el sistema impedirá publicar material que supere el techo de tokens asignado al curso en el periodo
- el sistema informará a la autora cuántos tokens lleva consumidos del techo de su curso en el periodo
  — consumo **ya ocurrido**, que sí se conoce
- el sistema exigirá a la autora señalar qué parte del material cambia antes de generar una nueva
  versión — contra el *"regenera diez veces por cambiar una palabra"*, que es la causa que el
  enunciado señala
- el sistema distribuirá a todas las regiones la versión publicada de la semana sin volver a generarla
- el sistema rendirá el gasto de tokens del periodo contra la línea base declarada

**Consecuencias.**

- **El 40 % se vuelve verificable**, que es lo que D3 pide. Hay un numerador, un denominador y un
  punto de comparación.
- **Los mecanismos quedan libres para el paso `D`.** El backlog dice qué se observa; el diseño dice
  cómo se consigue. La regla de dirección se respeta.
- **La línea base es un supuesto, no un dato.** Si el profesor la fija de otro modo, el RNF cambia de
  número aunque no de forma. Va marcado para que se vea que es una elección nuestra.
- **Se acepta un límite:** ninguno de los cinco comportamientos garantiza por sí solo el 40 %. La
  cifra es una meta del sistema, no la suma aritmética de sus títulos, y el backlog no puede fingir lo
  contrario.

---

## Decisiones pendientes

| # | La pregunta que la destrabaría | Dónde se decidirá |
|---|---|---|
| `P-01` | ¿Qué pasa cuando una región no recibió la semana y ya es lunes? ¿Se dicta con la anterior, o se reprograma? | `spec.md`, edge cases de Rómulo |
| `P-02` | ¿Cuánto material retiene el nodo del pueblo — solo la semana vigente, o un histórico? | Paso `A` |
| `P-03` | ¿El techo de tokens es por curso, por autora, o por ambos? | `spec.md`, al cerrar `D-07` |
