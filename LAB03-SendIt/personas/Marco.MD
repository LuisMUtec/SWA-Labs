---
persona: Marco Salas
rol: oficial de cumplimiento de SendIt — responde por que la empresa no mueva dinero que no debe mover
status: proto
---

# Marco Salas — oficial de cumplimiento

<!--
  Quién es esta persona y qué necesita. Nunca qué hace el sistema.
  La lee su agente de evaluación (../evals/README.md) y la cita el backlog.
  status: proto = la inventamos nosotros.
-->

Marco es la persona por la que el enunciado dice que **la seguridad es muy importante**. No es un
requisito técnico buscando dueño: es el trabajo de alguien. Y es también quien ordena la única
operación que rompe la consistencia si está mal hecha —detener dinero que ya está en movimiento—,
de modo que las dos exigencias del enunciado se cruzan en su escritorio.

## Contexto

<!-- Dónde vive o trabaja y de qué responde. Conducta, no demografía. -->

Marco responde por que SendIt no mueva dinero de quien no debe, hacia quien no debe, ni en la forma
en que se mueve el dinero que se está escondiendo. Responde personalmente: la licencia que permite
operar el corredor está atada a que exista alguien en su puesto haciendo exactamente esto, y las
sanciones por incumplir no las paga solo la empresa.

Su trabajo tiene dos filos y se corta con los dos. Un falso negativo —dejar pasar lo que no debía
pasar— puede cerrar SendIt. Un falso positivo —detener a Rosa— le cuesta a Rosa la medicina de su
madre, y Rosa no vuelve. Marco lo sabe: cada control que él necesita es fricción que sufre alguien
que no hizo nada. No está buscando detener más envíos; está buscando detener los mismos que hoy
detiene, pero antes, más rápido y con menos gente atrapada de paso.

Lo que hoy le arruina el trabajo es el orden de las cosas. El tamizaje corre después de aceptar el
dinero. Cuando salta una alerta, el envío ya está en camino, así que detenerlo no es dejar de
hacer algo: es deshacer algo, en un sistema donde parte del camino ya lo recorrió un tercero con su
propio registro contable. La mitad de sus casos no son «¿esto es sospechoso?» sino «¿dónde está
ahora ese dinero y quién puede pararlo?».

Y hay una asimetría que ninguna otra persona del conjunto vive: cuando Marco reporta una operación
a la autoridad, **está obligado a no decírselo al cliente**. No es una decisión de servicio, es una
prohibición. De modo que Rosa exige una explicación que Marco tiene prohibido darle, y ese choque
no se resuelve mejorando la redacción de un mensaje.

`[ASSUMPTION: Marco puede retener un envío por su cuenta hasta 72 horas. Más allá de ese plazo, o
para bloquear a un cliente de forma permanente, decide un comité. El plazo existe para que una
retención no pueda volverse indefinida por omisión.]`

`[ASSUMPTION: las listas de personas y entidades sancionadas provienen de fuentes externas que se
actualizan sin aviso, y una lista nueva puede alcanzar a un envío que ya fue aprobado con la lista
anterior.]`

## Flujo principal

<!-- Lo puntúa D1: el agente pregunta si esto corre de extremo a extremo en el backlog. -->

**Cuando** un envío coincide con una lista o rompe el patrón de quien lo manda, **quiero** decidirlo
antes de que el dinero salga y con la evidencia a la vista, **para** detener lo que hay que detener
sin retener a nadie más tiempo del que puedo justificar.

1. Veo la coincidencia o la anomalía antes de que el dinero se comprometa, no después.
2. Veo contra qué coincidió y con qué grado de parecido: el nombre, la lista, la fecha de esa lista.
   Un homónimo y una coincidencia exacta no son el mismo caso y no pueden llegarme iguales.
3. Veo el patrón de esa persona: qué manda normalmente, a quién, cada cuánto. Un envío de USD 300
   quincenal desde hace tres años y un envío de USD 2.900 a un destinatario nuevo son cosas
   distintas aunque el monto individual no lo diga.
4. Decido: liberar, retener por un plazo con un motivo registrado, o escalar. Si retengo, el plazo
   corre y se vence solo.
5. Cuando corresponde reportar, reporto — y el envío sigue el curso que la ley me obliga a darle,
   sin que el cliente reciba una explicación que tengo prohibido darle.
6. Meses después, cualquiera que revise el caso encuentra qué decidí, cuándo, con qué evidencia y
   contra qué versión de qué lista. Sin eso, mi decisión no vale nada aunque haya sido correcta.

**Cuando sale mal:** ordené detener un envío y el dinero ya había sido puesto a disposición en el
agente del destino. Mi sistema decía «retenido»; el del pagador decía «disponible para cobro». El
destinatario cobró. Durante dos días tuve una operación que estaba simultáneamente detenida y
pagada, y la única forma de saber cuál de las dos cosas era verdad fue llamar por teléfono. Cuando
tuve que explicarle eso a un auditor, lo que no pude explicar no fue la decisión: fue por qué mis
propios registros afirmaban dos hechos incompatibles sobre el mismo dinero.

## Qué se le interpone

<!-- Límites y frustraciones de hoy: tiempo, información, autoridad, dinero, distancia. Alimenta D2. -->

- El control corre después de aceptar el dinero, así que su herramienta no es detener sino revertir
  — y revertir cruza la frontera con el pagador, donde él ya no manda.
- Las alertas le llegan todas iguales. Un homónimo de una lista y una coincidencia exacta ocupan la
  misma fila de la misma pantalla, y el noventa y tantos por ciento son homónimos.
- Sin el patrón histórico de la persona no puede juzgar un envío suelto. Un monto no es sospechoso;
  un monto que no se parece a nada de lo que esa persona hizo antes, sí.
- Una retención sin plazo no la cierra nadie. Los casos que no se deciden no se pierden: se quedan
  reteniendo el dinero de alguien, en silencio, hasta que ese alguien reclama.
- Las listas cambian sin avisar. Un envío aprobado ayer puede estar prohibido hoy, y él no tiene
  cómo saber cuál de sus aprobaciones pasadas dejó de ser válida.
- No puede explicarle a Rosa por qué se detuvo su dinero, y no puede explicarle tampoco por qué no
  puede explicárselo.
- La evidencia sobre la que decidió está esparcida en pantallas que se refrescan. Si el dato que vio
  cambió después, no queda rastro de lo que él efectivamente tenía delante cuando decidió.

## Permisos

<!-- Qué puede y qué nunca debe poder hacer. Alimenta D4 cuando dos personas chocan. -->

- **Puede:** retener un envío antes de que el dinero se comprometa; retener uno en curso dentro de
  su plazo; exigir evidencia adicional al remitente antes de liberar; liberar con motivo registrado;
  reportar a la autoridad; escalar al comité lo que excede su plazo o su alcance.
- **Nunca debe:** mover, devolver ni redirigir dinero — decidir que un envío se detiene y tocar el
  dinero son dos trabajos de dos personas distintas; retener indefinidamente sin decisión del
  comité; revelar al cliente la existencia de un reporte a la autoridad; borrar o editar una
  decisión suya ya registrada, ni la evidencia sobre la que se tomó; consultar los datos de un
  cliente sin un caso abierto que lo justifique.

## Señal de éxito

<!-- Signo observable de que el sistema le funciona. Se vuelve título del backlog. -->

- Ninguna decisión suya se toma sobre dinero que ya salió: el control ocurre antes de comprometer,
  o el envío no ocurre.
- Un homónimo y una coincidencia exacta le llegan separados, y él dedica su tiempo a los segundos.
- Toda retención tiene plazo, y el plazo vencido produce una consecuencia por sí solo, sin depender
  de que alguien se acuerde.
- Una operación nunca figura en dos estados incompatibles a la vez, ni siquiera cruzando la
  frontera con el pagador.
- Un año después, la decisión, su momento, su evidencia y la versión de la lista contra la que se
  tomó siguen siendo recuperables y nadie pudo haberlas alterado.
