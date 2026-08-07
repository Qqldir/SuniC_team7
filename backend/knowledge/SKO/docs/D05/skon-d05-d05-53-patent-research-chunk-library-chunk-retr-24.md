---
id: skon-d05-d05-53-patent-research-chunk-library-chunk-retr-24
title: Patent & Research Chunk Library — Chunk Retrieval Rules
summary: 특허 및 연구 정보 질문 유형별로 우선 참조 청크와 필수 검증 항목을 정의한 검색 규칙
tags: [d05, rnd, schema]
keywords: [특허권, FTO, OI, 청크 검색, 우선순위, 기술스크리닝, 연구결과, 지식재산, 상용화, 자유실시, 특허 조회, 연구 결과, 소유권 검증, 경쟁사 분석, 상용화 현황, 기술 스크리닝, Chunk Retrieval]
related: []
priority: normal
domain: D05
section: D05-53.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: Patent & Research Chunk Library
tokens: 245
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산 · Patent & Research Chunk Library

## 53.2 Chunk Retrieval Rules

```yaml
d05_chunk_retrieval_rules:

  current_owned_patents:
    filters:
      - ownership_scope
      - official_register_status
    mandatory_warning:
      - 공식 등록부 미검증 여부

  product_patent_question:
    priority_chunks:
      - CH-SKON-D05-014
      - relevant_technology_chunk
    prohibited:
      - Direct product implementation inference

  research_result_question:
    priority_chunks:
      - CH-SKON-D05-011
    mandatory_output:
      - Cell configuration
      - Research scale
      - Commercial validation status

  fto_question:
    priority_chunks:
      - CH-SKON-D05-015
      - relevant competitor landscape chunk
    mandatory_warning:
      - Preliminary technical screening only

  oi_question:
    priority_chunks:
      - CH-SKON-D05-016
      - CH-SKON-D05-017
      - CH-SKON-D05-019
```

---
