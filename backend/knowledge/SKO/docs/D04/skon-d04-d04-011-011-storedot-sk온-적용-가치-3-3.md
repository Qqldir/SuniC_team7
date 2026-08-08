---
id: skon-d04-d04-011-011-storedot-sk온-적용-가치-3-3
title: 011 — StoreDot — SK온 적용 가치 (3)
summary: StoreDot 기술의 형태·충전·안전·팩·BMS 등 주요 기술 분야별 적용 현황과 SK온과의 기술 연계 매트릭스
tags: [d04, technology, schema]
keywords: [StoreDot, 배터리 벤치마크, 기술 분류체계, 고속충전, 열관리, Cell-to-Pack, BMS, 안전 아키텍처, 음극재, 수명 예측, 프리즈매틱, 파우치, 급속충전, 열 관리, S-Pack, 배터리 냉각, ESS]
related: [TECH-SKON-D04-043]
priority: normal
domain: D04
section: D04-011
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 011 — StoreDot
tokens: 3750
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 011 — StoreDot

```yaml
F04_entities:

  - TECH-SKON-D04-006
    name: On-Vent Prismatic Technology

  - TECH-SKON-D04-017
    name: Pouch-Integrated Prismatic Architecture

  - TECH-SKON-D04-022
    name: Z-Folding Stacking Technology

  - TECH-SKON-D04-021
    name: Cell-Level Safety Architecture
    evidence_scope: ANALYSIS_WITH_OFFICIAL_COMPONENTS

  - TECH-SKON-D04-023
    name: Ceramic-Coated Separator Safety Interface
    ownership_scope: SK_INNOVATION_GROUP_AFFILIATE

  - TECH-SKON-D04-055
    name: Tab and Current-Collector Joining

  - TECH-SKON-D04-056
    name: Pouch Forming, Sealing and Degassing
```

---

## F05. Fast Charging & Performance

```yaml
F05_entities:

  - TECH-SKON-D04-005
    name: SUFast

  - TECH-SKON-D04-043
    name: Simulation-Based Charging Protocol Optimization

  - TECH-SKON-D04-014
    name: Dual-Layer Anode Architecture

  - TECH-SKON-D04-015
    name: Magnetic Alignment Process

  - TECH-SKON-D04-013
    name: Silicon–Graphite Anode Platform

  - TECH-SKON-D04-016
    name: Large-Surface Cooling
```

SUFast는 셀 전극설계와 충전 프로토콜을 함께 최적화하는 상위 기술이고, `TECH-SKON-D04-043`은 그 안에서 SOC·온도·음극전위 등을 바탕으로 전류를 설계하는 알고리즘 하위기술로 관리한다.

---

## F06. Safety & Thermal Management

```yaml
F06_entities:

  - TECH-SKON-D04-002
    name: Thermal Propagation Prevention

  - TECH-SKON-D04-026
    name: Thermal Barrier and Gas-Path Control

  - TECH-SKON-D04-016
    name: Large-Surface Cooling

  - TECH-SKON-D04-027
    name: Bottom-Cooling Reference Architecture
    ownership_scope: INDUSTRY_BASELINE

  - TECH-SKON-D04-028
    name: EV Battery Immersion Cooling

  - TECH-SKON-D04-009
    name: Coolant Immersion ESS Safety

  - TECH-SKON-D04-024
    name: S-Pack CTP Safety Architecture

  - TECH-SKON-D04-025
    name: S-Pack+ Integrated Safety Architecture

  - TECH-SKON-D04-029
    name: Wireless BMS

  - TECH-SKON-D04-030
    name: Multi-Layer Battery Abnormality Detection
    evidence_scope: ANALYSIS_WITH_OFFICIAL_COMPONENTS
```

---

## F07. Pack & ESS Architecture

```yaml
F07_entities:

  - TECH-SKON-D04-004
    name: Cell-to-Pack Technology

  - TECH-SKON-D04-020
    name: Flexible ESS DC/AC Block Architecture

  - TECH-SKON-D04-024
    name: S-Pack

  - TECH-SKON-D04-025
    name: S-Pack+

  - TECH-SKON-D04-031
    name: VIB ESS Safety Platform
    ownership_scope: JOINT_DEVELOPMENT

  - TECH-SKON-D04-062
    name: Module, Pack and CTP Assembly
```

---

## F08. BMS·Diagnostics·BaaS

```yaml
F08_entities:

  - TECH-SKON-D04-008
    name: EIS-Based BMS

  - TECH-SKON-D04-018
    name: BaaS AI Platform

  - TECH-SKON-D04-019
    name: SOH·RUL·Residual-Value Prediction

  - TECH-SKON-D04-029
    name: Wireless BMS

  - TECH-SKON-D04-030
    name: Multi-Layer Abnormality Detection

  - TECH-SKON-D04-044
    name: Battery Operational Digital Twin
    ownership_scope: ANALYTICAL_TARGET

  - TECH-SKON-D04-045
    name: Fleet Battery Analytics

  - TECH-SKON-D04-046
    name: Battery Passport Data Architecture
```

---

## F09. Digital R&D & AI

```yaml
F09_entities:

  - TECH-SKON-D04-032
    name: AI Researcher Orchestration Platform

  - TECH-SKON-D04-033
    name: RFQ Analysis AI

  - TECH-SKON-D04-034
    name: AI-Based Design and Analysis Machine

  - TECH-SKON-D04-035
    name: Cell Performance Prediction AI

  - TECH-SKON-D04-036
    name: Cell Cost Calculation AI

  - TECH-SKON-D04-037
    name: Materials Development AI Researcher

  - TECH-SKON-D04-038
    name: Battery Foundation Model Target Capability
    ownership_scope: ANALYTICAL_TARGET

  - TECH-SKON-D04-039
    name: AI Calendering Process Control

  - TECH-SKON-D04-040
    name: Battery Manufacturing Digital Twin

  - TECH-SKON-D04-042
    name: Predictive Quality Intelligence Layer
    ownership_scope: ANALYTICAL_TARGET
```

SK온은 Cell Development AI Researcher를 구축했고, 공개 시점에는 Materials Development AI Researcher를 개발 중이었다. RFQ 분석, 설계안 생성, 성능예측, 원가계산과 보고서 생성이 기능별 AI로 연결되는 구조다. ([ASK Inno][1])

---

## F10. Electrode Manufacturing

```yaml
F10_entities:

  - TECH-SKON-D04-003
    name: Dry Electrode Process

  - TECH-SKON-D04-047
    name: Wet Mixing and Slurry Intelligence

  - TECH-SKON-D04-048
    name: Dry Powder Mixing

  - TECH-SKON-D04-049
    name: Wet Electrode Coating

  - TECH-SKON-D04-050
    name: Dual-Layer Electrode Coating

  - TECH-SKON-D04-051
    name: Solvent Drying and Recovery

  - TECH-SKON-D04-052
    name: Electrode Calendering

  - TECH-SKON-D04-053
    name: Slitting, Notching and Edge-Quality Control
```

건식전극은 습식공정의 용매·건조·회수 단계를 줄일 수 있지만, 분말층의 두께와 밀도를 균일하게 만드는 캘린더링이 핵심 스케일업 과제로 남는다. SK온은 복수의 건식 코팅방식을 개발하고 AI를 이용한 롤 속도·압력·온도 제어를 공개했다. ([ASK Inno][2])

---

## F11. Cell Manufacturing

```yaml
F11_entities:

  - TECH-SKON-D04-022
    name: Z-Folding

  - TECH-SKON-D04-055
    name: Tab and Current-Collector Joining

  - TECH-SKON-D04-056
    name: Pouch Forming, Sealing and Degassing

  - TECH-SKON-D04-057
    name: Electrolyte Filling and Wetting

  - TECH-SKON-D04-058
    name: Formation, Degassing and Aging

  - TECH-SKON-D04-059
    name: Cell Grading and Sorting

  - TECH-SKON-D04-060
    name: High-Speed Nondestructive Cell Inspection

  - TECH-SKON-D04-061
    name: Battery Laser Processing Platform
```

---

## F12. Pack·System Manufacturing

```yaml
F12_entities:

  - TECH-SKON-D04-062
    name: Module, Pack and CTP Assembly

  - TECH-SKON-D04-020
    name: ESS DC/AC Block Architecture

  - TECH-SKON-D04-016
    name: Large-Surface Cooling Integration

  - TECH-SKON-D04-028
    name: EV Immersion Cooling Integration

  - TECH-SKON-D04-029
    name: Wireless BMS Integration

  - TECH-SKON-D04-026
    name: Pack Gas-Path Control
```

---

## F13. Smart Factory & Digital Thread

```yaml
F13_entities:

  - TECH-SKON-D04-040
    name: Manufacturing Digital Twin

  - TECH-SKON-D04-041
    name: Intelligent Production Equipment and OT Infrastructure

  - TECH-SKON-D04-042
    name: Predictive Quality Intelligence

  - TECH-SKON-D04-064
    name: Manufacturing Digital Thread

  - TECH-SKON-D04-039
    name: AI Calendering Control
```

---

## F14. Analytical Target Capabilities

아래 엔티티들은 SK온이 공식적으로 동일 명칭의 통합 플랫폼을 보유한다고 확인된 기술이 아니다.

```yaml
F14_analytical_entities:

  - TECH-SKON-D04-038
    name: Battery Foundation Model
    status: ANALYTICAL_TARGET

  - TECH-SKON-D04-042
    name: Predictive Quality Intelligence Layer
    status: ANALYTICAL_INTEGRATION_LAYER

  - TECH-SKON-D04-044
    name: Battery Operational Digital Twin
    status: ANALYTICAL_INTEGRATION_LAYER

  - TECH-SKON-D04-064
    name: Manufacturing Digital Thread
    status: ANALYTICAL_INTEGRATION_LAYER

  - TECH-SKON-D04-073
    name: High-Pressure Stack Management
    status: REQUIRED_CAPABILITY_WITHOUT_DISCLOSED_SK_ON_DESIGN

  - TECH-SKON-D04-078
    name: Prelithiation
    status: EXTERNAL_CAPABILITY_CANDIDATE
```

---

# D04-47. Product–Technology–Process Integrated Mapping

## 47.1 SF Fast-Charging Family

```text
PROD-SKON-EV-003 SF Battery
├─ USES_TECHNOLOGY → High-Nickel NCM
├─ USES_TECHNOLOGY → Fast-Charging Cell Design
└─ USES_PROCESS → Z-Folding

PROD-SKON-EV-005 SF+ Battery
├─ EVOLVED_FROM → SF Battery
├─ USES_TECHNOLOGY → Silicon–Graphite Anode
├─ USES_TECHNOLOGY → Dual-Layer Anode Architecture
├─ USES_PROCESS → Dual-Layer Coating
└─ HAS_PAIN_POINT → Differential Layer Expansion

PROD-SKON-EV-004 Advanced SF
├─ EVOLVED_FROM → SF Battery
├─ USES_TECHNOLOGY → Magnetic Alignment
├─ USES_PROCESS → Microstructure-Controlled Electrode Manufacturing
└─ HAS_PAIN_POINT → Inline Particle-Orientation Verification

PROD-SKON-EV-006 Hyper Fast Battery
├─ USES_TECHNOLOGY → SUFast
├─ USES_TECHNOLOGY → Charging Protocol Optimization
├─ USES_TECHNOLOGY → Silicon–Graphite Anode
├─ REQUIRES → Fast-Charge Thermal Management
├─ REQUIRES → Lithium-Plating Detection
└─ HAS_STATUS → TECHNOLOGY_DEMONSTRATION
```

---

## 47.2 LFP Product Chain

```text
PROD-SKON-EV-007 LFP EV Platform
├─ USES_CHEMISTRY → LFP
├─ USES_TECHNOLOGY → LFP Electrode Densification
├─ MAY_USE → Dry Electrode Process
├─ MAY_USE → CTP
├─ REQUIRES → Low-Temperature Performance Control
└─ HAS_STATUS → PRE_COMMERCIAL

PROD-SKON-ESS-001 LFP ESS Battery
├─ USES_CHEMISTRY → LFP
├─ APPLIED_TO → GRIDON
├─ USES_PROCESS → Electrode Manufacturing
├─ USES_PROCESS → Formation and Aging
└─ HAS_STATUS → CONTRACTED_OR_PRODUCTION_PLANNED
```

`MAY_USE` 관계는 기술적 적용 가능성을 의미하며, 공식 제품 BOM이나 양산공정 적용이 확인됐다는 뜻은 아니다.

---

## 47.3 Prismatic·CTP Chain

```text
PROD-SKON-EV-009 On-Vent Prismatic
├─ USES_TECHNOLOGY → Configurable Vent Design
├─ USES_PROCESS → Laser Engraving
├─ REQUIRES → Rupture-Pressure Inspection
└─ HAS_STATUS → PROTOTYPE

PROD-SKON-EV-008 Pouch-Integrated Prismatic
├─ USES → Mid-Nickel Pouch Cells
├─ USES → Aluminum Outer Case
├─ USES → Large-Surface Cooling
├─ USES → Compression Pad
├─ USES → Directional Venting
└─ HAS_STATUS → PROTOTYPE_VALIDATION

TECH-SKON-D04-004 CTP
├─ REQUIRES_PROCESS → Automated Cell Placement
├─ REQUIRES_PROCESS → Structural Bonding
├─ REQUIRES_TECHNOLOGY → Thermal Propagation Prevention
├─ REQUIRES_TECHNOLOGY → Large-Surface Cooling
├─ REQUIRES → Swelling Accommodation
└─ REQUIRES → Rework Strategy
```

On-Vent는 각형 캔에 레이저로 벤트를 형성해 위치와 가스 배출방향을 설계하는 기술이며, SK온은 반복 압력시험 결과를 공개했다. 제품 적용과 양산수율은 별도 근거가 필요한 상태다. ([ASK Inno][3])

---

## 47.4 GRIDON Technology Chain

```text
PROD-SKON-ESS-002 GRIDON Gen 1
├─ USES → LFP ESS Battery
├─ USES → EIS-Based BMS
├─ USES → Coolant Immersion ESS Safety
├─ USES → Multi-Layer Abnormality Detection
├─ HAS_ARCHITECTURE → DC Block
└─ SUPPORTS_APPLICATION → Grid / Industrial / Data Center ESS

PROD-SKON-ESS-003 GRIDON Gen 2
├─ EVOLVED_FROM → GRIDON Gen 1
├─ SUPPORTS → DC Block
├─ SUPPORTS → AC Block
├─ REQUIRES → PCS Integration
├─ REQUIRES → EMS Interoperability
├─ REQUIRES → Cybersecure Edge Control
└─ HAS_STATUS → DEVELOPMENT
```

---

## 47.5 BaaS Technology Chain

```text
Vehicle and Battery Data
├─ Driving History
├─ Charging History
├─ Voltage
├─ Current
├─ Temperature
└─ Abnormal Event History
          ↓
TECH-SKON-D04-018 BaaS AI
├─ ESTIMATES → SOH
├─ ESTIMATES → RUL
├─ ESTIMATES → Residual Value
├─ DETECTS → Abnormality
└─ SUPPORTS → Fleet Battery Analytics
          ↓
Lifecycle Decision
├─ Continue Use
├─ Repair
├─ Used-EV Valuation
├─ Reuse as ESS
└─ Recycling
```

---

## 47.6 Solid-State Technology Chain

```text
PROD-SKON-NEXT-002 Sulfide ASSB
├─ USES → Sulfide Solid Electrolyte
├─ MAY_USE → Lithium-Metal Anode
├─ REQUIRES → Solid–Solid Interface Engineering
├─ REQUIRES → Moisture-Controlled Manufacturing
├─ REQUIRES → H2S Risk Management
├─ REQUIRES → Pressure Management
├─ PILOT_TECHNOLOGY_FROM → Solid Power
└─ EXPLORES_ALTERNATIVE_PLATFORM_WITH → Factorial
```

Solid Power는 2026년 1분기 SK온 파일럿 셀 라인의 현장인수시험 완료를 공식 발표했다. 이는 기술협력이 파일럿 설비 설치와 공정이전 단계까지 진행됐다는 직접 근거다. ([Solid Power][4])

Factorial과 SK온은 2026년 7월 29일 기존 리튬이온 생산 인프라에서 전고체 기술을 제조할 가능성을 평가하는 MOU를 발표했다. 현재 관계는 비구속적 제조 타당성 검토 단계로 저장한다. ([Factorial Energy][5])

---

## 47.7 Dry Electrode Chain

```text
TECH-SKON-D04-003 Dry Electrode Process
├─ USES_PROCESS → Dry Powder Mixing
├─ USES_PROCESS → Dry Coating
├─ USES_PROCESS → Calendering
├─ USES_AI → AI Calendering Control
├─ REQUIRES → Inline Thickness Measurement
├─ REQUIRES → Inline Porosity Measurement
├─ HAS_PAIN_POINT → Powder Segregation
├─ HAS_PAIN_POINT → Electrode Cracking
├─ HAS_PAIN_POINT → Adhesion
└─ HAS_PAIN_POINT → Pilot-to-Mass-Production Yield
```

---

## 47.8 AI Researcher Chain

```text
TECH-SKON-D04-032 AI Researcher
├─ HAS_COMPONENT → RFQ Analysis AI
├─ HAS_COMPONENT → AI-Based Design and Analysis Machine
├─ HAS_COMPONENT → Performance Prediction AI
├─ HAS_COMPONENT → Cost Calculation AI
├─ HAS_COMPONENT → Report Generation AI
└─ EXPANDS_TO → Materials Development AI Researcher

RFQ Analysis AI
└─ GENERATES → Structured Requirement Set

AI Design and Analysis Machine
├─ GENERATES → Cell Design Candidates
├─ PREDICTS → Performance
├─ ESTIMATES → Cost
└─ REQUIRES → Human Approval
```

---

# D04-48. Partner–Technology Relationship Master

## 48.1 Partner Classification
