---
id: skon-d03-d03-rp-004-추가-source-library-등록
title: 004. 추가 Source Library 등록
summary: "SK온의 ESS와 로봇 등 새로운 시장으로의 제품 적용영역 확대와 Flatiron, 현대차, 국내 ESS 시장 등 주요 배터리 공급계약 및 고객 정보를 담은 4건 공식 자료의 메타데이터 등록."
tags: [d03, product, schema]
keywords: [ESS, LFP 배터리, 에너지저장시스템, 배터리 공급계약, Flatiron Energy, 현대자동차그룹, 전기차 배터리, 중앙계약시장, 배터리 제조, 자율주행로봇, BESS, 공급계약, 제품 다각화, 고객 정보, 생산능력]
related: []
priority: normal
domain: D03
section: D03-RP
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 2939
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# SK온 D03 Products & Solutions

## Part 3. Application Mapping 및 Customer Mapping

**문서 버전:** D03 v1.2
**기준일:** 2026-07-30
**이전 완료 지점:** `D03-04 Product Architecture v1.0`

---

# D03-RP-004. 추가 Source Library 등록

## SRC-SKON-D03-027 — 제품 적용영역 확장

```yaml
source_id: SRC-SKON-D03-027
title: INTERBATTERY 2026 Preview – Unlock the Next Energy
publisher: SK Innovation Newsroom
source_type: Official Exhibition Preview
publication_date: 2026-03-10
access_date: 2026-07-30
language:
  - Korean
  - English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_applications:
  - Electric Vehicle
  - Energy Storage System
  - Industrial Robot
  - Autonomous Mobile Robot
  - Emerging Mobility

covered_products:
  - NCM Battery
  - LFP ESS Battery
  - GRIDON
  - Hyper Fast Battery
  - Prismatic Cell Concepts
```

SK온은 인터배터리 2026에서 제품 적용영역을 전기차 중심에서 ESS와 로봇 등으로 넓히고 있다고 공식적으로 제시했다. 실제 전시에는 현대위아의 자율주행 물류로봇에 탑재된 SK온 NCM 배터리가 포함됐다. 해당 로봇은 현대자동차그룹 메타플랜트 아메리카 등 산업현장에서 활용되는 모델로 소개됐다. ([ASK Inno][1])

---

## SRC-SKON-D03-028 — Flatiron ESS 공급계약

```yaml
source_id: SRC-SKON-D03-028
title: SK On Expands into U.S. BESS Market with LFP Batteries
publisher: SK On / SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2025-09-04
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

named_customer:
  - Flatiron Energy Development

confirmed_scope:
  initial_volume:
    value: 1
    unit: GWh
  potential_total_volume:
    value: 7.2
    unit: GWh
  initial_delivery:
    period: 2026_H2
    location: Massachusetts
```

SK온은 미국 에너지저장 개발·운영사 Flatiron Energy Development와 1GWh 규모의 LFP 기반 컨테이너형 BESS 공급계약을 체결했다. 추가 프로젝트 우선협상권을 포함한 잠재 공급규모는 2030년까지 최대 7.2GWh다. ([ASK Inno][2])

---

## SRC-SKON-D03-029 — 국내 ESS 중앙계약시장

```yaml
source_id: SRC-SKON-D03-029
title: SK On Wins Second ESS Central Contract Market
publisher: SK Innovation Newsroom
source_type: Official Corporate Article
publication_date: 2026-02-12
access_date: 2026-07-30
language: Korean
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_market:
  - Korea ESS Central Contract Market

production_relation:
  location: Seosan
  planned_lfp_ess_capacity:
    value: 3
    unit: GWh
```

SK온은 국내 제2차 ESS 중앙계약시장 사업자로 최종 선정됐으며, 서산공장 일부 라인을 ESS용 LFP 배터리 생산라인으로 전환해 총 3GWh 규모의 생산능력을 확보할 계획을 공개했다. 다만 공개자료만으로는 실제 계약상 직접 구매자, 프로젝트별 운영사 및 개별 설치지역 전체를 확정하기 어렵다. ([ASK Inno][3])

---

## SRC-SKON-D03-030 — 현대자동차그룹 EV 공급관계

```yaml
source_id: SRC-SKON-D03-030
title: SK On Signs MOU with Hyundai Motor Group to Supply EV Batteries in North America
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2022-11-29
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

named_customer:
  - Hyundai Motor Group
  - Hyundai Motor
  - Kia

historically_confirmed_vehicle_applications:
  - Hyundai IONIQ 5
  - Hyundai IONIQ 6
  - Kia EV6
```

공식 자료는 SK온 배터리가 현대 아이오닉 5·아이오닉 6와 기아 EV6에 적용됐음을 확인한다. 양사는 북미 전기차 생산을 위한 배터리 공급협력을 확대했고, 2026년 공식 자료에는 현대자동차그룹과의 미국 합작공장 HSBMA가 가동 준비 단계에 있는 것으로 제시됐다. ([ASK Inno][4])

---

## SRC-SKON-D03-031 — 포드 관계 최신 상태

```yaml
source_id: SRC-SKON-D03-031
title: SK On and Ford to Independently Operate Former BlueOval SK Facilities
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2025-12-11
access_date: 2026-07-30
language: Korean
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

relationship_change:
  previous_structure: 50_50_JOINT_VENTURE
  latest_structure: INDEPENDENT_FACILITY_OWNERSHIP_AND_OPERATION
  sk_on_asset: Tennessee Plant
  ford_asset: Kentucky Plants
  ongoing_relation: STRATEGIC_COOPERATION_CONTINUES
```

SK온과 포드는 2025년 12월 BlueOval SK 합작법인 체제를 종료하고 생산시설을 독립적으로 운영하기로 했다. SK온은 테네시 공장을, 포드는 켄터키 공장을 각각 운영하며, SK온은 테네시 공장을 중심으로 포드와 전략적 협력을 이어간다고 밝혔다. 따라서 D03에서는 포드를 단순한 “현재 합작법인 고객”이 아니라 **과거 합작 파트너이자 현재 전략적 OEM 관계사**로 구분한다. ([ASK Inno][5])

---

## SRC-SKON-D03-032 — Ford·Volkswagen 차량 적용

```yaml
source_id: SRC-SKON-D03-032
title: SK Battery America Vehicle Applications
publisher: SK Innovation Newsroom
source_type: Official Corporate Article
publication_date:
  - 2021
  - 2023
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

confirmed_vehicle_applications:
  - Ford F-150 Lightning
  - Volkswagen ID.4

product_relation:
  Ford_F150_Lightning:
    chemistry: NCM9
  Volkswagen_ID4:
    chemistry: NOT_FULLY_DISCLOSED_IN_SOURCE
```

SK온의 미국 조지아 공장은 포드 F-150 Lightning과 폭스바겐 ID.4용 배터리를 생산한 것으로 공식 확인된다. F-150 Lightning에는 NCM9 제품이 공급된 것으로 공개됐지만, 폭스바겐 ID.4 적용 셀의 세부 화학조성과 규격은 해당 자료만으로 확정할 수 없다. ([ASK Inno][6])

---

## SRC-SKON-D03-033 — BaaS 소비자 진단 서비스

```yaml
source_id: SRC-SKON-D03-033
title: SK On Develops Battery Diagnosis Technology for EV Drivers
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2021-11-25
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

partners:
  - SoftBerry
  - EV Infra

application:
  - Consumer Battery Diagnosis
  - Charging Data Analysis
  - Driving Habit Analysis
```

SK온은 소프트베리와 협력해 EV Infra 애플리케이션 이용자를 대상으로 BaaS AI 기반 배터리 진단 시범서비스를 제공했다. 서비스는 주행·충전 데이터를 분석해 수명상태, 이상징후, 위험상황 및 배터리 수명에 영향을 주는 운전습관을 제공하도록 설계됐다. ([ASK Inno][7])

---

## SRC-SKON-D03-034 — 중고 EV 가치평가

```yaml
source_id: SRC-SKON-D03-034
title: SK On to Certify Battery Value of Used Cars with K Car
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2022-02-24
access_date: 2026-07-30
language:
  - Korean
  - English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

partner:
  - K Car

application:
  - Used EV Battery Valuation
  - Remaining Life Certification
  - Residual Value Certification
```

SK온과 K Car는 K Car가 매입·판매하는 중고 전기차의 배터리 잔여수명과 잔존가치를 측정·인증하는 업무협약을 체결했다. 이는 BaaS AI를 중고차 거래가격 산정과 배터리 후속 용도 판단에 연결한 사례다. ([ASK Inno][8])

---

## SRC-SKON-D03-035 — EV 내차관리 서비스

```yaml
source_id: SRC-SKON-D03-035
title: SK On Launches EV My Car Management
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2022-10-04
access_date: 2026-07-30
language:
  - Korean
  - English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

partners:
  - SK Rent-a-car
  - Macarong Factory

delivery_channel:
  - Mycle Application
  - Partner Repair Shops
```

SK온은 SK렌터카 및 마카롱팩토리와 협력해 주행거리, 충전이력, 배터리 열화상태 및 기온별 주행가능거리 등을 제공하는 ‘EV 내차관리’ 서비스를 출시했다. SK렌터카의 스마트링크가 차량 데이터를 수집하고, SK온의 BaaS 시스템이 이를 분석해 마카롱팩토리의 ‘마이클’ 애플리케이션을 통해 결과를 제공하는 구조였다. ([ASK Inno][9])

---

## SRC-SKON-D03-036 — 중고 EV 평가 표준화

```yaml
source_id: SRC-SKON-D03-036
title: SK On and KAIWA Establish Used-EV Battery Evaluation Standards
publisher: SK Innovation Newsroom
source_type: Official Press Release
publication_date: 2022-04-28
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

partner:
  - Korea Automotive Inspection and Warranty Association

application:
  - Battery Performance Evaluation Standard
  - Residual Value Standard
  - Used EV Inspection
```

SK온과 한국자동차진단보증협회는 전기차 배터리 상태와 가치평가 기준을 만들기 위한 협약을 체결했다. 공식 자료에는 K Car, 오토허브 셀카, SK렌터카 및 EV Infra 등과의 기존 BaaS 프로젝트도 함께 확인된다. ([ASK Inno][10])

---
