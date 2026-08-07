# O/I 과제 발굴 서비스 — 인수인계서 / 프로젝트 개요

> 이 문서 하나로 프로젝트 맥락을 파악하고 다른 대화·담당자가 이어서 작업할 수 있도록 정리했습니다.
> 최종 갱신: 2026-08 기준 · 작성 맥락: 프론트 담당자 관점 + 전체 아키텍처

---

## 1. 서비스 한 줄 정의

**SK이노베이션 O/I추진단**을 위한 도구. 경쟁사 IR·공시·전문지·뉴스 등 **외부 벤치마킹을 자동 수집·요약**해, 계열사(OC)별 **O/I(Operation Improvement) 과제 후보**를 발굴·평가하고 제안서·리포팅까지 연결한다.
핵심 원칙: **확장 투자형보다 비용·효율·수익성 개선 과제를 우선**한다.

### 서비스 명칭 (확정 전)
- 코드/초기 데모: **O/I Scout**
- 최신 데모: **O/I Spark**
- "O/I"가 직무명 느낌이라 전면에서 빼고 **밤하늘·별(spark→star) 컨셉**으로 리브랜딩 논의 중.
  후보: **Aster**(별+asterisk ✳, 1순위 추천) · **Nova**(빛남) · **Constella**(사례별→과제 별자리). 미확정.

---

## 2. 기술 스택 & 아키텍처

| 영역 | 스택 | 상태 |
|------|------|------|
| 프론트엔드 | **Vite + React** | O/I Scout 분리본 존재. 최신 O/I Spark HTML 데모를 React로 재구현 예정 |
| 백엔드 | **Python FastAPI** | 파이프라인 모듈 구조 |
| DB | **SQLite** (로컬) | 나중에 Postgres 전환 여지 |
| LLM | **Anthropic Claude** | 발굴/평가/제안에 사용 |
| 저장소 | GitHub `Qqldir/SuniC_team7` | |

**데이터 파이프라인(10단계)**
`① 트리거 → ② 소스 조합 → ③ 원문 수집(크롤) → ④ 본문 추출 → ⑤ LLM 요약·태깅 → ⑥ 지식기반 DB → ⑦ 과제 발굴 agent(Claude) → ⑧ 기대효과 Logic → ⑨ 평가·Top N → ⑩ 활용(목록·CSV / 프롬프트 내보내기 / AI Reporting: Outlook·Teams)`

백엔드 폴더: `backend/app/pipeline/{farming, knowledge, discovery, evaluation, proposal}`

---

## 3. 레포 & 실행

- **로컬 경로**: `C:\Users\삐약이\suniC`
- **원격**: https://github.com/Qqldir/SuniC_team7.git
- **주요 폴더**
  ```
  suniC/
  ├─ frontend/        Vite+React (O/I Scout 분리본: data·lib·components·views)
  ├─ backend/         FastAPI + SQLite
  │  └─ app/
  │     ├─ api/       feed·tasks·discovery·cases  (+브랜치: evaluation·proposal)
  │     ├─ db/        schema.sql · seed.py · seed_data.py · database.py
  │     ├─ models.py  Pydantic 입출력 스키마
  │     ├─ config.py  환경변수
  │     └─ pipeline/  farming·knowledge·discovery·evaluation·proposal
  └─ docs/            pipeline.md · demo-original.jsx · 혁신사례_입력양식.xlsx · (이 문서)
  ```
- **환경변수** (`backend/.env`, 커밋 제외): `ANTHROPIC_API_KEY`, `DART_API_KEY`(없으면 DART skip), `SEC_USER_AGENT`(연락처 이메일), `OI_MODEL`
- **백엔드 실행**
  ```bash
  cd backend && python -m venv .venv && .venv\Scripts\activate
  pip install -r requirements.txt
  python -m app.db.seed          # DB 초기화 + 데모 데이터
  uvicorn app.main:app --reload  # http://localhost:8000/docs
  ```
- **크롤 실행**: `python -m app.pipeline.farming.run` (SEC·뉴스는 키 없이 동작, DART는 키 필요)
- **프론트**: 이 PC에 **Node 미설치** → 설치 후 `cd frontend && npm install && npm run dev`
- `.gitignore`: `*.db`, `backend/data/`, `backend/.env`, `.claude/settings.local.json` 제외

---

## 4. Git 현황

```
main ── 35254e0 Init(데모 분리·백엔드·크롤러)
     ── f5196b3 혁신 사례 DB 3층
     ── 696d610 프론트 문구 수정            ← 프론트 마지막 코드
     ── 5a147f9 · 72eab11 README 정리       ← 팀원(코드 변화 아님)

feat/evaluation-agent ── d924255 과제 평가·제안서 생성 agent 구현   ← ⚠ 아직 main 미머지
```

---

## 5. 구현 상태 (노드별)

| # | 단계 | 상태 | 위치 |
|---|------|------|------|
| 3 | 원문 수집(크롤러) | ✅ 동작 확인(SEC·뉴스 라이브, DART는 키 필요) | `farming/{crawler,dart,sec,news,ingest,run,watchlist}.py` |
| 6 | 지식기반 DB | ✅ 스키마·seed·조회 | `db/schema.sql`, `knowledge/repository.py` |
| 7 | 과제 발굴 agent | ✅ Claude 호출 | `discovery/agent.py` |
| — | 혁신사례 3층 CRUD+검토 | ✅ | `api/cases.py`, `frontend .../CasesView.jsx` |
| 9 | 평가 agent(Impact·Feasibility·ROI·우선순위) | 🌿 **브랜치에 구현(미머지)** | `feat/evaluation-agent` |
| — | 제안서 생성 agent | 🌿 **브랜치에 구현(미머지)** | `feat/evaluation-agent` |
| 4·5 | 본문 추출 / LLM 요약·태깅 | ⬜ 스텁 | `farming/{pdf,llm,entity}.py` |
| — | kb_business/process/technology/kpi 적재 | ⬜ 표만 존재, 비어있음 | |
| 8 | **기대효과 Logic**(레버 산출식+현업 기준값) | ⬜ 미구현(별개 기능) | O/I Spark 데모 `LOGIC` 참고 |
| 1·2 | 트리거·소스관리 UI | ⬜ (watchlist는 코드 상수) | |
| 10 | AI Reporting 실발송(Outlook·Teams)·버전/재생성·업로드·권한 | ⬜ | |

> ⚠️ **프론트 담당자 기준 "실사용 가능"은 사실상 미완**입니다. 크롤러만 실제로 돌려봤고(③), 나머지는 스캐폴드/데모 수준. 상태 과대표기 주의.

---

## 6. `feat/evaluation-agent` 브랜치 상세 (팀원 구현)

우리 Init에서 스텁이던 `evaluation/`·`proposal/`을 채운 브랜치. **models.py는 append-only(기존 스키마 무변경)**.

- **평가 3단계**: `validator`(LLM 없는 결정적 게이트: 필수필드·근거환각·신선도·KPI·중복 → block/warn) → `scorer`(Claude 채점 Impact·Feasibility·ROI + grounding, 휴리스틱 폴백) → `priority`(가중합 임팩트40%·실현35%·ROI25% × 근거계수 → 0~100·A/B/C·Top N, **선정기준 투명 노출**)
- **제안서**: `generator`(3단계 추진안, **금액 안 지어냄→`(산정 필요)`**) + `renderer`(Markdown)
- **API**: `POST /api/evaluation/evaluate·/validate`, `GET /api/evaluation/criteria`, `POST /api/proposal/build·/markdown`
- 프론트 함의: 과제 목록/상세의 **순위·등급·사유**, AI Reporting의 **Top N 기준 문구**, 상세의 **제안서 내보내기**가 이 API에서 나온다.

---

## 7. 핵심 설계 원칙·결정 (합의된 것)

- **AI가 기대효과 금액을 지어내지 않는다** — 시스템은 레버별 산출식·필요 기준값 항목만 제시, 값은 현업이 입력.
- **근거 환각 차단** — 근거는 실제 수집 문서(`feed_item`)에 존재하는 것만 인용, 없는 id는 차단.
- **선정 기준 투명 노출** — Top N을 블랙박스 점수로 보여주지 않고 가중치·사유를 함께.
- **혁신사례 3층 구조** — `source_type`(manual/ai/auto) + `status`(approved/pending) : 사람 큐레이션 + AI 추출 검토 + 자동. 승인 워크플로.
- **데이터 형식은 사람이, 채우기는 프로그램·AI가, 검수는 사람이.**
- **LLM 단계별 분리 권장** — 요약=Haiku, 발굴·평가=Sonnet, 제안=Opus. 민감 내부데이터는 **엔터프라이즈 no-train / 국내 리전 / 온프렘** 정책 확인 필요.
- **레버 7종**: 정비/TA · 에너지비 · 물류비 · 수율 · 구매 · 간접비 · 운전자본.

---

## 8. 팀 구성 & 역할

- **개발 3 + 비개발 3.**
- 이 문서 소유자 = **프론트엔드 담당** (HTML 데모 → React 재구현).
- 백엔드/agent = 팀원 (evaluation·proposal 브랜치 등).
- 비개발 3 = 리서치·혁신사례 입력·피드백. 이들이 참여하려면 **공용 환경(배포/공용 DB)** 이 필요(현재 각자 로컬 SQLite라 미공유).

---

## 9. 산출물·참고 자료

- **회의 자료(파이프라인·DB 스키마·API 협의)**: Claude 아트팩트 (계약 협의용)
- **전체 흐름도**(가로 노드 + 노드별 상세, PNG/SVG 저장): Claude 아트팩트
- **엑셀 입력 양식**: `docs/혁신사례_입력양식.xlsx` (비개발자용 사례 수집)
- **파이프라인 원문 기획**: `docs/pipeline.md`
- **원본 데모(분리 전)**: `docs/demo-original.jsx`
- **최신 데모(O/I Spark)**: 프론트 담당 로컬 `Downloads/7월30일데모.html` — 6화면·레버 LOGIC·버전·소스관리 등 목표 기능 총집합 (⚠ 레포 미포함, 별도 공유 필요)

---

## 10. 다음 할 일

**프론트(담당자)** — HTML 데모 → React
1. Node 설치 → Vite+React → `react-router-dom`, `zustand`
2. 뼈대: CSS 이관 · 데이터/유틸 분리 · 라우팅 · 사이드바 레이아웃
3. 화면 순서: 목록 → 상세(기대효과 Logic) → 내보내기 → 리포팅 → 커스텀 위저드 → 관리자
4. `lib/api.js`: 목 데이터 → 백엔드 `fetch` 교체 (API 계약 선합의)

**백엔드/공통**
- `feat/evaluation-agent` **리뷰 후 머지**
- **기대효과 Logic**(레버 산출식+현업 입력) 신규 구현
- 소스관리·버전/재생성·내부자료 업로드·AI Reporting 실발송·권한
- farming `pdf/llm/entity` 채우기, `kb_*` 정제 적재
- **DB 스키마 + API 계약 확정** (신규 테이블: source·generation·task_effect_input·upload·setting·app_user)
- **공용 환경 배포**(6인 협업 전제)

---

## 11. 다른 대화에서 이어가는 법

새 대화에 이 문서를 붙여넣고, 로컬 경로(`C:\Users\삐약이\suniC`)와 함께
> "이 인수인계서 기준으로 O/I 과제 발굴 서비스 작업을 이어서 도와줘"
라고 요청하면 맥락이 복원됩니다. `feat/evaluation-agent` 브랜치는 별도 확인 필요.
