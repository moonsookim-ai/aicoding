# 클로드·GPT 완전정복 100단계

**채팅에서 Claude Code·Codex까지, 일을 맡기는 법을 따라 하며 익히는 실전 매뉴얼**  
CEO비즈니스스쿨 김문수 교수

웹으로 읽기: <https://ceoai.kr/aicoding/claude-gpt/> · PDF도 이곳에서

| 편 | 부 | 단계 | 원고 |
|---|---|---|---|
| 제1편 기초 다지기 | 1 첫 대화와 제대로 묻는 법 | 1~13 | [part01.md](book/part01.md) |
| | 2 결과물로 받아 내기 | 14~19 | [part02.md](book/part02.md) |
| 제2편 Claude Code와 Codex | 3 Claude Code로 직접 만들기 | 20~30 | [part03.md](book/part03.md) |
| | 4 Codex로 직접 만들기 | 31~39 | [part04.md](book/part04.md) |
| 제3편 브라우저와 컴퓨터 | 5 브라우저와 컴퓨터를 맡기다 | 40~46 | [part05.md](book/part05.md) |
| 제4편 나만의 업무 시스템 | 6 반복 업무를 스킬로 만들기 | 47~55 | [part06.md](book/part06.md) |
| | 7 일을 통째로 맡기기 | 56~63 | [part07.md](book/part07.md) |
| | 8 회사 도구와 연결하기 | 64~71 | [part08.md](book/part08.md) |
| 제5편 자동화와 조직 확산 | 9 알아서 돌아가게 만들기 | 72~80 | [part09.md](book/part09.md) |
| | 10 부서별 AX: 일의 흐름을 다시 짜기 | 81~90 | [part10.md](book/part10.md) |
| | 11 조직에 뿌리내리기 | 91~100 | [part11.md](book/part11.md) |

- [머리말](book/front.md) · [부록](book/appendix.md)
- [복사해 쓰는 프롬프트](prompts.md) · [링크 모음](links.md) · [스킬 모음](skills.md) · [칼럼](columns.md) · [커리큘럼](curriculum.md)
- [실습 파일](samples/) · [양식](templates/) · [강사용 안내](instructor/)
- [퀴즈](quiz/) · [미션](missions/)

단계마다 같은 짜임입니다: 핵심 한 문장 → 이 단계를 마치면 → 본문 → 현장 장면 → 따라 하기(성공 기준) →
복사해 쓰는 프롬프트 → 막히면 이렇게 → 스스로 점검 → 기억할 것 → 더 알아보기.
도구가 갈리는 단계에는 「ChatGPT·Codex에서는」 상자가 있어 같은 일을 ChatGPT와 Codex로도 따라 할 수 있습니다.

## 원고와 곁 파일

| 파일 | 무엇 |
|---|---|
| `book/front.md`, `book/part01.md`~`part11.md`, `book/appendix.md` | 원고 |
| `book/checks/partNN.md` | 단계별 난이도·선택 단계 표시와 「스스로 점검」 해설 |
| `book/practice.json` | 단계마다 쓰는 실습 파일과 양식 |
| `book/checked.json` | 화면이 자주 바뀌는 단계의 마지막 화면 확인일 |
| `book/figures/` | 개념 그림 설명(그림은 `tools/figures.py`가 그립니다) |
| `book/VERSION` | 판 번호(날짜) |

`prompts.md`, `links.md`, `skills.md`, `columns.md`, `curriculum.md`는 `tools/make_extras.py`가 원고에서 뽑습니다.
원고를 고친 뒤 다시 돌리고, 손으로 고치지 않습니다.
