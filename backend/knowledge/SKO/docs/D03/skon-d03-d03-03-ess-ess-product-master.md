---
id: skon-d03-d03-03-ess-ess-product-master
title: ESS. ESS Product Master
summary: "SK온의 주력 ESS 솔루션 GRIDON의 1세대·2세대 제품 사양, 기술 특성, 상용화 계획을 담은 제품 마스터."
tags: [d03, product, schema, "xref:d17"]
keywords: [GRIDON, 그리드 규모 저장, LFP 배터리, 배터리 관리 시스템, 냉각액 침지, EIS, DC 블록, 유틸리티 저장소, AI 데이터 센터, 신재생 에너지, 배터리 관리, 전력 저장, 그리드 규모, 데이터센터, 열관리, 화재 안전, 냉각액 침지식]
related: [PROD-SKON-ESS-001]
priority: normal
domain: D03
section: D03-03
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 1515
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03-03-ESS. ESS Product Master

## PROD-SKON-ESS-002 — GRIDON Gen 1

```yaml
entity_id: PROD-SKON-ESS-002
entity_type: NAMED_ESS_SOLUTION
official_name: GRIDON
generation: GEN_1
company: SK On

product_role: FLAGSHIP_ESS_SOLUTION

commercial_status: COMMERCIAL_PRODUCTION_PLANNED
planned_production:
  region: United States
  year: 2026

target_markets:
  - Grid-Scale Storage
  - Renewable Energy Integration
  - AI Data Center
  - Industrial Facility
  - Utility

core_value_propositions:
  - Safety
  - Cost Efficiency
  - Operational Performance
  - Local Supply
  - Flexible System Architecture

core_components:
  - LFP Battery Cell
  - Battery Module
  - Rack
  - DC Block Container
  - Battery Management System
  - Thermal Management System
  - Fire Suppression System

diagnostic_system:
  technology: EIS-Based BMS
  function:
    - Real-Time Condition Analysis
    - Predictive Diagnosis

thermal_safety:
  technology: Coolant Immersion
  structure: Dual-Valve
  intended_function:
    - Early risk response
    - Heat control
    - Fire safety enhancement

evidence:
  - SRC-SKON-D03-017
  - SRC-SKON-D03-018
  - SRC-SKON-D03-002

confidence:
  product_existence: HIGH
  production_plan: HIGH
  detailed_capacity: NOT_DISCLOSED
```

GRIDON은 셀 단품이 아니라 진단·열관리·화재안전 및 컨테이너 구조를 묶은 ESS 솔루션 브랜드다. 따라서 D03에서는 `PRODUCT_SYSTEM`으로 관리하며, 개별 셀 사양은 별도 엔티티인 `PROD-SKON-ESS-001`과 연결한다. ([ASK Inno][3])

### 관계 그래프

```text
GRIDON Gen 1
├─ CONTAINS → LFP ESS Battery
├─ CONTAINS → ESS Module
├─ CONTAINS → ESS Rack
├─ CONTAINS → DC Block Container
├─ USES → EIS-Based BMS
├─ USES → Coolant Immersion
├─ TARGETS → Utility-Scale Storage
├─ TARGETS → AI Data Center
└─ PRODUCED_IN → United States
```

---

## PROD-SKON-ESS-003 — GRIDON Gen 2

```yaml
entity_id: PROD-SKON-ESS-003
entity_type: NEXT_GENERATION_ESS_SOLUTION
official_name: GRIDON Gen 2
company: SK On

development_status: UNDER_DEVELOPMENT
commercial_status: PRE_COMMERCIAL

target_commercial_production:
  year: 2027
  quarter: Q3
  status: OFFICIAL_TARGET

supported_architectures:
  - DC Block
  - AC Block

performance_improvement:
  energy_capacity_per_dc_container:
    improvement: average_15_percent
    benchmark: previous_generation

safety_features:
  - Electrochemical Impedance Spectroscopy
  - Coolant-Based Fire Suppression

target_applications:
  - Grid-Scale ESS
  - AI Data Center
  - Large Load Facility
  - Renewable Energy Project

evidence:
  - SRC-SKON-D03-018

confidence:
  development_program: HIGH
  production_target: HIGH
  eventual_mass_production: NOT_YET_VERIFIED
```

GRIDON Gen 2는 DC 블록과 AC 블록을 모두 지원하고, 컨테이너당 에너지용량을 평균 15% 높이도록 설계된 차세대 ESS 솔루션이다. 2027년 3분기 상업생산은 현재 시점의 공식 목표이지 이미 확정된 생산실적은 아니다. ([ASK Inno][4])

### D17 OI Metadata

```yaml
oi_metadata:
  priority: VERY_HIGH

  pain_points:
    - Higher container energy density
    - Thermal propagation between racks
    - Accurate EIS measurement under operating load
    - PCS and EMS interoperability
    - Long-term warranty risk
    - Site-level fire code compliance

  external_capability_needs:
    - Online EIS estimation
    - Container digital twin
    - AI dispatch optimization
    - Immersion coolant monitoring
    - Early off-gas detection
    - AC-block control software
    - Bankability and warranty analytics

  potential_poc_kpis:
    - Energy capacity per container
    - Round-trip efficiency
    - Availability
    - Thermal alarm lead time
    - False-positive fire alarm rate
    - Cell imbalance rate
    - Maintenance cost per MWh
```

---

## PROD-SKON-ESS-004 — ESS DC Block

```yaml
entity_id: PROD-SKON-ESS-004
entity_type: ESS_SYSTEM_COMPONENT
official_name: DC Block
company_relation: SK On GRIDON

system_boundary:
  included:
    - Battery Cells
    - Modules
    - Racks
    - Container
    - BMS
    - Thermal Management
  typically_excluded:
    - External PCS
    - Grid Interconnection Equipment

commercial_relation:
  gridon_gen_1: SUPPORTED
  gridon_gen_2: SUPPORTED

evidence:
  - SRC-SKON-D03-018

confidence: HIGH
```

---

## PROD-SKON-ESS-005 — ESS AC Block Configuration

```yaml
entity_id: PROD-SKON-ESS-005
entity_type: ESS_SYSTEM_CONFIGURATION
official_name: AC Block-Compatible GRIDON Configuration
company: SK On

development_relation:
  product: GRIDON Gen 2

system_boundary:
  battery_dc_block: INCLUDED
  power_conversion_system: INTEGRATED_OR_CO_CONFIGURED
  energy_management_interface: REQUIRED

commercial_status: UNDER_DEVELOPMENT
target_production: 2027_Q3

evidence:
  - SRC-SKON-D03-018

confidence:
  architecture_support: HIGH
  exact_pcs_vendor: NOT_DISCLOSED
  exact_ems_vendor: NOT_DISCLOSED
```

SK온은 ESS 시장이 기존 DC 블록 중심에서 PCS가 통합된 AC 블록 방향으로 이동하고 있다고 판단하고, GRIDON Gen 2를 두 구조 모두에 대응하도록 개발하고 있다. PCS 및 EMS의 구체적 공급사나 자체개발 범위는 공개되지 않았다. ([ASK Inno][4])

---
