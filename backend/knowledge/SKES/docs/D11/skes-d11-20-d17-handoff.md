---
id: skes-d11-20-d17-handoff
title: D17 Handoff
summary: D11 원가·수익성 분석을 D17 실행 단계로 인수인계할 때 필수 정보 13개 항목과 우선순위 항목을 정의한 문서
tags: [d11, cost, schema, table, "xref:d17", "xref:d08", "xref:d06", "xref:d07"]
keywords: [인수인계, D11-D17, 경제성분석, 필수필드, EBIT, 마진, 원가, 수익성, POC, 카운터팩추얼]
related: []
priority: normal
domain: D11
section: 20
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 1176
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 20. D17 Handoff

## 20.1 Cross-domain Join

| D11 Output | Upstream Domain | D17 질문 |
|---|---|---|
| Contract/Cargo Margin | D08 | 어느 공급·운송·권리 조합이 반복 Margin과 현금을 만드는가? |
| Heat-rate·Outage Cost | D06·D07 | 어느 설비·운전조건·고장모드의 경제적 손실이 가장 큰가? |
| Customer Cost-to-Serve | D09 | 물량이 아니라 순이익·현금 기준으로 우선 고객은 누구인가? |
| Market Scenario | D10 | 가격·수요·경쟁 변화가 어떤 자산에 얼마의 Margin-at-Risk를 만드는가? |
| CAPEX/ROIC Gate | D12 | 증설·전환·유지·매각 중 위험조정 가치가 가장 큰 Option은 무엇인가? |
| Contract/JV Economics | D13 | 수익·비용·Credit·책임의 경제적 귀속은 누구에게 있는가? |
| Policy-on/off Economics | D14 | 지원이 없거나 지연돼도 생존 가능한가? |
| Tail Loss | D15 | 어떤 Trigger가 유동성·손상·운영중단을 일으키는가? |
| Partner Capability Gap | D16 | 데이터·모델·센서·통합·현장검증의 빈칸을 누가 채우는가? |

## 20.2 Mandatory Handoff Fields

```yaml
d17_economics_handoff:
  mandatory_fields:
    - seed_id_and_problem_statement
    - business_asset_contract_customer_scope
    - baseline_period_and_counterfactual
    - physical_denominator_and_settlement_boundary
    - recurring_EBIT_cash_and_risk_hypothesis
    - required_internal_data_and_owner
    - external_partner_type_and_integration_boundary
    - implementation_cost_and_change_cost
    - safety_regulatory_market_and_cyber_constraints
    - poc_duration_control_group_and_success_KPI
    - benefit_class_and_double_count_dependency
    - scale_exit_and_vendor_lock_in_gate
    - source_ids_and_claim_status
```

## 20.3 D11 Priority Handoff Records

```yaml
d11_priority_handoff:
  - seed_id: SEED-ENS-D11-002
    title: Segment-to-Asset Margin Graph
    problem: E&S_segment_profit_cannot_be_allocated_by_public_data
    owner: CFO_controller_FPandA_business_finance
    partner: energy_data_graph_and_management_accounting_analytics
    poc: one_power_asset_plus_connected_LNG_route
    success: reconcile_revenue_cost_EBIT_and_cash_to_control_total

  - seed_id: SEED-ENS-D11-007
    title: Cargo Landed-cost Digital Twin
    problem: contract_shipping_terminal_inventory_and_destination_costs_are_fragmented
    owner: LNG_trading_terminal_SCM_finance
    partner: commodity_analytics_maritime_AI_optimization
    poc: ten_to_twenty_completed_cargoes
    success: finance_verified_landed_cost_and_margin_per_cargo

  - seed_id: SEED-ENS-D11-017
    title: Heat-rate-to-P&L Causal AI
    problem: operating_efficiency_is_not_closed_to_fuel_cost_and_EBIT
    owner: power_operations_engineering_finance
    partner: industrial_AI_digital_twin_sensor_analytics
    poc: one_CCGT_unit_full_season
    success: recurring_fuel_saving_verified_without_safety_or_availability_loss

  - seed_id: SEED-ENS-D11-035
    title: BESS Shadow-bid Counterfactual Lab
    problem: algorithm_uplift_requires_same_constraint_counterfactual
    owner: KCE_trading_asset_management_risk_finance
    partner: electricity_market_simulation_MLOps
    poc: one_or_two_assets_with_shadow_bids
    success: risk_and_degradation_adjusted_net_revenue_uplift

  - seed_id: SEED-ENS-D11-048
    title: Paid-kg Hydrogen Cost Twin
    problem: nameplate_tonnes_do_not_measure_delivered_and_paid_hydrogen_economics
    owner: hydrogen_plant_logistics_sales_finance
    partner: process_digital_twin_mass_balance_TEA
    poc: plant_to_one_fleet_cluster
    success: production_to_paid_kg_and_cost_reconciliation

  - seed_id: SEED-ENS-D11-054
    title: CCS Capture-Storage Match Graph
    problem: announced_storage_capacity_can_be_stranded_without_firm_capture
    owner: CCS_business_development_engineering_finance_legal
    partner: project_finance_geospatial_contract_graph_MRV
    poc: Bayu_Undan_candidate_emitter_portfolio
    success: probability_weighted_firm_volume_and_COD_coverage
```

---
