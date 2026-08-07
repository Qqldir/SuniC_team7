---
id: skon-d04-d04-011-d04-011-high-nickel-ncm-platform-oi-meta
title: D04-011 — High-Nickel NCM Platform — OI Metadata
summary: SK온의 고니켈 NCM 플랫폼의 우선순위·부족 역량·POC지표와 고전압 미드니켈(50-70% Ni) 배터리 기술의 전략·과제·가치제안을 정리한 메타데이터 문서.
tags: [d04, technology, schema]
keywords: [미드니켈 기술, 고전압 배터리, NCM 양극, 파우치 셀, 사이클 수명, 열안정성, 에너지밀도, 코발트 저감, 전해질, 양산, 미드니켈, 고전압, 양극소재, electrolyte, single-crystal, 파우치, cycle-life]
related: []
priority: normal
domain: D04
section: D04-011
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Detailed Technology Master > D04-011 — High-Nickel NCM Platform
tokens: 709
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Detailed Technology Master > D04-011 — High-Nickel NCM Platform

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: HIGH

  missing_capabilities:
    - Low-cost ultrahigh-nickel precursor
    - Large single-crystal scale-up
    - Crack-free high-density calendering
    - Operando gas-generation analysis
    - High-voltage electrolyte
    - Cathode-interface artificial coating
    - Moisture-resistant logistics

  poc_kpis:
    - Initial capacity
    - First-cycle efficiency
    - Gas-generation rate
    - Particle-crack density
    - Cycle retention
    - Thermal onset temperature
    - Electrode density
```

---

## TECH-SKON-D04-012 — High-Voltage Mid-Nickel Technology

```yaml
technology_id: TECH-SKON-D04-012
canonical_name: High-Voltage Mid-Nickel Battery Technology
korean_name: 고전압 미드니켈 배터리 기술

technology_category:
  - Cathode Chemistry
  - Cost-Performance Balance
  - EV Battery

technology_status: PROTOTYPE_AND_PRECOMMERCIAL
commercial_customer: NOT_CONFIRMED

nickel_content:
  range:
    minimum: 50
    maximum: 70
    unit: percent

form_factor:
  disclosed: POUCH

technical_strategy:
  - Reduce nickel and cobalt content
  - Increase operating voltage
  - Protect cathode-electrolyte interface
  - Stabilize crystal structure
  - Extend cycle life

enabling_technologies:
  - Single-crystal cathode material
  - Cathode-interface electrolyte additive
  - Electrode-structure doping
  - High-voltage electrolyte
  - Thermal-stability control

value_propositions:
  - Lower material cost than high-nickel
  - Better energy density than conventional LFP
  - Improved thermal stability
  - Long-life potential
  - Standard-market EV suitability

technical_challenges:
  - Electrolyte oxidation at high voltage
  - Cathode surface reconstruction
  - Transition-metal dissolution
  - Gas generation
  - Voltage fade
  - Calendar-life stability

related_products:
  - Pouch-Integrated Prismatic Cell
  - High-Voltage Mid-Nickel Pouch Cell

source_ids:
  - SRC-SKON-D04-014
  - SRC-SKON-D04-016

confidence:
  technology_disclosure: VERY_HIGH
  mass_production: NOT_CONFIRMED
```

SK온의 미드니켈 전략은 양극의 니켈·코발트 사용량을 낮추되 충전전압을 높여 에너지밀도 감소를 보완하는 방식이다. 파우치 통합 각형 셀 내부에도 미드니켈 파우치 셀이 적용됐다고 공개됐지만, 구체적인 전압·용량·고객 및 양산시점은 공개되지 않았다. ([ASK Inno][1])
