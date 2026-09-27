# aicoding

**AI코딩 완전정복 — AI에게 일을 맡기는 법을 따라 하며 익히는 한국어 실전 매뉴얼**

여기서 코딩은 AI에게 말로 일을 설계해 맡기는 일입니다.

CEO비즈니스스쿨 김문수 교수가 경영진·실무 리더·연구자·공공기관 담당자를 가르치며 다듬어 온 강의를
누구나 읽고 따라 할 수 있도록 공개합니다. 지금 공개한 책은 Claude와 ChatGPT·Codex를 함께 다루는
『클로드·GPT 완전정복 100단계』입니다. 원고와 실습 파일, 양식, 강사용 안내, 퀴즈와 미션을 모두 이 저장소에 둡니다.

> *A hands-on Korean playbook for delegating real work to AI — Claude and ChatGPT side by side, from chat to
> Claude Code and Codex, browser and computer use, skills, connectors, automation and AX. With practice files,
> templates, instructor guides, quizzes and missions.*

## 무엇이 들어 있나

| 폴더 | 내용 | 상태 |
|---|---|---|
| [`claude-gpt/`](claude-gpt/) | 『클로드·GPT 완전정복 100단계』 — Claude와 ChatGPT 채팅에서 Claude Code·Codex, 브라우저와 컴퓨터 맡기기, 스킬·연결자·자동화, 부서별 AX까지(5편 11부 100단계) | 공개 |
| [`claude-gpt/quiz/`](claude-gpt/quiz/) · [`claude-gpt/missions/`](claude-gpt/missions/) | 부마다 이해를 확인하는 퀴즈, 샘플 자료로 결과물을 만들어 보는 미션 | 차례로 올림 |
| [`common/`](common/) | 도구와 상관없이 통하는 원칙과 도구 비교, ChatGPT·Codex 사실 확인 기록(`gpt_사실확인.md`) | 준비 중 |
| `agent/` | AI 에이전트 완전정복 — 에이전트의 구조와 설계, 평가와 운영을 깊이 있게 | 준비 중 |

예전 `claude/` 폴더는 `claude-gpt/`로 옮겼고, Codex 내용은 책의 제4부(31~39단계)로 합쳤습니다.

## 바로 쓰기

- **웹으로 읽기(단계별): <https://ceoai.kr/aicoding/claude-gpt/>** · PDF도 이곳에서
- 책 원고: [`claude-gpt/book/`](claude-gpt/book/) — 머리말부터 부록까지 마크다운으로 읽을 수 있습니다.
- 복사해 쓰는 프롬프트 146개: [`claude-gpt/prompts.md`](claude-gpt/prompts.md)
- 공식 문서·도움말 링크 모음: [`claude-gpt/links.md`](claude-gpt/links.md)
- 인기 스킬과 스킬 모음: [`claude-gpt/skills.md`](claude-gpt/skills.md)
- 함께 읽을 칼럼(CEO경제신문): [`claude-gpt/columns.md`](claude-gpt/columns.md)
- 강의 커리큘럼(11회차 편성): [`claude-gpt/curriculum.md`](claude-gpt/curriculum.md)
- 실습 파일(가상 회사 자료): [`claude-gpt/samples/`](claude-gpt/samples/) · 빈칸 양식: [`claude-gpt/templates/`](claude-gpt/templates/)
- 강사용 안내(부별 수업 시간표·시연·채점 기준·슬라이드 뼈대): [`claude-gpt/instructor/`](claude-gpt/instructor/)
- 퀴즈: [`claude-gpt/quiz/`](claude-gpt/quiz/) · 미션: [`claude-gpt/missions/`](claude-gpt/missions/)
- 변경 기록(날짜 판 번호): [`CHANGELOG.md`](CHANGELOG.md)

## 전자책(PDF) 만들기

```bash
pip install markdown playwright pymupdf
python3 claude-gpt/tools/make_ebook.py
# → claude-gpt/dist/ebook/ 에 HTML·PDF가 만들어집니다

python3 claude-gpt/tools/make_extras.py
# → 원고에서 prompts.md·links.md·skills.md·columns.md·curriculum.md를 다시 뽑습니다
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

AI 에이전트편도 이 일곱 단계에 맞춰 씁니다.

## 저자

**김문수** — CEO비즈니스스쿨 설립총장, CEO경제신문 발행인  
강의·칼럼: <https://ceoai.kr> · 칼럼 모음 <https://ceoai.kr/leadership2/reads/>

## 알려 두기

- 이 자료는 저자의 독립적인 실습서입니다. Claude는 Anthropic의, ChatGPT·Codex·GPT는 OpenAI의 상표입니다.
- 기능과 화면은 자주 바뀝니다. 책과 화면이 다르면 각 도구의 공식 문서가 기준입니다.
- 고칠 곳이나 더할 사례, 퀴즈와 미션에 대한 의견은 Issue로 알려 주세요.
