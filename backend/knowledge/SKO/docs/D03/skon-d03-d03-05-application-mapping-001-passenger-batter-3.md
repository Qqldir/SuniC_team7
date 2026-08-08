---
id: skon-d03-d03-05-application-mapping-001-passenger-batter-3
title: Application Mapping — 001 — Passenger Battery Electric Vehicle
summary: "SK온 승용 전기차 배터리의 기술 요구사항(에너지 밀도, 급속 충전 등)과 현대·기아·폭스바겐 탑재 사례를 정리한 문서"
tags: [d03, product, schema]
keywords: [전기차, 하이니켈, EV 배터리, 에너지밀도, 충전속도, 저온성능, 파우치, 주행거리, 에너지 밀도, 급속 충전, 충방전 사이클, 저온 성능, 아이오닉5, EV6, ID.4]
related: []
priority: normal
domain: D03
section: D03-05.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Application Mapping
tokens: 360
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Application Mapping

## APP-SKON-001 — Passenger Battery Electric Vehicle

```yaml
application_id: APP-SKON-001
application_name: Passenger Battery Electric Vehicle
application_type: ROAD_MOBILITY
maturity: COMMERCIAL_CORE

required_product_characteristics:
  - High energy density
  - Long driving range
  - Fast charging
  - Crash safety
  - Cycle life
  - Low-temperature performance
  - Vehicle-pack integration

mapped_products:
  - PROD-SKON-EV-001
  - PROD-SKON-EV-002
  - PROD-SKON-EV-003
  - PROD-SKON-EV-004
  - PROD-SKON-EV-005

historically_confirmed_vehicle_examples:
  - Hyundai IONIQ 5
  - Hyundai IONIQ 6
  - Kia EV6
  - Volkswagen ID.4

customer_types:
  - Global Automaker
  - EV Platform Company

evidence:
  - SRC-SKON-D03-030
  - SRC-SKON-D03-032

confidence: HIGH
```

승용 전기차는 SK온 하이니켈 파우치 제품군의 핵심 상용 적용영역이다. 현대·기아 전기차와 폭스바겐 ID.4 적용은 공식 자료로 확인되지만, 차량 연식·트림·생산지역에 따라 배터리 공급사가 달라질 수 있으므로 특정 모델의 전 생산물량에 SK온 배터리가 사용된다고 일반화해서는 안 된다. ([ASK Inno][4])

---
