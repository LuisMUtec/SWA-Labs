# Feature Specification: RemoteSchooly — educación en línea para pueblos remotos

**Feature Branch**: `001-remoteschooly`

**Created**: 2026-09-02

**Status**: Draft

**Input**: Caso de Estudio #4 del curso ([`docs/LAB-04-ARQ-2026.2.md`](../../docs/LAB-04-ARQ-2026.2.md)):
distribución semanal de materiales educativos desde una central en Lima a pueblos remotos con internet
limitado, y reducción del gasto de tokens de IA en al menos 40 %.

> **Este documento es la autoridad sobre qué debe hacer el sistema** ([`D-01`](../../docs/DECISIONES.md)).
> El [backlog](../../redale/R-requerimientos/backlog.md) es su proyección al formato del profesor y es
> lo único que el [EVAL](../../evals/README.md) puntúa. La trazabilidad `FR ↔ RF` y `SC ↔ RNF` vive en
> [`insumos.md`](../../redale/R-requerimientos/insumos.md).
>
> **Los requerimientos bajan, nunca suben.** Una corrección se hace acá y se reproyecta; nunca al
> revés.

## User Scenarios & Testing *(mandatory)*

Las cuatro personas están en [`personas/`](../../personas/). Cada historia es el flujo principal de
una de ellas, y sus *Acceptance Scenarios* incluyen el **cuando sale mal**, que es lo que D1 exige
cubierto.

### User Story 1 - Nayra abre la semana sin conexión (Priority: P1)

Nayra llega el lunes a la escuela de su pueblo y necesita el material de esa semana. El equipo de la
escuela tiene un enlace que unos días anda y otros no. Ella abre el material y estudia; el equipo no
le pregunta nada a Lima en ese momento.

**Why this priority**: Es el propósito del sistema. El enunciado empieza por acá —*"se necesita que
los alumnos tengan acceso a los materiales para la semana"*— y todo lo demás existe para que esto
ocurra. Sin esta historia no hay producto.

**Independent Test**: Con una semana ya publicada y distribuida, desconectar el nodo del pueblo de la
red y comprobar que las piezas se abren y que el sistema declara la semana completa.

**Acceptance Scenarios**:

1. **Given** la semana vigente está completa en el nodo del pueblo, **When** Nayra abre cualquier
   pieza **sin conexión activa**, **Then** la pieza se abre y el sistema no emite ninguna petición a
   la central.
2. **Given** la semana vigente está en el nodo, **When** Nayra la consulta, **Then** ve qué piezas la
   componen, cuáles tiene, y a qué semana y versión corresponden.
3. **Given** la semana llegó incompleta, **When** Nayra la abre, **Then** el sistema le dice cuáles
   piezas faltan en lugar de mostrar la semana como si estuviera entera.
4. **Given** una semana nueva está llegando y todavía no está completa, **When** Nayra abre el
   material, **Then** sigue viendo la **anterior completa** y no una mezcla de las dos.
5. **Given** Nayra tiene el material abierto, **When** intenta modificarlo o borrarlo, **Then** el
   sistema lo impide.

---

### User Story 2 - Rómulo sabe el domingo si puede dictar el lunes (Priority: P2)

Rómulo dicta varios cursos en la misma escuela. Antes de que empiece la semana quiere confirmar que
el material que le toca está completo en el equipo, y si falta algo, enterarse con tiempo de hacer
algo al respecto.

**Why this priority**: Es la exigencia *"que los cursos lleguen correctamente"* vista desde quien la
verifica. Sin ella el sistema puede fallar en silencio, que es el modo de fallo que el caso tiene que
eliminar.

**Independent Test**: Retener deliberadamente una pieza de una semana y comprobar que Rómulo la ve
como faltante antes de la fecha de inicio, y que el aviso se emite.

**Acceptance Scenarios**:

1. **Given** la semana está por empezar, **When** Rómulo consulta el estado de sus cursos, **Then**
   ve por curso qué piezas componen la semana, cuáles llegaron y de qué versión son.
2. **Given** falta una pieza y la ventana de entrega venció, **When** se cumple la ventana, **Then**
   el sistema **avisa a Rómulo y al coordinador** sin que ninguno tenga que preguntar.
3. **Given** una pieza falta, **When** Rómulo la reclama, **Then** el reclamo queda registrado contra
   esa semana-curso y llega a quien puede resolverlo.
4. **Given** Rómulo dictó la semana, **When** la registra como dictada, **Then** queda constancia con
   la versión del material que efectivamente tenía.
5. **Given** la semana-curso nunca llegó, **When** Rómulo intenta registrarla como dictada, **Then**
   el sistema lo impide.
6. **Given** Rómulo tiene la semana descargada, **When** intenta editar o publicar material, **Then**
   el sistema lo impide: no es autor.

---

### User Story 3 - Marisol produce la semana dentro de su techo (Priority: P3)

Marisol arma en Lima el material de la semana de sus cursos con ayuda de la IA. Quiere saber cuánto
lleva gastado mientras trabaja, corregir sin regenerar todo, y publicar a tiempo.

**Why this priority**: Es donde se produce el gasto que el enunciado manda bajar 40 %. Cambiar su
comportamiento es lo que hace la cifra alcanzable.

**Independent Test**: Generar una semana, corregir una parte, y comprobar que el consumo imputado de
la corrección es el de la parte y no el del documento entero; y que al llegar al techo la publicación
se bloquea.

**Acceptance Scenarios**:

1. **Given** Marisol abre la semana de un curso, **When** consulta antes de generar, **Then** ve
   cuántos tokens lleva consumidos del techo de ese curso en el periodo y cuánto le queda.
2. **Given** ya generó una pieza, **When** quiere corregirla, **Then** el sistema le **exige señalar
   qué parte cambia** antes de generar una versión nueva.
3. **Given** una generación terminó, **When** se cierra, **Then** su consumo queda imputado a esa
   semana-curso y a ese periodo.
4. **Given** el consumo del curso alcanzó el techo del periodo, **When** Marisol intenta publicar,
   **Then** el sistema lo impide.
5. **Given** la semana está revisada, **When** Marisol la publica, **Then** queda **congelada**: esa
   versión ya no se edita.
6. **Given** una semana publicada tiene un error, **When** Marisol lo corrige, **Then** se publica una
   **versión nueva** y la anterior se conserva — nadie edita lo ya distribuido.
7. **Given** Marisol abre un curso que no es suyo, **When** intenta generar o publicar en él,
   **Then** el sistema lo impide.

---

### User Story 4 - Aurelio rinde cobertura y ahorro (Priority: P4)

Aurelio responde ante el gobierno por que los pueblos reciban los cursos y por que el programa baje el
gasto de IA al menos 40 %. Necesita saber qué regiones recibieron cada semana —recibieron, no se les
despachó— y poder mostrar el ahorro contra algo.

**Why this priority**: Es la exigencia del −40 % vista desde quien responde por ella, y la única que
convierte la cifra en verificable. Depende de que las tres historias anteriores estén produciendo
datos, por eso va última.

**Independent Test**: Con dos periodos de datos, pedir la rendición y comprobar que el porcentaje se
calcula por semana-curso publicada contra la línea base declarada; y que una región atrasada dispara
aviso.

**Acceptance Scenarios**:

1. **Given** el periodo está corriendo, **When** Aurelio consulta la cobertura, **Then** ve por región
   qué semana tiene vigente y cuál fue la última **confirmada por el destino**.
2. **Given** una región lleva atraso, **When** el atraso supera el umbral, **Then** el sistema avisa a
   Aurelio **mientras todavía se puede reponer**.
3. **Given** el periodo cerró, **When** Aurelio pide la rendición, **Then** obtiene el gasto de tokens
   por semana-curso publicada, la línea base, y el porcentaje de reducción.
4. **Given** Aurelio quiere ajustar el gasto, **When** fija el techo de un curso para el periodo,
   **Then** el techo rige para las publicaciones de ese curso.
5. **Given** una semana fue despachada pero ninguna región la confirmó, **When** Aurelio consulta la
   cobertura, **Then** **no** figura como entregada.
6. **Given** Aurelio consulta un curso, **When** intenta ver material no publicado o editarlo,
   **Then** el sistema lo impide.

---

### Edge Cases

Cada uno es el «cuando sale mal» de una persona. D1 no aprueba un flujo cubierto solo en su camino
feliz.

- **La semana llega a medias y nadie se entera hasta el lunes en clase** (Nayra, Rómulo). Cubierto
  por FR-013, FR-014, FR-015, FR-019.
- **Llega la versión vieja y se dicta como si fuera la de la semana** (Nayra, Rómulo). Cubierto por
  FR-011, FR-018.
- **Una corrección se publica cuando el aula ya tiene la versión anterior descargada** (Marisol ↔
  Rómulo, tensión `T3`). Cubierto por FR-005, FR-018, FR-019.
- **La transferencia se corta a la mitad y hay que empezar de nuevo** (Nayra). Cubierto por FR-012 y
  SC-006.
- **Marisol regenera diez veces el documento entero por cambiar una palabra** (Marisol, Aurelio).
  Cubierto por FR-003, FR-007, FR-009.
- **La factura llega después de gastada** (Marisol, Aurelio). Cubierto por FR-007, FR-008, FR-024.
- **«Enviado» se confunde con «llegado» y se firma un informe falso** (Aurelio). Cubierto por FR-014,
  FR-022, FR-025.
- **Una región lleva tres semanas sin material y se sabe cuando ya no se puede reponer** (Aurelio,
  Nayra). Cubierto por FR-023.
- **La semana pesa más de lo que el enlace de la región puede traer en la ventana** (Nayra, Marisol,
  tensión `T1`). Cubierto por FR-011 y SC-004.
- **Llegar a la región más lejana cuesta más de lo que el presupuesto rinde** (Aurelio ↔ Nayra,
  tensión `T4`). Ver `[CLARIFY]` en *Assumptions*.

## Requirements *(mandatory)*

### Functional Requirements

**Producción del material en la central**

- **FR-001**: El sistema MUST permitir a la autora componer la semana de un curso como un conjunto
  declarado de piezas.
- **FR-002**: El sistema MUST permitir generar piezas de material con la IA de la plataforma.
- **FR-003**: El sistema MUST exigir a la autora señalar qué parte del material cambia antes de
  generar una versión nueva de una pieza ya generada.
- **FR-004**: El sistema MUST congelar la semana al publicarla: la versión publicada no se edita.
- **FR-005**: El sistema MUST permitir corregir una semana publicada **publicando una versión nueva**,
  conservando la anterior.

**Gobierno del gasto de IA**

- **FR-006**: El sistema MUST permitir al coordinador fijar el techo de gasto de tokens por curso y
  periodo.
- **FR-007**: El sistema MUST informar a la autora cuántos tokens lleva consumidos del techo de su
  curso en el periodo y cuánto le queda.
- **FR-008**: El sistema MUST impedir publicar material de un curso cuyo consumo del periodo alcanzó
  el techo.
- **FR-009**: El sistema MUST imputar el consumo de cada generación a la semana-curso y al periodo que
  la originaron.

**Distribución hacia la región**

- **FR-010**: El sistema MUST distribuir a todas las regiones la versión publicada de la semana **sin
  volver a generarla**.
- **FR-011**: El sistema MUST declarar, para cada semana-curso, qué piezas la componen y cuánto pesa.
- **FR-012**: El sistema MUST reanudar una transferencia interrumpida desde donde se cortó, sin
  reenviar lo ya recibido.
- **FR-013**: El sistema MUST verificar en el destino que cada pieza llegó íntegra y corresponde a la
  versión publicada.
- **FR-014**: El sistema MUST dar una semana-curso por entregada **solo cuando el destino confirma
  todas sus piezas**.
- **FR-015**: El sistema MUST avisar al docente y al coordinador cuando una semana-curso no quedó
  completa en el destino al vencer su ventana de entrega.

**Consumo en el pueblo**

- **FR-016**: El sistema MUST servir el material de la semana vigente desde el nodo local **sin
  conexión activa con la central**.
- **FR-017**: El sistema MUST mostrar al alumno y al docente qué piezas componen la semana y cuáles
  están disponibles en el nodo.
- **FR-018**: El sistema MUST mostrar a qué semana y a qué versión publicada corresponde el material
  que el nodo tiene.
- **FR-019**: El sistema MUST conservar la semana vigente hasta que la siguiente esté completa en el
  nodo, sin reemplazarla parcialmente.
- **FR-020**: El sistema MUST permitir al docente registrar que dictó una semana-curso, y MUST
  impedirlo si esa semana-curso nunca se le entregó.
- **FR-021**: El sistema MUST permitir al docente reclamar una pieza faltante y MUST registrar el
  reclamo contra esa semana-curso.

**Rendición ante el mandante**

- **FR-022**: El sistema MUST mostrar por región qué semana tiene vigente y cuál fue la última
  confirmada por el destino.
- **FR-023**: El sistema MUST avisar al coordinador cuando una región acumula atraso por encima del
  umbral definido.
- **FR-024**: El sistema MUST reportar el gasto de tokens del periodo por semana-curso publicada,
  contra la línea base declarada, con el porcentaje de reducción.
- **FR-025**: El sistema MUST conservar la constancia de cada entrega confirmada: qué semana-curso,
  qué destino y cuándo.

**Identidad y permisos**

- **FR-026**: El sistema MUST restringir cada acción al rol de quien la ejerce, según los permisos
  declarados en [`personas/`](../../personas/): el alumno no modifica material, el docente no publica,
  la autora no toca cursos ajenos, el coordinador no edita material.

### Key Entities

Insumo directo del paso [`A`](../../redale/A-armar-modelo-datos/) de R.E.D.A.L.E.

- **Curso**: la unidad que se dicta. Tiene autora asignada, regiones destino y techo de gasto por
  periodo.
- **Semana-curso**: el átomo del sistema — el material de una semana de un curso. Es la unidad de
  entrega, de medición del gasto y de congelamiento.
- **Pieza**: cada componente del material de una semana-curso. Tiene tamaño y una huella que permite
  verificar su integridad en destino.
- **Versión publicada**: el estado congelado de una semana-curso. Inmutable; una corrección es una
  versión nueva.
- **Región / nodo local**: el punto del pueblo que recibe, guarda y sirve el material sin conexión.
- **Confirmación de entrega**: el hecho de que un destino tiene todas las piezas de una versión.
  Distinto del despacho.
- **Consumo de tokens**: lo gastado por una generación, imputado a una semana-curso y un periodo.
- **Techo de gasto**: el límite por curso y periodo que fija el coordinador.
- **Constancia de dictado**: el registro de que un docente dictó una semana-curso con una versión.
- **Reclamo**: una pieza que el docente declara faltante contra una semana-curso.

## Success Criteria *(mandatory)*

Medibles y agnósticos de tecnología. Son la fuente de los no funcionales del backlog, y **cada uno
lleva número** — el criterio que el profesor dictó en clase `[11:49]` y por el que objetó los no
funcionales del Caso #1.

### Measurable Outcomes

- **SC-001**: El **100 %** de las piezas de una semana-curso está verificado como íntegro y de la
  versión correcta en el nodo destino antes de la fecha de inicio de esa semana; y **cero** semanas se
  dictan con material incompleto sin que haya habido aviso previo. *(Es la exigencia «que los cursos
  lleguen correctamente» del enunciado.)*
- **SC-002**: El gasto de tokens **por semana-curso publicada** baja **≥ 40 %** respecto de la línea
  base del periodo anterior. *(Única cifra dura del enunciado; unidad y línea base fijadas en
  [`D-07`](../../docs/DECISIONES.md).)*
- **SC-003**: Abrir cualquier pieza de la semana vigente en el nodo local produce **cero** peticiones
  a la central.
- **SC-004**: Una semana-curso empaquetada pesa **≤ 80 MB**. *(Derivado del enlace supuesto — ver
  Assumptions.)*
- **SC-005**: La semana-curso queda completa y confirmada en el destino **≥ 2 días** antes de la fecha
  de inicio de esa semana.
- **SC-006**: Tras una interrupción, la transferencia retoma retransmitiendo **≤ 5 %** de lo ya
  recibido.
- **SC-007**: El aviso de semana-curso incompleta llega al docente y al coordinador dentro de las
  **24 h** de vencida la ventana de entrega.

## Assumptions

El enunciado no da cifras y `[14:08]` deja claro que la ambigüedad es deliberada. Todo número que no
salga del enunciado va marcado, con su justificación a la vista.

- **`[ASSUMPTION: enlace de 128 kbps efectivos con ~3 h útiles al día]`** — es la lectura conservadora
  de *"el internet es limitado"*. Da ≈ 172 MB/día por escuela. Con una ventana de distribución de 4
  días son ≈ 690 MB para **todos** los cursos de esa escuela; con `[ASSUMPTION: 6 cursos por escuela]`
  quedan ≈ 115 MB por semana-curso. **SC-004 fija el techo en 80 MB** para dejar margen de reintentos.
- **`[ASSUMPTION: la línea base del −40 % es el consumo por semana-curso publicada del periodo
  inmediatamente anterior]`** — normaliza: bajar el gasto total cerrando cursos no cuenta como ahorro.
  Ver [`D-07`](../../docs/DECISIONES.md).
- **`[ASSUMPTION: el periodo de presupuesto es el mes]`** — es la granularidad con la que Aurelio
  rinde.
- **`[ASSUMPTION: la ventana de entrega abre cuando la semana se publica y vence 2 días antes del
  inicio de clases]`** — sostiene SC-005 y el aviso de FR-015.
- **`[ASSUMPTION: el umbral de atraso de una región es 1 semana-curso sin confirmar]`** — sostiene
  FR-023. Se eligió el mínimo que todavía se puede reponer.
- **`[ASSUMPTION: el nodo local conserva la semana vigente y la anterior]`** — sostiene FR-019. Ver
  `P-02` en [`DECISIONES.md`](../../docs/DECISIONES.md).
- **`[CLARIFY: qué pasa cuando el presupuesto no alcanza para llegar a todas las regiones — ¿se
  prioriza alguna, se degrada el material, o se reprograma?]`** — es la tensión `T4` y el enunciado no
  la decide. Está fuera de alcance del gate, pero el paso `E` la va a necesitar.
- **`[CLARIFY: si una región no recibió la semana y ya es lunes, ¿se dicta con la anterior o se
  reprograma?]`** — `P-01`. El backlog cubre el aviso (FR-015) y la conservación de la anterior
  (FR-019); qué se hace con la clase es decisión pedagógica, no del sistema.

## Out of Scope

Lo que el enunciado excluye con todas sus letras. **No se gastan requerimientos acá**, y
[`evals/README.md`](../../evals/README.md) avisa que un ítem de este grupo no suma en D3:

- Asegurar 100 % de disponibilidad. *(«pero sí que los cursos lleguen correctamente» — eso sí está,
  en SC-001.)*
- Mecanismos de confiabilidad / reliability.
- El escalamiento por tramos de carga — el material del curso lo marca como «esto no lo usaremos aún».
