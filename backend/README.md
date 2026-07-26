# O/I Scout — 백엔드

FastAPI + SQLite. `docs/pipeline.md`의 파이프라인을 모듈 구조로 구현합니다.

```
app/
├── main.py              FastAPI 진입점 + 라우터 등록
├── config.py            환경변수 설정
├── models.py            Pydantic 입출력 스키마
├── db/
│   ├── database.py      SQLite 커넥션 헬퍼
│   ├── schema.sql       테이블 정의 (지식기반 + 과제기록)
│   └── seed.py          스키마 생성 + 데모 데이터 주입
├── api/
│   ├── feed.py          GET /api/feed          외부 동향 조회
│   ├── tasks.py         GET/POST/DELETE /api/tasks   과제 기록 CRUD
│   └── discovery.py     POST /api/discovery/generate 과제 발굴
└── pipeline/
    ├── farming/         지식 파밍: 크롤링·PDF·LLM·엔티티 (스텁)
    ├── knowledge/       지식 기반: business·process·innovation·technology·KPI
    ├── discovery/       과제 발굴 agent (Claude 호출)
    ├── evaluation/      과제 평가 agent: Impact·Feasibility·ROI·우선순위 (스텁)
    └── proposal/        제안서 생성 agent (스텁)
```

## 실행

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env               # ANTHROPIC_API_KEY 입력
python -m app.db.seed                # DB 초기화 + 데모 데이터
uvicorn app.main:app --reload        # http://localhost:8000  (docs: /docs)
```

## 지식 파밍 (크롤러) — 구현됨

watchlist(`pipeline/farming/watchlist.py`)의 peer 기업/토픽을 대상으로 DART · SEC · 뉴스를
크롤해 `feed_item` 에 적재합니다.

```bash
# 전체 소스 크롤 → DB 적재 (최근 30일)
python -m app.pipeline.farming.run

python -m app.pipeline.farming.run --days 14           # 기간 지정
python -m app.pipeline.farming.run --source news --dry  # 특정 소스만, 적재 없이 미리보기
python -m app.pipeline.farming.run --source sec         # SEC만
```

| 소스 | 모듈 | 키 | 비고 |
|------|------|----|------|
| DART | `dart.py` | `DART_API_KEY` 필요 | [opendart.fss.or.kr](https://opendart.fss.or.kr) 무료 발급. corpCode.xml 로 명칭→고유번호 자동 매핑 |
| SEC  | `sec.py`  | `SEC_USER_AGENT` 필요 | 연락처 포함 UA만 있으면 됨(무료). 10-K/10-Q/8-K 등 |
| 뉴스 | `news.py` | 불필요 | Google News RSS. 운영 시 정식 뉴스 API로 교체 |

키가 없는 소스는 조용히 건너뛰므로 일부만으로도 부분 동작합니다.
요약(`summary`)은 아직 naive(본문/제목 절삭)이며, `pdf.py`/`llm.py`/`entity.py` 구현 시 고도화됩니다.

## 파이프라인 단계별 개발 순서

1. ✅ `pipeline/farming/*` — DART · SEC · 뉴스 크롤러로 `feed_item` 채우기 (**구현**)
2. `pipeline/farming/{pdf,llm,entity}.py` — 원문 본문 추출 · LLM 요약 · 정밀 태깅
3. `pipeline/knowledge/*` — 파밍 결과를 business/process/innovation/technology/KPI로 정제해 `kb_*` 적재
4. ✅ `pipeline/discovery/agent.py` — 지식기반을 근거로 과제 후보 생성 (**구현**)
5. `pipeline/evaluation/*` — Impact/Feasibility/ROI 산정 + 우선순위
6. `pipeline/proposal/*` — 제안서(정의·기대효과·추진 logic·투자) 생성
