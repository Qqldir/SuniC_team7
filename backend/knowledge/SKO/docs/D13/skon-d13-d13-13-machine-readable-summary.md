---
id: skon-d13-d13-13-machine-readable-summary
title: Machine-readable Summary
summary: "SK온의 계약·합작투자 현황을 파트너별 공급량, 기술협력, 거버넌스로 구조화한 기계 가독형 마스터 데이터."
tags: [d13, contract, schema, "xref:d14"]
keywords: [공급 계약, JV 현황, 의무 사항, 파트너 메타데이터, 계약 레지스트리, 기계 가독, 배터리 협력, 협력사 현황, 계약 상태, HSBMA, 계약, 합작투자, 공급, 파트너, 거버넌스, BlueOval_SK, 기술협력, 의무, 공급량]
related: []
priority: normal
domain: D13
section: D13-13
source: SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md
breadcrumb: "SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure"
tokens: 994
updated: 2026-08-03
---

> SK온 · D13 계약·JV·거버넌스·파트너십 · SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

## D13-13 Machine-readable Summary

```yaml
domain:
  id: D13
  name: Contracts_Joint_Ventures_Governance_and_Partnership_Structure
  version: v1.0
  as_of: 2026-08-03_KST

public_agreement_baseline:
  HSBMA:
    ownership: 50_50
    announced_investment_USD_billion_approx: 5
    design_capacity_GWh: 35
    status: ACTIVE_JV_COMMERCIAL_OPERATION
    governance_terms: NOT_DISCLOSED
  BlueOval_SK:
    status: RESTRUCTURED_AND_SEPARATED
    transaction_close: 2026-05-20
    historical_DOE_advances_USD_billion: 7.83554
    Ford_historical_guarantee_share_percent: 50
    Ford_terminated_capital_commitment_USD_billion_up_to: 6.6
    Kentucky_note_assumed_by_Ford_USD_billion: 3.80504
    post_close_direction:
      Kentucky_assets_and_related_liabilities: Ford_side
      BOSK_equity_and_Tennessee_asset: SKBA_SK_On_side
    SK_On_side_remaining_obligations: NOT_FULLY_DISCLOSED
  Solid_Power:
    status: ACTIVE_R_AND_D_ONLY
    R_and_D_license_payment_USD_million: 20
    line_installation_estimated_USD_million: 22
    site_acceptance: COMPLETE_2026_Q1
    electrolyte_minimum_metric_tons_through_2030: 8
    supplier_latest_expected_minimum_revenue_USD_million: 8.3
    commercial_production_license: NOT_GRANTED_IN_PUBLIC_DESCRIPTION
  Nissan:
    status: ACTIVE_FUTURE_SUPPLY
    volume_GWh_approx: 100
    period: 2028_to_2033
  Slate:
    status: ACTIVE_PARTLY_OPTIONAL
    base_volume_GWh_approx: 20
    period: 2026_to_2031
    additional_volume: OPTION_NOT_FIRM
  Flatiron:
    status: ACTIVE_PARTLY_OPTIONAL
    binding_GWh: 1
    preferential_negotiation_GWh: 6.2
  ExxonMobil:
    status: NON_BINDING_MOU
    potential_lithium_metric_tons_up_to: 100000
  Ferrari:
    status: NON_BINDING_TECH_MOU

registry:
  public_agreement_relationships: 8
  pain_points: 14
  external_cases: 7
  oi_seeds: 15
  priority_poc_candidates: 5
  sources: 18

critical_gaps:
  - HSBMA_board_reserved_matters_capital_calls_guarantees_price_and_exit
  - BOSK_post_separation_SK_On_debt_guarantee_supply_IP_and_surviving_liability
  - Customer_contract_price_take_or_pay_calloff_cancellation_and_termination
  - Solid_Power_foreground_IP_data_validation_remedy_and_commercial_license_trigger
  - Agreement_family_priority_amendment_side_letter_and_waiver_lineage
  - Legal_obligor_economic_bearer_accounting_scope_cash_payer_and_beneficiary
  - Capital_call_default_deadlock_put_call_ROFR_tag_drag_and_change_of_control
  - Claim_LD_warranty_recall_price_true_up_and_reimbursement_exposure
  - Partner_credit_demand_technical_and_policy_trigger_early_warning
  - Clause_level_access_control_AI_provenance_and_external_data_sharing

d17_priority_handoff:
  - OI-D13-01 Contract-JV Obligation Knowledge Graph
  - OI-D13-02 Economic Attribution Engine
  - OI-D13-12 JV Exit and Separation Digital Room
  - OI-D13-03 Contract-to-Call-off and Acceptance Bridge
  - OI-D13-06 Milestone Acceptance Evidence Agent

completion:
  domain_boundary: COMPLETE
  data_model: COMPLETE
  public_agreement_ledger: COMPLETE_WITH_NON_DISCLOSED_CLAUSES
  JV_governance_and_attribution: COMPLETE_AS_CONTROL_MODEL
  commercial_obligation_hierarchy: COMPLETE
  IP_and_data_governance: COMPLETE_WITH_CONTRACT_GAPS
  change_dispute_exit_control: COMPLETE
  pain_point_register: COMPLETE
  external_cases: COMPLETE
  oi_portfolio: COMPLETE_PRELIMINARY
  d17_bridge: COMPLETE
  source_registry: COMPLETE
```

## D13 완료 상태

**완료:** `SK온 D13 Contracts, Joint Ventures, Governance & Partnership Structure v1.0`

**다음 작업 지점:** `D14 Policy, Regulation, Subsidies & Compliance`
