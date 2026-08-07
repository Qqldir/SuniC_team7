---
id: skon-d06-d06-57-manufacturing-chunk-library-d06-003-mate-5
title: Manufacturing Chunk Library — D06-003 — Material Genealogy
summary: 배터리 제조 시 원재료 Lot에서 최종 Pack까지의 전체 계보를 추적하고 원료 확산 및 팩 구성을 관리하는 방법을 설명하는 문서
tags: [d06, process, schema]
keywords: [제조 추적성, 원료 Lot, 배터리 셀, 스택 어셈블리, 전극 롤, 혼합 배치, 공급사 관리, 제조 이력, Traceability, 공급망 추적, 원재료 Lot, Pack ID, 계보 추적, 배터리 팩, Cell, Batch, 전극, Stack, 계통 추적]
related: []
priority: normal
domain: D06
section: D06-57.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: Manufacturing Chunk Library
tokens: 238
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영 · Manufacturing Chunk Library

## CH-SKON-D06-003 — Material Genealogy

```yaml
chunk_id: CH-SKON-D06-003
title: 원재료 Lot에서 셀·팩까지의 제조 Genealogy
information_type: ANALYSIS

chunk_text: >
  제조 추적성은 공급사 Lot, 사내 Lot, 계량 이벤트, 혼합 Batch,
  전극 Roll, 절단 전극, Stack, Cell, Module과 Pack ID를 연결해야
  한다. 한 원료 Lot가 여러 제품으로 확산되거나 하나의 팩에 특정
  Genealogy가 집중되는 상황을 계산할 수 있어야 한다.

process_ids:
  - PROC-SKON-D06-001
  - PROC-SKON-D06-003
  - PROC-SKON-D06-024

oi_seed_ids:
  - OI-SEED-D06-007
  - OI-SEED-D06-034

source_ids:
  - SRC-BASE-D06-006

evidence_level: ANALYST_INFERENCE
confidence: VERY_HIGH
sk_on_disclosure_scope: NOT_DISCLOSED
```

---
