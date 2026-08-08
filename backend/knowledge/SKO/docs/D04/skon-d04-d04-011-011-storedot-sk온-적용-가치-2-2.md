---
id: skon-d04-d04-011-011-storedot-sk온-적용-가치-2-2
title: 011 — StoreDot — SK온 적용 가치 (2)
summary: 고체배터리 분야 선도 기업들의 기술 역량을 비교하고 SK온의 협력 현황 및 경쟁 벤치마크를 정리한 문서
tags: [d04, technology, schema, table, "xref:d17"]
keywords: [Factorial, 고체전지, MOU, 기술벤치마크, 경쟁사분석, Samsung SDI, CATL, 기술격차, 전고체배터리, 기술로드맵, 고체배터리, 기술역량비교, 차세대전지, 벤치마킹, 전고체전지, all-solid-state battery]
related: []
priority: normal
domain: D04
section: D04-011
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 011 — StoreDot
tokens: 3815
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 011 — StoreDot

* Solid Power
  * Factorial
  * QuantumScape
  * Toyota·Idemitsu
  * Samsung SDI
  * LG Energy Solution
  * CATL
  * ProLogium
  * SES AI
  * 24M
  * StoreDot
* **Factorial–SK온 2026년 7월 29일 MOU 신규 반영**
* External Capability Comparison Matrix
* SK온 직접 파트너·협력 후보·경쟁 벤치마크 분류
* External Capability Gap Register
* D17 연결용 External OI Seed 9건

## 다음 시작점

`D04-46 Integrated Technology Entity Master`

```text
D04-46 Integrated Technology Entity Master
├── 전체 Technology ID 통합·중복제거
├── Product–Technology–Process 연결
├── Partner–Technology 연결
├── TRL·상용화 상태 정규화
├── FACT·ANALYSIS·HYPOTHESIS 분리
├── Technology Relationship Graph
├── Chunk Library
├── Human-Readable Technology Report
├── Data Quality & Source Index
└── D04 Final YAML
```

[1]: https://www.solidpowerbattery.com/investor-relations/investor-news/news-details/2026/Solid-Power-Reports-First-Quarter-2026-Results/default.aspx "Solid Power Inc. - Solid Power Reports First Quarter 2026 Results"
[2]: https://factorialenergy.com/press-releases/factorial-and-sk-on-sign-mou-to-explore-solid-state-battery-manufacturing/ "Factorial and SK On Sign MoU to Explore Solid-State Battery Manufacturing  - Factorial Energy"
[3]: https://factorialenergy.com/press-releases/stellantis-and-factorial-integrate-advanced-solid-state-battery-into-stellantis-development-vehicle-and-launch-road-testing/ "Stellantis and Factorial Integrate Advanced Solid-State Battery into Stellantis Development Vehicle and Launch Road Testing - Factorial Energy"
[4]: https://ir.quantumscape.com/static-files/298db199-d53c-4b90-bf9e-e1fd2a5df11a?utm_source=chatgpt.com "Q4 FISCAL 2025"
[5]: https://global.toyota/en/newsroom/corporate/39865919.html?utm_source=chatgpt.com "Idemitsu and Toyota Announce Beginning of Cooperation ..."
[6]: https://www.samsungsdi.com/sdi-now/sdi-news/4782.html?utm_source=chatgpt.com "SAMSUNG SDI Unveils All-Solid-State Battery for Physical AI"
[7]: https://www.samsungsdi.com/sdi-now/sdi-news/4565.html?utm_source=chatgpt.com "Samsung SDI to Collaborate on All-Solid-State Battery ..."
[8]: https://inside.lgensol.com/en/2026/06/a-battery-without-an-anode-lg-energy-solutions-research-on-combining-anodeless-and-solid-state-batteries/?utm_source=chatgpt.com "A Battery Without an Anode? LG Energy Solution's ..."
[9]: https://www.lgensol.com/upload/file/irEvent/25_4Q_LGES_business_performance_F_EN.pdf?utm_source=chatgpt.com "LG Energy Solution - PowerPoint 프레젠테이션"
[10]: https://www.catl.com/en/news/6720.html?utm_source=chatgpt.com "CATL and CHANGAN Launch World's First Mass- ..."
[11]: https://www.catl.com/en/news/6812.html?utm_source=chatgpt.com "CATL and HyperStrong Sign the World's Largest Sodium- ..."
[12]: https://prologium.com/prologium-marks-20th-anniversary-at-ces-2026-unveils-breakthrough-superfluidized-all-inorganic-solid-state-battery-results/?utm_source=chatgpt.com "ProLogium Marks 20th Anniversary at CES 2026, Unveils ..."
[13]: https://prologium.com/prologiums-next-generation-lithium-ceramic-battery-shipments-surpass-2-4-million-units-a-new-milestone-in-the-commercialization-of-green-energy-technologies/?utm_source=chatgpt.com "ProLogium's Next-Generation Lithium Ceramic Battery ..."
[14]: https://www.ses.ai/?utm_source=chatgpt.com "SES AI"
[15]: https://www.ses.ai/events/2025-gtc-presentation?utm_source=chatgpt.com "SES AI Presentation at NVIDIA GTC"
[16]: https://24-m.com/?utm_source=chatgpt.com "24M Technologies"
[17]: https://24-m.com/press-releases/24m-introduces-impervio-a-separator-technology-that-delivers-unprecedented-safety-improvements-for-lithium-batteries?hs_amp=true&utm_source=chatgpt.com "24M® Introduces Impervio™ — a Separator Technology ..."
[18]: https://www.store-dot.com/press/storedot-and-polestar-showcase-worlds-first-electric-vehicle-10-minute-charge-with-si-dominant-cells?utm_source=chatgpt.com "StoreDot | STOREDOT AND POLESTAR SHOWCASE WORLD’S FIRST ELECTRIC VEHICLE 10-MINUTE CHARGE WITH SI-DOMINANT CELLS"
[19]: https://www.store-dot.com/technology?utm_source=chatgpt.com "StoreDot | Technology"

---

# SK온 D04 Technology Taxonomy

## Part 8. Integrated Technology Entity Master·Relationship Graph

**문서 버전:** D04 v1.7
**기준일:** 2026-08-02
**이전 완료 지점:** `D04-45 External Collaboration OI Seeds`

---

# D04-DQ-002. Source Grade Normalization v2

기존 Source Library의 신뢰도 등급을 아래 기준으로 최종 정규화한다.

```yaml
source_grade_policy_v2:

  A_PLUS:
    definition: 최상위 법정·제도·공시 근거
    source_types:
      - Regulatory filing
      - Annual report
      - Integrated report
      - Sustainability report
      - Government publication
      - Regulation
      - Patent

  A:
    definition: 공식 기업·연구 원문
    source_types:
      - Official corporate newsroom
      - Official product page
      - Official investor presentation
      - Peer-reviewed research paper
      - Public research institute publication
      - University research publication

  B_PLUS:
    definition: 주요 국제 경제·통신매체
    source_types:
      - Reuters
      - Bloomberg
      - Financial Times
      - Wall Street Journal

  B:
    definition: 산업 전문기관·컨설팅
    source_types:
      - Industry association
      - Reputable consulting company
      - Market research institute

normalization_actions:
  - 기업 뉴스룸·공식 기술 페이지: A
  - 기업 보도자료·제품 페이지: A
  - Peer-reviewed paper: A
  - 정부·공시·공식 ESG 보고서: A+
  - source_grade와 confidence를 별도 필드로 관리
  - manufacturer claim은 source_grade와 관계없이 별도 태그 유지
```

예를 들어 SK온의 AI Researcher 존재와 구성은 공식 기술자료에 의해 직접 확인되므로 `source_grade: A`, `evidence_type: OFFICIAL_DIRECT`, `confidence: VERY_HIGH`로 저장한다. 회사가 제시한 개발기간 단축이나 원가분석 속도는 같은 출처에 있어도 `claim_status: COMPANY_EXPECTATION`으로 별도 관리한다. ([ASK Inno][1])

---

# D04-46. Integrated Technology Entity Master

## 46.1 Canonical Entity Schema

```yaml
technology_entity_schema:

  technology_id:
    type: canonical_string
    required: true

  canonical_name:
    type: string
    required: true

  korean_name:
    type: string
    required: true

  aliases:
    type: array

  entity_type:
    allowed_values:
      - MATERIAL_TECHNOLOGY
      - ELECTROCHEMICAL_TECHNOLOGY
      - CELL_DESIGN
      - PACK_ARCHITECTURE
      - SAFETY_TECHNOLOGY
      - THERMAL_TECHNOLOGY
      - DIAGNOSTIC_TECHNOLOGY
      - DIGITAL_AI_TECHNOLOGY
      - MANUFACTURING_PROCESS
      - MANUFACTURING_SYSTEM
      - SYSTEM_ARCHITECTURE
      - ANALYTICAL_CAPABILITY
      - AFFILIATE_TECHNOLOGY
      - JOINT_DEVELOPMENT_PLATFORM

  ownership_scope:
    allowed_values:
      - SK_ON
      - SK_INNOVATION_GROUP_AFFILIATE
      - JOINT_DEVELOPMENT
      - EXTERNAL_PARTNER
      - INDUSTRY_BASELINE
      - ANALYTICAL_TARGET

  evidence_scope:
    allowed_values:
      - OFFICIAL_DIRECT
      - OFFICIAL_INDIRECT
      - PEER_REVIEWED
      - PARTNER_CONFIRMED
      - INDUSTRY_BASELINE
      - ANALYSIS
      - HYPOTHESIS

  maturity_status:
    type: controlled_vocabulary

  commercial_status:
    type: controlled_vocabulary

  related_product_ids:
    type: array

  related_process_ids:
    type: array

  related_partner_ids:
    type: array

  parent_technology_ids:
    type: array

  child_technology_ids:
    type: array

  pain_point_ids:
    type: array

  oi_seed_ids:
    type: array

  source_ids:
    type: array

  source_grade:
    type: array

  confidence:
    allowed_values:
      - VERY_HIGH
      - HIGH
      - MEDIUM
      - LOW
      - UNCONFIRMED

  claim_status:
    allowed_values:
      - VERIFIED_FACT
      - MANUFACTURER_CLAIM
      - CORPORATE_TARGET
      - ANALYST_INFERENCE
      - HYPOTHESIS

  last_verified_at:
    type: date
```

---

## 46.2 Duplicate·Alias Normalization Ledger

기존 `TECH-SKON-D04-001~078` 중 명칭이나 범위가 중복된 엔티티를 정리한다.

| 기존 ID             | 처리            | Canonical ID      | 사유                                   |
| ----------------- | ------------- | ----------------- | ------------------------------------ |
| TECH-SKON-D04-010 | `MERGED_INTO` | TECH-SKON-D04-032 | AI Researcher 일반 플랫폼과 오케스트레이션 플랫폼 중복 |
| TECH-SKON-D04-054 | `MERGED_INTO` | TECH-SKON-D04-022 | 두 엔티티 모두 Z-Folding·정밀 적층 기술          |
| TECH-SKON-D04-063 | `MERGED_INTO` | TECH-SKON-D04-041 | 지능형 생산설비와 OT 인프라 범위 중복               |
| TECH-SKON-D04-001 | 유지            | TECH-SKON-D04-001 | 황화물계 전고체 **셀 플랫폼**                   |
| TECH-SKON-D04-069 | 유지            | TECH-SKON-D04-069 | 황화물 **고체전해질 소재 플랫폼**                 |
| TECH-SKON-D04-004 | 유지            | TECH-SKON-D04-004 | CTP 제품·구조 기술                         |
| TECH-SKON-D04-062 | 유지            | TECH-SKON-D04-062 | CTP를 포함한 실제 조립공정 기술                  |
| TECH-SKON-D04-014 | 유지            | TECH-SKON-D04-014 | 이중층 음극의 전극구조                         |
| TECH-SKON-D04-050 | 유지            | TECH-SKON-D04-050 | 이중층을 제조하는 코팅공정                       |
| TECH-SKON-D04-009 | 유지            | TECH-SKON-D04-009 | ESS용 냉각수 침지 안전기술                     |
| TECH-SKON-D04-028 | 유지            | TECH-SKON-D04-028 | EV용 절연유 액침냉각                         |

```yaml
entity_normalization_snapshot:

  original_technology_ids: 78
  retired_duplicate_ids: 3
  active_canonical_entities: 75

  retired_ids:
    - TECH-SKON-D04-010
    - TECH-SKON-D04-054
    - TECH-SKON-D04-063

  count_status:
    state: PROVISIONAL_UNTIL_MACHINE_EXPORT
    required_check:
      - Duplicate name
      - Duplicate alias
      - Orphan entity
      - Circular parent-child relation
      - Missing source
```

---

## 46.3 Canonical Technology Families

```text
D04 Canonical Technology Master
│
├── F01 Chemistry & Active Materials
├── F02 Electrolyte & Interface
├── F03 Electrode Architecture
├── F04 Cell Design & Form Factor
├── F05 Fast Charging & Performance
├── F06 Safety & Thermal Management
├── F07 Pack & ESS Architecture
├── F08 BMS·Diagnostics·BaaS
├── F09 Digital R&D & AI
├── F10 Electrode Manufacturing
├── F11 Cell Manufacturing
├── F12 Pack·System Manufacturing
├── F13 Smart Factory & Digital Thread
└── F14 Analytical Target Capabilities
```

---

## F01. Chemistry & Active Materials

```yaml
F01_entities:

  - TECH-SKON-D04-011
    name: High-Nickel NCM Platform
    evidence_scope: OFFICIAL_DIRECT
    maturity_status: COMMERCIALIZED

  - TECH-SKON-D04-012
    name: High-Voltage Mid-Nickel Technology
    evidence_scope: OFFICIAL_DIRECT
    maturity_status: PROTOTYPE

  - TECH-SKON-D04-007
    name: High-Density LFP Electrode Technology
    evidence_scope: OFFICIAL_DIRECT
    maturity_status: DEVELOPMENT

  - TECH-SKON-D04-074
    name: LMRO Single-Crystal Cathode
    evidence_scope: PEER_REVIEWED
    maturity_status: LAB_VALIDATION

  - TECH-SKON-D04-075
    name: Ultrahigh-Nickel Large Single-Crystal Cathode
    evidence_scope: PEER_REVIEWED
    maturity_status: LAB_VALIDATION

  - TECH-SKON-D04-013
    name: Silicon–Graphite Anode Platform
    evidence_scope: OFFICIAL_DIRECT
    maturity_status: PRODUCT_TECHNOLOGY_DISCLOSED

  - TECH-SKON-D04-070
    name: Lithium-Metal Anode Platform
    evidence_scope: PEER_REVIEWED
    maturity_status: LAB_VALIDATION
```

---

## F02. Electrolyte & Interface

```yaml
F02_entities:

  - TECH-SKON-D04-065
    name: Polymer–Oxide Composite Electrolyte Platform
    maturity_status: PILOT_DEVELOPMENT

  - TECH-SKON-D04-066
    name: Single-Ion Conducting Polymer Electrolyte
    maturity_status: LAB_VALIDATION

  - TECH-SKON-D04-067
    name: LLZO Oxide Solid Electrolyte
    maturity_status: LAB_VALIDATION

  - TECH-SKON-D04-069
    name: Sulfide Solid Electrolyte Platform
    maturity_status: PILOT_VALIDATION

  - TECH-SKON-D04-071
    name: Surface-Modified Lithium Interphase
    maturity_status: LAB_VALIDATION

  - TECH-SKON-D04-072
    name: Solid–Solid Interface Engineering
    maturity_status: CORE_R_AND_D

  - TECH-SKON-D04-076
    name: High-Voltage Electrolyte and Additive Platform
    maturity_status: PRODUCT_TECHNOLOGY_DISCLOSED

  - TECH-SKON-D04-077
    name: Gel Polymer Electrolyte Curing Control
    maturity_status: LAB_VALIDATION
```

---

## F03. Electrode Architecture

```yaml
F03_entities:

  - TECH-SKON-D04-014
    name: Dual-Layer Anode Architecture

  - TECH-SKON-D04-015
    name: Magnetic Alignment Process

  - TECH-SKON-D04-050
    name: Dual-Layer Electrode Coating

  - TECH-SKON-D04-052
    name: Electrode Calendering

  - TECH-SKON-D04-068
    name: Ultrafast Photonic Sintering

  - TECH-SKON-D04-078
    name: Prelithiation Target Capability
    evidence_scope: ANALYSIS
    ownership_scope: ANALYTICAL_TARGET
```

---

## F04. Cell Design & Form Factor
