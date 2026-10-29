"""Renderiza un .excalidraw a SVG + PNG (rsvg-convert) con Excalifont, y escribe un .txt con el grafo (formas, textos, conexiones).
Uso: python render_x.py archivo.excalidraw [escala_png]"""
import json, sys, math, html, subprocess, os

FONT = {1: 'Virgil, Excalifont', 2: 'Helvetica, Arial', 3: 'Cascadia, Menlo, monospace', 5: 'Excalifont, "Comic Sans MS"',
        6: 'Nunito, Helvetica', 7: '"Lilita One", Helvetica', 8: '"Comic Shanns", "Comic Sans MS"'}


def load(p):
    d = json.load(open(p)); return [e for e in d['elements'] if not e.get('isDeleted')]


def bbox(els):
    xs = []; ys = []
    for e in els:
        if e['type'] in ('arrow', 'line', 'freedraw'):
            for px, py in e['points']: xs.append(e['x'] + px); ys.append(e['y'] + py)
        else:
            xs += [e['x'], e['x'] + e['width']]; ys += [e['y'], e['y'] + e['height']]
    return min(xs), min(ys), max(xs), max(ys)


def col(c): return 'none' if (not c or c == 'transparent') else c


def arrowhead(p_prev, p, color, sw):
    """Punta de flecha dibujada (triángulo abierto estilo Excalidraw)."""
    ang = math.atan2(p[1] - p_prev[1], p[0] - p_prev[0]); L = 14 + sw * 2
    a1 = ang + math.radians(25); a2 = ang - math.radians(25)
    x1, y1 = p[0] - L * math.cos(a1), p[1] - L * math.sin(a1)
    x2, y2 = p[0] - L * math.cos(a2), p[1] - L * math.sin(a2)
    return f'<polyline points="{x1:.1f},{y1:.1f} {p[0]:.1f},{p[1]:.1f} {x2:.1f},{y2:.1f}" stroke="{color}" stroke-width="{sw}" fill="none" stroke-linecap="round"/>'


byid_global = {}


def svg(els):
    byid_global.clear(); byid_global.update({e['id']: e for e in els})
    x0, y0, x1, y1 = bbox(els); pad = 60
    W = int(x1 - x0 + 2 * pad); H = int(y1 - y0 + 2 * pad)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0 - pad} {y0 - pad} {W} {H}" width="{W}" height="{H}">',
           f'<rect x="{x0 - pad}" y="{y0 - pad}" width="{W}" height="{H}" fill="white"/>']
    for e in els:
        t = e['type']; sc = col(e.get('strokeColor')); bg = col(e.get('backgroundColor')); sw = e.get('strokeWidth', 1)
        dash = {'dashed': '12 8', 'dotted': '3 6'}.get(e.get('strokeStyle'), '')
        op = e.get('opacity', 100) / 100
        cx = e['x'] + e.get('width', 0) / 2; cy = e['y'] + e.get('height', 0) / 2
        rot = f' transform="rotate({math.degrees(e.get("angle", 0)):.1f} {cx} {cy})"' if e.get('angle') else ''
        fillop = 0.3 if bg != 'none' else 0
        common = f'stroke="{sc}" stroke-width="{sw}" fill="{bg}" fill-opacity="{fillop}" opacity="{op}" stroke-dasharray="{dash}" stroke-linejoin="round"{rot}'
        if t in ('rectangle', 'frame', 'embeddable', 'image'):
            rx = min(16, e['width'] * 0.15, e['height'] * 0.25) if e.get('roundness') else 0
            out.append(f'<rect x="{e["x"]}" y="{e["y"]}" width="{e["width"]}" height="{e["height"]}" rx="{rx}" {common}/>')
        elif t == 'ellipse':
            out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{e["width"] / 2}" ry="{e["height"] / 2}" {common}/>')
        elif t == 'diamond':
            w, h = e['width'], e['height']; X, Y = e['x'], e['y']
            out.append(f'<polygon points="{X + w / 2},{Y} {X + w},{Y + h / 2} {X + w / 2},{Y + h} {X},{Y + h / 2}" {common}/>')
        elif t in ('arrow', 'line', 'freedraw'):
            P = [(e['x'] + px, e['y'] + py) for px, py in e['points']]
            pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in P)
            out.append(f'<polyline points="{pts}" stroke="{sc}" stroke-width="{sw}" fill="none" opacity="{op}" stroke-dasharray="{dash}" stroke-linecap="round" stroke-linejoin="round"/>')
            if t == 'arrow' and len(P) >= 2:
                if e.get('endArrowhead'): out.append(arrowhead(P[-2], P[-1], sc, sw))
                if e.get('startArrowhead'): out.append(arrowhead(P[1], P[0], sc, sw))
    for e in els:
        if e['type'] != 'text': continue
        fs = e.get('fontSize', 20); lh = e.get('lineHeight', 1.25); lines = e.get('text', '').split('\n')
        al = e.get('textAlign', 'left'); anchor = {'left': 'start', 'center': 'middle', 'right': 'end'}[al]
        tx = {'left': e['x'], 'center': e['x'] + e['width'] / 2, 'right': e['x'] + e['width']}[al]
        cx = e['x'] + e['width'] / 2; cy = e['y'] + e['height'] / 2
        rot = f' transform="rotate({math.degrees(e.get("angle", 0)):.1f} {cx} {cy})"' if e.get('angle') else ''
        fam = FONT.get(e.get('fontFamily', 5), FONT[5])
        color = col(e.get('strokeColor')) if col(e.get('strokeColor')) != 'none' else '#1e1e1e'
        bgc = col(e.get('backgroundColor'))
        cont = byid_global.get(e.get('containerId'))
        if cont is not None and cont['type'] == 'arrow':
            out.append(f'<rect x="{e["x"] - 3}" y="{e["y"] - 1}" width="{e["width"] + 6}" height="{e["height"] + 2}" fill="white"/>')
        if bgc != 'none' and e.get('containerId') is None:
            out.append(f'<rect x="{e["x"] - 4}" y="{e["y"] - 2}" width="{e["width"] + 8}" height="{e["height"] + 4}" fill="{bgc}" fill-opacity="0.9"/>')
        out.append(f'<text font-family=\'{fam}\' font-size="{fs}" fill="{color}" text-anchor="{anchor}" opacity="{e.get("opacity", 100) / 100}"{rot}>')
        for i, l in enumerate(lines):
            out.append(f'<tspan x="{tx}" y="{e["y"] + fs * lh * i + fs * 0.9}">{html.escape(l) or " "}</tspan>')
        out.append('</text>')
    out.append('</svg>'); return '\n'.join(out)


def describe(els):
    byid = {e['id']: e for e in els}
    label = {}
    for e in els:
        if e['type'] == 'text' and e.get('containerId') in byid:
            label[e['containerId']] = label.get(e['containerId'], '') + e['text'].replace('\n', ' / ')
    shapes = [e for e in els if e['type'] in ('rectangle', 'ellipse', 'diamond', 'image', 'frame')]

    def name(eid):
        if eid is None: return None
        e = byid.get(eid)
        if not e: return '?'
        return f'[{e["type"][:4]}] "{label.get(eid, "(sin texto)")}"'

    def nearest(px, py):
        best = None; bd = 1e9
        for s in shapes:
            dx = max(s['x'] - px, 0, px - (s['x'] + s['width'])); dy = max(s['y'] - py, 0, py - (s['y'] + s['height'])); dd = math.hypot(dx, dy)
            if dd < bd: bd, best = dd, s
        return (name(best['id']) + f' (~{bd:.0f}px)') if best and bd < 60 else '(suelto)'

    L = ['## Formas (con su texto), ordenadas por posición (y, x)']
    for s in sorted(shapes, key=lambda s: (round(s['y'] / 80), s['x'])):
        L.append(f'- {s["type"]} @({s["x"]:.0f},{s["y"]:.0f}) {s["width"]:.0f}x{s["height"]:.0f} color={s.get("strokeColor")} bg={s.get("backgroundColor")} style={s.get("strokeStyle")}: "{label.get(s["id"], "")}"')
    L.append('\n## Textos libres, ordenados por posición')
    for e in sorted([e for e in els if e['type'] == 'text' and not e.get('containerId')], key=lambda e: (round(e['y'] / 80), e['x'])):
        L.append(f'- @({e["x"]:.0f},{e["y"]:.0f}) fs={e.get("fontSize")} color={e.get("strokeColor")}: {e["text"]!r}')
    L.append('\n## Conexiones (flechas/líneas)')
    for e in sorted([e for e in els if e['type'] in ('arrow', 'line')], key=lambda e: (round(e['y'] / 80), e['x'])):
        p0 = (e['x'] + e['points'][0][0], e['y'] + e['points'][0][1]); p1 = (e['x'] + e['points'][-1][0], e['y'] + e['points'][-1][1])
        a = name((e.get('startBinding') or {}).get('elementId')) or nearest(*p0)
        b = name((e.get('endBinding') or {}).get('elementId')) or nearest(*p1)
        heads = ('<' if e.get('startArrowhead') else '-') + '--' + ('>' if e.get('endArrowhead') else '-')
        L.append(f'- {e["type"]} {a} {heads} {b}  label="{label.get(e["id"], "")}" style={e.get("strokeStyle")} color={e.get("strokeColor")}')
    return '\n'.join(L)


def overlaps(els):
    """Pares de formas con texto que se superponen (para control de calidad)."""
    shapes = [e for e in els if e['type'] in ('rectangle', 'ellipse', 'diamond') and e.get('strokeStyle') != 'dashed']
    texts = [e for e in els if e['type'] == 'text' and not e.get('containerId')]
    items = shapes + texts
    bad = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a, b = items[i], items[j]
            if a['x'] < b['x'] + b['width'] and b['x'] < a['x'] + a['width'] and a['y'] < b['y'] + b['height'] and b['y'] < a['y'] + a['height']:
                bad.append((a['type'], a.get('text', a['id'])[:30], b['type'], b.get('text', b['id'])[:30]))
    return bad


if __name__ == '__main__':
    p = sys.argv[1]; scale = float(sys.argv[2]) if len(sys.argv) > 2 else 1.5
    base = os.path.splitext(p)[0]
    els = load(p)
    open(base + '.svg', 'w').write(svg(els))
    open(base + '.txt', 'w').write(describe(els))
    subprocess.run(['rsvg-convert', '-z', str(scale), '-o', base + '.png', base + '.svg'], check=True)
    ov = overlaps(els)
    print(f'{base}.png listo; elementos={len(els)}; solapes={len(ov)}')
    for o in ov[:40]: print('  SOLAPE', o)
