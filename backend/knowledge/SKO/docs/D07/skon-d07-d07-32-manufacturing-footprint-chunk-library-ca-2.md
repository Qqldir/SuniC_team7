---
id: skon-d07-d07-32-manufacturing-footprint-chunk-library-ca-2
title: Manufacturing Footprint Chunk Library — Canonical Chunk Schema
summary: 제조 기반시설 청크 라이브러리에서 지식 정보를 저장할 때 필수적으로 따를 메타데이터 필드와 속성값 범위를 정의한 YAML 스키마 문서.
tags: [d07, footprint, core-candidate, schema]
keywords: [청크, schema, 메타데이터, canonical, 신뢰도, 근거, 생산거점, 거버넌스, 데이터구조, 상태, 지식 청크 메타데이터, 제조기지 데이터 구조, 캐파시티 이벤트, 신뢰도 레벨, 근거 등급, 플랜트 ID, 시간 범위, 데이터 거버넌스, D07 생산거점, canonical subject]
related: []
priority: critical
domain: D07
section: D07-32.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: Manufacturing Footprint Chunk Library
tokens: 227
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파 · Manufacturing Footprint Chunk Library

## 32.1 Canonical Chunk Schema

```yaml
footprint_chunk_schema:

  chunk_id: required
  chunk_type:
    - FACT
    - ANALYSIS
    - GOVERNANCE_RULE
    - HYPOTHESIS
    - MIXED

  title_ko: required
  canonical_subject_id: required
  canonical_text: required

  plant_ids: []
  site_ids: []
  customer_ids: []
  capacity_event_ids: []
  pain_point_ids: []
  oi_seed_ids: []

  source_ids:
    required: true

  source_grade:
    - A_PLUS
    - A
    - B_PLUS
    - B
    - C

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

  time_scope: required

  status:
    - ACTIVE
    - HISTORICAL
    - PROVISIONAL
    - SUPERSEDED

  allowed_uses: []
  blocked_uses: []
```

---
