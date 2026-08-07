---
id: skon-d03-8-6-fast-charging-product-evolution-graph
title: Fast-Charging Product Evolution Graph
summary: "SK온 초고속충전 배터리 제품의 진화 과정, 적용 기술, 충전 성능(10~80%), 개발 성숙도를 보여주는 그래프"
tags: [d03, product, schema]
keywords: [급속충전, SF배터리, 충전성능, 배터리기술, 기술진화, 성숙도, Hyper Fast, SKON-EV, 전극설계, 충전프로토콜, 초고속충전, fast-charging, SF 배터리, 배터리 진화, 충전 성능, 기술 성숙도, 양산성]
related: []
priority: normal
domain: D03
section: 8.6
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 418
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 8.6 Fast-Charging Product Evolution Graph

```text
PROD-SKON-EV-003 SF Battery
│
├── EVOLVED_TO
│   ├── PROD-SKON-EV-005 SF+ Battery
│   │   └── USES_TECHNOLOGY
│   │       └── TECH-SKON-DUAL-LAYER-ANODE
│   │
│   └── PROD-SKON-EV-004 Advanced SF Battery
│       └── USES_TECHNOLOGY
│           └── TECH-SKON-MAGNETIC-ALIGNMENT
│
└── TECHNOLOGY_LINEAGE_TO
    └── PROD-SKON-EV-006 Hyper Fast Battery
        └── USES_TECHNOLOGY
            └── TECH-SKON-SUFAST
                ├── OPTIMIZES → Electrode Design
                └── OPTIMIZES → Charging Protocol
```

```yaml
fast_charge_performance_nodes:

  PERF-SKON-SF:
    charge_window: 10_to_80_percent
    time_minutes: 18
    status: COMMERCIAL_PRODUCT_CLAIM

  PERF-SKON-SF-PLUS:
    charge_window: 10_to_80_percent
    time_minutes: 15
    status: DISCLOSED_PRODUCT_TECHNOLOGY

  PERF-SKON-ADV-SF:
    charge_window: 10_to_80_percent
    time_minutes: 18
    additional_attribute: 8_percent_energy_density_improvement
    status: VEHICLE_APPLICATION_CONFIRMED

  PERF-SKON-HYPER:
    charge_window: 10_to_80_percent
    time_minutes: less_than_7
    status: TECHNOLOGY_DEMONSTRATION
```

제품별 충전성능은 상용제품·공개기술·시제품이라는 서로 다른 성숙도 상태를 유지해야 한다. 특히 Hyper Fast의 7분 미만 성능은 양산성과 고객차량 적용이 아직 확인되지 않은 기술 시연값이다. ([ASK Inno][2])

---
