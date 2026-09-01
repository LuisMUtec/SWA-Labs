# SWA — Caso de Estudio #3: SendIt

Arquitectura de Software — UTEC 2026-II.
Diseño de la arquitectura de un servicio de **remesas internacionales**, por el método
[R.E.D.A.L.E.](redale/README.md)

## Contexto

Una remesa no es una transferencia. Entre que alguien paga en un país y alguien cuenta billetes en
otro, el dinero cruza dos jurisdicciones con dos reguladores, cambia de moneda a una tasa que se
mueve mientras el envío viaja, y termina en efectivo en la mano de una persona que no tiene cuenta
bancaria ni teléfono con datos. **El último tramo no tiene pantalla:** lo ejecuta un agente de una
red de terceros, con su propio registro contable, sobre el que este diseño no manda.

Ahí se cruzan las dos exigencias que el enunciado nombra por su nombre. **Seguridad:** la empresa
responde por no mover dinero de quien no debe hacia quien no debe, y un control que corre después de
aceptar el dinero ya no detiene nada —revierte—, y revertir cruza esa frontera. **Consistencia de
datos:** cuando el registro propio dice «retenido» y el del pagador dice «disponible para cobro», la
misma operación afirma dos hechos incompatibles sobre el mismo dinero, y ninguno de los dos sistemas
está en condiciones de decidir cuál es verdad.

El problema, entonces, no es mover un saldo. Es sostener una promesa —tantos soles, tal día— a
través de una frontera donde el sistema deja de mandar antes de que la promesa se cumpla.

| | |
|---|---|
| **Dificultad** | Easy Peazy |
| **Duración estimada** | 4 h |
| **Puntaje** | 20 ptos |
| **Vence** | 2026-08-28 23:59 — subida de archivo a Canvas |

Enunciado vigente: [`docs/LAB-03-ARQ-2026.2.md`](docs/LAB-03-ARQ-2026.2.md)

## Entregables

| Entregable | Criterio |
|---|---|
| **EVAL** con resultado de requerimientos | **≥ 8/10**. Puntúa el backlog del paso `R`, y nada más |
| Todos los entregables de **R.E.D.A.L.E.** | Los seis pasos, **mostrando claramente las iteraciones del diseño** |

**Restricción del enunciado:** los requerimientos se muestran en formato backlog, con un título
claro y entendible y **sin descripción**. No es una comodidad de formato: decide qué puede evaluar
el EVAL, porque un título es todo lo que un agente de persona va a tener delante. Por eso
[`evals/README.md`](evals/README.md) fija tres pruebas para saber cuándo un título *cubre* un paso
de un flujo, y qué se hace con un título comodín.

## El método

| Paso | Nombre | Salida | Dónde |
|---|---|---|---|
| **R** | Requerimientos | El backlog, funcionales y no funcionales | [`redale/R-requerimientos/backlog.md`](redale/R-requerimientos/backlog.md) |
| **E** | Estimar | Servidores, almacenamiento y ancho de banda | [`redale/E-estimar/`](redale/E-estimar/README.md) |
| **D** | Diseñar el servicio | Arquitectura, persistencia y diseño de la API | [`redale/D-disenar-servicio/`](redale/D-disenar-servicio/README.md) |
| **A** | Armar el modelo de datos | Tablas, campos y opciones de almacenamiento | [`redale/A-armar-modelo-datos/`](redale/A-armar-modelo-datos/README.md) |
| **L** | Listar los componentes | El diagrama de la arquitectura, **iteración por iteración** | [`redale/L-listar-componentes/`](redale/L-listar-componentes/README.md) |
| **E** | Escalar | Qué cambia cuando la carga sube, por tramos | [`redale/E-escalar/`](redale/E-escalar/README.md) |

**El orden importa: cada paso consume la salida del anterior.** Una estimación sin requerimientos no
tiene contra qué estimar, y un diagrama sin modelo de datos dibuja cajas que nadie llenó. La
consecuencia incómoda es la simétrica: corregir `R` deja a `E`, `D`, `A` y `L` afirmando lo viejo,
y esa propagación es el modo de falla dominante del proyecto hermano. Cada paso declara en su README
qué consume y qué queda inválido si el anterior cambia; el detalle del método está en
[`redale/README.md`](redale/README.md).

El segundo `E` aparece aunque el material del curso lo marque como *«esto no lo usaremos aún»* — el
enunciado pide **todos** los entregables del framework. La tensión y cómo se resuelve están en
[`docs/DECISIONES.md`](docs/DECISIONES.md) (D-03).

## El harness

R.E.D.A.L.E. dice qué producir; no dice quién sostiene la disciplina mientras se produce. Eso lo
aporta [Spec Kit](https://github.com/github/spec-kit), heredado del
[Caso #2](https://github.com/LuisMUtec/SWA-LAB02-Lease) e instalado acá con la misma forma: las
plantillas y los scripts en [`.specify/`](.specify/), las skills en `.claude/skills/`.

**Spec Kit no desplaza al backlog.** El enunciado fija el formato de los requerimientos y la
constitución lo vuelve vinculante: el backlog es el único artefacto con autoridad y el único
puntuado. Y conviene decir el saldo sin adornarlo — **de las diez skills instaladas, corre una**:

| Skill | Qué exige para correr | Estado |
|---|---|---|
| `/speckit-constitution` | Nada. Opera sobre [`.specify/memory/constitution.md`](.specify/memory/constitution.md) | **En uso** — v1.0.0 escrita |
| `/speckit-clarify` | Un `specs/<n>/spec.md` | Inerte |
| `/speckit-checklist` | Un `specs/<n>/plan.md` | Inerte |
| `/speckit-analyze` | `spec.md` + `plan.md` + `tasks.md` | Inerte |
| `/speckit-specify` · `/speckit-plan` · `/speckit-tasks` · `/speckit-implement` · `/speckit-converge` · `/speckit-taskstoissues` | Producen specs, planes, tareas y código, y este caso no entrega código | Inertes |

Las nueve inertes abortan en su primer paso, contra
`.specify/scripts/bash/check-prerequisites.sh`. **Lo que el harness aporta de verdad es la altitud
que faltaba** —la constitución, que antes no existía en ningún archivo— y la estructura compartida
con el Caso #2. Por qué se instala igual, y por qué no se despiertan las nueve inventando un
`specs/`, está en [D-08](docs/DECISIONES.md).

## Las personas y el usuario modelo

| Persona | Rol en la remesa | Qué ancla |
|---|---|---|
| **[Rosa Quispe](personas/Rosa.MD)** — *usuario modelo* | Remitente en Estados Unidos | Que el envío llegue por el monto y en la fecha prometidos |
| [Elena Quispe](personas/Elena.MD) | Destinataria en Huanta, cobra en efectivo | Que el último tramo, el que no tiene pantalla, también cierre |
| [Kevin Ramos](personas/Operario.MD) | Operario de la ventanilla de un agente | La **seguridad** del enunciado: es el vector, no el guardián — y la operación cortada que pone a prueba la **consistencia** |

**El usuario modelo es Rosa:** ella decide usar SendIt o abandonarlo, ella paga, y es la única de
las tres que elige libremente —Elena recibe por donde Rosa mandó y Kevin atiende el mostrador—. Elegirla no la vuelve la única usuaria, porque su problema no se resuelve dentro de su
pantalla: la promesa que ella necesita la cumple o la rompe Elena en la bodega de Huanta, y la
sostiene o la pierde Kevin en el mostrador.

Las tres se contradicen entre sí en **siete tensiones** (T1–T7) que el backlog tiene que decidir, no
esquivar. La séptima —el código perdido— no se enunció al principio: **la encontró el EVAL**, después
de que dos rondas la revirtieran en direcciones opuestas sin nombrarla ([D-10](docs/DECISIONES.md)). Están enunciadas, con su lado y su costo, en [`personas/README.md`](personas/README.md).

## Dónde vive cada cosa

Un mismo tema puede aparecer a más de una altitud sin duplicarse, mientras cada altitud afirme algo
distinto. **Cada afirmación ocurre una sola vez, en su altitud.**

| Altitud | Documento | Afirma |
|---|---|---|
| Gobierno | [`.specify/memory/constitution.md`](.specify/memory/constitution.md) | Por qué existe el proyecto y cómo se juzga el trabajo. Prevalece: donde un documento aguas abajo la contradiga, el equivocado es el documento |
| Enunciado | [`docs/LAB-03-ARQ-2026.2.md`](docs/LAB-03-ARQ-2026.2.md) | Qué pidió el curso, con sus hints, restricciones y metadatos de entrega. Se transcribe, no se interpreta |
| Método | [`redale/README.md`](redale/README.md) | Qué pregunta cada paso de R.E.D.A.L.E. y qué entrega. Vale para cualquier caso, no solo SendIt |
| Precedente | [`docs/EJEMPLO-CLASE-TOP-DOWN.md`](docs/EJEMPLO-CLASE-TOP-DOWN.md) | Qué significa «iteraciones del diseño», leído del excalidraw de clase. Aporta el método, no el contenido: el caso del ejemplo es Leasing |
| Decisiones | [`docs/DECISIONES.md`](docs/DECISIONES.md) | Qué se decidió, entre qué opciones y qué cuesta. Y qué **no** se puede decidir todavía |
| Personas | [`personas/`](personas/README.md) | Quién es cada persona, qué necesita, qué la frustra y qué nunca debe poder hacer. **Nunca qué hace el sistema** |
| **R** — el backlog | [`redale/R-requerimientos/backlog.md`](redale/R-requerimientos/backlog.md) | Qué debe hacer el sistema. Única fuente de verdad, y **único artefacto puntuado** |
| **R** — insumos | [`redale/R-requerimientos/insumos.md`](redale/R-requerimientos/insumos.md) | El razonamiento del que saldrán los títulos. **No es el entregable y no se puntúa** |
| Dominio | [`business-rules.md`](business-rules.md) | Las reglas que obedece el negocio, `BR-nn`. Sobreviven a cualquier backlog |
| **E** — estimar | [`redale/E-estimar/`](redale/E-estimar/README.md) | Cuántos servidores, cuánto almacenamiento y cuánto ancho de banda, con sus supuestos declarados |
| **D** — diseñar el servicio | [`redale/D-disenar-servicio/`](redale/D-disenar-servicio/README.md) | Qué arquitectura, qué persistencia, qué API — y el **mecanismo** de seguridad que el backlog solo puede exigir como garantía |
| **A** — armar el modelo de datos | [`redale/A-armar-modelo-datos/`](redale/A-armar-modelo-datos/README.md) | Qué entidades, qué campos y dónde vive cada uno |
| **L** — listar los componentes | [`redale/L-listar-componentes/`](redale/L-listar-componentes/README.md) | El diagrama, una sección por iteración, y la trazabilidad *ítem del backlog → iteración que lo cubre* |
| **E** — escalar | [`redale/E-escalar/`](redale/E-escalar/README.md) | Qué cambia y dónde aparece el cuello de botella al subir la carga, por tramos |
| Bitácora | [`redale/ITERACIONES.md`](redale/ITERACIONES.md) | Qué cambió, en qué paso, qué lo forzó y qué quedó afirmando lo viejo aguas abajo |
| EVAL — aparato | [`evals/README.md`](evals/README.md) | Cómo se puntúa el backlog: rúbrica, protocolo, techos y las reglas de redacción que exige |
| EVAL — corridas | [`evals/iterations/`](evals/iterations/) · [`evals/HISTORY.md`](evals/HISTORY.md) | Qué puntaje sacó qué SHA, y qué hallazgo produjo cada deducción |
| EVAL — jueces | [`.claude/agents/`](.claude/agents/) | Cómo juzga cada persona un backlog. Un agente por persona, derivado de ella; no introduce necesidades nuevas |

## EVAL

| Dim | Pts | Qué mide | Juzga |
|---|---|---|---|
| **D1** Satisfacción de las personas | 3 | El flujo de Rosa, Elena y Kevin corre de extremo a extremo en el backlog, **incluido cuando sale mal**. 1 pt por persona, **solo deducciones** | Los 3 agentes de persona |
| **D2** Ajuste al problema | 3 | Ataca la remesa internacional —frontera, moneda, efectivo sin banco— y no un «enviar plata» genérico. 1 pt por rasgo | Agregador |
| **D3** Cobertura de seguridad y consistencia | 2 | Las dos exigencias que el enunciado nombra, con medida o invariante y no como adjetivo. 1 pt cada una | Agregador |
| **D4** Coherencia del backlog | 2 | Sin huérfanos ni duplicados encubiertos, títulos atómicos y entendibles sin descripción, las siete tensiones decididas, prioridad asignada | Agregador |

**Gate: ≥ 8/10.** Se pueden perder dos puntos, no más. Un puntaje por debajo no baja la vara: se
corrige el backlog y se vuelve a evaluar, en un SHA nuevo.

**Regla de asimetría:** un agente de persona solo puede **restar** de D1, nunca sumar — lee su
persona y el backlog, así que ve un ángulo y no el conjunto, y si pudiera sumar, D1 mediría la
generosidad del agente en lugar de la calidad del backlog. Si ninguno objeta, D1 vale 3: el máximo
no se gana, se conserva.

**Solo se puntúa el paso `R`.** El enunciado pide el EVAL *con resultado de requerimientos*, y eso
fija el alcance: una estimación de servidores o un diagrama de componentes no se juzgan contra esta
rúbrica y no suman ni restan en ninguna dimensión. `E`, `D`, `A`, `L` y `E` son entregable exigido,
no puntaje.

Lo que impide que diverjan del backlog no es puntuarlos, sino **una regla de dirección: los
requerimientos bajan, nunca suben.** Ningún paso aguas abajo puede introducir un comportamiento que
el backlog no declare. Si `D` diseña un endpoint que responde algo que ningún título exige, o `A`
guarda un campo que ningún título obliga a conocer, el defecto **es del backlog**, se cobra en D4
como *decisión sin requerimiento*, y la corrección va arriba. La regla se paga sola: convierte
cualquier invención aguas abajo en una deducción de la única dimensión que sí se puntúa.

## Las dos clases de iteración

El enunciado exige mostrar las iteraciones y no dice de qué. Son dos cosas distintas y se confunden
con facilidad:

| | **Iteración del diseño** | **Iteración del EVAL** |
|---|---|---|
| Qué itera | El diagrama de componentes del paso `L` | El backlog del paso `R` |
| Qué la fuerza | Un ítem del backlog que el dibujo anterior no explica | Un puntaje por debajo del gate |
| Cómo se ve | El mismo diagrama, más abierto, y el ítem cubierto marcándose `DONE` | Un hallazgo con su cita, un título corregido y un SHA nuevo |
| De dónde sale | El [ejemplo de clase](docs/EJEMPLO-CLASE-TOP-DOWN.md) — es la que el profesor mostró | El aparato heredado del Caso #2 |
| Dónde vive el detalle | [`redale/L-listar-componentes/`](redale/L-listar-componentes/README.md) | [`evals/iterations/`](evals/iterations/) |

Ambas se registran en la misma bitácora —[`redale/ITERACIONES.md`](redale/ITERACIONES.md), en dos
tablas separadas—, y ahí se ve por qué hay que distinguirlas: **una fuerza a la otra.** Una iteración del EVAL cambia el
backlog, y cambiar el backlog invalida lo que `E`, `D`, `A` y `L` afirmaban — lo que obliga a una
iteración del diseño que no venía de ningún dibujo. La bitácora registra esa propagación aunque el
rebarrido no encuentre nada: un rebarrido vacío es un resultado, uno que nadie corrió no lo es, y
son indistinguibles si no se anota.

## Estado

**Los seis pasos llenos, diecinueve rondas de EVAL, y el gate alcanzado: 8,2669 / 10 sobre un umbral
de 8, con margen.** Lo que está:

- El **backlog**, que es el único artefacto puntuado: **236 ítems — 216 funcionales y 20 no
  funcionales**, cada uno con su persona, su regla `BR-nn` y su prioridad.
- Las **tres personas** —[Rosa](personas/Rosa.MD), [Elena](personas/Elena.MD),
  [Kevin](personas/Operario.MD)— en `status: proto`, el usuario modelo designado y las **siete
  tensiones**, cero de ellas sin decidir.
- Las **diecisiete reglas de negocio**, `BR-01` a `BR-17` en [`business-rules.md`](business-rules.md).
- **Diecinueve corridas del EVAL**, de **3,5 a 8,27**, en [`evals/iterations/`](evals/iterations/) y
  resumidas en [`HISTORY.md`](evals/HISTORY.md). Cada una diagnostica cómo *mutó* el modo de falla, no
  solo qué falló.
- Los **cinco pasos aguas abajo llenos y repropagados sobre los 236 ítems**: `E` con cifras
  calibradas —13 servidores, 3,3 TB, 1,7 Mbit/s—, `D` con su arquitectura, su persistencia y sus 48
  endpoints, `A` con 37 entidades en 10 bases, `L` con **tres iteraciones del diagrama** y
  trazabilidad **236 / 236**, y `E-escalar` por tramos con sus seis cuellos de botella.
- La **bitácora** de [`redale/ITERACIONES.md`](redale/ITERACIONES.md), con las dos tablas llenas.
- **Diez decisiones** registradas (`D-01` a `D-10`) y **ninguna pendiente**: las cinco que había se
  cerraron y [`docs/DECISIONES.md`](docs/DECISIONES.md) dice dónde se decidió cada una.
- El **harness de Spec Kit** y la **constitución**, ahora en v1.1.0.
- Los **dos documentos de entrega**, los dos regenerados sobre el estado vigente:
  [`docs/RESUMEN.md`](docs/RESUMEN.md) —el dossier de ocho láminas, una por paso— y
  [`docs/ENTREGA.md`](docs/ENTREGA.md), el documento completo con el backlog en su anexo.

Lo que **no** está, y hay que decirlo así:

- **La serie de puntajes está partida en dos.** `D4` se enmendó en la ronda 08 para puntuar por
  densidad ([D-09](docs/DECISIONES.md)), de modo que **las corridas 01 a 07 no son comparables con las
  siguientes**. Ninguna lectura de la tendencia puede cruzar esa ronda.
- **`D1` nunca pasó de 1,5 sobre 3.** Nueve rondas cerrando las reservas nombradas y nueve veces la
  misma lectura: cada persona encuentra una reserva nueva de la clase que se le acaba de cerrar. El
  punto y medio está disponible en teoría y es 0 de 9 en la práctica.
- **La enmienda a `D2` quedó redactada y sin aplicar**
  ([`evals/ENMIENDA-PROPUESTA-D4.md`](evals/ENMIENDA-PROPUESTA-D4.md)): satisface las condiciones,
  pero aplicarla en la ronda que voltea el veredicto es indistinguible de endurecer por su efecto.
- Las personas siguen en `status: proto`: cada afirmación inventada está marcada
  `[ASSUMPTION: …]` y ninguna se validó contra una persona real.

## Proyectos hermanos

| Caso | Repo | Qué es | Qué se heredó |
|---|---|---|---|
| **#1** | [SWA-LAB01-UCI-Essalud](https://github.com/LuisMUtec/SWA-LAB01-UCI-Essalud) | Gestión de UCI para Essalud: turnos, rotación de médicos y disponibilidad del diagnóstico | El aparato de evaluación por **agentes de persona** —un agente por persona, derivado de ella, que juzga en primera persona— y las **convenciones de redacción**: afirmación atómica y verificable, sin mecanismo, sin texto visible, ambigüedad marcada y nunca rellenada en silencio |
| **#2** | [SWA-LAB02-Lease](https://github.com/LuisMUtec/SWA-LAB02-Lease) | Lea$e, leasing de maquinaria en Perú: financiar el equipo de un proyecto que se cobra al final | La **rúbrica** de cuatro dimensiones sobre 10 con gate en 8, la **regla de asimetría**, la **plantilla de personas** ([`_TEMPLATE.MD`](personas/_TEMPLATE.MD)) y la lección más cara de sus nueve rondas: **el modo de falla dominante es la propagación** —se corrige un requisito y queda otro documento afirmando lo viejo, hasta que el defecto reaparece dos iteraciones después disfrazado de otra cosa |

La rúbrica no se heredó intacta: D3 medía criterios de aceptación demostrables, y acá el artefacto
puntuado es un backlog de solo títulos. El cambio, y lo que cuesta, están en
[`docs/DECISIONES.md`](docs/DECISIONES.md) (D-04).
