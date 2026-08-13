# Aníbal Quispe — Médico intensivista de guardia localizable

> Segunda persona ancla del **Problema P2 — Medianoche**: el extremo receptor del escalamiento.

## Perfil

| Campo | Valor |
|---|---|
| Edad | 44 |
| Rol | Médico intensivista, guardia localizable (*on-call* desde domicilio) |
| Institución | Cubre en llamada 2 UCIs de la Red Prestacional Lima |
| Turno / horario | Localizable de 20:00 a 08:00, en bloques de 7 días |
| Antigüedad | 12 años como intensivista |
| Nivel técnico | Medio |
| Dispositivo principal | Celular personal, con datos móviles; laptop en casa |

## Contexto

Aníbal duerme en su casa mientras está de guardia localizable. Su rol es decidir a distancia: la mayoría
de llamadas se resuelven con una indicación por teléfono, y solo algunas ameritan que se vista y maneje
40 minutos hasta el hospital. Esa decisión —ir o no ir— la toma con la información que le den por
teléfono a las dos de la mañana.

El problema es que la llamada casi siempre llega sin contexto suficiente. Le describen un signo aislado
—"está desaturando"— sin la tendencia de las últimas horas, sin los parámetros del ventilador, sin saber
qué se le indicó en el turno previo. Aníbal termina haciendo diez preguntas por teléfono a una enfermera
que está al lado de un paciente inestable y que no debería estar contestando un interrogatorio.

También pasa lo contrario: casos que sí requerían su presencia y en los que nadie logró ubicarlo, porque
llamaron a un número viejo o porque el rol decía que el de guardia era otro.

## Objetivos

- Decidir **ir o no ir** con información suficiente y en pocos minutos.
- Recibir el escalamiento con el contexto ya adjunto, sin tener que pedirlo.
- Que quien lo llama sepa que él ya está enterado y en camino a responder.
- No perderse una llamada que sí importaba.
- Delegar formalmente cuando esté genuinamente indisponible.

## Frustraciones / Dolores actuales

- Recibir "está mal el de la cama 3" sin ningún dato objetivo alrededor.
- Interrogar por teléfono a una enfermera que debería estar atendiendo al paciente.
- No poder ver la tendencia de signos vitales ni los parámetros actuales del ventilador.
- Viajar 40 minutos al hospital por algo que se resolvía con una indicación.
- Enterarse en la mañana de un evento nocturno que nadie le escaló.
- Que su indicación telefónica no quede registrada en ningún lado, y después no exista constancia.

## Tareas críticas en el sistema

| # | Tarea | Frecuencia | Criticidad |
|---|---|---|---|
| 1 | Recibir la alerta de escalamiento con contexto clínico adjunto | 0–4 veces por noche | Crítica |
| 2 | Confirmar recepción y tomar el caso | Ante cada alerta | Crítica |
| 3 | Consultar tendencia de signos, ventilación y última evolución | Ante cada alerta | Alta |
| 4 | Registrar la indicación dada de forma remota | Ante cada alerta atendida | Alta |
| 5 | Marcarse temporalmente indisponible y delegar | Ocasional | Alta |
| 6 | Revisar en la mañana lo ocurrido durante la noche | Diaria | Media |

## Escenario clave

**03:20, en su casa.** Suena el celular de Aníbal. Es la UCI del hospital B, donde no estuvo
físicamente en tres semanas. Le dicen que un paciente post-quirúrgico está hipotenso y que ya le
pasaron volumen.

Aníbal necesita, en ese momento: la presión de las últimas seis horas y no solo la actual, el balance
hídrico del día, si hay lactato reciente, qué antibiótico recibe y en qué día va, si hay vasopresor
corriendo y a qué dosis, y qué decidió el intensivista del turno diurno. Con eso decide si indica
noradrenalina por teléfono o si maneja al hospital.

Hoy consigue esa información preguntando de a poco, mientras la enfermera va y viene entre el monitor,
el kardex y el teléfono. Toma once minutos.

**Lo que el sistema debe garantizar:** que la alerta llegue con ese paquete de contexto ya armado, que
Aníbal pueda confirmar recepción con un toque, y que su indicación quede registrada y atribuida a él
sin necesidad de una PC.

## Criterios de éxito

Aníbal considera exitoso el sistema si:

- La alerta incluye el contexto clínico mínimo **sin que él tenga que pedirlo**.
- Puede decidir ir o no ir en menos de 3 minutos desde que recibe la alerta.
- Confirmar recepción le toma un toque, y quien escaló lo ve de inmediato.
- Puede registrar su indicación remota desde el celular, y queda con hora y autoría.
- Si él no responde en el tiempo definido, el sistema escala solo — y él se entera de que ocurrió.
- Al día siguiente puede revisar en un solo lugar todo lo que pasó en la noche.

## Restricciones

- Recibe las alertas dormido: la interfaz debe ser legible y operable con la mínima carga cognitiva.
- Usa datos móviles de calidad variable; a veces solo tiene 3G o señal débil.
- Usa su **celular personal**: el sistema no puede exigir un dispositivo institucional ni exponer datos
  del paciente en la pantalla de bloqueo.
- Cubre dos hospitales: toda alerta debe identificar sede, cama y paciente sin ambigüedad.
- No puede depender de tener una laptop encendida ni de una VPN corporativa.
- El escalamiento debe distinguir urgencia real de consulta rutinaria; si todo llega como crítico,
  deja de responder a todo.
