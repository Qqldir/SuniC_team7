---
id: skon-d04-d04-047-d04-047-wet-mixing-slurry-intelligence-o
title: D04-047 — Wet Mixing & Slurry Intelligence — OI Metadata
summary: "습식 혼합과 슬러리 지능화 기술의 개발 현황, 필요 외부 역량, 성과지표와 관련 건식·습식 전극 코팅 기술의 기술 분류 및 주요 도전과제를 정의한 메타데이터."
tags: [d04, technology, schema]
keywords: [슬러리 점도, 건식 분말, 전극 코팅, 전극 형성, 도전재 분산, 롤투롤 제조, 슬롯다이, 코팅 결함, 분말 응집, 바인더 기술, 습식혼합, 슬러리 지능화, 건식전극, 분말혼합, 전극코팅, 점도, 응집체, 코팅균일성, 용매없는제조]
related: []
priority: normal
domain: D04
section: D04-047
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Manufacturing Technology Master > D04-047 — Wet Mixing & Slurry Intelligence
tokens: 2047
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Manufacturing Technology Master > D04-047 — Wet Mixing & Slurry Intelligence

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: HIGH

  external_capability_needs:
    - Inline rheology measurement
    - Acoustic dispersion monitoring
    - AI formulation recommendation
    - Contamination particle sensing
    - Automated material dosing
    - Slurry digital twin

  poc_kpis:
    - Viscosity deviation
    - Agglomerate count
    - Coating defect density
    - Mixing time
    - Energy consumption
    - Lot-to-lot variation
```

---

## TECH-SKON-D04-048 — Dry Powder Mixing

```yaml
technology_id: TECH-SKON-D04-048
canonical_name: Dry Powder Mixing
korean_name: 건식 분말 혼합기술

technology_category:
  - Dry Electrode
  - Powder Processing
  - Solvent-Free Manufacturing

technology_status: DEVELOPMENT
mass_production_status: NOT_CONFIRMED

input_materials:
  - Active material
  - Conductive additive
  - Dry binder

primary_functions:
  - Uniform powder distribution
  - Conductive-network preparation
  - Binder fibrillation or activation
  - Stable feeding into coating process

critical_process_parameters:
  - Powder particle size
  - Mixing energy
  - Mixing time
  - Temperature
  - Humidity
  - Binder distribution
  - Electrostatic charge
  - Powder flowability

critical_quality_attributes:
  - Composition uniformity
  - Stable powder flow
  - Low segregation
  - Controlled binder network
  - Consistent bulk density

principal_challenges:
  - Powder segregation
  - Dust generation
  - Electrostatic accumulation
  - Binder agglomeration
  - Inconsistent fibrillation
  - Continuous feeding stability
  - Contamination control

related_technology:
  - TECH-SKON-D04-003 Dry Electrode Process
  - TECH-SKON-D04-039 AI Calendering

source_ids:
  - SRC-SKON-D04-035

confidence:
  program: VERY_HIGH
  detailed_method: NOT_DISCLOSED
```

SK온의 건식전극은 용매 없이 활물질·도전재·바인더를 혼합해 분말층을 형성하는 방식이다. 공식 자료에는 SK온이 복수의 건식 코팅방식을 개발하고 있다는 사실은 공개됐지만, 바인더 종류와 분말혼합 장비·조건은 공개되지 않았다. ([ASK Inno][1])

---

## TECH-SKON-D04-049 — Wet Electrode Coating

```yaml
technology_id: TECH-SKON-D04-049
canonical_name: Wet Electrode Coating
korean_name: 습식 전극 코팅

technology_category:
  - Roll-to-Roll Manufacturing
  - Electrode Formation
  - Slot-Die Coating

technology_status: COMMERCIAL_INDUSTRY_BASELINE
sk_on_use: CONFIRMED_AT_GENERAL_TECHNOLOGY_LEVEL
sk_on_equipment_specification: NOT_DISCLOSED

technical_mechanism:
  - Feed slurry to precision coating head
  - Apply slurry onto metal current collector
  - Control coating width and loading
  - Transport coated foil through drying zone

critical_process_parameters:
  - Slurry flow rate
  - Web speed
  - Coating gap
  - Slurry viscosity
  - Foil tension
  - Edge position
  - Coating temperature

critical_quality_attributes:
  - Areal loading
  - Thickness uniformity
  - Edge quality
  - Surface smoothness
  - Adhesion
  - Absence of streaks and pinholes

defect_modes:
  - Coating streak
  - Edge bead
  - Pin hole
  - Agglomerate mark
  - Thickness variation
  - Foil wrinkle
  - Delamination

source_ids:
  - SRC-SKON-D04-035
  - SRC-SKON-D04-039
  - SRC-SKON-D04-041

confidence:
  process_use: VERY_HIGH
  sk_on_line_parameters: NOT_DISCLOSED
```

습식 코팅은 슬러리를 알루미늄 또는 구리 집전체에 일정한 두께로 연속 도포하는 공정이다. 코팅두께가 증가하면 제거해야 할 용매량과 필요한 건조시간이 증가해 설비길이와 생산속도에 영향을 줄 수 있다. Argonne의 공개 비용모델도 전극 두께와 용매부하가 코팅·건조설비 조건에 영향을 주는 것으로 처리한다. ([ASK Inno][7])

---

## TECH-SKON-D04-050 — Dual-Layer Coating

```yaml
technology_id: TECH-SKON-D04-050
canonical_name: Dual-Layer Electrode Coating
korean_name: 이중층 전극 코팅

technology_category:
  - Advanced Coating
  - Electrode Architecture
  - Fast Charging

technology_status: PRODUCT_TECHNOLOGY_DISCLOSED

related_products:
  - SF+ Battery
  - Hyper Fast Battery

technical_objective:
  - Assign different functions to separate electrode layers
  - Balance high capacity and low resistance
  - Control ion transport by depth
  - Improve fast-charging performance

process_requirements:
  - Two slurry formulations or functional layers
  - Controlled layer thickness
  - Stable interlayer adhesion
  - Synchronized coating
  - Drying compatibility
  - Uniform cross-web distribution

defect_modes:
  - Layer-interface delamination
  - Unequal shrinkage
  - Composition mixing
  - Current-density nonuniformity
  - Differential swelling
  - Layer-thickness variation

source_ids:
  - SRC-SKON-D04-007
  - SRC-SKON-D04-033

confidence:
  technology_exist: VERY_HIGH
  detailed_equipment_configuration: NOT_DISCLOSED
```

SK온은 SF+와 SUFast 계열에서 기능이 다른 전극층을 활용하며, Hyper Fast 개발에서는 기존 이중층 코팅설비를 사용할 수 있도록 슬러리 조성을 조정했다고 설명한다. 실제 코팅헤드 수, 층별 두께와 양산속도는 공개되지 않았다. ([ASK Inno][1])

---

## TECH-SKON-D04-051 — Solvent Drying & Recovery

```yaml
technology_id: TECH-SKON-D04-051
canonical_name: Electrode Solvent Drying and Recovery
korean_name: 전극 건조·용매 회수기술

technology_category:
  - Wet Electrode Manufacturing
  - Thermal Processing
  - Environmental Control

technology_status: COMMERCIAL_INDUSTRY_BASELINE
sk_on_specific_configuration: NOT_DISCLOSED

process_functions:
  - Remove solvent from coated electrode
  - Stabilize electrode microstructure
  - Recover and treat process solvent
  - Control residual moisture and solvent

critical_process_parameters:
  - Oven-zone temperature
  - Airflow
  - Web speed
  - Residence time
  - Exhaust concentration
  - Heat recovery
  - Solvent-recovery efficiency

critical_quality_attributes:
  - Residual solvent
  - Binder distribution
  - Adhesion
  - Electrode cracking
  - Porosity distribution
  - Uniform drying across width

principal_cost_and_environment_drivers:
  - Thermal energy demand
  - Long drying oven
  - Solvent handling
  - Solvent recovery
  - Emission-control equipment
  - Factory footprint

source_ids:
  - SRC-SKON-D04-035
  - SRC-SKON-D04-040
  - SRC-SKON-D04-041

confidence:
  process_definition: VERY_HIGH
  sk_on_energy_intensity: NOT_DISCLOSED
```

SK온은 습식전극의 건조·용매회수 단계가 공정시간과 에너지·설비공간을 크게 요구한다고 설명하며, 이를 제거하는 건식전극을 핵심 원가혁신 기술로 개발한다. 공식 기술자료의 약 100℃ 건조 설명은 공정개념을 단순화한 값이며 모든 화학계·라인의 실제 조건으로 일반화해서는 안 된다. ([ASK Inno][7])
