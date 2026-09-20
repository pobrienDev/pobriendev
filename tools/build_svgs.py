"""Builds the animated SVGs used by the profile README (dark and light variants).

Run:  python3 tools/build_svgs.py
Logos in tools/icons/ come from Simple Icons (CC0). The Graph API and Entra ID
glyphs are simple custom shapes, not official marks. To add a tile, drop the
Simple Icons SVG into tools/icons/ and add a row to the `items` list in stack().
"""
import re, html, os
HERE = os.path.dirname(os.path.abspath(__file__))
ICONS = os.path.join(HERE, "icons")
OUT = os.path.join(HERE, "..", "assets")
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

THEMES = {
  "dark":  dict(bg="#10141A", bar="#171D26", border="#2A323F", text="#E7EBEF", dim="#94A1B2", accent="#E8A33D", dot="#2A323F",
                tile="#171D26", neutral="#E7EBEF"),
  "light": dict(bg="#FFFFFF", bar="#F6F8FA", border="#D0D7DE", text="#1F2328", dim="#57606A", accent="#9A6700", dot="#D0D7DE",
                tile="#F6F8FA", neutral="#1F2328"),
}

# ---------------------------------------------------------------- header
def header(t):
    W, H = 840, 236
    cw = 9.2                      # fixed advance per typed character (each glyph is placed explicitly)
    x0, y1 = 28, 74
    word = "whoami"
    step = 0.11
    start = 0.6
    chars = "".join(
        f'<text class="c" style="animation-delay:{start + (i+1)*step:.2f}s" x="{x0 + 2*cw + i*cw:.1f}" y="{y1}">{ch}</text>'
        for i, ch in enumerate(word))
    typed_end = start + (len(word)+1)*step          # when typing is done
    out1, out2, out3, prompt2 = typed_end+0.25, typed_end+0.55, typed_end+0.85, typed_end+1.35
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H+12}" width="{W}" height="{H+12}" role="img" aria-labelledby="t d">
<title id="t">Patrick O'Brien, Software Engineer</title>
<desc id="d">A terminal window types the command whoami and prints: Patrick O'Brien, Software Engineer, identity and access automation, full-stack web apps, Baltimore, Maryland.</desc>
<style>
  .mono{{font-family:{MONO};font-size:15px}}
  .c{{font-family:{MONO};font-size:15px;fill:{t["text"]};animation:show .01s linear both}}
  .fade{{animation:fadeup .45s ease-out both}}
  .cur1{{opacity:0;animation:move {len(word)*step:.2f}s steps({len(word)},end) {start+step:.2f}s forwards, on {typed_end+0.15:.2f}s linear 0s 1}}
  .cur2{{animation:off {prompt2:.2f}s linear 0s 1, blink 1.1s steps(1,end) {prompt2:.2f}s infinite}}
  @keyframes show{{from{{opacity:0}}to{{opacity:1}}}}
  @keyframes fadeup{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:translateY(0)}}}}
  @keyframes move{{to{{transform:translateX({len(word)*cw:.1f}px)}}}}
  @keyframes on{{from,to{{opacity:1}}}}
  @keyframes off{{from,to{{opacity:0}}}}
  @keyframes blink{{0%{{opacity:1}}50%{{opacity:0}}100%{{opacity:0}}}}
  @media (prefers-reduced-motion: reduce){{
    .c,.fade,.cur1,.cur2{{animation:none}}
  }}
</style>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="{t["bg"]}" stroke="{t["border"]}"/>
<path d="M1 11 A10 10 0 0 1 11 1 H{W-11} A10 10 0 0 1 {W-1} 11 V36 H1 Z" fill="{t["bar"]}"/>
<line x1="1" y1="36.5" x2="{W-1}" y2="36.5" stroke="{t["border"]}"/>
<circle cx="22" cy="18.5" r="5.5" fill="{t["dot"]}"/><circle cx="41" cy="18.5" r="5.5" fill="{t["dot"]}"/><circle cx="60" cy="18.5" r="5.5" fill="{t["dot"]}"/>
<text x="{W/2}" y="23" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="{t["dim"]}">pobriendev: ~</text>

<text class="mono" x="{x0}" y="{y1}" fill="{t["accent"]}">$</text>
{chars}
<rect class="cur1" x="{x0 + 2*cw:.1f}" y="{y1-14}" width="9" height="18" fill="{t["accent"]}"/>

<g class="fade" style="animation-delay:{out1:.2f}s">
  <text x="{x0}" y="126" font-family="{SANS}" font-size="36" font-weight="700" fill="{t["text"]}" letter-spacing="-0.3">Patrick O'Brien</text>
</g>
<g class="fade" style="animation-delay:{out2:.2f}s">
  <text x="{x0}" y="156" font-family="{SANS}" font-size="17" font-weight="600" fill="{t["accent"]}">Software Engineer</text>
</g>
<g class="fade" style="animation-delay:{out3:.2f}s">
  <text x="{x0}" y="182" font-family="{MONO}" font-size="13" fill="{t["dim"]}">identity &amp; access automation  ·  full-stack web apps  ·  Baltimore, MD</text>
</g>

<g class="fade" style="animation-delay:{prompt2-0.1:.2f}s">
  <text class="mono" x="{x0}" y="214" fill="{t["accent"]}">$</text>
</g>
<rect class="cur2" x="{x0 + 2*cw:.1f}" y="200" width="9" height="18" fill="{t["accent"]}"/>
</svg>
'''

# ---------------------------------------------------------------- tech stack
def icon_path(name):
    svg = open(os.path.join(ICONS, f"{name}.svg")).read()
    ds = re.findall(r'<path d="([^"]+)"', svg)
    assert len(ds) == 1, name
    return f'<path d="{ds[0]}"/>'

# Simple neutral glyphs for the two Microsoft services with no CC0 logo (not official marks)
GRAPH = ('<g fill="none" stroke-width="1.8" stroke-linecap="round"><path d="M12 4.5 5 18.5M12 4.5l7 14M5 18.5h14"/></g>'
         '<circle cx="12" cy="4.5" r="2.6"/><circle cx="5" cy="18.5" r="2.6"/><circle cx="19" cy="18.5" r="2.6"/>')
ENTRA = ('<path fill-rule="evenodd" d="M12 1.5 3.5 4.8v6.4c0 5.3 3.5 9.6 8.5 11.3 5-1.7 8.5-6 8.5-11.3V4.8L12 1.5zm0 5.2a3 3 0 1 1 0 6 3 3 0 0 1 0-6zm0 7.6c2.4 0 4.5 1.1 5.4 2.8A9.6 9.6 0 0 1 12 20.6a9.6 9.6 0 0 1-5.4-3.5c.9-1.700 3-2.800 5.4-2.800z"/>')

def stack(t):
    items = [  # label, source, colour (None = theme neutral)
      ("Python", "python", "#3776AB"), ("TypeScript", "typescript", "#3178C6"), ("JavaScript", "javascript", "#F7DF1E" if t is THEMES["dark"] else "#C9A500"), ("PowerShell", "powershell", "#5391FE"),
      ("React", "react", "#61DAFB" if t is THEMES["dark"] else "#0A7EA4"), ("FastAPI", "fastapi", "#009688"), ("Flask", "flask", None),
      ("PostgreSQL", "postgresql", "#4169E1"), ("Graph API", GRAPH, None), ("Entra ID", ENTRA, None),
      ("Azure", "microsoftazure", "#0078D4"), ("Terraform", "terraform", "#844FBA"), ("GitHub Actions", "githubactions", "#2088FF"),
    ]
    cols, pitch_x, pitch_y, tw, th = 7, 100, 94, 92, 84
    W, H = cols*pitch_x - (pitch_x - tw), 2*pitch_y - (pitch_y - th)
    tiles = []
    for i, (label, src, colour) in enumerate(items):
        x, y = (i % cols)*pitch_x, (i // cols)*pitch_y
        colour = colour or t["neutral"]
        glyph = src if src.startswith("<") else icon_path(src)
        stroke = f' stroke="{colour}"' if src is GRAPH else ""
        size = 10.5 if len(label) <= 11 else 9.5
        tiles.append(
          f'<g class="tile" style="animation-delay:{0.15 + i*0.06:.2f}s">'
          f'<rect x="{x+0.5}" y="{y+0.5}" width="{tw-1}" height="{th-1}" rx="8" fill="{t["tile"]}" stroke="{t["border"]}"/>'
          f'<g transform="translate({x + tw/2 - 15},{y+15}) scale(1.25)" fill="{colour}"{stroke}>{glyph}</g>'
          f'<text x="{x + tw/2}" y="{y+68}" text-anchor="middle" font-family="{MONO}" font-size="{size}" fill="{t["dim"]}">{html.escape(label)}</text>'
          f'</g>')
    names = ", ".join(l for l, _, _ in items)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">
<title id="t">Working with: {names}</title>
<style>
  .tile{{animation:rise .5s cubic-bezier(.2,.7,.2,1) both}}
  @keyframes rise{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:translateY(0)}}}}
  @media (prefers-reduced-motion: reduce){{.tile{{animation:none}}}}
</style>
{chr(10).join(tiles)}
</svg>
'''

for name, t in THEMES.items():
    open(f"{OUT}/header-{name}.svg", "w").write(header(t))
    open(f"{OUT}/stack-{name}.svg", "w").write(stack(t))
print("built:", *sorted(os.listdir(OUT)))
