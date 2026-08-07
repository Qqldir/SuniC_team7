---
id: skon-d04-d04-077-d04-077-gel-polymer-electrolyte-curing-c-2
title: D04-077 — Gel Polymer Electrolyte Curing Control — OI Metadata (2)
summary: "차세대 배터리 기술 개발을 위한 8개 혁신 과제(롤투롤 코팅, 광소결, 황화물 전해질, 고체전지 인터페이스 등)의 문제점, 기술요구사항, 우선순위를 담은 메타데이터"
tags: [d04, technology, schema, table, "xref:d00", "xref:d17", "xref:d03"]
keywords: [고체 전해질, 황화물 전해질, 산화물 전해질, 단결정 양극, 전극 인터페이스, Roll-to-Roll, 광자 소성, 차세대 배터리, Roll-to-roll, 고체 전지, ASSB, 단결정 cathode, LMRO, 인터페이스, 스케일업]
related: []
priority: normal
domain: D04
section: D04-077
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Next-Generation Technology Master > D04-077 — Gel Polymer Electrolyte Curing Control
tokens: 3281
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Next-Generation Technology Master > D04-077 — Gel Polymer Electrolyte Curing Control

```yaml
oi_seeds:

  - seed_id: OI-SEED-D04-NEXT-001
    title: Roll-to-Roll SIPE Electrolyte Film
    problem:
      - Research-level polymer electrolyte must be converted into thin, uniform commercial film
    external_technology:
      - Single-ion polymer chemistry
      - Precision film coating
      - In-line conductivity inspection
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-NEXT-002
    title: Photonic-Sintered Oxide Electrolyte Pilot
    problem:
      - Conventional oxide sintering requires high temperature and long processing time
    external_technology:
      - Pulsed-light equipment
      - Optical absorber formulation
      - Crack inspection
      - Roll-to-roll handling
    priority: HIGH

  - seed_id: OI-SEED-D04-NEXT-003
    title: Closed Sulfide Electrolyte Manufacturing System
    problem:
      - Moisture exposure causes electrolyte degradation and hazardous gas generation
    external_technology:
      - Closed powder transfer
      - H2S sensor and scrubber
      - Ultra-dry production module
      - Electrolyte recycling
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-NEXT-004
    title: Artificial Lithium Interphase Scale-Up
    problem:
      - Lithium surface protection validated in research cells requires continuous large-area processing
    external_technology:
      - Air-free surface cleaning
      - Artificial SEI coating
      - Interphase metrology
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-NEXT-005
    title: Solid-State Interface Inspection Platform
    problem:
      - Buried solid-solid interface defects are difficult to inspect nondestructively
    external_technology:
      - X-Ray CT
      - Ultrasound
      - Acoustic microscopy
      - Physics-informed defect reconstruction
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-NEXT-006
    title: Smart Pressure-Controlled ASSB Stack
    problem:
      - Contact must be maintained without excessive weight or electrolyte fracture
    external_technology:
      - Thin pressure sensor
      - Lightweight spring structure
      - Pressure-electrochemistry digital twin
      - Closed-loop compression
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-NEXT-007
    title: LMRO–Sulfide Stable Cathode Interface
    problem:
      - Oxygen release from LMRO can oxidize sulfide electrolyte
    external_technology:
      - Oxygen-suppressing coating
      - Gradient cathode interface
      - Operando gas and spectroscopy analysis
    priority: HIGH

  - seed_id: OI-SEED-D04-NEXT-008
    title: Large Single-Crystal Cathode Scale-Up
    problem:
      - High-density single-crystal performance must be reproduced at precursor and electrode scale
    external_technology:
      - Continuous crystal synthesis
      - Particle-quality AI
      - Crack-free calendering
      - Operando gas analysis
    priority: HIGH

  - seed_id: OI-SEED-D04-NEXT-009
    title: Rapid GPE Curing and Conversion Monitoring
    problem:
      - Short curing increases throughput but residual monomer can degrade the cathode interface
    external_technology:
      - Rapid volumetric heating
      - Spectroscopic conversion sensor
      - Curing digital twin
    priority: HIGH

  - seed_id: OI-SEED-D04-NEXT-010
    title: Lithium Inventory Management for Advanced Anodes
    problem:
      - Silicon-rich and next-generation anodes lose usable lithium during early cycles
    status:
      - Analytical candidate
      - No confirmed SK On prelithiation program
    external_technology:
      - Safe prelithiation material
      - Lithium dosing control
      - Initial-efficiency prediction
    priority: MEDIUM_HIGH
```

---

## 이번 구간 완료

* D00 연계 Source Library 추가: `SRC-SKON-D04-042~046`
* 학술 원문 Source Library 추가: `SRC-RES-D04-047~051`
* `D04-31 Next-Generation Materials & Electrochemistry Taxonomy`
* Technology Master 14개

  * 폴리머-산화물 복합 전해질
  * SIPE
  * LLZO 산화물 전해질
  * 초고속 광소결
  * 황화물 고체전해질
  * 리튬메탈 음극
  * 리튬메탈 인공계면
  * 고체-고체 계면
  * 고압 스택 관리
  * LMRO 단결정 양극
  * 초고니켈 대형 단결정
  * 고전압 전해액·첨가제
  * GPE 경화제어
  * 프리리치에이션 목표역량
* 전해질 비교표
* 계면 관계 그래프
* 기술 성숙도 맵
* 전고체 로드맵 변경이력 정규화
* Next-Generation Gap Register
* D17 연결용 OI Seed 10건

## 다음 시작점

`D04-39 Technology Benchmark & External Capability Mapping`

```text
D04-39 Technology Benchmark & External Capability Mapping
├── Solid Power
├── QuantumScape
├── Toyota
├── Samsung SDI
├── LG Energy Solution
├── CATL
├── Factorial Energy
├── ProLogium
├── SES AI
├── 24M Technologies
├── StoreDot
└── Materials·Equipment·AI Startup Capability Map
```

[1]: https://askinno.com/global/archives/153768 "[Battery Deep Dive] Part 1: Solid-State Batteries - Ask Inno Global"
[2]: https://askinno.com/global/archives/18283 "SK On develops polymer electrolytes for lithium metal batteries - Ask Inno Global"
[3]: https://askinno.com/global/archives/15664 "SK On develops new solid electrolyte with top-level lithium-ion conductivity - Ask Inno Global"
[4]: https://askinno.com/global/archives/19985 "SK On Unveils R&D Breakthroughs on All-Solid-State Batteries - Ask Inno Global"
[5]: https://askinno.com/global/archives/21163 "SK On Presents New Research Advances in Solid-state Batteries - Ask Inno Global"
[6]: https://pubs.acs.org/doi/10.1021/acsenergylett.5c00656?utm_source=chatgpt.com "Surface-Modified Lithium Enabling High-Performance All-Solid-State Lithium Metal Batteries | ACS Energy Letters"
[7]: https://pubs.acs.org/doi/10.1021/acsenergylett.4c02861?utm_source=chatgpt.com "Instantaneous Photonic Sintering Process for Scalable Fabrication of a 3D Garnet Electrolyte Scaffold for Solid-State Batteries | ACS Energy Letters"
[8]: https://pubs.acs.org/doi/10.1021/acs.chemmater.4c01762?utm_source=chatgpt.com "Active–Inactive Molten Salt Synthesis of Li- and Mn-Rich Layered Oxide Single Crystals as Cathode Materials for All-Solid-State Batteries | Chemistry of Materials"
[9]: https://onlinelibrary.wiley.com/doi/10.1002/ange.202424568?utm_source=chatgpt.com "Residual Monomer‐Induced Side Reactions in Gel Polymer Electrolytes: Unveiled High‐Ni Cathode Failure in Lithium Batteries - Choi - 2025 - Angewandte Chemie - Wiley Online Library"
[10]: https://askinno.com/global/archives/153680?utm_source=chatgpt.com "SK On Unveils Breakthrough in Next-Generation Cathode Research - Ask Inno Global"
[11]: https://askinno.com/global/archives/20224?utm_source=chatgpt.com "SK On to Showcase Expanded Battery Portfolio at InterBattery 2025 - Ask Inno Global"

---

# SK온 D04 Technology Taxonomy

## Part 7. Technology Benchmark & External Capability Mapping

**문서 버전:** D04 v1.6
**기준일:** 2026-08-01
**이전 완료 지점:** `D04-38 Next-Generation OI Seeds`

---

# D04-DQ-001. Source Grade 정규화

```yaml
source_grade_policy:

  A_PLUS:
    - Government publication
    - Regulatory document
    - Patent
    - Peer-reviewed paper
    - Annual or sustainability report
    - Official filing

  A:
    - Official corporate press release
    - Official product page
    - Official technology page
    - Official investor presentation not treated as filing

  B_PLUS:
    - Reuters
    - Bloomberg
    - Financial Times
    - Wall Street Journal

normalization_action:
  - 기존 D03·D04에서 A+로 입력된 기업 뉴스룸·제품 페이지는 A로 변경
  - 출처 등급만 변경하고 원문 내용과 엔티티 관계는 유지
```

---

# D04-RP-008. External Benchmark Source Library

| Source ID       | 기업·기관                | 핵심 근거                        | 등급 |
| --------------- | -------------------- | ---------------------------- | -: |
| SRC-EXT-D04-052 | Solid Power          | SK온 전고체 파일럿 라인 설치·검수 완료      |  A |
| SRC-EXT-D04-053 | Factorial            | SK온과 FEST 제조 타당성 검토 MOU      |  A |
| SRC-EXT-D04-054 | Factorial·Stellantis | FEST 셀의 개발차량 통합·도로시험         |  A |
| SRC-EXT-D04-055 | QuantumScape         | Cobra 기반 QSE-5 B1 샘플 출하      |  A |
| SRC-EXT-D04-056 | Toyota·Idemitsu      | 황화물 고체전해질 공급망·양산 협력          |  A |
| SRC-EXT-D04-057 | Samsung SDI          | SolidStack·S-Line·BMW 검증 협력  |  A |
| SRC-EXT-D04-058 | LG Energy Solution   | 전고체·무음극·건식전극 로드맵             |  A |
| SRC-EXT-D04-059 | CATL                 | Naxtra 나트륨이온 양산·적용 확대        |  A |
| SRC-EXT-D04-060 | ProLogium            | 무기계 고체전해질·세라믹 분리막 플랫폼        |  A |
| SRC-EXT-D04-061 | SES AI               | Molecular Universe·배터리 소재 AI |  A |
| SRC-EXT-D04-062 | 24M                  | SemiSolid·ETOP·Impervio 기술군  |  A |
| SRC-EXT-D04-063 | StoreDot             | 실리콘 중심 XFC 셀·차량 충전 시연        |  A |

---

## SRC-EXT-D04-052 — Solid Power·SK온

```yaml
source_id: SRC-EXT-D04-052
title: Solid Power Reports First Quarter 2026 Results
publisher: Solid Power
publication_date: 2026-05-05
access_date: 2026-08-01
source_type: Official Business Update
reliability_grade: A

confirmed_updates:
  - SK On pilot cell line site-acceptance testing completed
  - Solid Power technology line installed in South Korea
  - Continuous sulfide-electrolyte pilot line commissioning targeted by end-2026
  - Commercial-scale electrolyte production partners being explored in South Korea
```

Solid Power는 2026년 1분기 SK온 전고체 파일럿 셀 라인의 현장인수시험을 완료했다고 발표했다. 또한 황화물계 고체전해질 연속생산 파일럿 라인의 주요 설비 검수를 마쳤으며, 2026년 말 가동을 목표로 하고 있다. 이는 SK온과 Solid Power의 관계가 단순 연구 MOU를 넘어 **셀 파일럿 설비 설치와 공정 이전 단계**까지 진행됐음을 의미한다. ([Solid Power][1])

---

## SRC-EXT-D04-053 — Factorial·SK온 신규 MOU

```yaml
source_id: SRC-EXT-D04-053
title: Factorial and SK On Sign MoU to Explore Solid-State Battery Manufacturing
publisher: Factorial
publication_date: 2026-07-29
access_date: 2026-08-01
source_type: Official Partnership Release
reliability_grade: A

agreement_status:
  type: NON_BINDING_MOU
  binding_supply_contract: false
  licensing_agreement: false

collaboration_scope:
  - FEST manufacturing feasibility
  - Use of SK On lithium-ion manufacturing infrastructure
  - Solid-state process integration
  - Manufacturing-readiness assessment
```

2026년 7월 29일 Factorial과 SK온은 Factorial의 FEST 전고체 기술을 SK온의 기존 리튬이온 생산 인프라에서 제조할 수 있는지 공동 평가하는 MOU를 체결했다. 이번 협력은 비구속적 MOU이므로 기술이전·공급계약·양산결정으로 해석해서는 안 되지만, SK온의 전고체 외부협력 축이 Solid Power에 이어 Factorial까지 확대됐다는 점에서 중요하다. ([Factorial Energy][2])
