# Evaluación de Aníbal — iteración 1

Agente: [`Agents/agent-anibal.MD`](../../../../Agents/agent-anibal.MD) ·
Evaluado: `Requirements/ReqFunc.MD`, 42 requerimientos.

| ID | Veredicto | Justificación |
|---|---|---|
| RF-TUR-01 | Indiferente | Los cruces de programación no llegan a mi guardia localizable. |
| RF-TUR-02 | Indiferente | Los límites de jornada se vigilan en la oficina de la unidad. |
| RF-TUR-03 | Indiferente | No busco candidatos para cubrir una franja. |
| RF-TUR-04 | Indiferente | La versión vigente del rol mensual no cambia lo que hago a las 03:20. |
| RF-TUR-05 | Indiferente | Que me avisen de un cambio de programación no toca ninguna de mis seis tareas. |
| RF-TUR-06 | Indiferente | Los intercambios de turno presenciales son ajenos a mi bloque de siete días. |
| RF-TUR-07 | Indiferente | Las franjas descubiertas las mira la jefatura. |
| RF-TUR-08 | Indiferente | El rol impreso no me sirve: yo respondo desde mi casa con el celular. |
| RF-DIA-01 | Indiferente | El bloqueo del cierre de turno es del médico presencial con camas asignadas. |
| RF-DIA-02 | Indiferente | La entrega de turno se recibe al entrar a la unidad; yo no entro. |
| RF-DIA-03 | Indiferente | El señalamiento de camas sin diagnóstico ordena la entrega presencial. |
| RF-DIA-04 | Indiferente | El cierre de la entrega es del turno que sale y del que entra. |
| RF-DIA-05 | Indiferente | Los cambios desde el último contacto son para quien rota entre unidades. |
| RF-DIA-06 | Indiferente | La marca de inestabilidad ordena la entrega, no mi alerta. |
| RF-DIA-07 | Indiferente | Las versiones del diagnóstico son del registro presencial. |
| RF-DIA-08 | Indiferente | La entrega de enfermería no llega a mi celular. |
| RF-ESC-01 | Sirve | Es mi dolor exacto: que la alerta llegue al responsable vigente y no a quien decía un rol viejo, que es la razón por la que me han perdido llamadas que sí importaban. |
| RF-ESC-02 | Sirve | Es mi criterio: si no respondo en el plazo, el sistema sigue solo y el paciente no se queda esperando a que yo despierte. |
| RF-ESC-03 | Sirve | Es la tarea 1 entera: tendencia de seis horas, balance, vasoactivo con dosis, antimicrobiano con su día, último laboratorio y última evolución, sin que yo lo pida. |
| RF-ESC-04 | Sirve | Confirmar y que quien escaló lo vea de inmediato es lo que hoy resuelvo diciendo «ya voy» por teléfono, sin que quede constancia. |
| RF-ESC-05 | Indiferente | El estado de la cadena lo mira quien escaló. |
| RF-ESC-06 | Sirve | Sostiene mi lado de la tensión: si todo me llega como crítico dejo de responder a todo, y aquí la consulta diferible tiene su propia cadena y su propio plazo. |
| RF-ESC-07 | Sirve | Es mi tarea 5: me declaro indisponible, nombro delegado y el sistema deja de contarme en la cadena. |
| RF-ESC-08 | Indiferente | La cobertura clínica vigente la consulta quien está en la unidad. |
| RF-ESC-09 | Indiferente | El agotamiento de la cadena termina en la jefatura; a mí me alcanza antes. |
| RF-ESC-10 | Sirve | Es la segunda mitad de mi criterio: el sistema escala solo **y yo me entero** de que ocurrió, en vez de descubrirlo a la mañana. |
| RF-REG-01 | Sirve | Sin signos y balance incorporados al episodio con su hora no existe la tendencia sobre la que decido si voy o no voy. |
| RF-REG-02 | Indiferente | La captura sin conexión es del lado de quien registra a pie de cama. |
| RF-REG-03 | Sirve | «Sin saber qué se le indicó en el turno previo» es una de mis frustraciones; consultar las vigentes con su autor la cierra. |
| RF-REG-04 | Indiferente | La confirmación de ejecución no aparece en mis seis tareas. |
| RF-REG-05 | Indiferente | El registro de eventos y medicación lo produce enfermería. |
| RF-REG-06 | Sirve | A las 03:20 pregunto si hay lactato reciente; que los resultados disponibles se presenten al consultar la cama me ahorra el interrogatorio. |
| RF-REG-07 | Sirve | Es mi tarea 4 y mi frustración de siempre: la indicación que doy por teléfono queda registrada con mi autoría y su hora. |
| RF-REG-08 | Sirve | Es mi tarea 3: la tendencia de seis horas y el soporte vigente, no el valor aislado que me dictan por teléfono. |
| RF-IAM-01 | Sirve | Que la indicación quede atribuida a quien la produce es la constancia que hoy no existe cuando indico desde mi casa. |
| RF-IAM-02 | Ambiguo | Exige «turno vigente, delegación activa o responsabilidad de jefatura» para registrar, y no dice si mi guardia localizable es un turno vigente en esas dos unidades: leído de una forma registro, leído de la otra el sistema me rechaza la indicación remota que `RF-REG-07` me concede. |
| RF-IAM-03 | Indiferente | El registro de accesos no cambia mi decisión de ir o no ir. |
| RF-IAM-04 | Sirve | Resuelve los dos lados a la vez: admite mi celular personal sin exigir equipo institucional ni VPN, y saca la identificación del paciente del aviso hasta que me autentico. |
| RF-SUP-01 | Indiferente | El cumplimiento de entregas es el tablero de la jefatura. |
| RF-SUP-02 | Indiferente | Los indicadores de red no tocan mi guardia. |
| RF-SUP-03 | Sirve | Es mi tarea 6 y mi criterio: en un solo lugar, a la mañana, los escalamientos con su severidad, las indicaciones remotas y los ingresos y egresos de la noche. |
| RF-SUP-04 | Indiferente | Auditar un escalamiento es tarea de la coordinadora. |

### Necesidades no cubiertas

- **Los parámetros del ventilador.** «No poder ver la tendencia de signos vitales ni los parámetros
  actuales del ventilador» es una de mis frustraciones. `RF-ESC-03` adjunta «el soporte vasoactivo y
  ventilatorio vigentes con su dosis» y `RF-REG-08` presenta «el soporte vigente»: ninguno declara los
  parámetros, y el contrato de `RF-ESC-03` es cerrado, así que no puedo suponerlos.
- **Tomar el caso.** Mi tarea 2 es «confirmar recepción **y tomar el caso**». `RF-ESC-04` declara el
  acuse; ningún RF declara que asumir la responsabilidad clínica de esa cama sea un acto que el
  sistema registre y que los demás vean.
- **La decisión del turno diurno con su fundamento.** `RF-ESC-03` me adjunta «la última evolución
  registrada», que no es lo mismo que la decisión y su porqué —eso solo lo declara `RF-DIA-02`, y
  para el médico que inicia turno en la unidad.

### Riesgos que veo

- `RF-IAM-02` y `RF-REG-07` usan dos vocabularios distintos para el mismo permiso: «turno vigente,
  delegación activa o jefatura» frente a «responsable vigente o delegado». Mi figura —guardia
  localizable de dos UCIs— cabe en el segundo y no está claro que quepa en el primero. Si el sistema
  aplica el primero, la indicación de las 03:20 se rechaza.
- `RF-IAM-04` me pide autenticarme antes de ver el contexto. Lo acepto, pero con 3G y dormido cada
  paso cuesta: si la autenticación se interpone también en el acuse, mi criterio de «un toque» se
  rompe. El enunciado no lo aclara y por eso lo dejo dicho aquí y no en el veredicto.
- `RF-ESC-06` fija exactamente dos severidades. Es lo que pedía, pero deja a Milagros clasificando
  antes de escalar: si ella deja de usar el sistema y vuelve al teléfono, yo pierdo el contexto
  adjunto que es toda mi ganancia.

### Recorrido del escenario clave

**03:20, en mi casa. Hospital B, donde no estoy hace tres semanas.**

1. Llega la alerta al responsable vigente → `RF-ESC-01`. ✔
2. En mi celular personal, sin identificación del paciente hasta autenticarme → `RF-IAM-04`. ✔
3. Trae presión de las últimas seis horas, balance del día, último laboratorio, antimicrobiano con su
   día, vasoactivo con dosis y última evolución → `RF-ESC-03`. ✔
4. Identifica sede, unidad y cama sin que yo pregunte → `RF-ESC-03` CA-2. ✔
5. Confirmo recepción con un toque y quien escaló lo ve → `RF-ESC-04`. ✔
6. Decido y **registro la indicación remota** → `RF-REG-07` la incorpora con mi autoría e instante,
   **pero `RF-IAM-02`, que marqué Ambiguo, puede rechazarla** si mi guardia localizable no cuenta
   como turno vigente en esa unidad. **Este paso se sostiene en un ambiguo.**
7. Si no hubiera respondido, la cadena sigue y me entero → `RF-ESC-02` y `RF-ESC-10`. ✔
8. A la mañana reviso la noche en un solo lugar → `RF-SUP-03`. ✔

**El flujo se recorre completo, pero el paso 6 se apoya en `RF-IAM-02`, que admite dos lecturas.**

### Cobertura percibida: 100 %

Las seis tareas críticas tienen al menos un RF que marqué «Sirve».
