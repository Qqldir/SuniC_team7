---
id: skon-d04-d04-057-d04-057-electrolyte-filling-wetting-oi-m
title: D04-057 — Electrolyte Filling & Wetting — OI Metadata
summary: "배터리 셀 제조의 전해질 충전·웨팅 공정 운영 조건, 필요 역량, KPI와 함께 포메이션·에이징 기술을 정의한 제조 기술 가이드"
tags: [d04, technology, schema]
keywords: [습윤, 포메이션, 가스제거, 에이징, 셀 활성화, Wetting, Formation, Degassing, 초기 임피던스, 배터리 제조, 전해질 충전, 웨팅, 임피던스]
related: []
priority: normal
domain: D04
section: D04-057
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Manufacturing Technology Master > D04-057 — Electrolyte Filling & Wetting
tokens: 780
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Manufacturing Technology Master > D04-057 — Electrolyte Filling & Wetting

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: HIGH

  external_capability_needs:
    - Rapid wetting model
    - Electrolyte-distribution imaging
    - Gravimetric fill verification
    - Vacuum-pressure recipe optimization
    - Inline moisture sensing
    - Low-viscosity high-safety electrolyte

  poc_kpis:
    - Wetting time
    - Dry-area fraction
    - Electrolyte mass error
    - Residual gas
    - Initial impedance
    - Formation reject rate
```

---

## TECH-SKON-D04-058 — Formation, Degassing & Aging

```yaml
technology_id: TECH-SKON-D04-058
canonical_name: Cell Formation, Degassing and Aging
korean_name: 셀 포메이션·가스제거·에이징

technology_category:
  - Cell Activation
  - Electrochemical Conditioning
  - Quality Stabilization

technology_status:
  base_process: INDUSTRY_BASELINE
  sk_on_protocol: NOT_DISCLOSED

formation_functions:
  - Perform controlled initial charge and discharge
  - Establish electrode-electrolyte interphase
  - Activate cell capacity
  - Detect early electrical abnormality
  - Generate data for initial grading

degassing_functions:
  - Remove gas generated during early electrochemical reactions
  - Prepare cell for final sealing

aging_functions:
  - Observe voltage and impedance stability
  - Identify leakage or self-discharge
  - Detect latent defect
  - Stabilize cell before shipment or assembly

critical_process_parameters:
  - Formation current
  - Voltage limit
  - Temperature
  - Rest time
  - Pressure or compression
  - Number of cycles
  - Aging duration
  - Sampling frequency

critical_quality_attributes:
  - Initial capacity
  - Coulombic efficiency
  - Internal resistance
  - Self-discharge
  - Gas generation
  - Voltage stability
  - Temperature response

principal_cost_drivers:
  - Long process time
  - Large number of channels
  - Energy consumption
  - Controlled temperature
  - Factory space
  - Inventory tied up during aging

source_ids:
  - SRC-SKON-D04-039
  - SRC-SKON-D04-040
  - SRC-SKON-D04-041

confidence:
  process_definition: VERY_HIGH
  sk_on_duration_and_protocol: NOT_DISCLOSED
```

포메이션은 셀에 초기 충·방전을 실시해 계면을 형성하고 셀 성능을 활성화·검증하는 단계다. DOE의 과거 분석에서는 포메이션·선별이 셀 제조에서 상당한 시간과 비용을 차지하며, 당시 공정은 전체적으로 수 주가 소요될 수 있는 혁신대상으로 제시됐다. Argonne 모델도 포메이션·시험을 주요 자본집약 단계로 평가한다. 이 수치는 SK온의 현재 공정시간이나 비용을 뜻하지 않는다. ([energy.gov][6])
