---
id: skon-d16-d16-05-provider-fit-due-diligence-scorecard
title: Provider Fit & Due-Diligence Scorecard
summary: 외부 공급사의 적합성을 8개 평가축으로 점수화하고 의사결정하는 스코어카드와 벤더 실사 체크리스트.
tags: [d16, ecosystem, schema, table]
keywords: [벤더 평가, 공급사 실사, 기술 성능, 데이터 제어, 통합 가능성, hard gate, TCO, 공급망 리스크, 실사 체크리스트, POC, 벤더평가, 실사체크리스트, 스코어카드, 의사결정기준, 기술성능검증, 상업적적합성, Hard Gate, 벤더건강성, 공급망리스크]
related: []
priority: normal
domain: D16
section: D16-05
source: SK온_D16_External_Solutions_Startups_Vendors_Open_Innovation_Ecosystem.md
breadcrumb: "SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem"
tokens: 850
updated: 2026-08-03
---

> SK온 · D16 외부 솔루션·스타트업·벤더 생태계 · SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem

## D16-05 Provider Fit & Due-Diligence Scorecard

### 1. 100점 평가표

| 평가축 | 점수 | 핵심 질문 | Hard Gate |
|---|---:|---|---|
| Problem–Capability Fit | 15 | 특정 Pain Point와 KPI를 직접 바꾸는가? | Baseline·Owner 없음이면 중단 |
| Battery/Industrial Evidence | 15 | 명명된 Cell·Factory·ESS·OEM Reference가 있는가? | 홍보자료만이면 생산제어 금지 |
| Technical Performance | 15 | Accuracy·Latency·Throughput·False Alarm이 검증되는가? | Safety/Quality 허용범위 초과 시 중단 |
| Integration & Interoperability | 10 | MES·QMS·ERP·PLM·BMS·OT와 표준 Interface가 있는가? | Data export·rollback 불가 시 No-Go |
| Data·IP·Cyber | 15 | 학습·재사용·소유·보관·Access가 통제되는가? | 핵심 Recipe/Clause 재사용권 요구 시 No-Go |
| Vendor & Delivery Resilience | 10 | 재무·인력·Support·Escrow·Subprocessor가 지속 가능한가? | 핵심지원·소스/모델 복구계획 없음이면 제한 |
| Commercial & Economic Fit | 10 | License·Hardware·Integration·Change 비용을 포함한 TCO가 타당한가? | KPI와 지급조건 분리 시 재협상 |
| Scale & Change Adoption | 10 | 한 Line에서 다공장으로 표준화·교육·운영 가능한가? | Site Owner·운영인력 없으면 Pilot만 |

```yaml
decision_thresholds:
  80_to_100: D17_PRIORITY_POC_CANDIDATE
  65_to_79: CONDITIONAL_POC_AFTER_GAP_CLOSURE
  50_to_64: OBSERVE_OR_TECHNICAL_DILIGENCE_ONLY
  below_50: NO_GO_FOR_CURRENT_CYCLE

hard_gate_override:
  - safety_or_quality_control_bypass
  - unbounded_data_or_model_reuse
  - unresolved_sanctions_PFE_export_control_or_conflict
  - no_reversible_exit_or_data_export
  - no_accountable_internal_owner
```

### 2. Vendor Health 최소 Due Diligence

```yaml
vendor_health_pack:
  corporate:
    - legal_entity_and_ultimate_owner
    - sanctions_PFE_export_control_and_conflict
    - litigation_IP_claim_and_insurance
  financial:
    - audited_or_board_approved_financial_pack
    - cash_runway_revenue_concentration_and_financing_dependency
    - support_and_warranty_reserve
  delivery:
    - named_team_location_language_and_response_SLA
    - implementation_partner_and_subprocessor
    - battery_reference_contact_and_failure_lessons
  technology:
    - architecture_API_export_model_version_and_rollback
    - cybersecurity_SBOM_vulnerability_and_pen_test
    - accuracy_throughput_latency_and_drift_test
  continuity:
    - source_code_or_model_escrow_where_needed
    - data_export_and_transition_assistance
    - acquisition_insolvency_and_product_EoL_clause
```

공개자료만으로 위 항목 대부분은 확인되지 않는다. 따라서 D16의 Provider Master는 **Longlist**이며, 점수는 내부자료와 공급사 실사 없이는 최종 확정하지 않는다.

---
