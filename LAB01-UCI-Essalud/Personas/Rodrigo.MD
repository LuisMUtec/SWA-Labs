# Rodrigo Salazar — Médico internista rotante

> Persona ancla del **Problema P1 — Rotación de doctor**.

## Perfil

| Campo | Valor |
|---|---|
| Edad | 31 |
| Rol | Médico internista, rotante en UCI |
| Institución | Red Prestacional Lima — rota entre 3 hospitales de la red |
| Turno / horario | Guardias de 12 h, esquema variable; rara vez dos días seguidos en la misma UCI |
| Antigüedad en la unidad | 4 meses (y no es su sede fija) |
| Nivel técnico | Medio |
| Dispositivo principal | PC compartida de la estación de enfermería; celular personal como respaldo |

## Contexto

Rodrigo terminó el residentado hace dos años y cubre turnos de UCI en varios hospitales de la red.
Casi nunca entra a una unidad donde conozca a los pacientes: llega, recibe entre 8 y 12 camas y tiene
unos 15 minutos de entrega de turno antes de que el médico saliente se vaya. Ese margen se acorta si
hay un ingreso o una emergencia en curso.

Su fuente de verdad hoy es una mezcla de kardex en papel, notas manuscritas de evolución y lo que el
colega saliente alcance a contarle de memoria. Cuando la nota está incompleta o ilegible, Rodrigo
reconstruye el caso leyendo laboratorios e imágenes desde cero, o llama por WhatsApp al médico que ya
salió — que puede estar dormido o simplemente no responder.

## Objetivos

- Formarse un cuadro clínico confiable de cada cama en los primeros 15 minutos del turno.
- Saber qué cambió desde la última vez que él vio a ese paciente (si es que lo vio).
- Identificar de inmediato qué pacientes están inestables o tienen pendientes críticos.
- Dejar su diagnóstico y plan registrados antes de retirarse, sin que eso le tome media hora.

## Frustraciones / Dolores actuales

- Notas de evolución incompletas, ilegibles o escritas a la carrera al final del turno.
- No existe un registro de qué se decidió y por qué; solo el resultado, sin razonamiento.
- Tener que llamar al médico saliente ya fuera del hospital para entender un caso.
- Repetir exámenes porque no encuentra los resultados previos.
- Firmar entregas de turno sin haber podido revisar realmente todas las camas.
- Sistemas que le piden ingresar de nuevo datos que ya están en otro sistema.

## Tareas críticas en el sistema

| # | Tarea | Frecuencia | Criticidad |
|---|---|---|---|
| 1 | Recibir el handoff estructurado de todas las camas asignadas | Al inicio de cada turno | Alta |
| 2 | Consultar la evolución y el diagnóstico del turno anterior | Al inicio y ante cualquier duda | Alta |
| 3 | Registrar nota de evolución y diagnóstico por paciente | Al menos 1 vez por turno por cama | Alta |
| 4 | Marcar pacientes inestables o con pendientes críticos | Continuo | Alta |
| 5 | Consultar resultados de laboratorio e imágenes | Varias veces por turno | Media |
| 6 | Cerrar y firmar la entrega de turno | Al final de cada turno | Alta |

## Escenario clave

**19:00, Hospital Almenara, UCI de 10 camas.** Rodrigo entra a una guardia nocturna en una unidad donde
estuvo por última vez hace tres semanas. El médico saliente tuvo dos ingresos en la tarde y va con
retraso: le entrega las camas en ocho minutos, en voz alta, en el pasillo.

En la cama 6 hay un paciente de 68 años, post-operado, que "estaba mejorando". A las 23:40 el paciente
se descompensa. Rodrigo necesita saber: qué antibiótico se inició y en qué día va, si hubo un cultivo
pendiente, por qué se decidió no escalar soporte esa mañana, y si la familia ya fue informada del
pronóstico. Nada de eso está en la nota; estaba en la cabeza del médico que ya se fue.

**Lo que el sistema debe garantizar:** que ese contexto exista, esté completo y sea legible sin que
Rodrigo tenga que llamar a nadie.

## Criterios de éxito

Rodrigo considera exitoso el sistema si:

- Puede entender el estado de las 10 camas en ≤ 15 minutos usando solo el sistema.
- El handoff incluye no solo datos, sino **decisiones y su justificación**.
- Ninguna cama le llega sin diagnóstico del turno anterior — y si falta, el sistema lo señala antes de
  que él acepte la entrega.
- Registrar su propia nota de evolución le toma menos de lo que le tomaba escribirla a mano.
- Puede ver qué cambió desde su último contacto con ese paciente, sin releer todo el historial.

## Restricciones

- Trabaja con guantes y bajo presión de tiempo; interfaces con muchos clics lo expulsan al papel.
- Usa PCs compartidas y a veces desactualizadas de la estación de enfermería.
- No es usuario frecuente de ningún hospital en particular: la interfaz debe ser idéntica en toda la red.
- No tiene tiempo de capacitación formal; debe poder usarlo bien desde el primer turno.
- Puede tener sesiones abiertas por otro médico en la misma máquina — el sistema no debe atribuirle
  notas que no escribió.
