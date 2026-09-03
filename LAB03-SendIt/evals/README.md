# EVAL — backlog de requerimientos de SendIt

Aparato de evaluación del paso **R** de [R.E.D.A.L.E.](../redale/README.md). Se corre a mano.

El [enunciado](../docs/LAB-03-ARQ-2026.2.md) pide un *EVAL con resultado de requerimientos* y fija el
umbral en **8/10**. Eso decide el alcance de este documento: se puntúa el backlog, y nada más.

## Entradas

| Entrada | Papel |
|---|---|
| [`redale/R-requerimientos/backlog.md`](../redale/R-requerimientos/backlog.md) | **Lo único puntuado.** El único documento con autoridad sobre qué debe hacer el sistema |
| [`personas/Rosa.MD`](../personas/Rosa.MD) · [`Elena.MD`](../personas/Elena.MD) · [`Operario.MD`](../personas/Operario.MD) | Las lee cada agente de persona: la suya y el backlog, nada más |
| [`personas/README.md`](../personas/README.md) | La lee el agregador. De ahí salen las siete tensiones que D4 exige decididas y la designación del usuario modelo |
| [`docs/LAB-03-ARQ-2026.2.md`](../docs/LAB-03-ARQ-2026.2.md) | La lee el agregador. Fija el problema contra el que mide D2 y nombra las dos exigencias que cuenta D3 |
| [`.specify/memory/constitution.md`](../.specify/memory/constitution.md) | La lee el agregador. El enunciado dice cuál es el problema; la constitución dice **qué se hace con un ítem que no lo ataca** — el Principio III fija la prueba de D2, y el I la regla de dirección que D4 cobra como *decisión sin requerimiento* |

### Los demás pasos de R.E.D.A.L.E. no se puntúan

`E`, `D`, `A`, `L` y `E` son entregable exigido, no puntaje. El enunciado pide el EVAL **con resultado
de requerimientos**; una estimación de servidores o un diagrama de componentes no se juzgan contra esta
rúbrica y no suman ni restan en ninguna de sus cuatro dimensiones.

Lo que impide que diverjan del backlog no es puntuarlos, sino **una regla de dirección: los
requerimientos bajan, nunca suben.** Ningún paso aguas abajo puede introducir un comportamiento que el
backlog no declare. Si `D` diseña un endpoint que responde algo que ningún título exige, o `A` guarda un
campo que ningún título obliga a conocer, el defecto **es del backlog** y se cobra en D4 como
*decisión sin requerimiento*. La corrección va arriba —se agrega el título y se vuelve a puntuar—,
nunca abajo.

La regla se paga sola: convierte cualquier invención aguas abajo en una deducción de la única
dimensión que sí se puntúa, de modo que la coherencia entre pasos deja de depender de la buena
voluntad de quien los escribe.

## Rúbrica — 10 puntos

| Dim | Pts | Qué mide | Juzga |
|---|---|---|---|
| **D1** Satisfacción de las personas | 3 | El flujo principal de [Rosa](../personas/Rosa.MD), [Elena](../personas/Elena.MD) y [Kevin](../personas/Operario.MD) corre de extremo a extremo en el backlog, **incluido cuando sale mal**. 1 pt por persona, **solo deducciones** | Los 3 agentes de persona |
| **D2** Ajuste al problema | 3 | Ataca la remesa internacional —dinero que cruza una frontera y una moneda, y termina en efectivo en la mano de alguien sin banco— y no un «enviar plata» genérico | Agregador |
| **D3** Cobertura de seguridad y consistencia | 2 | Los dos requerimientos que el enunciado nombra, con medida y no como adjetivo | Agregador |
| **D4** Coherencia del backlog | 2 | Sin huérfanos ni duplicados encubiertos; títulos atómicos y entendibles **sin descripción**; las tensiones entre personas decididas y no esquivadas; prioridad asignada | Agregador |

**Gate: ≥ 8/10.** Se pueden perder dos puntos, no más. Un puntaje por debajo del gate no baja la vara:
se corrige el backlog y se vuelve a evaluar.

**La aritmética del gate no admite un camino barato.** Si el agregador entrega sus siete puntos
perfectos —cosa que no ocurrió una sola vez en las nueve rondas del caso anterior— dos personas pueden
devolver `No funciona` y el total sigue siendo exactamente 8. En cualquier otro escenario, un solo
`No funciona` obliga a que el agregador ceda como máximo un punto entre D2, D3 y D4. El gate se alcanza
por acuerdo de los dos lados o no se alcanza.

## La regla de asimetría

**Un agente de persona solo puede restar de D1. Nunca sumar.** Si ninguno objeta, D1 vale 3.

No es una cortesía metodológica, es una consecuencia de qué puede observar cada quien. Un agente lee su
persona y el backlog: ve un ángulo del problema y no ve el conjunto. Si además pudiera sumar, una
lectura entusiasta compraría puntos que ninguna otra lectura está en condiciones de contestar, y D1
terminaría midiendo la generosidad del agente en lugar de la calidad del backlog. Restringido a restar,
el agente solo puede aportar evidencia de un tipo —*acá se me corta el día*— que es exactamente el tipo
de evidencia que nadie más puede producir.

Del mismo lado: **un puntaje alto debe costar.** El máximo de D1 no se gana, se conserva; se pierde en
cuanto alguien demuestre una falla concreta con una cita concreta.

## Quién juzga qué

| Pregunta | Quién responde | Por qué |
|---|---|---|
| ¿Este backlog le resuelve el día a esta persona? | Su agente | Solo quien opera desde esa posición reconoce si el comportamiento enunciado le sirve |
| ¿Ataca la remesa internacional o un envío genérico? | Agregador | Cada persona ve un rasgo del problema; ninguna ve los tres |
| ¿Seguridad y consistencia están enunciadas con medida? | Agregador | La forma del enunciado es ajena a la perspectiva de cualquier persona |
| ¿Hay huérfanos, duplicados encubiertos o títulos comodín? | Agregador | Requiere el conjunto entero a la vista |
| ¿Las siete tensiones están decididas? | Agregador | Cada agente ve su lado de la tensión y lo da por bueno; ninguno ve el conflicto |
| ¿La prioridad está bien asignada? | Agregador | Es una comparación entre ítems, no dentro de uno |
| ¿Algún paso aguas abajo afirma lo viejo? | Agregador | La propagación solo es visible desde fuera del paso corregido |

## Cobertura contra un título

El enunciado prohíbe describir los requerimientos: **solo un título claro y entendible.** Eso deja al
agente de persona con un problema real, y hay que resolverlo antes de que alguien puntúe: ¿qué significa
que un título *cubra* un paso de mi flujo, si el título es todo lo que hay?

**Un título cubre un paso cuando pasa las tres pruebas y, leído contra ese paso, lo decide.**

| Prueba | Pasa | No pasa |
|---|---|---|
| **Nombra un hecho, no un área** | «Fijar en soles el monto que recibe la destinataria en el momento del pago» | «Gestión de tipo de cambio» — un sistema que no hace nada de eso también podría llevar ese título |
| **Es negable** | Se puede describir un sistema concreto que lo incumple | «Seguridad de extremo a extremo» — ningún sistema lo incumple y ninguno lo cumple; no exige nada |
| **Una sola lectura** | Dos lectores del enunciado y de las personas lo entienden igual | «Verificar la identidad del destinatario» — con o sin documento vigente son dos sistemas distintos, y el título no dice cuál |

Decidir el paso significa que el título determina el resultado observable que ese paso necesita. Si lo
determina en parte —cubre el monto pero no el momento en que queda fijo— la cobertura es parcial y el
veredicto no puede ser mejor que `Funciona con reservas`.

### Título comodín

Un título que falla la prueba 1 o la 2 es un **título comodín**: cubre cualquier cosa y por lo tanto no
cubre ninguna. Frente a él el agente hace dos cosas, y las dos:

1. **Cuenta el paso como no cubierto.** Un comodín no es cobertura débil; es ausencia de cobertura con
   apariencia de presencia, que es peor, porque nadie va a buscar el requerimiento que falta.
2. **Lo reporta por su nombre**, con el identificador del ítem. El agregador lo cobra en D4 como
   *título no entendible*.

Un título que falla la prueba 3 no es comodín sino **ambigüedad no marcada**: el título dice algo, pero
dice dos cosas. También lo cobra D4, y su corrección no es reescribirlo mejor sino marcarlo con
`[CLARIFY: …]` y decidirlo.

**Un mismo título puede costar en dos dimensiones a la vez, y es deliberado.** Un comodín que sostiene
el único paso donde Elena cobra falla de dos formas independientes: le deja el día sin resolver a
alguien (D1) y vuelve el backlog ilegible para cualquiera (D4). Cobrarlo una sola vez obligaría a
elegir cuál de las dos fallas se perdona.

## Protocolo del agente de persona

Se corre **una vez por persona, por separado**. Cada agente vive en
[`.claude/agents/`](../.claude/agents/) y lee **exactamente dos archivos**: el suyo en
[`personas/`](../personas/) y el [backlog](../redale/R-requerimientos/backlog.md). Nada más: ni las
otras personas, ni [`personas/README.md`](../personas/README.md), ni los veredictos ajenos, ni el
historial.

La exclusión de `personas/README.md` es la que más cuesta explicar y la que más importa: ese archivo
contiene las siete tensiones y el ángulo de las otras dos personas. Un agente que lo lee deja de
reclamar y empieza a negociar —«entiendo que Kevin necesita tiempo»— y ahí se pierde la única señal que
el agente existe para producir. Las tensiones las decide el backlog y las juzga el agregador, no la
persona que las sufre.

Cada agente responde, en este orden:

1. **¿Mi flujo principal corre de extremo a extremo, incluido cuando sale mal?** Citando los ítems del
   backlog por su identificador. Si se corta, decir en qué paso. Un flujo cubierto solo en su camino
   feliz no aprueba esta pregunta: el *cuando sale mal* de cada persona es parte del flujo.
2. **¿Qué me frustra?** Lo que el backlog decide en mi contra, lo que deja sin decidir para que lo
   absorba yo, y cualquier título que rompa mis permisos.
3. **Veredicto.**

| Veredicto | Resta | Se emite cuando |
|---|---|---|
| `Funciona` | 0 | Cada paso del flujo y el *cuando sale mal* están sostenidos por títulos que pasan las tres pruebas |
| `Funciona con reservas` | 0,5 | El flujo corre entero, pero al menos un paso se sostiene en un título comodín o en cobertura parcial, o el *cuando sale mal* se cubre solo en parte |
| `No funciona` | 1 | Un paso del flujo principal no lo sostiene ningún título; o el *cuando sale mal* no está cubierto en absoluto; o un título le concede a alguien algo que este archivo de persona declara «nunca debe» |

**Un veredicto sin cita al backlog es inadmisible y cuenta como `No funciona`.** Una cita a un
identificador que no existe en el backlog tampoco es cita.

**El agente califica en las dos direcciones.** Resta por lo que genuinamente falla, y **no** resta por
lo que su archivo no pide, por alcance razonablemente diferido, ni por una redacción que él solo habría
formulado de otro modo. Un agente que deduce por todo convierte D1 en ruido y deja de distinguir la
ronda en que el backlog empeoró.

**Precondición: sin los tres veredictos no se emite total.** Si falta uno, D1 se declara no computable,
se informan D2, D3 y D4, y el total queda en blanco. No se sustituye el veredicto ausente por el
criterio del agregador.

## Cómo puntúa el agregador

### D2 — Ajuste al problema · 3 pts

El problema tiene tres rasgos, y el backlog vale por atacarlos, no por nombrarlos. **Un punto por
rasgo**, y cada rasgo se puntúa contra un censo: *si el rasgo desapareciera, ¿qué ítems del backlog
seguirían siendo palabra por palabra lo que necesita una transferencia doméstica entre dos cuentas de
banco en la misma moneda?*

| Rasgo | 1 pt | 0,5 pt | 0 pt |
|---|---|---|---|
| **Cruza una frontera** — dos jurisdicciones, dos reguladores, un corredor prefinanciado | Al menos un ítem se vuelve falso si el rasgo desaparece | El rasgo se toca de costado | Nombrado o ausente |
| **Cruza una moneda** — hay un momento en que la tasa se fija y alguien carga el movimiento entre ese momento y el cobro | ídem | ídem | ídem |
| **Termina en efectivo, sin banco, en manos de un tercero** — el último tramo no tiene pantalla y su registro contable no es nuestro | ídem | ídem | ídem |

El censo se anota en la corrida con su conteo. Un backlog cuya mayoría de ítems sobrevive intacta a la
desaparición de los tres rasgos describe un producto distinto del que pidió el enunciado, por más
correcto que sea cada ítem por separado.

### D3 — Cobertura de seguridad y consistencia · 2 pts

**Un punto cada una.** El enunciado las nombra a las dos; nombrarlas de vuelta no es cubrirlas.

| Pts | Estado |
|---|---|
| **1** | Al menos un ítem enuncia la garantía con una medida o un invariante que alguien puede declarar cumplido o incumplido, y el camino de falla está cubierto |
| **0,5** | Enunciada como comportamiento, pero sin medida ni invariante, o solo en el camino feliz |
| **0** | Enunciada como adjetivo —«el sistema debe ser seguro»— o ausente |

**La medida no siempre es un número.** Para la consistencia, la forma correcta es casi siempre un
invariante: *ninguna operación figura retenida y pagada a la vez*, *ningún envío se cobra dos veces*.
Un invariante es más fuerte que un porcentaje porque no depende del conjunto de casos que alguien haya
armado. Exigir un número donde corresponde un invariante degrada el requerimiento.

**El hint del enunciado sobre «diseñar bien el mecanismo de seguridad» no autoriza a meterlo en el
backlog.** El mecanismo se decide en [`D`](../redale/D-disenar-servicio/). Lo que el backlog debe decir
es qué tiene que garantizar ese mecanismo —quién no puede leer qué, quién no puede hacer qué sin dejar
rastro—, y eso es lo que D3 puntúa.

### D4 — Coherencia del backlog · 2 pts

> **Enmendada el 2026-08-27, en la ronda 08, por el dictamen de la
> [iteración 07](iterations/2026-08-27-07.md).** La versión anterior —«empieza en 2 y baja 0,25 por
> hallazgo, con piso 0»— **medía tamaño, no coherencia**: en siete rondas `n` varió entre 15 y 41, un
> rango de 2,7×, y **D4 no se movió una sola vez**. Varianza cero.
>
> **Las corridas 01 a 07 dejan de ser comparables con las de aquí en adelante.** No se recalculan:
> quedan como se emitieron, con la vara con que se emitieron.

**D4 se puntúa por densidad de hallazgos, no por su cuenta.**

```
d  = n / ítems          densidad observada
D  = 0,40               densidad de referencia
D4 = 2 × (1 − d / D)    acotado a [0 , 2]
```

`D = 0,40` se fija **por encima de la peor densidad que este proyecto observó** (36,6 % en la ronda
01), de modo que un backlog peor que cualquiera de los siete puntúe 0 y uno sin hallazgos puntúe 2.

**Por qué densidad y no cuenta.** D4 era la única dimensión de esta rúbrica con un conteo absoluto.
D1 puntúa **por persona**; D2 y D3 son **existenciales**; y el censo de D2 se reportó **siempre como
razón** —«4 de 41», «78 de 118»—. La rúbrica ya normalizaba en D2 y no lo hacía acá. Los hallazgos
escalan con la superficie: con el piso en `n ≥ 8`, `D4 > 0` exigía un backlog de a lo sumo **31
ítems** a la mejor densidad alcanzada, y de **23** a la media. El ejemplo del profesor tiene cinco.

**Qué no cambia.** La lista de hallazgos, cómo se cuentan, los dos techos duros y el contraste
cruzado quedan **exactamente como estaban**. Lo único que cambia es cómo el número de hallazgos se
convierte en puntaje.

| Hallazgo | Qué es |
|---|---|
| Huérfano | Un ítem que no sirve a ninguna de las tres personas ni a una exigencia explícita del enunciado |
| Decisión sin requerimiento | Un paso aguas abajo afirma un comportamiento que ningún título exige |
| Duplicado encubierto | Dos títulos que dicen lo mismo con otras palabras, o uno que es caso particular de otro |
| Título no entendible | Un **título comodín**, según las pruebas de arriba |
| Ambigüedad no marcada | Dos lecturas razonables y ningún `[CLARIFY: …]` |
| Título no atómico | Dos cosas que pueden ser verdaderas o falsas por separado bajo un identificador |
| Tensión esquivada | Una de las siete de [`personas/README.md`](../personas/README.md) que ningún ítem decide |
| Prioridad ausente | Un ítem sin prioridad |

**Techos duros.** Se aplican después de las deducciones y no se negocian:

- Si **dos o más** de las siete tensiones quedan sin decidir, **D4 no supera 1,0**. Una tensión sin
  decidir no es un hallazgo más: es la decisión que el backlog existía para tomar.
- Si **todos** los ítems comparten la misma prioridad, **D4 no supera 1,5**. Una lista sin gradiente no
  está priorizada.

**Contraste cruzado — conformidad unánime.** Si los tres agentes devuelven `Funciona` sin una sola
reserva y alguna tensión queda sin decidir, el hallazgo encabeza la lista de correcciones y D4 no supera
1,0. Tres personas conformes a la vez es el resultado esperado de un backlog que decidió bien, y también
el resultado esperado de un backlog que evitó decidir; la tensión sin decidir es lo que distingue un
caso del otro.

## Reglas de redacción que el agregador exige al backlog

Son las que D3 y D4 comprueban. Deliberadamente pocas.

- **Verificable.** «Rápido», «seguro» y «confiable» se reemplazan por su medida o su invariante. Un
  enunciado que nadie puede declarar cumplido o incumplido no es un requerimiento.
- **Atómico.** Una cosa verdadera o falsa, modificable por separado.
- **Sin mecanismo.** El backlog enuncia la garantía, no la tecnología que la cumple. Una cola, un
  producto de nube o una topología dentro de un título son una decisión de arquitectura disfrazada, y
  su lugar es [`D`](../redale/D-disenar-servicio/).
- **Un título dice el comportamiento, no la tecnología.** *(Nueva en este caso.)* «Cifrado AES-256 en
  reposo» no es un requerimiento: es la respuesta a uno que nadie escribió. La garantía es otra cosa
  y se reconoce porque nombra a alguien y una circunstancia —*quién no puede leer los datos de
  identidad de Elena aunque tenga la base de datos delante*—. Si al quitarle el nombre del algoritmo
  el título deja de decir algo, no decía nada más que el algoritmo.
- **La ambigüedad se marca, nunca se rellena en silencio.** El enunciado deja el dominio abierto. Lo
  indefinido lleva uno de dos marcadores:
  - `[CLARIFY: pregunta concreta]` cuando la respuesta determina el contenido.
  - `[ASSUMPTION: enunciado]` cuando se avanza bajo una hipótesis declarada.
- **Sin referencias portantes.** Un puntero al final es admisible. Una frase que no se entiende sin ir
  a buscar lo que referencia, no — y en un backlog sin descripción, menos todavía.
- **Nada se nombra por su texto visible.** La etiqueta de un botón o el asunto de un mensaje cambian
  sin que cambie ningún requerimiento. Se nombra la intención.

## Propagación

La lección más cara del caso anterior no fue de sustancia. Fue esta: **el modo de falla dominante es la
propagación.** Nueve rondas, y la mayoría de los hallazgos de coherencia eran un requerimiento
corregido mientras el enunciado que lo gobernaba seguía afirmando lo viejo — incluido, dos veces, el
propio defecto de la ronda anterior sobreviviendo una altitud más abajo.

En R.E.D.A.L.E. pega más fuerte, porque los pasos están explícitamente encadenados y el método lo dice:
*cada paso consume la salida del anterior*. **Tocar `R` obliga a rebarrer `E`, `D`, `A` y `L`.** Un
título corregido deja una estimación calculada sobre el volumen viejo, un endpoint que responde lo que
ya no se promete y una tabla con un campo que ya nadie llena.

El agregador busca **por nombre** las cuatro variantes que el caso anterior encontró:

| Variante | Qué es | Cómo se ve en SendIt |
|---|---|---|
| **Cifra sin productor** | Un valor del que todo depende y que ningún ítem produce | El backlog promete el monto en soles fijado al pagar, y ningún título dice quién fija la tasa ni en qué instante queda fija |
| **Acto sin consumidor** | Algo que se puede hacer, registrar y recuperar, y que no llega a nadie ni puede ser respondido | El sistema retiene un envío y ningún ítem lo paga, lo devuelve ni lo libera |
| **Reparación en la altitud equivocada** | El arreglo se aplica donde se vio el síntoma, no en el enunciado que lo gobierna | Se corrige un `RF` y el usuario modelo, las preguntas de encuadre o `D` siguen afirmando lo anterior |
| **Estado sin terminador** | Un estado que se abre y que nada cierra | Una retención cuyo plazo vence y no produce consecuencia; un envío «en proceso» que no llega a ningún estado final; un cobro de Elena que no cierra el envío |

Cada rebarrido se registra en la corrida **aunque no encuentre nada**. Un rebarrido vacío es un
resultado; un rebarrido que nadie corrió no lo es, y son indistinguibles si no se anota.

## Cómo se corre una iteración

1. **Congela el estado.** Anota el SHA corto del commit que se evalúa. El puntaje pertenece a ese SHA.
2. **Corre los tres agentes de persona**, por separado y aislados entre sí, cada uno contra su archivo
   y el backlog. La coincidencia entre tres lecturas solo es evidencia si son independientes.
3. **Corre el agregador**: D2 con su censo, D3, D4 con sus techos, y los cuatro rebarridos de
   propagación por nombre.
4. **Computa** `D1 = 3 − Σ(deducciones)` y el total sobre 10. Verifica la precondición de los tres
   veredictos antes de emitir cualquier total.
5. **Escribe** `evals/iterations/AAAA-MM-DD-NN.md` siguiendo [la plantilla](iterations/_TEMPLATE.md).
6. **Agrega la fila** a [`HISTORY.md`](HISTORY.md), y la iteración a
   [`redale/ITERACIONES.md`](../redale/ITERACIONES.md) si cambió alguna decisión de diseño.
7. **Si el total es menor que 8: corrige el backlog y vuelve al paso 1.** El backlog cambia; la rúbrica
   no.

**Medir y corregir no ocurren a la vez.** Las correcciones se aplican **después** de puntuar y quedan
sin puntaje hasta la ronda siguiente, que las mide en un SHA nuevo. Corregir durante la medición
destruye la medición: quien corrige conoce la vara, y el segundo número diría tanto sobre el backlog
corregido como sobre la corrección ajustada al número.

**Ni la rúbrica ni las personas se editan para elevar el puntaje.** Son la vara.

## Cómo se enmienda la rúbrica

Hay un caso, y uno solo, en que la vara sí se toca: cuando **una dimensión deja de distinguir un
backlog bueno de uno malo**. Una dimensión así no está midiendo lo que dice medir, y conservarla
intacta no es rigor — es un punto muerto en una rúbrica de diez. La autorización y su límite están en
el Principio IV de la [constitución](../.specify/memory/constitution.md); acá va el procedimiento.

**Las cuatro condiciones. Se exhiben las cuatro, o no hay enmienda:**

| # | Condición | Cómo se comprueba |
|---|---|---|
| 1 | **La fuerza una falla del instrumento, no un puntaje** | Se cita la corrida que la detectó y la evidencia numérica: varianza, rango, correlación con algo que la dimensión no debía medir |
| 2 | **Se escribe antes de aplicarse, y corre en su propia ronda** | La ronda que la estrena no corrige nada más del backlog, para que el movimiento del puntaje sea atribuible a la enmienda y no a las correcciones |
| 3 | **Se declara qué corridas dejan de ser comparables** | Una línea en [`HISTORY.md`](HISTORY.md) y el aviso en la dimensión enmendada. Las viejas **no se recalculan**: quedan como se emitieron, con la vara con que se emitieron |
| 4 | **Se demuestra que no compra el gate** | Se recalculan las rondas pasadas con la fórmula nueva y se publica la tabla. **Si alguna alcanza el gate que con la vara vieja no alcanzaba, la enmienda es un ablandamiento y se rechaza** |

La cuarta es la que separa una calibración de una trampa, y es la única que no se puede argumentar:
se calcula. Un aparato que solo puede corregirse hacia arriba no es un aparato, es una expectativa.

**Dónde vive cada cosa.** La enmienda se redacta en un archivo propio de `evals/` —con la evidencia
de la condición 1 y la tabla de la condición 4— y el resultado se aplica a la dimensión de este
documento con la fecha y la ronda en que entró en vigor. El archivo **no se borra después de
aplicarla**: es donde queda la prueba de que las cuatro condiciones se cumplieron, y sin él la
dimensión enmendada solo afirma que alguna vez lo estuvieron.

Registro de enmiendas hasta hoy:

| Ronda | Dimensión | Qué falló en el instrumento | Evidencia |
|---|---|---|---|
| 08 | **D4** | Puntuaba por cuenta de hallazgos, no por densidad: en siete rondas `n` varió 2,7× y D4 no se movió una sola vez. Medía tamaño | [`ENMIENDA-PROPUESTA-D4.md`](ENMIENDA-PROPUESTA-D4.md) |
