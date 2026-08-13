# Requerimientos Funcionales

Sistema de Gestión de UCI — Essalud

Forma y verificación: [`docs/CONVENCIONES.md`](../docs/CONVENCIONES.md), secciones 5, 6 y 9.
Este documento es el único insumo de requerimientos que puntúa [`Spec/Eval-Spec.MD`](../Spec/Eval-Spec.MD).

## Convenciones

- **ID:** `RF-‹área›-‹n›`
- **Enunciado:** un patrón EARS con el auxiliar DEBE y el sistema como sujeto.
- **Prioridad:** MUST / SHOULD / COULD. MUST se reserva a lo que, ausente, deja sin resolver un
  problema crítico o deja a una persona sin su tarea crítica.
- **Trazabilidad:** persona que lo motiva y problema crítico al que responde.
- **Criterios de aceptación:** un par Cuando/Entonces por criterio, actor en tercera persona.

| Área | Prefijo |
|---|---|
| Gestión de turnos | `RF-TUR` |
| Diagnósticos y entrega de turno | `RF-DIA` |
| Escalamiento y disponibilidad del médico | `RF-ESC` |
| Registro clínico a pie de cama | `RF-REG` |
| Identidad y accesos | `RF-IAM` |
| Supervisión de la unidad | `RF-SUP` |

Patrones EARS admitidos: ubicuo, de estado (MIENTRAS), de evento (CUANDO), de opción (DONDE),
de borde (SI … ENTONCES) y complejo.

Los plazos que un enunciado invoca —«dentro del plazo definido para la severidad»— se fijan en
[`ReqNoFunc.MD`](ReqNoFunc.MD). El comportamiento pertenece a este documento; el umbral, al otro.

---

## RF-TUR — Gestión de turnos

### RF-TUR-01 — Rechazo de asignación con cruce en la red

**Enunciado:** SI una asignación de turno solapa la franja de otro turno vigente del mismo profesional en cualquier sede de la red, ENTONCES el sistema DEBE rechazar la asignación e indicar el turno con el que solapa.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional con un turno vigente el sábado de 19:00 a 07:00 en la sede A, cuando la coordinadora le asigna un turno el sábado de 19:00 a 07:00 en la sede B, entonces la asignación no queda registrada y se indica el turno de la sede A.
- **CA-2** — Dado un profesional con un turno vigente el sábado de 19:00 a 07:00 en la sede A, cuando la coordinadora le asigna un turno el domingo de 19:00 a 07:00 en la sede B, entonces la asignación queda registrada.

---

### RF-TUR-02 — Rechazo de asignación fuera de los límites de jornada

**Enunciado:** SI una asignación de turno excede el máximo de horas o el descanso mínimo del régimen laboral vigente para el profesional, ENTONCES el sistema DEBE rechazar la asignación e indicar el límite superado.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional que alcanzó su máximo mensual de horas, cuando la coordinadora le asigna un turno adicional en ese mes, entonces la asignación no queda registrada y se indica el máximo mensual como límite superado.
- **CA-2** — Dado un profesional que concluyó un turno hace menos que el descanso mínimo exigido, cuando la coordinadora le asigna el turno siguiente, entonces la asignación no queda registrada y se indica el descanso mínimo como límite superado.

`[ACLARAR: qué régimen de jornada rige a los rotantes que la Red asigna y que no dependen de la unidad, y si sus horas computan contra el mismo máximo mensual que el personal de planta.]`

---

### RF-TUR-03 — Candidatos elegibles para una franja

**Enunciado:** CUANDO el coordinador de la unidad solicita cobertura para una franja, el sistema DEBE presentar exactamente los profesionales que cumplen las tres condiciones: sin turno solapado en la red, dentro de sus límites de jornada y sin permiso vigente para esa franja.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una franja descubierta y un profesional con permiso vigente que la abarca, cuando la coordinadora solicita cobertura para esa franja, entonces ese profesional no figura entre los presentados.
- **CA-2** — Dada una franja descubierta y un profesional sin turno solapado, dentro de sus límites de jornada y sin permiso vigente, cuando la coordinadora solicita cobertura para esa franja, entonces ese profesional figura entre los presentados.

---

### RF-TUR-04 — Versión vigente única de la programación

**Enunciado:** El sistema DEBE mantener una sola programación vigente por unidad y conservar cada cambio con su autoría y su instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una programación vigente para una unidad, cuando la coordinadora publica una modificación, entonces la modificación pasa a ser la única vigente y la anterior queda consultable con su autoría e instante.
- **CA-2** — Dada una programación con tres cambios sucesivos, cuando un profesional consulta la programación de esa unidad, entonces obtiene únicamente la versión vigente.

---

### RF-TUR-05 — Alcance y acuse de un cambio de programación

**Enunciado:** CUANDO la programación vigente de una unidad cambia, el sistema DEBE alcanzar a cada profesional cuya asignación se modifica y registrar su acuse con el instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una programación vigente, cuando la coordinadora sustituye al profesional asignado a un turno, entonces tanto el profesional sustituido como el entrante quedan alcanzados y su acuse queda pendiente de registro.
- **CA-2** — Dado un profesional alcanzado por un cambio de programación, cuando ese profesional acusa el cambio, entonces el acuse queda registrado con su instante y resulta consultable por la coordinadora.

---

### RF-TUR-06 — Intercambio de turno sujeto a resolución del coordinador

**Enunciado:** CUANDO dos profesionales pactan un intercambio de turno, el sistema DEBE registrarlo como propuesta sin efecto sobre la programación vigente hasta que el coordinador de la unidad la resuelva.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen, Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una propuesta de intercambio entre dos profesionales, cuando la coordinadora aún no la resuelve, entonces la programación vigente conserva la asignación original.
- **CA-2** — Dada una propuesta de intercambio pendiente, cuando la coordinadora la acepta, entonces la programación vigente incorpora el intercambio y ambos profesionales quedan alcanzados por el cambio.
- **CA-3** — Dada una propuesta de intercambio que produciría un solapamiento en la red, cuando la coordinadora la acepta, entonces el intercambio no se incorpora y se indica el turno con el que solapa.

---

### RF-TUR-07 — Franjas sin responsable asignado

**Enunciado:** CUANDO el coordinador consulta la cobertura de una unidad para un horizonte dado, el sistema DEBE presentar las franjas sin profesional asignado, con su sede y su unidad.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una unidad con una franja nocturna sin profesional asignado dentro de los próximos siete días, cuando la coordinadora consulta la cobertura de ese horizonte, entonces esa franja figura entre las descubiertas con su sede y su unidad.
- **CA-2** — Dada una unidad con todas sus franjas asignadas en el horizonte consultado, cuando la coordinadora consulta la cobertura, entonces no se presenta franja descubierta alguna.

---

### RF-TUR-08 — Obtención de la programación en formato imprimible

**Enunciado:** El sistema DEBE permitir obtener la programación vigente de una unidad en un formato imprimible que conserve profesional, franja, sede y unidad.

| Campo | Valor |
|---|---|
| Prioridad | COULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una programación vigente, cuando la coordinadora la obtiene en formato imprimible, entonces el resultado contiene el profesional, la franja, la sede y la unidad de cada turno de esa programación.

---

## RF-DIA — Diagnósticos y entrega de turno

### RF-DIA-01 — Bloqueo del cierre de turno sin diagnóstico vigente

**Enunciado:** SI un turno finaliza sin diagnóstico vigente registrado para alguna de las camas asignadas al profesional, ENTONCES el sistema DEBE impedir el cierre de la entrega de turno y señalar las camas sin diagnóstico.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un médico con cuatro camas asignadas y diagnóstico vigente en tres de ellas, cuando ese médico cierra su entrega de turno, entonces la entrega no queda cerrada y se señala la cama sin diagnóstico.
- **CA-2** — Dado un médico con diagnóstico vigente en todas sus camas asignadas, cuando ese médico cierra su entrega de turno, entonces la entrega queda cerrada.

---

### RF-DIA-02 — Contenido de la entrega de turno médica

**Enunciado:** CUANDO un profesional inicia un turno en una unidad, el sistema DEBE presentar, por cada cama asignada, exactamente: el diagnóstico vigente, las decisiones clínicas del turno anterior con su fundamento, los pendientes críticos abiertos y el estado de la información entregada a la familia.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una cama cuyo turno anterior decidió no escalar el soporte ventilatorio y registró su fundamento, cuando el médico entrante inicia el turno, entonces esa decisión y su fundamento figuran en la entrega de esa cama.
- **CA-2** — Dada una cama con un cultivo solicitado y aún sin resultado, cuando el médico entrante inicia el turno, entonces ese pendiente figura entre los pendientes críticos abiertos de esa cama.
- **CA-3** — Dada una cama cuya familia no fue informada del pronóstico, cuando el médico entrante inicia el turno, entonces el estado de la información a la familia figura como pendiente en esa cama.

---

### RF-DIA-03 — Señalamiento de camas sin diagnóstico previo

**Enunciado:** SI alguna cama asignada carece de diagnóstico del turno anterior, ENTONCES el sistema DEBE señalarla antes de que el profesional entrante acepte la entrega de turno.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una cama sin diagnóstico del turno anterior, cuando el médico entrante recibe la entrega de turno, entonces esa cama queda señalada antes de que la aceptación quede registrada.
- **CA-2** — Dada una entrega con una cama señalada por falta de diagnóstico previo, cuando el médico entrante acepta la entrega, entonces la aceptación queda registrada junto con el señalamiento de esa cama.

---

### RF-DIA-04 — Cierre de la entrega con autoría e instante

**Enunciado:** CUANDO el profesional saliente confirma la entrega de turno, el sistema DEBE registrar la entrega con su autoría y el instante de la confirmación, y ponerla a disposición del turno entrante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una entrega de turno completa, cuando el médico saliente la confirma, entonces la entrega queda registrada con su autoría y el instante de confirmación.
- **CA-2** — Dada una entrega confirmada por el médico saliente, cuando el médico entrante inicia su turno en esa unidad, entonces obtiene esa entrega sin depender de la presencia del médico saliente.

---

### RF-DIA-05 — Cambios desde el último contacto del profesional

**Enunciado:** CUANDO un profesional consulta una cama sobre la que registró un contacto previo, el sistema DEBE presentar los cambios clínicos ocurridos desde ese contacto.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un médico cuyo último contacto registrado con una cama ocurrió tres semanas antes, cuando ese médico consulta esa cama, entonces obtiene los cambios de diagnóstico, de esquema terapéutico y de soporte ocurridos desde ese contacto.
- **CA-2** — Dado un médico sin contacto previo registrado con una cama, cuando ese médico consulta esa cama, entonces obtiene el estado clínico vigente completo.

---

### RF-DIA-06 — Marca de inestabilidad y pendiente crítico

**Enunciado:** CUANDO un profesional marca una cama como inestable o con pendiente crítico, el sistema DEBE mantener esa marca en la entrega de turno de esa cama hasta que un profesional la retire con su autoría.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una cama marcada como inestable en el turno anterior, cuando el médico entrante recibe la entrega de esa unidad, entonces esa cama figura marcada como inestable.
- **CA-2** — Dada una cama marcada como inestable, cuando un médico retira la marca, entonces la retirada queda registrada con su autoría y la cama deja de figurar marcada.

---

### RF-DIA-07 — Conservación de las versiones del diagnóstico

**Enunciado:** El sistema DEBE conservar cada versión registrada del diagnóstico de un episodio con su autoría y su instante, sin sustituir una versión previa.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo, Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio con un diagnóstico registrado, cuando un médico registra un diagnóstico distinto para ese episodio, entonces la versión previa permanece consultable con su autoría e instante y la nueva pasa a ser la vigente.
- **CA-2** — Dado un episodio con tres versiones de diagnóstico, cuando la coordinadora audita ese episodio, entonces obtiene las tres versiones en su orden de registro.

---

### RF-DIA-08 — Entrega de turno de enfermería

**Enunciado:** CUANDO un profesional de enfermería concluye su turno, el sistema DEBE registrar su entrega con exactamente: los pendientes de cuidado abiertos, los eventos del turno y la medicación administrada.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una enfermera con eventos y medicación registrados durante su turno, cuando concluye el turno, entonces su entrega contiene los pendientes de cuidado abiertos, los eventos y la medicación administrada de ese turno.
- **CA-2** — Dada una entrega de enfermería registrada, cuando la enfermera del turno entrante inicia su turno, entonces obtiene esa entrega sin transcribirla.

---

## RF-ESC — Escalamiento y disponibilidad del médico

### RF-ESC-01 — Escalamiento al responsable clínico vigente

**Enunciado:** CUANDO un profesional de enfermería escala un deterioro clínico de una cama, el sistema DEBE alcanzar al responsable clínico vigente de esa cama y registrar el instante de la emisión.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con responsable clínico vigente, cuando la enfermera escala un deterioro de esa cama, entonces ese responsable queda alcanzado y la emisión queda registrada con su instante.
- **CA-2** — Dada una cama cuyo responsable clínico difiere del publicado en la programación inicial del mes, cuando la enfermera escala un deterioro de esa cama, entonces queda alcanzado el responsable vigente en ese instante.

---

### RF-ESC-02 — Escalamiento automático por falta de acuse

**Enunciado:** SI el destinatario alcanzado no acusa recibo dentro del plazo definido para la severidad del escalamiento, ENTONCES el sistema DEBE alcanzar al siguiente integrante de la cadena sin intervención de quien escaló.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento emitido al responsable clínico vigente, cuando transcurre el plazo de acuse de esa severidad sin que él acuse, entonces el siguiente integrante de la cadena queda alcanzado sin que la enfermera realice acción alguna.
- **CA-2** — Dado un escalamiento emitido, cuando el destinatario acusa dentro del plazo, entonces ningún integrante posterior de la cadena queda alcanzado.

---

### RF-ESC-03 — Contexto clínico adjunto al escalamiento

**Enunciado:** CUANDO el sistema emite un escalamiento, DEBE adjuntar exactamente: sede, unidad, cama e identificación del episodio; el motivo declarado por quien escala; la tendencia de las últimas seis horas de signos vitales; el balance hídrico del día; el soporte vasoactivo y ventilatorio vigentes con su dosis; el esquema antimicrobiano en curso con su día de tratamiento; el último resultado de laboratorio disponible; y la última evolución registrada.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio con vasopresor en curso, cuando el sistema emite un escalamiento de esa cama, entonces el escalamiento incluye ese vasopresor con su dosis.
- **CA-2** — Dado un médico que cubre dos sedes, cuando recibe un escalamiento, entonces el escalamiento identifica la sede, la unidad y la cama sin requerir una consulta adicional.
- **CA-3** — Dado un episodio sin resultado de laboratorio registrado, cuando el sistema emite un escalamiento de esa cama, entonces el escalamiento declara la ausencia de resultado en lugar de omitir el dato.

---

### RF-ESC-04 — Acuse de recibo visible para quien escaló

**Enunciado:** CUANDO el destinatario de un escalamiento acusa recibo, el sistema DEBE registrar el acuse con su autoría y su instante y presentarlo a quien escaló.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento emitido por una enfermera, cuando el médico alcanzado acusa recibo, entonces el acuse queda registrado con su autoría e instante y resulta visible para esa enfermera.
- **CA-2** — Dado un escalamiento acusado, cuando la enfermera consulta ese escalamiento, entonces obtiene la identidad de quien acusó y el instante del acuse.

---

### RF-ESC-05 — Estado de la cadena mientras el escalamiento sigue abierto

**Enunciado:** MIENTRAS un escalamiento permanece sin acuse, el sistema DEBE presentar a quien escaló el integrante de la cadena alcanzado en ese momento.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento sin acuse que ya alcanzó al segundo integrante de la cadena, cuando la enfermera consulta ese escalamiento, entonces obtiene la identidad del segundo integrante como destinatario en curso.
- **CA-2** — Dado un escalamiento acusado, cuando la enfermera consulta ese escalamiento, entonces obtiene el acuse en lugar de un destinatario en curso.

---

### RF-ESC-06 — Severidades diferenciadas del escalamiento

**Enunciado:** CUANDO un profesional emite un escalamiento, el sistema DEBE ofrecer exactamente dos severidades —deterioro que exige respuesta inmediata y consulta que admite diferimiento— y aplicar a cada una su propia cadena y su propio plazo de acuse.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento clasificado como consulta diferible, cuando transcurre el plazo de acuse del deterioro inmediato, entonces ningún integrante posterior de la cadena queda alcanzado.
- **CA-2** — Dado un escalamiento clasificado como deterioro inmediato y otro clasificado como consulta diferible sobre la misma cama, cuando ambos se emiten, entonces cada uno aplica la cadena y el plazo de su severidad.

---

### RF-ESC-07 — Indisponibilidad temporal y delegación

**Enunciado:** CUANDO un médico se declara temporalmente indisponible e indica su delegado, el sistema DEBE excluirlo de la cadena de escalamiento vigente y situar en su lugar al delegado indicado.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico de guardia que se declara indisponible e indica un delegado, cuando se emite un escalamiento que le correspondería, entonces queda alcanzado el delegado y no él.
- **CA-2** — Dado un médico que se declara indisponible sin indicar delegado, cuando se emite un escalamiento que le correspondería, entonces queda alcanzado el siguiente integrante de la cadena.
- **CA-3** — Dado un médico cuyo periodo de indisponibilidad declarado concluyó, cuando se emite un escalamiento que le corresponde, entonces queda alcanzado él.

---

### RF-ESC-08 — Consulta de la cobertura clínica vigente

**Enunciado:** CUANDO un profesional consulta la cobertura clínica de una unidad, el sistema DEBE presentar el responsable vigente de cada cama en ese instante y su disponibilidad declarada.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P2, P3 |

**Criterios de aceptación**

- **CA-1** — Dado un responsable clínico que se declaró indisponible, cuando la enfermera consulta la cobertura de esa unidad, entonces obtiene a ese profesional con su indisponibilidad declarada y al delegado vigente.
- **CA-2** — Dada una unidad cuya programación cambió durante el turno en curso, cuando la enfermera consulta la cobertura, entonces obtiene el responsable resultante de ese cambio.

---

### RF-ESC-09 — Agotamiento de la cadena de escalamiento

**Enunciado:** SI un escalamiento agota su cadena sin obtener acuse, ENTONCES el sistema DEBE alcanzar a la jefatura de la unidad y registrar el agotamiento.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros, Carmen |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento que alcanzó a todos los integrantes de su cadena sin acuse, cuando vence el plazo del último integrante, entonces la jefatura de la unidad queda alcanzada y el agotamiento queda registrado.
- **CA-2** — Dado un escalamiento con agotamiento registrado, cuando la coordinadora consulta la actividad de esa unidad, entonces obtiene ese agotamiento con la cadena recorrida.

---

### RF-ESC-10 — Aviso al integrante que no acusó

**Enunciado:** CUANDO el sistema alcanza al siguiente integrante de la cadena por falta de acuse, DEBE informar de ese avance al integrante que no acusó.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico que no acusó un escalamiento dentro de su plazo, cuando el sistema alcanza al siguiente integrante, entonces ese médico queda informado de que el escalamiento avanzó en la cadena.

---

## RF-REG — Registro clínico a pie de cama

### RF-REG-01 — Registro de signos vitales y balance

**Enunciado:** CUANDO un profesional registra signos vitales o balance hídrico de una cama, el sistema DEBE incorporarlos al estado vigente del episodio con la autoría y el instante del registro.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con episodio abierto, cuando la enfermera registra los signos vitales, entonces esos signos integran el estado vigente del episodio con su autoría e instante.
- **CA-2** — Dada una cama con signos registrados, cuando el médico de guardia consulta esa cama, entonces obtiene esos signos sin que la enfermera los transcriba.

---

### RF-REG-02 — Continuidad del registro ante pérdida de conectividad

**Enunciado:** SI el registro a pie de cama se produce sin conexión con el resto del sistema, ENTONCES el sistema DEBE conservarlo en el dispositivo de captura e incorporarlo al episodio al restablecerse la conexión, sin pérdida ni duplicación.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una enfermera que registra signos vitales sin conexión, cuando la conexión se restablece, entonces ese registro figura una sola vez en el episodio con el instante en que fue tomado.
- **CA-2** — Dada una enfermera que registra dos observaciones sucesivas sin conexión, cuando la conexión se restablece, entonces ambas figuran en el episodio en el orden en que fueron tomadas.

---

### RF-REG-03 — Consulta de indicaciones vigentes

**Enunciado:** CUANDO un profesional consulta las indicaciones médicas de una cama, el sistema DEBE presentar exactamente las vigentes, cada una con su autor y su instante de emisión.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una cama cuya indicación fue sustituida por otra, cuando la enfermera consulta las indicaciones de esa cama, entonces obtiene únicamente la vigente.
- **CA-2** — Dada una indicación vigente, cuando la enfermera la consulta, entonces obtiene su autor y su instante de emisión.

---

### RF-REG-04 — Confirmación de ejecución de una indicación

**Enunciado:** CUANDO un profesional de enfermería confirma la ejecución de una indicación, el sistema DEBE registrar la confirmación con su autoría y su instante.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Milagros |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una indicación vigente, cuando la enfermera confirma su ejecución, entonces la confirmación queda registrada con su autoría e instante.
- **CA-2** — Dada una indicación vigente sin confirmación de ejecución, cuando el médico responsable consulta esa cama, entonces obtiene esa indicación como no ejecutada.

---

### RF-REG-05 — Registro de eventos y medicación administrada

**Enunciado:** CUANDO un profesional registra un evento clínico o la administración de un medicamento, el sistema DEBE incorporarlo al episodio con su autoría y su instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Milagros |
| Problema | P3 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con episodio abierto, cuando la enfermera registra la administración de un medicamento, entonces esa administración integra el episodio con su autoría e instante.
- **CA-2** — Dado un evento registrado durante el turno, cuando ese turno concluye, entonces el evento figura en la entrega de enfermería sin ser transcrito.

---

### RF-REG-06 — Resultados de laboratorio e imágenes del episodio

**Enunciado:** CUANDO un profesional consulta una cama, el sistema DEBE presentar los resultados de laboratorio e imágenes disponibles del episodio y señalar los estudios solicitados aún sin resultado.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un episodio con un cultivo solicitado y aún sin resultado, cuando el médico consulta esa cama, entonces ese estudio figura como solicitado sin resultado.
- **CA-2** — Dado un episodio con resultados de laboratorio disponibles, cuando el médico consulta esa cama, entonces obtiene esos resultados con su instante.

---

### RF-REG-07 — Registro de indicación a distancia

**Enunciado:** CUANDO un médico registra una indicación a distancia sobre una cama de la que es responsable vigente o delegado, el sistema DEBE incorporarla a las indicaciones vigentes de esa cama con su autoría y su instante.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico que acusó un escalamiento, cuando registra una indicación para esa cama desde el mismo dispositivo en que lo recibió, entonces la indicación integra las vigentes con su autoría e instante.
- **CA-2** — Dada una indicación registrada a distancia, cuando la enfermera de esa unidad consulta las indicaciones de esa cama, entonces obtiene esa indicación con su autor.

---

### RF-REG-08 — Tendencia clínica de la cama

**Enunciado:** CUANDO un profesional consulta la evolución de una cama, el sistema DEBE presentar la tendencia de las últimas seis horas de signos vitales, balance hídrico y soporte vigente.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una cama con registros de las últimas seis horas, cuando el médico de guardia consulta su evolución, entonces obtiene la tendencia de esos registros y no únicamente el valor más reciente.
- **CA-2** — Dada una cama con menos de seis horas de registros, cuando el médico consulta su evolución, entonces obtiene la tendencia del periodo disponible declarando su extensión.

---

## RF-IAM — Identidad y accesos

### RF-IAM-01 — Atribución del registro a su autor

**Enunciado:** El sistema DEBE atribuir cada registro clínico al profesional que lo produce y no a la sesión abierta en el equipo empleado.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Rodrigo |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un equipo compartido con la sesión de un médico abierta, cuando otro médico produce un registro clínico en ese equipo, entonces el registro queda atribuido al segundo médico.
- **CA-2** — Dado un registro clínico producido, cuando la coordinadora lo audita, entonces obtiene al profesional que lo produjo.

---

### RF-IAM-02 — Restricción del registro al ámbito de responsabilidad

**Enunciado:** SI un profesional registra sobre una cama de una unidad o sede en la que no tiene turno vigente, delegación activa ni responsabilidad de jefatura, ENTONCES el sistema DEBE rechazar el registro.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional sin turno vigente ni delegación en una unidad, cuando registra sobre una cama de esa unidad, entonces el registro no queda incorporado al episodio.
- **CA-2** — Dado un profesional con delegación activa sobre una unidad, cuando registra sobre una cama de esa unidad, entonces el registro queda incorporado con su autoría.

---

### RF-IAM-03 — Trazabilidad de acceso a datos clínicos

**Enunciado:** El sistema DEBE registrar cada consulta y cada modificación de datos clínicos con el profesional que la realiza, el episodio alcanzado y su instante.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dado un profesional que consulta el episodio de una cama, cuando esa consulta concluye, entonces quedan registrados el profesional, el episodio alcanzado y el instante.
- **CA-2** — Dado un episodio consultado por tres profesionales distintos, cuando la coordinadora audita ese episodio, entonces obtiene los tres accesos con su autoría e instante.

---

### RF-IAM-04 — Exposición de datos en dispositivo no institucional

**Enunciado:** DONDE el destinatario de un escalamiento emplea un dispositivo no institucional, el sistema DEBE excluir del aviso todo dato identificatorio del paciente y exigir autenticación del profesional antes de presentar el contexto clínico.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un médico que recibe un escalamiento en un dispositivo no institucional, cuando el aviso llega sin que él se autentique, entonces el aviso no contiene el nombre ni el documento de identidad del paciente.
- **CA-2** — Dado un médico que recibe un escalamiento en un dispositivo no institucional, cuando ese médico se autentica, entonces obtiene el contexto clínico completo del escalamiento.

---

## RF-SUP — Supervisión de la unidad

### RF-SUP-01 — Cumplimiento y completitud de las entregas de turno

**Enunciado:** CUANDO el coordinador consulta el cumplimiento de entregas de turno de una unidad en un periodo, el sistema DEBE presentar exactamente: las entregas cerradas sin camas señaladas, las cerradas con camas señaladas y los turnos concluidos sin entrega cerrada.

| Campo | Valor |
|---|---|
| Prioridad | MUST |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una unidad con un turno concluido sin entrega cerrada, cuando la coordinadora consulta el cumplimiento de ese periodo, entonces ese turno figura entre los concluidos sin entrega cerrada.
- **CA-2** — Dada una entrega cerrada con una cama señalada por falta de diagnóstico previo, cuando la coordinadora consulta el cumplimiento de ese periodo, entonces esa entrega figura entre las cerradas con camas señaladas.

---

### RF-SUP-02 — Indicadores de cobertura de la red

**Enunciado:** El sistema DEBE producir los indicadores de cobertura de turnos y de cumplimiento de entrega de las unidades de una red a partir de los registros vigentes, sin transcripción manual.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Carmen |
| Problema | P1 |

**Criterios de aceptación**

- **CA-1** — Dada una red con tres unidades y sus turnos registrados en un periodo, cuando la coordinadora obtiene los indicadores de cobertura de ese periodo, entonces obtiene las franjas descubiertas y las entregas cerradas de las tres unidades sin ingresar dato alguno.

---

### RF-SUP-03 — Revisión de la actividad de la unidad en un periodo

**Enunciado:** CUANDO un profesional consulta la actividad de una unidad en un periodo, el sistema DEBE presentar los escalamientos emitidos con su severidad, las indicaciones registradas a distancia y los ingresos y egresos ocurridos.

| Campo | Valor |
|---|---|
| Prioridad | SHOULD |
| Persona | Aníbal |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dada una unidad con dos escalamientos y una indicación a distancia durante la noche, cuando el médico consulta la actividad de esa noche a la mañana siguiente, entonces obtiene los dos escalamientos y la indicación en un solo resultado.

---

### RF-SUP-04 — Auditoría de un escalamiento

**Enunciado:** CUANDO el coordinador audita un escalamiento, el sistema DEBE presentar exactamente: su instante de emisión, su severidad, los integrantes alcanzados en orden, los acuses con su autoría e instante, y su desenlace.

| Campo | Valor |
|---|---|
| Prioridad | COULD |
| Persona | Carmen |
| Problema | P2 |

**Criterios de aceptación**

- **CA-1** — Dado un escalamiento que recorrió dos integrantes antes de ser acusado, cuando la coordinadora lo audita, entonces obtiene ambos integrantes en el orden en que fueron alcanzados y el acuse del segundo.

---

## Matriz de trazabilidad

Cada tarea crítica de cada persona traza a al menos un RF. Las filas sin RF son brechas abiertas.

| Persona | Tarea crítica | RF que la cubre |
|---|---|---|
| Rodrigo | Recibir el handoff estructurado de todas las camas asignadas | RF-DIA-02, RF-DIA-03 |
| Rodrigo | Consultar la evolución y el diagnóstico del turno anterior | RF-DIA-02, RF-DIA-05, RF-DIA-07 |
| Rodrigo | Registrar nota de evolución y diagnóstico por paciente | RF-DIA-07, RF-IAM-01 |
| Rodrigo | Marcar pacientes inestables o con pendientes críticos | RF-DIA-06 |
| Rodrigo | Consultar resultados de laboratorio e imágenes | RF-REG-06 |
| Rodrigo | Cerrar y firmar la entrega de turno | RF-DIA-01, RF-DIA-04 |
| Milagros | Registrar signos vitales y balance por paciente | RF-REG-01, RF-REG-02 |
| Milagros | Escalar un deterioro clínico al médico responsable | RF-ESC-01, RF-ESC-06 |
| Milagros | Consultar quién está de guardia y su estado de disponibilidad | RF-ESC-08 |
| Milagros | Ver y confirmar indicaciones médicas vigentes | RF-REG-03, RF-REG-04 |
| Milagros | Registrar eventos y administración de medicamentos | RF-REG-05 |
| Milagros | Recibir y entregar el turno de enfermería | RF-DIA-08 |
| Carmen | Elaborar y publicar la programación mensual de turnos | RF-TUR-04, RF-TUR-05 |
| Carmen | Validar que no existan cruces ni franjas descubiertas | RF-TUR-01, RF-TUR-02, RF-TUR-07 |
| Carmen | Aprobar o rechazar intercambios y permisos | RF-TUR-06, RF-TUR-03 |
| Carmen | Reasignar cobertura ante una ausencia imprevista | RF-TUR-03, RF-TUR-05 |
| Carmen | Monitorear cumplimiento y completitud de entregas de turno | RF-SUP-01 |
| Carmen | Generar indicadores de cobertura para la Dirección de Red | RF-SUP-02 |
| Aníbal | Recibir la alerta de escalamiento con contexto clínico adjunto | RF-ESC-03, RF-IAM-04 |
| Aníbal | Confirmar recepción y tomar el caso | RF-ESC-04 |
| Aníbal | Consultar tendencia de signos, ventilación y última evolución | RF-REG-08 |
| Aníbal | Registrar la indicación dada de forma remota | RF-REG-07 |
| Aníbal | Marcarse temporalmente indisponible y delegar | RF-ESC-07 |
| Aníbal | Revisar en la mañana lo ocurrido durante la noche | RF-SUP-03 |

## Cobertura de criterios de éxito

| Persona | Criterio de éxito | RF que lo satisface |
|---|---|---|
| Rodrigo | Entender el estado de las camas empleando solo el sistema | RF-DIA-02 |
| Rodrigo | El handoff incluye decisiones y su justificación | RF-DIA-02 |
| Rodrigo | Ninguna cama llega sin diagnóstico; si falta, el sistema lo señala | RF-DIA-01, RF-DIA-03 |
| Rodrigo | Registrar la nota de evolución cuesta menos que escribirla a mano | RF-DIA-07, `RNF-USA-01` |
| Rodrigo | Ver qué cambió desde su último contacto con el paciente | RF-DIA-05 |
| Milagros | Escalar un deterioro en el mínimo de pasos | RF-ESC-01, `RNF-USA-02` |
| Milagros | Ver quién está de guardia en este momento | RF-ESC-08 |
| Milagros | Recibir confirmación visible de que el médico vio la alerta | RF-ESC-04 |
| Milagros | Si nadie responde, el sistema escala sin que ella intervenga | RF-ESC-02, RF-ESC-09 |
| Milagros | Registrar a pie de cama, sin caminar hasta la estación | RF-REG-01, RF-REG-02 |
| Milagros | Dejar de transcribir del papel al sistema | RF-REG-05, RF-DIA-08 |
| Carmen | El sistema impide guardar una asignación con cruce | RF-TUR-01 |
| Carmen | Cubrir una ausencia imprevista toma minutos | RF-TUR-03, RF-TUR-05 |
| Carmen | Una sola versión vigente del rol, con historial de cambios | RF-TUR-04 |
| Carmen | Ver qué franjas de los próximos días están descubiertas | RF-TUR-07 |
| Carmen | Saber qué entregas se cerraron sin diagnóstico registrado | RF-SUP-01 |
| Carmen | Los indicadores salen del sistema sin trabajo manual | RF-SUP-02 |
| Aníbal | La alerta incluye el contexto clínico mínimo sin pedirlo | RF-ESC-03 |
| Aníbal | Decidir si acude, con el contexto ya recibido | RF-ESC-03, RF-REG-08 |
| Aníbal | Confirmar recepción y que quien escaló lo vea de inmediato | RF-ESC-04 |
| Aníbal | Registrar su indicación remota con hora y autoría | RF-REG-07 |
| Aníbal | Si no responde, el sistema escala solo y él se entera | RF-ESC-02, RF-ESC-10 |
| Aníbal | Revisar en un solo lugar lo ocurrido en la noche | RF-SUP-03 |

## Cobertura de problemas críticos

| Problema | RF que lo resuelve |
|---|---|
| P1 — Rotación de doctor | RF-DIA-01, RF-DIA-02, RF-DIA-03, RF-DIA-04, RF-DIA-05, RF-DIA-06, RF-DIA-07, RF-DIA-08, RF-TUR-01, RF-TUR-04, RF-TUR-05, RF-REG-06, RF-IAM-01, RF-SUP-01 |
| P2 — Medianoche | RF-ESC-01, RF-ESC-02, RF-ESC-03, RF-ESC-04, RF-ESC-05, RF-ESC-06, RF-ESC-07, RF-ESC-08, RF-ESC-09, RF-ESC-10, RF-REG-07, RF-REG-08, RF-IAM-04, RF-SUP-03, RF-SUP-04 |
| P3 — Actualizaciones en tiempo real | RF-REG-01, RF-REG-02, RF-REG-03, RF-REG-04, RF-REG-05, RF-ESC-08 |

## Cobertura de las preguntas del enunciado

| Pregunta del caso | RF que la responde |
|---|---|
| Qué ocurre si un paciente se agrava en el turno noche | RF-ESC-01, RF-ESC-06 |
| Cómo se contacta rápidamente al médico encargado | RF-ESC-01, RF-ESC-08 |
| Qué ocurre si el médico no está disponible | RF-ESC-02, RF-ESC-07, RF-ESC-09 |
| Cómo se avisa a varios médicos y enfermeras | RF-ESC-02, RF-ESC-05, RF-TUR-05 |
| Con qué garantía se conserva el diagnóstico | RF-DIA-07, RF-REG-02 |
| Cómo se sostiene su disponibilidad permanente | RF-DIA-04, RF-REG-02, `RNF-DIS-01`, `RNF-DIS-02` |

## Requerimientos de origen normativo

Estos RF no nacen de una tarea crítica sino de las restricciones externas declaradas en la sección 2.4
del [`README.md`](../README.md). Trazan igualmente a la persona sobre cuya operación recaen.

| Restricción externa | RF que la observa |
|---|---|
| Ley N.° 29733 — trazabilidad del acceso a datos de salud | RF-IAM-03 |
| Ley N.° 29733 — acceso limitado al ámbito de responsabilidad | RF-IAM-02 |
| Ley N.° 29733 — exposición de datos fuera del entorno institucional | RF-IAM-04 |
| SUSALUD — atribución cierta del registro clínico | RF-IAM-01, RF-DIA-07 |

## Decisión de tensiones

Cada tensión documentada en [`Personas/README.md`](../Personas/README.md) se decide en un RF. Una
tensión sin RF que la resuelva es una brecha de consistencia.

| Tensión | RF que la decide | Decisión adoptada |
|---|---|---|
| Velocidad frente a completitud del registro | RF-DIA-01 | Prevalece la completitud: el cierre de turno se bloquea ante una cama sin diagnóstico. El costo se traslada al esfuerzo de registro, acotado en `RNF-USA-01`. |
| Sensibilidad del escalamiento | RF-ESC-06 | No se impone ninguna de las dos posiciones: se admiten exactamente dos severidades con cadena y plazo propios, de modo que escalar ante la duda no consume la atención reservada al deterioro inmediato. |
| Autonomía de intercambio de turnos | RF-TUR-06 | El intercambio se pacta libremente pero no altera la programación vigente hasta que el coordinador lo resuelve: la responsabilidad de cobertura permanece indivisa. |
| Adopción voluntaria | RF-TUR-08, `RNF-USA-01`, `RNF-USA-02` | La adopción se sostiene acotando el esfuerzo de uso —registro y escalamiento medidos en `RNF-USA`— y conservando la salida imprimible que el equipo ya emplea. |
| Movilidad frente a control de datos | RF-IAM-04 | Se admite el dispositivo personal; lo que se restringe es el dato expuesto sin autenticación. La movilidad se conserva sin trasladar la identificación del paciente a un equipo no institucional. |

## Distribución de prioridad

| Prioridad | Cantidad | Proporción | Criterio aplicado |
|---|---|---|---|
| MUST | 28 | 66.7 % | Es la única cobertura de una tarea crítica, o su ausencia deja sin resolver un problema crítico |
| SHOULD | 12 | 28.6 % | Sostiene un criterio de éxito, o refuerza una tarea crítica que ya tiene cobertura MUST |
| COULD | 2 | 4.8 % | Preserva una práctica vigente del equipo sin condicionar la operación clínica |
