"""원고(book/)에서 곁 문서를 다시 뽑는다: 프롬프트 모음, 링크 모음, 스킬 모음, 칼럼 모음, 커리큘럼.

원고를 고친 뒤 한 번 돌리면 곁 문서가 원고와 같아진다. 손으로 고치지 않는다.

  python3 claude-gpt/tools/make_extras.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import make_ebook as eb  # noqa: E402

ROOT = os.path.dirname(HERE)
parts = [eb.read("part%02d.md" % i) for i in range(1, eb.PARTS + 1)]
appendix = eb.read("appendix.md")
ol = eb.outline(parts)
head = "<!-- tools/make_extras.py 가 원고(book/)에서 뽑은 파일입니다. 손으로 고치지 않습니다. -->\n\n"


def section(title):
    m = re.search(r"(?ms)^## %s\s*\n(.*?)(?=^## |\Z)" % re.escape(title), appendix)
    return m.group(1).strip() if m else ""


def write(name, title, body):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(head + "# %s\n\n『%s』 v%s 기준\n\n%s\n" % (title, eb.TITLE, eb.VERSION, body.strip()))


prompts = eb.collect_prompts(parts)
write("prompts.md", "복사해 쓰는 프롬프트 %d개" % len(prompts), eb.prompts_md(prompts).split("\n", 1)[1])
write("links.md", "주요 소스와 링크", section("주요 소스와 링크"))
write("skills.md", "인기 스킬과 스킬 모음", section("인기 스킬과 스킬 모음"))
write("columns.md", "함께 읽을 칼럼", section("함께 읽을 칼럼"))

# 커리큘럼: 부마다 단계와 걸리는 시간(읽기+따라 하기)을 모은다
rows, total = [], 0
for (pno, ptitle, lessons), text in zip(ol, parts):
    mins = {}
    cur = None
    for line in text.splitlines():
        m = eb.LESSON_RE.match(line)
        if m:
            cur = int(m.group(1))
        if cur and line.startswith("**걸리는 시간**"):
            mins[cur] = sum(int(n) * (60 if u == "시간" else 1) for n, u in re.findall(r"약 (\d+)(시간|분)", line))
    part_total = sum(mins.values())
    total += part_total
    rows.append("## %s · 제%d부 %s (%d~%d단계, 약 %d시간 %d분)\n\n| 단계 | 제목 | 시간(분) |\n|---|---|---|\n%s\n"
                % (eb.pyeon_title(pno), pno, ptitle, lessons[0][0], lessons[-1][0], part_total // 60, part_total % 60,
                   "\n".join("| %d | %s | %d |" % (n, t, mins.get(n, 0)) for n, t in lessons)))
intro = ("한 부를 한 회차로 잡으면 열한 회차 과정이 됩니다. 시간은 단계마다 적은 「걸리는 시간」(읽기와 따라 하기)을 "
         "더한 값이고, 도입·정리와 발표 시간은 강사용 안내(`instructor/`)의 시간표를 따릅니다. 전체 약 %d시간입니다.\n\n"
         % round(total / 60))
write("curriculum.md", "커리큘럼(부별 단계와 시간)", intro + "\n".join(rows))
print("prompts %d · parts %d · total %d min" % (len(prompts), len(ol), total))
