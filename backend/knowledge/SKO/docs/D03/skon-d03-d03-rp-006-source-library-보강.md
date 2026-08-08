---
id: skon-d03-d03-rp-006-source-library-보강
title: 006. Source Library 보강
summary: "SK온의 자동차·ESS 배터리 제품, 급속충전·다양한 셀 구조·전고체 기술 관련 공식 소스 5건의 신뢰도와 적용 범위"
tags: [d03, product, schema]
keywords: [차량용배터리, 급속충전, Prismatic, 전고체배터리, ESS, BMS, 기술신뢰성, 공식자료, 하이브리드셀, 배터리 셀, 전고체, 각형 셀, 파우치, Hyper Fast, 고체전해질, R&D 제품]
related: []
priority: normal
domain: D03
section: D03-RP
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 2984
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# SK온 D03 Products & Solutions

## Part 5. Product Relationship Graph·Entity Master·Chunk Library

**문서 버전:** D03 v1.4
**기준일:** 2026-07-30
**이전 완료 지점:** `D03-07 Competitive Product Mapping`

---

# D03-RP-006. Source Library 보강

## SRC-SKON-D03-051 — SK온 공식 R&D 제품 범위

```yaml
source_id: SRC-SKON-D03-051
title: R&D – Research Areas and Key Projects of the SK On Future Technology Institute
publisher: SK Innovation
source_type: Official R&D Page
publication_date: null
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - Automotive Battery Cell
  - Automotive Battery Module
  - Automotive Battery Pack
  - Automotive BMS
  - ESS Cell
  - ESS Module
  - ESS Rack
  - ESS System
  - ESS BMS
  - Solid-State Battery Material
  - Solid-State Battery Cell
```

SK이노베이션 공식 R&D 페이지는 SK온의 개발 범위를 자동차용 셀·모듈·팩·BMS와 ESS용 셀·모듈·랙·시스템·BMS까지 명시한다. 전고체 분야에서는 고체전해질, 리튬메탈 및 전고체 셀을 개발 대상으로 제시한다. ([SK Innovation][1])

---

## SRC-SKON-D03-052 — Hyper Fast Battery

```yaml
source_id: SRC-SKON-D03-052
title: Battery Deep Dive Part 5 – Seven-Minute Fast Charging
publisher: SK Innovation Newsroom
source_type: Official Technology Article
publication_date: 2026-04-09
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - SF Battery
  - SF+ Battery
  - Advanced SF Battery
  - Hyper Fast Battery
  - SUFast
```

공식 자료는 SK온의 급속충전 기술 계보를 설명하며, Hyper Fast Battery에 대해 충전상태 10%에서 80%까지 7분 미만이라는 기술 성능을 제시한다. 이는 공개 기술 시제품의 성능이며 양산차 적용 성능과 구분한다. ([ASK Inno][2])

---

## SRC-SKON-D03-053 — On-Vent Prismatic Cell

```yaml
source_id: SRC-SKON-D03-053
title: Battery Deep Dive Part 6 – On-Vent Prismatic Cell
publisher: SK Innovation Newsroom
source_type: Official Technology Article
publication_date: 2026-04-13
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - On-Vent Prismatic Cell
  - Configurable Vent
  - Laser Vent Processing
  - Thermal Propagation Mitigation
```

On-Vent 셀은 각형 셀의 벤트 위치를 설계 목적에 맞게 구성하는 기술이다. 공식 자료는 압력 반복시험에서 6,000회를 넘는 반복 후에도 목표 파열압력을 충족했다고 설명하지만, 양산차 적용과 고객계약은 별도로 확인되지 않았다. ([ASK Inno][3])

---

## SRC-SKON-D03-054 — Pouch-Integrated Prismatic Cell

```yaml
source_id: SRC-SKON-D03-054
title: Battery Deep Dive Part 7 – Pouch-Integrated Prismatic Cell
publisher: SK Innovation Newsroom
source_type: Official Technology Article
publication_date: 2026-04-17
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - Pouch-Integrated Prismatic Cell
  - Hybrid Cell Architecture
  - Prismatic Product Platform
```

파우치 통합 각형 셀은 SK온의 파우치 기술 경험과 각형 외장 구조를 결합한 하이브리드 개념이다. 회사는 셀 자체 성능뿐 아니라 셀 배열과 팩 구조를 포함한 시스템 경쟁력 강화를 개발 방향으로 제시한다. ([ASK Inno][4])

---

## SRC-SKON-D03-055 — 전고체 파일럿 플랜트

```yaml
source_id: SRC-SKON-D03-055
title: SK On Opens All-Solid-State Battery Pilot Plant
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2025
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - All-Solid-State Battery Pilot Plant
  - Sulfide ASSB
  - Polymer-Oxide Composite Battery
  - 2029 Commercialization Target
```

SK온은 대전 전고체 파일럿 플랜트 완공 사실과 2029년 상용화 목표를 공개했다. 상용화 연도는 기업 목표이므로 실제 양산개시를 의미하는 `COMMERCIAL` 상태가 아니라 `CORPORATE_TARGET`으로 저장한다. ([ASK Inno][5])

---

## SRC-SKON-D03-056 — BaaS AI

```yaml
source_id: SRC-SKON-D03-056
title: SK On Develops Battery Diagnosis Technology
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2021-11-25
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - BaaS AI
  - Battery Diagnosis
  - Battery Abnormality Detection
  - Residual Value Assessment
  - EV Infra
  - SoftBerry
```

BaaS AI는 주행·충전 데이터를 기반으로 배터리 상태와 이상 여부, 잔존가치 등을 분석하는 SK온의 진단 기술이다. 최초 공개 당시 EV Infra 애플리케이션을 통한 서비스가 운영됐지만, 현재 전체 유료고객과 매출 규모는 공개되지 않았다. ([ASK Inno][6])

---

## SRC-SKON-D03-057 — GRIDON

```yaml
source_id: SRC-SKON-D03-057
title: Powering the Future of Energy – SK On ESS GRIDON
publisher: SK Innovation Newsroom
source_type: Official Product Article
publication_date: 2026-05-08
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - GRIDON
  - EIS-Based BMS
  - Coolant Immersion
  - Dual-Valve Structure
```

GRIDON은 안전성·원가효율·운전성능을 중심 가치로 하는 SK온의 ESS 솔루션 브랜드다. 핵심 기술로 EIS 기반 예측진단 BMS와 이중 밸브 구조의 냉각수 침지 기술이 제시된다. ([ASK Inno][7])

---

## SRC-SKON-D03-058 — GRIDON Gen 2

```yaml
source_id: SRC-SKON-D03-058
title: SK On Expands U.S. ESS Push at ACP CLEANPOWER 2026
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2026-06-04
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - GRIDON Gen 1
  - GRIDON Gen 2
  - DC Block
  - AC Block
  - AI Data Center ESS
```

GRIDON Gen 2는 DC 블록과 AC 블록을 모두 지원하도록 개발되고 있으며, 이전 세대보다 DC 블록 컨테이너당 에너지용량을 평균 15% 높이는 것을 목표로 한다. 상업생산 목표는 2027년 3분기다. ([ASK Inno][8])

---

## SRC-SKON-D03-059 — CTP 개발

```yaml
source_id: SRC-SKON-D03-059
title: Battery Deep Dive Part 4 – Cell-to-Pack Technology
publisher: SK Innovation Newsroom
source_type: Official Technology Article
publication_date: 2026
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - Pouch-Type CTP
  - Module-Less Architecture
  - CTP Task Force
  - Thermal Propagation Design
```

SK온은 파우치형 CTP 기술을 발전시키기 위해 미래기술원 내 전담 조직을 운영하고 있다. CTP는 모듈 구조를 축소하거나 제거해 팩 공간효율을 높일 수 있지만, 셀 간 열전파 차단과 정비성 및 구조 안전성이 함께 해결돼야 한다. ([ASK Inno][9])

---

## SRC-COMP-D03-060 — CATL Shenxing PLUS

```yaml
source_id: SRC-COMP-D03-060
title: CATL Unveils Shenxing PLUS
publisher: CATL
source_type: Official Product Release
publication_date: 2024-04-25
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - CATL Shenxing PLUS
  - LFP 4C Fast Charging
  - CTP 3.0
  - 205 Wh/kg System Energy Density
```

CATL은 Shenxing PLUS에 LFP 화학계, 4C 충전 및 205Wh/kg의 시스템 에너지밀도를 제시한다. 제조사가 공개한 차량 주행거리와 충전주행거리 수치는 시험조건이 동일하지 않으므로 SK온 제품과 직접 순위화하지 않는다. ([CATL][10])

---

## SRC-COMP-D03-061 — CATL TENER

```yaml
source_id: SRC-COMP-D03-061
title: CATL Unveils TENER
publisher: CATL
source_type: Official ESS Product Release
publication_date: 2024-04-09
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - CATL TENER
  - 6.25 MWh Container
  - Five-Year Zero-Degradation Claim
  - 430 Wh/L ESS Cell
```

TENER는 20피트 컨테이너 기준 6.25MWh와 LFP ESS 셀 430Wh/L를 공개한 CATL의 제품이다. 초기 5년 무열화는 CATL의 제품 주장으로 저장하고 독립 검증결과와 구분한다. ([CATL][11])

---

## SRC-COMP-D03-062 — LG에너지솔루션 LFP Pouch

```yaml
source_id: SRC-COMP-D03-062
title: LG Energy Solution to Supply LFP EV Batteries to Ampere
publisher: LG
source_type: Official Press Release
publication_date: 2024-07-02
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - LGES LFP Pouch Battery
  - Ampere
  - 39 GWh Supply Contract
  - Pouch-Type CTP
```

LG에너지솔루션은 Ampere에 2025년 말부터 5년간 약 39GWh의 파우치형 LFP 배터리를 공급하기로 했다. 이는 SK온 EV용 LFP 플랫폼의 상용화 수준을 평가할 때 직접적인 벤치마크다. ([LG][12])

---

## SRC-COMP-D03-063 — Samsung SBB 1.7

```yaml
source_id: SRC-COMP-D03-063
title: Samsung SDI Debuts New SBB Products
publisher: Samsung SDI
source_type: Official ESS Product Release
publication_date: 2025
access_date: 2026-07-30
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

supported_entities:
  - Samsung SBB 1.7
  - Samsung SBB 2.0
  - 6.14 MWh Container
  - NCA ESS
  - LFP ESS
```

삼성SDI의 SBB 1.7은 20피트 컨테이너 기준 6.14MWh이며, 이전 제품보다 약 17% 높은 에너지밀도를 제시한다. SBB 2.0은 LFP 셀 기반 제품군으로 공개됐다. ([삼성SDI 뉴스룸][13])

---
