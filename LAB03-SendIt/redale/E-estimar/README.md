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
| **Consume de R** | Los requerimientos funcionales que producen carga (cada operación que Rosa, Elena o Kevin ejecutan), los no funcionales con medida, y los supuestos ya declarados en el backlog |
| **Entrega a D** | El orden de magnitud contra el que se elige arquitectura y persistencia: si el sistema es de decenas o de cientos de servidores, si el almacenamiento cabe en una base o exige almacenamiento de objetos, y si el ancho de banda de salida cambia el diseño de la API |
| **Queda inválido si R cambia** | **Todo.** Un requerimiento funcional nuevo agrega un tipo de dato o una operación, y ambos entran en los tres cálculos. Un supuesto que se retira —el corredor, la frecuencia de envío— reescribe la tabla de entradas completa |
| **Invalida a D, A, L y E** | Cambiar una entrada aquí mueve el dimensionamiento; si el resultado cruza un orden de magnitud, la arquitectura elegida en `D` deja de estar justificada por sí sola |

Cuando una cifra de este paso cambie, se abre una fila en [`ITERACIONES.md`](../ITERACIONES.md) y se
recorren `D`, `A`, `L` y `E` buscando qué quedó afirmando lo viejo.

---

## Entradas del paso

Las cinco que pide el material. Ninguna viene del enunciado.

| Entrada | Valor | De dónde sale | Marca |
|---|---|---|---|
| Usuarios totales (registrados) | — | — | — |
| Usuarios activos | — | — | — |
| RPS — requests por segundo | — | — | — |
| Logins por segundo | — | — | — |
| Almacenamiento requerido | — | — | — |

Se agrega una sexta que el material no lista y este caso obliga: **envíos por día**. El usuario de
una red social genera carga cada vez que abre la aplicación; el de una remesa genera carga cuando
manda dinero, dos veces al mes. Estimar SendIt por usuarios activos sin pasar por envíos diarios
mide la cosa equivocada.

| Entrada añadida | Valor | De dónde sale | Marca |
|---|---|---|---|
| Envíos por día | — | — | — |
| Factor de pico | — | — | — |

---

## Supuestos declarados

El ejemplo del material estima YouTube con cifras que el enunciado del ejercicio da (100 M de
usuarios activos, 10 vídeos por usuario, 1,3 M de vídeos diarios). **El enunciado de SendIt no da ni
una cifra.** Consecuencia directa: aquí toda entrada es un `[ASSUMPTION: ...]`, y un supuesto que no
declara contra qué se calibró es un número inventado con formato de estimación.

Cada fila declara **por qué hace falta** —qué cálculo se cae sin ella— y **contra qué se calibra**,
que es la única defensa que tiene un supuesto.

| # | Supuesto que hace falta | Por qué hace falta | Contra qué se calibra | Valor | Estado |
|---|---|---|---|---|---|
| S-01 | Corredor o corredores atendidos | Fija la moneda, el regulador, la red de puntos de pago propios que hay que abrir y operar, y el huso horario del pico. Sin él no hay volumen que estimar ni reglas que aplicar | El corredor que modela [Rosa](../../personas/Rosa.MD): Estados Unidos → Perú | — | — |
| S-02 | Usuarios registrados | Dimensiona el almacenamiento de identidad y de verificación, que se retiene aunque el usuario no envíe nunca más | — | — | — |
| S-03 | Proporción de usuarios activos sobre registrados | El registrado inactivo ocupa disco y no genera RPS. Confundirlos sobredimensiona el cómputo y subdimensiona la retención | — | — | — |
| S-04 | Envíos por usuario activo al mes | Convierte usuarios en envíos, que es la unidad real de carga | El patrón de Rosa: quincenal, estable desde hace tres años | — | — |
| S-05 | Ticket promedio | No mueve el cómputo, pero decide cuántos envíos cruzan el umbral de reporte y por lo tanto cuántos casos de cumplimiento se abren y se retienen | El rango de Rosa: USD 200–400 | — | — |
| S-06 | Consultas de estado por envío | Rosa consulta el estado sin necesitar que nadie le conteste. Es la operación de lectura dominante y no aparece en ningún requerimiento como carga | Lo que hoy la obliga a llamar por teléfono | — | — |
| S-07 | **Factor de pico** | Ver abajo | — | — | — |
| S-08 | Proporción de envíos que disparan una alerta de tamizaje | La tasa de coincidencias decide el volumen de evidencia, que es lo que domina el almacenamiento, y la abrumadora mayoría son homónimos | `[ASSUMPTION: sin fuente; el enunciado no da ninguna cifra de tamizaje]` | — | — |
| S-09 | Años de retención regulatoria | Multiplica el almacenamiento diario por un factor que el ejemplo de YouTube no tiene | — | — | — |

### El factor de pico

**Las remesas no son planas.** El volumen se concentra en la quincena y el fin de mes —cuando se
cobra— y se dispara en fechas señaladas: Día de la Madre, Navidad, el inicio del año escolar. El
sistema pasa la mayor parte del año por debajo de su capacidad y falla los pocos días que a Rosa le
importan, que son exactamente los días en que su madre tiene una fecha que cumplir.

De esto se sigue una regla para el cálculo 1: **el dimensionamiento se hace contra el pico, no
contra el promedio.** El promedio no falla nunca. Se declara como un factor explícito
`P = RPS pico / RPS promedio`, con su ventana (¿el pico dura una hora, un día, una semana?), porque
un pico de horas y uno de días no se enfrentan con la misma arquitectura.

| Ventana de pico | Multiplicador estimado | Qué la produce | Marca |
|---|---|---|---|
| Quincena / fin de mes | — | Ciclo de cobro del remitente | — |
| Fecha señalada | — | — | — |
| Hora del día | — | Huso horario del remitente, no del destinatario | — |

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
| 3. Carga objetivo | `RPS promedio × P` | — | — |
| 4. Servidores | `carga objetivo / capacidad de servidor` | — | — |

**Una advertencia que este caso obliga y el ejemplo del material no necesita:** un `request` de
SendIt no cuesta lo mismo que otro. Consultar el estado de un envío es una lectura; ejecutar un pago
es una escritura contable que toca varias filas, cruza una frontera —hacia el procesador que cobra a
Rosa, o hacia el mostrador que entrega el efectivo— y no puede servirse desde caché. Estimar con un
único «core = N req/s» promedia dos cosas que no se promedian.
Si el desglose por tipo de operación cambia el resultado en más de un orden de magnitud, se calcula
por separado y se suma.

| Operación | Tipo | Peso relativo | Volumen diario | Marca |
|---|---|---|---|---|
| Cotizar un envío | lectura | — | — | — |
| Ejecutar el pago | escritura contable | — | — | — |
| Consultar estado | lectura | — | — | — |
| Tamizar contra listas | lectura externa | — | — | — |
| Confirmar el cobro en destino | escritura contable + frontera | — | — | — |
| Login | — | — | — | — |

---

## Cálculo 2 — Almacenamiento requerido

El método: **determinar los tipos de dato → estimar el espacio de cada tipo → agregar y multiplicar
por el volumen diario.**

### Qué tipos de dato tiene una remesa, y cuál domina

La intuición engaña. El instinto dice que lo que ocupa es la transacción, y una transacción es una
fila de unos pocos cientos de bytes: quién manda, a quién, cuánto, cuándo. Si SendIt fuera solo
eso, el almacenamiento no sería un problema de arquitectura.

**Lo que ocupa es la evidencia.** Tres familias:

1. **La prueba de quién es cada quien** — imágenes de documento de identidad, la fotografía de
   contraste, el comprobante de domicilio. Son binarios de cientos de kilobytes o megabytes, se
   capturan una vez por persona y no se borran cuando la persona deja de ser cliente.
2. **La prueba de que se tamizó** — el resultado del contraste contra las listas de personas y
   entidades sancionadas, con la lista, su versión y su fecha. Se guarda **por cada envío, haya o no
   coincidencia**: la ausencia de coincidencia también hay que poder demostrarla, y una auditoría necesita
   saber contra qué versión de qué lista se aprobó lo que se aprobó.
3. **El registro inalterable** — el asiento contable de cada movimiento y la traza de auditoría.
   Esta última crece con las **lecturas**, no solo con las escrituras: cada consulta al expediente de cumplimiento sobre los
   datos de un cliente es una fila, porque su permiso dice que no puede consultarlos sin un caso
   abierto y eso solo es verificable si queda registrado que consultó.

Y sobre todo eso cae un multiplicador que el ejemplo de YouTube no tiene: **la retención
regulatoria**. YouTube se estima en «TB diarios». Una remesa se estima en `diario × 365 × años de
retención`, porque el dato de hace cinco años sigue ocupando disco por obligación legal. Un cálculo
que se detiene en el volumen diario subestima el total por dos órdenes de magnitud.

| Tipo de dato | Qué es | Tamaño unitario | Cuántos por envío | Volumen diario | Años de retención | Marca |
|---|---|---|---|---|---|---|
| Registro del envío | — | — | — | — | — | — |
| Asiento contable | — | — | — | — | — | — |
| Cotización / tasa aplicada | — | — | — | — | — | — |
| Documento de identidad (binario) | — | — | — | — | — | — |
| Resultado de tamizaje | — | — | — | — | — | — |
| Caso de cumplimiento y su evidencia | — | — | — | — | — | — |
| Traza de auditoría | — | — | — | — | — | — |
| Comprobante de entrega en destino | — | — | — | — | — | — |
| Aviso enviado a Elena (prueba de aviso) | — | — | — | — | — | — |

### Agregado

| | Fórmula | Valor | Marca |
|---|---|---|---|
| Espacio por envío | suma de los tipos por su multiplicidad | — | — |
| Almacenamiento diario | `espacio por envío × envíos por día` | — | — |
| Almacenamiento retenido | `diario × 365 × años de retención` | — | — |
| Almacenamiento independiente del envío | identidad por usuario registrado, se capture o no un envío | — | — |

**Verificación mínima antes de dar por buena la cifra:** si el binario de identidad no es la partida
más grande, o el cálculo omitió la retención, o supuso que solo se guarda evidencia cuando hay
coincidencia. Los tres errores producen un número demasiado pequeño y demasiado creíble.

---

## Cálculo 3 — Ancho de banda requerido

El método: **data de entrada por día → data de salida por día → dividir entre 86 400 s.**

| Paso | Qué se cuenta | Valor | Marca |
|---|---|---|---|
| 1. Entrada por día | Lo que sube al sistema: capturas de identidad, respuestas de las listas y del proveedor de tasa, y las confirmaciones de cobro que suben desde los puntos de pago —incluida la ráfaga que sube un punto al recuperar la conexión, que no es tráfico uniforme | — | — |
| 2. Salida por día | Lo que el sistema entrega: cotizaciones, estados consultados, avisos, y las descargas de evidencia que hace cumplimiento | — | — |
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
| El corredor (S-01) | Los tres cálculos | `D` — otra red de puntos propios que sincronizar, con otra calidad de conexión; `A` — otras reglas de retención |
| Los años de retención (S-09) | Almacenamiento | `A` — la política de retención por entidad |
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
