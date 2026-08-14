# Evaluación de Carmen — iteración 1

Agente: [`Agents/agent-carmen.MD`](../../../../Agents/agent-carmen.MD) ·
Evaluado: `Requirements/ReqFunc.MD`, 42 requerimientos.

| ID | Veredicto | Justificación |
|---|---|---|
| RF-TUR-01 | Sirve | Es mi criterio de éxito número uno y además cruza sedes: el sistema **impide** guardar el cruce en vez de advertirlo, que es lo que hoy descubro el sábado a las 19:00. |
| RF-TUR-02 | Ambiguo | El propio enunciado abre con `[ACLARAR]` qué régimen rige a los rotantes que la Red me asigna; sin esa respuesta no sé si el control me protege justo en el caso que no controlo. |
| RF-TUR-03 | Sirve | Es el viernes 15:40 resuelto: veo candidatos ya filtrados por solapamiento, jornada y permisos en vez de cruzar el Excel de memoria. |
| RF-TUR-04 | Sirve | Una sola versión vigente con autoría e instante de cada cambio termina con las tres versiones del rol circulando por WhatsApp. |
| RF-TUR-05 | Sirve | Publicar un cambio y que quede registrado quién lo acusó es la confirmación de lectura que hoy pido una por una. |
| RF-TUR-06 | Sirve | Sostiene mi lado de la tensión: los médicos pactan lo que quieran, pero la programación vigente no se mueve hasta que yo lo resuelvo. |
| RF-TUR-07 | Sirve | Es mi criterio de las franjas descubiertas de los próximos días, con su sede y su unidad. |
| RF-TUR-08 | Sirve | Conserva la salida imprimible para la pared de la unidad, que es lo que evita que el equipo vuelva al Excel. |
| RF-DIA-01 | Sirve | Es mi lado de la tensión con Rodrigo: el turno no se cierra con el registro a medias, y por fin sé si el internista saliente dejó su diagnóstico. |
| RF-DIA-02 | Sirve | Define qué debe contener una entrega; sin ese contenido cerrado, la «completitud» que yo monitoreo no sería auditable. |
| RF-DIA-03 | Sirve | El señalamiento de la cama sin diagnóstico previo es el dato que después cuento en el tablero de cumplimiento. |
| RF-DIA-04 | Sirve | La autoría y el instante de cada entrega son la trazabilidad de la documentación clínica por la que respondo ante la Red. |
| RF-DIA-05 | Indiferente | Ver lo que cambió desde el último contacto es una ayuda clínica para quien rota. |
| RF-DIA-06 | Indiferente | La marca de inestabilidad ordena el trabajo asistencial, no la programación ni la auditoría. |
| RF-DIA-07 | Sirve | Que ninguna versión se sustituya y todas queden consultables es exactamente lo que la auditoría médica me pide del episodio. |
| RF-DIA-08 | Indiferente | La entrega de enfermería no entra en los indicadores que me pide la Red. |
| RF-ESC-01 | Indiferente | El escalamiento nocturno lo opera enfermería. |
| RF-ESC-02 | Indiferente | La cadena automática no toca mis seis tareas. |
| RF-ESC-03 | Indiferente | El contexto adjunto es del receptor del escalamiento. |
| RF-ESC-04 | Indiferente | El acuse le sirve a quien escaló. |
| RF-ESC-05 | Indiferente | El estado de la cadena abierta se consulta de noche, no en horario administrativo. |
| RF-ESC-06 | Indiferente | Las severidades ordenan un circuito clínico ajeno a la programación. |
| RF-ESC-07 | Indiferente | La delegación del localizable no pasa por mi programación mensual. |
| RF-ESC-08 | Indiferente | La cobertura clínica del instante es otra cosa que la programación que yo publico. |
| RF-ESC-09 | Indiferente | Me alcanza como jefatura, pero no traza a ninguna de mis seis tareas. |
| RF-ESC-10 | Indiferente | El aviso al que no acusó es del circuito de guardia. |
| RF-REG-01 | Indiferente | El registro a pie de cama es de enfermería. |
| RF-REG-02 | Indiferente | La captura sin conexión es un problema de la unidad, no de la programación. |
| RF-REG-03 | Indiferente | La consulta de indicaciones vigentes es asistencial. |
| RF-REG-04 | Indiferente | La confirmación de ejecución no llega a mis indicadores. |
| RF-REG-05 | Indiferente | Eventos y medicación son registro asistencial. |
| RF-REG-06 | Indiferente | Laboratorio e imágenes son consulta clínica. |
| RF-REG-07 | Indiferente | La indicación remota es del localizable. |
| RF-REG-08 | Indiferente | La tendencia clínica se consulta a pie de cama o a distancia, no desde mi oficina. |
| RF-IAM-01 | Sirve | Atribuir cada registro a quien lo produce es la mitad de la trazabilidad de la documentación clínica que respondo ante la Red. |
| RF-IAM-02 | Indiferente | Limitar el registro al ámbito de responsabilidad no traza a ninguna de mis tareas, y me preocupa más por lo que le hace a Rodrigo que por lo que me da a mí. |
| RF-IAM-03 | Sirve | El registro de cada consulta y modificación con su autor es lo que la Ley N.° 29733 me obliga a poder demostrar. |
| RF-IAM-04 | Indiferente | La exposición en dispositivo personal es del receptor del escalamiento. |
| RF-SUP-01 | Sirve | Es mi tarea 5 completa: entregas cerradas limpias, cerradas con camas señaladas y turnos concluidos sin entrega. |
| RF-SUP-02 | Sirve | Es mi criterio de éxito: los indicadores para la Red salen del sistema sin que yo cuente a mano. |
| RF-SUP-03 | Indiferente | La revisión de la actividad nocturna es del intensivista localizable. |
| RF-SUP-04 | Indiferente | Auditar un escalamiento me interesa, pero no traza a ninguna de mis seis tareas críticas. |

### Necesidades no cubiertas

- **Asignar un profesional a una franja.** Ningún enunciado declara que el sistema registre una
  asignación de turno. `RF-TUR-01` y `RF-TUR-02` declaran cuándo la rechaza, `RF-TUR-03` presenta
  candidatos y `RF-TUR-04` mantiene la versión vigente: todos presuponen un acto de asignar que
  ningún RF declara. Es el centro de mis tareas 1 y 4.
- **Elaborar y publicar la programación mensual.** Mismo hueco visto desde arriba: no hay RF que
  declare la creación ni la publicación de la programación de un periodo.
- **Permisos.** Mi tarea 3 es «aprobar o rechazar intercambios **y permisos**». `RF-TUR-06` cubre el
  intercambio; el permiso solo aparece como dato preexistente en `RF-TUR-03` («sin permiso vigente
  para esa franja»). Nadie declara cómo se solicita, se aprueba ni se rechaza.
- **El efecto de mi resolución sobre un intercambio.** `RF-TUR-06` declara que la propuesta no tiene
  efecto hasta que yo la resuelva, pero no declara qué ocurre cuando la acepto. Eso vive en un
  criterio de aceptación, no en el enunciado.
- **La rotación como criterio de reparto.** Mi escenario dice «a quién le corresponde por rotación»;
  `RF-TUR-03` filtra por elegibilidad, no por equidad.

### Riesgos que veo

- **Adopción, y es mi problema.** `RF-IAM-02` puede rechazarle un registro a un rotante que la Red
  asignó sin pasar por mí, y `RF-ESC-06` le impone a Milagros clasificar antes de escalar. Los dos
  empujan a mi equipo de vuelta al papel, y el registro degradado lo respondo yo ante la Red.
- El tablero de `RF-SUP-01` mide la completitud de las entregas, pero el registro del diagnóstico que
  esa completitud exige no está declarado en ningún RF: voy a medir el cumplimiento de un acto que el
  sistema no declara soportar.
- La tensión de adopción voluntaria se decide en `RF-TUR-08` —un COULD que conserva la salida
  imprimible— y en dos RNF que esta rúbrica no puntúa. Es la única de las cinco tensiones que ningún
  RF vinculante decide.

### Recorrido del escenario clave

**Viernes 15:40. El internista del sábado nocturno presentó descanso médico.**

1. Necesito saber quién está disponible el sábado, sin exceder horas y sin turno en otra sede →
   `RF-TUR-03` presenta exactamente los elegibles por las tres condiciones. ✔
2. A quién le corresponde por rotación → ningún RF; lo resuelvo yo con criterio propio. ✖ (parcial)
3. **Asigno el reemplazo** → **ningún RF declara que el sistema registre una asignación.**
   `RF-TUR-01` solo declara el rechazo si hay cruce. **Aquí se corta.**
4. Publico el cambio y llega a los afectados con acuse → `RF-TUR-05`. ✔
5. Compruebo que no quedó franja descubierta → `RF-TUR-07`. ✔

**El flujo se interrumpe en el paso 3**, que es el único paso que el escenario existe para resolver.

### Cobertura percibida: 100 %

Las seis tareas críticas tienen al menos un RF que marqué «Sirve». El número sale de mi definición y
no de lo que acabo de recorrer: cuatro de esas seis tareas se apoyan en RF que presuponen un acto de
asignar que ningún enunciado declara.
