# O/I Scout — 신규 혁신 과제 발굴 AI Agent

SK이노베이션 계열사의 외부 동향을 수집·정제하여 O/I(Operation Improvement) 과제를
발굴·평가·제안하는 파이프라인과 대시보드입니다. `docs/pipeline.md`의 파이프라인 설계를
실제 개발 환경으로 옮긴 저장소입니다.

## 구성

```
suniC/
├── frontend/     Vite + React 대시보드 (데모 JSX를 컴포넌트 단위로 분리)
├── backend/      FastAPI + SQLite. 파밍 → 지식기반 → 발굴 → 평가 → 제안 파이프라인
├── docs/         파이프라인 설계 문서, 원본 데모(참고용)
└── README.md
```

## 파이프라인 (docs/pipeline.md 대응)

| 단계 | 백엔드 모듈 | 설명 |
|------|-------------|------|
| 지식 파밍 | `backend/app/pipeline/farming/` | 크롤링 · PDF · LLM · 엔티티 추출 |
| 지식 기반 | `backend/app/pipeline/knowledge/` | business · process · innovation · technology · KPI/Benefit |
| 과제 발굴 | `backend/app/pipeline/discovery/` | Business / Technology / Opportunity / Benchmark |
| 과제 평가 | `backend/app/pipeline/evaluation/` | Impact · Feasibility · ROI · 우선순위 |
| 제안서 생성 | `backend/app/pipeline/proposal/` | 과제 정의 · 기대효과 · 추진 logic · 투자 |

## 빠른 시작

### 1) 백엔드 (Python 3.11+)

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate            # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env            # ANTHROPIC_API_KEY 입력
python -m app.db.seed             # SQLite 초기화 + 데모 데이터 주입
uvicorn app.main:app --reload     # http://localhost:8000
```
For Linux:

```bash
cd ~/sunic/SuniC_team7/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
nano .env                          # ANTHROPIC_API_KEY 입력, Ctrl+O → Enter → Ctrl+X
python -m app.db.seed
uvicorn app.main:app --reload      # http://localhost:8000
```
### 2) 프론트엔드 (Node 18+)

```bash
cd frontend
npm install
copy .env.example .env            # VITE_API_BASE 확인 (기본 http://localhost:8000)
npm run dev                       # http://localhost:5173
```
For Linux:

```bash
cd ~/sunic/SuniC_team7/frontend
npm install
cp .env.example .env
npm run dev                        # http://localhost:5173
```

프론트엔드는 백엔드가 떠 있으면 SQLite에 과제를 저장하고, 없으면 브라우저
localStorage로 폴백해 단독으로도 화면을 확인할 수 있습니다.

## 원본 데모

최초 단일 파일 데모는 `docs/demo-original.jsx`로 보존했습니다. 현재 프론트엔드는
이 파일을 `data / lib / components / views`로 분리한 것입니다.
