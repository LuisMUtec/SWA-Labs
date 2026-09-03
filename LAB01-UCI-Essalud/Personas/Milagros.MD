# Milagros Chávez — Enfermera asistencial de UCI, turno noche

> Persona ancla de los **Problemas P2 — Medianoche** y **P3 — Actualizaciones en tiempo real**.

## Perfil

| Campo | Valor |
|---|---|
| Edad | 38 |
| Rol | Licenciada en enfermería, asistencial de UCI |
| Institución | Hospital de la Red Prestacional Lima — sede fija |
| Turno / horario | Turno noche, 19:00 – 07:00 |
| Antigüedad en la unidad | 11 años |
| Nivel técnico | Medio-bajo |
| Dispositivo principal | PC compartida de la estación; teléfono fijo de la unidad |

## Contexto

Milagros trabaja de noche con una colega y un técnico para 10 camas. Es quien está físicamente al lado
del paciente y quien nota primero cualquier deterioro: un cambio de patrón en el monitor, una diuresis
que cae, una piel que se pone marmórea.

De noche no hay médico intensivista en la unidad. Hay un internista de guardia que cubre también otros
servicios, y un intensivista localizable desde su casa. Cuando algo se complica, Milagros tiene que
encontrar a alguien: revisa el rol de turnos impreso pegado en la pared —que suele estar
desactualizado—, llama al anexo, y si no contesta empieza a marcar celulares de una lista escrita a
mano en un cuaderno.

Documenta todo en el kardex de enfermería en papel y transcribe una parte al sistema al final del
turno, cuando le alcanza el tiempo.

## Objetivos

- Escalar un deterioro y tener a un médico respondiendo en el menor tiempo posible.
- Saber **con certeza** quién está de guardia ahora mismo y cómo contactarlo.
- Registrar lo que pasa sin alejarse de la cama más de lo necesario.
- Que su registro quede como respaldo de que ella sí avisó, a qué hora y a quién.

## Frustraciones / Dolores actuales

- El rol de turnos pegado en la pared no coincide con quién está realmente de guardia.
- Llamar a tres números antes de que alguien conteste, con el paciente descompensándose.
- No saber si el médico ya vio su mensaje o si tiene que volver a llamar.
- Doble registro: papel primero, sistema después; termina el turno transcribiendo.
- Sistemas que la obligan a ir a la PC de la estación para registrar algo urgente.
- Cuando algo sale mal, no tener cómo demostrar a qué hora avisó.
- Cuando el primer médico no responde, tener que decidir sola cuánto esperar y a quién llamar después.
- Recibir una indicación médica por teléfono sin constancia clara de hora y autoría, y depender del papel
  para respaldar qué debía ejecutar.
- Que el WiFi falle durante un escalamiento y no saber si la alerta salió o quedó registrada, sin soporte
  de TI disponible durante la noche.

## Tareas críticas en el sistema

| # | Tarea | Frecuencia | Criticidad |
|---|---|---|---|
| 1 | Registrar signos vitales y balance por paciente | Cada 1–2 h por cama | Alta |
| 2 | Escalar un deterioro clínico al médico responsable | Impredecible, 0–4 veces por turno | Crítica |
| 3 | Consultar quién está de guardia y su estado de disponibilidad | Ante cada escalamiento | Crítica |
| 4 | Ver y confirmar indicaciones médicas vigentes | Continuo | Alta |
| 5 | Registrar eventos y administración de medicamentos | Continuo | Alta |
| 6 | Recibir y entregar el turno de enfermería | 2 veces por turno | Alta |

## Escenario clave

**02:15.** El paciente de la cama 3 empieza a desaturar. Milagros aumenta el oxígeno, toma signos y
decide que necesita al médico ahora.

Busca el rol en la pared: dice "Dr. Paredes". Llama al anexo: nadie contesta —el Dr. Paredes está
atendiendo una emergencia en otro piso. Busca en su cuaderno el celular del intensivista localizable;
el número es de hace dos años. Llama a la central telefónica del hospital para que le den el número
actualizado. Han pasado nueve minutos y todavía no habla con ningún médico.

**Lo que el sistema debe garantizar:** que un escalamiento llegue a alguien que efectivamente pueda
responder, que Milagros vea que fue recibido, y que si nadie responde en un tiempo definido, el sistema
escale solo al siguiente en la cadena sin que ella tenga que adivinar a quién llamar.

## Criterios de éxito

Milagros considera exitoso el sistema si:

- Puede escalar un deterioro en **menos de 30 segundos** desde que decide hacerlo.
- Ve quién está de guardia **en este momento**, no según un rol programado hace un mes.
- Recibe confirmación visible de que el médico vio la alerta, con la hora.
- Si nadie responde, el sistema escala automáticamente sin que ella intervenga.
- Puede registrar a pie de cama, sin caminar hasta la estación.
- Deja de transcribir del papel al sistema al final del turno.

## Restricciones

- Trabaja con guantes; a veces con doble guante y en aislamiento de contacto.
- Con frecuencia tiene una sola mano libre.
- La unidad tiene ruido de alarmas constante: las notificaciones sonoras se pierden.
- La PC de la estación es compartida entre tres personas y está a varios metros de las camas.
- La conectividad WiFi dentro de la unidad es intermitente.
- De noche no hay soporte de TI disponible.
- No tolera flujos largos: si escalar toma más de dos pasos, vuelve al teléfono.
