# Correcciones pendientes — ronda 15

Derivadas de la [iteración 14](iterations/2026-08-27-14.md), que cerró en **7,75 / 10**. Backlog
vigente: **180 RF + 20 RNF = 200 ítems**, congelado en `e8cd465`.

## Aritmética del gate

| Escenario | D1 | D2 | D3 | D4 | Total |
|---|---|---|---|---|---|
| Hoy (ronda 14) | 1,5 | 3,0 | 1,5 | 1,75 | **7,75** |
| **Con el bloque 1 solo** | 1,5 | 3,0 | **2,0** | ≈1,80 | **≈ 8,30** |
| Con el bloque 1 y las tres del 2 | 3,0 | 3,0 | 2,0 | ≈1,85 | **≈ 9,85** |
| Con las tres del 2 sin el 1 | 3,0 | 3,0 | 1,5 | ≈1,80 | **≈ 9,30** |

**Por primera vez en catorce rondas la corrección que separa del gate es de D3 y no de D1**, y es una
sola.

---

## Bloque 1 — la compuerta que falta sobre `RF-90` · +0,5 D3 y ≈ +0,05 D4 · **cruza el gate sola**

`RF-90` deja al receptor **declarar una diferencia por llamada o mensaje de texto**. `RF-180`
identifica a quien **consulta**, **comprueba** o **solicita un cambio de punto**. **Declarar no está
en la lista.** Detrás de la declaración hay dinero: `RF-193` le da cinco días hábiles, **`RF-194` la
repone cuando el plazo vence sin decidirse**, `RF-155` la paga en efectivo y `RF-143` la descuenta
del agente. Una declaración sin compuerta es **un pago por silencio**.

Dos formas, y la segunda es mejor:

1. Extender la enumeración de `RF-180`.
2. **Volver a partir `RF-180` en un ítem por disparador.** Cierra además el hallazgo de atomicidad y
   quita el `n` correspondiente — **y quita la causa**: la enumeración dentro de un solo título es lo
   que permitió que el cuarto disparador desapareciera sin que nadie lo viera.

> **La lección, escrita para no repetirla.** `RF-126` se retiró declarándolo «contenido en `RF-180`»
> y **la contención no se comprobó contra el texto de `RF-180`**. El barrido aguas abajo reemplazó el
> identificador en los cinco pasos, de modo que cuatro de ellos hoy **afirman una compuerta que no
> existe**. Retirar un identificador no es reemplazarlo: es demostrar que lo que decía sigue dicho.

## Bloque 2 — las tres reservas de persona · hasta +1,5 D1

Un título cada una, y **las tres con molde dentro del propio backlog**.

| Persona | Qué falta | El molde |
|---|---|---|
| **Rosa** | La salida barata que alcance al giro **devuelto** por `RF-174`, y no solo al **cancelado** de `RF-117`. Hoy rehace pagando comisión de nuevo y con la cotización del día | `RF-117` + `RF-134` + `RF-135`, que ya lo hacen para el otro borde |
| **Elena** | **Dónde** cobra. `RF-25` le dice que hay un giro y `RF-41` cuánto; `RF-75` presupone que ya sabe cuál es el punto | El backlog escribe «y en qué punto» **tres veces**: `RF-124`, `RF-156`, `RF-14` |
| **Kevin** | Qué se le dice **a él** del giro que creó, cuando pasa a no pagable quince minutos después de que el cliente se fue | `RF-172` al emisor y `RF-190` al receptor. Falta la tercera punta, que es la que tomó el efectivo |

## Bloque 3 — la referencia rota de `RNF-20` · ≈ +0,02 D4

Un identificador. La medida de `RNF-20` dice «`RF-192` dice qué pasa al vencerlo»; quien lo dice es
**`RF-191`**. **Es la única corrección del pliego que las tres personas pidieron por separado.**

## Bloque 4 — las cuatro decisiones sin requerimiento · ≈ +0,08 D4

Cuarta ronda para tres de ellas. Para cada una: **o se escribe el título, o se saca la decisión.**

- **La vida de la cotización antes de la ventanilla** — `A:121`, `A:473` le dan `vence_en` y ningún
  título le da vigencia a una cotización.
- **El reintento de avisos** — `A:139` «reencolar el aviso». `RF-132` trata como no avisado; ningún
  título ordena reintentar.
- **La capacidad de pago declarada por punto** — `A:126`. Y la desambiguación de `RF-75`/`RF-109` a
  «tiene efectivo» **agrandó** la distancia: lo que los títulos producen es efectivo (`RF-76`,
  `RF-95`), no una capacidad declarada.
- **El cierre de la superficie del receptor** — `D:272-274`, `D:317-333`, contra ocho títulos que la
  exigen.

## Bloque 5 — `RF-189` contra `RF-132` · ≈ +0,02 D4

Dos títulos dan respuestas opuestas sobre el mismo hecho. `RF-189` tiene el código **por llegado** si
el canal calla; `RF-132` trata como **no avisado** a quien no tenga constancia de que llegó, y
`RF-131` solo la registra «cuando el canal lo reporta». `RF-149` cuelga de la respuesta. **Es la
corrección del bloque 1 de la ronda 14 entrando sin barrer la regla que la contradecía.**

## Bloque 6 — los cuatro herederos de «no puede pagar» · ≈ +0,02 D4

El bloque 7 de la ronda 14 los nombró y **la ronda desambiguó dos de seis**: `RF-75` y `RF-109`
dicen «tiene efectivo para pagarle»; `RF-91`, `RF-111`, `RF-129` y `RF-164` siguen diciendo «no puede
pagar» y «capaz de pagarlo».

## Bloque 7 — la cifra que `RF-194` repone · ≈ +0,02 D4

`RF-59` cuelga de «diferencia **comprobada**»; `RF-194` repone precisamente la que **no** se
comprobó, y ningún título produce esa cifra. `A:140` la suple con `monto_declarado_recibido`, que es
la palabra del declarante.

## Bloque 8 — la autocertificación de «Disciplina de alcance»

No mueve puntaje directo **y gobierna cómo se escriben todas las demás**. Dice «los diez títulos de
la ronda 14 mueren los diez»: **son nueve, y cuatro no mueren** — `RF-189`, `RF-190`, `RF-194`,
`RNF-19`. O se corrige el conteo y la afirmación, o se escribe en los cuatro una razón comprobable
**en el título**.

## Bloque 9 — la propagación · no puntúa, y es la deuda más grande del repositorio

`D`, `E-estimar` y `E-escalar` siguen declarando **155 ítems**, el cierre de la ronda 11: tres rondas
y 45 ítems atrás. De los nueve identificadores nuevos de la ronda 14 hay **cero ocurrencias** en `D`,
`A`, `E-estimar` y `E-escalar`.

Y `L`, que sí se repropagó a 200 filas, **cita `RF-126` dos veces en `:862` y una en `:932`**, en la
casilla marcada que declara que la entrada del canal de voz tiene control de identidad, mientras
`:934` afirma «sin punteros a identificadores retirados».

---

## Enmienda candidata a D2 — sigue escrita y sin aplicar

Ver [`CORRECCIONES-RONDA-14.md`](CORRECCIONES-RONDA-14.md). La evidencia se refuerza: **D2 lleva once
rondas leyendo 3,0** y la fracción está en **49,5 %** — por debajo de la mitad por primera vez desde
la ronda 03. La condición 2 exige una ronda propia sin ninguna otra corrección; **no puede correr en
la ronda 15 si esa ronda aplica los bloques 1 a 9.**
