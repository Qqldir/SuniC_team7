---
id: skon-d03-d03-10-chunk-library-d03-011-baas-lifecycle-dec-13
title: Chunk Library — D03-011 — BaaS Lifecycle Decision
summary: "배터리의 차량 계속 사용, ESS 재활용, 소재 재활용 등 라이프사이클 단계를 판단하기 위한 평가 지표와 의사결정 프레임워크를 설명한다."
tags: [d03, product, schema]
keywords: [SOH, 잔여수명, RUL, ESS 재사용, 배터리 라이프사이클, 잔존가치, 사용이력, 5R, 차량 탑재, 의사결정, BaaS, 배터리 재사용, 배터리 재활용, ESS]
related: []
priority: normal
domain: D03
section: D03-10.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Chunk Library
tokens: 305
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Chunk Library

## CH-SKON-D03-011 — BaaS Lifecycle Decision

```yaml
chunk_id: CH-SKON-D03-011
title: BaaS의 재사용·재활용 의사결정 구조
information_type: ANALYSIS

chunk_text: >
  SK온의 BaaS 데이터는 배터리가 차량에서 계속 사용될 수 있는지,
  수리 또는 교체가 필요한지, 회수 후 ESS로 재사용할 수 있는지,
  또는 소재 재활용 단계로 보내야 하는지를 판단하는 기반으로 활용될
  수 있다. 이를 위해서는 SOH와 잔여수명뿐 아니라 사용이력, 이상이력,
  안전상태 및 경제적 잔존가치를 함께 평가해야 한다.

entity_ids:
  - SERV-SKON-BAAS-003
  - SERV-SKON-BAAS-004
  - SERV-SKON-BAAS-005

source_ids:
  - SRC-SKON-D03-021
  - SRC-SKON-D03-022
  - SRC-SKON-D03-056

reliability: A_PLUS
confidence: HIGH

embedding_tags:
  - 배터리 재사용
  - 배터리 재활용
  - 잔여수명
  - 잔존가치
  - 5R
```

---
