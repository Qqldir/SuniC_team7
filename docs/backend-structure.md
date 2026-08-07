# O/I Spark 백엔드 구조 — 테이블 · API · CRUD

> 작성 기준: `SuniC_team7` / 2026-08-07 (트렌드룸 재설계 반영)
> 엔드포인트 **27개(25 경로)** · 테이블 **32개** + 뷰 1개
> (감사 후 정리: 41→24 경로. 화면·파이프라인이 안 쓰는 라우트와 빈 테이블 제거. 기능 손실 0.
>  그 뒤 시세가 1경로(`GET /api/quotes`) · 1테이블(`quote_daily`)을 더했다 = 25 경로 · 32 테이블)
> 근거 명령: `cd backend && .venv/bin/python -c "from app.main import app; print(sorted(app.openapi()['paths']))"`
> — `/api/auth/me` 가 GET·DELETE, `/api/admin/users` 가 GET·POST 라 경로 25 · 오퍼레이션 27 이다.
> 이 문서의 모든 표는 **실행 중인 서버의 OpenAPI 와 소스의 SQL 을 추출해** 만들었습니다(손으로 옮기지 않음).
> 표에 적힌 행수는 작성 시점의 개발 DB 스냅샷입니다 — 구조를 감잡는 용도이지 고정값이 아닙니다.

---

## 0. 한눈에 보기

```
                  ┌───────────────────────────────────────────────────────┐
   화면            │  frontend/public/trendroom.html  (앱 전체가 이 파일 1개)│
                  │  frontend/src/views/Login.jsx    (로그인 랜딩만 React) │
                  └───────────────┬───────────────────────────────────────┘
                                  │ 화면이 뜰 때 딱 한 번
                                  ▼
                        GET /api/bootstrap          ← 화면 데이터 전부를 한 번에
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
   [마스터]                  [콘텐츠]                   [사용자별 상태]
   affiliate                 feed_item                 proposal_feedback
   biz_segment               proposal                  proposal_input
   lever / lever_alias       proposal_evidence         proposal_formula
   theme                     gen_version               report_setting
   source_kind               proposal_evaluation       report_recipient
                             proposal_feedback_log     report_exclude
```

**핵심 원칙 3가지**

1. **화면은 `/api/bootstrap` 하나로 초기 데이터를 다 받는다.** 나머지 API 는 전부 "바뀐 것만 저장".
2. **콘텐츠(모두 공유)와 사용자별 상태(계정마다 다름)를 테이블로 분리한다.**
   같은 과제라도 별점·기준값·산출식은 사람마다 다르다.
3. **사용자 별점과 AI 채점은 절대 같은 컬럼에 넣지 않는다.** (→ §4)

---

## 1. 테이블 지도

### 1-1. 마스터 — 사람이 정하는 기준값. 시드로 채우고 거의 안 바뀜

| 테이블 | 행수 | 무엇 | 주요 컬럼 |
|---|---:|---|---|
| `biz_segment` | 3 | 사업부문 | `key`(energy/battery/lng), `label`(에너지·화학…), `color` |
| `affiliate` | 9 | 계열사(OC) | `code`(SKE…), `name`, `biz`→biz_segment, `color`, `sort_order`, **`kb_company`** |
| `lever` | 7 | 개선 레버 + 기대효과 산출식 템플릿 | `name`(정비/TA…), `metric`, `formula`, `fields`(JSON), **`kb_query`**, **`impact_base`** |
| `lever_alias` | 16 | 레버 표기 변형 → 정식명 | `alias`(정비·TA), `lever`(정비/TA) |
| `theme` | 7 | 트렌드 테마 | `name`, `color`, `bg`, `head`, `body` |
| `source_kind` | 9 | 자료 종류 | `key`(disclosure/earnings/…), `label`(공시/실적발표/…) |
| `app_user` | 3 | 로그인 계정 | `email`(PK), `password_hash`, `is_active`, **`is_admin`**, `created_at` |

> **`affiliate.kb_company`** — `backend/knowledge/<디렉터리>` 이름. SKO·SKES 만 값이 있고 나머지 7개는 NULL.
> NULL 이면 RAG 가 내부 지식 블록을 통째로 생략한다. 이 값이 없는데 검색을 시도하면 500 이 난다.
> **`lever.kb_query`** — 레버로 내부 지식을 검색할 때 쓰는 질의어. 레버명("간접비")을 그대로 쓰면
> 0건이 나와서 따로 둔다. 튜닝할 때는 반드시 `prefetch.KB_TOP_K`(=2)와 **같은 top_k 로** 측정할 것.

### 1-2. 콘텐츠 — 파이프라인·LLM 이 채움. 모든 사용자가 공유

| 테이블 | 행수 | 무엇 | 채우는 주체 |
|---|---:|---|---|
| `feed_item` | 90 | **외부 근거 자료**(공시·실적·뉴스) | 파밍 크롤러 + LLM 정제 |
| `feed_item_tag` | 166 | 자료 ↔ 계열사 (bootstrap `evOc`) | 파밍 엔티티 태깅 |
| `feed_item_keyword` | 156 | 자료 ↔ 동향 키워드 (bootstrap `evKw`) | 파밍 사전 추출 + LLM |
| `keyword_daily` | 28 | 키워드 일별 등장 건수 (bootstrap `kwTrend` 의 차분 원천) | 파밍 실행 끝 스냅샷 |
| `gen_version` | 21 | **생성 버전**(재생성 1회 = 1행) | 재생성 |
| `proposal` | 68 | **과제 제안** | LLM 발굴 / 후보풀 / 커스텀 / 시드 |
| `proposal_evidence` | 74 | 과제 ↔ 근거 자료 | 과제 저장 시 |
| `proposal_pool` | 4 | 재생성 후보 풀(LLM 실패 시 폴백) | 시드 |
| `proposal_evaluation` | 400 | **AI 평가 결과**(이력 보존) | 평가 실행 |
| `proposal_evaluation_issue` | 405 | 검증 이슈(경고/차단) | 평가 실행 |
| `kb_innovation_case` | 8 | 혁신 사례 | 시드만 (입력 API 없음) |
| `crawl_source` / `upload_file` / `app_setting` | 12/5/3 | 관리자 화면 | 시드 + 관리자 |
| `quote_daily` | 기준일별 누적 | 관심 종목 시세 캐시 (`GET /api/quotes` 3단 폴백의 마지막 층) | `app/market.py` |
| `job` | 11 | 비동기 작업 상태 | 재생성·LLM 평가 |

> **`crawl_source.last_at` 은 아무도 갱신하지 않는다.** 시드가 넣은 표시용 문자열이라
> 화면이 그 값을 '마지막 수집' 으로 읽으면 거짓이 된다(실제 수집 시각은 `feed_item.farmed_at`).
> 그래서 bootstrap 은 `crawlAt` 키를 `MAX(farmed_at)`(KST)에서 따로 만들어 내린다.

> **`admin_member` 는 제거했다.** 화면 표시용 관리자 명단이었는데 재설계된 트렌드룸이
> 실제 로그인 계정(`app_user`)을 다루는 계정 관리 탭으로 갈아탔다 — 명단 테이블은 소비처가 0 이 됐다.
> 계정 관리는 `/api/admin/users` 4개 엔드포인트가 `app_user.is_admin` 으로 담당한다(2-5 절).
> 기존 DB 는 `app/db/seed.py` 의 `_DROPS` 가 시드 실행 때 지운다.

#### `feed_item` 컬럼 (외부 자료 1건)

```
원문 그대로            id, published_on, kind→source_kind, source, title, summary, url, farmed_at
화면 표시용            kind_label(Earnings call), source_label, title_label, publisher,
                      theme→theme, biz_hint, is_new, metrics(JSON), evidence_grade
LLM 정제 결과          levers, importance(0~100), reason, brief, case_worthy, enriched
```
> `source`/`title` 은 **원문을 보존**하고, 화면에는 `source_label`/`title_label` 이 있으면 그걸 쓴다.
> `evidence_grade` = 원문 확보 / 요약문 / 제목만 — "이 요약이 무엇을 보고 만들어졌는가".
> **`brief`(bootstrap `evBrief`)는 `summary`·`reason` 과 목적이 다르다.** `summary` 는 사실 재진술,
> `reason` 은 중요도 판단 근거(평가문), `brief` 는 트렌드룸 브리핑 카드에 쓸 1~2문장 해설이다.
> LLM 만 만들 수 있고, 비면 `store._ev_brief()` 가 **키 자체를 생략**해 화면이 요약으로 폴백한다.
> 본문 없는 재크롤(`--with-docs 0` / `--no-llm`)이 기존 값을 덮지 않도록 `ingest._UPSERT` 에 보존 가드가 있다.

#### `proposal` 컬럼 (과제 1건)

```
정체성      id(INTEGER PK), ver_id→gen_version, aff_code→affiliate, lever→lever
내용        name, summary, plan, background, risk, effect, kpi_name, kpi_formula
관리        origin(자동/커스텀/AI생성), status(검토중…), created_at
중복 차단   name_key   ← 공백·기호 제거한 정규화 과제명
근거        kb_refs(내부 지식 문서 id), proposal_evidence(외부 자료)
```

### 1-3. 사용자별 상태 — 계정마다 다름. 전부 `user_email` 이 PK 의 일부

| 테이블 | 행수 | 무엇 |
|---|---:|---|
| `proposal_feedback` | 6 | **사용자 별점**(`star` 0~5) + 메모 |
| `proposal_feedback_log` | 19 | 별점 이력 + **당시 과제 스냅샷**(학습 데이터) |
| `proposal_input` | 1 | 기대효과 기준값 입력(JSON) |
| `proposal_formula` | 1 | 사용자가 고친 산출식 / 시스템 제안 ON·OFF |
| `report_setting` / `report_recipient` / `report_exclude` | 1/2/0 | AI Reporting 설정 |
| `v_feedback_by_lever` (뷰) | 5 | 계열사·레버별 별점 평균 집계 |

> **`proposal_feedback_log` 에는 일부러 FK 를 걸지 않았다.** 과제가 삭제되면 `proposal_feedback` 은
> CASCADE 로 사라지지만 로그는 남아야 한다 — 별점의 근거가 된 과제 문장까지 함께 보존해야
> 나중에 학습 신호로 쓸 수 있기 때문이다. **"고아 행 정리"를 하면 축적된 피드백이 날아간다.**

---

## 2. API ↔ 테이블 CRUD 표

기호: **C** 생성 · **R** 조회 · **U** 수정 · **D** 삭제 · 🔒 인증 필요(Bearer)

### 2-1. 인증 `/api/auth`

| Method | 경로 | 테이블 CRUD | 비고 |
|---|---|---|---|
| POST | `/login` | `app_user` **R** | 이메일+비밀번호 → 토큰 발급 |
| GET | 🔒 `/me` | — | 토큰에서 이메일만 |
| POST | 🔒 `/change-password` | `app_user` **R U** | |
| DELETE | 🔒 `/me` | `app_user` **D** | 탈퇴 |

> 비밀번호는 pbkdf2_sha256(per-user salt). 토큰은 HMAC-SHA256 서명 문자열이라 **서버가 세션을 안 들고 있다.**
> `OI_AUTH_SECRET` 을 바꾸면 발급된 토큰이 전부 무효가 된다.

### 2-2. 화면 초기 데이터 `/api/bootstrap`

| Method | 경로 | 테이블 CRUD |
|---|---|---|
| GET | 🔒 `/api/bootstrap` | `affiliate` `biz_segment` `lever` `source_kind` `feed_item` `feed_item_tag` `feed_item_keyword` `keyword_daily` `gen_version` `proposal` `proposal_evidence` `proposal_evaluation` `proposal_evaluation_issue` `crawl_source` `upload_file` `app_setting` `proposal_feedback` `proposal_input` `proposal_formula` `report_*` **← 전부 R** |

> `theme` 테이블은 **더 이상 bootstrap 이 읽지 않는다** — 페이로드에서 `themes`/`evTheme` 두 키를
> 뺐기 때문이다. 테이블·`feed_item.theme` 컬럼은 그대로 살아 있고 파밍 분류(`farming/ingest._db_themes`)와
> 평가가 계속 쓴다. 지운 것은 응답 2키뿐이다.

**응답 구조 — 최상위 22키** (프론트 변수와 1:1. 이름·순서를 바꾸면 화면이 깨진다)

```jsonc
{
  "user":  {"email": "admin@sk.com"},   // 프론트가 localStorage['oi-user'] 를 이 값으로 맞춘다
  "today": "2026-08-07",                // 기간 필터 기준일 — **매 요청 시점 KST**(config.today_local()).
                                        //   OI_TODAY 는 데모 재현용 override 이고 빈 값이 정상이다.
                                        //   상수가 아니라 함수라 서버를 며칠 띄워도 부팅일에 굳지 않는다.
  "kinds": ["공시","실적발표","IR·보고서","시황·전문지","협회 자료","뉴스"],  // 실재하는 종류만
  "ocs": [{code,name,biz}], "ocColor": {...}, "bizColor": {...},
  "levers": {"정비/TA": {metric, text, fields[]}},   // calc/show 는 프론트 LEVER_CALC 가 합성
  "evidence":      { "e1": {src, kind, date, url, title, sum, metrics} },
  "evBizFallback": {"e1": "에너지·화학"},
  "evNew":         {"e1": 1},                        // **오늘(KST) 크롤분만.** 저장 플래그(is_new)가
                                                     //   아니라 date(farmed_at,'+9 hours')==today 판정이다.
                                                     //   farmed_at 은 UTC 저장이라 오프셋 보정이 필수 —
                                                     //   substr(farmed_at,1,10) 으로 비교하면 KST 새벽
                                                     //   크롤분이 통째로 빠진다(실측 76건 → 0건).
  "evOc":          {"e1": ["SKE","SKGC"]},           // feed_item_tag
  "evKw":          {"e1": ["정기보수","공기 단축"]},   // feed_item_keyword (최대 4)
  "evBrief":       {"e1": "…1~2문장…"},               // feed_item.brief. 비면 키 자체를 생략
  "kwTrend":       {"원가 절감": 3, "물류비": -1},     // keyword_daily 최근 2일 차분. 1일뿐이면 {}
  "kindMap":  {"수시공시 (8-K)": "공시"},
  "versions": [{id, label, trigger, at}],            // label 은 날짜('2026.08.07'),
                                                     //   at 은 분 단위 시각('2026.08.07 15:51').
                                                     //   at 은 state.send.lastAt 과 **같은 표기**여야
                                                     //   한다 — 발송 대상 필터가 문자열 비교다.
  "tasks":    [ /* 아래 21개 키 */ ],
  "sources": [...],
  "crawlAt": "2026.08.07 03:00",                     // MAX(feed_item.farmed_at) 를 KST 로.
                                                     //   crawl_source.last_at 은 파이프라인이 갱신하지
                                                     //   않는 표시용 컬럼이라 못 쓴다. 이력이 없으면 ""
                                                     //   이고 화면은 그 줄을 아예 그리지 않는다.
  "uploads": [...],
  "instruction": "...",
  "state": { "fb": {"1240": {"s": 4, "t": "메모"}},   // ← 사용자 별점
             "fields": {...}, "fx": {...}, "sysOff": {...},
             "sendOff": {...}, "send": {...}, "recipients": [...], "channels": {...} }
}
```

> **삭제된 4키**: `themes` · `evTheme` · `admins` · `evalCriteria`. 트렌드룸 재설계로 테마 카드와
> 관리자 명단 UI 가 사라졌고, 선정 기준은 `GET /api/evaluation/criteria` 가 따로 준다.
> **신설된 5키**: `evOc` · `evKw` · `evBrief` · `kwTrend`(위 표의 신규 2테이블 + `feed_item.brief`)
> · `crawlAt`(사이드바 '수집 파이프라인' 의 마지막 수집 시각).
> `state.fb`/`fields`/`fx`/`sysOff` 의 키는 JSON 직렬화 때문에 **문자열**("1134")이고 `tasks[].id` 는 number 다.

> **시세는 bootstrap 이 아니라 별도 경로입니다** — `GET /api/quotes`.
> 화면 상단 '관심 종목' 티커가 현재가·등락률을 보여 주며, 값은 `app/market.py` 가 3단 폴백으로
> 만듭니다: ① 네이버 금융 실시간 체결가(키 불필요, 12종목 즉시) → ② 공공데이터포털
> 금융위원회_주식시세정보(직전 영업일 종가, 기준일 다음 영업일 13시 이후) → ③ `quote_daily` 캐시.
> **bootstrap 22키와 분리한 이유**: 시세는 외부 API 호출이라 실패·지연이 잦은데, 한 응답에 묶으면
> 화면 전체가 그 지연을 기다리고 외부 장애가 로그인 직후 화면을 통째로 막습니다. 갱신 주기도
> 다릅니다(시세는 `QUOTE_TTL_SEC`, bootstrap 은 화면 진입 1회). 실패해도 예외를 올리지 않아
> 숫자만 빠지고 종목명·링크는 남습니다.

**`tasks[]` 원소 21개 키** — 이름·순서를 바꾸면 화면이 깨집니다

| 그룹 | 키 | 출처 |
|---|---|---|
| 기본 8 | `id ver oc lever ev name sum plan` | `proposal` + `proposal_evidence` |
| 내용 8 | `bg risk eff kpi kpiFx status origin at` | `proposal` (`kpi`/`kpiFx` 는 비면 `lever` 기본값 폴백) |
| 평가 5 | `evalScore grade verdict scoredBy flags` | `proposal_evaluation`(is_latest=1) + `..._issue` |

### 2-3. 과제 제안 `/api/proposals`

| Method | 경로 | 테이블 CRUD | 비고 |
|---|---|---|---|
| POST | 🔒 `/regenerate` | `job` **C** → (백그라운드) | **즉시 작업 id 반환** |
| GET | 🔒 `/regenerate/{job_id}` | `job` **R** | 완료 시 versions·tasks 동봉 |
| POST | 🔒 `/custom` | `job` **C** → (백그라운드) | 커스텀 생성 — **비동기**. LLM 발굴을 태우고 실패 시 문자열 조립 폴백 |
| GET | 🔒 `/custom/{job_id}` | `job` **R** | |
| PUT | 🔒 `/{pid}/feedback` | `proposal_feedback` **C/U**, `proposal_feedback_log` **C** | **사용자 별점** |
| PUT | 🔒 `/{pid}/fields` | `proposal_input` **C/U** | 기준값 입력 |
| PUT | 🔒 `/{pid}/formula` | `proposal_formula` **C/U** | 산출식 수정 |

#### 재생성이 비동기인 이유

LLM 발굴은 계열사 1곳당 **58~62초**(codex, 추론강도 medium). 기본 2곳이라 2분 안팎입니다.
동기 응답으로 붙잡으면 nginx(기본 60초)·Cloudflare(100초) 뒤에서 **무조건 끊깁니다.**

```
POST /api/proposals/regenerate        →  {"job":"QIFVmdsq9KKw","status":"running"}   (즉시)
GET  /api/proposals/regenerate/QIFV…  →  {"status":"running"}                        (2초마다 폴링)
GET  /api/proposals/regenerate/QIFV…  →  {"status":"done","ver":"n63","versions":[…],"tasks":[…]}
```

작업 상태를 메모리가 아니라 `job` 테이블에 두는 이유: uvicorn 워커가 여럿이면 폴링 요청이
작업을 시작한 워커로 간다는 보장이 없기 때문입니다. 15분 넘게 `running` 인 작업은
프로세스가 죽은 것으로 보고 실패 처리합니다(화면이 영원히 "생성 중"에 머물지 않게).

#### 재생성 내부 흐름

```
regenerate()
 ├ 대상 계열사 선정        feed_item_tag R (is_new 많은 순 → 과제 오래된 순)
 ├ RAG 컨텍스트 조립       lever R · affiliate R · knowledge/ 파일 · upload_file R
 │                        · kb_innovation_case R · feed_item R        (약 4,600 토큰)
 ├ LLM 발굴               codex exec --output-schema  (계열사당 1회)
 ├ 레버 정규화             lever R · lever_alias R      ← 실패하면 그 과제는 버림
 ├ 중복 차단               proposal R (name_key + 레버·근거 조합)
 ├ 저장                   gen_version C · proposal C · proposal_evidence C
 └ 규칙 평가 자동 실행      proposal_evaluation C · ..._issue C        (LLM 0회, 1초 미만)

 ※ LLM 이 안 되면 → proposal_pool R/U 로 폴백 (gen_version.source='후보풀')
```

### 2-4. 과제 평가 `/api/evaluation`

| Method | 경로 | 테이블 CRUD | 비고 |
|---|---|---|---|
| GET | 🔒 `/criteria` | — | 선정 기준 문장 + 가중치 |
| POST | 🔒 `/run` | `job` **C** → (백그라운드) | 범위(ids/ver/oc) 지정 평가 |
| GET | 🔒 `/run/{job_id}` | `job` **R** | |

**평가가 저장하는 것**

```
proposal_evaluation        verdict(통과/검토필요/차단) priority(0~100) grade(A/B/C)
                           impact_score/reason · feas_score/reason · roi_score/reason
                           grounding(뒷받침/느슨함/무관/미확인) · scored_by(LLM/규칙/미채점)
                           rank_in_aff · batch_id · is_latest
proposal_evaluation_issue  code(MISSING_FIELD/DUPLICATE/STALE_EVIDENCE/TOO_SHORT)
                           severity(경고/차단) · message
```

> **이력 보존**: 재평가하면 이전 행의 `is_latest` 를 0 으로 내리고 새 행을 넣습니다.
> 화면은 `is_latest=1` 만 봅니다. `UPDATE → INSERT` **순서를 지켜야** 부분 유니크 인덱스에 안 걸립니다.
> **`rank_in_aff` 는 "계열사 내" 순위**입니다. 채점이 계열사 단위라 배치 전체 순위는 의미가 없습니다.

### 2-5. 관리자 `/api/admin`

| Method | 경로 | 테이블 CRUD |
|---|---|---|
| PUT | 🔒 `/instruction` | `app_setting` **C·U** |
| POST | 🔒 `/instruction/reset` | `app_setting` **R U** |
| POST | 🔒 `/uploads/file` | `upload_file` **C** (multipart. `use_now=true` 면 바로 '검수 완료') |
| GET | 🔒👑 `/users` | `app_user` **R** → `{"users":[{email, is_admin, is_active, created_at}]}` |
| POST | 🔒👑 `/users` | `app_user` **C** — `{email, is_admin}` → `{email, initial_password:"1111"}` |
| POST | 🔒👑 `/users/{email}/reset-password` | `app_user` **U** → `{ok, email, initial_password:"1111"}` |
| DELETE | 🔒👑 `/users/{email}` | `app_user` **D** + `store.purge_user()` 로 사용자 상태 6테이블 **D** |

> 👑 = **관리자(`app_user.is_admin=1`)만.** `app/api/deps.py:current_admin` 이 게이트다.
> 인증이 없으면 **401**, 인증은 됐지만 관리자가 아니면 **403** `{"detail":"관리자 권한이 필요합니다."}` —
> 화면(`trendroom.html` 계정 관리 탭)이 403 만 특별 취급해 안내 문구를 띄우므로 이 구분을 바꾸면 안 된다.
> 나머지 실패는 400(이메일 형식 · 본인 삭제 · 마지막 관리자 삭제) / 404(없는 계정) / 409(중복)이고
> 응답은 전부 `{"detail": "..."}` 다.
> 비밀번호는 프론트가 보내지 않는다 — 서버가 항상 `1111`(seed_users 기본값)을 쓴다.
> `instruction` · `instruction/reset` · `uploads/file` 3개에는 👑 게이트를 **일부러 안 씌웠다**(전원 사용).
> 첫 관리자는 `python -m app.db.seed_users --admin admin@sk.com` 으로 승격한다.

> **업로드 본문이 RAG 에 들어가는 조건**: `status='검수 완료'` **이고** `extracted_at IS NOT NULL`.
> 검토되지 않은 내부 문서가 자동으로 LLM 프롬프트에 흘러드는 것을 막는 게이트입니다.
> `upload_file.body` 는 최대 30만 자라 **`/api/bootstrap` 응답에 절대 넣지 않습니다** —
> `store._uploads()` 가 컬럼을 명시 열거하는 형태를 유지해야 합니다(`SELECT *` 로 바꾸면 유출).

### 2-6. AI Reporting `/api/report`

| Method | 경로 | 테이블 CRUD |
|---|---|---|
| PUT | 🔒 `/settings` | `report_setting` **C·U**, `report_recipient` **D→C**, `report_exclude` **D→C** |
| POST | 🔒 `/test` | `report_setting` **C·U** (발송 시각만 기록) |

> 실제 Outlook·Teams 발송은 미구현입니다. `store.mark_report_sent()` 자리에 붙이면 됩니다.

### 2-7. 평가 · 파이프라인

| Method | 경로 | 테이블 CRUD | 비고 |
|---|---|---|---|
| GET | 🔒 `/api/evaluation/criteria` | — | 선정 기준 문장 + 가중치 |
| POST | 🔒 `/api/evaluation/run` | `job` **C** → (백그라운드) | 범위 지정 평가. **LLM 채점을 다시 돌릴 유일한 수단** |
| GET | 🔒 `/api/evaluation/run/{job_id}` | `job` **R** | |
| GET | `/api/feed` | `feed_item` `feed_item_tag` **R** | 파밍 품질 점검용(화면 미사용) |
| GET | `/api/quotes` | `quote_daily` **R U** | 관심 종목 시세. 네이버 금융 → 공공데이터포털 → `quote_daily` 캐시 3단 폴백. **bootstrap 과 분리** — 외부 API 지연·장애가 화면 전체를 막지 않게 |

**감사 후 제거된 것** — 화면·파이프라인·테스트 어디서도 호출하지 않음이 grep 으로 입증된 것만 지웠습니다.

| 제거 | 이유 |
|---|---|
| `GET /api/proposals`, `/report/settings`, `/admin/{uploads,sources,instruction}` | `/api/bootstrap` 이 같은 데이터를 이미 준다 |
| `POST`·`DELETE /api/admin/members` (+ `admin_member` 테이블) | 화면 표시용 관리자 명단이 재설계에서 사라졌다. 계정 관리는 `/api/admin/users` 가 담당 |
| `GET /api/proposals/{pid}/evaluation` | bootstrap 의 `tasks[]` 가 verdict·grade·evalScore·flags·scoredBy 를 준다 |
| `POST /api/admin/uploads`(JSON) | 본문 없는 유령 행만 만들어 RAG 게이트를 영원히 통과 못 함 |
| `PUT /api/admin/uploads/{id}/status` | 승인을 **업로드 시 선택**(`use_now`)으로 옮김 |
| `/api/cases` 4개 | UI 가 redesign 에서 삭제됨. 혁신사례는 **시드로만 관리**(데이터·RAG 사용은 유지) |
| `POST /api/discovery/generate` | 고유 가치였던 'OC 지정 + note 주입' 을 커스텀 생성에 합침 |
| `POST /api/evaluation/{evaluate,validate}` | validate 는 evaluate 의 진부분집합. 둘 다 화면 진입점 없음 |
| `POST /api/proposal/{build,markdown}` | 제안서 문서 생성. 화면 진입점 없음 — **기능 상실이므로 되살릴 수 있게 코드는 남김** |
| `task` / `task_evidence` / `kb_process` / `kb_technology` / `kb_kpi_benefit` | 0행 · 참조 0건 |

---

## 3. 데이터가 흐르는 길 (간선)

```
 ① 외부 자료 수집
    DART/SEC/뉴스 ──crawler──▶ RawDoc ──classify──▶ 종류·테마·사업분야
                                  │
                                  └──LLM 정제(codex)──▶ 요약·지표·중요도
                                                          │
                                                          ▼
                                          feed_item  +  feed_item_tag
                                                          │
 ② 과제 발굴                                               │
    lever.kb_query ──▶ knowledge/SKO/ (748 문서) ──┐       │
    upload_file(검수완료) ─────────────────────────┤       │
    kb_innovation_case ────────────────────────────┼───────┘
                                                   ▼
                                          RAG 컨텍스트(≈4,600토큰)
                                                   │
                                            codex exec (스키마 강제)
                                                   ▼
                              lever_alias ──▶ 레버 정규화 ──▶ 중복 차단
                                                   ▼
                              gen_version + proposal + proposal_evidence
                                                   │
 ③ 평가                                             ▼
                              validator(규칙) + scorer(규칙|LLM) + priority
                                                   ▼
                          proposal_evaluation + proposal_evaluation_issue
                                                   │
 ④ 화면 · 피드백                                     ▼
                                          GET /api/bootstrap
                                                   │
                            사용자 별점 ──▶ proposal_feedback
                                          + proposal_feedback_log (스냅샷)
                                                   │
                                                   └──▶ ② 발굴 프롬프트로 되먹임
```

---

## 4. ⚠️ 헷갈리기 쉬운 지점

### 4-1. 사용자 별점 ≠ AI 채점 (가장 중요)

| | 사용자 별점 | AI 채점 |
|---|---|---|
| **누가** | 사람이 매김 | 규칙 또는 LLM |
| **범위** | 0~5 | 0~100 |
| **테이블·컬럼** | `proposal_feedback.star` | `proposal_evaluation.priority` |
| **계정별인가** | ✅ 계정마다 다름 | ❌ 전체 공유 |
| **API 키** | `state.fb[과제id].s` | `tasks[].evalScore` |
| **화면** | 별 5개 위젯 | 등급 뱃지(A/B/C + 점수) |

> 원래 둘 다 `score` 였고 실제로 화면·API 에서 계속 혼동됐습니다. 그래서 컬럼명을 `star` 로,
> API 키를 `evalScore` 로 갈랐습니다. **다시 `score` 로 되돌리지 마세요.**
> 두 값은 서로 영향을 주지 않습니다 — 별점 저장 후 재평가해도 별점은 그대로고, 그 반대도 같습니다.

### 4-2. 과제 = `proposal` 하나뿐 (레거시 정리 완료)

- **`proposal`** = 과제 테이블. 화면 목록이 이것입니다.
- 옛 `task`/`task_evidence` 테이블과 `/api/tasks` 는 **제거했습니다**(0행이라 데이터 손실 없음).
  기존 DB 도 `seed.py` 의 `_DROPS` 가 실제로 DROP 합니다.
- 코드에 남은 `TaskDraft` 는 **LLM 출력을 담는 중간 객체**입니다(테이블 아님).
  평가 모듈이 이걸 입력으로 받으므로 `runner._to_draft()` 가 `proposal` 행을 변환해 넘깁니다.
- 제안서 생성의 입력 모델은 `TaskIn` → **`ProposalDocIn`** 으로 개명했습니다.

### 4-3. `Proposal` vs `ProposalDoc` — 파이썬 클래스 이름 충돌

- **화면 목록 원소**(21개 키)는 파이썬 클래스가 아니라 `store._proposals()` 가 만드는 dict 입니다
  (`GET /api/bootstrap` 의 `tasks[]`).
- `models.ProposalDoc` = **제안서 문서**(정의·기대효과·추진 phase·투자·리스크).
  `python -m app.pipeline.proposal --pid <id>` 가 만듭니다.
- 후자를 `Proposal` 로 되돌리지 마세요 — 두 개념은 필드 교집합이 0이라 이름이 겹치면
  텍스트 병합기가 못 잡은 채 서로 다른 것이 같은 이름을 갖게 됩니다.

### 4-4. `feed_item` 이 두 역할을 겸함

파밍 파이프라인이 채우는 테이블과 화면의 "근거 자료"가 **같은 테이블**입니다.
일부러 그렇게 했습니다 — 외부 자료의 단일 출처를 하나로 두기 위해서입니다.
그래서 컬럼이 원문용(`source`,`title`)과 화면용(`source_label`,`title_label`)으로 나뉘어 있습니다.

### 4-5. 재크롤이 정제 결과를 덮지 않는다

`ingest.py` 의 UPSERT 는 `excluded.enriched OR NOT feed_item.enriched` 가드를 씁니다.
`--no-llm` 으로 다시 크롤해도 기존 LLM 요약·지표·등급이 파괴되지 않습니다.
(가드가 없던 시절 `summary` 가 naive 200자 절삭으로 덮이는 버그가 있었습니다.)

---

## 5. LLM 은 전부 codex 를 거친다

**SK 사내망 정책상 codex 만 허용**되므로, 모든 AI 호출이 `app/llm_client.py` 한 곳을 지나갑니다.

| 단계 | 모듈 | provider 설정 |
|---|---|---|
| 과제 발굴 | `pipeline/discovery/agent.py` | `OI_TASK_PROVIDER` |
| 과제 평가 | `pipeline/evaluation/scorer.py` | `OI_TASK_PROVIDER` |
| 제안서 생성 | `pipeline/proposal/generator.py` | `OI_TASK_PROVIDER` |
| 파밍 정제 | `pipeline/farming/llm.py` | `OI_LLM_PROVIDER` |
| 재생성 | `store.py` | `OI_TASK_PROVIDER` |

둘 다 기본값 `codex-cli`. `OI_CODEX_ONLY=1`(기본)이면 다른 provider 를 `ready()` 가 **거부**합니다 —
조용히 naive 폴백으로 떨어지면 "왜 품질이 나쁜지" 추적이 안 되기 때문입니다.

- 인증은 API 키가 아니라 `codex login`(ChatGPT 계정). 정보는 `CODEX_HOME`(~/.codex)에 있습니다.
  **다른 사용자·docker·systemd 에서는 읽지 못해 `Not logged in`** 이 됩니다.
- `--output-schema` 로 JSON 형태를 강제할 수 있는 유일한 provider 입니다.
  단 **최상위는 object 여야 합니다**(array 를 주면 HTTP 400).
- 추론 강도가 속도를 지배합니다 — 발굴 1건 기준 `xhigh` 174~197초 / `medium` 58~62초 / `low` 38~41초.
  기본값은 `OI_CODEX_EFFORT=medium`.
- 회귀 방지: `tests/test_llm_policy.py` 가 AST 로 `anthropic`/`openai` 직접 import 를 스캔합니다.

---

## 5-2. 지식 베이스(RAG) 현황

| 회사 | 디렉터리 | 문서 | 구성 |
|---|---|---:|---|
| SK온 | `knowledge/SKO/` | 742 | docs 718 · seeds 24 |
| SK E&S | `knowledge/SKES/` | 378 | docs 360 · seeds 18 |
| 나머지 7개 계열사 | — | 0 | `affiliate.kb_company = NULL` → RAG 블록 생략 |

각 디렉터리는 `INDEX.md` · `manifest.json` · `core/` · `docs/` · `seeds/` 로 같은 구조입니다.
검색은 `pipeline/knowledge/retriever.py` 의 **파일 탐색형**(manifest 의 title·summary·keywords·tags 를
BM25 유사 가중으로) 이고, 임베딩·벡터DB 를 쓰지 않습니다.

**⚠ 알려진 한계 — `lever.kb_query` 가 회사와 무관한 전역 값입니다.**
현재 값은 SKO(배터리 제조) 어휘로 튜닝돼 있어, 같은 질의를 SKES(LNG·전력)에 쓰면 적중률이 떨어집니다.

| 레버 | SKO (top-2) | SKES (top-2) |
|---|---|---|
| 정비/TA | Digital Twin·Predictive Maintenance / Predictive Maintenance | External Deployment Evidence Registry / External Evidence → E&S Task Mapping ✗ |
| 에너지비 | Coating·Drying / Energy·Dry-Room·Formation Model | LNG·전력·열 제품과 인프라 서비스 / 에너지솔루션 ✓ |
| 수율 | Yield·Scrap·Rework Model / End-to-End Yield Waterfall | City-Gas Procurement… / Evidence and Data-Quality Policy ✗ |
| 구매 | Li/Ni/Co/Mn Supply Chain / Anode Supply Chain | KCE BESS Supplier Ledger / Supply-Risk Register ✓ |
| 운전자본 | CAPEX & Financial-Structure / Public Financial Baseline | Public Investment & Funding Register / CAPEX Stage-Gate ✓ |

레버 14개 중 실제로 맞는 문서를 끌어오는 것은 §7 실측 기준 SKO 7 / SKES 4 입니다
(위 표는 대표 사례만 뽑은 것이라 성공 쪽이 많아 보입니다). 회사마다 사업 어휘가 다르므로
**`(레버 × 회사)` 단위 질의어**가 필요합니다 — RAG 재설계 시 첫 번째 항목.

## 6. 실행

```bash
# 백엔드
cd backend
python -m venv .venv && .venv/bin/pip install -r requirements.txt
cp .env.example .env
.venv/bin/python -m app.db.seed          # 스키마 + 시드 (기존 DB 는 --reset 없이 따라감)
.venv/bin/python -m app.db.seed_users    # 계정 (초기 비밀번호 1111)
.venv/bin/python -m uvicorn app.main:app --reload

# 프론트 (개발)
cd frontend && npm install && npm run dev        # http://localhost:5173/login

# 한 프로세스로 (데모)
cd frontend && npm run build
cd ../backend && OI_SERVE_FRONTEND=1 .venv/bin/python -m uvicorn app.main:app --port 8000
```

**검증 도구**

| 무엇 | 명령 |
|---|---|
| provider 정책 | `cd backend && .venv/bin/python -m pytest tests/ -q` |
| 화면 전체 회귀 | `node <scratchpad>/dom/drive.mjs` |
| 화면 9지점 | `node <scratchpad>/dom/front9.mjs` |
| API 스펙 | `http://localhost:8000/docs` |

**마이그레이션 규칙** — `app/db/seed.py`
- 컬럼 추가: `_MIGRATIONS` 에 `(컬럼명, DDL)` 추가. **테이블당 키는 하나뿐**(두 번 적으면 앞엣것이 사라짐)
- 컬럼 이름 변경: `_RENAMES` 에 추가. 그 컬럼을 참조하는 뷰는 `_VIEWS_TO_REBUILD` 에 넣어야 함
  (뷰는 생성 시점이 아니라 SELECT 시점에만 깨져서 조용합니다)
- `create_schema()` 는 **마이그레이션 → schema.sql** 순서입니다. 뒤집으면 새 인덱스가
  아직 없는 컬럼을 참조해 기존 DB 에서 죽습니다.

---

## 7. 아직 안 된 것 · 알려진 한계

| 항목 | 현재 상태 |
|---|---|
| Outlook·Teams 실제 발송 | 발송 시각만 기록 (`store.mark_report_sent`) |
| 제안서 문서 생성 | 화면 진입점이 없어 라우트를 제거함. `pipeline/proposal/` 코드는 남아 있어 되살릴 수 있음 |
| 지식 베이스 | SKO(742) · SKES(378). 나머지 7개 계열사는 `kb_company=NULL` — 천천히 채울 예정 |
| `lever.kb_query` | **회사와 무관한 전역 값.** SKO 어휘로 튜닝돼 SKES 적중률이 낮다 (→ 아래) |
| `proposal.status` | 전 행이 '검토중'. 값을 바꾸는 API 가 없음 (v2 예정) |
| `feed_item.metrics` | 시드 자료엔 없음. 크롤+정제한 자료에만 붙음 |

### KB 검색 품질 — 실측 (문서를 열어 근거가 되는지 판정)

| | SKO | SKES |
|---|---|---|
| 현재 전역 질의어 | **7 / 14** | **4 / 14** |
| 회사별 질의어를 만들면 | 9 / 14 | **12 / 14** |

> 판정 기준: 레버별 상위 2건(`prefetch.KB_TOP_K`=2)을 실제로 열어 "이 레버의 과제 근거가 되는가".
> 제목만 보고 세면 훨씬 높게 나옵니다 — 한때 14/14·8/14 로 잘못 기록했던 이유입니다.
>
> SKO 가 회사별 질의어로도 9/14 에 그치는 것은 **문서 자체가 없기 때문**입니다:
> `판관비|SG&A` 는 두 KB 통틀어 0건, SKO 운전자본(재고자산 회전일수)도 실질 문서가 없습니다.
> 질의어로 풀리지 않으므로 레버 지표를 바꾸거나 재무제표를 업로드해야 합니다.

### 다음 라운드 후보 (감사에서 확인된 것)

1. **레버 × 회사 질의어 테이블** — 위 표의 개선폭이 근거
2. **`_kb_blocks` 라운드로빈 채움** — 지금은 레버 순차라 `KB_TOP_K` 를 3 으로 올리면
   뒤쪽 레버가 통째로 사라진다(K=5 면 레버커버 3/7). 라운드로빈이면 K 와 무관하게 7/7 유지
3. **본문 발췌가 항상 첫 레버(정비/TA)** — 나머지 6개 레버는 요약 한 줄만 받는다
4. **`seeds` 선반 42건이 한 번도 안 실림** — 사람이 점수·KPI 까지 매긴 과제 후보인데
   일반 문서와 같은 풀에서 경쟁해 14회 검색에서 top-2 진입 0회
5. **오염 문서 제외** — build-log 15건, `Domain Boundary` 류 보일러플레이트(SKES 토큰의 11%)

---

## 부록. 개발 중 알아둘 것

- **회귀 테스트가 커스텀 과제를 1건씩 만든다.** `drive.mjs` 를 돌릴 때마다 같은 이름의 과제가
  개발 DB 에 쌓인다(커스텀 생성은 명시적 사용자 행위라 중복 검사가 없다). 주기적으로 정리하거나
  `OI_DB_PATH` 로 격리해서 돌려라.
- **프로덕션 DB 는 읽기 위주로 다뤄라.** 쓰기 실험은 사본 + `OI_DB_PATH` + 다른 포트.
- **프론트를 고쳤으면 `npm run build`** — 서버는 `frontend/dist` 를 서빙한다.
