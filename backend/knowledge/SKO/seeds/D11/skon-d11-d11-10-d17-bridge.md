---
id: skon-d11-d11-10-d17-bridge
title: D17 Bridge
summary: D11의 원가·수익성 정보가 D17 의사결정 도메인으로 전달되는 매핑 규칙과 필수 전달 항목을 설명하는 연결 가이드.
tags: [d11, cost, oi-seed, schema, table, "xref:d17", "xref:d06", "xref:d07", "xref:d08"]
keywords: [D11-D17 연결, 원가구조, Qualified-kWh, Material Leakage, Customer Program Margin, 디지털 트윈, 수율·마진 분석, OI 시드, 반복이익, 전달규칙, 단위 원가, 원가 누수, 고객 프로그램, 정책 지원, 다운사이드, 외부 파트너, CAPEX 의사결정]
related: []
priority: normal
domain: D11
section: D11-10
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 1283
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-10 D17 Bridge

### 1. Cross-domain 연결

| D11 정보 | 연결 도메인 | D17에서 사용할 질문 |
|---|---|---|
| Qualified-kWh Unit Cost | D06·D07 | 어느 공정·Line·Ramp가 판매 가능한 kWh의 원가를 가장 크게 높이는가? |
| Material/Metal/FX Leakage | D08 | 조달가격과 고객 Pass-through 사이의 Margin 누수는 어디서 생기는가? |
| Customer Program Margin | D09 | 수주잔고가 아니라 실제로 반복이익과 현금을 만드는 Program은 무엇인가? |
| Market Price & Mix | D10 | LFP·Prismatic·ESS 전환이 가격·원가·가동률을 합쳐 이익을 개선하는가? |
| CAPEX·Impairment·Cash | D12 | 증설·휴지·전환 중 Risk-adjusted ROIC가 가장 높은 Option은 무엇인가? |
| Contract/JV Scope | D13 | Credit·보상·비용·자산의 경제적 귀속은 어느 법인과 Partner에 있는가? |
| Policy Eligibility | D14 | 정책지원이 사라져도 생존 가능한 원가구조인가? |
| Downside Trigger | D15 | 어떤 수요·수율·가동률·Credit 변화가 손상·현금위험을 촉발하는가? |
| External Solution | D16 | 어떤 Partner가 Sensor·Model·Integration·현장검증의 빈칸을 채울 수 있는가? |

### 2. D17 전달 규칙

```yaml
d17_handoff_rule:
  mandatory_fields:
    - oi_seed_id
    - plant_product_customer_and_program_scope
    - baseline_period_and_reporting_scope
    - quantified_problem_proxy
    - recurring_profit_and_cash_hypothesis
    - required_internal_data
    - decision_owner_and_finance_validator
    - external_partner_type
    - poc_duration_and_control_design
    - success_kpi_in_KRW_and_accepted_kWh
    - implementation_and_change_cost
    - source_ids
  gates:
    - reconcile_segment_entity_plant_and_program_scope
    - separate_reported_recurring_policy_and_one_off_profit
    - use_customer_accepted_kWh_as_primary_denominator
    - validate_contract_price_cost_and_customer_data_security
    - prevent_double_counting_of_improvement_benefits
    - distinguish_accounting_saving_cash_saving_and_avoided_cost
    - estimate_downside_exit_and_warranty_cost
    - prohibit_autonomous_process_bid_capex_or_shutdown_decision
```

### 3. D17 우선 전달 레코드

```yaml
d11_priority_handoff:
  - oi_seed_id: OI-D11-01
    title: Qualified-kWh Cost Digital Twin
    problem_proxy: public_profit_volatility_and_missing_plant_product_customer_unit_cost
    owner: CFO_controller_manufacturing_finance
    partner_type: battery_TEA_industrial_data_platform
    poc_duration: 6_to_9_months
    success_kpi: reconciled_cost_and_margin_per_customer_accepted_kWh

  - oi_seed_id: OI-D11-03
    title: Yield-to-Margin Causal AI
    problem_proxy: yield_scrap_capacity_and_margin_losses_are_fragmented
    owner: manufacturing_quality_finance
    partner_type: causal_AI_sensor_process_analytics_consortium
    poc_duration: 6_to_12_months
    success_kpi: finance_verified_recurring_margin_recovery

  - oi_seed_id: OI-D11-02
    title: Recurring Profit Waterfall Engine
    problem_proxy: Q2_2026_adjustment_amounts_not_public_and_recurring_EBIT_not_calculable
    owner: CFO_accounting_FPandA_tax
    partner_type: finance_AI_accounting_analytics
    poc_duration: 4_to_6_months
    success_kpi: complete_adjustment_lineage_and_recurring_EBIT_range

  - oi_seed_id: OI-D11-04
    title: Fixed-Cost Absorption and Mix Optimizer
    problem_proxy: utilization_and_customer_program_changes_amplify_fixed_cost
    owner: global_operations_SCM_sales_finance
    partner_type: operations_research_APS
    poc_duration: 6_to_9_months
    success_kpi: lower_fixed_cost_per_accepted_kWh_without_service_loss

  - oi_seed_id: OI-D11-05
    title: Customer Program Lifecycle Economics Graph
    problem_proxy: quote_to_actual_cost_to_serve_and_warranty_gap
    owner: sales_program_management_quality_finance
    partner_type: knowledge_graph_CPQ_PLM_analytics
    poc_duration: 6_to_9_months
    success_kpi: program_margin_bridge_from_quote_to_EOP
```

D11이 D17에 넘기는 핵심은 `원가를 낮추자`는 일반론이 아니다. **같은 고객승인 kWh를 더 적은 재료·시간·에너지·고정비·품질비용으로 만들고, 정책지원과 일회성 보상을 제외해도 현금이 남는지 증명하는 체계**가 과제다.

---
