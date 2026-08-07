---
id: skon-d14-d14-13-d17-bridge
title: D17 Bridge
summary: 정책·규제·인센티브가 D17과 연결되는 방식과 도메인 간 데이터 전달 규칙을 정의하는 문서
tags: [d14, policy, oi-seed, schema, table, "xref:d17", "xref:d01", "xref:d03", "xref:d05"]
keywords: [도메인 매핑, 정책 전달 규칙, eligibility 검증, PFE-MACR, 45X 증빙, UFLPA, Clawback, mandatory fields, handoff 규칙, 우선순위, 정책·규제·인센티브, 전달 규칙, Eligibility, PFE·UFLPA·EU, 세액공제, 법인·책임자, 원료·공급망]
related: []
priority: normal
domain: D14
section: D14-13
source: SK온_D14_Policy_Regulation_Incentives_Compliance.md
breadcrumb: "SK온 D14 — Policy, Regulation, Incentives & Compliance"
tokens: 1563
updated: 2026-08-03
---

> SK온 · D14 정책·규제·인센티브·컴플라이언스 · SK온 D14 — Policy, Regulation, Incentives & Compliance

## D14-13 D17 Bridge

### 1. Cross-domain 연결

| D14 정보 | 연결 도메인 | D17에서 사용할 질문 |
|---|---|---|
| 법인·책임자 | D01 | 어느 Legal Entity가 신고·시장출시·현금·Clawback을 부담하는가? |
| 제품·기술 | D03~D05 | 화학계·형태·IP·공정이 어떤 정책 Eligibility와 규제를 바꾸는가? |
| 공정·공장 | D06·D07 | 어느 Line의 생산·에너지·시험·판매가 세액공제·Passport 증빙인가? |
| 원료·공급망 | D08 | 어떤 Lot·시설·원가·원산지가 PFE·UFLPA·EU 실사에 연결되는가? |
| 고객·수요 | D09 | 정책 종료·변경이 OEM Forecast·ESS Pipeline을 어떻게 바꾸는가? |
| 시장·경쟁 | D10 | 경쟁사 Localisation·LFP·License 전략은 정책변화에 얼마나 탄력적인가? |
| 손익·현금 | D11 | 정책수익 없이도 반복이익이 남고, Claim이 실제 Cash로 전환되는가? |
| CAPEX·Funding | D12 | Eligibility·Covenant·Clawback을 반영한 Net CAPEX는 얼마인가? |
| 계약·JV | D13 | Credit Sharing·Change-in-law·Data·Audit·Exit 의무는 누구에게 있는가? |
| Risk | D15 | 어떤 정책 Event가 통관·가동·고객·유동성 중단을 촉발하는가? |
| 외부 Solution | D16 | RegTech·DPP·TaxTech·LCA·Traceability의 빈칸을 누가 채우는가? |

### 2. D17 전달 규칙

```yaml
d17_handoff_rule:
  mandatory_fields:
    - oi_seed_id
    - jurisdiction_authority_instrument_clause_and_version
    - legal_status_effective_date_transition_and_secondary_act_dependency
    - taxpayer_economic_operator_importer_producer_and_beneficiary_entity
    - facility_line_product_material_shipment_customer_program_scope
    - eligibility_prohibition_reporting_and_verification_rule
    - evidence_objects_source_ids_calculation_and_reviewer
    - eligible_applied_awarded_claimed_recognized_cash_and_clawback
    - policy_adjusted_demand_margin_CAPEX_and_landed_cost
    - required_internal_data_and_current_gap
    - owner_tax_legal_trade_EHS_product_compliance_and_finance
    - partner_type_PoC_duration_control_group_and_security
    - KPI_in_KRW_USD_kWh_days_percent_kgCO2e_and_audit_exceptions
  gates:
    - never_merge_30D_45X_48E_tariff_UFLPA_or_EU_market_access
    - never_convert_capacity_rate_or_award_ceiling_to_actual_cash
    - require_entity_facility_product_lot_transaction_and_period_specific_decision
    - separate_entity_PFE_from_material_assistance_MACR
    - calculate_EU_conditional_dates_from_latest_secondary_act
    - require_human_tax_legal_trade_and_product_compliance_approval
    - prohibit_autonomous_filing_certification_customs_release_claim_or_product_release
```

### 3. D17 우선 전달 레코드

```yaml
d14_priority_handoff:
  - oi_seed_id: OI-D14-04
    title: PFE-MACR Compliance Engine
    problem_proxy: ownership_control_contract_and_direct_material_cost_are_fragmented
    owner: tax_legal_procurement_compliance_cost_accounting
    partner_type: tax_trade_regtech_knowledge_graph_rules_engine
    poc_duration: 6_to_9_months
    success_kpi: full_PFE_cost_lot_certificate_and_reviewer_traceability
    source_ids: [SRC-D14-003, SRC-D14-004]

  - oi_seed_id: OI-D14-03
    title: 45X Qualified-kWh Evidence Agent
    problem_proxy: nameplate_capacity_production_sale_claim_recognition_and_cash_are_mixed
    owner: tax_plant_finance_operations_quality
    partner_type: taxtech_manufacturing_analytics_audit_workflow
    poc_duration: 4_to_6_months
    success_kpi: zero_double_counting_and_full_claim_to_cash_reconciliation
    source_ids: [SRC-D14-002, SRC-D14-003]

  - oi_seed_id: OI-D14-06
    title: EU Battery Passport Data Fabric
    problem_proxy: model_instance_lifecycle_and_access_data_are_fragmented_across_OEM_and_plants
    owner: EU_product_compliance_quality_IT_data_governance
    partner_type: digital_product_passport_data_space_cybersecurity
    poc_duration: 6_to_12_months
    success_kpi: validated_mandatory_fields_unique_ID_access_and_update_API
    source_ids: [SRC-D14-009, SRC-D14-010]

  - oi_seed_id: OI-D14-09
    title: Incentive Covenant and Clawback Monitor
    problem_proxy: award_ceiling_earned_benefit_cash_and_repayment_exposure_are_disconnected
    owner: tax_legal_HR_plant_finance_government_affairs
    partner_type: grant_taxtech_contract_workflow
    poc_duration: 4_to_6_months
    success_kpi: full_covenant_evidence_and_quantified_clawback_at_risk
    source_ids: [SRC-D14-008, SRC-D14-015, SRC-D14-016]

  - oi_seed_id: OI-D14-01
    title: Regulatory Obligation Knowledge Graph
    problem_proxy: legal_changes_do_not_propagate_to_product_contract_CAPEX_and_owner_fast_enough
    owner: compliance_legal_strategy_data_office
    partner_type: regtech_legal_NLP_knowledge_graph
    poc_duration: 6_to_9_months
    success_kpi: material_change_mapped_to_all_affected_scopes_and_owners_within_48_hours
    source_ids: [SRC-D14-001, SRC-D14-003, SRC-D14-009, SRC-D14-014]
```

D14가 D17에 넘기는 핵심은 `규제 대응을 자동화하자`는 일반론이 아니다. **공식 Rule Version을 실제 Cell·원료·공장·거래·법인에 연결하고, 적격성·시장접근·현금·Clawback을 같은 증빙에서 재현해 제품배정·조달·가격·투자 결정을 제때 바꾸는 체계**가 과제다.

---
