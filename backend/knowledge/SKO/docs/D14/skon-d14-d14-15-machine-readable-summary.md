---
id: skon-d14-d14-15-machine-readable-summary
title: Machine-readable Summary
summary: "미국 세금 크레딧, EU 배터리 규제, CBAM 등 주요 정책의 현재 상태와 데이터 완성도, 우선 해결 과제를 정리한 구조화된 정책 현황 요약본"
tags: [d14, policy, schema, "xref:d15"]
keywords: [배터리 규제, 45X 크레딧, 세제 인센티브, CBAM, UFLPA, 컴플라이언스, 규제 의무, 구조화 데이터, 45X, 30D, PFE-MACR, EU 배터리 여권, 규제 현황, 데이터 격차, 세제 지원]
related: []
priority: normal
domain: D14
section: D14-15
source: SK온_D14_Policy_Regulation_Incentives_Compliance.md
breadcrumb: "SK온 D14 — Policy, Regulation, Incentives & Compliance"
tokens: 905
updated: 2026-08-03
---

> SK온 · D14 정책·규제·인센티브·컴플라이언스 · SK온 D14 — Policy, Regulation, Incentives & Compliance

## D14-15 Machine-readable Summary

```yaml
domain:
  id: D14
  name: Policy_Regulation_Incentives_and_Compliance
  version: v1.0
  as_of: 2026-08-03_KST

key_current_states:
  US_30D_new_vehicle_credit:
    status: TERMINATED_WITH_TRANSITION
    new_acquisition_cutoff: 2025-09-30
  US_45X:
    status: EFFECTIVE_WITH_PFE_MATERIAL_ASSISTANCE_RULE
    cell_base_credit_USD_per_qualified_kWh: 35
    module_with_cells_base_credit_USD_per_qualified_kWh: 10
    warning: capacity_is_not_claimed_or_cash_credit
  US_PFE_MACR:
    guidance: IRS_Notice_2026_15
    applies_to_45X_taxable_years_beginning_after: 2025-07-04
    decision_layers: [taxpayer_entity_PFE, eligible_component_material_assistance_MACR]
  EU_battery_passport:
    effective_date: 2027-02-18
    scope: [EV_battery, industrial_battery_over_2kWh, LMT_battery]
  EU_battery_due_diligence:
    effective_date: 2027-08-18
    materials: [cobalt, natural_graphite, lithium, nickel]
    verification: third_party_notified_body
  EU_carbon_and_recycled_content:
    status: PHASED_AND_CONDITIONAL_ON_SECONDARY_ACTS
  EU_CBAM:
    definitive_regime_start: 2026-01-01
    current_core_sectors: [cement, iron_and_steel, aluminium, fertilisers, electricity, hydrogen]
    warning: finished_battery_not_automatically_in_scope

registry:
  policy_events: 14
  pain_points: 14
  external_cases: 7
  oi_seeds: 15
  priority_poc_candidates: 5
  sources: 18

critical_gaps:
  - US_taxpayer_entity_and_related_party_election_by_facility
  - actual_qualified_kWh_claim_recognition_cash_and_credit_sharing
  - supplier_facility_ownership_control_debt_license_and_contract_rights
  - direct_material_cost_and_PFE_cost_by_component_lot_and_period
  - UFLPA_upstream_chain_of_custody_and_shipment_pre_clearance_pack
  - EU_economic_operator_role_by_OEM_program_and_member_state
  - battery_passport_model_instance_access_and_lifecycle_data
  - plant_product_carbon_footprint_and_secondary_act_version
  - recycled_content_product_mass_balance_and_third_party_verification
  - incentive_award_claim_cash_covenant_and_clawback_by_legal_entity
  - HTSUS_CN_origin_and_trade_measure_by_material_and_shipment
  - Korea_technology_and_asset_level_tax_eligibility

d17_priority_handoff:
  - OI-D14-04 PFE-MACR Compliance Engine
  - OI-D14-03 45X Qualified-kWh Evidence Agent
  - OI-D14-06 EU Battery Passport Data Fabric
  - OI-D14-09 Incentive Covenant and Clawback Monitor
  - OI-D14-01 Regulatory Obligation Knowledge Graph

completion:
  domain_boundary: COMPLETE
  data_model: COMPLETE
  US_tax_credit_architecture: COMPLETE_WITH_TAXPAYER_AND_CASH_GAPS
  PFE_MACR_engine: COMPLETE_AS_RULE_AND_DATA_SCHEMA
  trade_UFLPA_CBAM: COMPLETE_WITH_SHIPMENT_LEVEL_GAPS
  EU_battery_regulation: COMPLETE_WITH_SECONDARY_ACT_DEPENDENCIES
  incentives_and_Korea_policy: COMPLETE_WITH_ASSET_LEVEL_GAPS
  chemical_regulation: COMPLETE_AS_PROPOSAL_SCENARIO
  compliance_operating_model: COMPLETE
  pain_point_register: COMPLETE
  external_cases: COMPLETE
  oi_portfolio: COMPLETE_PRELIMINARY
  d17_bridge: COMPLETE
  source_registry: COMPLETE
```

## D14 완료 상태

**완료:** `SK온 D14 Policy, Regulation, Incentives & Compliance v1.0`

**다음 작업 지점:** `D15 Enterprise Risk, Quality, Safety & Resilience`
