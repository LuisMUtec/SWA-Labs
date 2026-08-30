# Correcciones pendientes — ronda 14

Derivadas de la [iteración 13](iterations/2026-08-27-13.md), que cerró en **7,66 / 10**. Backlog
vigente: **174 RF + 18 RNF = 192 ítems**, congelado en `13b1fdb`.

## Aritmética del gate

| Escenario | D1 | D2 | D3 | D4 | Total |
|---|---|---|---|---|---|
| Hoy (ronda 13) | 1,5 | 3,0 | 1,5 | 1,66 | **7,66** |
| Con **dos cualesquiera** de los bloques 1–3 | 2,5 | 3,0 | 1,5 | ≈1,7 | **≈ 8,7** |
| Con los bloques 1–3 | 3,0 | 3,0 | 1,5 | ≈1,7 | **≈ 9,2** |
| Con los bloques 1–4 | 3,0 | 3,0 | 2,0 | ≈1,7 | **≈ 9,7** |

**Los tres primeros son un solo título cada uno.** Y los tres tienen molde escrito dentro del propio
backlog: no hay que inventar la forma, hay que aplicarla al ítem al que no se le aplicó.

---

## Bloque 1 — el productor de la constancia, y el orden entre sus dos terminadores · −0,5 D1

La reserva (a) de Rosa, y **la cifra sin productor más cara de la ronda**: `RF-149`, `RF-173` y
`RF-174` dependen los tres de la palabra «constancia», y el único que la produce es `RF-131`
—*«cuando el canal lo reporta»*—. Si el canal no reporta nunca, la constancia no llega nunca.

- **Escribir qué produce la constancia cuando el canal no la reporta**, o qué se tiene por llegado a
  falta de reporte. Hoy Rosa puede salir de la ventanilla con el mensaje leído en la mano y el
  sistema afirmando que no llegó.
- **Ordenar la carrera `RF-173` ↔ `RF-174`.** `RF-174` devuelve a las 72 h y `RF-173` vuelve pagable
  «cuando la constancia llega», sin guarda contra un giro ya devuelto. `RNF-13` prohíbe *devuelto y
  cobrado*, no *devuelto y pagable* — el molde del invariante está al lado.

> **Vale nombrar la clase, porque nació esta ronda:** tres títulos nuevos se apoyaron en una cifra que
> la misma ronda no produjo. La corrección del bloque 2 de la ronda 13 cerró un *estado sin
> terminador* y abrió una *cifra sin productor* en su lugar.

## Bloque 2 — el gemelo de `RF-172` del lado de Elena · −0,5 D1

Un solo título, **con cuatro precedentes de simetría en el propio backlog**: `RF-51`/`RF-120`,
`RF-67`/`RF-37`, `RF-60`/`RF-121`, `RF-14`/`RF-156`.

`RF-172` avisa al emisor el paso a *no pagable*. Elena ya recibió `RF-25` («hay un giro a tu nombre»)
y `RF-41` («esto vas a cobrar»), y toma la combi con esos dos avisos vivos y el giro no pagable.
**`RF-172` es el único cambio de estado del backlog que viaja a una sola punta.**

## Bloque 3 — el final del techo de 10 minutos de `RNF-09` · −0,5 D1 y ≈ +0,03 D4

La reserva de Kevin. Y la corrección **no es agregar un título**: es **partir `RNF-09`**, que hoy
empaqueta tres promesas —3 minutos de atención, 10 minutos de segundo rol, 60 segundos de lista
externa— de las cuales **solo una tiene consecuencia escrita**.

- **Partir el ítem en sus tres plazos**, que son modificables por separado.
- **Escribir el final del de 10 minutos**, con `RF-177` como molde: está en el mismo ítem y dice qué
  pasa al vencer los 60 segundos.

> La ronda 13 le dio techo y consecuencia al plazo donde se vio el síntoma y no tocó la decisión que
> lo generó: que un identificador lleve tres promesas. Es *reparación en la altitud equivocada*, y va
> por la sexta ronda consecutiva.

## Bloque 4 — la compuerta de `RF-187`, y el origen que hoy se le oculta a Rosa · +0,5 D3 y ≈ +0,03 D4

`RF-187` es el **tercer acto remoto originado por el receptor y el único sin compuerta de identidad**.
`RF-126` identifica antes de admitir una declaración de diferencia; `RF-180` identifica antes de
responder una consulta o comprobación. **Cambiar dónde se paga el dinero es la más consecuente de las
tres y es la que entra sin control.**

- **La compuerta**, con `RF-126` y `RF-180` de molde.
- **La decisión sobre el origen**, que no se corrige reescribiendo el aviso: `RF-187` **obliga** a
  presentarle la solicitud a Rosa *«como si el sistema la hubiera originado»*, y `RF-105` le da la
  última palabra sobre el cambio de punto. El título le quita el único dato con el que la ejercería.
  Hay que decidir qué se le dice a la dueña del dinero cuando la solicitud no es suya.
- **Partirlo**, además: admitir la solicitud y falsear su origen son dos cosas separables.

## Bloque 5 — plazo y terminador para `RF-154` · comparte punto con el bloque 1

`RF-154` decide si una diferencia declarada queda comprobada y **no tiene plazo ni terminador**,
mientras `RF-153` y `RF-184` se los dieron a la objeción del agente **en esta misma ronda**. Rosa lo
dice sin adornos: *«el backlog le puso plazo a la disputa del agente y se lo dejó abierto a la
reposición de mi madre»*.

## Bloque 6 — aplicar el bloque 8, que nunca se aplicó · preserva 3,0 D2

**El valor más alto de la lista, y el único que no cuesta un título:** es una restricción sobre cómo
se escriben las cinco de arriba.

De los 18 títulos que la ronda 13 agregó, **12 sobreviven intactos a una transferencia doméstica y
ninguno lleva la razón escrita** que el bloque exigía. La mortalidad de títulos nuevos cayó de 54 % a
**33 %**. La fracción global bajó menos solo porque se agregaron menos ítems.

**Cada título nuevo muere en una transferencia doméstica entre dos cuentas de banco en la misma
moneda, o lleva escrito por qué no.**

## Bloque 7 — las cinco ambigüedades y el duplicado · ≈ +0,06 D4

- **`RF-75` y `RF-109`:** «puede pagarle» — ¿la caja del punto o la disponibilidad del giro? La
  heredan `RF-91`, `RF-111`, `RF-129` y `RF-164`.
- **`RF-180`:** identificar «como el receptor designado» a quien todavía no dijo de qué giro habla es
  circular.
- **`RF-188`:** «el aviso con plazo escrito» — ¿el que enuncia un plazo o el que está sujeto a uno?
- **`RF-104`:** informar antes y adjuntar la evidencia son dos obligaciones negables por separado.
- **Retirar `RF-126`**, contenido en `RF-180`.
- **Declarar `RF-181`** en «Identificadores retirados», o explicar el hueco. Es el único número
  muerto sin declarar en trece rondas.

## Bloque 8 — las cuatro decisiones sin requerimiento vivas · ≈ +0,04 D4

La vida de la cotización antes de la ventanilla (`D:828`, `A:121`), el cierre de la superficie del
receptor (`D:272-274`), el reintento de avisos (`A:139`, `E-estimar:192`) y la capacidad de pago
declarada por punto (`A:126`). **Para cada una: o se escribe el título, o se saca la decisión.**

Y **`L:873-877` a `RF-170`** — tercer punto del bloque 1 de la ronda 13, segunda ronda sin aplicar.

---

## Enmienda candidata a D2 — escrita, no aplicada

El agregador la deja anotada bajo el **Principio IV**, y esta entrada existe para que la ronda que la
estrene cumpla la condición 2: *se escribe antes de aplicarse y corre en su propia ronda*.

**La evidencia (condición 1):** D2 lleva **diez rondas consecutivas leyendo 3,0** —de la 04 a la 13—
mientras la fracción específica de remesa se movió entre 52,6 % y 61,3 % y la disciplina de escritura
se degradó de forma medible: la mortalidad de títulos nuevos cayó de 54 % a 33 % en una sola ronda.
**Un test existencial por rasgo no distingue un backlog que ataca la remesa de uno que la ataca en
seis ítems de 192.** Es la misma forma de evidencia —varianza baja frente a un sustrato que sí
varía— que forzó la enmienda de D4 en la ronda 07.

**La condición 4 es trivial en este caso y hay que decirlo:** una D2 sensible a la fracción **solo
puede bajar puntajes**, nunca subirlos, de modo que no puede comprar el gate por construcción. Eso la
vuelve admisible — pero **no exime de las condiciones 2 y 3**: se corre en su propia ronda, sin
corregir nada más, y se declara qué corridas dejan de ser comparables.

**Por qué no se aplicó en la ronda 13:** porque cambiar la vara a mitad de una corrida es exactamente
lo que el Principio IV prohíbe, y porque el censo de la ronda 12 no era auditable —publicó los IDs de
frontera y de moneda y no los 74 del rasgo 3—. El de la ronda 13 sí lo es: está enumerado entero.
