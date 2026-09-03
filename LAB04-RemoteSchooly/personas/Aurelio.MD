---
persona: Aurelio
rol: Coordinador del programa en la central — responde ante el gobierno por presupuesto y cobertura
status: proto
---

# Aurelio — el mandante

## Contexto

Coordina el programa de educación en línea desde la central de Lima. No produce material ni dicta:
**responde**. Ante el gobierno, por dos cosas — que los pueblos reciban los cursos y que el programa
no se coma su presupuesto `[ASSUMPTION: rinde cuentas por periodo, y el presupuesto de IA es una
partida con techo, no un gasto abierto]`.

Es quien recibe la exigencia del enunciado: reducir el gasto de tokens **al menos 40 %**. La cifra es
suya. Marisol la causa; él la paga y la tiene que explicar.

Lo único que puede verificar con sus propios ojos es **lo que el sistema le reporta**. No puede ir al
pueblo a comprobar si llegó el material, y no puede auditar cada generación de cada autora.

Lo que le pasó: firmó un informe diciendo que la cobertura del trimestre estaba completa. Dos meses
después supo que una región llevaba tres semanas sin recibir material — el sistema decía «enviado» y
nadie había mirado si eso significaba «llegado». Desde entonces no acepta un número que no diga
contra qué se mide.

## Flujo principal

**Cuando** cierra un periodo, **quiero** saber qué regiones recibieron efectivamente cada semana y
cuánto costó producirlas **para** rendir cuentas al gobierno y decidir dónde ajustar.

1. Fija el techo de gasto de IA por curso para el periodo.
2. Durante el periodo, ve qué regiones tienen la semana vigente y cuáles no.
3. Cuando una región se queda atrás, se entera **mientras todavía se puede reponer**.
4. Al cierre, ve el gasto del periodo **contra la línea base** y el porcentaje de reducción.
5. Rinde: cobertura y ahorro, los dos con su medida.

**Cuando sale mal:** se entera tarde de las dos cosas. De que una región lleva semanas sin material
cuando ya no se puede reponer nada, y del gasto cuando ya está gastado. Con «enviado» en la pantalla
y nada que le diga si eso significa que alguien lo recibió, firma informes que no puede sostener.

## Qué se le interpone

- **La distancia.** No puede comprobar en el terreno; depende por completo de lo que el sistema
  afirme.
- **«Enviado» no es «llegado».** La distinción es todo su problema y ningún tablero se la daba.
- **El presupuesto es finito y las regiones no son igual de caras.** Llegar a la más lejana cuesta
  más; alcanzar a todas puede no caber.
- **No manda sobre cómo trabaja Marisol.** Puede poner un techo; no puede sentarse a mirarle cada
  generación.

## Permisos

- **Puede:** fijar y cambiar el techo de gasto de IA por curso y periodo; ver la cobertura por región
  y el gasto por curso; recibir el aviso cuando una región se atrasa; obtener la rendición del
  periodo contra la línea base.
- **Nunca debe:** poder editar ni publicar material —no es autor—; ni dar por recibida una semana que
  ninguna región confirmó; ni ver el trabajo no publicado de una autora.

## Señal de éxito

- Puede decir, con fecha, qué regiones tienen la semana vigente y cuáles no — y la afirmación se
  apoya en que el destino la confirmó, no en que la central la despachó.
- El −40 % lo puede mostrar con numerador, denominador y línea base.
- Se entera de un atraso **con tiempo de reponerlo**.

## Tensiones que encarna

- Con **Marisol**: su techo es el límite del trabajo de ella. `T2`.
- Con **Nayra**: llegar a la región más lejana cuesta más de lo que el presupuesto rinde, y alguien
  tiene que decidir qué pasa entonces. `T4`.

Ver [`README.md`](README.md).
