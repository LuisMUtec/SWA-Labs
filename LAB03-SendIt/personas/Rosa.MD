---
persona: Rosa Quispe
rol: peruana que trabaja en Estados Unidos y sostiene a su madre en Ayacucho
status: proto
usuario_modelo: true
---

# Rosa Quispe — remitente

<!--
  Quién es esta persona y qué necesita. Nunca qué hace el sistema.
  La lee su agente de evaluación (../evals/README.md) y la cita el backlog.
  status: proto = la inventamos nosotros.

  [ASSUMPTION: el enunciado no nombra a nadie ni fija un corredor. Rosa modela el corredor
  Estados Unidos → Perú, que es el de mayor volumen hacia el país; el diseño debe sostenerse si
  el corredor cambia, y donde no se sostenga hay que marcarlo.]
-->

**Rosa es el usuario modelo del caso.** Es quien decide usar SendIt o abandonarlo, quien paga, y
la única de las tres personas que elige libremente. Elena recibe lo que Rosa mandó por donde Rosa
lo mandó, y Marco trabaja dentro de SendIt. Si el diseño no resuelve el día de Rosa, no hay
sistema que diseñar.

## Contexto

<!-- Dónde vive o trabaja y de qué responde. Conducta, no demografía. -->

Rosa limpia casas en Paterson, Nueva Jersey. Cobra parte en efectivo y parte por transferencia
instantánea de sus clientas, y no siempre el mismo día. Cada quincena manda a Huanta lo que pudo
juntar: entre 200 y 400 dólares.

Ese dinero no es un ahorro ni un regalo. Paga las medicinas de su madre y el colegio del sobrino
que vive con ella, y ambas cosas tienen fecha. Rosa no está comprando un envío: está comprando una
llegada. Lo que necesita saber es cuántos soles va a tener su madre en la mano y qué día, y todo lo
demás —la comisión, el tipo de cambio, quién es el banco corresponsal— le importa solo en la medida
en que mueva esa cifra.

Por eso la publicidad de «cero comisión» la enfureció la primera vez que entendió lo que era: no le
cobraron comisión y le dieron cuatro por ciento menos de soles por dólar. Rosa no distingue una
cosa de la otra ni tiene por qué; la única cifra que puede verificar es la que su madre cuenta al
salir de la bodega.

`[ASSUMPTION: Rosa envía dos veces al mes, entre USD 200 y USD 400, y su patrón es estable desde
hace tres años. Ese patrón es lo que la hace reconocible y también lo que hace ruidosa cualquier
alerta que se dispare por un envío fuera de rango.]`

`[ASSUMPTION: Rosa opera desde un teléfono propio con datos móviles. Es su único canal.]`

## Flujo principal

<!-- Lo puntúa D1: el agente pregunta si esto corre de extremo a extremo en el backlog. -->

**Cuando** junté el dinero de la quincena, **quiero** que mi madre tenga una cantidad de soles que
yo conozca de antemano, en una fecha que yo conozca de antemano, **para** poder decirle cuándo ir a
cobrar sin hacerla viajar en vano.

1. Digo cuánto quiero mandar, y veo cuántos soles va a recibir Elena — el número final, ya con todo
   descontado, antes de comprometer un centavo.
2. Digo dónde y cómo lo va a cobrar: efectivo en la bodega-agente de Huanta, que es lo único que le
   sirve a mi madre.
3. Pago. A partir de ahí el monto en soles que vi es el monto que Elena cobra, aunque el dólar se
   mueva mientras el envío viaja.
4. Sé en qué estado está el envío sin tener que preguntar, y sé cuándo el dinero ya está
   disponible para que Elena vaya.
5. Cuando Elena cobra, me entero. Ese es el final del envío: no cuando SendIt lo despachó, sino
   cuando mi madre tiene los billetes.

**Cuando sale mal:** mandé un lunes y el martes no había pasado nada. La app decía «en proceso» y
nada más. Llamé, y una persona me dijo que estaba «en revisión» y que no podía darme más detalle.
Al sexto día apareció el dinero, sin explicación y sin que nadie me avisara. En esos seis días mi
madre se quedó sin una medicina y yo mandé cien dólares más por otro servicio, más caro, para
cubrir el hueco — de modo que cuando el primer envío por fin llegó, había mandado el doble de lo
que podía. Nadie me devolvió esos seis días ni la comisión del envío de emergencia. Lo que necesito
no es que nunca me revisen: es saber, el mismo lunes, que hay una revisión, cuánto puede durar como
máximo, y que si se pasa de ese plazo el dinero vuelve a mi cuenta sin que yo tenga que pelearlo.

## Qué se le interpone

<!-- Límites y frustraciones de hoy: tiempo, información, autoridad, dinero, distancia. Alimenta D2. -->

- El precio verdadero está partido en dos —comisión y tipo de cambio— y solo la comisión se
  anuncia. Comparar dos servicios exige una aritmética que Rosa hace en el bus y con la que a veces
  se equivoca.
- Entre que paga y que su madre cobra pasan horas o días, y en ese intervalo el tipo de cambio se
  mueve. Si el monto en soles se fija recién al cobrar, Rosa nunca pudo prometer una cifra.
- El estado «en proceso» no distingue entre «va bien y falta poco» y «hay un problema y nadie te lo
  va a decir». Rosa reacciona igual ante los dos: llama, y luego manda de nuevo.
- Su madre no tiene cuenta bancaria ni teléfono con datos. Todo lo que Rosa elija tiene que
  terminar en efectivo, en un lugar al que Elena pueda llegar.
- Rosa trabaja de día en casas ajenas. No puede pasar cuarenta minutos en una llamada ni ir a una
  oficina en horario de atención.
- Cuando algo se detiene, Rosa no tiene a quién reclamarle con efecto. El servicio le responde que
  «se está revisando», y ella no tiene forma de saber si eso significa dos horas o dos semanas.
- Una devolución no la deja como estaba: le devuelven los dólares pero el envío que hizo para
  tapar el hueco ya se cobró su comisión, y la fecha de la medicina ya pasó.

## Permisos

<!-- Qué puede y qué nunca debe poder hacer. Alimenta D4 cuando dos personas chocan. -->

- **Puede:** iniciar un envío; ver el monto exacto que recibirá Elena antes de pagar; elegir cómo y
  dónde cobra Elena entre las formas disponibles en el destino; consultar el estado de cualquier
  envío suyo; cancelar un envío mientras el dinero no haya sido puesto a disposición de Elena;
  reclamar la devolución cuando un envío excede el plazo prometido.
- **Nunca debe:** conocer el motivo de una retención cuando informarlo está prohibido por la
  obligación de reserva de Marco; alterar el destinatario de un envío ya pagado, porque eso
  convierte una verificación hecha sobre una persona en un pago a otra; cobrar ella misma en el
  destino; ver, corregir ni exportar los datos de identidad que Elena entregó al agente pagador.

## Señal de éxito

<!-- Signo observable de que el sistema le funciona. Se vuelve título del backlog. -->

- El número de soles que Rosa vio antes de pagar es el número de soles que Elena cuenta al cobrar.
  Si difiere, difiere por una razón que Rosa aceptó antes de pagar.
- Rosa sabe, sin preguntarle a nadie, si su envío está en camino o detenido — y cuando está
  detenido, sabe hasta cuándo puede estarlo.
- Rosa se entera de que Elena cobró, sin que Elena tenga que avisarle.
- Un envío que no se completa devuelve el dinero a Rosa dentro de un plazo que Rosa conocía desde
  el principio, sin que ella tenga que reclamarlo.
- Rosa nunca paga dos veces por el mismo envío, ni siquiera cuando la app se le cierra a mitad del
  pago y vuelve a entrar.
