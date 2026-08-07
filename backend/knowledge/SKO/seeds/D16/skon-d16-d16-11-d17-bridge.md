---
id: skon-d16-d16-11-d17-bridge
title: D17 Bridge
summary: "D16의 9개 도메인별 정보를 D17로 전달할 때 필수 필드, 검증 게이트, 우선순위를 정의한 외부솔루션 인수인계 프로세스."
tags: [d16, ecosystem, oi-seed, schema, table, "xref:d17", "xref:d01", "xref:d02", "xref:d03"]
keywords: [벤더, 공급자, Open Innovation, 도메인 연결, 전달 규칙, 게이트, 외부 솔루션, 검증, PoC, D16-D17, D16-D17 핸드오프, 외부솔루션 검증, 필수필드, 검증게이트, 오픈이노베이션, 에비던스, 도메인연결]
related: []
priority: normal
domain: D16
section: D16-11
source: SK온_D16_External_Solutions_Startups_Vendors_Open_Innovation_Ecosystem.md
breadcrumb: "SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem"
tokens: 1537
updated: 2026-08-03
---

> SK온 · D16 외부 솔루션·스타트업·벤더 생태계 · SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem

## D16-11 D17 Bridge

### 1. Cross-domain 연결

| D16 정보 | 연결 도메인 | D17에서 사용할 질문 |
|---|---|---|
| 법인·Owner·기존 협력 | D01 | 누가 Sponsor·Operator·Approver이며 기존 관계를 재사용할 수 있는가? |
| 사업·제품 | D02·D03 | 어떤 Product/Service의 고객가치와 매출·원가를 바꾸는가? |
| 기술·R&D·IP | D04·D05 | Build해야 할 Core와 License/Co-develop할 외부역량은 무엇인가? |
| 공정·설비·공장 | D06·D07 | 어느 Line·Site·Data·Safety Layer에서 검증할 것인가? |
| 공급망·고객·시장 | D08~D10 | Supplier/OEM/ESS Partner와 어떤 Data·Network Effect가 필요한가? |
| 원가·CAPEX·현금 | D11·D12 | KRW/kWh·Cash·Ramp·EAC에 검증 가능한 변화가 있는가? |
| 계약·거버넌스 | D13 | Data·IP·배타성·성과지급·Exit·Escrow를 어떻게 정할 것인가? |
| 규제 | D14 | DPP·PFE·UFLPA·Audit Evidence를 충족하면서 Human approval을 유지하는가? |
| Risk·품질·안전 | D15 | False Negative·Control bypass·Vendor failure·OT Risk를 어떻게 제한하는가? |

### 2. D17 전달 규칙

```yaml
d17_handoff_rule:
  mandatory_fields:
    - oi_seed_id_and_verified_internal_pain_point
    - capability_definition_and_non_negotiable_control
    - provider_solution_legal_entity_and_version
    - evidence_level_named_reference_claim_owner_and_date
    - existing_SK_On_or_affiliate_relationship_and_exact_scope
    - build_buy_partner_license_invest_observe_posture
    - fit_gap_conflict_vendor_health_and_lock_in_risk
    - site_line_product_customer_supplier_and_period_scope
    - data_access_IP_training_retention_export_and_deletion_rights
    - baseline_control_group_primary_KPI_guardrail_and_counterfactual
    - G0_to_G8_gate_stop_scale_exit_and_PIR
    - TCO_internal_hours_KRW_kWh_cash_risk_and_safety_value
    - source_ids_and_human_approvers
  gates:
    - never_equate_product_MOU_pilot_operation_and_scale
    - never_copy_vendor_or_competitor_reported_ROI_to_SK_On
    - never_treat_affiliate_relationship_as_SK_On_contractual_right
    - require_battery_or_industrial_reference_or_stricter_shadow_mode
    - require_data_IP_cyber_legal_and_export_controls_before_PoC
    - require_portable_data_model_API_and_reversible_exit
    - prohibit_autonomous_safety_quality_release_recall_tax_customs_legal_or_OT_control
    - require_independent_outcome_validation_and_post_implementation_review
```

### 3. D17 우선 전달 레코드

```yaml
d16_priority_handoff:
  - oi_seed_id: OI-D16-01
    title: Capability–Pain Point–Provider Knowledge Graph
    problem_proxy: domain_seeds_provider_evidence_relationship_and_risk_are_fragmented
    owner: open_innovation_strategy_data_architecture_domain_owners
    partner_type: knowledge_graph_research_intelligence_workflow
    poc_duration: 4_to_6_months
    success_kpi: every_priority_seed_has_capability_evidence_risk_and_PoC_path
    source_ids: [SRC-D16-001, SRC-D16-004, SRC-D16-007, SRC-D16-016]

  - oi_seed_id: OI-D16-02
    title: External Evidence and Reference Validation Agent
    problem_proxy: product_MOU_pilot_operation_and_scale_claims_are_mixed
    owner: open_innovation_procurement_legal_finance_domain_experts
    partner_type: evidence_AI_vendor_intelligence_audit_workflow
    poc_duration: 3_to_4_months
    success_kpi: zero_known_stage_misclassification_and_reproducible_claim_lineage
    source_ids: [SRC-D16-002, SRC-D16-003, SRC-D16-011, SRC-D16-018]

  - oi_seed_id: OI-D16-04
    title: Multi-Vendor Battery Data Sandbox
    problem_proxy: vendors_are_tested_on_different_data_KPI_and_security_conditions
    owner: IT_data_quality_RnD_manufacturing_cyber_legal
    partner_type: confidential_computing_data_clean_room_MLOps
    poc_duration: 6_to_9_months
    success_kpi: comparable_results_with_zero_unapproved_training_or_residual_data
    source_ids: [SRC-D16-009, SRC-D16-010, SRC-D16-012, SRC-D16-014]

  - oi_seed_id: OI-D16-03
    title: PoC-to-Scale Stage-Gate Orchestrator
    problem_proxy: pilots_lack_baseline_stop_scale_TCO_and_post_review
    owner: open_innovation_strategy_finance_procurement_domain_owner
    partner_type: decision_intelligence_process_mining_portfolio_workflow
    poc_duration: 4_to_6_months
    success_kpi: all_pilots_have_G0_to_G8_decision_trace_and_validated_value
    source_ids: [SRC-D16-007, SRC-D16-008, SRC-D16-024, SRC-D16-026]

  - oi_seed_id: OI-D16-09
    title: Battery Passport Interoperability Bake-off
    problem_proxy: provider_claims_are_not_tested_against_one_mandatory_data_and_API_pack
    owner: EU_compliance_sustainability_supply_chain_IT_customer_program
    partner_type: DPP_traceability_data_space_assurance
    poc_duration: 6_to_9_months
    success_kpi: mandatory_fields_unique_ID_access_version_API_and_evidence_export_pass
    source_ids: [SRC-D16-016, SRC-D16-017, SRC-D16-018, SRC-D16-019]
```

D16이 D17에 넘기는 핵심은 `유명한 AI·스타트업을 추천하자`가 아니다. **검증된 SK온 문제를 기준으로 필요한 외부 Capability를 정의하고, 관계·증거·권리·Risk·경제성·PoC 종료조건까지 연결해 실제로 Build·Buy·Partner·Stop 결정을 내릴 수 있게 만드는 것**이 과제다.

---
