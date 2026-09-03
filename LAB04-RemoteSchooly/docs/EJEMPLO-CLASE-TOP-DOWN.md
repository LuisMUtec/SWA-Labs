# El ejemplo de clase — Top Down Design

Transcripción y lectura del excalidraw que el profesor mostró en clase
([módulo del curso](https://utec.instructure.com/courses/24631/modules/items/2549106), requiere
sesión UTEC). El caso del ejemplo es **Leasing**, no RemoteSchooly: lo que se hereda es el **método**, no
el contenido.

![Top Down Design — el ejemplo de clase](ejemplo-clase-top-down.png)

> El original es un excalidraw; lo que se conserva acá es la captura
> ([`ejemplo-clase-top-down.png`](ejemplo-clase-top-down.png)). El resto de este documento la lee.

---

## Qué establece el ejemplo

**1. «Las iteraciones de su diseño» son iteraciones del diagrama de componentes.**

Es la lectura que decide el entregable. El enunciado del Caso #3 exigía *"mostrar claramente las
iteraciones de su diseño"*; el del **Caso #4 ya no lo repite**, pero paga 5 de sus 20 puntos por
*"happy path(s) se cumple en Diagrama"*, que es lo mismo visto desde el otro lado: el diagrama tiene
que **mostrar** que cada flujo corre. El ejemplo dice qué significa: **el mismo diagrama, dibujado
tres veces, cada vez más abierto.** No son versiones de un documento ni rondas de revisión: es
refinamiento sucesivo — *top down design*.

| Iteración | Qué se ve |
|---|---|
| **#1** | Los actores conectados a **una sola caja**. Todo el sistema es un cuadrado que dice `leasing app` |
| **#2** | Esa caja se abre en servicios, con sus bases de datos, sus APIs externas y sus dos ramas de resultado |
| **#3** | Se agrega lo que faltaba del backlog — evaluación, presupuesto, cobranza, reportes — repitiendo el subgrafo de la #2 |

La consecuencia práctica: **no se dibuja el diagrama final y después se inventan las iteraciones
previas.** El paso 1 es un cuadrado. Lo que fuerza el paso 2 es un ítem del backlog que el cuadrado
no explica, y lo mismo el 3.

**2. El backlog gobierna las iteraciones, y se marca `DONE`.**

El lienzo lleva, arriba a la izquierda, el backlog escrito a mano, y los ítems ya cubiertos por el
diagrama terminan con la palabra **DONE**:

```
Leasing
- el sistema soportara registro de pymes                                    DONE
- el sistema soportara ver mi balance diario como lease company
- el sistema permitira registrar solicitud de leasing
- el sistema enviara mensajes de aprobación de leasing
- el sistema me permitira ver mis deudores y montos adeudados - Leaser      DONE
```

Ese `DONE` es el mecanismo de trazabilidad completo: **una iteración del diagrama existe porque hay
un ítem sin `DONE`.** El diagrama no crece por gusto; crece hasta que el backlog está cubierto.

**3. El formato de un ítem de backlog.**

Literalmente: *"el sistema [verbo en futuro] [capacidad]"*. Y cuando el ítem pertenece a alguien en
particular, se le anexa el actor: *"...ver mis deudores y montos adeudados **- Leaser**"*.

Coincide con la restricción del enunciado del Caso #3 —*solo un título claro y entendible, sin
describirlo*— y le agrega algo que el enunciado no dice pero el ejemplo sí hace: **el ítem nombra a
su dueño**.

El enunciado del Caso #4 **no repite esa restricción**. Se adopta igual, porque el profesor la dictó
en voz en la clase del 2026-08-25: *"no puede ser una lista, un backlog"* `[15:00]`, *"mapean
requerimientos, es un backlog, por si acaso, un backlog"* `[76:52]`. Queda registrado en
[`D-02`](DECISIONES.md).

---

## El diagrama, iteración por iteración

### Iteración #1 — la caja única

```
PYME ──┐
Leaser ─┼──▶ [ leasing app ]
Broker ─┤
Proveedor ─┘
```

Cuatro actores y un cuadrado. Nada más. Lo único que afirma es **quién habla con el sistema**.

### Iteración #2 — la caja se abre

```
PYME ──▶ Login Service ──▶ Security Service ──▶ (BD)
              │
              ▼
      Validation Service ──▶ INFO CORP API   ┐
              │           ──▶ SUNAT           ├─ externos
              │           ──▶ RENIEC          ┘
              │
              ├──"TODO OK"────────▶ Register Service ──▶ (BD)
              │
              └──"Validation Failed"─▶ Messaging Service ──▶ SMS Service
                                                        └──▶ Email Service

Broker ──▶ leasing app ──▶ Register Service
Leaser ──▶ leasing app
```

Lo que aparece por primera vez, y que la iteración #1 no podía mostrar: la **autenticación**, la
**validación contra terceros**, la **bifurcación del resultado** y el **canal por el que se avisa
cuando falla**.

### Iteración #3 — el resto del backlog

Repite todo el subgrafo de la #2 y le agrega:

```
Loan Service ──▶ Evaluation Service ──▶ Budget Service
                        │            ──▶ Provider API
                        ├──"OK"──────▶ (BD)
                        │          ──▶ Messaging Service
                        └──"NO LOAN"─▶ LoanCancel Service ──▶ LessAmount Service ──▶ Messaging Service ──▶ (BD)
                                                          └──▶ Messaging Service

Debt Job <EOD> ──▶ Evaluation Service
               ──▶ Report Service ──▶ Debt Dashboard ◀── Leaser
```

---

## Convenciones que se adoptan

| Convención | Regla |
|---|---|
| **Servicio** | `<Nombre> Service` — `Login Service`, `Validation Service`, `Register Service` |
| **Proceso batch** | `<Nombre> Job <momento>` — `Debt Job <EOD>` (*end of day*) |
| **Base de datos** | `BD`, en elipse. **Hay varias**, no una sola: cada grupo de servicios tiene la suya |
| **Sistema externo** | Su nombre real — `SUNAT`, `RENIEC`, `INFO CORP API`, `Provider API` |
| **Actor** | Círculo con etiqueta, fuera del sistema |
| **Rama condicional** | La arista lleva su etiqueta: `TODO OK`, `Validation Failed`, `OK`, `NO LOAN` |

**Código de color.** Hay que leerlo del dibujo, no de su leyenda: la leyenda del lienzo declara
solo dos categorías —un cuadrado verde rotulado `BD` y uno azul rotulado `LEASING`— y el diagrama
usa cinco colores que no le corresponden. Es una leyenda de pizarra que quedó a medio hacer. Lo que
el cuerpo del diagrama efectivamente hace, que es lo que se adopta:

| Color | Qué agrupa |
|---|---|
| Azul | Servicios propios del sistema |
| Verde | Servicios de soporte y notificación — `Messaging`, `SMS`, `Email`, `Dashboard` |
| Rosado | Sistemas de terceros, fuera de la frontera de confianza |
| Amarillo | Procesos batch y servicios secundarios |
| Naranja (elipse) | Bases de datos — **pese a que la leyenda las pinta de verde** |

El código de color hace un trabajo real: **el rosado marca dónde termina el sistema**. Todo lo
rosado es algo sobre lo que el diseño no manda, y por lo tanto algo que puede fallar, mentir o
tardar sin que el sistema pueda impedirlo.

---


---

## Cómo se traduce a RemoteSchooly

Lo que se hereda es el método. Lo que cambia es qué hay del otro lado de cada frontera.

| En el ejemplo (Leasing) | En RemoteSchooly |
|---|---|
| `SUNAT`, `RENIEC`, `INFO CORP API` | El proveedor de modelos de IA con el que Marisol genera, que **se paga por token** y es el que hay que bajar 40 %. Y el transporte hacia la región, que puede ser de un tercero |
| `Validation Service` con dos ramas | La verificación de que la semana llegó **completa e íntegra**: la rama de fallo no es un mensaje al usuario, es que la clase del lunes no existe |
| `Messaging Service` → `SMS` / `Email` | El canal por el que Rómulo se entera de que le falta una pieza **antes** de la clase, y por el que Aurelio se entera de que una región no recibió |
| Una `BD` por grupo de servicios | La central en Lima y **el almacén local del pueblo**, que no son la misma base ni pueden serlo |
| `Debt Job <EOD>` | El corte semanal: el momento en que la semana se congela, se empaqueta y sale hacia las regiones |

La diferencia de fondo **no es de color, y ahí es donde el método heredado se queda corto.** En
Leasing todo el azul está conectado por definición: el diseño manda sobre sus servicios y el rosado
marca dónde deja de mandar. Una sola frontera alcanza.

Acá hacen falta dos. El nodo del pueblo es propio —azul, corriendo nuestro software, obedeciendo
nuestras órdenes— pero **está del otro lado de un enlace que no responde**. El enunciado lo dice como
premisa, no como falla: *"en estos pueblos el internet es limitado"*. Así que el diagrama tiene que
marcar **dónde termina el mando** (lo heredado) y **dónde termina la conexión** (lo que este caso
obliga a inventar). Todo lo que quede al otro lado de esa segunda línea tiene que poder servirle la
semana a Nayra sin preguntarle nada a Lima.

Y una advertencia que el ejemplo no puede dar, porque su caso no la tiene: **`[113:48]` — en este
diagrama todavía no va tecnología.** «Acá no pongo Java, acá no pongo Amazon, Azure, acá no pongo
Postgres.» El nombre del proveedor de IA no entra; entra que hay un servicio que genera y que cuesta.

## Dónde aterriza cada cosa

| Lo que establece el ejemplo | Dónde se cumple en este repo |
|---|---|
| Iteraciones del diagrama | [`../redale/L-listar-componentes/`](../redale/L-listar-componentes/) |
| Backlog con `DONE` | Tabla de trazabilidad *ítem → iteración que lo cubre*, en el mismo paso `L` |
| Formato del ítem | [`../redale/R-requerimientos/backlog.md`](../redale/R-requerimientos/backlog.md), por [`D-02`](DECISIONES.md) |
| Bitácora de qué cambió y por qué | [`../redale/ITERACIONES.md`](../redale/ITERACIONES.md) |
