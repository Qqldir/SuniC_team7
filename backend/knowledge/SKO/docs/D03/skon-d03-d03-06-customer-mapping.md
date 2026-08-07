---
id: skon-d03-d03-06-customer-mapping
title: Customer Mapping
summary: "SK온의 고객을 OEM·ESS·BaaS 등으로 분류하고, 주요 고객(현대, 포드 등)과의 거래 현황 및 납품 제품을 기록한 고객 맵핑 분류표"
tags: [d03, product, schema]
keywords: [고객분류, 자동차OEM, 배터리공급, ESS, BaaS, 현대자동차, 포드, HSBMA, IONIQ, 생태계고객, Automotive OEM, 거래현황, 배터리납품, 전략파트너]
related: []
priority: normal
domain: D03
section: D03-06.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 3491
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03-06. Customer Mapping

## 6.1 Customer Taxonomy

```text
SK On Customer Universe
│
├── CUST-01 Automotive OEM
│   ├── Hyundai Motor Group
│   ├── Ford Motor Company
│   ├── Volkswagen Group
│   └── Mercedes-Benz [Historical Disclosure]
│
├── CUST-02 ESS Customer
│   ├── Flatiron Energy Development
│   ├── Utility
│   ├── Independent Power Producer
│   ├── Renewable Energy Developer
│   ├── ESS Integrator
│   ├── AI Data Center Operator
│   └── Industrial Facility Operator
│
├── CUST-03 BaaS Partner / Customer
│   ├── SoftBerry
│   ├── K Car
│   ├── SK Rent-a-car
│   ├── Macarong Factory
│   ├── Korea Automotive Inspection and Warranty Association
│   └── AUTOHUB SELLCAR
│
├── CUST-04 Industrial Mobility
│   ├── Hyundai WIA
│   ├── Factory Automation Company
│   └── Robot OEM
│
└── CUST-05 Ecosystem Customer
    ├── Financial Institution
    ├── Insurance Company
    ├── Vehicle Inspection Provider
    ├── Recycler
    └── Battery Reuse Operator
```

---

## CUST-SKON-OEM-001 — Hyundai Motor Group

```yaml
customer_id: CUST-SKON-OEM-001
official_name: Hyundai Motor Group
customer_type: GLOBAL_AUTOMOTIVE_OEM
relationship_status: ACTIVE_STRATEGIC

relationship_modes:
  - Battery supply
  - Vehicle application
  - North American supply cooperation
  - U.S. manufacturing joint venture
  - BaaS historical cooperation

confirmed_vehicle_applications:
  - Hyundai IONIQ 5
  - Hyundai IONIQ 6
  - Kia EV6

manufacturing_relation:
  entity: Hyundai SK Battery Manufacturing America
  status_as_of_2026: STARTUP_OR_OPERATION_PREPARATION
  product_family: Ternary EV Battery

mapped_applications:
  - APP-SKON-001
  - APP-SKON-002
  - APP-SKON-003
  - APP-SKON-009

evidence:
  - SRC-SKON-D03-030
  - SRC-SKON-D03-027

confidence: HIGH
```

현대자동차그룹은 SK온의 가장 명확한 현재 전략 고객·파트너 중 하나다. 과거 차량 적용, 북미 공급협력 및 HSBMA 합작 생산기반이 공식적으로 확인된다. 다만 차종별 배터리 공급기간과 물량은 공개계약 범위를 넘어 임의로 추정하지 않는다. ([ASK Inno][4])

### 관계 트리플

```text
SK On → SUPPLIES_BATTERY_TO → Hyundai Motor Group
SK On → JOINTLY_OPERATES → HSBMA
SK On Battery → INSTALLED_IN → Hyundai IONIQ 5
SK On Battery → INSTALLED_IN → Hyundai IONIQ 6
SK On Battery → INSTALLED_IN → Kia EV6
SK On NCM Battery → POWERS → Hyundai WIA AMR
```

---

## CUST-SKON-OEM-002 — Ford Motor Company

```yaml
customer_id: CUST-SKON-OEM-002
official_name: Ford Motor Company
customer_type: GLOBAL_AUTOMOTIVE_OEM

relationship_status:
  historical_supply: CONFIRMED
  former_joint_venture: TERMINATED
  current_strategic_cooperation: CONTINUES
  future_model_allocation: NOT_DISCLOSED

confirmed_vehicle:
  - Ford F-150 Lightning

confirmed_product:
  - NCM9 Battery

relationship_history:
  - Direct supply
  - BlueOval SK joint venture
  - North American manufacturing cooperation

latest_structure:
  sk_on_facility: Tennessee
  ford_facility: Kentucky

evidence:
  - SRC-SKON-D03-031
  - SRC-SKON-D03-032

confidence: HIGH
```

포드는 과거 SK온의 대표적인 대형 고객이자 합작 파트너였지만, 2025년 12월 이후 관계구조가 변경됐다. 고객 데이터베이스에서는 `ACTIVE_JV`가 아니라 `STRATEGIC_OEM_RELATION_AFTER_JV_RESTRUCTURING`으로 기록한다. ([ASK Inno][5])

---

## CUST-SKON-OEM-003 — Volkswagen Group

```yaml
customer_id: CUST-SKON-OEM-003
official_name: Volkswagen Group
customer_type: GLOBAL_AUTOMOTIVE_OEM

relationship_status:
  historical_supply: CONFIRMED
  current_contract_status: NOT_PUBLICLY_RECONFIRMED

confirmed_vehicle:
  - Volkswagen ID.4 U.S. Version

production_relation:
  facility: SK Battery America Georgia

battery_specification:
  chemistry: NOT_FULLY_DISCLOSED
  capacity: NOT_DISCLOSED
  contract_volume: NOT_DISCLOSED

evidence:
  - SRC-SKON-D03-032

confidence:
  historical_application: HIGH
  current_supply_scope: LOW
```

폭스바겐 ID.4 미국 생산모델에 SK온 배터리가 적용된 사실은 공식 자료로 확인된다. 그러나 최신 공급기간과 후속 차종은 검토된 공개자료에서 재확인되지 않았으므로 `HISTORICAL_CONFIRMED` 상태로 관리한다. ([ASK Inno][6])

---

## CUST-SKON-OEM-004 — Mercedes-Benz

```yaml
customer_id: CUST-SKON-OEM-004
official_name: Mercedes-Benz
customer_type: GLOBAL_AUTOMOTIVE_OEM

relationship_status:
  historical_customer_disclosure: CONFIRMED
  specific_vehicle: NOT_CONFIRMED_IN_CURRENT_SOURCE_SET
  current_contract: NOT_PUBLICLY_RECONFIRMED

evidence_period: 2020
confidence:
  historical_relationship: MEDIUM_HIGH
  current_status: LOW
```

SK이노베이션은 2020년 공식 자료에서 Mercedes-Benz를 배터리사업 고객사 중 하나로 언급했다. 그러나 이번 D03 자료군에서는 적용 차종과 최신 계약을 확인하지 못했으므로 고객명만 역사정보로 보존한다. ([ASK Inno][16])

---

## CUST-SKON-ESS-001 — Flatiron Energy Development

```yaml
customer_id: CUST-SKON-ESS-001
official_name: Flatiron Energy Development
customer_type:
  - BESS Developer
  - BESS Owner
  - BESS Operator
  - Renewable Energy Company

relationship_status: ACTIVE_CONTRACT

contract:
  confirmed_volume:
    value: 1
    unit: GWh
  product:
    - LFP Battery
    - Containerized BESS
  project_location:
    - Massachusetts
  delivery_start:
    period: 2026_H2

additional_opportunity:
  right_of_first_offer:
    value: 6.2
    unit: GWh
  maximum_total:
    value: 7.2
    unit: GWh
  end_year: 2030

mapped_products:
  - PROD-SKON-ESS-001
  - PROD-SKON-ESS-002
  - PROD-SKON-ESS-004

confidence: A_PLUS
```

Flatiron은 D03에서 확인되는 가장 구체적인 ESS 실명 고객이다. 1GWh는 확정 공급물량이지만 추가 6.2GWh는 우선협상권이므로 확정 수주잔고와 동일하게 합산해서는 안 된다. ([ASK Inno][2])

---

## CUST-SKON-ESS-002 — Korean ESS Central Contract Market

```yaml
customer_id: CUST-SKON-ESS-002
official_name: Korea ESS Central Contract Market
entity_type: INSTITUTIONAL_PROCUREMENT_MARKET
customer_type: PUBLIC_OR_REGULATED_PROCUREMENT

relationship_status: AWARDED
award_round: SECOND

named_direct_buyer: NOT_DISCLOSED_IN_REVIEWED_SOURCE
project_operator: NOT_FULLY_DISCLOSED
installation_sites: PARTIALLY_OR_NOT_DISCLOSED

mapped_product:
  - Domestic LFP ESS Battery
  - Containerized ESS
  - GRIDON-Related Solution

production_relation:
  facility: Seosan
  planned_capacity: 3_GWh

confidence:
  award: HIGH
  counterparty_identity: LOW
```

이 엔티티는 개별 회사가 아니라 제도 기반의 조달시장이다. 직접 계약상대방이 공개되지 않은 상태에서 특정 전력회사나 운영사를 고객으로 추정해서는 안 된다. ([ASK Inno][3])

---

## CUST-SKON-ESS-003 — U.S. ESS Customer Pipeline

```yaml
customer_id: CUST-SKON-ESS-003
official_name: U.S. ESS Customer Pipeline
entity_type: ANONYMIZED_CUSTOMER_GROUP
relationship_status: NEGOTIATION

reported_pipeline:
  negotiation_volume:
    value: greater_than_10
    unit: GWh
  customer_count: MULTIPLE
  customer_names: NOT_DISCLOSED

target_customer_types:
  - IPP
  - Renewable Developer
  - Utility
  - ESS Integrator
  - Data Center Operator
  - Infrastructure Investor

commercial_target:
  2026_order_target:
    value: greater_than_20
    unit: GWh

confidence:
  negotiation_disclosure: HIGH
  conversion_to_contract: UNCONFIRMED
```

2026년 6월 SK온은 복수의 미국 고객사와 총 10GWh 이상의 ESS 공급계약을 논의 중이며, 연간 20GWh 이상의 글로벌 ESS 수주를 목표로 한다고 밝혔다. 이는 영업목표와 협상 파이프라인이지 확정수주가 아니다. ([ASK Inno][17])

---

## CUST-SKON-BAAS-001 — SoftBerry / EV Infra

```yaml
customer_id: CUST-SKON-BAAS-001
official_name: SoftBerry
platform: EV Infra
customer_type:
  - BaaS Platform Partner
  - EV Charging Application Operator

relationship_status: HISTORICAL_PILOT_CONFIRMED

mapped_services:
  - Battery Monitoring
  - Battery Diagnosis
  - Driving Habit Analysis
  - Battery Life Guidance

end_user:
  - Individual EV Driver

confidence: HIGH
```

---

## CUST-SKON-BAAS-002 — K Car

```yaml
customer_id: CUST-SKON-BAAS-002
official_name: K Car
customer_type:
  - Used-Car Platform
  - BaaS Partner

relationship_status: BUSINESS_AGREEMENT_CONFIRMED

mapped_services:
  - Remaining Life Assessment
  - Residual Value Certification
  - Used-EV Price Support

confidence: HIGH
```

---

## CUST-SKON-BAAS-003 — SK Rent-a-car

```yaml
customer_id: CUST-SKON-BAAS-003
official_name: SK Rent-a-car
customer_type:
  - Rental-Car Company
  - Fleet Data Partner
  - BaaS Service Partner

relationship_status: SERVICE_COOPERATION_CONFIRMED

mapped_services:
  - Fleet Monitoring
  - Battery Diagnosis
  - Driving Data Collection
  - EV My Car Management

confidence: HIGH
```

---

## CUST-SKON-BAAS-004 — Macarong Factory

```yaml
customer_id: CUST-SKON-BAAS-004
official_name: Macarong Factory
service_brand: Mycle
customer_type:
  - Vehicle Management Platform
  - Repair-Shop Network
  - BaaS Delivery-Channel Partner

relationship_status: SERVICE_COOPERATION_CONFIRMED

mapped_services:
  - EV My Car Management
  - Consumer Battery Information
  - Repair-Shop-Based Vehicle Checkup

confidence: HIGH
```

---

## CUST-SKON-BAAS-005 — Korea Automotive Inspection and Warranty Association

```yaml
customer_id: CUST-SKON-BAAS-005
official_name: Korea Automotive Inspection and Warranty Association
abbreviation: KAIWA

customer_type:
  - Inspection Standard Partner
  - Industry Association
  - Used-EV Evaluation Partner

relationship_status: STANDARDIZATION_AGREEMENT_CONFIRMED

mapped_activities:
  - Battery-condition evaluation standard
  - Residual-value standard
  - Diagnostic method development
  - Policy recommendation

confidence: HIGH
```

---

## CUST-SKON-IND-001 — Hyundai WIA

```yaml
customer_id: CUST-SKON-IND-001
official_name: Hyundai WIA
customer_type:
  - Industrial Robot Manufacturer
  - Factory Automation Company

relationship_status: PRODUCT_APPLICATION_CONFIRMED

confirmed_equipment:
  - Autonomous Mobile Robot

battery:
  supplier: SK On
  chemistry: NCM
  exact_product: NOT_DISCLOSED

confidence:
  application: HIGH
  commercial_supply_scope: NOT_DISCLOSED
```

---

# 6.2 Customer Relationship Status Codes

```yaml
customer_status_codes:

  ACTIVE_CONTRACT:
    definition: Signed and publicly confirmed supply contract

  ACTIVE_STRATEGIC:
    definition: Current strategic cooperation with supply, JV or development evidence

  BUSINESS_AGREEMENT_CONFIRMED:
    definition: MOU or business agreement exists, but revenue scale is not confirmed

  PRODUCT_APPLICATION_CONFIRMED:
    definition: Product or equipment application is publicly demonstrated

  HISTORICAL_SUPPLY_CONFIRMED:
    definition: Past supply or vehicle application confirmed; latest scope unknown

  TARGET_MARKET:
    definition: Market officially targeted without named customer contract

  NEGOTIATION:
    definition: Customer discussions disclosed but no final contract confirmed

  PIPELINE:
    definition: Potential volume or business opportunity, not booked order

  UNCONFIRMED:
    definition: Insufficient evidence for customer or contract assertion
```

---

# 6.3 Product–Customer Mapping

```text
High-Nickel Pouch Battery
├─ → Hyundai Motor Group
├─ → Ford [Historical / Continuing Strategic Relation]
├─ → Volkswagen [Historical Confirmed]
└─ → Mercedes-Benz [Historical Customer Disclosure]

NCM9
└─ → Ford F-150 Lightning

NCM Robot Battery
└─ → Hyundai WIA AMR

LFP ESS Battery
├─ → Flatiron Energy Development
├─ → Korea ESS Central Contract Market
└─ → U.S. ESS Customer Pipeline [Unnamed]

GRIDON
├─ → Flatiron-Related U.S. ESS Market
├─ → Utility / IPP
├─ → Renewable Developer
├─ → AI Data Center [Target]
└─ → Industrial Facility [Target]

BaaS AI
├─ → SoftBerry / EV Infra
├─ → K Car
├─ → SK Rent-a-car
├─ → Macarong Factory
├─ → KAIWA
└─ → AUTOHUB SELLCAR
```

---
