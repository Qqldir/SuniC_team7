---
id: skon-d07-d07-32-manufacturing-footprint-chunk-library-d0-3
title: Manufacturing Footprint Chunk Library — D07-001 — Capacity Evidence Boundary
summary: "생산능력 수치를 어떻게 분류하고 결합해야 하나? 설계능력, 공시능력, 고객승인능력, 실제생산량 등을 구분하는 거버넌스 규칙이다."
tags: [d07, footprint, schema]
keywords: [생산능력 수치 분류, 설계 생산능력, 공시상 최대 생산능력, GWh, JV 총설계능력, 생산량, 캐파시티, 거버넌스 규칙, 생산거점, 회계연결범위, 생산능력, 설계능력, 공시능력, 고객승인, 실제생산량, JV, 회계 범위, 배터리]
related: []
priority: normal
domain: D07
section: D07-32.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: Manufacturing Footprint Chunk Library
tokens: 258
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파 · Manufacturing Footprint Chunk Library

## CH-SKON-D07-001 — Capacity Evidence Boundary

```yaml
chunk_id: CH-SKON-D07-001
chunk_type: GOVERNANCE_RULE
title_ko: 생산능력 수치의 구분원칙
canonical_subject_id: CO-SKON

canonical_text: >
  설계 생산능력, 공시상 최대 생산능력, JV 총설계능력,
  고객승인 생산능력, 실제 생산량과 미래 목표 생산능력을 분리한다.
  기준일·소유구조·회계 연결범위가 다른 GWh는 하나의 합계로
  결합하지 않는다.

source_ids:
  - SRC-REG-D07-001
  - SRC-OFF-D07-002

source_grade: A_PLUS
evidence_level: ANALYST_INFERENCE
confidence: VERY_HIGH
time_scope: ALL_D07_RECORDS
status: ACTIVE

allowed_uses:
  - Capacity reconciliation
  - Scenario design
  - Plant comparison

blocked_uses:
  - Adding all published GWh
  - Treating targets as current output
```

---
