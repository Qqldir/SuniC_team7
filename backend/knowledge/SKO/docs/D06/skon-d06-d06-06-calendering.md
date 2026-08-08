---
id: skon-d06-d06-06-calendering
title: Calendering
summary: "배터리 전극의 두께·밀도를 조절하는 압연 공정의 제조 파라미터, 결함 모드, AI 제어 아키텍처를 설명한다."
tags: [d06, process, schema, "xref:d04", "xref:d05"]
keywords: [전극 압연, Electrode Calendering, 밀도 제어, 공극 구조, 두께 제어, 공정 파라미터, 결함 모드, AI 제어, 자동제어, closed-loop control, 밀도 균형, Roll gap, 공극도 제어, AI 공정 최적화, 폐루프 제어, 두께 균일성, 입자 파손, Roll pressure, 전극 성능]
related: []
priority: normal
domain: D06
section: D06-06.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1178
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-06. Calendering

## 06.1 Process Role

```text
Dry Electrode Roll
        ↓
Preheating if required
        ↓
Roll Gap·Pressure·Speed Control
        ↓
Electrode Compression
        ↓
Thickness·Density·Porosity Adjustment
        ↓
Post-Calender Inspection
```

캘린더링은 전극의 두께·밀도와 공극구조를 조절해 체적 에너지밀도, 전기접촉과 이온이동 특성에 영향을 주는 공정이다. 과도한 압착은 입자 파손이나 공극 감소로 이어질 수 있어 밀도와 이온전달 사이의 균형이 필요하다. ([ASK Inno][12])

---

## PROC-SKON-D06-008 — Electrode Calendering

```yaml
process_id: PROC-SKON-D06-008
canonical_name: Electrode Calendering
korean_name: 전극 압연
process_layer: ELECTRODE
ownership_scope: SK_ON_DEVELOPMENT

equipment_classes:
  - Calender roll
  - Roll-gap actuator
  - Roll-heating system
  - Tension controller
  - Thickness gauge
  - Surface inspection system

critical_process_parameters:
  - Roll gap
  - Line speed
  - Roll pressure or force
  - Roll temperature
  - Web tension
  - Number of passes
  - Entry electrode temperature

critical_quality_attributes:
  - Electrode thickness
  - Electrode density
  - Porosity
  - Surface roughness
  - Adhesion
  - Electrical resistance
  - Thickness uniformity
  - Particle integrity

defect_modes:
  - Excessive densification
  - Insufficient densification
  - Particle fracture
  - Delamination
  - Electrode cracking
  - Thickness profile variation
  - Roll mark
  - Edge-wave defect

inspection_methods:
  - Inline thickness gauge
  - Density sampling
  - Porosity measurement
  - Peel test
  - Electrical resistance
  - Surface inspection

sk_on_confirmed_capability:
  - AI-based process-data analysis
  - Real-time correlation analysis
  - Input-condition optimization

not_confirmed:
  - Closed-loop control architecture
  - Production-line deployment
  - Quantified quality improvement
  - Quantified yield improvement

technology_ids:
  - TECH-SKON-D04-039
  - TECH-SKON-D04-052

patent_family_ids:
  - PF-SKON-D05-003

source_ids:
  - SRC-SKON-D06-001
  - SRC-BASE-D06-007
```

---

## 06.2 AI Calendering Data Architecture

```yaml
ai_calendering_architecture:

  inputs:
    material:
      - Active-material lot
      - Particle-size distribution
      - Binder lot
      - Electrode formulation

    upstream_process:
      - Slurry viscosity
      - Coating loading
      - Drying history
      - Residual solvent

    equipment:
      - Roll gap
      - Roll speed
      - Roll force
      - Roll temperature
      - Bearing vibration
      - Motor current

    inline_quality:
      - Thickness profile
      - Surface defect
      - Web tension
      - Electrode temperature

  model_outputs:
    - Predicted thickness
    - Predicted density
    - Defect risk
    - Recommended process setting
    - Confidence score

  control_modes:
    advisory:
      description: 작업자에게 설정값 추천

    supervised_closed_loop:
      description: 허용범위 내 자동조정 후 작업자 승인

    autonomous_closed_loop:
      description: 자동제어
      current_sk_on_status: NOT_CONFIRMED

  mandatory_governance:
    - Model version
    - Training-data range
    - Recipe applicability
    - Confidence threshold
    - Manual override
    - Change history
```

---

## 06.3 Calendering Pain-Point Graph

```text
Incoming Electrode Loading Variation
        ↓
Roll Force·Gap Response Variation
        ↓
Thickness and Porosity Variation
        ↓
Local Resistance·Electrolyte Wetting Difference
        ↓
Cell Capacity·Fast-Charge·Life Variation
```

```yaml
calendering_root_causes:

  material:
    - Particle-size variation
    - Particle strength
    - Binder distribution
    - Silicon content

  upstream:
    - Coating-loading variation
    - Drying-induced binder migration
    - Residual moisture

  equipment:
    - Roll deflection
    - Thermal expansion
    - Bearing wear
    - Gap calibration error

  operation:
    - Recipe mismatch
    - Speed change
    - Start-up transient
    - Product changeover
```

---
