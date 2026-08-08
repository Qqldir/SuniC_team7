---
id: skon-d07-d07-25-local-content-tariff-incentive-constrain
title: Local Content·Tariff·Incentive Constraints
summary: "배터리 생산에 적용되는 미국 세액공제(45X), 중국산 관세(301조), 유럽 시장 준수 요건 등 각국의 정책 제약과 인센티브 조건을 설명하는 문서"
tags: [d07, footprint, schema]
keywords: [Section 45X, 세액공제, 국산화, PFE, 배터리 여권, 중요 광물, 관세, HSBMA, 용량 적격성, EU 규정, 45X 세액공제, Section 301 관세, 금지된 외국 기업, Clean Vehicle Battery Ledger, 배터리 패스포트, 지역 콘텐츠 규제, HSBMA 인센티브, 탄소 집약도, 물질 이력 추적]
related: []
priority: normal
domain: D07
section: D07-25.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 910
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-25. Local Content·Tariff·Incentive Constraints

## 25.1 United States Policy Stack

```yaml
us_policy_stack:

  section_45x:
    relevance:
      - Cell production credit
      - Module production credit
    plant_requirement:
      - U.S. production
      - Eligible production and sale
      - Capacity substantiation

  prohibited_foreign_entity:
    relevance:
      - Material-assistance cost ratio
      - Supplier and ownership screening

  clean_vehicle_battery_ledger:
    relevance:
      - Component origin
      - Critical-mineral origin
      - Constituent-material data

  section_301:
    relevance:
      - 25 percent additional tariff on China-origin EV batteries
      - 25 percent additional tariff on other China-origin lithium-ion batteries from 2026

  state_incentives:
    relevance:
      - Investment
      - Employment
      - Property and infrastructure support
      - Performance covenants
```

---

## 25.2 Capacity Eligibility vs Physical Capacity

```text
Physical U.S. Cell Production
        ↓
45X Technical Eligibility
        ↓
PFE Material-Assistance Test
        ↓
Sale and Taxpayer Structure
        ↓
Substantiated Credit Capacity
        ↓
Recognized Tax Credit
```

```text
Vehicle Battery Production
        ↓
Material and Component Origin Ledger
        ↓
OEM Compliance Certification
        ↓
Vehicle-Level Credit Eligibility
```

**미국산 Cell 생산량과 세액공제 대상 생산량은 같지 않을 수 있다.** 공제는 적격성·판매구조·PFE와 기록요건의 영향을 받으므로 D07은 `physical_output_gwh`와 `credit_eligible_output_gwh`를 별도 필드로 관리한다. ([국세청][13])

---

## 25.3 HSBMA Incentive Covenant

```yaml
hsbma_incentive_covenant:

  confirmed:
    - HSBMA entered an incentive agreement with local government
    - Incentives depend on specified employment and investment conditions
    - SK On-related entities provided financial-support arrangements for certain obligations

  values:
    incentive_amount: NOT_DISCLOSED_IN_USED_EXCERPT
    employment_threshold: NOT_DISCLOSED_IN_USED_EXCERPT
    investment_threshold: NOT_DISCLOSED_IN_USED_EXCERPT

  required_monitoring:
    - Actual employment
    - Qualified investment
    - Production start
    - Compliance period
    - Potential clawback
```

SK이노베이션 1분기 공시는 HSBMA가 현지정부와 고용·투자 요건을 충족하면 인센티브를 받는 계약을 체결했으며, 미충족 또는 환경 관련 의무에 대비한 지원약정이 존재한다고 설명한다. ([KIND][11])

---

## 25.4 European Compliance Stack

```yaml
eu_capacity_eligibility:

  physical:
    - Installed manufacturing capacity

  market_compliance:
    - Conformity documents
    - Carbon-footprint information
    - QR and battery-passport data
    - Material due diligence
    - Recycled-content information

  economic:
    - Electricity cost
    - Carbon intensity
    - Public support eligibility
    - Customer proximity
    - Logistics cost

  implication:
    - Installed GWh can exist without being fully competitive or market-qualified
```

---
