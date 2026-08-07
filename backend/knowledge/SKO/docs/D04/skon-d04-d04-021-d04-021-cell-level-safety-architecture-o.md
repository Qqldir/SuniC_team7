---
id: skon-d04-d04-021-d04-021-cell-level-safety-architecture-o
title: D04-021 — Cell-Level Safety Architecture — OI Metadata
summary: "Z-폴딩 스태킹으로 내부단락을 방지하는 원리, 제조변수와 위험요소, 셀 안전 검사에서 필요한 기능들을 설명하는 기술 사양서."
tags: [d04, technology, schema]
keywords: [셀 안전, 분리막 결함, 내부 단락, Z-폴딩, 전극 정렬, stacking technology, separator defect, electrode edge contact, 포우치 셀, 안전 아키텍처, Z-폴딩 스태킹, 내부단락 방지, 파우치셀, separator web, 제조 변수, 고속 생산]
related: []
priority: normal
domain: D04
section: D04-021
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Safety & Thermal Technology Master > D04-021 — Cell-Level Safety Architecture
tokens: 789
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Safety & Thermal Technology Master > D04-021 — Cell-Level Safety Architecture

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: HIGH

  missing_capabilities:
    - Inline separator-defect detection
    - Metallic-particle detection
    - Electrode-edge alignment inspection
    - Cell-internal hot-spot sensing
    - Pouch-seal nondestructive inspection
    - Gas-generation prediction
    - Multi-modal cell safety digital twin

  poc_kpis:
    - Separator defect detection rate
    - Electrode misalignment
    - False reject rate
    - Internal-short detection lead time
    - Gas generation rate
    - First-pass yield
```

---

## TECH-SKON-D04-022 — Z-Folding Stacking Technology

```yaml
technology_id: TECH-SKON-D04-022
canonical_name: Z-Folding Stacking Technology
korean_name: Z-폴딩 스태킹 기술

technology_category:
  - Cell Assembly
  - Electrode Stacking
  - Separator Handling
  - Internal Short-Circuit Prevention

technology_status: COMMERCIALIZED
ownership:
  company: SK On
  status: PROPRIETARY_TECHNOLOGY_DISCLOSED

applicable_form_factors:
  confirmed:
    - Pouch
    - Prismatic prototypes
  cylindrical: NOT_APPLICABLE_AS_PRIMARY_STACKING_METHOD

technical_mechanism:
  - Feed separator as a continuous web
  - Place cathode and anode sheets alternately
  - Fold separator in a zigzag direction
  - Enclose electrode edges with separator
  - Maintain repeated electrode alignment

safety_functions:
  - Prevent direct anode-cathode contact
  - Reduce edge-contact probability
  - Reduce electrode displacement
  - Maintain separator continuity
  - Improve stacking precision

manufacturing_variables:
  - Separator tension
  - Fold-position accuracy
  - Electrode placement accuracy
  - Web speed
  - Static-electricity control
  - Vision alignment
  - Edge overlap
  - Particle contamination

technical_risks:
  - Separator wrinkle
  - Fold-position drift
  - Electrode skew
  - Tension variation
  - Burr-induced separator damage
  - Throughput-quality tradeoff

source_ids:
  - SRC-SKON-D04-021
  - SRC-SKON-D04-025

confidence:
  technology_use: VERY_HIGH
  production_parameters: NOT_DISCLOSED
```

공식 설명에 따르면 Z-Folding은 분리막을 절단된 낱장으로 반복 삽입하는 대신 연속된 분리막으로 양극과 음극을 감싸며 적층한다. SK온은 이 방식이 전극 가장자리 접촉 가능성을 낮추고 고속 생산에서도 정밀도를 확보하는 데 유리하다고 설명한다. ([ASK Inno][1])

### Relation Graph

```text
Z-Folding
├─ USES → Continuous Separator Web
├─ ALTERNATELY_STACKS → Cathode / Anode
├─ REDUCES → Electrode Edge Contact
├─ REDUCES → Internal Short-Circuit Risk
├─ REQUIRES → Precision Web Control
├─ REQUIRES → Vision Alignment
└─ APPLIED_TO → Pouch and Prismatic Cell Programs
```
