---
id: skon-d03-d03-05-application-mapping-003-fast-charging-ev-5
title: Application Mapping — 003 — Fast-Charging EV
summary: "SK온의 빠른 충전 EV 솔루션에 매핑된 제품군과 SF Battery, SF Plus, Hyper Fast 세 성능 계층별 10~80% 충전 시간을 정의하는 표."
tags: [d03, product, schema]
keywords: [충전 속도, 배터리 열관리, 적응형 충전 프로토콜, 셀 밸런싱, 리튬 플레이팅, 고전력 충전기, 10-80% 충전, Hyper Fast, SF Battery, 그리드 연결 용량, 초급속 충전, EV 배터리, 열관리 시스템, 리튬 도금 방지, 그리드 연계, 도로 이동, 제품 매핑]
related: []
priority: normal
domain: D03
section: D03-05.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Application Mapping
tokens: 297
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Application Mapping

## APP-SKON-003 — Fast-Charging EV

```yaml
application_id: APP-SKON-003
application_name: Fast-Charging EV
application_type: ROAD_MOBILITY
maturity:
  current: COMMERCIAL
  advanced: TECHNOLOGY_DEMONSTRATION

mapped_products:
  commercial:
    - PROD-SKON-EV-003
    - PROD-SKON-EV-004
  disclosed_product_technology:
    - PROD-SKON-EV-005
  prototype:
    - PROD-SKON-EV-006

performance_layers:
  SF_Battery: 10_to_80_percent_in_18_minutes
  SF_Plus: 10_to_80_percent_in_15_minutes
  Hyper_Fast: 10_to_80_percent_in_less_than_7_minutes

critical_system_dependencies:
  - High-power charger
  - Battery thermal management
  - Adaptive charging protocol
  - Cell balancing
  - Lithium-plating prevention
  - Grid connection capacity

confidence: HIGH
```

Hyper Fast의 7분 미만 충전은 공개된 기술 성능이지 특정 양산차 적용을 확인한 수치가 아니다. 따라서 사람용 보고서와 AI 질의응답 모두에서 `PROTOTYPE_PERFORMANCE` 태그를 유지해야 한다.

---
