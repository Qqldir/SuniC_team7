---
id: skon-d04-d04-003-d04-003-dry-electrode-process-oi-metadat
title: D04-003 — Dry Electrode Process — OI Metadata
summary: 건식전극공정(D04-003)의 기술 필수요건과 셀투팩 기술의 구조 및 개발 현황을 설명하는 기술 메타데이터
tags: [d04, technology, schema]
keywords: [드라이 전극 공정, 셀투팩, Cell-to-Pack, CTP, 파우치형, 대면적 냉각, 배터리 팩 아키텍처, 전극 로딩, 정전기 건식 증착, 팩 아키텍처, 파우치형 냉각, 무용매 바인더, 기계비전, 배터리 팩 구조]
related: []
priority: normal
domain: D04
section: D04-003
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Core Technology Master > D04-003 — Dry Electrode Process
tokens: 612
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Core Technology Master > D04-003 — Dry Electrode Process

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  external_capability_needs:
    - Powder-flow characterization
    - Electrostatic dry deposition
    - Solvent-free binder formulation
    - Inline thickness metrology
    - Machine-vision crack inspection
    - AI calendering control
    - Roll-pressure monitoring
    - High-loading electrode simulation

  poc_kpis:
    - Electrode loading
    - Thickness deviation
    - Adhesion strength
    - Crack density
    - Porosity distribution
    - Line speed
    - First-pass yield
    - Energy use per square meter
```

---

## TECH-SKON-D04-004 — Cell-to-Pack Technology

```yaml
technology_id: TECH-SKON-D04-004
canonical_name: Cell-to-Pack Technology
korean_name: 셀투팩 기술
abbreviation: CTP

technology_category:
  - Pack Architecture
  - Structural Integration
  - Cost Efficiency

technology_status: DEVELOPMENT
commercial_vehicle_application: NOT_PUBLICLY_CONFIRMED

architecture_change:
  conventional:
    sequence:
      - Cell
      - Module
      - Pack

  ctp:
    sequence:
      - Cell
      - Pack

primary_value:
  - Module-part reduction
  - Improved internal-space utilization
  - Reduced structural mass
  - Simplified assembly
  - Potential pack-cost reduction
  - Potential system-energy-density improvement

sk_on_variants:
  - Pouch-Type CTP
  - Large-Surface-Cooling CTP
  - Pouch-Integrated Prismatic Pack
  - Immersion-Cooled Pack Concept

critical_challenges:
  - Cell fixation
  - Thermal propagation
  - Crash load distribution
  - Pack sealing
  - Repairability
  - Cell replacement
  - Manufacturing tolerance accumulation

source_ids:
  - SRC-SKON-D04-006

confidence:
  development: VERY_HIGH
  mass_production: NOT_CONFIRMED
```

CTP는 모듈 제거만으로 완성되는 기술이 아니다. 모듈이 담당하던 셀 고정, 충돌하중 분산, 열차단, 전기연결 및 정비기능을 팩 자체가 수행해야 하므로 구조·열·제조기술의 통합이 요구된다. SK온은 파우치형 CTP와 대면적 냉각을 함께 개발하고 있다. ([ASK Inno][5])
