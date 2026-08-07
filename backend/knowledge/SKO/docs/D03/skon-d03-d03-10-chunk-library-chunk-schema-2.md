---
id: skon-d03-d03-10-chunk-library-chunk-schema-2
title: Chunk Library — Chunk Schema
summary: "지식 베이스 청크의 속성과 필드 타입, 신뢰도 등급을 정의한 데이터 스키마"
tags: [d03, product, core-candidate, schema]
keywords: [메타데이터필드, 정보유형, 신뢰도, 확신도, YAML정의, 데이터속성, entity_ids, embedding_tags, 필드타입, D03, 청크 구조, 신뢰도 등급, information_type, 메타데이터, reliability, confidence, 필드 정의, 정보 분류, 속성 정의]
related: []
priority: critical
domain: D03
section: D03-10.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Chunk Library
tokens: 243
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Chunk Library

## 10.1 Chunk Schema

```yaml
chunk_schema:

  chunk_id:
    type: string

  domain:
    fixed_value: D03

  company_id:
    fixed_value: CO-SKON

  title:
    type: string

  chunk_text:
    type: natural_language

  entity_ids:
    type: array

  relation_ids:
    type: array

  information_type:
    allowed_values:
      - FACT
      - ANALYSIS
      - HYPOTHESIS
      - MIXED

  commercial_status:
    type: array

  time_scope:
    type: string

  geography:
    type: array

  source_ids:
    type: array

  reliability:
    allowed_values:
      - A_PLUS
      - A
      - B_PLUS
      - B
      - C

  confidence:
    allowed_values:
      - VERY_HIGH
      - HIGH
      - MEDIUM
      - LOW

  embedding_tags:
    type: array

  exclusions:
    description: 해당 청크로 답변하면 안 되는 질문 또는 과도한 일반화
```

---
