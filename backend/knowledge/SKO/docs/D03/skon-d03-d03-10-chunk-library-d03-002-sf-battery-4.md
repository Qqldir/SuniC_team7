---
id: skon-d03-d03-10-chunk-library-d03-002-sf-battery-4
title: Chunk Library — D03-002 — SF Battery
summary: SK온의 하이니켈 급속충전 EV 배터리인 SF Battery의 성능 사양과 제품 계보상 위치를 설명한다.
tags: [d03, product, schema]
keywords: [하이니켈, 18분 충전, 급속충전, EV 배터리, 초고속충전, 제품 계보, 충전 성능, 전기차, 니켈계, 초고속 충전, 전기자동차]
related: []
priority: normal
domain: D03
section: D03-10.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Chunk Library
tokens: 260
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Chunk Library

## CH-SKON-D03-002 — SF Battery

```yaml
chunk_id: CH-SKON-D03-002
title: SF Battery의 제품 정의와 성능
information_type: FACT

chunk_text: >
  SF Battery는 SK온이 공개한 하이니켈 계열 급속충전 EV 배터리다.
  공식 공개성능은 충전상태 10%에서 80%까지 약 18분이다.
  SF Battery는 SK온 급속충전 제품 계보의 출발점으로, 이후 SF+,
  Advanced SF 및 Hyper Fast Battery 개발로 이어졌다.

entity_ids:
  - PROD-SKON-EV-003
  - PERF-SKON-SF

source_ids:
  - SRC-SKON-D03-004
  - SRC-SKON-D03-005
  - SRC-SKON-D03-052

reliability: A_PLUS
confidence: VERY_HIGH

embedding_tags:
  - SF Battery
  - 18분 충전
  - 급속충전
  - Super Fast Battery

exclusions:
  - 충전기 출력과 외기온도 등 시험조건을 무시한 절대비교 금지
```

---
