---
id: skon-d04-d04-077-d04-077-gel-polymer-electrolyte-curing-c-1
title: D04-077 — Gel Polymer Electrolyte Curing Control — OI Metadata
summary: "젤 폴리머 전해질 경화 제어의 기술 메타데이터, 리튬 사전 충전(프리리치에이션) 기술 현황, 그리고 SIPE·폴리머·산화물·황화물 등 전해질 기술 비교 평가표를 담은 문서."
tags: [d04, technology, schema, table, "xref:d17"]
keywords: [단량체 전환율, 이온전도도, 프리리천에이션, 첫사이클효율, 음극 기술, 리튬메탈, LLZO, 황화물계, 경화 공정, 전해질 비교, 젤 폴리머 전해질, 경화 제어, 프리리치에이션, 리튬 인벤토리, 전해질 기술 비교, 초기 쿨롱 효율, 실리콘 음극]
related: []
priority: normal
domain: D04
section: D04-077
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Next-Generation Technology Master > D04-077 — Gel Polymer Electrolyte Curing Control
tokens: 3291
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Next-Generation Technology Master > D04-077 — Gel Polymer Electrolyte Curing Control

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: HIGH

  missing_capabilities:
    - Inline monomer-conversion measurement
    - Rapid low-temperature curing
    - Uniform volumetric heating
    - Residual-monomer sensor
    - Curing-reaction digital twin
    - High-voltage-stable monomer

  poc_kpis:
    - Monomer conversion
    - Curing time
    - Ionic conductivity
    - Capacity retention
    - Gas generation
    - Cathode interphase resistance
```

---

## TECH-SKON-D04-078 — Prelithiation Target Capability

```yaml
technology_id: TECH-SKON-D04-078
canonical_name: Prelithiation Target Capability
korean_name: 프리리치에이션 목표역량

technology_category:
  - Lithium Inventory Management
  - High-Capacity Anode
  - First-Cycle Efficiency

technology_status: ANALYTICAL_TARGET_CAPABILITY
official_named_sk_on_program: NOT_FOUND_IN_REVIEWED_SOURCE_SET
commercial_status: NOT_APPLICABLE

reason_for_registration:
  - Silicon-rich anodes experience high first-cycle lithium loss
  - Lithium-metal and advanced anodes require precise lithium-inventory control
  - SK On is developing silicon-graphite, lithium-metal and next-generation cells
  - No direct SK On prelithiation program was confirmed in reviewed official sources

potential_approaches:
  information_type: INDUSTRY_ANALYSIS
  candidates:
    - Stabilized lithium metal powder
    - Sacrificial lithium-rich cathode additive
    - Electrochemical prelithiation
    - Direct lithium contact
    - Prelithiated silicon composite

potential_value:
  - Improve initial coulombic efficiency
  - Compensate initial SEI lithium consumption
  - Increase usable cell capacity
  - Improve silicon-anode viability

principal_risks:
  - Lithium handling safety
  - Process complexity
  - Uneven lithium distribution
  - Gas generation
  - Overlithiation
  - Additional cost
  - Moisture sensitivity

information_type: ANALYSIS
source_basis:
  - Silicon-Graphite Anode Program
  - Lithium-Metal Program
  - Surface-Modified Lithium Research

confidence:
  strategic_relevance: HIGH
  sk_on_current_implementation: UNCONFIRMED
```

이번 공식·학술 자료 검토에서는 SK온이 `프리리치에이션`을 명시적으로 보유 또는 적용한다고 밝힌 근거를 확인하지 못했다. 따라서 이 기술은 현재 보유기술이 아니라 실리콘 음극과 차세대 음극의 초기 리튬 손실을 보완할 수 있는 외부역량 후보로만 등록한다.

---

# D04-33. Electrolyte Technology Comparison

| 기술         | 상온 이온전도      | 기계적 특성   | 계면 접촉    | 대기 안정성   | 제조 난도    | SK온 상태 |
| ---------- | ------------ | -------- | -------- | -------- | -------- | ------ |
| SIPE 고분자   | 황화물보다 낮음     | 유연함      | 상대적으로 우수 | 조성 의존    | 필름화 과제   | 연구검증   |
| 폴리머-산화물 복합 | 중간 목표        | 유연성+보강   | 우수 목표    | 산화물로 보완  | 복합분산·경화  | 파일럿 개발 |
| LLZO 산화물   | 연구값 1.7mS/cm | 단단하지만 취성 | 접촉저항 과제  | 상대적으로 우수 | 고온소결     | 연구·특허  |
| 광소결 LLZTO  | 연구단계         | 다공성 지지체  | 폴리머 결합   | 추가검증     | 광 균일성    | 연구     |
| 황화물계       | 높은 전도 잠재력    | 비교적 연성   | 우수       | 수분에 취약   | 초저습·가스관리 | 파일럿    |

위 비교는 동일 조건의 SK온 내부시험 결과가 아니라 각 공식 연구에서 공개된 물성·구조적 특성을 정리한 기술비교다. SIPE 수치와 LLZO 수치는 서로 다른 연구체계에서 측정됐으므로 직접 제품순위를 의미하지 않는다. ([ASK Inno][3])

---

# D04-34. Solid-State Interface Relationship Graph

```text
Polymer–Oxide Composite Battery
├─ USES → Polymer Electrolyte
├─ USES → Oxide Solid Electrolyte
├─ MAY_USE → SIPE
├─ MAY_USE → Photonic-Sintered Garnet Scaffold
├─ REQUIRES → Thermal Curing Control
└─ HAS_PAIN_POINT → Residual Monomer

Sulfide All-Solid-State Battery
├─ USES → Sulfide Solid Electrolyte
├─ MAY_USE → Lithium-Metal Anode
├─ MAY_USE → LMRO Cathode
├─ REQUIRES → Solid-Solid Interface Engineering
├─ REQUIRES → High-Pressure Stack Management
├─ REQUIRES → Moisture-Controlled Manufacturing
└─ HAS_PAIN_POINT → H2S and Interface Degradation

Lithium-Metal Anode
├─ HAS_PAIN_POINT → Native Resistive Layer
├─ HAS_PAIN_POINT → Dendrite
├─ HAS_PAIN_POINT → Dead Lithium
├─ IMPROVED_BY → SIPE
├─ IMPROVED_BY → Surface-Modified Lithium Interphase
└─ REQUIRES → Pressure and Current Uniformity

LMRO Cathode
├─ HAS_ADVANTAGE → Manganese-Based Cost Structure
├─ HAS_PAIN_POINT → Oxygen Release
├─ HAS_PAIN_POINT → Voltage Decay
├─ DEGRADES → Sulfide Electrolyte
└─ IMPROVED_BY → Surface Coating

Ultrahigh-Nickel Single Crystal
├─ REDUCES → Grain-Boundary Cracking
├─ SUPPORTS → High Electrode Density
└─ REQUIRES → Crack-Free Calendering
```

---

# D04-35. Next-Generation Maturity Map

| Technology   | 검증 수준            | D04 성숙도                | 상용 근거      |
| ------------ | ---------------- | ---------------------- | ---------- |
| 폴리머-산화물 복합   | 파일럿·시제품 개발       | PILOT_DEVELOPMENT      | 미확인        |
| SIPE         | 논문·연구셀           | RESEARCH_VALIDATION    | 없음         |
| LLZO 고전도 전해질 | 논문·특허출원          | RESEARCH_AND_PATENT    | 없음         |
| 광소결 가넷 지지체   | 논문               | LAB_RESEARCH           | 없음         |
| 황화물 전해질      | 파일럿·파트너 협력       | PILOT_VALIDATION       | 없음         |
| 리튬메탈 음극      | 연구셀              | RESEARCH_VALIDATION    | 없음         |
| 표면개질 리튬      | 300회 연구셀         | PEER_REVIEWED_LAB      | 없음         |
| 고체-고체 계면     | 핵심 연구영역          | CORE_R&D               | 없음         |
| 고압 스택        | 필요역량             | ANALYTICAL_CAPABILITY  | SK온 구조 미공개 |
| LMRO 단결정     | 논문               | PEER_REVIEWED_RESEARCH | 없음         |
| 초고니켈 대형 단결정  | Nature Energy 논문 | PEER_REVIEWED_RESEARCH | 양산 미확인     |
| 고전압 첨가제      | 제품기술 공개          | PRODUCT_TECHNOLOGY     | 조성 미공개     |
| GPE 경화제어     | 논문               | PEER_REVIEWED_RESEARCH | 양산 미확인     |
| 프리리치에이션      | 공식 프로그램 미확인      | ANALYTICAL_TARGET      | 없음         |

---

# D04-36. Roadmap Reconciliation Register

```yaml
roadmap_reconciliation:

  polymer_oxide_composite:
    disclosures:
      - date: 2023-09
        target: commercialization_by_2028
      - date: 2024-06
        target: commercial_prototype_2028
      - date: 2025-01
        target: commercial_prototype_2027
      - date: 2025-05
        target: commercialization_2028
      - date: 2026-01
        target: no_specific_year_separately_disclosed

    canonical_status:
      commercialization_year: NOT_FIXED
      state: PILOT_AND_PROTOTYPE_DEVELOPMENT

  sulfide_assb:
    disclosures:
      - date: 2023-09
        target: commercialization_by_2028
      - date: 2024-06
        target: commercial_prototype_2029
      - date: 2025-01
        target: commercial_prototype_2029
      - date: 2025-05
        target: commercialization_2030
      - date: 2026-01
        target: commercialization_2029

    canonical_status:
      latest_official_target: 2029
      confidence: MEDIUM
      rule: FORWARD_LOOKING_TARGET_REQUIRES_ANNUAL_UPDATE
```

SK온의 전고체 목표연도는 발표시점과 `상업용 시제품`·`상용화`의 정의에 따라 변경됐다. D04에서는 날짜를 하나로 덮어쓰지 않고 발표시점별 값을 모두 보존하며, 황화물계는 2026년 최신 공식자료의 2029년을 현재 기준 목표로 사용한다. ([ASK Inno][3])

---

# D04-37. Next-Generation Technology Gap Register

```yaml
next_generation_gaps:

  - gap_id: GAP-D04-NEXT-001
    technology: Polymer-Oxide Composite
    gap:
      - Commercial prototype timing instability
      - Residual monomer
      - High-voltage stability
      - Thin-film production
      - Mass-production yield
    priority: VERY_HIGH

  - gap_id: GAP-D04-NEXT-002
    technology: SIPE
    gap:
      - Large-area film production
      - Full-cell cycle life
      - High-voltage cathode compatibility
      - Conductivity at low temperature
    priority: VERY_HIGH

  - gap_id: GAP-D04-NEXT-003
    technology: LLZO
    gap:
      - High-temperature sintering
      - Brittle fracture
      - Grain-boundary resistance
      - Lithium interface contact
    priority: HIGH

  - gap_id: GAP-D04-NEXT-004
    technology: Photonic Sintering
    gap:
      - Large-area irradiation uniformity
      - Roll-to-roll validation
      - Crack control
      - Commercial equipment
    priority: HIGH

  - gap_id: GAP-D04-NEXT-005
    technology: Sulfide Electrolyte
    gap:
      - Cost
      - Moisture sensitivity
      - H2S safety
      - Sheet fabrication
      - Pilot yield
    priority: VERY_HIGH

  - gap_id: GAP-D04-NEXT-006
    technology: Lithium-Metal Anode
    gap:
      - Dendrite
      - Dead lithium
      - Surface contamination
      - Large-area handling
      - High-current lifetime
    priority: VERY_HIGH

  - gap_id: GAP-D04-NEXT-007
    technology: Artificial Lithium Interphase
    gap:
      - Roll-to-roll surface treatment
      - Layer uniformity
      - Long-term pressure compatibility
      - Treatment cost
    priority: VERY_HIGH

  - gap_id: GAP-D04-NEXT-008
    technology: Solid-Solid Interface
    gap:
      - Contact loss
      - Chemical decomposition
      - Interface inspection
      - Mechanical-electrochemical modeling
    priority: VERY_HIGH

  - gap_id: GAP-D04-NEXT-009
    technology: High-Pressure Stack
    gap:
      - SK On architecture not disclosed
      - Lightweight pressure structure
      - Distributed pressure sensing
      - Creep compensation
    priority: VERY_HIGH

  - gap_id: GAP-D04-NEXT-010
    technology: LMRO Cathode
    gap:
      - Oxygen release
      - Voltage decay
      - Sulfide oxidation
      - Single-crystal synthesis scale-up
    priority: HIGH

  - gap_id: GAP-D04-NEXT-011
    technology: Ultrahigh-Nickel Single Crystal
    gap:
      - Commercial synthesis yield
      - High-density calendering fracture
      - Thermal stability
      - Cost
    priority: HIGH

  - gap_id: GAP-D04-NEXT-012
    technology: Gel Polymer Curing
    gap:
      - Rapid curing versus complete conversion
      - Inline residual-monomer measurement
      - Large-cell temperature uniformity
    priority: HIGH

  - gap_id: GAP-D04-NEXT-013
    technology: Prelithiation
    gap:
      - No confirmed SK On program
      - Safe lithium dosing
      - Uniformity
      - Process integration
    priority: MEDIUM_HIGH
```

---

# D04-38. D17 연결용 Next-Generation OI Seeds
