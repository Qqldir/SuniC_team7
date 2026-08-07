---
id: skes-d17-d17-08-ai-task-recommendation-engine
title: AI Task Recommendation Engine
summary: 오픈이노베이션 과제의 선별과 우선순위 결정을 위한 표준화된 태스크 스키마와 8단계 평가·게이트 검사 알고리즘을 정의한다.
tags: [d17, oi-portfolio, oi-seed, schema, "xref:d00", "xref:d01"]
keywords: [태스크 스키마, 게이트 검사, POC 설계, 포트폴리오, OI 모드, 스코어링, 거버넌스, 경제성 분석, 역량 평가, 문제 검증]
related: []
priority: normal
domain: D17
section: D17-08
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 1148
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-08 AI Task Recommendation Engine

## 1. Canonical Task Schema

```yaml
oi_task_record:
  identity:
    task_id: D17-OI-NNN
    title: null
    portfolio: null
    version: 1
    status: SCREEN|G0|G1|G2|G3|G4|G5|G6|G7|G8|HOLD|STOP
    as_of_date: YYYY-MM-DD
  lineage:
    source_domain_ids: []
    source_seed_ids: []
    pain_ids: []
    failure_mode_ids: []
    risk_ids: []
    external_evidence_ids: []
  problem:
    statement: null
    evidence_state: VERIFIED_FACT|ANALYTICAL_DERIVATION|HYPOTHESIS|INTERNAL_REQUIRED
    cause_confidence: null
    affected_entity_asset_contract_customer: []
    exposure_unit: cargo|MWh|GJ|customer|site|kg_H2|tCO2|KRW|other
    baseline_period: null
    baseline_value: null
  decision:
    accountable_owner: null
    operator: null
    human_approvers: []
    current_workflow: []
    current_systems: []
    decision_latency: null
  capability:
    required_outcome: null
    oi_mode: BUILD|BUY|CO_DEVELOP|LICENSE|PARTNER|INVEST|OBSERVE
    external_capability_type: []
    non_negotiable_controls: []
  provider:
    legal_entity: null
    solution_version: null
    maturity: COMMERCIAL|PILOT|RESEARCH|UNKNOWN
    evidence_tier: null
    exact_reference_scope: null
    current_ens_relationship: null
    tco_and_exit: null
    lock_in_and_eol: []
  data:
    required_datasets: []
    grain_and_history: []
    source_systems: []
    owner: []
    quality_state: null
    rights_state: CONFIRMED|LIMITED|UNKNOWN
    classification_residency_retention: []
  poc:
    bounded_scope: null
    baseline_and_counterfactual: null
    duration: null
    primary_kpi: null
    secondary_kpis: []
    guardrails: []
    stop_criteria: []
    rollback_plan: null
  rights_and_governance:
    contract_consent: null
    data_training_reuse_right: null
    background_foreground_ip: null
    safety_gate: null
    legal_tax_gate: null
    cyber_privacy_gate: null
    finance_gate: null
  economics:
    implementation_cost: null
    internal_hours: null
    recurring_tco: null
    physical_benefit: null
    cash_benefit: null
    risk_benefit: null
    benefit_state: IDEA|BASELINED|PILOT_MEASURED|FINANCE_VERIFIED|CASH_REALIZED|SCALED
    double_count_group_id: null
  score:
    strategic_relevance_15: null
    quantified_value_risk_20: null
    evidence_problem_proof_15: null
    data_readiness_10: null
    external_capability_10: null
    bounded_poc_10: null
    scale_reuse_10: null
    governance_reversibility_10: null
    total_100: null
    tier: P0|P1|P2|HOLD|NO_GO
    hard_gate_flags: []
```

## 2. 추천 알고리즘

```text
1. D00/D01~D16의 최신 Source·Entity·Asset·Rule Version을 확인한다.
2. Pain/Failure가 재현되지 않으면 Solution을 추천하지 않고 G0 Problem Proof를 생성한다.
3. 기존 시스템·계약·과제·벤더와 Dedupe한다.
4. Physical/Financial denominator를 하나 이상 지정한다.
5. Core Data/IP와 외부 Capability 경계를 정하고 O/I Mode를 먼저 결정한다.
6. Finance/Contract/Compliance/SHE/Cyber/OI Hard Gate를 검사한다.
7. 하나라도 FAIL이면 점수와 관계없이 HOLD/NO-GO다.
8. 통과 후보만 100점 Pre-screen한다.
9. Dependency가 없으면 READY가 아니라 BLOCKED_BY_FOUNDATION으로 표시한다.
10. 최상위 과제도 가장 작은 Replay/Offline/Shadow Scope부터 추천한다.
11. G5에서 Domain 외 Finance/SHE/Legal/Cyber가 독립검증한다.
12. G8 PIR 결과를 다음 추천의 Prior 및 No-Go Memory로 저장한다.
```

## 3. AI가 하지 않는 것

- 제어 Setpoint, ESD/SIS, 가스차단, 보호계전 직접 조작
- Human limit 밖 Market bid/dispatch 자동 제출
- Tax·Legal·Regulatory eligibility 최종판정
- JV Reserved Matter·투자·계약·구매 승인
- 외부자료의 ROI를 E&S realized benefit으로 기록
- Source 없는 사실 보완, MOU→firm demand 변환, pipeline→operating capacity 변환

---
