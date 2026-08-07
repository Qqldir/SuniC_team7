---
id: skon-d04-d04-053-d04-053-slitting-notching-edge-quality-o
title: "D04-053 — Slitting, Notching & Edge Quality — OI Metadata"
summary: "배터리 슬리팅·노칭·엣지 품질 공정의 요구사항과 KPI를 정의하는 YAML 메타데이터이며, Z-폴딩과 탭 접합 등 관련 조립 기술도 포함한다."
tags: [d04, technology, schema]
keywords: [슬릿팅, 노칭, 버, Z-폴딩, 전극적층, 탭, 집전체, 용접, 분리막, 버 높이, 입자 수, 라인 속도, 전극 정렬, 탭 접합, 열영향부]
related: []
priority: normal
domain: D04
section: D04-053
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: "Manufacturing Technology Master > D04-053 — Slitting, Notching & Edge Quality"
tokens: 2045
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Manufacturing Technology Master > D04-053 — Slitting, Notching & Edge Quality

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  external_capability_needs:
    - Inline burr metrology
    - Laser-cut heat-affected-zone monitoring
    - Particle extraction and counting
    - Tool-wear prediction
    - Edge-defect machine vision
    - Closed-loop cut-position control

  poc_kpis:
    - Burr height
    - Particle count
    - Dimensional error
    - Tool replacement interval
    - Cutting speed
    - Separator-damage incidence
```

---

## TECH-SKON-D04-054 — Z-Folding & Precision Stacking

```yaml
technology_id: TECH-SKON-D04-054
canonical_name: Z-Folding and Precision Electrode Stacking
korean_name: Z-폴딩·정밀 전극 적층

technology_category:
  - Cell Assembly
  - Separator Handling
  - Precision Automation
  - Safety-Critical Manufacturing

technology_status: COMMERCIALIZED_PROPRIETARY_TECHNOLOGY

technical_sequence:
  - Unwind continuous separator
  - Place electrode sheet
  - Fold separator over electrode
  - Place opposite electrode
  - Repeat zigzag sequence
  - Compress and align completed stack

critical_process_parameters:
  - Separator tension
  - Fold pitch
  - Electrode placement
  - Web speed
  - Static-electricity control
  - Stack compression
  - Vision alignment

critical_quality_attributes:
  - Anode-cathode alignment
  - Separator coverage
  - Stack flatness
  - Fold repeatability
  - Low particle contamination
  - No separator wrinkle

principal_defects:
  - Electrode skew
  - Separator wrinkle
  - Fold drift
  - Edge exposure
  - Misplaced electrode
  - Particle intrusion
  - Stack thickness variation

source_ids:
  - SRC-SKON-D04-036

confidence:
  technology_use: VERY_HIGH
  exact_line_speed: NOT_DISCLOSED
  defect_rate: NOT_DISCLOSED
```

SK온은 Z-Folding을 파우치 배터리의 안전성과 정밀 적층을 가능하게 하는 핵심 조립기술로 공개한다. 분리막이 연속적으로 전극을 감싸기 때문에 양극과 음극의 가장자리 직접 접촉 가능성을 낮추는 것이 핵심이며, 생산속도가 증가하더라도 위치정밀도를 유지하는 것이 양산 경쟁력의 핵심이다. ([ASK Inno][2])

---

## TECH-SKON-D04-055 — Tab & Current-Collector Joining

```yaml
technology_id: TECH-SKON-D04-055
canonical_name: Tab and Current-Collector Joining
korean_name: 탭·집전체 접합기술

technology_category:
  - Cell Assembly
  - Electrical Joining
  - Welding

technology_status:
  base_process: INDUSTRY_BASELINE
  sk_on_method: NOT_DISCLOSED

possible_joining_methods:
  - Laser welding
  - Ultrasonic welding
  - Resistance welding
  - Mechanical or hybrid joining

functions:
  - Electrically connect electrode foils
  - Form positive and negative terminals
  - Minimize electrical resistance
  - Maintain mechanical durability

critical_quality_attributes:
  - Weld strength
  - Electrical resistance
  - Weld penetration
  - Low spatter
  - No foil damage
  - Stable heat-affected zone

defect_modes:
  - Weak weld
  - Excessive heat
  - Foil tearing
  - Spatter contamination
  - Incomplete fusion
  - High contact resistance
  - Tab misalignment

source_ids:
  - SRC-SKON-D04-039
  - SRC-SKON-D04-041

confidence:
  process_need: VERY_HIGH
  sk_on_joining_method: NOT_DISCLOSED
```

셀 조립에서는 전극 집전체와 탭을 전기·기계적으로 안정되게 연결해야 한다. Argonne의 제조모델은 집전체 용접과 셀 적층을 자동화가 쉽지 않은 주요 공정으로 다루지만, SK온이 제품별로 어떤 용접방식을 사용하는지는 공개되지 않았다. 

---

## TECH-SKON-D04-056 — Pouch Forming, Sealing & Degassing

```yaml
technology_id: TECH-SKON-D04-056
canonical_name: Pouch Forming, Sealing and Degassing
korean_name: 파우치 성형·실링·가스 제거기술

technology_category:
  - Cell Packaging
  - Hermetic Sealing
  - Pouch Cell Manufacturing

technology_status: COMMERCIAL_INDUSTRY_PROCESS
sk_on_specific_parameter: NOT_DISCLOSED

process_functions:
  pouch_forming:
    - Form cavity in laminated pouch film
    - Accommodate electrode stack

  initial_sealing:
    - Seal cell perimeter while retaining electrolyte-injection path

  degassing:
    - Remove gas generated during early activation

  final_sealing:
    - Complete hermetic enclosure
    - Trim or fold excess pouch film

critical_process_parameters:
  - Forming depth
  - Film tension
  - Seal temperature
  - Seal pressure
  - Seal time
  - Surface cleanliness
  - Vacuum level
  - Gas-removal timing

critical_quality_attributes:
  - Seal strength
  - Low leakage
  - No film crack
  - Stable insulation
  - Controlled residual gas
  - Dimensional consistency

defect_modes:
  - Seal contamination
  - Pouch delamination
  - Microleak
  - Film wrinkle
  - Tab-seal leakage
  - Excessive residual gas
  - Mechanical damage

source_ids:
  - SRC-SKON-D04-036
  - SRC-SKON-D04-039

confidence:
  process_definition: HIGH
  sk_on_process_recipe: NOT_DISCLOSED
```

SK온 공식 Z-Folding 자료는 적층체를 파우치 필름으로 밀봉해 셀을 완성하는 구조를 설명한다. 다만 성형깊이·실링온도·압력·누설기준과 가스제거 조건은 공개되지 않아 산업 공통공정으로만 등록한다. ([ASK Inno][2])

---

## TECH-SKON-D04-057 — Electrolyte Filling & Wetting

```yaml
technology_id: TECH-SKON-D04-057
canonical_name: Electrolyte Filling and Electrode Wetting
korean_name: 전해액 주입·함침 기술

technology_category:
  - Cell Activation Preparation
  - Dry-Room Process
  - Electrolyte Management

technology_status:
  base_process: INDUSTRY_BASELINE
  sk_on_specific_method: NOT_DISCLOSED

process_functions:
  - Meter electrolyte quantity
  - Inject electrolyte into cell
  - Remove trapped gas
  - Promote pore penetration
  - Wet separator and electrode
  - Prepare cell for formation

critical_process_parameters:
  - Electrolyte quantity
  - Moisture level
  - Vacuum and pressure sequence
  - Filling rate
  - Temperature
  - Resting time
  - Cell compression
  - Electrolyte viscosity

critical_quality_attributes:
  - Complete electrode wetting
  - Uniform electrolyte distribution
  - Low residual gas
  - Correct electrolyte quantity
  - Low moisture contamination
  - No external leakage

defect_modes:
  - Underfilling
  - Overfilling
  - Dry electrode region
  - Trapped gas
  - Moisture contamination
  - Electrolyte leakage
  - Slow wetting

source_ids:
  - SRC-SKON-D04-039
  - SRC-SKON-D04-040
  - SRC-SKON-D04-041

confidence:
  process_need: VERY_HIGH
  sk_on_filling_recipe: NOT_DISCLOSED
```

전해액 주입은 적층·밀봉된 셀 내부에 전해액을 공급해 전극과 분리막의 기공을 충분히 적시는 단계다. DOE는 셀 조립·전해액 주입을 별도 제조영역으로 구분하며, SK온의 전해액 종류·주입량·진공함침 조건은 공개자료에서 확인되지 않는다. ([energy.gov][5])
