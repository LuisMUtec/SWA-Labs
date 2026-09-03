# R.E.D.A.L.E. — el método

Framework para diseñar una arquitectura desde cero, tomado del capítulo 3 del curso
(`2026.II-chapter 3-Arquitectura-2.pdf`, Carlos Balbuena), a su vez basado en
*The System Design Interview* — Lewis C. Lin & Shivam P. Patel.

> Diseñar una arquitectura sin un método es como construir un edificio sin planos.

| Paso | Nombre | Salida | Carpeta |
|---|---|---|---|
| **R** | Requerimientos | El [backlog](R-requerimientos/backlog.md) —lo único puntuado por el EVAL— y sus [insumos](R-requerimientos/insumos.md) | [`R-requerimientos/`](R-requerimientos/) |
| **E** | Estimar | Servidores, almacenamiento y ancho de banda requeridos | [`E-estimar/`](E-estimar/) |
| **D** | Diseñar el servicio | Arquitectura high-level, tipo de persistencia, diseño de API | [`D-disenar-servicio/`](D-disenar-servicio/) |
| **A** | Armar el modelo de datos | Tablas/objetos, campos, opciones de almacenamiento | [`A-armar-modelo-datos/`](A-armar-modelo-datos/) |
| **L** | Listar los componentes | El diagrama de la arquitectura base — **10 de los 20 puntos** | [`L-listar-componentes/`](L-listar-componentes/) |
| **E** | Escalar | Qué cambia cuando la carga sube | [`E-escalar/`](E-escalar/) — *el material lo marca como "esto no lo usaremos aún"* |

El orden importa: cada paso consume la salida del anterior. Una estimación sin
requerimientos no tiene contra qué estimar, y un diagrama sin modelo de datos dibuja cajas
que nadie llenó.

## Qué pesa en este caso

El [enunciado](../docs/LAB-04-ARQ-2026.2.md) reparte 20 puntos y **15 de ellos están en el
diagrama**: 10 por la arquitectura y 5 por los happy paths que debe mostrar cumplidos. Los
requerimientos valen 3 y el gate del EVAL vale 2.

Eso no invierte el orden —el pipeline del enunciado no deja pasar al diagrama sin `Score > 8`—
pero sí fija dónde se gana la nota. El backlog es la llave de entrada, no el entregable
principal. Conviene tenerlo presente al decidir su tamaño: en el Caso #1 el profesor objetó
194 requerimientos como *inmanejables*, y objetó que los no funcionales parecieran escritos
para que los leyera una IA y no una persona.

## Alcance que el enunciado recorta

Dos cosas quedan explícitamente fuera y **no** deben consumir diseño:

- No hace falta asegurar 100 % de disponibilidad — pero **sí** que los cursos lleguen correctamente.
- No hace falta todavía usar mecanismos de confiabilidad.

Lo que sí es obligación de este caso: los materiales salen de una central en Lima y llegan a
regiones remotas **con internet limitado**, y el gasto de tokens de IA de los profesores debe
bajar **al menos 40 %**.

---

## R — Requerimientos

Preguntar todo lo necesario para entender qué estamos resolviendo:

- ¿Tenemos claro el o los problemas?
- ¿Para quién estamos resolviendo el problema?
- ¿Cuáles son las limitaciones?

> Requerimientos poco claros y ambiguos son parte del mundo "real" del trabajo en ingeniería
> de software. Debemos romper la fantasía de que nos van a dar todo documentado y listo para
> diseñar/programar.

**Salida:** lista de requerimientos funcionales / no funcionales. El formato puede ser lista o
tipo backlog.

## E — Estimar

Calcular las necesidades del sistema para funcionar sin degradación, y qué recursos hacen
falta para escalar.

**Entradas:** número total de usuarios · usuarios activos · RPS · logins por segundo ·
almacenamiento requerido.

Tres cálculos:

1. **Servidores requeridos**
   1. Cuánto maneja un único CPU core.
   2. Cuánto maneja un servidor = `#cores × capacidad de un core`.
   3. `#servidores = carga objetivo / capacidad de un servidor`.
   > Ejemplo: 1 core = 5 req/s · servidor de 32 cores = 160 req/s · para 100 k req/s →
   > 100 000 / 160 = **625 servidores**.
2. **Almacenamiento requerido**
   1. Determinar los tipos de dato.
   2. Estimar el espacio de cada tipo.
   3. Agregar y multiplicar por el volumen diario.
3. **Ancho de banda requerido**
   1. Data de entrada por día.
   2. Data de salida por día.
   3. Dividir entre 86 400 s para obtener el ancho de banda por segundo.

En este caso el ancho de banda no es un número decorativo: **el enlace de la región es la
restricción del enunciado**, y es contra él que se dimensiona la distribución de materiales.

## D — Diseñar el servicio

Qué construimos y cómo. A alto nivel: **qué arquitectura** (3-tier, MVC, monolito,
servicios), **qué persistencia** (SQL, NoSQL, mixta) y **el diseño de la API** (endpoints).
Aquí se define el alcance y las expectativas de la arquitectura.

## A — Armar el modelo de datos

Tablas, campos, opciones de base de datos y otros almacenamientos (archivos, caché, object
storage, sistemas de archivos distribuidos).

## L — Listar los componentes

Diagramar la arquitectura con todo lo mapeado en los pasos previos: la arquitectura base.
Es el paso donde se juegan 15 de los 20 puntos, y donde los **happy paths** tienen que verse
cumplidos.

## E — Escalar

Qué pasa si la carga aumenta, y dónde aparece el cuello de botella. El material lo presenta
por tramos (< 1 k usuarios, 1 k–10 k, …) y **lo marca como fuera de alcance por ahora**.

---

## Iteraciones

Cada pasada por R.E.D.A.L.E. queda registrada en [`ITERACIONES.md`](ITERACIONES.md): qué cambió,
en qué paso, y qué lo forzó. Un paso que se corrige tarde arrastra a los que dependen de él —
esa propagación es lo que la bitácora tiene que dejar ver.
