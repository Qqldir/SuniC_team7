---
id: skon-d12-d12-13-machine-readable-summary
title: Machine-readable Summary
summary: SK온의 자본지출·투자·자금조달 구조와 FY2025 재무 현황(자산·부채·현금흐름)을 구조화된 데이터로 정의한 기준선
tags: [d12, capex, schema, "xref:d13"]
keywords: [SK온 재무, CAPEX, 투자사업, HSBMA, BlueOval SK, 현금흐름, 자금조달, 자본구조, 유동성, 데이터 모델, 자본지출, 재무현황, 채권, JV]
related: []
priority: normal
domain: D12
section: D12-13
source: SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md
breadcrumb: "SK온 D12 — CAPEX, Investment, Funding & Financial Structure"
tokens: 889
updated: 2026-08-03
---

> SK온 · D12 CAPEX·투자·자금조달 · SK온 D12 — CAPEX, Investment, Funding & Financial Structure

## D12-13 Machine-readable Summary

```yaml
domain:
  id: D12
  name: CAPEX_Investment_Funding_and_Financial_Structure
  version: v1.0
  as_of: 2026-08-03_KST

public_baseline:
  scope: SK_Innovation_consolidated_not_SK_On_standalone
  FY2025:
    assets_KRW_trillion: 105.6085
    liabilities_KRW_trillion: 69.2170
    equity_KRW_trillion: 36.3915
    liabilities_to_equity_percent_derived: 190.2
    operating_cash_flow_KRW_trillion: 2.2831
    investing_cash_flow_KRW_trillion: -4.2854
    simple_FCF_proxy_KRW_trillion: -2.0023
    financing_cash_flow_KRW_trillion: 2.3457
    ending_cash_KRW_trillion: 16.0916
  SK_On_impairment_2025_KRW_trillion_approx: 4.2

major_public_investment_events:
  HSBMA:
    announced_gross_investment_USD_bn: 5.0
    ownership: 50_50
    design_capacity_GWh: 35
    status: COMMERCIAL_OPERATION
    warning: SK_On_actual_cash_contribution_not_disclosed
  BlueOval_SK:
    DOE_loan_approved_ceiling_USD_bn: 9.63
    status: RESTRUCTURED
    allocation_direction:
      Kentucky_assets_and_related_liabilities: Ford
      Tennessee_asset_and_obligations: SK_On_side
    warning: drawn_balance_and_exact_post_split_obligations_not_disclosed
  SK_On_2025_equity_event:
    announced_third_party_allotment_KRW_trillion: 2.0
    structure: PRS_linked
  SK_On_FI_exit_decision:
    parent_purchase_amount_KRW_trillion: 3.588

registry:
  pain_points: 14
  external_cases: 7
  oi_seeds: 15
  priority_poc_candidates: 5
  sources: 18

critical_gaps:
  - SK_On_standalone_and_entity_restricted_cash_debt_and_maturity
  - Project_and_line_level_approved_committed_paid_and_capitalized_CAPEX
  - Cost_to_complete_change_orders_and_ramp_cash_by_facility
  - JV_partner_contribution_capital_call_and_default_remedy
  - BOSK_post_separation_drawn_debt_guarantee_and_covenant_allocation
  - HSBMA_actual_partner_contribution_debt_incentive_and_clawback_terms
  - PRS_reference_price_settlement_and_all_in_economic_cost
  - Green_finance_instrument_balance_use_of_proceeds_and_impact
  - EV_to_ESS_and_format_conversion_CAPEX_qualification_and_exit_cost
  - CGU_level_recoverable_amount_and_impairment_leading_indicators

d17_priority_handoff:
  - OI-D12-01 CAPEX Real-Options Stage-Gate Engine
  - OI-D12-02 Asset-Debt-Guarantee Knowledge Graph
  - OI-D12-04 Ramp-to-Cash Liquidity Twin
  - OI-D12-03 Project Cost-to-Complete Causal AI
  - OI-D12-05 Incentive Covenant and Clawback Monitor

completion:
  domain_boundary: COMPLETE
  data_model: COMPLETE
  public_financial_baseline: COMPLETE_WITH_SCOPE_LIMITATIONS
  investment_and_JV_register: COMPLETE_WITH_NON_DISCLOSED_AMOUNTS
  funding_structure: COMPLETE_WITH_CURRENT_BALANCE_GAPS
  stage_gate_and_real_options: COMPLETE_AS_DECISION_LOGIC
  cash_and_impairment_control: COMPLETE_AS_INTERNAL_DATA_SCHEMA
  covenant_and_guarantee_control: COMPLETE_WITH_CONTRACT_GAPS
  pain_point_register: COMPLETE
  external_cases: COMPLETE
  oi_portfolio: COMPLETE_PRELIMINARY
  d17_bridge: COMPLETE
  source_registry: COMPLETE
```

## D12 완료 상태

**완료:** `SK온 D12 CAPEX, Investment, Funding & Financial Structure v1.0`

**다음 작업 지점:** `D13 Contracts, Joint Ventures, Governance & Partnership Structure`
