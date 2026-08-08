---
id: skon-d07-d07-34-plant-customer-policy-relationship-graph
title: Plant–Customer–Policy Relationship Graph
summary: "SK온의 배터리 생산시설이 고객, 규제 정책과 맺는 소유권, 공급, 용량 관계를 지식 그래프로 표현한 스키마."
tags: [d07, footprint, schema]
keywords: [발전소, 생산거점, 용량, 고객, 정책, 소유권, SKON, 생산, 관계 데이터, 배터리 공장, 소유권 관계, 생산 용량, 고객 공급, 정책 준수, 지식 그래프, predicate, triple, 규제 요건]
related: []
priority: normal
domain: D07
section: D07-34.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1986
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-34. Plant–Customer–Policy Relationship Graph

## 34.1 Canonical Predicate Vocabulary

```yaml
d07_predicates:

  ownership:
    - OWNS
    - CONTROLS
    - PARTICIPATES_IN
    - TRANSFERRED_TO
    - DISPOSAL_PENDING
    - ACQUISITION_PENDING

  location:
    - LOCATED_IN
    - CONTAINS_PLANT
    - NEAR_CUSTOMER_SITE

  capacity:
    - HAS_DESIGN_CAPACITY
    - HAS_REPORTED_CAPACITY
    - HAS_JV_GROSS_CAPACITY
    - INCLUDED_IN_CONSOLIDATED_CAPACITY
    - EXCLUDED_FROM_CONSOLIDATED_CAPACITY

  production:
    - PRODUCES
    - STARTED_COMMERCIAL_PRODUCTION
    - PREPARING_FOR_PRODUCTION
    - SUPPLIES
    - HISTORICALLY_SUPPLIED

  qualification:
    - QUALIFIED_FOR_CUSTOMER
    - REQUIRES_QUALIFICATION
    - TECHNICALLY_COMPATIBLE_WITH

  policy:
    - MAY_QUALIFY_FOR
    - SUBJECT_TO
    - REQUIRES_ORIGIN_DATA
    - RECEIVES_INCENTIVE_IF_COMPLIANT

  analysis:
    - CONTRIBUTES_TO_PRO_FORMA
    - HAS_PAIN_POINT
    - GENERATES_OI_SEED
```

---

## 34.2 Core Relationship Triples

```yaml
relationship_triples:

  - edge_id: EDGE-D07-001
    subject: CO-SKON
    predicate: CONTROLS
    object: PLANT-D07-KR-SEO
    source_ids: [SRC-REG-D07-001]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-002
    subject: CO-SKON
    predicate: CONTROLS
    object: PLANT-D07-HU-KOM1
    source_ids: [SRC-REG-D07-001]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-003
    subject: CO-SKON
    predicate: CONTROLS
    object: PLANT-D07-HU-KOM2
    source_ids: [SRC-REG-D07-001]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-004
    subject: CO-SKON
    predicate: CONTROLS
    object: PLANT-D07-HU-IVA
    source_ids: [SRC-REG-D07-001]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-005
    subject: CO-SKON
    predicate: CONTROLS
    object: PLANT-D07-US-GA1
    source_ids: [SRC-REG-D07-001]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-006
    subject: CO-SKON
    predicate: CONTROLS
    object: PLANT-D07-US-GA2
    source_ids: [SRC-REG-D07-001]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-007
    subject: SITE-D07-US-COMMERCE
    predicate: CONTAINS_PLANT
    object: PLANT-D07-US-GA1
    source_ids: [SRC-GOV-D07-008]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-008
    subject: SITE-D07-US-COMMERCE
    predicate: CONTAINS_PLANT
    object: PLANT-D07-US-GA2
    source_ids: [SRC-GOV-D07-008]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-009
    subject: SITE-D07-US-COMMERCE
    predicate: HISTORICALLY_SUPPLIED
    object: MODEL-FORD-F150-LIGHTNING
    source_ids: [SRC-GOV-D07-008]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-010
    subject: SITE-D07-US-COMMERCE
    predicate: HISTORICALLY_SUPPLIED
    object: MODEL-VW-ID4
    source_ids: [SRC-GOV-D07-008]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-011
    subject: CO-SKON
    predicate: PARTICIPATES_IN
    object: PLANT-D07-US-HSBMA
    source_ids: [SRC-OFF-D07-005]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-012
    subject: CUST-HYUNDAI-MOTOR-GROUP
    predicate: PARTICIPATES_IN
    object: PLANT-D07-US-HSBMA
    source_ids: [SRC-OFF-D07-005]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-013
    subject: PLANT-D07-US-HSBMA
    predicate: HAS_JV_GROSS_CAPACITY
    object: CAPACITY-35-GWH
    source_ids: [SRC-OFF-D07-005]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-014
    subject: PLANT-D07-US-HSBMA
    predicate: STARTED_COMMERCIAL_PRODUCTION
    object: DATE-2026-06-01
    source_ids: [SRC-OFF-D07-005]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-015
    subject: PLANT-D07-US-HSBMA
    predicate: SUPPLIES
    object: MODEL-HYUNDAI-IONIQ9
    source_ids: [SRC-OFF-D07-005]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-016
    subject: PLANT-D07-US-TN
    predicate: PREPARING_FOR_PRODUCTION
    object: DATE-2028
    source_ids: [SRC-OFF-D07-004]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-017
    subject: PLANT-D07-US-TN
    predicate: HAS_DESIGN_CAPACITY
    object: CAPACITY-45-GWH-LEGACY
    source_ids: [SRC-REG-D07-019]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-018
    subject: PLANT-D07-US-KY1
    predicate: TRANSFERRED_TO
    object: CO-FORD
    source_ids: [SRC-REG-D07-003]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-019
    subject: PLANT-D07-US-KY2
    predicate: TRANSFERRED_TO
    object: CO-FORD
    source_ids: [SRC-REG-D07-003]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-020
    subject: PLANT-D07-CN-CHA-JV
    predicate: EXCLUDED_FROM_CONSOLIDATED_CAPACITY
    object: CO-SKON
    source_ids: [SRC-REG-D07-001]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-021
    subject: PLANT-D07-CN-HUI-JV
    predicate: EXCLUDED_FROM_CONSOLIDATED_CAPACITY
    object: CO-SKON
    source_ids: [SRC-REG-D07-001]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-022
    subject: CO-SKON
    predicate: DISPOSAL_PENDING
    object: PLANT-D07-CN-HUI-JV
    source_ids: [SRC-REG-D07-006]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-023
    subject: CO-SKON
    predicate: ACQUISITION_PENDING
    object: SK_ON_JIANGSU_REMAINING_30_PERCENT
    source_ids: [SRC-REG-D07-006]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-024
    subject: CO-SKON
    predicate: HAS_REPORTED_CAPACITY
    object: CAPACITY-97_4-GWH-Q1-2026
    source_ids: [SRC-REG-D07-001]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-025
    subject: CAPACITY-94_3-GWH-PRO_FORMA
    predicate: DERIVED_FROM
    object: CAPACITY-97_4-GWH-Q1-2026
    basis_source_ids:
      - SRC-REG-D07-001
      - SRC-REG-D07-003
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D07-026
    subject: CUST-NISSAN
    predicate: HAS_SUPPLY_AGREEMENT
    object: CO-SKON
    source_ids: [SRC-OFF-D07-017]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-027
    subject: CUST-NISSAN
    predicate: REQUIRES_US_PRODUCTION
    object: SUPPLY-NEARLY-100-GWH-2028-2033
    source_ids: [SRC-OFF-D07-017]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-028
    subject: CUST-SLATE
    predicate: HAS_SUPPLY_AGREEMENT
    object: CO-SKON
    source_ids: [SRC-OFF-D07-018]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-029
    subject: CUST-SLATE
    predicate: REQUIRES_US_PRODUCTION
    object: SUPPLY-APPROX-20-GWH-2026-2031
    source_ids: [SRC-OFF-D07-018]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D07-030
    subject: REGION-D07-USA
    predicate: SUBJECT_TO
    object: POLICY-PFE-MATERIAL-ASSISTANCE
    source_ids: [SRC-REG-D07-012]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-031
    subject: REGION-D07-USA
    predicate: REQUIRES_ORIGIN_DATA
    object: POLICY-CLEAN-VEHICLE-BATTERY-LEDGER
    source_ids: [SRC-REG-D07-014]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D07-032
    subject: PP-D07-002
    predicate: GENERATES_OI_SEED
    object: OI-SEED-D07-007
    basis_source_ids:
      - SRC-REG-D07-001
    evidence_level: ANALYST_INFERENCE
```

---
