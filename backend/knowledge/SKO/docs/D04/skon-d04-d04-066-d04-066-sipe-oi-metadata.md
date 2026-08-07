---
id: skon-d04-d04-066-d04-066-sipe-oi-metadata
title: D04-066 — SIPE — OI Metadata
summary: "SIPE 및 LLZO 산화물 고체전해질 기술의 개발 우선순위, 부족한 역량, 성과지표, 기술상태를 종합한 기술 메타데이터."
tags: [d04, technology, schema]
keywords: [SIPE, LLZO, 고체전해질, 이온전도도, 산화물, 광소결, 가넷, 덴드라이트, 전고체전지, 롤투롤, 단일이온고분자전해질, 리튬금속전지, 기술우선순위]
related: []
priority: normal
domain: D04
section: D04-066
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Next-Generation Technology Master > D04-066 — SIPE
tokens: 1192
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Next-Generation Technology Master > D04-066 — SIPE

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  missing_capabilities:
    - High-conductivity single-ion polymer
    - High-voltage-resistant polymer backbone
    - Continuous thin-film casting
    - Polymer-lithium interface coating
    - Operando dendrite imaging
    - Flame-resistant polymer formulation

  poc_kpis:
    - Conductivity at 25°C
    - Lithium transference number
    - Critical current density
    - Film thickness deviation
    - Lithium symmetric-cell life
    - Full-cell cycle retention
```

---

## TECH-SKON-D04-067 — LLZO Oxide Solid Electrolyte

```yaml
technology_id: TECH-SKON-D04-067
canonical_name: Air-Stable LLZO Oxide Solid Electrolyte
korean_name: 대기안정형 LLZO 산화물 고체전해질

technology_category:
  - Oxide Solid Electrolyte
  - Garnet Electrolyte
  - Lithium-Metal Battery

technology_status: RESEARCH_AND_PATENT_APPLICATION
commercial_status: NOT_COMMERCIALIZED

material_family:
  abbreviation: LLZO
  elements:
    - Lithium
    - Lanthanum
    - Zirconium
    - Oxygen

research_partner:
  - Dankook University

reported_result:
  ionic_conductivity:
    value: 1.7
    unit: mS_per_cm
    improvement:
      value: 70
      unit: percent
    evidence_type: COMPANY_REPORTED_RESEARCH

  air_stability:
    status: IMPROVED
    exposure_factors:
      - Moisture
      - Carbon dioxide

technical_value:
  - Chemical stability
  - Thermal stability
  - Lithium-metal compatibility
  - Potential high-voltage application
  - Mechanical suppression of dendrite penetration

principal_challenges:
  - Brittle fracture
  - High-temperature sintering
  - Grain-boundary resistance
  - Lithium-metal contact loss
  - Surface contamination
  - High-density ceramic processing
  - Large-area thin-film fabrication

source_ids:
  - SRC-SKON-D04-044
  - SRC-RES-D04-048

confidence:
  material_research: VERY_HIGH
  commercial_cell_integration: NOT_CONFIRMED
```

LLZO는 화학적 안정성이 높은 산화물계 전해질이지만 취성, 고온 소결과 전극 접촉저항이 양산장벽이다. SK온·단국대학교 연구는 미세구조와 첨가물을 조절해 이온전도도와 대기안정성을 함께 개선하는 데 초점을 맞췄다. ([ASK Inno][3])

---

## TECH-SKON-D04-068 — Ultrafast Photonic Sintering

```yaml
technology_id: TECH-SKON-D04-068
canonical_name: Ultrafast Photonic Sintering of Garnet Electrolyte
korean_name: 가넷 전해질 초고속 광소결 기술

technology_category:
  - Solid-Electrolyte Manufacturing
  - Low-Temperature Sintering
  - Roll-to-Roll Process Candidate

technology_status: LABORATORY_RESEARCH
commercial_status: NOT_COMMERCIALIZED

research_partner:
  - Korea Institute of Ceramic Engineering and Technology

conventional_issue:
  conventional_oxide_sintering:
    temperature: greater_than_1000_C
    duration: greater_than_10_hours
    source_type: COMPANY_TECHNOLOGY_DESCRIPTION

technical_mechanism:
  - Add light-absorbing inorganic material to oxide powder
  - Apply high-intensity pulsed light
  - Rapidly heat and bond particles
  - Form porous three-dimensional garnet scaffold
  - Combine scaffold with gel polymer electrolyte

target_benefits:
  - Reduced sintering time
  - Lower thermal budget
  - Reduced brittle-fracture exposure
  - Porous ion-conduction network
  - Potential roll-to-roll compatibility
  - Lower manufacturing energy

critical_challenges:
  - Through-thickness sintering uniformity
  - Light-absorption control
  - Thermal-stress cracking
  - Residual porosity control
  - Roll-to-roll web stability
  - Scale-up of illuminated area
  - Consistent scaffold-electrode contact

source_ids:
  - SRC-SKON-D04-045
  - SRC-RES-D04-048

confidence:
  research_result: VERY_HIGH
  industrial_scale: NOT_CONFIRMED
```

광소결은 장시간 전기로 소결을 강한 광에너지를 이용한 순간 가열로 대체하려는 기술이다. 논문은 롤투롤 적용 가능성을 제시하지만, 실제 SK온 파일럿 라인에서 연속생산이 검증됐다는 공개근거는 없다. ([ASK Inno][4])
