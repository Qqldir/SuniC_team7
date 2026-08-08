---
id: skon-d04-d04-019-d04-019-soh-rul-residual-value-predictio
title: D04-019 — SOH·RUL·Residual Value Prediction — OI Metadata
summary: "배터리 건강도·수명·잔존 가치 예측 기술의 개발 우선순위와 필요 역량을 정의하고, GRIDON Gen 2의 DC·AC 블록 아키텍처, 시스템 경계, 인터페이스 및 기술 과제를 상세 설명하는 문서."
tags: [d04, technology, schema, "xref:d03"]
keywords: [배터리 진단, 수명 예측, 상태 추정, 임피던스 계측, 신뢰도 구간, 교차-차량 전이, 배터리 이력 인증, 진단 시간, 예측 오차, 모델 보정, SOH, RUL, 잔존 가치 예측, 배터리 건강도, ESS 아키텍처, DC/AC 블록, GRIDON, BMS, PCS, EMS]
related: []
priority: normal
domain: D04
section: D04-019
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Detailed Technology Master > D04-019 — SOH·RUL·Residual Value Prediction
tokens: 895
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Detailed Technology Master > D04-019 — SOH·RUL·Residual Value Prediction

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  missing_capabilities:
    - Physics-informed RUL model
    - Rapid impedance estimation
    - Confidence-interval prediction
    - Cross-vehicle transfer learning
    - Battery-history authentication
    - Standard battery health certificate

  poc_kpis:
    - SOH mean absolute error
    - RUL prediction error
    - Diagnosis time
    - Model-calibration error
    - Residual-value correlation
    - Cross-model generalization
```

---

## TECH-SKON-D04-020 — ESS DC/AC Block Architecture

```yaml
technology_id: TECH-SKON-D04-020
canonical_name: Flexible ESS DC/AC Block Architecture
korean_name: ESS DC·AC 블록 유연형 아키텍처

technology_category:
  - ESS System Architecture
  - Power Electronics Integration
  - Grid Interface

technology_status:
  dc_block: PRODUCT_AND_PRODUCTION_PLANNED
  ac_block: UNDER_DEVELOPMENT

related_products:
  - PROD-SKON-ESS-002 GRIDON Gen 1
  - PROD-SKON-ESS-003 GRIDON Gen 2
  - PROD-SKON-ESS-004 DC Block
  - PROD-SKON-ESS-005 AC Block Configuration

dc_block_boundary:
  included:
    - Battery cell
    - Module
    - Rack
    - Container
    - BMS
    - Thermal management
    - Fire-safety system

  typically_external:
    - PCS
    - Transformer
    - Grid-interconnection equipment
    - Site EMS

ac_block_boundary:
  included_or_integrated:
    - DC battery block
    - Power conversion system
    - Local controls
    - Protection interface

  external_or_site_level:
    - Transformer
    - Grid protection
    - Site energy-management system

value_propositions:
  dc_block:
    - Flexible PCS selection
    - Easier integration into existing projects
    - Separation of battery and power-conversion procurement

  ac_block:
    - Simplified customer procurement
    - Pre-integrated controls
    - Reduced site engineering
    - Potentially faster commissioning
    - Clearer system-level warranty boundary

critical_interfaces:
  - BMS to PCS
  - PCS to EMS
  - Thermal and fire alarm
  - Site SCADA
  - Grid-code response
  - Cybersecurity
  - Remote maintenance

technical_challenges:
  - Multi-vendor interoperability
  - Harmonic and power-quality control
  - Grid-code variation
  - Fault isolation
  - System-level warranty allocation
  - Software-version compatibility
  - Cybersecurity certification

source_ids:
  - SRC-SKON-D04-020
  - SRC-SKON-D03-057
  - SRC-SKON-D03-058

confidence:
  flexible_architecture: VERY_HIGH
  named_pcs_partner: NOT_DISCLOSED
  named_ems_partner: NOT_DISCLOSED
```

GRIDON Gen 2는 DC와 AC 블록 양쪽을 지원해 고객의 조달·통합 방식에 대응하도록 개발 중이다. 다만 PCS·EMS 공급사, 통신 프로토콜, 계통인증 및 통합 보증조건은 공개되지 않았다. ([ASK Inno][7])

### Architecture Graph

```text
GRIDON DC Block
├─ Battery Cell
├─ Module
├─ Rack
├─ Container
├─ BMS
├─ Thermal Management
└─ Fire Safety
       │
       ▼
External or Selected PCS
       │
       ▼
Site EMS / Grid

GRIDON AC Block
├─ DC Block
├─ Integrated PCS
├─ Local Control
└─ Protection Interface
       │
       ▼
Transformer / EMS / Grid
```
