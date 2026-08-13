# Carmen Rojas — Jefa de UCI / coordinadora de programación

> Persona ancla de la meta **"horarios sin cruces"** y del cumplimiento de **P1** a nivel de unidad.

## Perfil

| Campo | Valor |
|---|---|
| Edad | 47 |
| Rol | Médico intensivista, jefa de la Unidad de Cuidados Intensivos |
| Institución | Hospital de la Red Prestacional Lima — sede fija |
| Turno / horario | Administrativo 08:00 – 16:00, más guardias asistenciales |
| Antigüedad en la unidad | 15 años, 6 como jefa |
| Nivel técnico | Medio |
| Dispositivo principal | Laptop de oficina; celular fuera de horario |

## Contexto

Carmen es responsable de que las 10 camas de su UCI tengan cobertura médica las 24 horas, los 365 días.
Arma la programación mensual en una hoja de Excel que heredó de su antecesor: filas por profesional,
columnas por día, colores por tipo de turno. La publica impresa en la unidad y la envía por WhatsApp al
grupo del servicio.

El plan sobrevive intacto unos tres días. Después empiezan los cambios: licencias por enfermedad,
permisos, capacitaciones, intercambios que los médicos pactan entre ellos y le avisan después —o no le
avisan. Rotantes que la Red le asigna o le quita sin consultarle. Cada cambio obliga a revisar
manualmente que nadie quede con dos turnos simultáneos, que nadie exceda las horas permitidas y que
ninguna franja quede descubierta.

Además responde ante la Dirección de Red por indicadores: cobertura, cumplimiento de entregas de turno
y trazabilidad de la documentación clínica.

## Objetivos

- Publicar una programación mensual sin cruces ni franjas descubiertas.
- Absorber cambios de último minuto sin rehacer todo el mes.
- Que todos vean la misma versión vigente del rol, siempre.
- Comprobar que las entregas de turno se están cumpliendo y documentando.
- Responder a la Red con datos y no con estimaciones.

## Frustraciones / Dolores actuales

- Detectar cruces a mano, revisando celda por celda en Excel.
- Enterarse de un intercambio de turnos después de que ocurrió.
- Convivir con varias versiones del rol circulando por WhatsApp.
- No tener forma de saber si el internista saliente dejó su diagnóstico registrado.
- Descubrir una franja sin cobertura cuando ya empezó el turno.
- Que le pidan indicadores que solo puede armar contando a mano.

## Tareas críticas en el sistema

| # | Tarea | Frecuencia | Criticidad |
|---|---|---|---|
| 1 | Elaborar y publicar la programación mensual de turnos | Mensual | Alta |
| 2 | Validar que no existan cruces ni franjas descubiertas | Ante cada cambio | Crítica |
| 3 | Aprobar o rechazar intercambios y permisos | Varias veces por semana | Alta |
| 4 | Reasignar cobertura ante una ausencia imprevista | 2–5 veces por mes | Crítica |
| 5 | Monitorear cumplimiento y completitud de entregas de turno | Semanal | Alta |
| 6 | Generar indicadores de cobertura para la Dirección de Red | Mensual | Media |

## Escenario clave

**Viernes, 15:40.** Carmen está por salir cuando le avisan que el internista programado para la guardia
nocturna del sábado presentó descanso médico. Tiene que encontrar reemplazo para un turno de 12 horas
que empieza en 27 horas.

Necesita saber quién está disponible ese sábado, quién no excede sus horas del mes, quién no está ya
asignado en otro hospital de la red, y a quién le corresponde por rotación. Hoy eso significa abrir el
Excel, cruzarlo mentalmente con lo que recuerda de los permisos, y empezar a llamar uno por uno. Si se
equivoca y asigna a alguien que ya tiene turno en otra sede, el error recién aparece el sábado a las
19:00 — con una UCI sin médico.

**Lo que el sistema debe garantizar:** que Carmen vea candidatos elegibles y libres de conflicto, que el
sistema rechace una asignación que genere cruce, y que la publicación del cambio llegue a todos los
afectados con confirmación de lectura.

## Criterios de éxito

Carmen considera exitoso el sistema si:

- El sistema **impide** guardar una asignación que produzca un cruce, en vez de solo advertirlo.
- Cubrir una ausencia imprevista le toma minutos, no una tarde de llamadas.
- Existe una sola versión vigente del rol, visible para todos y con historial de cambios.
- Puede ver en cualquier momento qué franjas de los próximos 7 días están descubiertas.
- Puede saber qué entregas de turno se cerraron sin diagnóstico registrado.
- Los indicadores para la Red salen del sistema sin trabajo manual.

## Restricciones

- La programación debe respetar límites de horas y descansos del régimen laboral vigente.
- Un mismo profesional puede estar asignado a más de un hospital de la red: los cruces son
  **entre sedes**, no solo dentro de su unidad.
- Carmen no tiene autoridad sobre los rotantes que asigna la Red; los recibe como un dato.
- No puede exigir a su equipo que aprenda una herramienta compleja: la adopción es voluntaria en la
  práctica, y si el sistema estorba vuelven al Excel y al WhatsApp.
- Necesita seguir pudiendo exportar el rol a un formato imprimible para la pared de la unidad.
