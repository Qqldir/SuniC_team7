---
id: skon-d03-d03-05-application-mapping-002-premium-and-long-4
title: Application Mapping — 002 — Premium and Long-Range EV
summary: "프리미엄 전기차의 에너지밀도, 충전성능, 고전압 등 성능 요구사항을 충족하는 SK온 배터리 제품 매핑 현황"
tags: [d03, product, schema]
keywords: [하이니켈 NCM, Advanced SF, 전고체 배터리, 에너지밀도, 급속충전, 열관리, 프리미엄 EV, 고전압 배터리, 응용 매핑, 장거리, 고전압, 상용화]
related: []
priority: normal
domain: D03
section: D03-05.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Application Mapping
tokens: 308
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Application Mapping

## APP-SKON-002 — Premium and Long-Range EV

```yaml
application_id: APP-SKON-002
application_name: Premium and Long-Range EV
application_type: ROAD_MOBILITY
maturity: COMMERCIAL

priority_requirements:
  - Volumetric energy density
  - Gravimetric energy density
  - High-power output
  - Fast charging
  - Thermal management
  - High-voltage compatibility

mapped_products:
  primary:
    - PROD-SKON-EV-001
    - PROD-SKON-EV-002
    - PROD-SKON-EV-004
  future:
    - PROD-SKON-NEXT-002

competitive_logic:
  - High-nickel NCM for long-range performance
  - Advanced SF for energy-density and charge-time balance
  - Solid-state battery for future energy-density expansion

confidence: HIGH
```

**ANALYSIS**

하이니켈 NCM과 Advanced SF는 제한된 차량 하부공간에서 에너지밀도와 충전성능을 동시에 높여야 하는 프리미엄 EV에 적합하다. 전고체 배터리는 이 영역의 장기 후보지만 현재 상용제품이 아니므로 `FUTURE_APPLICATION`으로만 연결한다.

---
