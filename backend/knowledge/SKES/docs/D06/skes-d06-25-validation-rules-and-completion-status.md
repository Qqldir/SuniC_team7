---
id: skes-d06-25-validation-rules-and-completion-status
title: Validation Rules and Completion Status
summary: "E&S 운영 프로세스의 자동화 검증 규칙 10가지와 LNG·발전·도시가스·신재생·ESS·EV·수소·CCS 등 9개 분야별 공개 데이터 완성도 평가 표, 그리고 시스템의 8가지 알려진 제한사항을 정리한 현황 문서."
tags: [d06, process, schema, table, "xref:d17"]
keywords: [검증 규칙, 데이터 완성도, 자동화 검사, LNG, ESS, CCS, SCADA, 시스템 제한사항, 공개 데이터, KPI 정의]
related: []
priority: normal
domain: D06
section: 25
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 500
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 25. Validation Rules and Completion Status

## 25.1 Automated Structure Checks

```yaml
checks:
  unique_process_id: required
  unique_equipment_class_id: required
  unique_failure_mode_id: required
  unique_seed_id: required
  source_id_resolves: required
  planned_vs_operating_status: required
  company_fact_vs_industry_baseline: required
  KPI_definition_and_boundary: required
  safety_critical_seed_has_guardrail: required
  internal_data_request_for_P0: required
```

## 25.2 Public-Data Completeness

| Area | Process depth | E&S direct evidence | Internal Gap | D17 usability |
|---|---:|---:|---:|---:|
| LNG portfolio/cargo | High | Medium-high | contract·schedule | High after internal check |
| LNG terminal | High | Medium | actual equipment/tag | High |
| Power/CHP | High | Medium | unit performance/OEM | High |
| City gas | High | High for portfolio/RBMS | GIS·failure history | Very high |
| Renewable/PPA | High | High for business | plant SCADA/contract | Very high |
| ESS/KCE | High | Medium-high | model/BMS/warranty | Very high |
| EV/EverCharge | High | Medium-high | session/site/internal IP | High |
| Liquid hydrogen | High | Medium | process/vendor/performance | Very high |
| CCS | High baseline | Medium for plan/pilot | design/MRV/contract | Medium, stage-gated |

## 25.3 Known Limitations

```yaml
limitations:
  - no_internal_process_flow_diagram_or_P_and_ID
  - no_live_tag_dictionary
  - no_actual_equipment_vendor_and_configuration_except_public_partner_context
  - no_actual_efficiency_yield_BOR_failure_rate_or_OEE
  - no_contract_or_market_rule_legal_interpretation
  - no_complete_asset_and_capacity_master_deferred_to_D07
  - no_cyber_architecture_or_safety_cause_and_effect
  - CCS_blue_hydrogen_and_VPP_not_treated_as_full_commercial_operation
```

---
