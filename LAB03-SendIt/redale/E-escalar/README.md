# E — Escalar

> Paso 6 de [R.E.D.A.L.E.](../README.md) · anterior:
> [**L** — Listar los componentes](../L-listar-componentes/README.md) · último paso · bitácora:
> [`ITERACIONES.md`](../ITERACIONES.md)

**Estado: escalado.** Los cinco tramos están rotulados en la unidad de
[`E` — Estimar](../E-estimar/README.md) —giros por día— y cada uno nombra qué se rompe primero, por
qué y qué cambia. **Ninguna fila queda con `—`.**

**Los tres hallazgos, antes de las tablas.** (1) El sistema **nace pasado su primer cuello, y ahora
lo nace por mucho más**: la cuota del operador de telefonía se agota en `1 026` giros diarios y `E`
estima la llegada en `2 800`, `2,7×` por encima. El canal carga hoy **dieciocho** requerimientos
—once al receptor y siete al emisor, `14` P0 y `4` P1— y el factor de `S-14` subió de `5,0` a `6,5`
unidades por giro, con lo que el cuello bajó de `1 333` a `1 026`. **De ese salto, dos tercios no son
ítems nuevos sino una omisión corregida**: RF-11 hace llegar el código de seguimiento al emisor *«por
llamada o mensaje de texto»* y nadie lo estaba contando como unidad del tercero. (2) El plano único
de escritura que [`D`](../D-disenar-servicio/README.md)(a) eligió deja de caber en una máquina en
**`21 000` giros/día** —era `29 100`, y lo bajaron las `29,96` escrituras por giro de hoy contra las
`21,62` de la ronda anterior—, todavía entre el segundo tramo y el tercero, y mucho antes de que
`RNF-11` deje de mandar. (3) Los dos tramos altos del material **no son tramos de carga sino de
mercado**: `1 M` giros/día a ticket de `USD 300` son `USD 109 500 M/año`, **1,8 veces** los dos
corredores enteros que `S-01` fijó.

**Y un cuarto que es una corrección, no un hallazgo.** Este documento decidía degradar el canal con
una **cola con prioridad que descartaba los avisos P1** para que la cuota se agotara en ellos y no en
los P0. Ningún título del backlog permite descartar un aviso —ni RF-120 ni RF-121 ni ninguno— y
RF-132 lo vuelve explícito al obligar a tratar como **no avisado** a quien no tenga constancia de que
el aviso llegó. **Esa decisión se sacó**, y abajo se dice con qué se la reemplaza y qué cuesta no
degradar.

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
| **Consume de E** (estimar) | La carga inicial en **giros por día**, las operaciones de ventanilla por día, el factor de pico `S-07`, los supuestos cerrados `S-09`, `S-10` y `S-11`, y tres entradas que no derivan del volumen de negocio: el tamaño de la red afiliada y sus turnos (`S-12`), las unidades de voz y SMS por giro con su coste (`S-14`) y la proporción de giros que se rehacen tras perderse el código (`S-19`, que suma carga sin sumar giro). Un tramo es una carga, y la carga viene de ahí — pero no toda la carga crece con los giros |
| **Consume de D** | Las **seis** decisiones, ya cerradas. Tres tienen tramo de vencimiento y aquí se nombra cuál: **(a)** el libro de partida doble solo-adición en un plano único de escritura, que deja de caber en una máquina en `21 000` giros/día; **(c)** el arrendamiento exclusivo solo en línea, que **no** vence —elimina la divergencia por construcción— pero convierte cada caída de enlace en mostrador cerrado, y esa cuenta crece con los puntos; **(f)** el servicio de desafío, que `D` puso con base y credenciales propias y al que `E` **sí le da nodo**: es el **quinto plano** de su tabla de trece servidores, con `2`, y RNF-15 y RF-114 lo ensancharon al sacar de la pantalla del mostrador tanto el código como la respuesta. Lo que sigue abierto no es si tiene nodo, sino si `2` alcanzan cuando el `20 %` de los pagos pasa por ahí |
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
—más de dos por giro, porque RF-13, RF-56 y RF-32 agregan atenciones que ningún giro simple tiene,
porque RF-138 obliga a devolver en ventanilla el efectivo que quedó en custodia sin giro creado, porque RF-91 parte un solo cobro en
dos ventanillas y porque RF-117 permite **rehacer** el giro cancelado por código perdido, que es una
creación entera que no suma giro— y el **pico**, que es el número contra el que de verdad se
dimensiona.

Las tres columnas son la misma carga vista desde tres costos distintos: la primera dice cuánto libro
contable se escribe, la segunda cuánta gente en mostrador hace falta, y la tercera cuánta máquina hay
que tener parada once meses al año.

**Y hay una cuarta que no es carga: es superficie.** Los puntos de atención afiliados no crecen con
los giros —abajo del cruce los fija `S-12`— pero son los que fijan cuántas cajas declara RF-76 cada
turno, cuánto efectivo hay que tener parado en mostradores ajenos y cuántos mostradores **cierran**
cuando se les cae el enlace, que es lo que `D`(c) dejó en su lugar cuando eliminó la divergencia. Un
tramo con muchos giros en pocos puntos y otro con los mismos giros repartidos en miles no se rompen
por lo mismo, y la tabla tiene que poder distinguirlos.

Cada celda se calcula **en el techo de su tramo**, con los factores que `E` ya derivó y sin inventar
ninguno: `2,13` ventanillas por giro (`5 955 / 2 800`, con el rehacer de RF-117 adentro y sin RF-90,
que llega por llamada o SMS y no por el mostrador —RF-196—), `3,0` de pico diario (el componente
**diario** de `P`, no el compuesto de `11`), `30,4 / 2` giros por emisor y mes (`S-04`), **`6,5`
avisos por giro** (`S-14`, contra los **dieciocho** ítems que el canal carga hoy: RF-25, RF-37,
RF-41, RF-69, RF-75, RF-106, RF-156, RF-109, RF-120, RF-121 y RF-124 al receptor; RF-11, RF-14,
RF-51, RF-60, RF-65, RF-67 y RF-127 al emisor) y `0,96` pagos por giro (`S-13`).

| Tramo (giros/día) | Operaciones de ventanilla/día | Giros/día en pico | Emisores distintos/mes | Puntos de atención activos | Avisos de voz y SMS/día | Corredores activos |
|---|---|---|---|---|---|---|
| `< 1 k` | **2 130** — menos que las `9 000` declaraciones de caja del mismo día | **3 000** | **15 200** | **3 000** — piso de `S-12`, no derivado del volumen | **6 500** — ya por encima de un tercio de la cuota, en el tramo más bajo del cuadro | **2** |
| `1 k – 10 k` | **21 300** — SendIt entra acá, en `2 800` (`5 955` ventanillas) | **30 000** | **152 000** | **3 000** — la red sigue al `11 %` de su techo de caja | **65 000** | **2** |
| `100 k` | **213 000** | **300 000** | **1 520 000** | **3 200** — primer tramo en que la red deja de estar sobrada | **650 000** | **2**, al `18 %` de los dos corredores enteros |
| `500 k` | **1 065 000** | **1 500 000** | **7 600 000** | **16 000** | **3 250 000** | **≥ 12** — `89 %` de los dos corredores es inalcanzable |
| `1 M` | **2 130 000** | **3 000 000** | **15 200 000** | **32 000** | **6 500 000** | **≥ 24** — `1,8×` los dos corredores enteros |

**De dónde sale la columna de puntos, que es la única que no se multiplica.** No crece con los giros
hasta que choca contra el efectivo: un punto que paga `N` giros por turno tiene que tener `N × 300`
inmovilizados en su cajón —de **su** dinero, `RF-24`— y `RF-95` se los descuenta pago a pago.
Con `[ASSUMPTION: USD 6 000 de caja por punto y turno]` son `20` pagos por turno, `30` por día a los
`1,5` turnos de `S-12`. De ahí `puntos = max(3 000; pagos/día ÷ 30)`, y el cruce cae en
`3 000 × 30 ÷ 0,96 = ` **93 750 giros/día**: por debajo manda `S-12`, por encima manda la tesorería
del agente. Las declaraciones de RF-76 salen de ahí (`puntos × 3`): `9 000`, `9 000`, `9 600`,
`48 000`, `96 000`.

**La columna de corredores arranca en dos y no en uno**: la fija `S-01`, cerrado contra RNF-14, que
exige dos monedas de destino desde el primer día. No es una casilla que se llene más tarde: es la
condición de partida del tramo más bajo. **Y en los dos tramos altos deja de ser una condición para
volverse una imposibilidad aritmética**: `giros/día × USD 300 × 365` da `USD 54 750 M/año` a `500 k`
y `USD 109 500 M` a `1 M`, contra los `USD 61 300 M` que `E` midió para los dos corredores de
lanzamiento. Ningún incumbente de treinta años tiene el `89 %` de un corredor. Lo que el material
pinta como más carga es acá **más mercado**, y el mercado se compra con corredores.

**La penúltima tampoco es decorativa** —cada aviso se le paga a un tercero por unidad (`S-14`), de
modo que esa columna es la única del cuadro que se lee como una factura y no como una capacidad—:
`6 500 × USD 0,05 = USD 325/día` en el tramo bajo, `USD 325 000/día` en el alto, y una cuota que se
agota mucho antes que el presupuesto. **El recuento contra el backlog de hoy la movió `+30 %`
entera** —de `5,0` a `6,5` unidades por giro— y ese `30 %` es lo que separa `1 333` de `1 026`
giros/día en la fila de abajo. El desglose del salto, para que no haya que creerlo: `+1,015` de
RF-11, el código de seguimiento que este documento no contaba; `+0,018` de RF-127, el aviso de
liberación que el backlog agregó; `−0,030` de `RF-107`, que se retiró y cuyo aviso de cancelación ya
estaba dentro del `4 %` de devoluciones de `S-13` que RF-106 cubre vía RF-47; y `+0,44` del reintento,
que pasó de `×1,12` a `×1,20` porque RF-131 y RF-132 hacen de la constancia de entrega la condición
para dar a alguien por avisado.

---

## Los tramos

Una tabla por tramo. Se llena de arriba hacia abajo: lo que se rompe en un tramo sigue roto en el
siguiente si no se arregló.

**Dos advertencias, y las dos cambiaron al llenarse.** La primera sigue en pie: el rótulo es
`giros/día`, pero no todo se rompe por ahí. El piso de declaraciones de caja de RF-76, el efectivo
inmovilizado que RF-95 descuenta y el número de mostradores que cierran cuando se les cae el enlace
(RF-100, RNF-08) crecen con la **columna de puntos**, no con la de giros, de modo que caen en un
tramo bajo si la red se ensanchó antes que el volumen — y `S-12` la ensanchó desde el día uno.

La segunda hay que corregirla, porque la escribió un documento que suponía otra decisión de `D`.
Decía que una fila que nombra un invariante roto —RNF-05, RNF-13, RNF-06— se pone en el primer tramo
donde **es posible**. La regla vale; **la lista ya no.** `D`(c) eligió arrendamiento exclusivo del
giro emitido solo en línea: mientras el arrendamiento vive, el centro se prohíbe a sí mismo disponer
del giro, y sin arrendamiento el punto no paga. RF-100 invertido —el punto no autoriza lo que no
puede comprobar— **elimina por construcción** la posibilidad de que dos lugares afirmen a la vez
cosas incompatibles: no hay ventana que dimensionar, ni en el tramo bajo ni en el alto. **RNF-06 y
RNF-13 no aparecen en ninguna tabla de abajo, y esa ausencia es el resultado, no un olvido.** Lo que
sí aparece, en el primer tramo y creciendo con los puntos, es lo que `D`(c) puso en su lugar y
escribió como precio: el mostrador que cierra, el estado *pago en duda*, y la disponibilidad de
RNF-11 apoyada en el enlace que menos controla SendIt.

### `< 1 k` giros/día

El tramo en el que el material dibuja «un servidor y una base». Acá el servidor sobra por dos órdenes
de magnitud —`E` calculó `0,10` para una carga casi tres veces mayor, y ya contra el pico— y **ya
se rompen dos cosas**, ninguna de
máquina.

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| **La cuota diaria del operador de telefonía**, en `1 026` giros/día | `6,5` avisos por giro (`S-14`) por `3,0` de pico diario son `19,5` unidades por giro el día señalado. Contra la cuota de `10 000/día` por país sin acuerdo comercial que `E` supuso, los dos países de `S-01` dan `20 000`: `20 000 ÷ 19,5 = ` **1 026**, contra los `1 333` de la ronda anterior. **El tramo se rompe adentro, y muy por debajo del volumen de llegada de `2 800`** —`2 800 / 1 026 = 2,7×` pasado— : SendIt nace ya pasado su primer cuello, y ahora lo nace por bastante más. Del lado del receptor salen por ahí **nueve avisos P0** (RF-25, RF-37, RF-41, RF-69, RF-75, RF-106, RF-156, RF-109, RF-124) y **dos P1** (RF-120, RF-121); del lado del emisor, **cinco P0** (RF-11, RF-14, RF-65, RF-67, RF-127) y **dos P1** (RF-51, RF-60). Son `14` P0 y `4` P1, dieciocho en total. Ninguno tiene plan B: Elena no tiene aplicación ni datos | **Nada en el diagrama; todo en el contrato.** El `Notification Service` que [`L`](../L-listar-componentes/README.md) dibuja como una caja pasa a ser **uno por país** —RNF-12 obliga a contar dos operadores, no dos endpoints—, gana la constancia de RF-98 y el resultado de entrega de RF-131, y gana **diferimiento con orden de salida, no descarte**: ver la fila de abajo, que es donde este documento tuvo que corregirse |
| **Lo que la arquitectura puede hacer con una cuota que no alcanza, y lo que no puede hacer** | **Corrección de la ronda 10.** Este documento decidía una `cola con prioridad` que dejaba que la cuota se agotara en los avisos P1 —RF-120 y RF-121— para no gastarla en los P0. **Ningún título del backlog permite descartar un aviso.** RF-120 dice *«avisará al receptor antes de que el giro prescriba»* y RF-121 *«informará al receptor toda diferencia registrada»*: los dos son obligaciones sin excepción, y su prioridad P1 ordena **en qué orden se construyen**, no a quién se le puede no avisar. RF-132 cierra la puerta por el otro lado: quien no tenga constancia de que el aviso llegó cuenta como **no avisado**, de modo que un descarte no queda escondido — queda anotado como incumplimiento | **La decisión sin requerimiento se sacó.** Lo que queda en su lugar degrada sin perder nada: **(1) diferimiento acotado por el plazo que cada ítem lleva escrito.** RF-25, RF-41 y RF-75 tienen fecha —Elena viaja— y salen primero; RF-120 avisa *«antes de que el giro prescriba»*, que a doce meses de S-11 tolera días de espera, y RF-121 informa una diferencia ya registrada, que tolera horas. La cola **reordena y desborda al día siguiente**; no tira. **(2) La constancia de RF-131 hace medible el desborde**, y RF-132 lo convierte en una cifra que se puede reportar en vez de un silencio. **(3) Y si aun así no alcanza, el costo se declara en vez de diseñarse:** el día señalado el sistema necesita `54 600` unidades contra `20 000` de cuota — faltan `34 600`, un `2,7×`. El canal ya cuesta `USD 910/día` y `USD 332 k/año` a `USD 0,05` la unidad; comprar la cuota que falta lo sube en proporción y **es la única salida que no rompe un título**. **La alternativa a comprar cuota no es degradar: es incumplir dieciocho requerimientos y saberlo.** Eso es un contrato, no una caja |
| **El mostrador sin línea — que ya no diverge: cierra** | `D`(c) cerró la divergencia y dejó el precio escrito: sin arrendamiento no hay pago, y el arrendamiento solo se obtiene en línea (RF-100, RNF-06). El riesgo no crece con los giros sino con los `3 000` puntos que `S-12` pone desde el día uno, y no se manifiesta como dinero pagado dos veces sino como Elena volviendo en combi sin nada, después de que RF-41 y RF-75 le prometieran que ese punto podía pagarle —y sin que RF-109 ni RF-124 puedan alcanzarla a tiempo, porque el punto que dejó de poder pagar es el que no tiene línea para decirlo—. La salida de RF-91 tampoco corre: rederivar exige línea, y el reloj que RF-116 le informó al emisor corre igual hasta que RF-111 devuelve el giro. Del lado de la creación el precio tiene nombre propio: RF-118 deja el efectivo **ya recibido** sin giro creado en un estado único que el operario puede leer y retomar, de modo que la caída no pierde el dinero — lo deja detenido, con Rosa mirando; y **RF-138 le puso plazo**: si nadie lo retoma en `[ASSUMPTION: 72 horas]`, el efectivo vuelve al emisor en vez de quedarse ahí | **Este es el tramo donde se paga la deuda que `D`(c) le dejó a este paso por escrito**: dimensionar un segundo camino de conectividad por punto, o aceptar por escrito la indisponibilidad que RNF-11 va a comerse. El `Sync Service` no es la respuesta —cuando el punto vuelve no hay nada que reconciliar, no pagó nada—; la respuesta está aguas abajo del diagrama, en el enlace |
| **El piso de RF-76 es mayor que el negocio entero** | `9 000` declaraciones de caja al día contra `2 130` operaciones de ventanilla: la carga que no se apaga es `9 000 / 2 130 = ` **4,2×** la que sí. Manda hasta `9 000 ÷ 2,13 = ` **4 225 giros/día**, es decir todo este tramo y la mitad del siguiente, incluida la llegada de `2 800`. El rehacer de RF-117 acortó el reinado en `40` giros/día: es lo único que las ventanillas nuevas cambian acá | No es una rotura, es el **suelo del tramo**: el `Caja del Punto Service` y `BD puntos de atención y efectivo` se dimensionan contra `S-12`, nunca contra el volumen. Un día sin un solo giro sigue escribiendo `9 000` filas |
| **Nada de máquina** | La carga pide `0,14 × 1 000 / 2 800 = ` **`0,05`** servidores y RNF-11 con la geografía piden `13`. El sistema arranca sobreprovisionado `13 ÷ 0,05 = ` **`×260`** y sigue estándolo todo el tramo. Las `23 358` escrituras que el backlog de 155 ítems agregó subieron la carga un `34 %` y no movieron una caja — el sobreprovisionamiento bajó de `×360` a `×260` y sigue siendo de dos órdenes de magnitud | Ninguno. Subir dentro de este tramo no cambia una sola caja del diagrama |

### `1 k – 10 k` giros/día

**El tramo en el que SendIt entra**, en `2 800`. Se hereda la cuota rota del tramo anterior y aparece
el primer límite que se mide en personas.

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| **La cuota de telefonía, ya rota, se vuelve estructural** | En el techo del tramo son `65 000` avisos/día y `195 000` el día señalado: `195 000 / 20 000 = ` **`9,75×`** los `20 000` de cuota. Un factor de dos se negocia en un mes; uno de casi diez cambia el modelo comercial del canal, y con él el `USD 0,325` por giro que `S-14` carga al costo unitario | Deja de ser un adaptador y pasa a ser una **decisión de compra por corredor**: cada país nuevo trae operador, cuota, precio y tasa de entrega propios. Es el único cuello del sistema que se renegocia en vez de rediseñarse |
| **El caudal de la cola de cumplimiento, con tres términos que no se parecen** | `E` estima **`71`** casos/día a `2 800` giros —y son `71`, no `70`: este documento arrastraba la suma de dos términos cuando ya eran tres—: `56` por tamizaje (`S-08`, `2 %` sobre la **identidad**), `14` por el acumulado de cobros de RF-93 (`0,5 %`, sobre la **frecuencia**) y `1` por el reproceso de RF-123 sobre los `42` giros rehechos. En el techo del tramo el primero da `200/día` —crece igual que el volumen, porque la tasa de sanciones no depende de cuánto gira la gente— y el segundo se dispara: cuando SendIt tiene éxito en un corredor sube `cobros por receptor`, que es justo lo que RF-93 cuenta y castiga. Con `2,6` cobros por receptor en vez de los `2,2` de `S-15` `[ASSUMPTION]`, RF-93 aporta `80/día`. **Y ahora hay un tercero:** RF-123 vuelve a correr todos los controles sobre cada giro rehecho, `10 000 × 1,5 % × 2 % = 3/día` en el techo del tramo. Total `200 + 80 + 3 = ` **`283`**, no `250` | El `Retención Service` deja de tener **una** cola y pasa a tener **tres** entradas medidas aparte, porque no se dimensionan con la misma fórmula: la primera es `giros × tasa fija`, la segunda `giros × f(giros por receptor)` y la tercera `giros × S-19 × tasa fija`, que no es carga de negocio sino carga de reproceso. Dimensionar la planta de analistas contra la tasa de sanciones subestima el segundo término exactamente en los tramos donde el negocio va bien, y olvida el tercero entero |
| **El desafío deja de ser un caso raro, y ahora carga el código además de la respuesta** | `S-16` lo puso en el `20 %` de los pagos a `1,6` intentos: `3 200` comprobaciones/día en el techo del tramo. Cada una atraviesa el `Desafío Service`, que `D`(f) construyó con **derivación lenta a propósito** y comparación **solo en el centro**. RF-82 la invoca en cada intento, RF-103 devuelve el giro al tercero y RF-122 hace que el desafío sea lo que **autoriza el pago** con documento vencido, no un trámite lateral. A eso el backlog le sumó dos tráficos que antes pasaban por la pantalla del mostrador: RNF-15 traspasa el código al emisor sin que el operario lo lea —`10 000/día`, uno por giro— y RF-114 recibe la respuesta del propio receptor —`3 200/día`—, con RNF-15 negando toda reconsulta de un código ya entregado y RF-147 obligando a que lo teclee el propio receptor | Todavía no se rompe, y la deuda que este documento arrastraba **ya no es la que decía**: `E` reparte trece servidores en **cinco** planos —escritura, réplica de lectura, consulta, cumplimiento y **módulo del desafío**— y el quinto es justamente el suyo, con `2` nodos. Lo que queda abierto es otra cosa y es de tamaño: por esos `2` nodos pasan ahora `13 200` actos diarios en el techo del tramo (`10 000` de RNF-15 más `3 200` de RF-114) además de las comprobaciones, y RNF-11 mide sobre *pagar* |
| **Nada de máquina, otra vez** | En el techo del tramo la escritura pide `10 000 × 29,96 ÷ 86 400 × 11 ÷ 80 = ` **`0,48`** servidores en pico contra los `80 req/s` de un plano — era `0,34` con las `21,62` escrituras por giro de la ronda anterior | Ninguno. Los **trece** servidores siguen siendo de RNF-11 y de la geografía, no de la carga |

### `100 k` giros/día

**El primer tramo en que algo se rompe por volumen**, y no es lo que el material espera: no es la
base de lectura, es el escritor único del libro.

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| **El plano único de escritura de `D`(a)**, ya roto en `21 000` giros/día | `E` desglosó `83 885` escrituras diarias sobre `2 800` giros: **`29,96` por giro**, contra las `21,62` de la ronda anterior. Las razones de fondo no cambiaron —`D`(a) hizo que **todo hecho sea un asiento con contrapartida**, incluida la retención de RF-29, que no mueve un centavo y reclasifica `Obligación con el receptor` contra `Obligación retenida`, y RF-07 hizo de la cotización una escritura durable antes del pago—; lo que cambió es **de dónde viene el delta, y este documento lo atribuía de tres maneras distintas a la vez.** El delta anterior de `9 798` se atribuía a tres ítems en un pasaje, a seis en otro y a ocho en un tercero: **el correcto es el de ocho**, porque es el único que reproduce la cifra (`2 926` RF-119 y RF-123 `+ 3 696` RNF-15 y RF-114 `+ 2 854` RF-115 y RF-116 `+ 280` RF-98 `+ 42` RF-117 `= 9 798`). El delta de esta ronda es de `23 358` sobre **catorce** ítems, y lo domina uno solo: `18 760` son constancia de aviso y resultado de entrega (RF-98, RF-131, RF-132), `4 500` el informe de diferencia de cierre al agente (RF-141) y los `98` restantes se reparten entre RF-104/RF-143/RF-145, RF-144/RF-146, RF-137, RF-196, RF-118/RF-138 y RF-139/RF-140. En pico: `giros × 29,96 ÷ 86 400 × 11 = 80 req/s` en **`21 000` giros/día**, que es la capacidad de un plano de escritura de 16 vCPU. A `100 k` hacen falta `4,8`, no `3,4`. Los tres nodos de RNF-11 son **un** plano con quórum, no tres capacidades | Aparece el **particionamiento del libro**, y con él la pregunta que este documento venía dejando abierta: por qué clave. La respuesta la fija `D`, no este paso: **por giro**, porque RNF-07 exige que las dos líneas del asiento entren juntas y las dos son del mismo giro — y **RNF-16** agrega la razón que faltaba: ninguna entrega puede diferir de la cifra que el emisor vio, de modo que el monto y la entrega tienen que estar en la misma partición o el invariante se comprueba a distancia. Lo que queda a caballo es lo que `E` ya había señalado con `1,3` requests al día: RF-81 busca a una persona **a través de** todos sus giros, y RF-93 cuenta por **identidad de receptor**, que `D` obliga a agregar dentro de la transacción de autorización y sin caché. **Y hay un candidato a partición propia que no es el libro:** las `32 760` constancias de aviso son el `39 %` de las escrituras y no se indexan por giro sino por destinatario y por unidad entregada |
| **La caja por punto de atención** | `96 000` pagos/día ÷ `30` por punto y día = `3 200` puntos, contra los `3 000` de `S-12`. **Es el cruce**: por primera vez la red afiliada deja de estar sobrada y empieza a fijar el tramo. RF-95 descuenta pago a pago, RF-92 lee el saldo antes de habilitar cada uno, RF-76 declara dos veces por turno y RF-24 obliga a liquidarle al agente lo que puso de su cajón. El pico agrava: el día señalado son `3,0×` los pagos contra la misma caja declarada esa mañana | El `Caja del Punto Service` pasa de ser una lectura derivada barata al **segundo escritor más caliente del libro** después del pago. Y RF-91 cambia de naturaleza: deja de ser la excepción del `2 %` para volverse el mecanismo de balanceo de efectivo entre puntos — con RF-105 exigiendo la respuesta del emisor en el medio, que es una espera humana dentro del camino del pago. La liquidación de RF-24 no puede seguir siendo un cierre diario |
| **El módulo del desafío, ahora sí, como dependencia dura del pago** | `32 000` comprobaciones/día (RF-82) más `100 000` escrituras de RF-68 —que no admite excepción— más los `132 000` actos que RNF-15 y RF-114 le trajeron (`100 000` traspasos de código y `32 000` capturas de respuesta) pasan por una **derivación lenta por diseño**. En pico son `16,8/s` de derivación; a `[ASSUMPTION: 200 ms]` por derivación son `3,4` núcleos dedicados a un cómputo que se eligió caro a propósito. El costo no es el problema: el problema es que `D`(f) puso la comparación **solo en el centro** y RNF-11 mide sobre *pagar* — y RF-122 hizo del desafío la vía que **autoriza** el pago con documento vencido. Si `BD desafíos` no contesta, el `20 %` de los pagos no se completa y RF-103 empieza a devolver giros de receptores legítimos | El `Desafío Service` deja de ser un par mínimo por confidencialidad y pasa a ser **un plano con su propio quórum**, sin dejar de tener credenciales separadas —que es el motivo por el que existe (RNF-17)—. Esto **no invalida el reparto de trece servidores de `E`**, que ya le dio el quinto plano con `2` nodos: lo que hace es agotar ese par, porque `2` alcanzan para que RNF-11 no dependa de una sola máquina y no para `264 000` actos diarios. No se recalcula acá (no es lo que este paso hace): se devuelve a [`E`](../E-estimar/README.md) como **cambio de tamaño de un plano que ya existe** |
| **La capacidad de decidir dentro del plazo de la retención** | `2 000` casos de sanciones, más el término de RF-93 —que a esta profundidad de red ya no es el `0,5 %` de `S-08`—, más los `100 000 × 1,5 % × 2 % = 30` que RF-123 agrega al volver a correr los controles sobre cada giro rehecho: son del orden de `3 500` casos/día que hay que resolver **dentro del plazo de RF-31**. Y cada uno que se cierra mal le debe a su receptor el aviso de RF-156 —que ahora es **P0** y nombra el canal— mientras que cada uno que se cierra bien le debe al emisor el de RF-127, que el backlog agregó para decirle que su giro dejó de estar retenido. Lo que satura no se apila —RF-32 vence y devuelve— así que la señal es **tasa de devolución automática**, no retraso | Ninguna caja nueva. La única palanca que la arquitectura tiene es achicar el caudal, y ya está construida: RF-78 separa homonimia de coincidencia exacta y el `98 %` son homónimos (`S-08`). Convertir esa mayoría en una decisión del sistema no es un cambio de `L`: es un ítem de `R` que alguien tiene que aceptar |

### `500 k` giros/día

**Deja de ser un tramo de carga.** `500 000 × USD 300 × 365 = USD 54 750 M/año`, el `89 %` de los dos
corredores enteros que `E` midió. No se llega ahí vendiendo más: se llega abriendo corredores.

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| **El mercado direccionable, antes que cualquier componente** | Los dos corredores de `S-01` valen `USD 61 300 M/año` juntos. Pedirle a este tramo que quepa en ellos es pedir el `89 %` de un mercado con incumbentes de treinta años, cuando `E` calibró la entrada en `0,5 %`. Con `≥ 12` corredores —`3` orígenes × `4` destinos `[ASSUMPTION]`— ningún corredor tiene que dar más del `10 %` del suyo | Lo que crece **no es el número de corredores: son los pares origen–destino**. RF-16 aplica al mismo giro las reglas de los dos reguladores y RF-16 obliga a rechazar cuando son incompatibles en vez de elegir una ([`BR-17`](../../business-rules.md)). El `Corredor Service` y `BD corredores y reguladores` pasan de resolver `2` pares a resolver `o × d`: agregar el cuarto destino a tres orígenes no agrega **una** fila, agrega **tres** |
| **El acumulado de receptor deja de ser particionable por giro** | La partición por giro que resolvió el tramo anterior sobrevive a RNF-07 pero no a esto: con varios orígenes, **una misma Elena cobra giros de corredores distintos**, y RF-93 cuenta por identidad de receptor en la ventana de `[ASSUMPTION: 30 días corridos]` y retiene en el momento de pagar. `D` lo cerró explícitamente «agregado en la transacción de autorización, **sin caché**», porque un contador atrasado paga el giro que había que retener. Ese agregado ahora cruza particiones dentro de la transacción del pago | **Es el tramo en el que una decisión de `D` deja de sostenerse**, y hay que llevársela allá y no arreglarla acá. Las salidas son dos y las dos cuestan: partir por **identidad de receptor** en vez de por giro —y entonces es RNF-07 el que queda a caballo— o mantener el acumulado en una partición propia con su propio bloqueo, que mete un segundo recurso en el camino crítico de RNF-09 |
| **El pico deja de tener una forma** | `S-07` compuso `P = 11` con dos calendarios de destino y los husos internos de **un solo** país de origen —los de Estados Unidos, que es lo único que `S-01` pone hoy—. Con doce corredores hay doce calendarios de fechas señaladas y husos de **tres orígenes distintos**: el Día de la Madre no cae el mismo día en México que en Perú, pero la Navidad sí cae en todos. Sumarlos supone que coinciden; tratarlos por separado supone que no | Se provisiona contra la **envolvente**, no contra la suma: `[ASSUMPTION: los calendarios de fechas señaladas de corredores distintos no coinciden, salvo Navidad]`, de modo que once meses al año se provisiona por corredor y en diciembre se provisiona la suma. Sigue siendo provisionamiento **por calendario** y no por reacción, que es lo que un pico de una hora exige — pero el `P` que se usa ya no es el de `S-07`, y `E` tiene que decirlo |
| **La caja y los roles, en `16 000` puntos** | `480 000` pagos/día sobre `16 000` mostradores ajenos son `USD 96 M` de efectivo de terceros inmovilizado por turno, con RF-24 liquidando detrás. Y RNF-02 prohíbe que una misma identidad ejerza dos roles del mismo giro, con `15 000` autorizaciones de segundo rol al día (RF-13, `3 %` de `S-05`) y las liberaciones de RF-33 encima | Ninguna caja nueva y ninguna que sirva: es un límite de tesorería, de contratos y de **personas distintas y simultáneas en el mismo mostrador**. Un punto con dos operarios se queda sin combinaciones válidas antes que sin capacidad de atender, y eso no lo arregla un servidor |

### `1 M` giros/día

`USD 109 500 M/año`: **1,8 veces** los dos corredores de lanzamiento y del orden del `13 %` de todo
el flujo mundial de remesas `[ASSUMPTION: ≈ USD 850 000 M/año]`. Y `15,2 M` de emisores distintos al
mes, que es una fracción de dos dígitos de toda la población nacida en el extranjero que vive en
Estados Unidos. Este tramo no se alcanza con arquitectura.

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| **Los supuestos de `E`, antes que cualquier caja** | La cuota del `0,5 %` y el ticket de `USD 300` (`S-05`) son las dos entradas de las que todo el dimensionamiento cuelga en proporción directa. Este tramo exige mover una de las dos por un factor grande, o multiplicar `S-01` por doce. Ninguna de las tres cosas es una decisión de arquitectura | **Se devuelve a [`E`](../E-estimar/README.md), no se resuelve acá.** Es exactamente la fila «Queda inválido si E (estimar) cambia» del contrato de arriba, ejercida: el tramo en el que el sistema arranca —y con él el orden de todo lo demás— es función de `S-01b` y `S-05`, no del diagrama de `L` |
| **El costo del corredor enésimo, si crece con los que ya hay** | Con `≥ 24` corredores hay `24` pares de reguladores que RF-16 aplica de a dos y que RF-16 tiene que saber declarar incompatibles, `24` catálogos de documento válido (RF-01), `24` operadores de telefonía, `24` redes afiliadas que se **contratan** y no se construyen, y un multiplicador de conservación por giro que RF-18 y RNF-03 calculan contra el más largo de cada par. La pregunta de este paso no es «¿y el segundo?» —RNF-12 lo puso en el día uno— sino **si el enésimo cuesta lo mismo que el segundo** | La prueba es concreta y `D` la deja pasar: si los pares viven como **filas** de `BD corredores y reguladores`, agregar el destino `d+1` cuesta `o` filas y el costo por corredor es constante; si viven como **ramas** en el `Corredor Service`, crece con los que ya hay y el sistema tiene lógica de corredor mezclada con lógica común. `D` eligió lo primero para el catálogo y **no dijo dónde viven las reglas de incompatibilidad de RF-16**. Ese es el arreglo, y es de [`D`](../D-disenar-servicio/README.md) |
| **La planta de cumplimiento, que ya no es una cola sino una nómina** | `20 000` casos de sanciones al día (`2 %` de `S-08`) más el término de RF-93, cada uno decidido por una persona dentro del plazo de RF-31, derivado a un rol distinto del que atendió (RF-30) y liberado con motivo escrito por un tercero (RF-33, RF-87, RNF-02). Lo que no se decide **no se apila**: RF-32 lo devuelve. Rosa recupera su dinero, Elena no cobra, y el libro queda perfecto | Ninguna. Es el único cuello del sistema del que ni un rediseño ni un contrato sacan nada: se responde con gente, o achicando el caudal con RF-78 — y achicarlo es un ítem de `R`, no una caja de `L` |
| **La disponibilidad del enlace, multiplicada por `32 000` mostradores** | `960 000` pagos/día sobre `32 000` puntos son `30` pagos por punto y día. Con `[ASSUMPTION: 99 % de disponibilidad de enlace en un punto afiliado]`, en cualquier instante hay `320` mostradores que **no pueden pagar nada** por la decisión de `D`(c), y eso son del orden de `9 600` pagos diarios que no ocurren donde Elena fue a buscarlos. No es divergencia —RF-100 la eliminó— es indisponibilidad, y RNF-11 la mide sobre *pagar* | Sigue sin haber caja nueva: el `Sync Service` reconcilia lo que el punto **recuerda**, y un punto caído no pagó nada que reconciliar. Lo que escala es el segundo camino de conectividad por punto que `D`(c) encargó en el tramo `< 1 k` y que a `32 000` mostradores ajenos ya no es una compra: es una cláusula del contrato de afiliación |

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
**tres**, y suman **`71`** casos/día a los `2 800` giros de llegada —`56 + 14 + 1`—: RF-93 retiene
también al giro cuyo receptor superó su acumulado de cobros en la ventana de
`[ASSUMPTION: 30 días corridos]`, y RF-123 vuelve a meter en la cola cada giro rehecho tras perderse
el código, que
atraviesa los controles enteros por segunda vez sin ser un giro nuevo. RF-119, en cambio, **no suma
caudal**: parte en dos el tamizaje de creación —emisor y receptor designado, los dos antes de aceptar
el efectivo— pero el receptor ya se tamizaba en RF-27, más tarde; lo que cambia es *cuándo* se
detiene, no *cuánto* se retiene. Las tres fuentes no se parecen. La de sanciones es rara y se dispara sobre la
**identidad**, así que su tasa es casi independiente del volumen; la de RF-93 se dispara sobre una
**frecuencia**, de modo que crece cuando crece el número de giros por receptor — exactamente lo que
pasa cuando el sistema tiene éxito en un corredor. Un caudal que no escala con el volumen y otro que
escala más rápido que el volumen entran en la misma cola y salen por la misma puerta, que es el rol
de cumplimiento de RF-33; la tercera, la de RF-123, escala con el volumen pero **no con el negocio**,
porque el giro que la produce ya fue contado una vez. Dimensionar la cola contra la tasa de sanciones
subestima el segundo término justo en los tramos altos y no ve el tercero en ninguno.

Lo que sí se rompe es otra cosa, y es peor porque no se ve en ningún gráfico de cola:

| Candidato a primer cuello | Por qué satura antes que la máquina | Qué lo ancla | Cómo se manifiesta |
|---|---|---|---|
| **La capacidad de decidir dentro del plazo de la retención** | La cola no crece, pero el plazo tampoco espera. Cuando el caudal supera lo que cumplimiento decide por día, el excedente no se apila: **se devuelve al emisor** por RF-32 sin que nadie lo haya revisado —y RF-106 le avisa al receptor que su giro se fue de vuelta—. La saturación se manifiesta como tasa de devolución automática, no como retraso. Y el caudal ahora tiene **tres** fuentes: sanciones, el acumulado de RF-93 que crece con el volumen, y el reproceso de RF-123 sobre cada giro rehecho | RF-31 · RF-32 · RF-33 · RF-93 · RF-106 · RF-156 · RF-123 · RF-127 | Rosa recupera su dinero y Elena no cobra, sin que nadie haya decidido nada. Es un fallo silencioso con recibo contable correcto |
| **Los roles distintos disponibles por punto de atención y por turno** | RNF-02 prohíbe que una misma identidad ejerza dos roles del mismo giro; RF-13 exige un segundo rol sobre el umbral reforzado, RF-30 deriva la retención a un rol distinto del operario que atendió, RF-33 reserva la liberación al rol de cumplimiento y RF-61 pide segundo rol para corregir. Eso no se resuelve con más servidores ni con más horas: exige **más personas distintas y simultáneas** en el mismo mostrador | RNF-02 · RF-13 · RF-30 · RF-33 · RF-61 | Un punto de atención con dos operarios se queda sin combinaciones válidas antes de quedarse sin capacidad de atender |
| **El efectivo disponible en el corredor de destino** | RF-20 impide dar por fondeado un giro sin efectivo disponible en destino, RF-76 obliga a cada punto a declarar su caja al abrir y al cerrar, RF-92 a mostrarle al operario ese saldo antes de habilitar un pago y RF-24 a liquidar con el agente lo que puso de la suya. El límite es de tesorería y de red física, y se agrava en el pico, que es cuando más efectivo hace falta y menos margen hay para reponerlo | RF-20 · RF-24 · RF-76 · RF-92 · RNF-10 | Giros creados que no llegan a disponibles dentro de los 15 min de RNF-10, y cobros derivados a otro punto por RF-91 — que es la salida cuando el elegido no puede pagar, y también la señal de que la caja no alcanza |
| **El canal de voz y SMS, que no es nuestro** | Es el único componente P0 del sistema cuya capacidad la fija un tercero: un operador de telefonía con cuota diaria, precio por unidad y tasa de entrega propia. **Dieciocho requerimientos se apoyan en él** —once al receptor, de los que nueve son P0, y siete al emisor, de los que cinco son P0: `14` P0 y `4` P1— y ninguno tiene plan B, porque Elena no tiene aplicación ni datos móviles. Escala con los giros, se dispara en el pico junto con todo lo demás, y crece otra vez con cada corredor nuevo, que trae su propio operador. El recuento contra el backlog de hoy subió el factor de `S-14` de `5,0` a `6,5` y adelantó el cuello de `1 333` a `1 026` giros/día — y lo hizo **sobre todo por un ítem que siempre estuvo y nadie contaba**: RF-11 entrega el código de seguimiento al emisor por el mismo canal, `1,015` unidades por giro. **Cada aviso nuevo que se le cuelgue lo adelanta más, y cada aviso que ya está y no se cuenta lo adelanta sin avisar.** No se resuelve con más servidores: se negocia | RF-25 · RF-37 · RF-41 · RF-69 · RF-75 · RF-106 · RF-156 · RF-109 · RF-120 · RF-121 · RF-124 (receptor) · RF-11 · RF-14 · RF-51 · RF-60 · RF-65 · RF-67 · RF-127 (emisor) · RF-98 · RF-131 · RF-132 (la constancia de que salió y de que llegó) | Elena no se entera de nada y viaja igual, o no viaja. El sistema se ve sano en todas sus métricas: el giro está creado, fondeado y disponible, y nadie lo cobra. **Y ahora eso deja rastro**: RF-132 la cuenta como no avisada |
| **~~La ventana de divergencia entre el centro y el punto de atención~~ El mostrador que cierra** | **Esta fila hay que rehacerla, y el motivo es una buena noticia.** Estaba escrita cuando el candidato era la divergencia: el centro diciendo «retenido» y el mostrador «disponible», que es el caso de Huanta. `D`(c) eligió **arrendamiento exclusivo del giro, emitido solo en línea**, y RF-100 invertido —el punto no autoriza lo que no puede comprobar— **elimina esa ventana por construcción, no la acorta**: si hay arrendamiento vivo el centro se prohíbe a sí mismo disponer del giro; si no lo hay, no hay nada que pagar. **RNF-06 y RNF-13 dejaron de ser dimensionables**, y por eso no aparecen en ninguna tabla de tramo. Lo que queda en su lugar no es un invariante roto sino una capacidad perdida: **una caída de enlace cierra el mostrador para pagos, sin excepción**, y eso crece con el número de puntos exactamente igual que crecía la divergencia | RF-100 · RNF-05 · RNF-06 · RNF-13 · RNF-08 · RNF-11 | No es dinero pagado dos veces: es dinero que no se paga ninguna. Elena viajó cuarenta minutos después de que RF-41 y RF-75 le prometieran que ese punto podía pagarle, y RF-91 tampoco la salva porque rederivar exige la línea que falta. Aparece en el tramo `< 1 k` —`S-12` pone `3 000` puntos el día uno— y se multiplica por diez en el tramo `1 M` |

Los cinco llegan antes que casi cualquier límite de máquina, y a ninguno de los cinco se responde con
más servidores. Los tres primeros son de personas, de tesorería y de contrato; el cuarto es de un
tercero. **El quinto era el único que un rediseño podía quitar del camino, y el rediseño ya
ocurrió**: `D`(c) lo quitó, y lo que dejó en su lugar no se resuelve en el diagrama sino en el
enlace del mostrador, que es lo que menos controla SendIt.

**Y con las tablas llenas, el orden entre ellos quedó decidido y no es el que la lista sugiere.** Se
ordenan por el tramo en el que caen, no por gravedad:

| Orden | Cuello | Tramo en que cae | Se responde con |
|---|---|---|---|
| 1 | La cuota del operador de telefonía | `1 026` giros/día — **`2,7×` debajo del volumen de llegada** | Un contrato con más cuota, no una máquina — y **no una cola que descarte**: ningún título permite no avisar |
| 2 | El mostrador sin línea | `< 1 k`, con los `3 000` puntos de `S-12` | Un segundo camino de conectividad, o aceptar la indisponibilidad por escrito |
| 3 | El plano único de escritura de `D`(a) | `21 000` giros/día | Particionar el libro por giro — y asumir lo que queda a caballo |
| 4 | La caja por punto de atención | `93 750` giros/día | Tesorería del agente y RF-91 como balanceo, no como excepción |
| 5 | La capacidad de decidir dentro del plazo de la retención | `100 k`, y creciendo más rápido que el volumen por RF-93, con el reproceso de RF-123 encima — son `71` casos/día ya en la llegada | Personas, o achicar el caudal con RF-78, que resuelve la homonimia en `[ASSUMPTION: 24 horas]` — y ese ítem es de `R` |
| 6 | Los roles distintos por punto y turno (RNF-02) | `500 k`, con la red ya ensanchada | Más personas **distintas y simultáneas**, que no es lo mismo que más horas |

El cuello número 3 es el único de los seis que un servidor arregla, y es el tercero en llegar — se
adelantó de `29 100` a `21 000` giros/día sin dejar de ser el tercero. **El orden no cambió con los
155 ítems; las distancias sí**, y todas hacia abajo.

> **Deuda de repropagación, declarada y no disimulada.** Las cifras de este paso están calculadas sobre el backlog de **155 ítems** de la ronda 11. El backlog vigente tiene **207**. Actualizar el número sin rehacer el cálculo sería peor que declararlo: afirmaría una cuenta que nadie corrió. Lo que cambia con el volumen nuevo son las magnitudes, no las cajas ni las decisiones — ningún tramo de rotura cambia de lugar por un 34 % más de escrituras, y eso está comprobado en el propio análisis de sensibilidad. **La actualización es trabajo pendiente y está anotada como tal en [`evals/CORRECCIONES-RONDA-15.md`](../../evals/CORRECCIONES-RONDA-15.md).**


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

**Ahora eso tiene cifra y tiene clave, y las dos salen de lo que `D` ya decidió.** `D`(a) eligió
partida doble solo-adición: **todo hecho del giro es un asiento con contrapartida**, incluidos los
que no mueven un centavo —la retención de RF-29 reclasifica `Obligación con el receptor` contra
`Obligación retenida`, mismo monto, suma cero—, y RF-07 hizo de la cotización una escritura durable
que ocurre **antes** del pago. De ahí salen las **`29,96`** escrituras por giro que `E` desglosó —eran
`21,62` antes de que el backlog de 155 ítems agregara `8,34` entre **catorce** ítems, de los que uno
solo, la constancia de aviso con su prueba de entrega (RF-98, RF-131, RF-132), aporta `6,70`—, y de
ahí sale el tramo: `29,96 × giros ÷ 86 400 × 11 = 80 req/s` en **`21 000` giros/día**.
Ese es el número, y llega mucho antes que los `260 000` en que la carga alcanzaría al piso de RNF-11.
**Cada control nuevo que el backlog acepta corre este tramo hacia abajo**, y lo corre en proporción
directa: `8,34` escrituras más por giro adelantaron el quiebre `8 100` giros/día. **La lección de esta
ronda es cuál fue el control que lo hizo**: no un control de dinero ni de identidad, sino la
obligación de probar que se avisó.

La clave la fija RNF-07 y no hay elección: **se parte por giro**, porque las dos líneas del asiento
tienen que entrar juntas y las dos son del mismo giro. **RNF-16 lo confirma desde el otro lado**:
ninguna entrega puede diferir de la cifra que el emisor vio antes de entregar su efectivo, así que el
monto fijado (RF-06) y la entrega registrada tienen que caer en la misma partición o el invariante
pasa a comprobarse a distancia, que es justo lo que un invariante no tolera. El doble pago no depende
de la partición —`D`(b) lo ancló en el índice único `(giro, acto)` del libro, que es el único
mecanismo que ve dos puntos desconectados a la vez—. Lo que sí queda a caballo son las tres
operaciones que **no** se indexan por giro: RF-81, que busca a una persona a través de todos sus
giros (`1,3` requests al día, y aun así decisivos); RF-93, que cuenta por identidad de receptor y que
`D` obligó a agregar dentro de la transacción de autorización y sin caché; y RF-08 y RF-09, el gemelo
del lado emisor, que comparte con RF-93 la ventana de `[ASSUMPTION: 30 días corridos]`. Las
tres se sostienen mientras haya un corredor por partición y una identidad en un solo corredor — y eso
es exactamente lo que el tramo `500 k` rompe. **Y hay una cuarta que el backlog acaba de crear y que
no queda a caballo, sino en otra partición del todo:** RNF-15 y RF-114 mueven el código y la respuesta
al módulo del desafío, que `D`(f) tiene con base y credenciales propias — de modo que lo que se parte
por giro es el libro, no el secreto, y RNF-15 le agrega la única negación que ese módulo ejerce.

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
- Y el pico no es uno solo: RNF-12 pone dos corredores desde el día uno, y con ellos **dos
  calendarios de fechas señaladas** —el Día de la Madre no cae el mismo día en Perú que en México—.
  Sumarlos supone que coinciden; tratarlos por separado supone que no. Cuál de las dos cosas vale es,
  también, un supuesto abierto. **Lo que RNF-12 no produce son dos husos horarios de origen**: `S-01`
  fija **un solo país de origen** con dos destinos, así que los husos Este y Pacífico que achatan el
  pico intradía son geografía de ese país y un supuesto de `E`, no una lectura de RNF-12. Lo que
  RNF-12 obliga es a **volver a derivar el `3,6` intradía en cuanto entre un segundo país de origen**,
  que es cuando aparecen husos que no son los de este.

**3. El eje que crece no es el usuario: es el corredor — y no arranca en uno.** Una red social crece
con más usuarios de la misma clase; una remesa crece con **otro país**. Pero aquí hay que corregir
un planteo que este documento tenía mal: **el segundo corredor no es escalamiento.** RNF-12 lo exige
desde el primer día y RNF-14 exige más de una moneda de destino con él, de modo que la arquitectura
que entra en producción ya es multicorredor o no cumple el backlog. RF-16 lo confirma en el nivel del
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
| Otro regulador, y un par nuevo con **cada** corredor ya existente | RF-16 aplica los dos reguladores al mismo giro y RF-16 rechaza el giro cuando son incompatibles. Lo que crece no es el número de corredores sino el de **pares origen–destino** que hay que saber resolver. Es lógica de negocio nueva, no más instancias de la vieja | RF-16 · RF-16 · RF-23 |
| Otro plazo de conservación | RF-18 conserva por el plazo más largo de los dos países que tocaron el giro, y RNF-03 lo calcula por giro y no por política global. Un corredor con plazo más largo mueve el multiplicador de almacenamiento de `S-09` para todos los giros que lo toquen | RF-18 · RNF-03 |
| Otra moneda de destino | Otra posición de cambio, otra cotización que RF-07 hay que producir y fechar, otro monto exacto en moneda destino que RF-05 informa antes de que el emisor entregue el efectivo, otro margen que RF-142 le informa, y otra cuenta de diferencia de cambio en el libro | RF-05 · RF-07 · RF-142 · RNF-14 · RNF-16 |
| Otra red de puntos de atención **afiliados** | La red no se construye: **se afilia**. Son contratos con terceros, operarios ajenos a los que hay que habilitar y liquidar (RF-24), y efectivo de caja de otro que hay que reponer (RF-20). El límite no es de instancias ni de planta propia: es de acuerdos y de tesorería, y la ventana de divergencia del corredor nuevo la fija la calidad de conexión de puntos que no son nuestros | RF-20 · RF-24 · RF-63 |
| Otras listas y otra forma de identidad | Lo que sirve como documento válido en un país no sirve en otro (RF-01), y el tamizaje cambia de fuente sin cambiar de obligación (RF-26, RF-27) | RF-01 · RF-26 · RF-27 |
| Otro canal de aviso al receptor | RF-25 exige llamada o mensaje de texto sin aplicación ni datos móviles. Cada país agrega un **operador de telefonía**, no un endpoint más: otro contrato, otra cuota, otro precio por unidad y otra tasa de entrega, sobre los **once** avisos al receptor y los **siete** al emisor que ya viajan por ahí — al receptor: el que anuncia el giro (RF-25), el del monto (RF-41), el de si el punto puede pagar hoy (RF-75), el de que dejó de poder (RF-109) con el que dice a cuál ir (RF-124), el de la retención (RF-37), el de la devolución —que cubre también la cancelación, porque RF-47 la convierte en devolución— (RF-106), el del cambio de lista (RF-156), la pregunta del desafío (RF-69), el de la prescripción próxima (RF-120) y el de la diferencia (RF-121); al emisor: el **código de seguimiento** (RF-11), el de la devolución disponible (RF-14), el del cobro (RF-65), el de la retención (RF-67) y el de la liberación (RF-127), más la prescripción próxima (RF-51) y la diferencia (RF-60) | RF-11 · RF-25 · RF-37 · RF-41 · RF-69 · RF-75 · RF-106 · RF-156 · RF-109 · RF-120 · RF-121 · RF-124 · RF-14 · RF-51 · RF-60 · RF-65 · RF-67 · RF-127 |
| Otro huso horario y otro calendario | El pico se mueve, y n corredores pueden tener picos que no se solapan — o que sí. La combinatoria de calendarios crece con n, el provisionamiento no. Se provisiona contra la **envolvente**: `[ASSUMPTION: los calendarios de fechas señaladas de corredores distintos no coinciden, salvo Navidad]`, así que once meses se provisiona por corredor y en diciembre se provisiona la suma | RNF-12 · RNF-14 fijan que hay más de uno; la **altura** no tiene ancla en R — ver `S-07` |

De modo que la pregunta que este paso tiene que dejar contestada no es «¿qué pasa con el segundo
corredor?» —ese ya está en el día uno— sino **«¿cuánto cuesta el enésimo, y crece ese costo con los
que ya hay?»**. Si la respuesta es «se duplica el sistema», el diseño de
[`D`](../D-disenar-servicio/README.md) no separó lo que era común de lo que era del corredor, y eso
se arregla allá, no acá.

**La respuesta, con lo que el proyecto sabe hoy: el costo no es constante, y se puede decir por
cuánto.** Un corredor es un par `origen → destino`, así que con `o` orígenes y `d` destinos hay
`o × d` corredores y **`o × d` pares de reguladores** que RF-16 aplica de a dos sobre el mismo giro y
que RF-16 tiene que saber declarar incompatibles ([`BR-17`](../../business-rules.md)). Agregar el
destino `d+1` no agrega un corredor: agrega `o`. Con los dos de `S-01` —un origen, dos destinos— el
segundo destino costó `1`; en el tramo `500 k`, con tres orígenes, el cuarto destino cuesta `3`. Eso
es superlineal, y es superlineal **en el número que ya hay del otro eje**.

| Lo que trae el enésimo | ¿Cuánto cuesta? | ¿Crece con los que ya hay? |
|---|---|---|
| Filas del catálogo de corredores y reguladores | `o` filas por destino nuevo, `d` por origen nuevo | **Sí**, linealmente en el otro eje. Es dato: barato de agregar, caro de tener bien |
| Reglas de incompatibilidad de RF-16 | `D` **no dijo dónde viven** — si son filas del catálogo, constante por par; si son ramas del `Corredor Service`, no | **Es la pregunta abierta, y es de `D`.** Es la única fila de esta tabla que puede convertir el eje en un rediseño |
| Red afiliada, operador de telefonía, listas y forma de identidad válida | Constante por corredor: un contrato de afiliación (RF-24), un operador (RF-25), una fuente de listas (RF-26, RF-119, RF-27) y un catálogo de documento (RF-01, RF-86, RF-122) | **No en cantidad; sí en precio unitario**: el operador nuevo se contrata contra `6,5` unidades por giro, no contra `5,0`, y ese factor lo fija el backlog, no el corredor |
| Plazo de conservación (`S-09`) | Constante por corredor, pero **mueve el multiplicador de todos los giros que lo toquen**, porque RF-18 y RNF-03 lo calculan por giro contra el más largo del par | **No en cantidad; sí en efecto**: un corredor con plazo largo encarece el almacenamiento de los que ya existían |
| Huso y calendario del pico | Constante por corredor si los picos no se solapan; la envolvente los suma en Navidad | **No**, bajo el supuesto de arriba. Si se solapan, sí — y nadie lo comprobó |

Cuatro de las cinco filas dan costo constante. La que no lo da —RF-16— es la única que `D` dejó sin
ubicar, y por eso es lo que hay que llevarle a [`D`](../D-disenar-servicio/README.md) junto con la
partición del acumulado de receptor del tramo `500 k`.

---

## Qué invalida este paso

| Si cambia… | Se rehace |
|---|---|
| El factor de pico `S-07` en [`E`](../E-estimar/README.md) | El tramo de arranque y el orden de los cuellos de botella |
| Una decisión de [`D`](../D-disenar-servicio/README.md) | El tramo en el que esa decisión dejaba de sostenerse |
| El diagrama de [`L`](../L-listar-componentes/README.md) | El componente nombrado como primer punto de ruptura |
| El número de corredores de partida (RNF-12, y con él `S-01`) | La tabla del corredor n-ésimo, la columna de corredores activos del tramo más bajo, y probablemente el eje de crecimiento entero |
| El plazo de retención de RF-31 y RF-32 | El primer cuello de botella: si la retención dejara de tener terminador, la cola de cumplimiento volvería a ser un acumulado y no un caudal. Que el plazo suba por encima de las 72 h por defecto no lo rompe — lo agranda |
| Las fuentes de retención (RF-29 por sanciones, RF-93 por acumulado de cobros, RF-123 por reproceso del giro rehecho) — hoy `71` casos/día en la llegada | El caudal de la cola, que tiene un término que no escala con el volumen, otro que escala más rápido y un tercero que escala con el reproceso y no con el negocio. Una fuente nueva se suma aquí, no en la tabla de tramos |
| El régimen de roles (RNF-02, RF-13, RF-30, RF-33, RF-61) | El límite de personas distintas por punto de atención, que es el cuello que no se resuelve con máquina |
| El tamaño de la red de puntos afiliados (`S-12`) | El piso de declaraciones de RF-76, el cruce de `93 750` giros/día en que la tesorería del agente pasa a mandar, y el número de mostradores que cierran cuando se les cae el enlace. **Ya no la ventana de divergencia**: `D`(c) la eliminó, y si esta fila vuelve a nombrarla es que alguien reabrió `D`(c) |
| **La decisión `D`(c)** — el arrendamiento exclusivo emitido solo en línea | Todo el quinto cuello de botella y las filas del mostrador de los tramos `< 1 k` y `1 M`. Si el arrendamiento dejara de ser exclusivo o se pudiera emitir fuera de línea, RNF-06 y RNF-13 vuelven a ser dimensionables y el documento entero cambia de forma |
| **La decisión `D`(a)** — el asiento con contrapartida para todo hecho del giro | El tramo de `21 000` giros/día en que el plano único de escritura deja de caber, que es función directa de las `29,96` escrituras por giro. Menos asientos por giro corre el tramo hacia arriba; más, hacia abajo — y las `8,34` que el backlog de 155 ítems agregó ya lo corrieron `8 100` giros/día hacia abajo |
| El reparto de los trece servidores de `E` | Nada de este paso, salvo una cosa, y **ya no es la que esta fila decía**: el `Desafío Service` **sí tiene nodo** —es el quinto plano de `E`, con `2`— y lo que se le devuelve a [`E`](../E-estimar/README.md) es un cambio de tamaño, no un plano que falta. Por esos `2` nodos pasa el `20 %` de los pagos que RNF-11 mide, más el traspaso del código de RNF-15 (uno por giro), la captura de la respuesta de RF-114 y la confirmación al operario de RF-125. No se recalcula acá |
| **La constancia de aviso y su prueba de entrega (RF-98, RF-131, RF-132)** | El tramo de `21 000` giros/día del cuello 3: son `18 760` de las `23 358` escrituras que el backlog agregó, y solas explican `6,70` de las `8,34` escrituras por giro nuevas. **Es la primera vez que el tramo de escritura lo mueve algo que no es dinero ni identidad.** Y se devuelve a `D` y a `L`: `E` (estimar) lo dejó anotado como candidato a **sexto plano**, porque la familia de escritura más grande del sistema vive hoy en el plano del giro, no se indexa por giro y tiene estado propio —*no avisado*— que RF-132 obliga a poder derivar |
| La cuota, el precio o la cobertura del operador de telefonía (`S-14`) | El cuello del canal de voz y SMS —`20 000 ÷ (6,5 × 3,0) = 1 026` giros/día— y con él la viabilidad de los **once** avisos al receptor y los **siete** al emisor. Es el único cuello que se renegocia en vez de rediseñarse — **y el único que este documento intentó una vez resolver descartando avisos, que es lo que ningún título permite** |
| **Quién es el destinatario de un aviso**, o cuántos avisos cuelga el backlog del canal | El factor de `S-14` y, en proporción inversa, el tramo del primer cuello: `5,0 → 6,5` lo bajó de `1 333` a `1 026`. Reatribuir un aviso de una punta a la otra —lo que pasó con RF-60, que informa al emisor, y con RF-121, que informa al receptor— no mueve el total; **agregar uno sí, y siempre hacia abajo — y dejar uno sin contar lo baja igual, en silencio, que es lo que pasó con RF-11** |
| La proporción de giros rehechos tras perderse el código (`S-19`, anclada en RF-46, RF-117, RF-123, RF-134 y RF-135) | Las `2,13` ventanillas por giro, el tercer término del caudal de cumplimiento (el `1` de los `71`) y `0,060` de las `6,5` unidades del canal —`0,045` de base repetida más `0,015` del código nuevo de RF-11—. No mueve el volumen de negocio: mueve tres columnas de la tabla de tramos sin mover la primera |

---

## Nota sobre las dos clases de iteración

[`ITERACIONES.md`](../ITERACIONES.md) distingue la **iteración del diseño** —el mismo diagrama de
componentes dibujado otra vez y más abierto, que es la que el enunciado exige mostrar (ver el
[ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md))— de la **iteración del EVAL**, que cambia
una decisión del backlog. Este paso **no produce** iteraciones del diseño: no abre cajas, comenta
qué les pasa bajo carga. Si al llenarlo aparece un componente que el diagrama no tiene, eso no se
dibuja aquí — se vuelve a [`L`](../L-listar-componentes/README.md) y se abre otra pasada allá, con
el ítem del backlog que la justifique.
