"""화면(O/I Spark) 초기 데이터 시드.

원본은 `seed_assets/trendroom.json` — frontend/public/trendroom.html 이 상수로 들고
있던 데모 데이터를 그대로 뽑아 둔 파일입니다(scratchpad 의 extract.mjs 로 생성).
손으로 옮기지 않았으므로 화면이 보여 주던 값과 1:1 로 일치합니다.

실서비스에서는 farming 파이프라인이 feed_item 을, discovery 가 proposal 을 채웁니다.
여기서는 서버를 띄웠을 때 화면이 곧바로 채워지도록 초기값만 넣습니다.
"""
import json
from datetime import date
from pathlib import Path

ASSET = Path(__file__).with_name("seed_assets") / "trendroom.json"

# 사업부문 라벨 → biz_segment.key
BIZ_KEY = {"에너지·화학": "energy", "배터리·소재": "battery", "LNG·전력": "lng"}

# 트렌드룸 종류 필터 카테고리 → source_kind.key
KIND_KEY = {
    "공시": "disclosure",
    "실적발표": "earnings",
    "IR·보고서": "ir",
    "시황·전문지": "market",
    "협회 자료": "assoc",
}
KIND_CSS = {
    "disclosure": "badge-adhoc", "earnings": "badge-periodic",
    "ir": "badge-sec", "market": "badge-news", "assoc": "badge-news",
}

# AI Reporting 기본값 — 계정이 아직 설정을 저장하지 않았을 때 화면에 보여 줄 값.
# (원본 trendroom.html 의 S.send / S.recipients / S.channels)
REPORT_DEFAULTS = {
    "freq": "매일",
    "time": "08:00",
    "lastAt": "2026.07.24 08:00",
    "recipients": ["O/I추진단 (jin.k@sk.com)", "SKGC 혁신팀 (gc-innov@sk.com)"],
    "channels": {"outlook": True, "teams": True},
}

# 레버명 → 내부 지식 베이스 검색 질의어 (lever.kb_query).
# 레버 어휘(정유·화학)와 KB 어휘(배터리 제조)가 달라서, 레버명을 그대로 질의하면
# '간접비' 0건 / '정비/TA' 3건 전부 무관이 나온다. 아래 값은 실측으로 검증된 매핑이다.
# 코드 상수가 아니라 DB 컬럼인 이유: KB 를 다시 빌드할 때마다 매핑 품질이 바뀌고,
# 회사별 KB 가 늘면 회사마다 달라질 수 있어 배포 없이 고칠 수 있어야 한다.
# ★ 튜닝할 때는 반드시 prefetch.KB_TOP_K 와 **같은 top_k** 로 측정하라.
#   top_k=3 으로 재면 좋아 보이지만 실제로 프롬프트에 실리는 것은 상위 2건뿐이라,
#   3위에만 걸리는 문서는 영원히 주입되지 않는다(이 함정으로 한 번 잘못 측정한 적이 있다).
LEVER_KB_QUERY = {
    "정비/TA": "예지보전 설비 고장 digital twin predictive maintenance 가동",
    "에너지비": "전력 원단위 유틸리티 에너지 건조 공정 소비",
    "물류비": "raw material receiving storage 입고 보관 물류 창고",
    "수율": "yield 수율 불량 defect quality 검사 공정능력",
    "구매": "원소재 가격 변동 조달 리스크 공급 계약",
    "간접비": "cost structure 원가 구조 고정비 비용 절감",
    "운전자본": "재고 자산 회전 capex 투자 현금흐름 재무",
}

# 레버별 평가 임팩트 기준값 (lever.impact_base, 1.0~5.0). 과제 평가(scorer)가 쓴다.
# 관리자가 레버를 새로 추가하면 스키마 기본값 3.0 이 적용된다.
LEVER_IMPACT_BASE = {
    "정비/TA": 4.0,
    "에너지비": 4.5,
    "물류비": 3.5,
    "수율": 4.5,
    "구매": 3.5,
    "간접비": 3.0,
    "운전자본": 3.5,
}

# ★ SKES 의 표시명은 `SK E&S` 다(사용자 결정, 2026-08-07 — 사내 통용 표기로 통일).
#   affiliate.name 은 화면 표시로 끝나지 않고 prefetch 가 발굴 프롬프트의 {aff_name} 으로
#   그대로 넣는다. 그런데 knowledge/SKES/core/rules.md 는 2024-11-01 이후 표준명을
#   `SK이노베이션 E&S CIC` 로 두고 `SK E&S` 를 합병 전(~2024-10-31) 법인명으로 규정한다.
#   즉 프롬프트 회사명과 KB 규칙이 어긋나 있어, 합병 전 계약·재무·지분 사실이 CIC 로
#   소급될 여지가 남는다. KB 쪽 사실 기술은 일부러 건드리지 않았다 —
#   그 문서들은 시점별 법인을 구분해 적은 기록이라 이름을 일괄 치환하면 사실이 깨진다.

# 계열사 → 내부 지식 베이스 디렉터리명 (affiliate.kb_company, backend/knowledge/<이름>).
# 여기 없는 계열사는 NULL 이고, prefetch 가 내부 지식 블록을 통째로 생략한다.
# NULL 을 그대로 retriever.load 에 넘기면 FileNotFoundError 로 발굴이 500 이 된다.
AFFILIATE_KB_COMPANY = {
    "SKO": "SKO",
    "SKES": "SKES",
}

# 계열사 사업 요약 (kb_business.summary) — 발굴 프롬프트의 [대상 계열사] 블록에 실린다.
#
# 왜 필요한가: prefetch._profile_block 은 kb_business 가 비면 "코드 이름 (사업부문 …)"
# 한 줄만 싣는다. affiliate.kb_company 가 NULL 인 7개 계열사는 내부 지식 블록(4·5)도
# 통째로 빠지므로, 그 상태에서는 계열사에 대해 모델이 아는 것이 사실상 이름뿐이었다.
#
# ★ 사실만, 사업부문 수준으로만 적는다. 확실하지 않은 수치·설비명·전략은 쓰지 않는다 —
#   프롬프트 맨 앞에 놓이는 블록이라 여기 적힌 틀린 문장이 그대로 과제로 굳는다.
#   내부 지식 베이스가 있는 SKO·SKES 는 각 knowledge/<회사>/INDEX.md 의 도메인 구성을
#   근거로 했고, 나머지 7곳은 공개된 사업부문 사실만 적었다.
# ★ 여기는 '간략 시드' 다(사용자 결정). 계열사별 상세 프로필은 나중에 채운다.
AFFILIATE_BUSINESS = {
    "SKE": "원유를 정제해 휘발유·경유·항공유 등 석유제품을 생산·공급하는 정유사업을 한다. "
           "대규모 정제설비를 연속 가동하므로 정기보수(TA)·에너지 원단위·가동률이 원가를 좌우한다.",
    "SKGC": "나프타 분해로 얻은 기초유분과 이를 원료로 한 화학제품을 생산한다. "
            "폐플라스틱 재활용을 포함한 순환경제 사업을 함께 추진한다.",
    "SKEN": "윤활기유와 윤활유를 생산·판매한다. 고급 윤활기유 중심의 제품 구성이다.",
    "SKIPC": "인천 공장에서 원유를 정제해 석유제품과 파라자일렌 등 방향족 화학제품을 생산한다.",
    "SKTI": "원유 도입과 석유제품 트레이딩을 담당한다. 실물 거래와 운송·재고가 손익의 축이라 "
            "물류비와 운전자본 회전이 핵심 관리 대상이다.",
    "SKEO": "석유·가스 자원의 탐사와 개발·생산(E&P)을 한다. 해외 광구 운영과 "
            "이산화탄소 포집·저장(CCS) 사업을 추진한다.",
    "SKO": "리튬이온 배터리 셀을 생산한다. 전극(믹싱·코팅·건조·압연) → 조립 → 충방전 완성공정 → "
           "모듈·팩 순으로 이어지는 제조 공정을 국내외 생산 거점에서 운영하며, "
           "수율·가동률과 원소재(리튬·니켈·코발트) 조달이 원가를 좌우한다.",
    "SKIET": "리튬이온 배터리용 분리막(LiBS)을 생산한다. 필름 연신·코팅 공정 기반이라 "
             "라인 가동률과 수율이 수익성에 직결된다.",
    "SKES": "LNG 밸류체인(도입·터미널·발전)과 도시가스 공급을 축으로 하고, "
            "수소·재생에너지·ESS·CCS 등 저탄소 사업을 함께 한다. "
            "연료비와 발전소·터미널 설비 운영이 원가의 중심이다.",
}


def load() -> dict:
    return json.loads(ASSET.read_text(encoding="utf-8"))


def _iso(dotted: str) -> str:
    """2026.07.17 → 2026-07-17."""
    return dotted.replace(".", "-")


def seed_master(conn, d: dict) -> None:
    """사업부문 · 계열사 · 자료 종류 · 레버 · 테마."""
    for label, key in BIZ_KEY.items():
        conn.execute(
            "INSERT INTO biz_segment(key,label,color) VALUES (?,?,?) "
            "ON CONFLICT(key) DO UPDATE SET label=excluded.label, color=excluded.color",
            (key, label, d["bizColor"].get(label, "#666")),
        )
    for i, oc in enumerate(d["ocs"]):
        conn.execute(
            "INSERT INTO affiliate(code,name,biz,color,sort_order,kb_company) VALUES (?,?,?,?,?,?) "
            "ON CONFLICT(code) DO UPDATE SET name=excluded.name, biz=excluded.biz, "
            "color=excluded.color, sort_order=excluded.sort_order, "
            # 상수표에 없는 계열사(관리자가 직접 넣은 KB)를 NULL 로 지우지 않는다.
            "kb_company=COALESCE(excluded.kb_company, affiliate.kb_company)",
            (oc["code"], oc["name"], BIZ_KEY[oc["biz"]], d["ocColor"].get(oc["code"]), i,
             AFFILIATE_KB_COMPANY.get(oc["code"])),
        )
    for label, key in KIND_KEY.items():
        conn.execute(
            "INSERT INTO source_kind(key,label,css_class) VALUES (?,?,?) "
            "ON CONFLICT(key) DO UPDATE SET label=excluded.label",
            (key, label, KIND_CSS[key]),
        )
    for i, (name, lv) in enumerate(d["levers"].items()):
        # kb_query / impact_base 는 화면 시드(trendroom.json)에 없는 값이라 위 상수표에서 온다.
        # 표에 없는 레버(관리자 추가분)는 기존 값을 유지하도록 COALESCE 로 덮어쓰기를 막는다.
        conn.execute(
            "INSERT INTO lever(name,metric,formula,fields,sort_order,kb_query,impact_base) "
            "VALUES (?,?,?,?,?,?,COALESCE(?,3.0)) "
            "ON CONFLICT(name) DO UPDATE SET metric=excluded.metric, formula=excluded.formula, "
            "fields=excluded.fields, sort_order=excluded.sort_order, "
            "kb_query=COALESCE(excluded.kb_query, lever.kb_query), "
            "impact_base=COALESCE(?, lever.impact_base)",
            (name, lv["metric"], lv["text"],
             json.dumps(lv["fields"], ensure_ascii=False), i,
             LEVER_KB_QUERY.get(name), LEVER_IMPACT_BASE.get(name),
             LEVER_IMPACT_BASE.get(name)),
        )
    for i, (name, th) in enumerate(d["themes"].items()):
        conn.execute(
            "INSERT INTO theme(name,color,bg,head,body,sort_order) VALUES (?,?,?,?,?,?) "
            "ON CONFLICT(name) DO UPDATE SET color=excluded.color, bg=excluded.bg, "
            "head=excluded.head, body=excluded.body, sort_order=excluded.sort_order",
            (name, th["c"], th["bg"], th["head"], th["body"], i),
        )


def seed_business(conn) -> None:
    """계열사 사업 요약(kb_business) 시드. 재실행해도 행이 늘지 않는다.

    ★ 계열사당 시드 행은 **하나**다. 같은 aff_code 의 가장 오래된 행(=시드 행)만
      갱신하고, 사람이 뒤에 덧붙인 두 번째 행부터는 건드리지 않는다
      (prefetch._profile_block 은 `ORDER BY id` 로 전부 이어 붙인다).
    ★ affiliate 마스터가 들어간 뒤에 불러야 한다 — kb_business.aff_code 가
      affiliate(code) FK 라 순서가 뒤집히면 전부 거부된다.
    """
    today = date.today().isoformat()
    for code, summary in AFFILIATE_BUSINESS.items():
        row = conn.execute(
            "SELECT id FROM kb_business WHERE aff_code = ? ORDER BY id LIMIT 1", (code,)
        ).fetchone()
        if row:
            conn.execute(
                "UPDATE kb_business SET summary = ?, updated_on = ? WHERE id = ?",
                (summary, today, row["id"]),
            )
        else:
            conn.execute(
                "INSERT INTO kb_business(aff_code, summary, updated_on) VALUES (?,?,?)",
                (code, summary, today),
            )


def seed_evidence(conn, d: dict) -> None:
    """근거 자료 = feed_item. 파밍 파이프라인이 채우는 테이블과 같은 곳에 넣는다."""
    for fid, ev in d["evidence"].items():
        cat = d["kindMap"].get(ev["kind"], "IR·보고서")
        conn.execute(
            """INSERT INTO feed_item
               (id, published_on, kind, source, title, summary, url,
                kind_label, theme, biz_hint, is_new)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(id) DO UPDATE SET
                 published_on=excluded.published_on, kind=excluded.kind,
                 source=excluded.source, title=excluded.title, summary=excluded.summary,
                 url=excluded.url, kind_label=excluded.kind_label, theme=excluded.theme,
                 biz_hint=excluded.biz_hint, is_new=excluded.is_new""",
            (fid, _iso(ev["date"]), KIND_KEY[cat], ev["src"], ev["title"], ev["sum"],
             ev.get("url", ""), ev["kind"], d["evTheme"].get(fid),
             d["evBizFallback"].get(fid), 1 if d["evNew"].get(fid) else 0),
        )


def seed_proposals(conn, d: dict) -> None:
    """생성 버전 · 과제 제안 · 근거 연결 · 재생성 후보 풀."""
    # sort_order 는 생성일 오름차순 — 클수록 최신
    vers = sorted(d["versions"], key=lambda v: v["label"])
    for i, v in enumerate(vers):
        conn.execute(
            "INSERT INTO gen_version(id,label,trigger,created_at,sort_order) VALUES (?,?,?,?,?) "
            "ON CONFLICT(id) DO UPDATE SET label=excluded.label, trigger=excluded.trigger, "
            "sort_order=excluded.sort_order",
            (v["id"], _iso(v["label"]), v.get("trigger", ""), _iso(v["label"]), i),
        )

    ver_label = {v["id"]: _iso(v["label"]) for v in d["versions"]}
    for t in d["tasks"]:
        conn.execute(
            """INSERT INTO proposal(id, ver_id, aff_code, lever, name, summary, plan, origin, created_at)
               VALUES (?,?,?,?,?,?,?,'자동',?)
               ON CONFLICT(id) DO UPDATE SET ver_id=excluded.ver_id, aff_code=excluded.aff_code,
                 lever=excluded.lever, name=excluded.name, summary=excluded.summary,
                 plan=excluded.plan""",
            (t["id"], t["ver"], t["oc"], t["lever"], t["name"],
             t.get("sum", ""), t.get("plan", ""), ver_label.get(t["ver"])),
        )
        for fid in t.get("ev", []):
            conn.execute(
                "INSERT OR IGNORE INTO proposal_evidence(proposal_id, feed_id) VALUES (?,?)",
                (t["id"], fid),
            )

    # 후보 풀 — 이름이 같으면 이미 있는 것으로 본다(중복 시드 방지)
    for p in d["pool"]:
        exists = conn.execute(
            "SELECT 1 FROM proposal_pool WHERE name = ? AND aff_code = ?", (p["name"], p["oc"])
        ).fetchone()
        if exists:
            continue
        conn.execute(
            "INSERT INTO proposal_pool(aff_code, lever, name, summary, plan, evidence) "
            "VALUES (?,?,?,?,?,?)",
            (p["oc"], p["lever"], p["name"], p.get("sum", ""), p.get("plan", ""),
             ",".join(p.get("ev", []))),
        )


def seed_feed_tags(conn) -> None:
    """근거 자료 ↔ 계열사 태그를 과제 참조 관계에서 역산한다.

    과제 발굴(discovery)이 `feed_item_tag` 로 계열사별 컨텍스트를 뽑기 때문에
    화면 데이터만 넣으면 발굴 쪽이 비어 버린다.
    """
    conn.execute(
        """INSERT OR IGNORE INTO feed_item_tag(feed_id, aff_code)
           SELECT DISTINCT pe.feed_id, p.aff_code
           FROM proposal_evidence pe JOIN proposal p ON p.id = pe.proposal_id"""
    )


def seed_admin(conn, d: dict) -> None:
    """크롤링 소스 · 내부 자료 · 권한 · 생성 인스트럭션."""
    for i, s in enumerate(d["sources"]):
        exists = conn.execute("SELECT id FROM crawl_source WHERE name = ?", (s["name"],)).fetchone()
        row = (s["name"], s.get("url", ""), s.get("type", ""), 1 if s.get("paid") else 0,
               s.get("last", ""), s.get("cnt", 0), s.get("fresh", 0), s.get("st", "정상"), i)
        if exists:
            conn.execute(
                "UPDATE crawl_source SET name=?, url=?, type=?, paid=?, last_at=?, "
                "doc_count=?, fresh_count=?, status=?, sort_order=? WHERE id=?",
                row + (exists["id"],),
            )
        else:
            conn.execute(
                "INSERT INTO crawl_source(name,url,type,paid,last_at,doc_count,fresh_count,"
                "status,sort_order) VALUES (?,?,?,?,?,?,?,?,?)", row,
            )

    for u in d["uploads"]:
        exists = conn.execute("SELECT 1 FROM upload_file WHERE name = ?", (u["name"],)).fetchone()
        if not exists:
            conn.execute(
                "INSERT INTO upload_file(name, aff, size, uploaded_at, status) VALUES (?,?,?,?,?)",
                (u["name"], u.get("oc", "전사"), u.get("size", ""), u.get("at", ""),
                 u.get("st", "검수 대기")),
            )

    for a in d["admins"]:
        conn.execute(
            "INSERT INTO admin_member(mail, role, note) VALUES (?,?,?) "
            "ON CONFLICT(mail) DO UPDATE SET role=excluded.role, note=excluded.note",
            (a["mail"], a["role"], a.get("note", "")),
        )

    # 초기값 복원 버튼이 쓰는 기본 인스트럭션은 항상 최신으로 유지하고,
    # 관리자가 저장한 현재값은 이미 있으면 건드리지 않는다.
    conn.execute(
        "INSERT INTO app_setting(key,value) VALUES ('instruction_default', ?) "
        "ON CONFLICT(key) DO UPDATE SET value = excluded.value", (d["instruction"],),
    )
    conn.execute(
        "INSERT OR IGNORE INTO app_setting(key,value) VALUES ('instruction', ?)",
        (d["instruction"],),
    )
    conn.execute(
        "INSERT INTO app_setting(key,value) VALUES ('report_defaults', ?) "
        "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        (json.dumps(REPORT_DEFAULTS, ensure_ascii=False),),
    )


def seed_all(conn) -> dict:
    d = load()
    seed_master(conn, d)
    seed_business(conn)          # affiliate 마스터 직후 — FK 가 성립하는 순서
    seed_evidence(conn, d)
    seed_proposals(conn, d)
    seed_feed_tags(conn)
    seed_admin(conn, d)
    return d
