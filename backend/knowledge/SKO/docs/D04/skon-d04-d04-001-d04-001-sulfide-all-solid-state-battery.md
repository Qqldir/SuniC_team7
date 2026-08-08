---
id: skon-d04-d04-001-d04-001-sulfide-all-solid-state-battery
title: D04-001 — Sulfide All-Solid-State Battery Technology — OI Metadata
summary: "황화물 전고체 배터리의 기술 격차와 필요 협력사를 분석하고, 열전파 방지 기술의 개발 현황을 정리한 메타데이터."
tags: [d04, technology, schema]
keywords: [전고체 배터리, 황화물 전해질, 열전파 방지, OI 메타데이터, 열관리, 배터리 팩 안전, 역량 갭, 협력 파트너, SKON-D04, 열안전, sulfide electrolyte, 협력사, Pack Safety, GRIDON, 전고체, 냉각 기술, 개발 격차]
related: []
priority: normal
domain: D04
section: D04-001
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Core Technology Master > D04-001 — Sulfide All-Solid-State Battery Technology
tokens: 593
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Core Technology Master > D04-001 — Sulfide All-Solid-State Battery Technology

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  missing_capabilities:
    - Low-cost sulfide electrolyte synthesis
    - Moisture-resistant electrolyte handling
    - High-speed solid-electrolyte coating
    - Inline interfacial-defect detection
    - Stack-pressure sensing
    - Hydrogen-sulfide monitoring
    - Pilot-yield digital twin

  potential_external_partner_types:
    - Solid-electrolyte startup
    - Precision pressing-equipment company
    - X-ray or ultrasound inspection company
    - Gas-sensor startup
    - Dry-room energy-efficiency company
    - Solid-state university laboratory
```

---

## TECH-SKON-D04-002 — Thermal Propagation Prevention

```yaml
technology_id: TECH-SKON-D04-002
canonical_name: Thermal Propagation Prevention
korean_name: 열전파 방지 기술
abbreviation: TP Prevention

technology_category:
  - Pack Safety
  - Thermal Management
  - System Architecture

technology_status: DEVELOPMENT_AND_PRODUCT_INTEGRATION

technical_objective:
  - Prevent heat from one cell spreading to adjacent cells
  - Delay or suppress propagation through module and pack
  - Provide time for detection and emergency response
  - Maintain structural integrity during abnormal events

technology_layers:
  cell:
    - Thermal stability
    - Controlled venting

  inter_cell:
    - Thermal barrier
    - Cell spacing
    - Isolation structure

  cooling:
    - Large-surface cooling
    - Coolant immersion

  pack:
    - Vent channel
    - Gas discharge path
    - Structural containment

related_products:
  - Pouch-Type CTP
  - On-Vent Prismatic Cell
  - GRIDON
  - GRIDON Gen 2

related_technologies:
  - TECH-SKON-D04-006
  - TECH-SKON-D04-008
  - TECH-SKON-D04-010

source_ids:
  - SRC-SKON-D04-004
  - SRC-SKON-D04-012

confidence: VERY_HIGH
```

열전파 방지는 하나의 소재나 부품이 아니라 셀, 셀 간 구조, 냉각, 벤트와 팩 하우징을 동시에 설계하는 복합 안전기술이다. SK온은 이를 4대 R&D 우선과제 중 하나로 분류한다. ([ASK Inno][2])
