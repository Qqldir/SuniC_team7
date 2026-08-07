---
id: skon-d03-d03-03-next-next-generation-product-master
title: NEXT. Next-Generation Product Master
summary: "SK온의 폴리머-산화물 복합 배터리와 황화물계 전고체 배터리의 기술 사양, 개발 진행도, 상용화 시점을 정리한 제품 기술 자료"
tags: [d03, product, schema, "xref:d17"]
keywords: [폴리머-산화물 복합 배터리, 황화물계 전고체, Sulfide ASSB, 고체 전해질, 에너지 밀도, 2029년 상용화, Solid Power, 대전 파일럿, 안전성 강화, 브리지 기술, 전고체배터리, 황화물계, 고체전해질, 에너지밀도, ASSB, 폴리머-산화물, 파일럿]
related: []
priority: normal
domain: D03
section: D03-03
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 1383
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03-03-NEXT. Next-Generation Product Master

## PROD-SKON-NEXT-001 — Polymer-Oxide Composite Battery

```yaml
entity_id: PROD-SKON-NEXT-001
entity_type: NEXT_GENERATION_BATTERY
official_name: Polymer-Oxide Composite Battery
company: SK On

electrolyte:
  type: POLYMER_OXIDE_COMPOSITE

classification:
  primary: SOLID_STATE_TRANSITION_TECHNOLOGY
  alternative: SEMI_SOLID_STATE
  note: Classification varies by definition

development_status: PILOT_DEVELOPMENT
commercial_status: NOT_COMMERCIAL

strategic_role:
  - Bridge between conventional lithium-ion and all-solid-state battery
  - Improvement of cell-level safety
  - Compatibility with existing manufacturing processes

technical_characteristics:
  polymer_function:
    - Flexibility
    - Improved ion transport
  oxide_function:
    - Thermal stability
    - Chemical stability

commercial_prototype_target:
  historical_target: 2028
  current_status: REQUIRES_FUTURE_VERIFICATION

evidence:
  - SRC-SKON-D03-024
  - Historical_Solid_State_Source

confidence:
  development: HIGH
  commercialization_date: MEDIUM_LOW
```

폴리머-산화물 복합 배터리는 기존 리튬이온 공정과의 호환성을 유지하면서 전해질의 고체 비중을 높여 안전성을 강화하려는 과도기적 기술이다. SK온은 이를 황화물계 완전 전고체로 가기 위한 브리지 제품으로 설명한다. ([ASK Inno][10])

---

## PROD-SKON-NEXT-002 — Sulfide-Based All-Solid-State Battery

```yaml
entity_id: PROD-SKON-NEXT-002
entity_type: NEXT_GENERATION_BATTERY
official_name: Sulfide-Based All-Solid-State Battery
abbreviation: Sulfide ASSB
company: SK On

electrolyte:
  type: SULFIDE_SOLID_ELECTROLYTE

commercial_status: R_AND_D
pilot_status:
  facility_location: Daejeon
  facility_size:
    value: 4628
    unit: square_meters
  establishment: 2025_H2

commercialization_target:
  year: 2029
  status: CORPORATE_TARGET_NOT_REALIZED_RESULT

energy_density_targets:
  initial:
    value: 800
    unit: Wh/L
  long_term:
    value: 1000
    unit: Wh/L

technology_partner:
  - Solid Power

expected_value:
  - Improved cell safety
  - High ionic conductivity
  - High energy density
  - Reduced liquid-electrolyte fire risk

critical_challenges:
  - Solid-solid interfacial resistance
  - Moisture sensitivity
  - Sulfide gas management
  - High-pressure cell operation
  - Manufacturing yield
  - Material cost
  - Large-cell scale-up

evidence:
  - SRC-SKON-D03-023
  - SRC-SKON-D03-024

confidence:
  development_program: HIGH
  pilot_facility: HIGH
  commercialization_target: MEDIUM
  final_performance: NOT_VALIDATED_PUBLICLY
```

SK온은 황화물계 전고체 배터리를 장기 차세대 제품으로 개발하고 있으며, 대전 파일럿 시설과 Solid Power 협력을 통해 셀 설계, 고체전해질 및 파일럿 생산공정을 검증하고 있다. 2029년과 800~1,000Wh/L은 목표값이며, 양산성과가 아니다. ([ASK Inno][9])

### D17 OI Metadata

```yaml
oi_metadata:
  priority: VERY_HIGH

  critical_needs:
    - Low-cost sulfide electrolyte manufacturing
    - Moisture-resistant material handling
    - Dry-room energy reduction
    - Solid-solid interface engineering
    - High-pressure stack management
    - Non-destructive defect inspection
    - Large-area solid-electrolyte coating
    - H2S detection and control

  potential_external_partners:
    - Solid electrolyte startup
    - Precision pressing equipment company
    - Dry-room technology company
    - X-ray or ultrasound inspection startup
    - University solid-state electrochemistry lab
    - Advanced simulation company

  poc_kpis:
    - Ionic conductivity
    - Interfacial resistance
    - Cycle retention
    - Defect density
    - Moisture exposure tolerance
    - Pilot-line yield
    - Cost per kWh
```

---

# D03-04. Product Architecture v1.0

```text
SK On Product Architecture
│
├── EV Battery Architecture
│   ├── Active Materials
│   ├── Electrode
│   ├── Cell
│   │   ├── Pouch Cell
│   │   ├── Prismatic Cell
│   │   └── Cylindrical Cell [Exploratory]
│   ├── Module
│   ├── Pack
│   ├── BMS
│   └── Vehicle Interface
│
├── ESS Architecture
│   ├── LFP Cell
│   ├── Module
│   ├── Rack
│   ├── DC Block Container
│   ├── AC Block
│   ├── BMS
│   ├── Thermal Management
│   ├── Fire Suppression
│   ├── PCS
│   └── EMS
│
├── BaaS Architecture
│   ├── Vehicle/Battery Data Collection
│   ├── Data Transmission
│   ├── BaaS AI
│   ├── SOH and RUL Estimation
│   ├── Risk Detection
│   ├── Residual Value Assessment
│   └── Reuse/Recycling Decision
│
└── Next-Generation Architecture
    ├── Polymer-Oxide Composite Cell
    ├── Sulfide ASSB
    ├── Solid Electrolyte
    ├── Lithium-Metal or Advanced Anode
    ├── High-Nickel/LMRO Cathode
    └── High-Pressure Cell Structure
```

---
