---
id: skon-d03-d03-03-product-master-확장
title: Product Master 확장
summary: "SK온의 Advanced SF, SF+ 배터리 제품의 기술사양, 성능지표, 자기정렬 공정, 적용차량, 협력파트너 요구사항을 정의한 제품정보 문서"
tags: [d03, product, schema, "xref:d17"]
keywords: [에너지밀도, 급속충전, 자기정렬공정, 고니켈, 포우치, IONIQ 9, 음극재, 배터리기술협력, 리튬이온, 성능명세, Advanced SF, SF+ Battery, Magnetic Alignment, 자기정렬 공정, 고니켈 배터리, 리튬도금, 제조협력]
related: [PRE-COMMERCIAL]
priority: normal
domain: D03
section: D03-03.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 3586
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03-03. Product Master 확장

## PROD-SKON-EV-004 — Advanced SF Battery

```yaml
entity_id: PROD-SKON-EV-004
entity_type: NAMED_BATTERY_PRODUCT
official_name: Advanced SF Battery
company: SK On

parent_product:
  - PROD-SKON-EV-001
  - PROD-SKON-EV-003

product_family:
  - High-Nickel EV Battery
  - Fast-Charging Battery
  - Pouch Battery

commercial_status: COMMERCIAL_APPLICATION_CONFIRMED

vehicle_application:
  confirmed_vehicle:
    - Hyundai IONIQ 9
  evidence_status: OFFICIAL_EXHIBITION_DISCLOSURE

performance:
  fast_charge:
    start_soc: 10
    end_soc: 80
    time: 18
    unit: minutes

  energy_density_improvement:
    canonical_value: 8
    unit: percent
    benchmark: Original SF Battery
    initial_disclosure: approximately_9_percent

enabling_technology:
  - Magnetic Alignment Process
  - Graphite Particle Orientation
  - Reduced Lithium-Ion Transport Path

value_proposition:
  - Higher energy density than original SF Battery
  - Retention of 18-minute fast charging
  - Longer vehicle range potential
  - High-capacity premium EV application

evidence:
  - SRC-SKON-D03-015
  - SRC-SKON-D03-016

confidence:
  product_existence: HIGH
  charging_performance: HIGH
  energy_density_improvement: HIGH
  full_cell_specification: NOT_DISCLOSED
```

Advanced SF는 기존 SF의 18분 급속충전 성능을 유지하면서 에너지밀도를 높인 후속 제품이다. 음극재 내 흑연 입자를 수직 방향으로 정렬해 리튬이온 이동거리를 단축하는 자기정렬 공정이 핵심 기술로 제시된다. ([ASK Inno][1])

### 관계 그래프

```text
Advanced SF Battery
├─ EVOLVED_FROM → SF Battery
├─ USES → Magnetic Alignment Process
├─ IMPROVES → Volumetric Energy Density
├─ RETAINS → 18-Minute Fast Charging
├─ APPLIED_TO → Hyundai IONIQ 9
├─ HAS_RISK → Lithium Plating
├─ HAS_RISK → Fast-Charge Heat Generation
└─ NEEDS → High-Speed Electrode Alignment Control
```

### D17 OI Metadata

```yaml
oi_metadata:
  priority: HIGH

  pain_points:
    - Magnetic particle alignment uniformity
    - High-speed roll-to-roll process compatibility
    - Fast-charge thermal load
    - Silicon/graphite volume expansion
    - Cell-to-cell performance dispersion

  external_capability_needs:
    - Inline magnetic alignment measurement
    - AI electrode microstructure control
    - Fast-charge lithium plating sensor
    - High-throughput anode inspection
    - Physics-informed charging algorithm

  potential_partner_types:
    - Magnetic processing equipment company
    - Machine-vision startup
    - Battery analytics startup
    - Advanced anode material company
    - University electrochemistry laboratory
```

---

## PROD-SKON-EV-005 — SF+ Battery

```yaml
entity_id: PROD-SKON-EV-005
entity_type: NAMED_BATTERY_PRODUCT
official_name: SF+ Battery
company: SK On

parent_product:
  - PROD-SKON-EV-003

product_family:
  - Fast-Charging EV Battery
  - High-Nickel Battery
  - Pouch Battery

public_introduction_year: 2024

commercial_status: PRODUCT_TECHNOLOGY_DISCLOSED
customer_application_status: NOT_SPECIFICALLY_DISCLOSED

performance:
  fast_charge:
    start_soc: 10
    end_soc: 80
    time: 15
    unit: minutes

anode_architecture:
  structure: DUAL_LAYER
  materials:
    - High-Capacity Silicon
    - Low-Resistance Graphite

technical_mechanism:
  - Shortened lithium-ion transport distance
  - Increased lithium-ion transport speed
  - Reduced charging resistance

evidence:
  - SRC-SKON-D03-015

confidence:
  product_existence: HIGH
  charging_claim: HIGH
  customer_application: UNCONFIRMED
  commercial_volume: NOT_DISCLOSED
```

SF+는 고용량 실리콘과 저저항 흑연을 결합한 이중층 음극 구조를 적용해 10%에서 80%까지의 충전시간을 15분으로 단축한 제품이다. 현재 공개자료만으로는 구체적인 적용 차량, 생산공장 및 출하량을 확정할 수 없다. ([ASK Inno][1])

```text
SF+ Battery
├─ EVOLVED_FROM → SF Battery
├─ USES → High-Capacity Silicon
├─ USES → Low-Resistance Graphite
├─ HAS_STRUCTURE → Dual-Layer Anode
├─ ENABLES → 15-Minute Fast Charging
└─ REQUIRES → Silicon Expansion Control
```

---

## PROD-SKON-EV-006 — Hyper Fast Battery

```yaml
entity_id: PROD-SKON-EV-006
entity_type: ADVANCED_BATTERY_PROTOTYPE
official_name: Hyper Fast Battery
company: SK On

public_introduction:
  event: InterBattery 2026
  year: 2026

product_family:
  - Ultra-Fast-Charging EV Battery
  - Advanced Lithium-Ion Battery

commercial_status: TECHNOLOGY_DEMONSTRATION
mass_production_status: NOT_CONFIRMED
customer_contract_status: NOT_CONFIRMED

performance_target:
  fast_charge:
    start_soc: 10
    end_soc: 80
    time: less_than_7
    unit: minutes

  energy_density:
    value: 650
    unit: Wh/L
    type: volumetric

  claimed_range:
    seven_minute_charge:
      value: greater_than_450
      unit: km
    three_minute_charge:
      additional_range: approximately_200
      unit: km
    qualification: VEHICLE_AND_TEST_CONDITION_DEPENDENT

enabling_technologies:
  - SUFast
  - Simulation-Based Charging Protocol Optimization
  - Integrated Electrode and Charging Design

evidence:
  - SRC-SKON-D03-015

confidence:
  prototype_existence: HIGH
  disclosed_performance: HIGH
  mass_production: UNCONFIRMED
```

Hyper Fast Battery는 2026년 공개된 기술 시제품으로, 상용 양산제품으로 확정해서는 안 된다. SK온은 전극설계와 충전 프로토콜을 함께 최적화해 650Wh/L의 에너지밀도와 7분 미만의 급속충전을 동시에 구현했다고 설명한다. ([ASK Inno][1])

### OI Metadata

```yaml
oi_metadata:
  priority: VERY_HIGH

  critical_pain_points:
    - Lithium plating under extreme C-rate
    - Rapid temperature rise
    - Electrolyte decomposition
    - Silicon-anode swelling
    - Cycle-life degradation
    - Charger-grid compatibility

  required_external_capabilities:
    - Operando lithium plating detection
    - Ultra-fast thermal sensing
    - Adaptive charging control
    - Electrolyte additive screening
    - Physics-based degradation model
    - High-power charging infrastructure optimization

  expected_kpi_candidates:
    - Charge time
    - Lithium plating incidence
    - Cycle retention
    - Peak cell temperature
    - Cell-to-cell temperature deviation
    - Energy throughput before end-of-life
```

---

## PROD-SKON-EV-007 — LFP EV Battery Platform

```yaml
entity_id: PROD-SKON-EV-007
entity_type: BATTERY_PRODUCT_PLATFORM
official_name: LFP Battery for Electric Vehicles
company: SK On

chemistry:
  cathode: Lithium Iron Phosphate

target_application:
  - Affordable EV
  - Standard-range EV
  - Cost-sensitive vehicle segment

development_status: TECHNOLOGY_READY_REPORTED
commercial_status: NOT_CONFIRMED_AS_MASS_PRODUCED_EV_PRODUCT
customer_status: OEM_DISCUSSIONS_REPORTED

historical_timeline:
  2024_disclosure:
    possible_mass_production:
      - 2026
      - 2027
    target_regions_discussed:
      - Europe
      - China

current_verified_status:
  ev_mass_production: NOT_FOUND_IN_REVIEWED_OFFICIAL_SOURCES
  ess_mass_production: CONFIRMED_SEPARATELY

evidence:
  - SRC-SKON-D03-014
  - Reuters_LFP_2024

confidence:
  development: HIGH
  ev_commercialization: LOW
```

2024년 SK온 경영진은 EV용 LFP 기술개발을 완료하고 OEM과 공급을 논의 중이며, 협의 결과에 따라 2026~2027년 양산할 수 있다고 밝혔다. 그러나 이번 검토 범위에서 확인된 확정 양산계약은 ESS용 LFP이며, EV용 LFP의 실제 양산개시 또는 고객계약은 별도로 확인되지 않았다. 따라서 EV용 LFP는 `PRE-COMMERCIAL`로 관리한다. ([Reuters][13])

---

## PROD-SKON-EV-008 — Pouch-Integrated Prismatic Cell

```yaml
entity_id: PROD-SKON-EV-008
entity_type: BATTERY_CELL_CONCEPT
official_name: Pouch-Integrated Prismatic Cell
company: SK On

form_factor:
  outer_structure: PRISMATIC
  internal_cell_concept: POUCH_INTEGRATED

commercial_status: EXHIBITION_PROTOTYPE
public_introduction:
  event: InterBattery 2026

strategic_purpose:
  - Diversification beyond conventional pouch format
  - Combination of pouch-cell experience with rigid enclosure
  - Response to OEM form-factor requirements

technical_specification:
  capacity: NOT_DISCLOSED
  chemistry: NOT_DISCLOSED
  dimensions: NOT_DISCLOSED
  energy_density: NOT_DISCLOSED

evidence:
  - SRC-SKON-D03-025

confidence:
  prototype_existence: HIGH
  commercial_readiness: UNKNOWN
```

이 제품은 SK온의 파우치 설계·생산 경험을 각형 외장구조와 결합하려는 개념으로 해석할 수 있다. 다만 실제 셀 구조, 모듈 통합방식 및 고객 적용 여부는 공식 자료에서 공개되지 않았다. ([ASK Inno][11])

---

## PROD-SKON-EV-009 — On-Vent Prismatic Cell

```yaml
entity_id: PROD-SKON-EV-009
entity_type: BATTERY_CELL_CONCEPT
official_name: On-Vent Prismatic Cell
company: SK On

form_factor: PRISMATIC
commercial_status: EXHIBITION_PROTOTYPE

core_feature:
  name: Configurable Vent Position
  enabling_process: Laser Engraving
  intended_function:
    - Controlled gas discharge
    - Controlled heat discharge
    - Greater cell and pack design flexibility

public_introduction:
  event: InterBattery 2026

evidence:
  - SRC-SKON-D03-025

confidence:
  prototype_existence: HIGH
  safety_performance_validation: NOT_PUBLICLY_DISCLOSED
  mass_production: UNCONFIRMED
```

On-Vent 각형 셀은 벤트 위치를 제품 설계에 맞춰 설정할 수 있도록 한 구조다. 이는 열폭주 발생 시 가스와 열의 배출방향을 제어하는 팩 안전설계와 연결될 가능성이 있으나, 실제 열폭주 시험결과와 양산 적용 여부는 공개되지 않았다. ([ASK Inno][11])

### D17 OI Metadata

```yaml
oi_metadata:
  priority: HIGH

  opportunity_topics:
    - Directional gas vent simulation
    - Vent opening pressure optimization
    - Laser engraving quality inspection
    - Gas composition sensing
    - Pack-level vent channel design
    - Thermal propagation CFD

  partner_types:
    - Laser processing company
    - CAE/CFD software startup
    - Gas sensor startup
    - Battery safety testing institution
    - Advanced sealing-material company
```

---

## PROD-SKON-EV-010 — Prismatic Battery Platform

```yaml
entity_id: PROD-SKON-EV-010
entity_type: FORM_FACTOR_PLATFORM
official_name: Prismatic Battery Platform
company: SK On

form_factor: PRISMATIC
technology_status: DEVELOPMENT_CONFIRMED
commercial_status: PRE_COMMERCIAL

historical_status:
  2024:
    technology_completed_reported: true
    customer_discussions_reported: true

latest_public_evidence:
  2026:
    prototypes_disclosed:
      - Pouch-Integrated Prismatic Cell
      - On-Vent Prismatic Cell

customer_contract:
  status: NOT_PUBLICLY_CONFIRMED

evidence:
  - SRC-SKON-D03-025
  - SRC-SKON-D03-026

confidence:
  technology_program: HIGH
  mass_production: UNCONFIRMED
```

2024년 각형 기술개발 완료 및 OEM 협의 사실이 보도됐고, 2026년에는 두 종류의 각형 시제품이 공식 전시됐다. 따라서 각형 플랫폼은 단순 검토단계보다 진전된 개발상태로 평가할 수 있지만, 양산제품으로 분류할 근거는 아직 부족하다. ([Reuters][12])

---

## PROD-SKON-EV-011 — Cylindrical Battery Platform

```yaml
entity_id: PROD-SKON-EV-011
entity_type: FORM_FACTOR_PLATFORM
official_name: Cylindrical Battery Platform
company: SK On

form_factor: CYLINDRICAL
development_status: EXPLORATORY_REPORTED
commercial_status: NOT_CONFIRMED

disclosed_dimensions:
  18650: NOT_CONFIRMED
  2170: NOT_CONFIRMED
  4680: NOT_CONFIRMED

customer_contract: NOT_CONFIRMED
pilot_line: NOT_CONFIRMED
public_prototype: NOT_FOUND

evidence:
  - SRC-SKON-D03-026

confidence:
  exploration: MEDIUM_HIGH
  active_development: UNKNOWN
  commercialization: LOW
```

원통형 배터리는 2024년 당시 개발을 검토하는 단계로 언급됐다. 이후 검토한 공식 공개자료에서는 특정 규격, 시제품, 고객계약 또는 양산계획을 확인하지 못했으므로, D03에서는 제품이 아니라 `탐색형 플랫폼`으로만 등록한다. ([Reuters][12])

---
