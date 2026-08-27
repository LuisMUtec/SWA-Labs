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
objetivo. Diseñar hoy para el millón de usuarios es el error que el paso previene, no el que
recomienda.

---

## Contrato con los pasos vecinos

| | |
|---|---|
| **Consume de L** | El diagrama base de la última iteración. Sin él no hay sobre qué preguntar qué se rompe primero |
| **Consume de E** (estimar) | La carga inicial, el factor de pico y los supuestos declarados. Un tramo es una carga, y la carga viene de ahí |
| **Consume de D** | Las cinco decisiones. Varias tienen un tramo en el que dejan de funcionar: la conciliación revisada a mano se rompe mucho antes que la base de datos |
| **Entrega a** | Nadie. Es el último paso, y por eso es el único que puede quedar sin cerrar sin invalidar a otro |
| **Queda inválido si L cambia** | El componente que se nombró como primer cuello de botella, si dejó de existir o cambió de lugar |
| **Queda inválido si E (estimar) cambia** | El tramo en el que el sistema arranca, y con él el orden de todo lo demás |

---

## Contra qué se cuenta un tramo

El material rotula sus tramos en **usuarios**. Antes de llenar nada hay que declarar qué usuario,
porque en este dominio la palabra tapa tres cosas que no escalan igual: **usuarios registrados**,
**remitentes activos al mes** y **envíos por día**. Un millón de registrados que envían dos veces al
mes y un millón de envíos diarios son sistemas distintos por dos órdenes de magnitud.

| Tramo | Usuarios registrados | Remitentes activos/mes | Envíos/día | Envíos/día en pico |
|---|---|---|---|---|
| `< 1 k` | — | — | — | — |
| `1 k – 10 k` | — | — | — | — |
| `100 k` | — | — | — | — |
| `500 k` | — | — | — | — |
| `1 M` | — | — | — | — |

---

## Los tramos

Una tabla por tramo. Se llena de arriba hacia abajo: lo que se rompe en un tramo sigue roto en el
siguiente si no se arregló.

### `< 1 k` usuarios

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| — | — | — |

### `1 k – 10 k` usuarios

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| — | — | — |

### `100 k` usuarios

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| — | — | — |

### `500 k` usuarios

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| — | — | — |

### `1 M` usuarios

| Qué se rompe primero | Por qué | Qué cambia en la arquitectura |
|---|---|---|
| — | — | — |

**Un candidato a primer cuello de botella que no es técnico y suele quedar fuera:** el trabajo
humano de cumplimiento. El equipo revisa casos uno por uno. Si la tasa de coincidencias se mantiene y
los envíos se multiplican por diez, lo primero que se satura no es una base de datos sino la cola de
el equipo — y una retención sin decidir es dinero de alguien detenido en silencio. Ese límite llega
antes que casi cualquier límite de máquina, y la respuesta no es más servidores.

---

## Qué escala distinto en una remesa

Los ejemplos del material escalan redes sociales y un rastreador de páginas. Tres diferencias
cambian qué respuesta sirve.

**1. La carga no es lectura, es escritura contable.** El repertorio habitual —caché, réplicas de
lectura, contenido distribuido en el borde— resuelve el problema de servir muchas veces lo mismo. En
SendIt el trabajo caro es el pago, y una réplica de lectura no acepta un asiento. Peor: los datos
que más se consultan son justamente los que no toleran estar viejos, porque son el monto que Rosa
prometió y el estado de un envío detenido. Cachearlos es servir una mentira reciente. El eje de
escalamiento tiene que ser el de escritura, y ese eje se paga con particionamiento, con lo que trae:
decidir por qué clave se parte un libro contable sin que un asiento quede a caballo entre dos
particiones.

**2. El pico es estacional, no continuo.** El volumen se concentra en la quincena, el fin de mes y
unas pocas fechas señaladas. El sistema pasa la mayor parte del año por debajo de su capacidad y
falla los días que a Rosa le importan. Dos consecuencias:

- Escalar automáticamente por reacción llega tarde. Un pico que dura horas y se conoce con meses de
  anticipación se atiende **provisionando por calendario**, no esperando a que suba una métrica.
- El promedio anual es una cifra inútil para dimensionar y una cifra cómoda para reportar. El tramo
  en el que está el sistema es el de su pico, no el de su media.

**3. Añadir un corredor no es más de lo mismo.** Este es el eje de crecimiento que los tramos del
material no tienen, porque una red social crece con más usuarios de la misma clase y una remesa crece
con **otro país**:

| Lo que trae un corredor nuevo | Por qué no es escalar horizontalmente |
|---|---|
| Otro regulador | Otros umbrales de reporte, otras obligaciones de retención, otra autoridad. Es lógica de negocio nueva, no más instancias de la vieja |
| Otra moneda | Otra posición de cambio, otro proveedor de tasa, otra cuenta de diferencia de cambio en el libro |
| Otra red pagadora | Otro registro contable con el que conciliar, otro formato, otra ventana de divergencia, otro modo de fallar |
| Otras listas y otra forma de identidad | Lo que sirve como documento válido en un país no sirve en otro, y el tamizaje cambia de fuente |
| Otro huso horario | El pico se mueve, y dos corredores pueden tener picos que no se solapan — o que sí |

De modo que la pregunta que este paso tiene que dejar contestada no es solo «¿qué pasa con diez
veces más usuarios?» sino **«¿qué pasa con el segundo corredor?»**. Si la respuesta es «se duplica
el sistema», el diseño de [`D`](../D-disenar-servicio/README.md) no separó lo que era común de lo
que era del corredor, y eso se arregla allá, no acá.

---

## Qué invalida este paso

| Si cambia… | Se rehace |
|---|---|
| El factor de pico en [`E`](../E-estimar/README.md) | El tramo de arranque y el orden de los cuellos de botella |
| Una decisión de [`D`](../D-disenar-servicio/README.md) | El tramo en el que esa decisión dejaba de sostenerse |
| El diagrama de [`L`](../L-listar-componentes/README.md) | El componente nombrado como primer punto de ruptura |
| El corredor supuesto (`S-01`) | La tabla de corredor nuevo, y probablemente el eje de crecimiento entero |

---

## Nota sobre las dos clases de iteración

[`ITERACIONES.md`](../ITERACIONES.md) distingue la **iteración del diseño** —el mismo diagrama de
componentes dibujado otra vez y más abierto, que es la que el enunciado exige mostrar (ver el
[ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md))— de la **iteración del EVAL**, que cambia
una decisión del backlog. Este paso **no produce** iteraciones del diseño: no abre cajas, comenta
qué les pasa bajo carga. Si al llenarlo aparece un componente que el diagrama no tiene, eso no se
dibuja aquí — se vuelve a [`L`](../L-listar-componentes/README.md) y se abre otra pasada allá, con
el ítem del backlog que la justifique.
