---
id: skon-d04-d04-074-source-reconciliation
title: Source Reconciliation
summary: "단결정 양극 기술의 데이터 정합 규칙과 초고니켈 대형 단결정 양극의 기술 특성, 목표, 규모화 도전과제를 정의"
tags: [d04, technology, schema]
keywords: [초고니켈, 단결정, 양극, Single-crystal cathode, 메타데이터, 입자 균열, LMRO, 캘린더링, 전극 밀도, 니켈 함량, 데이터 정합, 초고니켈 양극, 입계균열, 전극밀도, 규모확대]
related: []
priority: normal
domain: D04
section: D04-074
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Next-Generation Technology Master > D04-074 — LMRO Single-Crystal Cathode for ASSB
tokens: 693
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Next-Generation Technology Master > D04-074 — LMRO Single-Crystal Cathode for ASSB

### Source Reconciliation

```yaml
source_reconciliation:
  issue_id: DQ-D04-NEXT-001
  corporate_article_journal_reference: Advanced Energy Materials
  linked_primary_paper_journal: Chemistry of Materials
  canonical_publication_record:
    title: Active-Inactive Molten Salt Synthesis of Li- and Mn-Rich Layered Oxide Single Crystals
    journal: Chemistry of Materials
  resolution:
    - Use primary paper metadata as canonical
    - Retain corporate article statement as source discrepancy
```

기업 보도자료의 학술지 언급과 연결된 논문의 실제 메타데이터가 일치하지 않으므로, D00에서는 ACS의 1차 논문정보를 기준으로 저장한다. ([ASK Inno][4])

---

## TECH-SKON-D04-075 — Ultrahigh-Nickel Large Single-Crystal Cathode

```yaml
technology_id: TECH-SKON-D04-075
canonical_name: Ultrahigh-Nickel Large Single-Crystal Cathode
korean_name: 초고니켈 대형 단결정 양극

technology_category:
  - Ultrahigh-Nickel Cathode
  - High-Density Electrode
  - Single-Crystal Material

technology_status: PEER_REVIEWED_RESEARCH
commercial_status: NOT_CONFIRMED

research_partners:
  - Seoul National University
  - Institute for Basic Science

material_characteristics:
  nickel_content:
    value: greater_than_94
    unit: percent
  particle_type:
    - Large single crystal
  reported_particle_scale:
    value: approximately_10
    unit: micrometers

technology_objectives:
  - Approach theoretical electrode-density limit
  - Reduce grain-boundary cracking
  - Reduce gas generation
  - Improve cycle stability
  - Increase volumetric energy density

principal_scale_up_challenges:
  - Uniform large single-crystal synthesis
  - Cation-disorder control
  - Precursor cost
  - Particle fracture during calendering
  - Slurry and coating behavior
  - High-density electrode wetting
  - Thermal stability
  - Mass-production yield

source_ids:
  - SRC-RES-D04-051
  - SRC-SKON-D04-015

confidence:
  research_result: VERY_HIGH
  mass_production: NOT_CONFIRMED
```

다결정 하이니켈 양극은 입자 내부 결정립계에서 균열이 시작될 수 있다. 대형 단결정은 이러한 입계를 줄여 균열과 계면부반응을 완화할 수 있지만, 대형 입자의 합성균일성과 고밀도 캘린더링 중 파손을 제어해야 한다. ([ASK Inno][10])
