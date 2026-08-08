---
id: skon-d05-d05-05-r-d-program-master
title: R&D Program Master
summary: "리튬이온 배터리, 열확산 방지, 건식전극, CTP 등 SK온이 진행 중인 배터리 R&D의 4개 핵심 프로그램의 진행 단계와 연구 범위를 정리한 공식 목록."
tags: [d05, rnd, schema, "xref:d04"]
keywords: [리튬이온 배터리, Lithium-Ion, R&D 프로그램, 배터리 안전, 건식전극, Dry Electrode, CTP, 열 확산, 급속충전, GRIDON, Lithium-ion, 열확산 방지, Thermal Propagation, 에너지밀도]
related: []
priority: normal
domain: D05
section: D05-05.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 2764
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-05. R&D Program Master

## RDP-SKON-D05-001 — Commercial Lithium-Ion Advancement

```yaml
program_id: RDP-SKON-D05-001
canonical_name: Commercial Lithium-Ion Battery Advancement

program_scope:
  - High energy density
  - Fast charging
  - Safety
  - Battery life
  - Customer-specific cell and system design

research_objects:
  - Cathode
  - Anode
  - Electrolyte
  - Cell
  - Module
  - Pack
  - BMS

program_status: ACTIVE_CONTINUOUS

related_technology_ids:
  - TECH-SKON-D04-011
  - TECH-SKON-D04-012
  - TECH-SKON-D04-005
  - TECH-SKON-D04-013
  - TECH-SKON-D04-015

facility_ids:
  - FAC-SKON-D05-001

evidence_level: DIRECT_OFFICIAL
confidence: VERY_HIGH

source_ids:
  - SRC-SKON-D05-001
```

SK온 미래기술원은 안전·급속충전·에너지밀도·수명을 리튬이온 배터리의 핵심 연구축으로 제시한다. 이 프로그램은 일회성 프로젝트라기보다 고객 요구와 제품세대에 따라 계속 이어지는 상시 연구영역이다. ([SK Innovation][1])

---

## RDP-SKON-D05-002 — Thermal Propagation Prevention

```yaml
program_id: RDP-SKON-D05-002
canonical_name: Thermal Propagation Prevention Program

program_status: ACTIVE_PRIORITY_PROGRAM

research_scope:
  - Cell-level thermal stability
  - Inter-cell barrier
  - Cooling
  - Directed venting
  - Gas-path control
  - Pack containment
  - Early abnormality detection

related_technology_ids:
  - TECH-SKON-D04-002
  - TECH-SKON-D04-016
  - TECH-SKON-D04-026
  - TECH-SKON-D04-030

program_outputs:
  - S-Pack
  - S-Pack+
  - Large-surface cooling
  - On-Vent
  - GRIDON safety system

maturity_range:
  minimum: PROTOTYPE
  maximum: PRODUCT_INTEGRATED

source_ids:
  - SRC-SKON-D05-008
```

---

## RDP-SKON-D05-003 — Dry Electrode Scale-Up

```yaml
program_id: RDP-SKON-D05-003
canonical_name: Dry Electrode Scale-Up Program

program_status: DEVELOPMENT_AND_PILOT

research_scope:
  - Solvent-free powder mixing
  - Dry coating
  - Binder distribution
  - Current-collector adhesion
  - Calendering
  - AI process control
  - Yield improvement

related_technology_ids:
  - TECH-SKON-D04-003
  - TECH-SKON-D04-048
  - TECH-SKON-D04-052
  - TECH-SKON-D04-039

critical_gaps:
  - Pilot yield
  - Electrode cracking
  - Thickness uniformity
  - Line speed
  - Commercial cost reduction

source_ids:
  - SRC-SKON-D05-008
```

건식전극은 SK온이 공개한 핵심 R&D 우선과제다. 그러나 공개자료는 실제 양산수율·처리속도·원가절감률을 제공하지 않으므로 `양산 적용 완료`가 아닌 `개발·파일럿` 단계로 관리한다.

---

## RDP-SKON-D05-004 — CTP & Multi-Form-Factor Program

```yaml
program_id: RDP-SKON-D05-004
canonical_name: CTP and Multi-Form-Factor Development

program_status: DEVELOPMENT_AND_PROTOTYPE

research_scope:
  - Pouch CTP
  - Large-surface cooling
  - S-Pack+
  - On-Vent prismatic cell
  - Pouch-integrated prismatic architecture
  - Pack structure and venting
  - Cell placement and rework

related_technology_ids:
  - TECH-SKON-D04-004
  - TECH-SKON-D04-006
  - TECH-SKON-D04-017
  - TECH-SKON-D04-024
  - TECH-SKON-D04-025

critical_gaps:
  - Named OEM validation
  - Mass-production yield
  - Crash validation
  - Repairability
  - Form-factor-specific production assets

source_ids:
  - SRC-SKON-D05-008
```

---

## RDP-SKON-D05-005 — ESS & Battery Intelligence

```yaml
program_id: RDP-SKON-D05-005
canonical_name: ESS and Battery Intelligence Program

program_status: PRODUCT_DEVELOPMENT_AND_INTEGRATION

research_scope:
  - LFP ESS cell
  - Module, rack and container
  - ESS BMS
  - EIS diagnostics
  - Predictive safety
  - DC and AC block
  - Battery degradation analytics

related_products:
  - GRIDON Gen 1
  - GRIDON Gen 2

related_technology_ids:
  - TECH-SKON-D04-008
  - TECH-SKON-D04-009
  - TECH-SKON-D04-020
  - TECH-SKON-D04-030

facility_ids:
  - FAC-SKON-D05-001

confidence: VERY_HIGH
source_ids:
  - SRC-SKON-D05-001
```

---

## RDP-SKON-D05-006 — Solid-State Battery Program

```yaml
program_id: RDP-SKON-D05-006
canonical_name: Solid-State Battery Program

program_status: PILOT_VALIDATION

research_tracks:
  polymer_oxide_composite:
    role: Transitional or bridge technology
    maturity: PROTOTYPE_AND_PILOT

  sulfide_assb:
    role: Long-term all-solid-state platform
    maturity: PILOT_VALIDATION
    latest_commercialization_target: 2029

research_scope:
  - Solid electrolyte
  - Lithium-metal anode
  - Solid-state cathode
  - Solid-solid interface
  - Pressure management
  - Moisture and H2S control
  - Pilot manufacturing

facility_ids:
  - FAC-SKON-D05-002

partner_ids:
  - PART-SOLID-POWER
  - PART-FACTORIAL

related_technology_ids:
  - TECH-SKON-D04-001
  - TECH-SKON-D04-065
  - TECH-SKON-D04-069
  - TECH-SKON-D04-070
  - TECH-SKON-D04-071
  - TECH-SKON-D04-072

critical_gaps:
  - Pilot yield
  - Large-area cell uniformity
  - Electrolyte cost
  - Customer sample status
  - Vehicle validation
  - Commercial plant decision

source_ids:
  - SRC-SKON-D05-003
  - SRC-SKON-D05-004
  - SRC-SKON-D05-005
```

전고체 프로그램은 자체 소재·계면 연구와 외부 기술 도입을 병행한다. 대전 파일럿 시설과 Solid Power 기술라인은 확인됐지만, 상업용 셀 규격·고객 샘플·차량검증은 공개되지 않았다. ([ASK Inno][3])

---

## RDP-SKON-D05-007 — Next-Generation Materials Research

```yaml
program_id: RDP-SKON-D05-007
canonical_name: Next-Generation Battery Materials Research

program_status: LAB_RESEARCH_AND_PILOT_CONNECTION

research_topics:
  - SIPE polymer electrolyte
  - LLZO oxide electrolyte
  - Sulfide electrolyte
  - Surface-modified lithium metal
  - LMRO cathode
  - Ultrahigh-nickel single crystal
  - High-voltage electrolyte additive
  - Gel-polymer curing

research_model:
  - Joint research with universities
  - Peer-reviewed publication
  - Patent filing
  - Pilot-cell applicability assessment

linked_program:
  - RDP-SKON-D05-006

confidence: VERY_HIGH
```

이 프로그램의 개별 연구성과는 D04에서 확인했지만, 논문성과를 양산제품 적용으로 자동 변환하지 않는다. D05 후속 구간에서 각 논문·특허군·연구자를 연결한다.

---

## RDP-SKON-D05-008 — AI Researcher

```yaml
program_id: RDP-SKON-D05-008
canonical_name: AI Researcher Program

program_status:
  cell_development_ai: INTERNAL_OPERATION
  materials_development_ai: DEVELOPMENT_AT_LAST_DISCLOSURE

research_scope:
  - RFQ analysis
  - Cell design generation
  - Performance prediction
  - Cost calculation
  - Automated reporting
  - Materials discovery

related_technology_ids:
  - TECH-SKON-D04-032
  - TECH-SKON-D04-033
  - TECH-SKON-D04-034
  - TECH-SKON-D04-035
  - TECH-SKON-D04-036
  - TECH-SKON-D04-037

critical_gaps:
  - Public prediction accuracy
  - Model uncertainty
  - Training-data lineage
  - Experiment automation
  - Patent and literature integration

source_ids:
  - SRC-SKON-D05-007
```

---

## RDP-SKON-D05-009 — Quality·Metrology·Validation

```yaml
program_id: RDP-SKON-D05-009
canonical_name: Battery Quality, Metrology and Validation Program

program_status: ACTIVE

organization_ids:
  - ORG-SKON-QUALITY-001

facility_ids:
  - FAC-SKON-D05-003
  - FAC-SKON-D05-004

research_and_quality_scope:
  - Calibration
  - Measurement traceability
  - Test-equipment reliability
  - Global quality standardization
  - Pilot and product measurement support

confirmed_external_accreditation:
  - KOLAS international calibration laboratory

not_confirmed:
  - Exact relationship to historical Global Quality-Control Center plan
  - Complete global laboratory network
  - Product-specific validation capacity

source_ids:
  - SRC-SKON-D05-002
  - SRC-SKON-D05-006
```

---

## RDP-SKON-D05-010 — Open Research Collaboration

```yaml
program_id: RDP-SKON-D05-010
canonical_name: Open Research and Technology Collaboration

program_status: ACTIVE_PORTFOLIO

collaboration_types:
  - University joint research
  - Peer-reviewed publication
  - Technology licensing
  - Pilot-line installation
  - Joint development
  - Manufacturing feasibility MOU
  - Affiliate technology collaboration

partner_categories:
  university:
    - Seoul National University
    - Hanyang University
    - Yonsei University
    - Dankook University
    - University of Texas research team

  research_institute:
    - Korea Institute of Ceramic Engineering and Technology

  technology_company:
    - Solid Power
    - Factorial
    - Standard Energy
    - Siemens Digital Industries Software

  group_affiliate:
    - SK Enmove
    - SK IE Technology

ip_questions:
  - Background IP ownership
  - Foreground invention ownership
  - Improvement patent ownership
  - Field-of-use rights
  - Manufacturing geography
  - Publication review
  - Data and model ownership
```

---

# D05-06. Program–Facility–Technology Graph

```text
SK On Future Technology Institute
│
├── HOSTS → Commercial Li-Ion Advancement
│   ├── High-Nickel NCM
│   ├── Fast Charging
│   ├── Mid-Nickel
│   └── LFP
│
├── HOSTS → Safety & Architecture Programs
│   ├── Thermal Propagation Prevention
│   ├── CTP
│   ├── Prismatic
│   └── Cooling
│
├── HOSTS → ESS R&D
│   ├── GRIDON
│   ├── EIS-Based BMS
│   └── DC/AC Block
│
├── HOSTS → AI Researcher
│   ├── RFQ Analysis AI
│   ├── Cell Design AI
│   └── Materials AI
│
└── CONTAINS → ASSB Pilot Plant
    ├── Polymer–Oxide Composite
    ├── Sulfide ASSB
    ├── Lithium Metal
    ├── Solid–Solid Interface
    └── Solid Power Technology Line

SK On Quality Management Division
└── OPERATES → Calibration and Metrology Infrastructure
    └── SUPPORTS → Research and Product Validation
```

---
