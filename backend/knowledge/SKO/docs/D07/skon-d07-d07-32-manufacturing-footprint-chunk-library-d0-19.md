---
id: skon-d07-d07-32-manufacturing-footprint-chunk-library-d0-19
title: Manufacturing Footprint Chunk Library — D07-017 — Ramp-Up
summary: "SK온 신규 배터리 공장 4곳의 현재 가동 단계와 상업생산 상태를 정의하는 자료로, 각 공장이 부분가동·고객Ramp·Pre-SOP 중 어느 단계에 있는지 파악할 수 있다."
tags: [d07, footprint, schema]
keywords: [상업생산, 신규공장, 가동현황, Pre-SOP, 고객승인, Iváncsa, Yancheng, HSBMA, Tennessee, 배터리공장, Ramp-Up, 부분가동, 고객Ramp, 배터리, 가동단계]
related: []
priority: normal
domain: D07
section: D07-32.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: Manufacturing Footprint Chunk Library
tokens: 233
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파 · Manufacturing Footprint Chunk Library

## CH-SKON-D07-017 — Ramp-Up

```yaml
chunk_id: CH-SKON-D07-017
chunk_type: ANALYSIS
title_ko: 신규공장 Ramp-Up 상태
canonical_subject_id: CO-SKON

canonical_text: >
  Iváncsa와 Yancheng 3은 부분가동, HSBMA는 상업생산 이후
  고객 Ramp 단계, Tennessee는 Pre-SOP 단계다. 상업생산 개시는
  전체 설계능력·정상수율·완전한 고객승인을 의미하지 않는다.

plant_ids:
  - PLANT-D07-HU-IVA
  - PLANT-D07-CN-YAN3
  - PLANT-D07-US-HSBMA
  - PLANT-D07-US-TN

oi_seed_ids:
  - OI-SEED-D07-005
  - OI-SEED-D07-011
  - OI-SEED-D07-012

source_ids:
  - SRC-REG-D07-001
  - SRC-OFF-D07-004
  - SRC-OFF-D07-005

source_grade: A_PLUS
evidence_level: ANALYST_INFERENCE
confidence: HIGH
time_scope: AS_OF_2026-08-02
status: ACTIVE
```

---
