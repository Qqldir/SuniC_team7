---
id: skes-d05-8-patent-research-protocol
title: Patent Research Protocol
summary: "도시가스, 수소, 충방전 등 SK E&S 사업별 특허를 체계적으로 검색·수집하기 위한 6단계 프로토콜과 15가지 검색 쿼리 라이브러리, 특허 기록 표준 스키마."
tags: [d05, rnd, schema, table]
keywords: [특허검색, 검색프로토콜, 도시가스, 수소, 탄소포집, 특허정보, 선행기술, Patent Research, 법적지위, 쿼리라이브러리]
related: []
priority: normal
domain: D05
section: 8
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 899
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 8. Patent Research Protocol

## 8.1 검색 순서

```yaml
protocol:
  step_1_entity_search:
    - canonical_assignee
    - Korean_name
    - English_variants
    - former_name
    - affiliate_name
  step_2_technology_search:
    - title_abstract_claim_keywords
    - IPC_CPC
    - inventor_cluster
    - cited_and_citing_patents
  step_3_family_normalization:
    - priority_application
    - PCT_and_national_phase
    - continuation_divisional
    - grant_and_application_versions
  step_4_legal_status:
    - official_register
    - fee_and_expiration
    - assignment_and_security_interest
    - opposition_or_litigation
  step_5_mapping:
    - D03_product
    - D04_technology
    - R&D_program
    - inventor_and_partner
  step_6_internal_gate:
    - invention_disclosure
    - confidential_contract
    - source_code_or_BOM
    - legal_counsel
```

## 8.2 Search Query Library

| Query ID | 목적 | 검색식 예시 |
|---|---|---|
| `Q-ENS-001` | 직접 출원 | `assignee:("SK E&S" OR "에스케이이엔에스")` |
| `Q-ENS-002` | 합병 후 | `assignee:("SK Innovation") AND (carbon capture OR city gas OR hydrogen)` |
| `Q-ENS-003` | 도시가스 관계사 | `assignee:("부산도시가스" OR "충청에너지서비스" OR "코원에너지서비스")` |
| `Q-ENS-004` | 정압·계량 | `(gas regulator OR pressure corrector OR volume corrector OR meter) AND assignee_group` |
| `Q-ENS-005` | 배관안전 | `(gas pipeline AND repair) OR leakage OR cathodic protection` |
| `Q-ENS-006` | CO₂ 포집 | `(carbon dioxide AND absorbent AND capture) AND assignee_group` |
| `Q-ENS-007` | 흡수제 운전 | `(solvent AND solidification) OR (waste heat AND absorbent)` |
| `Q-ENS-008` | EverCharge | `assignee:(EverCharge OR GreenIT) AND (EVSE OR charging OR load)` |
| `Q-ENS-009` | SmartPower | `("smart load management" OR "smart energy distribution") AND EverCharge` |
| `Q-ENS-010` | KCE | `assignee:("Key Capture Energy") OR inventor_cluster AND storage bidding` |
| `Q-ENS-011` | 수소 JV | `assignee:("SK Plug HyVerse") OR applicant and PEM electrolyzer` |
| `Q-ENS-012` | 액화수소 | `(liquid hydrogen OR cryogenic hydrogen) AND (SK OR affiliate)` |
| `Q-ENS-013` | PPA·DERMS | `(PPA settlement OR DERMS OR VPP) AND E&S_entity_group` |
| `Q-ENS-014` | 인수 전 IP | `assignee:EverCharge priority:<acquisition_date` |
| `Q-ENS-015` | 개량발명 | `inventor_cluster AND partner_assignee AND post_collaboration_date` |

## 8.3 Patent Record Schema

```yaml
patent_family:
  family_id: PF-ENS-DOMAIN-NNN
  title: string
  earliest_priority: YYYY-MM-DD
  priority_application: string
  representative_publication: string
  jurisdictions: []
  applicant_at_filing: []
  current_assignee_reported: []
  inventors: []
  legal_status_reported: string
  status_checked_at: date
  status_source: aggregator_or_register
  ownership_class: code
  acquisition_timeline: string
  technical_problem: string
  solution_elements: []
  linked_products: []
  linked_technologies: []
  claim_scope_summary: preliminary_nonlegal
  implementation_evidence: none_public_partial_confirmed
  FTO_use: landscape_only
  source_ids: []
```

---
