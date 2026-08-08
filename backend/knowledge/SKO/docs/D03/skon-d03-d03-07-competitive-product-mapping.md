---
id: skon-d03-d03-07-competitive-product-mapping
title: Competitive Product Mapping
summary: "배터리 제품의 경쟁사 비교 분석 시 상용화상태, 측정경계, 정보출처신뢰성, 출시시점, 사양등가성 등을 고려하여 공정하게 수행하기 위한 5가지 표준화 비교 원칙"
tags: [d03, product, schema]
keywords: [배터리벤치마킹, 경쟁사분석, 배터리사양, 주행거리, 에너지밀도, C-rate, CATL, BYD, 배터리경쟁분석, 상용화상태, 측정경계, 충전시간, 정보출처, 사양정규화, 제품벤치마킹]
related: []
priority: normal
domain: D03
section: D03-07.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 345
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03-07. Competitive Product Mapping

## 7.1 비교 원칙

```yaml
comparison_rules:

  rule_01:
    name: Commercial status separation
    values:
      - Commercial
      - Contracted
      - Pilot
      - Prototype
      - R&D
      - Corporate target

  rule_02:
    name: Measurement-boundary separation
    values:
      - Cell
      - Module
      - Pack
      - Vehicle
      - Container
      - Site

  rule_03:
    name: Claim ownership
    values:
      - Manufacturer claim
      - Customer-confirmed application
      - Independent certification
      - Third-party test
      - Analyst inference

  rule_04:
    name: Time normalization
    description: Products from different launch years are not treated as same-generation competitors.

  rule_05:
    name: Specification non-equivalence
    description: Range, charging time, C-rate and energy density cannot be compared without test conditions.
```

CATL의 1,000km 주행거리, SK온의 450km 충전주행거리, BYD의 605km 주행거리 등은 서로 다른 차량·시험·팩 조건에서 나온 수치이므로 절대적인 제품순위 산정에 직접 사용하지 않는다. ([CATL][1])

---
