---
id: skon-d03-8-14-pain-point-graph
title: Pain Point Graph
summary: 배터리·ESS 제품의 기술적 한계(pain point)와 이를 근거로 도출한 사업 기회 아이디어(OI Seed)의 인과 관계를 매핑한 분석 자료.
tags: [d03, product, "xref:d17"]
keywords: [기술 과제, GRIDON, 급속충전, 생산 수율, 혁신 기회, ASSB, 배터리 제품, 상용화, 경쟁 과제, 제품 전략, 기술과제, 혁신기회, 고속충전, 열관리, Prismatic, 사이클수명, SOH, 양산]
related: []
priority: normal
domain: D03
section: 8.14
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 695
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 8.14 Pain Point Graph

```text
PROD-SKON-EV-006 Hyper Fast Battery
├── HAS_PAIN_POINT → PAIN-LITHIUM-PLATING
├── HAS_PAIN_POINT → PAIN-FAST-CHARGE-HEAT
├── HAS_PAIN_POINT → PAIN-ELECTROLYTE-DECOMPOSITION
└── HAS_PAIN_POINT → PAIN-CYCLE-LIFE

PROD-SKON-EV-010 Prismatic Platform
├── HAS_PAIN_POINT → PAIN-CAN-SEALING
├── HAS_PAIN_POINT → PAIN-VENT-RELIABILITY
├── HAS_PAIN_POINT → PAIN-MASS-PRODUCTION-YIELD
└── HAS_PAIN_POINT → PAIN-PACK-INTEGRATION

PROD-SKON-ESS-002 GRIDON
├── HAS_PAIN_POINT → PAIN-THERMAL-PROPAGATION
├── HAS_PAIN_POINT → PAIN-OFF-GAS-EARLY-DETECTION
├── HAS_PAIN_POINT → PAIN-LONG-TERM-DEGRADATION
├── HAS_PAIN_POINT → PAIN-WARRANTY-RISK
└── HAS_PAIN_POINT → PAIN-PCS-EMS-INTEROPERABILITY

PROD-SKON-NEXT-002 Sulfide ASSB
├── HAS_PAIN_POINT → PAIN-SOLID-SOLID-INTERFACE
├── HAS_PAIN_POINT → PAIN-MOISTURE-SENSITIVITY
├── HAS_PAIN_POINT → PAIN-H2S-SAFETY
├── HAS_PAIN_POINT → PAIN-HIGH-PRESSURE-STACK
└── HAS_PAIN_POINT → PAIN-PILOT-YIELD

SERV-SKON-BAAS-003 Residual Value Assessment
├── HAS_PAIN_POINT → PAIN-CROSS-OEM-DATA
├── HAS_PAIN_POINT → PAIN-SOH-STANDARDIZATION
├── HAS_PAIN_POINT → PAIN-DATA-OWNERSHIP
└── HAS_PAIN_POINT → PAIN-DIAGNOSIS-EXPLAINABILITY
```

위 Pain Point 관계는 제품 특성과 경쟁사 공개자료를 기반으로 도출한 **분석 엔티티**다. SK온이 해당 문제를 공식적으로 모두 인정했다는 뜻이 아니며, D17 과제 발굴을 위한 분석 레이어로 저장한다.

---

# 8.15 OI Seed Graph

```text
PAIN-LFP-EV-COMMERCIALIZATION
└── GENERATES_OI_SEED
    └── OI-SEED-D03-001 LFP Ultra-Fast-Charging EV Platform

PAIN-PRISMATIC-MASS-PRODUCTION
└── GENERATES_OI_SEED
    └── OI-SEED-D03-002 Prismatic Commercialization Accelerator

PAIN-ESS-CONTAINER-DENSITY
└── GENERATES_OI_SEED
    └── OI-SEED-D03-003 GRIDON High-Density Container Program

PAIN-ESS-WARRANTY-RISK
└── GENERATES_OI_SEED
    └── OI-SEED-D03-004 GRIDON Software and Warranty Intelligence

PAIN-HYPER-FAST-COMMERCIALIZATION
└── GENERATES_OI_SEED
    └── OI-SEED-D03-005 Seven-Minute Charging Commercial Validation

PAIN-DRY-ELECTRODE-SCALE-UP
└── GENERATES_OI_SEED
    └── OI-SEED-D03-006 Dry Electrode Mass-Production Scale-Up

PAIN-ESS-OFF-GAS-DETECTION
└── GENERATES_OI_SEED
    └── OI-SEED-D03-007 ESS Thermal Propagation and Off-Gas Intelligence

PAIN-MULTI-FORM-FACTOR
└── GENERATES_OI_SEED
    └── OI-SEED-D03-008 Multi-Form-Factor Manufacturing Platform
```

---
