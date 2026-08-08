"""파밍 파이프라인이 쓰는 자료 종류 · 레버 별칭 · 혁신 사례 시드.

계열사·사업부문·근거 자료(feed_item)·과제 제안은 app/db/seed_trendroom.py 가
frontend/public/trendroom.html 에서 뽑아 둔 데이터로 채웁니다(단일 출처).
여기에는 그쪽에 포함되지 않는 값만 남겨 둡니다.
"""

# 파밍 파이프라인(DART 수시/정기 · SEC · 뉴스)이 feed_item.kind 로 쓰는 값.
#
# ★ '레거시' 가 아니다 — 지우지 마라. classify.py 가 RawDoc.kind 로 이 4개 값을
#   **지금도 만들고**(adhoc/periodic/sec/news), feed_item.kind 는 source_kind(key) FK 다.
#   이 4행이 없으면 크롤러 INSERT 가 FOREIGN KEY constraint 로 전량 실패한다.
#   화면 필터가 쓰는 종류(disclosure/earnings/ir/market/assoc)는 seed_trendroom 쪽이다.
SOURCE_KINDS = [
    ("adhoc", "DART 수시", "badge-adhoc"),
    ("periodic", "DART 정기", "badge-periodic"),
    ("sec", "SEC", "badge-sec"),
    ("news", "뉴스", "badge-news"),
]


# ─────────────── 레버 표기 변형 → 정식 레버명 ───────────────
# proposal.lever 는 lever(name) FK 이고 PRAGMA foreign_keys = ON 이라
# LLM·혁신사례가 쓰는 변형 표기('정비·TA', '간접비/가동률', '기타' ...)를 그대로 넣으면
# INSERT 자체가 FOREIGN KEY constraint failed 로 실패한다.
# 저장 직전 app/pipeline/discovery/lever_map.normalize_lever 가 이 표로 정식명을 찾는다.
#
# ★ 오른쪽 값은 반드시 lever 마스터 7개(정비/TA · 에너지비 · 물류비 · 수율 · 구매 ·
#   간접비 · 운전자본) 중 하나여야 한다. 아니면 시드에서 FK 로 거부된다.
LEVER_ALIASES = [
    # 정비/TA
    ("정비·TA", "정비/TA"),        # agent.py 프롬프트가 쓰던 가운뎃점(U+00B7) 표기
    ("정비", "정비/TA"),
    ("TA", "정비/TA"),
    # 에너지비
    ("에너지", "에너지비"),
    ("에너지비용", "에너지비"),
    ("유틸리티", "에너지비"),
    # 물류비
    ("물류", "물류비"),
    ("운송비", "물류비"),
    # 수율
    ("수율개선", "수율"),
    ("가동률", "수율"),
    # 구매
    ("구매비", "구매"),
    ("조달", "구매"),
    # 간접비
    ("판관비", "간접비"),
    ("간접비/가동률", "간접비"),   # kb_innovation_case.category 실측 표기
    # 운전자본
    ("운전자금", "운전자본"),
    ("재고", "운전자본"),
]


# ─────────────── 혁신 사례 모음 (큐레이션 시드) ───────────────
#
# ★ 여기가 혁신 사례의 **유일한 관리 경로**다(사용자 결정). 입력·검토 API 는 없다.
#   사례를 더하거나 고치려면 이 표를 고치고 `python -m app.db.seed` 를 다시 돌린다
#   (seed.seed_cases 가 title 기준 멱등).
#   이미 들어간 행의 **내용 수정은 시드가 하지 않는다** — title 이 같으면 건너뛰므로,
#   문장을 바꾸려면 title 을 바꾸거나 해당 행을 직접 지우고 다시 돌려야 한다.
#   테이블(kb_innovation_case · kb_case_affiliate)은 그대로 살아 있고,
#   발굴 프롬프트의 [검증된 혁신 사례] 블록을 prefetch._case_block 이 직접 읽는다.
#
# (title, category, background, effect, kpi_name, kpi_formula,
#  source_org, source_type, source_ref, status, [aff_codes])
# source_type: manual(사람 큐레이션) / ai(AI 추출·검토대기) / auto
# status: approved(승인) / pending(검토대기)
INNOVATION_CASES = [
    (
        "NCC 정기보수(TA) 표준화·병렬화로 정비기간 단축", "정비/TA",
        "미쓰이화학이 결산설명회에서 TA 공정을 표준화·병렬화해 정비 기간을 단축한 사례를 공개.",
        "TA 1일 단축 시 기회손실·고정비 부담 축소",
        "TA 기간 단축률", "(기준 TA일수 − 실제 TA일수) ÷ 기준 TA일수",
        "미쓰이화학", "manual", "e04", "approved", ["SKGC", "SKE"],
    ),
    (
        "머신비전 검사 자동화로 셀 수율 개선", "수율",
        "CATL이 머신비전 기반 전수검사로 전환해 수율과 검사 인건비를 동시에 개선한 사례.",
        "불량 유출 감소와 검사 인건비 절감 동시 달성",
        "공정 수율", "양품 수 ÷ 투입 수 × 100(%)",
        "CATL", "manual", "e06", "approved", ["SKO"],
    ),
    (
        "전력 다소비 공정 피크관리·요금제 최적화", "에너지비",
        "산업용 전기요금 인상 국면에서 부하 이동·피크 관리로 전력비 원단위를 방어한 접근.",
        "요금 인상분 흡수 및 전력비 원단위 개선",
        "전력 원단위", "전력사용량(kWh) ÷ 생산량(t)",
        "GS칼텍스", "manual", "e11", "approved", ["SKE", "SKGC", "SKIPC"],
    ),
    (
        "장기 운송계약 재협상으로 물류비 원단위 절감", "물류비",
        "컨테이너 해상운임 하락 구간에 장기 운송계약을 재협상해 물류비를 낮춘 사례.",
        "운임 하락분 반영으로 물류 원단위 절감",
        "물류 원단위", "물류비 ÷ 출하량(t)",
        "해운 시황", "manual", "e08", "approved", ["SKTI", "SKE", "SKO"],
    ),
    (
        "저가동 라인 통합·재편으로 고정비 구조 개선", "간접비/가동률",
        "아사히카세이가 저가동 분리막 라인을 통합 운영해 가동률 방어형 원가구조로 전환.",
        "가동률 방어 및 단위당 고정비 절감",
        "설비 가동률", "실제 생산량 ÷ 생산능력 × 100(%)",
        "아사히카세이", "manual", "e10", "approved", ["SKIET", "SKGC"],
    ),
    (
        "단지 내 유틸리티·물류 공동활용", "구매",
        "석화 콤비나트 경쟁력 방안에서 단지 내 유틸리티·물류 공동화가 원가 절감 의제로 논의.",
        "인접사 공동활용으로 유틸리티·물류비 절감",
        "유틸리티 원단위", "유틸리티 비용 ÷ 생산량(t)",
        "산업부", "manual", "e12", "approved", ["SKGC", "SKIPC"],
    ),
    (
        "재고·운전자본 회전 관리 강화", "운전자본",
        "삼성SDI 반기보고서의 재고자산 회전·가동 전략을 참고한 운전자본 관리 사례.",
        "재고 회전 개선으로 운전자본 부담 축소",
        "재고자산회전율", "매출원가 ÷ 평균 재고자산",
        "삼성SDI", "manual", "e15", "approved", ["SKO"],
    ),
    # ── AI 추출·검토대기 예시 (3층 구조 시연용) ──
    (
        "연 10억 달러 규모 전사 비용절감 프로그램 벤치마크", "간접비",
        "Dow 10-Q에 공개된 물류·구매·정비 영역별 비용절감 프로그램. AI가 공시에서 자동 추출한 초안.",
        "영역별 절감목표 설정으로 구조적 원가 개선",
        "비용절감 달성률", "실제 절감액 ÷ 목표 절감액 × 100(%)",
        "Dow", "ai", "e03", "pending", ["SKGC"],
    ),
]
