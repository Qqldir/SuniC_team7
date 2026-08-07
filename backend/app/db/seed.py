"""DB 초기화 + 데모 데이터 주입.

    python -m app.db.seed          # 스키마 생성 후 마스터/화면 데이터 시드
    python -m app.db.seed --reset  # 기존 DB 삭제 후 재생성

화면(O/I Spark)이 쓰는 데이터는 app/db/seed_trendroom.py 가 담당하고,
여기서는 스키마 생성·마이그레이션과 혁신 사례 시드를 맡습니다.
"""
import sys
from pathlib import Path

from app.config import DB_PATH, TODAY
from app.db.database import get_connection
from app.db import seed_data as S
from app.db import seed_trendroom

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


# schema.sql 에 나중에 추가된 컬럼 — 기존 DB 를 --reset 없이 따라가게 합니다.
# CREATE TABLE IF NOT EXISTS 는 이미 있는 테이블을 갱신하지 않기 때문입니다.
#
# ★ 테이블당 키는 하나뿐입니다. 같은 테이블 이름을 두 번 적으면 뒤엣것이 앞엣것을 덮어
#   앞의 컬럼들이 조용히 누락됩니다. 컬럼을 더할 때는 반드시 기존 리스트에 append 하세요.
_MIGRATIONS = {
    "feed_item": [
        ("levers", "TEXT"),
        ("importance", "INTEGER"),
        ("reason", "TEXT"),
        ("case_worthy", "INTEGER NOT NULL DEFAULT 0"),
        ("enriched", "INTEGER NOT NULL DEFAULT 0"),
        # 화면 표시용
        ("kind_label", "TEXT"),
        ("theme", "TEXT"),
        ("biz_hint", "TEXT"),
        ("is_new", "INTEGER NOT NULL DEFAULT 0"),
        # 표시용 라벨·지표 (원문 source/title 은 그대로 보존)
        ("source_label", "TEXT"),
        ("title_label", "TEXT"),
        ("publisher", "TEXT"),
        ("metrics", "TEXT NOT NULL DEFAULT '[]'"),
        ("evidence_grade", "TEXT NOT NULL DEFAULT '제목만'"),
        ("brief", "TEXT"),                         # 트렌드룸 브리핑 1~2문장(LLM 전용)
    ],
    # ★ is_admin 을 여기 넣지 않으면 기존 DB(oi_scout.db)에 컬럼이 끝내 안 생기고
    #   deps.current_admin 의 SELECT 가 no such column 으로 500 을 낸다.
    #   프론트는 403 분기를 못 타서 원인이 화면에 드러나지 않는다.
    "app_user": [
        ("is_admin", "INTEGER NOT NULL DEFAULT 0"),
    ],
    "affiliate": [
        ("color", "TEXT"),
        ("sort_order", "INTEGER NOT NULL DEFAULT 0"),
        ("kb_company", "TEXT"),   # 내부 지식 베이스 디렉터리명. NULL 이면 KB 없음
    ],
    "lever": [
        ("kb_query", "TEXT"),                      # 내부 지식 검색 질의어
        ("impact_base", "REAL NOT NULL DEFAULT 3.0"),  # 평가 임팩트 기준값
    ],
    "upload_file": [
        ("body", "TEXT"),                          # 추출한 평문 본문
        ("chars", "INTEGER NOT NULL DEFAULT 0"),   # 추출 글자 수
        ("extracted_at", "TEXT"),                  # 본문 추출 완료 시각(ISO)
    ],
    "proposal": [
        ("background", "TEXT"),    # 배경 2문장
        ("risk", "TEXT"),          # 핵심 리스크 1문장
        ("effect", "TEXT"),        # 기대효과 1문장
        ("kpi_name", "TEXT"),      # 과제별 관리지표명
        ("kpi_formula", "TEXT"),   # 과제별 KPI 산출식
        ("status", "TEXT NOT NULL DEFAULT '검토중'"),  # 검수 상태
        ("name_key", "TEXT"),      # 중복 차단용 정규화 과제명
        ("kb_refs", "TEXT"),       # 근거로 쓴 내부 지식 문서 id
    ],
    "gen_version": [
        ("source", "TEXT NOT NULL DEFAULT '시드'"),  # 시드 / AI생성 / 후보풀
        ("model", "TEXT"),                           # 사용한 provider/모델
    ],
}


def create_schema(conn):
    # 마이그레이션이 먼저입니다. schema.sql 의 인덱스·뷰가 새 컬럼(proposal.name_key,
    # proposal.status ...)을 참조하므로, 기존 DB 에 컬럼이 없는 상태로 executescript 를
    # 돌리면 "no such column" 으로 죽습니다. 새 DB 에서는 테이블이 아직 없어
    # _migrate 가 전부 건너뛰고 executescript 가 스키마 전량을 만듭니다.
    _migrate(conn)
    # ★ 순서가 전부다. schema.sql 이 idx_proposal_namekey 를 **UNIQUE** 로 만들므로
    #   그 전에 ① name_key 를 채우고 ①' 정규화 규칙이 바뀌었으면 전량 재계산하고
    #   ② 옛 비-UNIQUE 인덱스를 떨구고 ③ 이미 쌓인 중복을 해소해야 한다. 하나라도
    #   빠지면 executescript 가
    #   'UNIQUE constraint failed: proposal.aff_code, proposal.name_key' 로 죽는다.
    backfill_name_key(conn)
    _recompute_name_key(conn)
    _upgrade_namekey_index(conn)
    _disambiguate_proposal_name_key(conn)
    _drop_legacy(conn)
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    # 규칙 개정 번호는 executescript 가 app_setting 을 만든 **뒤에** 기록한다
    # (새 DB 에는 이 시점까지 app_setting 테이블 자체가 없다).
    _mark_name_key_rev(conn)


_NAME_KEY_REV_SETTING = "name_key_rev"


def _table_exists(conn, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone() is not None


def _recompute_name_key(conn):
    """store.name_key 규칙이 바뀌었으면 기존 proposal 의 name_key 를 전량 재계산한다.

    ★ 왜 필요한가: 정규화 규칙을 바꿔도 **이미 저장된 행의 키는 옛 규칙 그대로**다.
      그러면 새 규칙으로 만든 키와 서로 안 걸려 중복 차단(L1·L3)이 조용히 뚫린다.
      실측으로 뚫렸던 구멍이 정확히 이것이다 — 과제명 끝에 마침표 하나.
    ★ UNIQUE 인덱스를 **먼저 떨군다.** 재계산은 서로 다른 옛 키를 같은 새 키로 모으므로
      인덱스가 걸린 채 UPDATE 하면 IntegrityError 로 죽는다. 새로 생긴 충돌은 바로
      뒤 _disambiguate_proposal_name_key 가 '#id' 로 해소하고, schema.sql 이 인덱스를
      다시 만든다. **행은 지우지 않는다.**
    ★ 멱등: app_setting 에 기록된 개정 번호가 store.NAME_KEY_REV 와 같으면 건너뛴다.
    """
    from app import store  # 순환 import 회피 — 정규화 규칙은 저장 계층이 단독 소유한다

    if not _table_exists(conn, "proposal"):
        return
    if _table_exists(conn, "app_setting"):
        row = conn.execute(
            "SELECT value FROM app_setting WHERE key = ?", (_NAME_KEY_REV_SETTING,)
        ).fetchone()
        if row and (row["value"] or "") == str(store.NAME_KEY_REV):
            return

    rows = conn.execute("SELECT id, name, name_key FROM proposal").fetchall()
    # '#id' 는 이전 마이그레이션이 붙인 중복 구분자다 — 이름에서 파생되지 않으므로
    # 재계산하면 사라진다. 그래야 아래 _disambiguate 가 새 기준으로 다시 붙인다.
    changed = [(store.name_key(r["name"]), r["id"])
               for r in rows if store.name_key(r["name"]) != (r["name_key"] or "")]
    if not changed:
        return
    if conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='index' AND name='idx_proposal_namekey'"
    ).fetchone():
        conn.execute("DROP INDEX idx_proposal_namekey")
    conn.executemany("UPDATE proposal SET name_key = ? WHERE id = ?", changed)
    print(f"마이그레이션: name_key 정규화 규칙 개정(rev {store.NAME_KEY_REV}) — "
          f"{len(changed)}행 재계산(행 유지)")


def _mark_name_key_rev(conn):
    """재계산이 끝났음을 기록한다(멱등 판정용). app_setting 이 생긴 뒤에만 부른다."""
    from app import store

    if not _table_exists(conn, "app_setting"):
        return
    conn.execute(
        "INSERT INTO app_setting(key, value) VALUES (?,?) "
        "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        (_NAME_KEY_REV_SETTING, str(store.NAME_KEY_REV)),
    )


def _upgrade_namekey_index(conn):
    """옛 비-UNIQUE idx_proposal_namekey 를 떨군다. schema.sql 이 UNIQUE 로 다시 만든다.

    CREATE ... IF NOT EXISTS 는 **이름만** 보므로, 이미 같은 이름의 일반 인덱스가 있으면
    조용히 건너뛰어 제약이 영원히 안 걸린다.
    """
    row = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='index' AND name='idx_proposal_namekey'"
    ).fetchone()
    if row and "UNIQUE" not in (row["sql"] or "").upper():
        conn.execute("DROP INDEX idx_proposal_namekey")
        print("마이그레이션: idx_proposal_namekey 를 UNIQUE 로 승격합니다(옛 인덱스 제거)")


def _disambiguate_proposal_name_key(conn):
    """(aff_code, name_key) 중복 그룹의 name_key 를 구분한다. **행은 지우지 않는다.**

    가장 이른 id 를 원본으로 두고 나머지 행의 name_key 뒤에만 '#id' 를 붙인다.
    ★ 왜 삭제하지 않나: 사용자가 만든 데이터이고, 무엇이 버릴 값인지 마이그레이션에는
      판단 근거가 없다. 키만 구분해도 원본이 클린 키를 유지하므로 새 중복 생성은 계속 막힌다.
    ★ 화면의 name 은 건드리지 않는다 — 중복 과제가 '…#1402' 로 보이면 안 된다.
    """
    if not conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='proposal'"
    ).fetchone():
        return
    groups = conn.execute(
        """SELECT aff_code, name_key, COUNT(*) AS n FROM proposal
            WHERE name_key IS NOT NULL
            GROUP BY aff_code, name_key HAVING n > 1"""
    ).fetchall()
    for g in groups:
        ids = [r["id"] for r in conn.execute(
            "SELECT id FROM proposal WHERE aff_code = ? AND name_key = ? ORDER BY id",
            (g["aff_code"], g["name_key"]),
        )]
        for pid in ids[1:]:
            conn.execute(
                "UPDATE proposal SET name_key = name_key || ? WHERE id = ?",
                (f"#{pid}", pid),
            )
        print(f"마이그레이션: {g['aff_code']} 중복 과제명 {g['n']}건 — "
              f"#{ids[0]} 를 원본으로 두고 {ids[1:]} 의 name_key 를 구분합니다(행 유지)")


# 이름을 바로잡은 컬럼 — ADD COLUMN 으로는 못 하므로 따로 처리한다.
# (테이블, 옛이름, 새이름)
_RENAMES = [
    # rank_in_batch 는 실제로 '계열사 내 순위' 다. 채점이 계열사 단위로 돌아
    # 한 배치에 1위가 계열사 수만큼 생겼다 — 이름이 값을 오해하게 만들었다.
    ("proposal_evaluation", "rank_in_batch", "rank_in_aff"),
    # ★ '점수' 가 두 개였다. 둘 다 이름이 score 라 코드·쿼리에서 섞이기 쉬웠다.
    #   사용자 별점(0~5, 사람이 매김)   → proposal_feedback(.log).star
    #   AI 채점(0~100, 기계가 매김)    → proposal_evaluation.priority (그대로)
    #   이름이 다르면 한 컬럼에 섞어 넣는 실수가 SQL 단계에서 바로 드러난다.
    ("proposal_feedback", "score", "star"),
    ("proposal_feedback_log", "score", "star"),
]


# 컬럼을 참조하는 뷰 — 리네임 전에 지운다. schema.sql 의 CREATE VIEW IF NOT EXISTS 가
# 뒤이어 새 정의로 다시 만든다. 지우지 않으면 옛 컬럼명을 가리키는 뷰가 그대로 남아
# SELECT 할 때만 "no such column" 으로 터진다(생성 시점에는 조용하다).
_VIEWS_TO_REBUILD = ["v_feedback_by_lever"]


# 제거된 테이블 — 기존 DB 에서도 정리한다.
# `task`/`task_evidence` 는 화면이 쓰지 않는 옛 과제 모델이고 `proposal` 로 완전히 대체됐다.
# 남겨 두면 "과제 테이블이 둘" 인 상태가 이어져 다음 사람이 어느 쪽을 봐야 할지 헷갈린다.
# `kb_process`/`kb_technology`/`kb_kpi_benefit` 은 정의만 있고 3개 다 전량 0행이었으며
# INSERT·SELECT 하는 코드가 0건이었다(지식은 파일 KB 와 kb_innovation_case 로 들어온다).
# `admin_member` 는 화면 표시용 관리자 명단이었는데, 계정 관리 탭이 로그인 계정
# (app_user.is_admin)을 직접 다루게 되면서 이중 명단이 됐다.
# ★ kb_business 는 여기 넣지 마라 — prefetch._profile_block 이 읽는 현역 테이블이다.
# ★ 여기에만 넣으면 안 된다. create_schema 가 _migrate → _drop_legacy → executescript 순이라
#   schema.sql 에 CREATE 문이 남아 있으면 드롭 직후 빈 테이블로 되살아난다. 두 곳을 같이 고칠 것.
_DROPS = [
    "task_evidence", "task",                              # FK 때문에 자식 테이블 먼저
    "kb_process", "kb_technology", "kb_kpi_benefit",
    "admin_member",
]

# 제거된 인덱스 — 어느 쿼리에도 안 쓰이는데 INSERT 마다 갱신 비용만 냈다.
# schema.sql 에서 CREATE 문을 지우는 것만으로는 **기존 DB 에서 사라지지 않는다**
# (CREATE INDEX IF NOT EXISTS 를 안 돌린다고 이미 만들어진 인덱스가 없어지지는 않는다).
# ★ idx_proposal_namekey(중복 검사)와 idx_pev_latest(최신 평가 유일성 제약)는 넣지 마라.
_DROP_INDEXES = [
    "idx_feed_importance", "idx_feed_case_worthy", "idx_feed_theme",
    "idx_proposal_status", "idx_proposal_aff", "idx_pev_batch",
]


def _drop_legacy(conn):
    for table in _DROPS:
        if conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)
        ).fetchone():
            conn.execute(f"DROP TABLE {table}")
            print(f"마이그레이션: 레거시 테이블 {table} 제거")
    for index in _DROP_INDEXES:
        if conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='index' AND name=?", (index,)
        ).fetchone():
            conn.execute(f"DROP INDEX {index}")
            print(f"마이그레이션: 미사용 인덱스 {index} 제거")


def _rename(conn):
    renamed = False
    for table, old, new in _RENAMES:
        cols = {r["name"] for r in conn.execute(f"PRAGMA table_info({table})")}
        if not cols or new in cols or old not in cols:
            continue
        if not renamed:
            for view in _VIEWS_TO_REBUILD:
                conn.execute(f"DROP VIEW IF EXISTS {view}")
            renamed = True
        conn.execute(f"ALTER TABLE {table} RENAME COLUMN {old} TO {new}")
        print(f"마이그레이션: {table}.{old} → {new}")


def _migrate(conn):
    """누락된 컬럼만 ALTER TABLE 로 채운다. 아직 없는 테이블은 건너뛴다."""
    _rename(conn)
    for table, columns in _MIGRATIONS.items():
        have = {r["name"] for r in conn.execute(f"PRAGMA table_info({table})")}
        if not have:
            continue  # 새 DB — executescript 가 schema.sql 로 통째로 만든다
        for name, ddl in columns:
            if name not in have:
                conn.execute(f"ALTER TABLE {table} ADD COLUMN {name} {ddl}")
                print(f"마이그레이션: {table}.{name} 추가")


def seed_legacy_kinds(conn):
    """파밍 파이프라인(DART/SEC/뉴스)이 쓰는 source_kind 를 유지한다.

    ★ 이름에 legacy 가 붙어 있지만 **현역이다.** classify.py 가 지금도
      adhoc/periodic/sec/news 를 만들고 feed_item.kind 가 source_kind FK 라,
      이 4행을 지우면 크롤러 INSERT 가 전량 FK 오류로 실패한다.
    """
    conn.executemany(
        "INSERT OR IGNORE INTO source_kind(key,label,css_class) VALUES (?,?,?)", S.SOURCE_KINDS
    )


def seed_lever_aliases(conn):
    """레버 표기 변형 → 정식명 매핑 시드.

    ★ lever 마스터가 먼저 들어간 뒤에 호출해야 한다 —
      lever_alias.lever 가 lever(name) FK 라 마스터가 비어 있으면 전부 거부된다.
      따라서 main() 에서 seed_trendroom.seed_all(conn) **직후**에 부른다.
    """
    have = {r["name"] for r in conn.execute("SELECT name FROM lever")}
    for alias, lever in S.LEVER_ALIASES:
        if lever not in have:
            print(f"경고: lever_alias '{alias}' → '{lever}' 는 lever 마스터에 없어 건너뜁니다")
            continue
        conn.execute(
            "INSERT INTO lever_alias(alias, lever) VALUES (?,?) "
            "ON CONFLICT(alias) DO UPDATE SET lever = excluded.lever",
            (alias, lever),
        )


def backfill_name_key(conn):
    """기존 proposal 행의 name_key 를 name 에서 파생 계산해 채운다(멱등).

    name_key 는 중복 차단용 정규화 과제명이라 값이 비어 있으면
    저장 경로가 '기존에 같은 과제가 없다' 고 오판한다. 컬럼을 새로 붙인 직후
    한 번만 도는 UPDATE 이며 다른 컬럼은 건드리지 않는다(데이터 손실 없음).
    """
    from app import store  # 순환 import 회피 — 정규화 규칙은 저장 계층이 단독 소유한다

    # create_schema 가 executescript **앞에서도** 부르므로 새 DB(테이블 없음)를 견뎌야 한다.
    if not conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='proposal'"
    ).fetchone():
        return
    rows = conn.execute(
        "SELECT id, name FROM proposal WHERE name_key IS NULL OR name_key = ''"
    ).fetchall()
    for r in rows:
        conn.execute(
            "UPDATE proposal SET name_key = ? WHERE id = ?",
            (store.name_key(r["name"]), r["id"]),
        )
    if rows:
        print(f"백필: proposal.name_key {len(rows)}행")


def clear_fabricated_timestamps(conn):
    """시드가 지어낸 '오늘 08:52' · '2026.07.24 08:00' 같은 값을 지운다(멱등).

    시드 JSON·상수는 이미 '—' / 빈 값으로 고쳤지만, **이미 만들어진 행은 시드가 다시
    쓰지 않는다**(upload_file 은 INSERT-only, report_setting 은 사용자 행이라 시드가
    아예 안 건드린다). 그래서 화면은 계속 '오늘 08:52 업로드' 라고 말한다.

    ★ 지우는 대상은 **시드 리터럴 완전일치뿐**이다. 사람이 실제로 만든 값
      (mark_report_sent 가 넣는 '2026.08.07 14:02' 형태, 실제 업로드 시각)은
      형태가 달라 여기 걸리지 않는다.
    """
    fake_uploads = ("오늘 08:52", "오늘 09:20", "어제 17:41")
    cur = conn.execute(
        f"UPDATE upload_file SET uploaded_at = '—' "
        f" WHERE uploaded_at IN ({','.join('?' * len(fake_uploads))})", fake_uploads,
    )
    if cur.rowcount:
        print(f"정리: upload_file.uploaded_at 지어낸 값 {cur.rowcount}행 → '—'")
    # 한 번도 발송한 적 없는 계정에 박힌 가짜 발송 이력. 빈 값이면 화면이
    # '발송 이력이 없습니다.' 를 그린다.
    cur = conn.execute(
        "UPDATE report_setting SET last_at = '' WHERE last_at = '2026.07.24 08:00'"
    )
    if cur.rowcount:
        print(f"정리: report_setting.last_at 가짜 발송 이력 {cur.rowcount}행 → 빈 값")


def backfill_version_label(conn):
    """gen_version.label 을 **실제 생성일**(created_at 의 날짜부)로 맞춘다(멱등).

    옛 _next_version 이 label 을 '직전 라벨 + 1일' 로 발급해서, 하루에 여러 번
    재생성할수록 화면에 찍히는 생성일이 미래로 밀렸다(실측: 하루 11회 재생성 →
    2026-08-06 에 만든 버전이 2026-10-09 로 표시). 생성기는 고쳤지만 이미 쌓인
    행은 그대로라 화면의 캘린더·차트가 계속 미래 날짜를 그린다.

    ★ 값을 지어내지 않는다. created_at 이 이미 갖고 있는 날짜를 label 로 복사할 뿐이다.
    ★ created_at 이 'YYYY-MM-DDTHH:MM:SS' 인 행만 고친다. 시드 버전(g1~)은
      created_at 이 날짜만이고 label 과 이미 같아서 대상이 아니다.
    ★ 같은 날 여러 버전이 생기면 label 이 겹치는데 화면은 깨지지 않는다 —
      버전 선택은 id 로 하고, 캘린더는 그날 버전을 합쳐 한 칸으로 그린다.
      정렬은 label 이 아니라 sort_order 가 담당한다.
    """
    rows = conn.execute(
        "SELECT id, label, SUBSTR(created_at, 1, 10) AS real_day FROM gen_version "
        "WHERE created_at LIKE '____-__-__T%' AND label <> SUBSTR(created_at, 1, 10)"
    ).fetchall()
    for r in rows:
        conn.execute("UPDATE gen_version SET label = ? WHERE id = ?", (r["real_day"], r["id"]))
    if rows:
        print(f"백필: gen_version.label {len(rows)}행 (표시 생성일 → 실제 생성일)")


def seed_cases(conn):
    """혁신 사례 시드. 중복 방지를 위해 title 기준으로 이미 있으면 건너뜀."""
    for (title, category, background, effect, kpi_name, kpi_formula,
         source_org, source_type, source_ref, status, affs) in S.INNOVATION_CASES:
        exists = conn.execute(
            "SELECT id FROM kb_innovation_case WHERE title = ?", (title,)
        ).fetchone()
        if exists:
            case_id = exists["id"]
        else:
            cur = conn.execute(
                """INSERT INTO kb_innovation_case
                   (title, category, background, effect, kpi_name, kpi_formula,
                    source_org, source_type, source_ref, status, created_at)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (title, category, background, effect, kpi_name, kpi_formula,
                 source_org, source_type, source_ref, status, TODAY),
            )
            case_id = cur.lastrowid
        for aff in affs:
            conn.execute(
                "INSERT OR IGNORE INTO kb_case_affiliate(case_id, aff_code) VALUES (?,?)",
                (case_id, aff),
            )


def main():
    if "--reset" in sys.argv:
        p = Path(DB_PATH)
        if p.exists():
            p.unlink()
            print(f"삭제됨: {DB_PATH}")

    conn = get_connection()
    try:
        create_schema(conn)
        seed_legacy_kinds(conn)
        # 화면 마스터·근거자료·과제 제안·관리자 데이터
        seed_trendroom.seed_all(conn)
        # lever 마스터가 들어간 직후 — FK 가 성립하는 유일한 순서다
        seed_lever_aliases(conn)
        backfill_name_key(conn)
        clear_fabricated_timestamps(conn)
        backfill_version_label(conn)
        seed_cases(conn)
        conn.commit()

        def n(sql):
            return conn.execute(sql).fetchone()[0]

        print(f"완료: {DB_PATH}")
        print(f"  계열사 {n('SELECT COUNT(*) FROM affiliate')}개 · "
              f"레버 {n('SELECT COUNT(*) FROM lever')}개 · "
              f"테마 {n('SELECT COUNT(*) FROM theme')}개")
        print(f"  근거 자료 {n('SELECT COUNT(*) FROM feed_item')}건 · "
              f"생성 버전 {n('SELECT COUNT(*) FROM gen_version')}개 · "
              f"과제 제안 {n('SELECT COUNT(*) FROM proposal')}건 · "
              f"후보 풀 {n('SELECT COUNT(*) FROM proposal_pool')}건")
        print(f"  크롤링 소스 {n('SELECT COUNT(*) FROM crawl_source')}개 · "
              f"혁신 사례 {n('SELECT COUNT(*) FROM kb_innovation_case')}건 · "
              f"레버 별칭 {n('SELECT COUNT(*) FROM lever_alias')}쌍")
        print("  계정은 `python -m app.db.seed_users` 로 별도 생성하세요.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
