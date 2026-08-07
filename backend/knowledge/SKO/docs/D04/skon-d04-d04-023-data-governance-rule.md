---
id: skon-d04-d04-023-data-governance-rule
title: Data Governance Rule
summary: 배터리팩 기술 공개 범위(ENPASS CCS·분리막 관련)와 S-Pack CTP 안전 아키텍처의 기술 사양·상용화 현황을 규정하는 거버넌스 문서다.
tags: [d04, technology, schema]
keywords: [ENPASS CCS, SKIET, S-Pack CTP, 셀투팩, 분리막, 권리 명제, 열 차단, 가스 경로 제어, S-Pack, 열차단, 가스경로제어, 안전아키텍처, Z-Folding, 상용화현황]
related: []
priority: normal
domain: D04
section: D04-023
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Safety & Thermal Technology Master > D04-023 — Ceramic-Coated Separator Safety Interface
tokens: 551
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Safety & Thermal Technology Master > D04-023 — Ceramic-Coated Separator Safety Interface

### Data Governance Rule

```yaml
governance_rule:
  prohibited_statement:
    - SK On owns ENPASS CCS
    - All SK On cells use the same SKIET separator specification

  permitted_statement:
    - SKIET owns and develops ENPASS CCS
    - Separator and Z-Folding jointly contribute to cell-level isolation
    - Product-level separator mapping requires contract or BOM evidence
```

---

## TECH-SKON-D04-024 — S-Pack CTP Safety Architecture

```yaml
technology_id: TECH-SKON-D04-024
canonical_name: S-Pack CTP Safety Architecture
korean_name: S-Pack 셀투팩 안전 아키텍처

technology_category:
  - Cell-to-Pack
  - Pack Safety
  - Thermal Propagation Mitigation
  - Gas-Path Management

technology_status: TECHNOLOGY_DEMONSTRATION
commercial_vehicle_application: NOT_PUBLICLY_CONFIRMED

architecture:
  module_reduction: true
  cell_volume_utilization: INCREASED_COMPANY_CLAIM
  internal_component_simplification: true

safety_functions:
  - Thermal blocking
  - Heat-spread control
  - Gas-path control
  - Abnormal-cell isolation
  - Pack-level containment

value_propositions:
  - Improved cell-volume ratio
  - Potential pack energy-density improvement
  - Reduced structural components
  - Safety and efficiency integration

critical_challenges:
  - Removal of module-level protection
  - Pack structural rigidity
  - Cell swelling management
  - Thermal barrier durability
  - Gas-discharge routing
  - Crash integrity
  - Repairability
  - Cell-to-pack assembly tolerance

source_ids:
  - SRC-SKON-D04-022

confidence:
  disclosed_architecture: VERY_HIGH
  commercial_application: LOW
```

S-Pack은 모듈을 최소화한 CTP 구조와 열 차단·가스 경로 제어를 결합한 초기 팩 솔루션이다. 공식 전시자료는 제품 개념과 기술방향을 보여주지만 특정 차량에 상용 적용됐다는 근거는 제공하지 않는다. ([ASK Inno][2])
