---
id: skon-d05-d05-64-authoritative-final-yaml-v2-0
title: Authoritative Final YAML v2.0
summary: "R&D·특허·지식재산 도메인의 공개자료 기반 인벤토리 규모(특허족, 논문, 연구자 등)와 완료상태, 사용 허용·금지 범위를 정의한 마스터 YAML."
tags: [d05, rnd, schema, "xref:d00", "xref:d01", "xref:d17"]
keywords: [FTO, 특허족, 기술지도, 경쟁사분석, 공개정보, 사용제한, 의사결정Gate, R&D포트폴리오, 특허 패밀리, R&D 프로그램, 지식재산, 완료상태, 인벤토리, 특허경관, 논문저자, 연구자네트워크, 도메인마스터]
related: []
priority: normal
domain: D05
section: D05-64.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 812
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-64. Authoritative Final YAML v2.0

> 아래 YAML은 앞의 `D05 Final YAML v1.8` 중 완료상태와 Gap 분류를 대체한다. v1.8의 기술·Family·논문·연구자 수량은 유지한다.

```yaml
domain:
  domain_id: D05
  canonical_name: R&D, Patents and Intellectual Property
  company_id: CO-SKON
  version: 2.0
  reference_date: 2026-08-03
  status: PUBLIC_EVIDENCE_DB_COMPLETE_INTERNAL_VALIDATION_REQUIRED

inventory:
  rnd_programs: 10
  patent_families_confirmed_or_provisional: 33
  candidate_patent_families: 4
  verified_peer_reviewed_papers: 7
  candidate_papers: 1
  sk_on_paper_authors: 11
  research_chunks: 20
  graph_query_templates: 20
  core_relationship_triples: 30
  ip_white_spaces: 9
  priority_fto_gate_cards: 5

completion:
  organization_facilities_programs: COMPLETE_V1
  patent_taxonomy: COMPLETE_V1
  patent_family_master: COMPLETE_PROVISIONAL
  independent_claim_pre_map: COMPLETE_V1
  product_patent_technical_map: COMPLETE_V1
  paper_and_researcher_network: COMPLETE_V1
  competitor_landscape: COMPLETE_SAMPLE_BASED
  fto_gate_design: COMPLETE_V1
  joint_ip_rights_register: COMPLETE_V1
  official_source_operating_register: COMPLETE_V1
  public_gap_routing: COMPLETE_V1
  d17_handoff_correction: COMPLETE_V1

recurring_controls:
  official_register_status:
    status: REFRESH_AT_DECISION_DATE
    stale_after_days: 30
  continuation_and_divisional_monitoring:
    status: QUARTERLY_AND_EVENT_DRIVEN
  competitor_landscape:
    status: EXPAND_ONLY_FOR_APPROVED_FTO_PROJECT

internal_gates:
  product_bom_and_process_recipe: REQUIRED_FOR_G2
  confidential_joint_ip_contract: REQUIRED_FOR_RIGHTS_GATE
  invention_and_trade_secret_register: REQUIRED_FOR_INTERNAL_COMPLETENESS
  legal_counsel_fto_opinion: REQUIRED_BEFORE_COMMERCIAL_COMMITMENT

permitted_use:
  - Technology and patent landscaping
  - R&D and inventor-network analysis
  - Preliminary claim-element screening
  - Open-innovation opportunity generation
  - FTO project scoping and evidence request
  - Joint-IP contract field design

prohibited_use:
  - Final FTO conclusion
  - Patent infringement or validity opinion
  - Definitive current ownership certification without status packet
  - Product implementation assertion without internal element map
  - Commercial license-right assertion without contract review

next_project_step:
  domain_id: D00
  action: BUILD_SOURCE_ENTITY_ID_CHANGELOG_MASTER_AND_RUN_CROSS_DOMAIN_AUDIT
```

---

# D05 v2.0 완료 상태

**공개자료 기반 D05는 완료됐다.** 남은 항목은 문서 작성 누락이 아니라 실제 제품·계약·권리상태에 대한 `의사결정 시점 검증 Gate`다.

다음 작업 지점은 `D00 통합 출처·Entity·ID·변경이력 관리체계`이며, 이후 D01~D17 전체 교차검수를 수행한다.
