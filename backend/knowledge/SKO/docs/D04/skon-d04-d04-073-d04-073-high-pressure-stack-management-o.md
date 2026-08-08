---
id: skon-d04-d04-073-d04-073-high-pressure-stack-management-o
title: D04-073 — High-Pressure Stack Management — OI Metadata
summary: "전고체배터리의 고압 스택 관리용 LMRO 단결정 양극의 기술 사양, 합성 방법, 성능 특성, 열화 메커니즘, 완화 기술을 정리한 SK온 기술 문서"
tags: [d04, technology, schema]
keywords: [LMRO, 단결정 양극, 전고체배터리, 망간계 양극재, 산소 방출, 황화물 전해질, 표면 코팅, 용융염 합성, 원가경쟁력, 전압저하, 망간계 카소드, 열화]
related: []
priority: normal
domain: D04
section: D04-073
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Next-Generation Technology Master > D04-073 — High-Pressure Stack Management
tokens: 666
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Next-Generation Technology Master > D04-073 — High-Pressure Stack Management

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  external_capability_needs:
    - Thin pressure sensor
    - Distributed force mapping
    - Lightweight compression structure
    - Creep-resistant elastic material
    - Pressure-electrochemistry digital twin
    - Closed-loop stack-pressure control

  poc_kpis:
    - Pressure uniformity
    - Interface resistance
    - Solid-electrolyte crack rate
    - Cell thickness change
    - Added stack mass
    - Cycle retention
```

---

## TECH-SKON-D04-074 — LMRO Single-Crystal Cathode for ASSB

```yaml
technology_id: TECH-SKON-D04-074
canonical_name: LMRO Single-Crystal Cathode for All-Solid-State Batteries
korean_name: 전고체용 LMRO 단결정 양극

technology_category:
  - Manganese-Rich Cathode
  - Low-Cost Cathode
  - Solid-State Battery Material

technology_status: PEER_REVIEWED_RESEARCH
commercial_status: NOT_COMMERCIALIZED

research_partner:
  - Seoul National University

material_family:
  full_name: Lithium-and-Manganese-Rich Layered Oxide
  abbreviation: LMRO

value_propositions:
  - Reduced dependence on nickel and cobalt
  - High theoretical capacity
  - Lower raw-material cost potential
  - Potential high-energy solid-state application

synthesis_technology:
  method: Active-Inactive Molten Salt Synthesis
  active_lithium_source:
    - LiOH
  inactive_or_low_reactivity_medium:
    - Li2SO4
  product:
    - Micrometer-scale discrete LMRO single crystals

principal_degradation_mechanisms:
  - Oxygen release
  - Voltage decay
  - Capacity fade
  - Structural rearrangement
  - Sulfide electrolyte oxidation
  - Cathode-electrolyte contact degradation

mitigation_researched:
  - Surface coating suppressing oxygen release
  - Single-crystal particle structure
  - Sulfide-compatible interface design

source_ids:
  - SRC-SKON-D04-042
  - SRC-SKON-D04-045
  - SRC-RES-D04-049

confidence:
  research_program: VERY_HIGH
  commercial_cell_application: NOT_CONFIRMED
```

LMRO는 망간 활용도가 높아 원가경쟁력이 있지만 고전압에서 산소 방출과 전압저하가 발생할 수 있다. SK온·서울대학교 연구는 단결정 합성과 표면 코팅을 통해 황화물 전해질 산화와 사이클 열화를 억제하는 방향을 검토했다. ([ASK Inno][4])
