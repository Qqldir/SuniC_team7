"""평가 파이프라인 수동 점검 스크립트.

    python tests_eval.py

API 키가 없으면 규칙 기반 채점으로 자동 폴백하므로 그대로 실행된다.
"""
from app.models import Kpi, TaskDraft
from app.pipeline.evaluation import evaluate_tasks, criteria_text

GOOD = TaskDraft(
    title="정기보수(TA) 주기 최적화를 통한 정비비 절감",
    category="정비·TA",
    background="미쓰이화학이 TA 공정 개선으로 보수 기간을 단축한 사례가 확인되며, 반기보고서상 정기보수 원가 부담이 증가하고 있다.",
    plan="설비별 열화 데이터를 모니터링해 고정 주기 정비를 상태 기반 정비로 전환하고, 파일럿 2개 라인에 우선 적용한다.",
    risk="상태 기반 전환 초기에 예측 정확도가 낮아 돌발 정지 위험이 있다.",
    effect="정비 기간 8% 단축으로 연간 정비비 약 12% 절감 기대",
    kpi=Kpi(name="정비비 원단위", formula="연간 정비비 / 가동시간"),
    evidence=["e04", "e09"],
)

VAGUE = TaskDraft(
    title="원가 경쟁력 제고 방안 마련",
    category="기타",
    background="원가 부담이 커지고 있다.",
    plan="다각도로 개선 방안을 적극 검토한다.",
    risk="",
    effect="원가 절감에 기여할 것으로 기대",
    kpi=Kpi(name="원가", formula="-"),
    evidence=["e14"],
)

HALLUCINATED = TaskDraft(
    title="자가발전 설비 확대를 통한 전력비 절감",
    category="에너지비",
    background="산업용 전기요금 인상이 논의되고 있어 자가발전 비중 확대가 필요하다.",
    plan="신규 열병합 발전 설비를 증설하여 외부 구매 전력 비중을 낮춘다.",
    risk="대규모 투자에 따른 회수기간 장기화.",
    effect="전력비 15% 절감",
    kpi=Kpi(name="전력 자급률", formula="자가발전량 / 총 전력사용량"),
    evidence=["e02", "e99"],          # e99 는 존재하지 않는 근거
)

DUPLICATE = TaskDraft(
    title="정기보수 TA 주기 최적화를 통한 정비비 절감",   # GOOD 과 사실상 동일
    category="정비·TA",
    background="정기보수 원가 부담이 증가하고 있어 주기 재검토가 필요하다.",
    plan="열화 데이터 기반으로 정비 주기를 재설정한다.",
    risk="예측 정확도 확보 필요.",
    effect="정비비 10% 절감",
    kpi=Kpi(name="정비비 원단위", formula="연간 정비비 / 가동시간"),
    evidence=["e09"],
)

BROKEN = TaskDraft(
    title="무제 과제",
    category="",
    background="",
    plan="",
    risk="",
    effect="",
    kpi=Kpi(),
    evidence=[],
)

DRAFTS = [GOOD, VAGUE, HALLUCINATED, DUPLICATE, BROKEN]

results = evaluate_tasks(DRAFTS, aff_code="SKE", use_llm=False)

print("=" * 78)
print(criteria_text())
print("=" * 78)
for r in results:
    e = r.evaluation
    mark = {"pass": "PASS   ", "review": "REVIEW ", "blocked": "BLOCKED"}[e.verdict]
    rk = f"#{e.rank}" if e.rank else "  -"
    print(f"\n[{mark}] {rk}  {e.priority:5.1f}점 ({e.grade})  {r.task.title}")
    if e.verdict != "blocked":
        print(f"         임팩트 {e.impact.score} · 실현 {e.feasibility.score} · ROI {e.roi.score}"
              f"  [{e.scoredBy}]")
    for i in e.validation.issues:
        print(f"         └ {i.severity:5s} {i.code:22s} {i.message}")

print("\n" + "=" * 78)
counts = {"pass": 0, "review": 0, "blocked": 0}
for r in results:
    counts[r.evaluation.verdict] += 1
print(f"통과 {counts['pass']} · 검토필요 {counts['review']} · 차단 {counts['blocked']}")

print("\n--- Top 2 ---")
for r in evaluate_tasks(DRAFTS, aff_code="SKE", use_llm=False, top_n=2):
    print(f"  #{r.evaluation.rank} {r.task.title} ({r.evaluation.priority}점)")
