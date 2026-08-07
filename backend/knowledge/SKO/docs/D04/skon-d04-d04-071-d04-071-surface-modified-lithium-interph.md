---
id: skon-d04-d04-071-d04-071-surface-modified-lithium-interph
title: D04-071 — Surface-Modified Lithium Interphase — OI Metadata
summary: "전고체 배터리의 표면개질 리튬 계면, 고체-고체 계면 엔지니어링, 고압 스택 관리 기술의 개발 현황과 핵심 지표를 정의한 기술 메타데이터이다."
tags: [d04, technology, schema]
keywords: [계면 엔지니어링, 고체-고체 접촉, SEI, 임계 전류 밀도, 고압 스택 관리, 인터페이스 저항, 전고체 배터리, 고체 전해질, 부피 변화, 표면개질 리튬, 계면 저항, 임계전류밀도, 고체-고체 계면, 고체전해질, 고압 스택, 리튬 금속 음극, 계면 설계]
related: []
priority: normal
domain: D04
section: D04-071
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Next-Generation Technology Master > D04-071 — Surface-Modified Lithium Interphase
tokens: 1229
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Next-Generation Technology Master > D04-071 — Surface-Modified Lithium Interphase

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  external_capability_needs:
    - Continuous lithium surface cleaning
    - Artificial SEI roll coating
    - Air-free lithium handling
    - Interphase thickness metrology
    - Operando lithium deposition imaging
    - Critical-current-density testing

  poc_kpis:
    - Interfacial resistance
    - Critical current density
    - Lithium symmetric-cell life
    - Full-cell cycle retention
    - Surface-layer uniformity
    - Treatment cost per square meter
```

---

## TECH-SKON-D04-072 — Solid–Solid Interface Engineering

```yaml
technology_id: TECH-SKON-D04-072
canonical_name: Solid-Solid Interface Engineering
korean_name: 고체-고체 계면 엔지니어링

technology_category:
  - Solid-State Interface
  - Electrochemical Contact
  - Mechanical-Electrochemical Co-Design

technology_status: CORE_RESEARCH_CAPABILITY
commercial_status: NOT_COMMERCIALIZED

interface_types:
  - Cathode active material to solid electrolyte
  - Conductive additive to cathode composite
  - Solid electrolyte to lithium-metal anode
  - Oxide scaffold to polymer phase
  - Electrolyte layer to current collector

failure_modes:
  - Physical contact loss
  - Interfacial void
  - Chemical decomposition
  - Space-charge resistance
  - Mechanical crack
  - Particle debonding
  - Reaction-layer thickening
  - Nonuniform current concentration

control_methods:
  confirmed_or_researched:
    - Cathode coating
    - Lithium surface modification
    - Hybrid polymer-oxide electrolyte
    - Microstructure control

  analytical_candidates:
    - Gradient interface
    - Soft buffer layer
    - In-situ polymerization
    - Atomic-layer coating
    - Pressure-adaptive interlayer

related_technologies:
  - Sulfide Solid Electrolyte
  - LLZO
  - SIPE
  - LMRO Coating
  - Surface-Modified Lithium

source_ids:
  - SRC-SKON-D04-044
  - SRC-SKON-D04-045
  - SRC-SKON-D04-046
  - SRC-RES-D04-047

confidence:
  capability_need: VERY_HIGH
  full_commercial_solution: NOT_CONFIRMED
```

액체 전해액은 전극의 미세공극을 채우지만 고체전해질은 고체입자와 물리적 접촉을 유지해야 한다. 따라서 화학반응 억제뿐 아니라 충·방전 중 부피변화와 압력변화에도 접촉면을 유지하는 계면설계가 전고체 상용화의 핵심이다. SK온의 표면개질·양극 코팅·복합 전해질 연구는 각각 이 문제를 다른 계면에서 해결한다. ([ASK Inno][4])

---

## TECH-SKON-D04-073 — High-Pressure Stack Management

```yaml
technology_id: TECH-SKON-D04-073
canonical_name: High-Pressure Stack Management
korean_name: 고압 스택 관리기술

technology_category:
  - Solid-State Cell Mechanics
  - Pressure Control
  - Cell Structure

technology_status: ANALYTICAL_CORE_CAPABILITY
official_named_sk_on_program: NOT_CONFIRMED
commercial_status: NOT_APPLICABLE

technical_role:
  - Maintain solid-solid contact
  - Reduce interfacial void formation
  - Control lithium-metal deposition
  - Compensate electrode volume change
  - Reduce composite cathode contact loss

system_components:
  - Mechanical compression structure
  - Pressure-distribution plate
  - Elastic or spring element
  - Pressure sensor
  - Temperature compensation
  - Cell swelling model
  - Pressure-release safety structure

principal_tradeoffs:
  - Higher pressure may improve contact
  - Excess pressure may fracture solid electrolyte
  - Heavy compression hardware reduces system energy density
  - Pressure variation may create uneven current distribution
  - Long-term creep may reduce contact force

information_type: ANALYSIS

source_ids:
  - SRC-SKON-D04-042
  - SRC-SKON-D04-046
  - SRC-RES-D04-047

confidence:
  technology_need: VERY_HIGH
  sk_on_specific_architecture: NOT_DISCLOSED
```

SK온은 전고체 파일럿과 계면 안정화 연구를 공개했지만, 스택압력 수치나 압력유지 하드웨어는 공개하지 않았다. 이 엔티티는 전고체 셀의 고체-고체 접촉을 유지하기 위해 필요한 분석역량으로 등록하며 SK온의 특정 장치 보유를 뜻하지 않는다. ([ASK Inno][1])
