# O/I Scout — 백엔드

FastAPI + SQLite. 엔드포인트 27개(25 경로) · 테이블 32개 + 뷰 1개.
경로별 계약과 설계 결정의 근거는 [`../docs/backend-structure.md`](../docs/backend-structure.md) 에 있습니다.

```
app/
├── main.py              FastAPI 진입점 + 라우터 등록 (GET /api/health 포함)
├── config.py            환경변수 설정
├── models.py            Pydantic 입출력 스키마
├── store.py             화면 데이터 저장소 (프론트가 쓰던 상수를 대체)
├── security.py          비밀번호 해시 + 로그인 토큰 (표준 라이브러리만)
├── jobs.py              오래 걸리는 작업의 백그라운드 실행 + 상태(job 테이블)
├── llm_client.py        모든 LLM 호출의 단일 통로 (provider 분기 · 재시도 · 정책)
├── market.py            관심 종목 시세 (네이버 금융 → 공공데이터포털 → quote_daily 캐시)
├── db/
│   ├── database.py      SQLite 커넥션 헬퍼
│   ├── schema.sql       테이블 정의 (마스터 + 파밍 + 지식기반 + 과제 제안 + 관리자)
│   ├── seed.py          스키마 생성 · 마이그레이션 + 시드 실행
│   ├── seed_data.py     시드 원본 상수 (계열사 · 레버 · 혁신 사례 · 크롤 소스)
│   ├── seed_trendroom.py  화면 초기 데이터 시드
│   ├── seed_users.py    로그인 계정 시드
│   ├── backfill_trendroom.py  기존 feed_item 에 동향 키워드·스냅샷 채우기(1회성 CLI)
│   └── seed_assets/trendroom.json   화면 데이터 원본 (trendroom.html 에서 추출)
├── api/                 (단일 출처는 `curl -s localhost:8000/openapi.json`)
│   ├── deps.py          인증 의존성 (current_email)
│   ├── auth.py          POST /api/auth/login · GET /me · 비밀번호 변경 · 탈퇴
│   ├── bootstrap.py     GET /api/bootstrap     화면 초기 데이터 일괄
│   ├── proposals.py     과제 재생성 · 커스텀 생성(둘 다 비동기 job) · 별점/기준값/산출식 저장
│   ├── admin.py         인스트럭션 · 내부 자료 업로드 · 권한  (조회는 bootstrap 이 담당)
│   ├── report.py        AI Reporting 설정                     (조회는 bootstrap 이 담당)
│   ├── evaluation.py    GET /criteria · POST /run(+폴링)      저장된 과제 재평가
│   ├── quotes.py        GET /api/quotes        관심 종목 시세 (market.py 3단 폴백)
│   └── feed.py          GET /api/feed          파밍 결과 점검(인증 필요)
└── pipeline/
    ├── farming/         지식 파밍: 크롤러(dart·sec·news) · llm 정제 · classify · entity · pdf
    ├── knowledge/       지식 기반: 파일 KB 검색(retriever) · 프롬프트 조립(prefetch) · DB 조회(repository)
    ├── discovery/       과제 발굴 agent (codex 호출) — 재생성과 커스텀 생성이 함께 쓴다
    ├── evaluation/      과제 평가: 검증(validator) · 채점(scorer) · 우선순위(priority)
    └── proposal/        제안서 생성 agent (CLI 진입점)
```

> **화면이 안 쓰는 조회 API 는 두지 않습니다.** 화면 데이터는 `GET /api/bootstrap` 하나로
> 내려가고, 나머지는 전부 "바뀐 것만 저장" 입니다. 그래서 `GET /api/proposals`,
> `GET /api/report/settings`, `GET /api/admin/{instruction,sources,uploads}`,
> `GET /api/proposals/{id}/evaluation` 은 없습니다 — 같은 값이 bootstrap 에 이미 있습니다.
>
> **예외는 `GET /api/admin/users` 하나입니다.** 계정 목록은 관리자만 볼 수 있어(👑 403 게이트)
> 전원에게 나가는 bootstrap 에 실을 수 없습니다. 계정 관리 탭이 열릴 때만 따로 부릅니다.
> 관리자 명단 테이블(`admin_member`)과 `POST`·`DELETE /api/admin/members` 는 **제거했습니다** —
> 화면 표시용 명단 UI 가 재설계에서 사라졌고, 계정 관리는 `/api/admin/users` 가 담당합니다.
>
> 화면이 없는 기능은 **API 대신 CLI** 로 돌립니다.
>
> ```bash
> # 저장된 과제 재평가 (LLM 채점 포함). HTTP 로도 가능: POST /api/evaluation/run
> python -m app.pipeline.evaluation.runner --all --llm
> python -m app.pipeline.evaluation.runner --ver g12          # 범위: --ids/--ver/--oc
>
> # 제안서 문서 생성 (proposal.id 지정)
> python -m app.pipeline.proposal --pid 1240                  # Markdown
> python -m app.pipeline.proposal --pid 1240 --llm --json     # LLM 확장 + JSON
> ```

## 실행

```bash
python -m venv .venv
source .venv/bin/activate            # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env                 # Windows: copy .env.example .env
uvicorn app.main:app --reload        # http://localhost:8000  (docs: /docs)
```

`oi_scout.db` 는 **저장소에 함께 들어 있습니다**(계정 3개 포함, 초기 비밀번호 `1111`).
크롤 산출물 76건이 시드로 복원되지 않아 파일째 넘기기 때문입니다 — 클론 직후 바로 뜹니다.

DB 를 처음부터 다시 만들려면(근거자료는 시드 14건에서 시작합니다):

```bash
python -m app.db.seed --reset        # 기존 DB 삭제 후 재생성
python -m app.db.seed_users --admin admin@sk.com   # 로그인 계정 + 첫 관리자
```

> 추적 파일이라 서버를 켜면 `git status` 에 곧바로 변경으로 잡힙니다.
> 데이터 갱신을 커밋할 게 아니면 `git checkout -- backend/oi_scout.db` 로 되돌리세요.

`OI_SERVE_FRONTEND=1` 로 띄우면 `frontend/dist` 까지 이 프로세스가 서빙합니다
(`npm run build` 선행 필요). 개발 중에는 0(기본)으로 두고 Vite dev 서버를 쓰세요.

> ⚠ **`frontend/public/trendroom.html` 을 고쳤으면 반드시 `npm run build` 를 다시 돌리세요.**
> `main.py` 가 돌려주는 것은 `public/` 이 아니라 **`frontend/dist/trendroom.html`** 입니다
> (vite build 가 `public/` 을 `dist/` 로 복사합니다). 재빌드를 빼먹으면 `OI_SERVE_FRONTEND=1`
> 로 띄운 사람만 **옛 화면**을 받습니다 — 실제로 그 상태에서 dist 판이 삭제된
> `POST`·`DELETE /api/admin/members` 를 불러 404 를 받고, bootstrap 이 더는 안 내리는
> `themes`·`evTheme`·`admins`·`evalCriteria` 를 읽어 테마 카드와 관리자 명단이 빈 채로 떴습니다.
> 확인: `grep -c "api/admin/members\|d\.themes\|d\.admins\|d\.evalCriteria" ../frontend/dist/trendroom.html` → **0**,
> 그리고 `diff -q ../frontend/dist/trendroom.html ../frontend/public/trendroom.html` → 차이 없음.

## 테스트

```bash
python -m app.db.seed                # ← 선행 필수
python -m pytest tests/ -q           # 현재 99개
```

`*.db` 는 저장소에 포함되지 않습니다. 시드를 먼저 돌리지 않으면 `tests/test_discovery_context.py`
가 모듈 최상위에서 DB 를 읽다가 **수집 단계에서 통째로 죽어 한 개도 실행되지 않습니다**
(`no such table: affiliate`). 실패가 아니라 collection error 로 나오니 헷갈리지 마세요.

회귀 테스트는 커스텀 과제를 실제로 1건씩 쌓습니다. 운영 DB 를 건드리기 싫으면
`OI_DB_PATH=/tmp/t.db python -m app.db.seed && OI_DB_PATH=/tmp/t.db python -m pytest tests/ -q`
처럼 격리해서 돌리세요.

## 화면 데이터 (O/I Spark)

화면이 쓰는 데이터는 `store.py` 한 곳에서 모아 `GET /api/bootstrap` 으로 한 번에 내려갑니다.
반환 키는 프론트 코드가 기대하는 이름(`ev`, `sum`, `oc`, `st` ...)에 그대로 맞춰져 있습니다.

| 화면 개념 | 테이블 | 비고 |
|---|---|---|
| OC(계열사) | `affiliate` + `biz_segment` | 화면 색상은 `affiliate.color` |
| 레버(기대효과 Logic) | `lever` | 관리지표 · 산출식 · 입력 항목. **계산 함수는 프론트**(`LEVER_CALC`) |
| 트렌드 테마 | `theme` | LLM 자료 분류·평가용. **bootstrap 페이로드에는 안 실린다**(화면에 렌더 지점 없음) |
| 근거 자료 | `feed_item` | 파밍 파이프라인이 채우는 테이블과 동일. 화면용 컬럼(`kind_label`·`theme`·`biz_hint`·`is_new`·`brief`) 추가 |
| 생성 버전 · 과제 제안 | `gen_version` · `proposal` · `proposal_evidence` | 재생성 후보는 `proposal_pool` |
| 평가 · 기준값 · 산출식 | `proposal_feedback` · `proposal_input` · `proposal_formula` | **계정별** 저장 |
| AI Reporting | `report_setting` · `report_recipient` · `report_exclude` | 계정별 |
| 관리자 | `crawl_source` · `upload_file` · `app_setting` | 계정 관리는 `app_user.is_admin` |
| 동향 키워드 | `feed_item_keyword` · `keyword_daily` | 자료별 키워드(최대 4개) · 일자별 등장 건수 스냅샷(전일 대비 증감 원천) |

초기 데이터는 `db/seed_assets/trendroom.json` — `frontend/public/trendroom.html` 이 상수로
갖고 있던 값을 그대로 추출한 파일이라 화면이 보여 주던 내용과 정확히 일치합니다.

### 트렌드룸 신규 4키의 출처

| bootstrap 키 | 원천 | 채우는 주체 |
|---|---|---|
| `evOc` | `feed_item_tag` | 파밍(`entity.tag_affiliates`) · 시드는 과제 인용 관계 역산 + 화면 상수 `EV_OC` (둘 다 더하기만) |
| `evKw` | `feed_item_keyword` | **사전 추출**(`pipeline/farming/keywords.py`)이 주(主), LLM `keywords` 가 앞자리를 덮는다 |
| `evBrief` | `feed_item.brief` | LLM 전용(`pipeline/farming/llm.py`). 비면 키를 안 내리고 화면이 요약으로 폴백 |
| `kwTrend` | `keyword_daily` | 파밍 실행 끝의 일자별 스냅샷 차분. **스냅샷이 하루뿐이면 `{}`** → 화면은 전부 `–` |

#### `evBrief` 는 지금 시드 14건만 채워져 있습니다 (LLM 크레딧 소진)

`brief` 는 LLM 만 만들 수 있는 값이라 규칙으로 지어내지 않습니다 — 근거 없는 문장이
트렌드룸 브리핑 카드에 박히기 때문입니다. 크롤분은 화면이 `EV_BRIEF[k] || e.sum` 으로
요약에 폴백하므로 깨지지는 않지만, 브리핑이 요약 재탕이 됩니다.

크레딧이 복구되면 **재크롤 없이 정제만** 돌려 채웁니다.

```bash
python -m app.pipeline.farming.run --with-docs 5    # --no-llm 을 빼면 정제까지 간다
```

> ★ `keywords`·`brief` 는 `llm.OUTPUT_SCHEMA` 에 나중에 붙은 필드라 **실호출 검증이 안 된
> 유일한 경로**입니다. 크레딧 복구 후 반드시 소량(`--enrich-limit 1`)으로 먼저 돌려
> `codex --output-schema` 가 400(invalid_json_schema)을 내지 않는지 확인하세요.
> OpenAI structured outputs strict 는 `properties` 전 키가 `required` 여야 해서
> 두 필드도 `required` 에 들어 있습니다(자기정합성은 단위 확인 완료).

이미 쌓인 자료(재크롤 전)에는 키워드가 없으므로 1회성 백필을 돌립니다.

```bash
cp oi_scout.db oi_scout.db.bak              # 원본 보호
python -m app.db.backfill_trendroom --dry-run   # 무엇이 바뀌는지 먼저 확인
python -m app.db.backfill_trendroom             # 키워드 없는 자료만 채운다
python -m app.db.backfill_trendroom --force     # lexicon 을 고친 뒤 전량 재추출
```

기본 실행은 **키워드가 이미 있는 자료를 건너뜁니다** — 시드 14건의 키워드는 화면 상수를
옮긴 손질된 값이라 사전 추출로 덮으면 품질이 떨어집니다. `brief` 는 어느 경우에도
건드리지 않습니다(LLM 만 만들 수 있는 값입니다).

#### `kwTrend` 가 `{}` 로 나온다면 — 정상입니다. 파밍을 한 번 더 돌리세요

`keyword_daily` 에 스냅샷이 **하루치뿐이면** 비교 기준이 없어 `_kw_trend()` 가 `{}` 를
내립니다(화면은 증감 칸을 전부 `–` 로 그립니다). 첫 스냅샷만 있는 상태에서 `n − 0 = +n` 을
내려 전 키워드에 ▲ 를 붙이는 것보다 정직한 표시입니다.

둘째 날 스냅샷은 **파밍을 한 번 더 돌리면 자동으로 생깁니다.**

```bash
cp oi_scout.db oi_scout.db.bak                        # 원본 보호
python -m app.pipeline.farming.run --no-llm --with-docs 5   # 약 2.4분. LLM 크레딧 불필요
```

`ingest._KW_SNAPSHOT` 이 `substr(farmed_at,1,10)` 기준으로 그날치를 `INSERT OR REPLACE`
하므로 실행 즉시 오늘 날짜 행이 생기고, 다음 bootstrap 부터 `kwTrend` 가 채워집니다.
(실측: 하루 더 돌려 `2026-08-06` 28종 ↔ `2026-08-07` 26종이 되자 차분 9종이 나왔습니다.
차분이 0 인 키워드는 페이로드에서 빠집니다 — 렌더 결과가 같습니다.)

> **재크롤은 이미 확보한 키워드를 깎지 않습니다.** `_sync_keywords` 가 추출 원문을
> 이번 실행이 들고 온 값이 아니라 **`_UPSERT` 를 마친 행에서 다시 읽기** 때문입니다.
> 예전에는 이번 실행의 빈 ref/naive 요약으로 뽑아서 '지우고 다시 넣기' 가 `_UPSERT` 의
> 보존 가드를 우회했고, `--no-llm --with-docs 5` 재크롤 한 번에 키워드 보유 자료가
> **77건 → 43건**으로 무너졌습니다(실측). 회귀 테스트가 `tests/test_trendroom_contract.py`
> 의 `test_추출_원문은_이번_실행값이_아니라_저장된_행에서_읽는다` 입니다.

## 인증

`app_user` 에 등록된 이메일로 로그인합니다. 비밀번호는 pbkdf2_sha256(per-user salt)로
저장하고, 토큰은 HMAC-SHA256 서명 문자열이라 서버가 세션을 들고 있지 않습니다.

```bash
python -m app.db.seed_users                    # 기본 데모 계정 3개 (admin@sk.com 이 관리자)
python -m app.db.seed_users --file emails.txt  # 파일에서 (한 줄에 하나)
python -m app.db.seed_users --pw 0000 a@sk.com # 초기 비밀번호 지정
python -m app.db.seed_users --reset-pw a@sk.com
python -m app.db.seed_users --admin admin@sk.com   # 관리자 지정(기존 계정도 승격)
```

화면의 **계정 관리** 탭(`/api/admin/users`)은 `app_user.is_admin = 1` 인 계정만 쓸 수 있고,
아니면 403 + "관리자 권한이 필요합니다." 를 돌려줍니다. 관리자를 만드는 API 자체가 그 권한
뒤에 있으므로, **첫 관리자는 반드시 위 `--admin` 으로 지정합니다.** 기존 DB 도 이 명령 한 번이면
컬럼 추가(마이그레이션)와 승격이 함께 끝납니다.

> `OI_AUTH_SECRET` 기본값은 개발용입니다. 운영에서는 반드시 임의의 긴 문자열로 바꾸세요
> — 바꾸면 발급된 토큰이 모두 무효화됩니다(재로그인 필요).

## 지식 파밍 (크롤러) — 구현됨

watchlist(`pipeline/farming/watchlist.py`)의 peer 기업/토픽을 대상으로 DART · SEC · 뉴스를
크롤해 `feed_item` 에 적재합니다.

```bash
# 전체 소스 크롤 → 원문 확보 → LLM 정제 → DB 적재 (기본값으로 충분합니다)
python -m app.pipeline.farming.run

python -m app.pipeline.farming.run --days 14              # 기간 지정
python -m app.pipeline.farming.run --source news --dry     # 특정 소스만, 적재 없이 미리보기
python -m app.pipeline.farming.run --with-docs 0           # 목록만 (원문 확보 없이)
python -m app.pipeline.farming.run --no-llm                # LLM 정제 없이 naive 요약
python -m app.pipeline.farming.run --enrich-limit 20       # 정제 건수 상한(비용 통제)

# watchlist 밖 기업의 사례를 역방향 발굴 (EDGAR 전문검색)
python -m app.pipeline.farming.run --search "cost reduction program"
```

원문 확보 상한은 `--with-docs N × 소스별 배수(BODY_FACTOR)` 입니다. 소스마다 확보 비용이
자릿수 단위로 다르기 때문입니다 — DART 0.47초/건(일 20,000건 한도의 0.07%),
SEC 0.53초/건(실측 3.80 req/s, 차단선 10 req/s), 뉴스 1.9초/건(링크 해석·예의 대기).
기본값 `--with-docs 5` 의 실효 상한은 dart 20 · sec 20 · news 45 로 실측 목록 전량을 덮습니다.

크롤 1회 소요 실측(69건): **원문 확보까지 1.9분** (목록 17초 + 본문 99초),
LLM 정제 62건을 포함해 **10.0분**. 정제가 소요의 8할입니다(codex 호출당 약 23초, 동시 3).
`--enrich-limit` 가 확보한 본문 수보다 작으면 '원문 확보' 배지에 요약이 빈 행이 생기므로
두 값은 같이 올려야 합니다(로그가 경고합니다).

크롤 끝에 소스별 요약표가 찍힙니다 — 수집 / 원문 확보 / 정제 / 미확보 사유별 건수.
사유가 `한도밖` 이면 `--with-docs` 를 올려 회수할 수 있고, `시도안함`·`요청실패` 는
페이월·JS 렌더링·봇 차단이라 우회하지 않고 '원문 미확보' 로 남깁니다.

| 소스 | 모듈 | 키 | 비고 |
|------|------|----|------|
| DART | `dart.py` | `DART_API_KEY` 필요 | [opendart.fss.or.kr](https://opendart.fss.or.kr) 무료 발급. `document.xml` 로 원문 확보 |
| SEC  | `sec.py`  | `SEC_USER_AGENT` 필요 | 연락처 포함 UA만 있으면 됨(무료). EX-99 첨부 + 전문검색 |
| 뉴스 | `news.py` | 불필요 | Google News RSS. 검색어 언어에 따라 로케일 자동 분기 |

키가 없는 소스는 조용히 건너뛰므로 일부만으로도 부분 동작합니다.

#### 뉴스 대체 경로 (탐색 결과 · 2026-08-07 실측)

Google News 는 robots 금지 경로라 대체재를 실측했습니다. **아직 교체하지 않았습니다** —
아래 셋 다 현행 대비 손해가 있어, 선택은 배포 시점의 판단으로 남깁니다.

| 후보 | robots | 실측 | 한계 |
|------|--------|------|------|
| **네이버 검색 API** | 무관(계약·키) | 키 없이 401 확인 | 키 발급 필요. 국내만 |
| **GDELT DOC API** | 무관(공개 API) | 1질의 20건·18매체 | 5초당 1건 + **연장 패널티**. 한국어 제목 깨짐 |
| **매체 자체 RSS** | **7곳 전부 허용** | 390건 중 적중 15건 | 검색이 아닌 고정 피드. URL 수명 짧음 |

핵심 제약 — 현재 뉴스 49건이 **32개 매체**에 흩어져 있습니다(대부분 1건씩).
Google News 가 하는 일은 피드 구독이 아니라 **웹 전체 검색**이라, 고정 피드 구독으로는
이 꼬리를 덮지 못합니다. 검색을 대체할 수 있는 건 네이버 API 와 GDELT 뿐입니다.

- GDELT 는 영어 질의로도 국내 매체를 색인하지만(heraldcorp·newstomato 확인),
  한국어 제목이 `금호석화 , R _ xB85C _ 불황 돌파` 처럼 깨져 옵니다 — 한국어 제품에는 치명적입니다.
  또 초기 버스트 후 IP 에 연장 패널티가 걸려 10분 넘게 풀리지 않았습니다.
- 매체 RSS 는 robots 가 깨끗한 유일한 후보지만, 시도한 9개 중 4개(서울경제·데일리안·뉴스핌·아주경제)가
  404 였습니다. 보조 소스로는 쓸 만해도 단독 대체는 안 됩니다.

→ **권고**: 사내 배포 시 네이버 검색 API 키를 발급받아 국내 축을 옮기고,
해외 축은 지금처럼 DART·SEC 공시로 받는 조합. 매체 RSS 는 보강용으로만.

### 정제 (`llm.py` / `entity.py`)

원문을 **3줄 요약 · 레버 · 계열사 · 사례성 · 중요도**로 압축해 `feed_item` 에 함께 적재합니다.

**LLM provider 는 codex 하나로 통일돼 있습니다.** SK 사내망 정책이 codex 만 허용하기 때문에,
발굴·평가·제안서·파밍 정제가 전부 `codex exec` 를 씁니다. `OI_CODEX_ONLY=1`(기본)이면
다른 provider 는 `ready()` 가 거부해, 잘못 설정했을 때 조용히 naive 폴백으로 떨어지지 않고
큰 소리로 실패합니다.

| provider | 인증 | 비고 |
|---|---|---|
| `codex-cli` (기본·사내망 유일) | **API 키 불필요** — `codex login`(ChatGPT 계정) | `--output-schema` 로 JSON 형태를 강제할 수 있는 유일한 provider |
| `claude-cli` · `anthropic` · `openai` | — | 사외 개발용. `OI_CODEX_ONLY=0` 으로만 열립니다 |

인증 정보가 `CODEX_HOME`(~/.codex)에 있어, 이를 읽을 수 없는 컨텍스트(다른 사용자·docker·
systemd)에서는 설치돼 있어도 `Not logged in` 이 됩니다. 서비스 계정으로 `codex login` 을
한 번 돌리거나 `CODEX_HOME` 을 그 계정이 읽을 수 있게 두세요.

**추론 강도가 속도를 지배합니다.** codex 기본값 `xhigh` 는 매우 느립니다 —
실측(발굴 프롬프트 4,573토큰 1건): xhigh 174~197초 / medium 58~62초 / low 38~41초.
`OI_CODEX_EFFORT` 기본값을 `medium` 으로 두었습니다. 출력 형태는 `--output-schema` 가
강제하므로 강도를 낮춰도 구조가 깨지지 않습니다.

호출이 느려 `OI_LLM_CONCURRENCY`(기본 3) 만큼 동시에 돌립니다.

**설정이 없어도 파이프라인은 그대로 돕니다.** provider 미설정·네트워크·파싱 실패는 전부
naive 요약(제목/본문 절삭) + watchlist·키워드 태깅으로 폴백하고 `enriched=0` 으로 기록됩니다.

#### 본문을 잘못 고르면 정제가 통째로 무의미해집니다

두 가지가 실측으로 확인돼 각각 대응돼 있습니다. 소스를 추가할 때도 같은 함정을 점검하세요.

**1. 정기보고서는 앞부분을 그냥 자르면 안 된다.** DART 분기보고서 앞 4,000자는 표지와
목차입니다(실측: S-Oil 159,534자 문서에서 '원가' 첫 등장이 13,739자 지점).
→ `llm.select_excerpt()` 가 원가·가동률·정기보수 등 신호 키워드 주변을 발췌합니다.

**2. SEC 8-K 의 primary document 는 표지 서식일 뿐이다.** 실적·보도자료는 `EX-99` 첨부에
있습니다(실측: Dow 8-K primary 26KB=표지 / EX-99.1 553KB=press release).
→ `sec.list_documents()` 로 첨부 목록을 읽고 `pick_content_doc()` 이 EX-99 를 우선합니다.

같은 문서에 대한 정제 결과 변화:

| | 표지·목차만 넣었을 때 | 실제 본문을 넣었을 때 |
|---|---|---|
| Dow 8-K | importance 5, `case_worthy=false` | **75, `case_worthy=true`** — "self-help initiatives, PE 가격 +30%" |
| LyondellBasell 8-K | 12, `case_worthy=false` | **75, `case_worthy=true`** — "Cash Improvement Plan, 고정비 감축" |
| S-Oil 분기보고서 | 15 — "정제능력 66.9만배럴" | 22~48 — "정유 95.9% 고가동률" |

| 컬럼 | 의미 |
|---|---|
| `summary` | 정제 시 3줄 요약(개행 포함), 아니면 naive 절삭 |
| `levers` | 비용 절감 / 수익 증대 / 운영 효율 |
| `importance` | 0~100. 대시보드 top-n 선정 기준 |
| `reason` | 중요도 판단 근거 1문장 |
| `case_worthy` | 1이면 `kb_innovation_case` 승격 후보 |
| `enriched` | 1이면 LLM 정제 성공 |

> `pdf.py` 는 크롤러가 아니라 **관리자 업로드**가 씁니다 — `POST /api/admin/uploads/file` 이
> PDF 본문을 여기서 뽑습니다. 크롤 소스 중에는 PDF 가 없어(DART=XML, SEC=HTML) 크롤 경로에서는
> 호출되지 않고, IR·지속가능경영보고서를 소스로 추가하면 그때 바로 연결됩니다.

### 운영 주의

- `python -m app.db.seed --reset` 은 DB 파일을 삭제합니다 — **크롤 데이터가 함께 날아갑니다.**
  스키마만 갱신하려면 `--reset` 없이 실행하세요(누락 컬럼만 ALTER TABLE 로 추가).
- `OI_TODAY` 는 **빈 값이 정상**입니다(현재 `.env` 도, 코드 기본값도 빈 값입니다).
  값을 주는 것은 데모 재현용뿐이고, 고정하면 오늘 수집한 항목이 과제 발굴의 최근 30일
  창 밖으로 밀려 제외됩니다.
  화면 기준일(`GET /api/bootstrap` 의 `today`)은 모듈 상수가 아니라 매 요청
  `config.today_local()` = **실제 오늘 날짜(KST)** 입니다. 서버를 며칠 띄워 둬도
  부팅일에 굳지 않습니다.
- **NEW 배지 = '오늘(KST) 크롤한 자료'** 입니다. 저장 플래그가 아니라 읽는 시점 판정이라
  (`store._evidence` 가 `date(farmed_at, '+9 hours') = 오늘`), 파밍을 안 돌린 날에는
  자동으로 0건이 되고 '오늘 언급된 키워드' 패널도 함께 빕니다 — 그게 정직한 동작입니다.
  `feed_item.is_new` 컬럼은 남아 있지만 **아무도 읽지 않는 레거시**입니다.
  `farmed_at` 은 UTC ISO 로 저장하고 해석만 KST 로 합니다(`OI_UTC_OFFSET_HOURS`).
  전제: 파밍을 하루 1회 이상(적어도 7일 안에) 돌립니다.
- **커스텀 과제는 같은 계열사에 같은 이름으로 두 번 만들어지지 않습니다.**
  라우트 사전검사(409 `duplicate_exact` / 확인 후 진행 가능한 `duplicate_similar`) →
  저장 직전 재확인 → `proposal(aff_code, name_key)` **UNIQUE 인덱스** 3층입니다.
  기존 DB 에 이미 쌓인 중복은 `python -m app.db.seed`(--reset 없이) 가 늦게 만들어진
  쪽의 `name_key` 에만 `#id` 를 붙여 구분합니다 — **행은 지우지 않습니다.**
  `name_key` 는 NFKC 정규화 후 공백·괄호·**문장부호**를 지운 값입니다 — 예전에는 마침표
  하나만 붙여도 키가 갈라져 완전일치 층이 통째로 뚫렸습니다. 규칙을 바꿀 때는
  `store.NAME_KEY_REV` 를 올리세요. 그래야 `python -m app.db.seed` 가 기존 행의 키를
  **전량 재계산**합니다(안 하면 옛 키가 남아 중복 차단이 조용히 뚫립니다).
- **'비슷한 과제' 판정은 근거가 2건 이상 겹칠 때만 근거집합으로 봅니다**
  (`persist.EV_MATCH_MIN`). 화면 커스텀 생성이 근거를 1건만 보내고 실제 과제 대다수가
  근거 1건짜리라, 예전 규칙(1건만 같아도 중복)은 같은 (계열사,레버) 60쌍 중 37쌍을
  중복으로 잡았습니다 — 이름 유사도 0.06~0.36 인 서로 다른 과제들입니다.
  그 밖에는 이름 유사도 `OI_DUP_SIMILARITY`(기본 0.70)로 판정합니다.
  재생성이 버린 초안은 **서버 로그**에 이유와 함께 남습니다(`초안 N건 중 M건 저장 · K건 제외`).
- SEC 는 초당 10건 초과 시 약 10분간 IP 가 차단됩니다. `--with-docs` 를 크게 잡지 마세요.
- 뉴스 본문은 **DB 에 저장하지 않습니다**(저작권). 본문을 확보하지 못하면 요약을 비우고
  화면에 '원문 미확보' 로 표시합니다 — 빈 요약을 버그로 오해하지 마세요.
- ⚠ **Google News 진입 경로는 robots.txt 금지 대상입니다.** `news.google.com/robots.txt` 는
  `Disallow: /` 에 `/rss/` 를 허용하지 않으므로 RSS 목록·기사 셸·batchexecute RPC 가 모두
  금지 경로입니다(매체 기사 본문 요청은 robots 를 지킵니다 — 층이 다릅니다).
  사내 검증 용도라 현행 유지 중이며, `OI_NEWS_ROBOTS_STRICT=1` 로 두면 진입 자체를 막습니다.
  **외부 배포·상시 운영 전에는 그 값을 1 로 돌리거나 아래 대체 경로로 교체하십시오.**
