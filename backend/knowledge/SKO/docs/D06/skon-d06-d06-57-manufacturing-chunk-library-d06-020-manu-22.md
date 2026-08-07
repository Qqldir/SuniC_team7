---
id: skon-d06-d06-57-manufacturing-chunk-library-d06-020-manu-22
title: Manufacturing Chunk Library — D06-020 — Manufacturing Data Backbone
summary: MES·Historian·QMS의 역할 분담과 Equipment ID·Lot·시간정보를 통한 제조 데이터 통합 기준을 정의한 데이터 아키텍처 거버넌스.
tags: [d06, process, schema]
keywords: [MES, Historian, QMS, 생산지시, 공정신호, 제조 데이터, Equipment ID, Genealogy, 데이터 통합, 공정 아키텍처, Lot 추적, 제조 데이터 통합, 데이터 거버넌스]
related: []
priority: normal
domain: D06
section: D06-57.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: Manufacturing Chunk Library
tokens: 218
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영 · Manufacturing Chunk Library

## CH-SKON-D06-020 — Manufacturing Data Backbone

```yaml
chunk_id: CH-SKON-D06-020
title: MES·Historian·QMS 제조 데이터 아키텍처
information_type: GOVERNANCE_RULE

chunk_text: >
  MES는 생산지시·공정경로·Genealogy를, Historian은 고주파
  설비·공정신호를, QMS는 검사·부적합·Release를 관리해야 한다.
  데이터에는 공통 Equipment ID, Recipe·제품·소재 Lot·공정단계와
  시간정보가 연결돼야 한다.

process_ids:
  - PROC-SKON-D06-024

oi_seed_ids:
  - OI-SEED-D06-007
  - OI-SEED-D06-034
  - OI-SEED-D06-038

source_ids:
  - SRC-STD-D06-033

evidence_level: ANALYST_INFERENCE
confidence: VERY_HIGH
sk_on_disclosure_scope: NOT_DISCLOSED
```

---
