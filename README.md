# aicoding

**클로드 코드, Codex 등 AI 코딩의 모든 것**

여기서 코딩은 AI에게 말로 일을 설계해 맡기는 일입니다.

AI 코딩 에이전트에게 일을 맡기는 법을 따라 하며 익히는 한국어 실전 매뉴얼입니다.

CEO비즈니스스쿨 김문수 교수가 경영진·실무 리더·연구자·공공기관 담당자를 가르치며 다듬어 온 강의를
누구나 읽고 따라 할 수 있도록 공개합니다. 첫 권은 Claude입니다. 이어서 Codex 등 다른 AI 코딩
에이전트를 같은 틀로 더해 갑니다.

> *A hands-on Korean playbook for delegating real work to AI coding agents — starting with Claude
> (chat → Claude Code → Claude in Chrome → skills, connectors, automation, AX), with Codex and
> others to follow.*

## 무엇이 들어 있나

| 폴더 | 내용 | 상태 |
|---|---|---|
| [`claude/`](claude/) | 『클로드 완전정복 100단계』 — 채팅에서 Claude Code, Claude in Chrome, 스킬·연결자·자동화, 부서별 AX까지 | 공개 |
| [`codex/`](codex/) | Codex 완전정복 — Codex로 일을 맡기는 법 | 준비 중 |
| `agent/` | AI 에이전트 완전정복 — 에이전트의 구조와 설계, 평가·운영을 깊이 있게 | 준비 중 |
| [`common/`](common/) | 도구와 상관없이 통하는 원칙 · 도구 비교 | 준비 중 |

## 바로 쓰기

- **웹으로 읽기(단계별): <https://ceoai.kr/aicoding/claude/>** · PDF·EPUB 내려받기도 이곳에서

- 책 원고: [`claude/book/`](claude/book/) — 머리말부터 부록까지 마크다운으로 읽을 수 있습니다.
- 복사해 쓰는 프롬프트 128개: [`claude/prompts.md`](claude/prompts.md)
- 공식 문서·도움말 링크 모음: [`claude/links.md`](claude/links.md)
- 인기 스킬과 스킬 모음: [`claude/skills.md`](claude/skills.md)
- 함께 읽을 칼럼(CEO경제신문): [`claude/columns.md`](claude/columns.md)
- 강의 커리큘럼(10회차 편성): [`claude/curriculum.md`](claude/curriculum.md)
- 실습 파일(가상 회사 자료): [`claude/samples/`](claude/samples/) · 빈칸 템플릿: [`claude/templates/`](claude/templates/)
- 강사용 안내(부별 수업 시간표·시연·채점 기준·슬라이드 뼈대): [`claude/instructor/`](claude/instructor/)
- 변경 기록(날짜 판 번호): [`CHANGELOG.md`](CHANGELOG.md)

## 전자책(PDF·EPUB) 만들기

```bash
pip install markdown playwright pymupdf
python3 claude/tools/make_ebook.py
# → claude/dist/ebook/ 에 HTML·EPUB·PDF가 만들어집니다
```

## 같은 틀로 넓혀 가기

도구마다 부르는 이름은 달라도 일을 맡기는 순서는 같습니다.

1. 제대로 묻는다 (프롬프트)
2. 결과물로 받는다 (문서·표·화면·코드)
3. 반복되는 설명을 파일로 남긴다 (CLAUDE.md, AGENTS.md, 스킬)
4. 회사 도구와 잇는다 (연결자, MCP)
5. 정해진 때에 알아서 돌게 한다 (자동화)
6. 평가하고, 고친 흔적으로 나아지게 한다 (평가 세트, 개선 루프)
7. 부서의 일하는 방식을 다시 짠다 (AX)

새 도구를 더할 때도 이 일곱 단계에 맞춰 씁니다.

## 저자

**김문수** — CEO비즈니스스쿨 설립총장, CEO경제신문 발행인  
강의·칼럼: <https://ceoai.kr> · 칼럼 모음 <https://ceoai.kr/leadership2/reads/>

## 알려 두기

- 이 자료는 저자의 독립적인 실습서입니다. Claude는 Anthropic의, Codex는 OpenAI의 상표입니다.
- 기능과 화면은 자주 바뀝니다. 책과 화면이 다르면 각 도구의 공식 문서가 기준입니다.
- 고칠 곳이나 더할 사례는 Issue로 알려 주세요.
