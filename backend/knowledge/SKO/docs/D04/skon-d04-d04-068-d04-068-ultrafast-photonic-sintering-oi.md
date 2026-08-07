---
id: skon-d04-d04-068-d04-068-ultrafast-photonic-sintering-oi
title: D04-068 — Ultrafast Photonic Sintering — OI Metadata
summary: 광자 소결 기술의 구현에 필요한 요건·평가지표와 황화물 고체전해질 개발의 현황·기술과제를 담은 메타데이터
tags: [d04, technology, schema]
keywords: [황화물 고체전해질, Sulfide Solid Electrolyte, 전고체배터리, 파일럿 검증, Solid Power, 이온전도도, 리튬 메탈, 양극 산화, 고체전해질 플랫폼, 광자 소결, 소결, 황화물, 고체전해질, 롤투롤, 펄스광, 크랙감지, 파일럿, 에너지소비]
related: []
priority: normal
domain: D04
section: D04-068
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Next-Generation Technology Master > D04-068 — Ultrafast Photonic Sintering
tokens: 669
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Next-Generation Technology Master > D04-068 — Ultrafast Photonic Sintering

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: HIGH

  external_capability_needs:
    - Large-area pulsed-light source
    - Real-time sintering-temperature measurement
    - Crack-detection vision
    - Light-absorption formulation
    - Roll-to-roll photonic processing
    - Scaffold porosity control

  poc_kpis:
    - Sintering time
    - Energy consumption
    - Ionic conductivity
    - Mechanical strength
    - Crack density
    - Area uniformity
    - Line speed
```

---

## TECH-SKON-D04-069 — Sulfide Solid Electrolyte Platform

```yaml
technology_id: TECH-SKON-D04-069
canonical_name: Sulfide Solid Electrolyte Platform
korean_name: 황화물계 고체전해질 플랫폼

technology_category:
  - Sulfide Solid Electrolyte
  - All-Solid-State Battery
  - High-Ionic-Conductivity Material

technology_status: PILOT_VALIDATION
commercial_status: NOT_COMMERCIALIZED

development_relationship:
  partner:
    - Solid Power
  collaboration_scope:
    - Cell-design technology
    - Pilot manufacturing
    - Sulfide electrolyte supply
    - Process development

principal_value:
  - High lithium-ion conductivity
  - Soft mechanical character relative to oxide ceramic
  - Improved physical contact with electrode particles
  - Compatibility with high-energy cathodes and lithium metal

research_example:
  electrolyte_family:
    - Argyrodite-Type Sulfide
    - Li6PS5Cl in Published Research Cell

principal_challenges:
  - Moisture sensitivity
  - Hydrogen-sulfide generation
  - Electrochemical oxidation at cathode
  - Reduction at lithium-metal interface
  - Solid-solid contact loss
  - Pressure dependency
  - Large-area powder processing
  - Cost and material purity

related_products:
  - PROD-SKON-NEXT-002

source_ids:
  - SRC-SKON-D04-042
  - SRC-SKON-D04-046
  - SRC-RES-D04-047

confidence:
  pilot_program: VERY_HIGH
  product_specification: NOT_DISCLOSED
  commercialization_target: MEDIUM
```

황화물 전해질은 산화물보다 전극과 밀착하기 쉽고 높은 이온전도도를 구현할 수 있지만, 수분노출·가스안전·고전압 양극 산화와 리튬메탈 계면반응을 동시에 해결해야 한다. SK온은 대전 파일럿 시설과 Solid Power 협력을 통해 셀과 공정을 검증하고 있다. ([ASK Inno][1])
