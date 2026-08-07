---
id: skon-d03-d03-rp-003-추가-검증-자료-등록
title: 003. 추가 검증 자료 등록
summary: SK온의 배터리와 ESS 제품에 대한 공식 검증 자료 4건을 등록하고 데이터 버전 관리 기준을 제시한다.
tags: [d03, product, schema, "xref:d04", "xref:d05", "xref:d06", "xref:d15"]
keywords: [배터리, 급속충전, 에너지밀도, GRIDON, ESS, SF Battery, Hyper Fast Battery, BMS, 소스 라이브러리, 데이터 조정, Advanced SF, 냉각 침지 기술, 데이터 조정 규칙]
related: []
priority: normal
domain: D03
section: D03-RP
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 3566
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# SK온 D03 Products & Solutions

## Part 2. Source Library 보강 및 Product Master 확장

**문서 버전:** D03 v1.1
**기준일:** 2026-07-30
**이전 완료 지점:** `SERV-SKON-BAAS-001 Battery Diagnosis Service`

---

# D03-RP-003. 추가 검증 자료 등록

## SRC-SKON-D03-015 — 급속충전 제품 로드맵

```yaml
source_id: SRC-SKON-D03-015
title: "[Battery Deep Dive] Part 5: Seven-Minute Fast Charging"
publisher: SK Innovation Newsroom
source_type: Official Corporate Technology Article
publication_date: 2026
access_date: 2026-07-30
language: English
reliability_grade: A+
access_status: OPEN_CONFIRMED

covered_entities:
  - SF Battery
  - SF+ Battery
  - Advanced SF Battery
  - Hyper Fast Battery
  - SUFast
  - Magnetic Alignment Process

primary_domains:
  - D03
  - D04
  - D05
  - D06
  - D15
  - D16
  - D17
```

공식 자료는 SK온의 급속충전 제품 계보를 `SF Battery → SF+ Battery → Advanced SF Battery → Hyper Fast Battery`로 설명한다. SF+는 10%에서 80%까지의 충전시간을 15분으로 줄였고, Advanced SF는 기존 SF 대비 에너지밀도를 8% 높이면서 급속충전 성능을 유지했다. 2026년 공개된 Hyper Fast Battery는 10%에서 80%까지 7분 이내 충전, 650Wh/L의 에너지밀도 및 7분 충전 기준 450km 이상 주행 가능성을 제시한다. 다만 차량 주행거리는 차량 효율과 시험조건에 따라 달라지므로 셀 자체의 절대 성능값으로 일반화하지 않는다. ([ASK Inno][1])

---

## SRC-SKON-D03-016 — Advanced SF 초기 공개자료

```yaml
source_id: SRC-SKON-D03-016
title: Advanced SF Battery Official Release
publisher: SK On
source_type: Official Press Release
publication_date: 2024-03
access_date: 2026-07-30
language: Korean
reliability_grade: A+
access_status: DIRECT_PAGE_INTERMITTENT

key_claims:
  - 기존 SF 대비 에너지밀도 향상
  - 급속충전 시간 유지
```

SK온 공식 보도자료 검색 색인에는 Advanced SF 배터리가 기존 SF 대비 에너지밀도를 약 9% 높이면서 18분 급속충전 성능을 유지했다고 기록돼 있다. 이후 2026년 공식 기술 콘텐츠는 개선 폭을 8%로 표기한다. 따라서 DB에서는 **최신 공식 자료의 8%를 기준값으로 채택**하고, 9%는 초기 발표값으로 별도 보존한다. ([SK ON][2])

```yaml
data_reconciliation:
  metric: energy_density_improvement_vs_original_sf
  initial_disclosure: approximately_9_percent
  latest_official_disclosure: 8_percent
  canonical_value: 8_percent
  reconciliation_rule: USE_LATEST_OFFICIAL_SOURCE
```

---

## SRC-SKON-D03-017 — GRIDON 공식 제품 소개

```yaml
source_id: SRC-SKON-D03-017
title: "[Inside ESS] Powering the Future of Energy SK On ESS: GRIDON"
publisher: SK Innovation Newsroom
source_type: Official Product Article
publication_date: 2026-05-08
access_date: 2026-07-30
language: English
reliability_grade: A+
access_status: OPEN_CONFIRMED

covered_entities:
  - GRIDON
  - EIS-Based BMS
  - Coolant Immersion Technology
  - Dual-Valve Structure

primary_domains:
  - D03
  - D04
  - D06
  - D14
  - D15
  - D16
  - D17
```

GRIDON은 SK온이 공개한 ESS 대표 솔루션 브랜드다. 공식 자료는 제품의 핵심 목표를 안전성, 원가효율 및 운전성능으로 정의하며, EIS 기반 BMS를 통한 실시간 예측진단과 이중 밸브 구조의 냉각수 침지 기술을 핵심 구성요소로 제시한다. ([ASK Inno][3])

---

## SRC-SKON-D03-018 — GRIDON Gen 2

```yaml
source_id: SRC-SKON-D03-018
title: SK On Expands U.S. ESS Push at ACP CLEANPOWER 2026
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2026-06-04
access_date: 2026-07-30
language: English
reliability_grade: A+
access_status: OPEN_CONFIRMED

covered_entities:
  - GRIDON Gen 1
  - GRIDON Gen 2
  - DC Block
  - AC Block
  - EIS
  - Coolant-Based Fire Suppression

primary_domains:
  - D03
  - D04
  - D06
  - D07
  - D08
  - D16
  - D17
```

SK온은 GRIDON 1세대 제품의 미국 생산을 2026년 중 시작할 계획이라고 밝혔다. GRIDON Gen 2는 2027년 3분기 상업생산을 목표로 개발 중이며, DC 블록과 전력변환장치가 결합된 AC 블록을 모두 지원하는 구조다. 또한 컨테이너당 에너지용량을 평균 15% 높이고, EIS 및 냉각수 기반 화재억제 기술을 적용하도록 설계됐다. ([ASK Inno][4])

---

## SRC-SKON-D03-019 — BaaS 공식 사업 범위

```yaml
source_id: SRC-SKON-D03-019
title: SK On BaaS Business
publisher: SK On
source_type: Official Business Page
publication_date: null
access_date: 2026-07-30
language: English
reliability_grade: A+
access_status: DIRECT_PAGE_INTERMITTENT

official_scope:
  - Battery Management
  - Battery Reuse
  - Battery Recycling
```

SK온 공식 사업 페이지는 BaaS를 배터리의 안전하고 편리한 사용을 지원하는 플랫폼으로 정의하고, 관리·재사용·재활용을 핵심 범위로 제시한다. 직접 페이지는 간헐적으로 접속 오류가 발생하므로, 해당 사실은 접속 가능한 SK이노베이션 공식 뉴스룸 자료와 교차검증해 사용한다. ([SK 온][5])

---

## SRC-SKON-D03-020 — BaaS AI 진단 서비스

```yaml
source_id: SRC-SKON-D03-020
title: SK On Develops Battery Diagnosis Technology
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2021-11-25
access_date: 2026-07-30
language: English
reliability_grade: A+
access_status: OPEN_CONFIRMED

covered_entities:
  - BaaS AI
  - Battery Diagnosis
  - Battery Abnormality Detection
  - Battery Lifespan Analysis
  - User Driving Habit Analysis
```

BaaS AI는 전기차의 주행 및 충전 과정에서 발생하는 데이터를 분석해 배터리 수명, 이상 여부, 위험상황 및 배터리 수명연장에 도움이 되는 운전습관을 제공하도록 개발됐다. 초기 서비스는 EV Infra 충전 애플리케이션을 통해 제공됐다. ([ASK Inno][6])

---

## SRC-SKON-D03-021 — 중고 전기차 배터리 가치평가

```yaml
source_id: SRC-SKON-D03-021
title: SK On to Certify the Battery Value of Used Cars
publisher: SK Innovation Newsroom
source_type: Official Corporate Article
publication_date: 2022-02-24
access_date: 2026-07-30
language: English
reliability_grade: A+
access_status: OPEN_CONFIRMED

covered_entities:
  - Used-EV Battery Certification
  - Residual Value Assessment
  - Reuse Decision
  - Recycling Decision
```

SK온은 BaaS AI를 활용해 배터리 상태, 잔여수명, 잔존가치 및 이상 여부를 분석하고, 그 결과를 중고 전기차 가치평가에 활용하는 사업모델을 추진했다. 배터리 진단 결과는 중고차 가격평가뿐 아니라 회수 배터리를 ESS로 재사용할지, 재활용 단계로 보낼지를 판단하는 기반으로 제시됐다. ([ASK Inno][7])

---

## SRC-SKON-D03-022 — BaaS 5R 개념

```yaml
source_id: SRC-SKON-D03-022
title: The 40 Years of SK Innovation's Battery Development
publisher: SK Innovation Newsroom
source_type: Official Historical Technology Article
publication_date: 2020
access_date: 2026-07-30
language: English
reliability_grade: A+
access_status: OPEN_CONFIRMED

baas_framework:
  - Rental
  - Recharge
  - Repair
  - Reuse
  - Recycle
```

SK이노베이션은 BaaS의 장기 가치사슬을 5R, 즉 Rental·Recharge·Repair·Reuse·Recycle로 제시했다. 이는 현재 개별 서비스의 완전한 상용화를 의미하는 것이 아니라, 배터리 생산 이후 전 생애주기를 연결하려는 전략적 서비스 프레임워크로 해석해야 한다. ([ASK Inno][8])

---

## SRC-SKON-D03-023 — 전고체 배터리 및 Solid Power 협력

```yaml
source_id: SRC-SKON-D03-023
title: SK On Strengthens Partnership with Solid Power
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2024-01-17
access_date: 2026-07-30
language: English
reliability_grade: A+
access_status: OPEN_CONFIRMED

covered_entities:
  - Sulfide-Based All-Solid-State Battery
  - Solid Power
  - Sulfide Solid Electrolyte
  - ASSB Pilot Line
```

SK온은 Solid Power의 전고체 셀 설계 및 파일럿 생산공정 기술을 연구개발 목적으로 사용할 수 있는 라이선스 계약을 체결했다. Solid Power는 황화물계 고체전해질을 공급하고, SK온은 대전 배터리연구원 내 파일럿 라인을 구축하는 협력구조를 추진했다. ([ASK Inno][9])

---

## SRC-SKON-D03-024 — 2026년 전고체 개발현황

```yaml
source_id: SRC-SKON-D03-024
title: "[Battery Deep Dive] Part 1: Solid-State Batteries"
publisher: SK Innovation Newsroom
source_type: Official Technology Article
publication_date: 2026-01-16
access_date: 2026-07-30
language: English
reliability_grade: A+
access_status: OPEN_CONFIRMED

covered_entities:
  - Polymer-Oxide Composite Battery
  - Sulfide-Based ASSB
  - Solid-State Pilot Plant
  - LMRO Cathode Research

primary_domains:
  - D03
  - D04
  - D05
  - D06
  - D16
  - D17
```

SK온은 폴리머-산화물 복합 전해질 배터리와 황화물계 전고체 배터리를 병행 개발 중이다. 2025년 하반기 대전에 약 4,628㎡ 규모의 전고체 파일럿 시설을 구축했으며, 2029년을 상용화 목표연도로 제시한다. 황화물계 전고체 제품은 초기 800Wh/L, 장기적으로 1,000Wh/L의 에너지밀도를 목표로 한다. 이 수치는 양산제품의 확정 사양이 아니라 연구개발 목표치다. ([ASK Inno][10])

---

## SRC-SKON-D03-025 — 각형 셀 및 건식전극 공개

```yaml
source_id: SRC-SKON-D03-025
title: INTERBATTERY 2026 Preview
publisher: SK Innovation Newsroom
source_type: Official Exhibition Preview
publication_date: 2026
access_date: 2026-07-30
language: English
reliability_grade: A+
access_status: OPEN_CONFIRMED

covered_entities:
  - Pouch-Integrated Prismatic Cell
  - On-Vent Prismatic Cell
  - Dry Electrode Process
```

SK온은 2026년 인터배터리 전시에서 파우치 통합형 각형 셀과 On-Vent 각형 셀을 공개했다. On-Vent 구조는 레이저 가공을 통해 가스와 열의 배출 위치를 설계할 수 있도록 한 개념이며, 건식전극 공정은 2024년 파일럿 라인 구축을 완료한 뒤 상용화 개발이 진행 중인 것으로 설명됐다. ([ASK Inno][11])

---

## SRC-SKON-D03-026 — 각형·원통형 포트폴리오 상태

```yaml
source_id: SRC-SKON-D03-026
title: South Korea's SK On in Talks to Supply Prismatic EV Batteries
publisher: Reuters
source_type: Global News Wire
publication_date: 2024-07-12
access_date: 2026-07-30
language: English
reliability_grade: A
access_status: OPEN_CONFIRMED

covered_entities:
  - Prismatic Battery Platform
  - Cylindrical Battery Platform
```

Reuters 인터뷰에서 SK온은 각형 배터리 기술개발을 완료했으며, 공급을 원하는 복수 완성차 업체와 논의 중이라고 밝혔다. 원통형 배터리는 개발 가능성을 검토하는 단계로 설명됐다. 이후 공개된 2026년 각형 시제품은 각형 플랫폼 개발이 지속되고 있음을 뒷받침하지만, 원통형 제품의 양산 또는 고객계약은 아직 공개자료에서 확인되지 않는다. ([Reuters][12])

---
