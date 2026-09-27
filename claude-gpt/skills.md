<!-- tools/make_extras.py 가 원고(book/)에서 뽑은 파일입니다. 손으로 고치지 않습니다. -->

# 인기 스킬과 스킬 모음

『클로드·GPT 완전정복 100단계』 v2026.09.27.7 기준

스킬을 처음부터 만들기 전에 이미 공개된 스킬을 먼저 살펴봅시다. 잘 만든 스킬의 SKILL.md를 읽어 보는 것만으로도 48단계의 네 마디가 어떻게 쓰이는지 보입니다. 남이 만든 스킬은 설치하기 전에 폴더 안의 파일을 열어 무엇을 하는지 확인합니다. 특히 스크립트가 들어 있으면 IT 담당과 함께 봅니다. ChatGPT와 Codex도 같은 모양의 스킬을 씁니다. ChatGPT에서는 `@`, Codex에서는 `$`로 부르고, 새로 만들 때는 `@skill-creator`(Codex에서는 `$skill-creator`)에게 맡깁니다(51단계).

**설치와 사용 안내**

| 무엇 | 주소 |
|---|---|
| 스킬이란 무엇인가(도움말) | <https://support.claude.com/en/articles/12512176-what-are-skills> |
| Claude 앱에서 스킬 쓰기와 올리기 | <https://support.claude.com/en/articles/12512180-use-skills-in-claude> |
| Claude Code에서 스킬 쓰기 | <https://code.claude.com/docs/en/skills> |
| API에서 스킬 쓰기 | <https://platform.claude.com/docs/en/build-with-claude/skills-guide> |
| 스킬 개념 설명(개발자 문서) | <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview> |
| 스킬을 만든 배경(Anthropic 엔지니어링 글) | <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills> |
| 플러그인 마켓플레이스 | <https://claude.com/marketplace/plugins> |

**Anthropic 공개 스킬 저장소** — <https://github.com/anthropics/skills>

Claude Code에서는 `/plugin marketplace add anthropics/skills`로 이 저장소를 등록한 뒤 필요한 묶음을 설치할 수 있습니다. 유료 요금제의 Claude 앱에는 여기 있는 스킬 상당수가 이미 들어 있습니다.

| 스킬 | 하는 일 | 이 책에서 |
|---|---|---|
| `docx` | 워드 문서 만들기·고치기 | 15단계 |
| `xlsx` | 엑셀 만들기·정리·수식 | 15단계 |
| `pptx` | 파워포인트 장표 만들기 | 16단계 |
| `pdf` | PDF 읽기·합치기·나누기·양식 채우기 | 12단계 |
| `skill-creator` | 스킬을 만들고 시험하고 다듬기 | 47~54단계 |
| `doc-coauthoring` | 제안서·기획서를 단계별로 함께 쓰기 | 15단계 |
| `internal-comms` | 사내 공지·보고 같은 내부 커뮤니케이션 | 81단계 |
| `brand-guidelines` | 브랜드 색과 글꼴을 결과물에 입히기(자기 회사 것으로 바꿔 쓰는 본보기) | 84단계 |
| `theme-factory` | 장표·문서·웹페이지에 테마 입히기 | 16단계 |
| `frontend-design` | 화면 디자인 방향 잡기 | 18단계, 제3부 |
| `web-artifacts-builder` | 여러 구성 요소로 된 웹 아티팩트 만들기 | 18단계 |
| `webapp-testing` | 만든 웹 화면을 브라우저로 시험하기 | 30단계 |
| `mcp-builder` | MCP 서버 만들기 | 64단계 |
| `canvas-design` | 포스터 같은 시각 자료 만들기 | 17단계 |
| `claude-api` | Claude API로 개발할 때 참고 | 96단계 |

**개발 작업용 스킬 묶음: Superpowers** — <https://github.com/obra/superpowers>

계획 세우기(`writing-plans`), 체계적인 디버깅(`systematic-debugging`), 테스트 먼저 쓰기(`test-driven-development`), 끝났다고 말하기 전 확인(`verification-before-completion`), 서브에이전트로 나눠 개발하기(`subagent-driven-development`) 같은 스킬이 들어 있습니다. 공식 플러그인 마켓플레이스(https://claude.com/marketplace/plugins/superpowers)에서 설치할 수 있습니다. 30단계의 "다 됐다는 말을 그대로 믿지 않는다"와 같은 생각을 스킬로 만든 예입니다.

**모음 목록(커뮤니티)**

| 목록 | 주소 |
|---|---|
| Awesome Claude Skills (travisvn) | <https://github.com/travisvn/awesome-claude-skills> |
| Awesome Claude Skills (ComposioHQ) | <https://github.com/ComposioHQ/awesome-claude-skills> |
| Awesome Claude Code (스킬·명령·훅·도구 모음) | <https://github.com/hesreallyhim/awesome-claude-code> |
| Anthropic 공식 플러그인 목록 | <https://github.com/anthropics/claude-plugins-official> |

커뮤니티 목록에 실린 스킬은 누구나 올릴 수 있습니다. 쓰기 전에 만든 사람, 마지막 수정일, 폴더 안의 스크립트를 확인하고, 회사 자료를 다루는 스킬이라면 98단계의 규칙에 따라 승인을 받습니다.
