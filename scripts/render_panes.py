#!/usr/bin/env python3
"""Render the three terminal panes from data.json.

Panes are 600px wide at 16px type, which lands at ~9-10px effective on a phone
(a 880px pane at 14px lands at ~5px, which is unreadable).
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "scripts" / "data.json").read_text())
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "assets"
OUT.mkdir(parents=True, exist_ok=True)

MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'DejaVu Sans Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
W, FS, CW, LH = 600, 16, 9.62, 28
X0, BAR, TOP = 34, 44, 84
COLS = int((W - 2 * X0) / CW)          # 55
TYPE, PRINT, PAUSE, SPIN = 0.030, 0.14, 0.30, 0.085
SPIN_FRAMES = "⠋⠙⠹⠸⠼⠴⠦⠧"

T = {
    "dark": dict(bg="#0C1017", chrome="#141922", border="#222A36", bar_text="#6B7A90",
                 path="#7DD3FC", sign="#4ADE80", cmd="#E6EDF3", flag="#F0A868", pipe="#F472B6",
                 out="#93A2B8", strong="#F0F6FC", num="#FBBF24", repo="#A78BFA",
                 cursor="#4ADE80", dim="#5A6A80", glow="#FFFFFF", glow_op="0.030"),
    "light": dict(bg="#FFFFFF", chrome="#F2F4F8", border="#DDE3EC", bar_text="#7A8699",
                  path="#0369A1", sign="#15803D", cmd="#111827", flag="#B45309", pipe="#BE185D",
                  out="#4B5563", strong="#0F172A", num="#B45309", repo="#6D28D9",
                  cursor="#15803D", dim="#94A3B8", glow="#0F172A", glow_op="0.012"),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def syn(cmd):
    segs, tok = [], ""
    def flush():
        nonlocal tok
        if tok:
            key = "flag" if tok.startswith("-") else "pipe" if tok in ("|", ">", "&&") else "cmd"
            segs.append((tok, key)); tok = ""
    for ch in cmd:
        if ch == " ":
            flush(); segs.append((" ", "cmd"))
        else:
            tok += ch
    flush()
    return segs


PROMPT = [("~", "path"), (" git:(", "dim"), ("main", "num"), (")", "dim"), (" $ ", "sign")]
PLEN = sum(len(s) for s, _ in PROMPT)


def render(lines, title, t, tag):
    body, defs, clock, li = [], [], 0.0, 0

    for idx, e in enumerate(lines):
        kind, y = e[0], TOP + li * LH

        if kind == "gap":
            li += 1
            continue

        if kind == "raw":
            body.append(e[1])
            continue

        if kind == "prompt":
            spans = "".join(f'<tspan fill="{t[k]}">{esc(s)}</tspan>' for s, k in PROMPT)
            body.append(f'  <text x="{X0}" y="{y}" font-family="{MONO}" font-size="{FS}" opacity="0" xml:space="preserve">{spans}'
                        f'<set attributeName="opacity" to="1" begin="{clock:.2f}s"/></text>')
            body.append(f'  <rect x="{X0+PLEN*CW:.1f}" y="{y-12}" width="{CW:.1f}" height="17" rx="1.5" fill="{t["cursor"]}" opacity="0">'
                        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.45;0.5;1" dur="1.1s" begin="{clock:.2f}s" repeatCount="indefinite"/></rect>')
            li += 1
            continue

        if kind == "cmd":
            segs = PROMPT + syn(e[1])
            n = sum(len(s) for s, _ in segs)
            dur = len(e[1]) * TYPE
            cid = f"c{tag}{li}"
            defs.append(f'    <clipPath id="{cid}"><rect x="{X0}" y="{y-FS}" width="0" height="{LH}">'
                        f'<animate attributeName="width" values="0;{n*CW+4:.1f}" dur="{dur:.2f}s" begin="{clock:.2f}s" fill="freeze"/></rect></clipPath>')
            spans = "".join(f'<tspan fill="{t[k]}">{esc(s)}</tspan>' for s, k in segs)
            body.append(f'  <g clip-path="url(#{cid})"><text x="{X0}" y="{y}" font-family="{MONO}" font-size="{FS}" xml:space="preserve">{spans}</text></g>')
            body.append(f'  <rect y="{y-12}" width="{CW:.1f}" height="17" rx="1.5" fill="{t["cursor"]}" opacity="0" x="{X0+PLEN*CW:.1f}">'
                        f'<set attributeName="opacity" to="1" begin="{clock:.2f}s"/>'
                        f'<animate attributeName="x" values="{X0+PLEN*CW:.1f};{X0+n*CW:.1f}" dur="{dur:.2f}s" begin="{clock:.2f}s" fill="freeze"/>'
                        f'<set attributeName="opacity" to="0" begin="{clock+dur:.2f}s"/></rect>')
            clock += dur + PRINT
            li += 1
            continue

        if kind == "spin":
            for i, ch in enumerate(SPIN_FRAMES):
                body.append(f'  <text x="{X0}" y="{y}" font-family="{MONO}" font-size="{FS}" fill="{t["sign"]}" opacity="0">{ch}'
                            f'<set attributeName="opacity" to="1" begin="{clock+i*SPIN:.2f}s"/>'
                            f'<set attributeName="opacity" to="0" begin="{clock+(i+1)*SPIN:.2f}s"/></text>')
            clock += len(SPIN_FRAMES) * SPIN
            li += 1
            continue

        if kind == "bar":
            _, label, val, mx, key = e
            blocks = max(1, round(20 * val / mx))
            bx = X0 + 11 * CW
            cid = f"b{tag}{li}"
            defs.append(f'    <clipPath id="{cid}"><rect x="{bx:.1f}" y="{y-FS}" width="0" height="{LH}">'
                        f'<animate attributeName="width" values="0;{blocks*CW+2:.1f}" dur="0.75s" begin="{clock:.2f}s" fill="freeze"/></rect></clipPath>')
            body.append(f'  <text x="{X0}" y="{y}" font-family="{MONO}" font-size="{FS}" fill="{t["out"]}" opacity="0" xml:space="preserve">{esc(label)}'
                        f'<set attributeName="opacity" to="1" begin="{clock:.2f}s"/></text>')
            body.append(f'  <g clip-path="url(#{cid})"><text x="{bx:.1f}" y="{y}" font-family="{MONO}" font-size="{FS}" fill="{t[key]}">{"█"*blocks}</text></g>')
            body.append(f'  <text x="{bx + 21*CW:.1f}" y="{y}" font-family="{MONO}" font-size="{FS}" fill="{t["num"]}" opacity="0">{val}'
                        f'<set attributeName="opacity" to="1" begin="{clock+0.75:.2f}s"/></text>')
            clock += 0.30
            li += 1
            continue

        spans = "".join(f'<tspan fill="{t[k]}">{esc(s)}</tspan>' for s, k in e[1])
        body.append(f'  <text x="{e[2] if len(e) > 2 else X0}" y="{y}" font-family="{MONO}" font-size="{FS}" opacity="0" xml:space="preserve">{spans}'
                    f'<set attributeName="opacity" to="1" begin="{clock:.2f}s"/></text>')
        clock += PRINT
        li += 1
        if idx + 1 < len(lines) and lines[idx + 1][0] == "gap":
            clock += PAUSE

    h = TOP + (li - 1) * LH + 54
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{title}">
  <defs>
    <clipPath id="w{tag}"><rect width="{W}" height="{h}" rx="12"/></clipPath>
    <linearGradient id="s{tag}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{t['glow']}" stop-opacity="{t['glow_op']}"/>
      <stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/>
    </linearGradient>
{chr(10).join(defs)}
  </defs>
  <g clip-path="url(#w{tag})">
    <rect width="{W}" height="{h}" fill="{t['bg']}"/>
    <rect y="{BAR}" width="{W}" height="140" fill="url(#s{tag})"/>
    <rect width="{W}" height="{BAR}" fill="{t['chrome']}"/>
    <line x1="0" y1="{BAR}" x2="{W}" y2="{BAR}" stroke="{t['border']}"/>
    <circle cx="24" cy="22" r="5.5" fill="#FF5F57"/><circle cx="43" cy="22" r="5.5" fill="#FEBC2E"/><circle cx="62" cy="22" r="5.5" fill="#28C840"/>
    <text x="{W//2}" y="26" text-anchor="middle" font-family="{SANS}" font-size="11.5" font-weight="600" fill="{t['bar_text']}">{title}</text>
{chr(10).join(body)}
  </g>
  <rect x="0.5" y="0.5" width="{W-1}" height="{h-1}" rx="12" fill="none" stroke="{t['border']}"/>
</svg>
"""


def hero(t):
    ls = [("cmd", "whoami"),
          ("out", [("Achyuthan Sivasankar", "strong")]),
          ("out", [("research assistant · Choromanska Lab, NYU", "out")]),
          ("gap",),
          ("cmd", "cat focus.txt"),
          ("out", [("sparse neural routing", "out")]),
          ("out", [("self-supervised world models · LiDAR", "out")]),
          ("gap",),
          ("cmd", "ls upstream/")]
    for r in DATA["repos"]:
        ls.append(("out", [(r, "repo")]))
    ls += [("gap",),
           ("cmd", "git log --merged --upstream | wc -l"),
           ("spin",),
           ("out", [(str(DATA["count"]), "num"), ("  and counting", "out")]),
           ("gap",), ("prompt",)]
    return render(ls, "achyuthan@nyu — zsh", t, "h")


ART = ["██████   ██████ ", "██   ██  ██     ", "██   ██  ██     ", "███████   █████ ",
       "██   ██       ██", "██   ██       ██", "██   ██  ██████ "]
CELL = 7
IX = X0 + len(ART[0]) * CELL + 22


def art_rects(t):
    """Run-length the block rows into rects — block glyphs gap on the text grid."""
    y_top = TOP + 2 * LH - 16
    out = []
    for r, row in enumerate(ART):
        c = 0
        while c < len(row):
            if row[c] == "█":
                run = 0
                while c + run < len(row) and row[c + run] == "█":
                    run += 1
                out.append(f'<rect x="{X0 + c*CELL}" y="{y_top + r*CELL}" width="{run*CELL}" height="{CELL}" fill="{t["sign"]}"/>')
                c += run
            else:
                c += 1
    return ('  <g opacity="0">' + "".join(out) +
            '<animate attributeName="opacity" values="0;1" dur="0.45s" begin="1.0s" fill="freeze"/></g>')


def neofetch(t):
    info = [("Host", "Choromanska Lab, NYU"), ("Role", "research assistant"),
            ("Focus", "sparse MoE · world models"), ("Upstream", DATA["orgs_line"]),
            ("Merged", f"{DATA['count']} PRs and counting"), ("Preprints", "2 (sole author)"),
            ("Langs", "Python · C/C++ · Go"), ("Stack", "PyTorch · Docker · AWS"),
            ("Blog", "blog-blogachyuthan.vercel.app"), ("Contact", "as21154@nyu.edu")]
    ls = [("cmd", "neofetch"), ("gap",), ("raw", art_rects(t))]
    for i in range(len(info) + 2):
        if i == 0:
            segs = [("achyuthan", "num"), ("@", "out"), ("nyu", "path")]
        elif i == 1:
            segs = [("─" * 29, "dim")]
        else:
            k, v = info[i - 2]
            segs = [(f"{k+':':<10}", "strong"), (v, "out")]
        ls.append(("out", segs, IX))
    ls += [("gap",),
           ("out", [("███", "path"), ("███", "sign"), ("███", "num"),
                    ("███", "pipe"), ("███", "repo"), ("███", "flag")]),
           ("gap",), ("prompt",)]
    return render(ls, "achyuthan@nyu — neofetch", t, "n")


def upstream(t):
    ls = [("cmd", "git log --merged --upstream | head -5"), ("gap",)]
    for e in DATA["recent"]:
        ls.append(("out", [("* ", "sign"), (f"{e['number']:<7}", "num"),
                           (f"{e['short']:<11}", "repo"), (e["msg"], "out")]))
    ls += [("gap",), ("cmd", "prs --by-org"), ("gap",)]
    mx = max(o["count"] for o in DATA["by_org"])
    for o in DATA["by_org"]:
        ls.append(("bar", f"{o['name']:<10}", o["count"], mx, o["colour"]))
    ls += [("gap",), ("prompt",)]
    return render(ls, "achyuthan@nyu — upstream", t, "u")


over = []
for name, fn in (("term", hero), ("neofetch", neofetch), ("upstream", upstream)):
    for theme, t in T.items():
        svg = fn(t)
        (OUT / f"{name}-{theme}.svg").write_text(svg)
    for ln in fn(T["dark"]).split("\n"):
        pass
print(f"rendered 6 SVGs at {W}px into {OUT}")
