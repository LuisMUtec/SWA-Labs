---
persona: Kevin Ramos
rol: cajero de la ventanilla de un agente de la red — identifica, cobra y paga
status: proto
usuario_modelo: false
---

# Kevin Ramos — operario de ventanilla

<!--
  Quién es esta persona y qué necesita. Nunca qué hace el sistema.
  La lee su agente de evaluación (../evals/README.md) y la cita el backlog.
  status: proto = la inventamos nosotros.

  [ASSUMPTION: el modelo Western Union —red de agentes con efectivo en las dos puntas— hace
  que exista un mostrador y alguien detrás de él. Kevin modela ese puesto en las dos puntas
  del corredor: es quien atiende a Rosa en Paterson y quien atiende a Elena en Huanta. Si
  SendIt originara desde una aplicación, esta persona no existiría en el origen y la mitad de
  su flujo se caería.]
-->

Kevin **encarna la exigencia de seguridad del enunciado**, y conviene decir en qué sentido:
no porque la aplique, sino porque es **por donde se rompe**. Está solo frente al mostrador,
maneja efectivo, y puede crear giros y pagarlos. Un mecanismo de seguridad que no lo contemple
a él está protegiendo la puerta equivocada.

## Contexto

<!-- Dónde vive o trabaja y de qué responde. Conducta, no demografía. -->

Kevin atiende el mostrador de un negocio afiliado a la red de SendIt. El negocio no es de
SendIt: es una bodega, una farmacia, una casa de cambio que además manda y paga remesas. Kevin
atiende remesas entre todo lo demás que hace y no es especialista en cumplimiento ni en
prevención de fraude. Aprendió el procedimiento mirando, y lo que sabe de las reglas es lo que
la pantalla le deja o no le deja hacer.

El efectivo con el que paga es de su empleador, no de SendIt: SendIt se lo repone después. Eso
lo vuelve conservador de una forma muy concreta —**pagar de más le cuesta a él**— y explica por
qué prefiere rechazar en la duda, aunque el que se vaya sin su dinero sea alguien que viajó
medio día para llegar.

`[ASSUMPTION: el agente es un tercero afiliado y el efectivo es suyo, liquidado después. Si los
locales fueran propios de SendIt, la segunda autorización y el mínimo privilegio pierden la
mitad de su razón de ser: dejarían de proteger a SendIt de su propia red.]`

`[ASSUMPTION: Kevin no tiene autoridad para decidir sobre una retención ni para levantarla. Su
papel frente a ella es decir algo a la persona que tiene delante, y no tiene qué decir.]`

## Flujo principal

<!-- Lo puntúa D1: el agente pregunta si esto corre de extremo a extremo en el backlog. -->

**Cuando** alguien llega al mostrador a enviar o a cobrar, **quiero** resolverlo en pocos
minutos sabiendo que no me estoy equivocando, **para** atender al siguiente sin quedarme con la
duda ni con la pérdida.

1. Pido el documento y verifico que la persona que tengo delante sea la del documento.
2. **Si envía:** registro destinatario, país y monto, y el sistema me dice si puede o no antes
   de que yo toque el efectivo.
3. Si el monto lo exige, pido la segunda autorización **antes** de recibir el dinero, no
   después.
4. Recibo el efectivo y recién entonces la operación queda cerrada. Entrego el código.
5. **Si cobra:** verifico el código contra el documento, y pago solo si el sistema me dice que
   el giro está disponible y no fue pagado antes.
6. Cierro la operación sabiendo en qué estado quedó, sin tener que deducirlo.

**Cuando sale mal:** el sistema me deja a mitad de camino. Cobré el efectivo y la pantalla se
cortó antes de confirmar, y no sé si el giro quedó creado —si lo vuelvo a registrar, ¿la señora
mandó dos veces?—. O pagué, se cayó la conexión, y no sé si quedó marcado como pagado o si el
próximo que venga con ese código va a cobrar otra vez, con la plata de mi patrón. Ese es el
momento exacto en que el dinero se pierde, y el que lo pone soy yo. Lo que necesito no es que
nunca se corte: es que cuando se corte, la pantalla me diga en qué estado quedó y me deje
retomar sin adivinar.

**Y el otro caso malo:** el sistema me dice que no puedo pagar y no me dice por qué, o me dice
algo que tengo prohibido repetir. La señora del otro lado del mostrador viajó medio día, y yo
soy la cara de SendIt para ella. Que la decisión no sea mía no significa que la conversación no
sea mía.

## Qué se le interpone

<!-- Límites y frustraciones de hoy: tiempo, información, autoridad, dinero, distancia. Alimenta D2. -->

- Tiene cola esperando. Cada verificación que agrega un minuto la paga con la gente que se va,
  y esa gente es la clientela del negocio de su empleador, no la de SendIt.
- No sabe si una coincidencia con una lista es un homónimo o algo serio, **y no le corresponde
  decidirlo** — pero es él quien tiene que decirle algo a la persona que tiene delante.
- Cuando el nombre del documento no coincide exactamente con el que puso quien envió —una
  letra, un apellido de más, un documento vencido— la decisión de pagar o no recae sobre él, y
  es la que más le puede costar.
- No tiene forma de saber si alguien ya operó hoy en otra ventanilla de la red, salvo que el
  sistema se lo diga.
- El efectivo de la caja es finito y nadie le avisa cuánto le queda para pagos del día.
- Aprendió mirando. Cada excepción que el procedimiento no cubre la resuelve con criterio
  propio, y su criterio propio es exactamente lo que un defraudador va a buscar.

## Permisos

<!-- Qué puede y qué nunca debe poder hacer. Alimenta D4 cuando dos personas chocan. -->

- **Puede:** identificar a quien envía y crear giros dentro de su límite; verificar a quien
  cobra y pagar contra código y documento coincidente; ver los datos de la operación que está
  atendiendo; detener una operación y escalarla a quien sí decide.
- **Nunca debe:** completar solo un giro por encima del umbral reforzado; pagar un giro ya
  pagado; pagar antes de que los fondos del origen estén confirmados; alterar ni borrar el
  registro de un giro ya pagado; ver el historial de quien envía o de quien cobra más allá de
  la operación en curso; conocer el código completo de giros que no está pagando; cancelar el
  giro de un remitente, que es una facultad de quien puso el dinero; revelar el motivo de una
  retención cuando informarlo está prohibido.

## Señal de éxito

<!-- Signo observable de que el sistema le funciona. Se vuelve título del backlog. -->

- Una operación interrumpida a la mitad queda en un estado que él puede leer y retomar, sin
  tener que adivinar si cobró o no, y sin que reintentar produzca un segundo giro ni un segundo
  pago.
- Nunca paga dos veces el mismo giro, **aunque quiera** — y esa es la formulación correcta: el
  control no depende de su honestidad.
- Cuando el sistema le dice que no, le dice también qué corresponde ofrecerle a la persona que
  tiene delante, sin exponer nada que él no deba repetir.
- Ninguna operación grande queda cerrada por él solo, y él lo prefiere: es lo que lo protege
  cuando alguien pregunte quién autorizó qué.
