# E — Escalar

> Paso 6 de [R.E.D.A.L.E.](../README.md) · anterior:
> [**L** — Listar los componentes](../L-listar-componentes/README.md) · último paso · bitácora:
> [`ITERACIONES.md`](../ITERACIONES.md)

**Estado: andamiaje.** Las tablas por tramo están vacías.

---

## Por qué este paso existe, si el material dice que no

Hay una tensión y conviene reconocerla antes que esquivarla. El material del curso lista el paso
como *«E - scalar ( esto no lo usaremos aun )»*. Pero el enunciado del Caso #3 pide **todos los
entregables del framework R.E.D.A.L.E.**, y los dos ejemplos completos del propio material —X
(*former Twitter*) y Paper.ly— **sí recorren el paso 6**: ambos terminan en una lámina `6. S(cale)`.

**Decisión tomada: se incluye, acotado** —registrada como
[D-03](../../docs/DECISIONES.md#d-03--se-incluye-el-segundo-paso-e-escalar-acotado)—. Acotado
quiere decir esto:

| Sí hace | No hace |
|---|---|
| Nombrar qué se rompe primero en cada tramo de carga y por qué | Recalcular el dimensionamiento — eso es [`E` — Estimar](../E-estimar/README.md) |
| Decir qué cambia en la arquitectura al pasar de un tramo al siguiente | Elegir productos, proveedores ni topología de despliegue |
| Marcar en qué tramo una decisión de [`D`](../D-disenar-servicio/README.md) deja de sostenerse | Rediseñar el sistema para el tramo más alto desde el principio |

La última columna importa: el material presenta los tramos como una **secuencia**, no como un
objetivo. Diseñar hoy para el millón de giros diarios es el error que el paso previene, no el que
recomienda.

**Con una excepción que RNF-12 y RNF-14 imponen y que hay que decir aquí, no al final:** la
multiplicidad de corredores **no es un tramo**. Los dos corredores del lanzamiento son Estados
Unidos → Perú y Estados Unidos → México: un solo país de origen y **dos monedas de destino**. Cada
RNF cobra en un plano distinto, y conviene no confundirlos. RNF-14 se satisface en la carga —hay dos
monedas de llegada en producción desde el día uno, y ninguna cifra puede suponer una— mientras que
RNF-12 se satisface en el código: su invariante no pide dos orígenes en el catálogo, pide que
**ninguna cifra ni regla suponga uno solo**. Un sistema que hoy tiene un origen y mañana no puede
agregar otro sin reescribirse ya está incumpliendo, aunque su tabla de corredores se vea bien. Lo
que en otro proyecto sería el primer salto de escalamiento, aquí es la línea de partida: este paso
no puede diferirlo, y tampoco puede contarlo como logro.

---

## Contrato con los pasos vecinos

| | |
|---|---|
| **Consume de L** | El diagrama base de la última iteración. Sin él no hay sobre qué preguntar qué se rompe primero |
| **Consume de E** (estimar) | La carga inicial en **giros por día**, las operaciones de ventanilla por día, el factor de pico `S-07`, los supuestos cerrados `S-09`, `S-10` y `S-11`, y dos entradas que no derivan del volumen: el tamaño de la red afiliada y sus turnos (`S-12`) y las unidades de voz y SMS por giro con su coste (`S-14`). Un tramo es una carga, y la carga viene de ahí — pero no toda la carga crece con los giros |
| **Consume de D** | Las cinco decisiones. Varias tienen un tramo en el que dejan de funcionar: la divergencia entre el centro y los puntos de atención, revisada a mano una por una, se rompe mucho antes que la base de datos |
| **Entrega a** | Nadie. Es el último paso, y por eso es el único que puede quedar sin cerrar sin invalidar a otro |
| **Queda inválido si L cambia** | El componente que se nombró como primer cuello de botella, si dejó de existir o cambió de lugar |
| **Queda inválido si E (estimar) cambia** | El tramo en el que el sistema arranca, y con él el orden de todo lo demás |

---

## Contra qué se cuenta un tramo

El material rotula sus tramos en **usuarios registrados**. Esa unidad no existe en este modelo:
RF-01 identifica al emisor presencialmente contra un documento vigente cada vez que crea un giro, y
no hay cuenta, padrón ni sesión que contar. Un tramo de SendIt se rotula en **giros por día**, que
es la unidad de carga que [`E` — Estimar](../E-estimar/README.md) produce, y se lee junto a dos
columnas derivadas que no crecen con el mismo factor: las **operaciones de ventanilla por día**
—más de dos por giro, porque RF-13, RF-56 y RF-32 agregan atenciones que ningún giro simple tiene, y
porque RF-90 le da al receptor un acto propio en el mostrador y RF-91 parte un solo cobro en dos
ventanillas— y el **pico**, que es el número contra el que de verdad se dimensiona.

Las tres columnas son la misma carga vista desde tres costos distintos: la primera dice cuánto libro
contable se escribe, la segunda cuánta gente en mostrador hace falta, y la tercera cuánta máquina hay
que tener parada once meses al año.

**Y hay una cuarta que no es carga: es superficie.** Los puntos de atención afiliados no crecen con
los giros —los fija `S-12`— pero son los que fijan cuántas cajas declara RF-76 cada turno, cuántos
lugares pueden divergir del centro y cuántos tienen que volver solos después de una caída (RNF-08).
Un tramo con muchos giros en pocos puntos y otro con los mismos giros repartidos en miles no se
rompen por lo mismo, y la tabla tiene que poder distinguirlos.

| Tramo (giros/día) | Operaciones de ventanilla/día | Giros/día en pico | Emisores distintos/mes | Puntos de atención activos | Avisos de voz y SMS/día | Corredores activos |
|---|---|---|---|---|---|---|
| `< 1 k` | — | — | — | — | — | — |
| `1 k – 10 k` | — | — | — | — | — | — |
| `100 k` | — | — | — | — | — | — |
| `500 k` | — | — | — | — | — | — |
| `1 M` | — | — | — | — | — | — |

La última columna arranca en **dos** y no en uno: la fija `S-01`, cerrado contra RNF-14, que exige
dos monedas de destino desde el primer día. No es una casilla que se llene más tarde: es la
condición de partida del tramo más bajo. La penúltima tampoco es decorativa —cada aviso se le paga a
un tercero por unidad (`S-14`), de modo que esa columna es la única del cuadro que se lee como una
factura y no como una capacidad.

---

## Los tramos

Una tabla por tramo. Se llena de arriba hacia abajo: lo que se rompe en un tramo sigue roto en el
siguiente si no se arregló.

**Dos advertencias para quien las llene.** La primera: el rótulo es `giros/día`, pero no todo se
rompe por ahí. La ventana de divergencia entre el centro y los puntos (RNF-06, RNF-13, RF-45,
RNF-08) y el piso de declaraciones de caja de RF-76 crecen con la **columna de puntos**, no con la
de giros, de modo que pueden caer en un tramo bajo si la red se ensanchó antes que el volumen. La
segunda: una fila que nombra un invariante roto —RNF-05, RNF-13, RNF-06— no describe una
degradación, describe dinero perdido; no se pone en el tramo donde empieza a doler sino en el
primero donde **es posible**.

### `< 1 k` giros/día

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| — | — | — |

### `1 k – 10 k` giros/día

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| — | — | — |

### `100 k` giros/día

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| — | — | — |

### `500 k` giros/día

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| — | — | — |

### `1 M` giros/día

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| — | — | — |

### El primer cuello de botella no es técnico, y no es el que parecía

El candidato obvio era la **cola de casos de cumplimiento**: Kevin revisa uno por uno, los giros se
multiplican por diez y la cola crece sin fin. **RF-31 y RF-32 le quitan la premisa.** Toda retención
nace con el plazo del regulador más estricto de los dos países del giro —a falta de norma expresa,
72 h, que es un piso y no un techo— y la que vence sin liberarse se resuelve sola devolviendo el
monto al emisor. La cola no es un acumulado: es un caudal con tiempo de residencia acotado, y su
tamaño en régimen es `giros retenidos por día × plazo de residencia`, una cifra que no diverge por
más que suba el volumen. Que ese plazo se dimensione contra el corredor más estricto y no contra las
72 h por defecto no cambia la forma del problema; cambia su tamaño, y el tamaño se toma de `S-10`,
no de aquí.

**Pero el caudal sí cambió, y por eso el planteo hay que corregirlo.** Cuando esta sección se
escribió, la única fuente de retención era el tamizaje de sanciones (RF-26, RF-27, RF-29). Ahora hay
dos: RF-93 retiene también al giro cuyo receptor superó el acumulado de cobros de la ventana que
RF-58 lleva. Las dos fuentes no se parecen. La de sanciones es rara y se dispara sobre la
**identidad**, así que su tasa es casi independiente del volumen; la de RF-93 se dispara sobre una
**frecuencia**, de modo que crece cuando crece el número de giros por receptor — exactamente lo que
pasa cuando el sistema tiene éxito en un corredor. Un caudal que no escala con el volumen y otro que
escala más rápido que el volumen entran en la misma cola y salen por la misma puerta, que es el rol
de cumplimiento de RF-33. Dimensionar la cola contra la tasa de sanciones subestima el segundo
término justo en los tramos altos.

Lo que sí se rompe es otra cosa, y es peor porque no se ve en ningún gráfico de cola:

| Candidato a primer cuello | Por qué satura antes que la máquina | Qué lo ancla | Cómo se manifiesta |
|---|---|---|---|
| **La capacidad de decidir dentro del plazo de la retención** | La cola no crece, pero el plazo tampoco espera. Cuando el caudal supera lo que cumplimiento decide por día, el excedente no se apila: **se devuelve al emisor** por RF-32 sin que nadie lo haya revisado. La saturación se manifiesta como tasa de devolución automática, no como retraso. Y el caudal ahora tiene dos fuentes, una de las cuales (RF-93) crece con el volumen | RF-31 · RF-32 · RF-33 · RF-58 · RF-93 | Rosa recupera su dinero y Elena no cobra, sin que nadie haya decidido nada. Es un fallo silencioso con recibo contable correcto |
| **Los roles distintos disponibles por punto de atención y por turno** | RNF-02 prohíbe que una misma identidad ejerza dos roles del mismo giro; RF-13 exige un segundo rol sobre el umbral reforzado, RF-30 deriva la retención a un rol distinto del operario que atendió, RF-33 reserva la liberación al rol de cumplimiento y RF-61 pide segundo rol para corregir. Eso no se resuelve con más servidores ni con más horas: exige **más personas distintas y simultáneas** en el mismo mostrador | RNF-02 · RF-13 · RF-30 · RF-33 · RF-61 | Un punto de atención con dos operarios se queda sin combinaciones válidas antes de quedarse sin capacidad de atender |
| **El efectivo disponible en el corredor de destino** | RF-20 impide dar por fondeado un giro sin efectivo disponible en destino, RF-76 obliga a cada punto a declarar su caja al abrir y al cerrar, RF-92 a mostrarle al operario ese saldo antes de habilitar un pago y RF-24 a liquidar con el agente lo que puso de la suya. El límite es de tesorería y de red física, y se agrava en el pico, que es cuando más efectivo hace falta y menos margen hay para reponerlo | RF-20 · RF-24 · RF-76 · RF-92 · RNF-10 | Giros creados que no llegan a disponibles dentro de los 15 min de RNF-10, y cobros derivados a otro punto por RF-91 — que es la salida cuando el elegido no puede pagar, y también la señal de que la caja no alcanza |
| **El canal de voz y SMS, que no es nuestro** | Es el único componente P0 del sistema cuya capacidad la fija un tercero: un operador de telefonía con cuota diaria, precio por unidad y tasa de entrega propia. Cinco requerimientos se apoyan en él —RF-25, RF-37, RF-41 y RF-75, los cuatro P0, y RF-60— y ninguno tiene plan B, porque Elena no tiene aplicación ni datos móviles. Escala con los giros, se dispara en el pico junto con todo lo demás, y crece otra vez con cada corredor nuevo, que trae su propio operador. No se resuelve con más servidores: se negocia | RF-25 · RF-37 · RF-41 · RF-60 · RF-75 | Elena no se entera de nada y viaja igual, o no viaja. El sistema se ve sano en todas sus métricas: el giro está creado, fondeado y disponible, y nadie lo cobra |
| **La ventana de divergencia entre el centro y el punto de atención** | Este es el que rompe un invariante en vez de una capacidad. RNF-06 exige un solo estado entre el centro y el punto; RF-45 impide que un punto sin conexión pague un giro que el centro ya retuvo, canceló o dio por pagado en otro punto; RNF-13 declara imposible que un giro quede devuelto y cobrado a la vez — y esa es justamente la combinación que sale de un punto desconectado pagando un giro que RF-32 ya devolvió al vencer su retención. El riesgo no crece con los giros por día: crece con el **número de puntos** y con la duración de sus desconexiones, y RNF-08 obliga además a que el punto que vuelve reconcilie solo | RNF-06 · RNF-13 · RF-45 · RNF-08 · RF-35 | No se manifiesta como lentitud sino como dinero pagado dos veces: una a Elena en el mostrador, otra a Rosa como devolución. Aparece primero en el tramo donde la red se ensancha, no en el de más volumen |

Los cinco llegan antes que casi cualquier límite de máquina, y a ninguno de los cinco se responde
con más servidores. Los tres primeros son de personas, de tesorería y de contrato; el cuarto es de
un tercero; el quinto es el único que un rediseño puede quitar del camino, y por eso es el que hay
que llevarle a [`D`](../D-disenar-servicio/README.md).

---

## Qué escala distinto en una remesa

Los ejemplos del material escalan redes sociales y un rastreador de páginas. Tres diferencias
cambian qué respuesta sirve.

**1. La carga no es lectura, es escritura contable.** El repertorio habitual —caché, réplicas de
lectura, contenido distribuido en el borde— resuelve el problema de servir muchas veces lo mismo. En
SendIt el trabajo caro es el pago, y una réplica de lectura no acepta un asiento. **Y empieza antes
del pago:** RF-07 hace que cotizar también sea una escritura —el sistema produce y fecha la
cotización, no consulta una ajena— y RF-06 la conserva sin recalcularla, así que el primer acto de
todo giro ya es durable. Peor: los datos que más se consultan son justamente los que no toleran
estar viejos, porque son el monto que RF-06 le prometió a Rosa y el estado de un giro retenido que
RF-66 tiene que mostrarle con su fecha. Cachearlos es servir una mentira reciente, y RNF-06 lo
prohíbe de frente: dos lugares del sistema nunca pueden afirmar a la vez que un giro está retenido y
disponible para cobro. El eje de escalamiento tiene que ser el de escritura, y ese eje se paga con
particionamiento, con lo que trae: decidir por qué clave se parte un libro contable sin que un
asiento quede a caballo entre dos particiones — y sin que la partición abra la puerta al doble pago
que RNF-05 declara imposible.

**2. El pico es estacional, no continuo — y no lo fija ningún RNF.** El volumen se concentra en la
quincena, el fin de mes y unas pocas fechas señaladas. El sistema pasa la mayor parte del año por
debajo de su capacidad y falla los días que a Rosa le importan.

**Antes de provisionar nada hay que decir de dónde sale la cifra, y la respuesta es incómoda:**
ningún requerimiento del backlog fija la altura del pico. RNF-09, RNF-10 y RNF-11 dan umbrales que
hay que cumplir *también* en el pico —3 minutos de ventanilla, 15 minutos hasta disponible, 99,9 %
mensual sobre crear y pagar— pero ninguno dice cuánto es el pico. El multiplicador vive donde tiene
que vivir: en `S-07` de [`E` — Estimar](../E-estimar/README.md), como supuesto abierto y sin ancla
en R. Este paso **no lo inventa**: lo consume marcado como supuesto, y cualquier tramo que se
provisione contra él hereda esa marca. Dicho de otro modo: la estacionalidad está argumentada, su
magnitud no. Dos consecuencias:

- Escalar automáticamente por reacción llega tarde. Un pico que dura horas y se conoce con meses de
  anticipación se atiende **provisionando por calendario**, no esperando a que suba una métrica. Pero
  provisionar por calendario exige saber *cuánto*, y eso es `S-07`, no un RNF.
- El promedio anual es una cifra inútil para dimensionar y una cifra cómoda para reportar. El tramo
  en el que está el sistema es el de su pico, no el de su media.
- Y el pico no es uno solo: RNF-12 pone dos corredores desde el día uno, con dos husos horarios y dos
  calendarios de fechas señaladas. Sumarlos supone que coinciden; tratarlos por separado supone que
  no. Cuál de las dos cosas vale es, también, un supuesto abierto.

**3. El eje que crece no es el usuario: es el corredor — y no arranca en uno.** Una red social crece
con más usuarios de la misma clase; una remesa crece con **otro país**. Pero aquí hay que corregir
un planteo que este documento tenía mal: **el segundo corredor no es escalamiento.** RNF-12 lo exige
desde el primer día y RNF-14 exige más de una moneda de destino con él, de modo que la arquitectura
que entra en producción ya es multicorredor o no cumple el backlog. RF-15 lo confirma en el nivel del
giro: cada uno lleva las reglas de **dos** reguladores a la vez, y RF-16 obliga a rechazarlo cuando
son incompatibles en vez de elegir una. Un diseño que trate el corredor como una configuración
duplicada nace fuera de requisito, no se rompe en un tramo.

Lo que este paso tiene que preguntar, entonces, es lo otro: **qué cuesta el enésimo.** La diferencia
importa porque los dos primeros esconden el problema —dos casos particulares se sostienen a mano— y
el tercero lo revela: si el costo de agregar un corredor es constante, el eje escala; si crece con
los que ya hay, el sistema tiene lógica de corredor mezclada con lógica común y el arreglo está en
[`D`](../D-disenar-servicio/README.md), no acá.

| Lo que trae el corredor n-ésimo | Por qué no es escalar horizontalmente | Requerimiento |
|---|---|---|
| Otro regulador, y un par nuevo con **cada** corredor ya existente | RF-15 aplica los dos reguladores al mismo giro y RF-16 rechaza el giro cuando son incompatibles. Lo que crece no es el número de corredores sino el de **pares origen–destino** que hay que saber resolver. Es lógica de negocio nueva, no más instancias de la vieja | RF-15 · RF-16 · RF-23 |
| Otro plazo de conservación | RF-18 conserva por el plazo más largo de los dos países que tocaron el giro, y RNF-03 lo calcula por giro y no por política global. Un corredor con plazo más largo mueve el multiplicador de almacenamiento de `S-09` para todos los giros que lo toquen | RF-18 · RNF-03 |
| Otra moneda de destino | Otra posición de cambio, otra cotización que RF-07 hay que producir y fechar, otra cuenta de diferencia de cambio en el libro | RF-07 · RNF-14 · RF-21 |
| Otra red de puntos de atención **afiliados** | La red no se construye: **se afilia**. Son contratos con terceros, operarios ajenos a los que hay que habilitar y liquidar (RF-24), y efectivo de caja de otro que hay que reponer (RF-20). El límite no es de instancias ni de planta propia: es de acuerdos y de tesorería, y la ventana de divergencia del corredor nuevo la fija la calidad de conexión de puntos que no son nuestros | RF-20 · RF-24 · RF-63 |
| Otras listas y otra forma de identidad | Lo que sirve como documento válido en un país no sirve en otro (RF-01), y el tamizaje cambia de fuente sin cambiar de obligación (RF-26, RF-27) | RF-01 · RF-26 · RF-27 |
| Otro canal de aviso al receptor | RF-25 exige llamada o mensaje de texto sin aplicación ni datos móviles. Cada país agrega un **operador de telefonía**, no un endpoint más: otro contrato, otra cuota, otro precio por unidad y otra tasa de entrega, sobre los cinco avisos que ya viajan por ahí — el que anuncia el giro (RF-25), el del monto (RF-41), el de si el punto puede pagar hoy (RF-75), el de la retención (RF-37) y el de la diferencia (RF-60) | RF-25 · RF-37 · RF-41 · RF-60 · RF-75 |
| Otro huso horario y otro calendario | El pico se mueve, y n corredores pueden tener picos que no se solapan — o que sí. La combinatoria de calendarios crece con n, el provisionamiento no | — (sin ancla en R; ver `S-07`) |

De modo que la pregunta que este paso tiene que dejar contestada no es «¿qué pasa con el segundo
corredor?» —ese ya está en el día uno— sino **«¿cuánto cuesta el enésimo, y crece ese costo con los
que ya hay?»**. Si la respuesta es «se duplica el sistema», el diseño de
[`D`](../D-disenar-servicio/README.md) no separó lo que era común de lo que era del corredor, y eso
se arregla allá, no acá.

---

## Qué invalida este paso

| Si cambia… | Se rehace |
|---|---|
| El factor de pico `S-07` en [`E`](../E-estimar/README.md) | El tramo de arranque y el orden de los cuellos de botella |
| Una decisión de [`D`](../D-disenar-servicio/README.md) | El tramo en el que esa decisión dejaba de sostenerse |
| El diagrama de [`L`](../L-listar-componentes/README.md) | El componente nombrado como primer punto de ruptura |
| El número de corredores de partida (RNF-12, y con él `S-01`) | La tabla del corredor n-ésimo, la columna de corredores activos del tramo más bajo, y probablemente el eje de crecimiento entero |
| El plazo de retención de RF-31 y RF-32 | El primer cuello de botella: si la retención dejara de tener terminador, la cola de cumplimiento volvería a ser un acumulado y no un caudal. Que el plazo suba por encima de las 72 h por defecto no lo rompe — lo agranda |
| Las fuentes de retención (RF-29 por sanciones, RF-93 por acumulado de cobros) | El caudal de la cola, que tiene un término que no escala con el volumen y otro que sí. Una fuente nueva se suma aquí, no en la tabla de tramos |
| El régimen de roles (RNF-02, RF-13, RF-30, RF-33, RF-61) | El límite de personas distintas por punto de atención, que es el cuello que no se resuelve con máquina |
| El tamaño de la red de puntos afiliados (`S-12`) | La ventana de divergencia de RNF-06 y RNF-13, el alcance de RF-45 y el volumen de reconciliaciones automáticas de RNF-08 — todo lo que crece con puntos y no con giros |
| La cuota, el precio o la cobertura del operador de telefonía (`S-14`) | El cuello del canal de voz y SMS, y con él la viabilidad de los cinco avisos al receptor. Es el único cuello que se renegocia en vez de rediseñarse |

---

## Nota sobre las dos clases de iteración

[`ITERACIONES.md`](../ITERACIONES.md) distingue la **iteración del diseño** —el mismo diagrama de
componentes dibujado otra vez y más abierto, que es la que el enunciado exige mostrar (ver el
[ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md))— de la **iteración del EVAL**, que cambia
una decisión del backlog. Este paso **no produce** iteraciones del diseño: no abre cajas, comenta
qué les pasa bajo carga. Si al llenarlo aparece un componente que el diagrama no tiene, eso no se
dibuja aquí — se vuelve a [`L`](../L-listar-componentes/README.md) y se abre otra pasada allá, con
el ítem del backlog que la justifique.
