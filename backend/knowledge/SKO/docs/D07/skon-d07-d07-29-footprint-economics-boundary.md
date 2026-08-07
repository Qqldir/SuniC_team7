---
id: skon-d07-d07-29-footprint-economics-boundary
title: Footprint Economics Boundary
summary: SK온 배터리 공장의 경제성 분석 모델과 부정확한 추정 방법을 제시하여 정확한 공장 수익성 평가 방법을 안내한다.
tags: [d07, footprint, schema]
keywords: [생산거점, EBITDA, 경제성 분석, Plant Economics Model, Section 45X, 비용 구조, 손익분기점, 정책 효과, 공장 경제, 정책 인센티브, 배터리 채산성, 경제 추정, 수익 동인, 고정비 흡수]
related: []
priority: normal
domain: D07
section: D07-29.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 400
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-29. Footprint Economics Boundary

## 29.1 Plant Economics Model

```yaml
plant_economics_model:

  revenue_drivers:
    - Customer volume
    - Cell selling price
    - Product mix
    - Contract adjustment
    - Qualification status

  variable_cost:
    - Cathode and anode materials
    - Electrolyte and separator
    - Energy
    - Yield loss
    - Logistics
    - Warranty provision

  fixed_cost:
    - Depreciation
    - Labor
    - Facility
    - Maintenance
    - IT and OT
    - Local tax

  policy_effect:
    - Section 45X
    - State incentive
    - Tariff avoidance
    - Domestic-content benefit
    - PFE restriction

  ownership_effect:
    - Consolidated subsidiary
    - Joint venture
    - Minority interest
    - Partner approval
    - Support and guarantee

  required_output:
    - EBITDA before incentives
    - EBITDA after incentives
    - Cash cost
    - Fixed-cost absorption
    - Break-even good output
```

---

## 29.2 Prohibited Economic Inference

```yaml
footprint_economics_prohibited_inference:

  - Multiply design GWh by Section 45X credit rate
  - Treat every produced kWh as credit eligible
  - Treat HSBMA revenue and capacity as fully attributable to SK On
  - Estimate plant EBITDA from consolidated SK On profit
  - Treat Q2 customer compensation as recurring margin
  - Infer plant cost from regional wage averages
  - Treat transferred Kentucky cost as current SK On fixed cost
```

---
