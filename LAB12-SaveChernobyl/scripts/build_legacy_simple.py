"""Lab 12 - Save Chernobyl, lamina 2 (version simple): foto actual del legacy y plan de coexistencia.
Pocas cajas, una o dos lineas por caja, fuentes 18-20. Uso: python3 -I build_legacy_simple.py salida.excalidraw"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xlib import *

OUT = sys.argv[1]
c = Canvas()


def mark(x, y, n):
    return c.ellipse(x - 20, y - 20, 40, 40, str(n), fs=18, stroke=RED, tcolor=RED, bg='#ffffff')


def pbox(x, y, w, h, txt, stroke=BLACK, fs=20):
    """Caja de texto alineada a la izquierda."""
    r = c.rect(x, y, w, h, txt, fs=fs, stroke=stroke, tcolor=BLACK)
    t = c.byid[r['boundElements'][-1]['id']]; t['textAlign'] = 'left'; t['x'] = x + 20
    return r


# ------------------------------------------------------------------ cabecera
c.text(0, -150, 'Lab #12 - Save Chernobyl - Lamina 2: el legacy por dentro y como convivimos con el', 32)
c.text(0, -110, 'TEAM: Maquera - Barzola     INTEGRANTES: Luis Maquera, Johar Barzola     Prof. Carlos Balbuena', 18)
c.text(0, -78, 'Verde = CONSERVAR     Naranja = CAMBIAR (envolver, no reescribir)     Rojo = RETIRAR     (1) (2) (3) = puntos de integracion', 18, GRAY)

# ------------------------------------------------------------------ A. foto actual
legbox = c.box(0, 0, 1400, 780, GRAY, 'dashed')
c.text(14, 10, 'Foto actual del legacy (supuesto: el enunciado no describe el interior)', 20, GRAY)
cols = {}
for i, x in ((2, 40), (3, 420)):
    med = c.rect(x, 70, 300, 80, f'Medidores {i}', fs=20, stroke=GREEN, tcolor=GREEN)
    ctl = c.rect(x, 210, 300, 100, f'Controller {i}\nlee cada 0.05 s, comanda PLC', fs=18, stroke=GREEN, tcolor=GREEN)
    ref = c.rect(x, 370, 300, 80, f'Refrigeracion {i}', fs=20, stroke=GREEN, tcolor=GREEN)
    c.arrow(med, ctl); c.arrow(ctl, ref)
    mark(x + 200, 180, 1)
    cols[i] = ctl
main = c.rect(180, 560, 540, 110, 'Main Controller legacy\nproceso unico = SPOF', fs=20, stroke=ORANGE, tcolor=ORANGE)
c.text(190, 680, 'CAMBIAR ahora -> RETIRAR en fase 3', 16, ORANGE)
c.arrow(cols[2], main, color=ORANGE, heads='both', start_at=(340, 240), via=[(360, 240), (360, 540)], end_at=(360, 560))
c.arrow(cols[3], main, color=ORANGE, heads='both', start_at=(420, 290), via=[(400, 290), (400, 540)], end_at=(400, 560))
mark(440, 500, 2)
c.text(470, 488, 'enlace unico = SPOF', 16, ORANGE)
consola = c.rect(820, 70, 320, 90, 'Consola manual', fs=20, stroke=RED, tcolor=RED)
c.cross(consola)
c.rect(820, 230, 380, 90, 'Sin login, sin trazabilidad', fs=18, stroke=RED, tcolor=RED, style='dashed')
bd = c.db(840, 540, 'BD legacy\n(esquema viejo)', color=ORANGE, fs=18, w=200)
op = c.actor(1280, 90, 'Operador')
c.arrow(op, consola, heads='both')
c.arrow(main, consola, start_at=(720, 590), via=[(780, 590), (780, 115)], end_at=(820, 115))
c.arrow(main, bd, start_at=(720, 640), end_at=c.border(bd, 720, 640))
mark(780, 420, 3)

# ------------------------------------------------------------------ B. que cuelga de cada punto
c.text(1460, 0, 'Que se le cuelga a cada punto de integracion', 24)
pbox(1460, 60, 1000, 100, '(1) Medidor -> Controller\nACL: traduce el formato propietario al nuevo', ORANGE)
pbox(1460, 200, 1000, 150, '(2) Controller <-> Main\nStrangler Router (ruteo por reactor) + Circuit Breaker\nParallel Run + Comparador: el Main nuevo no comanda hasta el GO', ORANGE)
pbox(1460, 390, 1000, 150, '(3) Main -> BD / consola\nDatabase View Layer (lectura)  ·  Event Interception (trigger -> cola)\nSidecar Proxy (logs)  ·  Dashboard + Login reemplazan la consola', ORANGE)
pbox(1460, 580, 1000, 120, 'Costo: doble mantenimiento hasta el GO (2 Mains, 2 BDs, ruteo).\nRollback real = Controller 1 legacy sigue vivo en shadow.', RED, 18)

# ------------------------------------------------------------------ C. migracion de datos
c.text(0, 840, 'Migracion de datos: hibrida con conciliacion (no Big Bang: el historico no se descarta)', 24)
bdleg = c.db(40, 900, 'BD legacy', color=ORANGE, fs=20, w=180)
loader = pbox(360, 890, 560, 90, 'Loader << cron >>: ETL del historico\nen orden de foreign keys', ORANGE, 18)
cdc = pbox(360, 1020, 560, 70, 'CDC / trigger: cambios en vivo -> cola', ORANGE, 18)
logdb = c.db(1060, 900, 'Log DB nueva', color=BLUE, fs=20, w=180)
concil = pbox(1340, 895, 680, 100, 'Conciliacion << cron >>\nON en una BD y OFF en la otra = alarma, sin GO', RED, 18)
c.arrow(bdleg, loader, label='historico', fs=15, label_dy=-14)
c.arrow(loader, logdb)
c.arrow(bdleg, cdc, style='dashed', start_at=(190, 1020), end_at=(360, 1055))
c.arrow(cdc, logdb, style='dashed', start_at=(920, 1055), end_at=c.border(logdb, 920, 1055))
c.arrow(logdb, concil, heads='both')
c.arrow(bdleg, concil, style='dashed', start_at=(130, 1080), via=[(130, 1150), (1680, 1150)], end_at=(1680, 995))

# ------------------------------------------------------------------ D. fases
c.text(0, 1220, 'Fases (los reactores nunca se detienen)', 24)
f0 = pbox(0, 1270, 540, 100, 'Fase 0: foto actual\nmedir P95/P99 del legacy', BLACK, 18)
f1 = pbox(620, 1270, 580, 100, 'Fase 1: alrededor, sin tocarlo\nSidecar + Interceptor + View Layer', ORANGE, 18)
f2 = pbox(1280, 1270, 580, 100, 'Fase 2: Strangler reactor 1\nParallel Run del Main -> GO', ORANGE, 18)
f3 = pbox(1940, 1270, 520, 100, 'Fase 3: reactores 2 y 3\nETL final; legacy R.I.P.', RED, 18)
c.arrow(f0, f1); c.arrow(f1, f2); c.arrow(f2, f3)

c.save(OUT)
x0, y0, x1, y1 = c.extent()
print('ok', OUT, len(c.els), 'elementos; extent', round(x1 - x0), 'x', round(y1 - y0))
