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
    code TEXT PRIMARY KEY,     -- SKE, SKGC ...
    name TEXT NOT NULL,
    biz  TEXT NOT NULL REFERENCES biz_segment(key)
);

CREATE TABLE IF NOT EXISTS source_kind (
    key       TEXT PRIMARY KEY,   -- adhoc / periodic / sec / news
    label     TEXT NOT NULL,
    css_class TEXT NOT NULL
);

-- ─────────────── 인증 (사용자 계정) ───────────────
-- 관리자가 seed 로 등록. email(=Outlook) 이 로그인 ID, 초기 비밀번호는 해시로 저장.
CREATE TABLE IF NOT EXISTS app_user (
    email         TEXT PRIMARY KEY,       -- Outlook 이메일 = 로그인 ID (소문자 정규화)
    password_hash TEXT NOT NULL,          -- pbkdf2_sha256$iter$salt$hash
    is_active     INTEGER NOT NULL DEFAULT 1,
    is_admin      INTEGER NOT NULL DEFAULT 0,   -- 관리자 여부 (사용자 관리 권한)
    created_at    TEXT NOT NULL
);

-- ─────────────── 지식 파밍 결과 (크롤링·PDF·LLM·엔티티) ───────────────
CREATE TABLE IF NOT EXISTS feed_item (
    id           TEXT PRIMARY KEY,
    published_on TEXT NOT NULL,               -- YYYY-MM-DD
    kind         TEXT NOT NULL REFERENCES source_kind(key),
    source       TEXT NOT NULL,               -- 발표 주체 (롯데케미칼, Dow ...)
    title        TEXT NOT NULL,
    summary      TEXT NOT NULL,
    url          TEXT,                         -- 원문 링크 (근거 추적용)
    farmed_at    TEXT                          -- 파밍 시각 (ISO). NULL이면 시드 데이터
);

CREATE TABLE IF NOT EXISTS feed_item_tag (
    feed_id  TEXT NOT NULL REFERENCES feed_item(id) ON DELETE CASCADE,
    aff_code TEXT NOT NULL REFERENCES affiliate(code),
    PRIMARY KEY (feed_id, aff_code)
);

-- ─────────────── 지식 기반 (정제된 계열사 지식) ───────────────
CREATE TABLE IF NOT EXISTS kb_business (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    aff_code   TEXT NOT NULL REFERENCES affiliate(code),
    summary    TEXT NOT NULL,
    updated_on TEXT
);

CREATE TABLE IF NOT EXISTS kb_process (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    aff_code    TEXT NOT NULL REFERENCES affiliate(code),
    name        TEXT NOT NULL,
    description TEXT
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

CREATE TABLE IF NOT EXISTS kb_technology (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    aff_code    TEXT REFERENCES affiliate(code),
    name        TEXT NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS kb_kpi_benefit (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    aff_code TEXT REFERENCES affiliate(code),
    name     TEXT NOT NULL,
    formula  TEXT,
    benefit  TEXT
);

-- ─────────────── 과제 기록 (발굴·평가·저장 결과) ───────────────
CREATE TABLE IF NOT EXISTS task (
    id          TEXT PRIMARY KEY,             -- OI-000001
    created_at  TEXT NOT NULL,
    aff_code    TEXT NOT NULL REFERENCES affiliate(code),
    title       TEXT NOT NULL,
    category    TEXT,
    background  TEXT,
    plan        TEXT,
    risk        TEXT,
    effect      TEXT,
    kpi_name    TEXT,
    kpi_formula TEXT,
    status      TEXT DEFAULT '검토중',        -- 검토중 / 채택 / 보류 ...
    origin      TEXT                          -- 생성 / 봇 / 수기
);

CREATE TABLE IF NOT EXISTS task_evidence (
    task_id TEXT NOT NULL REFERENCES task(id) ON DELETE CASCADE,
    feed_id TEXT NOT NULL,                    -- feed_item.id (파밍 근거)
    PRIMARY KEY (task_id, feed_id)
);

CREATE INDEX IF NOT EXISTS idx_feed_published ON feed_item(published_on);
CREATE INDEX IF NOT EXISTS idx_feed_tag_aff   ON feed_item_tag(aff_code);
CREATE INDEX IF NOT EXISTS idx_task_aff       ON task(aff_code);
CREATE INDEX IF NOT EXISTS idx_case_status    ON kb_innovation_case(status);
CREATE INDEX IF NOT EXISTS idx_case_aff       ON kb_case_affiliate(aff_code);
