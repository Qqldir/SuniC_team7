---
id: skon-d17-d17-06-ai-task-recommendation-engine
title: AI Task Recommendation Engine
summary: "D17 오픈이노베이션 포트폴리오에서 Pain Point와 증거를 기반으로 과제를 평가·추천하고 우선순위를 매기는 AI 엔진의 스키마, 로직, 의존성을 설명하는 문서."
tags: [d17, oi-portfolio, oi-seed, schema, table]
keywords: [오픈이노베이션, 포트폴리오 구성, 의존 관계, Pain Point, PoC, 스코어링, Hard Gate, 의사결정, 과제평가, 포트폴리오, 의존성, 우선순위결정, 게이팅프로세스]
related: []
priority: normal
domain: D17
section: D17-06
source: SK온_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation
tokens: 865
updated: 2026-08-03
---

> SK온 · D17 오픈이노베이션 과제 포트폴리오·AI 추천 · SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation

## D17-06 AI Task Recommendation Engine

### 1. 입력 스키마

```yaml
oi_task_record:
  task_id: D17-OI-...
  title: null
  source_seed_ids: []
  pain_point:
    statement: null
    status: VERIFIED_FACT|ANALYTICAL_DERIVATION|HYPOTHESIS|NOT_DISCLOSED
    denominator_unit_period: null
    affected_entity_site_line_product_customer_supplier: []
    quantified_loss_time_safety_or_market_access: null
    cause_confidence: null
  decision:
    accountable_owner: null
    operator: null
    human_approvers: []
    current_workflow_and_systems: []
  capability:
    required_outcome: null
    build_buy_codevelop_license_partner_invest_observe: null
    non_negotiable_controls: []
  provider:
    legal_entity_solution_version: null
    evidence_level_reference_claim_owner_date: null
    existing_SK_On_relationship_exact_scope: null
    conflict_vendor_health_lock_in: []
  poc:
    site_line_product_customer_supplier_period: null
    baseline_control_group_counterfactual: null
    primary_KPI_unit: null
    secondary_KPI_units: []
    guardrails: []
    duration: null
    G0_to_G8_status: null
    stop_scale_exit_criteria: []
  rights:
    data_access_classification_retention_deletion_export: []
    training_reuse_and_derived_model_rights: []
    background_foreground_improvement_IP: []
  economics:
    implementation_cost_internal_hours_TCO: null
    value_KRW_per_accepted_kWh_cash_risk_safety: null
    double_count_group_id: null
  evidence:
    source_ids: []
    as_of_date: null
    stale_or_conflict_flag: false
  score:
    total_100: null
    tier: P0|P1|P2|HOLD|NO_GO
    hard_gate_flags: []
```

### 2. 추천 로직

```text
1. 최신 Source와 Scope를 확인한다.
2. Pain Point가 재현되지 않으면 추천하지 않고 G0 Problem Proof를 생성한다.
3. 기존 과제·시스템·계약·협력과 Dedupe한다.
4. Core Data/IP 여부에 따라 Build–Buy–Partner 자세를 먼저 정한다.
5. Hard Gate를 검사한다. 하나라도 위반하면 HOLD/NO-GO다.
6. 100점 사전심사와 Evidence Confidence를 계산한다.
7. 동일 가치의 이중계상을 막고 Dependency를 반영해 Portfolio를 구성한다.
8. 최상위 과제라도 가장 작은 Bounded Scope와 G0/G1부터 추천한다.
9. Human Approver가 승인한 Decision만 실행시스템으로 전달한다.
10. G5 독립검증과 G8 PIR 결과를 다음 추천의 Prior로 사용한다.
```

### 3. Dependency Rule

| 선행 기반 | 의존 과제 |
|---|---|
| 001·002·003 | 모든 D17 과제의 근거·Gate·학습 |
| 004 | 외부 AI·Sensor·DPP·Analytics 비교 |
| 006 | 007·008·009·010·016·021 |
| 011 | 012·013·014·015·024·026 |
| 016·031 | 017·018·025·032·036~040 |
| 021 | 007·013·022~030·041~045 |
| 046 | 036·043·045·047~050 |

AI는 의존 기반이 없을 때 후속 과제를 `READY`로 추천하지 않고 `BLOCKED_BY_FOUNDATION`으로 표시한다.

---
