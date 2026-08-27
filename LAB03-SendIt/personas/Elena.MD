---
persona: Elena Quispe
rol: destinataria en Huanta, Ayacucho — cobra en efectivo y no tiene teléfono con datos
status: proto
---

# Elena Quispe — destinataria

<!--
  Quién es esta persona y qué necesita. Nunca qué hace el sistema.
  La lee su agente de evaluación (../evals/README.md) y la cita el backlog.
  status: proto = la inventamos nosotros.
-->

Elena existe en este conjunto por una razón concreta: **el corredor no termina en la aplicación de
Rosa, termina en la mano de Elena.** Un diseño que declara un envío completado cuando el dinero
llegó al agente pagador no resolvió el día de nadie. Elena es la prueba de que el último tramo —el
que no tiene pantalla— también es parte del sistema.

## Contexto

<!-- Dónde vive o trabaja y de qué responde. Conducta, no demografía. -->

Elena tiene 68 años y vive en Huanta. Su teléfono hace llamadas y recibe mensajes de texto; no
tiene datos, ni aplicación, ni correo. No tiene cuenta bancaria y no quiere abrir una: la sucursal
más cercana está en Ayacucho y la última vez que intentó le pidieron un comprobante de domicilio
que no tiene a su nombre.

Cobra en una bodega de la plaza que además es agente de varios servicios de remesa. Le queda a
cuarenta minutos en combi, y la combi pasa cuando pasa. El bodeguero la conoce de toda la vida, lo
cual resuelve muchas cosas informalmente y crea el problema exactamente opuesto: cuando algo falla,
Elena no tiene a quién reclamarle que no sea su vecino.

Su DNI está vencido desde hace catorce meses. La foto es de cuando tenía cincuenta.

`[ASSUMPTION: el destino se cobra en efectivo en un agente de una red de terceros, no en una
sucursal propia de SendIt. La red pagadora es un tercero con su propio registro contable, y esa
frontera es donde el dinero puede figurar entregado de un lado y pendiente del otro.]`

`[ASSUMPTION: el canal disponible hacia Elena es la llamada y el mensaje de texto. No se le puede
exigir instalar nada ni leer un correo.]`

## Flujo principal

<!-- Lo puntúa D1: el agente pregunta si esto corre de extremo a extremo en el backlog. -->

**Cuando** mi hija manda dinero, **quiero** saber que ya está y cuánto es antes de tomar la combi,
**para** no hacer el viaje dos veces ni volver con menos de lo que me dijeron.

1. Me entero de que hay dinero para mí, por el canal que tengo: una llamada o un mensaje de texto.
2. Sé cuánto es, en soles, antes de salir de mi casa. Ese número tiene que ser el mismo que Rosa me
   dijo por teléfono.
3. Sé que en ese agente hay efectivo hoy para pagarme, y no me entero de que no lo hay al llegar.
4. Me identifico con lo que tengo encima y cobro el monto completo.
5. El envío queda cerrado cuando conté los billetes — no antes.

**Cuando sale mal:** viajé, hice la cola, y el bodeguero me dijo que el sistema no le dejaba pagar
porque mi documento estaba vencido. Rosa había mandado el dinero a mi nombre tal como figura en ese
documento. Volví a mi casa, llamé a Rosa a Estados Unidos —donde eran las cinco de la mañana— y ella
tuvo que llamar al servicio y explicar quién era yo. Tres días después pude cobrar. La otra vez que
salió mal fue distinta: cobré, pero me dieron treinta soles menos de los que Rosa me había dicho, y
el bodeguero me explicó que era «por el cambio». No supe si le estaban cobrando a Rosa, si me
estaban cobrando a mí, o si el bodeguero se los había quedado, y no tenía cómo averiguarlo.

## Qué se le interpone

<!-- Límites y frustraciones de hoy: tiempo, información, autoridad, dinero, distancia. Alimenta D2. -->

- No tiene el canal por el que el sistema quiere hablarle. Todo aviso que dependa de una aplicación
  o de un correo, para Elena no existe.
- Su documento está vencido y su foto no se le parece. Cualquier verificación pensada para una
  persona con documentos en regla la deja afuera, y la deja afuera del lado donde ya no hay a quién
  pedirle ayuda.
- El viaje al agente cuesta dinero y medio día. Un viaje en vano no es una molestia: es una pérdida.
- El efectivo del agente es finito y nadie le informa cuánto queda. Descubre que no alcanza cuando
  ya está ahí.
- No puede distinguir un descuento legítimo de un cobro indebido del agente, porque el único que le
  explica la cifra es el que se la está pagando.
- Cuando algo se traba, el único con capacidad de reclamar es Rosa, que está a ocho mil kilómetros y
  cinco husos horarios. Elena depende de despertarla.
- No tiene forma de saber si el dinero «llegó» en el sentido del sistema o en el sentido que a ella
  le sirve, que es el de poder retirarlo hoy.

## Permisos

<!-- Qué puede y qué nunca debe poder hacer. Alimenta D4 cuando dos personas chocan. -->

- **Puede:** conocer el monto que le corresponde y su disponibilidad antes de viajar; identificarse
  con los medios que el destino admita; cobrar el monto íntegro; que el cierre del envío quede
  registrado en el momento en que recibe el dinero.
- **Nunca debe:** modificar el monto ni el destinatario de un envío; cobrar en nombre de otra
  persona; pagar por recibir, ni al agente ni a nadie — todo cargo que exista es cargo de Rosa y
  Rosa lo vio antes de pagar; iniciar un envío desde el destino, porque eso convierte un cobro en
  una ruta de retorno que nadie verificó.

## Señal de éxito

<!-- Signo observable de que el sistema le funciona. Se vuelve título del backlog. -->

- Elena no viaja hasta que el dinero está disponible para ella en ese agente, y lo sabe por el
  canal que tiene.
- El monto que le pagan es el monto que Rosa vio. Cualquier diferencia tiene un nombre y un
  responsable, y ninguno de los dos es el bodeguero.
- Un problema de identidad de Elena se resuelve sin que Rosa tenga que despertarse a las cinco de la
  mañana.
- Un envío no queda cerrado mientras Elena no haya cobrado, ni siquiera cuando el agente ya recibió
  el dinero.
- Elena nunca cobra dos veces el mismo envío, ni un envío que ya fue devuelto a Rosa.
