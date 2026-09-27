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
.toc ul{list-style:none;padding-left:1em;margin:.2em 0 1em}
.toc a{text-decoration:none}
"""

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


def build():
    front = read("front.md")
    parts = [read("part%02d.md" % i) for i in range(1, 11)]
    appendix = read("appendix.md")
    ol = outline(parts)
    missing = [n for n in range(1, 101) if n not in {l for _, _, ls in ol for l, _ in ls}]
    if missing:
        sys.exit("원고에 빠진 단계가 있다: %s" % missing)
    prompts = collect_prompts(parts)
    appendix_full = appendix.replace("# 부록", "# 부록 {#appendix}", 1) + "\n" + prompts_md(prompts)

    os.makedirs(OUT, exist_ok=True)
    today = VERSION[:10].replace(".", "-")

    # ── 한 장짜리 HTML (PDF 원본 겸 웹 열람용)
    cover = ('<section class="cover"><div class="t">%s</div><div class="s">%s</div>'
             '<div class="a">%s</div><div class="v">v%s · %s 기준</div></section>') % (TITLE, SUBTITLE, AUTHOR, VERSION, VERSION_DATE)
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
  await p.pdf({path: process.argv[2], preferCSSPageSize: true, printBackground: true,
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
    with open(pdf_src, "w", encoding="utf-8") as f:
        f.write(page.replace("<style>", "<style>" + "".join(faces), 1))
    if node:
        env = dict(os.environ)
        env.setdefault("NODE_PATH", subprocess.run([node, "-e", "process.stdout.write(require('path').join(process.execPath,'..','..','lib','node_modules'))"],
                                                   capture_output=True, text=True).stdout)
        r = subprocess.run([node, "-e", script, pdf_src, pdf_path], env=env, capture_output=True, text=True)
        if r.returncode == 0:
            made.append(pdf_path)
        else:
            print("PDF를 건너뛴다:", r.stderr.strip()[:300])
    print("단계 %d개 · 프롬프트 %d개" % (sum(len(ls) for _, _, ls in ol), len(prompts)))
    for p in made:
        print(" ", os.path.relpath(p, ROOT), "%.0f KB" % (os.path.getsize(p) / 1024))


if __name__ == "__main__":
    build()
