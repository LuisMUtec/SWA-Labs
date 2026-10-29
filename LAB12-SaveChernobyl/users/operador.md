# Operador de planta

## Quién es

Empleado de la planta nuclear que hoy controla los 3 reactores con el sistema legacy, de forma demasiado manual. Es el único usuario humano del sistema; los medidores, los controladores y la refrigeración son componentes, no personas.

## Qué hace en el sistema

- Ve en el panel el estado de los reactores en tiempo real.
- Recibe las alarmas cuando una temperatura supera el umbral.
- Consulta reportes.
- Envía comandos (prender o apagar refrigeración) cuando la decisión no es automática.

## Necesidades del sistema

- Que las decisiones críticas se tomen con latencia mínima, aunque él no esté mirando el panel.
- Que el control de un reactor no se pierda si falla un sensor, un controlador o el Main Controller.
- Que quede registrado quién prendió o apagó qué, y cuándo, para la trazabilidad.
- Que la modernización no detenga ni reemplace de golpe el sistema que hoy controla los reactores.

## Problemas que tiene hoy

- El control es manual y le hace perder tiempo.
- No hay registro de quién hizo qué.
- Si el Main Controller se desconecta o un sensor falla, no hay un plan claro.

Fuente: RF3, RF4, RF5, RF6, RF7, RNF1, RNF2 y RC2 del enunciado.
