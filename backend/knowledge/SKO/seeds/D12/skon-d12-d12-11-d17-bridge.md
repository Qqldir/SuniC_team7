---
id: skon-d12-d12-11-d17-bridge
title: D17 Bridge
summary: "D12 CAPEX 의사결정 정보를 D17 리스크 분석에 전달할 때 필요한 필수 필드, 검증 규칙, 크로스 도메인 연결을 명시한 전달 프레임워크."
tags: [d12, capex, oi-seed, schema, table, "xref:d17", "xref:d06", "xref:d07", "xref:d08"]
keywords: [CAPEX 커밋먼트, Cross-domain 연결, D12 D17 정보전달, 도메인 매핑, 필수 필드, 검증 게이트, 자산부채보증, Real-Options, 우선 이행과제, 합작투자 거버넌스, CAPEX-투자 연계, 필수 전달 필드, 크로스 도메인, 현금 노출, 리스크 트리거, 실옵션 분석, 계약 선형성, 우선 연결 사항]
related: []
priority: normal
domain: D12
section: D12-11
source: SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md
breadcrumb: "SK온 D12 — CAPEX, Investment, Funding & Financial Structure"
tokens: 1475
updated: 2026-08-03
---

> SK온 · D12 CAPEX·투자·자금조달 · SK온 D12 — CAPEX, Investment, Funding & Financial Structure

## D12-11 D17 Bridge

### 1. Cross-domain 연결

| D12 정보 | 연결 도메인 | D17에서 사용할 질문 |
|---|---|---|
| 설비·공사·Ramp | D06·D07 | 어떤 Critical Path와 설비위험이 Cost-to-Complete와 SOP를 바꾸는가? |
| 원료·현지화 투자 | D08 | 공급안정·PFE 적격·원가절감을 위해 어느 자산에 투자해야 하는가? |
| 고객승인·수요 | D09 | 고객 확정수요가 어느 CAPEX Commitment를 정당화하는가? |
| 시장·전환 Option | D10 | EV·ESS·화학계 변화에서 expand/hold/convert/exit 중 최적안은 무엇인가? |
| 반복이익·현금 | D11 | 정책·보상을 제외해도 투자 후 Accepted-kWh Cash가 남는가? |
| 계약·JV Governance | D13 | 자산·부채·보증·Credit·Exit Cost의 법적 귀속은 누구에게 있는가? |
| 정책·보조금 | D14 | 지원 적격성·상환·Clawback을 반영한 Net CAPEX는 얼마인가? |
| Downside Risk | D15 | 어떤 Trigger가 유동성·Covenant·손상·사업중단을 촉발하는가? |
| 외부 Solution | D16 | Digital Twin·Project Controls·FinTech·LegalTech의 빈칸을 누가 채우는가? |

### 2. D17 전달 규칙

```yaml
d17_handoff_rule:
  mandatory_fields:
    - oi_seed_id
    - legal_entity_facility_line_and_customer_program_scope
    - decision_gate_and_business_case_version
    - gross_project_cost_and_SK_On_net_cash_exposure
    - committed_paid_capitalized_and_cost_to_complete
    - funding_instrument_partner_contribution_and_guarantee
    - incentive_cash_and_clawback_exposure
    - base_downside_severe_incremental_cash_and_ROIC
    - expand_hold_convert_mothball_sell_exit_options
    - required_internal_data_and_source_ids
    - owner_finance_legal_and_technical_validator
    - partner_type_PoC_duration_and_control_group
    - KPI_in_KRW_cash_months_and_customer_accepted_kWh
  gates:
    - reconcile_group_segment_entity_JV_and_project_scope
    - never_convert_announced_total_or_loan_ceiling_to_actual_cash
    - use_incremental_forward_cash_not_sunk_cost
    - include_ramp_working_capital_financing_guarantee_and_exit_cost
    - separate_eligible_awarded_recognized_and_cash_policy_support
    - require_clause_level_covenant_and_obligation_lineage
    - prohibit_autonomous_CAPEX_financing_guarantee_shutdown_or_sale
```

### 3. D17 우선 전달 레코드

```yaml
d12_priority_handoff:
  - oi_seed_id: OI-D12-01
    title: CAPEX Real-Options Stage-Gate Engine
    problem_proxy: demand_product_policy_and_CAPEX_commitments_change_at_different_speeds
    owner: strategy_CFO_FPandA_global_operations
    partner_type: real_options_scenario_and_decision_intelligence
    poc_duration: 6_to_9_months
    success_kpi: finance_approved_incremental_NPV_range_and_stop_triggers
    source_ids: [SRC-D12-001, SRC-D12-003, SRC-D12-004, SRC-D12-006]

  - oi_seed_id: OI-D12-02
    title: Asset-Debt-Guarantee Knowledge Graph
    problem_proxy: BOSK_separation_requires_clause_level_asset_liability_and_guarantee_lineage
    owner: legal_treasury_accounting_JV_management
    partner_type: legaltech_knowledge_graph_contract_analytics
    poc_duration: 4_to_6_months
    success_kpi: complete_obligation_transfer_and_zero_orphan_exposure
    source_ids: [SRC-D12-002, SRC-D12-010, SRC-D12-011, SRC-D12-012]

  - oi_seed_id: OI-D12-04
    title: Ramp-to-Cash Liquidity Twin
    problem_proxy: group_cash_does_not_equal_entity_available_cash_and_ramp_cash_need_is_dynamic
    owner: treasury_FPandA_manufacturing_finance
    partner_type: treasury_analytics_digital_twin
    poc_duration: 6_to_9_months
    success_kpi: monthly_liquidity_forecast_accuracy_and_downside_runway
    source_ids: [SRC-D12-003, SRC-D12-004, SRC-D12-008, SRC-D12-009]

  - oi_seed_id: OI-D12-03
    title: Project Cost-to-Complete Causal AI
    problem_proxy: budget_commitment_physical_progress_and_ramp_cost_are_fragmented
    owner: capex_PMO_procurement_engineering_finance
    partner_type: construction_analytics_causal_AI_project_controls
    poc_duration: 6_to_12_months
    success_kpi: cost_and_schedule_overrun_warning_at_least_three_months_early
    source_ids: [SRC-D12-008, SRC-D12-009, SRC-D12-017]

  - oi_seed_id: OI-D12-05
    title: Incentive Covenant and Clawback Monitor
    problem_proxy: employment_investment_production_and_reporting_conditions_create_cash_and_guarantee_exposure
    owner: tax_legal_HR_government_affairs_plant_finance
    partner_type: regtech_taxtech_evidence_workflow
    poc_duration: 4_to_6_months
    success_kpi: full_covenant_evidence_coverage_and_quantified_clawback_at_risk
    source_ids: [SRC-D12-013, SRC-D12-014, SRC-D12-016]
```

D12가 D17에 넘기는 핵심은 `투자를 줄이자`는 일반론이 아니다. **고객이 인수할 합격 kWh와 반복현금을 기준으로 각 투자 Option의 추가 현금부담·자금조달·보증·정책조건·Exit Cost를 비교하고, 정보가 바뀔 때 확장·보류·전환·철수를 제때 결정하는 체계**가 과제다.

---
