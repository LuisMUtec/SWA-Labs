# E — Estimar

> Paso 2 de [R.E.D.A.L.E.](../README.md) · anterior:
> [**R** — backlog de requerimientos](../R-requerimientos/backlog.md) · siguiente:
> [**D** — Diseñar el servicio](../D-disenar-servicio/README.md) · bitácora:
> [`ITERACIONES.md`](../ITERACIONES.md)

**Estado: andamiaje.** Ninguna cifra de este documento está calculada. Las tablas están vacías a
propósito: se llenan contra el backlog ya evaluado, no antes.

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
| **Giros por día** | Giros creados, medidos sobre el conjunto de corredores de RNF-12 | — | — | — |
| **Operaciones de ventanilla por día** | Atenciones presenciales: crear, pagar, autorizar, corregir, devolver, declarar diferencia, rederivar el cobro | — | — | — |
| **Aperturas y cierres de caja por día** | `puntos activos × turnos × 2` (RF-76). No depende de los giros | — | — | — |
| **Avisos al receptor por día** | Unidades de voz o SMS entregadas a un tercero (RF-25, RF-37, RF-41, RF-60, RF-75). Se pagan por unidad, no por byte | — | — | — |
| Giros por día en pico | `giros por día × P` | — | — | — |
| RPS — requests por segundo | Derivada, no supuesta: sale del desglose por operación del cálculo 1 | — | — | — |
| Almacenamiento requerido | Salida del cálculo 2, no entrada | — | — | — |
| Factor de pico `P` | Ver abajo | — | — | — |

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
| RNF-09 | Operación de ventanilla en menos de 3 minutos, **incluida la verificación del documento** | Servidores | El presupuesto de máquina es lo que sobra de los 3 min después del tiempo humano de RF-01; es un techo de latencia por operación, no de throughput | — | — |
| RNF-10 | Giro fondeado disponible para cobro en destino en menos de 15 min desde su creación | Servidores y ancho de banda | Acota la ventana de propagación entre origen y destino, y con ella cuánto puede diferirse el trabajo de RF-20 y RF-36 | — | — |
| RNF-11 | 99,9 % mensual, medido **sobre crear y pagar, no sobre consultar** | Servidores | Reparte la redundancia de forma desigual: la ruta de escritura se dimensiona con margen de disponibilidad, la de consulta (RF-52, RF-53) no | — | — |

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
| S-02 | Emisores distintos por mes | Dimensiona el almacenamiento de la evidencia de identidad que RF-80 conserva, y que persiste por el plazo de RNF-03 aunque el emisor no vuelva nunca. No es un padrón: es el recuento de identificaciones practicadas en ventanilla. Su gemelo del lado receptor no tiene supuesto propio porque no hay uno solo por giro: ver S-15 | — | — | — |
| S-03 | Proporción de giros que exigen captura nueva de identidad | Un emisor recurrente se identifica otra vez (RF-01 no admite excepción) pero puede no producir un binario nuevo. La proporción decide cuánto del cálculo 2 crece con los giros y cuánto con las personas | El patrón de [Rosa](../../personas/Rosa.MD): la misma emisora, quincena tras quincena | — | — |
| S-04 | Giros por emisor al mes | Convierte emisores en giros por día, que es la unidad de carga del paso | El patrón de Rosa: quincenal, estable desde hace tres años | — | — |
| S-05 | Ticket promedio | No mueve el cómputo, pero decide cuántos giros cruzan el umbral de reporte transfronterizo (RF-17, RF-22) y cuántos el umbral reforzado que obliga a un segundo rol (RF-13) — y con ello cuántas operaciones de ventanilla extra aparecen | El rango de Rosa: USD 200–400 | — | — |
| S-06 | Consultas de estado por giro | **RF-52 y RF-53 la exigen como capacidad, y RF-66 le agrega el estado retenido con su fecha**: la consulta es carga requerida, no tráfico incidental. Es la operación de lectura dominante y la única que RNF-11 excluye explícitamente de su medida de disponibilidad | Lo que hoy obliga a Rosa a llamar por teléfono, ahora exigido por RF-52 | — | — |
| S-07 | **Factor de pico** | Ver abajo | — | — | — |
| S-08 | Proporción de giros que disparan una coincidencia de tamizaje | La tasa decide el volumen de evidencia, que es lo que domina el almacenamiento, y RF-28 obliga a guardar separadas la coincidencia exacta y la homonimia — la abrumadora mayoría son homónimos | `[ASSUMPTION: sin fuente; el enunciado no da ninguna cifra de tamizaje]` | — | — |
| S-09 | Años de retención regulatoria | Multiplica el almacenamiento diario por un factor que el ejemplo de YouTube no tiene | **Cerrado por RNF-03 y RF-18**: el plazo más largo de los dos reguladores del giro, con un piso de 5 años. Se calcula por giro y no por política global, así que el multiplicador del cálculo 2 no es único: es el máximo por corredor | ≥ 5 años | **Cerrado** |
| S-10 | Plazo de una retención | Acota cuántos giros retenidos coexisten: la cola no es un acumulado sin fin, es un caudal con tiempo de residencia. RF-31 le pone plazo y RF-32 la termina devolviendo al emisor | **Cerrado**: lo que fije el regulador más estricto de los dos países del giro; **a falta de norma expresa, 72 h**. Es un piso por defecto, no un techo — un regulador puede exigir más, y RF-31 obliga a obedecerlo. El tiempo de residencia se dimensiona **por corredor**, contra el plazo más largo, igual que S-09 | ≥ 72 h, por corredor | **Cerrado** |
| S-11 | Plazo de prescripción | Fija cuánto tiempo un giro creado sigue siendo pagable y por tanto vivo en el estado caliente antes de que RF-49 lo vuelva no pagable y RF-50 lo ponga a disposición del emisor. Separa el dato caliente del dato meramente retenido | **Cerrado**: 12 meses desde la creación del giro | 12 meses | **Cerrado** |
| S-12 | Puntos de atención activos y turnos por punto | Es la única entrada que no deriva del volumen: RF-76 escribe dos declaraciones de caja por punto y turno aunque no haya un solo giro, y RF-92 lee el saldo antes de cada pago. Fija además cuántos destinos ofrece RF-63 al emisor y cuántos puede alcanzar la rederivación de RF-91 | La red afiliada de los dos corredores de S-01, no la planta propia | — | — |
| S-13 | Proporción de giros que terminan devueltos, y cuánto tarda el emisor en retirar | Toda devolución es una operación de ventanilla más (RF-71 en efectivo, RF-72 en el punto que el emisor elija), un aviso más (RF-14) y un asiento más que incluye la comisión (RF-74). Y RF-89 la mantiene disponible hasta la prescripción: **un giro devuelto no cierra**, sigue caliente hasta 12 meses, así que esta proporción no mueve solo el cálculo 1 — mueve el almacenamiento caliente del cálculo 2 | Las tres fuentes de devolución ya en el backlog: retención vencida (RF-32), cancelación (RF-47) y prescripción (RF-50) | — | — |
| S-14 | Avisos al receptor por giro, y coste por unidad del canal | El canal de voz y SMS es de un tercero y se paga **por unidad entregada**, no por byte: es la única partida del paso cuyo costo no baja aunque el mensaje quepa en 140 caracteres. Un giro sin incidente ya gasta tres (RF-25, RF-41, RF-75); uno retenido gasta el cuarto (RF-37) y uno con diferencia el quinto (RF-60). El reintento de una entrega fallida cuenta como unidad nueva | La cuota que un operador de telefonía concede por país, que RNF-12 obliga a contar dos veces | — | — |
| S-15 | Receptores distintos por mes, y cobros por receptor en la ventana | RF-58 cuenta los cobros de un mismo receptor y RF-93 retiene al que supera el acumulado: hace falta una clave de receptor estable entre giros, no una fila por giro. Y RF-80 conserva la evidencia de identidad **del receptor además de la del emisor**, de modo que el binario pesado del cálculo 2 se captura dos veces por giro y no una | El mismo patrón de S-02, del otro lado del mostrador: Elena cobra todos los meses y se identifica todas las veces | — | — |
| S-16 | Proporción de pagos que se resuelven por desafío, e intentos por pago | RF-68 obliga a registrar pregunta y respuesta en **todo** giro, así que el dato existe siempre y RNF-17 exige guardarlo ilegible en los dos lados del mostrador — coste fijo por giro, en el camino de escritura de la creación. Lo que varía es el consumo: RF-69 abre el desafío como salida al documento vencido, RF-82 acota los intentos y RF-12 los comprueba sin mostrarlos, así que un pago puede costar hasta `intentos` comprobaciones en vez de una | La proporción de documentos vencidos que hoy dejan a Elena sin cobrar, que es la tensión T3 del backlog | — | — |
| S-17 | Proporción de pagos con declaración de diferencia en el mostrador | RF-90 le da al receptor un acto propio que antes no tenía, y cada declaración abre la cadena cara: atribución al punto (RF-59), aviso al receptor (RF-60), y si termina en corrección, un movimiento nuevo (RF-56) con autorización de un segundo rol (RF-61). Es baja en proporción y alta en operaciones por caso | `[ASSUMPTION: sin fuente; el enunciado no da ninguna cifra de diferencias]` | — | — |
| S-18 | Pedidos de supresión de datos personales por mes | **Es el único término negativo del cálculo 2.** RF-81 suprime a pedido los datos de quien los entregó —y de nadie más— salvo lo que el registro de actos debe conservar, que RNF-03 y RNF-03 declaran inalterable. Resta binarios de identidad; no resta trazas. Y agrega una operación cara que ningún giro pide: buscar a una persona **a través de** todos sus giros, que es el eje por el que el libro contable no está particionado | El plazo de RNF-03 acota lo que puede suprimirse: por debajo del piso de conservación no hay nada que borrar | — | — |

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
| Quincena / fin de mes | — | Ciclo de cobro del emisor | — |
| Fecha señalada | — | — | — |
| Hora del día | — | Huso horario del emisor, no del receptor — y RNF-12 obliga a contar dos, uno por corredor, que pueden no solaparse | — |

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

| Paso | Fórmula | Valor | Marca |
|---|---|---|---|
| 1. Capacidad de un core | — req/s | — | — |
| 2. Capacidad de un servidor | `#cores × core` | — | — |
| 3. Carga objetivo | `RPS derivado del desglose de abajo × P` | — | — |
| 4. Servidores | `carga objetivo / capacidad de servidor` | — | — |

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
| Identificar al emisor contra documento | escritura + verificación externa | RF-01, RF-02 | — | — | — |
| Conservar la evidencia de identidad de las dos puntas | escritura de binario | RF-80, RNF-01 | — | — | — |
| Registrar la pregunta y su respuesta al crear | escritura ilegible, una por giro | RF-68, RNF-17 | — | — | — |
| Cotizar y fechar la cotización | **escritura durable** | RF-05, RF-06, RF-07 | — | — | — |
| Contar límites sobre la identidad del emisor | lectura agregada | RF-08, RF-09, RF-10 | — | — | — |
| Contar los cobros del receptor en la ventana | lectura agregada **por identidad de receptor** | RF-58, RF-93 | — | — | — |
| Tamizar contra listas | lectura externa + escritura de evidencia | RF-26, RF-27, RF-28 | — | — | — |
| Crear el giro y emitir su código | escritura contable | RF-11, RF-13, RF-20 | — | — | — |
| Declarar el efectivo al abrir y al cerrar caja | escritura, `puntos × turnos × 2` | RF-76 | — | — | — |
| Informar al operario el efectivo del punto | lectura previa a cada pago | RF-92 | — | — | — |
| Comprobar la respuesta del desafío sin mostrarla | lectura ilegible, hasta `intentos` por pago | RF-12, RF-69, RF-82 | — | — | — |
| Ejecutar el pago en destino | escritura contable + frontera | RF-34, RNF-05, RF-36, RF-85, RF-86 | — | — | — |
| Rederivar el cobro a otro punto del país destino | escritura de estado + segunda ventanilla | RF-91 | — | — | — |
| Declarar en el mostrador una diferencia de monto | escritura + atribución al punto | RF-90, RF-59 | — | — | — |
| Cerrar el giro y avisar al emisor | escritura + notificación | RF-64, RF-65 | — | — | — |
| Consultar estado | lectura | RF-52, RF-53, RF-66 | — | — | — |
| Avisar al receptor por llamada o mensaje | **salida por canal de un tercero, por unidad** | RF-25, RF-37, RF-41, RF-60, RF-75 | — | — | — |
| Devolver al emisor (retención vencida, cancelación, prescripción) | escritura contable | RF-32, RF-47, RF-50 | — | — | — |
| Entregar la devolución en ventanilla y avisarla | escritura + notificación + ventanilla | RF-14, RF-71, RF-72, RF-74, RF-88 | — | — | — |
| Suprimir a pedido los datos de una persona | **búsqueda transversal + borrado parcial** | RF-81 | — | — | — |

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

**Y una cuarta familia que va con signo menos, la única del paso.** RF-81 suprime a pedido los datos
personales de quien los entregó —y de nadie más— salvo los que el registro de actos debe conservar.
No es una excepción cosmética a las tres de arriba: recorta la familia 1, que es justamente la que
domina, y deja intactas la 2 y la 3, que RNF-03 y RNF-03 declaran inalterables. El efecto neto sobre
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
| Registro del giro | — | — | — | — | — | — |
| Asiento contable | — | — | — | — | — | — |
| Cotización producida y fechada (RF-07) | — | — | — | — | — | — |
| Documento de identidad (binario, RF-80: emisor **y** receptor) | — | — | — | — | — | — |
| Pregunta y respuesta del desafío, ilegibles (RF-68, RNF-17) | — | — | — | — | — | — |
| Intentos de respuesta al desafío (RF-82, RF-83) | — | — | — | — | — | — |
| Resultado de tamizaje (RF-26 y RF-27: dos por giro) | — | — | — | — | — | — |
| Acumulado de cobros por identidad de receptor (RF-58, RF-93) | — | — | — | — | — | — |
| Caso de cumplimiento y su evidencia de liberación (RF-33, RF-87) | — | — | — | — | — | — |
| Traza de auditoría de actos y de accesos (RF-54, RNF-04) | — | — | — | — | — | — |
| Declaración de caja al abrir y al cerrar (RF-76) — **por punto y turno, no por giro** | — | — | — | — | — | — |
| Comprobante de entrega en destino | — | — | — | — | — | — |
| Declaración de diferencia del receptor y su atribución (RF-90, RF-59) | — | — | — | — | — | — |
| Aviso al receptor (prueba de aviso, RF-25, RF-37, RF-91) | — | — | — | — | — | — |
| Devolución al emisor y su disponibilidad abierta (RF-32, RF-47, RF-50, RF-89) | — | — | — | — | — | — |
| **Supresión a pedido (RF-81)** — término **negativo**, el único | — | — | — | — | — | — |

### Agregado

| | Fórmula | Valor | Marca |
|---|---|---|---|
| Espacio por giro | suma de los tipos por su multiplicidad | — | — |
| Almacenamiento diario | `espacio por giro × giros por día` | — | — |
| Almacenamiento retenido | `diario × 365 × años de retención (S-09, ≥ 5)` | — | — |
| Almacenamiento caliente | la fracción del retenido que todavía es pagable: `diario × 365 × 1` por los 12 meses de prescripción (S-11), **más las devoluciones no retiradas**, que RF-89 mantiene abiertas hasta ese mismo plazo | — | — |
| Almacenamiento independiente del giro | identidad y verificación de un emisor identificado en ventanilla que no llegó a crear giro (RF-01 corre antes de RF-02), y las declaraciones de caja de RF-76, que existen aunque el punto no pague nada en todo el turno | — | — |
| **Menos: lo suprimido a pedido** | `pedidos (S-18) × lo que RF-81 puede borrar`, que es la evidencia de identidad y no la traza. Se resta al retenido, nunca al registro de actos | — | — |

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
| 1. Entrada por día | Lo que sube al sistema: las capturas de identidad de las dos puntas que RF-80 conserva, respuestas de las listas de sanciones, declaraciones de caja de RF-76, y las confirmaciones de cobro que suben desde los puntos de atención —incluida la ráfaga que sube un punto al recuperar la conexión y reconciliar su estado (RNF-08), que no es tráfico uniforme | — | — |
| 2. Salida por día | Lo que el sistema entrega: cotizaciones fechadas, estados consultados por el emisor (RF-52, RF-53, RF-66), saldos de caja al operario antes de cada pago (RF-92), y las descargas de evidencia que hace cumplimiento | — | — |
| 2b. Salida por canal de terceros | **No se mide en bytes.** Avisos de voz y SMS entregados a un operador de telefonía (RF-25, RF-37, RF-41, RF-60, RF-75), contados en unidades y facturados por unidad. Van aparte porque dividirlos entre 86 400 no dice nada útil: lo que los limita es la cuota del tercero, no el enlace | — | — |
| 3. Entrada por segundo | `entrada por día / 86 400` | — | — |
| 4. Salida por segundo | `salida por día / 86 400` | — | — |
| 5. Pico | `resultado × P` | — | — |

Dos observaciones específicas de este caso:

- **La asimetría se invierte respecto del ejemplo del material.** En YouTube la salida aplasta a la
  entrada por tres órdenes de magnitud: se sube un vídeo y se descarga cien millones de veces. En
  SendIt el binario pesado —el documento de identidad— **entra** y casi nunca sale; entra dos veces
  por giro desde que RF-80 lo pide de las dos puntas, y lo que sale son respuestas de pocos
  kilobytes consultadas muchas veces.
- **Dividir entre 86 400 supone que la carga es uniforme, y no lo es.** El resultado del paso 3 es
  un promedio contra el que no se dimensiona nada. La cifra que se usa es la del paso 5.

---

## Qué invalida esta estimación

Se registra aquí para que el paso siguiente sepa sobre qué está parado.

| Si cambia… | Se recalcula | Y hay que revisar |
|---|---|---|
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
