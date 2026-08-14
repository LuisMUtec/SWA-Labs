# Convenciones de redacción de los entregables

Estas convenciones rigen sobre todo markdown del repositorio. Fijan qué afirma cada documento, con
qué forma se enuncia un requerimiento y cómo se verifica lo escrito.

El criterio de fondo es uno: **un criterio incumplido se corrige moviendo la afirmación a su dueño,
no borrándola.** Toda afirmación tiene un dueño; lo que no encaja en un documento encaja en otro.

Cada sección sirve a una dimensión de la rúbrica de [`Eval-Spec.MD`](../Spec/Eval-Spec.MD):

| Sección | Dimensión que sirve |
|---|---|
| 1. Fronteras entre documentos | D5 Consistencia y tensiones |
| 2. Reglas transversales | D3 Verificabilidad y forma, D5 Consistencia y tensiones |
| 3. Personas | D1 Satisfacción de las personas |
| 4. Agentes de persona | D1 Satisfacción de las personas |
| 5. Requerimientos funcionales | D2 Problemas críticos, D3 Verificabilidad y forma |
| 6. Criterios de aceptación | D3 Verificabilidad y forma |
| 7. Requerimientos no funcionales | — fuera del alcance de la evaluación |
| 8. Glosario | D5 Consistencia y tensiones |
| 9. Trazabilidad y prioridad | D4 Trazabilidad, D6 Priorización |

La rúbrica puntúa únicamente requerimientos funcionales. `ReqNoFunc.MD` es entregable exigido por el
enunciado y se rige por la sección 7, pero ninguna de sus afirmaciones suma ni resta en el porcentaje.

---

## 1. Fronteras entre documentos

| Documento | Afirma | No afirma |
|---|---|---|
| `README.md` | El problema, los clientes y usuarios, los supuestos sobre el enunciado, el prompt de evaluación | Requerimientos; detalle de las personas |
| `Personas/*.MD` | Quién es una persona, qué necesita, qué la frustra, cuándo considera exitoso el sistema | Qué hace el sistema |
| `Agents/*.MD` | Cómo esa persona juzga un requerimiento | Requerimientos nuevos |
| `Requirements/ReqFunc.MD` | Qué comportamiento observable debe exhibir el sistema | Cómo se implementa; atributos de calidad |
| `Requirements/ReqNoFunc.MD` | Bajo qué condiciones y con qué medida debe responder el sistema | Comportamiento funcional; tecnología |
| `Spec/Eval-Spec.MD` | Cómo se puntúa la calidad del conjunto | Requerimientos ni personas |

**Requerimiento frente a decisión de arquitectura.** El enunciado del caso induce a resolver —cifras
de escalamiento, notificaciones push, disponibilidad de 99,9 %—, pero los entregables son
requerimientos. Ningún RF ni RNF nombra un mecanismo, un producto ni una topología: enuncia la
garantía que el sistema ofrece. La decisión técnica desplazada se registra en `docs/`, no se suprime.

## 2. Reglas transversales

Aplican a todo documento del repositorio.

- **Cada afirmación vive una sola vez, en su dueño.** Dos copias de una regla se corrigen por
  separado hasta contradecirse.
- **Cada afirmación es atómica:** una cosa verdadera o falsa, verificable y modificable por separado.
- **Cada afirmación es necesaria.** Si al suprimirla no falta nada, sobra.
- **Cada afirmación es verificable.** «Rápido», «intuitivo» y «confiable» se sustituyen por su
  medida. Un enunciado que nadie puede declarar cumplido o incumplido no es un requerimiento.
- **Coherencia interna.** Ninguna sección contradice a otra. Un RF no concede lo que un RNF restringe.
- **Contratos cerrados.** Se enuncia lo que el sistema produce —«exactamente X, Y, Z»—, no la lista
  de lo que no hace. Un contrato abierto no es verificable.
- **Nada se nombra por su texto visible.** La etiqueta de un botón, el nombre de una pantalla o el
  asunto de una notificación cambian sin que cambie ningún requerimiento. Se nombra la intención.
- **La ambigüedad se marca, no se rellena.** El enunciado del caso deja cuestiones abiertas —qué
  cuenta como hospital en la meta de 10 M, qué proporción está activa en el cambio de turno—. Lo
  indefinido se anota con uno de dos marcadores, nunca se resuelve en silencio:
  - `[ACLARAR: pregunta concreta]` cuando la respuesta condiciona el requerimiento.
  - `[SUPUESTO: enunciado]` cuando el trabajo continúa bajo una hipótesis declarada.
- **Sin referencias portantes.** Un puntero al final —`(RF-DIA-02)`— es admisible. Una frase que no
  se entiende sin ir a buscar lo que referencia, no.
- **Cero lápidas.** Lo descartado no se conserva tachado ni comentado dentro de un requerimiento. Su
  lector es `git log`.
- **Sin estado ni tracking.** Responsable, avance y ramas pertenecen al README del equipo y a los
  commits. Congelados dentro de un requerimiento, se pudren.

## 3. Personas

- **La persona opera el sistema.** Quien decide y financia es cliente, y vive en la tabla de clientes
  del `README.md`. Quien se ve afectado sin operarlo es usuario indirecto. Solo el usuario directo se
  modela como persona.
- **Cada persona existe porque el sistema le falla de una forma que a las demás no.** Dos personas
  que rompen el sistema por el mismo punto son una sola; la duplicación infla D1 sin cubrir nada.
- **Las tareas críticas se enuncian como acciones observables**, con frecuencia y criticidad. Son la
  columna contra la que `Eval-Spec` construye la matriz de cobertura: una tarea vaga no se puede
  declarar cubierta.
- **Los criterios de éxito se escriben de modo que un RF pueda satisfacerlos.** «Que el sistema sea
  confiable» no es un criterio; «que el diagnóstico del turno saliente esté disponible antes de
  recibir la primera cama» sí.

## 4. Agentes de persona

- **El agente habla en primera persona.** Es la única excepción admitida al registro impersonal de la
  sección 10, y es deliberada: el agente evalúa desde la perspectiva de su persona.
- **El agente no inventa capacidades.** Juzga el requerimiento tal como está enunciado.
- **La ambigüedad se declara como ambigüedad**, no se interpreta en el sentido favorable. Un
  requerimiento que el agente marca ambiguo resta en D1 y esa es su función.
- **Un agente por persona, derivado de ella.** El agente no introduce necesidades que su persona no
  documenta; si aparece una, se agrega primero a la persona.

## 5. Requerimientos funcionales

Todo RF adopta uno de los patrones **EARS** y lleva el auxiliar **DEBE**:

| Patrón | Forma | Corresponde cuando |
|---|---|---|
| Ubicuo | El sistema DEBE ‹respuesta› | Vale siempre, sin disparador ni condición |
| De estado | MIENTRAS ‹estado›, el sistema DEBE ‹respuesta› | Vale mientras dura un estado |
| De evento | CUANDO ‹disparador›, el sistema DEBE ‹respuesta› | Se activa ante un disparador |
| De opción | DONDE ‹variante presente›, el sistema DEBE ‹respuesta› | Solo aplica si la variante existe |
| De borde | SI ‹condición no deseada›, ENTONCES el sistema DEBE ‹respuesta› | Error, dato faltante o límite |
| Complejo | MIENTRAS ‹estado›, CUANDO ‹disparador›, el sistema DEBE ‹respuesta› | Estado y disparador a la vez |

- **Un patrón y una respuesta por RF.** Dos respuestas, o una condición pegada con punto y coma, son
  dos requerimientos.
- **El sujeto del DEBE es el sistema.** El actor aparece en el disparador —«CUANDO el médico saliente
  confirma la entrega de turno…»—, pero quien debe es siempre el sistema. Un requerimiento cuyo
  sujeto es una persona describe el proceso hospitalario y no el producto: se verifica contra quien
  trabaja en vez de contra lo construido, y nunca puede darse por cumplido.

  > **Antes** — El médico saliente DEBE registrar su diagnóstico antes de terminar el turno.
  >
  > **Después** — SI un turno finaliza sin diagnóstico registrado, ENTONCES el sistema DEBE
  > bloquear el cierre del turno y notificar al coordinador de la unidad.

- **El RF describe comportamiento observable, en lenguaje llano.** Nada de interfaz, navegación ni
  estructura de datos. «Aparece en la lista» y «lo lleva a la pantalla de camas» son experiencia de
  uso: su lugar es la persona o el criterio de aceptación. Los nombres de campos y entidades van al
  glosario.
- **El requerimiento enuncia la regla, no el mecanismo que la cumple.** «El sistema DEBE enviar una
  notificación push» condiciona sobre la solución; «el sistema DEBE alcanzar al médico de guardia
  localizable y registrar el acuse» condiciona sobre la garantía, y cubre las vías que el push no
  agota.
- **El RF no acuña terminología.** Si para enunciarlo se inventa un término, se reformula con la
  palabra que ya nombra la cosa, y esa palabra vive en el glosario.
- **Un borde con respuesta definida es un RF de borde.** La indisponibilidad del médico de guardia no
  es una pregunta abierta: es un `SI … ENTONCES`.

## 6. Criterios de aceptación

El criterio demuestra el comportamiento; no lo reespecifica.

- **Un solo par Cuando/Entonces por criterio.** Dos pares son dos criterios.
- **El Dado toma el estado; el Cuando, el disparador.** Un Cuando que dice «el sistema evalúa el
  caso» nombra un mecanismo y deja el criterio sin momento observable.
- **Sin pasos conjuntivos.** Un paso que une dos acciones con «y» esconde dos pasos.
- **Actor explícito, en tercera persona.** «La enfermera de turno registra…», no «registro…».
- **Sin detalle de interfaz.** Un guion de pulsaciones deja de valer cuando cambia el diseño; la
  intención, no.
- **Independiente y determinista.** El criterio no depende del estado que dejó otro.
- **Demuestra, no reespecifica.** Referencia el contrato del RF en lugar de recopiarlo.

## 7. Requerimientos no funcionales

Un valor objetivo sin condiciones no es verificable: «10 M hospitales» no dice qué ocurre ni bajo qué
circunstancias. Todo RNF se enuncia como **escenario de atributo de calidad**, en seis partes:

| Parte | Qué fija |
|---|---|
| Fuente | Quién o qué origina el estímulo |
| Estímulo | El evento que llega al sistema |
| Artefacto | La parte del sistema estimulada |
| Entorno | El estado del sistema cuando llega el estímulo, incluida la carga |
| Respuesta | Lo que el sistema hace en consecuencia |
| Medida | El umbral con el que se declara cumplida la respuesta |

> **RNF-PER-01** — *Fuente:* médico del turno entrante. *Estímulo:* solicita el diagnóstico del turno
> saliente. *Artefacto:* aplicación cliente y servicio de diagnósticos. *Entorno:* operación normal,
> 10 M hospitales registrados, `[SUPUESTO: 2 % concurrentes en la ventana de cambio de turno]`.
> *Respuesta:* se entrega el diagnóstico vigente. *Medida:* p95 inferior a 1 s.

- **La medida es un número con unidad y percentil**, no un adjetivo. Un RNF sin medida no es
  verificable, aunque la rúbrica no lo puntúe: la sección 7 rige por sí misma.
- **La medida es agnóstica de la tecnología.** Nombra el resultado, no el componente que lo produce.
- **Invariante antes que porcentaje.** «Ningún diagnóstico confirmado se pierde ante la caída de un
  nodo» no depende del conjunto de pruebas que alguien haya armado; «el 100 % de los casos de prueba
  pasa» sí.
- **El entorno declara la carga.** Las cifras de escalamiento del enunciado son entorno, no
  requerimientos por sí solas.

## 8. Glosario

El glosario es el modelo conceptual del dominio: qué denota cada término, sus atributos de negocio y
sus relaciones. Fija el vocabulario que RF, RNF, personas y agentes usan sin variación.

- **Define, no regula.** Dice qué es una entrega de turno y con qué se relaciona; no dice cuándo debe
  bloquearse. Eso es un RF.
- **Modelo conceptual, no de implementación.** Cardinalidad e identidad sí —«un turno pertenece a
  exactamente una unidad», «un episodio agrupa los diagnósticos de una estancia»—; tablas, columnas y
  claves, no.
- **Se referencia en un solo sentido.** El cuerpo apunta al glosario; el glosario no apunta a ningún
  RF ni RNF. Es la capa que todo lo demás referencia.

## 9. Trazabilidad y prioridad

- **Ningún requerimiento es huérfano.** Todo RF declara la persona que lo motiva y el problema crítico
  al que responde. Un RF sin trazas resta en D4 aunque esté bien escrito. Los RNF trazan al enunciado
  del caso como origen: ninguna persona los motiva, porque las cuatro modeladas son clínicas y los
  atributos de calidad no se juzgan desde su satisfacción.
- **Ninguna persona queda sin cobertura.** Cada tarea crítica de cada persona traza a al menos un RF.
  La matriz de trazabilidad se mantiene al día con el cuerpo del documento; una matriz desfasada es
  una contradicción interna.
- **P1, P2 y P3 tienen dueño explícito.** Cada problema crítico del enunciado traza a al menos un RF.
- **MUST se reserva.** Es MUST el requerimiento cuya ausencia deja sin resolver un problema crítico o
  deja a una persona sin su tarea crítica. Todo lo demás es SHOULD o COULD. Una lista donde todo es
  MUST no está priorizada y resta en D6.

## 10. Estilo

- **El documento registra el estado vigente, no cómo se llegó a él.** Sin fechas de decisión, sin
  cronología de la discusión, sin recomendaciones superadas conservadas tachadas. El historial está
  en git.
- **Registro formal e impersonal.** Se enuncian proposiciones; no se conversa con el lector. «Se
  adopta X porque…», no «elegimos X porque…». Sin preguntas retóricas ni apelaciones al lector.
- **Excepción:** `Personas/` y `Agents/` son narrativos y en primera persona por diseño. El resto del
  repositorio se rige por esta sección.
- **El registro formal no autoriza a perder precisión.** Cifras con su fuente; el fundamento y no
  solo la decisión; los costos aceptados, enunciados.

## 11. Verificación

Revisión documento por documento. Cada hallazgo se anota con el identificador afectado —`RF-DIA-02`,
`RNF-ESC-03`— y su destino. Corregido, se vuelve a recorrer: mover una afirmación de documento suele
romper la coherencia de otro.

```
- [ ] README: problema, clientes, usuarios y supuestos; ningún requerimiento
- [ ] Personas: operan el sistema; una por modo de falla; tareas críticas observables
- [ ] Agents: derivan de su persona; declaran la ambigüedad en vez de interpretarla
- [ ] RF: un patrón EARS y una respuesta por requerimiento; el sujeto del DEBE es el sistema;
      la regla y no el mecanismo; sin interfaz, sin tecnología, sin terminología acuñada
- [ ] Criterios de aceptación: un par Cuando/Entonces; actor en tercera persona; sin interfaz
- [ ] RNF: seis partes del escenario; medida con unidad y percentil; entorno con la carga declarada
- [ ] Glosario: define sin regular; sin punteros hacia RF ni RNF
- [ ] Trazabilidad: ningún huérfano; toda tarea crítica cubierta; P1, P2 y P3 con dueño; MUST reservado
- [ ] Transversales: necesario, verificable, sin ecos, sin lápidas, contratos cerrados
- [ ] Estilo: sin historial en el cuerpo; registro impersonal fuera de Personas y Agents
```

Cuatro comprobaciones son mecánicas y se ejecutan desde la raíz del repositorio:

```
grep -nE "^\*\*Enunciado:\*\*" Requirements/ReqFunc.MD | grep -v "DEBE"
grep -nEi "el médico DEBE|la enfermera DEBE|el coordinador DEBE|el hospital DEBE|el equipo DEBE" Requirements/*.MD
grep -nEi "kafka|redis|websocket|microservicio|kubernetes|base de datos|caché|endpoint|push" Requirements/*.MD
grep -nE "~~|\(Decidido|\(Refinado|\(Corregido|versión anterior|por ahora" README.md Requirements/*.MD Personas/*.MD
```

El primero y el cuarto no devuelven nada. El segundo marca requerimientos cuyo sujeto no es el
sistema. El tercero marca mecanismos infiltrados en un requerimiento; cada acierto se reformula como
garantía o se desplaza a `docs/`.
