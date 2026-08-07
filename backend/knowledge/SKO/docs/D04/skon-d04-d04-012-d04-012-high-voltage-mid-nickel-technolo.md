---
id: skon-d04-d04-012-d04-012-high-voltage-mid-nickel-technolo
title: D04-012 — High-Voltage Mid-Nickel Technology — OI Metadata
summary: "고전압 중니켈 양극 기술의 개발 필요사항과 성능 지표, 그리고 실리콘-흑연 복합 음극의 기술 특성 및 트레이드오프를 정리한 기술 메타데이터."
tags: [d04, technology, schema, "xref:d03"]
keywords: [고전압 중니켈, 실리콘-흑연 음극, 음극 재료, 에너지 밀도, 고속충전, SF+ 배터리, 사이클 보존율, 기술 메타데이터, 기술 트레이드오프, Anode platform, 고전압 양극, 중니켈, 양극-전해질 계면, 전해질 첨가제, 빠른 충전, 사이클 유지율]
related: []
priority: normal
domain: D04
section: D04-012
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Detailed Technology Master > D04-012 — High-Voltage Mid-Nickel Technology
tokens: 572
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Detailed Technology Master > D04-012 — High-Voltage Mid-Nickel Technology

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  external_capability_needs:
    - High-voltage electrolyte additive
    - Cathode-electrolyte interphase coating
    - Metal-dissolution suppression
    - Single-crystal mid-nickel precursor
    - High-voltage gas sensor
    - Calendar-aging prediction
    - Low-cobalt cathode optimization

  target_kpis:
    - Cost per kWh
    - Average discharge voltage
    - Cycle retention
    - Gas volume
    - Thermal stability
    - Fast-charge capability
```

---

## TECH-SKON-D04-013 — Silicon–Graphite Anode Platform

```yaml
technology_id: TECH-SKON-D04-013
canonical_name: Silicon–Graphite Anode Platform
korean_name: 실리콘-흑연 복합 음극 기술

technology_category:
  - Anode Material
  - Fast Charging
  - High-Energy-Density Battery

technology_status: PRODUCT_TECHNOLOGY_DISCLOSED

material_components:
  - Graphite
  - Silicon or silicon-based active material
  - Conductive network
  - Binder system

primary_functions:
  - Increase anode capacity
  - Improve cell energy density
  - Support fast-charge product design

principal_tradeoffs:
  - Silicon volume expansion
  - Particle pulverization
  - SEI growth
  - Initial lithium loss
  - Electrode swelling
  - Cycle-life degradation
  - Binder and conductive-network instability

related_products:
  - SF+ Battery
  - Advanced SF Battery
  - Hyper Fast Battery

related_technologies:
  - Dual-Layer Anode
  - Magnetic Alignment
  - SUFast
  - Charging Protocol Optimization

source_ids:
  - SRC-SKON-D04-007
  - SRC-SKON-D03-015

confidence:
  technology_use: HIGH
  exact_silicon_content: NOT_DISCLOSED
```

SK온은 SF+에서 고용량 실리콘과 저저항 흑연을 결합한 음극 구조를 공개했지만 실리콘 함량, 입자형태, 프리리치에이션 적용 여부 및 바인더 조성은 공개하지 않았다. 따라서 D04는 기술군의 존재와 기능만 저장한다. ([ASK Inno][9])
