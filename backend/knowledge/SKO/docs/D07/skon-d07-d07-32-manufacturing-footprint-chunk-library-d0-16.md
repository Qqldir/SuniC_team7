---
id: skon-d07-d07-32-manufacturing-footprint-chunk-library-d0-16
title: Manufacturing Footprint Chunk Library — D07-014 — 고객승인 Redundancy
summary: 물리적으로 동일한 설비가 있더라도 고객승인·원산지·제품검증·JV승인·물류조건을 모두 충족해야 실제 대체공장 용량으로 인정되는 지배규칙
tags: [d07, footprint, schema]
keywords: [대체Capacity, 공급복원능력, 고객승인기준, 제품검증, 소재원산지, JV승인, 물류조건, 백업공장, 공급망, 복구기준, 고객승인, 대체공장, 원산지, 경제적 가용용량]
related: []
priority: normal
domain: D07
section: D07-32.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: Manufacturing Footprint Chunk Library
tokens: 240
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파 · Manufacturing Footprint Chunk Library

## CH-SKON-D07-014 — 고객승인 Redundancy

```yaml
chunk_id: CH-SKON-D07-014
chunk_type: GOVERNANCE_RULE
title_ko: 물리적 Capacity와 대체공장 Capacity
canonical_subject_id: CO-SKON

canonical_text: >
  동일한 설비가 있어도 고객승인, 소재원산지, 제품검증,
  JV 승인과 물류조건을 충족하지 못하면 대체 Capacity가 아니다.
  실제 공급복원능력은 고객승인을 받은 경제적 가용 Capacity로
  계산해야 한다.

pain_point_ids:
  - PP-D07-007

oi_seed_ids:
  - OI-SEED-D07-009
  - OI-SEED-D07-013

source_ids:
  - SRC-OFF-D07-005
  - SRC-OFF-D07-017
  - SRC-OFF-D07-018

source_grade: A
evidence_level: ANALYST_INFERENCE
confidence: VERY_HIGH
time_scope: ALL_DISRUPTION_SCENARIOS
status: ACTIVE
```

---
