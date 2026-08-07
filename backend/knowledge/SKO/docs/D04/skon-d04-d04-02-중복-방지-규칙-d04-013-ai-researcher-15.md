---
id: skon-d04-d04-02-중복-방지-규칙-d04-013-ai-researcher-15
title: 중복 방지 규칙 — D04-013 — AI Researcher
summary: "AI Researcher와 기술 신뢰도, 분류체계를 정의하여 지식베이스 중복을 방지하는 규칙"
tags: [d04, technology, schema, table]
keywords: [셀 설계, 성능예측, 원가계산, Battery R&D, 설계 가속화, 기술 분류체계, AI 플랫폼, 신뢰도 평가, AI Researcher, 셀 설계 자동화, 신뢰도 등급, 기술분류체계, R&D 플랫폼, 배터리]
related: []
priority: normal
domain: D04
section: D04-02.
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Technology Classification Rules > 중복 방지 규칙
tokens: 2361
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Technology Classification Rules > 중복 방지 규칙

## SRC-SKON-D04-013 — AI Researcher

```yaml
source_id: SRC-SKON-D04-013
title: SK On's AI Researcher – A New Paradigm in Battery Development
publisher: SK Innovation Newsroom
source_type: Official Technology Article
publication_date: 2026-03-25
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_technologies:
  - Cell Development AI Researcher
  - Materials Development AI Researcher
  - RFQ Analysis AI
  - Cell Design AI
  - Performance Prediction
  - Cost Calculation
  - Report Generation AI
```

AI Researcher는 실험·공정·설계 데이터를 학습해 고객 요구조건을 분석하고, 셀 설계 후보 생성, 성능예측, 원가계산 및 보고서 작성을 지원하는 연구개발 플랫폼이다. SK온은 셀 설계기간을 기존의 약 3분의 1로 줄이고, 후보 검토 수를 15배 이상 확대하며, 원가분석 속도를 약 700배 높일 수 있을 것으로 제시한다. 이 수치는 회사가 제시한 내부 기대효과이며 외부 검증 성과와 구분한다. ([ASK Inno][12])

---

# D04-RP-002. Source Reliability Matrix

| Source ID | 출처 유형        | 직접성 |   최신성 | 신뢰도 | 사용 범위    |
| --------- | ------------ | --: | ----: | --: | -------- |
| D04-001   | 공식 R&D 페이지   |  직접 |    현재 |  A+ | 기술 범위 정의 |
| D04-002   | 공식 기술 시리즈    |  직접 | 매우 높음 |  A+ | 4대 R&D   |
| D04-003   | 공식 기술 콘텐츠    |  직접 |    높음 |  A+ | 전고체      |
| D04-004   | 공식 기술 콘텐츠    |  직접 |    높음 |  A+ | 열전파      |
| D04-005   | 공식 기술 콘텐츠    |  직접 |    높음 |  A+ | 건식전극     |
| D04-006   | 공식 기술 콘텐츠    |  직접 |    높음 |  A+ | CTP      |
| D04-007   | 공식 기술 콘텐츠    |  직접 | 매우 높음 |  A+ | 급속충전     |
| D04-008   | 공식 기술 콘텐츠    |  직접 | 매우 높음 |  A+ | On-Vent  |
| D04-009   | 공식 기술 콘텐츠    |  직접 | 매우 높음 |  A+ | 하이브리드 각형 |
| D04-010   | 공식 기술 콘텐츠    |  직접 | 매우 높음 |  A+ | LFP      |
| D04-011   | 공식 ESS 콘텐츠   |  직접 | 매우 높음 |  A+ | EIS      |
| D04-012   | 공식 ESS 콘텐츠   |  직접 | 매우 높음 |  A+ | ESS 안전   |
| D04-013   | 공식 AI 기술 콘텐츠 |  직접 | 매우 높음 |  A+ | AI R&D   |

```yaml
source_limitations:
  - 대부분 SK온 또는 SK이노베이션의 자체 발표자료
  - 기술 존재와 기업 목표 확인에는 신뢰도가 높음
  - 성능 우위와 경제효과는 독립검증 자료가 추가로 필요
  - 제조사 시험결과는 third_party_verified로 변경하지 않음
  - 목표연도와 기대효과는 realized_result로 저장하지 않음
```

---

# D04-01. Technology Taxonomy v1.0

```text
SK On Technology Taxonomy
│
├── T01 Electrochemistry & Chemistry Platform
│   ├── T01-01 High-Nickel NCM
│   ├── T01-02 Mid-Nickel NCM
│   ├── T01-03 LFP
│   ├── T01-04 Sulfide Solid Electrolyte
│   ├── T01-05 Polymer-Oxide Composite Electrolyte
│   └── T01-06 Lithium-Metal Battery
│
├── T02 Electrode & Active-Material Technology
│   ├── T02-01 High-Nickel Cathode Stabilization
│   ├── T02-02 High-Density LFP Electrode
│   ├── T02-03 Silicon-Graphite Anode
│   ├── T02-04 Dual-Layer Anode
│   ├── T02-05 Magnetic Particle Alignment
│   └── T02-06 High-Loading Electrode
│
├── T03 Cell Design & Form Factor
│   ├── T03-01 Pouch Cell
│   ├── T03-02 Conventional Prismatic Cell
│   ├── T03-03 On-Vent Prismatic Cell
│   ├── T03-04 Pouch-Integrated Prismatic Cell
│   └── T03-05 Cylindrical Platform [Exploratory]
│
├── T04 Charging & Performance Engineering
│   ├── T04-01 SF Fast-Charging Technology
│   ├── T04-02 SF+ Dual-Layer Anode
│   ├── T04-03 Advanced SF Magnetic Alignment
│   ├── T04-04 SUFast
│   ├── T04-05 Charging Protocol Simulation
│   ├── T04-06 Lithium-Plating Control
│   └── T04-07 Low-Temperature Charging
│
├── T05 Cell & Pack Safety
│   ├── T05-01 Cell-Level Thermal Stability
│   ├── T05-02 Thermal Propagation Prevention
│   ├── T05-03 Directed Gas Venting
│   ├── T05-04 Cell Isolation
│   ├── T05-05 Large-Surface Cooling
│   ├── T05-06 Coolant Immersion
│   └── T05-07 ESS Fire-Risk Response
│
├── T06 Module, Pack & System Architecture
│   ├── T06-01 Cell-to-Module
│   ├── T06-02 Cell-to-Pack
│   ├── T06-03 Pouch-Type CTP
│   ├── T06-04 Large-Surface-Cooling CTP
│   ├── T06-05 ESS Rack
│   ├── T06-06 DC Block
│   └── T06-07 AC Block
│
├── T07 BMS, Diagnostics & Battery Data
│   ├── T07-01 Automotive BMS
│   ├── T07-02 ESS BMS
│   ├── T07-03 EIS-Based Diagnostics
│   ├── T07-04 SOH Estimation
│   ├── T07-05 Remaining-Useful-Life Prediction
│   ├── T07-06 Abnormality Detection
│   └── T07-07 Residual-Value Assessment
│
├── T08 ESS Technology
│   ├── T08-01 LFP ESS Cell
│   ├── T08-02 Containerized BESS
│   ├── T08-03 Predictive ESS Diagnostics
│   ├── T08-04 Coolant-Based Fire Suppression
│   ├── T08-05 PCS Interface
│   └── T08-06 EMS Interface
│
├── T09 Manufacturing Technology
│   ├── T09-01 Wet Electrode Process
│   ├── T09-02 Dry Electrode Process
│   ├── T09-03 Dry Powder Mixing
│   ├── T09-04 Dry Coating
│   ├── T09-05 Calendering
│   ├── T09-06 Dual-Layer Coating
│   ├── T09-07 Magnetic Alignment Process
│   └── T09-08 Laser Vent Processing
│
├── T10 Digital & AI R&D
│   ├── T10-01 Cell Development AI Researcher
│   ├── T10-02 Materials Development AI Researcher
│   ├── T10-03 RFQ Analysis AI
│   ├── T10-04 Cell Design AI
│   ├── T10-05 Performance Prediction AI
│   ├── T10-06 Cost Prediction AI
│   ├── T10-07 AI Calendering Optimization
│   └── T10-08 Automated Technical Reporting
│
├── T11 Next-Generation Battery Platform
│   ├── T11-01 Polymer-Oxide Composite Battery
│   ├── T11-02 Sulfide All-Solid-State Battery
│   ├── T11-03 Lithium-Metal Anode
│   ├── T11-04 Solid-Solid Interface Engineering
│   ├── T11-05 High-Pressure Cell Structure
│   └── T11-06 Solid-State Pilot Manufacturing
│
└── T12 Technology Intelligence Metadata
    ├── Technology Readiness Level
    ├── Commercialization Status
    ├── Product Link
    ├── Process Link
    ├── Patent Link
    ├── Pain Point
    ├── Benchmark Technology
    ├── Missing Capability
    └── OI Opportunity Seed
```

---

# D04-02. Technology Classification Rules

```yaml
technology_classification_rules:

  technology_object:
    definition: >
      특정 제품을 가능하게 하는 재료, 설계, 공정, 알고리즘,
      진단, 안전 또는 시스템 기술

  product_object:
    definition: >
      고객에게 판매·공급되거나 제품명으로 공개된 셀, 팩,
      ESS 시스템 또는 서비스

  process_object:
    definition: >
      원재료를 제품으로 변환하는 제조단계와 운전조건

  architecture_object:
    definition: >
      셀·모듈·팩·랙·컨테이너 및 제어시스템의 연결구조

  capability_object:
    definition: >
      기술개발 또는 상용화를 위해 조직이 보유해야 하는 역량

  status_required:
    values:
      - COMMERCIALIZED
      - PRODUCT_APPLIED
      - PILOT_VALIDATION
      - PROTOTYPE
      - DEVELOPMENT
      - RESEARCH
      - EXPLORATORY
      - CORPORATE_TARGET
      - NOT_DISCLOSED
```

### 중복 방지 규칙

```yaml
examples:

  Hyper_Fast_Battery:
    D03_class: PRODUCT_PROTOTYPE
    D04_linked_technology:
      - SUFast
      - Dual-Layer Coating
      - Charging Protocol Simulation

  GRIDON:
    D03_class: ESS_PRODUCT_SYSTEM
    D04_linked_technology:
      - EIS-Based BMS
      - Coolant Immersion
      - Dual-Valve Safety Structure

  On_Vent_Cell:
    D03_class: PRODUCT_PROTOTYPE
    D04_linked_technology:
      - Laser Vent Processing
      - Configurable Vent Design
      - Directed Gas Release
```

---

# D04-03. Core Technology Master
