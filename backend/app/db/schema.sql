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

CREATE TABLE IF NOT EXISTS kb_innovation_case (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    aff_code    TEXT REFERENCES affiliate(code),
    title       TEXT NOT NULL,
    description TEXT,
    source      TEXT
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
