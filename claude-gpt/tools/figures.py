"""『클로드·GPT 완전정복 100단계』의 개념 그림을 설계안(JSON)에서 SVG로 그린다.

설계안은 docs/ebook/figures/*.json 에 둔다. 그림 하나는 이렇게 생겼다.
  {"id": "f03-deploy", "step": 30, "before": "### 따라 하기", "caption": "...", "type": "flow", ...}
step 단계 안의 before 제목 바로 앞에 그림이 들어간다(step 0은 머리말).

그림의 꼴은 여섯 가지다: flow(왼쪽→오른쪽 흐름), stack(층), compare(두 쪽 비교),
hub(가운데와 둘레), cycle(돌아가는 고리), grid(작은 표).

색은 SVG에 적지 않고 fg-* 이름표만 단다. PDF(밝은 바탕)와 웹(어두운 바탕)이 각자의 CSS로 칠한다.
화면 캡처는 쓰지 않는다. 기능이 바뀌면 캡처는 낡지만 개념 그림은 오래 간다.
"""
import glob
import html
import json
import math
import os
import re

W = 720          # 그림 폭(viewBox). 실제 크기는 CSS가 맞춘다
T, S = 15, 12.5  # 제목·설명 글자 크기
LH = 1.38        # 줄 간격


def text_w(t, size):
    w = 0.0
    for ch in t:
        if "가" <= ch <= "힣" or "㄰" <= ch <= "㆏":
            w += 1.0
        elif ch in " ":
            w += 0.3
        elif ch in "·.,:;!|()[]{}'\"`":
            w += 0.34
        elif ch.isupper() or ch in "→←↔×★☆":
            w += 0.68
        else:
            w += 0.56
    return w * size


def wrap(t, size, width):
    """단어(띄어쓰기) 단위로 줄을 나눈다. 한 단어가 너무 길면 글자 단위로 자른다."""
    if not t:
        return []
    lines, cur = [], ""
    for word in t.split(" "):
        cand = (cur + " " + word).strip()
        if text_w(cand, size) <= width or not cur:
            cur = cand
        else:
            lines.append(cur)
            cur = word
        while text_w(cur, size) > width and len(cur) > 1:
            k = len(cur)
            while k > 1 and text_w(cur[:k], size) > width:
                k -= 1
            lines.append(cur[:k])
            cur = cur[k:]
    if cur:
        lines.append(cur)
    return lines


def tspans(lines, x, y, size, cls, anchor="middle"):
    out = []
    for i, ln in enumerate(lines):
        out.append('<text x="%.1f" y="%.1f" class="%s" font-size="%s" text-anchor="%s">%s</text>'
                   % (x, y + i * size * LH, cls, size, anchor, html.escape(ln)))
    return "".join(out)


def block_h(tl, sl):
    h = len(tl) * T * LH - T * (LH - 1)
    if sl:
        h += 7 + len(sl) * S * LH - S * (LH - 1)
    return h


def card(x, y, w, node, hl=False, pad=11, min_h=0):
    """제목과 설명이 든 상자의 (높이, 제목 줄, 설명 줄)."""
    tl = wrap(node.get("t", ""), T, w - 2 * pad)
    sl = wrap(node.get("s", ""), S, w - 2 * pad)
    return max(block_h(tl, sl) + 2 * pad + 4, min_h), tl, sl


def draw_card(x, y, w, h, tl, sl, hl=False, box=True):
    ty = y + (h - block_h(tl, sl)) / 2 + T * 0.8
    out = ['<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="10" class="%s"/>' % (x, y, w, h, "fg-hl" if hl else "fg-box")] if box else []
    out.append(tspans(tl, x + w / 2, ty, T, "fg-t"))
    if sl:
        sy = ty + (len(tl) - 1) * T * LH + T * 0.25 + 7 + S * 0.85
        out.append(tspans(sl, x + w / 2, sy, S, "fg-s"))
    return "".join(out)


def arrow(x1, y1, x2, y2):
    ang = math.atan2(y2 - y1, x2 - x1)
    a, b = 8, 5
    p1 = (x2 - a * math.cos(ang) + b * math.sin(ang), y2 - a * math.sin(ang) - b * math.cos(ang))
    p2 = (x2 - a * math.cos(ang) - b * math.sin(ang), y2 - a * math.sin(ang) + b * math.cos(ang))
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" class="fg-ar"/>'
            '<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f Z" class="fg-ah"/>'
            % (x1, y1, x2 - a * 0.6 * math.cos(ang), y2 - a * 0.6 * math.sin(ang), x2, y2, p1[0], p1[1], p2[0], p2[1]))


def flow(sp):
    nodes, hl = sp["nodes"], set(sp.get("hl", []))
    labels = sp.get("labels") or []
    n = len(nodes)
    per = n if n <= 4 else math.ceil(n / 2)   # 다섯 개가 넘으면 두 줄로 꺾는다
    gap = 44 if any(labels) else 34
    bw = (W - 20 - (per - 1) * gap) / per
    lab_h = 22 if any(labels) else 0
    dims = [card(0, 0, bw, nd) for nd in nodes]
    h = max(d[0] for d in dims)
    row_gap = 44 + lab_h
    out, pos = [], []
    for i in range(n):
        r, c = divmod(i, per)
        pos.append((10 + c * (bw + gap), 6 + lab_h + r * (h + row_gap)))
    for i, (nd, (_, tl, sl)) in enumerate(zip(nodes, dims)):
        x, y = pos[i]
        out.append(draw_card(x, y, bw, h, tl, sl, i in hl))
        if i < n - 1:
            nx, ny = pos[i + 1]
            lab = labels[i] if i < len(labels) else ""
            if ny == y:
                ax = x + bw + 4
                out.append(arrow(ax, y + h / 2, nx - 4, y + h / 2))
                lx, ly = ax + (nx - 4 - ax) / 2, y - 8
            else:  # 줄 끝에서 아래 줄 처음으로 꺾어 내려간다
                mid = y + h + row_gap / 2
                out.append('<path d="M%.1f %.1f V%.1f H%.1f" class="fg-ar" fill="none"/>' % (x + bw / 2, y + h + 4, mid, nx + bw / 2))
                out.append(arrow(nx + bw / 2, mid, nx + bw / 2, ny - 4))
                lx, ly = W / 2, mid - 6
            if lab:
                out.append(tspans([lab], lx, ly, 11, "fg-lab"))
    return "".join(out), pos[-1][1] + h + 8


def stack(sp):
    layers, hl = sp["layers"], set(sp.get("hl", []))
    bw, x, y, out = 560, (W - 560) / 2, 6, []
    for i, ly in enumerate(layers):
        h, tl, sl = card(0, 0, bw - 60, ly, min_h=50)
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="10" class="%s"/>'
                   % (x, y, bw, h, "fg-hl" if i in hl else "fg-box"))
        out.append('<text x="%.1f" y="%.1f" class="fg-n" font-size="18" text-anchor="middle">%d</text>' % (x + 26, y + h / 2 + 6, i + 1))
        out.append(draw_card(x + 50, y, bw - 60, h, tl, sl, box=False))
        y += h + 10
    return "".join(out), y


def compare(sp):
    cw, out, hmax = (W - 40) / 2, [], 0
    for k, side in enumerate(("left", "right")):
        col = sp[side]
        x = 10 + k * (cw + 20)
        out.append('<rect x="%.1f" y="6" width="%.1f" height="40" rx="10" class="%s"/>' % (x, cw, "fg-hl" if k else "fg-box"))
        out.append(tspans([col["title"]], x + cw / 2, 32, T, "fg-t"))
        y = 70
        for it in col["items"]:
            lines = wrap(it, 13.5, cw - 40)
            out.append('<circle cx="%.1f" cy="%.1f" r="3.2" class="fg-ah"/>' % (x + 16, y - 4.5))
            out.append(tspans(lines, x + 28, y, 13.5, "fg-s2", "start"))
            y += len(lines) * 13.5 * LH + 8
        hmax = max(hmax, y)
    for k in range(2):
        x = 10 + k * (cw + 20)
        out.insert(0, '<rect x="%.1f" y="52" width="%.1f" height="%.1f" rx="10" class="fg-pane"/>' % (x, cw, hmax - 52))
    y = hmax + 6
    if sp.get("note"):
        lines = wrap(sp["note"], 13, W - 60)
        out.append(tspans(lines, W / 2, y + 16, 13, "fg-lab"))
        y += 16 + len(lines) * 13 * LH
    return "".join(out), y + 4


def ring(nodes, center=None, is_cycle=False):
    n = len(nodes)
    bw = 170 if n <= 4 else 150
    dims = [card(0, 0, bw, nd) for nd in nodes]
    bh = max(d[0] for d in dims)
    rx, ry = (W - bw) / 2 - 12, 118 if n > 4 else 104
    cx, cy = W / 2, ry + bh / 2 + 8
    pos = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n
        pos.append((cx + rx * math.cos(a) * (0.92 if n > 4 else 0.86), cy + ry * math.sin(a)))
    out = []
    if center:
        ch, ctl, csl = card(0, 0, 190, center)
        for px, py in pos:
            out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" class="fg-ln"/>' % (cx, cy, px, py))
        out.append(draw_card(cx - 95, cy - ch / 2, 190, ch, ctl, csl, True))
    if is_cycle:
        for i in range(n):
            (x1, y1), (x2, y2) = pos[i], pos[(i + 1) % n]
            dx, dy = x2 - x1, y2 - y1
            dist = math.hypot(dx, dy)
            # 상자 가장자리에서 시작하고 끝나게 줄인다
            sx = min(abs((bw / 2 + 6) / dx) if dx else 9e9, abs((bh / 2 + 6) / dy) if dy else 9e9)
            ux, uy = dx * sx, dy * sx
            if dist > 2 * math.hypot(ux, uy) + 10:
                out.append(arrow(x1 + ux, y1 + uy, x2 - ux, y2 - uy))
    for (px, py), nd, (_, tl, sl) in zip(pos, nodes, dims):
        out.append(draw_card(px - bw / 2, py - bh / 2, bw, bh, tl, sl))
    top = min(py for _, py in pos) - bh / 2
    shift = 6 - top
    body = "".join(out)
    return '<g transform="translate(0 %.1f)">%s</g>' % (shift, body), max(py for _, py in pos) + bh / 2 + shift + 8


def hub(sp):
    return ring(sp["around"], center=sp["center"])


def cycle(sp):
    return ring(sp["nodes"], center=sp.get("center"), is_cycle=True)


def grid(sp):
    cols, rows = sp["cols"], sp["rows"]
    nc = len(cols)
    first = 150
    cw = (W - 20 - first) / (nc - 1)
    widths = [first] + [cw] * (nc - 1)
    out, y = [], 6
    for r, row in enumerate([cols] + rows):
        cells = [wrap(c, 13.5 if r else 13.5, w - 16) for c, w in zip(row, widths)]
        h = max(max(len(c) for c in cells) * 13.5 * LH + 14, 38)
        x = 10
        for c, (lines, w) in enumerate(zip(cells, widths)):
            cls = "fg-hl" if r == 0 and c else ("fg-box" if c == 0 or r == 0 else "fg-cell")
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" class="%s"/>' % (x, y, w, h, cls))
            ty = y + (h - len(lines) * 13.5 * LH) / 2 + 13.5 * 0.95
            out.append(tspans(lines, x + w / 2, ty, 13.5, "fg-t" if (r == 0 or c == 0) else "fg-s2"))
            x += w
        y += h
    return "".join(out), y + 6


KINDS = {"flow": flow, "stack": stack, "compare": compare, "hub": hub, "cycle": cycle, "grid": grid}


def svg(sp):
    body, h = KINDS[sp["type"]](sp)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-label="%s">%s</svg>'
            % (W, math.ceil(h), html.escape(sp.get("caption", ""), quote=True), body))


def load(src):
    specs = []
    for path in sorted(glob.glob(os.path.join(src, "figures", "*.json"))):
        with open(path, encoding="utf-8") as f:
            specs += json.load(f)
    return specs


STEP_HEAD = re.compile(r"^## (\d+)단계 · ")


def place(texts, specs):
    """[(이름, 원고)] 에 그림을 끼운다. 번호는 읽는 순서대로 매긴다. 끼운 원고 목록과 [(번호, 설계안)] 을 돌려준다."""
    want = {}
    for sp in specs:
        want.setdefault((sp["step"], sp["before"]), []).append(sp)
    placed, out_texts, no = [], [], 0
    for name, text in texts:
        step = 0 if name == "front" else None
        lines, fence = [], False
        for line in text.splitlines():
            if line.lstrip().startswith("```"):
                fence = not fence
            m = None if fence else STEP_HEAD.match(line)
            if m:
                step = int(m.group(1))
            elif not fence and line.startswith("## ") and name != "front":
                step = None
            for sp in want.pop((step, line.strip()), []) if step is not None and not fence else []:
                no += 1
                placed.append((no, sp))
                lines += ["", '<figure class="fig" id="fig-%s">%s<figcaption>그림 %d · %s</figcaption></figure>'
                          % (sp["id"], svg(sp), no, html.escape(sp["caption"])), ""]
            lines.append(line)
        out_texts.append("\n".join(lines) + "\n")
    missing = [sp["id"] for v in want.values() for sp in v]
    return out_texts, placed, missing


LIGHT_CSS = """
.fig{margin:1.4em 0;text-align:center;break-inside:avoid}
.fig svg{width:100%;max-width:680px;height:auto;font-family:inherit}
.fig figcaption{margin-top:.4em;font-size:.86em;color:#5b6478}
.fg-box{fill:#f6f3ec;stroke:#d8cfb8}.fg-hl{fill:#fbefd0;stroke:#b8871c}.fg-pane{fill:#fbfaf6;stroke:#e6e0d2}
.fg-cell{fill:#fff;stroke:#d9dde6}.fg-t{fill:#15223d;font-weight:700}.fg-s{fill:#5b6478}.fg-s2{fill:#1b2233}
.fg-n{fill:#b8871c;font-weight:800}.fg-ar,.fg-ln{stroke:#b8871c;stroke-width:1.6}.fg-ln{stroke:#d8cfb8;stroke-dasharray:4 4}
.fg-ah{fill:#b8871c}.fg-lab{fill:#8a6a1a;font-weight:600}
"""

DARK_CSS = """
.bk-body .fig{margin:26px 0;text-align:center}
.bk-body .fig svg{width:100%;max-width:720px;height:auto;font-family:inherit}
.bk-body .fig figcaption{margin-top:8px;font-size:13.5px;color:var(--faint)}
.fg-box{fill:#141b30;stroke:rgba(255,255,255,.16)}.fg-hl{fill:rgba(212,168,67,.14);stroke:#d4a843}.fg-pane{fill:rgba(20,27,48,.45);stroke:rgba(255,255,255,.08)}
.fg-cell{fill:rgba(20,27,48,.35);stroke:rgba(255,255,255,.12)}.fg-t{fill:#eef1f9;font-weight:700}.fg-s{fill:#9aa4bd}.fg-s2{fill:#dfe4f1}
.fg-n{fill:#e9c96a;font-weight:800}.fg-ar{stroke:#d4a843;stroke-width:1.6}.fg-ln{stroke:rgba(255,255,255,.22);stroke-width:1.4;stroke-dasharray:4 4}
.fg-ah{fill:#d4a843}.fg-lab{fill:#e9c96a;font-weight:600}
"""
