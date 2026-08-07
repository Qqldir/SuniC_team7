---
id: skon-d06-d06-57-manufacturing-chunk-library-d06-019-pack-21
title: Manufacturing Chunk Library — D06-019 — Pack·BMS·EoL
summary: 배터리팩 조립에 통합되는 구성요소들과 출하검사에서 검증해야 할 전압·절연·냉각·센싱·통신 등의 확인항목을 규정하는 지침
tags: [d06, process, schema]
keywords: [배터리팩 조립, Module, CTP, 냉각회로, BMS 관리, 고전압 부품, 출하검사 기준, Contactor, 절연 검사, 품질 검증, 고전압부품, 절연검사, 센싱, Firmware, Genealogy, 누수검사]
related: []
priority: normal
domain: D06
section: D06-57.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: Manufacturing Chunk Library
tokens: 260
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영 · Manufacturing Chunk Library

## CH-SKON-D06-019 — Pack·BMS·EoL

```yaml
chunk_id: CH-SKON-D06-019
title: 팩 구조·BMS·냉각회로·출하검사
information_type: ANALYSIS

chunk_text: >
  팩 조립은 Module 또는 CTP 어셈블리, 구조부재, 냉각회로,
  고전압부품, BMS와 센싱·통신부를 통합한다. 출하검사에서는
  전압·절연·Contactor·통신·센서·냉각누설·Enclosure Seal,
  Firmware와 Genealogy를 확인하는 목표모델이 필요하다.

process_ids:
  - PROC-SKON-D06-021A
  - PROC-SKON-D06-021B
  - PROC-SKON-D06-021C
  - PROC-SKON-D06-021D

defect_ids:
  - DEF-D06-017
  - DEF-D06-018
  - DEF-D06-020

oi_seed_ids:
  - OI-SEED-D06-032
  - OI-SEED-D06-033

source_ids:
  - SRC-PAT-D06-027
  - SRC-PAT-D06-028
  - SRC-PAT-D06-030

evidence_level: ANALYST_INFERENCE
confidence: HIGH
sk_on_disclosure_scope: NOT_DISCLOSED
```

---
