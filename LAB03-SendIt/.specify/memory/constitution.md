<!--
Sync Impact Report
Cambio de versión: ninguna → 1.0.0 (ratificación inicial)
Principios modificados: ninguno (primera versión)
Secciones agregadas:
  - Principios I–V
  - Ambigüedad y supuestos
  - Flujo de trabajo
  - Gobernanza
Secciones eliminadas: ninguna
Plantillas que requieren actualización:
  - .specify/templates/spec-template.md — sin cambio. Este caso no produce specs: el artefacto
    con autoridad es el backlog del paso R (Principio IV)
  - .specify/templates/plan-template.md, tasks-template.md — sin cambio, inertes por el mismo motivo
TODOs pendientes: ninguno
-->

# Constitución de SendIt

## Principios

### I. Los requerimientos se identifican antes de diseñar (NO NEGOCIABLE)

El [enunciado](../../docs/LAB-03-ARQ-2026.2.md) da dos hints y el orden entre ellos no es
negociable: primero se identifica quién es el usuario modelo, después se diseña el mecanismo de
seguridad. Ninguna cifra de capacidad, endpoint, tabla o caja del diagrama puede producirse antes de
que exista el requerimiento al que sirve.

De ahí sale la regla que gobierna los seis pasos: **los requerimientos bajan, nunca suben.** Ningún
paso aguas abajo puede introducir un comportamiento que el backlog no declare. Si `D` diseña un
endpoint que responde algo que ningún título exige, o `A` guarda un campo que ningún título obliga a
conocer, el defecto **es del backlog** y la corrección va arriba, nunca abajo.

Un requerimiento enuncia la garantía, nunca el mecanismo. Una cola, un producto de nube o una
topología dentro de un título es una decisión de diseño disfrazada: se mueve a
[`D`](../../redale/D-disenar-servicio/README.md), no se borra.

### II. Todo comportamiento tiene dueño

Todo comportamiento que el sistema exhiba traza o a la necesidad de una persona nombrada —
[Rosa](../../personas/Rosa.MD), [Elena](../../personas/Elena.MD),
[Kevin](../../personas/Operario.MD)— o a una regla de negocio. Lo que no traza a ninguna de las dos
se elimina o se le da dueño; nunca se conserva «por si acaso».

Las reglas de negocio forman **un solo cuerpo** en
[`business-rules.md`](../../business-rules.md), citadas por identificador estable. Los `BR-nn` no se
renumeran ni se reutilizan, aunque la redacción de la regla se revise.

### III. El problema manda

SendIt existe por una sola razón: entre que alguien paga en un país y alguien cuenta billetes en
otro, el dinero cruza dos jurisdicciones, cambia de moneda a una tasa que se mueve mientras el envío
viaja, y termina en efectivo en la mano de una persona sin cuenta bancaria. El último tramo lo
ejecuta un tercero sobre el que este diseño no manda.

El modo de falla que este principio existe para impedir es un «enviar plata» genérico: un sistema
que administra transferencias competentemente y nunca se hace cargo de la frontera. **Cualquier ítem
que sobreviva palabra por palabra si el envío dejara de cruzar un país está fuera de alcance.**

### IV. El gate del EVAL es 8/10 (NO NEGOCIABLE)

[`redale/R-requerimientos/backlog.md`](../../redale/R-requerimientos/backlog.md) es el único
documento con autoridad sobre qué debe hacer el sistema, y el único puntuado. Lo puntúa el aparato
de [`evals/`](../../evals/README.md) sobre cuatro dimensiones y diez puntos, y tiene que llegar a
ocho.

Los agentes de persona **solo pueden restar**: su trabajo es detectar la falla, no certificar el
éxito. Un puntaje por debajo del gate corrige el backlog, **nunca la vara**. Cada corrida queda
versionada, para que la mejora sea evidencia y no afirmación.

`E`, `D`, `A`, `L` y `E` son entregable exigido, no puntaje. Lo que impide que diverjan del backlog
no es puntuarlos, sino la regla de dirección del Principio I.

### V. Las iteraciones se muestran

El enunciado no pide un diseño: pide un diseño **con sus iteraciones a la vista**. Un diagrama final
sin los estados por los que pasó no cumple el entregable, por bueno que sea el dibujo.

Hay dos clases de iteración y ninguna sustituye a la otra: la del **diagrama** —que fuerza un ítem
del backlog que el dibujo anterior no explica— y la del **EVAL** —que fuerza un puntaje bajo el
gate—. Ambas se registran en [`redale/ITERACIONES.md`](../../redale/ITERACIONES.md).

Corregir el backlog invalida lo que los pasos aguas abajo afirmaban. **El rebarrido de propagación
se registra aunque no encuentre nada:** un rebarrido vacío es un resultado, uno que nadie corrió no
lo es, y son indistinguibles si no se anota.

## Ambigüedad y supuestos

El enunciado son cuatro líneas y deja el dominio abierto: no fija corredor, ni carga, ni moneda, ni
qué se le debe a quién cuando el dinero se detiene. La mayor parte de las reglas de este caso las
inventamos nosotros.

Lo que no está definido lleva una de dos marcas y **nunca se resuelve en silencio**:

- `[CLARIFY: pregunta específica]` cuando la respuesta determina el contenido.
- `[ASSUMPTION: enunciado]` cuando se avanza bajo una hipótesis declarada.

Una regla inventada sin marcar es un defecto, no un atajo. La marca es lo que le permite a un lector
distinguir el dominio de nuestras conjeturas.

## Flujo de trabajo

Un mismo tema puede aparecer a más de una altitud sin duplicarse, mientras cada altitud afirme algo
distinto. **Cada afirmación ocurre una sola vez, en su altitud.**

| Altitud | Dónde vive | Afirma |
|---|---|---|
| Gobierno | esta constitución | Por qué existe el proyecto y cómo se juzga el trabajo |
| Enunciado | [`docs/LAB-03-ARQ-2026.2.md`](../../docs/LAB-03-ARQ-2026.2.md) | Qué pidió el curso. Se transcribe, no se interpreta |
| Decisiones | [`docs/DECISIONES.md`](../../docs/DECISIONES.md) | Qué se decidió, entre qué opciones y qué cuesta |
| Método | [`redale/README.md`](../../redale/README.md) | Qué pregunta cada paso y qué entrega |
| Personas | [`personas/`](../../personas/README.md) | Quién es cada persona y qué necesita. Nunca qué hace el sistema |
| Dominio | [`business-rules.md`](../../business-rules.md) | Las reglas que obedece el negocio, `BR-nn` |
| Requerimientos | [`redale/R-requerimientos/backlog.md`](../../redale/R-requerimientos/backlog.md) | Qué debe hacer el sistema. Único artefacto puntuado |
| Diseño | `redale/E-estimar/` · `D-disenar-servicio/` · `A-armar-modelo-datos/` · `L-listar-componentes/` · `E-escalar/` | Cómo se sostiene lo que el backlog exige |
| Evaluación | [`evals/`](../../evals/README.md) | Cómo se puntúa el backlog y qué sacó cada corrida |

El orden de R.E.D.A.L.E. es vinculante porque cada paso consume la salida del anterior. Cada README
declara qué consume y qué queda inválido si el paso previo cambia; ese contrato es lo que hace
detectable la propagación del Principio V.

**Qué hace acá Spec Kit.** El harness está instalado —[`.specify/`](../) y las skills
`/speckit-*`— y **una sola de sus diez skills corre en este repositorio**: `/speckit-constitution`,
que mantiene este archivo. Las otras nueve exigen un `specs/<n>/` con `spec.md`, `plan.md` o
`tasks.md`, y este caso no produce ninguno de los tres; abortan antes de hacer nada. Están
declaradas inertes, no olvidadas — el detalle está en [`D-08`](../../docs/DECISIONES.md).

Lo que sí aporta el harness es la altitud que faltaba: este documento, y la estructura compartida con
el [Caso #2](https://github.com/LuisMUtec/SWA-LAB02-Lease), que vuelve comparables los dos
repositorios en su forma.

**Spec Kit no desplaza al backlog.** El enunciado fija el formato de los requerimientos —backlog, un
título claro y entendible, sin descripción— y por el Principio IV ese archivo es el único con
autoridad. Si alguna vez se produce un `specs/<n>/spec.md` para despertar alguna de las nueve, deriva
del backlog y no puede agregarle comportamiento: hacerlo sería una violación de la regla de dirección
del Principio I, y se cobra en D4 como *decisión sin requerimiento*.

## Gobernanza

Esta constitución prevalece sobre cualquier otra práctica del repositorio. Donde un documento aguas
abajo la contradiga, **el equivocado es el documento aguas abajo**.

Una enmienda exige un commit que diga qué cambió y por qué, un salto de versión bajo la política de
abajo, y el Sync Impact Report de la cabecera actualizado.

El versionado es semántico: MAYOR cuando un principio se elimina o se redefine de forma
incompatible, MENOR cuando se agrega o se amplía materialmente un principio o una sección, PARCHE
para aclaraciones que no cambian el significado.

El cumplimiento se revisa en cada corrida del EVAL y en cada transición entre pasos de R.E.D.A.L.E.
Un paso que viole un principio se corrige antes de avanzar; la complejidad que un principio prohíbe
se justifica por escrito o se descarta.

**Versión**: 1.0.0 | **Ratificada**: 2026-08-27 | **Última enmienda**: 2026-08-27
