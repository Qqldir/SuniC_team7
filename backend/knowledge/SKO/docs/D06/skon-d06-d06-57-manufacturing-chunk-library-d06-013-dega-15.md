---
id: skon-d06-d06-57-manufacturing-chunk-library-d06-013-dega-15
title: Manufacturing Chunk Library — D06-013 — Degassing·Aging·Grading
summary: "배터리 셀의 가스 제거와 에이징 단계에서 OCV, 자가방전, 두께 변화를 검사하고 성능 기준으로 등급을 분류하는 제조공정을 설명한다."
tags: [d06, process, schema]
keywords: [디개싱, 에이징, 셀 등급분류, OCV, 자가방전, WIP, 잠재결함, 포메이션, 셀 분류 체계, 배터리 품질, 실링, 가스 제거, 용량, 저항, 효율, 안정성]
related: []
priority: normal
domain: D06
section: D06-57.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: Manufacturing Chunk Library
tokens: 291
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영 · Manufacturing Chunk Library

## CH-SKON-D06-013 — Degassing·Aging·Grading

```yaml
chunk_id: CH-SKON-D06-013
title: 디개싱·에이징·셀 등급분류
information_type: ANALYSIS

chunk_text: >
  포메이션 중 생성된 가스를 제거하고 최종 실링한 뒤, 셀을 일정
  조건에서 보관하면서 OCV 감소·자가방전·두께변화를 검사한다.
  이후 용량·저항·효율과 안정성에 따라 셀을 분류한다. 장시간
  에이징은 잠재결함 검출에는 유리하지만 WIP·공간·피드백 지연을
  증가시킨다.

process_ids:
  - PROC-SKON-D06-016
  - PROC-SKON-D06-017
  - PROC-SKON-D06-018

defect_ids:
  - DEF-D06-008
  - DEF-D06-009
  - DEF-D06-010

oi_seed_ids:
  - OI-SEED-D06-020
  - OI-SEED-D06-021
  - OI-SEED-D06-022

source_ids:
  - SRC-BASE-D06-016
  - SRC-BASE-D06-017
  - SRC-BASE-D06-023

evidence_level: ANALYST_INFERENCE
confidence: HIGH
sk_on_disclosure_scope: NOT_DISCLOSED
```

---
