---
id: skon-d06-d06-59-process-defect-kpi-relationship-graph
title: Process·Defect·KPI Relationship Graph
summary: "SK온 제조공정에서 프로세스 단계, 불량, KPI 간의 인과관계를 정의하는 간선 어휘와 관계 트리플 집합을 제공한다."
tags: [d06, process, schema, "xref:d05", "xref:d04"]
keywords: [공정 흐름도, 결함 추적, FEEDS, FOLLOWED_BY, 품질 영향, 메타데이터, 증거 수준, CQA, 공정 맵핑, 운영 제약, 공정흐름, 간선어휘, 불량탐지, KPI영향, genealogy, relationship triples, 품질제어, 제조계보, 운영최적화]
related: []
priority: normal
domain: D06
section: D06-59.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 2439
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-59. Process·Defect·KPI Relationship Graph

## 59.1 Canonical Edge Vocabulary

```yaml
d06_edge_vocabulary:

  process_flow:
    - FEEDS
    - FOLLOWED_BY
    - PRODUCES
    - CONSUMES
    - INSPECTED_BY

  genealogy:
    - DERIVED_FROM
    - CONTAINS
    - INSTALLED_IN
    - PROCESSED_BY

  quality:
    - MAY_GENERATE
    - MAY_CONTRIBUTE_TO
    - DETECTS
    - ESCAPED_FROM
    - AFFECTS_CQA

  operations:
    - IMPACTS_KPI
    - CREATES_WIP
    - CONSTRAINS_THROUGHPUT
    - CONSUMES_ENERGY

  digital:
    - GENERATES_EVENT
    - STORED_IN
    - SIMULATED_BY
    - MONITORED_BY
    - OPTIMIZED_BY

  improvement:
    - HAS_PAIN_POINT
    - GENERATES_OI_SEED
    - REQUIRES_GOVERNANCE
```

---

## 59.2 Core Relationship Triples

```yaml
relationship_triples:

  - edge_id: EDGE-D06-FINAL-001
    subject: PROC-SKON-D06-003
    predicate: FEEDS
    object: PROC-SKON-D06-004
    source_ids: [SRC-BASE-D06-006]
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-FINAL-002
    subject: PROC-SKON-D06-004
    predicate: FEEDS
    object: PROC-SKON-D06-006
    source_ids: [SRC-BASE-D06-006, SRC-BASE-D06-007]
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-FINAL-003
    subject: PROC-SKON-D06-005
    predicate: FEEDS
    object: PROC-SKON-D06-008
    source_ids: [SRC-SKON-D06-001]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-004
    subject: PROC-SKON-D06-006
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-007
    source_ids: [SRC-BASE-D06-006]
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-FINAL-005
    subject: PROC-SKON-D06-007
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-008
    source_ids: [SRC-BASE-D06-006]
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-FINAL-006
    subject: PROC-SKON-D06-008
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-009
    source_ids: [SRC-BASE-D06-006]
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-FINAL-007
    subject: PROC-SKON-D06-009
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-010
    source_ids: [SRC-BASE-D06-006]
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-FINAL-008
    subject: PROC-SKON-D06-010
    predicate: FEEDS
    object: PROC-SKON-D06-011
    source_ids: [SRC-SKON-D06-011, SRC-BASE-D06-012]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-009
    subject: PROC-SKON-D06-011
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-012
    source_ids: [SRC-BASE-D06-012]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-010
    subject: PROC-SKON-D06-012
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-013
    source_ids: [SRC-BASE-D06-012, SRC-BASE-D06-015]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-011
    subject: PROC-SKON-D06-013
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-014
    source_ids: [SRC-BASE-D06-012, SRC-BASE-D06-014]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-012
    subject: PROC-SKON-D06-014
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-014A
    source_ids: [SRC-BASE-D06-014]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-013
    subject: PROC-SKON-D06-014A
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-015
    source_ids: [SRC-BASE-D06-016]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-014
    subject: PROC-SKON-D06-015
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-016
    source_ids: [SRC-BASE-D06-016]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-015
    subject: PROC-SKON-D06-016
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-017
    source_ids: [SRC-BASE-D06-016, SRC-BASE-D06-017]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-016
    subject: PROC-SKON-D06-017
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-018
    source_ids: [SRC-BASE-D06-017]
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-FINAL-017
    subject: PROC-SKON-D06-018
    predicate: FEEDS
    object: PROC-SKON-D06-019A
    source_ids: [SRC-SKON-D06-024]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-018
    subject: PROC-SKON-D06-018
    predicate: FEEDS
    object: PROC-SKON-D06-020A
    source_ids: [SRC-SKON-D06-024]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-019
    subject: PROC-SKON-D06-019A
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-019B
    source_ids: [SRC-PAT-D06-029]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-020
    subject: PROC-SKON-D06-019B
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-019C
    source_ids: [SRC-PAT-D06-028, SRC-PAT-D06-029]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-021
    subject: PROC-SKON-D06-019C
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-019D
    source_ids: [SRC-PAT-D06-028, SRC-PAT-D06-030]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-022
    subject: PROC-SKON-D06-020A
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-020B
    source_ids: [SRC-PAT-D06-027]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-023
    subject: PROC-SKON-D06-020B
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-020C
    source_ids: [SRC-PAT-D06-027, SRC-PAT-D06-028]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-024
    subject: PROC-SKON-D06-020C
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-020D
    source_ids: [SRC-PAT-D06-027, SRC-PAT-D06-030]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-025
    subject: PROC-SKON-D06-021A
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-021B
    source_ids: [SRC-PAT-D06-027, SRC-PAT-D06-028]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-026
    subject: PROC-SKON-D06-021B
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-021C
    source_ids: [SRC-PAT-D06-028, SRC-PAT-D06-030]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-027
    subject: PROC-SKON-D06-021C
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-021D
    source_ids: [SRC-PAT-D06-030]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-028
    subject: PROC-SKON-D06-008
    predicate: MAY_CONTRIBUTE_TO
    object: DEF-D06-004
    source_ids: [SRC-BASE-D06-013, SRC-BASE-D06-014]
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-FINAL-029
    subject: PROC-SKON-D06-011
    predicate: MAY_GENERATE
    object: DEF-D06-001
    source_ids: [SRC-SKON-D06-011, SRC-BASE-D06-012]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-030
    subject: PROC-SKON-D06-012
    predicate: MAY_GENERATE
    object: DEF-D06-002
    source_ids: [SRC-BASE-D06-015]
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-FINAL-031
    subject: PROC-SKON-D06-015
    predicate: DETECTS
    object: DEF-D06-006
    source_ids: [SRC-SKON-D06-018]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D06-FINAL-032
    subject: PROC-SKON-D06-017
    predicate: DETECTS
    object: DEF-D06-009
    source_ids: [SRC-BASE-D06-017]
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-FINAL-033
    subject: PROC-SKON-D06-018C
    predicate: DETECTS
    object: DEF-D06-011
    source_ids: [SRC-SKON-D06-022, PF-SKON-D05-030, PF-SKON-D05-031]
    evidence_level: DIRECT_REGULATORY

  - edge_id: EDGE-D06-FINAL-034
    subject: PROC-SKON-D06-019B
    predicate: MAY_GENERATE
    object: DEF-D06-013
    source_ids: [SRC-PAT-D06-029]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-035
    subject: PROC-SKON-D06-019D
    predicate: MAY_GENERATE
    object: DEF-D06-016
    source_ids: [SRC-SKON-D06-025, SRC-PAT-D06-030]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-036
    subject: PROC-SKON-D06-020B
    predicate: MAY_GENERATE
    object: DEF-D06-019
    source_ids: [SRC-PAT-D06-027]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-037
    subject: PROC-SKON-D06-021D
    predicate: DETECTS
    object: DEF-D06-020
    source_ids: [SRC-PAT-D06-028]
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-FINAL-038
    subject: PROC-SKON-D06-008
    predicate: OPTIMIZED_BY
    object: TECH-SKON-D04-039
    source_ids: [SRC-SKON-D06-001]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D06-FINAL-039
    subject: PROC-SKON-D06-022
    predicate: SIMULATES
    object: PROCESS_AND_FACTORY
    source_ids: [SRC-SKON-D06-031, SRC-SIEMENS-D06-032]
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D06-FINAL-040
    subject: PROC-SKON-D06-024
    predicate: GENERATES_OI_SEED
    object: OI-SEED-D06-038
    source_ids: [SRC-STD-D06-033]
    evidence_level: ANALYST_INFERENCE
```

---
