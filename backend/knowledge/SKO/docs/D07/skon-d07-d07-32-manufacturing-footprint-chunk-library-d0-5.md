---
id: skon-d07-d07-32-manufacturing-footprint-chunk-library-d0-5
title: Manufacturing Footprint Chunk Library — D07-003 — 연결 가동률
summary: SK온의 2024년부터 2026년 1분기까지 연결 평균 가동률(43.8% → 48.7% → 36.5%) 및 부하시간/조업시간 기반 계산 방식을 정의하는 사실 데이터
tags: [d07, footprint, schema]
keywords: [SK온, 가동률, 연결 기준, capacity utilization, 부하시간, 조업시간, 계획정지, operational efficiency, 캐파, 계획정지시간, 가동 효율, 평균율, 산식, capacity, 가동 현황, 반기별]
related: []
priority: normal
domain: D07
section: D07-32.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: Manufacturing Footprint Chunk Library
tokens: 243
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파 · Manufacturing Footprint Chunk Library

## CH-SKON-D07-003 — 연결 가동률

```yaml
chunk_id: CH-SKON-D07-003
chunk_type: FACT
title_ko: SK온 연결 평균 가동률
canonical_subject_id: CO-SKON

canonical_text: >
  연결 기준 평균 가동률은 2024년 43.8%, 2025년 48.7%,
  2026년 1분기 36.5%다. 회사 산식은 부하시간을 조업시간으로
  나누며 계획정지시간을 부하시간에서 제외한다.

source_ids:
  - SRC-REG-D07-001

source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY
confidence: VERY_HIGH
time_scope: 2024_TO_2026_Q1
status: ACTIVE

allowed_uses:
  - Consolidated trend analysis

blocked_uses:
  - Applying 36.5% to every plant
  - Deriving plant output
```

가동률은 연결법인 평균이며, 공장별 가동률로 분해할 수 없다. ([KIND][3])

---
