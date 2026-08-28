# Iteraciones del diseño

El enunciado exige **mostrar claramente las iteraciones**. Esta es la bitácora.

Hay **dos clases de iteración** y confundirlas arruina el entregable. Ambas viven acá, en tablas
separadas, porque una fuerza a la otra.

| Clase | Qué es | Qué la hace avanzar | Dónde se ve |
|---|---|---|---|
| **Del diseño** (*top-down*) | El **mismo diagrama de componentes**, dibujado otra vez y más abierto | Un ítem del backlog que el diagrama actual no explica | [`L-listar-componentes/`](L-listar-componentes/) |
| **Del EVAL** | Una pasada de evaluación que **cambia una decisión** del backlog | Un puntaje bajo el gate, o un veredicto de persona | [`../evals/iterations/`](../evals/iterations/) |

La que el enunciado pide mostrar es la **primera** — así la mostró el profesor en clase (ver
[`../docs/EJEMPLO-CLASE-TOP-DOWN.md`](../docs/EJEMPLO-CLASE-TOP-DOWN.md)). La segunda es cómo se
llega a un backlog que valga la pena diagramar.

---

## Iteraciones del diseño

Cada fila es una pasada del diagrama. La regla que las gobierna: **no se dibuja el diagrama final y
después se inventan las iteraciones previas.** La primera es un cuadrado; lo que fuerza la
siguiente es un ítem del backlog que el cuadrado no explica.

| # | Qué muestra | Qué ítem del backlog la forzó | Ítems que quedan `DONE` |
|---|---|---|---|
| **1** | Los cuatro actores y **una sola caja**. Rosa y Elena hablan cada una con un operario, y el operario con el sistema — bajo el modelo Western Union las dos puntas pasan por una ventanilla | Nada la fuerza: es el punto de partida. Lo único que afirma es **quién habla con el sistema** | **1** — RF-11, que se demuestra por la *ausencia* de una arista hacia el receptor |
| **2** | La caja se abre: identificación, tamizaje, creación del giro y pago, con sus `BD`, sus sistemas externos y las aristas condicionales etiquetadas | **RF-26** — el tamizaje contra listas antes de aceptar el efectivo no cabe dentro de un cuadrado que no distingue quién decide qué | **36** — 29 RF y 7 RNF |
| **3** | El resto: devolución, desafío, caja por punto, cobro alternativo, reclamo del receptor, supresión, acumulado de cobros y liquidación con el agente | **RF-68 y RF-69** — el desafío obliga a un servicio y un almacén propios, porque RNF-17 exige que la respuesta sea ilegible **en los dos lados del mostrador** | **118** — 108 RF y 10 RNF |

**Total: 222 de 222.** La tercera pasada **creció de 81 a 175 filas** entre las rondas 05 y 17 del EVAL
sin que hiciera falta una cuarta: casi todo ítem nuevo cayó dentro de un componente que ya existía.
Eso es lo que una tercera iteración bien abierta tiene que poder absorber, y es la prueba de que el
corte fue en el lugar correcto. Los pocos componentes que nacieron después de la tercera pasada son
los que el propio EVAL forzó —`Código Service`, `Terminal del Cliente`, `Rehacer Service`,
`Condiciones Previas Service`—, y cada uno tiene su ítem que lo pidió. La trazabilidad ítem por ítem vive en
[`L-listar-componentes/`](L-listar-componentes/), que es donde el `DONE` se verifica; esta tabla
dice **por qué** hubo otra pasada, no **qué** quedó cubierto.

La trazabilidad completa —qué ítem cubre qué iteración— vive en
[`L-listar-componentes/`](L-listar-componentes/), no acá. Esta tabla dice **por qué** hubo otra
pasada; aquella dice **qué** quedó cubierto.

---

## Iteraciones del EVAL

Una fila por corrida. El detalle de cada una en [`../evals/iterations/`](../evals/iterations/) y el
resumen en [`../evals/HISTORY.md`](../evals/HISTORY.md).

| # | Fecha | D1 /3 | D2 /3 | D3 /2 | D4 /2 | Total | Qué la forzó y qué cambió |
|---|---|---|---|---|---|---|---|
| **01** | 2026-08-26 | 1,0 | 1,5 | 1,0 | 0,0 | **3,5** | Primera corrida, sobre un backlog de 41 ítems escrito antes del modelo Western Union. **El censo de D2 lo mató: solo 4 de 41 ítems cambiaban si el envío dejaba de cruzar un país.** El corredor vivía en un `[ASSUMPTION]`, no en un requerimiento — *la frontera no era puntuable porque no era exigible* |
| **02** | 2026-08-26 | 0,5 | 2,5 | 1,0 | 0,0 | **4,0** | Backlog reescrito entero desde `insumos.md` sobre el modelo nuevo. Entró el bloque **«La frontera»** y D2 subió un punto. **D1 bajó**: dos correcciones incompletas costaron dos `No funciona`. De diez correcciones, **2 aplicadas, 6 a medias** |
| **03** | 2026-08-26 | 1,0 | 2,5 | 1,5 | 0,0 | **5,0** | **Dos tensiones cerradas en una ronda** (T5 y T6) y la retención por fin termina. Consistencia llega a 1,0 con RNF-13 y RF-45 ampliado |
| **04** | 2026-08-26 | 1,5 | **3,0** | 1,5 | 0,0 | **6,0** | **D2 al máximo**: 51 de 97 ítems mueren en una transferencia doméstica, y la proporción se sostuvo mientras el backlog crecía 20 %. **Cero tensiones sin decidir por primera vez.** Elena sale de `No funciona` gracias al desafío — que abrió el agujero de seguridad de la 05 |
| **05** | 2026-08-26 | 1,5 | **3,0** | **2,0** | 0,0 | **6,5** | **D3 al máximo**: el triángulo RF-68/69/57 cerró con invariante declarable (RNF-17). Censo de D2 en **73 de 110**. Gradiente de prioridad verificado exacto. **D4 sigue en el piso con n=28** |
| **06** | 2026-08-27 | 1,5 | 3,0 | 1,0 | 0,0 | **5,5** | **Primera regresión de la serie, entera en D3.** Tres de los nueve ítems nuevos niegan el invariante que los justificaba: RF-94 contra RNF-15 —un sistema que no puede mostrar un código no puede reentregarlo—, RF-100 contra RNF-05, y RF-101 contra RF-69, que reabre T3 |
| **07** | 2026-08-27 | 1,0 | 3,0 | **2,0** | 0,0 | **6,0** | **Se revierte la regresión**: RF-94 y RF-100 pasan de negar su invariante a ejercerlo. `n` baja de 41 a **26**, la mejor densidad de la serie, y el backlog **se achica por primera vez**. Y el agregador dictamina que **D4 no está calibrada para 118 ítems: varianza cero en siete rondas** |

| **08** | 2026-08-27 | 1,5 | 3,0 | 1,5 | **1,12** | **7,12** | **La ronda que cambió la vara.** El dictamen de la 07 se aplica: `D4` pasa de restar 0,25 por hallazgo a puntuar por **densidad**, `2 × (1 − d/D)` con `D = 0,40`. Las corridas 01-07 dejan de ser comparables y **no se recalculan**. La comprobación de honestidad, hecha sobre datos nuevos: con la fórmula vieja y n=22 habría leído 0,00 por octava vez y el total habría sido 6,0, idéntico al de la 07 — **la enmienda no ablandó la vara**. Y D3 **bajó**, porque el agregador empezó a cobrar en D3 el hueco del mostrador que antes solo cobraba en D1 |
| **09** | 2026-08-27 | 1,0 | 3,0 | 1,5 | 1,00 | **6,5** | **El techo duro de las tensiones ata por primera vez en nueve rondas.** T2 y T3 se reabrieron, las dos por correcciones de la 08: al reescribir RF-39 se le dio a Kevin **la razón** en vez de **la acción**, que es justo lo que RF-40 prohíbe; y al partir RF-69 se perdió el título que autorizaba el pago con documento vencido. La lección: **partir un ítem puede perder una garantía sin que ningún `grep` lo delate** |
| **10** | 2026-08-27 | **1,5** | 3,0 | 1,5 | 0,54 | **6,54** | **Primera ronda sin un solo `No funciona`**: los tres flujos corren de extremo a extremo y Elena sale del piso. Y el puntaje sube 0,04, porque es **la primera ronda que rebarre enteras las tres mil líneas de `E`, `D`, `A`, `L` y `E-escalar`**: `n` salta de 26 a **40**. El hallazgo que ordena a los demás: **T5, la tensión de los canales, era la única que no decidía el suyo** — la fila decía que el código no se transmite a nadie, RF-11 decía que se entrega al emisor, RNF-15 que no puede mostrarse, y ningún título nombraba el canal. Kevin lo venía reportando desde la 06 como «el paso 4 no existe» |

| **11** | 2026-08-27 | 1,5 | 3,0 | 1,5 | 0,61 | **6,61** | **La ronda que más cerró y menos movió el puntaje.** Cero tensiones sin decidir por primera vez desde la 05, 28 de los 40 hallazgos anteriores cerrados, el backlog de 137 a 155 ítems y la propagación rehecha entera en los cinco pasos — **+0,07**. Lo que lo explica: el rebarrido fue tan profundo como el de la 10 y encontró 43 hallazgos nuevos. Y el hallazgo que ordena a los demás es sobre la corrección de la ronda anterior: **el hueco del mostrador se movió de extremo en vez de cerrarse.** La 10 decidió por dónde *sale* el código y no por dónde *entra*, y `D` y `L` ya habían llenado la ausencia inventando |

| **12** | 2026-08-27 | 1,5 | 3,0 | 1,5 | **1,34** | **7,34** | **El salto más grande de la serie: +0,73.** `n` cae de 43 a **23** mientras el backlog crece 13 %, y la densidad se parte casi por la mitad. Se cierran los dos extremos del secreto —`RF-147` decide por dónde **entra** el código— y **T3 queda decidida entera por primera vez** con `RF-148`. La contradicción `A`↔`D` de las cuentas contables, el defecto más grave del rebarrido anterior, queda saldada. El medio punto de D3 se mueve: partir `RF-39` en tres **destapó** que `RF-40` y `RF-152` protegen el motivo del *rechazo* y dejan descubierto el de la *retención* — el defecto estaba tapado dentro de un título no atómico desde que `RF-40` se escribió. Y la fracción específica de remesa baja por segunda vez, de 61,3 % a **54,9 %** |
| **13** | 2026-08-27 | 1,5 | 3,0 | 1,5 | **1,66** | **7,66** | **`n` cae a 13 y la densidad a 6,77 %, la mejor de la serie por un margen amplio** — y **dos clases enteras de hallazgo llegan a cero por primera vez**: sin huérfanos y sin comodines. El total lo aporta D4 entero: D1, D2 y D3 no se mueven. **Los cuatro bloques que separaban del gate se escribieron los cuatro, cerraron las tres reservas nombradas, y D1 siguió en 1,5**: cada persona encontró una reserva nueva *de la misma clase* que la que se le cerró, y esta vez con la forma «el título existe y le falta el par». `RF-187`, escrito para cerrar el lado de Elena, **cerró 0,5 de D1 y abrió 0,5 de D3**: es el tercer acto remoto del receptor y el único sin compuerta de identidad, y además obliga a ocultarle a Rosa el origen de la solicitud. El agregador deja anotado un **candidato a enmienda de D2** —diez rondas leyendo 3,0 con la fracción moviéndose entre 52,6 % y 61,3 %— y no lo aplica |
| **14** | 2026-08-27 | 1,5 | 3,0 | 1,5 | **1,75** | **7,75** | **`n = 10` y `D4 = 1,75`, las dos mejores lecturas de la serie** — y cuatro clases de hallazgo en cero. El movimiento vuelve a ser D4 entero: D1, D2 y D3 no se mueven por segunda ronda. **El medio punto de D3 lo produjo la corrección que venía a recuperarlo**: retirar `RF-126` declarándolo «contenido en `RF-180`» fue falso —`RF-180` enumera consultar, comprobar y solicitar, y **declarar una diferencia no está**— y detrás de esa declaración `RF-194` repone por vencimiento de plazo, o sea **un pago por silencio**. La no atomicidad de `RF-180` es lo que permitió que el cuarto disparador desapareciera sin que nadie lo viera, y **cuatro pasos aguas abajo creen que la compuerta existe**. La disciplina de alcance subió la mortalidad de títulos nuevos de 33 % a 55,6 % y su autocertificación es falsa: dice diez títulos, son nueve, y cuatro sobreviven |
| **15** | 2026-08-28 | 1,5 | 3,0 | 1,5 | 1,73 | **7,73** | **Segunda regresión de la serie, −0,02, con ocho de nueve bloques cerrados enteros.** El pliego afirmaba que su bloque 1 cruzaba el gate solo; se aplicó mejor de lo pedido —`RF-180` partido en cuatro— y **D3 no se movió**. El dictamen del agregador vale más que el puntaje: *«una corrección deducida de un informe corrige el informe, no la dimensión»*. La otra mitad de la seguridad llevaba **quince rondas abierta**: `RF-01` exige documento para recibir el efectivo y `RF-85`/`RF-86` para cobrarlo, **y para devolverlo no exige nada** — ocho títulos producen devoluciones que se pagan en efectivo en un mostrador sin compuerta, y la superficie remota del emisor tampoco la tiene. La encontraron Rosa y Kevin por separado. D2 **sube por primera vez en cuatro rondas** (50,2 %) porque la disciplina de alcance mató seis de siete títulos nuevos, y su autocertificación es verdadera |
| **16** | 2026-08-28 | 1,5 | 3,0 | 1,5 | 1,70 | **7,70** | **Las seis compuertas del dinero que sale se escribieron, cubren más de lo pedido, y D3 no subió** — segunda confirmación consecutiva de que *«una corrección deducida de un informe corrige el informe, no la dimensión»*, y el agregador **deja de publicar escenarios**. El medio punto de D3 se mueve de *quién* a *cuánto*: `RF-194` repone «por el monto que el receptor declaró», nada lo acota ni lo produce, y `RF-168` guarda la evidencia firmada sin que ningún título obligue a leerla. Lo reportaron dos personas y **Elena contra su propio interés**. `n = 13` con **cinco clases en cero**, incluida *decisión sin requerimiento* por primera vez, y la integridad de identificadores verificada: cada número de 1 a 213 está exactamente una vez, vivo o declarado muerto. El hallazgo más viejo: `insumos.md` lleva **dieciséis rondas** en la numeración de la ronda 01, contradiciendo al documento que lo cita |

**Gate ≥ 8. Mejor resultado: 7,75 (iteración 14). Última medición: 7,70 (iteración 16).** El detalle de cada corrida está en
[`../evals/iterations/`](../evals/iterations/) y el resumen en
[`../evals/HISTORY.md`](../evals/HISTORY.md).

---

## Cómo se registra una iteración del diseño

1. **Qué ítem del backlog no explicaba el diagrama anterior.** Ese es el motivo, y es el único
   motivo válido. Un componente que aparece sin un ítem que lo pida es un huérfano, y el
   [agregador](../evals/README.md) lo cobra.
2. **Qué se abrió.** Qué caja de la pasada anterior dejó de ser una caja.
3. **Qué ítems quedan `DONE`** al cerrar la pasada.
4. **Qué quedó sin cubrir**, que es lo que va a forzar la siguiente.

## Cómo se registra una iteración del EVAL

Una iteración es una pasada que **cambia una decisión**, no una corrección de redacción. Se abre
cuando algo obliga a volver atrás: el EVAL quedó bajo el gate, una estimación no cierra contra los
requerimientos, el modelo de datos no soporta un flujo, o una persona no puede completar su día.

1. **Qué la forzó** — el hallazgo concreto, con su origen (una deducción del agregador, el veredicto
   de una persona, una contradicción entre dos pasos).
2. **Qué paso se corrigió** y qué decisión reemplazó a cuál.
3. **La propagación** — qué pasos aguas abajo quedaron afirmando lo viejo. Este es el punto:
   corregir `R` sin volver a mirar `E`, `D`, `A` y `L` deja el diseño incoherente, y el defecto
   reaparece dos iteraciones después disfrazado de otra cosa.
4. **El puntaje** de esa ronda.

---

## La propagación, que es el defecto que hay que vigilar

En el proyecto hermano ([Caso #2](https://github.com/LuisMUtec/SWA-LAB02-Lease)), nueve rondas de
evaluación encontraron que el modo de falla dominante **no era la sustancia sino la propagación**:
se enmendaba un requisito y quedaban la decisión que lo generó, la entidad, el flujo o el criterio
afirmando lo viejo. Tres rondas seguidas encontraron la misma forma con distinto disfraz.

En R.E.D.A.L.E. pega más fuerte, porque los pasos están encadenados por construcción: una
estimación se calcula **contra** unos requerimientos, un modelo de datos se arma **para** un
servicio diseñado, y un diagrama dibuja **lo que** el modelo de datos sostiene. Tocar `R` invalida
aguas abajo, siempre.

Las cuatro variantes que el Caso #2 encontró, que acá se buscan **por nombre**:

| Variante | En qué consiste | Cómo se cierra |
|---|---|---|
| **Cifra sin productor** | Un requisito se apoya en un número que nada produce | Dándole un productor a la cifra, nunca reescribiendo el criterio que la usa |
| **Acto sin consumidor** | Algo se puede registrar, guardar y recuperar, y no le llega a nadie ni puede responderse | Dándole un destinatario y un cierre |
| **Reparación en la altitud equivocada** | Se corrige el ítem y no la decisión que lo generó, que sigue diciendo lo contrario | Subiendo la corrección al documento que gobierna |
| **Estado sin terminador** | Algo se abre y nada lo cierra — acá, típicamente: una retención | Dándole un plazo que se vence solo |

---

## Lo que estas diecisiete rondas enseñaron

El defecto dominante **no fue la sustancia sino la propagación**, y mutó de forma cada ronda:

| Ronda | La forma que tomó |
|---|---|
| **02** | Entró el ítem visible y **no la decisión que lo gobernaba** |
| **03** | Entró la decisión y **no se barrió lo que la contradecía** |
| **04** | **Entra la corrección y trae consigo un defecto de la clase que vino a corregir** |
| **05** | La misma, atenuada: cuatro instancias sobre veintiocho hallazgos |

### El error de método que más caro salió

Al partir y limpiar el backlog **reusé identificadores en vez de retirarlos**. `RF-02` dejó de ser
«rechazar el efectivo antes de identificar» y pasó a ser «entregar en efectivo sin cuenta bancaria»;
`RF-12` dejó de ser la prohibición del canal y pasó a ser el desafío; `RF-14`, `RF-37` y `RF-58`
cambiaron igual.

Ahorró cuatro ítems en el documento puntuado y **movió el defecto de la contradicción explícita —que
se ve— a la deriva semántica silenciosa, que no se ve porque la cita sigue resolviendo.** Siete
lugares en cuatro pasos siguieron leyendo `RF-02` con su significado viejo, y **ningún `grep` lo
delata**: el puntero apunta a un ítem que existe y dice otra cosa.

**Los `BR-nn` de [`business-rules.md`](../business-rules.md) no cometen ese error: su catálogo
declara que no se renumeran ni se reutilizan.** El backlog debería haber hecho lo mismo.
