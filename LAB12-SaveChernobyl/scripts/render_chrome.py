"""Renderiza un .excalidraw a SVG (con render_x.svg) y a PNG con Chrome headless (no hay rsvg-convert).
Uso: python3 -I render_chrome.py archivo.excalidraw [escala]"""
import sys, os, re, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_x

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
p = sys.argv[1]; scale = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
base = os.path.splitext(p)[0]
els = render_x.load(p)
s = render_x.svg(els)
m = re.search(r'width="(\d+)" height="(\d+)"', s)
W, H = int(int(m.group(1)) * scale), int(int(m.group(2)) * scale)
if scale != 1.0:
    s = s.replace(m.group(0), f'width="{W}" height="{H}"', 1)
open(base + '.svg', 'w').write(s)
open(base + '.txt', 'w').write(render_x.describe(els))
profile = os.path.join(tempfile.gettempdir(), 'lab12-chrome-profile')
subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--no-default-browser-check',
                f'--user-data-dir={profile}', '--force-device-scale-factor=1', f'--window-size={W},{H}',
                '--virtual-time-budget=3000', f'--screenshot={base}.png', 'file://' + os.path.abspath(base + '.svg')],
               check=True, capture_output=True)
ov = render_x.overlaps(els)
print(f'{base}.png {W}x{H}; elementos={len(els)}; solapes={len(ov)}')
for o in ov[:40]: print('  SOLAPE', o)
