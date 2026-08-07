# O/I Scout — 신규 혁신 과제 발굴 AI Agent

SK이노베이션 계열사의 외부 동향을 수집·정제하여 O/I(Operation Improvement) 과제를
발굴·평가·제안하는 파이프라인과 대시보드입니다.

## 구성

```
SuniC_team7/
├── frontend/     로그인 랜딩(React) + 앱 화면(public/trendroom.html)
├── backend/      FastAPI + SQLite. 파밍 → 지식기반 → 발굴 → 평가 → 제안 파이프라인
├── docs/         백엔드 구조·지식 베이스 설계 문서
└── README.md
```

| 문서 | 내용 |
|---|---|
| `docs/backend-structure.md` | **백엔드 단일 출처.** 엔드포인트·테이블·주요 결정과 그 근거 |
| `docs/knowledge-base-flow.md` | 계열사 원본 DB → `backend/knowledge/` 빌드 절차(S0~S4) |
| `docs/llm-agent-knowledge-strategy.md` | 지식 베이스 설계 전략(위 두 문서가 §번호로 인용) |
| `backend/README.md` | 백엔드 실행·운영 안내 |

### 화면 구성

| 경로 | 내용 |
|------|------|
| `/login` | 로그인 랜딩 (React · `src/views/Login.jsx`) |
| `/trendroom.html` | 앱 본체 — 과제 제안 · 커스텀 생성 · 트렌드룸 · 프롬프트 내보내기 · AI Reporting · 관리자 |

`trendroom.html` 은 상수 대신 **`GET /api/bootstrap`** 한 번으로 화면 데이터를 모두 받고,
사용자가 바꾼 값(평가·기준값·산출식·발송 설정·인스트럭션)은 그때그때 API 로 저장합니다.
계정별로 분리 저장되므로 다시 로그인해도 작업하던 상태가 그대로 복원됩니다.

## 파이프라인

| 단계 | 백엔드 모듈 | 설명 |
|------|-------------|------|
| 지식 파밍 | `backend/app/pipeline/farming/` | DART·SEC·뉴스 크롤링 → LLM 요약·지표 추출 → `feed_item` |
| 지식 기반 | `backend/app/pipeline/knowledge/` | 파일 KB 검색(retriever) · 발굴 프롬프트 조립(prefetch) |
| 과제 발굴 | `backend/app/pipeline/discovery/` | 계열사별 LLM 발굴 → `proposal` 저장(persist) |
| 과제 평가 | `backend/app/pipeline/evaluation/` | 검증 · Impact/Feasibility/ROI 채점 · 우선순위 |
| 제안서 생성 | `backend/app/pipeline/proposal/` | 과제 정의 · 기대효과 · 추진 logic · 투자 (CLI) |

## 빠른 시작

### 1) 백엔드 (Python 3.11+)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate         # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env              # Windows: copy .env.example .env
python -m app.db.seed             # SQLite 초기화 + 화면 데이터 주입
python -m app.db.seed_users       # 로그인 계정 생성 (초기 비밀번호 1111)
uvicorn app.main:app --reload     # http://localhost:8000
```

`seed_users` 는 기본으로 `admin@sk.com` · `user1@sk.com` · `user2@sk.com` 을 만듭니다.
실제 사용자 목록은 인자로 넘기세요 — `python -m app.db.seed_users --file emails.txt`.

> 공개 저장소에 올라간 기본값입니다. 실제 배포 시에는 초기 비밀번호와
> `.env` 의 `OI_AUTH_SECRET`(예시 값이 `dev-insecure-secret-change-me`)을 반드시 바꾸세요.

### 2) 프론트엔드 (Node 18+)

```bash
cd frontend
npm install
cp .env.example .env              # Vite 프록시가 /api 를 보낼 대상 (기본 http://localhost:8000)
npm run dev                       # http://localhost:5173
```

Vite 가 `/api` 요청을 백엔드(8000)로 프록시하므로 CORS 설정 없이 바로 붙습니다.
`http://localhost:5173/login` 에서 시드 계정으로 로그인하면 앱 화면으로 넘어갑니다.

### 3) 한 프로세스로 띄우기 (데모·운영)

```bash
cd frontend && npm run build       # frontend/dist 생성
cd ../backend
OI_SERVE_FRONTEND=1 uvicorn app.main:app --port 8000
```

FastAPI 가 `frontend/dist` 를 함께 서빙해 `http://localhost:8000` 하나로 화면까지 뜹니다.
프론트를 고쳤으면 `npm run build` 를 다시 돌려야 반영됩니다.

## 주요 API

엔드포인트는 24개입니다. 전체 스펙은 서버를 띄운 뒤 `http://localhost:8000/docs`,
경로별 설명과 응답 계약은 `docs/backend-structure.md` 를 보세요.

| 엔드포인트 | 설명 |
|---|---|
| `POST /api/auth/login` · `GET /api/auth/me` | 로그인 / 세션 확인 (Bearer 토큰) |
| `GET /api/bootstrap` | 화면 초기 데이터 일괄 (OC · 레버 · 테마 · 근거자료 · 과제 · 소스 · 권한 · 사용자 상태) |
| `POST /api/proposals/regenerate` · `/custom` | 과제 재생성 / 커스텀 생성 — **비동기**. 작업 id 를 받아 `GET .../{job_id}` 로 폴링 |
| `PUT /api/proposals/{id}/feedback` · `/fields` · `/formula` | 별점·메모 · 기준값 · 산출식 저장 (계정별) |
| `POST /api/evaluation/run` · `GET /api/evaluation/criteria` | 저장된 과제 재평가(비동기) / 선정 기준 |
| `PUT /api/admin/instruction` · `POST /api/admin/uploads/file` · `/members` | 관리자 화면 (조회는 `/api/bootstrap` 이 담당) |
| `PUT /api/report/settings` · `POST /api/report/test` | AI Reporting 설정 |
| `GET /api/feed` | 파밍 결과 확인 (혁신 사례는 API 없이 시드로만 관리) |

## 데이터 출처

화면 초기 데이터는 `backend/app/db/seed_assets/trendroom.json` 에 있습니다. 이 파일은
`frontend/public/trendroom.html` 이 상수로 들고 있던 데모 데이터를 그대로 추출한 것이라
화면이 보여 주던 값과 1:1 로 일치합니다. 실서비스에서는 farming 파이프라인이 `feed_item`
(근거 자료)을, discovery 가 `proposal`(과제 제안)을 채웁니다.

계열사 지식 베이스(`backend/knowledge/`)는 빌드 결과물을 저장소에 포함합니다.
원본 DB 는 사내 자산이라 저장소에 없으므로, 클론한 환경에서는 재빌드할 수 없습니다
(절차는 `docs/knowledge-base-flow.md`).
