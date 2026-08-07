---
id: skes-d11-21-machine-readable-summary
title: Machine-readable Summary
summary: "SK이노베이션 E&S 원가·수익성 영역의 재무 데이터(2025-2026), KPI 레지스트리, 데이터 갭, 완료도 현황을 조회할 수 있는 메타데이터 문서"
tags: [d11, cost, schema, "xref:d12"]
keywords: [영업마진, D11, LNG, cost_driver, BESS, 경제지표, hydrogen, CCS]
related: []
priority: normal
domain: D11
section: 21
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 688
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 21. Machine-readable Summary

```yaml
domain:
  id: D11
  name: Cost_Profitability_and_Business_Economics
  version: 1.0
  as_of: 2026-08-06_KST
  status: REPRESENTATIVE_COMPANY_DEEP_DB

public_profitability:
  FY2025:
    revenue_KRW_100m: 118631
    operating_profit_KRW_100m: 6811
    operating_margin_percent_derived: 5.74
  Q1_2026:
    revenue_KRW_100m: 36961
    operating_profit_KRW_100m: 2832
    operating_margin_percent_derived: 7.66
  Q2_2026:
    revenue_KRW_100m: 25961
    operating_profit_KRW_100m: 1059
    operating_margin_percent_derived: 4.08
  H1_2026:
    revenue_KRW_100m_derived: 62922
    operating_profit_KRW_100m_derived: 3891
    operating_margin_percent_derived: 6.18
  segment_breakdown_by_business:
    value: NOT_DISCLOSED
    rule: do_not_allocate_public_segment_profit_without_internal_ledger

registry:
  sources: 40
  cost_drivers: 72
  economics_KPIs: 52
  scenarios: 18
  pain_points: 35
  oi_seeds: 60
  priority_poc_candidates: 15
  internal_data_requests: 35

critical_gaps:
  - segment_to_legal_entity_asset_contract_reconciliation
  - LNG_contract_and_cargo_landed_cost
  - power_heat_rate_outage_and_settlement_margin
  - city_gas_weather_normalized_customer_cost_to_serve
  - PPA_hourly_shape_curtailment_and_credit_cost
  - BESS_degradation_adjusted_counterfactual_revenue
  - charging_site_and_installation_margin
  - hydrogen_production_to_paid_kg_economics
  - CCS_firm_capture_storage_match_and_long_tail_liability
  - working_capital_collateral_and_cash_conversion
  - finance_verified_OI_benefit_without_double_counting

completion:
  domain_boundary: COMPLETE
  evidence_policy: COMPLETE
  public_profitability_baseline: COMPLETE_WITH_SCOPE_LIMITATIONS
  economics_data_model: COMPLETE
  LNG_unit_economics: COMPLETE_AS_INTERNAL_SCHEMA
  power_CHP_economics: COMPLETE_AS_INTERNAL_SCHEMA
  city_gas_economics: COMPLETE_AS_INTERNAL_SCHEMA
  renewable_PPA_economics: COMPLETE_AS_INTERNAL_SCHEMA
  BESS_economics: COMPLETE_AS_INTERNAL_SCHEMA
  EV_charging_economics: COMPLETE_AS_INTERNAL_SCHEMA
  hydrogen_economics: COMPLETE_AS_INTERNAL_SCHEMA
  CCS_economics: COMPLETE_AS_INTERNAL_SCHEMA
  scenario_engine: COMPLETE
  pain_point_register: COMPLETE
  oi_seed_master: COMPLETE_PRELIMINARY
  d17_handoff: COMPLETE
```

---

# 22. Completion Note

**완료:** `SK이노베이션 E&S D11 Cost, Profitability & Business Economics v1.0`

**다음 작업 지점:** `D12 CAPEX, Investment, Funding & Financial Structure`
