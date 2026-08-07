---
id: skon-d05-d05-53-patent-research-chunk-library-canonical-3
title: Patent & Research Chunk Library — Canonical Chunk Schema
summary: "SK온 특허·연구 정보의 표준 색인 스키마로서 청크 메타데이터 필드, 정보유형, 신뢰도, 법적상태 분류 기준을 제시한다."
tags: [d05, rnd, core-candidate, schema]
keywords: [메타데이터, 필드 정의, YAML, D05, 데이터 모델, 정보 유형, 신뢰도, chunk_id, 소스 추적, 기술 연계, 정보유형, 색인화, 법적상태, 기술정보, 거버넌스]
related: []
priority: critical
domain: D05
section: D05-53.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: Patent & Research Chunk Library
tokens: 338
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산 · Patent & Research Chunk Library

## 53.1 Canonical Chunk Schema

```yaml
d05_chunk_schema:

  chunk_id:
    type: canonical_string
    required: true

  title:
    type: string
    required: true

  domain:
    fixed_value: D05

  company_id:
    fixed_value: CO-SKON

  information_type:
    allowed_values:
      - FACT
      - ANALYSIS
      - HYPOTHESIS
      - GOVERNANCE_RULE
      - MIXED

  chunk_text:
    type: string
    required: true

  organization_ids:
    type: array

  facility_ids:
    type: array

  program_ids:
    type: array

  technology_ids:
    type: array

  patent_family_ids:
    type: array

  paper_ids:
    type: array

  researcher_ids:
    type: array

  partner_ids:
    type: array

  source_ids:
    type: array
    required: true

  legal_status_scope:
    allowed_values:
      - NOT_APPLICABLE
      - DOCUMENT_IDENTIFIED
      - AGGREGATOR_SNAPSHOT
      - OFFICIAL_REGISTER_VERIFIED
      - AUDIT_REQUIRED

  claim_status:
    allowed_values:
      - SOURCE_SUPPORTED_FACT
      - TECHNICAL_MATCH
      - ANALYST_INFERENCE
      - HYPOTHESIS

  confidence:
    allowed_values:
      - VERY_HIGH
      - HIGH
      - MEDIUM
      - LOW

  retrieval_tags:
    type: array

  exclusions:
    type: array
```

---
