---
id: skon-d03-8-8-ess-architecture-graph
title: ESS Architecture Graph
summary: "SK온 GRIDON ESS와 BaaS 솔루션의 제품 아키텍처, 고객 대상, 배터리 생명주기, 파트너십을 보여주는 네 가지 그래프"
tags: [d03, product]
keywords: [GRIDON, ESS, BaaS, 배터리모니터링, BMS, LFP, 상태진단, 잔존수명, 재사용결정, 데이터센터, 배터리 모니터링, 상태 진단, 잔존가치, 생명주기, 파트너, 재사용, 고객 세그먼트]
related: []
priority: normal
domain: D03
section: 8.8
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 1381
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 8.8 ESS Architecture Graph

```text
PROD-SKON-ESS-002 GRIDON Gen 1
│
├── HAS_COMPONENT
│   ├── PROD-SKON-ESS-001 LFP ESS Cell
│   ├── ARCH-SKON-ESS-MODULE
│   ├── ARCH-SKON-ESS-RACK
│   ├── PROD-SKON-ESS-004 DC Block
│   ├── TECH-SKON-EIS-BMS
│   └── TECH-SKON-COOLANT-IMMERSION
│
├── SUPPORTS_APPLICATION
│   ├── APP-SKON-005 Utility-Scale Storage
│   ├── APP-SKON-006 Renewable Integration
│   ├── APP-SKON-007 AI Data Center
│   └── APP-SKON-008 Industrial Facility
│
└── HAS_SUCCESSOR
    └── PROD-SKON-ESS-003 GRIDON Gen 2
        ├── SUPPORTS_ARCHITECTURE → PROD-SKON-ESS-004 DC Block
        ├── SUPPORTS_ARCHITECTURE → PROD-SKON-ESS-005 AC Block
        ├── USES_TECHNOLOGY → TECH-SKON-EIS-BMS
        └── USES_TECHNOLOGY → TECH-SKON-COOLANT-FIRE-SUPPRESSION
```

GRIDON은 단일 셀이 아니라 BMS·열관리·화재대응과 시스템 아키텍처가 결합된 ESS 솔루션이다. Gen 2는 DC와 AC 블록 지원, 컨테이너 용량 개선 및 2027년 3분기 상업생산 목표를 갖는다. ([ASK Inno][7])

---

# 8.9 ESS Customer Graph

```text
PROD-SKON-ESS-001 LFP ESS Battery
├── SUPPLIED_TO → CUST-SKON-ESS-001 Flatiron Energy Development
└── APPLIED_TO → CUST-SKON-ESS-002 Korea ESS Central Contract Market

PROD-SKON-ESS-002 GRIDON Gen 1
├── TARGETS_CUSTOMER_TYPE → Utility
├── TARGETS_CUSTOMER_TYPE → IPP
├── TARGETS_CUSTOMER_TYPE → Renewable Energy Developer
├── TARGETS_CUSTOMER_TYPE → ESS Integrator
├── TARGETS_CUSTOMER_TYPE → AI Data Center Operator
└── TARGETS_CUSTOMER_TYPE → Industrial Facility

PROD-SKON-ESS-003 GRIDON Gen 2
├── TARGETS_APPLICATION → Grid-Scale Storage
├── TARGETS_APPLICATION → AI Data Center
└── TARGETS_APPLICATION → Large-Load Facility
```

GRIDON Gen 2는 미국 전력사업자·재생에너지 개발사·유틸리티·ESS 통합사·금융투자자 등을 대상으로 공개됐지만, 행사 참여기업 전체가 계약고객을 의미하지는 않는다. ([ASK Inno][8])

---

# 8.10 BaaS Lifecycle Graph

```text
VEHICLE_OR_BATTERY
│
└── GENERATES_DATA
    ├── Driving Data
    ├── Charging Data
    ├── Temperature Data
    ├── Voltage Data
    └── Battery Usage History
          │
          ▼
SERV-SKON-BAAS-002 Battery Monitoring
          │
          ▼
TECH-SKON-BAAS-AI
├── ESTIMATES → State of Health
├── ESTIMATES → Remaining Useful Life
├── DETECTS → Battery Abnormality
├── ESTIMATES → Residual Value
└── GENERATES → Driving and Charging Guidance
          │
          ▼
SERV-SKON-BAAS-004 Reuse Decision Support
├── ROUTES_TO → Continue Vehicle Use
├── ROUTES_TO → Repair
├── ROUTES_TO → Reuse as ESS
└── ROUTES_TO → Recycling
```

BaaS AI는 주행·충전 데이터를 활용해 상태진단과 잔존가치 분석을 수행하도록 개발됐다. K Car와의 협력은 중고 EV 평가로, KAIWA 협력은 평가표준으로 연결된다. ([ASK Inno][6])

---

# 8.11 BaaS Partner Graph

```text
TECH-SKON-BAAS-AI
│
├── DELIVERED_THROUGH
│   └── PART-SOFTBERRY
│       └── OPERATES → EV Infra
│
├── APPLIED_WITH
│   └── CUST-SKON-BAAS-002 K Car
│       └── SUPPORTS → Used-EV Valuation
│
├── APPLIED_WITH
│   └── CUST-SKON-BAAS-003 SK Rent-a-car
│       └── PROVIDES → Fleet Driving Data
│
├── DELIVERED_THROUGH
│   └── CUST-SKON-BAAS-004 Macarong Factory
│       └── OPERATES → Mycle
│
├── STANDARDIZED_WITH
│   └── CUST-SKON-BAAS-005 KAIWA
│
└── INTEGRATED_WITH
    └── PART-SK-SIGNET
        └── ENABLES → Charger-Based Battery Diagnosis
```

SK온은 애플리케이션, 렌터카, 중고차, 검사·보증기관 및 충전기 기업과 BaaS 기술을 연결해 왔다. 다만 각각의 협력은 시범·업무협약·서비스 출시 등 상태가 다르므로 모두 현재 대규모 상용매출로 처리하지 않는다. ([ASK Inno][14])

---

# 8.12 Next-Generation Battery Graph

```text
PF-SKON-NEXT-GEN-BATTERY
│
├── HAS_PRODUCT
│   ├── PROD-SKON-NEXT-001 Polymer-Oxide Composite Battery
│   │   ├── USES_TECHNOLOGY → Polymer Electrolyte
│   │   ├── USES_TECHNOLOGY → Oxide Electrolyte
│   │   └── STATUS → PILOT_DEVELOPMENT
│   │
│   └── PROD-SKON-NEXT-002 Sulfide ASSB
│       ├── USES_CHEMISTRY → Sulfide Solid Electrolyte
│       ├── MAY_USE → Lithium-Metal Anode
│       ├── CO_DEVELOPED_WITH → PART-SOLID-POWER
│       ├── PILOTED_AT → SITE-SKON-DAEJEON-ASSB
│       └── STATUS → R_AND_D
│
└── HAS_COMMERCIALIZATION_TARGET
    └── TARGET-2029
```

SK온은 폴리머-산화물 복합형과 황화물계 전고체 기술을 개발하고 있으며, 대전 파일럿 시설과 Solid Power 협력을 통해 양산 전 검증을 진행한다. 상용화 목표는 계획값으로 유지한다. ([ASK Inno][15])

---
