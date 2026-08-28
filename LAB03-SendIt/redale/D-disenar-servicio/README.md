# D — Diseñar el servicio

> Paso 3 de [R.E.D.A.L.E.](../README.md) · anterior: [**E** — Estimar](../E-estimar/README.md) ·
> siguiente: [**A** — Armar el modelo de datos](../A-armar-modelo-datos/README.md) · bitácora:
> [`ITERACIONES.md`](../ITERACIONES.md)

**Estado: decidido.** Las tres salidas del material están elegidas —arquitectura, persistencia por
familia de dato y diseño de la API— y las seis decisiones que este caso obliga están cerradas, cada
una con su alternativa descartada, el requisito que la obliga y **lo que se pierde**. Ninguna tabla
queda con `—`.

Qué construimos y cómo. El material pide tres salidas: **arquitectura high-level** (3-tier, MVC,
monolito, servicios), **tipo de persistencia** (SQL, NoSQL, mixta) y **diseño de la API** (los
endpoints). Aquí se define el alcance y las expectativas de la arquitectura.

---

## Contrato con los pasos vecinos

| | |
|---|---|
| **Consume de E** | El orden de magnitud: cuántos servidores, cuánto almacenamiento y de qué tipo, cuánto ancho de banda y con qué asimetría. Y los supuestos declarados, porque una arquitectura elegida bajo un supuesto que se retira queda sin fundamento |
| **Consume de R** | Las garantías enunciadas en el backlog. Cada decisión de este paso es el **mecanismo** de una garantía; una decisión que no responde a ninguna garantía es preferencia técnica |
| **Entrega a A** | El tipo de persistencia por familia de dato, que es lo que `A` convierte en entidades y motores; y las decisiones de consistencia, que deciden si un dato se actualiza en el sitio o se agrega |
| **Entrega a L** | Los servicios que el diagrama dibuja como cajas, las fronteras con terceros que el diagrama dibuja como externas, y la frontera con el **punto de atención** —que corre el software de SendIt sobre el mostrador de un agente afiliado, paga con el efectivo de la caja del agente y obliga a liquidárselo después (`RF-24`)—: es a la vez frontera contable y extremo que puede quedarse sin conexión |
| **Queda inválido si E cambia** | La justificación de escala. Si el número de servidores cruza un orden de magnitud, la opción de arquitectura deja de estar sostenida por su cálculo aunque siga siendo defendible por otra razón — y esa otra razón hay que escribirla |
| **Queda inválido si R cambia** | La decisión cuyo requerimiento desapareció, y toda la fila de la tabla de endpoints que lo servía |

**Advertencia de dependencia, declarada y no disimulada.** [`E`](../E-estimar/README.md) sigue en
andamiaje: no hay cifra de servidores, de almacenamiento ni de ancho de banda contra la cual elegir.
Por eso **ninguna decisión de este documento se apoya en escala**, y así está escrito en cada fila:
se apoyan en modos de falla, en atomicidad y en invariantes del backlog, que son argumentos que la
estimación no puede desmentir. Lo que sí puede desmentir es el **tamaño** de las unidades de
despliegue, no su frontera — y esa es exactamente la fila «Queda inválido si E cambia» de arriba.

---

## Lo que este paso registra y el backlog no puede contener

El backlog **enuncia la garantía**; este paso **elige el mecanismo**. La frontera es operativa, no
estilística: un requerimiento que nombra un mecanismo se verifica contra la implementación en vez de
contra el efecto, y sobrevive a su propia obsolescencia.

| El backlog dice | Este paso decide |
|---|---|
| `RNF-05` — «ningún giro registra dos entregas al receptor, en ningún punto y en ningún momento» | Clave de idempotencia: quién la genera, cuándo se persiste, cuánto vive, qué devuelve el reintento (`RF-43`, `RF-44`) — decisión **(b)** |
| `RF-06` — «el sistema conservará ese monto sin recalcularlo durante toda la vida del giro» | Cuánto vive la cotización que `RF-07` fecha, y quién absorbe el movimiento cambiario hasta que el receptor cobra — decisión **(d)** |
| `RNF-06` — «el sistema mantendrá un solo estado del giro entre el centro y el punto de atención» | Qué puede hacer un punto sin conexión, cuál lado manda mientras dura, y cómo se resuelve la divergencia al reconectar (`RNF-08`) — decisión **(c)** |
| `RNF-03` — «ningún acto registrado se modifica ni se borra, cualquiera sea quien lo pida» | Registro por adición frente a actualización en el sitio — decisión **(a)** |
| `RNF-17` **citado como está** desde la ronda 12, que lo extendió al mostrador: «ni quien administra la infraestructura ni quien atiende el mostrador reconstruye una respuesta: el sistema la comprueba sin mostrársela a ninguno de los dos». **Los dos lectores están nombrados en el propio invariante**, y por eso acá no hace falta agregarle ninguna cláusula; `RF-114` cierra además la superficie por la que la respuesta entra. `RF-12` se retiró por decir lo que estas dos fuentes ya dicen | Con qué transformación se guarda la respuesta que `RF-68` le pide al emisor, dónde corre la comparación que `RF-69` habilita, cómo se cuentan los intentos de `RF-82` y qué caduca con el giro por `RF-83` — decisión **(f)** |
| `RF-113` — «impedirá que quien atiende el mostrador lea o transcriba el código de seguimiento» —, con `RF-11` —«hará llegar el código de seguimiento al emisor por llamada o mensaje de texto al teléfono que él registró»— y `RF-125` —«confirmará al operario que el código salió hacia el emisor, sin mostrárselo»— y `RF-114` — «recibirá la respuesta del desafío del propio receptor, sin que quien atiende pueda leerla ni digitarla» | **Por dónde entra y sale el secreto.** Los dos ítems enuncian una prohibición sobre un ojo humano, y ninguna prohibición se cumple sola: hay que elegir el camino físico —qué dispositivo lo muestra, qué proceso lo cifra, qué respuesta ve el mostrador— y qué pasa cuando ese camino no está. Es lo que decide **(f)**, del lado de la entrada y del de la salida |

Toda decisión técnica desplazada desde el backlog aterriza **aquí**, no se suprime.

> **Nota de identificadores.** **Ocho** identificadores están **retirados** en el
> [backlog](../R-requerimientos/backlog.md#identificadores-retirados), y un número retirado no se
> reutiliza: su número queda muerto. Este documento no cita ninguno, y cita en su lugar lo que hoy
> cubre cada uno.
>
> | Retirado | Este documento cita |
> |---|---|
> | `RF-35` | `RNF-05` — ningún giro registra dos entregas al receptor |
> | `RF-38` | `RNF-16` — ninguna entrega difiere de la cifra que el emisor vio |
> | `RF-55` | `RNF-03` — ningún acto registrado se modifica ni se borra |
> | `RF-62` | `RNF-13` — ningún giro figura devuelto y cobrado a la vez |
> | `RF-21` | `RF-05` — informar el monto exacto **en moneda destino** antes del efectivo |
> | `RF-45` | `RNF-05`, `RNF-06` y `RNF-13` — los tres invariantes que ya prohíben pagar dos veces, afirmar dos estados a la vez, y devolver y cobrar a la vez |
> | `RF-58` | `RF-93` — retener al receptor que superó su acumulado, que contiene el contar |
> | `RF-107` | `RF-106` vía `RF-47` — avisar al receptor toda devolución, y la cancelación es una devolución |
>
> Hay una segunda forma de puntero muerto que ningún `grep`
> delata: **el ítem que se partió y conserva su número para una sola de las mitades.** Siete se
> partieron y todas se citan aquí por la mitad que corresponde: el tamizaje del receptor es
> `RF-119` y `RF-26` es solo el del emisor; el aviso de diferencia al receptor es `RF-121` y `RF-60`
> es solo el del emisor; el aviso previo a la prescripción al receptor es `RF-120` y `RF-51` es solo
> el del emisor; rehacer es `RF-117`, **conservar la cotización es `RF-134`** y **no recobrar la
> comisión es `RF-135`**; asociar la acción ofrecible es `RF-39` y **mostrársela al operario es
> `RF-130`**; la constancia del aviso es `RF-98`, **registrar si llegó es `RF-131`** y **tratar como
> no avisado a quien no tenga constancia es `RF-132`**; informar el plazo de aviso es `RF-115` y
> **el techo de una hora entre retención y aviso es `RF-133`**. Toda referencia de abajo resuelve a
> un ítem vivo y a la mitad que dice.

---

## 1. Arquitectura high-level

| Opción | A favor | En contra | Decisión |
|---|---|---|---|
| Monolito 3-tier | Una sola transacción cubre el asiento contable y el estado del giro, que es literalmente lo que piden `RNF-07` y `RNF-05`; un solo despliegue para los **155** ítems del backlog —138 funcionales y 17 no funcionales—; la latencia de `RNF-09` no gasta saltos de red | Mete en el mismo proceso cinco terceros que fallan por su cuenta (`RF-01`, `RF-26`, `RF-07`, `RF-17`, `RF-25`): un proveedor de listas lento consume los hilos del camino del pago. Y no puede satisfacer `RNF-17`, que exige que la respuesta del desafío sea inalcanzable para quien administra la infraestructura del giro — dentro de un proceso y una base únicos, quien administra la base lo alcanza todo | **Descartada como forma total.** Su núcleo se conserva: ver la fila mixta |
| Monolito modular | Fronteras de compilación sin fronteras de red; una sola base transaccional; permite partir después sin reescribir el dominio | Un módulo comparte proceso y credenciales de base con los demás: no aísla el fallo de un tercero ni el secreto de `RNF-17`. Y no dice nada sobre el mostrador, que es un despliegue físicamente separado lo quiera el diseño o no | **Descartada sola. Adoptada como forma interna del núcleo** |
| Servicios | Cada frontera que falla distinto se aísla, se reintenta sola y se despliega sola; el desafío obtiene base y credenciales propias (`RNF-17`); el punto de atención es por naturaleza una unidad aparte (`RF-100`, `RNF-06`) | Parte el libro contable en escrituras distribuidas: `RNF-07` —«lo que sale de una cuenta entra en otra»— dejaría de ser una transacción para volverse un protocolo, y el doble pago que `RNF-05` prohíbe pasaría a depender de una compensación en vez de una restricción. Es un problema que el diseño se crea a sí mismo | **Descartada como forma total** |
| MVC (como organización interna) | Organiza bien la única superficie con pantalla: el cliente de ventanilla y el tablero de cumplimiento | No es una arquitectura de sistema, es un patrón de la capa de presentación. Adoptarlo arriba pone `RF-08`, `RF-13` y `RF-40` en controladores, y obliga a reimplementar el mismo control en cada mostrador — con `RF-84` diciendo explícitamente que decide el sistema y no el operario | **Descartada como arquitectura.** Se usa dentro del cliente de ventanilla y del tablero de cumplimiento, y en ningún otro lado |
| Mixta — núcleo monolítico + servicios en la frontera | Conserva la transacción única donde el dinero la exige y aísla exactamente lo que falla distinto: los cinco terceros, el secreto del desafío y el mostrador que se queda sin línea. Cada frontera se justifica con un ítem, no con una preferencia | Son cuatro clases de unidad de despliegue en vez de una, con cuatro formas de fallar y un contrato entre ellas que hay que sostener. La frontera núcleo↔mostrador introduce el problema más caro del caso —la decisión **(c)**— y ninguna otra opción lo evita, porque el mostrador está lejos por geografía y no por diseño | **Elegida** |

**Arquitectura elegida: mixta — un núcleo monolítico modular, en 3 capas, con servicios adaptadores
en cada frontera externa, un servicio aislado para el secreto del desafío, y el punto de atención
como unidad de despliegue propia y desconectable.** Cuatro clases de unidad, y cada una existe por
un ítem:

| Unidad | Qué contiene | Por qué está separada | Ítems que la obligan |
|---|---|---|---|
| **Núcleo transaccional** (un despliegue, una base) | Libro contable, giro y su estado, límites del emisor, acumulado de cobros del receptor (`RF-93`), cotización aplicada, idempotencia, doble control, retención, devolución, cancelación, prescripción, caja por punto, **efectivo en custodia sin giro** (`RF-118`) y **giro rehecho con su cotización conservada** (`RF-117`) | **No se separa**, y esa es la decisión: todo lo que tiene que entrar en la misma transacción que el asiento vive acá. Partirlo convierte una escritura atómica en un protocolo | `RNF-07`, `RNF-05`, `RNF-13`, `RNF-16`, `RF-08`, `RF-09`, `RF-93`, `RF-117`, `RF-134`, `RF-135`, `RF-118`, `RF-138` |
| **Adaptadores de frontera** (uno por tercero) | Verificación del documento, listas de sanciones, proveedor de cotización, reporte a la autoridad, canal de voz y SMS | Cada uno falla, tarda o miente por su cuenta, y ninguno puede arrastrar el camino del pago. Tienen su propio reintento, su propia cola y su propio tiempo, medido aparte del techo de `RNF-09`. El canal de voz y SMS es además la **salida del código** de `RF-113`: el único camino hacia el emisor que no pasa por el mostrador | `RF-01`, `RF-26`, `RF-119`, `RF-07`, `RF-17`, `RF-25`, `RF-98`, `RF-113`, `RNF-09` |
| **Servicio de desafío** (proceso y base propios, credenciales propias) | La pregunta, la respuesta derivada, el contador de intentos, la comparación y **la llave que abre el sobre que el receptor sella** (`RF-114`) | `RNF-17` exige que el valor sea inalcanzable **para quien administra la infraestructura**. Un módulo del núcleo comparte credenciales con el núcleo; una base aparte con su propio administrador es el único mecanismo que hace declarable el invariante. Y es el único componente que puede tener la llave del dispositivo orientado al cliente sin que el mostrador la tenga | `RF-68`, `RF-101`, `RF-82`, `RF-83`, `RF-114`, `RF-122`, `RF-148`, `RNF-17` |
| **Punto de atención** (una instancia por mostrador, con almacén local) | El cliente de ventanilla, el **dispositivo orientado al cliente** que el operario no ve, el diario local de actos y la copia de catálogos de solo lectura | Está en una plaza de Huanta y pierde la conexión. `RF-100` obliga a que esa condición sea explícita en el diseño en vez de un accidente de red, y `RNF-05`, `RNF-06` y `RNF-13` son los tres invariantes que un punto desconectado podría romper si decidiera solo. Y `RF-113`, `RF-114` y `RF-147` obligan a que dentro del mostrador haya una superficie que el operario no lee **y por la que el receptor teclea él mismo el código y la respuesta**: es una frontera de despliegue, no una pantalla que se apaga | `RF-100`, `RF-42`, `RF-118`, `RF-144`, `RF-146`, `RF-57`, `RF-113`, `RF-114`, `RF-147`, `RNF-05`, `RNF-06`, `RNF-08`, `RNF-13` |

**Las tres capas.** Cada unidad se organiza en las mismas tres —presentación, lógica de negocio,
datos— y la regla que las hace útiles es una sola: **ninguna regla de negocio vive en presentación.**
Lo que Kevin ve o no ve (`RF-40`, `RF-57`) es una decisión de la capa de lógica que la presentación
obedece; si viviera en la pantalla, un cliente modificado en un mostrador afiliado la anularía, y el
mostrador afiliado es precisamente el vector que [Kevin](../../personas/Operario.MD) modela.

**El criterio del propio material no se cumple aquí, y por eso el argumento es otro.** El ejemplo
del material elige monolito 3-tier con el argumento de que su aplicación no tiene conexiones hacia
afuera —no está transcrito literal en este repositorio, así que se usa como criterio y no como
cita—. SendIt es lo contrario de ese caso: tiene al menos cinco conexiones hacia afuera
—verificación del documento oficial (`RF-01`), listas de sanciones (`RF-26`, `RF-27`), proveedor de
tipo de cambio (`RF-07`), la autoridad de origen a la que reporta (`RF-17`) y el canal de llamada o
mensaje de texto por el que se avisa al receptor (`RF-25`)—, y cada una falla, tarda o miente por su
cuenta. Y tiene además un extremo que puede quedar incomunicado: el punto de atención corre el
software de SendIt sobre el mostrador de un agente afiliado, está en una plaza de Huanta y puede
perder la conexión con los billetes del agente en la caja.

De modo que **el criterio del material queda descartado, no invocado**. El núcleo sigue siendo
monolítico, pero por un argumento distinto y que hay que decir con todas las letras: **no por
ausencia de fronteras externas, sino por presencia de una invariante contable.** `RNF-07` exige que
lo que sale de una cuenta entre en otra en el mismo acto, y `RNF-05` que ningún giro registre dos
entregas «en ningún punto y en ningún momento». Las dos son restricciones de una única transacción.
Un diseño en servicios las convierte en un protocolo de compensación —es decir, en dos escrituras
que pueden quedar a medias y un proceso que después arregla— y con dinero de terceros (`BR-01`)
«después se arregla» es exactamente la falla que el enunciado nombra como crítica. Se paga el precio
inverso, y también hay que decirlo: el núcleo monolítico se despliega entero o no se despliega, y una
regresión en el módulo de devoluciones detiene también la creación de giros.

**Las tres preguntas que la tabla tenía que responder, respondidas.**

- **¿Qué se aísla porque falla distinto?** Los cinco terceros, cada uno en su adaptador, con su
  reintento y su tiempo medido aparte de `RNF-09`; y el secreto del desafío, que no falla distinto
  sino que **se compromete distinto**. Ninguno está en el camino sincrónico del pago: la única
  llamada externa que el pago necesitaría —la lista de sanciones vigente de `RF-27`— se resuelve
  contra una **copia local versionada** y no contra el proveedor en vivo (decisión **(e)**).
- **¿Qué no se separa porque separarlo rompe una transacción?** El libro contable, el estado del
  giro, la clave de idempotencia, los acumulados de `RF-08`/`RF-09` y el de cobros del receptor de
  `RF-93`, y el efectivo por punto que `RF-95` descuenta al autorizar **cada pago y cada
  devolución**. Todo eso entra en la misma escritura o
  no vale: son las cinco cosas que tienen que ser verdad a la vez para que `RNF-07` sea comprobable.
- **¿El puesto de retenciones y el mostrador son el mismo sistema?** **No, y es un mecanismo, no un
  gusto de despliegue.** El **tablero de cumplimiento** es una unidad de presentación distinta, con
  su propio catálogo de permisos y su propia sesión: `RF-30` deriva el giro retenido a un rol
  distinto del que lo atendió, `RF-33` reserva la liberación al rol de cumplimiento, `RF-87` obliga a
  dejar el motivo escrito y `RNF-02` prohíbe que una misma identidad ejerza dos roles del mismo giro.
  La comprobación de `RNF-02` **no vive en el tablero**: vive en el núcleo, contra la traza de actos
  del giro, y rechaza la liberación aunque venga con credenciales válidas. El tablero separado
  impide el error; el núcleo impide el fraude.

## 2. Tipo de persistencia

La decisión es **por familia de dato, no global**. El propio material lo hace así en su ejemplo
—NoSQL para las imágenes, SQL para la metadata de usuario—, y aquí la diferencia es más marcada: el
mismo giro tiene una parte que exige integridad transaccional estricta y otra que es un binario de
megabytes que nunca se consulta salvo por auditoría.

| Familia de dato | Necesidad dominante | SQL / NoSQL / objetos / otro | Por qué | Decisión |
|---|---|---|---|---|
| Registro contable del dinero | Atomicidad multi-fila y suma comprobable en cualquier instante | **SQL relacional, solo-adición** | `RNF-07` es una restricción sobre un conjunto de filas escritas juntas: sin transacción no es declarable. `BR-13` y `RNF-03` prohíben corregir borrando | Tabla de asientos con línea de débito y crédito, restricción de suma cero por asiento, sin `UPDATE` ni `DELETE` concedidos al servicio. Es el único escritor de dinero del sistema |
| Giro y su estado | Lectura frecuente de un estado que **deriva** de los asientos | **SQL relacional, misma base y misma transacción que el asiento** | `RNF-06` y `RNF-13` prohíben dos afirmaciones incompatibles a la vez; escribir el estado en otra base o en otro momento es fabricar esa posibilidad | Proyección materializada del libro, escrita en la misma transacción que el asiento que la mueve, y **reconstruible desde el libro**. Cuando difieren, manda el libro y la proyección se reconstruye |
| Código de seguimiento (`RF-11`, `RF-113`, `RF-125`, `RF-147`, `RF-149`, `RNF-15`) | Comprobar sin poder mostrar | **SQL, y no el valor: su derivado** | `RNF-15`, citado como está: *«ni quien administra la infraestructura ni quien atiende el mostrador reconstruye un código: el sistema lo comprueba sin mostrárselo a ninguno de los dos»* — **dos lectores nombrados en el propio invariante**, y por eso acá no hace falta agregarle ninguna cláusula. Guardar el código en claro lo vuelve legible para el primero; mostrarlo en la pantalla del mostrador, para el segundo | Se genera con aleatoriedad criptográfica, **nunca se persiste en claro** y se persiste solo como derivado con sal por giro. Existe en claro durante un solo instante y en un solo lugar: el mensaje que sale hacia el **teléfono que el emisor registró** (`RF-11`). Al mostrador se le devuelve el acuse de que salió y nada más (`RF-125`). `RF-94` y `RF-113` dejan de ser políticas que alguien puede saltarse: son consecuencias — no hay fila que releer ni ruta que consultar. Y **entra por donde no lo toca el operario**: el receptor lo teclea él mismo en el dispositivo orientado al cliente (`RF-147`), igual que la respuesta del desafío |
| Efectivo recibido sin giro creado (`RF-118`) | Ser una obligación abierta con dueño, no un intento a medio terminar | **SQL, en la misma base contable y con asiento propio** | El efectivo de Rosa ya entró al cajón: `BR-01` lo vuelve pasivo de SendIt desde ese instante, aunque el giro nunca llegara a existir. Un registro que caduque solo deja dinero sin contrapartida | Fila de custodia en el núcleo, respaldada por su asiento contra `Obligación en custodia`, con el punto, el operario y el momento. Se cierra de una de dos formas —el giro se completa, o se devuelve el efectivo— y **ninguna es el paso del tiempo** |
| Oferta de punto alternativo y su plazo (`RF-91`, `RF-116`, `RF-111`) | Un ofrecimiento con vencimiento comunicado, que decide una devolución | **SQL en el núcleo, con fecha absoluta y no con plazo relativo** | `RF-116` obliga a informarle al emisor dentro de cuánto debe responder, y `RF-111` devuelve el giro si no responde dentro de **ese** plazo. Un temporizador en memoria no sobrevive a un reinicio, y el que se recalcula al vencer no es el que se le informó | Fila por oferta con `ofrecida_en`, el plazo tal como se comunicó y la fecha absoluta que produce; el `Vencimiento Job` barre por fecha. `RF-105` congela el punto elegido hasta que llega la respuesta o vence el plazo |
| Respuesta del desafío y sus intentos (`RF-68`, `RF-114`, `RF-82`, `RNF-17`) | Comprobar sin poder mostrar, **también frente al administrador de la infraestructura del giro** | **SQL en base propia, con credenciales propias, valor derivado con función lenta** | `RNF-17` prohíbe que la respuesta sea legible **para quien administre la infraestructura y para quien atiende el mostrador** desde que la ronda 12 lo extendió, y su invariante nombra a los dos lectores. Una columna de la base de giros incumple el primero por construcción, y una pantalla que la muestre incumple el segundo | Base separada, escrita solo por el servicio de desafío. Derivación lenta con sal por giro más una clave de servicio fuera de la base, de modo que ni con la base robada se prueban candidatos. Contador de intentos en la **misma** base, nunca en el giro (decisión **(f)**) |
| Acumulado del emisor en la ventana vigente (`RF-09`, `RF-10`) | Exactitud en el instante del rechazo, no rapidez | **SQL, agregado en la transacción de creación, sin caché** | `RF-08` y `RF-09` rechazan **antes** de registrar la recepción del efectivo. Un acumulado en caché de un minuto es una ventana para el fraccionamiento que `BR-04` existe para impedir | Consulta agregada sobre los giros del emisor con índice por identidad y fecha, dentro de la transacción y con bloqueo sobre la identidad del emisor. `RF-10` obliga a que la clave sea la identidad, no el punto |
| Acumulado de cobros del receptor en la ventana vigente (`RF-93`) | Igual que el anterior, del otro lado del mostrador | **SQL, agregado en la transacción de autorización, sin caché** | `RF-93` retiene en el momento de pagar; un contador atrasado paga el giro que había que retener | Misma forma, con **clave estable de receptor** —no una fila por giro—, que es lo que `S-15` del paso `E` ya anticipó que haría falta. La retención que produce cuelga de un caso de cumplimiento como cualquier otra, para que `RF-33` tenga quién la libere y `RF-87` qué motivo registrar |
| Identidad de personas | Confidencialidad frente al administrador, y borrabilidad selectiva | **SQL con cifrado por campo y clave fuera del motor** | `RNF-01`: «nadie que tenga acceso al almacenamiento reconstruye un documento de identidad». `RF-81` obliga a poder suprimir a una persona sin tocar la traza | Campos sensibles cifrados con clave por persona, custodiada fuera de la base. Suprimir es destruir esa clave, no recorrer filas: `RF-81` se ejecuta sin violar `RNF-03` |
| Binarios de identidad (imágenes) — evidencia que `RF-80` obliga a conservar | Volumen alto, lectura rarísima, retención larga | **Almacenamiento de objetos, cifrado por objeto** | Es el caso del ejemplo del material, agravado: `RNF-03` y `RF-18` obligan a conservarlos por el plazo más largo de los dos reguladores, con piso de cinco años. Una fila de base de datos no es el lugar | Un objeto por captura, cifrado con clave por giro; la fila relacional guarda puntero y huella, nunca el binario. Clase de almacenamiento frío después de la ventana de prescripción. `RF-99` borra el objeto del emisor que no llegó a crear giro; `RF-81` borra la clave |
| Resultado de tamizaje | Guardar entero un documento ajeno cuya forma decide un tercero | **NoSQL documental** | `RF-28` obliga a distinguir coincidencia exacta de homonimia y `RF-97` a re-tamizar cuando la lista cambia: hace falta la respuesta **completa** del proveedor como evidencia, y su esquema no es nuestro ni es estable | Un documento por tamizaje, con el veredicto y la **versión de lista** contra la que corrió, indexado por giro y por persona. El veredicto —y solo él— se copia al núcleo como campo |
| Traza de auditoría | Solo-adición demostrable y retención larga | **SQL solo-inserción, encadenada por huella, en base propia** | `RNF-03` («ningún acto registrado se modifica ni se borra») y `RNF-04` (todo acceso con autor, momento y giro). El encadenamiento hace que borrar una fila del medio sea detectable, no solo prohibido | Base con permiso de `INSERT` y nada más para todos los servicios; cada fila encadena la huella de la anterior; archivo a almacenamiento de objetos con retención inmutable pasada la ventana caliente |
| Cotizaciones de tipo de cambio | Vida corta como oferta, vida perpetua como evidencia | **SQL, y copiada por valor al giro** | `RF-07` obliga a producirla y fecharla; `RF-06` prohíbe recalcular el monto. Una clave foránea a una tabla que cambia no es una promesa: es una promesa que alguien puede editar | Tabla de cotizaciones con instante de emisión y vencimiento; al crear el giro, la tasa y el monto destino se **copian dentro del giro**, y el giro no vuelve a leer la tabla nunca más (decisión **(d)**). El giro rehecho de `RF-117` **copia la misma tasa del giro cancelado** aunque haya vencido hace rato: rehacer no es recotizar, y la comisión no se vuelve a cobrar porque el asiento que la registró sigue en pie |
| Catálogo de puntos, corredores y reguladores, y efectivo disponible en el corredor (`RF-20`, `RF-63`, `RF-15`, `RNF-12`, `RNF-14`) | Lectura muy frecuente sobre datos que cambian poco, salvo el saldo | **SQL versionado, con caché de solo lectura por versión para el catálogo y sin caché para el saldo** | `RF-63` ofrece la lista al emisor —tolera segundos de atraso—, pero `RF-20` exige efectivo disponible **antes** de dar el giro por fondeado, y ahí un saldo atrasado promete un pago que no existe | Catálogo cacheado por versión; disponibilidad del corredor derivada del libro y leída en la transacción, nunca del caché. **La tabla de corredores lleva más de un país de origen y más de una moneda destino desde la primera fila** (`RNF-12`, `RNF-14`): ninguna cifra ni consulta de este diseño supone un solo corredor, y por eso el par origen-destino es clave y no configuración |
| Efectivo que cada punto declara al abrir y al cerrar su caja (`RF-76`, `RF-92`) | Dos hechos por punto y turno que existen aunque no haya un solo giro | **SQL solo-adición** | `RF-76` registra declaraciones, no un saldo: una declaración corregida con `UPDATE` borra la única prueba de qué dijo el operario. Y `RF-95` descuenta cada pago **sin esperar al cierre** | Dos filas por punto y turno, inmutables. El saldo que `RF-92` le muestra al operario se deriva de la declaración de apertura más los asientos del libro de ese punto, no de un campo que alguien mantiene |
| Devolución pendiente de retiro y su plazo (`RF-14`, `RF-89`) | Es una obligación abierta, no un aviso | **SQL, en la misma base contable** | `RF-89` la mantiene disponible hasta la prescripción: un giro devuelto **no cierra**, sigue siendo pasivo de SendIt (`BR-01`) hasta que alguien retira el efectivo | Fila de obligación en el núcleo, respaldada por su asiento; el retiro es otro asiento, no un cambio de bandera |
| Declaración de diferencia hecha por el receptor **fuera del mostrador** (`RF-90`, `RF-180`, `RF-59`) | Testimonio identificado, no cálculo | **SQL solo-adición, en la base de casos** | `RF-59` obliga a **reponer toda diferencia comprobada** a quien le faltó —emisor o receptor— y `RF-143` a descontársela al agente en cuyo punto se originó: son dos hechos y no uno, y el segundo depende de que el primero esté comprobado. `RF-90` la hace entrar por llamada o mensaje de texto y `RF-180` exige identificar antes al declarante como el receptor designado: lo que Elena declaró tiene que sobrevivir intacto aunque la investigación concluya lo contrario, y **no puede depender de que la escriba el mostrador sobre el que se declara** | Un caso por declaración, inmutable, con la comprobación y la resolución agregadas como hechos posteriores y no como ediciones. `RF-104` resuelve con el agente en un caso aparte, y **antes** de tocar su liquidación: el descuento se le informa con la evidencia que lo sustenta y `RF-145` le deja objetarlo, así que la fila lleva el aviso, su evidencia, la objeción y no solo el importe |
| Estado que el punto sostiene mientras opera sin conexión | Durabilidad local con transacción, y **cero autoridad** | **Base embebida en el mostrador, solo-adición, firmada** | `RF-100` prohíbe autorizar lo que no se puede comprobar contra el centro: lo local no decide, solo **recuerda**. `RNF-08` exige recuperar sin que el operario cuente nada | Diario local append-only de intentos y actos, firmado por el punto, más copias de solo lectura de catálogos. Se sube entero al reconectar y el centro reconcilia. Nunca es fuente de verdad de un pago (decisión **(c)**) |

## 3. Diseño de la API

Los ejemplos del material listan rutas desnudas (`/tweet`, `/timeline`, `/user`, `/invoice`). Aquí
la tabla lleva tres columnas más y las tres son obligatorias:

- **Quién la usa** — la ventanilla donde Rosa origina, el canal de Elena, el mostrador de Kevin, o
  un proceso interno. Una ruta sin llamador identificado es una superficie de ataque sin dueño, y
  el enunciado dice que la seguridad es muy importante.
- **Qué garantiza** — y en particular, si es idempotente. **Un endpoint que mueve dinero y no
  declara su comportamiento ante el reintento es un defecto**, no una omisión de documentación.
- **Traza a** — el ítem del backlog que la exige. Una ruta sin ítem no existe.

**Convención de idempotencia**, que se aplica a toda fila marcada `IDEMP`: el llamador envía una
clave de intento en la cabecera `Idempotency-Key`; el servidor la persiste **antes** de escribir el
primer asiento; el reintento con la misma clave devuelve **la misma respuesta** y no ejecuta nada;
el reintento con la misma clave y distinto contenido devuelve `409` y no ejecuta nada. El detalle y
lo que cuesta están en la decisión **(b)**.

### Endpoints

| Método | Ruta | Quién la usa | Qué garantiza | Traza a |
|---|---|---|---|---|
| `POST` | `/cotizaciones` | Ventanilla de origen, por Rosa | Devuelve **cuatro cifras con nombre y no una**: monto en moneda destino —con el nombre de la moneda y no solo su cifra (`RF-05`)—, tasa, **margen aplicado sobre la cotización** (`RF-142`) y **comisión que se le cobra** (`RF-136`), más el instante de vencimiento. Los cuatro se devuelven **antes de que el emisor entregue el efectivo**, que es el borde temporal que los tres ítems comparten. **No reserva dinero y no crea nada.** Segura de repetir | `RF-05`, `RF-07`, `RF-136`, `RF-142` |
| `GET` | `/corredores/{origen}/{destino}` | Ventanilla de origen, por Rosa | Antes del efectivo: si el país destino se puede atender, desde cuándo el giro estará disponible, el plazo de una eventual devolución, cuánto puede durar como máximo una revisión y **dentro de cuánto se le avisará si el giro queda retenido**. Solo lectura, y los cuatro plazos se **copian al giro** al crearlo: lo que se informó es lo que después vence | `RF-19`, `RF-73`, `RF-77`, `RF-96`, `RF-115`, `RF-133` |
| `GET` | `/puntos?pais=&cerca_de=` | Ventanilla de origen, por Rosa | Lista de puntos del país destino con su capacidad declarada de pago, para que el emisor elija. Solo lectura, tolera atraso de segundos | `RF-63`, `RF-20` |
| `POST` | `/identificaciones` | Ventanilla de origen | Registra la verificación del documento y conserva la evidencia. Devuelve una referencia, **nunca el documento**. `IDEMP` | `RF-01`, `RF-80`, `RF-84`, `RNF-01` |
| `POST` | `/tamizajes` | Ventanilla de origen, antes del efectivo | Contrasta contra la copia versionada de listas **al emisor** (`RF-26`) **y al receptor designado** (`RF-119`), en dos filas y con dos veredictos: son dos personas distintas y una limpia no absuelve a la otra. Devuelve veredicto —limpio, homonimia o coincidencia exacta— y la versión de lista. **Nunca devuelve la entrada de la lista.** Segura de repetir | `RF-26`, `RF-119`, `RF-28`, `RF-78` |
| `POST` | `/giros` | Ventanilla de origen, por Rosa | Crea el giro **pendiente de efectivo** con un receptor y un país únicos, punto de atención elegido, y la cotización copiada por valor. **Al mostrador no le devuelve el código**: le devuelve el `giro_id` y **el acuse de que el código salió hacia el emisor, sin mostrárselo** (`RF-125`), por el canal y al teléfono que `RF-11` nombra. No hay segunda entrega ni ruta de lectura (`RF-94`, `RF-113`, `RNF-15`), y **el giro del que no hay constancia de que el código llegó queda no pagable** (`RF-149`) en vez de quedar mudo. Aplica las reglas de los **dos** reguladores y rechaza si son incompatibles en vez de elegir una (`RF-15`, `RF-16`), y no crea en origen lo que el regulador de destino ya rechazó (`RF-23`). El receptor designado queda fijo: no hay ruta que lo altere después (`RF-70`). `IDEMP` | `RF-03`, `RF-04`, `RF-11`, `RF-15`, `RF-16`, `RF-23`, `RF-63`, `RF-70`, `RF-94`, `RF-113`, `RF-125`, `RF-149`, `RNF-15` |
| `POST` | `/giros/{id}/desafio` | Dispositivo orientado al cliente, tecleado por Rosa | Registra pregunta y respuesta. Responde sin cuerpo: **no hay lectura de vuelta, para nadie**. El transporte lo cifra el dispositivo contra el servicio de desafío; el punto de atención no tiene la clave | `RF-68`, `RF-101`, `RNF-17` |
| `POST` | `/giros/{id}/autorizaciones` | Segundo rol, nunca el mismo operario | Otorga la segunda autorización sobre el umbral reforzado. Rechaza si la identidad ya actuó sobre este giro. `IDEMP` | `RF-13`, `RNF-02` |
| `POST` | `/giros/{id}/recepcion-efectivo` | Ventanilla de origen | **El acto que da el giro por creado.** Comprueba límite por operación, acumulado del emisor y efectivo en el corredor; escribe el asiento; deja el giro fondeado. Los tres rechazos de límite corren **antes de que el operario reciba el efectivo** (`RF-08`, `RF-09`), que es lo que permite detener en vez de revertir. Fija `disponible_desde` dentro del techo de `RNF-10`. Si se interrumpe con el efectivo ya en el cajón, **no deshace: deja custodia abierta** (`RF-118`) y el asiento que la respalda, con la fecha en que `RF-138` la devolverá si nadie la retoma. `IDEMP` | `RF-79`, `RF-08`, `RF-09`, `RF-10`, `RF-20`, `RF-36`, `RF-118`, `RF-138`, `RNF-07`, `RNF-10` |
| `GET` | `/puntos/{id}/pendientes` | Punto de atención, por el operario | Lo que quedó a medias en ese mostrador, **en un solo estado que se lee y se retoma**: los giros interrumpidos (`RF-42`) y el efectivo recibido sin giro creado (`RF-118`), **cada uno con la acción ofrecible que lleva asociada** (`RF-39`) **y que se le muestra sobre el giro que tiene delante** (`RF-130`), no con un código de estado. Solo lectura | `RF-42`, `RF-118`, `RF-39`, `RF-130` |
| `POST` | `/custodias/{id}/vencimiento` | Proceso interno, tarea minutada | **Cierra el efectivo en custodia que nadie retomó** al vencer `[ASSUMPTION: 72 horas]`: abre la devolución al emisor con su asiento y deja la custodia en `devuelta` (`RF-138`). **No purga la fila y no caduca nada** — salda un pasivo de `BR-01`, que es lo contrario de un TTL. Avisa al emisor dónde retirarla (`RF-14`, `RF-72`). `IDEMP` por custodia | `RF-138`, `RF-118`, `RF-14`, `RF-72`, `RNF-07` |
| `POST` | `/giros/{id}/pago/resolucion` | Proceso interno, **nunca el operario** | **El terminador del pago dejado en duda por `RF-144`.** Lo resuelve **contra el registro del centro** —el libro, y el diario firmado que sube `POST /puntos/{id}/sincronizacion`— hacia `resuelta como pagada` (el giro cierra por `RF-64`) o `resuelta como no pagada` (el giro vuelve a ser arrendable), **sin intervención del operario** (`RF-146`, `RNF-08`). No acepta un cuerpo que declare el resultado: lo deriva. `IDEMP` por giro | `RF-144`, `RF-146`, `RF-64`, `RNF-05`, `RNF-08` |
| `GET` | `/giros?emisor={id}` | Rosa, sin depender del receptor | Estado de sus giros, con lo disponible para cobro distinguido de lo que todavía no lo está, y lo retenido con su fecha límite —nunca su motivo. Solo lectura | `RF-52`, `RF-53`, `RF-66` |
| `POST` | `/receptores/verificacion` | **Adaptador de canal → centro, por Elena desde su teléfono** | **La compuerta de identidad del receptor, que antes no existía porque no existía ninguna entrada suya.** `RF-180` obliga a identificar como el receptor designado a quien declara una diferencia fuera del mostrador **antes de admitir su declaración**, y la misma compuerta sirve a `RF-128`. El mecanismo, elegido acá porque el ítem manda el qué y no el cómo: (1) el número desde el que llega la llamada o el mensaje se compara contra `telefono_token` del receptor designado —el mismo que `RF-25` y `RF-41` ya usan para avisarle—; (2) sobre ese número se despacha un verificador de un solo uso y vida de minutos, **que no es el código de seguimiento** (`RF-94`, `RNF-15` lo prohíben) **ni consume el cupo de intentos del desafío** (`RF-82` los cuenta para pagar, no para consultar). Devuelve una sesión de canal acotada a los giros de ese receptor. `IDEMP` por número y ventana | `RF-180`, `RF-128`, `RF-25`, `RF-41` |
| `GET` | `/giros?receptor={id}` | **Elena, sin depender del emisor**, sobre la sesión de canal de arriba | Estado de los giros a su nombre: cuáles hay, de qué monto, si están disponibles para cobro y en qué punto (`RF-128`). **Devuelve estrictamente menos que la ruta del emisor**: nunca el código ni parte de él (`RNF-15`), nunca la respuesta ni la pregunta del desafío (`RF-101`, `RNF-17`), y del giro retenido solo el hecho —el motivo está prohibido de revelar por `RF-40` y no tiene por qué llegarle a ella. Solo lectura | `RF-128`, `RF-180`, `RF-53`, `RNF-15` |
| `POST` | `/giros/{id}/cancelacion` | Rosa, **nunca el receptor** | Cancela mientras el dinero no esté a disposición del receptor, solo a pedido del emisor que lo creó, y abre la devolución. Vale también —y sobre todo— para el giro **cuyo código se perdió**: `RF-46` es la única salida que `RF-94` deja, y desde la ronda 12 es un solo título y no dos, porque `RF-110` decía el mismo borde palabra por palabra. Rechaza sobre un giro entregado, y avisa al receptor que ese giro se devolvió al emisor —`RF-47` hace de la cancelación una devolución y `RF-106` avisa **toda** devolución, así que no hace falta un ítem propio para este caso. `IDEMP` | `RF-46`, `RF-47`, `RF-48`, `RF-106`, `RNF-13` |
| `POST` | `/giros/{id}/rehacer` | Rosa, sobre un giro suyo cancelado por `RF-46` | Crea un giro nuevo **al mismo receptor**, **conservando la cotización que fijó el giro cancelado** (`RF-134`) y **sin volver a cobrar la comisión** (`RF-135`); emite código nuevo por el canal de `RF-11`, con el acuse de `RF-125` al mostrador. Vuelve a correr enteros los controles de uno nuevo —tamizaje de las dos puntas, límites del emisor, doble control sobre el umbral, efectivo en el corredor— porque un giro rehecho es un giro (`RF-123`). `IDEMP` | `RF-117`, `RF-134`, `RF-135`, `RF-123`, `RF-46`, `RF-26`, `RF-119`, `RF-08`, `RF-09` |
| `POST` | `/giros/{id}/punto-alternativo` | Ventanilla u operario, con respuesta del emisor | Ofrece otro punto del mismo distrito cuando el elegido no puede pagar e **informa al emisor dentro de cuánto debe responder** (`RF-116`), abriendo la oferta con fecha absoluta de vencimiento. **No cambia nada sin la respuesta del emisor** (`RF-105`), y avisa al receptor que el punto cambió y a cuál ir (`RF-109`, `RF-124`). **Cuando en el distrito elegido no queda ningún punto capaz de pagar, no hay nada que ofrecer y el giro se devuelve al emisor** (`RF-129`). `IDEMP` | `RF-91`, `RF-105`, `RF-116`, `RF-109`, `RF-124`, `RF-129`, `RF-39`, `RF-130` |
| `POST` | `/giros/{id}/punto-alternativo/vencimiento` | Proceso interno, tarea minutada | Vence la oferta que el emisor no contestó **dentro del plazo que `RF-116` le informó** —no dentro de uno recalculado después— y devuelve el giro al emisor. `IDEMP` por oferta | `RF-111`, `RF-116` |
| `POST` | `/giros/{id}/arrendamiento` | Punto de atención → centro | Emite el **arrendamiento exclusivo** del giro a ese punto, por una ventana corta: re-tamiza contra listas vigentes, comprueba fondos confirmados y efectivo del punto, y mientras el arrendamiento vive el centro no dispone del giro en ningún otro lado. **Solo se obtiene en línea.** `IDEMP` | `RF-27`, `RF-36`, `RF-100`, `RNF-06` |
| `GET` | `/puntos/{id}/efectivo` | Punto de atención, **antes de cada pago y de cada devolución** | Efectivo disponible en ese punto, derivado de la declaración de apertura y del libro, que `RF-95` descuenta en cada pago y en cada devolución sin esperar al cierre. Solo lectura | `RF-92`, `RF-95` |
| `POST` | `/puntos/{id}/caja` | Punto de atención → centro | Registra la declaración de apertura o de cierre de caja. Solo-adición: no corrige la anterior. Al cerrar, calcula la diferencia entre el efectivo **esperado** —derivado del libro— y el **declarado**, y **se la informa al agente** (`RF-141`) por `POST /avisos`: es la única cifra de este documento cuyo destinatario no es una de las tres personas del backlog. `IDEMP` | `RF-76`, `RF-141` |
| `POST` | `/giros/{id}/desafio/intentos` | Dispositivo orientado al cliente → centro, **con el punto de atención solo como transporte** | Recibe el sobre que **el receptor selló él mismo** en el dispositivo que el operario no ve ni teclea (`RF-114`) y **devuelve un veredicto, nunca el valor**. Consume un intento del cupo acotado; informa cuántos quedan y nada más. Corre solo en el centro. **No es idempotente y no debe serlo**: cada envío es un intento | `RF-69`, `RF-82`, `RF-83`, `RF-86`, `RF-114`, `RF-122`, `RF-148`, `RNF-17` |
| `POST` | `/giros/{id}/pago` | Punto de atención → centro | Registra la entrega en efectivo contra código y documento, por el monto fijado y sin cobrarle nada al receptor; descuenta el efectivo del punto y cierra el giro. Exige documento vigente **salvo el único relevo que el backlog admite**: desafío respondido correctamente (`RF-122`), que el centro comprueba contra el veredicto y no contra lo que diga el mostrador. Exige arrendamiento vigente. `IDEMP`, **y además con unicidad natural**: el libro tiene una sola entrega por giro | `RF-02`, `RF-34`, `RF-85`, `RF-86`, `RF-122`, `RF-64`, `RF-95`, `RF-102`, `RNF-05`, `RNF-16` |
| `POST` | `/giros/{id}/diferencias` | **Adaptador de canal → centro, por el receptor, desde su llamada o su mensaje de texto** (`RF-90`) | Registra la declaración de Elena de que el dinero recibido no coincide con lo informado, **después de identificarla como el receptor designado** (`RF-180`, ver `POST /receptores/verificacion`). **Ya no entra por el mostrador**: `RF-90` la hace entrar por el canal de Elena, y ese cambio importa porque el punto sobre el que se declara es aquel al que `RF-143` le descuenta la diferencia — pedirle a Kevin que la escriba era pedirle que se acusara solo. Toda diferencia registrada se informa **a las dos puntas**: al emisor (`RF-60`) y al receptor (`RF-121`); la comprobada se repone a quien le faltó (`RF-59`) y se descuenta al agente por el camino de `RF-104` y `RF-143`. Solo-adición. `IDEMP` | `RF-90`, `RF-180`, `RF-59`, `RF-60`, `RF-121` |
| `POST` | `/puntos/{id}/sincronizacion` | Punto de atención → centro | Sube el diario local completo y baja el estado autoritativo. **Sin intervención del operario**: no se le pregunta qué pasó (`RNF-08`, `RF-146`). Es la fuente con la que se resuelve el pago dejado `en duda` por `RF-144`, junto con el libro. Repetible sin efecto: el diario es solo-adición y el centro descarta lo ya visto | `RF-100`, `RF-42`, `RF-144`, `RF-146`, `RNF-05`, `RNF-06`, `RNF-08`, `RNF-13` |
| `GET` | `/retenciones` | Rol de cumplimiento, en su tablero | Lista de giros retenidos con su plazo y su clase de coincidencia, separando exacta de homonimia. Excluye los giros que el propio solicitante atendió | `RF-29`, `RF-30`, `RF-28`, `RF-78` |
| `POST` | `/retenciones/{id}/liberacion` | Rol de cumplimiento, distinto del que atendió | Libera el giro —potestad reservada al rol de cumplimiento por `RF-33`— **exigiendo motivo escrito** (`RF-87`); rechaza si la identidad ya ejerció otro rol sobre el giro (`RNF-02`), y avisa al emisor por su canal que su giro dejó de estar retenido (`RF-127`). `IDEMP` | `RF-33`, `RF-87`, `RF-127`, `RNF-02` |
| `POST` | `/retenciones/{id}/vencimiento` | Proceso interno, tarea diaria | Vence la retención no liberada en plazo y dispara la devolución al emisor, avisando también al receptor de que ese giro se devolvió (`RF-106`). `IDEMP` por retención | `RF-31`, `RF-32`, `RF-106` |
| `GET` | `/receptores/{id}/acumulado` | Proceso interno → rol de cumplimiento | Cobros de ese receptor en la ventana vigente `[ASSUMPTION: 30 días corridos]`, contados sobre identidad estable. Es la lectura que retiene cuando se supera, y la retención que abre lleva su caso, su plazo y su rol de liberación como cualquier otra | `RF-93`, `RF-31`, `RF-33` |
| `POST` | `/tamizajes/relista` | Proceso interno, al cambiar una lista | Re-tamiza los giros no pagados contra la versión nueva. El giro que pasa a coincidir queda **retenido** (`RF-29`), con el plazo de `RF-31`, y el aviso al receptor sale por `RF-37` — **no** anuncia una devolución, porque la devolución la produce el vencimiento de la retención (`RF-32`) y no el cambio de lista: por eso `RF-108` se retiró. `IDEMP` por versión de lista | `RF-97`, `RF-27`, `RF-29`, `RF-37` |
| `POST` | `/reportes-autoridad` | Proceso interno → autoridad de origen **y autoridad de destino** | Reporta el giro sobre el umbral transfronterizo, medido **sobre el giro completo** y no sobre su tramo local (`RF-22`). Son **dos reportes y dos umbrales**: el de origen (`RF-17`) y el de la jurisdicción de destino (`RF-139`), y ninguno absuelve al otro. Es la **única** ruta del sistema autorizada a leer la fecha de nacimiento del emisor y del receptor, y solo cuando el reporte que se está armando la exige (`RF-140`). `IDEMP` por giro, lado y periodo | `RF-17`, `RF-139`, `RF-140`, `RF-22` |
| `POST` | `/avisos` | Proceso interno → canal de voz y SMS; **y al agente**, para la diferencia de cierre de caja y el descuento por diferencia | Entrega el aviso por llamada o mensaje de texto, sin exigir aplicación ni datos, y **conserva constancia oponible de haberlo enviado** (`RF-98`): destinatario, hecho, momento, texto y acuse del operador. **Registra si llegó cuando el canal lo reporta** (`RF-131`) y **trata como no avisado a quien no tenga constancia de que llegó** (`RF-132`) — de modo que un despacho sin acuse reencola y **no** da por cumplida ninguna obligación que dependa de haber avisado. Toma **destinatario** como parámetro y no lo deduce, porque el mismo hecho tiene dos avisos con dos textos —la diferencia se le informa al emisor por `RF-60` y al receptor por `RF-121`, y la prescripción al emisor por `RF-51` y al receptor por `RF-120`—. El aviso de retención al emisor sale **dentro del plazo que `RF-115` le prometió** y **nunca más de una hora después de la retención** (`RF-133`), no cuando el proceso pase. `IDEMP` por hecho **y destinatario**: un reintento del canal no genera un aviso nuevo | `RF-25`, `RF-37`, `RF-41`, `RF-51`, `RF-60`, `RF-65`, `RF-67`, `RF-69`, `RF-75`, `RF-91`, `RF-98`, `RF-104`, `RF-106`, `RF-109`, `RF-115`, `RF-116`, `RF-120`, `RF-121`, `RF-124`, `RF-127`, `RF-131`, `RF-132`, `RF-133`, `RF-141`, `RF-156` |
| `GET` | `/devoluciones?emisor={id}` | Rosa | Devoluciones disponibles y en qué punto retirarlas, con su plazo. Solo lectura | `RF-14`, `RF-72`, `RF-89` |
| `POST` | `/devoluciones/{id}/retiro` | Punto elegido por el emisor → centro | Entrega la devolución **en efectivo y en la moneda que el emisor entregó**, con la comisión incluida cuando el giro no llegó a pagarse. Escribe el asiento que cierra la obligación. `IDEMP` | `RF-71`, `RF-74`, `RF-88`, `RF-89` |
| `POST` | `/prescripciones` | Proceso interno, tarea diaria | Deja no pagable el giro vencido y pone el monto a disposición del emisor. El aviso previo sale **a las dos puntas y como dos avisos distintos**: al emisor, que puede cancelar y cobrar la devolución (`RF-51`); al receptor, que todavía está a tiempo de ir a cobrar (`RF-120`). Y da por prescrita la **devolución** que nadie retiró al vencer su plazo, dejando de mantenerla disponible (`RF-137`), con el asiento que cierra la obligación. `IDEMP` por giro | `RF-49`, `RF-50`, `RF-51`, `RF-120`, `RF-137`, `RF-89` |
| `POST` | `/correcciones` | Segundo rol, sobre un giro pagado. **Nunca una identidad que opere un mostrador** | Registra la corrección del monto como **movimiento nuevo**, nunca editando el anterior, y exige la autorización de un segundo rol (`RF-61`). Rechaza la solicitud cuando el solicitante tiene punto de atención asignado: `RNF-02` prohíbe que quien atiende un mostrador **inicie** la corrección de un giro pagado, y esa es la mitad del invariante que este endpoint no comprobaba. Repone al emisor o al receptor, según a quién le faltó, **toda diferencia comprobada** (`RF-59`). `IDEMP` | `RF-56`, `RF-61`, `RF-59`, `RNF-02`, `RNF-03` |
| `POST` | `/liquidaciones` | Proceso interno → agente afiliado | Liquida con el agente el efectivo que puso de su caja, en el plazo acordado con él, contra la cuenta del libro que lo registra (`RF-24`). **Descuenta la diferencia repuesta que se originó en su punto** (`RF-143`) y **ninguna que no le haya sido informada antes, con la evidencia que la sustenta** (`RF-104`): el aviso precede al asiento, no lo acompaña, y un descuento sin fecha de aviso no entra. Tampoco entra el que está objetado (`RF-145`). `IDEMP` por agente y periodo | `RF-24`, `RF-104`, `RF-143`, `RF-145` |
| `POST` | `/liquidaciones/descuentos/{id}/objecion` | **Agente afiliado → centro**, sobre un descuento que ya le fue informado | Recibe la objeción del agente a un descuento por diferencia **antes de que se aplique a su liquidación** (`RF-145`). Mientras la objeción vive, el descuento no entra en ninguna corrida de `POST /liquidaciones`: `RF-104` ya exigía el aviso previo con evidencia, y `RF-145` agrega que el aviso tiene que poder ser contestado — un aviso que no admite respuesta es una notificación, no un control. Solo-adición: la objeción no se edita, se resuelve con otra fila. `IDEMP` | `RF-145`, `RF-104`, `RF-143` |
| `POST` | `/supresiones` | Rosa → proceso interno | Suprime los datos personales **de quien los pide y de nadie más**, destruyendo la clave de su evidencia. No toca la traza de actos, que prevalece. `IDEMP` | `RF-81`, `RF-99`, `RNF-03` |

**Cuarenta rutas para cuarenta y siete capacidades**, contra un backlog de **155 ítems** —138
funcionales y 17 no funcionales—. El conteo anterior —35 y 36— quedó sin valor cuando el backlog pasó
de 137 a 155, y rehacerlo no fue sumar: **cinco rutas nuevas** aparecieron porque cinco capacidades
no tenían ninguna —la superficie del receptor (`RF-180`, `RF-128`), el vencimiento de la custodia
(`RF-138`), la resolución del pago en duda (`RF-146`), la objeción del agente (`RF-145`)—, y
**ninguna ruta vieja se cayó**, porque cada una se volvió a comprobar contra un título vivo: las que
colgaban de `RF-21`, `RF-45`, `RF-58` o `RF-107` cuelgan ahora de lo que los cubre. Las capacidades
que este caso obliga a exponer y el ítem del que cada una cuelga están abajo; **cada endpoint de
arriba traza a una fila de esta tabla, y cada fila de esta tabla tiene al menos un endpoint**.

| Capacidad obligada | Traza a | Llamador | Endpoint que la sirve |
|---|---|---|---|
| Cotizar e informar antes del efectivo el monto en moneda destino, **la comisión y el margen** | `RF-05`, `RF-07`, `RF-136`, `RF-142` | Ventanilla de origen | `POST /cotizaciones` |
| Informar antes del efectivo lo que el emisor tiene que saber: desde cuándo se cobra, el plazo de una eventual devolución, cuánto dura como máximo una revisión, dentro de cuánto se le avisará si el giro queda retenido y si el país destino se puede atender | `RF-77`, `RF-73`, `RF-96`, `RF-115`, `RF-19` | Ventanilla de origen | `GET /corredores/{origen}/{destino}` |
| Elegir el punto de atención donde cobrará el receptor | `RF-63` | Ventanilla de origen, por el emisor | `GET /puntos` |
| Identificar al emisor y conservar la evidencia | `RF-01`, `RF-80`, `RF-84` | Ventanilla de origen | `POST /identificaciones` |
| Tamizar a las dos puntas antes de aceptar el efectivo — al emisor y al receptor designado, en dos contrastes y no en uno | `RF-26`, `RF-119`, `RF-28`, `RF-78` | Ventanilla de origen | `POST /tamizajes` |
| Crear el giro con un receptor y un país únicos e inalterables, aplicando las reglas de los dos reguladores | `RF-03`, `RF-04`, `RF-15`, `RF-16`, `RF-23`, `RF-63`, `RF-70` | Ventanilla de origen | `POST /giros` |
| Hacer llegar el código únicamente al emisor por su canal, **sin que quien atiende pueda leerlo, transcribirlo ni volver a consultarlo — y confirmándole que salió** | `RF-11`, `RF-94`, `RF-113`, `RF-125`, `RF-149`, `RNF-15` | Ventanilla de origen; la salida del código, adaptador de canal → teléfono registrado del emisor | `POST /giros` |
| Registrar la pregunta del desafío y su respuesta al crear el giro | `RF-68`, `RF-101`, `RNF-17` | Ventanilla de origen, por el emisor | `POST /giros/{id}/desafio` |
| Registrar la recepción del efectivo, que es lo que da el giro por creado | `RF-79`, `RF-08`, `RF-09`, `RF-20` | Ventanilla de origen | `POST /giros/{id}/recepcion-efectivo` |
| Dejar en un estado único, legible y retomable lo que quedó a medias — el giro interrumpido **y el efectivo ya recibido sin giro creado** | `RF-42`, `RF-118`, `RF-43` | Punto de atención, por el operario | `GET /puntos/{id}/pendientes`, `POST /giros/{id}/recepcion-efectivo` |
| **Mostrarle al operario la acción ofrecible del giro que tiene delante**, sobre un catálogo que cubre los tres estados sin excepción | `RF-39`, `RF-130`, `RF-40` | Punto de atención, por el operario | `GET /puntos/{id}/pendientes`, `POST /giros/{id}/punto-alternativo` |
| **Devolver al emisor el efectivo en custodia que nadie retomó**, saldando el pasivo en vez de dejarlo abierto | `RF-138`, `RF-118` | Proceso interno | `POST /custodias/{id}/vencimiento` |
| **Dejar en un estado único el pago cuya confirmación no llegó, y resolverlo contra el registro del centro sin intervención del operario** | `RF-144`, `RF-146` | Proceso interno, nunca el operario | `POST /giros/{id}/pago/resolucion`, `POST /puntos/{id}/sincronizacion` |
| Pedir y otorgar la segunda autorización | `RF-13`, `RF-61` | Segundo rol, nunca el mismo operario | `POST /giros/{id}/autorizaciones`, `POST /correcciones` |
| Avisar al receptor por llamada o mensaje de texto: que hay un giro, cuánto cobrará, **la pregunta del desafío cuando no tiene documento vigente**, si el punto puede pagarle y a cuál ir si deja de poder, si quedó retenido —incluido cuando lo retiene un cambio de lista—, si se devolvió, la diferencia registrada, **que su reposición está disponible y en qué punto retirarla** y la prescripción que se acerca | `RF-25`, `RF-41`, `RF-69`, `RF-75`, `RF-37`, `RF-106`, `RF-109`, `RF-120`, `RF-121`, `RF-124`, `RF-156` | Proceso interno hacia el canal de Elena | `POST /avisos` |
| Avisar al emisor por llamada o mensaje de texto: que su giro fue cobrado, que pasó a retenido **dentro del plazo prometido y nunca más de una hora después**, **que dejó de estar retenido**, la diferencia registrada, la prescripción que se acerca y la devolución disponible | `RF-65`, `RF-67`, `RF-115`, `RF-133`, `RF-127`, `RF-60`, `RF-51`, `RF-14` | Proceso interno hacia el canal de Rosa | `POST /avisos` |
| Reportar a la autoridad de origen **y a la del país de destino**, cada una contra su umbral, con la fecha de nacimiento cuando el reporte la exige | `RF-17`, `RF-139`, `RF-140`, `RF-22` | Proceso interno hacia las dos autoridades | `POST /reportes-autoridad` |
| Listar y decidir giros retenidos | `RF-29`, `RF-30` | Rol de cumplimiento | `GET /retenciones` |
| Liberar una retención —solo el rol de cumplimiento— dejando registrado el motivo, y **avisarle al emisor que dejó de estar retenido** | `RF-33`, `RF-87`, `RF-127` | Rol de cumplimiento, distinto del que atendió | `POST /retenciones/{id}/liberacion` |
| Retener al receptor que superó su acumulado de cobros en la ventana | `RF-93`, `RF-31` | Proceso interno hacia el rol de cumplimiento | `GET /receptores/{id}/acumulado` |
| Volver a tamizar cuando cambia una lista, retener el giro que pasa a coincidir y avisarle al receptor que quedó retenido | `RF-97`, `RF-29`, `RF-37` | Proceso interno | `POST /tamizajes/relista` |
| Autorizar el pago hacia el punto contra las listas vigentes | `RF-27`, `RF-36` | Centro → punto de atención | `POST /giros/{id}/arrendamiento` |
| Informar al operario el efectivo de su punto antes de habilitarle **un pago o una devolución** | `RF-92`, `RF-95` | Centro → punto de atención | `GET /puntos/{id}/efectivo` |
| Declarar el efectivo del punto al abrir y al cerrar la caja | `RF-76` | Punto de atención → centro | `POST /puntos/{id}/caja` |
| **Informarle al agente la diferencia entre el efectivo esperado y el declarado en cada cierre de caja de sus puntos** | `RF-141` | Proceso interno hacia el agente | `POST /puntos/{id}/caja`, `POST /avisos` |
| Recibir del propio receptor **el código del giro y la respuesta del desafío, sin que quien atiende los lea ni los digite**, y comprobarlos con intentos acotados | `RF-114`, `RF-147`, `RF-69`, `RF-82`, `RF-83`, `RNF-17` | Dispositivo orientado al cliente → centro, con el punto solo como transporte. **Nunca devuelve la respuesta: devuelve el veredicto** | `POST /giros/{id}/desafio/intentos` |
| Autorizar el pago con documento vencido cuando el desafío se respondió bien, y solo entonces | `RF-122`, `RF-86`, `RF-69` | Punto de atención → centro; lo resuelve el centro contra el veredicto, nunca el mostrador | `POST /giros/{id}/desafio/intentos`, `POST /giros/{id}/pago` |
| Confirmar el cobro desde el mostrador, en efectivo y por el monto fijado | `RF-34`, `RF-85`, `RF-86`, `RF-02`, `RF-102`, `RF-64`, `RF-65`, `RNF-16` | Punto de atención → centro | `POST /giros/{id}/pago` |
| Cobrar en otro punto del país destino cuando el elegido no puede pagar, **con plazo de respuesta informado** y con las dos puntas avisadas | `RF-91`, `RF-105`, `RF-116`, `RF-109`, `RF-124` | Punto de atención → centro; el aviso, proceso interno hacia las dos puntas | `POST /giros/{id}/punto-alternativo` |
| Devolver el giro cuya respuesta al punto alternativo no llegó dentro del plazo que se le informó | `RF-111`, `RF-116` | Proceso interno | `POST /giros/{id}/punto-alternativo/vencimiento` |
| **Identificar al receptor designado antes de admitirle nada fuera del mostrador** | `RF-180` | Adaptador de canal → centro, por el receptor | `POST /receptores/verificacion` |
| Registrar **por llamada o mensaje de texto** la declaración del receptor de que el dinero no coincide, y reponer a quien le faltó toda diferencia comprobada | `RF-90`, `RF-180`, `RF-59` | Adaptador de canal → centro, por el receptor | `POST /giros/{id}/diferencias` |
| **Consultar el estado de los giros a nombre del receptor, sin depender del emisor** | `RF-128`, `RF-180` | Receptor, sobre su sesión de canal | `GET /giros?receptor={id}` |
| Sincronizar un punto que estuvo sin conexión, sin preguntarle nada al operario | `RF-100`, `RF-42`, `RNF-05`, `RNF-06`, `RNF-08`, `RNF-13` | Punto de atención → centro | `POST /puntos/{id}/sincronizacion` |
| Consultar el estado de los giros propios | `RF-52`, `RF-53`, `RF-66` | Emisor | `GET /giros?emisor={id}` |
| Cancelar y devolver, incluido el giro cuyo código se perdió, y avisarle al receptor que se devolvió | `RF-46`, `RF-47`, `RF-106`, `RNF-13` | Emisor, nunca el receptor (`RF-48`) | `POST /giros/{id}/cancelacion` |
| Rehacer al mismo receptor el giro cancelado, **conservando la cotización que fijó el cancelado** y **sin recobrar la comisión**, con los controles corridos otra vez enteros | `RF-117`, `RF-134`, `RF-135`, `RF-123`, `RF-46` | Emisor → ventanilla de origen | `POST /giros/{id}/rehacer` |
| Avisar la devolución disponible y dónde retirarla | `RF-14`, `RF-72` | Proceso interno hacia el emisor | `GET /devoluciones`, `POST /avisos` |
| Retirar la devolución en efectivo, en la moneda entregada, con su comisión | `RF-71`, `RF-88`, `RF-74`, `RF-89` | Punto de atención elegido por el emisor → centro | `POST /devoluciones/{id}/retiro` |
| Vencer una retención, devolver al emisor y avisar al receptor de que el giro se devolvió | `RF-31`, `RF-32`, `RF-106` | Proceso interno | `POST /retenciones/{id}/vencimiento` |
| Prescribir, poner el monto a disposición del emisor y avisar antes a las dos puntas | `RF-49`, `RF-50`, `RF-51`, `RF-120` | Proceso interno | `POST /prescripciones` |
| **Dar por prescrita la devolución que nadie retiró y dejar de mantenerla disponible** | `RF-137`, `RF-89` | Proceso interno | `POST /prescripciones` |
| **Devolver el giro para el que no queda ningún punto capaz de pagar en el distrito elegido** | `RF-129`, `RF-91` | Proceso interno | `POST /giros/{id}/punto-alternativo` |
| Liquidar con el agente el efectivo que puso de su caja, **descontándole la diferencia repuesta originada en su punto** e informándole antes cada descuento con su evidencia | `RF-24`, `RF-104`, `RF-143` | Proceso interno hacia el agente | `POST /liquidaciones` |
| **Admitirle al agente una objeción al descuento antes de aplicarlo** | `RF-145`, `RF-104` | Agente afiliado → centro | `POST /liquidaciones/descuentos/{id}/objecion` |
| Suprimir a pedido los datos personales de quien los entregó | `RF-81`, `RF-99` | Emisor → proceso interno, acotado por lo que `RNF-03` obliga a conservar | `POST /supresiones` |
| **Conservar constancia de cada aviso, registrar si llegó y tratar como no avisado a quien no la tenga** | `RF-98`, `RF-131`, `RF-132` | Proceso interno | `POST /avisos` |

**Tres ausencias deliberadas, porque una API se define también por lo que no expone.** No hay
`GET /giros/{id}/desafio` ni `GET /giros/{id}/codigo`: `RNF-17` y `RNF-15` los prohíben, y una ruta
que no existe es un control más fuerte que una ruta con permisos. La variante que quedaba
—**volver a consultar un código ya entregado**— la cierra `RNF-15` del mismo modo: no existe la
ruta, ni siquiera para el mostrador que lo acaba de crear, de modo que la prohibición no depende de
un permiso que alguien pueda concederse. Desde la ronda 12 esto no necesita ítem propio: `RF-112`
decía lo que `RF-113` y `RNF-15` ya dicen, y se retiró. La tercera es `GET /giros/{id}/motivo-retencion`: `RF-40`
omite el motivo al operario cuando revelarlo está prohibido, y lo que se le sirve es la acción
ofrecible de `RF-39` y `RF-130`, elegida por **clase de estado** y nunca por causa.

**Y una cuarta ausencia que dejó de serlo, porque el backlog la abrió.** Este documento afirmaba
que *«no hay ningún endpoint de consulta dirigido al receptor»* y lo fundaba en que Elena no es
clienta de SendIt. Eso **ya no es cierto**, y no porque el diseño haya cambiado de opinión: `RF-128`
—*permitirá al receptor consultar el estado de los giros a su nombre sin depender del emisor*— es un
ítem P0, y `RF-90` le deja **declarar una diferencia** por llamada o mensaje de texto. Una superficie
que el backlog ordena no se puede cerrar desde acá. Lo que sí decide este paso es **cómo se abre sin
regalar nada**, y son tres restricciones:

1. **Entra por su canal, no por una aplicación.** Elena sigue sin cuenta, sin datos y sin teléfono
   inteligente supuesto: la entrada es la llamada o el mensaje de texto que `RF-90` nombra, servida
   por el mismo adaptador que ya le habla por `RF-25` y `RF-41`.
2. **Con identidad comprobada antes de admitirle nada.** `RF-180` obliga a identificarla como **el
   receptor designado** antes de admitir su declaración, y `POST /receptores/verificacion` es esa
   compuerta: número de origen contra `telefono_token` del receptor designado, más un verificador de
   un solo uso hacia ese mismo número. **No es el código de seguimiento** —`RF-94` prohíbe
   reemitirlo y `RNF-15` que quede legible— **ni consume el cupo de `RF-82`**, que cuenta intentos
   para cobrar y no para consultar.
3. **Devuelve estrictamente menos que la ruta del emisor.** `GET /giros?receptor={id}` sirve el
   hecho —hay un giro, de cuánto, disponible o no, en qué punto— y nada de lo que ningún título le
   concede: ni el código ni parte de él (`RNF-15`), ni la pregunta ni la respuesta del desafío
   (`RF-101`, `RNF-17`), ni el motivo de una retención (`RF-40`).

Lo que Elena sigue sin originar es el sobre sellado de `RF-114`, que **no es una ruta suya sino una
superficie de entrada del punto de atención**: escribe y no lee, no lleva sesión, no consulta nada y
devuelve un veredicto que tampoco es para ella.

---

## Las seis decisiones que este caso obligaba, resueltas

Seis. **Están cerradas.** Cada una lleva lo mismo: qué se eligió, contra qué alternativa, qué
requisito la obliga y **qué se pierde** — esta última parte no es cortesía, es la mitad que vuelve
auditable la decisión. Donde el backlog ya decidió el *qué*, aquí se elige solo el *cómo*.

### (a) Dónde vive la verdad del dinero

**Decisión.** **Libro de movimientos de partida doble, solo-adición, en el núcleo transaccional, con
el estado del giro como proyección escrita en la misma transacción y siempre reconstruible desde el
libro. Cuando el libro y la proyección difieren, manda el libro.**

**Las cuentas del libro**, que es lo que la decisión realmente fija: `Efectivo recibido en origen`,
`Obligación con el receptor` (`BR-01`: el dinero no es ingreso de SendIt, es deuda),
`Obligación retenida`, `Caja del agente por punto` (el efectivo que el agente puso y que `RF-24`
obliga a liquidarle), `Comisión`, `Diferencia de cambio` y `Devoluciones por retirar`.

**Todo hecho del giro es un asiento, incluidos los que no parecen contables.** La retención de
`RF-29` no mueve dinero pero **reclasifica** la obligación: `Obligación con el receptor` contra
`Obligación retenida`, mismo monto, suma cero. El vencimiento sin liberación (`RF-32`), la
devolución por cancelación (`RF-47`) y la prescripción (`RF-50`) hacen el camino inverso hacia
`Devoluciones por retirar`. Un giro sin asiento es un giro que no ocurrió.

**Contra qué alternativa.** Contra un campo `estado` o `saldo` que se actualiza en el sitio. Se lee
más rápido y no tiene historia: el valor anterior desapareció cuando se sobrescribió.

**Qué requisito la obliga.** `RNF-07` —«lo que sale de una cuenta entra en otra; ningún movimiento
deja el total distinto»— no es una propiedad que un campo mutable pueda tener: es una restricción
sobre un conjunto de filas escritas juntas. Y `RNF-03` prohíbe modificar o borrar el registro de un
acto, mientras `RF-18` obliga a conservarlo por el plazo más largo de los dos reguladores (`BR-15`).
Nadie audita un campo que se sobrescribió.

**Qué se pierde.**

- Cada hecho nuevo del dominio obliga a inventarle un asiento y una contrapartida con nombre, aunque
  no mueva un centavo. Agregar un estado al giro deja de ser una migración de una columna.
- El estado ya no se lee con un `SELECT` barato: se lee de una proyección que hay que mantener,
  reconstruir y probar. Y hay dos lugares donde puede estar el error en vez de uno.
- **No se puede corregir un error de tipeo, solo compensarlo.** La traza conserva los errores para
  siempre, con nombre y autor (`RF-54`), y eso incluye los de Kevin.
- El volumen crece: cada giro deja varios asientos donde un campo dejaba una fila. Cuando
  [`E`](../E-estimar/README.md) calcule, el multiplicador del almacenamiento no es uno.

**Se propaga a** `A` (entidades y su mutabilidad) y a `L` (`Ledger Service`, el único escritor).

### (b) Idempotencia

**Decisión.** **Dos mecanismos, no uno, porque protegen cosas distintas.**

1. **Unicidad natural en el libro**, que es lo que garantiza *a lo sumo una vez para siempre*: un
   índice único sobre `(giro, acto)` para los actos que mueven dinero —entrega al receptor, retiro
   de devolución, recepción del efectivo—. Un segundo pago del mismo giro no falla por política:
   **no entra en la base**, venga del punto que venga y llegue cuando llegue.
2. **Clave de intento generada por el cliente**, enviada como `Idempotency-Key` y persistida en la
   misma transacción que el primer asiento y **antes de mover un centavo**, que es lo que garantiza
   *la misma respuesta al reintento*. El reintento devuelve el resultado original —no un error,
   porque un error hace que Rosa lo intente por tercera vez—; con la misma clave y distinto
   contenido devuelve `409` y no ejecuta nada.

**Ventana de vida: la del giro pagable, no un plazo corto.** La clave vive lo que vive el giro
(hasta la prescripción) y la restricción de unicidad **no caduca nunca**.

**Alcance.** Todo acto que mueve dinero o cambia irreversiblemente el estado: recepción del efectivo,
pago, cancelación y devolución (`RF-46`, `RF-47`), retiro de la devolución, corrección (`RF-56`),
liberación de una retención —que `RF-33` y `RF-87` obligan a registrar con motivo— y **rehacer el
giro cancelado** (`RF-117`), que crea un giro nuevo y por tanto se puede duplicar como cualquier
otro. **Queda fuera, y es deliberado:** el intento de desafío, porque cada envío *es* un intento y
`RF-82` los cuenta.

**Y queda fuera por una razón distinta, que importa más:** el efectivo recibido sin giro creado de
`RF-118` **no es una clave de intento**. Una clave de idempotencia caduca sola, y lo que caducaría
acá es el rastro del dinero que Rosa ya entregó — `BR-01` lo vuelve deuda de SendIt desde que entra
al cajón, con giro o sin él. Ese estado es una **obligación en custodia con asiento propio**, y se
cierra completando el giro o devolviendo el efectivo — **nunca dejando de existir**. `RF-138` le
agregó un tercer camino que no contradice esto sino que lo completa: a las
`[ASSUMPTION: 72 horas]` sin que nadie la retome, el vencimiento **abre la devolución al emisor con
su asiento** en vez de purgar la fila. La diferencia con un TTL es entera: un TTL borra la deuda; el
vencimiento de `RF-138` la salda. La clave de intento
sigue sirviendo para que el reintento de Kevin sea la misma operación, que es otra cosa — y por eso
el `Idempotencia Service` de `L` no puede cargar con `RF-42` ni con `RF-118`.

**Contra qué alternativa.** Contra la clave generada por el servidor —un corte antes de que la
respuesta llegue convierte el reintento en operación nueva, y Rosa entrega un giro y le cobran dos,
que es justo lo que `RF-43` prohíbe—, y contra una ventana de vida corta de 24 horas, que vuelve a
habilitar el doble pago al día siguiente y contradice el «en ningún momento» de `RNF-05`.

**Qué requisito la obliga.** `RF-43` (reintento de una creación interrumpida) y `RF-44` (reintento de
un pago interrumpido) enuncian el efecto; `RNF-05` lo vuelve invariante «en ningún punto y en ningún
momento», y ese *ningún punto* es lo que obliga al mecanismo 1: la clave del cliente vive en el punto
y dos puntos desconectados no se ven entre sí, pero el índice único del libro los ve a los dos. Que
el punto desconectado no pueda comprobar nada por su cuenta es lo que resuelve **(c)**.

**Qué se pierde.**

- Cada acto que mueve dinero necesita su fila de unicidad y su nombre en un catálogo cerrado: la
  lista de actos deja de ser extensible sin migración.
- La tabla de claves de intento **nunca se purga** mientras el giro sea pagable, y crece con el
  negocio sin aportar una sola lectura de valor.
- El punto tiene que escribir la clave en su disco local antes de mandar la petición. Si se le corta
  la corriente antes de esa escritura, el reintento del operario **sí** es un intento nuevo, y lo
  único que queda entre eso y un doble pago es el índice único del libro — la red de abajo, no la de
  arriba.
- Un `409` por mismo intento con distinto contenido es correcto y es antipático: Kevin corrigió un
  dígito, el sistema le dice que no, y él no sabe cuál de los dos cuerpos es el que quedó.

**Se propaga a** `A`, `L` (`Idempotencia Service`) y a toda la tabla de endpoints.

### (c) La frontera entre el centro y el punto de atención

**Lo que el backlog ya cerró — reconstruido, porque el ítem sobre el que esto se apoyaba está
retirado.** Este documento citaba `RF-45` entre comillas con una condición que el título no tenía
—*«pague un giro que el centro ya retuvo, canceló o dio por pagado en otro punto»*— y construía la
decisión sobre esa lectura. `RF-45` está **retirado**, y lo está por duplicado encubierto: decía como
comportamiento lo que tres invariantes ya dicen. Son esos tres, citados como están, los que sostienen
la decisión, y sostienen **más** que la frase inventada:

| Invariante | Qué prohíbe, textualmente | Qué le prohíbe al punto sin conexión |
|---|---|---|
| `RNF-05` | «Ningún giro registra dos entregas al receptor, **en ningún punto y en ningún momento**» | Pagar un giro que ya se pagó en otro punto. El *ningún punto* es literal y nombra el caso |
| `RNF-06` | «Dos lugares del sistema nunca afirman a la vez que un giro está retenido y disponible para cobro» | Afirmar «disponible» mientras el centro afirma «retenido». Un punto que decide solo **es** el segundo lugar que afirma |
| `RNF-13` | «Ningún giro figura simultáneamente devuelto al emisor y entregado al receptor, en ningún punto y en ningún momento» | Pagar un giro que el centro ya canceló o devolvió |

Los tres son P0 y ninguno admite ventana. Y `RF-100` cierra la puerta que quedaba con un
comportamiento y no con un invariante: *«el sistema impedirá que un punto sin conexión
autorice un pago que no puede comprobar contra el centro»*. Entre los cuatro eliminan
pagar-y-arreglar, pagar-contra-autorización-pre-descargada y
pagar-lo-que-no-está-en-la-lista-de-prohibidos: **las tres son la misma cosa, un punto decidiendo sin
poder comprobar.** No son opciones caras; son opciones prohibidas. Lo que queda por decidir es
**cómo comprueba** y **qué pasa en la reconexión**.

**Decisión: arrendamiento exclusivo del giro, emitido solo en línea.** El centro no baja
«autorizaciones» abiertas. Baja un **arrendamiento** de un giro concreto a un punto concreto, por una
ventana corta —`[ASSUMPTION: 120 segundos, renovable únicamente en línea]`—, y mientras ese
arrendamiento vive **el centro se prohíbe a sí mismo disponer del giro**: no lo retiene, no lo
cancela, no lo arrienda en otro punto. Al vencer sin confirmación, el arrendamiento caduca y el
centro recupera la potestad.

**Por qué esto lleva la ventana de `RNF-06` a cero y no a «poco».** El invariante dice que dos
lugares del sistema nunca afirman a la vez que un giro está retenido y disponible para cobro. El
mecanismo no sincroniza dos afirmaciones más rápido: **hace que solo uno de los dos tenga derecho a
afirmar en cada instante.** La retención de `RF-29` que nace mientras el punto está caído ya no
compite con nada — si hay arrendamiento vivo, la retención espera a que venza (segundos), y si no lo
hay, se aplica y el punto no podrá arrendar nunca ese giro.

| Opción sobre el giro sin condición en contra | Qué supone | Por qué no se eligió |
|---|---|---|
| El punto paga contra la autorización que el centro ya le bajó, con caducidad y tope de monto | Que la caducidad y el tope acoten el daño | **Prohibida por `RF-100`**: el punto autoriza lo que no puede comprobar. Y `RNF-05`, `RNF-06` y `RNF-13` no admiten ventana —dicen *en ningún momento*—, así que no hay caducidad lo bastante corta que la vuelva legal |
| El centro le empuja al punto las prohibiciones antes de la caída y el punto paga lo demás | Que la lista de prohibiciones viaje antes que la caída | Se rompe con la retención que nace mientras el punto está caído: `RF-29` no espera a que vuelva. No elimina la ventana, la desplaza al último empujón hecho |
| **Arrendamiento exclusivo, obtenido solo en línea** | Que la exclusión, y no la sincronización, sea el mecanismo del invariante | **Elegida.** Es la única que hace `RNF-05`, `RNF-06` y `RNF-13` demostrables en vez de probables, y la única compatible con `RF-100` |

**Qué corre en el mostrador cuando el centro no está.** No un pago. Sí: consultar lo que el punto ya
tiene, declarar la caja de apertura y cierre (`RF-76`), registrar la declaración de diferencia del
receptor (`RF-90`), y **encolar en el diario local, firmado y solo-adición**. El operario ve un
estado único que puede leer y retomar —el giro a medias de `RF-42` y el efectivo ya recibido sin
giro creado de `RF-118`, los dos en `GET /puntos/{id}/pendientes`— y **la acción ofrecible que el giro lleva
asociada** (`RF-39`) y que `RF-130` obliga a **mostrarle sobre el giro que tiene delante**, que en
este caso es una sola y hay que tenerla escrita de antemano: volver cuando haya línea, o ir a otro
punto si lo hay. `RF-39` no pide que la pantalla improvise: pide que **todo** giro rechazado,
retenido o no pagable **tenga asociada al menos una acción ofrecible** antes de que Kevin la
necesite; `RF-130` es lo que después la pone delante de él. Son dos ítems, y por eso son una
cobertura comprobable —no hay estado de esos tres sin acción asociada— y una lectura del mostrador,
no un mensaje de error redactado con cuidado.

**La ventana de reconexión, que es lo que faltaba decidir.** Al volver la línea, el punto sube su
diario entero y el centro reconcilia **sin preguntarle nada al operario**, que es lo que `RNF-08`
exige. El caso duro es el pago que se ejecutó y no se confirmó: el arrendamiento venció en el centro
y el efectivo puede haber salido del cajón. El centro **no** devuelve ese giro a «disponible».

**Ese estado tiene ahora los dos ítems que le faltaban, y por eso deja de ser una invención de este
documento.** `RF-144` lo crea: *«el sistema dejará en un estado único el pago cuya confirmación no
llegó del punto al centro»*, que es el mismo *estado único* que `RF-42` y `RF-118` piden para lo
interrumpido, aplicado al tercer caso que faltaba. Y `RF-146` lo termina: *«el sistema resolverá
contra el registro del centro el pago cuya confirmación no llegó, sin intervención del operario»*.

**El estado, con su terminador.** El pago pasa a **`en duda`** —no arrendable en ningún punto, ni
pagable ni devolvible— y **no se queda ahí**: el `Sync Service` lo resuelve contra el **registro del
centro**, que son dos fuentes y ninguna es una persona: el **libro** —donde el `UNIQUE(giro, acto)`
de **(b)** dice si el asiento de entrega llegó a existir— y el **diario local firmado** que el punto
sube al reconectar, que es un hecho del punto y no una declaración del operario. De ahí salen las dos
salidas y no hay una tercera: **`resuelta como pagada`**, y el giro cierra por `RF-64` con su asiento;
o **`resuelta como no pagada`**, y el giro vuelve a ser arrendable. `RF-146` prohíbe expresamente la
tercera salida que un diseño perezoso elegiría —preguntarle a Kevin qué pasó—, y `RNF-08` ya lo
exigía del lado de la recuperación. El cierre de caja de `RF-76` **no resuelve** el estado: cuadra el
efectivo y, si aparece diferencia, `RF-141` se la informa al agente. Son dos cosas distintas y
confundirlas era darle al operario la última palabra por la puerta de atrás.

**Qué pasa si el punto nunca vuelve.** El estado no puede quedar abierto para siempre, y no queda:
sin diario que suba, el registro del centro es el libro, y el libro no tiene el asiento de entrega —
así que el pago se resuelve como **no pagada** y el giro vuelve a ser arrendable, con la diferencia
de efectivo que eso produzca viajando por el camino de `RF-141` y `RF-143` hacia la liquidación del
agente. La resolución nunca depende de que alguien conteste.

**El caso de Huanta, que hoy es lo que el backlog prohíbe.** Se ordenó detener un giro cuando la
autorización ya había bajado al punto, que llevaba desde la mañana sin conexión. El centro decía
«retenido»; el mostrador decía «disponible para cobro»; Elena cobró. Con arrendamiento eso es
inalcanzable: o el punto tenía arrendamiento vivo y entonces la orden de retener **esperó** y el
pago fue legítimo, o no lo tenía y no había nada que pagar. Lo que el caso sigue aportando es el
costo, y está escrito abajo sin adornos.

**Qué se pierde.**

- **Una caída de línea cierra el mostrador para pagos, sin excepción.** Elena viajó cuarenta minutos
  en combi, hizo la cola y vuelve con las manos vacías, después de que `RF-41` y `RF-75` le
  prometieran antes de viajar que ese punto podía pagarle. La salida de `RF-91` tampoco corre: para
  trasladar el cobro a otro punto hace falta línea, que es justo lo que falta.
- **El estado *pago en duda* de `RF-144` congela un giro que ni se paga ni se devuelve** hasta que el
  registro del centro lo resuelva (`RF-146`). Termina siempre y sin preguntarle a nadie, pero puede
  tardar lo que tarde el punto en reconectar: es correcto y es horrible para quien está delante del
  mostrador, y no hay mensaje que lo mejore.
- Toda la disponibilidad de `RNF-11` —99,9 % mensual, medida sobre crear y pagar— queda apoyada en
  el enlace del mostrador, que es lo que menos controla SendIt. Esto obliga a
  [`E` (escalar)](../E-escalar/README.md) a dimensionar un segundo camino de conectividad o a
  aceptar por escrito la indisponibilidad.
- El arrendamiento agrega una llamada en línea al camino del pago y consume presupuesto de los tres
  minutos de `RNF-09`.

**Se propaga a** `A`, `L` (`Sync Service`, `Punto de Atención Service`) y `E` (escalar).

### (d) Cuándo se fija el tipo de cambio

**Lo que el backlog ya cerró.** El *cuándo* no se vuelve a decidir: `RF-05` obliga a informar el
monto exacto en moneda destino **antes de que el emisor entregue el efectivo**, `RF-06` lo conserva
«sin recalcularlo durante toda la vida del giro» y `RF-07` produce y fecha la cotización (`BR-07`).
La tasa se fija **al crear el giro**. Aquí se elige el mecanismo.

**Decisión.** **Cotización con vencimiento corto —`[ASSUMPTION: 15 minutos]` desde su emisión—,
copiada por valor dentro del giro al crearlo; la exposición la absorbe SendIt en una cuenta
`Diferencia de cambio` del libro de (a), financiada por un margen incorporado a la cotización **que
se le informa al emisor antes de que entregue el efectivo** (`RF-142`), y
cubierta por corredor al cierre del día, no giro a giro.**

- **Cuánto vive una cotización:** 15 minutos. Si vence mientras Rosa hace la cola, se recotiza y se
  le vuelve a informar **antes** del efectivo, que es lo que `RF-05` exige de todos modos.
- **Copiada por valor, no referenciada:** el giro guarda tasa y monto destino dentro de sí. Una clave
  foránea a una tabla de cotizaciones es una promesa que alguien puede editar.
- **Quién absorbe el movimiento:** SendIt, y queda escrito en una cuenta con nombre. Cero ajustes
  silenciosos: `RNF-16` prohíbe que la entrega difiera de la cifra que el emisor vio y `RF-59` obliga
  a reponer **toda diferencia comprobada** a quien le faltó.
- **El margen no es silencioso, y esta ronda lo cambió.** `RF-142` obliga a informarle al emisor
  **el margen que se aplica sobre la cotización, antes de que entregue el efectivo**, y `RF-136` a
  informarle la comisión con el mismo borde temporal. De modo que la cotización que `POST
  /cotizaciones` devuelve no lleva un solo número sino cuatro con nombre: **monto en moneda destino,
  tasa, margen y comisión**, y los cuatro se congelan con `RF-06`. Un margen «incorporado a la
  cotización» y no desglosado dejó de ser una opción de diseño: sería la misma mecánica del «cero
  comisión» que este documento critica dos párrafos más abajo.
- **Devoluciones:** `RF-88` obliga a devolver en la moneda que el emisor entregó y `RF-74` a devolver
  también la comisión cuando el giro no llegó a pagarse. La devolución se hace por el **nominal
  entregado**, sin reconvertir: el asiento cierra la obligación en moneda destino y la diferencia va
  a su cuenta. Vale igual para la retención vencida (`RF-32`), la cancelación (`RF-47`) y la
  prescripción (`RF-50`).

**Contra qué alternativa.** Contra fijar al pagar —prohibido por `RF-06` y `BR-07`, y es exactamente
lo que Elena ya vivió: treinta soles menos «por el cambio», explicados por un mostrador que no
produjo esa diferencia—; y contra una cotización sin vencimiento, que expone a SendIt sin límite y
deja que la ventanilla lenta se vuelva una opción gratuita sobre el mercado.

**Qué se pierde.**

- La cotización vencida obliga a **recotizar con Rosa delante**, y el número que le prometió a su
  madre por teléfono puede cambiar entre que llegó al local y llegó a la ventanilla. Es el precio
  concreto que paga la señal de éxito de [Rosa](../../personas/Rosa.MD).
- SendIt carga la exposición desde la creación hasta el cobro, que por `RF-89` y la prescripción de
  doce meses puede ser **muy** largo. La cubre con margen — y **el margen lo paga Rosa, ahora
  viéndolo**: `RF-142` obliga a decírselo antes del efectivo, así que lo que se pierde ya no es su
  ignorancia sino su comparación. Con el número delante, Rosa puede irse a la competencia en la
  ventanilla misma, y la conversión cae en el peor momento posible del embudo. **Se elige eso**: era
  exactamente la mecánica del «cero comisión» que la enfureció, y sostenerla habría sido reproducir
  el agravio del que esta persona nació. La decisión es honesta en el libro **y en el mostrador**, y
  se paga en el mostrador.
- La cuenta `Diferencia de cambio` puede quedar negativa sin que nadie haya hecho nada mal, y hay que
  poder explicarlo sin que parezca un descuadre.
- Cubrir por corredor y no giro a giro es más barato y deja una exposición residual que ninguna
  operación individual explica.

**Se propaga a** `A` (entidad de cotización y cuenta de diferencia) y `L` (`Quote Service`,
`Vencimiento Job`).

### (e) Dónde corre el tamizaje respecto del momento en que el dinero se compromete

**Lo que el backlog ya cerró.** `RF-26` fija el momento: el tamizaje corre **antes de aceptar el
efectivo**, y la tensión T1 lo decide a favor del control con precio acotado. `RF-119` fija el
**alcance**: el mismo contraste, antes del mismo instante, sobre el **receptor designado** — dos
personas y dos veredictos, porque un emisor limpio no absuelve al destinatario del dinero. `RF-27` agrega el
segundo contraste, al autorizar el pago y contra las listas **vigentes en ese momento**. Aquí se
elige el mecanismo, y sobre todo qué pasa cuando el tercero no contesta.

**Decisión.** **Copia local versionada de las listas, replicada del proveedor, contra la que corren
los dos tamizajes de forma sincrónica. El camino del dinero nunca llama al proveedor en vivo.**

- **Frescura vigilada, y falla cerrada:** el adaptador replica y sella cada versión. Si la copia
  supera `[ASSUMPTION: 24 horas]` sin actualizarse, el sistema **deja de crear giros** en vez de
  crearlos sin tamizar. `BR-06` no admite mover dinero sin contrastar.
- **Los cinco momentos, cada uno con su control:** identificar y tamizar **las dos puntas** antes del
  efectivo (`RF-01`, `RF-26` para el emisor y `RF-119` para el receptor designado); aceptar el
  efectivo (`RF-02`, `RF-79`); dar el giro por fondeado con efectivo
  en el corredor (`RF-20`, `RF-36`); **arrendar el giro al punto contrastando contra la versión
  vigente** (`RF-27`); entregar el efectivo contra código, documento y —si el documento no está
  vigente— desafío (`RF-34`, `RF-85`, `RF-86`, `RF-69`, `RF-64`).
- **El punto de no retorno tiene nombre: la emisión del arrendamiento de (c).** A partir de ahí el
  efectivo puede salir del cajón sin que el centro se entere hasta la confirmación. Todo control que
  quiera *detener* en vez de *deshacer* tiene que correr antes de esa llamada.
- **Un tamizaje posterior al punto de no retorno no detiene: alcanza.** `RF-97` re-tamiza los giros
  no pagados cuando cambia una lista y avisa por su canal a quien deja de poder cobrar; sobre un giro
  con arrendamiento vivo, espera a que venza (mecanismo de (c)).
- **Qué ve Rosa mientras su giro está retenido, sin que el motivo se deduzca.** `RF-66` le muestra
  que está retenido y hasta qué fecha; `RF-67` le avisa cuando pasa a estarlo **dentro del plazo que
  `RF-115` le prometió antes de que entregara el efectivo**, y **nunca más de una hora después de la
  retención** (`RF-133`) —un plazo comprometido y no un mejor
  esfuerzo: se copia al giro al crearlo y vence contra fecha absoluta, como todos los demás—; a Kevin, `RF-40` le
  omite el motivo y `RF-39` le muestra **la acción ofrecible que ese giro retenido lleva asociada**
  —no el motivo: qué puede hacer hoy quien está delante—. Las dos cosas conviven porque son dos
  campos con lectores distintos, y la acción se elige por **clase de estado**, nunca por causa: si la
  acción variara con el motivo, revelaría lo que `RF-40` oculta. El mecanismo que impide la deducción es que
  **el mensaje y el plazo son los mismos para toda retención, cualquiera sea su causa**: se informa
  siempre el plazo **máximo** del regulador más estricto (`RF-31`), nunca el esperado. Esto importa
  porque `RF-78` resuelve la homonimia más rápido que la coincidencia exacta: si a Rosa se le
  informara el plazo esperado, **la duración filtraría la causa**. La resolución anticipada se le
  comunica como resolución, no como reducción de plazo.

**Contra qué alternativa.** Contra llamar al proveedor en línea dentro del camino del pago: un
tercero lento consume los tres minutos de `RNF-09` y su caída cierra la red entera con dinero ya
adentro. Y contra tamizar después de aceptar el efectivo, que `RF-26` prohíbe y que convierte la
herramienta de Kevin de *detener* en *revertir* — que es precisamente el movimiento que el lavado
busca provocar (`BR-03`).

**Qué se pierde.**

- Hay que replicar, versionar y almacenar listas ajenas, y aceptar que la copia **va atrasada**.
  Existe una ventana real en la que un giro se aprueba contra una lista vieja; `RF-97` la cierra
  después, pero con el dinero ya recibido.
- **Fallar cerrado es indisponibilidad autoinfligida:** una caída del proveedor de más de 24 horas
  detiene la creación de giros en toda la red y consume el presupuesto de `RNF-11`. Es la decisión
  correcta y hay que estar dispuesto a sostenerla el día que pase.
- Informar siempre el plazo máximo significa **decirle a Rosa un número peor que el probable**. La
  mayoría de las retenciones son homónimos que se resuelven rápido (`RF-78`), y ella va a esperar
  angustiada por un plazo que casi nunca se cumple. Se elige eso antes que filtrar la causa.

**Se propaga a** `A`, `L` (`Screening Service`, `Screening Job`) y `E` (estimar: la carga del camino
del pago y el almacenamiento de listas replicadas).

### (f) El secreto que no pasa por el operario: dónde vive la respuesta, quién la compara, y por dónde entra y sale

**Decisión.** **La respuesta no se guarda ni se transmite en claro en ningún punto del sistema. Vive
como derivado irreversible en una base propia del servicio de desafío, y la comparación corre solo en
el centro, dentro de ese servicio, que es el único componente que llega a ver el valor. Y el camino
por el que el secreto entra y sale del mostrador no atraviesa al operario: hay un dispositivo
orientado al cliente, con su propia clave contra el centro, que el software del punto transporta y
no abre.**

- **Con qué transformación entra.** Normalización decidida por el sistema —mayúsculas, acentos,
  espacios—, igual que `RF-84` decide qué diferencia de escritura cuenta; después, función de
  derivación **lenta** con sal por giro, y sobre el resultado un sellado con una clave de servicio
  que vive fuera de la base. Quien administre `BD desafíos` tiene el derivado y no tiene la clave:
  no puede probar candidatos ni siquiera con la base entera en la mano. Eso es lo que vuelve
  declarable `RNF-17` frente a **los dos lectores que su invariante nombra desde la ronda 12** —quien
  administra la infraestructura y quien atiende el mostrador—, sin que haga falta un ítem aparte
  para el segundo.
- **Cómo llega el valor sin que nadie lo vea.** Rosa lo teclea en el dispositivo de captura de la
  ventanilla, que lo cifra contra el servicio de desafío. El `Punto de Atención Service` transporta
  el sobre y **no tiene la clave para abrirlo**: `RNF-17` lo mantiene ilegible para quien atiende el
  mostrador y `RF-101` prohíbe transmitirlo a nadie, ni siquiera a quien registró la pregunta.
- **Dónde corre la comparación: solo en el centro.** Por la línea sube el sobre con lo que dijo
  Elena y baja **un veredicto booleano y el número de intentos restantes**. Nunca el valor, nunca el
  derivado, nunca la sal. Consecuencia directa y aceptada: **sin conexión no hay desafío**, y por
  tanto `RF-69` no funciona en un punto caído — es la frontera de (c) otra vez, ahora sobre un
  secreto en vez de sobre un estado.
- **Intentos.** `[ASSUMPTION: tres por giro]`, contados en `BD desafíos` y no en el giro, porque el
  contador es a su vez un dato sobre el secreto. Al operario se le muestra solo «quedan N», que es
  todo lo que `RF-57` le permite ver. Agotados, `RF-103` devuelve el giro al emisor.
- **Qué hace la caducidad de `RF-83`.** No borra filas: **destruye la sal y el sellado de ese giro**.
  El derivado queda inservible y la traza de auditoría sigue intacta —hubo intentos, con autor,
  momento y veredicto (`RF-54`, `RNF-04`)—, sin que `RNF-03` tenga que ceder. Es borrado
  criptográfico, no `DELETE`.

**Contra qué alternativa.** Contra cifrado reversible con clave del sistema —quien administra la
infraestructura la descifra, y `RNF-17` lo prohíbe explícitamente—; y contra bajar el derivado al
mostrador para comparar ahí, que resolvería el caso sin línea y a cambio entrega el material para un
ataque de diccionario **dentro de un local que no es de SendIt**, que es exactamente el vector que
[Kevin](../../personas/Operario.MD) modela.

**El mismo mecanismo, del otro lado del mostrador: la respuesta que entra (`RF-114`).** Lo que vale
para Rosa al registrar vale para Elena al cobrar, y `RF-114` lo exige con todas las letras: la
respuesta la introduce **el propio receptor**, y quien atiende no puede leerla **ni digitarla**. Esas
dos palabras cierran la salida barata —«que Elena se la dicte a Kevin y él la teclee»—, que es
exactamente lo que hoy pasa en cualquier ventanilla y lo que convertiría a `RNF-17` en una regla de
pantalla. **Desde la ronda 12 el código del giro entra por el mismo camino** (`RF-147`): el control
que autoriza todos los pagos del sistema dejó de tener una única forma implementable prohibida. El mecanismo es el mismo dispositivo: Elena teclea en la superficie orientada al cliente,
que sella el sobre contra el `Desafío Service` con su propia clave; el `Punto de Atención Service`
lo transporta y no lo abre; el centro devuelve veredicto e intentos restantes. **El operario nunca
tiene el valor en la mano, ni siquiera durante el segundo en que lo escribiría.** Y `RF-122` cuelga
de ese veredicto y de ningún otro: el pago con documento vencido lo habilita **el centro** al ver la
respuesta correcta, no el mostrador al declararla.

**Y la salida, que es el código (`RF-11`, `RF-113`, `RF-125`).** El código lo genera el sistema y
`RF-11` lo hace llegar **únicamente al emisor, por llamada o mensaje de texto al teléfono que él
registró** — pero entregárselo mostrándolo en la pantalla del mostrador es
entregárselo también a Kevin, que es el vector que [su persona](../../personas/Operario.MD) modela.
`RF-113` cierra esa puerta —*impedirá que quien atiende el mostrador lea o transcriba el código*— y
`RF-125` evita que el mostrador quede mudo. El mecanismo tiene tres mitades:

- **La respuesta de `POST /giros` no lo lleva.** El mostrador recibe `giro_id` y nada más del
  código; el código en claro existe durante un único instante, dentro del núcleo, y sale por el
  **adaptador de canal** hacia **el teléfono que el emisor registró** —el mismo por el que viaja todo
  lo demás (T5)—. Persistido queda solo el derivado.
- **Y sale por ahí y por ningún otro lado.** Este documento traía una segunda salida —imprimir el
  código sellado desde el dispositivo orientado al cliente cuando el emisor no tuviera señal en el
  local— y **se retira**: `RF-11` nombra el canal y el teléfono, y ninguna otra ruta de salida tiene
  título que la autorice. Un mecanismo elegido acá no puede agregarle al sistema una capacidad que
  el backlog no pidió. **Qué se pierde:** el emisor sin señal en el local se va sin código, y la
  única salida sigue siendo cancelar y rehacer (`RF-46`, `RF-117`) — el mismo precio que ya se paga
  cuando el mensaje no llega, ahora también cuando no hay cobertura.
- **El operario recibe la confirmación de que salió, y solo eso.** `RF-125` le devuelve el acuse
  —*el código salió hacia el emisor*— **sin mostrárselo**. Sin ese ítem, la única forma de que Kevin
  supiera si tenía que repetir la operación habría sido enseñarle el código o dejarlo adivinando;
  con él, la respuesta de `POST /giros` lleva `giro_id` + acuse de despacho y ni un carácter del
  secreto.
- **No hay segunda oportunidad de leerlo, para nadie.** `RNF-15` mantiene el código ilegible para
  quien atiende el mostrador y `RF-94` prohíbe reemitirlo aun al emisor que lo perdió. Las dos se
  cumplen por ausencia de ruta y por ausencia de valor persistido, no por permisos: **no existe el
  `GET`, y aunque existiera no habría qué devolver.** La salida al código perdido no es leerlo otra
  vez sino cancelar y rehacer (`RF-46`, `RF-117`), que es donde la tensión T7 quedó decidida.

**Y el lado que el código de seguimiento no tiene.** El código lo genera el sistema; la respuesta la
elige Rosa, delante de Kevin, y se la transmite a Elena por un canal que SendIt no controla. Es un
**secreto compartido entre dos personas** que el sistema solo arbitra: no puede regenerarlo, no puede
recordárselo a nadie, no puede aceptar que se adivine.

**Qué se pierde.**

- **Nadie puede recuperar la respuesta.** Ni SendIt para ayudar a Elena, ni Rosa si se olvidó de qué
  escribió. No hay procedimiento de excepción, porque un procedimiento de excepción es un agujero
  con formulario.
- **A los tres intentos el giro se devuelve** aunque quien estaba delante fuera la receptora
  legítima. Elena vuelve a Huanta sin dinero y con el giro cancelado, y Rosa tiene que empezar de
  nuevo.
- Un **error de tipeo de Kevin gasta un intento real**, y él no puede ver qué tecleó mal porque el
  campo no se muestra.
- **El desafío no funciona sin línea**, que es justo el escenario del documento vencido en una plaza
  de Ayacucho. La salida de `RF-69` es la más frágil del sistema precisamente donde más falta hace.
- La normalización que decide el sistema puede rechazar una respuesta correcta escrita distinto, o
  aceptar una demasiado parecida, y **esa decisión ya no se puede auditar contra el valor** porque el
  valor no existe en ninguna parte.
- **El dispositivo orientado al cliente es hardware en un local que no es de SendIt**, y su clave
  vive ahí. Se puede robar, sustituir o intervenir, y la única defensa es que lo que sella no vale
  sin el centro. Cada mostrador pasa a tener dos superficies en vez de una, y `E` (escalar) tiene
  que contarlas: `RF-113` y `RF-114` no se cumplen con software solo.
- **Si el dispositivo se avería, no hay giro y no hay desafío.** No queda el atajo de que Kevin
  teclee —`RF-114` lo prohíbe—, así que la falla de un periférico cierra la operación igual que la
  caída de línea de **(c)**. Es coherente y es caro, y quien está delante del mostrador no distingue
  una cosa de la otra.
- **El código que sale por el canal depende del canal.** Si el mensaje no llega, Rosa se va sin
  código y `RF-94` impide reemitirlo. Desde la ronda 12 ese giro **no queda mudo**: `RF-149` lo deja
  no pagable, `RF-151` le asocia una acción ofrecible y `RF-130` se la muestra al operario, y la
  salida es cancelar y rehacer (`RF-46`, `RF-117`). Se elige eso antes que mostrarle el código a
  Kevin.

**Se propaga a** `A` (la entidad que lo guarda, su trato en la tabla de datos personales y el relevo
de vigencia que `RF-122` obliga a registrar), a `L` (`Desafío Service` y `BD desafíos`, el único
componente que toca el valor, más el dispositivo orientado al cliente como frontera del
`Punto de Atención Service`) y a `E` (escalar: dos superficies por mostrador, no una).

---

## Resumen de propagación

| Decisión | Qué quedó decidido | Se propaga a | Qué queda inválido si se reabre |
|---|---|---|---|
| (a) Verdad del dinero | Libro de partida doble solo-adición; estado como proyección; manda el libro | `A`, `L` | El modelo de datos completo del giro y del movimiento; el componente que escribe el libro |
| (b) Idempotencia | Unicidad natural en el libro + clave del cliente persistida antes del primer asiento; vive lo que el giro; el efectivo en custodia de `RF-118` **queda fuera y es entidad con asiento**, que `RF-138` cierra devolviendo y no caducando | `A`, `L`, API | La tabla de endpoints; la entidad que persiste la clave; la entidad de custodia y su vencimiento |
| (c) Frontera centro ↔ punto de atención | Arrendamiento exclusivo por giro, solo en línea; sin conexión no se paga; *pago en duda* (`RF-144`) al reconectar, **resuelto contra el registro del centro y sin intervención del operario** (`RF-146`) | `A`, `L`, `E` (escalar) | El estado del giro y el que el punto sostiene sin conexión; el componente que sincroniza al reconectar; el presupuesto de disponibilidad de `RNF-11` |
| (d) Tipo de cambio | Cotización de 15 min copiada por valor; SendIt absorbe en cuenta `Diferencia de cambio`; cobertura por corredor | `A`, `L` | La entidad de cotización y la cuenta de diferencia de cambio |
| (e) Momento del tamizaje | Copia local versionada, falla cerrada a las 24 h; punto de no retorno = emisión del arrendamiento; plazo máximo informado siempre | `A`, `L`, `E` (estimar) | La carga del camino del pago; el orden de los componentes en el diagrama |
| (f) El secreto que no pasa por el operario | Derivado irreversible en base propia con clave fuera de la base; comparación solo en el centro; caducidad por borrado criptográfico; **el secreto entra por un dispositivo orientado al cliente que el punto transporta y no abre** (`RF-114`, `RF-147`) y **sale por un canal que no toca el mostrador** — llamada o mensaje de texto al teléfono que el emisor registró (`RF-11`, `RF-113`) | `A`, `L`, `E` (escalar) | La entidad que la guarda y su fila en la tabla de datos personales; el componente que la compara; el flujo de pago con documento no vigente (`RF-69`, `RF-86`, `RF-122`); la superficie física del mostrador y su costo |

---

## Supuestos que este paso introduce

Cinco, y son suyos: ninguno viene del backlog, y cada uno es un número que el enunciado no da.

| Marca | Dónde | Qué pasa si se retira |
|---|---|---|
| `[ASSUMPTION: el arrendamiento del giro dura 120 segundos, renovable solo en línea]` | (c) | El mecanismo sobrevive; lo que cambia es cuánto espera una retención y cuán frecuente es *pago en duda* |
| `[ASSUMPTION: la cotización vive 15 minutos]` | (d) | Sube o baja la exposición cambiaria de SendIt y la frecuencia con que se recotiza con Rosa delante |
| `[ASSUMPTION: la copia de listas falla cerrada a las 24 horas sin actualizar]` | (e) | Mueve el equilibrio entre `BR-06` y `RNF-11`: más plazo es más riesgo de tamizar contra lista vieja, menos plazo es más indisponibilidad |
| `[ASSUMPTION: tres intentos de desafío por giro]` | (f) | Cambia cuántos giros legítimos terminan devueltos por `RF-103` y cuánto margen tiene un ataque de adivinanza |
| `[ASSUMPTION: la oferta de punto alternativo vence 24 horas después de comunicada]` | Endpoints `punto-alternativo` y su vencimiento | `RF-116` obliga a informar el plazo pero el backlog no lo fija; retirarlo no cambia el mecanismo —fecha absoluta comunicada al emisor y barrida por el `Vencimiento Job`— sino cuánto espera el giro antes de que `RF-111` lo devuelva |

---

## Nota sobre las dos clases de iteración

La **iteración del diseño** —el mismo diagrama de componentes, dibujado otra vez y más abierto, que
es la que exige el enunciado ([ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md))— y la
**iteración del EVAL** no son lo mismo y [`ITERACIONES.md`](../ITERACIONES.md) las lleva en tablas
separadas. Este paso alimenta la primera: los servicios que aquí se nombran son las cajas que
[`L`](../L-listar-componentes/README.md) abre en su segunda pasada. Y lo afecta la segunda: un ítem
nuevo en el backlog puede reabrir cualquiera de las seis decisiones de arriba — y reabrirla obliga a
recorrer la columna «se propaga a» completa, no a corregir esta página sola.
