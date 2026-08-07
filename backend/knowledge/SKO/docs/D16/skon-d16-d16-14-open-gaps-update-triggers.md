---
id: skon-d16-d16-14-open-gaps-update-triggers
title: Open Gaps & Update Triggers
summary: "외부 솔루션·벤더 협력에서 기술·재무·규제 검증이 필요한 10개 갭 항목과 D17 영향도, 모니터링 트리거를 정의한 표"
tags: [d16, ecosystem, schema, table, "xref:d17", "xref:d14"]
keywords: [공급자검증, 미확인항목, 벤더평가, 외부생태계리스크, DPP, ESS, PoC평가, TCO분석, 재무건정성, 데이터공유범위, 공급사 검증, Siemens, 기술 갭, 벤더 위험, 규제 기준, PoC, 폐배터리, 협력사]
related: [GAP-D16-01, GAP-D16-02, GAP-D16-03, GAP-D16-04, GAP-D16-05, GAP-D16-06, GAP-D16-07, GAP-D16-08, GAP-D16-09, GAP-D16-10]
priority: normal
domain: D16
section: D16-14
source: SK온_D16_External_Solutions_Startups_Vendors_Open_Innovation_Ecosystem.md
breadcrumb: "SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem"
tokens: 764
updated: 2026-08-03
---

> SK온 · D16 외부 솔루션·스타트업·벤더 생태계 · SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem

## D16-14 Open Gaps & Update Triggers

| Gap ID | 미확인 항목 | 필요한 내부/외부 자료 | D17 영향 |
|---|---|---|---|
| `GAP-D16-01` | 기존 Siemens·설비지능화 협력의 실제 배포·성과 | 계약·PoC Report·Site Architecture | 신규 Scout 중복 방지 |
| `GAP-D16-02` | Provider별 가격·Integration·Support TCO | RFI/RFP·Reference Call | Business Case |
| `GAP-D16-03` | Startup 재무·인력·제품 EoL 위험 | NDA Financial Pack·Customer Churn·Runway | Vendor Continuity |
| `GAP-D16-04` | Recipe·Cell Data·BMS·Contract의 외부 제공 가능범위 | Data Classification·고객/JV 계약 | Sandbox 범위 |
| `GAP-D16-05` | DPP Provider의 D14 Mandatory Field·API 실증 | Common Test Pack·Supplier Data | 2027 Market Access |
| `GAP-D16-06` | Inspection Provider의 Pouch/Prismatic Line-speed 성능 | Golden Cell·Defect Library·Cycle Test | Quality PoC |
| `GAP-D16-07` | Field/ESS Analytics의 OEM·Warranty·보험 권리 | Data-sharing·Liability·Action Protocol | Safety/Business Model |
| `GAP-D16-08` | Recycling Partner의 실제 Yield·Spec·원가·물류·Permit | Sample Qualification·Mass Balance·TEA | Closed-loop Economics |
| `GAP-D16-09` | 경쟁사 관계·배타성·Conflict | Contractual Conflict Disclosure | Partner Selection |
| `GAP-D16-10` | 실패·중단된 과거 PoC | 내부 O/I Archive·Interview | No-Go Memory |

```yaml
update_triggers:
  - new_SK_On_partnership_license_JV_investment_or_termination
  - provider_acquisition_insolvency_major_funding_or_product_EoL
  - named_battery_factory_ESS_OEM_deployment_or_recall
  - EU_DPP_delegated_act_Catena_X_interoperability_or_audit_rule
  - PFE_MACR_UFLPA_tariff_or_export_control_change
  - material_change_in_vendor_security_incident_or_certification
  - PoC_gate_decision_scale_stop_or_post_implementation_result
```

---

## D16-15 Completion Check

```yaml
completion:
  domain_boundary: COMPLETE
  external_capability_data_model: COMPLETE
  existing_SK_On_ecosystem_register: 10_relationships
  cross_domain_capability_map: 12_capabilities
  external_provider_master: 24_providers
  provider_families: 5
  pain_point_register: 14
  external_case_patterns: 8
  OI_candidate_portfolio: 15
  priority_handoff_records: 5
  source_registry: 29_official_sources
  machine_export_schema: COMPLETE
  unknown_internal_metrics: NOT_ESTIMATED
  purchase_investment_partnership_approval: NOT_GRANTED_BY_THIS_DOCUMENT

next_domain:
  domain_id: D17
  canonical_name: Open-Innovation Opportunity Portfolio and AI Task Recommendation
```

**다음 작업 지점:** `D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation`
