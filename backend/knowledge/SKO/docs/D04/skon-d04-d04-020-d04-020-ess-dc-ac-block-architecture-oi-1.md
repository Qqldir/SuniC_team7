---
id: skon-d04-d04-020-d04-020-ess-dc-ac-block-architecture-oi-1
title: D04-020 — ESS DC/AC Block Architecture — OI Metadata
summary: ESS DC/AC 블록에 필요한 기술 역량 및 성과지표와 배터리 기술의 개발 상태를 기술한 운영 메타데이터.
tags: [d04, technology, schema, table, "xref:d00"]
keywords: [OI 메타데이터, PCS / 전력변환, 고-니켈 NCM, 배터리 성숙도 단계, BaaS AI, 기술 의존성 그래프, 상용화 / COMMERCIALIZED, 에너지 저장 시스템, BMS-PCS 프로토콜, 에너지저장, 전력변환, 성숙도평가, 배터리기술, 상용화현황, NCM양극재, BMS프로토콜, KPI, SOH/RUL예측, 기술로드맵]
related: []
priority: normal
domain: D04
section: D04-020
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Detailed Technology Master > D04-020 — ESS DC/AC Block Architecture
tokens: 3717
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Detailed Technology Master > D04-020 — ESS DC/AC Block Architecture

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  external_capability_needs:
    - Modular bidirectional PCS
    - Open BMS-PCS protocol
    - Grid-forming inverter
    - Cybersecure edge controller
    - Digital commissioning platform
    - System-level warranty analytics
    - Multi-vendor EMS integration
    - Container digital twin

  poc_kpis:
    - Round-trip efficiency
    - Commissioning time
    - System availability
    - PCS response time
    - Interoperability success rate
    - Cybersecurity vulnerability count
    - Maintenance cost
```

---

# D04-08. Detailed Technology Relationship Graph

```text
High-Nickel NCM
├─ ENABLES → High-Energy-Density EV Battery
├─ REQUIRES → Coating and Doping
├─ EVOLVES_TO → Ultrahigh-Nickel Single-Crystal Cathode
└─ HAS_TRADEOFF → Thermal Stability

High-Voltage Mid-Nickel
├─ REDUCES → Nickel and Cobalt Exposure
├─ USES → High-Voltage Operation
├─ REQUIRES → Electrolyte Interface Protection
└─ APPLIED_TO → Pouch-Integrated Prismatic Cell

Silicon–Graphite Anode
├─ ENABLES → Higher Capacity
├─ HAS_VARIANT → Dual-Layer Anode
├─ CONNECTS_TO → Magnetic Alignment
└─ HAS_PAIN_POINT → Volume Expansion

Dual-Layer Anode
└─ ENABLES → SF+ Battery

Magnetic Alignment
└─ ENABLES → Advanced SF Battery

SUFast
├─ USES → Dual-Layer Coating
├─ USES → Charging Protocol Simulation
└─ ENABLES → Hyper Fast Battery

Large-Surface Cooling
├─ SUPPORTS → Thermal Propagation Prevention
├─ SUPPORTS → Pouch CTP
└─ SUPPORTS → Pouch-Integrated Prismatic

BaaS AI
├─ ESTIMATES → SOH
├─ ESTIMATES → RUL
├─ ESTIMATES → Residual Value
└─ SUPPORTS → Reuse and Recycling Decision

GRIDON Gen 2
├─ SUPPORTS → DC Block
├─ SUPPORTS → AC Block
├─ USES → EIS-Based BMS
└─ USES → Coolant-Based Fire Suppression
```

---

# D04-09. Detailed Technology Maturity Update

| Technology                      | 공개 상태          | D04 성숙도                   | 양산·고객 근거 |
| ------------------------------- | -------------- | ------------------------- | -------- |
| High-Nickel NCM                 | 차량 적용·양산       | COMMERCIALIZED            | 확인       |
| Ultrahigh-Nickel Single Crystal | 공동연구·논문        | RESEARCH                  | 미확인      |
| High-Voltage Mid-Nickel         | 시제품 공개         | PROTOTYPE                 | 미확인      |
| Silicon–Graphite Anode          | 제품기술 공개        | PRODUCT_TECHNOLOGY        | 일부       |
| Dual-Layer Anode                | SF+ 공개         | PRODUCT_TECHNOLOGY        | 고객 미공개   |
| Magnetic Alignment              | Advanced SF 적용 | PRODUCT_APPLIED           | 차량 적용 확인 |
| Large-Surface Cooling           | CTP 시제품        | PROTOTYPE                 | 양산 미확인   |
| Pouch-Integrated Prismatic      | 최종 성능검증        | PROTOTYPE_VALIDATION      | 미확인      |
| BaaS AI                         | 시범·협력 적용       | PILOT_APPLICATION         | 확인       |
| SOH/RUL Prediction              | 서비스·표준화        | PILOT_AND_STANDARDIZATION | 제한적      |
| DC Block                        | GRIDON 제품      | PRODUCT_INTEGRATED        | 생산계획     |
| AC Block                        | GRIDON Gen 2   | DEVELOPMENT               | 2027 목표  |

---

# D04-10. Technology Gap Register v1

```yaml
technology_gaps:

  - gap_id: GAP-D04-001
    technology: Ultrahigh-Nickel Single-Crystal Cathode
    gap:
      - Large-scale synthesis
      - Electrode calendering yield
      - Cost
      - Commercial cell validation
    priority: HIGH

  - gap_id: GAP-D04-002
    technology: High-Voltage Mid-Nickel
    gap:
      - High-voltage electrolyte durability
      - Gas suppression
      - Named OEM validation
      - Mass-production evidence
    priority: VERY_HIGH

  - gap_id: GAP-D04-003
    technology: Silicon–Graphite Anode
    gap:
      - Expansion
      - Initial efficiency
      - Long-term fast-charge life
    priority: VERY_HIGH

  - gap_id: GAP-D04-004
    technology: Magnetic Alignment
    gap:
      - Inline orientation measurement
      - High-speed process control
    priority: HIGH

  - gap_id: GAP-D04-005
    technology: Large-Surface Cooling
    gap:
      - Field reliability
      - Leak detection
      - Pack serviceability
      - Mass and cost
    priority: VERY_HIGH

  - gap_id: GAP-D04-006
    technology: Pouch-Integrated Prismatic
    gap:
      - Final validation
      - OEM certification
      - Mass-production yield
      - Long-term compression durability
    priority: VERY_HIGH

  - gap_id: GAP-D04-007
    technology: BaaS AI
    gap:
      - Current commercial scale
      - Cross-OEM data access
      - Explainability
      - Data standardization
    priority: HIGH

  - gap_id: GAP-D04-008
    technology: SOH and RUL Prediction
    gap:
      - Public accuracy metrics
      - Uncertainty quantification
      - Cross-vehicle transfer
    priority: VERY_HIGH

  - gap_id: GAP-D04-009
    technology: AC Block
    gap:
      - PCS partner
      - EMS interoperability
      - Grid certification
      - Integrated warranty
    priority: VERY_HIGH
```

---

## 이번 구간 완료

* D00 Source Library 추가 등록: `SRC-SKON-D04-014~020`
* `D04-07 Detailed Technology Master`

  * 하이니켈 NCM
  * 고전압 미드니켈
  * 실리콘-흑연 음극
  * 이중층 음극
  * 자기정렬 공정
  * 대면적 냉각
  * 파우치 통합 각형
  * BaaS AI
  * SOH·RUL·잔존가치 예측
  * ESS DC·AC 블록
* Detailed Technology Relationship Graph
* Technology Maturity Update
* Technology Gap Register v1

## 다음 시작점

`D04-11 Safety & Thermal Technology Master`

다음 구간:

```text
D04-11 Safety & Thermal Technology Master
├── Cell-Level Safety
├── Z-Folding and Separator Safety
├── S-Pack / S-Pack+
├── Thermal Propagation Barriers
├── Bottom Cooling
├── Immersion Cooling
├── Directional Venting
├── Wireless BMS
├── Abnormality Detection
└── VIB ESS Safety Technology
```

[1]: https://askinno.com/global/archives/20224?utm_source=chatgpt.com "SK On to Showcase Expanded Battery Portfolio at InterBattery 2025 - Ask Inno Global"
[2]: https://askinno.com/global/archives/153680?utm_source=chatgpt.com "SK On Unveils Breakthrough in Next-Generation Cathode Research - Ask Inno Global"
[3]: https://askinno.com/global/archives/154429?utm_source=chatgpt.com "[Battery Deep Dive] Part 7: Pouch-Integrated Prismatic Cell"
[4]: https://askinno.com/global/archives/153882?utm_source=chatgpt.com "[Battery Deep Dive] Part 4: Cell-to-Pack Technology - Ask Inno Global"
[5]: https://askinno.com/global/wp-content/uploads/sites/2/2022/09/2021-SKI-ESG-Report_en.pdf?utm_source=chatgpt.com "ESG Report 2021"
[6]: https://askinno.com/global/archives/8067?utm_source=chatgpt.com "SK On develops battery diagnosis technology that allows electric ..."
[7]: https://askinno.com/global/archives/154786?utm_source=chatgpt.com "SK On Expands U.S. ESS Push at ACP CLEANPOWER 2026"
[8]: https://askinno.com/global/archives/2557?utm_source=chatgpt.com "SK Innovation recruits more talents for next-generation battery ..."
[9]: https://askinno.com/global/archives/154332?utm_source=chatgpt.com "[Battery Deep Dive] Part 5: Seven-Minute Fast Charging"
[10]: https://askinno.com/wp-content/uploads/2022/07/2021-SKI-ESG-Report_kr.pdf?utm_source=chatgpt.com "ESG Report 2021"

---

# SK온 D04 Technology Taxonomy

## Part 3. Safety & Thermal Technology Master

**문서 버전:** D04 v1.2
**기준일:** 2026-07-30
**이전 완료 지점:** `D04-10 Technology Gap Register v1`

---

# D04-RP-004. 추가 Source Library 등록

## SRC-SKON-D04-021 — Z-Folding 기술

```yaml
source_id: SRC-SKON-D04-021
title: Z-folding, a Technique that Ensures the Safety of SK Innovation's Batteries
publisher: SK Innovation Newsroom
source_type: Official Technology Article
publication_date: 2021-07-09
access_date: 2026-07-30
language: English
reliability_grade: A+
claim_type: COMPANY_TECHNOLOGY_DISCLOSURE
accessibility_status: OPEN_CONFIRMED

covered_technologies:
  - Z-Folding
  - Separator Stacking
  - Electrode Alignment
  - Internal Short-Circuit Prevention
  - Pouch Cell Assembly
```

Z-Folding은 길게 이어진 분리막이 양극과 음극 사이를 지그재그로 오가며 전극을 감싸도록 적층하는 조립기술이다. SK온은 이 방식이 전극 가장자리의 정렬오차와 양극·음극 직접 접촉 가능성을 낮추고, 고속 생산에서도 정밀한 적층을 가능하게 한다고 설명한다. ([ASK Inno][1])

---

## SRC-SKON-D04-022 — S-Pack

```yaml
source_id: SRC-SKON-D04-022
title: SK On S-Pack and Battery Safety Technologies
publisher: SK Innovation Newsroom
source_type: Official Product and Technology Article
publication_date:
  first_public_disclosure: 2022
  ces_product_article: 2023
access_date: 2026-07-30
language:
  - Korean
  - English
reliability_grade: A+
claim_type: COMPANY_PRODUCT_DISCLOSURE
accessibility_status: OPEN_CONFIRMED

covered_technologies:
  - S-Pack
  - Cell-to-Pack
  - Thermal Blocking
  - Gas-Path Control
  - Cell Volume Utilization
```

S-Pack은 SK온의 CTP 기술이 적용된 팩 개념으로, 내부 구조와 부품을 간소화해 셀 탑재 공간을 높이고, 열 차단과 가스 경로 제어를 통해 특정 셀에서 시작된 이상이 팩 전체로 확산되는 것을 억제하도록 설계됐다. 공개된 자료는 전시 모델과 기술 개념을 확인해 주지만 특정 양산차 적용은 별도로 밝히지 않는다. ([ASK Inno][2])

---

## SRC-SKON-D04-023 — S-Pack+

```yaml
source_id: SRC-SKON-D04-023
title: SK On to Showcase Expanded Battery Portfolio at InterBattery 2025
publisher: SK Innovation Newsroom
source_type: Official Product and Technology Release
publication_date: 2025-02-23
access_date: 2026-07-30
language:
  - Korean
  - English
reliability_grade: A+
claim_type: COMPANY_PRODUCT_DISCLOSURE
accessibility_status: OPEN_CONFIRMED

covered_technologies:
  - S-Pack+
  - Cell-to-Pack
  - Electrical Insulation
  - Gas and Dust Discharge
  - Thermal Insulation
  - Module-Function Integration
```

S-Pack+는 모듈이 담당하던 일부 기능을 팩으로 통합한 CTP형 제품 개념이다. SK온은 제조공정 단순화와 제품설계 최적화를 통한 원가절감 가능성, 높은 전기절연성, 가스·분진 배출구조 및 단열기술을 핵심 특징으로 제시했다. 공개 상태는 전시·기술 공개이며 양산차 또는 고객 적용은 확인되지 않았다. ([ASK Inno][3])

---

## SRC-SKON-D04-024 — EV 액침냉각 및 무선 BMS

```yaml
source_id: SRC-SKON-D04-024
title: SK On and SK Enmove Unveil EV Battery Immersion Cooling Technology
publisher: SK Innovation Newsroom
source_type: Official Joint Technology Release
publication_date: 2025-03-03
access_date: 2026-07-30
language:
  - Korean
  - English
reliability_grade: A+
claim_type: JOINT_TECHNOLOGY_DISCLOSURE
accessibility_status: OPEN_CONFIRMED

covered_technologies:
  - EV Battery Immersion Cooling
  - Insulating Thermal Fluid
  - Wireless BMS
  - Cell-Tab Wireless Chip
  - Thermal-Fluid Flow Path
  - Thermal Propagation Mitigation
```

SK온과 SK엔무브는 절연성 냉각 플루이드를 팩 내부에 순환시켜 셀과 직접 접촉하게 하는 EV용 액침냉각 기술을 공개했다. SK온의 무선 BMS는 셀 탭의 무선 칩이 수집한 정보를 모듈 안테나를 통해 BMS에 전달하는 구조이며, 배선을 줄여 플루이드 유동을 방해하는 요소를 최소화하는 방향으로 개발됐다. ([ASK Inno][4])

---

## SRC-SKON-D04-025 — 배터리 안전 전시 및 3대 폼팩터

```yaml
source_id: SRC-SKON-D04-025
title: SK On Unveils Diverse Battery Portfolio at InterBattery 2025
publisher: SK Innovation Newsroom
source_type: Official Exhibition Report
publication_date: 2025-03-07
access_date: 2026-07-30
language: English
reliability_grade: A+
claim_type: COMPANY_EXHIBITION_DISCLOSURE
accessibility_status: OPEN_CONFIRMED

covered_technologies:
  - Wireless BMS
  - EV Immersion Cooling
  - S-Pack+
  - Z-Folding in Prismatic Cells
  - Pouch, Prismatic and Cylindrical Form Factors
```

인터배터리 2025에서 SK온은 무선 BMS와 EV 액침냉각, S-Pack+를 배터리 안전기술로 함께 전시했다. 따라서 세 기술은 각각 독립된 기술이면서도 `진단·열관리·팩 구조`를 결합하는 통합 안전 아키텍처로 연결해 관리해야 한다. ([ASK Inno][5])

---

## SRC-SKON-D04-026 — VIB 공동개발
