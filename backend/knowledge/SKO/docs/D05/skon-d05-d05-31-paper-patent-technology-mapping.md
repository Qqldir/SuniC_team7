---
id: skon-d05-d05-31-paper-patent-technology-mapping
title: Paper–Patent–Technology Mapping
summary: 논문이 지원하는 특허군과 기술을 체계적으로 연결하고 관계 유형·확신도를 기록하는 통합 매핑 매트릭스 및 관계 분류 체계.
tags: [d05, rnd, schema, table, "xref:d04"]
keywords: [논문-특허 매핑, 기술 검증, 특허 대응 관계, 관계 분류, LMRO 단결정, 선행기술 추적, 확신도 평가, 메타데이터, 논문-특허 연결, 특허군, 선행기술, 관계 어휘, 확신도, LMRO, LLZO, 발명 대응]
related: []
priority: normal
domain: D05
section: D05-31.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1316
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-31. Paper–Patent–Technology Mapping

## 31.1 Canonical Relationship Vocabulary

```yaml
paper_relationship_vocabulary:

  PAPER_VALIDATES_TECHNOLOGY:
    meaning: 논문 실험이 특정 기술의 작동원리나 성능을 검증

  PAPER_EXPLAINS_FAILURE_MODE:
    meaning: 논문이 열화·불량·계면반응의 원인을 규명

  PAPER_SUPPORTS_PATENT:
    meaning: 논문과 특허가 동일하거나 매우 유사한 발명구성을 공유
    requirement:
      - Inventor or author overlap
      - Priority and publication timeline
      - Technical claim correspondence

  PAPER_TECHNICALLY_LINKED_TO_PATENT:
    meaning: 기술적으로 연결되지만 동일 발명인지 미확정

  PAPER_PRECEDES_PATENT:
    meaning: 논문이 후속 특허의 선행기술이 될 수 있음

  NO_DIRECT_PATENT_IDENTIFIED:
    meaning: 검토한 공개자료에서 직접 대응 특허군 미확인
```

## 31.2 Integrated Mapping Matrix

| Paper ID      | 핵심 기술         | 연결 Patent Family | 관계                                 |   확신도 |
| ------------- | ------------- | ---------------- | ---------------------------------- | ----: |
| PAPER-D05-001 | SIPE          | 미확인              | NO_DIRECT_PATENT_IDENTIFIED        |    높음 |
| PAPER-D05-002 | 광소결 LLZTO     | PF-D05-032       | PAPER_TECHNICALLY_LINKED_TO_PATENT |    높음 |
| PAPER-D05-002 | LLZO 플랫폼      | PF-D05-033       | RELATED_MATERIAL_PLATFORM          |    중간 |
| PAPER-D05-003 | 리튬 표면개질       | 미확인              | NO_DIRECT_PATENT_IDENTIFIED        |    높음 |
| PAPER-D05-004 | GPE 경화·잔류 모노머 | 미확인              | NO_DIRECT_PATENT_IDENTIFIED        |    높음 |
| PAPER-D05-005 | LMRO 단결정 합성   | 미확인              | NO_DIRECT_PATENT_IDENTIFIED        |    중간 |
| PAPER-D05-006 | LMRO·황화물 계면   | PF-D05-011       | POSSIBLY_SUPPORTS                  | 낮음~중간 |
| PAPER-D05-007 | 초고니켈 대형 단결정   | PF-D05-013       | EARLIER_PLATFORM_IP_ONLY           |    낮음 |

## 31.3 Relationship Triples

```yaml
paper_patent_technology_triples:

  - edge_id: EDGE-D05-PAPER-001
    subject: PAPER-SKON-D05-001
    predicate: PAPER_VALIDATES_TECHNOLOGY
    object: TECH-SKON-D04-066
    source_ids:
      - SRC-RES-D05-001
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-PAPER-002
    subject: PAPER-SKON-D05-002
    predicate: PAPER_TECHNICALLY_LINKED_TO_PATENT
    object: PF-SKON-D05-032
    source_ids:
      - SRC-RES-D05-002
      - SRC-PAT-D05-032
    evidence_level: ANALYST_INFERENCE
    confidence: HIGH

  - edge_id: EDGE-D05-PAPER-003
    subject: PAPER-SKON-D05-003
    predicate: PAPER_VALIDATES_TECHNOLOGY
    object: TECH-SKON-D04-071
    source_ids:
      - SRC-RES-D05-003
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-PAPER-004
    subject: PAPER-SKON-D05-004
    predicate: PAPER_EXPLAINS_FAILURE_MODE
    object: TECH-SKON-D04-077
    source_ids:
      - SRC-RES-D05-004
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-PAPER-005
    subject: PAPER-SKON-D05-005
    predicate: PAPER_VALIDATES_TECHNOLOGY
    object: TECH-SKON-D04-074
    source_ids:
      - SRC-RES-D05-005
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-PAPER-006
    subject: PAPER-SKON-D05-006
    predicate: PAPER_EXPLAINS_FAILURE_MODE
    object: TECH-SKON-D04-072
    source_ids:
      - SRC-RES-D05-006
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH

  - edge_id: EDGE-D05-PAPER-007
    subject: PAPER-SKON-D05-007
    predicate: PAPER_VALIDATES_TECHNOLOGY
    object: TECH-SKON-D04-075
    source_ids:
      - SRC-RES-D05-007
    evidence_level: THIRD_PARTY_VERIFIED
    confidence: VERY_HIGH
```

### 분석

논문과 특허의 관계가 가장 선명한 영역은 광소결 산화물 전해질이다. 반대로 SIPE, 표면개질 리튬, GPE 잔류 모노머와 초고니켈 대형 단결정은 연구성과가 명확하지만 직접 대응하는 특허군이 아직 확인되지 않았다. 이는 곧바로 IP 공백을 의미하지 않으며, 비공개 출원·공동출원·다른 명칭의 특허 또는 노하우 보호 가능성을 추가 검증해야 한다.

---
