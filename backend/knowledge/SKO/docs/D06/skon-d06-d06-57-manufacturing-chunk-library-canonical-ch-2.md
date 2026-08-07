---
id: skon-d06-d06-57-manufacturing-chunk-library-canonical-ch-2
title: Manufacturing Chunk Library — Canonical Chunk Schema
summary: "제조 영역에서 정보 청크의 출처, 신뢰도, 공개 범위 등 메타데이터를 표준화된 YAML 형식으로 정의하는 스키마 구조."
tags: [d06, process, core-candidate, schema]
keywords: [chunk, metadata, schema, 증거 수준, confidence, disclosure scope, 정보 유형, 제조, 메타데이터, 신뢰도, 공개범위, 정보타입, YAML, 필드정의, 데이터구조, confidence_level, disclosure_scope]
related: []
priority: critical
domain: D06
section: D06-57.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: Manufacturing Chunk Library
tokens: 223
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영 · Manufacturing Chunk Library

## 57.1 Canonical Chunk Schema

```yaml
manufacturing_chunk_schema:

  chunk_id: required
  title: required
  domain: D06
  company_id: CO-SKON

  information_type:
    - FACT
    - ANALYSIS
    - HYPOTHESIS
    - GOVERNANCE_RULE
    - MIXED

  chunk_text: required

  process_ids: []
  equipment_ids: []
  technology_ids: []
  patent_family_ids: []
  defect_ids: []
  pain_point_ids: []
  oi_seed_ids: []

  source_ids:
    required: true

  evidence_level:
    - DIRECT_REGULATORY
    - DIRECT_OFFICIAL
    - THIRD_PARTY_VERIFIED
    - ANALYST_INFERENCE
    - HYPOTHESIS

  confidence:
    - VERY_HIGH
    - HIGH
    - MEDIUM
    - LOW

  sk_on_disclosure_scope:
    - DIRECTLY_DISCLOSED
    - PARTIALLY_DISCLOSED
    - NOT_DISCLOSED
    - NOT_APPLICABLE

  exclusions: []
  retrieval_tags: []
```

---
