---
id: skon-d07-d07-rp-003-capacity-economics-policy-research-p
title: 003. Capacity Economics & Policy Research Pack
summary: "배터리 생산 투자의 경제성 평가에 필요한 SK온 실적, 미국 세액공제, PFE 제한, 중국 관세 등 규제·제도 정보를 종합한 자료다."
tags: [d07, footprint, schema, "xref:d08", "xref:d09"]
keywords: [45X, Section 301, PFE, 세액공제, 배터리 관세, 리튬이온배터리, 생산세액공제, 캐파 경제성, 미국 정책, 공급체인 제한, 배터리 생산능력, 금지외국기업, 중국 관세, 미국 인센티브, SK온, 통상환경]
related: []
priority: normal
domain: D07
section: D07-RP
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 2787
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-RP-003. Capacity Economics & Policy Research Pack

## SRC-OFF-D07-010 — 2026년 2분기 실적 업데이트

```yaml
source_id: SRC-OFF-D07-010
title: SK Innovation Q2 2026 Financial Results
publisher: SK Innovation
publication_date: 2026-07-30
source_type: Official Earnings Release
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - SK On battery business returned to quarterly operating profit
  - Asian sales volume expanded
  - Customer compensation was received
  - U.S. tax-credit recognition increased
  - BlueOval SK restructuring was completed
  - SK On Tennessee became a standalone operation

not_confirmed:
  - Current plant-level utilization
  - Current consolidated capacity
  - Plant-level profitability
  - Recurring margin excluding one-time items
```

---

## SRC-REG-D07-011 — 미국 45X 생산세액공제

```yaml
source_id: SRC-REG-D07-011
title: Advanced Manufacturing Production Credit Final Regulations
publisher:
  - U.S. Treasury
  - Internal Revenue Service
publication_date: 2024-10-28
source_type: Federal Regulation
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

battery_credit_rates:
  cell:
    value: USD_35_per_kWh
  module_with_cells:
    value: USD_10_per_kWh
  module_without_cells:
    value: USD_45_per_kWh

principal_condition:
  - Eligible components must be produced in the United States
  - Production and sale requirements must be satisfied
```

45X 최종규정은 미국에서 생산되는 적격 배터리 Cell에 kWh당 35달러, Cell을 사용한 적격 Module에 kWh당 10달러의 공제를 규정한다. 다만 공제 대상, 판매구조, Module의 최초 적격구성 시점과 측정기준을 충족해야 하므로 공장 설계 Capacity에 단순히 35달러를 곱해서 실제 수익으로 계산할 수 없다. ([Federal Register][2])

---

## SRC-REG-D07-012 — PFE 관련 45X 제한

```yaml
source_id: SRC-REG-D07-012
title: Notice 2026-15 and PFE Material-Assistance Guidance
publisher:
  - U.S. Treasury
  - Internal Revenue Service
publication_year: 2026
source_type: Official Tax Guidance
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

confirmed:
  - New prohibited-foreign-entity restrictions affect Section 45X
  - Material-assistance cost-ratio analysis is required
  - Interim safe harbors are provided pending proposed regulations

footprint_implication:
  - U.S. production location alone may not guarantee full credit eligibility
  - Input sourcing and supplier ownership must also be examined
```

2026년 IRS 지침은 45X를 포함한 세액공제에서 PFE가 제공한 실질적 지원을 판단하는 추가 제한을 반영했다. 따라서 미국 내 생산이라는 사실뿐 아니라 소재·부품의 공급국, 공급업체 지배구조와 비용비중을 함께 추적해야 한다. ([국세청][3])

---

## SRC-REG-D07-013 — 중국산 배터리 Section 301 관세

```yaml
source_id: SRC-REG-D07-013
title: Section 301 Tariff Modification for Lithium-Ion Batteries
publisher: Office of the United States Trade Representative
source_type: Official Trade Action
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

tariff_schedule:
  china_origin_ev_lithium_ion_batteries:
    additional_tariff_rate: 25_percent
    effective_year: 2024

  china_origin_other_lithium_ion_batteries:
    additional_tariff_rate: 25_percent
    effective_year: 2026

footprint_implication:
  - U.S. ESS localization gains additional strategic value
  - Imported China-origin finished batteries face greater tariff exposure
```

USTR의 Section 301 조치는 중국산 전기차용 리튬이온 배터리의 추가 관세를 2024년 25%로 높였고, 기타 리튬이온 배터리는 2026년에 25%로 높이도록 했다. 실제 부담은 원산지와 HTS 분류에 따라 달라지므로 중국 Cell을 제3국에서 단순 조립한 경우까지 자동으로 미국산으로 간주해서는 안 된다. ([United States Trade Representative][4])

---

## SRC-REG-D07-014 — 미국 배터리 원산지 Ledger

```yaml
source_id: SRC-REG-D07-014
title: Clean-Vehicle Qualified-Manufacturer Requirements
publisher: Internal Revenue Service
source_type: Official Compliance Guidance
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

confirmed:
  - Vehicle manufacturers submit battery-component information to DOE
  - Critical-mineral and constituent-material calculations are required
  - Compliance information forms a battery ledger

footprint_implication:
  - Plant, component and material origin must be traceable
  - Alternative-site transfers require compliance data preservation
```

미국의 적격 완성차 제조사는 배터리 구성요소·핵심광물·관련 소재에 대한 계산과 근거를 DOE에 제출해 Compliance Battery Ledger를 구축해야 한다. D07의 공장배정 정보는 D08 소재원산지와 D09 고객·차종 정보에 연결돼야 한다. ([국세청][5])

---

## SRC-REG-D07-015 — EU Batteries Regulation

```yaml
source_id: SRC-REG-D07-015
title: Regulation EU 2023/1542 Concerning Batteries and Waste Batteries
publisher: European Union
source_type: EU Regulation
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

relevant_requirements:
  - Battery carbon-footprint information
  - QR-based information
  - Battery passport
  - Recycled-content information
  - Supply-chain due diligence
  - Collection and recycling requirements

affected_plants:
  - Komarom_1
  - Komarom_2
  - Ivancsa
```

EU 배터리 규정은 EV·산업용 배터리에 탄소발자국, QR 정보, 배터리 여권과 공급망 실사 등을 단계적으로 요구한다. 이에 따라 헝가리 공장은 GWh뿐 아니라 전력배출계수·소재원산지·재활용 정보와 Cell별 데이터 연결능력을 Capacity의 적격성 조건으로 관리해야 한다. ([Eur-Lex][6])

---

## SRC-OFF-D07-016 — EU Battery Booster

```yaml
source_id: SRC-OFF-D07-016
title: European Battery Booster Facility
publisher: European Commission
publication_year: 2026
source_type: Official Policy Program
source_grade: A_PLUS
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Up to EUR 1.5 billion is intended to support European cell manufacturing
  - Support is aimed at production ramp-up and competitiveness

plant_relevance:
  - Hungary production base
  - Low-carbon production investment
  - Ramp-up financing and modernization
```

유럽연합은 2026년 Battery Booster를 통해 최대 15억 유로를 배터리 Cell 제조 Ramp-Up 지원에 활용한다고 밝혔다. 이는 SK온에 대한 확정지원금이 아니라 헝가리 공장이 접근할 수 있는 정책환경이다. ([Climate Action][7])

---

## SRC-OFF-D07-017 — Nissan 미국 공급계약

```yaml
source_id: SRC-OFF-D07-017
title: SK On Battery Supply Agreement with Nissan
publisher: SK
publication_date: 2025-03-19
source_type: Official Supply Agreement Release
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  total_supply: nearly_100_GWh
  period: 2028_to_2033
  production_origin: United_States
  chemistry:
    - High_nickel
  cell_format:
    - Pouch
  customer_vehicle_site:
    - Nissan_Canton_Mississippi

unresolved:
  - SK On production plant
  - Annual delivery profile
  - Dedicated line capacity
```

Nissan 계약은 2028~2033년 약 100GWh의 미국산 High-Nickel Pouch Cell 공급을 포함하지만, 어느 SK온 미국공장이 생산하는지는 공식자료에서 공개되지 않았다. 계약 총량을 Tennessee 45GWh와 직접 연결하거나 연평균 물량을 확정 생산능력으로 바꾸면 안 된다. ([SK][8])

---

## SRC-OFF-D07-018 — Slate 미국 공급계약

```yaml
source_id: SRC-OFF-D07-018
title: SK On Selected as Battery Supplier for Slate
publisher: SK
publication_date: 2025-04-25
source_type: Official Supply Agreement Release
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  total_supply: approximately_20_GWh
  period: 2026_to_2031
  production_origin: United_States
  chemistry:
    - High_nickel_NCM

unresolved:
  - Production plant
  - Annual delivery profile
  - Dedicated capacity
  - Alternative site
```

Slate 계약 역시 미국산 배터리라는 사실은 확인되지만 생산공장은 공개되지 않았다. 따라서 Commerce, HSBMA 또는 Tennessee 중 하나에 자동 배정하지 않는다. ([SK][9])

---

## SRC-REG-D07-019 — Tennessee Legacy Design Basis

```yaml
source_id: SRC-REG-D07-019
title: Environmental Assessment for Stanton Tennessee Battery Plant
publisher: U.S. Department of Energy
publication_year: 2023
source_type: Government Environmental Assessment
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

confirmed_historical_design:
  annual_capacity_gwh: 45
  project_scope: BlueOval_SK_Tennessee

current_use:
  - Legacy physical design reference only

not_confirmed:
  - 2028 commissioned capacity
  - Product allocation
  - Current customer
  - Final equipment configuration after restructuring
```

DOE 환경평가의 45GWh는 BlueOval SK 시절 Tennessee 프로젝트의 설계기준이다. 현재 SK On Tennessee가 2028년 정확히 45GWh를 전부 가동한다는 의미로 사용하지 않는다. ([The Department of Energy's Energy.gov][10])

---
