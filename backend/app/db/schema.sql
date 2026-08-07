-- O/I Scout SQLite 스키마
-- 크게 (1) 마스터 (2) 지식 파밍 결과 (3) 지식 기반 (4) 과제 기록 으로 구성.

PRAGMA foreign_keys = ON;

-- ─────────────── 마스터 ───────────────
CREATE TABLE IF NOT EXISTS biz_segment (
    key   TEXT PRIMARY KEY,   -- energy / battery / lng
    label TEXT NOT NULL,
    color TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS affiliate (
    code       TEXT PRIMARY KEY,     -- SKE, SKGC ...
    name       TEXT NOT NULL,
    biz        TEXT NOT NULL REFERENCES biz_segment(key),
    color      TEXT,                 -- 화면 OC 색상 (사업부문별 램프)
    sort_order INTEGER NOT NULL DEFAULT 0,
    kb_company TEXT   -- backend/knowledge/<디렉터리> 이름. NULL 이면 내부 지식 베이스 없음
);

CREATE TABLE IF NOT EXISTS source_kind (
    key       TEXT PRIMARY KEY,   -- disclosure / earnings / ir / market / assoc (+ 레거시 adhoc/periodic/sec/news)
    label     TEXT NOT NULL,      -- 트렌드룸 종류 필터에 그대로 노출되는 이름
    css_class TEXT NOT NULL
);

-- ─────────────── 인증 (사용자 계정) ───────────────
-- 관리자가 seed 로 등록. email(=Outlook) 이 로그인 ID, 초기 비밀번호는 해시로 저장.
CREATE TABLE IF NOT EXISTS app_user (
    email         TEXT PRIMARY KEY,       -- Outlook 이메일 = 로그인 ID (소문자 정규화)
    password_hash TEXT NOT NULL,          -- pbkdf2_sha256$iter$salt$hash
    is_active     INTEGER NOT NULL DEFAULT 1,
    is_admin      INTEGER NOT NULL DEFAULT 0,  -- 1이면 계정 관리(/api/admin/users) 사용 가능
    created_at    TEXT NOT NULL
);

-- ─────────────── 화면 마스터 (레버 · 테마) ───────────────
-- 레버 = 기대효과 Logic 템플릿. 산출식과 필요 기준값 항목만 제시하고 값은 현업이 입력한다.
CREATE TABLE IF NOT EXISTS lever (
    name       TEXT PRIMARY KEY,   -- 정비/TA, 에너지비, 물류비, 수율, 구매, 간접비, 운전자본
    metric     TEXT NOT NULL,      -- 관리지표 (TA 공기(일) ...)
    formula    TEXT NOT NULL,      -- 시스템 제안 산출식
    fields     TEXT NOT NULL,      -- 기준값 입력 항목 JSON 배열 [{k,l,u,ph,hint}]
    sort_order INTEGER NOT NULL DEFAULT 0,
    kb_query    TEXT,                    -- 내부 지식 베이스 검색 질의어(공백 구분 명사). 비면 name 을 그대로 질의
    impact_base REAL NOT NULL DEFAULT 3.0 -- 평가 임팩트 기준값 1.0~5.0
);

-- 레버 표기 변형 → 정식 레버명 매핑.
-- proposal.lever 가 lever(name) FK 이고 PRAGMA foreign_keys=ON 이라
-- LLM·혁신사례가 쓰는 변형 표기('정비·TA', '간접비/가동률' ...)는 그대로 넣으면 INSERT 가 실패한다.
-- 저장 직전 이 표로 정식명을 찾아 치환한다.
CREATE TABLE IF NOT EXISTS lever_alias (
    alias TEXT PRIMARY KEY,                       -- LLM·혁신사례가 쓰는 표기 변형
    lever TEXT NOT NULL REFERENCES lever(name)    -- lever 마스터 정식명
);

-- 트렌드 테마 = 자료를 묶어 보는 축. 레버 체계와 대응한다.
CREATE TABLE IF NOT EXISTS theme (
    name       TEXT PRIMARY KEY,
    color      TEXT NOT NULL,      -- 강조색
    bg         TEXT NOT NULL,      -- 배경색
    head       TEXT NOT NULL,      -- 한 줄 헤드라인
    body       TEXT NOT NULL,      -- 해설 문단
    sort_order INTEGER NOT NULL DEFAULT 0
);

-- ─────────────── 지식 파밍 결과 (크롤링·PDF·LLM·엔티티) ───────────────
CREATE TABLE IF NOT EXISTS feed_item (
    id           TEXT PRIMARY KEY,
    published_on TEXT NOT NULL,               -- YYYY-MM-DD
    kind         TEXT NOT NULL REFERENCES source_kind(key),
                                              -- 화면 축 6종(disclosure/earnings/ir/market/assoc/news), adhoc·periodic·sec 는 레거시
    source       TEXT NOT NULL,               -- 발표 주체 (롯데케미칼, Dow ...)
    title        TEXT NOT NULL,
    summary      TEXT NOT NULL,               -- LLM 정제 시 단일 문단 3문장 90~160자(개조식), 아니면 naive 절삭
    url          TEXT,                         -- 원문 링크 (근거 추적용)
    farmed_at    TEXT,                         -- 파밍 시각 (ISO). NULL이면 시드 데이터
    -- ── 화면(트렌드룸·근거 카드) 표시용 ──
    kind_label   TEXT,                         -- 원문 자료명 그대로 (Earnings call, 결산설명회 ...). NULL 이면 source_kind.label
    theme        TEXT REFERENCES theme(name),  -- 트렌드 테마 배정 결과
    biz_hint     TEXT,                         -- 참조 과제가 없을 때 쓰는 사업분야 fallback
    is_new       INTEGER NOT NULL DEFAULT 0,   -- 1이면 화면에 NEW 배지
    -- ── LLM 정제 결과 (farming/llm.py). 미정제 시 NULL/0 ──
    levers       TEXT,                         -- 비용 절감 / 수익 증대 / 운영 효율 (콤마 결합)
    importance   INTEGER,                      -- 0~100. 대시보드 top-n 선정 기준
    reason       TEXT,                         -- 중요도 판단 근거 1문장
    case_worthy  INTEGER NOT NULL DEFAULT 0,   -- 1이면 kb_innovation_case 승격 후보
    enriched     INTEGER NOT NULL DEFAULT 0,   -- 1이면 LLM 정제 성공
    -- ── 표시용 라벨·지표 (원문 값은 위쪽 source/title 에 그대로 보존) ──
    source_label   TEXT,                          -- 화면 표기용 발표 주체 (LLM org). 비면 source 로 폴백
    title_label    TEXT,                          -- 화면 표기용 한국어 한 줄 제목. 비면 title 로 폴백
    publisher      TEXT,                          -- 매체·발행처 (연합뉴스 / Reuters / SEC EDGAR / DART)
    metrics        TEXT NOT NULL DEFAULT '[]',    -- 핵심 지표 JSON 배열 [{label,value,period}] 최대 3개
    evidence_grade TEXT NOT NULL DEFAULT '제목만', -- 원문 확보 / 요약문 / 제목만
    brief          TEXT                           -- 트렌드룸 브리핑 1~2문장(LLM 전용).
                                                  -- reason(중요도 판단 근거)과 목적이 다르다 — 섞지 마라.
);

CREATE TABLE IF NOT EXISTS feed_item_tag (
    feed_id  TEXT NOT NULL REFERENCES feed_item(id) ON DELETE CASCADE,
    aff_code TEXT NOT NULL REFERENCES affiliate(code),
    PRIMARY KEY (feed_id, aff_code)
);

-- 자료별 동향 키워드 (화면 EV_KW). 사전 기반 추출(pipeline/farming/keywords.py)이 주(主)고
-- LLM 정제 결과가 있으면 앞자리를 덮는다. seq 0..3 = 화면 표기 순서.
-- ★ feed_item.levers 로 대신하지 마라 — 값이 '비용 절감/수익 증대/운영 효율' 3종뿐이라
--   화면이 기대하는 동향 키워드('정기보수','통합 조달' ...)와 입도가 완전히 다르다.
CREATE TABLE IF NOT EXISTS feed_item_keyword (
    feed_id TEXT NOT NULL REFERENCES feed_item(id) ON DELETE CASCADE,
    keyword TEXT NOT NULL,
    seq     INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (feed_id, keyword)
);

CREATE INDEX IF NOT EXISTS idx_fik_kw ON feed_item_keyword(keyword);

-- 일자별 키워드 등장 건수 스냅샷 (화면 KW_TREND 의 전일 대비 증감 원천).
-- 파밍 실행 끝에 그날치를 1회 갱신한다. distinct day 가 1개 이하면 증감은 {} 로 내린다.
CREATE TABLE IF NOT EXISTS keyword_daily (
    day     TEXT NOT NULL,   -- YYYY-MM-DD
    keyword TEXT NOT NULL,
    n       INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (day, keyword)
);

-- ─────────────── 지식 기반 (정제된 계열사 지식) ───────────────
-- ★ kb_business 는 **현역이다.** prefetch._profile_block 이 계열사 프로필 블록을
--   여기서 만든다 — 지우면 모든 발굴이 OperationalError 로 죽는다.
--   시드는 app/db/seed_trendroom.AFFILIATE_BUSINESS(계열사 9곳).
-- ★ kb_process · kb_technology · kb_kpi_benefit 은 제거했다 — 정의만 있고 3개 다
--   전량 0행이었으며 INSERT 하는 코드도 SELECT 하는 코드도 0건이었다.
--   (지식은 파일 KB(knowledge/<회사>/)와 kb_innovation_case 로 들어온다.)
CREATE TABLE IF NOT EXISTS kb_business (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    aff_code   TEXT NOT NULL REFERENCES affiliate(code),
    summary    TEXT NOT NULL,
    updated_on TEXT
);


-- 혁신 사례 모음 (큐레이션 대상). 3층 구조:
--   source_type = manual(사람이 직접) / ai(AI 추출·사람 검토대기) / auto(자동 후보)
--   status      = approved(승인·사용) / pending(검토대기) / rejected(반려)
-- 적용 계열사는 다대다이므로 kb_case_affiliate 로 연결.
CREATE TABLE IF NOT EXISTS kb_innovation_case (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    title        TEXT NOT NULL,               -- 사례명
    category     TEXT,                        -- 레버 분류 (에너지비/정비·TA/물류비/수율/구매/간접비/운전자본 ...)
    background   TEXT,                        -- 배경·사례 내용
    effect       TEXT,                        -- 기대효과 (정량 방향성)
    kpi_name     TEXT,                        -- KPI 지표명
    kpi_formula  TEXT,                        -- KPI 산출식
    source_org   TEXT,                        -- 사례 주체 (미쓰이화학, CATL, McKinsey ...)
    source_type  TEXT NOT NULL DEFAULT 'manual',    -- manual / ai / auto
    source_ref   TEXT,                        -- 근거 링크 또는 feed_item.id
    status       TEXT NOT NULL DEFAULT 'approved',  -- approved / pending / rejected
    created_at   TEXT
);

CREATE TABLE IF NOT EXISTS kb_case_affiliate (
    case_id  INTEGER NOT NULL REFERENCES kb_innovation_case(id) ON DELETE CASCADE,
    aff_code TEXT NOT NULL REFERENCES affiliate(code),
    PRIMARY KEY (case_id, aff_code)
);




-- ─────────────── 과제 제안 (화면 "과제 제안" 목록) ───────────────
-- 재생성할 때마다 gen_version 이 하나 쌓이고, 그 버전에 속한 proposal 이 붙는다.
CREATE TABLE IF NOT EXISTS gen_version (
    id         TEXT PRIMARY KEY,           -- g1 ... g12, 재생성분은 n1 ...
    label      TEXT NOT NULL,              -- 생성일 YYYY-MM-DD
    trigger    TEXT,                       -- "외부 자료 64건 갱신"
    created_at TEXT,
    sort_order INTEGER NOT NULL DEFAULT 0, -- 클수록 최신
    source     TEXT NOT NULL DEFAULT '시드',  -- 시드 / AI생성 / 후보풀
    model      TEXT                            -- 사용한 provider/모델. 폴백이면 NULL
);

CREATE TABLE IF NOT EXISTS proposal (
    id         INTEGER PRIMARY KEY,        -- 화면에서 그대로 쓰는 과제 번호
    ver_id     TEXT NOT NULL REFERENCES gen_version(id) ON DELETE CASCADE,
    aff_code   TEXT NOT NULL REFERENCES affiliate(code),
    lever      TEXT NOT NULL REFERENCES lever(name),
    name       TEXT NOT NULL,              -- 과제명
    summary    TEXT,                       -- 한 줄 요약(벤치마크 → 적용 대상)
    plan       TEXT,                       -- 적용 방안
    origin     TEXT NOT NULL DEFAULT '자동',  -- 자동 / 커스텀 / AI생성
    created_at TEXT,
    -- ── 발굴 LLM 산출 본문 (기존 행은 NULL. 백필하지 않는다) ──
    background  TEXT,                          -- 배경 2문장, 각 '~다.' 종결, 합계 60~140자
    risk        TEXT,                          -- 핵심 리스크 1문장, '~다.' 종결, 25~70자
    effect      TEXT,                          -- 기대효과 1문장, 숫자/% 포함, 금액 금지, 20~60자
    kpi_name    TEXT,                          -- 과제별 관리지표명. NULL 이면 읽기 시점에 lever.metric 폴백
    kpi_formula TEXT,                          -- 과제별 KPI 산출식. NULL 이면 읽기 시점에 lever.formula 폴백
    -- ── 검수 상태 · 중복 차단 · 내부 근거 ──
    status      TEXT NOT NULL DEFAULT '검토중', -- 검토중 / 채택 / 보류 / 반려 (사람의 결정. 평가 verdict 와 다른 개념)
    name_key    TEXT,                          -- 중복 차단용 정규화 과제명 (공백·[·/()-] 제거 후 소문자)
    kb_refs     TEXT                           -- 근거로 쓴 내부 지식 문서 id 콤마 결합 (외부 근거는 proposal_evidence)
);

CREATE TABLE IF NOT EXISTS proposal_evidence (
    proposal_id INTEGER NOT NULL REFERENCES proposal(id) ON DELETE CASCADE,
    feed_id     TEXT NOT NULL REFERENCES feed_item(id) ON DELETE CASCADE,
    PRIMARY KEY (proposal_id, feed_id)
);

-- 재생성 시 꺼내 쓰는 후보 풀. used_at 이 오래된 순으로 소진한다.
CREATE TABLE IF NOT EXISTS proposal_pool (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    aff_code TEXT NOT NULL REFERENCES affiliate(code),
    lever    TEXT NOT NULL REFERENCES lever(name),
    name     TEXT NOT NULL,
    summary  TEXT,
    plan     TEXT,
    evidence TEXT,                          -- feed_item.id 콤마 결합
    used_at  TEXT                           -- NULL 이면 아직 안 쓴 후보
);

-- ─────────────── 사용자별 작업 상태 ───────────────
-- 평가·기준값·수식은 사람마다 다르므로 email 로 분리 저장한다.
-- ★ star(사용자 별점 0~5, 사람이 매김)와 proposal_evaluation.priority(AI 채점 0~100)는
--   **완전히 다른 개념**이다. 한 컬럼에 섞지 마라. 이름을 score 로 되돌리지도 마라 —
--   둘 다 score 로 불리던 시절에 화면·API 에서 계속 혼동됐다.
CREATE TABLE IF NOT EXISTS proposal_feedback (
    user_email  TEXT NOT NULL,
    proposal_id INTEGER NOT NULL REFERENCES proposal(id) ON DELETE CASCADE,
    star        INTEGER NOT NULL DEFAULT 0,   -- 사용자 별점 0~5
    memo        TEXT NOT NULL DEFAULT '',
    updated_at  TEXT,
    PRIMARY KEY (user_email, proposal_id)
);

CREATE TABLE IF NOT EXISTS proposal_input (
    user_email  TEXT NOT NULL,
    proposal_id INTEGER NOT NULL REFERENCES proposal(id) ON DELETE CASCADE,
    fields      TEXT NOT NULL DEFAULT '{}',   -- {필드키: 입력값} JSON
    PRIMARY KEY (user_email, proposal_id)
);

CREATE TABLE IF NOT EXISTS proposal_formula (
    user_email  TEXT NOT NULL,
    proposal_id INTEGER NOT NULL REFERENCES proposal(id) ON DELETE CASCADE,
    sys_off     INTEGER NOT NULL DEFAULT 0,   -- 1이면 시스템 제안 산출식 OFF
    text        TEXT,                         -- 사용자가 고친 산출식
    updated_at  TEXT,
    PRIMARY KEY (user_email, proposal_id)
);

-- ─────────────── 과제 평가 (기계 검증 · 채점) ───────────────
-- 과제 1건의 평가 1회 = 1행. 덮어쓰지 않고 이력으로 쌓는다.
-- 가중치·프롬프트를 바꾸면 '바꾸기 전 점수' 와 비교해야 튜닝을 검증할 수 있기 때문이다.
-- 최신 평가는 is_latest=1 행 하나뿐이며 부분 유니크 인덱스(idx_pev_latest)가 이를 강제한다.
-- 저장 코드는 반드시 한 트랜잭션 안에서 is_latest=0 UPDATE → INSERT 순서를 지켜야 한다.
CREATE TABLE IF NOT EXISTS proposal_evaluation (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    proposal_id      INTEGER NOT NULL REFERENCES proposal(id) ON DELETE CASCADE,
    evaluated_at     TEXT NOT NULL,                 -- 평가 시각 (ISO)
    verdict          TEXT NOT NULL,                 -- 통과 / 검토필요 / 차단
    priority         REAL NOT NULL DEFAULT 0,       -- 0~100 우선순위 점수
    grade            TEXT NOT NULL DEFAULT 'C',     -- A / B / C
    rank_in_aff      INTEGER,                       -- **계열사 내** 순위(1부터). 차단이면 NULL.
                                                    -- 채점·중복검사가 계열사 단위라 배치 전체 순위는 의미가 없다
                                                    -- (한 배치에 1위가 계열사 수만큼 생긴다).
    impact_score     REAL NOT NULL DEFAULT 0,       -- 임팩트 1.0~5.0
    impact_reason    TEXT NOT NULL DEFAULT '',
    feas_score       REAL NOT NULL DEFAULT 0,       -- 실현가능성 1.0~5.0
    feas_reason      TEXT NOT NULL DEFAULT '',
    roi_score        REAL NOT NULL DEFAULT 0,       -- ROI 1.0~5.0
    roi_reason       TEXT NOT NULL DEFAULT '',
    grounding        TEXT NOT NULL DEFAULT '미확인', -- 뒷받침 / 느슨함 / 무관 / 미확인
    grounding_reason TEXT NOT NULL DEFAULT '',
    scored_by        TEXT NOT NULL DEFAULT '규칙',   -- LLM / 규칙 / 미채점
    weights          TEXT NOT NULL DEFAULT '{}',    -- 채점 당시 가중치 JSON (재현용)
    batch_id         TEXT,                          -- 같은 실행에서 나온 평가 묶음 id
    is_latest        INTEGER NOT NULL DEFAULT 1     -- 1이면 이 과제의 최신 평가
);

-- 검증 이슈 1건 = 1행. 과제당 0~n개라 proposal_evaluation 에 컬럼으로 넣을 수 없다.
CREATE TABLE IF NOT EXISTS proposal_evaluation_issue (
    eval_id  INTEGER NOT NULL REFERENCES proposal_evaluation(id) ON DELETE CASCADE,
    seq      INTEGER NOT NULL,               -- 표시 순서 (0부터)
    code     TEXT NOT NULL,                  -- MISSING_FIELD / NO_EVIDENCE / DUPLICATE / STALE_EVIDENCE ...
    severity TEXT NOT NULL,                  -- 차단 / 경고
    field    TEXT NOT NULL DEFAULT '',       -- title / plan / evidence / kpi / category
    message  TEXT NOT NULL,                  -- 화면에 그대로 노출하는 한국어 설명
    PRIMARY KEY (eval_id, seq)
);

-- 별점·피드백 1회 저장 = 1행 (append-only, 덮어쓰지 않는다).
-- proposal_feedback 은 '지금 값'(화면 왕복용), 이 테이블은 '언제 어떤 문장을 보고 몇 점을 줬는가'.
--
-- ★ proposal_id 에 일부러 FK 를 걸지 않는다 — 지우지 말 것.
--   proposal 은 gen_version 에 ON DELETE CASCADE 로 매달려 있어 생성 버전 하나만 지워도
--   피드백이 통째로 증발한다. 이 테이블은 프롬프트 되먹임의 학습 데이터라 과제가 사라져도 남아야 한다.
--   그래서 과제 본문을 스냅샷으로 함께 저장한다. 고아 행이 쌓이는 것은 의도한 동작이며,
--   '참조 무결성 정리' 를 이유로 FK 를 추가하거나 orphan 행을 삭제하면 축적된 학습 데이터가 날아간다.
CREATE TABLE IF NOT EXISTS proposal_feedback_log (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email    TEXT NOT NULL,
    proposal_id   INTEGER NOT NULL,              -- 일부러 FK 를 걸지 않는다 (위 설명 참조)
    star          INTEGER,                       -- 0~5. NULL 이면 이번엔 메모만 바꿈
    memo          TEXT NOT NULL DEFAULT '',
    created_at    TEXT NOT NULL,
    -- 별점을 매긴 시점의 과제 스냅샷
    ver_id        TEXT NOT NULL DEFAULT '',
    aff_code      TEXT NOT NULL DEFAULT '',
    lever         TEXT NOT NULL DEFAULT '',
    name          TEXT NOT NULL DEFAULT '',
    summary       TEXT NOT NULL DEFAULT '',
    plan          TEXT NOT NULL DEFAULT '',
    origin        TEXT NOT NULL DEFAULT '',
    evidence_ids  TEXT NOT NULL DEFAULT '',      -- feed_item.id 콤마 결합
    -- 그 시점의 평가 결과
    eval_id       INTEGER,                       -- proposal_evaluation.id (미평가면 NULL)
    eval_grade    TEXT NOT NULL DEFAULT '',
    eval_priority REAL
);

-- ─────────────── AI Reporting 설정 ───────────────
CREATE TABLE IF NOT EXISTS report_setting (
    user_email TEXT PRIMARY KEY,
    freq       TEXT NOT NULL DEFAULT '매일',   -- 매일 / 주 3회 / 주 1회
    send_time  TEXT NOT NULL DEFAULT '08:00',
    channels   TEXT NOT NULL DEFAULT '{"outlook":true,"teams":true}',
    last_at    TEXT
);

CREATE TABLE IF NOT EXISTS report_recipient (
    user_email TEXT NOT NULL,
    label      TEXT NOT NULL,                 -- "O/I추진단 (jin.k@sk.com)"
    PRIMARY KEY (user_email, label)
);

-- 발송에서 뺀 과제 (기본은 전체 포함)
CREATE TABLE IF NOT EXISTS report_exclude (
    user_email  TEXT NOT NULL,
    proposal_id INTEGER NOT NULL REFERENCES proposal(id) ON DELETE CASCADE,
    PRIMARY KEY (user_email, proposal_id)
);

-- ─────────────── 관리자 화면 ───────────────
CREATE TABLE IF NOT EXISTS crawl_source (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    url         TEXT,
    type        TEXT,                          -- 고정 URL / 키워드
    paid        INTEGER NOT NULL DEFAULT 0,
    last_at     TEXT,                          -- 마지막 수집 표시 문자열
    doc_count   INTEGER NOT NULL DEFAULT 0,
    fresh_count INTEGER NOT NULL DEFAULT 0,
    status      TEXT NOT NULL DEFAULT '정상',   -- 정상 / 지연 / 계정 필요
    sort_order  INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS upload_file (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    aff         TEXT,                          -- 전사 또는 계열사명
    size        TEXT,
    uploaded_at TEXT,
    status      TEXT NOT NULL DEFAULT '검수 대기',
                -- 검수 대기 / 본문 추출됨 / 본문 미지원 / 검수 완료
                -- (검수 완료 + extracted_at NOT NULL 인 행만 RAG 투입)
    body        TEXT,                        -- 추출한 평문 본문. 최대 300,000자. 미지원 포맷은 NULL
                                             -- 이 값은 bootstrap 페이로드에 절대 넣지 않는다
    chars       INTEGER NOT NULL DEFAULT 0,  -- 추출 글자 수. 0 이면 추출 실패 또는 미지원
    extracted_at TEXT                        -- 본문 추출 완료 시각(ISO). NULL 이면 추출 전
);

-- ★ admin_member 는 제거했다. 화면 '관리자 명단' 표시용 별도 테이블이었는데,
--   새 계정 관리 탭은 **로그인 계정 자체**(app_user.is_admin)를 관리한다.
--   두 개를 같이 두면 "관리자 명단에는 있는데 로그인은 안 되는 계정" 이 생긴다.
--   기존 DB 의 테이블은 seed._DROPS 가 지운다(여기서만 지우면 executescript 가 도로 만든다).

-- ─────────────── 비동기 작업 ───────────────
-- LLM 발굴은 계열사 1곳당 1분 내외라 HTTP 응답으로 붙잡고 있을 수 없다
-- (nginx 기본 proxy_read_timeout 60초 · Cloudflare 100초에서 끊긴다).
-- 요청은 작업을 만들고 즉시 id 를 돌려주며, 화면이 상태를 폴링한다.
-- 상태를 메모리가 아니라 DB 에 두는 이유: uvicorn 워커가 여럿이면 폴링 요청이
-- 작업을 시작한 워커가 아닌 곳으로 갈 수 있기 때문이다.
CREATE TABLE IF NOT EXISTS job (
    id          TEXT PRIMARY KEY,                 -- 무작위 토큰
    kind        TEXT NOT NULL,                    -- regenerate / evaluate ...
    status      TEXT NOT NULL DEFAULT 'running',  -- running / done / failed
    result      TEXT,                             -- 완료 시 응답 JSON
    error       TEXT,                             -- 실패 시 사용자에게 보일 한국어 사유
    created_at  TEXT NOT NULL,
    finished_at TEXT
);

-- 전역 설정 (생성 인스트럭션 등)
CREATE TABLE IF NOT EXISTS app_setting (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- 관심 종목 시세 캐시 (공공데이터포털 금융위원회_주식시세정보).
-- ★ 성능용 캐시가 아니다. 외부 API 가 죽거나 키가 만료돼도 티커가 비지 않게 하는 것이 목적이다.
--   그래서 기준일별로 누적한다(덮어쓰지 않는다) — 나중에 추세를 그리려면 그대로 쓰면 된다.
-- ★ app/market.py 가 첫 사용 시 CREATE TABLE IF NOT EXISTS 로 한 번 더 보장한다.
--   schema.sql 을 다시 돌리지 않은 기존 DB 를 위해서다. 둘 다 있는 것이 맞다.
CREATE TABLE IF NOT EXISTS quote_daily (
    code       TEXT    NOT NULL,
    bas_dt     TEXT    NOT NULL,              -- 'YYYYMMDD' (금융위 basDt 원형)
    name       TEXT    NOT NULL,
    close      INTEGER NOT NULL,              -- 종가(원)
    diff       INTEGER NOT NULL,              -- 전일 대비(원)
    rate       REAL    NOT NULL,              -- 등락률(%)
    fetched_at TEXT    NOT NULL,              -- 우리가 받아 온 시각(UTC ISO)
    PRIMARY KEY (code, bas_dt)
);

-- ─────────────── 집계 뷰 ───────────────
-- 계열사·레버별 평균 별점. score>0 조건으로 '메모만 남기고 별점은 안 준' 행을 제외한다.
-- 규모가 작아 캐시 테이블 대신 뷰로 둔다.
CREATE VIEW IF NOT EXISTS v_feedback_by_lever AS
SELECT p.aff_code, p.lever,
       COUNT(*)                                                AS n,
       ROUND(AVG(f.star), 2)                                    AS avg_star,
       SUM(CASE WHEN f.star BETWEEN 1 AND 2 THEN 1 ELSE 0 END)  AS low_n,
       SUM(CASE WHEN f.star >= 4 THEN 1 ELSE 0 END)             AS high_n
FROM proposal_feedback f
JOIN proposal p ON p.id = f.proposal_id
WHERE f.star > 0
GROUP BY p.aff_code, p.lever;

-- ─────────────── 인덱스 ───────────────
-- 원칙: **실제로 도는 쿼리의 WHERE/JOIN 만** 만든다. 인덱스는 공짜가 아니라 INSERT 마다
-- 갱신 비용이고, 안 쓰이는 인덱스는 "이 컬럼으로 조회하는 코드가 있다" 는 거짓 신호가 된다.
-- ★ 제거한 6개(idx_feed_importance · idx_feed_case_worthy · idx_feed_theme ·
--   idx_proposal_status · idx_proposal_aff · idx_pev_batch)는 어느 쿼리에도 안 쓰였다.
--   되살리기 전에 실제 SELECT 를 먼저 찾을 것. 기존 DB 의 것은 seed._DROP_INDEXES 가 지운다.
CREATE INDEX IF NOT EXISTS idx_feed_published ON feed_item(published_on);
CREATE INDEX IF NOT EXISTS idx_feed_tag_aff   ON feed_item_tag(aff_code);
CREATE INDEX IF NOT EXISTS idx_case_status    ON kb_innovation_case(status);
CREATE INDEX IF NOT EXISTS idx_case_aff       ON kb_case_affiliate(aff_code);
CREATE INDEX IF NOT EXISTS idx_proposal_ver   ON proposal(ver_id);
-- ★ 저장 직전 같은 계열사 내 동일 과제명 검사이자 **제약**이다(store.name_key_exists /
--   find_by_name_key). 커스텀 생성이 같은 과제를 반복 INSERT 하는 것을 DB 층에서
--   물리적으로 막는다 — 파이썬 사전검사는 동시 job 두 개를 막지 못한다.
--   지우지 마라: 없으면 재생성 1건마다 proposal 전체를 풀스캔한다.
--   기존 중복 행은 seed._disambiguate_proposal_name_key 가 늦은 쪽 키에 '#id' 를 붙여
--   해소한 뒤에 이 인덱스를 만든다(행은 지우지 않는다).
-- ★ 부분조건에 `AND name_key <> ''` 를 절대 붙이지 마라 — SQLite 가 부분 인덱스를 못 쓰고
--   조회가 풀스캔이 된다(EXPLAIN QUERY PLAN 실측: SEARCH → SCAN).
CREATE UNIQUE INDEX IF NOT EXISTS idx_proposal_namekey ON proposal(aff_code, name_key)
    WHERE name_key IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_pev_proposal ON proposal_evaluation(proposal_id, id DESC);
-- ★ 과제 1건당 is_latest=1 행이 정확히 하나임을 DB 가 강제한다(최신 평가를 LEFT JOIN 1회로
--   조회). 제약이지 성능 인덱스가 아니다 — 지우면 _proposals 의 LEFT JOIN 이 행을 곱한다.
CREATE UNIQUE INDEX IF NOT EXISTS idx_pev_latest ON proposal_evaluation(proposal_id) WHERE is_latest = 1;
CREATE INDEX IF NOT EXISTS idx_pfl_proposal ON proposal_feedback_log(proposal_id);
CREATE INDEX IF NOT EXISTS idx_pfl_lever    ON proposal_feedback_log(aff_code, lever);

-- FK 자식 인덱스 — proposal 삭제 시 SQLite 가 ON DELETE CASCADE 를 처리하려고
-- 자식 테이블을 proposal_id 로 훑는다. 인덱스가 없으면 그때마다 자식 전량 풀스캔이다
-- (PK 가 (user_email, proposal_id) 라 선두 컬럼이 user_email 이어서 PK 인덱스가 안 먹는다).
CREATE INDEX IF NOT EXISTS idx_pfb_proposal  ON proposal_feedback(proposal_id);
CREATE INDEX IF NOT EXISTS idx_pin_proposal  ON proposal_input(proposal_id);
CREATE INDEX IF NOT EXISTS idx_pfx_proposal  ON proposal_formula(proposal_id);
CREATE INDEX IF NOT EXISTS idx_rex_proposal  ON report_exclude(proposal_id);
