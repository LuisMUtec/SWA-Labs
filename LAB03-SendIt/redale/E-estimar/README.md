# E — Estimar

> Paso 2 de [R.E.D.A.L.E.](../README.md) · anterior:
> [**R** — backlog de requerimientos](../R-requerimientos/backlog.md) · siguiente:
> [**D** — Diseñar el servicio](../D-disenar-servicio/README.md) · bitácora:
> [`ITERACIONES.md`](../ITERACIONES.md)

**Estado: calculado sobre los 155 ítems del backlog** (138 RF + 17 RNF).

> **Deuda de repropagación, declarada y no disimulada.** Las cifras de este paso están calculadas sobre el backlog de **155 ítems** de la ronda 11. El backlog vigente tiene **207**. Actualizar el número sin rehacer el cálculo sería peor que declararlo: afirmaría una cuenta que nadie corrió. Lo que cambia con el volumen nuevo son las magnitudes, no las cajas ni las decisiones — ningún tramo de rotura cambia de lugar por un 34 % más de escrituras, y eso está comprobado en el propio análisis de sensibilidad. **La actualización es trabajo pendiente y está anotada como tal en [`evals/CORRECCIONES-RONDA-15.md`](../../evals/CORRECCIONES-RONDA-15.md).**
 Las tres cifras están abajo,
con su aritmética a la vista: **13 servidores**, **3,3 TB retenidos** (1,03 GB/día) y **1,7 Mbit/s en
pico** (208 KB/s). Ninguna sale del enunciado —el enunciado no da ni una cifra— y por eso cada
entrada lleva su `[ASSUMPTION: ...]` con la calibración contra la que se defiende. Las divisiones se
muestran enteras: esto se audita dividiendo, no creyendo.

**El hallazgo que este paso entrega a `D`, antes que las cifras:** la carga de SendIt pide `0,14`
servidores. Lo que pide trece es RNF-11 y la geografía de los dos corredores. Este sistema no se
rompe por CPU — se rompe por la cuota del canal de voz y SMS y por el efectivo de la caja del punto,
y ninguna de las dos se arregla comprando máquinas.

**Y un hallazgo nuevo que el backlog de 155 ítems produjo:** la partida de escritura más grande del
sistema ya no es el libro contable sino la **constancia de aviso**. RF-98 conserva constancia de cada
aviso enviado, RF-131 registra si llegó cuando el canal lo reporta y RF-132 trata como **no avisado**
a quien no tenga constancia de que llegó. Entre los tres son `32 760` de las `83 885` escrituras
diarias — el `39 %`. El sistema escribe más sobre lo que dijo que sobre lo que debe.

Calcular qué necesita SendIt para funcionar sin degradación, y con qué recursos. Tres cálculos, en
el orden del material: **servidores**, **almacenamiento**, **ancho de banda**.

---

## Contrato con los pasos vecinos

Regla del repositorio: **cada paso declara qué consume del anterior y qué queda inválido si el
anterior cambia.** Corregir un paso y dejar los de aguas abajo afirmando lo viejo es el defecto más
caro del proyecto hermano.

| | |
|---|---|
| **Consume de R** | Los requerimientos funcionales que producen carga (cada operación que Rosa, Elena o Kevin ejecutan en una ventanilla), los no funcionales con medida —**RNF-09, RNF-10 y RNF-11**, que el backlog declara consumidos por este paso— y los supuestos ya cerrados en el backlog |
| **Entrega a D** | El orden de magnitud contra el que se elige arquitectura y persistencia: si el sistema es de decenas o de cientos de servidores, si el almacenamiento cabe en una base o exige almacenamiento de objetos, y si el ancho de banda de salida cambia el diseño de la API |
| **Queda inválido si R cambia** | **Todo.** Un requerimiento funcional nuevo agrega un tipo de dato o una operación, y ambos entran en los tres cálculos. Un supuesto que se retira —los corredores de RNF-12, la frecuencia con que un emisor gira— reescribe la tabla de entradas completa |
| **Invalida a D, A, L y E** | Cambiar una entrada aquí mueve el dimensionamiento; si el resultado cruza un orden de magnitud, la arquitectura elegida en `D` deja de estar justificada por sí sola |

Cuando una cifra de este paso cambie, se abre una fila en [`ITERACIONES.md`](../ITERACIONES.md) y se
recorren `D`, `A`, `L` y `E` buscando qué quedó afirmando lo viejo.

---

## Entradas del paso

El material pide cinco: usuarios registrados, usuarios activos, RPS, **logins por segundo** y
almacenamiento. Tres de ellas suponen un modelo que este backlog no tiene. **SendIt no tiene
cuenta ni sesión**: RF-01 identifica al emisor presencialmente contra un documento oficial vigente,
cada vez que se crea un giro, y RF-11 le entrega un código de seguimiento —no una credencial— que
solo él transmite. El único secreto que el sistema comprueba sin mostrarlo es la respuesta del
desafío (RF-114, RNF-17), y se comprueba una vez, en el mostrador de destino: tampoco es un login. No
hay padrón que contar ni login que medir. Dimensionar sobre «usuarios registrados» mediría un
sistema que no es este.

**Con una excepción que hay que declarar, porque es la única.** RF-93 retiene el giro cuyo receptor
superó su acumulado de cobros en la ventana `[ASSUMPTION: 30 días corridos]`, lo que obliga a contar
cuántos giros cobró un mismo receptor en esa ventana —el ítem que antes lo pedía aparte, `RF-58`, se
retiró por estar contenido en este—. Contar por identidad y no por giro exige una clave estable de
receptor que persista
**entre giros** — y eso es lo más parecido a un padrón que este sistema tiene, del lado de Elena,
que ni siquiera es clienta. No es un padrón que se registre: se acumula solo, un cobro por vez. Se
dimensiona en el cálculo 2 como agregado por identidad, no como fila por giro.

Las unidades de carga de SendIt son tres. Las dos primeras salen del giro y se cuentan por día:
**giros por día** —la unidad de negocio, la que crea el bloque de creación del backlog y paga el
de pago— y **operaciones de ventanilla por día**,
que es la unidad de trabajo del operario y **no coincide** con la anterior: un giro consume al menos
dos ventanillas (la de creación y la de pago), y suma más cuando hay autorización de segundo rol
(RF-13), corrección (RF-56, RF-61), devolución al emisor —que es presencial y en efectivo (RF-71,
RF-72)—, entrega del efectivo que quedó en custodia sin giro creado y que RF-138 devuelve al vencer
`[ASSUMPTION: 72 horas]`, cobro derivado a otro
punto del país destino (RF-91), que consume dos ventanillas para un solo pago, o **rehacer** el giro
cancelado por código perdido (RF-46, RF-117), que es una creación entera y no suma un giro al
volumen de negocio.

**Y una que salió de esta cuenta, contra lo que este documento afirmaba.** La declaración de
diferencia de RF-90 **no es una atención de ventanilla**: el título dice *«permitirá al receptor
declarar **por llamada o mensaje de texto**»*, y RF-196 lo confirma al exigir identificar como el
receptor designado a quien declara una diferencia **fuera del mostrador** antes de admitir su
declaración. Se cuenta en el desglose de requests, no en las ventanillas — y trae consigo un acto de
identificación remota que antes nadie contaba.

**Y hay una tercera unidad, que no deriva de ninguna de las dos.** RF-76 hace que cada punto de
atención declare su efectivo al abrir y al cerrar la caja: dos escrituras por punto y por turno,
haya cero giros o mil. RF-92 le suma una lectura de saldo antes de habilitar cada pago. La primera
escala con la **red afiliada** —con S-01, no con el volumen— y es la única carga que no se apaga
cuando el día está flojo; la segunda escala con los pagos. Contarlas juntas esconde que una tiene
piso y la otra no.

| Entrada | Qué cuenta | Valor | De dónde sale | Marca |
|---|---|---|---|---|
| **Giros por día** | Giros creados, medidos sobre el conjunto de corredores de RNF-12 | **2 800** | `0,5 % de un mercado de USD 61 300 M/año ÷ USD 300 de ticket ÷ 365` — derivación completa abajo | `[ASSUMPTION: S-01b · S-05]` |
| **Operaciones de ventanilla por día** | Atenciones presenciales: crear, pagar, autorizar, corregir, devolver, entregar custodia, rederivar el cobro, rehacer | **6 000** | `2 800 crear + 2 690 pagar + 84 autorizar (RF-13) + 8 corregir (RF-56, RF-61) + 95 entregar devolución (RF-71, RF-72) + 3 entregar el efectivo en custodia (RF-118, RF-138) + 54 rederivar (RF-91) + 42 rehacer (RF-117) + 179 identificar sin giro (RF-01 corre antes de RF-79) = 5 955` | Derivado — **2,13 ventanillas por giro**, no 2. La diferencia son `5 955 − 2 × 2 800 = ` **355** atenciones diarias que ningún giro explica. RF-90 salió de esta cuenta: es una declaración por llamada o SMS, no una atención (RF-196) |
| **Aperturas y cierres de caja por día** | `puntos activos × turnos × 2` (RF-76). No depende de los giros | **9 000** | `3 000 puntos × 1,5 turnos × 2 = 9 000`, más `4 500` informes de diferencia de cierre al agente (RF-141, uno por cierre) | `[ASSUMPTION: S-12]` — es **3,2 veces** el número de giros del día: la carga con piso es mayor que la carga de negocio |
| **Avisos por llamada o SMS por día** | Unidades de voz o SMS entregadas a un tercero, **al receptor y al emisor**. Al receptor: RF-25, RF-37, RF-41, RF-69, RF-75, RF-106, RF-156, RF-109, RF-120, RF-121, RF-124. Al emisor: RF-11, RF-14, RF-51, RF-60, RF-65, RF-67, RF-127. Se pagan por unidad, no por byte | **18 200** | `6,5 unidades por giro × 2 800 = 18 200` — desglose en S-14. A USD 0,05 la unidad: `18 200 × 0,05 = USD 910/día`, `× 365 = ` **USD 332 k/año**, `910 / 2 800 = ` **USD 0,325 por giro** | `[ASSUMPTION: S-14]` |
| Giros por día en pico | `giros por día × P` | **8 400** | `2 800 × 3,0` — el componente **diario** de `P`, no el compuesto | `[ASSUMPTION: S-07]` |
| RPS — requests por segundo | Derivada, no supuesta: sale del desglose por operación del cálculo 1 | **1,34 promedio · 14,7 en pico** | `115 791 requests/día ÷ 86 400 s = 1,340` · `1,340 × 11 = 14,74` | Derivado |
| Almacenamiento requerido | Salida del cálculo 2, no entrada | **1,03 GB/día · 3,3 TB retenidos** | Cálculo 2 | Derivado |
| Factor de pico `P` | Ver abajo | **11** | `3,0 (día señalado) × 3,6 (hora del día) = 10,8` | `[ASSUMPTION: S-07]` — el único de los grandes sin ancla en ningún RNF |

### De dónde salen los 2 800 giros por día

Un supuesto de volumen que no se calibra contra nada es un número inventado con formato de
estimación. Se calibra contra el tamaño real de los dos corredores que RNF-12 y RNF-14 fijaron, y se
declara la cuota que SendIt aspira a tomar de ellos. La aritmética, a la vista:

1. **Tamaño de los dos corredores.** México recibe del orden de **USD 62 000 M/año** en remesas, de
   los que ≈ 96 % salen de Estados Unidos → `62 000 × 0,96 ≈ USD 59 700 M`. Perú recibe del orden de
   **USD 4 600 M/año**, de los que ≈ 35 % salen de Estados Unidos → `4 600 × 0,35 ≈ USD 1 600 M`.
   Suma de los dos corredores de S-01: `59 700 + 1 600 = USD 61 300 M/año`.
   `[ASSUMPTION: órdenes de magnitud públicos de remesas recibidas, redondeados a la baja. El
   enunciado no da ninguno; el corredor de Rosa es el chico de los dos por un factor de 37]`
2. **Cuota de SendIt al lanzamiento: 0,5 %** → `61 300 × 0,005 = USD 306,5 M/año`. Medio punto de un
   mercado con incumbentes de treinta años es agresivo sin ser fantasioso para un año 1 apoyado en
   red afiliada. **Es la cifra de la que más depende todo el documento**: mover la cuota mueve los
   tres cálculos en proporción directa.
3. **Ticket promedio USD 300** (S-05, punto medio del rango de Rosa) →
   `306 500 000 / 300 = 1 021 667 giros/año`.
4. **A giros por día** → `1 021 667 / 365 = 2 799` → **2 800 giros/día**.

**Contraste *bottom-up*, que es la única forma de saber si el número de arriba miente.** 2 800
giros/día son `2 800 × 30,4 = 85 120 giros/mes`; a `2` giros por emisor y mes (S-04, la quincena de
Rosa) son `85 120 / 2 = 42 560` **emisores distintos al mes** (S-02). Repartidos en los 3 000 puntos
de S-12: `42 560 / 3 000 ≈ 14` emisores por punto y mes, es decir **menos de un giro por punto y por
día**. Una red ancha y flojamente cargada es exactamente la forma del modelo Western Union que el
profesor indicó — y es la razón por la que el cálculo 1 va a dar lo que da. Si el *bottom-up* hubiera
dado cien giros por punto y día, uno de los dos supuestos estaría roto.

**El reparto entre corredores no es la cuota uniforme.** SendIt entra por el corredor peruano, donde
tiene la persona modelo y la red, con una cuota veinte veces mayor que en el mexicano:
`1 600 × 5,0 % = USD 80 M` (Perú) y `59 700 × 0,38 % = USD 226,5 M` (México), que suman los
`USD 306,5 M`. A ticket igual, el reparto por **giros** es `80 / 306,5 = 26 %` Perú y
`226,5 / 306,5 = 74 %` México `[ASSUMPTION: S-01b]`. Ese reparto no mueve el cálculo 1 ni el 3, pero
**decide el multiplicador del cálculo 2**, porque los dos reguladores no piden el mismo plazo de
conservación.

La reposición de «usuarios» por «giros» no es cosmética: un padrón crece de forma monótona y una
identidad inactiva sigue ocupando disco; un giro nace, se paga o se devuelve, y **se cierra**
(RF-64). Lo que persiste después del cierre es el registro, no el cliente — y eso es lo que cuenta
el cálculo 2. Con una salvedad, y el backlog acaba de acotarla: el giro **devuelto** no cierra al
devolverse —RF-89 mantiene la devolución disponible hasta la prescripción—, pero **ya tiene
terminador**: RF-137 da por prescrita la devolución que nadie retiró al vencer ese plazo y deja de
mantenerla disponible. El estado abierto que este documento describía como sin fin dura, como
máximo, lo mismo que el resto del dato caliente: doce meses.

### Umbrales de servicio que este paso recoge

El backlog marca `[ASSUMPTION: umbrales de servicio de RNF-09 a RNF-11]` como *«Vigente — los
consume el paso `E`»*. Aquí es donde se consumen. Ninguno de los tres cabe en las tablas de
arriba, porque no son volúmenes sino restricciones: cada uno acota un cálculo distinto por un lado
distinto.

| RNF | Umbral declarado en R | Qué cálculo restringe | Cómo lo restringe | Valor derivado | Marca |
|---|---|---|---|---|---|
| RNF-09 — **P0**, el techo de latencia lo fija ahora un ítem de máxima prioridad | *«resolverá en un tiempo acotado **la parte de una atención que solo depende de él**»*: menos de 3 minutos desde que alguien llega al mostrador, incluida la verificación del documento. La espera por un segundo rol lleva **techo propio de 10 minutos** y la de una lista externa, el de RNF-11 | Servidores | El presupuesto de máquina es lo que sobra de los 3 min después del tiempo humano de RF-01; es un techo de latencia **por atención**, no de throughput. El título nuevo **acota el numerador**: lo que se mide contra los 180 s es solo lo que SendIt controla | `180 s − 150 s de tiempo humano = 30 s de máquina por atención`. **Lo que sigue es derivación de este paso, no de RNF-09:** RNF-09 no fija ningún techo por request; fija uno por atención, y repartirlo exige un supuesto propio. Una creación encadena **13** requests sincrónicos —identificar (RF-01), conservar la evidencia (RF-80), contar límites (RF-08, RF-09, RF-10), cotizar (RF-07), tamizar al emisor (RF-26), tamizar al receptor (RF-119), registrar el desafío (RF-68), dejar constancia de lo informado antes del efectivo (RF-73, RF-77, RF-96, RF-115, RF-136, RF-142), exigir efectivo en destino (RF-20), registrar la recepción (RF-79), emitir el código (RF-11), traspasárselo al emisor sin que el operario lo lea (RNF-15) y confirmarle al operario que salió sin mostrárselo (RF-125)— y, **repartiendo el presupuesto por igual entre los trece**, `30 / 13 = ` **2,3 s por request en p99**. Sigue cabiendo la llamada externa a las listas; **el margen bajó un 30 % respecto de los 3,3 s de la ronda anterior, y lo bajaron RF-119, RNF-15, RF-115, RF-136, RF-142 y RF-125** | `[ASSUMPTION: 150 s de tiempo humano en RF-01 — pedir el documento, mirar la foto, tipear]` · `[ASSUMPTION: E-01 — el presupuesto de máquina de RNF-09 se reparte **por igual** entre los requests sincrónicos de la atención. RNF-09 no lo dice: acota la atención entera. Un reparto desigual —cargar el tamizaje externo y aliviar el resto— da otro techo por request y no cambia el de la atención]` |
| RNF-10 | Giro fondeado disponible para cobro en destino en menos de 15 min desde su creación | Servidores y ancho de banda | Acota la ventana de propagación entre origen y destino, y con ella cuánto puede diferirse el trabajo de RF-20 y RF-36 | `15 min = 900 s` de ventana origen → destino. Una réplica asíncrona entre regiones propaga en ≈ 1 s: `900 / 1 = 900×` de margen. **Conclusión que reparte los servidores: RNF-10 no obliga a escritura síncrona multirregión**, así que hay un solo plano de escritura y réplicas de lectura en destino, no un quórum global | Derivado |
| RNF-11 — **P1** | 99,9 % mensual, medido **sobre crear y pagar, no sobre consultar** | Servidores | Reparte la redundancia de forma desigual: la ruta de escritura se dimensiona con margen de disponibilidad, la de consulta (RF-52, RF-53) no | `43 200 min/mes × 0,001 = ` **43,2 min/mes** de presupuesto de error sobre crear y pagar. Un nodo solo no lo cumple → **3 nodos con quórum** en la ruta de escritura (tolera una caída); la de consulta queda excluida de la medida y se sostiene con **2** sin quórum | Derivado — **es el término que manda en el cálculo 1**, no la carga |

---

## Supuestos declarados

El ejemplo del material estima YouTube con cifras que el enunciado del ejercicio da (100 M de
usuarios activos, 10 vídeos por usuario, 1,3 M de vídeos diarios). **El enunciado de SendIt no da ni
una cifra.** Consecuencia directa: aquí toda entrada es un `[ASSUMPTION: ...]`, y un supuesto que no
declara contra qué se calibró es un número inventado con formato de estimación.

Cada fila declara **por qué hace falta** —qué cálculo se cae sin ella— y **contra qué se calibra**,
que es la única defensa que tiene un supuesto. Cuatro de ellas ya no dependen de este paso: el
backlog las cerró en su iteración 03 y aquí se consumen como dadas, no como pendientes.

| # | Supuesto que hace falta | Por qué hace falta | Contra qué se calibra | Valor | Estado |
|---|---|---|---|---|---|
| S-01 | Corredores atendidos | Fija las monedas, los dos reguladores que RF-16 aplica al mismo giro, la red de **puntos de atención afiliados** en la que hay que sostener efectivo (RF-20) y los husos horarios del pico. Sin él no hay volumen que estimar ni reglas que aplicar | **Cerrado por RNF-12 y RNF-14**: dos corredores al lanzamiento — Estados Unidos → Perú y Estados Unidos → México. Un solo país de origen con **dos monedas de destino**, que es lo que RNF-14 exige desde el primer día. El primero es el que modela [Rosa](../../personas/Rosa.MD) | Dos corredores | **Cerrado** |
| S-01b | Reparto de los giros entre los dos corredores | S-09 fija la conservación **por giro y no por política global**, así que el multiplicador del cálculo 2 es el promedio ponderado de los dos plazos. Sin este reparto no hay ponderación: solo un rango de 5 a 10 años | La cuota diferenciada de la derivación de arriba: `USD 80 M` en Perú (5,0 % de su corredor) y `USD 226,5 M` en México (0,38 % del suyo). SendIt entra por donde tiene red y persona modelo, no por donde hay más dinero | **26 % Perú · 74 % México** | `[ASSUMPTION]` |
| S-02 | Emisores distintos por mes | Dimensiona el almacenamiento de la evidencia de identidad que RF-80 conserva, y que persiste por el plazo de RNF-03 aunque el emisor no vuelva nunca. No es un padrón: es el recuento de identificaciones practicadas en ventanilla. Su gemelo del lado receptor no tiene supuesto propio porque no hay uno solo por giro: ver S-15 | El contraste *bottom-up* de arriba, que es aritmética y no opinión: `85 120 giros/mes ÷ 2 giros por emisor` | **42 500 emisores distintos/mes** | `[ASSUMPTION]` |
| S-03 | Proporción de giros que exigen captura nueva de identidad | Un emisor recurrente se identifica otra vez (RF-01 no admite excepción) pero puede no producir un binario nuevo. La proporción decide cuánto del cálculo 2 crece con los giros y cuánto con las personas | El patrón de [Rosa](../../personas/Rosa.MD): la misma emisora, quincena tras quincena | **30 % de los giros, por punta** — un emisor gira 24 veces al año y solo produce binario nuevo al alta, al renovar documento o cuando el anterior no es legible; en el año 1 la base crece, así que 1 de cada 3,3 giros trae captura nueva. El otro 70 % guarda una **referencia de 2 KB**, no una imagen | `[ASSUMPTION]` |
| S-04 | Giros por emisor al mes | Convierte emisores en giros por día, que es la unidad de carga del paso | El patrón de Rosa: quincenal, estable desde hace tres años | **2 giros/emisor/mes** | `[ASSUMPTION]` — declarado en su propia ficha |
| S-05 | Ticket promedio | No mueve el cómputo, pero decide cuántos giros cruzan el umbral de reporte transfronterizo (RF-17, RF-22, RF-139) y cuántos el umbral reforzado que obliga a un segundo rol (RF-13) — y con ello cuántas operaciones de ventanilla extra aparecen | El rango de Rosa: USD 200–400 | **USD 300** (punto medio). Con él: `3 %` de los giros cruzan el umbral reforzado de RF-13 `[ASSUMPTION: umbral reforzado de BR-05]` → **84 autorizaciones de segundo rol al día**; `0,1 %` cruzan el umbral de reporte transfronterizo, que **ya no hace falta inventar acá**: RF-17 lo lleva escrito como `[ASSUMPTION: USD 10 000 por operación, o el que fije cada regulador si es menor]` y RF-22 lo aplica sobre el giro completo → **3 reportes al día a la autoridad de origen**, más los **3** que RF-139 obliga a hacer a la autoridad de destino, con la fecha de nacimiento de las dos puntas que RF-140 exige informar → **6 reportes al día** | `[ASSUMPTION]` — la cifra la produce ahora `R`, no `E` |
| S-06 | Consultas de estado por giro, **de las dos puntas** | **RF-52 y RF-53 la exigen como capacidad del emisor, RF-66 le agrega el estado retenido con su fecha, y RF-128 la exige también del receptor «sin depender del emisor»**: la consulta es carga requerida, no tráfico incidental. Es la operación de lectura dominante y la única que RNF-11 excluye explícitamente de su medida de disponibilidad | Lo que hoy obliga a Rosa a llamar por teléfono, ahora exigido por RF-52; y lo que hoy obliga a Elena a llamar a Rosa, ahora exigido por RF-128 | **8 consultas por giro: `6` del emisor `+ 2` del receptor.** Rosa consulta al salir de la ventanilla, antes de pasarle el código a Elena, el día que le dijo que fuera, y otra vez si no pasó nada. Elena consulta menos porque el sistema le avisa: `[ASSUMPTION: S-06b — 2 consultas por giro del lado del receptor, un tercio de las del emisor, porque RF-25, RF-41 y RF-75 le llegan sin que pregunte]`. Es la familia más numerosa del sistema: `8 × 2 800 = 22 400/día`, el **19,3 %** de todos los requests | `[ASSUMPTION]` |
| S-07 | **Factor de pico** | Ver abajo | El ciclo de pago quincenal de Rosa y el calendario de fechas señaladas de los dos destinos. **Ningún RNF lo ancla**, y por eso es el supuesto más frágil de los grandes | **`P` = 11** = `3,0` (día señalado) `× 3,6` (hora del día). Ventana: **una hora**, dentro de un día señalado | `[ASSUMPTION]` |
| S-08 | Proporción de giros que disparan una coincidencia de tamizaje | La tasa decide el volumen de evidencia, que es lo que domina el almacenamiento, y RF-28 obliga a guardar separadas la coincidencia exacta y la homonimia — la abrumadora mayoría son homónimos | `[ASSUMPTION: sin fuente; el enunciado no da ninguna cifra de tamizaje]` | **2 % de los giros**, de los que **98 % son homonimia** (RF-28, RF-78) y 2 % coincidencia exacta: `2 800 × 0,02 = 56 casos/día`, de los que `56 × 0,02 ≈ 1` es exacto. RF-93 agrega `0,5 %` por acumulado de receptor → `14`. Y RF-123 vuelve a correr los controles sobre cada giro rehecho: `42 × 0,02 ≈ 1`. Total `56 + 14 + 1 = ` **71 casos de cumplimiento al día**. **RF-119 no lo mueve**: parte el tamizaje de creación en dos actos (emisor y receptor) pero no agrega una identidad — el receptor ya se tamizaba en RF-27, más tarde | `[ASSUMPTION]` |
| S-09 | Años de retención regulatoria | Multiplica el almacenamiento diario por un factor que el ejemplo de YouTube no tiene | **Cerrado por RNF-03 y RF-18**: el plazo más largo de los dos reguladores del giro, con un piso de 5 años. Se calcula por giro y no por política global, así que el multiplicador del cálculo 2 no es único: es el máximo por corredor | ≥ 5 años | **Cerrado** |
| S-10 | Plazo de una retención | Acota cuántos giros retenidos coexisten: la cola no es un acumulado sin fin, es un caudal con tiempo de residencia. RF-31 le pone plazo y RF-32 la termina devolviendo al emisor | **Cerrado**: lo que fije el regulador más estricto de los dos países del giro; **a falta de norma expresa, 72 h**. Es un piso por defecto, no un techo — un regulador puede exigir más, y RF-31 obliga a obedecerlo. El tiempo de residencia se dimensiona **por corredor**, contra el plazo más largo, igual que S-09 | ≥ 72 h, por corredor | **Cerrado** |
| S-11 | Plazo de prescripción | Fija cuánto tiempo un giro creado sigue siendo pagable y por tanto vivo en el estado caliente antes de que RF-49 lo vuelva no pagable y RF-50 lo ponga a disposición del emisor. Separa el dato caliente del dato meramente retenido | **Cerrado**: 12 meses desde la creación del giro | 12 meses | **Cerrado** |
| S-12 | Puntos de atención activos y turnos por punto | Es la única entrada que no deriva del volumen: RF-76 escribe dos declaraciones de caja por punto y turno aunque no haya un solo giro, y RF-92 lee el saldo antes de cada pago. Fija además cuántos destinos ofrece RF-63 al emisor y cuántos puede alcanzar la rederivación de RF-91 | La red afiliada de los dos corredores de S-01, no la planta propia | **3 000 puntos activos · 1,5 turnos por punto**. Da `9 000` declaraciones de caja al día (RF-76) y `2 690` lecturas de saldo (RF-92). Nótese: `9 000 > 2 800` — **la carga que no se apaga es mayor que la que sí** | `[ASSUMPTION]` |
| S-13 | Proporción de giros que terminan devueltos, y cuánto tarda el emisor en retirar | Toda devolución es una operación de ventanilla más (RF-71 en efectivo, RF-72 en el punto que el emisor elija), un aviso más al emisor (RF-14) y otro al receptor (RF-106), y un asiento más que incluye la comisión (RF-74). RF-89 la mantiene disponible hasta la prescripción y **RF-137 la termina ahí**: el estado ya no es abierto, es acotado a 12 meses. Esta proporción mueve el cálculo 1 y el borde —no el tamaño— del almacenamiento caliente del cálculo 2 | Las **seis** fuentes de devolución que el backlog tiene hoy: retención vencida (RF-32), cancelación (RF-47), prescripción (RF-50), intentos de desafío agotados (RF-103), falta de respuesta al cambio de punto (RF-111) y ningún punto capaz de pagar en el distrito (RF-129). La tasa es un supuesto; el número de fuentes, no | **4 % de los giros terminan devueltos** → `112/día`. De ellos, **85 % se retira dentro de 30 días** → `95` entregas de ventanilla al día; el **15 % restante** (`17/día`, `0,6 % de los giros`) queda abierto hasta la prescripción por RF-89 y **RF-137 lo cierra ahí**: `17 × 365 × 366,2 KB = 2,27 GB` en régimen, el `0,07 %` del retenido | `[ASSUMPTION]` |
| S-14 | Avisos por giro —al receptor **y** al emisor—, y coste por unidad del canal | El canal de voz y SMS es de un tercero y se paga **por unidad entregada**, no por byte: es la única partida del paso cuyo costo no baja aunque el mensaje quepa en 140 caracteres. Un giro sin incidente ya gasta tres al receptor (RF-25, RF-41, RF-75) y uno al emisor —el código de RF-11—; cada desenlace agrega el suyo. RF-132 hace del reintento una obligación y no una cortesía: **quien no tenga constancia de que el aviso llegó cuenta como no avisado**, así que la unidad se repite hasta que RF-131 registre la entrega | La cuota que un operador de telefonía concede por país, que RNF-12 obliga a contar por país de origen y de destino | **6,5 unidades por giro · USD 0,05 por unidad.** Al receptor: `3,0` de base (RF-25, RF-41, RF-75) `+ 0,045` la base repetida sobre el giro rehecho (`1,5 % × 3`, S-19) `+ 0,20` pregunta del desafío (RF-69) `+ 0,0254` retenido (RF-37, sobre los 71 casos de S-08) `+ 0,02` el punto dejó de poder pagarle (RF-109) `+ 0,02` a qué otro punto ir (RF-124, uno por cada RF-109) `+ 0,04` devuelto al emisor (RF-106, S-13) `+ 0,01` giro retenido por cambio de lista (RF-37, sobre RF-97) `+ 0,005` prescripción próxima (RF-120) `+ 0,005` diferencia registrada (RF-121) `= 3,370`. Al emisor: `1,015` el código de seguimiento (RF-11, uno por giro creado **más uno por giro rehecho**) `+ 0,96` cobrado (RF-65) `+ 0,04` devolución disponible (RF-14) `+ 0,0254` retenido (RF-67) `+ 0,018` giro liberado (RF-127, sobre las retenciones que no vencen) `+ 0,005` prescripción próxima (RF-51) `+ 0,005` diferencia (RF-60) `= 2,068`. Suma `5,438`, `× 1,20` de reintentos `= 6,526` → **6,5**. **Tres correcciones de fondo respecto de la ronda anterior:** (1) **faltaba RF-11** — el código de seguimiento viaja «por llamada o mensaje de texto al teléfono que él registró», es una unidad del tercero como cualquier otra y este documento no la contaba: sola vale `+1,015`; (2) el aviso de cancelación que se cargaba a `RF-107` **desaparece sin restar nada**, porque ese ítem se retiró y RF-106 lo cubre vía RF-47 —la cancelación *es* una devolución— y el `4 %` de S-13 ya la contenía: los `0,030` que se le sumaban eran un doble conteo; (3) RF-127 es un aviso nuevo. **Y RF-115, RF-116, RF-136 y RF-142 no entran acá**: son plazos y cifras que se informan en la ventanilla, no unidades del canal | `[ASSUMPTION]` · `[ASSUMPTION: reintento de 1,20 — 12 % por entrega fallida más 8 % por entrega sin constancia, que RF-132 obliga a tratar como no avisado. Era 1,12 cuando la constancia solo probaba el envío]` · `[ASSUMPTION: 70 % de las retenciones se liberan y disparan RF-127; el 30 % vence y sale por RF-32]` |
| S-15 | Receptores distintos por mes, y cobros por receptor en la ventana | RF-93 retiene el giro cuyo receptor superó su acumulado de cobros en la ventana: hace falta una clave de receptor estable entre giros, no una fila por giro. Y RF-80 conserva la evidencia de identidad **del receptor además de la del emisor**, de modo que el binario pesado del cálculo 2 se captura dos veces por giro y no una | El mismo patrón de S-02, del otro lado del mostrador: Elena cobra todos los meses y se identifica todas las veces. **La ventana ya no la fija este paso**: RF-09 y RF-93 la llevan escrita como `[ASSUMPTION: 30 días corridos]` | **39 000 receptores distintos/mes · 2,2 cobros por receptor** en la ventana de `30 días corridos` que RF-93 declara: `85 120 / 2,2 = 38 690`. El acumulado de RF-93 pesa `0,2 KB` **por identidad**, no por giro → `0,2 / 2,2 = 0,09 KB` por giro | `[ASSUMPTION]` — la ventana la produce ahora `R` (RF-09, RF-93), no `E` |
| S-16 | Proporción de pagos que se resuelven por desafío, e intentos por pago | RF-68 obliga a registrar pregunta y respuesta en **todo** giro, así que el dato existe siempre y RNF-17 exige guardarlo ilegible en los dos lados del mostrador — coste fijo por giro, en el camino de escritura de la creación. Lo que varía es el consumo: RF-69 abre el desafío como salida al documento vencido, RF-82 acota los intentos y RNF-17 obliga a comprobarlos sin mostrarlos a ninguno de los dos lados, así que un pago puede costar hasta `intentos` comprobaciones en vez de una | La proporción de documentos vencidos que hoy dejan a Elena sin cobrar, que es la tensión T3 del backlog | **Coste fijo: 1 escritura por giro** (RF-68 no admite excepción) → `2 800/día`. **Consumo: 20 % de los pagos** usan el desafío, a `1,6` intentos promedio contra el techo que **RF-82 lleva escrito**, `[ASSUMPTION: 3]` → `0,20 × 1,6 = 0,32` comprobaciones por giro → `896/día`. El DNI de Elena lleva catorce meses vencido: el 20 % no es un caso raro, es su caso | `[ASSUMPTION]` — el `3` lo produce ahora `R` (RF-82), no `E` |
| S-17 | Proporción de pagos con declaración de diferencia | RF-90 le da al receptor un acto propio que antes no tenía —y lo ejerce **por llamada o mensaje de texto**, no en el mostrador, de modo que RF-196 obliga a identificarlo antes de admitir la declaración—, y cada declaración abre la cadena cara: atribución al punto (RF-59), aviso **al emisor** (RF-60) y **al receptor** (RF-121), y si termina en corrección, un movimiento nuevo (RF-56) con autorización de un segundo rol (RF-61). Es baja en proporción y alta en operaciones por caso | `[ASSUMPTION: sin fuente; el enunciado no da ninguna cifra de diferencias]` | **0,5 % de los pagos** → `13/día`. Baja en proporción y cara por caso: cada una abre identificación del declarante (RF-196), atribución (RF-59), aviso a los dos —**RF-60 al emisor y RF-121 al receptor**—, informe previo al agente con la evidencia que lo sustenta (RF-104), descuento a su liquidación (RF-143) contra el que puede objetar (RF-145) y, si termina en corrección, movimiento nuevo (RF-56) con segundo rol (RF-61) → `13 × 7 ≈ 91` actos diarios que nacen de 13 casos | `[ASSUMPTION]` |
| S-19 | Proporción de giros cuyo código se pierde, se cancelan y se rehacen | RF-94 no reemite un código nunca, así que la única salida de T7 es cancelar (RF-46) y rehacer (RF-117). **El giro rehecho no suma volumen de negocio** —RF-134 le conserva la cotización que fijó el cancelado y RF-135 no vuelve a cobrarle la comisión— **pero sí carga**: RF-123 le vuelve a correr todos los controles, incluida la identificación del emisor contra su documento, de modo que es una creación entera cuyo ticket ya se contó una vez | La tensión T7 del backlog, que trata el código perdido como escenario real y no como borde: Rosa pasa un código de papel por teléfono | **1,5 % de los giros** → `2 800 × 0,015 = ` **42 rehechos/día**, `42` ventanillas más, `42 × 3 = 126` tamizajes más (RF-123), `42 × 3 = 126` avisos de base más al receptor (RF-25, RF-41, RF-75 otra vez) y `42` códigos nuevos al emisor (RF-11), que son `42` unidades más del canal | `[ASSUMPTION]` |
| S-20 | Proporción de pagos cuya confirmación no llega del punto al centro | RF-144 los deja en un estado único y RF-146 obliga a resolverlos **contra el registro del centro y sin intervención del operario**. Es un estado nuevo del backlog de hoy, y es el único que se resuelve solo: no consume ventanilla, consume dos escrituras y una comparación. Sin él, la reconciliación de RNF-08 no tenía dónde apoyarse | El mismo orden de magnitud que la caída de enlace de `D`(c), que es lo que la produce: la confirmación se pierde donde el enlace falla | **0,5 % de los pagos** → `13/día`, `2` actos cada uno (estado y resolución) = **27 escrituras/día**. No entra en las ventanillas: RF-146 lo resuelve sin el operario | `[ASSUMPTION]` |
| S-21 | Proporción de creaciones que dejan efectivo recibido sin giro creado | RF-118 lo deja en un estado único que el operario puede leer y retomar, y **RF-138 lo termina**: devuelve al emisor el efectivo en custodia que nadie retomó al vencer `[ASSUMPTION: 72 horas]`. Antes de RF-138 este estado no tenía salida y el cálculo 2 lo llevaba como piso indefinido | La tasa de interrupción de una atención presencial de tres minutos | **0,1 % de las creaciones** → `3/día` en custodia y `3/día` devueltos por RF-138 al vencer las 72 h; en régimen conviven `3 × 3 = 9` custodias abiertas. Son `6` escrituras y `3` ventanillas al día | `[ASSUMPTION]` — el plazo lo produce ahora `R` (RF-138), no `E` |
| S-18 | Pedidos de supresión de datos personales por mes | **Es uno de los dos términos negativos del cálculo 2** — el otro es RF-99, y resulta ser treinta veces mayor. RF-81 suprime a pedido los datos de quien los entregó —y de nadie más— salvo lo que el registro de actos debe conservar, que RNF-03 declara inalterable. Resta binarios de identidad; no resta trazas. Y agrega una operación cara que ningún giro pide: buscar a una persona **a través de** todos sus giros, que es el eje por el que el libro contable no está particionado | El plazo de RNF-03 acota lo que puede suprimirse: por debajo del piso de conservación no hay nada que borrar | **40 pedidos/mes** = `1,3/día`, que borran ≈ `1,4` capturas de `500 KB` cada uno = `700 KB` por pedido → **−0,9 MB/día**. Es el **0,09 %** del retenido: irrelevante en la cifra, decisivo en el diseño | `[ASSUMPTION]` |

### El factor de pico

**Las remesas no son planas.** El volumen se concentra en la quincena y el fin de mes —cuando se
cobra— y se dispara en fechas señaladas: Día de la Madre, Navidad, el inicio del año escolar. El
sistema pasa la mayor parte del año por debajo de su capacidad y falla los pocos días que a Rosa le
importan, que son exactamente los días en que su madre tiene una fecha que cumplir.

De esto se sigue una regla para el cálculo 1: **el dimensionamiento se hace contra el pico, no
contra el promedio.** El promedio no falla nunca. Se declara como un factor explícito
`P = giros por día en pico / giros por día promedio`, con su ventana (¿el pico dura una hora, un
día, una semana?), porque un pico de horas y uno de días no se enfrentan con la misma arquitectura.

**Ningún RNF del backlog fija este factor.** RNF-09, RNF-10 y RNF-11 dan umbrales de servicio que el
sistema debe cumplir *también* en el pico, pero no dicen cuán alto es el pico. S-07 es, por tanto, un
supuesto abierto y sin ancla en R — y se declara como tal en vez de heredarlo de un RNF que no lo
dice.

| Ventana de pico | Multiplicador estimado | Qué la produce | Marca |
|---|---|---|---|
| Quincena / fin de mes | **2,0×** | Ciclo de cobro del emisor. `40 % del volumen del mes cae en 6 días` (los dos de pago y los dos siguientes de cada quincena) → `(0,40 / 6) / (1 / 30,4) = 0,0667 / 0,0329 = 2,03` | `[ASSUMPTION: S-07]` |
| Fecha señalada | **3,0×** | Día de la Madre (10 de mayo en México, segundo domingo en Perú), Navidad, inicio del año escolar. No sustituyen al pico de quincena: se apilan sobre él → `2,0 × 1,5 = 3,0`. **Es el que dimensiona**, porque es el día que a Rosa le importa | `[ASSUMPTION: S-07]` |
| Hora del día | **3,6×** | Huso horario del emisor, no del receptor. `15 % del día en 1 h → 0,15 × 24 = 3,6`. Los husos que achatan el pico tres horas son **Este y Pacífico dentro del único país de origen que S-01 fija**, no dos países: son geografía de Estados Unidos, no multiplicidad de corredores. **RNF-12 no los produce** —lo que RNF-12 exige es que ninguna cifra suponga un solo país de origen, y esta lo supone hoy porque S-01 lo fija así—; lo que obliga es a **volver a derivar este 3,6 en cuanto entre un segundo país de origen**, que es cuando aparecen calendarios y husos que no son los de este. El 15 % ya contempla el achatamiento interno, y es por eso que no es 20 % | `[ASSUMPTION: S-07]` · `[ASSUMPTION: los husos Este y Pacífico del país de origen de S-01 achatan el pico ~3 h. Es un supuesto de este paso, no una lectura de RNF-12]` |

**El compuesto es el que se usa, y no es la suma de los tres.** La quincena ya está dentro de la
fecha señalada, así que multiplicarlas otra vez contaría dos veces lo mismo. `P` se compone del
factor **diario** que dimensiona el volumen del día y del factor **intradía** que dimensiona el
instante: `P = 3,0 × 3,6 = 10,8` → **`P` = 11**, con ventana de **una hora**. Un pico de una hora se
enfrenta con capacidad ya encendida; uno de una semana, con otra arquitectura. Este es de una hora.

---

## Cálculo 1 — Servidores requeridos

El método del material, con su aritmética explícita:

1. Cuánto maneja **un único CPU core**.
2. Cuánto maneja **un servidor** = `#cores × capacidad de un core`.
3. `#servidores = carga objetivo / capacidad de un servidor`.

> **Ejemplo del material, para la forma —no son cifras de SendIt.** Un core a 5 req/s · un servidor
> de 32 cores → `32 × 5 = 160` req/s · carga objetivo de 100 k req/s → `100 000 / 160 = 625
> servidores`.

### La aritmética de SendIt

Se calcula **en dos columnas**, no en una, por la razón que el párrafo siguiente explica: promediar
una escritura contable con una consulta de estado promedia dos cosas que no se promedian.

| Paso | Fórmula | Valor | Marca |
|---|---|---|---|
| 1. Capacidad de un core | `req/s` que sostiene un core, **por tipo de operación** | **escritura contable: 5 req/s · lectura: 50 req/s** | `[ASSUMPTION: la escritura de SendIt cuesta al menos lo que el request genérico del material, que fija 5 req/s por core — toca varias filas, cruza la frontera del corredor y no puede servirse desde caché. La lectura sale de un índice caliente y rinde 10× ]` |
| 2. Capacidad de un servidor | `#cores × core` | escritura: `16 × 5 = ` **80 req/s** · lectura: `16 × 50 = ` **800 req/s** | `[ASSUMPTION: servidor de 16 vCPU]` |
| 3. Carga objetivo | `RPS derivado del desglose de abajo × P` | escritura: `83 885 / 86 400 = 0,971 req/s`, `× 11 = ` **10,68 req/s** · lectura: `31 906 / 86 400 = 0,369 req/s`, `× 11 = ` **4,06 req/s** | Derivado |
| 4. Servidores | `carga objetivo / capacidad de servidor` | escritura: `10,68 / 80 = 0,134` · lectura: `4,06 / 800 = 0,005` · suma: **0,139 → 0,14 servidores** | Derivado — **un solo servidor cubre siete veces la carga del pico**. Era `0,10` sobre 137 ítems: los 155 de hoy subieron la carga un `34 %` y siguen sin llegar a media máquina |

Donde el material obtiene `100 000 / 160 = 625 servidores`, SendIt obtiene `10,68 / 80 = 0,134`. No es
un error de método: es el resultado, y dice algo. Un sistema de remesas en efectivo mueve **dinero**,
no *bytes*: 2 800 giros diarios son `USD 840 000` al día atravesando la frontera con dos reguladores
encima, y caben en una máquina. **La dificultad de SendIt nunca fue el cómputo.** Lo que sigue —el
piso de disponibilidad, la cuota del canal de terceros, el efectivo de la caja— es donde está.

**Una advertencia que este caso obliga y el ejemplo del material no necesita:** un `request` de
SendIt no cuesta lo mismo que otro. Consultar el estado de un giro es una lectura; ejecutar un pago
es una escritura contable que toca varias filas, cruza la frontera del corredor —hacia el punto de
atención que entrega el efectivo, y hacia el regulador de destino cuyas reglas RF-16 obliga a
aplicar sobre el mismo giro— y no puede servirse desde caché. Estimar con un único «core = N req/s»
promedia dos cosas que no se promedian. Si el desglose por tipo de operación cambia el resultado en
más de un orden de magnitud, se calcula por separado y se suma.

**Y una corrección de perfil que RF-07 obliga:** cotizar **no es una lectura**. El sistema no
consulta una tasa ajena y la muestra: *produce y fecha* la cotización de la que sale el monto, y
RF-06 lo conserva sin recalcularlo durante toda la vida del giro. Eso es una escritura durable —una
por giro, en el camino crítico de RNF-09— y mueve el perfil de carga del sistema hacia la escritura
mucho antes de llegar al pago. Un dimensionamiento que la contara como lectura cacheable
subestimaría el eje que más caro escala.

Del lado del efectivo tampoco hay procesador que cobre a Rosa: **RF-79 hace que el efectivo entre
por la ventanilla** —el giro se da por creado en el momento en que se registra la recepción del
efectivo—, contra un emisor ya identificado. La única frontera de cobro que este sistema cruza es la
de la liquidación con el agente (RF-24), y el backlog acaba de agregarle camino: RF-104 prohíbe
descontarle nada sin informárselo antes con la evidencia, RF-143 descuenta la diferencia repuesta que
se originó en su punto y RF-145 le admite una objeción antes de aplicarla. Sigue sin estar en el
camino del giro; ya no es un asiento suelto.

**La tercera advertencia es de unidad, no de peso: el aviso no se mide en requests.** Es una llamada
o un SMS que entrega un operador de telefonía, con cuota diaria y precio por unidad, y su latencia y
su tasa de fallo no las fija este sistema. **Dieciocho requerimientos se apoyan en él, y esa cuenta
hay que hacerla contra el backlog de hoy, no arrastrarla:** **once del lado del receptor** —RF-25,
RF-37, RF-41, RF-69, RF-75, RF-106, RF-156, RF-109 y RF-124 en P0, más RF-120 y RF-121 en P1— y
**siete del lado del emisor** —RF-11, RF-14, RF-65, RF-67 y RF-127 en P0, más RF-51 y RF-60 en P1—.
Son **14 P0 y 4 P1**. Contra los diecisiete de la ronda anterior la diferencia no es un ítem sino
tres movimientos: `RF-107` **se retiró** (RF-106 lo cubre vía RF-47, porque la cancelación es una
devolución), **RF-127 entró** —avisar al emisor que su giro dejó de estar retenido— y **RF-11 siempre
estuvo y faltaba en la cuenta**: el código de seguimiento viaja por el mismo canal de terceros que
todo lo demás.
Ninguno tiene alternativa: Elena no tiene aplicación ni datos móviles, así que un aviso no entregado
no degrada, **desaparece** — y RF-132 obliga ahora a saberlo, porque quien no tenga constancia de que
el aviso llegó cuenta como **no avisado**. Se dimensiona en unidades por día contra la cuota del
tercero, no en RPS contra la capacidad de un core, y por eso lleva fila propia en la tabla de
entradas.

**Y una cuarta, que es de altitud: RF-115, RF-116, RF-136 y RF-142 no son avisos.** Son **plazos y
cifras que se informan** —dentro de cuánto se avisará una retención, dentro de cuánto hay que
responder a la oferta de otro punto, cuánta comisión se cobra, qué margen se aplica sobre la
cotización— y se informan donde el emisor ya está: en la ventanilla, antes de que entregue el
efectivo. No consumen unidad del tercero; consumen un dato más en la respuesta del mostrador y una
constancia más en el libro. Contarlos como avisos habría inflado el cuello del canal con carga que no
pasa por él. **La contraria también vale y este documento la tenía mal:** RF-90 no es una atención de
ventanilla sino una declaración **por llamada o mensaje de texto**, y RF-196 obliga a identificar a
quien la hace fuera del mostrador antes de admitirla.

| Operación | Tipo | Requerimiento que la exige | Peso relativo | Volumen diario | Marca |
|---|---|---|---|---|---|
| Identificar al emisor contra documento | escritura + verificación externa | RF-01, RF-79 | 6 | **2 980** = `2 800 giros + 179 identificaciones sin giro` | Escritura |
| Conservar la evidencia de identidad de las dos puntas | escritura de binario | RF-80, RNF-01 | **40** — la más cara por unidad | **1 734** = `2 800 × 0,619 capturas` (S-03 en las dos puntas, más las 54 que RF-99 descartará) | Escritura |
| Registrar la pregunta y su respuesta al crear | escritura ilegible, una por giro | RF-68, RNF-17 | 2 | **2 800** = `1 × 2 800` — RF-68 no admite excepción | Escritura |
| Cotizar y fechar la cotización | **escritura durable** | RF-05, RF-06, RF-07, RNF-16 | 10 | **3 640** = `2 800 × 1,3` — RF-05 se cotiza más de una vez por giro cuando Rosa pregunta por dos montos | Escritura |
| Contar límites sobre la identidad del emisor | lectura agregada | RF-08, RF-09, RF-10 | 3 | **2 980** — una por creación intentada, antes de tocar el efectivo | Lectura |
| Contar los cobros del receptor en la ventana de `30 días corridos` | lectura agregada **por identidad de receptor** | RF-93 | 3 | **2 690** — una por pago | Lectura — y la única que no se resuelve con la clave del giro |
| Tamizar contra listas | lectura externa + escritura de evidencia | RF-26, RF-119, RF-27, RF-28, RF-97, RF-123 | 12 | **11 326** = `2 800 × 4 = 11 200` — **tres obligatorias, no dos**: RF-26 tamiza al emisor y RF-119 al receptor designado, **las dos antes de aceptar el efectivo**, y RF-27 vuelve sobre el receptor contra las listas vigentes al autorizar el pago; la cuarta es el retamizaje por cambio de lista (RF-97). Más `42 rehechos × 3 = 126` que RF-123 obliga a repetir enteros | Escritura de evidencia |
| Crear el giro y emitir su código | escritura contable | RF-79, RF-11, RF-13, RF-20 | 10 | **2 800** | Escritura |
| Declarar el efectivo al abrir y al cerrar caja | escritura, `puntos × turnos × 2` | RF-76 | 4 | **9 000** = `3 000 × 1,5 × 2` — **la operación más numerosa que no depende del volumen** | Escritura con piso |
| Informar al agente la diferencia de cada cierre de caja | escritura + salida al agente | RF-141 | 2 | **4 500** = `3 000 × 1,5` — uno por cierre, haya o no diferencia: el título dice *«la diferencia»*, y una diferencia de cero también lo es | Escritura con piso — **nueva** |
| Informar al operario el efectivo del punto | lectura previa a cada pago | RF-92 | 1 | **2 690** | Lectura |
| Mostrar al operario la acción ofrecible del giro que tiene delante | lectura | RF-39, RF-130, RF-40 | 1 | **250** = `71 retenidos + 179 rechazados en ventanilla` | Lectura — **nueva** |
| Comprobar la respuesta del desafío sin mostrarla | lectura ilegible, hasta `[ASSUMPTION: 3]` intentos por pago (RF-82) | RF-114, RF-69, RF-82 | 2 | **896** = `2 800 × 0,20 × 1,6` (S-16) | Lectura |
| Ejecutar el pago en destino | escritura contable + frontera | RF-34, RF-36, RF-85, RF-86, RNF-05, **RNF-16** | **15** — la más cara del camino crítico | **2 690** = `2 800 × 0,96` (el 4 % restante se devuelve, S-13) | Escritura. **RNF-16 es el invariante que la gobierna**: ninguna entrega difiere de la cifra que el emisor vio antes de entregar su efectivo |
| Resolver el pago cuya confirmación no llegó del punto al centro | escritura de estado + resolución automática | RF-144, RF-146, RNF-08 | 15 | **27** = `13 estados + 13 resoluciones` (S-20). RF-146 lo resuelve **contra el registro del centro y sin el operario** | Escritura — **nueva** |
| Rederivar el cobro a otro punto del país destino | escritura de estado + segunda ventanilla | RF-91, RF-105, RF-129 | 6 | **54** = `2 690 × 2 %` `[ASSUMPTION]` — consume **dos** ventanillas para un solo pago, y RF-105 exige la respuesta del emisor en medio | Escritura |
| Admitir una declaración de diferencia hecha fuera del mostrador | escritura + identificación remota + atribución al punto | RF-90, RF-196, RF-59 | 8 | **26** = `13` declaraciones (S-17) `+ 13` identificaciones del declarante (RF-196) | Escritura. **No es ventanilla**: RF-90 llega por llamada o SMS |
| Informar, descontar y objetar la diferencia en la liquidación del agente | escritura contable + salida al agente | RF-104, RF-143, RF-145 | 6 | **29** = `13` informes previos con evidencia (RF-104) `+ 13` descuentos (RF-143) `+ 3` objeciones `[ASSUMPTION: 20 % objeta]` | Escritura — **nueva** |
| Cerrar el giro y avisar al emisor | escritura + notificación | RF-64, RF-65 | 10 | **2 690** — RF-64 cierra cuando Elena cuenta los billetes, no antes | Escritura |
| Consultar estado — **las dos puntas** | lectura | RF-52, RF-53, RF-66, **RF-128** | 1 | **22 400** = `2 800 × 8` (S-06: `6` del emisor `+ 2` del receptor) — **el 19,3 % de todos los requests del sistema**, y la única familia que RNF-11 excluye de su medida | Lectura |
| Avisar por llamada o mensaje de texto (receptor y emisor) | **salida por canal de un tercero, por unidad** | Receptor: RF-25, RF-37, RF-41, RF-69, RF-75, RF-106, RF-156, RF-109, RF-120, RF-121, RF-124 · Emisor: RF-11, RF-14, RF-51, RF-60, RF-65, RF-67, RF-127 | **No se mide en requests** | **18 200 unidades** entregadas al tercero (`6,5 × 2 800`, S-14), más **32 760** escrituras propias: `18 200` constancias de envío (RF-98) y `14 560` registros de resultado de entrega (RF-131, sobre el `[ASSUMPTION: 80 %]` de unidades cuyo canal reporta resultado). RF-132 hace de la ausencia de constancia un estado —**no avisado**— y no una escritura más | Unidad de tercero + escritura. **Es la familia de escritura más grande del sistema: el 39 % del total** |
| Rehacer el giro cancelado por código perdido, con todos sus controles | escritura contable + tamizaje completo | RF-46, RF-117, RF-123, RF-134, RF-135 | 12 | **42** = `2 800 × 1,5 %` (S-19). **No suma un giro al volumen de negocio** —RF-134 conserva la cotización del cancelado y RF-135 no vuelve a cobrar la comisión— y sí suma una creación entera a la carga: sus `126` tamizajes ya están en la fila de arriba | Escritura |
| Traspasar el código al emisor y recibir la respuesta del propio receptor | escritura ilegible **dentro del módulo del desafío** | RF-11, RNF-15, RF-114, RF-125, RF-147, RNF-15, RNF-17 | 4 | **3 696** = `2 800 (RNF-15, un traspaso por giro) + 896 (RF-114, una captura por comprobación de S-16)`. RF-125 —confirmarle al operario que el código salió sin mostrárselo— viaja en la respuesta del mismo acto y **no agrega escritura durable** | Escritura |
| Dejar constancia de lo informado al emisor antes del efectivo | escritura de constancia, **una por giro con seis campos, no seis escrituras** | RF-73, RF-77, RF-96, RF-115, RF-116, RF-133, RF-136, RF-142 | 1 | **2 854** = `2 800` (una por giro: plazo de devolución RF-73, fecha de disponibilidad RF-77, retención máxima RF-96, plazo de aviso RF-115, comisión RF-136, margen RF-142) `+ 54` (RF-116, uno por cada rederivación de RF-91). RF-133 acota el aviso de RF-67 a `[ASSUMPTION: 1 hora]`, que es el techo que RF-115 promete | Escritura — **cuatro ítems más, la misma cuenta**: es una pantalla y una constancia, no seis |
| Devolver al emisor (retención vencida, cancelación, prescripción, intentos agotados, sin respuesta, sin punto capaz) | escritura contable | RF-32, RF-47, RF-50, RF-103, RF-111, RF-129 | 15 | **112** = `2 800 × 4 %` (S-13) | Escritura |
| Entregar la devolución en ventanilla y avisarla | escritura + notificación + ventanilla | RF-14, RF-71, RF-72, RF-74, RF-88, RF-106 | 12 | **95** = `112 × 85 %` retirado (S-13) | Escritura |
| Dar por prescrita la devolución que nadie retiró | escritura de cierre | RF-89, RF-137 | 4 | **17** = `112 × 15 %`. **Es el terminador que faltaba**: sin RF-137 este estado no cerraba nunca | Escritura — **nueva** |
| Custodiar y devolver el efectivo recibido sin giro creado | escritura de estado + devolución | RF-118, RF-138 | 6 | **6** = `3` custodias abiertas `+ 3` devueltas al vencer `[ASSUMPTION: 72 horas]` (S-21) | Escritura — **nueva** |
| Reportar a las dos autoridades el giro sobre el umbral | escritura + salida regulatoria | RF-17, RF-22, RF-139, RF-140 | 10 | **6** = `3` a la autoridad de origen (RF-17, `[ASSUMPTION: USD 10 000 por operación, o el que fije cada regulador si es menor]`) `+ 3` a la de destino (RF-139), con la fecha de nacimiento de las dos puntas que RF-140 exige | Escritura — **nueva** |
| Suprimir a pedido los datos de una persona | **búsqueda transversal + borrado parcial** | RF-81 | **400** — dos órdenes de magnitud sobre la más cara del camino crítico | **1,3** = `40/mes ÷ 30,4` (S-18) | Escritura. **1,3 requests al día que dictan una decisión de particionado en `A`** |

**Suma del desglose:** `115 791 requests/día`, repartidos en **83 885 escrituras** y **31 906
lecturas**. `115 791 / 86 400 = 1,34 req/s` de promedio; `× 11 = ` **14,7 req/s en pico**. Son
**29,96 escrituras por giro**, contra las `21,62` que este documento calculó sobre 137 ítems.

**De dónde salen las `23 358` escrituras que el backlog de hoy agregó sobre las `60 527` anteriores.**
La ronda anterior atribuía su propio delta de `9 798` a tres ítems en un pasaje, a seis en otro y a
ocho en un tercero; el único de los tres que reproducía la cifra era el de **ocho** —`2 926` de
tamizaje (RF-119, RF-123) `+ 3 696` del traspaso del código y la respuesta (RNF-15, RF-114) `+ 2 854`
de los plazos informados (RF-115, RF-116) `+ 280` de constancias (RF-98) `+ 42` del rehacer
(RF-117) `= 9 798`— y es el que este documento adopta. El delta de esta ronda se atribuye igual, y
suma **catorce ítems**:

| Qué lo agrega | Escrituras/día |
|---|---|
| Constancia de aviso sobre un canal recontado, más el resultado de entrega (RF-98, RF-131; RF-132 lo vuelve obligatorio) | `+18 760` |
| Informe de la diferencia de cierre de caja al agente (RF-141) | `+4 500` |
| Liquidación del agente: informe previo con evidencia, descuento y objeción (RF-104, RF-143, RF-145) | `+29` |
| Pago sin confirmación: estado y resolución automática (RF-144, RF-146) | `+27` |
| Devolución prescrita (RF-137) | `+17` |
| Identificación de quien declara una diferencia fuera del mostrador (RF-196) | `+13` |
| Custodia del efectivo sin giro y su devolución (RF-118, RF-138) | `+6` |
| Reporte a la autoridad de destino y fecha de nacimiento (RF-139, RF-140) | `+6` |
| **Total** | **`+23 358`** → `83 885` |

Del lado de la lectura el delta es `+5 850`: `5 600` de RF-128 —el receptor consultando sin depender
del emisor— y `250` de la acción ofrecible que RF-130 le muestra al operario. `26 056 → 31 906`.

**La comprobación que este documento se exigió a sí mismo.** Arriba se dijo que si el desglose por
peso cambiara el resultado en más de un orden de magnitud, habría que calcular por separado y sumar.
Se hizo la cuenta, normalizando el peso 10 a un core de 5 req/s: las escrituras dan
`493 679 / 10 = 49 368` escrituras equivalentes —**menos** que el recuento plano de 83 885, porque la
familia más numerosa, la constancia de aviso, es la más liviana— y las lecturas dan `44 142`
equivalentes, `1,38×` el recuento plano de 31 906, arrastradas por las 22 400 consultas de estado.
Ninguno de los dos mueve la cifra ni medio orden de magnitud:
`49 368 / 86 400 × 11 / 80 = 0,079` servidores de escritura. **El sistema sigue pidiendo menos de un
décimo de máquina por el camino ponderado, y catorce centésimas por el plano.**

### Lo que sí dimensiona: RNF-11, RNF-10 y la geografía

`0,14` no es un número de servidores: es la prueba de que la carga no es la restricción activa. El
número real sale de tomar el **máximo** entre lo que pide la carga y lo que piden los umbrales de
servicio, y aquí manda el segundo término por dos órdenes de magnitud.

| Plano | Por qué existe | Nodos | De dónde sale |
|---|---|---|---|
| Escritura del giro | RNF-11 pide 99,9 % **sobre crear y pagar**, RNF-06 exige un solo estado del giro entre el centro y el punto, y **RNF-16** exige que ninguna entrega difiera de la cifra que el emisor vio: los tres viven del mismo plano. Un plano de escritura, no tres | **3** | Quórum que tolera una caída sin gastar los 43,2 min/mes del presupuesto de error |
| Réplica de lectura en destino | Dos países de destino (RNF-12, RNF-14) y RNF-10 con 900 s de margen: alcanza réplica asíncrona. Dos nodos por país para no caer a cero con una máquina | **4** = `2 × 2 países` | RNF-10, RNF-12 |
| Consulta de las dos puntas | RF-52, RF-53, RF-66 del lado del emisor y **RF-128 del lado del receptor**, que el backlog agregó y que no puede depender del emisor. **RNF-11 la excluye explícitamente de su medida**, y esa exclusión —no su tamaño— es lo que la separa: son el `19,3 %` de los requests, y aunque fueran el `2 %` seguirían sin poder compartir suerte con la escritura, porque lo que no se mide no puede arrastrar a lo que sí | **2** | RNF-11 por exclusión |
| Cumplimiento y tamizaje | RF-26, RF-27 y RF-97 llaman a listas externas cuya latencia y disponibilidad SendIt no fija. Aislarlo evita que una lista lenta consuma el techo de `2,3 s` por request que este paso deriva de RNF-09, que **es P0 y se estrechó** cuando RF-119 sumó el tamizaje del receptor y RF-136, RF-142 y RF-125 sumaron pasos a la misma creación | **2** | RNF-09, RF-26, RF-119 |
| Módulo del desafío — **el quinto plano, y ya lo era** | `D`(f) exige que la llave del verificador **nunca salga del módulo** y que la derivación corra adentro (RF-114, RNF-17): es una frontera de proceso y de credenciales, no una biblioteca. Compartir plano con el giro le daría al mismo host la llave y los datos que protege. **RNF-15 y RF-114 lo ensanchan sin agregar plano**: el código deja de pasar por la pantalla del mostrador y la respuesta deja de digitarla el operario, de modo que los `3 696` actos diarios de esa fila del desglose entran acá y no en el plano del giro. RNF-15 le agrega la única regla de negación que el plano ejerce —un código ya entregado no se vuelve a consultar— y RF-125 la única de afirmación: confirmarle al operario que salió, sin mostrárselo | **2** | Par mínimo para que RNF-11 no dependa de una sola máquina en el camino de pago de RF-69 y RF-122 |
| **Total** | `3 + 4 + 2 + 2 + 2` | **13** | `max(carga 0,14; piso 13)` |

`servidores = max(carga / capacidad; piso de disponibilidad y geografía) = max(0,14; 13) = ` **13**.

**Un sexto plano candidato, que este paso nombra y no decide.** RF-98, RF-131 y RF-132 convirtieron
la constancia de aviso en la familia de escritura más grande del sistema —`32 760` de `83 885`, el
`39 %`— y le dieron estado propio: *no avisado* es ahora una condición que hay que poder derivar y
reintentar, no un hueco en un log. Hoy esas escrituras viajan en el plano del giro. Si merecen plano
propio no lo decide `E`: es una caja de [`L`](../L-listar-componentes/README.md) y una frontera de
[`D`](../D-disenar-servicio/README.md). Lo que `E` aporta es el número, y el número dice que ya no es
un adaptador.

**Y una nota de prioridad que el backlog acaba de mover:** el término que manda es RNF-11, que es
**P1**; el que acota la latencia de la atención es RNF-09, que pasó a **P0**. La cifra de servidores
la dicta el requerimiento menos prioritario de los dos, y el más prioritario no la dicta sino que la
acota por el otro lado —180 s por atención, de los que este paso deriva `2,3 s` por request bajo el
supuesto `E-01`— sin pedir una máquina más.

**Y la consecuencia para `E`-escalar, que es lo que este paso realmente entrega:** para que el
término de carga alcance al término de disponibilidad, el volumen tendría que multiplicarse por
`13 / 0,14 = 93`, es decir **260 000 giros diarios**, que son `USD 78 M` al día y una cuota del
46 % de los dos corredores. **El backlog de 155 ítems acercó ese horizonte en un tercio** —eran
`364 000` sobre 137 ítems— y lo acercó sin mover una sola caja. Antes de eso se rompen otras tres
cosas, y ninguna se arregla con servidores: la **cuota diaria del operador de telefonía** (cálculo 3,
punto 2b), el **efectivo de la caja del punto** (RF-92, RF-95) y el **caudal de la cola de
cumplimiento** (71 casos/día contra cuántos analistas). Ese es el orden en que este sistema se rompe.
---

## Cálculo 2 — Almacenamiento requerido

El método: **determinar los tipos de dato → estimar el espacio de cada tipo → agregar y multiplicar
por el volumen diario** — y aquí, obligatoriamente, **por los años de retención**, que es el paso
que el método del material no tiene porque su ejemplo no está regulado.

### Qué tipos de dato tiene una remesa, y cuál domina

La intuición engaña. El instinto dice que lo que ocupa es la transacción, y una transacción es una
fila de unos pocos cientos de bytes: quién manda, a quién, cuánto, cuándo. Si SendIt fuera solo
eso, el almacenamiento no sería un problema de arquitectura.

**Lo que ocupa es la evidencia.** Tres familias:

1. **La prueba de quién es cada quien** — imágenes de documento de identidad y la fotografía de
   contraste. Son binarios de cientos de kilobytes o megabytes y no se borran cuando la persona deja
   de ser cliente. **El comprobante de domicilio se retiró en la ronda 12**: ningún título lo exige,
   y agregarlo por cuenta de este paso habría metido un dato personal más bajo `RNF-01` y `RF-81` sin
   requerimiento que lo pidiera. **RF-80 y RF-160 los piden de las dos puntas**, emisor y receptor,
   así que la unidad no es «una persona por giro» sino dos: quien entrega y quien cobra,
   cada una capturada en su mostrador y en su país. Es la partida que domina el cálculo, y este
   backlog la duplicó.
2. **La prueba de que se tamizó** — el resultado del contraste contra las listas de personas y
   entidades sancionadas, con la lista, su versión y su fecha. **Son cuatro evidencias por giro, no
   dos, y el backlog las partió así a propósito:** RF-26 tamiza al emisor y RF-119 al receptor
   designado, **las dos antes de aceptar el efectivo** —de modo que el sistema se detiene en vez de
   revertir—, RF-27 vuelve sobre el receptor contra las listas vigentes al autorizar el pago, y
   RF-97 retamiza cuando una lista cambia. Se guardan **haya o no coincidencia**: la ausencia
   también hay que poder demostrarla, y una auditoría necesita saber contra qué versión de qué lista
   se aprobó lo que se aprobó. RF-123 obliga a repetir el juego entero sobre el giro rehecho.
3. **El registro inalterable** — el asiento contable de cada movimiento y la traza de auditoría que
   RF-54 asocia a la identidad de quien ejecutó cada acto y RNF-03 impide modificar o eliminar. Esta
   última crece con las **lecturas**, no solo con las escrituras: RNF-04 exige traza de todo acceso a
   datos de identidad, con autor, momento y giro, así que cada consulta que Kevin hace sobre un
   expediente es una fila más.

Y sobre todo eso cae un multiplicador que el ejemplo de YouTube no tiene: **la retención
regulatoria**. YouTube se estima en «TB diarios», y ahí se detiene. **Aquí el diario no es el
resultado: es un factor.** RNF-03 y RF-18 fijan la conservación en el plazo más largo de los dos
reguladores que tocaron el giro, con un piso de 5 años, y la calculan **por giro y no por política
global** — de modo que el multiplicador no es único: hay uno por corredor de RNF-12, y el agregado
se dimensiona contra el mayor. Una remesa se estima en `diario × 365 × años de retención`, porque el
dato de hace cinco años sigue ocupando disco por obligación legal. Un cálculo que se detiene en el
volumen diario subestima el total por dos órdenes de magnitud, y el piso de 5 años dice exactamente
por cuánto: el mínimo defendible del factor es `365 × 5`.

**Y una cuarta familia que va con signo menos, y tiene dos miembros, no uno.** RF-81 suprime a pedido
los datos personales de quien los entregó —y de nadie más— salvo los que el registro de actos debe
conservar. **RF-99 es el otro, y es el mayor de los dos por un factor de treinta:** obliga a
descartar la evidencia de identificación de todo emisor que se identificó y no llegó a crear un giro
**a los `[ASSUMPTION: 3 días]` que el propio RF-99 lleva escritos** —la cifra ya no la inventa este
paso—
—porque RF-01 corre antes de RF-79, y entre los dos caben el rechazo por límite (RF-08, RF-09), el
país no atendible (RF-19), la incompatibilidad de reguladores (RF-16) y el emisor que simplemente se
fue. Ese binario **entra al sistema** —y por eso aparece con signo más en el cálculo 3— pero no
llega al retenido. Restarlo no es opcional: retenerlo sería ilegal por la vía contraria a RF-81.
No es una excepción cosmética a las tres de arriba: recorta la familia 1, que es justamente la que
domina, y deja intactas la 2 y la 3, que RNF-03 declara inalterables. El efecto neto sobre
el total es pequeño y el efecto sobre el **diseño** no lo es, porque obliga a poder encontrar a una
persona a través de todos sus giros y a borrar parte de una fila sin romper lo que la referencia.
Un cálculo que ignore el término negativo se equivoca por poco; uno que ignore la operación que lo
produce se equivoca en el paso siguiente.

Debajo de la retención larga viven dos plazos cortos que no cambian el total pero sí **dónde está el
dato**. El primero es el de la retención: dura lo que fije el regulador más estricto de los dos
países del giro —**a falta de norma expresa, 72 h**, que es un piso y no un techo— así que el
tamaño del estado caliente de cumplimiento se calcula contra el plazo **más largo** de los
corredores de S-01, no contra el mínimo cómodo. El segundo es la prescripción: un giro es pagable 12
meses antes de que RF-49 lo vuelva no pagable. Y hay un tercero que corre *después* del cierre
aparente y que **el backlog acaba de cerrar por el otro extremo**: RF-89 mantiene disponible la
devolución no retirada hasta la prescripción del giro y **RF-137 la da por prescrita ahí**, dejando
de mantenerla disponible. Un giro devuelto no sale del dato caliente cuando se devuelve, sino cuando
prescribe — y **sale**, que es lo que antes no se podía decir. El cuarto plazo corto es el más nuevo
y el más corto: las `[ASSUMPTION: 72 horas]` de RF-138, tras las cuales el efectivo en custodia sin
giro creado (RF-118) se devuelve al emisor en vez de esperar indefinidamente. Todo lo demás es
archivo: dato que hay que conservar y casi nunca leer.

| Tipo de dato | Qué es | Tamaño unitario | Cuántos por giro | Volumen diario | Años de retención | Marca |
|---|---|---|---|---|---|---|
| Registro del giro | La fila del giro: emisor, receptor único (RF-03), país único (RF-04), punto elegido (RF-63), monto fijado (RF-06), código ilegible (RNF-15) y su historia de estados | 1,0 KB | 1 | **2,8 MB** | 8,7 | `[ASSUMPTION]` |
| Asiento contable | Recepción del efectivo (RF-79), fondeo del corredor (RF-20), descuento de la caja al pagar (RF-95), más los extra de devolución (RF-74) y corrección (RF-56) | 0,4 KB | 3,2 | **3,6 MB** | 8,7 | `[ASSUMPTION]` |
| Cotización producida y fechada (RF-07) | Par de monedas, tasa, comisión, sello de tiempo y autor. **No es una lectura cacheada de una tasa ajena**: es un acto del sistema | 0,3 KB | 1,3 | **1,1 MB** | 8,7 | `[ASSUMPTION]` |
| Documento de identidad (binario, RF-80: emisor **y** receptor) | Anverso, reverso y foto de contraste, comprimidos, ilegibles en reposo por RNF-01 | **500 KB** por captura · 2 KB por referencia | `0,619` capturas (S-03 en las dos puntas, más las que RF-99 descarta) **+ 2 referencias** | **878 MB** — el **86 %** del diario | 8,7 | `[ASSUMPTION: S-03]` |
| Pregunta y respuesta del desafío, ilegibles (RF-68, RNF-17) | Pregunta en claro, resumen con sal de la respuesta. RF-101 prohíbe transmitirla y RNF-17 mostrarla | 0,25 KB | 1 — coste fijo por giro | **0,7 MB** | 8,7 | `[ASSUMPTION]` |
| Intentos de respuesta al desafío (RF-82, RF-83) | Momento, punto y resultado de cada intento. Nunca la respuesta | 0,15 KB | `0,32` = `0,20 × 1,6` (S-16) | **0,13 MB** | 8,7 | `[ASSUMPTION: S-16]` |
| Resultado de tamizaje (RF-26, RF-119 y RF-27: **tres por giro antes del retamizaje**) | Lista, versión, fecha y veredicto. **La ausencia de coincidencia también hay que poder probarla**; el expediente completo solo cuando la hay | 2 KB sin coincidencia · **60 KB** con | `4,045` = `11 326 / 2 800` (RF-26 emisor + RF-119 receptor antes del efectivo + RF-27 al autorizar + RF-97 por cambio de lista, más los `126` que RF-123 repite sobre los rehechos) · `2 %` con coincidencia (S-08) | **26,0 MB** = `(4,045 × 2 KB + 0,02 × 60 KB) × 2 800` | 8,7 | `[ASSUMPTION: S-08]` |
| Acumulado de cobros por identidad de receptor (RF-93) | Clave estable de receptor, contador y la ventana de `[ASSUMPTION: 30 días corridos]` que RF-09 y RF-93 declaran. **Por identidad, no por giro** — es lo más parecido a un padrón que este sistema tiene | 0,2 KB por identidad | `0,45` = `1 / 2,2 cobros` (S-15) | **0,25 MB** | Vive mientras la ventana lo exija; se archiva con el último giro de esa identidad | `[ASSUMPTION: S-15]` |
| Caso de cumplimiento y su evidencia de liberación (RF-33, RF-87, RF-163, RF-127) | Motivo, derivación al segundo rol (RF-30), plazo del regulador más estricto (RF-31), el motivo de la liberación que RF-87 exige y que RF-163 obliga a mostrar, el aviso de retención de RF-37 a quien dejó de poder cobrar y el aviso de RF-127 al emisor cuando el giro deja de estar retenido | 40 KB | `0,0254` = 2 % de S-08 `+ 0,5 %` de RF-93 `+ 2 %` de los `42` rehechos de RF-123 → **71 casos/día** | **2,8 MB** | 8,7 | `[ASSUMPTION: S-08]` |
| Traza de auditoría de actos y de accesos (RF-54, RNF-04) | Autor, momento, giro y acto. **Crece con las lecturas**: RNF-04 exige traza de todo acceso a datos de identidad, así que cada consulta de Kevin es una fila | 0,35 KB | `30` ≈ 22 actos + 8 accesos a identidad — **subió con el desglose**: hay más escrituras por giro y RF-128 agrega accesos del lado del receptor | **29,4 MB** | 8,7 — y **RNF-03 la declara inalterable: no se suprime nunca, ni por RF-81** | `[ASSUMPTION]` |
| Declaración de caja al abrir y al cerrar (RF-76) — **por punto y turno, no por giro** | Efectivo declarado por el punto, dos veces por turno, haya cero giros o mil | 0,4 KB | `3,21` equivalentes por giro = `9 000 / 2 800` | **3,6 MB** | 8,7 | `[ASSUMPTION: S-12]` |
| Diferencia de cierre informada al agente (RF-141) — **por cierre, no por giro** | Efectivo esperado contra el declarado, y la diferencia entre los dos, en cada cierre de caja de los puntos del agente | 0,3 KB | `1,61` equivalentes por giro = `4 500 / 2 800` | **1,35 MB** | 8,7 | `[ASSUMPTION: S-12]` — **nueva, y es la segunda partida con piso** |
| Comprobante de entrega en destino | Recibo firmado por el receptor en el mostrador, digitalizado. Es la prueba de que Elena contó los billetes | 35 KB | `0,96` — un pago por cada giro no devuelto | **94,1 MB** | 8,7 | `[ASSUMPTION]` |
| Declaración de diferencia del receptor, su atribución y su liquidación (RF-90, RF-196, RF-59, RF-104, RF-143, RF-145) | Lo que el receptor declara **por llamada o SMS**, la identificación que RF-196 exige antes de admitirla, la atribución al punto, el informe previo con evidencia que RF-104 obliga a darle al agente, el descuento de RF-143 y la objeción de RF-145 | 12 KB | `0,005` (S-17) | **0,17 MB** | 8,7 | `[ASSUMPTION: S-17]` |
| Aviso por llamada o SMS y **la prueba de que llegó** (receptor: RF-25, RF-37, RF-41, RF-69, RF-75, RF-106, RF-156, RF-109, RF-120, RF-121, RF-124 · emisor: RF-11, RF-14, RF-51, RF-60, RF-65, RF-67, RF-127) | Dos registros, no uno: la constancia de envío que RF-98 obliga a conservar de cada unidad entregada al tercero —destinatario, canal, momento— y el **resultado de entrega** que RF-131 registra cuando el canal lo reporta, sin el cual RF-132 obliga a tratar al destinatario como **no avisado** | 0,3 KB la constancia · 0,1 KB el resultado | `6,5` constancias (S-14) `+ 5,2` resultados (`80 %` de las unidades) | **6,9 MB** = `(6,5 × 0,3 + 5,2 × 0,1) × 2 800` | 8,7 | `[ASSUMPTION: S-14]` — **la partida que más creció, y no mueve un centavo** |
| Plazos y cifras informados al emisor antes del efectivo (RF-73, RF-77, RF-96, RF-115, RF-116, RF-133, RF-136, RF-142) | Constancia de lo informado, **una fila con más campos y no más filas**: plazo de devolución (RF-73), fecha de disponibilidad (RF-77), duración máxima de la retención (RF-96), dentro de cuánto se le avisará una retención —techo `[ASSUMPTION: 1 hora]` que RF-133 fija y RF-67 tiene que respetar—, **la comisión que se le cobra (RF-136)** y **el margen que se aplica sobre la cotización (RF-142)**; más, aparte, dentro de cuánto debe responder a la oferta de otro punto (RF-116), vencido el cual RF-111 devuelve | 0,35 KB | `1,019` = `1` (todo giro) `+ 0,019` (RF-116, uno por rederivación) | **1,0 MB** | 8,7 | `[ASSUMPTION]` |
| Giro rehecho tras la pérdida del código (RF-46, RF-117, RF-123) | Registro nuevo, vínculo al cancelado, y la constancia de que se conservó la cotización de RF-06 y **no** se volvió a cobrar la comisión. Sus tamizajes y sus avisos están en sus propias filas | 1,4 KB | `0,015` (S-19) | **0,06 MB** | 8,7 | `[ASSUMPTION: S-19]` |
| Traspaso del código y captura de la respuesta (RNF-15, RF-114) | Constancia de que el código llegó al emisor **sin pasar por la pantalla del mostrador** y de que la respuesta la entró el propio receptor. Nunca el código ni la respuesta: RNF-15 y RNF-17 los mantienen ilegibles, y RNF-15 lo mantiene no reconsultable para el mostrador | 0,3 KB | `1,32` = `1` (RNF-15) `+ 0,32` (RF-114, S-16) | **1,1 MB** | 8,7 | `[ASSUMPTION]` |
| Devolución al emisor, su disponibilidad y **su prescripción** (RF-32, RF-47, RF-50, RF-89, RF-103, RF-111, RF-129, RF-137) | Motivo, monto en la moneda que el emisor entregó (RF-88), comisión devuelta (RF-74), punto que el emisor eligió (RF-72) y, al vencer el plazo, la constancia de que RF-137 la dio por prescrita | 1,6 KB | `0,04` (S-13) | **0,18 MB** | 8,7 — **caliente hasta 12 meses y no más**: RF-89 no deja archivar la devolución no retirada y RF-137 la cierra al prescribir | `[ASSUMPTION: S-13]` |
| Efectivo en custodia sin giro creado y su devolución (RF-118, RF-138) | El estado único que el operario puede leer y retomar, y la constancia de la devolución al vencer `[ASSUMPTION: 72 horas]` | 1,0 KB | `0,002` (S-21) | **0,006 MB** | 8,7 | `[ASSUMPTION: S-21]` — **nueva** |
| Pago sin confirmación y su resolución (RF-144, RF-146) | El estado único del pago cuya confirmación no llegó del punto al centro, y el resultado de resolverlo contra el registro del centro sin el operario | 1,0 KB | `0,010` (S-20) | **0,03 MB** | 8,7 | `[ASSUMPTION: S-20]` — **nueva** |
| Reporte a las dos autoridades (RF-17, RF-22, RF-139, RF-140) | Lo que se reportó, a qué autoridad, contra qué umbral y con la fecha de nacimiento de las dos puntas que RF-140 obliga a informar | 50 KB | `0,002` = `6 / 2 800` (S-05) | **0,30 MB** | 8,7 — el plazo más largo de los dos reguladores | `[ASSUMPTION: S-05]` |
| **Supresión a pedido (RF-81)** — término **negativo** | Borra la evidencia de identidad de quien la entregó. **Nunca la traza**: RNF-03 prevalece sobre toda supresión | **−700 KB** por pedido (≈ 1,4 capturas) | **−0,00046** = `40 pedidos/mes ÷ 85 120 giros/mes` | **−0,9 MB** | Se resta del retenido, jamás del registro de actos | `[ASSUMPTION: S-18]` |
| **Descarte de evidencia sin giro (RF-99, a los `[ASSUMPTION: 3 días]` que el ítem lleva escritos)** — término **negativo**, el mayor de los dos | La captura del emisor que se identificó (RF-01) y no llegó a que se registrara la recepción de su efectivo (RF-79): rechazado por límite, país no atendible, reguladores incompatibles, o se fue | **−500 KB** por captura | **−0,019** = `54 descartes/día ÷ 2 800 giros` | **−27,0 MB** — **30× lo que resta RF-81** | Nunca entra al retenido, aunque sí al ancho de banda de entrada | `[ASSUMPTION: 6 % de las identificaciones no terminan en giro]` |

### Agregado

| | Fórmula | Valor | Marca |
|---|---|---|---|
| Espacio por giro | suma de los tipos por su multiplicidad | `376,2 KB brutos − 9,64 KB (RF-99) − 0,32 KB (RF-81) = ` **366,2 KB** | Derivado. El binario de identidad son `313,5` de esos `376,2`: **el 83 %**. La verificación de abajo pasa. Los `3,51 KB` que los ítems nuevos agregaron al bruto **ya no son tamizaje**: `+1,75` la traza que crece con las escrituras y con los accesos de RF-128, `+0,97` la constancia de aviso y su resultado de entrega (RF-98, RF-131, RF-132), `+0,48` el informe de diferencia de cierre al agente (RF-141), `+0,15` los seis campos que ahora lleva la constancia de lo informado antes del efectivo (RF-136, RF-142 sobre RF-115, RF-116), `+0,10` los reportes a la autoridad de destino (RF-139, RF-140) y `+0,06` entre la cadena de la diferencia (RF-196, RF-104, RF-143, RF-145), la custodia (RF-118, RF-138), el pago sin confirmación (RF-144, RF-146) y la prescripción de la devolución (RF-137) |
| Almacenamiento diario | `espacio por giro × giros por día` | `366,2 KB × 2 800 = 1 025 360 KB = ` **1,03 GB/día** | Derivado. Para escala: YouTube, en el ejemplo del material, hace `52 TB` diarios — **51 000 veces esto** |
| Almacenamiento retenido | `diario × 365 × años de retención (S-09, ≥ 5)` | Los dos reguladores no piden lo mismo: **5 años** en el corredor peruano, **10 años** en el mexicano `[ASSUMPTION]`. S-09 obliga a tomar el máximo **por giro**, así que el multiplicador se pondera por el reparto de S-01b: `0,26 × 5 + 0,74 × 10 = 1,3 + 7,4 = ` **8,7 años**. → `1,0254 GB × 365 × 8,7 = 3 256 GB = ` **3,3 TB** | Derivado. Piso defendible si los dos pidieran 5 años: `1,0254 × 365 × 5 = ` **1,87 TB**. Techo si los dos pidieran 10: **3,74 TB**. **Detenerse en el diario habría dicho `1 GB` en vez de `3 300 GB`: los dos órdenes de magnitud que el método del material no tiene por qué contemplar y este caso sí** |
| Almacenamiento caliente | la fracción del retenido que todavía es pagable: `diario × 365 × 1` por los 12 meses de prescripción (S-11). **Las devoluciones no retiradas caen dentro de esa ventana, no fuera**, y RF-137 las cierra al llegar a ella | `1,0254 GB × 365 × 1 = ` **374 GB ≈ 0,37 TB**, el `374 / 3 256 = ` **11,5 %** del retenido. **Este cálculo se rehízo porque la frase que lo justificaba dejó de ser cierta:** este documento decía que «un giro devuelto no cierra» y cifraba el caliente contra un estado sin terminador. **RF-137 le puso terminador** — da por prescrita la devolución que nadie retiró y deja de mantenerla disponible—, así que el `0,6 %` de los giros que quedaba abierto (`17/día`, `17 × 365 × 366,2 KB = 2,27 GB` en régimen) sale del caliente **al mismo tiempo que todo lo demás** y no después. La cifra no se mueve —el `11,5 %` era y sigue siendo doce meses de diario, porque esas devoluciones **ya estaban dentro** de la ventana y nunca fueron aditivas— pero la afirmación sí: eran `2,27 GB` sin fecha de salida y ahora tienen una | Derivado. El otro `88,5 %` es archivo: dato que hay que conservar y casi nunca leer, y que por tanto **no tiene por qué vivir donde vive el giro pagable**. **Lo que RF-137 elimina no son gigabytes: es un estado abierto**, y un estado abierto en un libro contable es lo que impide decir cuándo se puede archivar una partición entera |
| Almacenamiento independiente del giro | identidad y verificación de un emisor identificado en ventanilla que no llegó a crear giro (RF-01 corre antes de RF-79), el **efectivo ya recibido sin giro creado** que RF-118 deja en un estado único y RF-138 devuelve a las 72 h, y las declaraciones de caja de RF-76 con los informes de cierre de RF-141, que existen aunque el punto no pague nada en todo el turno | Caja: `9 000 × 0,4 KB = 3,6 MB/día` → `× 365 × 8,7 = ` **11,4 GB**. Diferencias de cierre (RF-141): `4 500 × 0,3 KB = 1,35 MB/día` → **4,3 GB**. Capturas de RF-99 mientras esperan el descarte, a los `[ASSUMPTION: 3 días]` que el ítem lleva escritos: `54 × 500 KB × 3 días = ` **81 MB** en régimen. Acumulados por identidad de receptor (RF-93): `39 000 × 0,2 KB = ` **7,8 MB/mes**. Efectivo sin giro de RF-118 (S-21): `3 × 1,0 KB/día` → **9,5 MB** | Derivado. Suma `15,8 GB`: irrelevante en el total y **el único piso que no baja cuando el volumen baja** — un día sin un solo giro sigue escribiendo 9 000 declaraciones de caja y 4 500 informes de diferencia |
| **Menos: lo suprimido a pedido** | `pedidos (S-18) × lo que RF-81 puede borrar`, que es la evidencia de identidad y no la traza. Se resta al retenido, nunca al registro de actos | RF-81: `40 pedidos/mes × 700 KB × 12 × 8,7 años = 2,92 GB` → el `2,92 / 3 256 = ` **0,09 %** del retenido. RF-99: `27,0 MB/día × 365 × 8,7 = 85,7 GB` → el `85,7 / 3 256 = ` **2,6 %**, treinta veces más | Derivado. **Ninguno de los dos mueve la cifra; los dos mueven el diseño.** RF-81 obliga a encontrar a una persona *a través de* todos sus giros —el eje por el que el libro contable no está particionado— y RF-99 obliga a un ciclo de vida del binario que empieza **antes** de que exista el giro al que colgarlo y termina a los 3 días que el propio ítem fija |

**Verificación mínima antes de dar por buena la cifra:** si el binario de identidad no es la partida
más grande, o se contó una identidad por giro en vez de las dos que pide RF-80, o el cálculo omitió
la retención, o supuso que solo se guarda evidencia cuando hay coincidencia, o restó la supresión de
RF-81 contra la traza de auditoría en vez de contra la evidencia. Los primeros cuatro errores
producen un número demasiado pequeño y demasiado creíble; el último produce un número que además es
ilegal.

---

## Cálculo 3 — Ancho de banda requerido

El método: **data de entrada por día → data de salida por día → dividir entre 86 400 s.**

| Paso | Qué se cuenta | Valor | Marca |
|---|---|---|---|
| 1. Entrada por día | Lo que sube al sistema: las capturas de identidad de las dos puntas que RF-80 conserva, respuestas de las listas de sanciones, declaraciones de caja de RF-76, los **resultados de entrega que el operador de telefonía devuelve** y que RF-131 registra, y las confirmaciones de cobro que suben desde los puntos de atención —incluida la ráfaga que sube un punto al recuperar la conexión y reconciliar su estado (RNF-08), que no es tráfico uniforme | `identidad 1 734 × 500 KB = 867 MB` **(el 71 %)** · `listas de sanciones 11 326 × 15 KB = 169,9 MB` · `comprobantes de entrega 2 690 × 35 KB = 94,2 MB` · `resto de escrituras de ventanilla 21 875 × 3 KB = 65,6 MB` — `83 885 − 1 734 − 11 326 − 9 000 − 2 690 − 32 760 − 4 500` · `resultados de entrega de RF-131: 14 560 × 0,5 KB = 7,3 MB` · `ráfaga de RNF-08: 45 puntos × 400 KB = 18 MB` · `caja 9 000 × 0,4 KB = 3,6 MB` → **1 225,6 MB ≈ 1,23 GB/día** | Derivado. Los `27,0 MB` de capturas que RF-99 descartará **entran igual**: en el cálculo 2 son un negativo, aquí son un positivo. **Y hay una corrección de método, no de ítem:** la fórmula anterior metía en «resto de escrituras de ventanilla» las `14 000` constancias de aviso, que el sistema **genera** y no recibe — `42 MB/día` que nunca subieron por el enlace. Hoy las `32 760` constancias de RF-98 y RF-131 y los `4 500` informes de RF-141 se restan del resto por la misma razón |
| 2. Salida por día | Lo que el sistema entrega: cotizaciones fechadas, estados consultados por **las dos puntas** (RF-52, RF-53, RF-66, RF-128), saldos de caja al operario antes de cada pago (RF-92), la acción ofrecible que RF-130 le muestra, el informe de diferencia de cierre que RF-141 le manda al agente y las descargas de evidencia que hace cumplimiento | `consultas de estado 22 400 × 8 KB = 179,2 MB` · `respuestas de ventanilla 20 750 × 6 KB = 124,5 MB` · `descargas de evidencia de cumplimiento 71 casos × 2 × 500 KB = 71 MB` · `cotizaciones 3 640 × 4 KB = 14,6 MB` · `diferencia de cierre al agente RF-141, 4 500 × 2 KB = 9,0 MB` · `saldos de caja RF-92 2 690 × 2 KB = 5,4 MB` · `constancia de lo informado al emisor, 2 854 × 1 KB = 2,9 MB` · `reportes a las dos autoridades RF-17, RF-22, RF-139 y RF-140, 6 × 50 KB = 0,3 MB` · `acción ofrecible RF-130, 250 × 1 KB = 0,25 MB` → **407,2 MB ≈ 0,41 GB/día** | Derivado |
| 2b. Salida por canal de terceros | **No se mide en bytes.** Avisos de voz y SMS entregados a un operador de telefonía —al receptor (RF-25, RF-37, RF-41, RF-69, RF-75, RF-106, RF-156, RF-109, RF-120, RF-121, RF-124) y al emisor (RF-11, RF-14, RF-51, RF-60, RF-65, RF-67, RF-127)—, contados en unidades y facturados por unidad. Van aparte porque dividirlos entre 86 400 no dice nada útil: lo que los limita es la cuota del tercero, no el enlace | **18 200 unidades/día** · en el día señalado `18 200 × 3,0 = ` **54 600 unidades**. Contra una cuota típica de `10 000/día` por país sin acuerdo comercial `[ASSUMPTION]`, los dos países dan `20 000` → **el día pico la excede por `54 600 / 20 000 = ` 2,7×**. Costo: `USD 910/día`, `USD 332 k/año`. **El agujero se abre antes que el pico:** `20 000 ÷ (6,5 × 3,0) = ` **1 026 giros/día**, muy por debajo de los `2 800` de llegada | `[ASSUMPTION: S-14]` — **este es el primer cuello de botella del sistema, y no se resuelve comprando servidores.** Elena no tiene datos móviles: un aviso no entregado no degrada, desaparece — y RF-132 obliga ahora a **anotar** que desapareció, tratando al destinatario como no avisado |
| 3. Entrada por segundo | `entrada por día / 86 400` | `1 225 600 KB / 86 400 = ` **14,2 KB/s** ≈ 0,12 Mbit/s | Derivado |
| 4. Salida por segundo | `salida por día / 86 400` | `407 200 KB / 86 400 = ` **4,7 KB/s** ≈ 0,04 Mbit/s | Derivado |
| 5. Pico | `resultado × P` | `(14,2 + 4,7) × 11 = ` **208 KB/s ≈ 1,7 Mbit/s** — entrada `156 KB/s`, salida `52 KB/s` | **Es la cifra que se usa.** Y hay una que no obedece a `P`: la ráfaga de RNF-08, `18 MB en 60 s = 300 KB/s`, que sola supera el pico entero. Se dimensiona contra ella, no contra los 208 KB/s |

Dos observaciones específicas de este caso:

- **La asimetría se invierte respecto del ejemplo del material.** En YouTube la salida aplasta a la
  entrada por tres órdenes de magnitud: se sube un vídeo y se descarga cien millones de veces. En
  SendIt el binario pesado —el documento de identidad— **entra** y casi nunca sale; entra dos veces
  por giro desde que RF-80 lo pide de las dos puntas, y lo que sale son respuestas de pocos
  kilobytes consultadas muchas veces. Con las cifras: YouTube `40 PB / 52 TB = 769×` a favor de la
  salida; SendIt `1 225,6 / 407,2 = 3,0×` a favor de la **entrada** — y la asimetría **se achicó**,
  por primera vez desde que se mide: los ítems nuevos del backlog cargan casi todos del lado de la
  salida (RF-128 consulta, RF-141 informa al agente, RF-139 reporta a la segunda autoridad) o no
  tocan el enlace en absoluto (las constancias de RF-98, que el sistema se escribe a sí mismo). La
  única salida pesada del sistema siguen siendo los `71 MB/día` que cumplimiento descarga de
  evidencia, y es el `71 / 407,2 = ` 17 % de toda la salida generada por menos del 0,1 % de las
  operaciones.
- **Dividir entre 86 400 supone que la carga es uniforme, y no lo es.** El resultado del paso 3 es
  un promedio contra el que no se dimensiona nada. La cifra que se usa es la del paso 5.

---

## Qué invalida esta estimación

Se registra aquí para que el paso siguiente sepa sobre qué está parado.

| Si cambia… | Se recalcula | Y hay que revisar |
|---|---|---|
| **La cuota de mercado del lanzamiento (0,5 %) o el ticket promedio (S-05)** | **Los tres cálculos, en proporción directa** | Nada, mientras no cruce un orden de magnitud: `0,14` servidores de carga aguantan `×93` antes de alcanzar el piso de 13. Es el supuesto del que más depende la cifra y el que menos cambia la arquitectura |
| **El reparto entre corredores (S-01b, 26 % / 74 %)** | El multiplicador de retención del cálculo 2: `8,7 años` se mueve entre `5` y `10` | `A` — la política de conservación es **por giro**, no global; el reparto solo elige contra qué extremo se dimensiona el agregado |
| El número de corredores (S-01, anclado en RNF-12) | Los tres cálculos | `D` — otra red afiliada que sincronizar, con otra calidad de conexión; `A` — otro plazo de conservación en el máximo por corredor |
| Los años de retención (S-09, anclado en RNF-03 y RF-18) | Almacenamiento | `A` — la política de retención por entidad, que es por giro y no global |
| El plazo de retención o el de prescripción (S-10, S-11) | Almacenamiento caliente, y el caudal de casos de cumplimiento | `E` (escalar) — el tamaño en régimen de la cola de cumplimiento, que se mide contra el plazo más largo de los corredores y no contra el piso de 72 h |
| El factor de pico (S-07) | Servidores y ancho de banda | `E` (escalar) — el tramo en que el sistema se rompe |
| La tasa de coincidencias (S-08) | Almacenamiento | `D` — dónde corre el tamizaje; `L` — el componente que lo ejecuta |
| El tamaño de la red afiliada o sus turnos (S-12) | Servidores y almacenamiento, por el piso de RF-76 que no depende del volumen | `E` (escalar) — el tramo más bajo, que ya nace con carga aunque no haya giros |
| La tasa de devolución o la de retiro (S-13) | Operaciones de ventanilla y almacenamiento caliente, por RF-89 | `D` — el ciclo de vida del giro, que no termina en el pago |
| El coste o la cuota del canal de voz y SMS (S-14) | El costo por giro, no el cómputo | `E` (escalar) — es un candidato a cuello de botella que no se resuelve con servidores; `L` — el componente que habla con el tercero |
| La proporción de códigos perdidos que se rehacen (S-19, anclada en RF-46, RF-117 y RF-123) | Las operaciones de ventanilla (`2,13` por giro), los tamizajes (`126/día`) y los avisos de base repetidos al receptor (`0,045` por giro) | `E` (escalar) — el caudal de la cola de cumplimiento, que gana su tercera fuente; `D` — el ciclo de vida de un giro que puede volver a nacer conservando la cotización de RF-06 |
| El reparto de avisos entre receptor y emisor (S-14, y quién es el destinatario de cada RF) | El factor de unidades por giro y, con él, **el tramo en que se agota la cuota del tercero**. Mover un aviso de una punta a la otra no cambia el total; agregar uno sí | `E` (escalar) — es el primer cuello y el más sensible: `6,5 × 3,0` unidades en el día señalado agotan `20 000` en `1 026` giros/día |
| El acumulado de cobros del receptor (S-15, anclado en RF-93 y su ventana de `30 días corridos`) | El caudal de la cola de cumplimiento, que gana una fuente de retención nueva | `E` (escalar) — el primer cuello de botella; `D` — la clave por la que se cuenta del lado receptor |
| El volumen de supresiones (S-18) | Almacenamiento, con signo menos | `D` — poder borrar la evidencia sin tocar la traza, que RNF-03 no deja mover |
| **La constancia de aviso y su prueba de entrega (RF-98, RF-131, RF-132)** | El desglose de escrituras, que hoy le debe `32 760` de `83 885` — el `39 %` — y el espacio por giro, que le debe `0,97` de los `3,51 KB` nuevos | `D` y `L` — es el candidato a **sexto plano**: la familia de escritura más grande del sistema vive hoy en el plano del giro y tiene estado propio (*no avisado*), que RF-132 obliga a poder derivar |
| **El terminador de la devolución no retirada (RF-137)** | Nada en la cifra: los `2,27 GB` que cerraba ya estaban dentro de la ventana de 12 meses. Sí la **frase**: «un giro devuelto no cierra» dejó de ser cierta | `A` — el ciclo de vida del giro tiene ahora un estado final para todas sus ramas, y eso decide cuándo se puede archivar una partición entera |
| Un requerimiento funcional nuevo en el backlog | Los tres | Todo lo de aguas abajo |

---

## Nota sobre las dos clases de iteración

[`ITERACIONES.md`](../ITERACIONES.md) registra dos cosas que se llaman «iteración» y **no son la
misma**:

- **Iteración del diseño** (*top down*) — el mismo diagrama de componentes, dibujado otra vez y más
  abierto. Es la que el enunciado exige mostrar, ocurre en
  [`L`](../L-listar-componentes/README.md) y la define el
  [ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md).
- **Iteración del EVAL** — la pasada de evaluación que cambia una decisión del backlog.

Este paso se ve afectado por las dos, por vías distintas: una iteración del EVAL que cambia el
backlog obliga a recalcular; una iteración del diseño no mueve ninguna cifra, pero puede revelar un
componente cuya carga nadie estimó.
