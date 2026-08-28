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
| [D-09](#d-09--d4-se-enmienda-para-puntuar-por-densidad) | D4 se enmienda para puntuar por densidad | Cuándo se puede tocar la vara, y qué hay que demostrar para tocarla |
| [D-10](#d-10--el-codigo-perdido-es-la-septima-tension) | El código perdido es la séptima tensión | Cuántas tensiones exige D4 decididas, y qué se le responde a Rosa cuando pierde el código |

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

## D-09 — D4 se enmienda para puntuar por densidad

**Contexto.** El dictamen de la [iteración 07](../evals/iterations/2026-08-27-07.md) no fue sobre el
backlog sino sobre el aparato: `D4 = 2 − 0,25n` con piso en `n ≥ 8`. En siete rondas el backlog creció
de 41 a 118 ítems y `n` osciló entre 15 y 41 —un rango de 2,7×—, y **D4 marcó 0,00 las siete veces.
Varianza cero.** Una dimensión que devuelve el mismo número para el peor y el mejor backlog de la
serie no está midiendo coherencia: mide tamaño, porque los hallazgos escalan con la superficie.

Y hay un choque de gobierno: el Principio IV de la [constitución](../.specify/memory/constitution.md)
dice que un puntaje bajo el gate corrige el backlog, **nunca la vara**.

**Opciones.**

| Opción | A favor | En contra |
|---|---|---|
| Dejar D4 como estaba | Respeta la letra del Principio IV y ninguna corrida deja de ser comparable | Deja dos puntos muertos en una rúbrica de diez: con el piso en `n ≥ 8`, `D4 > 0` exigía un backlog de a lo sumo 31 ítems a la mejor densidad alcanzada. **El gate se vuelve inalcanzable por aritmética, no por calidad** |
| Subir el piso o bajar el paso por hallazgo | Cambio mínimo, la fórmula se mantiene | Es exactamente el ablandamiento que el Principio IV prohíbe: mueve el número sin arreglar qué mide |
| **Puntuar por densidad** | Mide `n` contra el tamaño, que es lo que la dimensión decía medir. Normaliza igual que D2, que siempre se reportó como razón —«4 de 41», «78 de 118»— | Las corridas 01 a 07 dejan de ser comparables con las siguientes |

**Decisión.** **Densidad**, en vigor desde la ronda 08: `D4 = 2 × (1 − d/D)` acotado a `[0, 2]`, con
`d = n / ítems` y `D = 0,40` fijada por encima de la peor densidad observada (36,6 % en la ronda 01),
de modo que un backlog peor que cualquiera de los siete puntúe 0 y uno sin hallazgos puntúe 2.

**El choque con el Principio IV se resuelve enmendando el principio, no ignorándolo.** La constitución
pasa a v1.1.0 y distingue **calibrar el instrumento** de **ablandar la vara**, con cuatro condiciones
que hay que exhibir las cuatro. Esta enmienda las cumple, y la cuarta es la que la separa de una
trampa: recalculadas con la fórmula nueva, **ninguna ronda pasada alcanza el gate que con la vara
vieja no alcanzaba** — la ronda 08 con la fórmula vieja habría dado 6,0, idéntico a la 07. La
evidencia completa está en [`evals/ENMIENDA-PROPUESTA-D4.md`](../evals/ENMIENDA-PROPUESTA-D4.md) y el
procedimiento en [`evals/README.md`](../evals/README.md).

**Consecuencias.**

- **La serie se parte en dos.** Las corridas 01 a 07 y las 08 en adelante no son comparables entre sí.
  No se recalculan: quedan como se emitieron, con la vara con que se emitieron. Cualquier lectura de
  la tendencia que cruce la ronda 08 es inválida, y hay que decirlo cada vez que se muestre el
  historial completo.
- **La vara deja de ser intocable y pasa a ser enmendable bajo prueba**, que es una pérdida real: un
  aparato que se puede cambiar es un aparato que se puede negociar. Lo que lo sostiene es la condición
  cuarta, la única que no se argumenta sino que se calcula.
- **La densidad tiene su propio punto ciego, y ya apareció.** La auditoría de la
  [ronda 09](../evals/iterations/2026-08-27-09.md) mostró que la ronda tocó el 18 % del backlog y
  produjo el 81 % de los hallazgos: un factor de 19× que el promedio aplana hasta volverlo invisible.
  La fórmula mide mejor que la anterior, no mide bien.

---

## D-10 — El código perdido es la séptima tensión

**Contexto.** Las tensiones entre personas eran seis y se creían completas. La
[iteración 07](../evals/iterations/2026-08-27-07.md) encontró una séptima, y la encontró de la peor
manera: **dos rondas la habían revertido en direcciones opuestas**, cada una costando un punto entero
de D3, sin que nadie la nombrara. Rosa **nunca debe** poder recuperar el código por un canal de
SendIt, porque eso lo volvería obtenible por cualquiera que se haga pasar por ella. Y Elena **no puede
cobrar sin él**.

**Opciones.**

| Opción | A favor | En contra |
|---|---|---|
| Tratarla como defecto de dos ítems | No toca la lista de tensiones | Es lo que se intentó dos veces, y las dos rondas siguientes lo revirtieron. Un conflicto que no está nombrado se «arregla» hacia un lado y hacia el otro para siempre |
| Reponer el código por un canal verificado | Elena cobra, Rosa no pierde el dinero | Un secreto reponible deja de ser secreto: el procedimiento de excepción *es* el agujero |
| **Nombrarla T7 y decidirla en el backlog** | Queda bajo el techo duro de D4, que obliga a decidirla en vez de esquivarla | Sube a siete el denominador de las tensiones y obliga a rebarrer los documentos que decían seis |

**Decisión.** **T7 existe y se decide por cancelación, no por reposición.** El código no se repone
nunca (RF-94); el emisor cancela el giro cuyo código se perdió mientras el dinero no esté a
disposición del receptor (RF-110) y lo rehace al mismo receptor (RF-117), conservando la cotización
del cancelado (RF-134) y sin volver a cobrar comisión (RF-135). El giro rehecho vuelve a correr todos
los controles, incluida la identificación contra documento (RF-123).

**Consecuencias.**

- **El dinero deja de quedar atrapado hasta prescribir sin que el secreto deje de serlo.** Es la única
  salida que no abre una ruta de lectura, y cuesta: Rosa tiene que volver a la ventanilla.
- **El techo duro de D4 ahora se cuenta sobre siete.** Dos tensiones sin decidir siguen dejando D4 en
  1,0, pero el denominador cambió y hay que barrer todo documento que dijera «seis» — cosa que la
  ronda que la introdujo **no terminó de hacer**.
- **La forma de esta tensión es la que hay que recordar, no su contenido.** Dos correcciones opuestas
  y sucesivas sobre los mismos ítems no son dos errores: son la firma de un conflicto que nadie
  nombró. Buscar esa firma es más barato que descubrir la tensión a la tercera ronda.

---

## Decisiones pendientes

**Ninguna. Las cinco quedaron cerradas.**

Se registraron cuando el backlog estaba vacío y ninguna se podía decidir sin él. Se cierran ahora
porque el trabajo que las destrababa se hizo, y **ninguna se rellenó en silencio**: cada una se
decidió en la altitud que le correspondía, y esta tabla dice cuál. Las que se resolvieron **dentro de
un paso** no ascienden a `D-nn` — la regla de admisión de este archivo las deja gobernadas por el
contrato de su paso.

| # | La pregunta que la destrababa | Dónde se decidió | Qué se decidió |
|---|---|---|---|
| **P-01** | Qué carga objetivo se asume, si el enunciado no da ni una cifra | [`E-estimar`](../redale/E-estimar/README.md) | Cifras propias, cada una con su `[ASSUMPTION: …]` y la calibración contra la que se defiende. **No se pidieron al curso** |
| **P-02** | Qué arquitectura y qué persistencia sostienen a la vez el invariante contable y la evidencia inmutable | [`D-disenar-servicio`](../redale/D-disenar-servicio/README.md) | Resuelto en sus secciones 1 y 2, y en las seis decisiones que el paso registra —empezando por dónde vive la verdad del dinero y la idempotencia |
| **P-03** | Cuándo se fija el tipo de cambio, y quién carga el movimiento (T4) | El **backlog**: RF-05 · RF-06 · RF-07 | Se fija al crear el giro y no se recalcula nunca, contra una cotización que el sistema produce y fecha. **La empresa carga el movimiento** |
| **P-04** | Qué recibe Rosa durante una retención reservada, sin revelar el reporte (T2) | El **backlog**: RF-39 · RF-40 · RF-66 · RF-67 | Rosa ve **que** está retenido y **hasta cuándo**, nunca por qué. Y el operario recibe **la acción y no el motivo**, para que no pueda deducirlo ni filtrarlo |
| **P-05** | Si el diseño debe sostenerse para cualquier corredor o basta con uno | El **backlog**: RNF-12 y su supuesto | Más de un país de origen desde el primer día, con **dos corredores declarados** al lanzamiento —Estados Unidos → Perú y Estados Unidos → México—, que es lo que impide que una sola moneda destino se cuele como supuesto tácito |

**Que la lista esté vacía no significa que no quede nada abierto.** Lo que queda abierto son
correcciones del backlog, no decisiones de arquitectura, y viven donde les corresponde:
[`evals/CORRECCIONES-RONDA-12.md`](../evals/CORRECCIONES-RONDA-12.md).
