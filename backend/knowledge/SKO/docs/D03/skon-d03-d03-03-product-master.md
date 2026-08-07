---
id: skon-d03-d03-03-product-master
title: Product Master
summary: "SK온의 고에너지밀도 하이니켈 파우치 배터리와 NCM9+ 기술의 사양, 응용 분야, 기술적 과제"
tags: [d03, product, schema, "xref:d17"]
keywords: [고니켈 배터리, NCM9+, 파우치 셀, 에너지밀도, 급속충전, 열안정성, 니켈 함량, EV 배터리, 배터리 화학, 열화 관리, 하이니켈, 파우치, 전기차 배터리, SF Battery]
related: []
priority: normal
domain: D03
section: D03-03.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 3082
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03-03. Product Master

## PROD-SKON-EV-001 — High-Nickel Pouch Battery Family

```yaml
entity_id: PROD-SKON-EV-001
entity_type: PRODUCT_FAMILY
official_name: High-Nickel Pouch Battery
company: SK On

portfolio:
  level_1: EV Battery
  level_2: Lithium-ion Battery
  level_3: High-Nickel Battery
  level_4: Pouch Cell

commercial_status: COMMERCIAL
product_role: CORE_PRODUCT_FAMILY

chemistry:
  cathode_family: NCM
  nickel_class: HIGH_NICKEL
  specific_variants:
    - NCM9+
    - SF Battery

form_factor:
  primary: POUCH
  evidence_status: CONFIRMED

target_applications:
  - Battery Electric Vehicle
  - Long-range EV
  - Fast-charging EV
  - Performance-oriented EV

core_value_propositions:
  - High energy density
  - Driving-range improvement
  - Fast charging
  - Safety performance
  - Long battery life

related_products:
  - PROD-SKON-EV-002
  - PROD-SKON-EV-003

related_technologies:
  - TECH-HIGH-NICKEL-CATHODE
  - TECH-FAST-CHARGING
  - TECH-SEPARATOR-FOLDING
  - TECH-THERMAL-SAFETY
  - TECH-BMS

evidence:
  - SRC-SKON-D03-004
  - SRC-SKON-D03-005
  - SRC-SKON-D03-006
  - SRC-SKON-D03-008

confidence:
  overall: HIGH
  grade: A+
```

### Human-readable description

SK온의 핵심 상용 제품군은 하이니켈 NCM 계열의 파우치형 전기차 배터리다. 공식 자료는 SK온이 고에너지밀도와 안전성, 급속충전 및 수명을 주요 경쟁요소로 개발해 왔음을 보여준다. NCM9+와 SF Battery는 이 제품군을 대표하는 공개 제품 또는 기술 브랜드다. ([SK Innovation][6])

### 사실·분석 구분

**FACT**

* SK온은 NCM 계열 하이니켈 배터리를 상용 공급해 왔다.
* 파우치형이 기존 주력 폼팩터다.
* NCM9+와 SF Battery가 공식 자료에 공개됐다.

**ANALYSIS**

하이니켈 파우치 제품은 높은 에너지밀도와 긴 주행거리를 요구하는 EV 시장에서 차별성이 있지만, 니켈 원재료 가격, 열안정성, 제조수율 및 급속충전 시 열화 관리가 동시에 요구되는 제품군이다.

**D17 연결 후보**

```text
High-Nickel Pouch Battery
→ NEEDS
  ├─ Thermal runaway prevention
  ├─ Low-cost high-nickel cathode
  ├─ Silicon-anode stabilization
  ├─ Fast-charge electrolyte
  ├─ AI degradation prediction
  └─ High-speed inline defect inspection
```

---

## PROD-SKON-EV-002 — NCM9+ Battery

```yaml
entity_id: PROD-SKON-EV-002
entity_type: BATTERY_PRODUCT_TECHNOLOGY
official_name: NCM9+
aliases:
  - NCM 9 Plus
  - Nickel 90%+ Battery

parent_product:
  - PROD-SKON-EV-001

chemistry:
  cathode: NCM
  nickel_content:
    threshold: greater_than_90_percent
    status: OFFICIAL_CONFIRMED

form_factor: POUCH
commercial_status: COMMERCIAL_TECHNOLOGY
product_generation: ADVANCED_HIGH_NICKEL

primary_value:
  - High energy density
  - Extended driving range
  - Reduced cobalt dependency relative to lower-nickel NCM formulations

key_risks:
  - Thermal stability
  - Cathode structural degradation
  - Gas generation
  - Electrolyte oxidation
  - Manufacturing consistency
  - Raw-material price exposure

evidence:
  - SRC-SKON-D03-006

confidence:
  grade: A+
  product_existence: HIGH
  detailed_specification: LIMITED
```

SK이노베이션 공식 ESG 자료는 SK온이 니켈 함량 90%를 초과하는 NCM9+ 배터리를 개발했다고 명시한다. 다만 해당 공개자료만으로는 용량, 전압, 중량, 에너지밀도 또는 개별 고객별 사양을 확정할 수 없다. ([SK Innovation][6])

### 데이터 제한

```yaml
cell_capacity_ah: NOT_DISCLOSED
gravimetric_energy_density_whkg: NOT_DISCLOSED
volumetric_energy_density_whl: NOT_DISCLOSED
cycle_life: NOT_DISCLOSED
vehicle_customer_mapping: REQUIRES_CONTRACT_LEVEL_EVIDENCE
```

---

## PROD-SKON-EV-003 — SF Battery

```yaml
entity_id: PROD-SKON-EV-003
entity_type: NAMED_BATTERY_PRODUCT
official_name: SF Battery
expanded_name: Super Fast Battery
company: SK On

parent_product:
  - PROD-SKON-EV-001

chemistry:
  family: NCM
  nickel_content:
    value: 83
    unit: percent
    evidence_level: SECONDARY_CROSS_VALIDATED

form_factor: POUCH

commercial_status: COMMERCIAL
recognition:
  event: CES 2023
  award: Best of Innovation
  category: Vehicle Tech and Advanced Mobility

performance:
  charge:
    target_soc: 80
    unit: percent
    duration: 18
    duration_unit: minutes
  driving_range:
    value: 400+
    unit: km
    condition: VEHICLE_DEPENDENT

development_history:
  fast_charge_task_force_start: 2016

target_application:
  - Fast-charging EV
  - Long-distance EV
  - Premium EV

evidence:
  - SRC-SKON-D03-004
  - SRC-SKON-D03-005
  - SRC-SKON-D03-011

confidence:
  grade: A+
  charging_claim: HIGH
  nickel_content: MEDIUM_HIGH
  driving_range: MEDIUM
```

SF Battery는 18분 내 80% 충전을 핵심 가치로 내세운 하이니켈 EV 배터리다. 공식 SK 자료는 해당 제품의 개발 배경과 급속충전 성능을 확인해 주며, 연합뉴스 자료는 니켈 함량 83%와 400km 이상의 주행거리 정보를 보완한다. ([SK][4])

### 제품 관계

```text
SF Battery
├─ IS_A → High-Nickel Pouch Battery
├─ USES → NCM Cathode
├─ OPTIMIZED_FOR → Fast Charging
├─ TARGETS → EV Market
├─ HAS_PAIN_POINT → Fast-charge Degradation
├─ HAS_PAIN_POINT → Heat Generation
├─ REQUIRES → Thermal Management
└─ REQUIRES → Fast-charge Electrolyte
```

### OI Metadata

```yaml
oi_metadata:
  priority: HIGH
  opportunity_topics:
    - Fast-charge electrolyte additives
    - Lithium plating detection
    - High-silicon anode stabilization
    - Cell-level thermal sensing
    - AI charging protocol optimization
    - Ultra-fast formation process
  partner_types:
    - Battery-material startup
    - Electrolyte company
    - AI battery analytics startup
    - University electrochemistry laboratory
    - Thermal-management company
```

---

## PROD-SKON-ESS-001 — LFP ESS Battery

```yaml
entity_id: PROD-SKON-ESS-001
entity_type: BATTERY_PRODUCT
official_name: LFP Battery for Energy Storage Systems
company: SK On

portfolio:
  level_1: ESS Battery
  level_2: Lithium-ion Battery
  level_3: LFP Battery

chemistry:
  cathode: Lithium Iron Phosphate
  abbreviation: LFP

commercial_status: CONTRACTED_FOR_MASS_PRODUCTION
planned_mass_production:
  period: 2026_H2
  geography: United States
  facility_relation:
    - SK Battery America
    - Commerce Georgia

initial_project:
  customer: Flatiron Energy Development
  location: Massachusetts
  volume:
    value: 1
    unit: GWh

potential_supply_framework:
  maximum_volume:
    value: 7.2
    unit: GWh
  period:
    start: 2026
    end: 2030

product_configuration:
  - LFP cell
  - ESS module
  - rack
  - containerized BESS

target_application:
  - Utility-scale energy storage
  - Renewable energy integration
  - Grid balancing
  - Peak management
  - Capacity support

evidence:
  - SRC-SKON-D03-002
  - SRC-SKON-D03-003
  - SRC-SKON-D03-014

confidence:
  grade: A+
  supply_contract: HIGH
  production_schedule: HIGH
  detailed_cell_specification: NOT_DISCLOSED
```

SK온의 LFP ESS 제품은 단순 연구단계가 아니라 공급계약과 양산계획이 확인된 제품이다. 1GWh 규모의 초기 프로젝트와 최대 7.2GWh의 공급 가능 구조가 공개됐으며, 미국 EV 배터리 라인의 일부를 ESS 제품 생산에 활용할 예정이다. ([SK On][2])

### Fact / Analysis

**FACT**

* LFP 기반 ESS 제품 공급계약 체결
* 초기 확정 프로젝트 1GWh
* 최대 7.2GWh 공급 가능
* 2026년 하반기 양산계획
* 미국 조지아 생산라인 활용계획

**ANALYSIS**

EV용 라인을 ESS용으로 전환하는 방식은 신규 공장 건설보다 투자부담과 시장진입 시간을 줄일 수 있다. 반면 EV 제품과 ESS 제품은 사용 프로파일, 수명요건, 열관리, 랙 구성 및 시스템 인증이 다르므로 단순한 셀 전환만으로 완성되지 않는다.

### D17 연결 후보

```text
LFP ESS Battery
→ OPEN_INNOVATION_NEEDS
  ├─ Long-duration degradation prediction
  ├─ Thermal propagation prevention
  ├─ Rack-level fire suppression
  ├─ AI dispatch optimization
  ├─ Cell imbalance diagnosis
  ├─ Low-cost LFP cathode materials
  ├─ Container energy-density improvement
  └─ ESS lifecycle and warranty analytics
```

---

## SERV-SKON-BAAS-001 — Battery Diagnosis Service

```yaml
entity_id: SERV-SKON-BAAS-001
entity_type: DIGITAL_BATTERY_SERVICE
official_name: Battery Diagnosis Service
company: SK On

parent_portfolio:
  - BaaS
  - Battery Lifecycle Service

service_functions:
  - Battery-status data collection
  - Battery-condition analysis
  - Abnormality detection
  - State-of-health assessment
  - Residual-value estimation

core_engine:
  name: BaaS AI
  ownership: SK On developed
  evidence_status: OFFICIAL_CONFIRMED

initial_customer_context:
  - Electric vehicle owner
  - Used EV market
  - Vehicle inspection
  - Battery reuse decision

historical_service_status:
  reference_year: 2021
  status: PILOT

current_commercial_scale:
  status: NOT_FULLY_DISCLOSED

evidence:
  - SRC-SKON-D03-001
  - SRC-SKON-D03-009
  - SRC-SKON-D03-010

confidence:
  technology_existence: HIGH
  current_scale: LOW
```

SK온은 BaaS AI를 활용해 전기차 배터리 상태를 수집하고 이상 여부 및 잔존가치를 분석하는 진단 서비스를 개발했다. 2021년 공개 당시 서비스는 시범사업 성격이었으며, 현재의 고객 수, 유료화 범위 및 매출 규모는 공개자료만으로 확정하기 어렵다. ([ASK Inno][9])

### 서비스 관계

```text
Battery Diagnosis Service
├─ IS_PART_OF → BaaS
├─ USES → BaaS AI
├─ ANALYZES → Battery Condition
├─ ESTIMATES → State of Health
├─ ESTIMATES → Residual Value
├─ SUPPORTS → Used EV Transaction
├─ SUPPORTS → Battery Reuse
├─ SUPPORTS → Battery Recycling
└─ REQUIRES → Standardized Battery Data
```

### OI Metadata

```yaml
oi_metadata:
  priority: HIGH
  missing_capabilities:
    - Cross-OEM battery data standardization
    - Explainable SOH estimation
    - Sparse-data degradation prediction
    - Tamper-proof battery history
    - Real-world fast diagnosis
  potential_external_technologies:
    - Physics-informed machine learning
    - Edge battery analytics
    - Digital battery passport
    - Cloud-based fleet analytics
    - Electrochemical impedance estimation
```

---
