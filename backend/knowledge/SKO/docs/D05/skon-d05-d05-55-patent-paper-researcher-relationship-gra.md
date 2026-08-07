---
id: skon-d05-d05-55-patent-paper-researcher-relationship-gra
title: Patent·Paper·Researcher Relationship Graph
summary: "특허, 기술, 조직, 시설, 연구 프로젝트 간의 관계를 표현하는 그래프 모델로, 5개 영역의 엣지 타입과 관계 정보의 구조 및 실제 데이터 예시를 제시한다."
tags: [d05, rnd, schema, "xref:d04"]
keywords: [지식 그래프, 온톨로지, 엣지 타입, 관계 트리플, 지적재산, FTO, 협력 관계, 메타데이터, 기술 노드, D05, 관계 스키마, EDGE_VOCABULARY, 기술 연계, 엔티티 관계, 지식그래프, 특허 맵핑, 거버넌스, 증거 수준, YAML 구조]
related: []
priority: normal
domain: D05
section: D05-55.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 2086
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-55. Patent·Paper·Researcher Relationship Graph

## 55.1 Canonical Edge Types

```yaml
d05_edge_vocabulary:

  organization:
    - OPERATES_FACILITY
    - HOSTS_PROGRAM
    - COLLABORATES_WITH

  research:
    - PROGRAM_RESEARCHES_TECHNOLOGY
    - PAPER_VALIDATES_TECHNOLOGY
    - PAPER_EXPLAINS_FAILURE_MODE
    - PAPER_AUTHORED_BY

  patent:
    - PATENT_SUPPORTS_TECHNOLOGY
    - PATENT_INVENTED_BY
    - ORIGINAL_APPLICANT
    - CURRENT_OWNER
    - TRANSFERRED_TO
    - JOINTLY_OWNED_BY

  product:
    - PATENT_TECHNICALLY_LINKED_TO_PRODUCT
    - PATENT_APPLIED_TO_PRODUCT
    - PRODUCT_USES_TECHNOLOGY

  governance:
    - REQUIRES_OFFICIAL_STATUS_AUDIT
    - REQUIRES_CONTRACT_REVIEW
    - HAS_FTO_RISK
    - HAS_IP_WHITE_SPACE
    - GENERATES_OI_SEED
```

---

## 55.2 Core Relationship Triples

```yaml
relationship_triples:

  - edge_id: EDGE-D05-001
    subject: ORG-SKON-RND-001
    predicate: OPERATES_FACILITY
    object: FAC-SKON-D05-001
    source_ids:
      - SRC-SKON-D05-001
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D05-002
    subject: FAC-SKON-D05-001
    predicate: CONTAINS_FACILITY
    object: FAC-SKON-D05-002
    source_ids:
      - SRC-SKON-D05-003
      - SRC-SKON-D05-004
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D05-003
    subject: ORG-SKI-RND-001
    predicate: COLLABORATES_WITH
    object: ORG-SKON-RND-001
    source_ids:
      - SRC-SKON-D05-001
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D05-004
    subject: RDP-SKON-D05-006
    predicate: HOSTED_AT
    object: FAC-SKON-D05-002
    source_ids:
      - SRC-SKON-D05-003
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D05-005
    subject: PF-SKON-D05-002
    predicate: PATENT_SUPPORTS_TECHNOLOGY
    object: TECH-SKON-D04-005
    source_ids:
      - PF-SKON-D05-002
    evidence_level: TECHNICAL_DOCUMENT
    confidence: HIGH

  - edge_id: EDGE-D05-006
    subject: PF-SKON-D05-017
    predicate: PATENT_SUPPORTS_TECHNOLOGY
    object: TECH-SKON-D04-014
    source_ids:
      - PF-SKON-D05-017
    evidence_level: TECHNICAL_DOCUMENT
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-007
    subject: PF-SKON-D05-003
    predicate: PATENT_SUPPORTS_TECHNOLOGY
    object: TECH-SKON-D04-003
    source_ids:
      - PF-SKON-D05-003
    evidence_level: TECHNICAL_DOCUMENT
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-008
    subject: PF-SKON-D05-025
    predicate: PATENT_SUPPORTS_TECHNOLOGY
    object: TECH-SKON-D04-006
    source_ids:
      - PF-SKON-D05-025
    evidence_level: TECHNICAL_DOCUMENT
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-009
    subject: PF-SKON-D05-026
    predicate: SIBLING_FAMILY_OF
    object: PF-SKON-D05-025
    source_ids:
      - PF-SKON-D05-025
      - PF-SKON-D05-026
    evidence_level: ANALYST_INFERENCE
    confidence: HIGH

  - edge_id: EDGE-D05-010
    subject: PF-SKON-D05-027
    predicate: PATENT_SUPPORTS_TECHNOLOGY
    object: TECH-SKON-D04-004
    source_ids:
      - PF-SKON-D05-027
    evidence_level: TECHNICAL_DOCUMENT
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-011
    subject: PF-SKON-D05-023
    predicate: PATENT_SUPPORTS_TECHNOLOGY
    object: TECH-SKON-D04-008
    source_ids:
      - PF-SKON-D05-023
    evidence_level: TECHNICAL_DOCUMENT
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-012
    subject: PF-SKON-D05-006
    predicate: PATENT_SUPPORTS_TECHNOLOGY
    object: TECH-SKON-D04-046
    source_ids:
      - PF-SKON-D05-006
    evidence_level: TECHNICAL_DOCUMENT
    confidence: HIGH

  - edge_id: EDGE-D05-013
    subject: PF-SKON-D05-011
    predicate: PATENT_SUPPORTS_TECHNOLOGY
    object: TECH-SKON-D04-001
    source_ids:
      - PF-SKON-D05-011
    evidence_level: TECHNICAL_DOCUMENT
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-014
    subject: PF-SKON-D05-012
    predicate: JOINTLY_OWNED_BY
    object: APP-POLYPLUS-001
    source_ids:
      - PF-SKON-D05-012
    evidence_level: TECHNICAL_DOCUMENT
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-015
    subject: PF-SKON-D05-033
    predicate: JOINTLY_OWNED_BY
    object: PART-DANKOOK-UNIV
    source_ids:
      - PF-SKON-D05-033
    evidence_level: TECHNICAL_DOCUMENT
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-016
    subject: PAPER-SKON-D05-001
    predicate: PAPER_VALIDATES_TECHNOLOGY
    object: TECH-SKON-D04-066
    source_ids:
      - SRC-RES-D05-001
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-017
    subject: PAPER-SKON-D05-002
    predicate: PAPER_VALIDATES_TECHNOLOGY
    object: TECH-SKON-D04-068
    source_ids:
      - SRC-RES-D05-002
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-018
    subject: PAPER-SKON-D05-002
    predicate: PAPER_TECHNICALLY_LINKED_TO_PATENT
    object: PF-SKON-D05-032
    source_ids:
      - SRC-RES-D05-002
      - PF-SKON-D05-032
    evidence_level: ANALYST_INFERENCE
    confidence: HIGH

  - edge_id: EDGE-D05-019
    subject: PAPER-SKON-D05-003
    predicate: PAPER_VALIDATES_TECHNOLOGY
    object: TECH-SKON-D04-071
    source_ids:
      - SRC-RES-D05-003
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-020
    subject: PAPER-SKON-D05-004
    predicate: PAPER_EXPLAINS_FAILURE_MODE
    object: TECH-SKON-D04-077
    source_ids:
      - SRC-RES-D05-004
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-021
    subject: PAPER-SKON-D05-006
    predicate: PAPER_EXPLAINS_FAILURE_MODE
    object: TECH-SKON-D04-072
    source_ids:
      - SRC-RES-D05-006
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-022
    subject: PAPER-SKON-D05-007
    predicate: PAPER_VALIDATES_TECHNOLOGY
    object: TECH-SKON-D04-075
    source_ids:
      - SRC-RES-D05-007
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-023
    subject: PAPER-SKON-D05-002
    predicate: PAPER_AUTHORED_BY
    object: RES-SKON-D05-007
    source_ids:
      - SRC-RES-D05-002
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D05-024
    subject: PF-SKON-D05-032
    predicate: PATENT_INVENTED_BY
    object: RES-SKON-D05-007
    source_ids:
      - PF-SKON-D05-032
    evidence_level: TECHNICAL_DOCUMENT
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-025
    subject: RES-SKON-D05-012
    predicate: INVENTED_PATENT
    object: PF-SKON-D05-002
    source_ids:
      - PF-SKON-D05-002
    evidence_level: TECHNICAL_DOCUMENT

  - edge_id: EDGE-D05-026
    subject: RES-SKON-D05-012
    predicate: INVENTED_PATENT
    object: PF-SKON-D05-003
    source_ids:
      - PF-SKON-D05-003
    evidence_level: TECHNICAL_DOCUMENT

  - edge_id: EDGE-D05-027
    subject: TECH-SKON-D04-003
    predicate: HAS_IP_WHITE_SPACE
    object: WS-D05-002
    source_ids:
      - D05-WHITE-SPACE-ANALYSIS
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D05-028
    subject: TECH-SKON-D04-006
    predicate: HAS_IP_WHITE_SPACE
    object: WS-D05-001
    source_ids:
      - D05-WHITE-SPACE-ANALYSIS
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D05-029
    subject: TECH-SKON-D04-001
    predicate: HAS_IP_WHITE_SPACE
    object: WS-D05-005
    source_ids:
      - D05-WHITE-SPACE-ANALYSIS
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D05-030
    subject: RDP-SKON-D05-008
    predicate: REQUIRES_GOVERNANCE
    object: WS-D05-007
    source_ids:
      - D05-AI-ASSISTED-INVENTION-GOVERNANCE
    evidence_level: ANALYST_INFERENCE
```

---
