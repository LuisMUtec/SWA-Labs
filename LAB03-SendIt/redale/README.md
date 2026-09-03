# R.E.D.A.L.E. — el método

Framework para diseñar una arquitectura desde cero, tomado del capítulo 3 del curso
(`2026.II-chapter 3-Arquitectura-2.pdf`, Carlos Balbuena), a su vez basado en
*The System Design Interview* — Lewis C. Lin & Shivam P. Patel.

> Diseñar una arquitectura sin un método es como construir un edificio sin planos.

| Paso | Nombre | Salida | Carpeta |
|---|---|---|---|
| **R** | Requerimientos | El [backlog](R-requerimientos/backlog.md) —lo único puntuado— y sus [insumos](R-requerimientos/insumos.md) | [`R-requerimientos/`](R-requerimientos/) |
| **E** | Estimar | Servidores, almacenamiento y ancho de banda requeridos | [`E-estimar/`](E-estimar/) |
| **D** | Diseñar el servicio | Arquitectura high-level, tipo de persistencia, diseño de API | [`D-disenar-servicio/`](D-disenar-servicio/) |
| **A** | Armar el modelo de datos | Tablas/objetos, campos, opciones de almacenamiento | [`A-armar-modelo-datos/`](A-armar-modelo-datos/) |
| **L** | Listar los componentes | El diagrama de la arquitectura base | [`L-listar-componentes/`](L-listar-componentes/) |
| **E** | Escalar | Qué cambia cuando la carga sube | [`E-escalar/`](E-escalar/) — *el material lo marca como "esto no lo usaremos aún"* |

El orden importa: cada paso consume la salida del anterior. Una estimación sin
requerimientos no tiene contra qué estimar, y un diagrama sin modelo de datos dibuja cajas
que nadie llenó.

---

## R — Requerimientos

Preguntar todo lo necesario para entender qué estamos resolviendo:

- ¿Tenemos claro el o los problemas?
- ¿Para quién estamos resolviendo el problema?
- ¿Cuáles son las limitaciones?

> Requerimientos poco claros y ambiguos son parte del mundo "real" del trabajo en ingeniería
> de software. Debemos romper la fantasía de que nos van a dar todo documentado y listo para
> diseñar/programar.

**Salida:** lista de requerimientos funcionales / no funcionales. El formato puede ser lista
o tipo backlog — **este caso exige backlog** (ver [restricciones](../docs/LAB-03-ARQ-2026.2.md#restricciones)).

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

## D — Diseñar el servicio

Qué construimos y cómo. A alto nivel: **qué arquitectura** (3-tier, MVC, monolito,
servicios), **qué persistencia** (SQL, NoSQL, mixta) y **el diseño de la API** (endpoints).
Aquí se define el alcance y las expectativas de la arquitectura.

## A — Armar el modelo de datos

Tablas, campos, opciones de base de datos y otros almacenamientos (archivos, caché, object
storage, sistemas de archivos distribuidos).

## L — Listar los componentes

Diagramar la arquitectura con todo lo mapeado en los pasos previos: la arquitectura base.

## E — Escalar

Qué pasa si la carga aumenta, y dónde aparece el cuello de botella. El material lo presenta
por tramos (< 1 k usuarios, 1 k–10 k, …) y **lo marca como fuera de alcance por ahora**.

---

## Iteraciones

El enunciado pide **mostrar claramente las iteraciones del diseño**. Cada pasada por
R.E.D.A.L.E. queda registrada en [`ITERACIONES.md`](ITERACIONES.md): qué cambió, en qué paso,
y qué lo forzó. Un paso que se corrige tarde arrastra a los que dependen de él — esa
propagación es justamente lo que la bitácora tiene que dejar ver.
