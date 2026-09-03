# SWA — Caso de Estudio #4: RemoteSchooly

Arquitectura de Software — UTEC 2026-II.
Diseño de la arquitectura de una plataforma de **educación en línea para pueblos remotos del Perú**,
por el método [R.E.D.A.L.E.](redale/README.md)

**Entrega: 2026-09-03 23:59** · 20 ptos · dificultad *Medium*

## Contexto

El gobierno encarga llevar educación en línea a pueblos remotos. Los materiales salen de una central
en Lima y tienen que llegar a todas las regiones, incluso las más lejanas, **donde el internet es
limitado**: los alumnos necesitan el material de la semana y los profesores necesitan poder enseñar
sin problema.

Hay un segundo problema, y es el que tiene filo: **los profesores que generan los materiales abusan
de la IA de la plataforma y el costo en tokens se disparó.** Como arquitecto se pide reducir ese
gasto **al menos 40 %**.

Los dos problemas se tocan. El material que la central genera es el mismo que hay que hacer llegar
por un enlace pobre, así que cada decisión sobre cómo se produce cambia cuánto hay que transmitir —
y al revés.

## Entregables

| Entregable | Puntos |
|---|---|
| Requerimientos | 3 |
| EVAL 8/10 passed | 2 |
| Diagrama de arquitectura | 10 |
| Happy path(s) cumplidos en el diagrama | 5 |

**Fuera de alcance por el enunciado:** asegurar 100 % de disponibilidad y los mecanismos de
confiabilidad. Pero **sí** se exige que los cursos lleguen correctamente.

El [pipeline del enunciado](docs/lab-04-pipeline.png) no deja pasar al diagrama sin `Score > 8` en
el EVAL de requerimientos. El EVAL del diagrama con agentes aparece dibujado como *not yet*.

## El método

[R.E.D.A.L.E.](redale/README.md), en seis pasos, cada uno consumiendo la salida del anterior:

| Paso | Salida | Carpeta |
|---|---|---|
| **R** Requerimientos | El [backlog](redale/R-requerimientos/backlog.md) — lo único que el EVAL puntúa | [`redale/R-requerimientos/`](redale/R-requerimientos/) |
| **E** Estimar | Servidores, almacenamiento, ancho de banda | [`redale/E-estimar/`](redale/E-estimar/) |
| **D** Diseñar el servicio | Arquitectura, persistencia, API | [`redale/D-disenar-servicio/`](redale/D-disenar-servicio/) |
| **A** Armar el modelo de datos | Entidades y dónde viven | [`redale/A-armar-modelo-datos/`](redale/A-armar-modelo-datos/) |
| **L** Listar los componentes | **El diagrama** — 15 de los 20 puntos | [`redale/L-listar-componentes/`](redale/L-listar-componentes/) |
| **E** Escalar | Fuera de alcance en este caso | [`redale/E-escalar/`](redale/E-escalar/) |

## Dónde vive cada cosa

| Ruta | Qué es |
|---|---|
| [`docs/`](docs/) | El enunciado en `.docx` y transcrito a `.md`, el pipeline, y la bitácora de [decisiones](docs/DECISIONES.md) |
| [`redale/`](redale/) | Los seis pasos del método y la [bitácora de iteraciones](redale/ITERACIONES.md) |
| [`personas/`](personas/) | Los usuarios modelo. Plantilla en [`_TEMPLATE.MD`](personas/_TEMPLATE.MD) |
| [`evals/`](evals/) | El [aparato de evaluación](evals/README.md) del backlog y el [historial](evals/HISTORY.md) de corridas |
| [`business-rules.md`](business-rules.md) | Las reglas que el sistema ejerce, separadas de los títulos que las invocan |
| [`.claude/`](.claude/) | Los agentes de persona del EVAL y los skills de Spec Kit |
| [`.specify/`](.specify/) | Spec Kit, con la [constitución](.specify/memory/constitution.md) del caso |
| [`scripts/`](scripts/) | Conversores de la entrega y el resumen a PDF |

## Lo que dejó dicho la corrección del Caso #1

El profesor abrió tres issues sobre el laboratorio 1 el 2026-09-02, y las tres apuntan al mismo
sitio: **194 requerimientos son inmanejables**, los no funcionales estaban **demasiado genéricos y
parecían escritos para que los leyera una IA y no una persona**, y con esos 194 ítems los EVAL
igual no se cumplían ni las necesidades de los usuarios quedaban cubiertas.

Aquí eso se traduce en una regla operativa y no en una intención: el backlog de este caso se mide
por **cobertura de los flujos de las personas**, no por volumen, y cada no funcional lleva **medida**
o no entra.

## Estado

**Recién creado.** No hay personas escritas, el backlog está vacío, la constitución sin ratificar y
el EVAL sin correr. Todo el andamiaje viene del [Caso #3](../LAB03-SendIt/), vaciado de su
contenido.

El primer paso es `R`: responder las tres preguntas de encuadre en
[`redale/R-requerimientos/backlog.md`](redale/R-requerimientos/backlog.md) y volcar el enunciado en
[`insumos.md`](redale/R-requerimientos/insumos.md).

## Casos hermanos

[#1 UCI-EsSalud](../LAB01-UCI-Essalud/) · [#2 Lea$e](../LAB02-Lease/) · [#3 SendIt](../LAB03-SendIt/)
