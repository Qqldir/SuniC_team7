---
id: skon-d11-d11-12-machine-readable-summary
title: Machine-readable Summary
summary: "SK온 배터리 세그먼트의 FY2025~Q2 2026 수익·원가·마진 현황과 주요 데이터 공백, 도메인 완료도를 메타데이터로 정리한 요약."
tags: [d11, cost, schema, "xref:d12"]
keywords: [영업이익, 배터리 세그먼트, 원가, 매출, AMPC, kWh 단가, 마진율, 데이터 갭, 배터리 원가, 수익성, 고객 원가, 데이터 공백, 단위경제, 이코노믹스, 메타데이터, 완료도]
related: []
priority: normal
domain: D11
section: D11-12
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 724
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-12 Machine-readable Summary

```yaml
domain:
  id: D11
  name: Cost_Profitability_and_Business_Economics
  version: v1.0
  as_of: 2026-08-03_KST

public_baseline:
  FY2025_battery_segment:
    revenue_KRW_trillion: 6.9782
    operating_profit_KRW_trillion: -0.9319
    operating_margin_percent_derived: -13.4
    AMPC_KRW_bn_derived_from_Q3_cumulative_plus_Q4: 718.6
    ex_AMPC_simple_loss_proxy_KRW_bn: -1650.5
    warning: not_audited_recurring_EBIT
  Q1_2026_battery_segment:
    revenue_KRW_trillion: 1.7912
    operating_profit_KRW_bn: -349.2
    operating_margin_percent_derived: -19.5
  Q2_2026_battery_segment:
    revenue_KRW_trillion: 2.9460
    operating_profit_KRW_bn: 821.8
    operating_margin_percent_derived: 27.9
    recurring_EBIT: NOT_CALCULABLE_FROM_PUBLIC_DATA
    adjustment_amounts_not_disclosed:
      - customer_compensation
      - increased_IRA_credit

registry:
  pain_points: 14
  external_cases: 7
  oi_seeds: 15
  priority_poc_candidates: 5
  sources: 17

critical_gaps:
  - Plant-product-customer-program actual margin and cash contribution
  - Customer-accepted GWh denominator and price per kWh
  - Q2 2026 customer compensation and IRA credit amounts
  - AMPC eligible-claimed-recognized-cash reconciliation by facility
  - First-pass yield, scrap, rework and cost of poor quality by process
  - Fixed-cost absorption by customer-qualified line
  - Customer-specific logistics, engineering, quality and warranty cost-to-serve
  - Metal and FX pass-through lag and inventory effect
  - EV-to-ESS conversion CAPEX, qualification lead time and opportunity cost
  - Program-level working capital, impairment trigger and exit cost

d17_priority_handoff:
  - OI-D11-01 Qualified-kWh Cost Digital Twin
  - OI-D11-03 Yield-to-Margin Causal AI
  - OI-D11-02 Recurring Profit Waterfall Engine
  - OI-D11-04 Fixed-Cost Absorption and Mix Optimizer
  - OI-D11-05 Customer Program Lifecycle Economics Graph

completion:
  domain_boundary: COMPLETE
  data_model: COMPLETE
  public_profitability_baseline: COMPLETE_WITH_SCOPE_LIMITATIONS
  recurring_profit_waterfall: COMPLETE_WITH_PUBLIC_DATA_GAPS
  qualified_kWh_unit_economics: COMPLETE_AS_INTERNAL_DATA_SCHEMA
  cost_driver_tree: COMPLETE
  scenario_engine: COMPLETE_AS_DECISION_LOGIC
  pain_point_register: COMPLETE
  external_cases: COMPLETE
  oi_portfolio: COMPLETE_PRELIMINARY
  d17_bridge: COMPLETE
  source_registry: COMPLETE
```

## D11 완료 상태

**완료:** `SK온 D11 Cost, Profitability & Business Economics v1.0`

**다음 작업 지점:** `D12 CAPEX, Investment, Funding & Financial Structure`
