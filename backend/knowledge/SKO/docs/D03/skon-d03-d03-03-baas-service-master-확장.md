---
id: skon-d03-d03-03-baas-service-master-확장
title: BAAS. Service Master 확장
summary: "SK온 BaaS 플랫폼의 배터리 모니터링, 가치평가, 재사용 의사결정 등 확장 서비스 포트폴롤과 상용화 현황"
tags: [d03, product, schema, "xref:d02"]
keywords: [배터리 모니터링, 잔존가치 평가, 재사용 의사결정, 5R 라이프사이클, BaaS, 전기차, 배터리 상태, 중고차 가격, 배터리 재활용, 생명주기 관리, 배터리 상태 진단, 중고차 배터리, 배터리 수명 예측, 순환경제, Battery Lifecycle]
related: []
priority: normal
domain: D03
section: D03-03
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 1152
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03-03-BAAS. Service Master 확장

## SERV-SKON-BAAS-002 — Battery Monitoring Service

```yaml
entity_id: SERV-SKON-BAAS-002
entity_type: DIGITAL_MONITORING_SERVICE
official_name: Battery Monitoring Service
company: SK On

parent_platform:
  - BaaS
  - BaaS AI

data_sources:
  - Driving Data
  - Charging Data
  - Battery Operating Data

outputs:
  - Battery Condition
  - Lifespan Information
  - Abnormality Alert
  - Risk Situation Alert
  - Battery-Life-Extending Driving Guidance

commercial_status:
  historical: PILOT_OR_PARTNER_SERVICE
  current_scale: NOT_DISCLOSED

evidence:
  - SRC-SKON-D03-019
  - SRC-SKON-D03-020

confidence:
  technology: HIGH
  current_customer_scale: LOW
```

배터리 모니터링은 BaaS 진단서비스의 데이터 수집층으로 작동한다. 주행 및 충전 조건에서 발생하는 데이터를 지속적으로 수집·분석해 배터리 상태와 이상징후를 사용자 또는 사업자에게 제공한다. ([ASK Inno][6])

---

## SERV-SKON-BAAS-003 — Residual Value Assessment

```yaml
entity_id: SERV-SKON-BAAS-003
entity_type: BATTERY_VALUATION_SERVICE
official_name: Battery Residual Value Assessment
company: SK On

parent_platform:
  - BaaS AI

primary_functions:
  - Remaining Life Estimation
  - Battery Condition Grading
  - Scrap Value Estimation
  - Used-EV Price Support
  - Reuse Eligibility Screening
  - Recycling Decision Support

target_users:
  - Used-Car Platform
  - Vehicle Inspection Organization
  - Fleet Operator
  - Finance Company
  - Insurance Company
  - Battery Recycler

commercial_status: PARTNERSHIP_AND_PILOT_BASED
standardization_status: UNDER_DEVELOPMENT

evidence:
  - SRC-SKON-D03-021
  - SRC-SKON-D03-020

confidence:
  capability: HIGH
  standardized_market_adoption: NOT_CONFIRMED
```

잔존가치 평가서비스는 중고 EV의 거래가격 산정과 회수 배터리의 후속 용도를 결정하는 연결점이다. 객관적인 평가기준이 확보되면 차량거래, 금융, 보증, 재사용 및 재활용 사업까지 확장될 수 있다. 이 확장 가능성은 분석이며, 모든 사업영역에서 실제 상용화됐다는 의미는 아니다. ([ASK Inno][14])

---

## SERV-SKON-BAAS-004 — Battery Reuse Decision Support

```yaml
entity_id: SERV-SKON-BAAS-004
entity_type: LIFECYCLE_DECISION_SERVICE
official_name: Battery Reuse Decision Support
company: SK On

parent_platform:
  - BaaS

decision_inputs:
  - State of Health
  - Remaining Useful Life
  - Usage History
  - Abnormality History
  - Residual Value
  - Safety Condition

decision_outputs:
  - Continue Vehicle Use
  - Repair
  - Reuse as ESS
  - Recycle
  - Dispose Under Controlled Procedure

commercial_status: STRATEGIC_SERVICE_CAPABILITY
current_revenue_model: NOT_DISCLOSED

evidence:
  - SRC-SKON-D03-019
  - SRC-SKON-D03-021
  - SRC-SKON-D03-022

confidence:
  strategic_scope: HIGH
  operational_scale: UNKNOWN
```

---

## SERV-SKON-BAAS-005 — 5R Lifecycle Platform

```yaml
entity_id: SERV-SKON-BAAS-005
entity_type: STRATEGIC_SERVICE_FRAMEWORK
official_name: BaaS 5R Lifecycle Platform
company: SK On / SK Innovation

framework:
  - Rental
  - Recharge
  - Repair
  - Reuse
  - Recycle

commercial_status: STRATEGIC_FRAMEWORK
individual_service_status:
  rental: NOT_CONFIRMED
  recharge: PARTNER_ECOSYSTEM_DEPENDENT
  repair: NOT_FULLY_DISCLOSED
  reuse: DEVELOPMENT_AND_PARTNERSHIP
  recycle: GROUP_VALUE_CHAIN_RELATED

evidence:
  - SRC-SKON-D03-022

confidence:
  framework_existence: HIGH
  full_platform_commercialization: LOW
```

5R는 하나의 완성형 상용상품명이라기보다, 배터리 생애주기 전반을 서비스 사업으로 연결하려는 장기 프레임워크다. 따라서 D03에는 전략적 서비스 아키텍처로 저장하고 개별 사업성과는 D02·D11에서 별도로 검증한다. ([ASK Inno][8])

---
