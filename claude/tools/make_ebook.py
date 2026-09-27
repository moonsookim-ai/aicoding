"""『클로드 완전정복 100단계』 전자책을 원고(docs/ebook/*.md)에서 EPUB·PDF·HTML로 만든다.

원고는 docs/ebook/ 한 곳에만 있다. 머리말(front.md) → 제1~10부(part01~10.md) → 부록
(appendix.md) 순서로 엮고, 차례와 「프롬프트 모음」은 원고에서 뽑아 만든다 — 손으로 적어
두지 않으므로 단계를 고치면 차례와 모음이 따라 바뀐다.

실행:
  pip install markdown
  python3 tools/make_ebook.py [출력폴더]      # 기본값 dist/ebook (저장소에 두지 않는다)

PDF는 전역 Playwright(크로미움)로 찍는다. 글꼴은 Pretendard를 CDN에서 curl로 받아 로컬 파일로
물린다(크로미움이 프록시 인증서를 믿지 않아 CDN을 직접 못 부르는 환경이 있다). 받지 못하면 시스템
글꼴로 찍고 경고한다. node가 없으면 PDF만 건너뛰고 EPUB·HTML은 만든다.
"""
import datetime
import html
import os
import re
import shutil
import subprocess
import sys
import uuid
import zipfile

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "book")
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "dist", "ebook"))

TITLE = "클로드 완전정복 100단계"
SUBTITLE = "채팅에서 Claude Code까지, 일을 맡기는 법을 따라 하며 익히는 실전 매뉴얼"
AUTHOR = "CEO비즈니스스쿨 김문수 교수"
SITES = ["ceobizschool.kr", "ceoai.kr"]
BASENAME = "claude-100-steps"


def _version():
    """판 표기는 날짜로 한다(YYYY.MM.DD). 같은 날 두 번째 판은 YYYY.MM.DD.2처럼 붙인다."""
    try:
        with open(os.path.join(SRC, "VERSION"), encoding="utf-8") as f:
            v = f.read().strip()
    except OSError:
        v = ""
    return v or datetime.date.today().strftime("%Y.%m.%d")


VERSION = _version()
VERSION_DATE = "%s년 %d월 %d일" % (VERSION[0:4], int(VERSION[5:7]), int(VERSION[8:10]))
PRETENDARD = "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/packages/pretendard/dist/web/static/woff2/Pretendard-%s.woff2"

PART_RE = re.compile(r"^# 제(\d+)부 · (.+)$")
LESSON_RE = re.compile(r"^## (\d+)단계 · (.+)$")

# 열 부를 다섯 편으로 묶는다. (편 제목, 첫 부, 끝 부)
PYEON = [("제1편 · 기초 다지기", 1, 2), ("제2편 · Claude Code", 3, 3), ("제3편 · Claude in Chrome", 4, 4),
         ("제4편 · 나만의 업무 시스템", 5, 7), ("제5편 · 자동화와 조직 확산", 8, 10)]


def pyeon_of(pno):
    for t, a, _ in PYEON:
        if pno == a:
            return t
    return None


def read(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read().strip() + "\n"


def tag_headings(text):
    """부·단계 제목에 고정 id를 단다(한글 제목은 자동 id가 불안정하다)."""
    lines = []
    for line in text.splitlines():
        m = PART_RE.match(line)
        if m:
            line += " {#p%s}" % m.group(1)
        m = LESSON_RE.match(line)
        if m:
            line += " {#l%s}" % m.group(1)
        lines.append(line)
    return "\n".join(lines) + "\n"


# ── 단계에 덧붙이는 것: 난이도·선택 표시, 화면 확인일, 실습 파일, 스스로 점검 해설 ─────────────
# 원고(partNN.md)는 그대로 두고, 곁 파일에서 읽어 PDF·EPUB·웹이 같은 규칙으로 끼워 넣는다.
#   docs/ebook/checks/partNN.md   단계별 난이도(1~3)·선택 여부·점검 해설
#   docs/ebook/practice.json      단계별 실습 파일(GitHub 공개 저장소의 샘플 자료와 양식)
#   docs/ebook/checked.json       화면이 자주 바뀌는 단계를 마지막으로 확인한 날
STARS = {1: "★☆☆ 기본", 2: "★★☆ 실무", 3: "★★★ 심화"}


def with_figures(front, parts):
    """개념 그림(docs/ebook/figures/*.json)을 머리말과 부 원고에 끼운다. 번호는 읽는 순서대로."""
    import figures
    texts, placed, missing = figures.place([("front", front)] + [("part", p) for p in parts], figures.load(SRC))
    if missing:
        sys.exit("그림을 끼울 제목을 찾지 못했다: %s" % missing)
    return texts[0], texts[1:]


def load_extras():
    import json
    info = {}
    cdir = os.path.join(SRC, "checks")
    for name in sorted(os.listdir(cdir)) if os.path.isdir(cdir) else []:
        with open(os.path.join(cdir, name), encoding="utf-8") as f:
            for block in re.split(r"(?m)^## (?=\d+\s*$)", f.read())[1:]:
                head, _, rest = block.partition("\n")
                n = int(head)
                lv = re.search(r"(?m)^난이도:\s*(\d)", rest)
                op = re.search(r"(?m)^선택:\s*(\S+)", rest)
                answers = [a.strip() for a in re.findall(r"(?m)^\d+\.\s+(.+)$", rest)]
                info[n] = {"level": int(lv.group(1)) if lv else None, "optional": bool(op and op.group(1) == "예"),
                           "answers": answers}
    for fname, key in (("practice.json", "files"), ("checked.json", "checked")):
        path = os.path.join(SRC, fname)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                for k, v in json.load(f).items():
                    info.setdefault(int(k), {})[key] = v
    return info


def enrich(text, extras, mode):
    """부 원고에 단계별 덧붙임을 끼운다. mode="pdf"면 해설을 부록으로 보내는 고리를, "web"이면 펼쳐 보는 해설을 단다."""
    out, cur, in_check = [], None, False
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = LESSON_RE.match(line)
        if m:
            cur = extras.get(int(m.group(1)), {})
            cur_no = int(m.group(1))
        if cur is not None and line.startswith("**걸리는 시간**"):
            tags = []
            if cur.get("level"):
                tags.append("난이도 " + STARS[cur["level"]])
            if cur.get("optional"):
                tags.append("처음엔 건너뛰어도 되는 단계")
            if cur.get("checked"):
                tags.append("화면 확인 " + cur["checked"])
            line += "".join(" · " + t for t in tags)
        if cur is not None and line.strip() == "### 스스로 점검":
            files = cur.get("files") or []
            if files:
                out += ["### 실습 파일", "",
                        "공개 저장소에 올려 둔 가공 자료와 양식이다. 회사 자료 대신 먼저 이것으로 해 본다.", ""]
                out += ["- %s [%s](%s) · %s" % (f["kind"], f["name"], f["url"], f["desc"]) for f in files]
                out.append("")
            in_check = True
        out.append(line)
        if in_check and line.startswith("- ") and not (i + 1 < len(lines) and lines[i + 1].startswith("- ")):
            in_check = False
            answers = cur.get("answers") or []
            if answers and mode == "web":
                out += ["", '<details class="bk-check" markdown="1"><summary>점검 해설 보기</summary>', ""]
                out += ["%d. %s" % (k + 1, a) for k, a in enumerate(answers)]
                out += ["", "</details>"]
            elif answers:
                out += ["", "해설은 부록 [「스스로 점검 해설」](#c%d)에 있다." % cur_no]
    return "\n".join(out) + "\n"


def checks_md(ol, extras):
    out = ["## 스스로 점검 해설", "",
           "단계마다 끝에 둔 「스스로 점검」 세 문항을 어떻게 판단하면 되는지 적었다. 통과로 볼 수 있는 모습과, "
           "아직이라면 다시 볼 곳을 함께 적었다.", ""]
    for pno, ptitle, lessons in ol:
        out += ["### 제%d부 · %s" % (pno, ptitle), ""]
        for lno, ltitle in lessons:
            ans = extras.get(lno, {}).get("answers") or []
            if not ans:
                continue
            out += ["**[%d단계 · %s](#l%d)**" % (lno, ltitle, lno), "{: #c%d }" % lno, ""]
            out += ["%d. %s" % (k + 1, a) for k, a in enumerate(ans)]
            out.append("")
    return "\n".join(out) + "\n"


# ── 부별 한 장 요약: 단계마다 핵심 한 문장과 난이도, 이 부의 과제를 한 쪽에 모은다 ────────────
SITE_BOOK = "https://ceoai.kr/aicoding/claude"


def part_facts(text):
    cores, cur = {}, None
    for line in text.splitlines():
        m = LESSON_RE.match(line)
        if m:
            cur = int(m.group(1))
            continue
        if cur and cur not in cores and line.startswith("> "):
            cores[cur] = line[2:].strip()
    task = text.split("### 이 부의 과제", 1)[1] if "### 이 부의 과제" in text else ""
    task = re.split(r"(?m)^#{1,3} ", task, 1)[0]
    # 부마다 적는 꼴이 조금씩 다르다: **과제 이름.** / **과제명**: / **과제: 이름** / 이름 없이 설명만
    name = (re.search(r"\*\*과제(?: 이름|명)?[.:：]?\*\*[.:：]?\s*(.+)", task)
            or re.search(r"\*\*과제[:：]\s*(.+?)\*\*", task))
    todo = re.search(r"\*\*(?:할 일|하는 일)[.:：]?\*\*[.:：]?\s*(.+)", task)
    if not todo:
        head = re.split(r"\*\*제출물|제출물은", task, 1)[0]  # 과제 설명은 제출물 앞에만 있다
        paras = [x.strip() for x in head.split("\n\n") if x.strip()]
        rest = [x for x in paras if not x.startswith(("**", "|", "-", "1.")) and "\n" not in x]
        todo_text = rest[0] if rest else ""
    else:
        todo_text = todo.group(1).strip()
    crit = []
    m = re.search(r"완료 기준[^\n]*\n+((?:[-|].*\n?)+)", task)
    if m:
        for line in m.group(1).splitlines():
            if line.startswith("- "):
                crit.append(line[2:].strip())
            elif line.startswith("|") and not re.match(r"^\|[\s:|-]+\|$", line):
                cells = [c.strip() for c in line.strip("|").split("|")]
                if len(cells) >= 2 and cells[0] not in ("항목", "번호"):
                    crit.append("%s: %s" % (cells[0], cells[-1]))
    name_text = name.group(1).strip().rstrip("*").strip() if name else ""
    if not name_text:
        name_text = "수료 과제" if "수료 과제" in todo_text else ""
    return {"cores": cores, "task": name_text, "todo": todo_text, "criteria": crit}


def doing_of(appendix):
    """부록 첫 표(편 | 부 | 단계 | 이 부에서 하는 일)에서 부마다 하는 일을 읽는다."""
    res = {}
    for m in re.finditer(r"(?m)^\|[^|]*\| (\d+) [^|]+\| \d+~\d+ \| ([^|]+) \|$", appendix):
        res[int(m.group(1))] = m.group(2).strip()
    return res


def summary_md(pno, ptitle, lessons, facts, extras, doing, web_links=False):
    link = (lambda n: "%s/step-%03d/" % (SITE_BOOK, n)) if web_links else (lambda n: "#l%d" % n)
    out = ["### 제%d부 · %s" % (pno, ptitle), "",
           "%s · %d~%d단계%s" % (pyeon_title(pno), lessons[0][0], lessons[-1][0],
                                 (" · " + doing[pno]) if doing.get(pno) else ""), "",
           "| 단계 | 핵심 한 문장 | 난이도 |", "|---|---|---|"]
    for lno, ltitle in lessons:
        e = extras.get(lno, {})
        lv = STARS.get(e.get("level"), "").split(" ")[0] + (" 선택" if e.get("optional") else "")
        out.append("| [%d · %s](%s) | %s | %s |" % (lno, ltitle.replace("|", "/"), link(lno),
                                                   facts["cores"].get(lno, "").replace("|", "/"), lv.strip()))
    if facts["task"]:
        out += ["", "**이 부의 과제 · %s** %s" % (facts["task"], facts["todo"])]
    if facts["criteria"]:
        out += ["", "**완료 기준**", ""] + ["- " + c for c in facts["criteria"]]
    return "\n".join(out) + "\n"


def pyeon_title(pno):
    return next(t for t, a, b in PYEON if a <= pno <= b)


STEP_REF = re.compile(r"(?<![\d·~])(\d{1,3}(?:[·~]\d{1,3})*)단계")
CELL_REFS = re.compile(r"^\s*\d{1,3}(?:[·~]\d{1,3})*단계(?:\s*,\s*\d{1,3}(?:[·~]\d{1,3})*단계)*\s*$")
KEEP = re.compile(r"(\[[^\]]*\]\([^)]*\)|`[^`]*`)")


def _refs(group):
    """'40·68·77' → [40, 68, 77], '16~21' → [(16, 21)]"""
    if "~" in group:
        a, b = group.split("~")[0], group.split("~")[-1]
        return [(int(a), int(b))]
    out = []
    for n in group.split("·"):
        if int(n) not in out:
            out.append(int(n))
    return out


def link_steps(text, titles, prose=False):
    """「17단계」 같은 단계 언급을 그 단계로 가는 링크로 바꾼다(PDF·EPUB·웹이 같은 규칙을 쓴다).

    표 칸이 단계 언급만으로 되어 있으면 「17단계 · 워드·엑셀 파일로 받기」처럼 제목을 붙여
    줄마다 하나씩 적는다. prose=True면 문장 속 언급도 링크만 건다 — 부록에서만 켠다.
    본문의 문장에는 「2단계와 3단계로 돌아가」처럼 실습 안의 순서 번호가 섞여 있어서다.
    링크는 #l17 꼴이다. 웹은 이것을 단계 쪽 주소로 바꾼다.
    """
    def ok(n):
        return 1 <= n <= 100 and n in titles

    def cell(c):
        items = []
        for g in STEP_REF.findall(c):
            for r in _refs(g):
                if isinstance(r, tuple):
                    a, b = r
                    if not (ok(a) and ok(b)):
                        return None
                    items.append("[%d~%d단계](#l%d)" % (a, b, a))
                else:
                    if not ok(r):
                        return None
                    items.append("[%d단계 · %s](#l%d)" % (r, titles[r].replace("[", "(").replace("]", ")"), r))
        return " " + "<br />".join(items) + " "

    def sentence(seg):
        def one(m):
            if seg[:m.start()].endswith("완전정복 "):
                return m.group(0)
            refs = _refs(m.group(1))
            if isinstance(refs[0], tuple):
                a, b = refs[0]
                return "[%s](#l%d)" % (m.group(0), a) if ok(a) and ok(b) else m.group(0)
            nums = m.group(1).split("·")
            if not all(ok(int(n)) for n in nums):
                return m.group(0)
            parts = ["[%s](#l%s)" % (n, n) for n in nums[:-1]] + ["[%s단계](#l%s)" % (nums[-1], nums[-1])]
            return "·".join(parts)
        return STEP_REF.sub(one, seg)

    def prose_line(line):
        return "".join(x if KEEP.fullmatch(x) else sentence(x) for x in KEEP.split(line))

    out, fence = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
        elif not fence and not line.startswith("#"):
            if line.startswith("|") and not re.match(r"^\|[\s:|-]+\|?\s*$", line):
                cells = line.split("|")
                for i in range(1, len(cells) - 1):
                    if CELL_REFS.match(cells[i]):
                        new = cell(cells[i])
                        if new:
                            cells[i] = new
                    elif prose:
                        cells[i] = prose_line(cells[i])
                line = "|".join(cells)
            elif prose:
                line = prose_line(line)
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def outline(parts):
    """[(부 번호, 부 제목, [(단계 번호, 단계 제목)])]"""
    res = []
    for text in parts:
        pno, ptitle, lessons = None, None, []
        for line in text.splitlines():
            m = PART_RE.match(line)
            if m:
                pno, ptitle = int(m.group(1)), m.group(2).strip()
            m = LESSON_RE.match(line)
            if m:
                lessons.append((int(m.group(1)), m.group(2).strip()))
        res.append((pno, ptitle, lessons))
    return res


def collect_prompts(parts):
    """```text 블록을 그 블록이 들어 있는 단계와 함께 모은다."""
    found = []
    for text in parts:
        cur = None
        in_block, buf = False, []
        for line in text.splitlines():
            m = LESSON_RE.match(line)
            if m and not in_block:
                cur = (int(m.group(1)), m.group(2).strip())
            if line.strip() == "```text" and not in_block:
                in_block, buf = True, []
                continue
            if line.strip() == "```" and in_block:
                in_block = False
                if cur:
                    found.append((cur, "\n".join(buf)))
                continue
            if in_block:
                buf.append(line)
    return found


def prompts_md(prompts):
    out = ["## 프롬프트 모음", "",
           "본문의 「복사해 쓰는 프롬프트」를 단계 순서대로 모았다. 대괄호 `[ ]` 안만 바꿔 넣는다.", ""]
    last = None
    for (no, title), body in prompts:
        if no != last:
            out += ["### %d단계 · %s" % (no, title), ""]
            last = no
        out += ["```text", body, "```", ""]
    return "\n".join(out) + "\n"


def toc_md(ol):
    out = ["# 차례", ""]
    for pno, ptitle, lessons in ol:
        if pyeon_of(pno):
            out += ["## %s" % pyeon_of(pno), ""]
        out.append("**[제%d부 · %s](#p%d)**" % (pno, ptitle, pno))
        out.append("")
        for lno, ltitle in lessons:
            out.append("- [%d단계 · %s](#l%d)" % (lno, ltitle, lno))
        out.append("")
    out.append("**[부록](#appendix)**")
    return "\n".join(out) + "\n"


def md(text, xhtml=False):
    # 체크 목록 "- [ ]"은 글자 그대로 찍히므로 빈 네모로 바꾼다.
    text = re.sub(r"(?m)^(\s*[-*]) \[ \] ", "\\1 ☐ ", text)
    return markdown.markdown(
        text, extensions=["tables", "fenced_code", "attr_list", "sane_lists", "md_in_html"],
        output_format="xhtml" if xhtml else "html")


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figures as _figures  # noqa: E402

CSS = """
:root{--ink:#1b2233;--sub:#5b6478;--line:#d9dde6;--accent:#b8871c;--navy:#15223d;--code:#f5f3ee}
html{font-size:10.5pt}
body{font-family:Pretendard,"Apple SD Gothic Neo","Noto Sans KR","Malgun Gothic",sans-serif;
  color:var(--ink);line-height:1.8;word-break:keep-all;overflow-wrap:break-word;margin:0}
h1{font-size:2em;line-height:1.3;color:var(--navy);margin:0 0 1em;padding-bottom:.4em;border-bottom:3px solid var(--accent)}
h2{font-size:1.4em;line-height:1.4;color:var(--navy);margin:2.2em 0 .6em}
h3{font-size:1.05em;color:var(--accent);margin:1.6em 0 .4em}
p{margin:.6em 0}
blockquote{margin:1em 0;padding:.7em 1em;border-left:4px solid var(--accent);background:#faf6ea;font-weight:600}
blockquote p{margin:0}
.column{margin:1.4em 0;padding:.9em 1.1em;border:1px solid #d8cfb8;border-radius:6px;background:#f6f3ec;font-size:.95em}
.column p{margin:.45em 0}
.column .label{font-weight:700;color:var(--accent)}
.column .src{font-size:.85em;color:#666;text-align:right}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.92em}
th,td{border:1px solid var(--line);padding:.4em .6em;text-align:left;vertical-align:top}
th{background:#eef1f6}
pre{background:var(--code);border:1px solid #e6e0d2;padding:.8em 1em;white-space:pre-wrap;font-size:.9em;line-height:1.6}
code{font-family:"D2Coding","JetBrains Mono",Menlo,monospace;font-size:.92em}
pre code{font-size:1em}
ul,ol{padding-left:1.4em}
li{margin:.2em 0}
a{color:var(--navy)}
hr{border:0;border-top:1px solid var(--line);margin:2em 0}
.cover{text-align:center;padding-top:30%}
.cover .t{font-size:2.6em;font-weight:800;color:var(--navy);line-height:1.25}
.cover .s{margin-top:1em;color:var(--sub);font-size:1.1em}
.cover .a{margin-top:4em;font-weight:700;color:var(--accent)}
.cover .v{margin-top:1.2em;color:var(--sub);font-size:.95em;letter-spacing:.02em}
.cover .w{margin-top:.6em;color:var(--navy);font-size:1em;font-weight:600;letter-spacing:.03em}
.toc ul{list-style:none;padding-left:1em;margin:.2em 0 1em}
.toc a{text-decoration:none}
.toc .pg{float:right;color:var(--sub);font-variant-numeric:tabular-nums;padding-left:.6em}
""" + _figures.LIGHT_CSS

PRINT_CSS = """
@page{size:182mm 257mm;margin:22mm 20mm 24mm}
section{break-before:page}
section.part h2{break-after:avoid}
h2[id^=l]{break-before:page;margin-top:0}
h3,blockquote{break-after:avoid}
pre,blockquote,.column,tr{break-inside:avoid}
td a{overflow-wrap:anywhere}
.cover{height:200mm}
"""


def finish_pdf(pdf_path, printed, render, ol):
    """차례에 쪽번호를 달고, PDF 보기 프로그램 옆에 뜨는 책갈피를 편·부·단계로 정리한다.

    쪽번호는 한 번 찍어 봐야 안다. 찍은 PDF에서 각 단계가 몇 쪽에 떨어졌는지 읽어 차례에 적고
    다시 찍는다. 번호를 적어도 줄바꿈이 달라지지 않게 짜 두었지만, 혹시 밀리면 한 번 더 맞춘다.
    PyMuPDF가 없으면 쪽번호와 책갈피 없이 둔다.
    """
    try:
        import pymupdf
    except ImportError:
        print("PyMuPDF가 없어 차례 쪽번호와 책갈피를 건너뛴다 (pip install pymupdf)")
        return
    toc_re = re.compile(r'(<section class="toc">)(.*?)(</section>)', re.S)

    def pages():
        with pymupdf.open(pdf_path) as d:
            return {k: v["page"] + 1 for k, v in d.resolve_names().items()}

    def numbered(pg):
        def one(m):
            key = m.group(1)
            return m.group(0) + ('<span class="pg">%d</span>' % pg[key] if key in pg else "")
        return toc_re.sub(lambda t: t.group(1) + re.sub(r'<a href="#([a-z]+\d*)">.*?</a>', one, t.group(2)) + t.group(3),
                          printed, count=1)

    pg = pages()
    for _ in range(3):
        if not render(numbered(pg)):
            return
        now = pages()
        if now == pg:
            break
        pg = now
    else:
        print("차례 쪽번호가 끝내 맞지 않았다 - 확인할 것")

    # 책갈피: 크로미움이 제목으로 만든 목록에서 부·단계·부 마무리, 머리말·부록의 절만 남기고 편으로 묶는다.
    d = pymupdf.open(pdf_path)
    raw = d.get_toc(simple=True)
    first = {a: t for t, a, _ in PYEON}
    toc, top = [], None
    for lvl, title, page_no in raw:
        m = PART_RE.match("# " + title)
        if lvl == 1:
            if m and int(m.group(1)) in first:
                toc.append([1, first[int(m.group(1))], page_no])
            top = "part" if m else title
            toc.append([2 if m else 1, title, page_no])
        elif lvl == 2:
            toc.append([3 if top == "part" else 2, title, page_no])
    d.set_toc(toc)
    d.set_metadata({"title": TITLE, "author": AUTHOR, "subject": SUBTITLE, "keywords": "v" + VERSION})
    tmp = pdf_path + ".tmp"
    d.save(tmp, garbage=3, deflate=True)
    d.close()
    os.replace(tmp, pdf_path)
    print("차례 쪽번호 %d곳 · 책갈피 %d개" % (sum(1 for k in pg if k[0] in "lp" or k == "appendix"), len(toc)))


SUMMARY_CSS = """
@page{size:A4;margin:13mm 14mm 12mm}
body{font-family:Pretendard,sans-serif;color:#1b2233;font-size:8.6pt;line-height:1.5;word-break:keep-all;margin:0}
.top{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2.5px solid #b8871c;padding-bottom:5px;margin-bottom:8px}
.top b{font-size:10pt;color:#15223d}.top span{color:#5b6478;font-size:8pt}
h3{font-size:15pt;color:#15223d;margin:2px 0 3px}
p{margin:4px 0}
table{border-collapse:collapse;width:100%;margin:7px 0}
th,td{border:1px solid #d9dde6;padding:3.5px 6px;text-align:left;vertical-align:top}
th{background:#eef1f6;font-size:8pt}
td:first-child{width:34%;font-weight:600}td:last-child{width:9%;white-space:nowrap;color:#b8871c}
a{color:#15223d;text-decoration:none}
ul{margin:3px 0;padding-left:1.2em}li{margin:1px 0}
.foot{margin-top:8px;border-top:1px solid #d9dde6;padding-top:4px;color:#5b6478;font-size:7.6pt;display:flex;justify-content:space-between}
"""


def one_pagers(node, env, faces, ol, facts, extras, doing):
    """부마다 한 장짜리 요약 PDF(dist/ebook/summary/part-NN.pdf). 링크는 웹 쪽 주소로 건다."""
    import json
    sdir = os.path.join(OUT, "summary")
    os.makedirs(sdir, exist_ok=True)
    jobs = []
    for (pno, ptitle, lessons), fx in zip(ol, facts):
        body = md(summary_md(pno, ptitle, lessons, fx, extras, doing, web_links=True))
        page = ('<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>%s%s</style></head><body>'
                '<div class="top"><b>%s · 한 장 요약</b><span>%s · v%s</span></div>%s'
                '<div class="foot"><span>%s/part-%02d/</span><span>ceobizschool.kr · ceoai.kr</span></div></body></html>'
                ) % ("".join(faces), SUMMARY_CSS, TITLE, AUTHOR, VERSION, body, SITE_BOOK, pno)
        src = os.path.join(sdir, ".part-%02d.html" % pno)
        with open(src, "w", encoding="utf-8") as f:
            f.write(page)
        jobs.append([src, os.path.join(sdir, "part-%02d.pdf" % pno)])
    script = r"""
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROME || undefined});
  const p = await b.newPage();
  for (const [src, out] of JSON.parse(process.argv[1])) {
    await p.goto('file://' + src, {waitUntil: 'networkidle'});
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({path: out, preferCSSPageSize: true, printBackground: true});
  }
  await b.close();
})().catch(e => { console.error(e.message); process.exit(1); });
"""
    r = subprocess.run([node, "-e", script, json.dumps(jobs)], env=env, capture_output=True, text=True)
    if r.returncode:
        print("부별 한 장 요약을 건너뛴다:", r.stderr.strip()[:300])
        return
    try:
        import pymupdf
        over = [os.path.basename(out) for _, out in jobs if pymupdf.open(out).page_count > 1]
        if over:
            print("한 장을 넘긴 요약:", over)
    except ImportError:
        pass
    print("부별 한 장 요약 %d개" % len(jobs))


def build():
    front = read("front.md")
    parts = [read("part%02d.md" % i) for i in range(1, 11)]
    appendix = read("appendix.md")
    ol = outline(parts)
    missing = [n for n in range(1, 101) if n not in {l for _, _, ls in ol for l, _ in ls}]
    if missing:
        sys.exit("원고에 빠진 단계가 있다: %s" % missing)
    prompts = collect_prompts(parts)
    titles = {l: t for _, _, ls in ol for l, t in ls}
    extras = load_extras()
    raw_parts = parts
    front, parts = with_figures(front, parts)
    front = link_steps(front, titles)
    parts = [link_steps(enrich(p, extras, "pdf"), titles) for p in parts]
    appendix = link_steps(appendix, titles, prose=True)
    doing = doing_of(appendix)
    facts = [part_facts(p) for p in raw_parts]
    summaries = ["## 부별 한 장 요약", "",
                 "부마다 단계의 핵심 한 문장과 난이도, 이 부의 과제를 한 쪽에 모았다. 복습할 때, 팀에 나눠 줄 때 쓴다. "
                 "웹에서는 부마다 한 장짜리 PDF로도 내려받을 수 있다.", ""]
    for (pno, ptitle, lessons), fx in zip(ol, facts):
        summaries.append(summary_md(pno, ptitle, lessons, fx, extras, doing))
    appendix_full = (appendix.replace("# 부록", "# 부록 {#appendix}", 1) + "\n" + "\n".join(summaries)
                     + "\n" + checks_md(ol, extras) + "\n" + prompts_md(prompts))

    os.makedirs(OUT, exist_ok=True)
    today = VERSION[:10].replace(".", "-")

    # ── 한 장짜리 HTML (PDF 원본 겸 웹 열람용)
    cover = ('<section class="cover"><div class="t">%s</div><div class="s">%s</div>'
             '<div class="a">%s</div><div class="w">%s</div><div class="v">v%s · %s 기준</div></section>') % (TITLE, SUBTITLE, AUTHOR, " · ".join(SITES), VERSION, VERSION_DATE)
    body = [cover,
            '<section>%s</section>' % md(front),
            '<section class="toc">%s</section>' % md(toc_md(ol))]
    body += ['<section class="part">%s</section>' % md(tag_headings(p)) for p in parts]
    body.append('<section>%s</section>' % md(appendix_full))
    page = ('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title>'
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">'
            '<style>%s body{max-width:46em;margin:0 auto;padding:2em 1.2em}'
            '@media print{body{max-width:none;padding:0}%s}</style></head><body>%s</body></html>'
            ) % (TITLE, CSS, PRINT_CSS, "\n".join(body))
    html_path = os.path.join(OUT, BASENAME + ".html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(page)

    # ── EPUB 3
    chapters = [("front", "머리말", front), ("toc", "차례", toc_md(ol))]
    chapters += [("part%02d" % pno, "제%d부 · %s" % (pno, pt), tag_headings(p))
                 for (pno, pt, _), p in zip(ol, parts)]
    chapters.append(("appendix", "부록", appendix_full))
    # 차례·부록의 #p1, #l12 같은 고리를 파일 경계를 넘도록 고친다.
    where = {"p%d" % pno: "part%02d.xhtml" % pno for pno, _, _ in ol}
    where.update({"l%d" % l: "part%02d.xhtml" % pno for pno, _, ls in ol for l, _ in ls})
    where["appendix"] = "appendix.xhtml"
    where.update({"c%d" % l: "appendix.xhtml" for _, _, ls in ol for l, _ in ls})

    def fix_links(x):
        return re.sub(r'href="#([a-z]+\d*)"',
                      lambda m: 'href="%s#%s"' % (where.get(m.group(1), ""), m.group(1)), x)

    def xhtml(title, inner):
        return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
                '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" '
                'lang="ko" xml:lang="ko"><head><meta charset="utf-8"/><title>%s</title>'
                '<link rel="stylesheet" type="text/css" href="style.css"/></head><body>%s</body></html>'
                ) % (html.escape(title), inner)

    book_id = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "ceoai.kr/ebook/" + BASENAME))
    epub_path = os.path.join(OUT, BASENAME + ".epub")
    with zipfile.ZipFile(epub_path, "w") as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
                   '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                   '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>'
                   '</rootfiles></container>', compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css", CSS, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/cover.xhtml", xhtml(TITLE, cover.replace("<section", "<div").replace("</section>", "</div>")),
                   compress_type=zipfile.ZIP_DEFLATED)
        for cid, ctitle, text in chapters:
            z.writestr("OEBPS/%s.xhtml" % cid, xhtml(ctitle, fix_links(md(text, xhtml=True))),
                       compress_type=zipfile.ZIP_DEFLATED)
        nav = ['<nav epub:type="toc" id="toc"><h1>차례</h1><ol>',
               '<li><a href="front.xhtml">머리말</a></li>']
        for pno, pt, ls in ol:
            nav.append('<li><a href="part%02d.xhtml">제%d부 · %s</a><ol>' % (pno, pno, html.escape(pt)))
            nav += ['<li><a href="part%02d.xhtml#l%d">%d단계 · %s</a></li>' % (pno, l, l, html.escape(t))
                    for l, t in ls]
            nav.append('</ol></li>')
        nav.append('<li><a href="appendix.xhtml">부록</a></li></ol></nav>')
        z.writestr("OEBPS/nav.xhtml", xhtml("차례", "".join(nav)), compress_type=zipfile.ZIP_DEFLATED)
        ids = ["cover"] + [c[0] for c in chapters]
        manifest = "".join('<item id="%s" href="%s.xhtml" media-type="application/xhtml+xml"/>' % (i, i) for i in ids)
        spine = "".join('<itemref idref="%s"/>' % i for i in ids)
        z.writestr("OEBPS/content.opf",
                   '<?xml version="1.0" encoding="utf-8"?>'
                   '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bid" xml:lang="ko">'
                   '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
                   '<dc:identifier id="bid">%s</dc:identifier><dc:title>%s</dc:title>'
                   '<dc:creator>%s</dc:creator><dc:language>ko</dc:language>'
                   '<dc:description>v%s (%s 기준)</dc:description>'
                   '<meta property="dcterms:modified">%sT00:00:00Z</meta></metadata>'
                   '<manifest><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>'
                   '<item id="css" href="style.css" media-type="text/css"/>%s</manifest>'
                   '<spine>%s</spine></package>' % (book_id, TITLE, AUTHOR, VERSION, VERSION_DATE, today, manifest, spine),
                   compress_type=zipfile.ZIP_DEFLATED)

    # ── PDF (전역 Playwright로 찍는다. 쪽번호는 바닥글로)
    pdf_path = os.path.join(OUT, BASENAME + ".pdf")
    node = shutil.which("node")
    script = r"""
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROME || undefined});
  const p = await b.newPage();
  await p.goto('file://' + process.argv[1], {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({path: process.argv[2], preferCSSPageSize: true, printBackground: true, outline: true, tagged: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;text-align:center;font-size:8px;color:#888"><span class="pageNumber"></span></div>'});
  await b.close();
})().catch(e => { console.error(e.message); process.exit(1); });
"""
    made = [html_path, epub_path]
    fonts = os.path.join(OUT, ".fonts")
    os.makedirs(fonts, exist_ok=True)
    faces = []
    for weight, name in ((400, "Regular"), (600, "SemiBold"), (700, "Bold"), (800, "ExtraBold")):
        dst = os.path.join(fonts, "Pretendard-%s.woff2" % name)
        if not os.path.exists(dst):
            subprocess.run(["curl", "-sSfL", "-o", dst, PRETENDARD % name], capture_output=True)
        if os.path.exists(dst) and os.path.getsize(dst) > 10000:
            faces.append("@font-face{font-family:Pretendard;font-weight:%d;src:url('file://%s') format('woff2')}"
                         % (weight, dst))
    if len(faces) < 4:
        print("Pretendard를 받지 못했다 - PDF가 시스템 글꼴로 찍힌다")
    pdf_src = os.path.join(OUT, ".print.html")
    if node:
        env = dict(os.environ)
        env.setdefault("NODE_PATH", subprocess.run([node, "-e", "process.stdout.write(require('path').join(process.execPath,'..','..','lib','node_modules'))"],
                                                   capture_output=True, text=True).stdout)
        def render(html_text):
            with open(pdf_src, "w", encoding="utf-8") as f:
                f.write(html_text)
            r = subprocess.run([node, "-e", script, pdf_src, pdf_path], env=env, capture_output=True, text=True)
            if r.returncode:
                print("PDF를 건너뛴다:", r.stderr.strip()[:300])
            return r.returncode == 0

        printed = page.replace("<style>", "<style>" + "".join(faces), 1)
        if render(printed):
            made.append(pdf_path)
            finish_pdf(pdf_path, printed, render, ol)
    if node and faces:
        one_pagers(node, env, faces, ol, facts, extras, doing)
    print("단계 %d개 · 프롬프트 %d개" % (sum(len(ls) for _, _, ls in ol), len(prompts)))
    for p in made:
        print(" ", os.path.relpath(p, ROOT), "%.0f KB" % (os.path.getsize(p) / 1024))


if __name__ == "__main__":
    build()
