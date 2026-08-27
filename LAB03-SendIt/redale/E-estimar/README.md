# E — Estimar

> Paso 2 de [R.E.D.A.L.E.](../README.md) · anterior:
> [**R** — backlog de requerimientos](../R-requerimientos/backlog.md) · siguiente:
> [**D** — Diseñar el servicio](../D-disenar-servicio/README.md) · bitácora:
> [`ITERACIONES.md`](../ITERACIONES.md)

**Estado: calculado.** Las tres cifras están abajo, con su aritmética a la vista: **11 servidores**,
**3,2 TB retenidos** (1,01 GB/día) y **1,6 Mbit/s en pico** (196 KB/s). Ninguna sale del enunciado
—el enunciado no da ni una cifra— y por eso cada entrada lleva su `[ASSUMPTION: ...]` con la
calibración contra la que se defiende. Las divisiones se muestran enteras: esto se audita
dividiendo, no creyendo.

**El hallazgo que este paso entrega a `D`, antes que las cifras:** la carga de SendIt pide `0,09`
servidores. Lo que pide once es RNF-11 y la geografía de los dos corredores. Este sistema no se
rompe por CPU — se rompe por la cuota del canal de voz y SMS y por el efectivo de la caja del punto,
y ninguna de las dos se arregla comprando máquinas.

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
desafío (RF-12, RNF-17), y se comprueba una vez, en el mostrador de destino: tampoco es un login. No
hay padrón que contar ni login que medir. Dimensionar sobre «usuarios registrados» mediría un
sistema que no es este.

**Con una excepción que hay que declarar, porque es la única.** RF-58 obliga a contar cuántos giros
cobró un mismo receptor en la ventana vigente, y RF-93 retiene el giro de quien superó ese
acumulado. Contar por identidad y no por giro exige una clave estable de receptor que persista
**entre giros** — y eso es lo más parecido a un padrón que este sistema tiene, del lado de Elena,
que ni siquiera es clienta. No es un padrón que se registre: se acumula solo, un cobro por vez. Se
dimensiona en el cálculo 2 como agregado por identidad, no como fila por giro.

Las unidades de carga de SendIt son tres. Las dos primeras salen del giro y se cuentan por día:
**giros por día** —la unidad de negocio, la que RF-01 a RF-14 crean y RF-34 a RF-41 pagan— y
**operaciones de ventanilla por día**,
que es la unidad de trabajo del operario y **no coincide** con la anterior: un giro consume al menos
dos ventanillas (la de creación y la de pago), y suma más cuando hay autorización de segundo rol
(RF-13), corrección (RF-56, RF-61), devolución al emisor —que es presencial y en efectivo (RF-71,
RF-72)—, declaración de diferencia del receptor en el mostrador (RF-90) o cobro derivado a otro
punto del país destino (RF-91), que consume dos ventanillas para un solo pago.

**Y hay una tercera unidad, que no deriva de ninguna de las dos.** RF-76 hace que cada punto de
atención declare su efectivo al abrir y al cerrar la caja: dos escrituras por punto y por turno,
haya cero giros o mil. RF-92 le suma una lectura de saldo antes de habilitar cada pago. La primera
escala con la **red afiliada** —con S-01, no con el volumen— y es la única carga que no se apaga
cuando el día está flojo; la segunda escala con los pagos. Contarlas juntas esconde que una tiene
piso y la otra no.

| Entrada | Qué cuenta | Valor | De dónde sale | Marca |
|---|---|---|---|---|
| **Giros por día** | Giros creados, medidos sobre el conjunto de corredores de RNF-12 | **2 800** | `0,5 % de un mercado de USD 61 300 M/año ÷ USD 300 de ticket ÷ 365` — derivación completa abajo | `[ASSUMPTION: S-01b · S-05]` |
| **Operaciones de ventanilla por día** | Atenciones presenciales: crear, pagar, autorizar, corregir, devolver, declarar diferencia, rederivar el cobro | **5 900** | `2 800 crear + 2 690 pagar + 84 autorizar (RF-13) + 8 corregir (RF-56, RF-61) + 95 entregar devolución (RF-71, RF-72) + 13 declarar diferencia (RF-90) + 54 rederivar (RF-91) + 179 identificar sin giro (RF-01 corre antes de RF-02) = 5 921` | Derivado — **2,11 ventanillas por giro**, no 2. La diferencia son 121 atenciones diarias que ningún giro explica |
| **Aperturas y cierres de caja por día** | `puntos activos × turnos × 2` (RF-76). No depende de los giros | **9 000** | `3 000 puntos × 1,5 turnos × 2 = 9 000` | `[ASSUMPTION: S-12]` — es **3,2 veces** el número de giros del día: la carga con piso es mayor que la carga de negocio |
| **Avisos al receptor por día** | Unidades de voz o SMS entregadas a un tercero (RF-25, RF-37, RF-41, RF-60, RF-75). Se pagan por unidad, no por byte | **13 720** | `4,9 unidades por giro × 2 800 = 13 720` — desglose en S-14. A USD 0,05 la unidad: `13 720 × 0,05 = USD 686/día`, **USD 250 k/año**, **USD 0,24 por giro** | `[ASSUMPTION: S-14]` |
| Giros por día en pico | `giros por día × P` | **8 400** | `2 800 × 3,0` — el componente **diario** de `P`, no el compuesto | `[ASSUMPTION: S-07]` |
| RPS — requests por segundo | Derivada, no supuesta: sale del desglose por operación del cálculo 1 | **0,89 promedio · 9,8 en pico** | `76 615 requests/día ÷ 86 400 s = 0,887` · `0,887 × 11 = 9,76` | Derivado |
| Almacenamiento requerido | Salida del cálculo 2, no entrada | **1,01 GB/día · 3,2 TB retenidos** | Cálculo 2 | Derivado |
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
el cálculo 2. Con una salvedad que el backlog agregó y que corre en contra: el giro **devuelto** no
cierra al devolverse. RF-89 mantiene la devolución disponible hasta la prescripción, así que sigue
vivo y consultable hasta doce meses después de haber dejado de ser un giro.

### Umbrales de servicio que este paso recoge

El backlog marca `[ASSUMPTION: umbrales de servicio de RNF-09 a RNF-11]` como *«Vigente — los
consume el paso `E`»*. Aquí es donde se consumen. Ninguno de los tres cabe en las tablas de
arriba, porque no son volúmenes sino restricciones: cada uno acota un cálculo distinto por un lado
distinto.

| RNF | Umbral declarado en R | Qué cálculo restringe | Cómo lo restringe | Valor derivado | Marca |
|---|---|---|---|---|---|
| RNF-09 | Operación de ventanilla en menos de 3 minutos, **incluida la verificación del documento** | Servidores | El presupuesto de máquina es lo que sobra de los 3 min después del tiempo humano de RF-01; es un techo de latencia por operación, no de throughput | `180 s − 150 s de tiempo humano = 30 s de máquina por operación`. Una creación encadena ≈ 9 requests sincrónicos → `30 / 9 = ` **3,3 s por request en p99**. Es un techo holgado: cabe la llamada externa a las listas (RF-26); no cabe una espera por el segundo rol de RF-13, y RNF-09 la mide aparte precisamente por eso | `[ASSUMPTION: 150 s de tiempo humano en RF-01 — pedir el documento, mirar la foto, tipear]` |
| RNF-10 | Giro fondeado disponible para cobro en destino en menos de 15 min desde su creación | Servidores y ancho de banda | Acota la ventana de propagación entre origen y destino, y con ella cuánto puede diferirse el trabajo de RF-20 y RF-36 | `15 min = 900 s` de ventana origen → destino. Una réplica asíncrona entre regiones propaga en ≈ 1 s: `900 / 1 = 900×` de margen. **Conclusión que reparte los servidores: RNF-10 no obliga a escritura síncrona multirregión**, así que hay un solo plano de escritura y réplicas de lectura en destino, no un quórum global | Derivado |
| RNF-11 | 99,9 % mensual, medido **sobre crear y pagar, no sobre consultar** | Servidores | Reparte la redundancia de forma desigual: la ruta de escritura se dimensiona con margen de disponibilidad, la de consulta (RF-52, RF-53) no | `43 200 min/mes × 0,001 = ` **43,2 min/mes** de presupuesto de error sobre crear y pagar. Un nodo solo no lo cumple → **3 nodos con quórum** en la ruta de escritura (tolera una caída); la de consulta queda excluida de la medida y se sostiene con **2** sin quórum | Derivado — **es el término que manda en el cálculo 1**, no la carga |

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
| S-01 | Corredores atendidos | Fija las monedas, los dos reguladores que RF-15 aplica al mismo giro, la red de **puntos de atención afiliados** en la que hay que sostener efectivo (RF-20) y los husos horarios del pico. Sin él no hay volumen que estimar ni reglas que aplicar | **Cerrado por RNF-12 y RNF-14**: dos corredores al lanzamiento — Estados Unidos → Perú y Estados Unidos → México. Un solo país de origen con **dos monedas de destino**, que es lo que RNF-14 exige desde el primer día. El primero es el que modela [Rosa](../../personas/Rosa.MD) | Dos corredores | **Cerrado** |
| S-01b | Reparto de los giros entre los dos corredores | S-09 fija la conservación **por giro y no por política global**, así que el multiplicador del cálculo 2 es el promedio ponderado de los dos plazos. Sin este reparto no hay ponderación: solo un rango de 5 a 10 años | La cuota diferenciada de la derivación de arriba: `USD 80 M` en Perú (5,0 % de su corredor) y `USD 226,5 M` en México (0,38 % del suyo). SendIt entra por donde tiene red y persona modelo, no por donde hay más dinero | **26 % Perú · 74 % México** | `[ASSUMPTION]` |
| S-02 | Emisores distintos por mes | Dimensiona el almacenamiento de la evidencia de identidad que RF-80 conserva, y que persiste por el plazo de RNF-03 aunque el emisor no vuelva nunca. No es un padrón: es el recuento de identificaciones practicadas en ventanilla. Su gemelo del lado receptor no tiene supuesto propio porque no hay uno solo por giro: ver S-15 | El contraste *bottom-up* de arriba, que es aritmética y no opinión: `85 120 giros/mes ÷ 2 giros por emisor` | **42 500 emisores distintos/mes** | `[ASSUMPTION]` |
| S-03 | Proporción de giros que exigen captura nueva de identidad | Un emisor recurrente se identifica otra vez (RF-01 no admite excepción) pero puede no producir un binario nuevo. La proporción decide cuánto del cálculo 2 crece con los giros y cuánto con las personas | El patrón de [Rosa](../../personas/Rosa.MD): la misma emisora, quincena tras quincena | **30 % de los giros, por punta** — un emisor gira 24 veces al año y solo produce binario nuevo al alta, al renovar documento o cuando el anterior no es legible; en el año 1 la base crece, así que 1 de cada 3,3 giros trae captura nueva. El otro 70 % guarda una **referencia de 2 KB**, no una imagen | `[ASSUMPTION]` |
| S-04 | Giros por emisor al mes | Convierte emisores en giros por día, que es la unidad de carga del paso | El patrón de Rosa: quincenal, estable desde hace tres años | **2 giros/emisor/mes** | `[ASSUMPTION]` — declarado en su propia ficha |
| S-05 | Ticket promedio | No mueve el cómputo, pero decide cuántos giros cruzan el umbral de reporte transfronterizo (RF-17, RF-22) y cuántos el umbral reforzado que obliga a un segundo rol (RF-13) — y con ello cuántas operaciones de ventanilla extra aparecen | El rango de Rosa: USD 200–400 | **USD 300** (punto medio). Con él: `3 %` de los giros cruzan el umbral reforzado de RF-13 `[ASSUMPTION: USD 1 000]` → **84 autorizaciones de segundo rol al día**; `0,1 %` cruzan el umbral de reporte transfronterizo de RF-17 y RF-22 `[ASSUMPTION: USD 10 000]` → **3 reportes al día** | `[ASSUMPTION]` |
| S-06 | Consultas de estado por giro | **RF-52 y RF-53 la exigen como capacidad, y RF-66 le agrega el estado retenido con su fecha**: la consulta es carga requerida, no tráfico incidental. Es la operación de lectura dominante y la única que RNF-11 excluye explícitamente de su medida de disponibilidad | Lo que hoy obliga a Rosa a llamar por teléfono, ahora exigido por RF-52 | **6 consultas por giro** — Rosa consulta al salir de la ventanilla, antes de pasarle el código a Elena, el día que le dijo que fuera, y otra vez si no pasó nada. Es la operación más numerosa del sistema: `6 × 2 800 = 16 800/día`, el **22 %** de todos los requests | `[ASSUMPTION]` |
| S-07 | **Factor de pico** | Ver abajo | El ciclo de pago quincenal de Rosa y el calendario de fechas señaladas de los dos destinos. **Ningún RNF lo ancla**, y por eso es el supuesto más frágil de los grandes | **`P` = 11** = `3,0` (día señalado) `× 3,6` (hora del día). Ventana: **una hora**, dentro de un día señalado | `[ASSUMPTION]` |
| S-08 | Proporción de giros que disparan una coincidencia de tamizaje | La tasa decide el volumen de evidencia, que es lo que domina el almacenamiento, y RF-28 obliga a guardar separadas la coincidencia exacta y la homonimia — la abrumadora mayoría son homónimos | `[ASSUMPTION: sin fuente; el enunciado no da ninguna cifra de tamizaje]` | **2 % de los giros**, de los que **98 % son homonimia** (RF-28, RF-78) y 2 % coincidencia exacta: `2 800 × 0,02 = 56 casos/día`, de los que `56 × 0,02 ≈ 1` es exacto. RF-93 agrega `0,5 %` por acumulado de receptor → **70 casos de cumplimiento al día** | `[ASSUMPTION]` |
| S-09 | Años de retención regulatoria | Multiplica el almacenamiento diario por un factor que el ejemplo de YouTube no tiene | **Cerrado por RNF-03 y RF-18**: el plazo más largo de los dos reguladores del giro, con un piso de 5 años. Se calcula por giro y no por política global, así que el multiplicador del cálculo 2 no es único: es el máximo por corredor | ≥ 5 años | **Cerrado** |
| S-10 | Plazo de una retención | Acota cuántos giros retenidos coexisten: la cola no es un acumulado sin fin, es un caudal con tiempo de residencia. RF-31 le pone plazo y RF-32 la termina devolviendo al emisor | **Cerrado**: lo que fije el regulador más estricto de los dos países del giro; **a falta de norma expresa, 72 h**. Es un piso por defecto, no un techo — un regulador puede exigir más, y RF-31 obliga a obedecerlo. El tiempo de residencia se dimensiona **por corredor**, contra el plazo más largo, igual que S-09 | ≥ 72 h, por corredor | **Cerrado** |
| S-11 | Plazo de prescripción | Fija cuánto tiempo un giro creado sigue siendo pagable y por tanto vivo en el estado caliente antes de que RF-49 lo vuelva no pagable y RF-50 lo ponga a disposición del emisor. Separa el dato caliente del dato meramente retenido | **Cerrado**: 12 meses desde la creación del giro | 12 meses | **Cerrado** |
| S-12 | Puntos de atención activos y turnos por punto | Es la única entrada que no deriva del volumen: RF-76 escribe dos declaraciones de caja por punto y turno aunque no haya un solo giro, y RF-92 lee el saldo antes de cada pago. Fija además cuántos destinos ofrece RF-63 al emisor y cuántos puede alcanzar la rederivación de RF-91 | La red afiliada de los dos corredores de S-01, no la planta propia | **3 000 puntos activos · 1,5 turnos por punto**. Da `9 000` declaraciones de caja al día (RF-76) y `2 690` lecturas de saldo (RF-92). Nótese: `9 000 > 2 800` — **la carga que no se apaga es mayor que la que sí** | `[ASSUMPTION]` |
| S-13 | Proporción de giros que terminan devueltos, y cuánto tarda el emisor en retirar | Toda devolución es una operación de ventanilla más (RF-71 en efectivo, RF-72 en el punto que el emisor elija), un aviso más (RF-14) y un asiento más que incluye la comisión (RF-74). Y RF-89 la mantiene disponible hasta la prescripción: **un giro devuelto no cierra**, sigue caliente hasta 12 meses, así que esta proporción no mueve solo el cálculo 1 — mueve el almacenamiento caliente del cálculo 2 | Las tres fuentes de devolución ya en el backlog: retención vencida (RF-32), cancelación (RF-47) y prescripción (RF-50) | **4 % de los giros terminan devueltos** → `112/día`. De ellos, **85 % se retira dentro de 30 días** → `95` entregas de ventanilla al día; el **15 % restante** (`17/día`, `0,6 % de los giros`) queda abierto hasta la prescripción por RF-89 y **no sale del dato caliente** | `[ASSUMPTION]` |
| S-14 | Avisos al receptor por giro, y coste por unidad del canal | El canal de voz y SMS es de un tercero y se paga **por unidad entregada**, no por byte: es la única partida del paso cuyo costo no baja aunque el mensaje quepa en 140 caracteres. Un giro sin incidente ya gasta tres (RF-25, RF-41, RF-75); uno retenido gasta el cuarto (RF-37) y uno con diferencia el quinto (RF-60). El reintento de una entrega fallida cuenta como unidad nueva | La cuota que un operador de telefonía concede por país, que RNF-12 obliga a contar dos veces | **4,9 unidades por giro · USD 0,05 por unidad.** Al receptor: `3,0` de base (RF-25, RF-41, RF-75) `+ 0,20` pregunta del desafío (RF-69) `+ 0,025` retenido (RF-37) `+ 0,04` devuelto (RF-32, RF-47) `+ 0,01` cambio de lista (RF-97) `+ 0,02` re-aviso de RF-75 `+ 0,005` diferencia (RF-60) `= 3,30`. Al emisor: `0,96` cobrado (RF-65) `+ 0,04` devolución disponible (RF-14) `+ 0,025` retenido (RF-67) `+ 0,005` prescripción próxima (RF-51) `+ 0,005` diferencia (RF-60) `= 1,035`. Suma `4,34`, `× 1,12` de reintentos por entrega fallida `= 4,86` → **4,9** | `[ASSUMPTION]` |
| S-15 | Receptores distintos por mes, y cobros por receptor en la ventana | RF-58 cuenta los cobros de un mismo receptor y RF-93 retiene al que supera el acumulado: hace falta una clave de receptor estable entre giros, no una fila por giro. Y RF-80 conserva la evidencia de identidad **del receptor además de la del emisor**, de modo que el binario pesado del cálculo 2 se captura dos veces por giro y no una | El mismo patrón de S-02, del otro lado del mostrador: Elena cobra todos los meses y se identifica todas las veces | **39 000 receptores distintos/mes · 2,2 cobros por receptor** en la ventana de 30 días: `85 120 / 2,2 = 38 690`. El acumulado de RF-58 pesa `0,2 KB` **por identidad**, no por giro → `0,2 / 2,2 = 0,09 KB` por giro | `[ASSUMPTION]` |
| S-16 | Proporción de pagos que se resuelven por desafío, e intentos por pago | RF-68 obliga a registrar pregunta y respuesta en **todo** giro, así que el dato existe siempre y RNF-17 exige guardarlo ilegible en los dos lados del mostrador — coste fijo por giro, en el camino de escritura de la creación. Lo que varía es el consumo: RF-69 abre el desafío como salida al documento vencido, RF-82 acota los intentos y RF-12 los comprueba sin mostrarlos, así que un pago puede costar hasta `intentos` comprobaciones en vez de una | La proporción de documentos vencidos que hoy dejan a Elena sin cobrar, que es la tensión T3 del backlog | **Coste fijo: 1 escritura por giro** (RF-68 no admite excepción) → `2 800/día`. **Consumo: 20 % de los pagos** usan el desafío, a `1,6` intentos promedio (RF-82 los acota en 3) → `0,20 × 1,6 = 0,32` comprobaciones por giro → `896/día`. El DNI de Elena lleva catorce meses vencido: el 20 % no es un caso raro, es su caso | `[ASSUMPTION]` |
| S-17 | Proporción de pagos con declaración de diferencia en el mostrador | RF-90 le da al receptor un acto propio que antes no tenía, y cada declaración abre la cadena cara: atribución al punto (RF-59), aviso al receptor (RF-60), y si termina en corrección, un movimiento nuevo (RF-56) con autorización de un segundo rol (RF-61). Es baja en proporción y alta en operaciones por caso | `[ASSUMPTION: sin fuente; el enunciado no da ninguna cifra de diferencias]` | **0,5 % de los pagos** → `13/día`. Baja en proporción y cara por caso: cada una abre atribución (RF-59), aviso a los dos (RF-60), resolución aparte con el agente (RF-104) y, si termina en corrección, movimiento nuevo (RF-56) con segundo rol (RF-61) → `13 × 5 ≈ 65` actos diarios que nacen de 13 casos | `[ASSUMPTION]` |
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
| Hora del día | **3,6×** | Huso horario del emisor, no del receptor — y RNF-12 obliga a contar dos, uno por corredor, que pueden no solaparse. `15 % del día en 1 h → 0,15 × 24 = 3,6`. Los dos husos de origen (Este y Pacífico) achatan el pico tres horas; el 15 % ya lo contempla, y es por eso que no es 20 % | `[ASSUMPTION: S-07]` |

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
| 3. Carga objetivo | `RPS derivado del desglose de abajo × P` | escritura: `50 555 / 86 400 = 0,585 req/s`, `× 11 = ` **6,4 req/s** · lectura: `26 060 / 86 400 = 0,302 req/s`, `× 11 = ` **3,3 req/s** | Derivado |
| 4. Servidores | `carga objetivo / capacidad de servidor` | escritura: `6,4 / 80 = 0,080` · lectura: `3,3 / 800 = 0,004` · suma: **0,09 servidores** | Derivado — **un solo servidor cubre once veces la carga del pico** |

Donde el material obtiene `100 000 / 160 = 625 servidores`, SendIt obtiene `6,4 / 80 = 0,08`. No es
un error de método: es el resultado, y dice algo. Un sistema de remesas en efectivo mueve **dinero**,
no *bytes*: 2 800 giros diarios son `USD 840 000` al día atravesando la frontera con dos reguladores
encima, y caben en una máquina. **La dificultad de SendIt nunca fue el cómputo.** Lo que sigue —el
piso de disponibilidad, la cuota del canal de terceros, el efectivo de la caja— es donde está.

**Una advertencia que este caso obliga y el ejemplo del material no necesita:** un `request` de
SendIt no cuesta lo mismo que otro. Consultar el estado de un giro es una lectura; ejecutar un pago
es una escritura contable que toca varias filas, cruza la frontera del corredor —hacia el punto de
atención que entrega el efectivo, y hacia el regulador de destino cuyas reglas RF-15 obliga a
aplicar sobre el mismo giro— y no puede servirse desde caché. Estimar con un único «core = N req/s»
promedia dos cosas que no se promedian. Si el desglose por tipo de operación cambia el resultado en
más de un orden de magnitud, se calcula por separado y se suma.

**Y una corrección de perfil que RF-07 obliga:** cotizar **no es una lectura**. El sistema no
consulta una tasa ajena y la muestra: *produce y fecha* la cotización de la que sale el monto, y
RF-06 lo conserva sin recalcularlo durante toda la vida del giro. Eso es una escritura durable —una
por giro, en el camino crítico de RNF-09— y mueve el perfil de carga del sistema hacia la escritura
mucho antes de llegar al pago. Un dimensionamiento que la contara como lectura cacheable
subestimaría el eje que más caro escala.

Del lado del efectivo tampoco hay procesador que cobre a Rosa: **RF-02 hace que el efectivo entre
por la ventanilla**, contra un emisor ya identificado. La única frontera de cobro que este sistema
cruza es la de la liquidación con el agente (RF-24), que no está en el camino del giro.

**La tercera advertencia es de unidad, no de peso: el aviso al receptor no se mide en requests.** Es
una llamada o un SMS que entrega un operador de telefonía, con cuota diaria y precio por unidad, y
su latencia y su tasa de fallo no las fija este sistema. Cinco requerimientos se apoyan en él
—RF-25, RF-37, RF-41 y RF-75, los cuatro P0, y RF-60 en P1— y ninguno tiene alternativa: Elena no
tiene aplicación ni datos móviles, así que un aviso no entregado no degrada, **desaparece**. Se
dimensiona en unidades por día contra la cuota del tercero, no en RPS contra la capacidad de un
core, y por eso lleva fila propia en la tabla de entradas.

| Operación | Tipo | Requerimiento que la exige | Peso relativo | Volumen diario | Marca |
|---|---|---|---|---|---|
| Identificar al emisor contra documento | escritura + verificación externa | RF-01, RF-02 | 6 | **2 980** = `2 800 giros + 179 identificaciones sin giro` | Escritura |
| Conservar la evidencia de identidad de las dos puntas | escritura de binario | RF-80, RNF-01 | **40** — la más cara por unidad | **1 734** = `2 800 × 0,619 capturas` (S-03 en las dos puntas, más las 54 que RF-99 descartará) | Escritura |
| Registrar la pregunta y su respuesta al crear | escritura ilegible, una por giro | RF-68, RNF-17 | 2 | **2 800** = `1 × 2 800` — RF-68 no admite excepción | Escritura |
| Cotizar y fechar la cotización | **escritura durable** | RF-05, RF-06, RF-07 | 10 | **3 640** = `2 800 × 1,3` — RF-05 se cotiza más de una vez por giro cuando Rosa pregunta por dos montos | Escritura |
| Contar límites sobre la identidad del emisor | lectura agregada | RF-08, RF-09, RF-10 | 3 | **2 980** — una por creación intentada, antes de tocar el efectivo | Lectura |
| Contar los cobros del receptor en la ventana | lectura agregada **por identidad de receptor** | RF-58, RF-93 | 3 | **2 690** — una por pago | Lectura — y la única que no se resuelve con la clave del giro |
| Tamizar contra listas | lectura externa + escritura de evidencia | RF-26, RF-27, RF-28 | 12 | **8 400** = `2 800 × 3` — dos obligatorias (RF-26 al aceptar, RF-27 al autorizar) más una de retamizaje por cambio de lista (RF-97) | Escritura de evidencia |
| Crear el giro y emitir su código | escritura contable | RF-11, RF-13, RF-20 | 10 | **2 800** | Escritura |
| Declarar el efectivo al abrir y al cerrar caja | escritura, `puntos × turnos × 2` | RF-76 | 4 | **9 000** = `3 000 × 1,5 × 2` — **la operación más numerosa que no depende del volumen** | Escritura con piso |
| Informar al operario el efectivo del punto | lectura previa a cada pago | RF-92 | 1 | **2 690** | Lectura |
| Comprobar la respuesta del desafío sin mostrarla | lectura ilegible, hasta `intentos` por pago | RF-12, RF-69, RF-82 | 2 | **896** = `2 800 × 0,20 × 1,6` (S-16) | Lectura |
| Ejecutar el pago en destino | escritura contable + frontera | RF-34, RF-36, RF-85, RF-86, RNF-05 | **15** — la más cara del camino crítico | **2 690** = `2 800 × 0,96` (el 4 % restante se devuelve, S-13) | Escritura |
| Rederivar el cobro a otro punto del país destino | escritura de estado + segunda ventanilla | RF-91 | 6 | **54** = `2 690 × 2 %` `[ASSUMPTION]` — consume **dos** ventanillas para un solo pago, y RF-105 exige la respuesta del emisor en medio | Escritura |
| Declarar en el mostrador una diferencia de monto | escritura + atribución al punto | RF-90, RF-59 | 8 | **13** = `2 690 × 0,5 %` (S-17) | Escritura |
| Cerrar el giro y avisar al emisor | escritura + notificación | RF-64, RF-65 | 10 | **2 690** — RF-64 cierra cuando Elena cuenta los billetes, no antes | Escritura |
| Consultar estado | lectura | RF-52, RF-53, RF-66 | 1 | **16 800** = `2 800 × 6` (S-06) — **el 22 % de todos los requests del sistema**, y la única familia que RNF-11 excluye de su medida | Lectura |
| Avisar al receptor por llamada o mensaje | **salida por canal de un tercero, por unidad** | RF-25, RF-37, RF-41, RF-60, RF-75 | **No se mide en requests** | **13 720 unidades** entregadas al tercero, más **13 720** constancias de RF-98 que sí son escrituras propias (peso 2) | Unidad de tercero + escritura |
| Devolver al emisor (retención vencida, cancelación, prescripción) | escritura contable | RF-32, RF-47, RF-50 | 15 | **112** = `2 800 × 4 %` (S-13) | Escritura |
| Entregar la devolución en ventanilla y avisarla | escritura + notificación + ventanilla | RF-14, RF-71, RF-72, RF-74, RF-88 | 12 | **95** = `112 × 85 %` retirado (S-13). Los `17` restantes siguen abiertos hasta 12 meses por RF-89 | Escritura |
| Suprimir a pedido los datos de una persona | **búsqueda transversal + borrado parcial** | RF-81 | **400** — dos órdenes de magnitud sobre la más cara del camino crítico | **1,3** = `40/mes ÷ 30,4` (S-18) | Escritura. **1,3 requests al día que dictan una decisión de particionado en `A`** |

**Suma del desglose:** `76 615 requests/día`, repartidos en **50 555 escrituras** y **26 060
lecturas**. `76 615 / 86 400 = 0,89 req/s` de promedio; `× 11 = ` **9,8 req/s en pico**.

**La comprobación que este documento se exigió a sí mismo.** Arriba se dijo que si el desglose por
peso cambiara el resultado en más de un orden de magnitud, habría que calcular por separado y sumar.
Se hizo la cuenta, normalizando el peso 10 a un core de 5 req/s: las escrituras dan
`392 498 / 10 = 39 250` escrituras equivalentes —**menos** que el recuento plano de 50 555, porque la
mayoría son ligeras— y las lecturas dan `38 292` equivalentes, `1,47×` el recuento plano de 26 060,
arrastradas por las 16 800 consultas de estado. Ninguno de los dos mueve la cifra ni medio orden de
magnitud: `39 250 / 86 400 × 11 / 80 = 0,062` servidores de escritura. **El sistema sigue pidiendo
menos de un décimo de máquina.**

### Lo que sí dimensiona: RNF-11, RNF-10 y la geografía

`0,09` no es un número de servidores: es la prueba de que la carga no es la restricción activa. El
número real sale de tomar el **máximo** entre lo que pide la carga y lo que piden los umbrales de
servicio, y aquí manda el segundo término por dos órdenes de magnitud.

| Plano | Por qué existe | Nodos | De dónde sale |
|---|---|---|---|
| Escritura del giro | RNF-11 pide 99,9 % **sobre crear y pagar**, y RNF-06 exige un solo estado del giro entre el centro y el punto. Un plano de escritura, no tres | **3** | Quórum que tolera una caída sin gastar los 43,2 min/mes del presupuesto de error |
| Réplica de lectura en destino | Dos países de destino (RNF-12, RNF-14) y RNF-10 con 900 s de margen: alcanza réplica asíncrona. Dos nodos por país para no caer a cero con una máquina | **4** = `2 × 2 países` | RNF-10, RNF-12 |
| Consulta del emisor | RF-52, RF-53 y RF-66. **RNF-11 la excluye explícitamente de su medida**, así que no lleva quórum — pero es el 22 % de los requests y no puede compartir suerte con la escritura | **2** | RNF-11 por exclusión |
| Cumplimiento y tamizaje | RF-26, RF-27 y RF-97 llaman a listas externas cuya latencia y disponibilidad SendIt no fija. Aislarlo evita que una lista lenta consuma el techo de 3,3 s de RNF-09 | **2** | RNF-09, RF-26 |
| | | **11** | |

`servidores = max(carga / capacidad; piso de disponibilidad y geografía) = max(0,09; 11) = ` **11**.

**Y la consecuencia para `E`-escalar, que es lo que este paso realmente entrega:** para que el
término de carga alcance al término de disponibilidad, el volumen tendría que multiplicarse por
`11 / 0,09 ≈ 122`, es decir **341 000 giros diarios**, que son `USD 102 M` al día y una cuota del
61 % de los dos corredores. Antes de eso se rompen otras tres cosas, y ninguna se arregla con
servidores: la **cuota diaria del operador de telefonía** (cálculo 3, punto 2b), el **efectivo de la
caja del punto** (RF-92, RF-95) y el **caudal de la cola de cumplimiento** (70 casos/día contra
cuántos analistas). Ese es el orden en que este sistema se rompe.

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

1. **La prueba de quién es cada quien** — imágenes de documento de identidad, la fotografía de
   contraste, el comprobante de domicilio. Son binarios de cientos de kilobytes o megabytes y no se
   borran cuando la persona deja de ser cliente. **RF-80 los pide de las dos puntas**, emisor y
   receptor, así que la unidad no es «una persona por giro» sino dos: quien entrega y quien cobra,
   cada una capturada en su mostrador y en su país. Es la partida que domina el cálculo, y este
   backlog la duplicó.
2. **La prueba de que se tamizó** — el resultado del contraste contra las listas de personas y
   entidades sancionadas, con la lista, su versión y su fecha. RF-26 lo exige antes de aceptar el
   efectivo y RF-27 otra vez al autorizar el pago, así que son **dos evidencias por giro, haya o no
   coincidencia**: la ausencia de coincidencia también hay que poder demostrarla, y una auditoría
   necesita saber contra qué versión de qué lista se aprobó lo que se aprobó.
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
—porque RF-01 corre antes de RF-02, y entre los dos caben el rechazo por límite (RF-08, RF-09), el
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
meses antes de que RF-49 lo vuelva no pagable. Y hay un tercero que el backlog agregó y que corre
*después* del cierre aparente: RF-89 mantiene disponible la devolución no retirada hasta la
prescripción del giro, de modo que un giro devuelto no sale del dato caliente cuando se devuelve,
sino cuando prescribe. Todo lo demás es archivo: dato que hay que conservar y casi nunca leer.

| Tipo de dato | Qué es | Tamaño unitario | Cuántos por giro | Volumen diario | Años de retención | Marca |
|---|---|---|---|---|---|---|
| Registro del giro | La fila del giro: emisor, receptor único (RF-03), país único (RF-04), punto elegido (RF-63), monto fijado (RF-06), código ilegible (RNF-15) y su historia de estados | 1,0 KB | 1 | **2,8 MB** | 8,7 | `[ASSUMPTION]` |
| Asiento contable | Recepción del efectivo (RF-79), fondeo del corredor (RF-20), descuento de la caja al pagar (RF-95), más los extra de devolución (RF-74) y corrección (RF-56) | 0,4 KB | 3,2 | **3,6 MB** | 8,7 | `[ASSUMPTION]` |
| Cotización producida y fechada (RF-07) | Par de monedas, tasa, comisión, sello de tiempo y autor. **No es una lectura cacheada de una tasa ajena**: es un acto del sistema | 0,3 KB | 1,3 | **1,1 MB** | 8,7 | `[ASSUMPTION]` |
| Documento de identidad (binario, RF-80: emisor **y** receptor) | Anverso, reverso y foto de contraste, comprimidos, ilegibles en reposo por RNF-01 | **500 KB** por captura · 2 KB por referencia | `0,619` capturas (S-03 en las dos puntas, más las que RF-99 descarta) **+ 2 referencias** | **878 MB** — el **87 %** del diario | 8,7 | `[ASSUMPTION: S-03]` |
| Pregunta y respuesta del desafío, ilegibles (RF-68, RNF-17) | Pregunta en claro, resumen con sal de la respuesta. RF-101 prohíbe transmitirla y RNF-17 mostrarla | 0,25 KB | 1 — coste fijo por giro | **0,7 MB** | 8,7 | `[ASSUMPTION]` |
| Intentos de respuesta al desafío (RF-82, RF-83) | Momento, punto y resultado de cada intento. Nunca la respuesta | 0,15 KB | `0,32` = `0,20 × 1,6` (S-16) | **0,13 MB** | 8,7 | `[ASSUMPTION: S-16]` |
| Resultado de tamizaje (RF-26 y RF-27: dos por giro) | Lista, versión, fecha y veredicto. **La ausencia de coincidencia también hay que poder probarla**; el expediente completo solo cuando la hay | 2 KB sin coincidencia · **60 KB** con | `3` (RF-26 + RF-27 + retamizaje de RF-97) · `2 %` con coincidencia (S-08) | **20,2 MB** | 8,7 | `[ASSUMPTION: S-08]` |
| Acumulado de cobros por identidad de receptor (RF-58, RF-93) | Clave estable de receptor, contador y ventana. **Por identidad, no por giro** — es lo más parecido a un padrón que este sistema tiene | 0,2 KB por identidad | `0,45` = `1 / 2,2 cobros` (S-15) | **0,25 MB** | Vive mientras la ventana lo exija; se archiva con el último giro de esa identidad | `[ASSUMPTION: S-15]` |
| Caso de cumplimiento y su evidencia de liberación (RF-33, RF-87) | Motivo, derivación al segundo rol (RF-30), plazo del regulador más estricto (RF-31), y el motivo de la liberación que RF-87 exige | 40 KB | `0,025` = 2 % de S-08 + 0,5 % de RF-93 → **70 casos/día** | **2,8 MB** | 8,7 | `[ASSUMPTION: S-08]` |
| Traza de auditoría de actos y de accesos (RF-54, RNF-04) | Autor, momento, giro y acto. **Crece con las lecturas**: RNF-04 exige traza de todo acceso a datos de identidad, así que cada consulta de Kevin es una fila | 0,35 KB | `25` ≈ 18 actos + 7 accesos a identidad | **24,5 MB** | 8,7 — y **RNF-03 la declara inalterable: no se suprime nunca, ni por RF-81** | `[ASSUMPTION]` |
| Declaración de caja al abrir y al cerrar (RF-76) — **por punto y turno, no por giro** | Efectivo declarado por el punto, dos veces por turno, haya cero giros o mil | 0,4 KB | `3,21` equivalentes por giro = `9 000 / 2 800` | **3,6 MB** | 8,7 | `[ASSUMPTION: S-12]` |
| Comprobante de entrega en destino | Recibo firmado por el receptor en el mostrador, digitalizado. Es la prueba de que Elena contó los billetes | 35 KB | `0,96` — un pago por cada giro no devuelto | **94,1 MB** | 8,7 | `[ASSUMPTION]` |
| Declaración de diferencia del receptor y su atribución (RF-90, RF-59) | Lo que el receptor declara, la atribución al punto y su resolución aparte con el agente (RF-104) | 5 KB | `0,005` (S-17) | **0,07 MB** | 8,7 | `[ASSUMPTION: S-17]` |
| Aviso al receptor (prueba de aviso, RF-25, RF-37, RF-91) | La constancia que RF-98 obliga a conservar de cada unidad entregada al tercero: destinatario, canal, momento y resultado | 0,3 KB | `4,9` (S-14) | **4,1 MB** | 8,7 | `[ASSUMPTION: S-14]` |
| Devolución al emisor y su disponibilidad abierta (RF-32, RF-47, RF-50, RF-89) | Motivo, monto en la moneda que el emisor entregó (RF-88), comisión devuelta (RF-74) y punto que el emisor eligió (RF-72) | 1,5 KB | `0,04` (S-13) | **0,17 MB** | 8,7 — pero **caliente hasta 12 meses**: RF-89 no deja archivar la devolución no retirada | `[ASSUMPTION: S-13]` |
| **Supresión a pedido (RF-81)** — término **negativo** | Borra la evidencia de identidad de quien la entregó. **Nunca la traza**: RNF-03 prevalece sobre toda supresión | **−700 KB** por pedido (≈ 1,4 capturas) | **−0,00046** = `40 pedidos/mes ÷ 85 120 giros/mes` | **−0,9 MB** | Se resta del retenido, jamás del registro de actos | `[ASSUMPTION: S-18]` |
| **Descarte de evidencia sin giro (RF-99)** — término **negativo**, el mayor de los dos | La captura del emisor que se identificó (RF-01) y no llegó a entregar efectivo (RF-02): rechazado por límite, país no atendible, reguladores incompatibles, o se fue | **−500 KB** por captura | **−0,019** = `54 descartes/día ÷ 2 800 giros` | **−27,0 MB** — **30× lo que resta RF-81** | Nunca entra al retenido, aunque sí al ancho de banda de entrada | `[ASSUMPTION: 6 % de las identificaciones no terminan en giro]` |

### Agregado

| | Fórmula | Valor | Marca |
|---|---|---|---|
| Espacio por giro | suma de los tipos por su multiplicidad | `370,0 KB brutos − 9,64 KB (RF-99) − 0,32 KB (RF-81) = ` **360,0 KB** | Derivado. El binario de identidad son `313,5` de esos `370,0`: **el 85 %**. La verificación de abajo pasa |
| Almacenamiento diario | `espacio por giro × giros por día` | `360,0 KB × 2 800 = 1 008 000 KB = ` **1,01 GB/día** | Derivado. Para escala: YouTube, en el ejemplo del material, hace `52 TB` diarios — **52 000 veces esto** |
| Almacenamiento retenido | `diario × 365 × años de retención (S-09, ≥ 5)` | Los dos reguladores no piden lo mismo: **5 años** en el corredor peruano, **10 años** en el mexicano `[ASSUMPTION]`. S-09 obliga a tomar el máximo **por giro**, así que el multiplicador se pondera por el reparto de S-01b: `0,26 × 5 + 0,74 × 10 = 1,3 + 7,4 = ` **8,7 años**. → `1,008 GB × 365 × 8,7 = 3 201 GB = ` **3,2 TB** | Derivado. Piso defendible si los dos pidieran 5 años: `1,008 × 365 × 5 = ` **1,84 TB**. Techo si los dos pidieran 10: **3,68 TB**. **Detenerse en el diario habría dicho `1 GB` en vez de `3 200 GB`: los dos órdenes de magnitud que el método del material no tiene por qué contemplar y este caso sí** |
| Almacenamiento caliente | la fracción del retenido que todavía es pagable: `diario × 365 × 1` por los 12 meses de prescripción (S-11), **más las devoluciones no retiradas**, que RF-89 mantiene abiertas hasta ese mismo plazo | `1,008 GB × 365 × 1 = ` **368 GB ≈ 0,37 TB**, el `368 / 3 201 = ` **11,5 %** del retenido. Dentro van las devoluciones que RF-89 no deja archivar: `4 % × 15 % = 0,6 %` de los giros, `17/día` | Derivado. El otro `88,5 %` es archivo: dato que hay que conservar y casi nunca leer, y que por tanto **no tiene por qué vivir donde vive el giro pagable** |
| Almacenamiento independiente del giro | identidad y verificación de un emisor identificado en ventanilla que no llegó a crear giro (RF-01 corre antes de RF-02), y las declaraciones de caja de RF-76, que existen aunque el punto no pague nada en todo el turno | Caja: `9 000 × 0,4 KB = 3,6 MB/día` → `× 365 × 8,7 = ` **11,4 GB**. Capturas de RF-99 mientras esperan el descarte: `54 × 500 KB × 3 días = ` **81 MB** en régimen. Acumulados por identidad de receptor (RF-58): `39 000 × 0,2 KB = ` **7,8 MB/mes** | Derivado. Suma `11,5 GB`: irrelevante en el total y **el único piso que no baja cuando el volumen baja** — un día sin un solo giro sigue escribiendo 9 000 declaraciones de caja |
| **Menos: lo suprimido a pedido** | `pedidos (S-18) × lo que RF-81 puede borrar`, que es la evidencia de identidad y no la traza. Se resta al retenido, nunca al registro de actos | RF-81: `40 pedidos/mes × 700 KB × 12 × 8,7 años = 2,92 GB` → el **0,09 %** del retenido. RF-99: `27 MB/día × 365 × 8,7 = 85,7 GB` → el **2,7 %**, treinta veces más | Derivado. **Ninguno de los dos mueve la cifra; los dos mueven el diseño.** RF-81 obliga a encontrar a una persona *a través de* todos sus giros —el eje por el que el libro contable no está particionado— y RF-99 obliga a un ciclo de vida del binario que empieza **antes** de que exista el giro al que colgarlo |

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
| 1. Entrada por día | Lo que sube al sistema: las capturas de identidad de las dos puntas que RF-80 conserva, respuestas de las listas de sanciones, declaraciones de caja de RF-76, y las confirmaciones de cobro que suben desde los puntos de atención —incluida la ráfaga que sube un punto al recuperar la conexión y reconciliar su estado (RNF-08), que no es tráfico uniforme | `identidad 1 734 × 500 KB = 867 MB` **(el 73 %)** · `listas de sanciones 8 400 × 15 KB = 126 MB` · `comprobantes de entrega 2 690 × 35 KB = 94,2 MB` · `resto de escrituras de ventanilla 28 785 × 3 KB = 86,4 MB` · `ráfaga de RNF-08: 45 puntos × 400 KB = 18 MB` · `caja 9 000 × 0,4 KB = 3,6 MB` → **1 195,2 MB ≈ 1,20 GB/día** | Derivado. Los `27 MB` de capturas que RF-99 descartará **entran igual**: en el cálculo 2 son un negativo, aquí son un positivo |
| 2. Salida por día | Lo que el sistema entrega: cotizaciones fechadas, estados consultados por el emisor (RF-52, RF-53, RF-66), saldos de caja al operario antes de cada pago (RF-92), y las descargas de evidencia que hace cumplimiento | `consultas de estado 16 800 × 8 KB = 134,4 MB` · `respuestas de ventanilla 20 750 × 6 KB = 124,5 MB` · `descargas de evidencia de cumplimiento 70 casos × 2 × 500 KB = 70 MB` · `cotizaciones 3 640 × 4 KB = 14,6 MB` · `saldos de caja RF-92 2 690 × 2 KB = 5,4 MB` · `reportes a la autoridad RF-17 y RF-22, 3 × 50 KB = 0,15 MB` → **349,1 MB ≈ 0,35 GB/día** | Derivado |
| 2b. Salida por canal de terceros | **No se mide en bytes.** Avisos de voz y SMS entregados a un operador de telefonía (RF-25, RF-37, RF-41, RF-60, RF-75), contados en unidades y facturados por unidad. Van aparte porque dividirlos entre 86 400 no dice nada útil: lo que los limita es la cuota del tercero, no el enlace | **13 720 unidades/día** · en el día señalado `13 720 × 3,0 = ` **41 160 unidades**. Contra una cuota típica de `10 000/día` por país sin acuerdo comercial `[ASSUMPTION]`, los dos países dan `20 000` → **el día pico la excede por 2,1×**. Costo: `USD 686/día`, `USD 250 k/año` | `[ASSUMPTION: S-14]` — **este es el primer cuello de botella del sistema, y no se resuelve comprando servidores.** Elena no tiene datos móviles: un aviso no entregado no degrada, desaparece |
| 3. Entrada por segundo | `entrada por día / 86 400` | `1 195 200 KB / 86 400 = ` **13,8 KB/s** ≈ 0,11 Mbit/s | Derivado |
| 4. Salida por segundo | `salida por día / 86 400` | `349 100 KB / 86 400 = ` **4,0 KB/s** ≈ 0,03 Mbit/s | Derivado |
| 5. Pico | `resultado × P` | `(13,8 + 4,0) × 11 = ` **196 KB/s ≈ 1,6 Mbit/s** — entrada `152 KB/s`, salida `44 KB/s` | **Es la cifra que se usa.** Y hay una que no obedece a `P`: la ráfaga de RNF-08, `18 MB en 60 s = 300 KB/s`, que sola supera el pico entero. Se dimensiona contra ella, no contra los 196 KB/s |

Dos observaciones específicas de este caso:

- **La asimetría se invierte respecto del ejemplo del material.** En YouTube la salida aplasta a la
  entrada por tres órdenes de magnitud: se sube un vídeo y se descarga cien millones de veces. En
  SendIt el binario pesado —el documento de identidad— **entra** y casi nunca sale; entra dos veces
  por giro desde que RF-80 lo pide de las dos puntas, y lo que sale son respuestas de pocos
  kilobytes consultadas muchas veces. Con las cifras: YouTube `40 PB / 52 TB = 769×` a favor de la
  salida; SendIt `1 195,2 / 349,1 = 3,4×` a favor de la **entrada**. La única salida pesada del
  sistema son los `70 MB/día` que cumplimiento descarga de evidencia, y es el 20 % de toda la
  salida generada por el 0,03 % de las operaciones.
- **Dividir entre 86 400 supone que la carga es uniforme, y no lo es.** El resultado del paso 3 es
  un promedio contra el que no se dimensiona nada. La cifra que se usa es la del paso 5.

---

## Qué invalida esta estimación

Se registra aquí para que el paso siguiente sepa sobre qué está parado.

| Si cambia… | Se recalcula | Y hay que revisar |
|---|---|---|
| **La cuota de mercado del lanzamiento (0,5 %) o el ticket promedio (S-05)** | **Los tres cálculos, en proporción directa** | Nada, mientras no cruce un orden de magnitud: `0,09` servidores de carga aguantan `×122` antes de alcanzar el piso de 11. Es el supuesto del que más depende la cifra y el que menos cambia la arquitectura |
| **El reparto entre corredores (S-01b, 26 % / 74 %)** | El multiplicador de retención del cálculo 2: `8,7 años` se mueve entre `5` y `10` | `A` — la política de conservación es **por giro**, no global; el reparto solo elige contra qué extremo se dimensiona el agregado |
| El número de corredores (S-01, anclado en RNF-12) | Los tres cálculos | `D` — otra red afiliada que sincronizar, con otra calidad de conexión; `A` — otro plazo de conservación en el máximo por corredor |
| Los años de retención (S-09, anclado en RNF-03 y RF-18) | Almacenamiento | `A` — la política de retención por entidad, que es por giro y no global |
| El plazo de retención o el de prescripción (S-10, S-11) | Almacenamiento caliente, y el caudal de casos de cumplimiento | `E` (escalar) — el tamaño en régimen de la cola de cumplimiento, que se mide contra el plazo más largo de los corredores y no contra el piso de 72 h |
| El factor de pico (S-07) | Servidores y ancho de banda | `E` (escalar) — el tramo en que el sistema se rompe |
| La tasa de coincidencias (S-08) | Almacenamiento | `D` — dónde corre el tamizaje; `L` — el componente que lo ejecuta |
| El tamaño de la red afiliada o sus turnos (S-12) | Servidores y almacenamiento, por el piso de RF-76 que no depende del volumen | `E` (escalar) — el tramo más bajo, que ya nace con carga aunque no haya giros |
| La tasa de devolución o la de retiro (S-13) | Operaciones de ventanilla y almacenamiento caliente, por RF-89 | `D` — el ciclo de vida del giro, que no termina en el pago |
| El coste o la cuota del canal de voz y SMS (S-14) | El costo por giro, no el cómputo | `E` (escalar) — es un candidato a cuello de botella que no se resuelve con servidores; `L` — el componente que habla con el tercero |
| El acumulado de cobros del receptor (S-15, anclado en RF-58 y RF-93) | El caudal de la cola de cumplimiento, que gana una fuente de retención nueva | `E` (escalar) — el primer cuello de botella; `D` — la clave por la que se cuenta del lado receptor |
| El volumen de supresiones (S-18) | Almacenamiento, con signo menos | `D` — poder borrar la evidencia sin tocar la traza, que RNF-03 no deja mover |
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
