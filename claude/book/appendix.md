# 부록

본문 곳곳에 흩어져 있던 것을 한데 모았다. 수업이 끝나고 현업으로 돌아간 뒤 가장 자주 펼쳐 보게 될
곳이다.

## 한눈에 보는 과정

| 편 | 부 | 단계 | 이 부에서 하는 일 |
|---|---|---|---|
| 제1편 기초 다지기 | 1 첫 대화와 제대로 묻는 법 | 1~15 | 기능이 어디 있는지 익히고, 한 번에 쓸 만한 답을 받아 낸다 |
| | 2 결과물로 받아 내기 | 16~22 | 대화를 문서·표·장표·화면으로 바꾼다 |
| 제2편 Claude Code | 3 Claude Code로 직접 만들기 | 23~34 | Claude Code를 설치하고 GitHub를 거쳐, 다른 사람이 열어 볼 수 있는 주소까지 만든다 |
| 제3편 Claude in Chrome | 4 Claude in Chrome, 브라우저를 맡기다 | 35~40 | 브라우저에서 하던 조사와 반복 입력을 맡기고, 안전선을 정한다 |
| 제4편 나만의 업무 시스템 | 5 반복 업무를 스킬로 만들기 | 41~50 | 매번 되풀이하던 설명을 스킬 파일 하나로 옮긴다 |
| | 6 일을 통째로 맡기기 | 51~60 | 폴더째 일을 맡기고 결과물을 받는다 |
| | 7 회사 도구와 연결하기 | 61~70 | Claude가 자료가 있는 곳에 직접 가서 읽게 한다 |
| 제5편 자동화와 조직 확산 | 8 알아서 돌아가게 만들기 | 71~80 | 정해진 때가 되면 사람 없이도 일이 돌게 한다 |
| | 9 부서별 AX: 일의 흐름을 다시 짜기 | 81~90 | 부서마다 일의 흐름과 지표, 사람의 역할을 다시 짜고 AX 로드맵을 만든다 |
| | 10 조직에 뿌리내리기 | 91~100 | 한 사람의 요령을 회사의 규칙으로 만든다 |

### 다섯 칸 질문 틀 (9단계)

**누구로서 · 왜 · 무엇을 · 어디까지 · 어떤 형식으로**. 이 다섯 가지만 채워 넣어도 첫 답부터 달라진다.

### SKILL.md 네 마디 (43단계)

맨 위에 언제 쓰는 스킬인지 밝히는 설명 한 문장을 두고, 그 아래에 **맡은 자리 · 일하는 순서 · 본보기 ·
결과의 꼴**을 차례로 적는다.

### 자동화 설계 여섯 줄 (72단계)

무엇을 얻으려는가 → 재료는 어디 있는가 → 어떤 지시를 주는가 → 무엇이 나오는가 → 누가 보는가 → 누구에게 가는가

### 메일 한 통에서 시트 한 줄까지 (76단계)

새 메일 → 내용 꺼내기 → Claude에게 넘기기 → 분류·요약 → 시트 기록과 담당자 알림 → 보관

## 늘 곁에 둘 일곱 줄

- 읽을 사람과 쓰임새부터 밝힌다
- 자주 쓰는 배경 설명은 프로젝트 지침에 넣어 둔다
- 좋은 본보기 하나를 보여 준다. 긴 설명은 그다음이다
- 결과물의 생김새(표·목록·분량·말투)를 미리 정해 준다
- 일은 한 번에 하나씩 맡긴다
- 모르는 것이 있으면 먼저 물어보라고 해 둔다
- 받은 결과물은 반드시 열어서 확인한다

## Claude Code 주요 / 명령어

Claude Code 입력창에 `/`를 치면 명령 목록이 뜬다. 명령은 버전마다 새로 생기거나 이름이 바뀌니, 아래 표와
화면이 다르면 `/help`와 공식 문서(code.claude.com/docs)를 따른다. 자세한 쓰임은 본문 26단계에 있다.

| 명령 | 하는 일 | 언제 | 본문 |
|---|---|---|---|
| `/help` | 지금 버전에서 쓸 수 있는 명령을 보여 준다 | 명령 이름이 기억나지 않을 때 | 25단계 |
| `/init` | 폴더를 훑어 CLAUDE.md 초안을 만든다 | 새 작업 폴더를 시작할 때 | 26단계 |
| `/memory` | CLAUDE.md 같은 메모리 파일을 연다 | 규칙을 직접 고칠 때 | 26단계 |
| `/config` | 설정 화면을 연다 | 화면 색·알림 같은 설정을 바꿀 때 | 26단계 |
| `/model` | 쓰는 모델을 바꾼다 | 속도와 꼼꼼함 사이에서 고를 때 | 26단계 |
| `/permissions` | 늘 허용·늘 거절할 일을 관리한다 | 같은 허락을 반복해 누를 때 | 31단계 |
| `/login`, `/logout` | 로그인하거나 로그아웃한다 | 계정을 바꾸거나 로그인이 풀렸을 때 | 25단계 |
| `/doctor` | 설치 상태를 점검한다 | 설치나 실행이 이상할 때 | 26단계 |
| `/clear` | 대화를 비우고 새로 시작한다 | 앞 대화와 상관없는 새 과제를 시작할 때 | 26단계 |
| `/compact` | 지금까지의 대화를 요약해 줄인다 | 같은 과제가 길어져 앞의 약속을 흘릴 때 | 26단계 |
| `/context` | 대화가 맥락을 얼마나 차지했는지 보여 준다 | 줄일지 비울지 판단할 때 | 26단계 |
| `/resume` | 이전 대화를 골라 이어 간다 | 어제 하던 일을 계속할 때 | 26단계 |
| `/rewind` | 대화와 Claude가 고친 파일을 앞 시점으로 돌린다 | 방금 시킨 일이 잘못됐을 때(커밋·원본 사본으로 한 번 더 지킨다) | 26단계 |
| `/status` | 계정·모델·버전을 보여 준다 | 지금 상태를 확인할 때 | 26단계 |
| `/usage` (`/cost`) | 사용량을 보여 준다(`/cost`는 같은 명령의 다른 이름) | 얼마나 썼는지 볼 때 | 26단계 |
| `/review` | 바뀐 코드의 검토를 요청한다 | 올리기 전에 한 번 더 볼 때 | 26단계 |
| `/mcp` | 연결한 MCP 서버를 확인·관리한다 | 바깥 도구 연결을 점검할 때 | 32단계 |
| `/agents` | 서브에이전트를 만들고 관리한다 | 검토 같은 일을 따로 맡길 때 | 32단계 |
| `/hooks` | 훅을 보고 관리한다 | 꼭 지킬 규칙을 장치로 옮길 때 | 32단계 |
| `/plugin` | 플러그인을 찾아 설치·관리한다 | 남이 묶어 둔 명령·스킬을 들일 때 | 26단계 |
| `/add-dir` | 다른 폴더를 작업 범위에 더한다 | 지금 폴더 밖의 자료도 읽혀야 할 때 | 26단계 |
| `/exit` | Claude Code를 끝낸다 | 작업을 마칠 때 | 25단계 |
| `/bug`, `/feedback` | 문제를 Anthropic에 알린다. 보내기 전에 확인 화면을 거친다 | 이상한 동작을 보고할 때 | 26단계 |

키보드: Esc는 멈추기, Esc 두 번은 이전 메시지로 돌아가기, Shift+Tab은 모드 바꾸기(플랜 모드 포함).

나만의 명령: `.claude/commands/이름.md` 또는 `.claude/skills/이름/SKILL.md`를 만들어 두면 `/이름`으로 부른다.
폴더 위치는 버전에 따라 다를 수 있다(26단계, 48단계).

## 가장 자주 빠지는 다섯 가지 함정 (91단계)

| 막히는 곳 | 이렇게 푼다 |
|---|---|
| 흐린 지시 | 누가 읽는지, 어디에 쓰는지를 한 문장씩 덧붙인다 |
| 빠진 맥락 | 자주 쓰는 맥락은 프로젝트 지침에 넣어 둔다 |
| 한꺼번에 맡기기 | 일을 단계로 쪼개고, 단계마다 결과를 확인한다 |
| 확인 생략 | 숫자·인용·고유명사는 반드시 출처와 대조한다 |
| 받은 글 그대로 내보내기 | 내 이름으로 나가는 글은 적어도 한 번은 직접 고쳐 쓴다 |

## 막힐 때 보는 표

| 증상 | 의심할 것 | 확인 순서 | 본문 |
|---|---|---|---|
| 그럴듯한 답인데 틀렸다 | 기억에 기대 지어낸 숫자·인용 | 출처를 요구한다 → 웹 검색을 켜고 다시 묻는다 → 원문과 대조한다 | 7단계 |
| 스킬이 불리지 않는다 | 설명(description) 문장 | 언제 쓰는지 적었는지 본다 → 실제 요청 표현과 맞는지 본다 → 스킬 이름을 직접 불러 본다 | 49단계 |
| 스킬이 엉뚱한 때 불린다 | 설명의 범위가 너무 넓다 | 쓰지 말아야 할 경우를 설명에 적어 넣는다 | 49단계 |
| 맡긴 작업이 파일을 덮어썼다 | 권한 범위 | 작업 폴더를 좁힌다 → 사본에서 작업하게 한다 → 실행 전에 확인을 받게 한다 | 59단계 |
| 연결자가 작동하지 않는다 | 로그인 만료·관리자 승인·권한 범위 | 다시 로그인한다 → 관리자에게 승인을 요청한다 → 읽기/쓰기 범위를 확인한다 | 69단계 |
| API 호출이 인증·결제 오류로 실패한다 | 키 복사 실수·폐기된 키·결제 미등록·한도 초과 | 키를 새로 만들어 다시 넣는다 → 콘솔의 결제 화면을 본다 → 한도와 사용량을 본다 | 75단계 |
| 자동화가 소리 없이 멈췄다 | 실패 알림이 없다 | 마지막 실행 기록 → 인증 만료 여부 → 입력 형식이 바뀌었는지 | 78단계 |
| 다 됐다는데 동작하지 않는다 | 확인 없이 받아 든 완료 보고 | 직접 실행해 본다 → 화면을 눈으로 확인한다 → 이전 상태로 되돌려 비교한다 | 33단계 |
| 브라우저 작업이 엉뚱한 곳을 누른다 | 페이지 구조 변경·모호한 지시 | 대상 페이지와 버튼 이름을 지시에 적는다 → 한 단계씩 확인을 받게 한다 → 결과 화면을 직접 본다 | 38단계 |
| 웹페이지 속 문구대로 Claude가 움직이려 한다 | 페이지에 숨은 지시(프롬프트 인젝션) | 작업을 멈춘다 → 허용 사이트를 좁힌다 → 발송·결제·삭제는 확인을 거치게 한다 | 40단계 |

## 주요 소스와 링크

기능과 화면은 자주 바뀐다. 책과 화면이 다르면 아래 공식 문서가 기준이다. 주소는 2026년 9월에 열리는 것을 확인했다.

| 무엇 | 주소 | 이 책에서 |
|---|---|---|
| Claude 앱(웹) | <https://claude.ai> | 1~22단계 |
| 데스크톱·모바일 앱 내려받기 | <https://claude.com/download> | 2단계, 제6부 |
| 요금제 비교 | <https://claude.com/pricing> | 2단계, 97단계 |
| 도움말 센터 | <https://support.claude.com> | 전체 |
| 도움말: 프로젝트 만들고 관리하기 | <https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects> | 5단계 |
| 도움말: 새 기능 소식(릴리스 노트) | <https://support.claude.com/en/articles/12138966-release-notes> | 99단계 |
| 서비스 상태 | <https://status.claude.com> | 막힐 때 |
| 프롬프트 작성 안내 | <https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview> | 9~15단계 |
| Claude Code 문서 | <https://code.claude.com/docs> | 제3부 |
| Claude Code 설치 | <https://code.claude.com/docs/en/setup> | 25단계 |
| Claude Code 명령어 전체 목록 | <https://code.claude.com/docs/en/commands> | 26단계 |
| Claude Code 메모리와 CLAUDE.md | <https://code.claude.com/docs/en/memory> | 26단계 |
| Claude Code 모범 사례 | <https://code.claude.com/docs/en/best-practices> | 26~33단계 |
| Claude Code 훅 | <https://code.claude.com/docs/en/hooks> | 32단계 |
| Claude Code 서브에이전트 | <https://code.claude.com/docs/en/sub-agents> | 32단계 |
| Claude Code MCP 연결 | <https://code.claude.com/docs/en/mcp> | 32단계, 66단계 |
| Claude Code 플러그인 | <https://code.claude.com/docs/en/plugins> | 48단계 |
| Claude Code 비용 관리 | <https://code.claude.com/docs/en/costs> | 97단계 |
| Claude Code 보안 | <https://code.claude.com/docs/en/security> | 31단계, 98단계 |
| Claude Code 변경 기록 | <https://code.claude.com/docs/en/changelog> | 99단계 |
| Claude in Chrome | <https://claude.com/chrome> | 제4부 |
| Claude Cowork | <https://claude.com/product/cowork> | 제6부 |
| 연결자·플러그인 목록 | <https://claude.com/connectors> | 제7부 |
| MCP 공식 안내 | <https://modelcontextprotocol.io> | 62단계 |
| MCP 서버 예시 모음 | <https://github.com/modelcontextprotocol/servers> | 62단계 |
| Hugging Face MCP 설정 | <https://huggingface.co/settings/mcp> | 66단계 |
| Claude Console(API 키·결제·사용량) | <https://platform.claude.com> | 75단계, 96~97단계 |
| API 개요 | <https://platform.claude.com/docs/en/api/overview> | 96단계 |
| 모델 목록 | <https://docs.claude.com/en/docs/about-claude/models/overview> | 2단계, 75단계 |
| Zapier의 Claude 연동 | <https://zapier.com/apps/anthropic-claude/integrations> | 75단계 |
| n8n 문서 | <https://docs.n8n.io> | 75단계 |
| GitHub 시작하기 | <https://docs.github.com/en/get-started> | 28~29단계 |
| Cloudflare Pages 문서 | <https://developers.cloudflare.com/pages/> | 30~31단계 |
| Cloudflare Pages Git 연결 | <https://developers.cloudflare.com/pages/get-started/git-integration/> | 30단계 |
| Cloudflare Pages 되돌리기 | <https://developers.cloudflare.com/pages/configuration/rollbacks/> | 31단계 |
| Vercel 배포 | <https://vercel.com/docs/deployments> | 30단계 |
| Vercel 도메인 | <https://vercel.com/docs/domains> | 30단계 |
| Vercel 즉시 되돌리기 | <https://vercel.com/docs/instant-rollback> | 31단계 |
| Anthropic 소식 | <https://www.anthropic.com/news> | 99단계 |
| Anthropic 엔지니어링 블로그 | <https://www.anthropic.com/engineering> | 99단계 |
| Claude Academy(무료 강좌) | <https://www.anthropic.com/learn> | 전체 |
| Claude Code 공개 저장소(이슈·소식) | <https://github.com/anthropics/claude-code> | 제3부 |
| Claude 쿡북(예제 코드) | <https://github.com/anthropics/claude-cookbooks> | 96단계 |
| 김문수 교수 칼럼 모음 | <https://ceoai.kr/leadership2/reads/> | 칼럼 인용 |

## 인기 스킬과 스킬 모음

스킬을 처음부터 만들기 전에 이미 공개된 스킬을 먼저 살펴보자. 잘 만든 스킬의 SKILL.md를 읽어 보는 것만으로도 43단계의 네 마디가 어떻게 쓰이는지 보인다. 남이 만든 스킬은 설치하기 전에 폴더 안의 파일을 열어 무엇을 하는지 확인한다. 특히 스크립트가 들어 있으면 IT 담당과 함께 본다.

**설치와 사용 안내**

| 무엇 | 주소 |
|---|---|
| 스킬이란 무엇인가(도움말) | <https://support.claude.com/en/articles/12512176-what-are-skills> |
| Claude 앱에서 스킬 쓰기와 올리기 | <https://support.claude.com/en/articles/12512180-using-skills-in-claude> |
| Claude Code에서 스킬 쓰기 | <https://code.claude.com/docs/en/skills> |
| API에서 스킬 쓰기 | <https://docs.claude.com/en/api/skills-guide> |
| 스킬 개념 설명(개발자 문서) | <https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview> |
| 스킬을 만든 배경(Anthropic 엔지니어링 글) | <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills> |
| 플러그인 마켓플레이스 | <https://claude.com/plugins> |

**Anthropic 공개 스킬 저장소** — <https://github.com/anthropics/skills>

Claude Code에서는 `/plugin marketplace add anthropics/skills`로 이 저장소를 등록한 뒤 필요한 묶음을 설치할 수 있다. 유료 요금제의 Claude 앱에는 여기 있는 스킬 상당수가 이미 들어 있다.

| 스킬 | 하는 일 | 이 책에서 |
|---|---|---|
| `docx` | 워드 문서 만들기·고치기 | 17단계 |
| `xlsx` | 엑셀 만들기·정리·수식 | 17단계 |
| `pptx` | 파워포인트 장표 만들기 | 18단계 |
| `pdf` | PDF 읽기·합치기·나누기·양식 채우기 | 14단계 |
| `skill-creator` | 스킬을 만들고 시험하고 다듬기 | 42~49단계 |
| `doc-coauthoring` | 제안서·기획서를 단계별로 함께 쓰기 | 17단계 |
| `internal-comms` | 사내 공지·보고 같은 내부 커뮤니케이션 | 81단계 |
| `brand-guidelines` | 브랜드 색과 글꼴을 결과물에 입히기(자기 회사 것으로 바꿔 쓰는 본보기) | 84단계 |
| `theme-factory` | 장표·문서·웹페이지에 테마 입히기 | 18단계 |
| `frontend-design` | 화면 디자인 방향 잡기 | 20단계, 제3부 |
| `web-artifacts-builder` | 여러 구성 요소로 된 웹 아티팩트 만들기 | 20단계 |
| `webapp-testing` | 만든 웹 화면을 브라우저로 시험하기 | 33단계 |
| `mcp-builder` | MCP 서버 만들기 | 62단계 |
| `canvas-design` | 포스터 같은 시각 자료 만들기 | 19단계 |
| `claude-api` | Claude API로 개발할 때 참고 | 96단계 |

**개발 작업용 스킬 묶음: Superpowers** — <https://github.com/obra/superpowers>

계획 세우기(`writing-plans`), 체계적인 디버깅(`systematic-debugging`), 테스트 먼저 쓰기(`test-driven-development`), 끝났다고 말하기 전 확인(`verification-before-completion`), 서브에이전트로 나눠 개발하기(`subagent-driven-development`) 같은 스킬이 들어 있다. 공식 플러그인 마켓플레이스(https://claude.com/plugins/superpowers)에서 설치할 수 있다. 33단계의 "다 됐다는 말을 그대로 믿지 않는다"와 같은 생각을 스킬로 만든 예다.

**모음 목록(커뮤니티)**

| 목록 | 주소 |
|---|---|
| Awesome Claude Skills (travisvn) | <https://github.com/travisvn/awesome-claude-skills> |
| Awesome Claude Skills (ComposioHQ) | <https://github.com/ComposioHQ/awesome-claude-skills> |
| Awesome Claude Code (스킬·명령·훅·도구 모음) | <https://github.com/hesreallyhim/awesome-claude-code> |
| Anthropic 공식 플러그인 목록 | <https://github.com/anthropics/claude-plugins-official> |

커뮤니티 목록에 실린 스킬은 누구나 올릴 수 있다. 쓰기 전에 만든 사람, 마지막 수정일, 폴더 안의 스크립트를 확인하고, 회사 자료를 다루는 스킬이라면 98단계의 규칙에 따라 승인을 받는다.

## 함께 읽을 칼럼

아래 칼럼은 저자가 CEO경제신문에 쓴 글이며, 모두 [https://ceoai.kr/leadership2/reads/](https://ceoai.kr/leadership2/reads/)에 모아 두었다.

| 칼럼 | 날짜 | 한 문장 요지 | 이 책에서 이어지는 곳 |
|---|---|---|---|
| [\[사설\] 신과 자연을 이긴 인류, 이제 '스스로 창조한 거인'의 어깨에 오르다](https://www.ceoeconomy.com/news/articleView.html?idxno=20003) | 2026.06.19 | 자연과 신과 신분의 굴레를 넘어선 인류가 이제 지능을 만드는 단계에 섰고, 여러 에이전트를 사람의 의도에 맞게 조율하는 하네스 엔지니어링이 새 과제가 됐다. | 제8부 71단계 |
| [일반 지능으로는 기업을 경영할 수 없다: AI 초지능(ASI)이 중요한 이유](https://www.ceoeconomy.com/news/articleView.html?idxno=20005) | 2026.06.26 | 사람 수준의 일반 지능을 넘어 전문가 집단 전체를 능가하는 초지능(ASI)이 기업 경영의 격차를 가르게 된다. | 관련: 책을 마치며 |
| [\[AX가이드\] 심장을 외주 줄 수는 없다](https://www.ceoeconomy.com/news/articleView.html?idxno=20008) | 2026.07.09 | 데이터와 개발 역량은 AX의 심장이므로 외주에 넘겨 두지 말고, 우리 고객 데이터를 우리 손으로 바로 꺼내 볼 수 있어야 한다. | 제7부 61단계 |
| [일반의학과 경영의학의 차이점 (AX담당자가 가져야 할 자세)](https://www.ceoeconomy.com/news/articleView.html?idxno=20011) | 2026.07.15 | AX 담당자는 도구부터 들이밀지 말고, 기업의 역사와 체질을 먼저 살핀 뒤 처방하는 경영의학자의 자세를 가져야 한다. | 제9부 90단계 |
| [\[AX CEO가이드\] 회계장부 보듯이, 코드장부도 봐야 한다](https://www.ceoeconomy.com/news/articleView.html?idxno=20027) | 2026.07.24 | 경영자는 회계장부처럼 오픈소스 의존, 기술부채, AI가 만든 코드를 적은 코드장부를 직접 챙겨야 하며, 그 첫걸음은 깃허브 계정이다. | 제3부 28단계, 제7부 67단계 |
| [인공지능 70주년, 지금부터 3년이 30년을 가른다](https://www.ceoeconomy.com/news/articleView.html?idxno=20092) | 2026.08.01 | 70년을 기다린 AI가 급가속하는 지금, 조직마다 다른 시계 속도 때문에 앞으로 3년의 차이가 30년의 순위를 정한다. | 제2부 20단계, 제2부 22단계 |
| [지능형 제품의 조건 (김문수 교수의 AX전략가이드)](https://www.ceoeconomy.com/news/articleView.html?idxno=20161) | 2026.08.09 | 지능은 반복해서 나아지는 능력이며, 예지·준비·위임·진화를 갖춘 제품은 갈아엎지 말고 계측과 되먹임, 책임자를 두어 키워야 한다. | 제8부 80단계, 제10부 95단계 |
| [AI시대에 콜센터는 보물이다](https://www.ceoeconomy.com/news/articleView.html?idxno=20227) | 2026.08.16 | 고객이 스스로 말해 주는 상담 기록은 AI 시대의 자산이므로, 원본과 분류 체계와 되먹임 경로를 되찾고 자산 지표로 관리해야 한다. | 제9부 87단계 |
| [\[AX 가이드\] 유지보수가 아니라 발전보수다](https://www.ceoeconomy.com/news/articleView.html?idxno=20228) | 2026.08.17 | 유지보수 계약에 개선 몫과 개선 지표, 되먹임 경로를 넣어 해마다 나아지는 발전보수로 바꿔야 하고, AI가 그 개선의 단가를 낮췄다. | 제8부 72단계 |
| [AI시대에 가장 각광받는 개발언어는?](https://www.ceoeconomy.com/news/articleView.html?idxno=20352) | 2026.08.30 | AI 시대에 가장 좋은 개발언어는 회사의 맥락이 담긴 사람의 말이며, 업무명세를 쓰고 현업에 도구를 열어 회사 전체를 AI에 이어야 한다. | 제1부 9단계, 제5부 50단계, 제9부 81단계 |
| [바이브 코딩은 대화(對話) 코딩이고, 에이전틱 코딩은 대리(代理) 코딩이다](https://www.ceoeconomy.com/news/articleView.html?idxno=20377) | 2026.09.02 | 바이브 코딩은 대화하며 만드는 방식이고 에이전틱 코딩은 목적지와 범위를 적은 위임장을 주고 맡기는 방식이며, 맡기면 감독의 비용이 따른다. | 제3부 26단계, 제4부 40단계, 제6부 51단계 |
| [AI의 원리, 어색할 뿐 설명 가능하다 (경영의 문법이 바뀌는 이유)](https://www.ceoeconomy.com/news/articleView.html?idxno=20446) | 2026.09.11 | AI는 확률과 연결이라는 낯선 문법으로 설명할 수 있는 기술이며, 경영자도 판단을 가설로 두고 빠르게 고치는 문법을 하나 더 갖춰야 한다. | 제1부 7단계 |
| [\[AGI 경영전략\] 의사결정의 품질을 설계하라](https://www.ceoeconomy.com/news/articleView.html?idxno=20457) | 2026.09.14 | AI에 실행을 맡길수록 목표와 흐름의 설계, 위임 범위, 일상적인 검증, 판단력의 축적 같은 의사결정의 품질이 성과를 가른다. | 제4부 38단계, 제6부 59단계, 제10부 98단계 |
| [\[AGI 경영전략\] 화려한 기획자가 아니라 유능한 확인자가 필요하다](https://www.ceoeconomy.com/news/articleView.html?idxno=20469) | 2026.09.14 | AI가 생산을 맡을수록 병목은 확인으로 옮겨 가므로, 윤리성과 꼼꼼함과 깊은 피드백을 갖춘 확인자가 필요하다. | 제1부 13단계, 제3부 33단계, 제6부 58단계 |
| [AX를 잘하는 기업은 무엇이 다를까?](https://www.ceoeconomy.com/news/articleView.html?idxno=20953) | 2026.09.19 | 같은 AI를 써도 암묵지·형식지·프로세스가 살아 순환하는 조직이 더 크게 성과를 내며, AX는 그 조직의 신경망을 잇는 일이다. | 제5부 41단계, 제10부 99단계 |

## 용어

| 용어 | 뜻 |
|---|---|
| 프로젝트 | 자료와 지침을 한곳에 모아 두는 작업 공간. 그 안에서 나누는 대화는 같은 맥락을 공유한다 |
| 아티팩트 | 대화 옆에 따로 열리는 결과물. 문서·코드·웹페이지·다이어그램 등을 바로 고치고 내려받기 쉽다 |
| 스킬 | 반복 업무의 지침·양식·예시를 담아 둔 폴더. 핵심은 SKILL.md 파일 하나다 |
| Claude Code | 폴더의 파일을 읽고 쓰고 명령을 실행하며 코드와 업무 파일을 다루는 에이전트. 터미널·데스크톱·웹에서 쓴다 |
| Claude in Chrome | Chrome 브라우저 안에서 페이지를 읽고, 이동하고, 입력하는 등 브라우저 작업을 맡는 확장 프로그램 |
| Cowork | 데스크톱 앱에서 폴더를 통째로 맡기고 여러 단계에 걸친 일을 시키는 방식 |
| 연결자 | Claude가 외부 도구(드라이브·메일·메신저 등)에 직접 들어가 읽고 쓸 수 있게 해 주는 통로 |
| MCP | 연결자를 만드는 공통 규격. 도구마다 따로 만들 필요 없이 한 가지 방식으로 연결한다 |
| Hugging Face | AI 모델·공개 데이터셋·논문·Space(작은 웹 앱)를 모아 둔 곳. MCP로 Claude에 연결해 찾고 비교할 수 있다(66단계) |
| 트리거 | 자동화를 시작시키는 신호. 정해진 시각, 새 메일, 새 파일, 버튼 클릭 등 |
| CLAUDE.md | Claude Code가 작업할 때마다 먼저 읽는 프로젝트 규칙 파일 |
| API | 화면을 거치지 않고 우리 시스템에서 Claude를 직접 호출하는 방법 |
| API 키 | API를 부를 때 쓰는 비밀 열쇠. Claude Console에서 발급하며, 전체 값은 만들 때 한 번만 보인다 |
