---
id: skon-d13-d13-11-d17-bridge
title: D17 Bridge
summary: "D13 계약·JV·거버넌스 정보를 D17 운영 및 컴플라이언스 도메인으로 전달할 때 필요한 크로스도메인 연결, 필수 필드, 전달 게이트와 우선순위를 정의하는 매핑 문서."
tags: [d13, contract, oi-seed, schema, table, "xref:d17", "xref:d01", "xref:d04", "xref:d05"]
keywords: [도메인연결, Cross-domain, 계약의무, 경제귀속, 전달규칙, 의무추적, 지식그래프, JV거버넌스, Cross-domain 연결, Contract Obligation, Economic Attribution, JV 거버넌스, Handoff Rule, Knowledge Graph, Mandatory Fields, D13-D17 매핑]
related: []
priority: normal
domain: D13
section: D13-11
source: SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md
breadcrumb: "SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure"
tokens: 1562
updated: 2026-08-03
---

> SK온 · D13 계약·JV·거버넌스·파트너십 · SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

## D13-11 D17 Bridge

### 1. Cross-domain 연결

| D13 정보 | 연결 도메인 | D17에서 사용할 질문 |
|---|---|---|
| 법인·조직·권한 | D01 | 누가 계약하고 승인하며 실제 의무를 부담하는가? |
| 기술·IP·Data | D04·D05 | R&D·Pilot·상업생산별 사용권과 공동개발 결과는 누구 것인가? |
| 공장·운영 | D06·D07 | 계약상 Capacity·Milestone·Change가 어느 공장·Line을 구속하는가? |
| 원료·공급사 | D08 | MOU·Offtake·PO·입고 중 실제 공급확보는 어디까지인가? |
| 고객·수요 | D09 | 총계약·Option·Forecast·Call-off·Accepted Volume은 어떻게 다른가? |
| 손익·현금 | D11 | Credit·보상·가격조정·비용·자산의 경제적 귀속은 누구에게 있는가? |
| 투자·자금조달 | D12 | 자산·Debt·Guarantee·Capital Call·Exit Cost의 법적 귀속은 누구인가? |
| 정책 | D14 | Change of Control·고용·투자·보고조건이 어떤 Consent·Clawback을 만드는가? |
| Risk | D15 | 어떤 위반·분쟁·Partner 변화가 공급·현금·운영중단을 촉발하는가? |
| 외부 Solution | D16 | CLM·Legal AI·Knowledge Graph·Data Room의 빈칸을 누가 채우는가? |

### 2. D17 전달 규칙

```yaml
d17_handoff_rule:
  mandatory_fields:
    - oi_seed_id
    - deal_agreement_clause_and_version_scope
    - legal_parties_obligor_beneficiary_and_guarantor
    - legal_entity_facility_line_product_customer_program_links
    - binding_status_base_option_ROFO_forecast_PO_and_accepted_quantity
    - right_obligation_condition_due_date_evidence_and_status
    - ownership_board_reserved_matter_capital_call_and_default_remedy
    - legal_obligor_economic_bearer_accounting_scope_and_cash_payer
    - background_foreground_IP_field_of_use_data_and_survival_rights
    - amendment_waiver_claim_dispute_transfer_exit_and_transition
    - quantified_problem_proxy_and_required_internal_data
    - owner_legal_finance_business_IP_and_technical_validator
    - partner_type_PoC_duration_control_group_and_source_ids
    - KPI_in_KRW_days_percent_GWh_and_orphan_obligation_count
  gates:
    - never_infer_governance_or_economic_burden_from_ownership_alone
    - never_upgrade_MOU_option_ROFO_or_forecast_to_firm_obligation
    - require_clause_level_source_and_human_legal_validation
    - reconcile_all_agreement_family_dependencies_and_latest_versions
    - separate_R_and_D_license_from_commercial_production_rights
    - quantify_both_value_recovery_and_downside_liability
    - prohibit_autonomous_notice_waiver_claim_dispute_amendment_or_termination
```

### 3. D17 우선 전달 레코드

```yaml
d13_priority_handoff:
  - oi_seed_id: OI-D13-01
    title: Contract-JV Obligation Knowledge Graph
    problem_proxy: agreement_families_and_obligations_are_fragmented_across_entities_and_documents
    owner: legal_JV_management_strategy_finance
    partner_type: legaltech_knowledge_graph_contract_analytics
    poc_duration: 6_to_9_months
    success_kpi: all_material_obligations_linked_to_clause_owner_evidence_and_entity
    source_ids: [SRC-D13-001, SRC-D13-003, SRC-D13-004, SRC-D13-007]

  - oi_seed_id: OI-D13-02
    title: Economic Attribution Engine
    problem_proxy: legal_obligor_accounting_scope_cash_payer_and_economic_bearer_can_differ
    owner: legal_controller_treasury_tax_JV_management
    partner_type: legal_finance_analytics_rules_engine
    poc_duration: 6_to_9_months
    success_kpi: finance_and_legal_approved_gross_to_net_exposure_without_double_counting
    source_ids: [SRC-D13-003, SRC-D13-004, SRC-D13-005, SRC-D13-006]

  - oi_seed_id: OI-D13-12
    title: JV Exit and Separation Digital Room
    problem_proxy: BOSK_separation_requires_simultaneous_transfer_of_asset_debt_guarantee_contract_IP_and_surviving_duty
    owner: legal_M_and_A_treasury_HR_IT_operations
    partner_type: M_and_A_legaltech_virtual_data_room_workflow
    poc_duration: 4_to_6_months
    success_kpi: zero_orphan_obligations_and_full_closing_evidence_coverage
    source_ids: [SRC-D13-003, SRC-D13-004, SRC-D13-005, SRC-D13-006]

  - oi_seed_id: OI-D13-03
    title: Contract-to-Call-off and Acceptance Bridge
    problem_proxy: announced_total_base_option_forecast_PO_and_accepted_volume_are_mixed
    owner: sales_S_and_OP_supply_chain_finance_legal
    partner_type: CLM_supply_chain_analytics_data_integration
    poc_duration: 6_to_9_months
    success_kpi: zero_double_counting_and_monthly_accepted_volume_reconciliation
    source_ids: [SRC-D13-009, SRC-D13-010, SRC-D13-011]

  - oi_seed_id: OI-D13-06
    title: Milestone Acceptance Evidence Agent
    problem_proxy: license_line_installation_and_supply_milestones_trigger_rights_and_payments_across_contracts
    owner: R_and_D_engineering_procurement_legal_finance
    partner_type: document_AI_quality_workflow_contract_analytics
    poc_duration: 4_to_6_months
    success_kpi: faster_acceptance_cycle_and_zero_unsubstantiated_payment_trigger
    source_ids: [SRC-D13-007, SRC-D13-008]
```

D13이 D17에 넘기는 핵심은 `계약을 AI로 요약하자`가 아니다. **최신 원문 Clause에서 권리·의무와 조건을 추출하고, 실제 증빙·법인·공장·고객·현금·IP에 연결해 이행·변경·재협상·Exit 의사결정을 안전하게 만드는 것**이 과제다.

---
