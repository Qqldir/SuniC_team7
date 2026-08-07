---
id: skon-d04-d04-034-d04-034-ai-based-design-analysis-machine
title: D04-034 — AI-Based Design & Analysis Machine — OI Metadata
summary: 배터리 셀의 성능을 예측하고 원가를 계산하는 AI 모듈의 기술 구성과 검증 요구사항을 명시한 기술 명세서다.
tags: [d04, technology, schema]
keywords: [셀 성능예측, 원가계산, 베이지안 최적화, 서로게이트 모델, 물리 기반 신경망, 설계-원가 트레이드오프, 불확실성 정량화, TECH-SKON-D04-035, TECH-SKON-D04-036, 능동학습, 성능예측, 배터리 설계, 물리정보신경망, Surrogate modeling, 화학계 검증, 설계-비용 트레이드오프, 제조 공정 모델]
related: []
priority: normal
domain: D04
section: D04-034
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: "Digital, AI & Battery Intelligence Technology Master > D04-034 — AI-Based Design & Analysis Machine"
tokens: 1401
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Digital, AI & Battery Intelligence Technology Master > D04-034 — AI-Based Design & Analysis Machine

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: HIGH

  external_capability_needs:
    - Multi-objective Bayesian optimization
    - Physics-informed neural network
    - Constraint-aware generative design
    - Uncertainty quantification
    - Active learning
    - Design-space explainability
    - Automated simulation pipeline
```

---

## TECH-SKON-D04-035 — Cell Performance Prediction AI

```yaml
technology_id: TECH-SKON-D04-035
canonical_name: Cell Performance Prediction AI
korean_name: 셀 성능예측 AI

technology_category:
  - Predictive Engineering
  - Surrogate Modeling
  - Battery Simulation

technology_status: INTERNAL_COMPONENT
parent_platform:
  - TECH-SKON-D04-032
  - TECH-SKON-D04-034

prediction_targets:
  - Capacity
  - Energy density
  - Power
  - Internal resistance
  - Fast-charge performance
  - Cycle life
  - Thermal response
  - Requirement-compliance probability

possible_model_layers:
  evidence_status: ANALYTICAL_ARCHITECTURE
  layers:
    - Empirical data model
    - Physics-based model
    - Machine-learning surrogate
    - Hybrid physics-informed model

validation_requirements:
  - Holdout experiment
  - Chemistry-specific validation
  - Temperature-specific validation
  - Manufacturing-lot validation
  - Prediction interval
  - Out-of-distribution detection

source_ids:
  - SRC-SKON-D04-029

confidence:
  function_existence: VERY_HIGH
  exact_prediction_targets: PARTIALLY_DISCLOSED
  public_accuracy_data: NONE
```

SK온은 설계 후보별 성능예측 기능의 존재를 공개했지만, 예측오차와 시험세트, 모델의 물리 기반 여부 및 화학계별 일반화 성능은 공개하지 않았다. 따라서 위 세부 모델계층은 D17에서 검토할 분석 구조이며 SK온의 실제 내부 모델구성과 동일하다고 단정하지 않는다. ([ASK Inno][1])

---

## TECH-SKON-D04-036 — Cost Calculation AI

```yaml
technology_id: TECH-SKON-D04-036
canonical_name: Battery Cell Cost Calculation AI
korean_name: 배터리 셀 원가계산 AI

technology_category:
  - Cost Engineering
  - Design-to-Cost
  - R&D Decision Support

technology_status: INTERNAL_COMPONENT
parent_platform:
  - TECH-SKON-D04-032
  - TECH-SKON-D04-034

potential_cost_inputs:
  - Active-material usage
  - Separator and electrolyte usage
  - Cell housing
  - Process time
  - Equipment utilization
  - Yield assumption
  - Energy consumption
  - Material price
  - Logistics and localization

outputs:
  - Estimated cell cost
  - Cost-driver contribution
  - Design-alternative comparison
  - Requirement-cost tradeoff

company_expected_speed:
  improvement: approximately_700_times
  status: COMPANY_EXPECTATION

critical_controls:
  - Material-price timestamp
  - Currency and region
  - Plant and process version
  - Yield assumption
  - Contracted versus spot price
  - Confidential cost access

source_ids:
  - SRC-SKON-D04-029

confidence:
  function_existence: VERY_HIGH
  cost_model_detail: NOT_DISCLOSED
  realized_speed_gain: NOT_INDEPENDENTLY_VERIFIED
```

원가계산 AI는 설계 초기부터 성능과 비용을 함께 비교하도록 지원한다. 회사는 원가분석 속도가 약 700배 높아질 것으로 제시했으나, 해당 수치는 내부 기대효과이며 정확한 기준 작업과 실현실적은 공개되지 않았다. ([ASK Inno][1])

---

## TECH-SKON-D04-037 — Materials Development AI Researcher

```yaml
technology_id: TECH-SKON-D04-037
canonical_name: Materials Development AI Researcher
korean_name: 소재개발 AI 연구원

technology_category:
  - Materials Informatics
  - AI-Assisted Discovery
  - Experiment Optimization

technology_status: UNDER_DEVELOPMENT_AT_2026_DISCLOSURE
operational_status: NOT_CONFIRMED_COMPLETE

candidate_material_domains:
  evidence_status: ANALYTICAL_SCOPE
  domains:
    - Cathode composition
    - Anode composition
    - Electrolyte additive
    - Binder
    - Conductive additive
    - Solid electrolyte
    - Thermal and safety material

expected_functions:
  - Literature and internal-data analysis
  - Candidate-material generation
  - Property prediction
  - Experiment prioritization
  - Formulation optimization
  - Failure-cause analysis

company_expected_effect:
  material_development_time_reduction:
    target: approximately_50_percent
    status: COMPANY_EXPECTATION

source_ids:
  - SRC-SKON-D04-029

confidence:
  development_program: VERY_HIGH
  completed_platform: NOT_CONFIRMED
  functional_scope: PARTIALLY_INFERRED
```

2026년 3월 공식 자료에서 Materials Development AI Researcher는 구축 중인 시스템으로 설명됐다. 따라서 D04에서는 `UNDER_DEVELOPMENT`로 저장하고, 완료된 소재 발굴 플랫폼으로 분류하지 않는다. ([ASK Inno][1])
