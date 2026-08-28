# Decisiones

Registro de las decisiones que gobiernan el resto del repositorio. Cada entrada tiene cuatro
partes —**contexto → opciones → decisión → consecuencias**— y ninguna ceremonia más: no hay estado,
ni fecha de revisión, ni decisiones superadas conservadas tachadas. El historial está en `git log`.

**Qué entra acá.** Una decisión se registra cuando cambiar de opinión obliga a reescribir más de un
documento. Lo que se decide dentro de un paso de [R.E.D.A.L.E.](../redale/README.md) —una cifra, un
endpoint, una tabla— se registra en ese paso y se rige por su contrato con los vecinos.

**Las consecuencias se escriben en los dos sentidos.** Una decisión que solo enumera lo que gana no
se decidió: se justificó. Lo que cuesta va escrito con el mismo cuidado que lo que rinde.

| # | Decisión | Qué gobierna |
|---|---|---|
| [D-01](#d-01--el-usuario-modelo-es-rosa) | El usuario modelo es Rosa | Contra quién se mide si el backlog resolvió algo |
| [D-02](#d-02--tres-personas-no-más) | Tres personas, no más | El reparto de D1 y quién tiene voz en el EVAL |
| [D-03](#d-03--se-incluye-el-segundo-paso-e-escalar-acotado) | Se incluye el segundo paso `E`, acotado | Cuántos entregables tiene R.E.D.A.L.E. en este caso |
| [D-04](#d-04--la-rúbrica-del-eval-se-recorta-respecto-del-caso-2) | La rúbrica se recorta respecto del Caso #2 | Qué mide el EVAL y qué puntajes son comparables |
| [D-05](#d-05--las-iteraciones-del-diseño-son-iteraciones-del-diagrama-de-componentes) | «Las iteraciones del diseño» son del diagrama | Qué se entrega como iteración y en qué orden se construye |
| [D-06](#d-06--el-backlog-adopta-el-formato-literal-del-profesor) | El backlog adopta el formato del profesor | La forma exacta de cada ítem del único artefacto puntuado |
| [D-07](#d-07--sendit-opera-el-modelo-western-union) | SendIt opera el modelo Western Union | El canal de origen, quién es la tercera persona y la mitad de las reglas de seguridad |
| [D-08](#d-08--spec-kit-se-instala-como-harness-y-no-produce-specs) | Spec Kit se instala como harness y no produce specs | Qué herramienta sostiene la disciplina y quién conserva la autoridad sobre los requerimientos |

---

## D-01 — El usuario modelo es Rosa

**Contexto.** El [enunciado](LAB-03-ARQ-2026.2.md) pide, como hint, *identificar correctamente quién
es el usuario modelo* — en singular. Una remesa tiene al menos cinco actores con un problema propio
y legítimo, y el enunciado no nombra a ninguno.

**Opciones.**

| Candidato | Su problema | Por qué no es el usuario modelo |
|---|---|---|
| **Remitente** (Rosa) | Comprar una llegada: tantos soles, tal día | — |
| **Destinatario** (Elena) | Cobrar sin viajar en vano y sin que le falte | No elige el servicio: recibe por donde el remitente mandó |
| **Operario de ventanilla** (Kevin) | Cerrar la operación sin equivocarse, con cola esperando y con el efectivo de su patrón | Atiende el mostrador de un tercero afiliado. No elige SendIt: SendIt llegó a su negocio |
| **Tesorería** | Prefinanciar el corredor, cerrar la posición de cambio | Su problema es de la empresa, no del envío |
| **Oficial de cumplimiento** | Detener lo que hay que detener, antes y con evidencia | Trabaja dentro de la empresa. Su día se resuelve sin que exista un cliente (ver D-07) |

**Decisión.** **Rosa.** Es quien decide usar SendIt o abandonarlo, quien paga, y la única de las
cinco que elige libremente.

**Consecuencias.**

- Un backlog que resuelve el día de Kevin y no el de Rosa **describe una red de agentes muy bien
  controlada y sin clientes.** Es la falla que esta decisión existe para prevenir, y el enunciado
  la invita: nombra la seguridad y no nombra al cliente.
- **En sentido inverso, y es igual de importante: elegirla no la vuelve la única.** Es el usuario
  modelo, no el único usuario, y la razón es concreta — **el problema de Rosa no se resuelve dentro
  de la pantalla de Rosa.** La promesa que ella necesita la cumple o la rompe Elena en la bodega de
  Huanta, y la sostiene o la pierde Kevin en el mostrador. Un diseño que solo mira su lado declara el envío
  terminado cuando el dinero salió, que es exactamente el momento en que nada se resolvió.
- **El usuario modelo no compra peso en la rúbrica.** D1 reparte un punto por persona, igual para
  las tres ([`evals/README.md`](../evals/README.md)). Ser el usuario modelo decide contra quién se
  mide el sentido del producto, no cuánto vale su veredicto.

---

## D-02 — Tres personas, no más

**Contexto.** D1 vale 3 puntos y los reparte a razón de uno por persona. El número de personas no es
una decisión narrativa: es el denominador de la única dimensión que las personas puntúan.

**Opciones.** Tres personas, o cuatro y más. Agregar una cuarta obliga a recortar la rúbrica —
repartir los mismos 3 puntos entre más lecturas diluye cada veredicto, y subir D1 a 4 puntos obliga
a quitárselos a D2, D3 o D4, que son las que miden el ajuste al problema y las dos exigencias que el
enunciado nombró.

**Decisión.** **Tres: [Rosa](../personas/Rosa.MD), [Elena](../personas/Elena.MD) y
[Kevin](../personas/Operario.MD).** Cada una existe porque el sistema le falla de una forma que a las
otras dos no.

| Persona | Por qué sí | El modo de falla que solo ella ve |
|---|---|---|
| Rosa | Es el usuario modelo (D-01) | La promesa de monto y fecha que nadie más está en posición de exigir |
| Elena | El corredor termina en su mano, no en el mostrador donde Rosa pagó | El envío que el sistema da por cerrado antes de que ella cuente los billetes |
| Kevin | La **seguridad** del enunciado necesita un cuerpo, y el cuerpo correcto es por donde se rompe, no quien la vigila (D-07) | La operación cortada a la mitad: la única que rompe la **consistencia** con dinero ya en la mano |

Los tres actores descartados están argumentados uno por uno en
[`personas/README.md`](../personas/README.md). En resumen: **tesorería** tiene un problema de la
empresa y no del envío, y su día se resuelve sin tocar el de Rosa; **el oficial de cumplimiento**
trabaja dentro de la empresa y su día se resuelve sin que exista un cliente, de modo que su función
vive en las reglas y no en una voz (D-07); **soporte al cliente** existe hoy porque el sistema no informa, y modelarlo como persona vuelve requisito al
síntoma —cada vez que Rosa «tiene que llamar», eso es un defecto del backlog, no un caso de uso.

**Consecuencias.**

- La rúbrica queda estable y comparable ronda a ronda: 3 = 1 + 1 + 1.
- Los tres actores excluidos **siguen apareciendo**, pero como frontera del sistema o como decisión
  aguas abajo, no como voz que puntúa. La liquidez del corredor se decide en
  [`D`](../redale/D-disenar-servicio/README.md); el cumplimiento vive en `BR-04`, `BR-06` y `BR-15`
  de [`business-rules.md`](../business-rules.md), y su conflicto sin resolver sobrevive en T1 y T2.
- **La consistencia de datos se queda sin persona propia**, y es deliberado: es la costura entre las
  tres y ninguna la ve entera. Por eso la puntúa D3, aparte de D1.
- Si aparece una necesidad que ninguna de las tres documenta, **se agrega primero a la persona** y
  recién después al backlog. Un agente no inventa capacidades: juzga contra su archivo.

---

## D-03 — Se incluye el segundo paso `E` (Escalar), acotado

**Contexto.** Hay una contradicción entre las dos fuentes, y conviene decirla completa en vez de
elegir la que conviene. El material del curso lista el sexto paso como
*«E - scalar ( esto no lo usaremos aun )»*. El [enunciado](LAB-03-ARQ-2026.2.md) pide **todos** los
entregables del framework R.E.D.A.L.E. Y los dos ejemplos completos del propio material —X (former
Twitter) y Paper.ly— **sí recorren el paso 6**, cada uno con su lámina.

**Opciones.**

| Opción | A favor | En contra |
|---|---|---|
| Omitirlo, citando el material | Es lo que el PDF dice literalmente | Falta un entregable que el enunciado pidió literalmente, y los ejemplos del PDF lo desmienten |
| Incluirlo completo | Cierra el enunciado sin discusión | Escala un sistema cuyas cifras no existen: el enunciado no da ni un número |
| **Incluirlo acotado** | Cierra el enunciado y no promete precisión que no hay | Puede quedar fuera de alcance |

**Decisión.** Se incluye, **acotado**, y con la forma que usa el material: **por tramos de carga**
—`< 1 k`, `1 k–10 k`, `100 k`, `500 k`, `1 M` usuarios—, diciendo en cada tramo qué cambia y dónde
aparece el cuello de botella. Vive en [`redale/E-escalar/`](../redale/E-escalar/README.md).

**Consecuencias.**

- **Cuesta poco y cierra el literal del enunciado.** Si el profesor lo considera fuera de alcance,
  **sobra un archivo y no falta ninguno** — que es el lado correcto del error cuando la fuente se
  contradice consigo misma.
- Hereda los supuestos del primer `E`: sus tramos se apoyan en las entradas de
  [`E-estimar`](../redale/E-estimar/README.md), de modo que un supuesto que se retira allá invalida
  los tramos de acá. Queda escrito en el contrato del paso.
- No se puntúa. Como el resto de `E`, `D`, `A` y `L`, es entregable exigido y no puntaje (D-04).

---

## D-04 — La rúbrica del EVAL se recorta respecto del Caso #2

**Contexto.** La rúbrica llega heredada del
[Caso #2](https://github.com/LuisMUtec/SWA-LAB02-Lease), donde el artefacto puntuado era una
especificación completa y **D3 medía «criterios de aceptación demostrables»**. Acá el artefacto
puntuado es un backlog de **solo títulos**: el enunciado prohíbe describirlos. La dimensión heredada
mediría algo que el enunciado prohíbe escribir.

**Opciones.**

| Opción | Por qué no / por qué sí |
|---|---|
| Conservar D3 tal cual | Puntúa la ausencia de un artefacto que el enunciado prohibió. Todo backlog sacaría 0 |
| Repartir sus 2 puntos entre D1, D2 y D4 | Deja **seguridad y consistencia** sin dimensión propia — las dos únicas cosas que el enunciado nombra por su nombre |
| **Reemplazarla** | La rúbrica sigue valiendo 10 y pasa a medir lo que este enunciado dijo que importa |

**Decisión.** D3 pasa a ser **cobertura de seguridad y consistencia**, 2 puntos, uno por cada una.
Un punto se gana cuando al menos un ítem enuncia la garantía **con una medida o un invariante** que
alguien puede declarar cumplido o incumplido, y el camino de falla está cubierto; medio punto si es
comportamiento sin medida o solo camino feliz; cero si es adjetivo —*«el sistema debe ser seguro»*—
o ausencia. D1, D2 y D4 conservan su peso y su redacción.

**Consecuencias.**

- **El EVAL puntúa lo que el enunciado dijo que importa.** Las dos exigencias nombradas dejan de
  depender de que alguien se acuerde de mirarlas: tienen dimensión, peso y umbral.
- **La medida no siempre es un número.** Para la consistencia la forma correcta es casi siempre un
  invariante —*ninguna operación figura retenida y pagada a la vez*—, que es más fuerte que un
  porcentaje porque no depende del conjunto de casos que alguien haya armado.
- **El hint sobre «diseñar bien el mecanismo de seguridad» no autoriza a meter el mecanismo en el
  backlog.** El mecanismo se decide en [`D`](../redale/D-disenar-servicio/README.md). Lo que el
  backlog dice es qué tiene que garantizar ese mecanismo —quién no puede leer qué, quién no puede
  hacer qué sin dejar rastro—, y eso es lo que D3 puntúa.
- **Los puntajes de los dos casos dejan de ser comparables.** Un 8,25 del Caso #2 y un 8,25 de este
  no miden lo mismo. Se declara acá para que nadie los ponga en la misma tabla.

---

## D-05 — «Las iteraciones del diseño» son iteraciones del diagrama de componentes

**Contexto.** El enunciado exige *mostrar claramente las iteraciones de su diseño* y no define qué
cuenta como iteración. Admite al menos tres lecturas, y la elegida decide el entregable entero.

**Opciones.**

| Lectura | Qué se entregaría | Por qué no |
|---|---|---|
| Versiones del documento | Un historial de cambios | Ya está en `git log`, y no muestra ningún diseño |
| Rondas del EVAL | La tabla de puntajes | Es otra cosa, y también existe — pero itera el backlog, no el diseño |
| **Refinamiento del diagrama** | El mismo diagrama, dibujado de nuevo más abierto | — |

**Decisión.** La tercera, y no por preferencia: es la que el profesor mostró en clase. El
[ejemplo](EJEMPLO-CLASE-TOP-DOWN.md) es **el mismo diagrama dibujado tres veces, cada vez más
abierto** —#1 los actores contra una sola caja; #2 esa caja abierta en servicios, bases y APIs
externas; #3 el resto del backlog—, con el backlog escrito en el mismo lienzo y los ítems ya
cubiertos terminando en **`DONE`**. *Top down design.*

**Consecuencias.**

- **No se dibuja el diagrama final y después se inventan las iteraciones previas.** Esta es la
  consecuencia operativa y la que hay que sostener aunque incomode: **la iteración 1 es un
  cuadrado**, y lo que fuerza la 2 es un ítem del backlog que el cuadrado no explica. Un diagrama
  desarmado hacia atrás se nota, porque cada paso resulta explicado por el siguiente en vez de
  forzado por el backlog.
- **El backlog tiene que existir antes que el diagrama**, y bien: el `DONE` es el mecanismo de
  trazabilidad completo. Una iteración del diagrama existe porque hay un ítem sin `DONE`; el
  diagrama no crece por gusto, crece hasta que el backlog está cubierto. Encadena con la regla de
  dirección del EVAL —*los requerimientos bajan, nunca suben*— sin necesitar nada más.
- **Conviven dos clases de iteración y hay que distinguirlas.** La del diseño y la del EVAL se
  registran en la misma bitácora ([`redale/ITERACIONES.md`](../redale/ITERACIONES.md)) y una fuerza
  a la otra: corregir `R` invalida lo que `E`, `D`, `A` y `L` afirmaban. La distinción está en el
  [README](../README.md#las-dos-clases-de-iteración).

---

## D-06 — El backlog adopta el formato literal del profesor

**Contexto.** El enunciado solo dice **título claro y entendible**, sin descripción. Eso deja la
forma del ítem abierta, y el ejemplo de clase la muestra resuelta.

**Opciones.**

| Forma | De dónde viene | Por qué no |
|---|---|---|
| `EARS` + auxiliar DEBE | Convención heredada del Caso #1 | Sus patrones llevan condición y disparador —`CUANDO…`, `SI…ENTONCES`—, y un backlog sin descripción no tiene dónde ponerlos |
| Historia de usuario | Uso corriente | *Como X quiero Y para Z* es una descripción, que es justamente lo que el enunciado prohíbe |
| **La forma del profesor** | [Ejemplo de clase](EJEMPLO-CLASE-TOP-DOWN.md) | — |

**Decisión.** **`el sistema [verbo en futuro] [capacidad]`**, con **` - <Persona>`** anexado cuando
el ítem pertenece a alguien concreto —tal como *«el sistema me permitira ver mis deudores y montos
adeudados **- Leaser**»*.

**Consecuencias.**

- **Es compatible con la restricción del enunciado** y le agrega algo que el enunciado no pide pero
  el ejemplo sí hace: **el ítem nombra a su dueño.** Eso da la trazabilidad que D4 exige —ningún
  huérfano— sin agregar una sola línea de descripción.
- **Se abandona EARS**, que era la convención heredada del Caso #1. No se pierde: lo que EARS
  garantizaba —un patrón, una respuesta, el sistema como sujeto— sobrevive en las reglas de
  redacción del EVAL: título atómico, verificable, sin mecanismo, sin texto visible.
- El sufijo de persona **no reemplaza al juicio del agente.** Un ítem etiquetado ` - Rosa` no está
  cubriendo a Rosa por llevar su nombre; lo decide su agente contra las tres pruebas de cobertura.

---

## D-07 — SendIt opera el modelo Western Union

**Contexto.** El enunciado no dice cómo se origina un envío. El andamiaje inicial supuso que Rosa
paga desde una aplicación y que el efectivo se cobra en una red pagadora de terceros. **El profesor
indicó que el modelo tiene que ser tipo Western Union**, que es otra cosa: red de agentes con
efectivo en las **dos** puntas, sin cuenta bancaria obligatoria de ninguno de los dos lados, y un
código que el remitente transmite por su cuenta.

**Opciones.**

| Opción | A favor | En contra |
|---|---|---|
| Originación por aplicación | Es el modelo dominante hoy y da a Rosa un canal propio | No es lo que el profesor pidió, y deja sin existir a la persona del mostrador en el origen |
| **Ventanilla en las dos puntas** | Es lo indicado, y hace concreta la exigencia de seguridad | Rosa pierde el canal digital para originar; hay que reescribir su flujo |
| Híbrido, ventanilla y aplicación | Más fiel al Western Union real, que tiene los dos | Agrega una cuarta voz o diluye D1, que reparte un punto por persona (D-02) |

**Decisión.** **Ventanilla en las dos puntas.** Rosa se identifica y entrega efectivo en el
mostrador de un agente y sale con un código; Elena cobra efectivo contra ese código y su documento.
El teléfono de Rosa sirve para consultar el estado y para pasarle el código a Elena, no para enviar.

**Consecuencias.**

- **Aparece el mostrador, y con él la tercera persona.** Existe alguien que identifica, cobra y
  paga: [Kevin](../personas/Operario.MD). Ocupa el tercer lugar que D-02 le había dado al oficial de
  cumplimiento, y esa parte de D-02 queda superada por esta decisión.
- **Cambia dónde vive la seguridad del enunciado, no cuánto pesa.** El oficial de cumplimiento la
  vigilaba; el operario **es por donde se rompe**. Está solo, con efectivo, y puede crear giros y
  pagarlos. Un mecanismo que no lo contemple protege la puerta equivocada, y por eso las reglas que
  lo acotan —segunda autorización sobre el umbral, mínimo privilegio, traza inalterable— son las que
  más trabajo hacen en [`business-rules.md`](../business-rules.md).
- **El cumplimiento no desaparece: deja de ser una persona.** Tamizaje, retención y reporte siguen
  siendo obligación del negocio y están en las reglas `BR-04`, `BR-06` y `BR-15`. Lo que se pierde
  es su voz en D1, y hay que decirlo porque cuesta: **nadie deduce ya desde adentro de la empresa.**
  Las tensiones T1 y T2 conservan el conflicto —la retención que nadie puede explicar— pero ahora la
  sufre quien está en el mostrador, no quien la ordenó.
- **Rosa pierde el canal digital de origen y gana un código.** Su flujo pasa de cuatro pasos a siete,
  y aparece un objeto nuevo que el modelo anterior no tenía: el código que **solo ella** puede
  transmitir. De ahí sale una prohibición que antes no existía —que SendIt no se lo dé a Elena— y sin
  la cual la cancelación no sería ejecutable.
- **El agente pagador deja de ser un tercero al que el diseño no puede mandarle.** En el modelo
  anterior era la frontera de sistemas que producía el peor defecto de consistencia; ahora el
  mostrador es parte de la red y el diseño sí manda sobre él. El defecto no desaparece —se muda al
  corte de la operación a la mitad, que es el caso malo de Kevin.

---

## D-08 — Spec Kit se instala como harness y no produce specs

**Contexto.** El [Caso #2](https://github.com/LuisMUtec/SWA-LAB02-Lease) corrió sobre
[Spec Kit](https://github.com/github/spec-kit): plantillas en `.specify/`, skills `/speckit-*`, y un
`specs/<n>/spec.md` como artefacto con autoridad. Este caso heredó de ahí la rúbrica, la regla de
asimetría y la plantilla de personas, pero llegó **sin el harness**. Traerlo choca de frente con una
restricción del [enunciado](LAB-03-ARQ-2026.2.md): los requerimientos van en **formato backlog, con
un título claro y entendible y sin descripción** (D-06). Un `spec.md` es exactamente lo contrario.

**Opciones.**

| Opción | A favor | En contra |
|---|---|---|
| No instalarlo | Cero ambigüedad sobre quién manda, y cero archivos que no se usan | Se pierde la altitud de gobierno: la regla de dirección seguiría viviendo solo en el README del EVAL, sin documento que la haga vinculante para los seis pasos |
| Instalarlo y migrar `R` a `specs/001-.../spec.md` | Los dos casos quedan idénticos y comparables archivo por archivo, y las diez skills funcionan | Viola la restricción del enunciado y deja al EVAL puntuando un artefacto que el curso no pidió |
| **Instalarlo y dejar el backlog como autoridad** | Se gana la constitución y la estructura compartida sin mover el artefacto puntuado | Nueve de las diez skills quedan instaladas y muertas |

**Decisión.** Se instala el harness completo —misma estructura que el Caso #2— y **el backlog
conserva la autoridad**.

**Corre una sola skill: `/speckit-constitution`.** Conviene decirlo con el número, porque la
expectativa razonable es la contraria. `/speckit-clarify` exige un `specs/<n>/spec.md`,
`/speckit-checklist` exige un `plan.md` y `/speckit-analyze` exige los tres archivos; sin ellos
abortan contra `.specify/scripts/bash/check-prerequisites.sh` antes de leer nada. Este caso no
produce ninguno de los tres, así que las nueve restantes quedan **inertes por decisión declarada**,
no por olvido.

La instalación se hizo con `specify init --here --integration claude --script sh`, versión
`1.0.2.dev0`. El Caso #2 quedó en `0.16.6.dev0`: misma estructura de archivos, contenido más nuevo.

**Consecuencias.**

- **Aparece una altitud que faltaba.** [`.specify/memory/constitution.md`](../.specify/memory/constitution.md)
  es el documento de gobierno, y con él la regla de dirección —*los requerimientos bajan, nunca
  suben*— deja de vivir solo en el README del EVAL y pasa a ser vinculante para los seis pasos.
- **El EVAL gana un insumo y no cambia de vara.** El agregador lee la constitución para D2, igual que
  en el Caso #2. La rúbrica, los pesos y el gate son los mismos de D-04: instalar una herramienta no
  reabre una decisión de puntaje.
- **Nueve skills instaladas que no se corren es deuda, y se paga declarándola.** La salida barata
  sería despertarlas creando un `specs/001-.../spec.md` mínimo; sería la peor de todas, porque ese
  archivo agregaría comportamiento sin pasar por el backlog — que es exactamente la violación de la
  regla de dirección que D4 cobra como *decisión sin requerimiento*. Borrarlas rompería los manifests
  de Spec Kit; por eso se quedan, y por eso el conteo está escrito en el [README](../README.md) y en
  la constitución en vez de quedar para que alguien lo descubra corriéndolas.
- **El saldo honesto es una skill y un documento.** Si el harness valiera solo por las herramientas,
  esta decisión sería mala. Vale por la constitución: es la primera vez que existe un documento que
  prevalece sobre los seis pasos, y sin él la regla de dirección era una convención del aparato de
  EVAL sobre pasos que no lo leen.
- **Los dos repos vuelven a ser comparables en forma, no en contenido.** `.specify/` y
  `.claude/skills/speckit-*` son la misma estructura en los dos casos. Lo que no se unifica es el
  artefacto: allá una spec, acá un backlog. Un lector que espere `specs/` acá no lo va a encontrar, y
  esta entrada existe para que no lo busque.

---

## Decisiones pendientes

Lo que todavía no se puede decidir, con la pregunta que lo destraba. Se marca con el formato del
repositorio —`[CLARIFY: pregunta]` cuando la respuesta determina el contenido— y **nunca se rellena
en silencio**. Una decisión tomada antes de tiempo es indistinguible de una inventada.

**P-01 — Los supuestos numéricos del paso `E`.** El enunciado no da **ni una cifra**: ni usuarios,
ni envíos, ni monto, ni latencia. Los tres cálculos del paso —servidores, almacenamiento, ancho de
banda— no tienen entrada.

> `[CLARIFY: ¿qué carga objetivo se asume —usuarios activos, envíos por día, factor de pico— si el enunciado no fija ninguna, y esas cifras se declaran como supuesto propio o se piden al curso?]`

**Qué la destraba:** primero, el backlog cerrado, porque las operaciones que producen carga salen de
ahí y no de la nada; después, o el curso fija una carga objetivo, o
[`E-estimar`](../redale/E-estimar/README.md) declara sus cifras como `[ASSUMPTION: …]` con la fuente
a la vista. Lo que no es admisible es una cifra sin origen: todo el paso, y los tramos de
[`E-escalar`](../redale/E-escalar/README.md), cuelgan de ella.

**P-02 — La arquitectura y la persistencia del paso `D`.** Monolito, tres capas o servicios; SQL,
NoSQL o mixta. El caso tiene una tensión interna real: el registro contable del dinero exige
transacción e invariantes duros, y el tamizaje de cumplimiento —listas que cambian sin aviso,
evidencia que hay que conservar tal como se vio— no.

> `[CLARIFY: ¿qué arquitectura y qué persistencia sostienen a la vez el invariante contable del envío y la conservación inmutable de la evidencia sobre la que se decidió una retención?]`

**Qué la destraba:** el orden de magnitud que entregue `E` —si el sistema es de decenas o de
cientos de servidores— y el backlog cerrado. Decidirla antes convierte a `D` en una decisión sin
requerimiento, que es una deducción de D4.

**P-03 — Cuándo se fija el tipo de cambio (tensión T4).** Rosa necesita que el monto en soles quede
fijo al pagar, para poder prometer una cifra. Fijarlo deja a SendIt cargando el movimiento del
cambio hasta que Elena cobre — que puede ser nunca.

> `[CLARIFY: ¿la tasa queda fija cuando Rosa paga, cuando el dinero se pone a disposición en el agente, o cuando Elena cobra — y quién carga el movimiento entre ese instante y el cobro?]`

**Qué la destraba:** nadie de afuera. **La decide el backlog**, con un título que la enuncie, y el
EVAL la cobra en D4 como *tensión esquivada* si ningún ítem la decide. La consecuencia de la opción
elegida —exposición cambiaria, prefinanciamiento del corredor— se registra en
[`D`](../redale/D-disenar-servicio/README.md), no acá.

**P-04 — Qué se le dice a Rosa cuando no se le puede decir nada (tensión T2).** Rosa exige saber por
qué se detuvo su dinero. Kevin, que es la cara de SendIt frente a ella, tiene **prohibido** decírselo
cuando hay un reporte de por medio, y ni siquiera fue él quien lo decidió. No
se resuelve redactando mejor un mensaje.

> `[CLARIFY: ¿qué recibe Rosa durante una retención reservada — plazo máximo sin motivo, silencio, o una consecuencia automática al vencer el plazo — sin que eso revele la existencia del reporte?]`

**Qué la destraba:** también el backlog. Es la tensión donde más fácil se cuela un título comodín
—«informar al cliente sobre el estado de su envío»— que aparenta decidirla sin decidir nada.

**P-05 — El corredor modelado.** Las tres personas asumen el corredor Estados Unidos → Perú, y está
marcado como `[ASSUMPTION: …]` en [`Rosa.MD`](../personas/Rosa.MD). El enunciado dice *«diferentes
países»*, en plural, y no nombra ninguno.

> `[CLARIFY: ¿el diseño debe sostenerse para cualquier corredor, o basta con uno bien resuelto y el resto se declara fuera de alcance?]`

**Qué la destraba:** el curso, o una decisión propia declarada. Pesa en D2 —el rasgo *cruza una
frontera* se puntúa contra dos jurisdicciones concretas— y en `A`, porque la identidad de Elena, las
listas de sancionados y el registro de la red pagadora cambian de forma según la jurisdicción.
