# GPT(Codex·ChatGPT) 사실 확인표

- 용도: 『클로드·GPT 완전정복 100단계』 집필용 사실 확인 자료
- 확인일: **2026-09-27** (아래 모든 항목은 이 날짜에 확인. 다른 날짜는 따로 적음)
- 원칙: 공식 출처 우선. 각 항목 끝 괄호 안이 출처. 공식 본문을 직접 읽지 못했거나 출처끼리 어긋나면 **확인 필요**로 표시.
- 문서 위치 변화: Codex·ChatGPT 공식 문서는 현재 `learn.chatgpt.com/docs/...`에 있고, 예전 주소 `developers.openai.com/codex/...`는 계속 열린다(200 응답 확인). 페이지 주소 끝에 `.md`를 붙이면 마크다운 원문이 열린다. (https://developers.openai.com/codex/llms.txt)
- 읽지 못한 곳: help.openai.com, chatgpt.com, platform.openai.com은 자동 수집을 막아(403) 본문을 직접 읽지 못했다. 이 세 곳이 출처인 항목은 검색 결과 요약으로만 확인했으므로 모두 **확인 필요**로 표시했다.
- GitHub 저장소(openai/codex)는 2026-09-27 커밋 67a7096 기준으로 복제해서 읽었다. 저장소의 `docs/` 폴더는 대부분 웹 문서로 넘기는 안내 페이지다.

---

# 1부. Codex

## 1. 제품 구성

| 쓰는 곳 | 무엇에 쓰나 | 출처 |
|---|---|---|
| Codex CLI | 터미널에서 로컬 저장소를 읽고, 고치고, 명령을 실행한다. `codex exec`로 스크립트나 CI에도 붙인다. | https://learn.chatgpt.com/docs/codex/cli |
| IDE 확장 | VS Code, Cursor, Windsurf, VS Code Insiders에서 쓴다. 확장 ID는 `openai.chatgpt`. 열린 파일과 선택 영역을 맥락으로 쓰고, 긴 작업은 클라우드로 넘긴다. Xcode와 JetBrains IDE는 각 회사가 만든 통합 기능으로 Codex를 쓴다. | https://learn.chatgpt.com/docs/codex/ide |
| ChatGPT 데스크톱 앱(Codex) | 별도 "Codex 앱"은 이제 **ChatGPT 데스크톱 앱 안의 Codex**다. 앱에서 ChatGPT와 Codex 중 하나를 고른다. 실행 위치는 Local(현재 폴더), Worktree(Git 워크트리로 격리), Cloud(클라우드 환경) 세 가지다. macOS·Windows·Linux를 지원한다. | https://learn.chatgpt.com/docs/app , https://learn.chatgpt.com/docs/environments/modes |
| CLI에서 앱으로 이동 | CLI에서 `codex app`을 실행하거나 `/app`을 입력하면 같은 세션을 데스크톱 앱에서 이어 간다. | https://github.com/openai/codex (README), https://learn.chatgpt.com/docs/developer-commands?surface=cli |
| Codex cloud(웹) | chatgpt.com/codex에서 쓴다. 격리된 클라우드 컨테이너에서 여러 작업을 동시에 돌리고, 결과 diff를 검토한 뒤 PR로 만든다. GitHub, GitLab(베타), Linear, Slack에서도 작업을 시작할 수 있다. | https://learn.chatgpt.com/docs/cloud |
| 모바일(Codex Remote) | ChatGPT 모바일 앱에서 연결된 Mac/Windows PC의 Codex 작업을 시작하고, 승인하고, 결과를 검토한다. 작업은 PC에서 실행된다. 기능이 계정마다 차례로 열린다(롤아웃). | https://learn.chatgpt.com/docs/remote |
| GitHub 연동 | PR 코드 리뷰(`@codex review`), 자동 리뷰, `@codex`로 작업 맡기기. Codex cloud 설정이 먼저 되어 있어야 한다. | https://learn.chatgpt.com/docs/third-party/github |
| SDK·자동화 | `codex exec`, GitHub Action(`openai/codex-action@v1`), TypeScript SDK(`@openai/codex-sdk`), Python SDK(`openai-codex`), 앱 서버(실험 단계). | https://learn.chatgpt.com/docs/non-interactive-mode , https://learn.chatgpt.com/docs/codex-sdk |
| ChatGPT Work와의 관계 | ChatGPT의 "Work" 모드와 Codex는 기능이 겹치고 사용량 한도를 함께 쓴다. 비개발 업무는 Work, 개발 도구와 기술적 세부가 필요하면 Codex를 쓰라고 안내한다. | https://learn.chatgpt.com/docs/use-chatgpt , https://learn.chatgpt.com/docs/pricing |

## 2. 요금제와 로그인

**요금제에 포함되는 범위** (출처: https://learn.chatgpt.com/docs/pricing , 가격은 바뀔 수 있음)

| 요금제 | Codex 범위 | 표시 가격(확인일 기준) |
|---|---|---|
| Free | 데스크톱 앱에서 GPT-6 Luna(표준 속도). 롤아웃에 따라 다름 | $0 |
| Go | 데스크톱 앱에서 GPT-6 Luna(표준 속도). 롤아웃에 따라 다름 | $8/월 |
| Plus | 웹, CLI, IDE 확장, iOS. 클라우드 연동(자동 코드 리뷰, Slack 등). GPT-6 Sol·Luna. 크레딧을 사서 사용량을 늘릴 수 있음 | $20/월 |
| Pro | Plus의 5배 또는 20배 사용량 중 선택 | $100/월부터 |
| Business | 데스크톱·모바일 앱, 더 큰 클라우드 VM, SAML SSO·MFA, 기본적으로 업무 데이터를 학습에 쓰지 않음 | 연간 결제 시 사용자당 $20/월(2인 이상), 월간 결제 시 $25 |
| Enterprise·Edu | Business 기능에 SCIM, EKM, RBAC, 감사 로그(Compliance API), 데이터 보존·저장 위치(레지던시) 통제 추가 | 영업팀 문의 |
| API 키 | CLI, SDK, IDE 확장만 쓸 수 있고 클라우드 기능(GitHub 코드 리뷰, Slack 등)은 못 쓴다. API 요금으로 과금 | 사용량 기준 |

- 기능표 기준으로 API 키 로그인에서 안 되는 것: Codex cloud, 클라우드 환경, GitHub `@codex` 위임·코드 리뷰, Slack·Linear 연동, 모바일 원격 제어. (https://learn.chatgpt.com/docs/pricing#feature-availability)
- 로그인 방식은 두 가지다. ChatGPT 계정으로 로그인하면 구독 한도 안에서 쓰고, API 키로 로그인하면 쓴 만큼 낸다. 데스크톱 앱, CLI, IDE 확장은 둘 다 되지만 **Codex cloud는 ChatGPT 로그인만 된다.** (https://learn.chatgpt.com/docs/auth)
- CLI 명령: `codex login`은 브라우저 로그인, `printenv OPENAI_API_KEY | codex login --with-api-key`는 API 키 로그인, `codex login status`는 현재 상태 확인, `codex logout`은 로그아웃. 원격 서버처럼 브라우저가 없는 곳에서는 `codex login --device-auth`(기기 코드 방식, 베타)를 쓴다. (https://learn.chatgpt.com/docs/auth)
- Enterprise 워크스페이스에서는 자동화용 **Codex 액세스 토큰**을 만들 수 있다(`codex login --with-access-token`). 기능표상 Business·Enterprise에서만 된다. (https://learn.chatgpt.com/docs/auth , https://learn.chatgpt.com/docs/pricing)
- 로그인 정보는 `~/.codex/auth.json` 또는 OS 자격 증명 저장소에 저장된다. auth.json은 비밀번호처럼 다뤄야 한다. CLI와 IDE 확장은 로그인 정보를 함께 쓴다. (https://learn.chatgpt.com/docs/auth)
- 이메일·비밀번호로 가입한 계정은 Codex cloud를 쓰기 전에 MFA(2단계 인증)를 켜야 한다. (https://learn.chatgpt.com/docs/auth)
- **사용량 한도 구조**: 5시간 단위로 쓸 수 있는 메시지 수의 범위가 제시되고, 주간 한도가 따로 걸릴 수 있다. 로컬 작업과 클라우드 작업은 같은 한도를 나눠 쓴다. 쓰는 양은 모델, 맥락 크기, 추론 강도에 따라 달라진다. 한도는 사용량 대시보드(chatgpt.com/codex/settings/usage)나 CLI의 `/status`, `/usage`에서 확인한다. 한도에 닿아도 진행 중인 턴은 마무리된다. Plus·Pro는 크레딧을 추가로 살 수 있다. (https://learn.chatgpt.com/docs/pricing , https://learn.chatgpt.com/docs/developer-commands?surface=cli)
- 예시 수치(Plus 기준, 5시간당 로컬 메시지): GPT-6 Sol 15~150개, GPT-6 Luna 350~3,000개, GPT-6 Astra 5~45개. 고정 한도가 아니라 추정치다. (https://learn.chatgpt.com/docs/pricing)
- ChatGPT Work와 Codex는 요금, 크레딧, 사용량 한도를 함께 쓴다. (https://learn.chatgpt.com/docs/pricing)
- help.openai.com의 "Codex in ChatGPT" 도움말(https://help.openai.com/en/articles/11369540-codex-in-chatgpt)은 README가 연결해 두었지만 403으로 막혀 열지 못했다 → **확인 필요**.

## 3. 설치와 첫 실행

| 방법 | 명령 | 출처 |
|---|---|---|
| macOS/Linux 공식 설치 스크립트 | `curl -fsSL https://chatgpt.com/codex/install.sh \| sh` (업데이트도 같은 명령) | https://learn.chatgpt.com/docs/codex/cli |
| Windows 공식 설치 스크립트(PowerShell) | `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 \| iex"` | https://learn.chatgpt.com/docs/codex/cli |
| npm | `npm install -g @openai/codex` | 같은 곳 |
| Homebrew | `brew install --cask codex` / 업데이트 `brew upgrade --cask codex` | 같은 곳 |
| 바이너리 직접 받기 | GitHub Releases에서 플랫폼별 파일 | https://github.com/openai/codex (README) |

- **Windows**: 이제 네이티브 Windows(PowerShell + Windows 샌드박스)를 지원한다. 샌드박스 모드는 `elevated`(권장)와 `unelevated`(관리자 권한이 없을 때 쓰는 대안) 두 가지다. WSL2도 쓸 수 있다. WSL1은 0.114까지만 지원했다. (https://learn.chatgpt.com/docs/windows/windows-sandbox , https://learn.chatgpt.com/docs/windows/wsl , https://learn.chatgpt.com/docs/config-file/config-basic)
  - 저장소 `docs/install.md`에는 아직 "Windows 11 **via WSL2**"라고 적혀 있다. 웹 문서보다 오래된 내용으로 보인다. (https://github.com/openai/codex/blob/main/docs/install.md)
- WSL에서 쓰기: PowerShell에서 `wsl --install` → `wsl`로 들어간 뒤 설치 스크립트 실행 → `codex`. 저장소는 `/mnt/c`가 아니라 리눅스 홈(`~/code/...`)에 두라고 권장한다. (https://learn.chatgpt.com/docs/windows/wsl)
- 첫 실행: 프로젝트 폴더에서 `codex`를 실행하고 **Sign in with ChatGPT**를 고른다. 작업 전후로 Git 체크포인트(커밋)를 만들라고 권장한다. (https://learn.chatgpt.com/docs/codex/cli)
- 버전 확인: `codex --version`. CLI가 clap의 `version` 속성을 쓰므로 이 플래그가 있다(소스 확인). 웹 문서에 이 명령이 적힌 곳은 찾지 못했다. (https://github.com/openai/codex/blob/main/codex-rs/cli/src/main.rs)
- 업데이트·진단: `codex update`(스스로 업데이트할 수 있는 빌드에서), `codex doctor`(설치·설정·인증 진단 보고서). (https://learn.chatgpt.com/docs/developer-commands?surface=cli)
- npm 최신 버전은 확인일 기준 **0.157.1**. (https://registry.npmjs.org/@openai/codex/latest)
- 권장 사양(저장소 문서): macOS 12+, Ubuntu 20.04+/Debian 10+, RAM 4GB 이상(8GB 권장), Git 2.23+ 권장. (https://github.com/openai/codex/blob/main/docs/install.md)
- 데스크톱 앱 설치: chatgpt.com/download에서 받는다. Windows는 Microsoft Store나 `winget install --id 9PLM9XGG6VKS -s msstore`로 설치한다. (https://learn.chatgpt.com/docs/app , https://learn.chatgpt.com/docs/windows/windows-app)

## 4. 규칙 파일(AGENTS.md)

- Codex는 작업을 시작하기 전에 `AGENTS.md`를 읽는다. (https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- 읽는 순서:
  1. 전역: `~/.codex/AGENTS.override.md`가 있으면 그것을, 없으면 `~/.codex/AGENTS.md`를 읽는다(`CODEX_HOME`으로 위치 변경 가능).
  2. 프로젝트: 저장소 루트(보통 Git 루트)에서 현재 폴더까지 내려가며 폴더마다 `AGENTS.override.md` → `AGENTS.md` → 대체 파일명 순으로 **폴더당 한 개**만 읽는다.
  3. 합치기: 위쪽 폴더부터 차례로 이어 붙이므로, 현재 폴더에 가까운 파일이 뒤에 붙어 앞 내용보다 우선한다.
  4. 빈 파일은 건너뛰고, 합친 크기가 `project_doc_max_bytes`(기본 32KiB)에 닿으면 더 읽지 않는다.
  (https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- 다른 파일 이름도 규칙 파일로 인정할 수 있다: `project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]`. (같은 출처)
- 무엇을 적나: 작업 약속(예: JS를 고친 뒤 `npm test` 실행, 의존성은 pnpm으로 설치, 운영 의존성 추가 전 확인 받기), 저장소 규칙(PR 전 lint), 하위 서비스별 규칙. GitHub 코드 리뷰 규칙은 `## Code Review Rules` 섹션에 적는다. (같은 출처)
- `/init`을 입력하면 현재 폴더에 AGENTS.md 초안을 만들어 준다. (https://learn.chatgpt.com/docs/developer-commands?surface=cli)
- 클라우드 작업도 AGENTS.md에서 lint·테스트 명령을 찾아 쓴다. (https://learn.chatgpt.com/docs/environments/cloud-environment)
- ChatGPT의 개인 맞춤 지침(custom instructions)은 Codex에서는 전역 `AGENTS.md`에 저장된다. (https://learn.chatgpt.com/docs/personalize)
- CLAUDE.md와 비교: 둘 다 마크다운으로 쓴 프로젝트 지침이고 전역·프로젝트·하위 폴더 단계가 있다. Codex는 `CLAUDE.md`를 자동으로 읽지 않는다(기본 목록은 AGENTS.override.md, AGENTS.md뿐). 같이 쓰려면 `project_doc_fallback_filenames`에 `CLAUDE.md`를 넣거나, `/import`로 Claude Code 설정을 가져온다. 대체 파일명 설정은 문서에서 확인했지만, CLAUDE.md를 넣어 실제로 읽히는지는 직접 시험하지 않았다. (https://learn.chatgpt.com/docs/agent-configuration/agents-md , https://learn.chatgpt.com/docs/import)
- `/import`: Codex CLI는 Claude Code와 Cursor에서, 데스크톱 앱은 Claude Code, Claude Cowork, Cursor에서 설정·스킬·플러그인·프로젝트·최근 대화를 가져온다. 가져와도 원래 도구의 설정은 바뀌지 않는다. (https://learn.chatgpt.com/docs/import)

## 5. 권한과 안전

**두 층으로 되어 있다**: 샌드박스(기술적으로 무엇을 할 수 있나)와 승인 정책(언제 멈추고 묻나). (https://learn.chatgpt.com/docs/agent-approvals-security)

샌드박스 모드(`sandbox_mode` / `--sandbox`) (https://learn.chatgpt.com/docs/config-file/config-reference)

| 값 | 의미 |
|---|---|
| `read-only` | 읽기만 한다 |
| `workspace-write` | 작업 폴더(와 /tmp 같은 임시 폴더) 안에서만 쓴다. 네트워크는 기본으로 꺼져 있다 |
| `danger-full-access` | 샌드박스 없음 |

승인 정책(`approval_policy` / `--ask-for-approval`, `-a`) (같은 출처)

| 값 | 의미 |
|---|---|
| `on-request` | 샌드박스 안의 일은 묻지 않고 하고, 밖으로 나가야 하면 묻는다(대화형 기본) |
| `never` | 묻지 않는다(비대화 실행용). 샌드박스 제한은 그대로 남는다 |
| `granular` | 항목별로 물을지 자동 거절할지 정한다(sandbox_approval, rules, mcp_elicitations, request_permissions, skill_approval) |
| `untrusted` | **지원 종료.** 설정에 남아 있으면 실행이 안 될 수 있다 |
| `on-failure` | **사용 중단 예정(deprecated)** |

- 대표 조합: **Auto** 프리셋 = `--sandbox workspace-write --ask-for-approval on-request`. 폴더 안에서는 읽기·수정·명령 실행을 알아서 하고, 폴더 밖 수정이나 네트워크 사용은 묻는다. 읽기 전용은 `--sandbox read-only --ask-for-approval on-request`. 전부 허용은 `--dangerously-bypass-approvals-and-sandbox`(별칭 `--yolo`)이며 권장하지 않는다. (https://learn.chatgpt.com/docs/agent-approvals-security)
- 시작할 때 폴더가 Git으로 관리되면 Auto를, 아니면 read-only를 권한다. CLI에서는 `/permissions`로 바꾼다. (같은 출처)
- **자동 승인 검토(Auto-review)**: `approvals_reviewer = "auto_review"`로 켜면 승인 요청을 사용자 대신 검토 에이전트가 판단한다. 샌드박스 범위는 넓어지지 않는다. 거절된 요청을 한 번 다시 허용하려면 `/approve`를 쓴다. (같은 출처)
- 데스크톱 앱과 IDE의 권한 모드 이름은 **Ask for approval**(기본), **Approve for me**(설정 화면 이름은 Auto-review), **Full access**다. 뒤의 두 개는 설정 > General > Permissions에서 켜야 메뉴에 나온다. (https://learn.chatgpt.com/docs/permission-modes)
- **네트워크 기본값**: 로컬은 `workspace-write`에서 꺼져 있다. `[sandbox_workspace_write] network_access = true`로 켠다. 도메인별로 허용하려면 `network_proxy` 기능을 쓴다. 웹 검색은 기본값이 `web_search = "cached"`(OpenAI가 미리 색인한 결과)이고 `--search`나 `"live"`로 실시간 검색을 한다. 클라우드는 설정 스크립트 단계에서만 인터넷을 쓰고, 에이전트 단계는 기본으로 차단한다. (https://learn.chatgpt.com/docs/agent-approvals-security , https://learn.chatgpt.com/docs/config-file/config-basic , https://learn.chatgpt.com/docs/cloud/internet-access)
- 보호 경로: `workspace-write`에서도 `.git`, `.agents`, `.codex` 폴더는 읽기 전용이다. (https://learn.chatgpt.com/docs/agent-approvals-security)
- OS별 샌드박스: macOS는 Seatbelt, Linux는 bwrap+seccomp, Windows는 네이티브 샌드박스 또는 WSL2(리눅스 방식)를 쓴다. (같은 출처)
- **되돌리기**
  - 공식 권장 방법은 Git 체크포인트다. 작업 전후로 커밋하고, 기능 브랜치에서 `git status`를 깨끗이 해 둔 뒤 맡기라고 한다. (https://learn.chatgpt.com/docs/codex/cli , https://learn.chatgpt.com/docs/agent-approvals-security)
  - CLI에서는 `/diff`로 변경 사항을 보고, `/review`로 검토한다. 현재 CLI 슬래시 명령 목록에 `/undo`는 없다(소스의 명령 목록에도 없음). (https://learn.chatgpt.com/docs/developer-commands?surface=cli)
  - 데스크톱 앱의 리뷰 화면에서는 전체, 파일, 덩어리(hunk) 단위로 Stage·Revert할 수 있다. (https://learn.chatgpt.com/docs/codex-manual.md, "Staging and reverting files" 절)
- 안전 모니터링: GPT-6 Astra는 위험한 행동을 감지하면 작업을 일시정지할 수 있다. CLI와 모바일에서는 이렇게 멈춘 작업을 다시 이어 가지 못하고 끝난다. (https://learn.chatgpt.com/docs/agent-approvals-security)

## 6. 슬래시 명령과 설정

**CLI 주요 `/` 명령** (https://learn.chatgpt.com/docs/developer-commands?surface=cli)

| 명령 | 하는 일 |
|---|---|
| `/model` | 모델과 추론 강도 선택 |
| `/permissions` | 승인·샌드박스 범위 변경(Auto ↔ Read Only 등) |
| `/plan` | 계획 모드로 전환. Shift+Tab으로도 켜고 끈다 |
| `/init` | AGENTS.md 초안 생성 |
| `/status` | 모델, 승인 정책, 쓰기 가능 폴더, 남은 맥락, 사용량 표시 |
| `/usage` | 계정 토큰 사용량 |
| `/diff` | Git diff 보기(추적 안 된 파일 포함) |
| `/review` | 작업 트리 코드 리뷰 |
| `/compact` | 대화를 요약해 맥락 확보 |
| `/new`, `/clear` | 새 대화 시작(`/clear`는 화면도 지움) |
| `/resume`, `/fork` | 저장된 대화 이어 가기, 대화 분기 |
| `/mcp` | 연결된 MCP 도구 목록 |
| `/skills`, `/plugins`, `/apps` | 스킬, 플러그인, 앱(커넥터) 둘러보기 |
| `/hooks` | 훅 보기·승인·끄기 |
| `/agent`(=`/subagents`) | 서브에이전트 스레드 전환 |
| `/goal` | 긴 작업의 목표를 저장해 두고 추적 |
| `/memories` | 메모리 사용 여부 설정 |
| `/import` | Claude Code·Cursor 설정 가져오기 |
| `/approve` | 자동 검토가 거절한 동작을 한 번 다시 허용 |
| `/fast` | Fast 속도 등급 켜기·끄기 |
| `/personality` | 말투 선택 |
| `/mention` | 파일 첨부 |
| `/side`(=`/btw`) | 본 대화를 방해하지 않는 곁가지 대화 |
| `/app` | 데스크톱 앱으로 이어 가기 |
| `/copy`, `/feedback`, `/logout`, `/quit`(=`/exit`) | 복사, 피드백 보내기, 로그아웃, 종료 |

- 데스크톱 앱과 IDE에는 따로 `/cloud`, `/local`, `/worktree`, `/cloud-environment`, `/reasoning`, `/project`, `/ide-context` 같은 명령이 있다. (같은 출처, IDE·앱 절)
- **config.toml 위치**: 사용자 설정은 `~/.codex/config.toml`, 프로젝트 설정은 `.codex/config.toml`(신뢰한 프로젝트에서만 읽음). 관리 시스템 설정은 `/etc/codex/config.toml`. CLI, IDE, 데스크톱 앱이 같은 설정을 쓴다. 우선순위는 CLI 플래그와 `-c`, 프로젝트, 프로필, 사용자, 클라우드 관리, 시스템, 기본값 순이다. 프로필 파일은 `~/.codex/<이름>.config.toml`에 두고 `--profile`로 고른다. (https://learn.chatgpt.com/docs/config-file/config-basic)
- 주요 키 예시 (https://learn.chatgpt.com/docs/config-file/config-basic , https://learn.chatgpt.com/docs/config-file/config-reference):
  ```toml
  model = "gpt-6-sol"
  model_reasoning_effort = "medium"
  approval_policy = "on-request"
  sandbox_mode = "workspace-write"
  web_search = "cached"
  [sandbox_workspace_write]
  network_access = false
  [mcp_servers.context7]
  command = "npx"
  args = ["-y", "@upstash/context7-mcp"]
  ```
- **추론 강도**(`model_reasoning_effort`): 모델이 지원하는 값 중에서 고른다. `low`, `medium`, `high`, `xhigh`, `max`, `ultra`. 화면 이름은 Light(CLI에서는 Low), Medium, High, Extra High, Max, Ultra다. Ultra는 서브에이전트로 일을 나눠 동시에 처리한다. 시작점으로 Sol은 Medium, Luna는 High, Astra는 Light(설정값 `low`)를 권한다. GPT-6 Luna는 Max까지만 되고 Ultra는 안 된다. 계획 모드 전용 추론 강도는 `plan_mode_reasoning_effort`로 따로 정한다. (https://learn.chatgpt.com/docs/models , https://learn.chatgpt.com/docs/config-file/config-reference)
- 실행할 때 모델 지정: `codex --model gpt-6-sol` 또는 `-m`. (https://learn.chatgpt.com/docs/models)

## 7. MCP 지원

- 데스크톱 앱, CLI, IDE 확장이 MCP 설정을 함께 쓴다. STDIO(로컬 프로세스)와 Streamable HTTP(원격 주소) 서버를 지원하고, Bearer 토큰과 OAuth 인증을 쓸 수 있다. (https://learn.chatgpt.com/docs/extend/mcp)
- 추가하는 법: `codex mcp add <이름> -- <실행 명령>`(예: `codex mcp add context7 -- npx -y @upstash/context7-mcp`). 목록은 `codex mcp list`, OAuth 로그인은 `codex mcp login <이름>`. 설정 파일에서는 `[mcp_servers.<이름>]` 표로 적는다. 대화 중에는 `/mcp`로 확인한다. 앱·IDE에서는 설정 > MCP servers > Add server로 추가한다. (같은 출처)
- **Codex를 MCP 서버로 쓰는 기능은 없어졌다**: `codex mcp-server` 명령과 `codex-mcp-server` 실행 파일이 제거됐다. 대신 JSON-RPC 방식의 **Codex 앱 서버**(`codex app-server`)를 쓰라고 안내하는데, 앱 서버는 MCP 서버가 아니고 실험 단계라 운영 환경용으로 지원하지 않는다. (https://learn.chatgpt.com/docs/mcp-server)
- ChatGPT 웹에서는 로컬 MCP 설정을 읽지 않는다. 플러그인에 들어 있는 원격 MCP 도구만 쓸 수 있다. (https://learn.chatgpt.com/docs/extend/mcp)

## 8. 클라우드 작업

- 시작 순서: chatgpt.com/codex에 로그인 → GitHub 또는 GitLab(베타) 연결 → 환경 설정(chatgpt.com/codex/settings/environments)에서 저장소별 환경 만들기 → 작업 지시 → 요약과 diff를 검토하고, 추가 지시를 하거나 **PR을 연다**. (https://learn.chatgpt.com/docs/cloud)
- 작업이 도는 방식: 컨테이너를 만들고 브랜치를 체크아웃 → 설정 스크립트(와 선택적으로 유지보수 스크립트) 실행 → 인터넷 설정 적용 → 에이전트가 명령 실행을 반복 → 답변과 diff 제시. 기본 이미지는 `universal`이고 언어 버전을 고정할 수 있다. 컨테이너는 최대 12시간 캐시된다. (https://learn.chatgpt.com/docs/environments/cloud-environment)
- 환경 변수는 작업 내내 쓸 수 있다. 시크릿은 **설정 스크립트에서만** 쓰이고 에이전트 단계에 들어가기 전에 지워진다. (같은 출처)
- **동시 실행**: 작업마다 별도 환경에서 병렬로 돌리고, 여러 시도를 비교할 수 있다. (https://learn.chatgpt.com/docs/cloud)
- **인터넷 접근**: 에이전트 단계는 기본으로 막혀 있다. 환경마다 Off/On을 고르고, On이면 도메인 허용 목록(None / Common dependencies / All)과 허용할 HTTP 메서드(GET·HEAD·OPTIONS만 허용 가능)를 정한다. 프롬프트 인젝션과 유출 위험을 경고한다. (https://learn.chatgpt.com/docs/cloud/internet-access)
- CLI에서 쓰기: `codex cloud`(작업 선택 화면), `codex cloud exec`(작업 제출), `codex cloud list`, `codex apply`(클라우드 결과 diff를 로컬에 적용). (https://learn.chatgpt.com/docs/developer-commands?surface=cli)
- 클라우드 작업 모델: ChatGPT 요금제에서는 **GPT-5.6 Sol**을 쓰고 사용자가 기본 모델을 바꿀 수 없다. (https://learn.chatgpt.com/docs/pricing , https://learn.chatgpt.com/docs/models)
- Business·Enterprise는 환경 캐시를 워크스페이스 사용자끼리 공유한다. (https://learn.chatgpt.com/docs/environments/cloud-environment)

## 9. GitHub 코드 리뷰

- 켜는 법: Codex cloud 설정 → Codex settings의 코드 리뷰 화면(chatgpt.com/codex/settings/code-review)에서 저장소의 **Code review**를 켠다. 저장소 push 또는 admin 권한이 필요하다. (https://learn.chatgpt.com/docs/third-party/github)
- 수동 요청: PR 댓글에 `@codex review`. Codex가 👀 반응을 달고 리뷰를 올린다. GitHub에는 P0·P1 이슈만 표시한다. 초점을 정하려면 `@codex review for issues in the database migration`처럼 쓴다. (같은 출처)
- 자동 리뷰: 같은 설정 화면에서 **Automatic reviews**를 켜면 새 PR마다 리뷰한다. (같은 출처)
- 리뷰 규칙은 AGENTS.md의 `## Code Review Rules` 섹션에 적는다. (같은 출처)
- 고치기와 다른 작업: `@codex fix the P1 issue`처럼 review 말고 다른 말을 붙여 `@codex`를 부르면 PR을 맥락으로 클라우드 작업을 시작한다. (같은 출처)
- 보안 리뷰(연구 프리뷰): `@codex security review`. (같은 출처)
- 로컬 리뷰: CLI의 `/review`나 `codex review --uncommitted` / `--base <브랜치>` / `--commit <SHA>`. (https://learn.chatgpt.com/docs/developer-commands?surface=cli)
- GitLab MR 리뷰도 베타로 지원한다. (https://learn.chatgpt.com/docs/third-party/gitlab.md)

## 10. 자동화

- **`codex exec`**(줄여서 `codex e`): 대화 없이 한 번 실행하고 끝낸다. 진행 상황은 stderr로, 최종 답만 stdout으로 나온다. **기본은 read-only 샌드박스**라서 수정을 허용하려면 `--sandbox workspace-write`를 붙인다. `--full-auto`는 사용 중단 예정이다. 주요 옵션은 `--json`(JSONL 이벤트), `-o/--output-last-message <파일>`, `--output-schema <schema.json>`, `--ephemeral`(세션 기록 안 남김). `codex exec resume --last`로 이어서 실행한다. (https://learn.chatgpt.com/docs/non-interactive-mode)
- CI 인증: API 키를 권장한다. 한 번 실행할 때만 `CODEX_API_KEY=... codex exec ...`로 넘긴다. 저장소 코드를 실행하는 잡에 `OPENAI_API_KEY`를 잡 전체 환경 변수로 두지 말라고 경고한다. (같은 출처)
- **GitHub Action**: `openai/codex-action@v1`. 입력값은 `openai-api-key`, `prompt` 또는 `prompt-file`, `sandbox`, `model`, `effort`, `output-file`, `safety-strategy`(기본 `drop-sudo`)이고, `final-message`를 출력한다. Linux/macOS 러너에서 돌리고, Windows는 `safety-strategy: unsafe`가 필요하다. (https://learn.chatgpt.com/docs/github-action)
- **SDK**: TypeScript는 `npm install @openai/codex-sdk`(Node 18 이상, `new Codex().startThread().run(...)`). Python은 `pip install openai-codex`(Python 3.10 이상, 로컬 앱 서버를 JSON-RPC로 제어). (https://learn.chatgpt.com/docs/codex-sdk)
- **앱 서버**: 자체 클라이언트를 만들 때 쓰는 JSON-RPC 프로토콜. 실험 단계다. (https://learn.chatgpt.com/docs/app-server , https://learn.chatgpt.com/docs/mcp-server)
- 예약 작업: CLI에는 예약 관리 화면이 없다. ChatGPT 웹이나 데스크톱 앱의 **Scheduled**에서 만든다. (https://learn.chatgpt.com/docs/automations)

## 11. 현재 모델 (확인일 2026-09-27)

| 모델(설정값) | 용도 | 비고 | 출처 |
|---|---|---|---|
| GPT-6 Astra (`gpt-6-astra`) | 가장 어려운 장기 작업 | Codex cloud에서는 안 됨. Enterprise는 관리자가 켜야 함 | https://learn.chatgpt.com/docs/models |
| GPT-6 Sol (`gpt-6-sol`) | 일상 작업과 복잡한 코딩(현재 권장) | 2026-09-22 출시, 롤아웃 중 | https://learn.chatgpt.com/docs/models , https://learn.chatgpt.com/docs/whats-new |
| GPT-6 Luna (`gpt-6-luna`) | 명확하고 반복적인 작업, 대량 처리 | Free·Go에서도(데스크톱 앱) 롤아웃 중 | 같은 곳 |
| GPT-5.6 Sol / Terra / Luna | 이전 세대 | 롤아웃 기간 동안 계속 제공. 클라우드 작업은 GPT-5.6 Sol | https://learn.chatgpt.com/docs/pricing |
| GPT-5.5 | 이전 플래그십 | **2026-10-14 ChatGPT·Codex에서 종료**(API는 유지) | https://learn.chatgpt.com/docs/models |
| gpt-5.4, gpt-5.4-mini | — | ChatGPT 로그인 Codex에서 2026-08-31 종료 | 같은 곳 |
| gpt-5.2, gpt-5.3-codex | — | ChatGPT 로그인 Codex에서 사용 중단 | 같은 곳 |

- 원고에 모델 이름을 적을 때는 "집필 시점 기준"이라고 밝히라. 몇 주 사이에도 바뀌고 있다(9월에만 GPT-6 Sol·Luna 출시와 GPT-5.5 종료 예고가 있었다). (https://learn.chatgpt.com/docs/whats-new)
- 서로 어긋나는 점: 모델 페이지의 GPT-6 Sol 항목에는 Codex cloud 지원 여부 칸이 없다. 요금 페이지는 클라우드 작업이 GPT-5.6 Sol을 쓴다고 한다. → 클라우드 모델은 **확인 필요**. (https://learn.chatgpt.com/docs/models , https://learn.chatgpt.com/docs/pricing)

## 12. 공식 문서 주소 (확인일에 실제로 열린 것, HTTP 200)

- Codex 문서 입구: https://developers.openai.com/codex
- 문서 전체 목록(llms.txt): https://developers.openai.com/codex/llms.txt
- Codex CLI: https://learn.chatgpt.com/docs/codex/cli (옛 주소 https://developers.openai.com/codex/cli)
- IDE 확장: https://learn.chatgpt.com/docs/codex/ide (옛 주소 https://developers.openai.com/codex/ide)
- VS Code 마켓플레이스: https://marketplace.visualstudio.com/items?itemName=openai.chatgpt
- Codex cloud: https://learn.chatgpt.com/docs/cloud
- 요금·한도: https://learn.chatgpt.com/docs/pricing (옛 주소 https://developers.openai.com/codex/pricing)
- 로그인: https://learn.chatgpt.com/docs/auth
- 모델: https://learn.chatgpt.com/docs/models
- AGENTS.md: https://learn.chatgpt.com/docs/agent-configuration/agents-md , https://agents.md
- 권한·보안: https://learn.chatgpt.com/docs/agent-approvals-security
- 명령어 모음: https://learn.chatgpt.com/docs/developer-commands?surface=cli
- 설정: https://learn.chatgpt.com/docs/config-file/config-basic , https://learn.chatgpt.com/docs/config-file/config-reference
- MCP: https://learn.chatgpt.com/docs/extend/mcp
- 비대화 실행: https://learn.chatgpt.com/docs/non-interactive-mode
- GitHub 리뷰: https://learn.chatgpt.com/docs/third-party/github
- GitHub Action: https://learn.chatgpt.com/docs/github-action
- SDK: https://learn.chatgpt.com/docs/codex-sdk
- Windows: https://learn.chatgpt.com/docs/windows/windows-sandbox , https://learn.chatgpt.com/docs/windows/wsl
- 새 소식: https://learn.chatgpt.com/docs/whats-new , 변경 기록: https://learn.chatgpt.com/docs/changelog
- 다른 에이전트에서 가져오기: https://learn.chatgpt.com/docs/import
- 로그인이 필요하거나 자동 수집을 막아서 직접 열람하지 못한 주소 → **확인 필요**: https://chatgpt.com/codex , https://github.com/openai/codex (git clone은 됐고 웹 요청만 403), https://github.com/openai/codex-action

## 13. Claude Code ↔ Codex 대응표

Claude 쪽 이름은 이 문서에서 다시 확인하지 않았다. Claude 사실 확인표와 대조할 것.

| 항목 | Claude Code | Codex | Codex 출처 |
|---|---|---|---|
| 설치 | 공식 설치 스크립트 / npm | 설치 스크립트(`install.sh`/`install.ps1`), `npm i -g @openai/codex`, `brew install --cask codex` | https://learn.chatgpt.com/docs/codex/cli |
| 규칙 파일 | `CLAUDE.md`(사용자·프로젝트·하위 폴더) | `AGENTS.md`(+`AGENTS.override.md`), `~/.codex/AGENTS.md` | https://learn.chatgpt.com/docs/agent-configuration/agents-md |
| 규칙 초안 만들기 | `/init` | `/init` | https://learn.chatgpt.com/docs/developer-commands?surface=cli |
| 권한/승인 | 권한 모드, `settings.json`의 allow/deny 규칙 | `approval_policy`(on-request/never/granular) + `sandbox_mode`(read-only/workspace-write/danger-full-access), `/permissions`, 명령 규칙(execpolicy `.rules`) | https://learn.chatgpt.com/docs/agent-approvals-security , https://learn.chatgpt.com/docs/agent-configuration/rules.md |
| 자동 판단 모드 | auto 모드 | Auto-review(`approvals_reviewer = "auto_review"`, 앱 이름은 Approve for me) | https://learn.chatgpt.com/docs/permission-modes |
| 전부 허용 | `--dangerously-skip-permissions` | `--dangerously-bypass-approvals-and-sandbox`(`--yolo`) | https://learn.chatgpt.com/docs/agent-approvals-security |
| 계획 모드 | Plan mode(Shift+Tab) | `/plan`(Shift+Tab으로도 전환) | https://learn.chatgpt.com/docs/developer-commands?surface=cli |
| 훅 | Hooks(`settings.json`) | Hooks(`hooks.json` 또는 config.toml `[hooks]`). 이벤트: PreToolUse, PostToolUse, PermissionRequest, UserPromptSubmit, Stop, SessionStart, SessionEnd, SubagentStart/Stop, Pre/PostCompact, Interrupt | https://learn.chatgpt.com/docs/hooks |
| 서브에이전트 | Subagents(`.claude/agents/`) | Subagents, 사용자 정의 에이전트(`~/.codex/agents/`, `.codex/agents/*.toml`), `/agent` | https://learn.chatgpt.com/docs/agent-configuration/subagents |
| 스킬 | Skills | Skills(`$스킬이름`으로 호출), `/skills`, 플러그인 | https://learn.chatgpt.com/docs/skills-and-plugins |
| MCP | `claude mcp add`, `.mcp.json` | `codex mcp add`, `[mcp_servers.*]`, `/mcp` | https://learn.chatgpt.com/docs/extend/mcp |
| 자신을 MCP 서버로 | `claude mcp serve` | 제거됨. 앱 서버(실험 단계)로 대체 | https://learn.chatgpt.com/docs/mcp-server |
| 슬래시 명령 | `/model`, `/compact`, `/clear`, `/resume`, `/review` 등 | `/model`, `/compact`, `/clear`·`/new`, `/resume`, `/review`, `/status`, `/diff` 등 | https://learn.chatgpt.com/docs/developer-commands?surface=cli |
| 비대화 실행 | `claude -p` | `codex exec`(기본 read-only) | https://learn.chatgpt.com/docs/non-interactive-mode |
| SDK | Claude Agent SDK | Codex SDK(TS `@openai/codex-sdk`, Python `openai-codex`) | https://learn.chatgpt.com/docs/codex-sdk |
| 클라우드/원격 | Claude Code on the web, Remote Control | Codex cloud(chatgpt.com/codex), `codex cloud`, Codex Remote(모바일) | https://learn.chatgpt.com/docs/cloud , https://learn.chatgpt.com/docs/remote |
| GitHub 리뷰 | Claude Code GitHub Actions(`@claude`), Code Review | `@codex review`, Automatic reviews, `openai/codex-action@v1` | https://learn.chatgpt.com/docs/third-party/github , https://learn.chatgpt.com/docs/github-action |
| 되돌리기 | 체크포인트(`/rewind`, Esc 두 번) | Git 커밋 체크포인트 권장, 앱 리뷰 화면의 Revert. CLI에는 `/undo`가 없음 | https://learn.chatgpt.com/docs/codex/cli |
| 설정 파일 | `~/.claude/settings.json`, `.claude/settings.json` | `~/.codex/config.toml`, `.codex/config.toml` | https://learn.chatgpt.com/docs/config-file/config-basic |
| 설정 이전 | — | `/import`(Claude Code에서 가져오기) | https://learn.chatgpt.com/docs/import |

---

# 2부. ChatGPT

먼저 알아둘 것: ChatGPT는 2026년에 구조가 크게 바뀌었다. 지금은 **Chat**(대화)과 **Work**(결과물까지 맡기는 모드), **Codex**(개발)의 세 방식으로 나뉜다. 예전 기능 가운데 ChatGPT agent, Atlas, 캔버스, 커스텀 GPT는 없어졌거나 없어지는 중이다(아래 각 항목 참고). (https://learn.chatgpt.com/docs/use-chatgpt)

## 1. 요금제, 모델, 계정, 데이터 학습 설정

- 요금제 이름: Free, Go, Plus, Pro(5배·20배), Business, Enterprise, Edu. 가격은 1부 2절의 표를 볼 것. ChatGPT 전체 요금 페이지(chatgpt.com/pricing)는 403으로 열지 못했다 → 표시 가격 **확인 필요**. (https://learn.chatgpt.com/docs/pricing)
- 방식 선택: 질문과 대화는 Chat, 문서·덱·분석처럼 검토할 결과물이 필요하면 Work, 개발이면 Codex. 웹에서는 입력창 위의 전환기에서 Chat/Work를 고른다. Work는 웹에서는 클라우드에서 돌고, 데스크톱 앱에서는 "Work locally"(내 컴퓨터)와 "Cloud" 중에서 고를 수 있다. (https://learn.chatgpt.com/docs/use-chatgpt , https://learn.chatgpt.com/docs/get-started-with-work)
- 모델(Work·Codex): GPT-6 Astra, GPT-6 Sol, GPT-6 Luna. 입력창 아래의 모델·추론 조절 메뉴에서 고른다. 기본 프리셋은 Luna High, Sol Light(시작값), Sol Medium, Astra Light, Astra Medium, Astra Extra High다. GPT-6 Sol·Luna는 **Chat에서는 쓸 수 없다.** (https://learn.chatgpt.com/docs/models)
- 모델(Chat): Instant와 Thinking 계열이다. 검색 결과로는 현재 GPT-5.5 Instant와 GPT-5.5 Thinking이고, Plus·Pro에서 Instant가 Thinking으로 자동 전환되던 기능은 2026-09-14에 없어졌다. GPT-5.5는 2026-10-14에 ChatGPT에서 종료되는데 Chat 쪽 후속 모델이 무엇인지는 찾지 못했다 → **확인 필요**. (https://help.openai.com/en/articles/6825453-chatgpt-release-notes , https://help.openai.com/en/articles/9624314-model-release-notes — 둘 다 검색 요약으로만 확인)
- 계정 종류: 개인(Free~Pro)과 워크스페이스(Business, Enterprise, Edu). Business 이상은 **업무 데이터를 기본적으로 학습에 쓰지 않는다.** 기능표에서 Plus·Pro는 이 항목이 "unavailable"로 되어 있어 개인이 직접 꺼야 한다. (https://learn.chatgpt.com/docs/pricing)
- 개인의 학습 제외 설정: 설정 > 데이터 제어(Data Controls) > "모두를 위한 모델 개선(Improve the model for everyone)"을 끈다. 끄면 새 대화는 기록에 남지만 학습에는 쓰이지 않는다. **확인 필요**(도움말 본문은 403으로 막혀 검색 요약으로만 확인). (https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt)

## 2. 파일·이미지, 웹 검색, 딥 리서치

- 이미지 입력: 웹 입력창에 첨부하거나, 붙여 넣거나, 끌어다 놓는다. 이미지만 주지 말고 무엇을 볼지 적으라고 권한다. (https://learn.chatgpt.com/docs/image-inputs)
- 파일: Work에서 원본 파일을 첨부하고 분석이나 결과물 제작을 맡긴다. (https://learn.chatgpt.com/docs/artifacts-viewer) 업로드 용량·개수 한도는 공식 문서에서 찾지 못했다 → **확인 필요**.
- 웹 검색: ChatGPT에 자체 웹 검색 도구가 있다. 웹에서는 검색을 쓰면 검색 결과와 **출처 표시(citations)**가 대화에 나온다. 워크스페이스 설정으로 검색을 제한할 수 있다. 검색 결과는 신뢰할 수 없는 입력으로 다루라고 안내한다. (https://learn.chatgpt.com/docs/web-search)
- 딥 리서치: 웹에서는 Work 대화의 **+** 메뉴에서 **Deep research**를 고른다. 데스크톱 앱에서는 Work > Plugins > **Deep research 플러그인**으로 쓴다. 결과는 출처가 달린 보고서다. (https://learn.chatgpt.com/docs/web-search)
- 이미지 생성: Free 요금제에서는 안 된다. 사용량 한도를 3~5배 빠르게 쓴다. (https://learn.chatgpt.com/docs/pricing)

## 3. 프로젝트, 메모리, 임시 채팅, 맞춤 지침

- 프로젝트: 관련 대화, 파일, 지침, 출처를 한곳에 모은다. 프로젝트 지침은 그 안의 모든 대화에 적용된다. 한 프로젝트 안에 Chat 대화와 Work 대화를 함께 둘 수 있다. 웹 프로젝트는 내 컴퓨터 폴더에 직접 접근하지 않는다. 데스크톱 앱에는 로컬 폴더를 연결하는 "로컬 프로젝트"도 있다. (https://learn.chatgpt.com/docs/projects)
- 메모리: 웹은 ChatGPT 메모리(설정 > Personalization)를 쓰고, 로컬 Codex는 이와 별개인 로컬 메모리(`~/.codex/memories/`, `/memories`)를 쓴다. macOS 데스크톱에는 선택 기능인 Computer History(앱·웹 활동을 메모리와 타임라인으로 만드는 기능)가 있다. (https://learn.chatgpt.com/docs/customization/memories , https://learn.chatgpt.com/docs/personalize)
- 맞춤 지침: 설정 > Personalization에서 쓴다. 성격(Friendly / Pragmatic / None)도 여기서 고른다. Codex에서는 개인 지침이 전역 AGENTS.md에 저장된다. (https://learn.chatgpt.com/docs/personalize)
- 임시 채팅: 대화 기록에 남지 않고, 임시 상태인 동안은 모델 학습에 쓰이지 않는다. 안전을 위해 최대 30일 보관될 수 있다. 데스크톱 단축키는 macOS ⌘+⇧+N, Windows Ctrl+Shift+N이다. 기능 설명은 **확인 필요**(도움말은 검색 요약만 확인), 단축키는 공식 문서에서 확인. (https://help.openai.com/en/articles/8914046-temporary-chat-faq , https://learn.chatgpt.com/docs/reference/commands.md)

## 4. 캔버스(canvas) → 현재는 없음 (Claude 아티팩트 대응)

- 캔버스는 GPT-5.5 Instant/Thinking에서 빠졌다. 글쓰기와 코딩은 대화 안의 "writing blocks"와 "code blocks"로 대신한다(2026-05-28 공지). 레거시 모델로 한동안 쓸 수 있다고 한다. **확인 필요**(공식 릴리스 노트는 검색 요약으로만 확인. 공식 문서 전체 덤프에도 "canvas 편집" 기능 설명이 없다). (https://help.openai.com/en/articles/6825453-chatgpt-release-notes , https://learn.chatgpt.com/docs/llms-full.txt)
- Claude 아티팩트와 가까운 현재 기능:
  - **파일 미리보기와 주석 수정**: 데스크톱 앱에서 문서, 슬라이드, 시트, PDF, HTML을 대화 옆에서 미리 보고, 부분을 지정해 고쳐 달라고 한다. (https://learn.chatgpt.com/docs/artifacts-viewer)
  - **Sites**(공개 베타, Plus 이상): 웹사이트, 웹앱, 게임을 만들어 호스팅하고 공유한다. 배포 URL은 모두 실제 운영 배포다. (https://learn.chatgpt.com/docs/sites)
  - **Visualizations**(롤아웃 중): `@Visualize`로 차트, 지도, 다이어그램, 계산기 같은 인터랙티브 시각화를 만든다. (https://learn.chatgpt.com/docs/visualizations)
- Sites의 요금제 표기가 문서마다 다르다. Sites 페이지는 Plus·Pro에서 된다고 하고, 요금 페이지 기능표에는 Plus·Pro가 "unavailable"로 되어 있다 → **확인 필요**. (https://learn.chatgpt.com/docs/sites , https://learn.chatgpt.com/docs/pricing)

## 5. 문서·엑셀·PPT 파일 만들기

- ChatGPT Work는 **문서, 프레젠테이션, 스프레드시트, PDF**를 만들고, 검토하고, 다운로드하게 해 준다. 시트, 열, 차트, 슬라이드 구성과 확인 기준을 구체적으로 적으라고 권한다. (https://learn.chatgpt.com/docs/artifacts-viewer , https://learn.chatgpt.com/docs/use-chatgpt)
- 예시 작업: 8장짜리 발표 자료, 비교 스프레드시트, 반복 업데이트. (https://learn.chatgpt.com/docs/get-started-with-work)
- ChatGPT for Excel(Plus 이상)은 Codex와 사용량 한도를 함께 쓴다. (https://learn.chatgpt.com/docs/pricing)

## 6. 브라우저 조작 (Claude in Chrome 대응)

- **ChatGPT agent(에이전트 모드)는 없어졌고 Work로 합쳐졌다.** 날짜는 출처마다 다르다(2026년 7~8월). **확인 필요**. (https://help.openai.com/en/articles/11752874-chatgpt-agent — 검색 요약)
- **ChatGPT Atlas 브라우저는 종료됐다**(검색 결과 기준 2026-08-09). 브라우저 기능은 ChatGPT와 Codex로 옮겨졌다. **확인 필요**. (https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work — 검색 요약)
- 현재 기능 (공식 문서로 확인):
  - **Browser(내장 브라우저)**: ChatGPT 웹과 데스크톱 앱에서 웹사이트를 열어 조사하고 조작한다. 데스크톱 브라우저는 평소 쓰는 브라우저와 분리된 프로필을 쓰고, 필요하면 직접 로그인한다. `@Browser`로 부른다. CLI와 IDE에서는 안 된다. (https://learn.chatgpt.com/docs/browser)
  - **브라우저 확장**: 데스크톱 앱이 Chrome, Edge, Brave, Opera, Vivaldi의 이미 로그인된 탭을 읽고 조작한다. 사이드 채팅은 Chrome, Edge, Brave, Vivaldi에서 된다(Opera는 안 됨). → **Claude in Chrome과 가장 가깝다.** (https://learn.chatgpt.com/docs/chrome-extension)
  - **Computer Use**: 데스크톱 앱이 다른 데스크톱 앱을 조작한다(기능표상 "limited"). (https://learn.chatgpt.com/docs/computer-use , https://learn.chatgpt.com/docs/pricing)
- Operator라는 이름은 현재 공식 문서에 나오지 않는다.

## 7. 커스텀 GPT와 스킬 (Claude 스킬 대응)

- **스킬**이 있다. 작업 지침과 자료(템플릿, 예시, 스키마 등)를 묶은 것이고, ChatGPT와 Codex가 함께 쓴다. ChatGPT에서는 `@`, Codex에서는 `$`로 부른다. 만들 때는 `@skill-creator`(Codex는 `$skill-creator`)에게 맡긴다. (https://learn.chatgpt.com/docs/skills-and-plugins , https://learn.chatgpt.com/docs/build-skills)
- **플러그인**은 스킬, MCP 서버, 훅 등을 묶어 설치하는 단위다. ChatGPT와 Codex는 하나의 플러그인 디렉터리를 함께 쓴다. 웹, 데스크톱, 모바일, Codex CLI(`/plugins`)에서 되고 **IDE 확장에서는 안 된다.** (https://learn.chatgpt.com/docs/plugins)
- **커스텀 GPT는 플러그인으로 옮기는 중이고 곧 종료된다.** 옮기면 지침은 스킬로, 지식 파일은 참고 파일로 바뀐다. 커스텀 액션은 옮겨지지 않아 다시 만들어야 한다. 옮긴 원본 GPT는 읽기 전용이 된다. (https://learn.chatgpt.com/docs/migrate-custom-gpts)
  - 종료 날짜: 검색 결과 기준 2026-12-11(연기 승인을 받은 Enterprise는 2027-02-11), 새 GPT 만들기 중단은 2026-10-26 예정. 공식 문서에는 날짜가 없다 → **확인 필요**. (https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq — 검색 요약)

## 8. 연결 앱(커넥터·앱·MCP) (Claude 커넥터 대응)

- 지금은 **플러그인** 안의 앱/MCP 서버로 Google Drive, Gmail, Slack, GitHub, SharePoint 같은 서비스에 연결한다. 입력창에서 `@플러그인이름`으로 지정한다. 관리자 문서에서는 "app"과 "MCP server"를 같은 뜻으로 쓴다. (https://learn.chatgpt.com/docs/get-started-with-work , https://learn.chatgpt.com/docs/enterprise/apps-and-connectors)
- ChatGPT 웹은 플러그인에 들어 있는 원격 MCP 도구만 쓴다. 로컬 MCP 설정은 Codex 쪽 기능이다. (https://learn.chatgpt.com/docs/extend/mcp)
- 개발자 모드: 설정 > Security and login > **Developer mode**를 켜고 ChatGPT Plugins 화면에서 MCP 서버를 추가해 시험한다. 계정·워크스페이스 정책에 따라 없을 수 있다. (https://developers.openai.com/plugins/deploy/connect-chatgpt.md)
- Apps SDK는 이제 개발자 문서에서 **Plugins** 문서 묶음(MCP 서버 + 선택적 UI)으로 정리돼 있다. (https://developers.openai.com/plugins/llms.txt)
- "Connectors"는 기능표에서 Plus 이상에서 되고 API 키로는 안 된다고 표시돼 있다. (https://learn.chatgpt.com/docs/pricing)

## 9. 예약 작업과 알림

- **Scheduled tasks**: 반복 작업을 백그라운드에서 돌린다. 웹과 모바일에서는 Gmail(새 메일), Slack(채널 새 메시지), GitHub(PR 활동) 이벤트로 시작하는 작업도 된다. 관리는 **Scheduled** 화면에서 한다. 데스크톱 앱 작업은 로컬 프로젝트 폴더나 워크트리에서 돌 수 있지만 컴퓨터와 앱이 켜져 있어야 한다. CLI와 IDE에는 관리 화면이 없다. (https://learn.chatgpt.com/docs/automations)
- 알림: 데스크톱 앱은 턴 완료, 권한 요청, 질문 알림을 설정하고 Activity 화면(벨)에서 모아 본다. 웹은 설정 > Notifications에서 푸시, 이메일, SMS를 고른다. (https://learn.chatgpt.com/docs/notifications)

## 10. 팀 공유와 관리

- Business: SAML SSO, MFA, 사용자 관리, 클라우드에서 관리하는 설정 정책. Enterprise·Edu: RBAC와 사용자 정의 역할, SCIM, EKM, 도메인 확인, 데이터 보존·저장 위치 통제, 분석 대시보드와 Analytics API, Compliance API 감사 로그. (https://learn.chatgpt.com/docs/pricing)
- 플러그인 통제: 관리자가 워크스페이스 설정(chatgpt.com/admin/settings)과 Workspace apps(chatgpt.com/admin/ca)에서 쓸 수 있는 플러그인, MCP 서버, 동작 권한을 정한다. (https://learn.chatgpt.com/docs/enterprise/apps-and-connectors)
- GPT 공유: 관리자가 누가 GPT를 만들고 공유할 수 있는지(특정 사람, 그룹, 전체 워크스페이스), 액션이 접근할 수 있는 도메인을 정한다. GPT 종료 이후에는 플러그인 공유로 옮겨 간다. (https://learn.chatgpt.com/docs/enterprise/gpts-and-sharing , https://learn.chatgpt.com/docs/migrate-custom-gpts)
- 로컬 실행 통제: `requirements.toml`로 승인 정책과 샌드박스를 강제한다(예: `never`나 `danger-full-access` 금지). (https://learn.chatgpt.com/docs/config-file/config-basic)
- 관리 문서 입구: https://learn.chatgpt.com/docs/administration

## 11. OpenAI API 키와 Responses API

- 키 발급: 대시보드의 API Keys(platform.openai.com/api-keys)에서 새 비밀 키를 만들어 안전한 곳에 보관하고, 환경 변수 `OPENAI_API_KEY`로 등록한다(macOS/Linux는 `export`, Windows는 `setx`). (https://developers.openai.com/api/docs/quickstart)
- Responses API 기본형(JavaScript): `client.responses.create({ model: "gpt-6-astra", input: "..." })` → `response.output_text`. Python도 `client.responses.create(...)`로 같다. SDK는 `npm install openai` / `pip install openai`. (https://developers.openai.com/api/docs/quickstart)
- 사용량 등급(tier): 누적 결제액에 따라 자동으로 올라간다. Tier 1은 $5 결제 시 월 $100 한도이고, Tier 5는 $1,000 결제 시 월 $200,000 한도다. 한도는 조직 설정의 Limits 페이지(platform.openai.com/settings/organization/limits)에서 본다. (https://developers.openai.com/api/docs/guides/rate-limits)
- 지출 알림과 월 상한(hard limit) 설정: 검색 요약으로만 확인 → **확인 필요**. (https://help.openai.com/en/articles/6614457-troubleshooting-api-usage-and-spend-limits)
- Codex에 API 키를 쓰면 API 요금으로 과금되고 클라우드 기능은 못 쓴다. (https://learn.chatgpt.com/docs/pricing)
- platform.openai.com은 403으로 막혀 화면을 직접 확인하지 못했다. 메뉴 이름은 **확인 필요**.

## 12. Claude ↔ ChatGPT 대응표

Claude 쪽 이름은 이 문서에서 다시 확인하지 않았다. Claude 사실 확인표와 대조할 것.

| 기능 | Claude | ChatGPT(현재 이름) | ChatGPT 출처 |
|---|---|---|---|
| 요금제 | Free / Pro / Max / Team / Enterprise | Free / Go / Plus / Pro / Business / Enterprise / Edu | https://learn.chatgpt.com/docs/pricing |
| 모델 선택 | Opus / Sonnet / Haiku, 확장 사고 | Work·Codex: GPT-6 Astra/Sol/Luna + 추론 강도. Chat: Instant/Thinking(버전은 **확인 필요**) | https://learn.chatgpt.com/docs/models |
| 결과물까지 맡기는 모드 | Cowork / 에이전트형 작업 | **ChatGPT Work** | https://learn.chatgpt.com/docs/get-started-with-work |
| 학습 제외 | 개인정보 설정의 모델 개선 옵션 | Data Controls > Improve the model for everyone(**확인 필요**) | https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt |
| 웹 검색 | Web search | Web search(출처 표시) | https://learn.chatgpt.com/docs/web-search |
| 심층 조사 | Research | Deep research(Work의 + 메뉴 / 플러그인) | https://learn.chatgpt.com/docs/web-search |
| 프로젝트 | Projects | Projects | https://learn.chatgpt.com/docs/projects |
| 메모리 | Memory | Memory(Personalization), Codex 로컬 메모리 | https://learn.chatgpt.com/docs/customization/memories |
| 기록 안 남기는 대화 | 시크릿(incognito) 채팅 | 임시 채팅(Temporary chat) | https://learn.chatgpt.com/docs/reference/commands.md |
| 맞춤 지침 | 개인 설정 지침 / 프로젝트 지침 | Custom instructions / 프로젝트 지침 | https://learn.chatgpt.com/docs/personalize |
| 아티팩트 | Artifacts | 캔버스는 없어짐 → 파일 미리보기+주석, Sites, Visualizations | https://learn.chatgpt.com/docs/artifacts-viewer , https://learn.chatgpt.com/docs/sites |
| 파일 만들기 | 파일 생성(docx/xlsx/pptx/pdf) | Work에서 문서·프레젠테이션·스프레드시트·PDF 생성 | https://learn.chatgpt.com/docs/artifacts-viewer |
| 브라우저 조작 | Claude in Chrome | 브라우저 확장(Chrome·Edge 등), 내장 Browser, Computer Use | https://learn.chatgpt.com/docs/chrome-extension |
| 스킬 | Skills | Skills(`@`), Plugins | https://learn.chatgpt.com/docs/skills-and-plugins |
| 맞춤형 봇 | (해당 없음) / 프로젝트 | 커스텀 GPT(종료 예정, 플러그인으로 이전) | https://learn.chatgpt.com/docs/migrate-custom-gpts |
| 연결 | Connectors(MCP) | 플러그인 속 앱·MCP 서버, 개발자 모드 | https://learn.chatgpt.com/docs/plugins |
| 예약 작업 | 예약 작업 | Scheduled tasks(시간, 이벤트) | https://learn.chatgpt.com/docs/automations |
| 팀 관리 | Team/Enterprise 관리자 콘솔 | 워크스페이스 관리(RBAC, SSO, SCIM, 플러그인 통제) | https://learn.chatgpt.com/docs/administration |
| API | Anthropic Console·Messages API | platform.openai.com·Responses API | https://developers.openai.com/api/docs/quickstart |
| 데스크톱 앱 | Claude 데스크톱 | ChatGPT 데스크톱 앱(Chat/Work/Codex 통합) | https://learn.chatgpt.com/docs/app |

---

## 컴퓨터 사용 (Claude · ChatGPT)

AI가 화면을 스크린샷으로 보고 마우스·키보드로 데스크톱 앱을 직접 조작하는 기능이다. 두 회사 모두 "커넥터·플러그인 → 브라우저 → 화면 조작" 순으로, 화면 조작을 가장 마지막 수단으로 둔다.

### A. Claude (Anthropic)

- **이름과 상태**: 데스크톱 앱에서는 "computer use", 베타(리서치 프리뷰)다. Claude Desktop 앱의 Cowork와 Claude Code에서 쓴다. (https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork , https://code.claude.com/docs/en/desktop.md) (2026-09-27 확인)
- **Cowork 이름 변화**: 도움말 상단 공지에 "Claude Cowork는 이제 그냥 Claude"라고 되어 있다. Pro·Max부터 입력창의 "Chat/Cowork" 선택지가 사라지고 Claude가 알아서 답변인지 작업인지 정한다(점진 적용). 책 화면이 달라질 수 있다. (https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) (2026-09-27 확인)
- **지원 OS**: 데스크톱 앱은 macOS와 Windows. Claude Code CLI에서는 macOS만 된다. 문서는 macOS와 Windows만 적고 Linux는 언급하지 않는다(Linux 지원 여부 확인 필요). (https://code.claude.com/docs/en/desktop.md , https://code.claude.com/docs/en/computer-use.md) (2026-09-27 확인)
- **요금제**: Pro, Max만. Team과 Enterprise에서는 현재 쓸 수 없다. Claude Desktop 앱이 켜져 있고 컴퓨터가 깨어 있어야 한다. (https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) (2026-09-27 확인)
- **켜는 법**: ① claude.com/download에서 최신 데스크톱 앱으로 업데이트 → ② 설정 > 일반(Settings > General, "Desktop app" 아래)에서 **Computer use**(도움말 표기는 "Enable computer use") 토글을 켠다 → ③ macOS는 **손쉬운 사용(Accessibility)**과 **화면 기록(Screen Recording)** 권한을 준다. Windows는 토글만 켜면 바로 적용된다. 기본값은 꺼짐이다. 토글이 안 보이면 OS·요금제를 확인하고 앱을 재시작한다. (https://code.claude.com/docs/en/desktop.md , https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) (2026-09-27 확인)
- **CLI(Claude Code)에서 켜는 법**: `/mcp`에서 내장 MCP 서버 `computer-use`를 Enable한다(프로젝트별로 유지). 대화형 세션에서만 되고 `-p` 비대화형 모드에서는 안 된다. 한 번에 한 세션만 컴퓨터를 쓸 수 있다(잠금). (https://code.claude.com/docs/en/computer-use.md) (2026-09-27 확인)
- **앱별 승인**: 어떤 앱을 처음 쓸 때 "Allow for this session(이번 세션만 허용)" 또는 "Deny(거부)"를 묻는다. 승인은 그 세션 동안만 유효하다(Dispatch로 시작된 세션은 30분). (https://code.claude.com/docs/en/desktop.md) (2026-09-27 확인)
- **앱 종류별 권한 단계(바꿀 수 없음)**: (https://code.claude.com/docs/en/desktop.md) (2026-09-27 확인)
  - 보기만(View only): 브라우저, 주식 거래 플랫폼 — 스크린샷으로 보기만 한다.
  - 클릭만(Click only): 터미널, IDE — 클릭·스크롤만, 타이핑·단축키 불가.
  - 전체 제어(Full control): 그 밖의 모든 앱 — 클릭, 타이핑, 드래그, 단축키.
  - 터미널, Finder/파일 탐색기, 시스템 설정처럼 범위가 넓은 앱은 승인 창에 추가 경고가 뜬다(차단은 아님).
- **기본 차단 앱**: 투자·거래 플랫폼, 암호화폐 앱은 기본적으로 막혀 있다. 설정에서 **Denied apps(차단 앱 목록)**에 앱을 추가하면 묻지 않고 거부한다. 다만 허용한 앱에서 링크를 누르면 차단 앱(예: Chrome)이 열릴 수는 있다. (https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork , https://code.claude.com/docs/en/desktop.md) (2026-09-27 확인)
- **Claude가 하지 않도록 학습된 일**: 주식·투자 거래, 민감 정보 입력, 얼굴 이미지 수집. 송금, 파일 수정·삭제, 민감 데이터 처리 같은 위험 작업도 피하도록 학습돼 있다. 단, "완벽하지 않으니 민감 앱 차단을 대신하지 않는다"고 명시한다. (https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) (2026-09-27 확인)
- **작업 방식**: macOS 15 이상에서는 기본적으로 **백그라운드 창**에서 일해서 사용자가 계속 컴퓨터를 쓸 수 있다(포인터·키보드를 뺏지 않음). 전체 화면이 필요하면 세션마다 처음 한 번 묻는다. 화면을 직접 넘겨주려면 설정 > 일반의 "When Claude requests access to an app"을 "Full control"로 바꾼다. 그 밖의 경우 작업 중 다른 창을 숨기고 끝나면 되살린다("Unhide apps when Claude finishes" 설정). (https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork , https://code.claude.com/docs/en/desktop.md) (2026-09-27 확인)
- **멈추기**: CLI 기준으로 "Claude is using your computer · press Esc to stop" 알림이 뜨고, 어디서든 `Esc`를 누르면 즉시 멈춘다. 데스크톱 앱에서도 언제든 멈출 수 있다고 안내한다. (https://code.claude.com/docs/en/computer-use.md , https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) (2026-09-27 확인)
- **할 수 있는 일 예시**: 로컬 파일과 커넥터로 경쟁사 분석 보고서 만들기, 커넥터가 없는 사내 대시보드·전문 프로그램 조작, 폰 시뮬레이터로 앱 UX 점검. **한계**: 커넥터보다 느리고, 복잡한 다단계 작업은 다시 시켜야 할 때가 있다. (https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) (2026-09-27 확인)
- **Claude in Chrome과의 관계**: 도구 우선순위는 ① 커넥터(Gmail, Drive, Slack 등) → ② 브라우저(데스크톱 앱 내장 브라우저 또는 Claude in Chrome) → ③ 화면 조작(computer use). 컴퓨터 사용에서 브라우저 앱은 "보기만" 단계라서, 웹 작업은 브라우저 도구로 하도록 유도된다. 선호 브라우저는 설정 > Cowork > Preferred browser에서 고른다. (https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork , https://code.claude.com/docs/en/desktop.md , https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) (2026-09-27 확인)
- **Claude in Chrome 요약**: 모든 유료 요금제(Pro, Max, Team, Enterprise). Chrome 전용(다른 크로미움 브라우저·모바일 미지원). 권한 모드 3가지: Manually approve(매번 승인), Automatically approve(안전 검사 후 자동 진행, Cowork 사이드 패널 기본값), Skip all approvals(검사 없음). 모드와 상관없이 **구매·금융 거래, 계정 생성, 카드·신분증 정보 처리, 영구 삭제, 투자 거래, 이메일·웹 속 지시 수행**은 금지다. 권한 설정 변경, 민감 정보 입력은 명시적 승인이 필요하다. (https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide , https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) (2026-09-27 확인)
- **개발자용 API 도구**: 현재 이름은 **`computer_toolset_20260801`**(클라이언트 툴셋, 정식 출시 GA). `tools`에 `{"type": "computer_toolset_20260801"}` 하나를 넣으면 `screenshot`, `left_click`, `type`, `zoom` 등 17개 하위 도구가 생긴다. **베타 헤더가 필요 없다.** 실제 동작은 개발자가 준비한 환경(VM·컨테이너)에서 실행한다. 이전 버전 `computer_20251124`(베타 헤더 `anthropic-beta: computer-use-2025-11-24`)와 `computer_20250124`(`computer-use-2025-01-24`)는 옛 모델용으로 남아 있다. Claude 5.5 이후 모델은 Claude API·Google Cloud에서 툴셋만 받는다. 웹페이지 안에서만 하는 작업이면 별도의 "browser use tool"이 더 맞다. (https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) (2026-09-27 확인)

### B. ChatGPT (OpenAI)

- **이름과 위치**: ChatGPT 데스크톱 앱의 **Computer Use** 플러그인. **ChatGPT Work와 Codex**에서 쓴다(Chat 모드에서는 아님). macOS와 Windows 지원, "지원 지역에서" 제공. (https://learn.chatgpt.com/docs/computer-use) (2026-09-27 확인)
- **켜는 법**: 데스크톱 앱에서 ChatGPT를 고르고 전환기에서 **Work**로 바꾸거나 Codex를 연다 → **Plugins > Computer Use** → **Install plugin**(또는 **Enable**) → Computer Use 서버와 스킬 토글을 켜고 **Try now**. 이후 **Settings > Computer use**에서 앱 접근을 관리한다. macOS는 **화면 기록**과 **손쉬운 사용** 권한을 준다(시스템 설정에서 항목 이름은 "Codex Computer Use"). (https://learn.chatgpt.com/docs/computer-use) (2026-09-27 확인)
- **부르는 법**: 프롬프트에 `@Computer` 또는 `@앱이름`(예: `@Chrome`)을 넣거나 Computer Use를 쓰라고 말한다. 어려운 시각 판단 작업에는 GPT-6 Astra를 권한다. (https://learn.chatgpt.com/docs/computer-use) (2026-09-27 확인)
- **앱별 승인**: 작업 중 앱을 쓰기 전에 허락을 묻는다. **Always allow**를 고르면 다음부터 묻지 않고, 설정 > Computer Use의 **Always-allowed apps**에서 뺄 수 있다. 민감하거나 방해가 되는 동작 전에도 물을 수 있다. OS 권한(화면 기록·손쉬운 사용)과 ChatGPT 앱 승인은 별개다. (https://learn.chatgpt.com/docs/computer-use) (2026-09-27 확인)
- **못 하는 일**: 터미널 앱과 ChatGPT 자신은 조작하지 못한다(보안 정책 우회 방지). 관리자 인증이나 컴퓨터의 보안·개인정보 권한 요청 창 승인도 못 한다. (https://learn.chatgpt.com/docs/computer-use) (2026-09-27 확인)
- **OS별 차이**: Windows는 **전면에서만** 동작해 작업 중 포인터와 키보드를 가져간다(가상 머신이나 다른 기기 사용 권장). macOS는 범위가 정해진 작업을 백그라운드에서 돌릴 수 있고, 선택 기능 **Locked use**(설정에서 켜면 Mac이 잠긴 뒤에도 연결된 기기에서 시킨 작업을 수행, 로컬 입력이 감지되면 다시 잠금)가 있다. (https://learn.chatgpt.com/docs/computer-use) (2026-09-27 확인)
- **요금제**: 기능표에서 Plus, Pro, Business, Enterprise 모두 "limited"이고 각주는 "특정 지역으로 제한"이다. Free·Go 제공 여부는 표에 없다 → **확인 필요**. 한국이 지원 지역인지 공식 문서에서 찾지 못했다 → **확인 필요**. (https://learn.chatgpt.com/docs/pricing , https://learn.chatgpt.com/docs/computer-use) (2026-09-27 확인)
- **관리자 통제**: 워크스페이스 관리자가 쓸 수 있는 앱과 승인 저장 여부를 제한할 수 있다. `requirements.toml`의 `[features].computer_use = false`로 끄고, `allow_locked_computer_use = false`로 Locked use를 막는다. (https://learn.chatgpt.com/docs/computer-use , https://learn.chatgpt.com/docs/enterprise/managed-configuration) (2026-09-27 확인)
- **내장 Browser·브라우저 확장과의 관계**: 모두 설정 > **Computer Use** 화면에서 관리한다. ① **내장 Browser**(`@Browser`): 데스크톱 앱에 자동 설치되고, "Computer Use in the browser"로 페이지를 열고 클릭·입력한다. 사이트마다 먼저 묻고, 제출·구매·권한 변경·삭제 같은 민감한 동작 전에 확인을 받는다. 파일 업로드는 자동화하지 못한다. ② **브라우저 확장**(Chrome, Edge, Brave, Opera, Vivaldi): 이미 로그인된 내 브라우저를 조작하고, Manage에서 허용·차단 사이트 목록을 관리한다. "Allow for all sites"는 위험도 높음 표시. ③ **Computer Use**: 브라우저 밖의 데스크톱 앱까지 조작. 로컬 웹앱 점검은 내장 Browser를 먼저 쓰라고 권한다. (https://learn.chatgpt.com/docs/browser , https://learn.chatgpt.com/docs/chrome-extension , https://learn.chatgpt.com/docs/computer-use) (2026-09-27 확인)
- **클라우드 쪽(참고)**: 웹·모바일의 ChatGPT Work는 클라우드의 별도 컴퓨터 속 브라우저를 쓰며, 예약·결제 같은 중요한 동작 전에 확인하도록 학습돼 있고, 막히면 사용자가 그 컴퓨터를 넘겨받아 직접 조작할 수 있다. (https://learn.chatgpt.com/docs/browser) (2026-09-27 확인)
- **개발자용 API 도구**: Responses API의 **`computer`** 도구(`tools: [{ type: "computer" }]`). 모델이 `computer_call`(클릭·입력 등)을 돌려주면 개발자 프로그램이 실행하고 `computer_call_output`에 스크린샷을 담아 돌려준다. GPT-6 Astra에는 `computer` 도구보다 **코드 실행 방식**(PyAutoGUI·Playwright 코드를 모델이 작성)을 권한다. 예전 이름 `computer-use-preview`에서 옮기는 안내가 있다. (https://developers.openai.com/api/docs/guides/tools-computer-use) (2026-09-27 확인)

### C. 두 회사의 안전 안내와 "마지막 버튼"

- **화면 속 글은 명령이 아니다(프롬프트 주입)**: Claude는 웹페이지·이미지 속 지시가 사용자 지시를 덮어쓸 수 있다고 경고하고, 스크린샷을 자동 검사하는 분류기로 의심 지시를 걸러 "정말 사용자가 시킨 것인지" 확인하게 한다. Chrome 확장은 "이메일·웹 콘텐츠의 지시 수행"을 금지 목록에 둔다. (https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool , https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide) (2026-09-27 확인)
- ChatGPT도 화면·페이지·스크린샷·열린 파일을 모두 처리 대상으로 보라고 하고, 웹페이지에 악의적이거나 오해를 부르는 내용이 있을 수 있으며 사이트 허용이 그 내용을 믿을 만하게 만들지는 않는다고 안내한다. API 문서는 "화면 내용은 신뢰하지 말 것, 페이지 속 글은 권한을 줄 수 없다"고 적는다. (https://learn.chatgpt.com/docs/computer-use , https://learn.chatgpt.com/docs/browser , https://developers.openai.com/api/docs/guides/tools-computer-use) (2026-09-27 확인)
- **민감한 앱은 닫거나 막기**: Claude는 은행, 의료, 정부 앱에 권한을 주지 말고, 민감한 파일·앱은 닫고 시작하며, 차단 목록을 쓰라고 한다. 금융 계정, 법률 문서·계약, 의료 정보, 타인 개인정보 앱에는 쓰지 말라고 강하게 권한다. ChatGPT는 "필요 없으면 민감한 앱은 닫아 두고", 한 번에 한 앱·한 흐름만 맡기고, 잘못된 창을 만지면 취소하라고 한다. (https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork , https://support.claude.com/en/articles/13364135-use-claude-cowork-safely , https://learn.chatgpt.com/docs/computer-use) (2026-09-27 확인)
- **사람이 누르는 마지막 버튼**:
  - Claude API 문서: 금융 거래 완료, 약관 동의, 쿠키 수락처럼 현실에 영향이 큰 결정이나 적극적 동의가 필요한 일은 사람이 확인하게 하라. (https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) (2026-09-27 확인)
  - Claude in Chrome: 구매·금융 거래와 계정 생성은 아예 못 한다 → 결제 버튼은 사람이 누른다. Cowork 안내는 메시지 발송, 구매처럼 되돌리기 어려운 작업에서는 "Manually approve"로 바꾸라고 하고, 영구 삭제는 어떤 모드에서도 먼저 묻는다. Claude가 한 행동(보낸 메시지, 구매, computer use 동작 포함)의 책임은 사용자에게 있다. (https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide , https://support.claude.com/en/articles/13364135-use-claude-cowork-safely) (2026-09-27 확인)
  - ChatGPT: 계정, 보안, 개인정보, 네트워크, **결제**, 자격 증명 관련 설정에서는 자리를 지키라고 하고, 비밀번호 같은 비밀 정보가 필요한 작업은 사람이 각 단계를 승인할 수 있을 때만 하라고 한다. 브라우저에서는 제출·구매·권한 변경·삭제 전에 확인을 받는다. API 문서는 구매, 데이터 전송(민감 정보를 폼에 입력하는 것 포함), 되돌릴 수 없는 변경은 사용자가 통제하게 하라고 한다. (https://learn.chatgpt.com/docs/computer-use , https://learn.chatgpt.com/docs/browser , https://developers.openai.com/api/docs/guides/tools-computer-use) (2026-09-27 확인)
  - "로그인된 계정으로 누른 클릭·제출은 사이트가 내 행동으로 본다"(ChatGPT). (https://learn.chatgpt.com/docs/computer-use) (2026-09-27 확인)

### D. 비교표

| 항목 | Claude | ChatGPT |
|---|---|---|
| 기능 이름 | computer use (베타) | Computer Use (플러그인) |
| 쓰는 곳 | Claude Desktop의 Cowork(이제 "Claude")·Claude Code, Claude Code CLI | ChatGPT 데스크톱 앱의 Work·Codex |
| 지원 OS | macOS, Windows (CLI는 macOS만) | macOS, Windows |
| 요금제 | Pro, Max만 (Team·Enterprise 불가) | Plus·Pro·Business·Enterprise "limited"(지역 제한). Free·Go와 한국 지원 여부 **확인 필요** |
| 켜는 법 | 설정 > 일반 > Computer use 토글 | Plugins > Computer Use 설치 → 서버·스킬 토글 |
| macOS 권한 | 손쉬운 사용 + 화면 기록 | 화면 기록 + 손쉬운 사용 |
| 앱 승인 | 앱마다 "이번 세션만 허용/거부" (저장 안 됨) | 앱마다 허락, "Always allow" 저장 가능 |
| 앱별 제한 | 브라우저·거래 플랫폼 보기만, 터미널·IDE 클릭만, 투자·암호화폐 앱 기본 차단, 차단 목록 | 터미널·ChatGPT 자신 조작 불가, 관리자 인증·보안 권한 창 승인 불가 |
| 사용자가 계속 컴퓨터 쓰기 | macOS 15 이상 백그라운드 기본 | macOS 백그라운드 가능, Windows는 전면 점유 |
| 브라우저 작업 | 내장 브라우저 또는 Claude in Chrome(Chrome 전용) | 내장 Browser 또는 브라우저 확장(Chrome·Edge·Brave·Opera·Vivaldi) |
| 결제·구매 | Chrome 확장에서는 금지, 사람에게 확인 권고 | 구매·결제 전 확인, 결제 설정 시 자리 지키기 |
| API 도구 | `computer_toolset_20260801` (베타 헤더 불필요, 옛 `computer_20251124`는 베타 헤더 필요) | Responses API `computer` 도구 (코드 실행 방식 권장) |
