---
id: skon-d04-d04-013-d04-013-silicon-graphite-anode-platform
title: D04-013 — Silicon–Graphite Anode Platform — OI Metadata
summary: "실리콘-흑연 음극 플랫폼의 개발 현황(우선순위, 필요 역량, KPI)과 SF+ 배터리의 이중층 음극 구조를 통한 15분 고속 충전 기술의 원리 및 기술 과제를 정리한 메타데이터."
tags: [d04, technology, schema]
keywords: [실리콘 음극, 흑연, 이중층 음극, 고속충전, 쿨롱 효율, SF+, 음극 저항, 리튬이온, 전극 팽창, 바인더, 고속 충전, SF+ 배터리, 리튬이온 전달, SEI 코팅, 듀얼레이어]
related: []
priority: normal
domain: D04
section: D04-013
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Detailed Technology Master > D04-013 — Silicon–Graphite Anode Platform
tokens: 568
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Detailed Technology Master > D04-013 — Silicon–Graphite Anode Platform

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  missing_capabilities:
    - Low-expansion silicon composite
    - Elastic and self-healing binder
    - Artificial SEI coating
    - Prelithiation technology
    - Electrode-swelling sensor
    - Silicon-state degradation model
    - High-throughput silicon dispersion

  poc_kpis:
    - Initial coulombic efficiency
    - Electrode thickness change
    - Capacity retention
    - Fast-charge resistance
    - Gas generation
    - Silicon utilization
```

---

## TECH-SKON-D04-014 — Dual-Layer Anode Architecture

```yaml
technology_id: TECH-SKON-D04-014
canonical_name: Dual-Layer Anode Architecture
korean_name: 이중층 음극 구조

technology_category:
  - Electrode Architecture
  - Fast Charging
  - Coating Process

technology_status: PRODUCT_TECHNOLOGY_DISCLOSED

related_product:
  - PROD-SKON-EV-005 SF+ Battery

layer_functions:
  high_capacity_layer:
    principal_material: Silicon-Based Active Material
    function:
      - Increase capacity
      - Improve energy density

  low_resistance_layer:
    principal_material: Low-Resistance Graphite
    function:
      - Improve lithium-ion transport
      - Reduce charging resistance

expected_benefits:
  - Shorter lithium-ion transport distance
  - Faster lithium-ion insertion
  - Reduced electrode resistance
  - Fifteen-minute fast-charge capability

technical_challenges:
  - Layer-interface adhesion
  - Coating-thickness balance
  - Nonuniform current distribution
  - Differential expansion
  - Dual-slurry rheology control
  - High-speed coating synchronization

source_ids:
  - SRC-SKON-D04-007

confidence:
  disclosed_structure: VERY_HIGH
  mass_production_scale: NOT_DISCLOSED
```

SF+는 이중층 음극을 통해 10%에서 80%까지 약 15분 충전성능을 제시한다. 이는 서로 다른 기능을 가진 음극층을 조합해 용량과 저항의 상충관계를 줄이는 접근이다. ([ASK Inno][9])
