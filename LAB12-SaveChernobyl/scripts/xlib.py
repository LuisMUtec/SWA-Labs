"""Mini-librería para generar archivos .excalidraw con el estilo "a mano" del profe
(Excalifont = fontFamily 5, trazo negro #1e1e1e, fondo transparente, roughness 1, strokeWidth 2).
Pensada para el Lab 12 pero reutilizable."""
import json, math

BLACK = '#1e1e1e'; RED = '#e03131'; BLUE = '#1971c2'; ORANGE = '#f08c00'
GREEN = '#2f9e44'; PURPLE = '#9c36b5'; GRAY = '#868e96'
B62 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
CHAR_W = 0.60   # ancho medio de un carácter Excalifont en "em"
LINE_H = 1.25


def text_size(txt, fs):
    lines = txt.split('\n')
    return max(len(l) for l in lines) * fs * CHAR_W, len(lines) * fs * LINE_H


class Canvas:
    def __init__(self):
        self.els = []
        self.byid = {}
        self._n = 0

    # ---------- infraestructura ----------
    def _id(self):
        self._n += 1
        return f'L12e{self._n:05d}'

    def _index(self):
        v = self._n; s = ''
        for _ in range(3):
            s = B62[v % 62] + s; v //= 62
        return 'c' + s

    def _base(self, t, x, y, w, h, stroke=BLACK, bg='transparent', sw=2, style='solid',
              opacity=100, roundness='auto', fill='solid'):
        if roundness == 'auto':
            roundness = {'type': 3} if t == 'rectangle' else ({'type': 2} if t in ('ellipse', 'diamond', 'arrow', 'line') else None)
        e = {'id': self._id(), 'type': t, 'x': float(x), 'y': float(y), 'width': float(w), 'height': float(h),
             'angle': 0, 'strokeColor': stroke, 'backgroundColor': bg, 'fillStyle': fill,
             'strokeWidth': sw, 'strokeStyle': style, 'roughness': 1, 'opacity': opacity,
             'groupIds': [], 'frameId': None, 'index': self._index(), 'roundness': roundness,
             'seed': 100000 + self._n * 7919, 'version': 1, 'versionNonce': 200000 + self._n * 104729,
             'isDeleted': False, 'boundElements': [], 'updated': 1, 'link': None, 'locked': False}
        return e

    def _add(self, e):
        self.els.append(e); self.byid[e['id']] = e
        return e

    # ---------- textos ----------
    def text(self, x, y, txt, fs=20, color=BLACK, align='left', font=5, container=None, valign=None):
        w, h = text_size(txt, fs)
        t = self._base('text', x, y, w, h, stroke=color, roundness=None)
        t.update({'text': txt, 'originalText': txt, 'fontSize': fs, 'fontFamily': font, 'textAlign': align,
                  'verticalAlign': valign or ('middle' if container else 'top'),
                  'containerId': container['id'] if container else None, 'autoResize': True, 'lineHeight': LINE_H})
        if container:
            t['textAlign'] = 'center'
            t['x'] = container['x'] + container['width'] / 2 - w / 2
            t['y'] = container['y'] + container['height'] / 2 - h / 2
            container['boundElements'].append({'type': 'text', 'id': t['id']})
        return self._add(t)

    # ---------- formas ----------
    def shape(self, t, x, y, w, h, label=None, fs=20, tcolor=None, **kw):
        if label is not None:
            tw, th = text_size(label, fs)
            w = max(w, tw + 24); h = max(h, th + 16)
        e = self._add(self._base(t, x, y, w, h, **kw))
        if label is not None:
            self.text(0, 0, label, fs, tcolor or kw.get('stroke', BLACK), container=e)
        return e

    def rect(self, x, y, w, h, label=None, **kw):
        return self.shape('rectangle', x, y, w, h, label, **kw)

    def ellipse(self, x, y, w, h, label=None, **kw):
        return self.shape('ellipse', x, y, w, h, label, **kw)

    def diamond(self, x, y, w, h, label=None, **kw):
        return self.shape('diamond', x, y, w, h, label, **kw)

    def box(self, x, y, w, h, color=GRAY, style='dashed', sw=2):
        """Recuadro grande (módulo / iteración), sin texto."""
        return self._add(self._base('rectangle', x, y, w, h, stroke=color, style=style, sw=sw))

    def actor(self, x, y, name, color=BLACK, fs=20):
        """Monigote como el del profe: cabeza (elipse 50x52) + cuerpo + brazos + nombre debajo.
        (x, y) = esquina superior izquierda de la cabeza. Devuelve la cabeza (para unir flechas)."""
        head = self._add(self._base('ellipse', x, y, 50, 52, stroke=color))
        body = self._add(self._base('line', x + 25, y + 51, 0, 58, stroke=color))
        body.update({'points': [[0, 0], [0, 58]], 'lastCommittedPoint': None, 'startArrowhead': None, 'endArrowhead': None})
        arms = self._add(self._base('line', x + 2, y + 66, 47, 11, stroke=color))
        arms.update({'points': [[0, 0], [47, 11]], 'lastCommittedPoint': None, 'startArrowhead': None, 'endArrowhead': None})
        for dx in (-22, 22):
            leg = self._add(self._base('line', x + 25, y + 109, abs(dx), 40, stroke=color))
            leg.update({'points': [[0, 0], [dx, 40]], 'lastCommittedPoint': None, 'startArrowhead': None, 'endArrowhead': None})
        tw, th = text_size(name, fs)
        self.text(x + 25 - tw / 2, y + 152, name, fs, color, align='center')
        gid = head['id'] + '_g'
        for e in self.els[-6:]:
            e['groupIds'] = [gid]
        head['_actor_bbox'] = (x - 22, y, x + 72, y + 152 + th)
        return head

    def db(self, x, y, name, color=BLACK, fs=20, w=None, h=None):
        """BD como círculo "X DB" (notación del simulacro del profe)."""
        tw, th = text_size(name, fs)
        d = max(w or 0, tw + 30, 90)
        return self.ellipse(x, y, d, h or d, name, fs=fs, stroke=color, tcolor=color)

    # ---------- geometría ----------
    def bbox(self, e):
        if e['type'] in ('arrow', 'line'):
            xs = [e['x'] + p[0] for p in e['points']]; ys = [e['y'] + p[1] for p in e['points']]
            return min(xs), min(ys), max(xs), max(ys)
        if '_actor_bbox' in e:
            return e['x'], e['y'], e['x'] + e['width'], e['y'] + e['height']
        return e['x'], e['y'], e['x'] + e['width'], e['y'] + e['height']

    def center(self, e):
        a, b, c, d = self.bbox(e); return (a + c) / 2, (b + d) / 2

    def border(self, e, tx, ty):
        """Punto del borde de e en dirección al punto (tx, ty)."""
        a, b, c, d = self.bbox(e); cx, cy = (a + c) / 2, (b + d) / 2
        dx, dy = tx - cx, ty - cy
        if dx == 0 and dy == 0:
            return cx, cy
        hw, hh = (c - a) / 2, (d - b) / 2
        if e['type'] == 'ellipse':
            k = 1 / math.sqrt((dx / hw) ** 2 + (dy / hh) ** 2)
        elif e['type'] == 'diamond':
            k = 1 / ((abs(dx) / hw) + (abs(dy) / hh))
        else:
            k = min(hw / abs(dx) if dx else 1e9, hh / abs(dy) if dy else 1e9)
        return cx + dx * k, cy + dy * k

    def _fixed(self, e, px, py):
        a, b, c, d = self.bbox(e)
        return [min(max((px - a) / (c - a), 0), 1), min(max((py - b) / (d - b), 0), 1)]

    # ---------- conectores ----------
    def arrow(self, s, t, label=None, via=None, color=BLACK, sw=2, style='solid', heads='end',
              fs=16, lcolor=None, start_at=None, end_at=None, label_dx=0, label_dy=0, shift=0, label_at=0.5, label_seg=None):
        """Flecha de s a t. heads: 'end' | 'both' | 'none' (none = línea simple como las sensor->controller del profe).
        via = lista de puntos intermedios absolutos. start_at/end_at = puntos absolutos forzados en el borde."""
        via = list(via or [])
        p0 = start_at or self.border(s, *(via[0] if via else self.center(t)))
        p1 = end_at or self.border(t, *(via[-1] if via else self.center(s)))
        if shift:
            dx, dy = p1[0] - p0[0], p1[1] - p0[1]; L = math.hypot(dx, dy) or 1
            nx, ny = -dy / L * shift, dx / L * shift
            p0 = (p0[0] + nx, p0[1] + ny); p1 = (p1[0] + nx, p1[1] + ny)
        pts = [p0] + via + [p1]
        ar = self._base('arrow', p0[0], p0[1], 1, 1, stroke=color, sw=sw, style=style)
        ar.update({'points': [[px - p0[0], py - p0[1]] for px, py in pts], 'lastCommittedPoint': None,
                   'startArrowhead': 'arrow' if heads == 'both' else None,
                   'endArrowhead': None if heads == 'none' else 'arrow', 'elbowed': False})
        xs = [p[0] for p in ar['points']]; ys = [p[1] for p in ar['points']]
        ar['width'] = max(xs) - min(xs); ar['height'] = max(ys) - min(ys)
        ar['startBinding'] = {'elementId': s['id'], 'mode': 'orbit', 'fixedPoint': self._fixed(s, *p0)}
        ar['endBinding'] = {'elementId': t['id'], 'mode': 'orbit', 'fixedPoint': self._fixed(t, *p1)}
        s['boundElements'].append({'id': ar['id'], 'type': 'arrow'})
        t['boundElements'].append({'id': ar['id'], 'type': 'arrow'})
        self._add(ar)
        if label:
            i = (label_seg + 1) if label_seg is not None else len(pts) // 2
            mx = pts[i - 1][0] + (pts[i][0] - pts[i - 1][0]) * label_at + label_dx
            my = pts[i - 1][1] + (pts[i][1] - pts[i - 1][1]) * label_at + label_dy
            tl = self.text(mx, my, label, fs, lcolor or color, align='center')
            tl['containerId'] = ar['id']; tl['verticalAlign'] = 'middle'
            tl['x'] = mx - tl['width'] / 2; tl['y'] = my - tl['height'] / 2
            ar['boundElements'].append({'type': 'text', 'id': tl['id']})
        return ar

    def line(self, pts, color=BLACK, sw=2, style='solid'):
        """Polilínea libre (sin puntas, sin binding)."""
        x0, y0 = pts[0]
        l = self._base('line', x0, y0, 1, 1, stroke=color, sw=sw, style=style)
        l.update({'points': [[px - x0, py - y0] for px, py in pts], 'lastCommittedPoint': None,
                  'startArrowhead': None, 'endArrowhead': None})
        xs = [p[0] for p in l['points']]; ys = [p[1] for p in l['points']]
        l['width'] = max(xs) - min(xs); l['height'] = max(ys) - min(ys)
        return self._add(l)

    # ---------- marcas ----------
    def mark_spof(self, e, note=None, fs=16, where='below', dx=0):
        """Marca un elemento como SPOF: lo pinta de rojo + etiqueta 'SPOF' debajo/arriba (y nota opcional)."""
        e['strokeColor'] = RED
        for b in e.get('boundElements', []):
            if b['type'] == 'text':
                self.byid[b['id']]['strokeColor'] = RED
        a, b_, c, d = self.bbox(e)
        tag = 'SPOF' + (f': {note}' if note else '')
        tw, th = text_size(tag, fs)
        y = d + 4 if where == 'below' else b_ - th - 4
        return self.text((a + c) / 2 - tw / 2 + dx, y, tag, fs, RED, align='center')

    def cross(self, e, color=RED, sw=3):
        a, b, c, d = self.bbox(e)
        self.line([(a, b), (c, d)], color, sw); self.line([(a, d), (c, b)], color, sw)

    def stack(self, x, y, w, h, label, n=2, off=10, **kw):
        """Cajas apiladas = instancias replicadas (notación del profe). Devuelve la caja frontal."""
        for i in range(n - 1, 0, -1):
            self._add(self._base('rectangle', x + off * i, y - off * i, w, h, **{k: v for k, v in kw.items() if k in ('stroke', 'bg', 'sw', 'style')}))
        return self.rect(x, y, w, h, label, **kw)

    # ---------- salida ----------
    def extent(self):
        xs, ys = [], []
        for e in self.els:
            a, b, c, d = self.bbox(e); xs += [a, c]; ys += [b, d]
        return min(xs), min(ys), max(xs), max(ys)

    def save(self, path):
        els = []
        for e in self.els:
            e = dict(e); e.pop('_actor_bbox', None); els.append(e)
        doc = {'type': 'excalidraw', 'version': 2, 'source': 'https://excalidraw.com', 'elements': els,
               'appState': {'gridSize': 20, 'gridStep': 5, 'gridModeEnabled': False, 'viewBackgroundColor': '#ffffff',
                            'lockedMultiSelections': {}}, 'files': {}}
        with open(path, 'w') as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
        return path
