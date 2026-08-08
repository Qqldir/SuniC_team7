---
id: skon-d03-8-5-core-product-hierarchy-graph
title: Core Product Hierarchy Graph
summary: "SK온의 EV배터리, ESS, BaaS 서비스 등 주요 제품·서비스의 계층 구조와 각 계열별 세부 제품 목록을 나타낸 그래프."
tags: [d03, product]
keywords: [EV배터리, ESS, 전고체전지, LFP, GRIDON, BaaS, 배터리모니터링, 제품계층, 고니켈, 배터리진단, 에너지저장장치, 배터리서비스, High-Nickel, 전고체셀, 잔존가치평가, BMS]
related: []
priority: normal
domain: D03
section: 8.5
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 387
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 8.5 Core Product Hierarchy Graph

```text
CO-SKON
│
├── HAS_PRODUCT_FAMILY
│   └── PF-SKON-EV-BATTERY
│       ├── HAS_PRODUCT
│       │   ├── PROD-SKON-EV-001 High-Nickel Pouch Battery
│       │   ├── PROD-SKON-EV-007 LFP EV Platform
│       │   ├── PROD-SKON-EV-010 Prismatic Platform
│       │   └── PROD-SKON-EV-011 Cylindrical Platform
│       │
│       └── HAS_NEXT_GENERATION_PRODUCT
│           ├── PROD-SKON-NEXT-001 Polymer-Oxide Composite
│           └── PROD-SKON-NEXT-002 Sulfide ASSB
│
├── HAS_PRODUCT_FAMILY
│   └── PF-SKON-ESS
│       ├── PROD-SKON-ESS-001 LFP ESS Battery
│       ├── PROD-SKON-ESS-002 GRIDON Gen 1
│       ├── PROD-SKON-ESS-003 GRIDON Gen 2
│       ├── PROD-SKON-ESS-004 DC Block
│       └── PROD-SKON-ESS-005 AC Block Configuration
│
└── HAS_SERVICE_FAMILY
    └── PF-SKON-BAAS
        ├── SERV-SKON-BAAS-001 Battery Diagnosis
        ├── SERV-SKON-BAAS-002 Battery Monitoring
        ├── SERV-SKON-BAAS-003 Residual Value Assessment
        ├── SERV-SKON-BAAS-004 Reuse Decision Support
        └── SERV-SKON-BAAS-005 5R Lifecycle Platform
```

SK온 공식 R&D 범위에는 자동차용 셀·모듈·팩·BMS, ESS용 셀·모듈·랙·시스템·BMS 및 전고체 셀이 포함되므로, D03 제품 계층 역시 셀 제품과 시스템·서비스를 분리해 구성한다. ([SK Innovation][1])

---
