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
RF-12 prohíbe transmitir por canal propio. No hay padrón que contar ni login que medir. Dimensionar
sobre «usuarios registrados» mediría un sistema que no es este.

Las unidades de carga de SendIt son dos, y las dos se cuentan por día: **giros por día** —la
unidad de negocio, la que RF-01 a RF-14 crean y RF-34 a RF-41 pagan— y **operaciones de ventanilla
por día**,
que es la unidad de trabajo del operario y **no coincide** con la anterior: un giro consume al menos
dos ventanillas (la de creación y la de pago), y suma más cuando hay autorización de segundo rol
(RF-13), corrección (RF-56, RF-61) o devolución al emisor (RF-32, RF-47, RF-50).

| Entrada | Qué cuenta | Valor | De dónde sale | Marca |
|---|---|---|---|---|
| **Giros por día** | Giros creados, medidos sobre el conjunto de corredores de RNF-12 | — | — | — |
| **Operaciones de ventanilla por día** | Atenciones presenciales: crear, pagar, autorizar, corregir, devolver | — | — | — |
| Giros por día en pico | `giros por día × P` | — | — | — |
| RPS — requests por segundo | Derivada, no supuesta: sale del desglose por operación del cálculo 1 | — | — | — |
| Almacenamiento requerido | Salida del cálculo 2, no entrada | — | — | — |
| Factor de pico `P` | Ver abajo | — | — | — |

La reposición de «usuarios» por «giros» no es cosmética: un padrón crece de forma monótona y una
identidad inactiva sigue ocupando disco; un giro nace, se paga o se devuelve, y **se cierra**
(RF-64). Lo que persiste después del cierre es el registro, no el cliente — y eso es lo que cuenta
el cálculo 2.

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
| S-01 | Corredores atendidos | Fija las monedas, los dos reguladores que RF-15 aplica al mismo giro, la red de **puntos de atención afiliados** en la que hay que sostener efectivo (RF-20) y los husos horarios del pico. Sin él no hay volumen que estimar ni reglas que aplicar | **Cerrado por RNF-12 y RNF-14**: dos corredores al lanzamiento — Estados Unidos → Perú y España → Perú. El primero es el que modela [Rosa](../../personas/Rosa.MD) | Dos corredores | **Cerrado** |
| S-02 | Emisores distintos por mes | Dimensiona el almacenamiento de identidad de RF-01, que persiste por el plazo de RNF-03 aunque el emisor no vuelva nunca. No es un padrón: es el recuento de identificaciones practicadas en ventanilla | — | — | — |
| S-03 | Proporción de giros que exigen captura nueva de identidad | Un emisor recurrente se identifica otra vez (RF-01 no admite excepción) pero puede no producir un binario nuevo. La proporción decide cuánto del cálculo 2 crece con los giros y cuánto con las personas | El patrón de [Rosa](../../personas/Rosa.MD): la misma emisora, quincena tras quincena | — | — |
| S-04 | Giros por emisor al mes | Convierte emisores en giros por día, que es la unidad de carga del paso | El patrón de Rosa: quincenal, estable desde hace tres años | — | — |
| S-05 | Ticket promedio | No mueve el cómputo, pero decide cuántos giros cruzan el umbral de reporte transfronterizo (RF-17, RF-22) y cuántos el umbral reforzado que obliga a un segundo rol (RF-13) — y con ello cuántas operaciones de ventanilla extra aparecen | El rango de Rosa: USD 200–400 | — | — |
| S-06 | Consultas de estado por giro | **RF-52 y RF-53 la exigen como capacidad, y RF-66 le agrega el estado retenido con su fecha**: la consulta es carga requerida, no tráfico incidental. Es la operación de lectura dominante y la única que RNF-11 excluye explícitamente de su medida de disponibilidad | Lo que hoy obliga a Rosa a llamar por teléfono, ahora exigido por RF-52 | — | — |
| S-07 | **Factor de pico** | Ver abajo | — | — | — |
| S-08 | Proporción de giros que disparan una coincidencia de tamizaje | La tasa decide el volumen de evidencia, que es lo que domina el almacenamiento, y RF-28 obliga a guardar separadas la coincidencia exacta y la homonimia — la abrumadora mayoría son homónimos | `[ASSUMPTION: sin fuente; el enunciado no da ninguna cifra de tamizaje]` | — | — |
| S-09 | Años de retención regulatoria | Multiplica el almacenamiento diario por un factor que el ejemplo de YouTube no tiene | **Cerrado por RNF-03 y RF-18**: el plazo más largo de los dos reguladores del giro, con un piso de 5 años. Se calcula por giro y no por política global, así que el multiplicador del cálculo 2 no es único: es el máximo por corredor | ≥ 5 años | **Cerrado** |
| S-10 | Plazo máximo de una retención | Acota cuántos giros retenidos coexisten: la cola no es un acumulado sin fin, es un caudal con tiempo de residencia. RF-31 le pone plazo y RF-32 la termina devolviendo al emisor | **Cerrado**: lo que fije el regulador más estricto de los dos países, con techo de 72 h | ≤ 72 h | **Cerrado** |
| S-11 | Plazo de prescripción | Fija cuánto tiempo un giro creado sigue siendo pagable y por tanto vivo en el estado caliente antes de que RF-49 lo vuelva no pagable y RF-50 lo ponga a disposición del emisor. Separa el dato caliente del dato meramente retenido | **Cerrado**: 12 meses desde la creación del giro | 12 meses | **Cerrado** |

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

| Operación | Tipo | Requerimiento que la exige | Peso relativo | Volumen diario | Marca |
|---|---|---|---|---|---|
| Identificar al emisor contra documento | escritura + verificación externa | RF-01, RF-02 | — | — | — |
| Cotizar y fechar la cotización | **escritura durable** | RF-05, RF-06, RF-07 | — | — | — |
| Contar límites sobre la identidad del emisor | lectura agregada | RF-08, RF-09, RF-10 | — | — | — |
| Tamizar contra listas | lectura externa + escritura de evidencia | RF-26, RF-27, RF-28 | — | — | — |
| Crear el giro y emitir su código | escritura contable | RF-11, RF-13, RF-20 | — | — | — |
| Ejecutar el pago en destino | escritura contable + frontera | RF-34, RF-35, RF-36, RF-37 | — | — | — |
| Cerrar el giro y avisar al emisor | escritura + notificación | RF-64, RF-65 | — | — | — |
| Consultar estado | lectura | RF-52, RF-53, RF-66 | — | — | — |
| Avisar al receptor por llamada o mensaje | salida por canal externo | RF-25, RF-41, RF-60 | — | — | — |
| Devolver al emisor (retención vencida, cancelación, prescripción) | escritura contable | RF-32, RF-47, RF-50 | — | — | — |

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
   contraste, el comprobante de domicilio. Son binarios de cientos de kilobytes o megabytes, se
   capturan una vez por persona y no se borran cuando la persona deja de ser cliente.
2. **La prueba de que se tamizó** — el resultado del contraste contra las listas de personas y
   entidades sancionadas, con la lista, su versión y su fecha. RF-26 lo exige antes de aceptar el
   efectivo y RF-27 otra vez al autorizar el pago, así que son **dos evidencias por giro, haya o no
   coincidencia**: la ausencia de coincidencia también hay que poder demostrarla, y una auditoría
   necesita saber contra qué versión de qué lista se aprobó lo que se aprobó.
3. **El registro inalterable** — el asiento contable de cada movimiento y la traza de auditoría que
   RF-54 asocia a la identidad de quien ejecutó cada acto y RF-55 impide modificar o eliminar. Esta
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

Debajo de esa retención larga viven dos plazos cortos que no cambian el total pero sí **dónde está
el dato**: una retención dura como mucho 72 h antes de que RF-32 la resuelva devolviendo al emisor, y
un giro es pagable 12 meses antes de que RF-49 lo vuelva no pagable. Todo lo demás es archivo: dato
que hay que conservar y casi nunca leer.

| Tipo de dato | Qué es | Tamaño unitario | Cuántos por giro | Volumen diario | Años de retención | Marca |
|---|---|---|---|---|---|---|
| Registro del giro | — | — | — | — | — | — |
| Asiento contable | — | — | — | — | — | — |
| Cotización producida y fechada (RF-07) | — | — | — | — | — | — |
| Documento de identidad (binario, RF-01) | — | — | — | — | — | — |
| Resultado de tamizaje (RF-26 y RF-27: dos por giro) | — | — | — | — | — | — |
| Caso de cumplimiento y su evidencia de liberación (RF-33) | — | — | — | — | — | — |
| Traza de auditoría de actos y de accesos (RF-54, RNF-04) | — | — | — | — | — | — |
| Comprobante de entrega en destino | — | — | — | — | — | — |
| Aviso al receptor (prueba de aviso, RF-25) | — | — | — | — | — | — |
| Devolución al emisor (RF-32, RF-47, RF-50) | — | — | — | — | — | — |

### Agregado

| | Fórmula | Valor | Marca |
|---|---|---|---|
| Espacio por giro | suma de los tipos por su multiplicidad | — | — |
| Almacenamiento diario | `espacio por giro × giros por día` | — | — |
| Almacenamiento retenido | `diario × 365 × años de retención (S-09, ≥ 5)` | — | — |
| Almacenamiento caliente | la fracción del retenido que todavía es pagable: `diario × 365 × 1` por los 12 meses de prescripción (S-11) | — | — |
| Almacenamiento independiente del giro | identidad y verificación de un emisor identificado en ventanilla que no llegó a crear giro (RF-01 corre antes de RF-02) | — | — |

**Verificación mínima antes de dar por buena la cifra:** si el binario de identidad no es la partida
más grande, o el cálculo omitió la retención, o supuso que solo se guarda evidencia cuando hay
coincidencia. Los tres errores producen un número demasiado pequeño y demasiado creíble.

---

## Cálculo 3 — Ancho de banda requerido

El método: **data de entrada por día → data de salida por día → dividir entre 86 400 s.**

| Paso | Qué se cuenta | Valor | Marca |
|---|---|---|---|
| 1. Entrada por día | Lo que sube al sistema: capturas de identidad de RF-01, respuestas de las listas de sanciones, y las confirmaciones de cobro que suben desde los puntos de atención —incluida la ráfaga que sube un punto al recuperar la conexión y reconciliar su estado (RNF-08), que no es tráfico uniforme | — | — |
| 2. Salida por día | Lo que el sistema entrega: cotizaciones fechadas, estados consultados por el emisor (RF-52, RF-53, RF-66), avisos por llamada o mensaje al receptor (RF-25, RF-41), y las descargas de evidencia que hace cumplimiento | — | — |
| 3. Entrada por segundo | `entrada por día / 86 400` | — | — |
| 4. Salida por segundo | `salida por día / 86 400` | — | — |
| 5. Pico | `resultado × P` | — | — |

Dos observaciones específicas de este caso:

- **La asimetría se invierte respecto del ejemplo del material.** En YouTube la salida aplasta a la
  entrada por tres órdenes de magnitud: se sube un vídeo y se descarga cien millones de veces. En
  SendIt el binario pesado —el documento de identidad— **entra** y casi nunca sale; lo que sale son
  respuestas de pocos kilobytes consultadas muchas veces.
- **Dividir entre 86 400 supone que la carga es uniforme, y no lo es.** El resultado del paso 3 es
  un promedio contra el que no se dimensiona nada. La cifra que se usa es la del paso 5.

---

## Qué invalida esta estimación

Se registra aquí para que el paso siguiente sepa sobre qué está parado.

| Si cambia… | Se recalcula | Y hay que revisar |
|---|---|---|
| El número de corredores (S-01, anclado en RNF-12) | Los tres cálculos | `D` — otra red afiliada que sincronizar, con otra calidad de conexión; `A` — otro plazo de conservación en el máximo por corredor |
| Los años de retención (S-09, anclado en RNF-03 y RF-18) | Almacenamiento | `A` — la política de retención por entidad, que es por giro y no global |
| El plazo de retención o el de prescripción (S-10, S-11) | Almacenamiento caliente, y el caudal de casos de cumplimiento | `E` (escalar) — el tamaño en régimen de la cola de cumplimiento |
| El factor de pico (S-07) | Servidores y ancho de banda | `E` (escalar) — el tramo en que el sistema se rompe |
| La tasa de coincidencias (S-08) | Almacenamiento | `D` — dónde corre el tamizaje; `L` — el componente que lo ejecuta |
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
