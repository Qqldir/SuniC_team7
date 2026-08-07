---
id: skes-d05-20-data-quality-and-validation-rules
title: Data Quality and Validation Rules
summary: 지식재산 데이터 수집·처리 시 준수할 검증 규칙 9가지와 각 데이터셋의 완성도 현황을 정의한 문서.
tags: [d05, rnd, core-candidate, schema]
keywords: [검증 규칙, 특허 데이터, 지식재산, 데이터 완성도, 정규화, FTO, 인벤터 네트워크, 포트폴리오, 법적 상태, 데이터 거버넌스]
related: []
priority: critical
domain: D05
section: 20
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 399
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 20. Data Quality and Validation Rules

## 20.1 Hard Rules

```yaml
hard_rules:
  - never_count_publications_as_inventions_without_family_normalization
  - never_merge_parent_affiliate_and_JV_IP_without_ownership_class
  - never_infer_product_implementation_from_patent_title_or_assignee
  - never_infer_license_right_from_investment_or_partnership
  - never_infer_current_employment_from_inventor_record
  - never_treat_PCT_ceased_as_all_country_rights_ceased
  - never_issue_final_FTO_without_counsel_and_claim_chart
  - always_preserve_priority_date_and_acquisition_timeline
  - always_refresh_legal_status_for_decision_use
```

## 20.2 Completeness Status

```yaml
completion:
  domain_boundary: COMPLETE
  source_registry: COMPLETE_V1
  entity_normalization: COMPLETE_V1
  R&D_operating_model: COMPLETE_V1
  organization_master: COMPLETE_PUBLIC_DATA
  program_taxonomy: COMPLETE_V1
  program_master: COMPLETE_V1
  patent_protocol: COMPLETE_V1
  patent_taxonomy: COMPLETE_V1
  initial_family_master: COMPLETE_TARGETED_SAMPLE
  inventor_network: COMPLETE_FOR_SAMPLED_FAMILIES
  partner_rights_matrix: COMPLETE_V1
  technology_IP_product_crosswalk: COMPLETE_V1
  software_data_trade_secret_register: COMPLETE_V1
  preliminary_risk_and_FTO_scope: COMPLETE_V1
  white_space_and_OI_seeds: COMPLETE_V1
  AI_chunk_library: COMPLETE_V1
  complete_global_portfolio: NOT_CLAIMED
  official_register_refresh: REQUIRED_AT_DECISION_DATE
```

---
