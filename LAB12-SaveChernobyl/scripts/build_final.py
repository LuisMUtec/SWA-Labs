"""Lab 12 - Save Chernobyl: una sola lamina con la arquitectura to-be (iteracion 3) para el evaluador.
Cambios respecto a la lamina de tres iteraciones: fuentes grandes, etiquetas literales de patron
(<< Strangler >>, << Side-car >>, << Cache-Aside >>, << Replicas >>, << Sharding >>), SPOF y BOTTLENECK
marcados con su mitigacion, y Login / Auth + User Registration para la trazabilidad del operador.
Uso: python3 -I build_final.py salida.excalidraw"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xlib import *

OUT = sys.argv[1]
c = Canvas()


def tag(e, txt, color=RED, fs=16, where='below', dx=0):
    """Etiqueta libre pegada a un elemento (sin cambiarle el color)."""
    a, b, cc, d = c.bbox(e); tw, th = text_size(txt, fs)
    y = d + 6 if where == 'below' else b - th - 6
    return c.text((a + cc) / 2 - tw / 2 + dx, y, txt, fs, color, align='center')


def block(x, y, title, lines, color=BLACK, fs=14, title_fs=22):
    c.text(x, y, title, title_fs, color)
    c.text(x, y + title_fs * 1.25 + 8, '\n'.join(lines), fs, BLACK)


# ------------------------------------------------------------------ cabecera
c.text(0, -150, 'Lab #12 - Save Chernobyl ( medium ) - Arquitectura to-be - Arquitectura de Software 2026-II', 32)
c.text(0, -105, 'TEAM: ____________   INTEGRANTES: ______________________________   Prof. Carlos Balbuena', 20)
c.text(0, -72, 'Reliability + fault tolerance + coexistencia con el legacy (<< Strangler >>): reactor 1 migrado al controller nuevo; reactores 2 y 3 siguen en el legacy.   Cajas apiladas = << Replicas >>.', 16, GRAY)

# ------------------------------------------------------------------ carril 1: critical path (HOST reactor 1)
med1 = c.rect(0, 20, 270, 110, 'Medidores de\ntemperatura 1..100\n(1 envio cada 0.05 s)', fs=18)
reac1 = c.rect(0, 180, 270, 70, 'Reactor 1', fs=20)
ref1 = c.rect(0, 320, 270, 90, 'Refrigeracion 1\n(actuador)', fs=18)
host = c.box(370, -40, 1180, 380, BLACK, 'solid', sw=1)
c.text(380, -35, 'HOST reactor 1 (decision local, sin red)', 16, BLACK)
lb1 = c.diamond(390, 40, 140, 110, 'LB\n/health', fs=16, stroke=BLUE, tcolor=BLUE)
ctl1 = c.stack(560, 20, 340, 150, 'Controller 1\n<< Replicas x2 >> + /health\n- refrigeracion y alertas\n- decision local (sin red)\n- sensores Healthy/Unhealthy', n=2, fs=18, stroke=BLUE, tcolor=BLUE)
side = c.rect(760, 230, 340, 100, '<< Side-car >> Pod 2\nLogging / Monitoring\n(no impacta al control)', fs=17, stroke=BLUE, tcolor=BLUE)
state = c.rect(1150, 230, 380, 100, 'Reactor State Cache (cache local)\n- ultimo comando (id, quien, cuando)\n- evita comandos duplicados', fs=16, stroke=BLUE, tcolor=BLUE)
evh = c.rect(950, 30, 560, 130, 'Event Handler (abstraccion)\nBranch by Abstraction: Lib actual | Lib nueva\n<< Feature Flag >> piloto solo en reactor 1', fs=17, stroke=ORANGE, tcolor=ORANGE)
alert = c.stack(1560, 20, 300, 110, 'Alert Service << Replicas >>\n- umbral de temperatura\n- alarma al operador', n=2, fs=18, stroke=BLUE, tcolor=BLUE)
op = c.actor(1975, 20, 'Operador')

c.arrow(med1, lb1, label='{sensor 17, 312 C}\ncada 0.05 s + heartbeat', color=GREEN, fs=15, lcolor=GREEN, sw=3, label_dy=45)
c.arrow(lb1, ctl1, color=GREEN, sw=3)
c.arrow(reac1, lb1, heads='none')
c.arrow(ctl1, ref1, label='{refrig: ON} + ack\n(sincrono)', color=GREEN, fs=15, lcolor=GREEN, sw=3,
        start_at=(560, 150), via=[(540, 200), (320, 200), (320, 365)], end_at=(270, 365), label_seg=1, label_dy=-30)
c.arrow(ctl1, side, label='Low Latency', fs=15, start_at=(860, 170), end_at=(860, 230), label_dx=75)
c.arrow(ctl1, state, heads='both', start_at=(900, 160), end_at=(1180, 230))
c.arrow(ctl1, evh, heads='both', label='eventos', fs=15, start_at=(900, 90), end_at=(950, 90), label_dy=-18)
c.arrow(ctl1, alert, label='alerta: temp > umbral (sincrono)', color=GREEN, fs=15, lcolor=GREEN, sw=3,
        start_at=(900, 40), via=[(930, -5), (1520, -5)], end_at=(1560, 60), label_seg=1, label_dy=-16)
c.arrow(alert, op, label='alarma', fs=15, label_dy=-14)

# ------------------------------------------------------------------ operador: login, registro, gateway
login = c.rect(1850, 250, 300, 90, 'Login / Auth Service\n(autenticacion de operadores,\nroles, sesion)', fs=15, stroke=BLUE, tcolor=BLUE)
reg = c.rect(2200, 250, 360, 90, 'User Registration Service\n(Sign Up: alta de operadores\ny roles, por el admin)', fs=15, stroke=BLUE, tcolor=BLUE)
usersdb = c.db(2620, 240, 'Users DB\n(operadores, roles)', color=BLUE, fs=14, w=150)
gw = c.diamond(1900, 400, 200, 120, 'API Gateway\nauth, rate limit', fs=14, stroke=BLUE, tcolor=BLUE)
c.arrow(op, login, label='login\n(credenciales)', fs=13, heads='both', start_at=(2000, 200), end_at=(2000, 250), label_dx=75)
c.arrow(login, gw, label='token / sesion', fs=13, start_at=(2000, 340), end_at=(2000, 400), label_dx=75)
c.arrow(login, usersdb, label='valida', fs=13, style='dashed', start_at=(2150, 320), via=[(2180, 380), (2600, 380)],
        end_at=c.border(usersdb, 2600, 380), label_seg=1, label_dy=-12)
c.arrow(reg, usersdb, label='crea usuario', fs=13, label_dy=-14)
c.arrow(op, reg, label='alta de operadores (admin)', fs=13, start_at=(2025, 46), end_at=c.border(reg, 2025, 46), label_dy=-14)

# ------------------------------------------------------------------ carril 2: decisiones globales (Strangler)
router = c.stack(330, 500, 400, 130, '<< Strangler >> Router (Facade)\n<< Replicas x2 >>\n- criterio de ruteo: por reactor\n- rollback: todo al legacy', n=2, fs=18, stroke=ORANGE, tcolor=ORANGE)
newbox = c.box(830, 440, 960, 280, BLUE, 'dashed')
c.text(840, 445, 'New Architecture', 16, BLUE)
lb = c.diamond(870, 490, 170, 150, 'LB\n/health', fs=18, stroke=BLUE, tcolor=BLUE)
main_new = c.stack(1100, 495, 360, 140, 'Main Controller (nuevo)\n<< Replicas x2 >> + /health\n- decisiones globales\n- comandos', n=2, fs=18, stroke=BLUE, tcolor=BLUE)
acl = c.rect(1530, 510, 230, 110, 'ACL\n(formato legacy\n-> nuevo)', fs=17, stroke=ORANGE, tcolor=ORANGE)
c.text(840, 650, 'parallel run: el Main nuevo recibe\ntambien datos de reactores 2 y 3\n(shadow, sin mandar comandos)', 14, ORANGE)
legbox = c.box(2140, 440, 820, 540, GRAY, 'dashed')
c.text(2150, 445, 'Legacy (sigue funcionando, sin cambios)', 16, GRAY)
main_leg = c.rect(2180, 500, 350, 120, 'Main Controller (legacy)\n- controla reactores 2 y 3', fs=17)
c.mark_spof(main_leg, 'Circuit Breaker + Retry en el router', fs=16, where='above')
intercept = c.rect(2580, 500, 360, 120, 'Event Interceptor (SQL trigger)\n+ << Side-car >> Proxy: Logging', fs=16, stroke=ORANGE, tcolor=ORANGE)
leg2 = c.rect(2180, 820, 350, 100, 'Reactor 2 + Medidor +\nRefrigeracion + Controller 2', fs=16)
leg3 = c.rect(2580, 820, 360, 100, 'Reactor 3 + Medidor +\nRefrigeracion + Controller 3', fs=16)

c.arrow(ctl1, router, label='datos / comandos\n(sincrono)', fs=15, start_at=(600, 170), end_at=(600, 500), label_dx=-90)
c.arrow(router, lb, label='reactor 1 -> New', fs=14, label_dy=-16)
c.arrow(lb, main_new)
c.arrow(main_new, acl, heads='both')
c.arrow(acl, main_leg, heads='both', label='datos legacy', fs=14, label_dy=-16)
c.arrow(router, main_leg, label='reactores 2 y 3 -> Legacy: << Circuit Breaker >> + Retry N=2 + timeout', fs=15, color=ORANGE, lcolor=ORANGE,
        start_at=(530, 630), via=[(530, 760), (2080, 760), (2080, 560)], end_at=(2180, 560), label_seg=1, label_at=0.3, label_dy=16)
c.arrow(leg2, main_leg, label='datos / comandos', fs=14, heads='both')
c.arrow(leg3, main_leg, heads='both', start_at=(2760, 820), via=[(2760, 740), (2450, 740)], end_at=(2450, 620))
c.arrow(main_leg, intercept, heads='none', style='dashed')

# ------------------------------------------------------------------ carril 3: trazabilidad y panel
queue = c.ellipse(390, 880, 380, 140, 'Cola de eventos << BMQ >>\n(mediciones, acciones, logs)\nasincrono', fs=17, stroke=BLUE, tcolor=BLUE)
logsvc = c.rect(0, 890, 290, 110, 'Log Service\n- quien prendio/apago que\n- latencia por accion', fs=17, stroke=BLUE, tcolor=BLUE)
logdb = c.db(0, 1080, 'Log DB << Master >>\n<< Sharding >> por reactor\n+ replica (failover)', color=BLUE, fs=14, w=200)
c.text(0, 1336, 'BOTTLENECK (escrituras: 6 000 mediciones/s) -> protegido con cola asincrona + Read Replica + Cache-Aside', 15, RED)
replica = c.db(300, 1090, 'Read Replica\n<< Replicas >>\n(reportes)', color=BLUE, fs=16, w=180)
panel = c.rect(1090, 880, 400, 140, 'Dashboard Service (panel)\n- tiempo real, alarmas, reportes\n- << Cache-Aside >> ultimas lecturas\n- Bulkhead: recursos propios', fs=17, stroke=BLUE, tcolor=BLUE)
report = c.rect(1090, 1090, 280, 90, 'Report Service\n<< cron >>', fs=17, stroke=BLUE, tcolor=BLUE)

c.arrow(side, queue, style='dashed', label='logs y eventos\n(asincrono)', fs=14, start_at=(800, 330), via=[(800, 400), (330, 400), (330, 870)],
        end_at=(430, 905), label_seg=2, label_dx=-75)
c.arrow(evh, queue, style='dashed', start_at=(1125, 160), via=[(1125, 420), (805, 420), (805, 850)], end_at=c.border(queue, 805, 850))
c.arrow(intercept, queue, style='dashed', label='eventos del legacy (trazabilidad)', fs=14, start_at=(2620, 620),
        via=[(2555, 700), (2555, 1060), (900, 1060)], end_at=c.border(queue, 900, 1060), label_seg=2, label_dy=-12)
c.arrow(queue, logsvc, style='dashed', label='consume', fs=14)
c.arrow(logsvc, logdb)
c.arrow(logdb, replica, label='replica', fs=14)
c.arrow(replica, panel, label='lecturas (80%)', fs=14, start_at=(470, 1140), via=[(950, 1140)], end_at=(1200, 1020), label_seg=0, label_dy=-14)
c.arrow(replica, report, start_at=(478, 1195))
c.arrow(gw, panel, heads='both', label='ver estado / alarmas /\nreportes y comandar', fs=14, start_at=(2000, 520), via=[(2000, 950)],
        end_at=(1490, 950), label_seg=0, label_dx=-110)
c.arrow(panel, main_new, label='comandos del operador\n(quedan en log)', fs=14, style='dashed', start_at=(1350, 880), end_at=(1350, 635), label_dx=120)

# ------------------------------------------------------------------ bloques de texto
Y = 1400
block(0, Y, 'Leyenda', [
    'Negro: legacy que sigue igual.  Azul: nuevo con reliability / fault tolerance.',
    'Naranja: migracion evolutiva (Strangler router, ACL, feature flag, interceptor).',
    'Rojo: SPOF / Bottleneck y flujos alternos.  Verde grueso: critical path.',
    'Linea solida = sincrono.  Punteada = asincrono (eventos, logs).',
    'Cajas apiladas = << Replicas >>.  Recuadros: HOST / New Architecture / Legacy.',
])
block(740, Y, 'Flujos alternos (que pasa si falla?)', [
    'OFF 1: sensor sin respuesta (timeout) -> Unhealthy;',
    '  el Controller sigue con los demas medidores + WARN + alarma.',
    'OFF 2: Main Controller sin respuesta -> Circuit Breaker abierto',
    '  -> decision local en el HOST + alarma (modo local).',
    'OFF 3: refrigeracion sin ack -> Retry N=2 -> alarma critica al operador.',
], RED)
block(1480, Y, 'SPOF y Bottleneck (hint)', [
    'SPOF: Main Controller legacy (unico). Mitigacion: Circuit Breaker + Retry',
    '  + timeout en el Strangler Router; Main nuevo en parallel run (shadow).',
    'Bottleneck: Log DB (escrituras 6 000 mediciones/s). Mitigacion: cola',
    '  asincrona + Read Replica + Cache-Aside en el Dashboard.',
    'SPOF eliminados: Controller 1, Main nuevo y Alert Service con Replicas + LB /health.',
], RED)
block(2220, Y, 'Patrones de escalabilidad (criterios en README)', [
    'Replicas: Controller 1, Main nuevo, Alert Service, Log DB read replica.',
    'Side-car: logging/monitoring junto al controller; Sidecar Proxy en el legacy.',
    'Cache-Aside: Dashboard (ultimas lecturas) y Reactor State Cache.',
    'Sharding: Log DB y cola particionadas por reactor (nuevo reactor = nuevo shard).',
    'Strangler: router por reactor.  BFF: no aplica (un solo panel).',
], BLUE)

c.save(OUT)
x0, y0, x1, y1 = c.extent()
print('ok', OUT, len(c.els), 'elementos; extent', round(x1 - x0), 'x', round(y1 - y0))
