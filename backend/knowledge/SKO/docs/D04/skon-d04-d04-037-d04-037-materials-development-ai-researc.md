---
id: skon-d04-d04-037-d04-037-materials-development-ai-researc
title: D04-037 — Materials Development AI Researcher — OI Metadata
summary: "배터리 재료 개발 AI 시스템에서 부족한 역량과 파운데이션 모델, 공정제어 기술 등 필요한 목표 기술을 정의한 메타데이터"
tags: [d04, technology, schema, "xref:d17"]
keywords: [지식그래프, 문헌 마이닝, 분자 특성 예측, 능동 학습, 파운데이션 모델, 멀티모달, 공정 제어, 드라이 전극, 결함 분류, 배터리 재료 개발, 물성 예측, 공정 제어 AI, 다중충실도 능동학습, 물질 정보 그래프, 캘린더링, 건식 전극, 멀티모달 AI, 역량 갭]
related: []
priority: normal
domain: D04
section: D04-037
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: "Digital, AI & Battery Intelligence Technology Master > D04-037 — Materials Development AI Researcher"
tokens: 1226
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Digital, AI & Battery Intelligence Technology Master > D04-037 — Materials Development AI Researcher

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  missing_capabilities:
    - Materials knowledge graph
    - Literature and patent mining
    - Molecular and crystal-property model
    - Autonomous formulation laboratory
    - Negative-result data integration
    - Multi-fidelity active learning
    - Synthesis feasibility prediction

  poc_kpis:
    - Candidate hit rate
    - Experiments per successful candidate
    - Property-prediction error
    - Development time
    - Researcher adoption
```

---

## TECH-SKON-D04-038 — Battery Foundation Model Target Capability

```yaml
technology_id: TECH-SKON-D04-038
canonical_name: Battery Foundation Model Target Capability
korean_name: 배터리 파운데이션 모델 목표역량

technology_category:
  - Foundation Model
  - Multimodal Battery Intelligence
  - Strategic AI Capability

technology_status: ANALYTICAL_TARGET_CAPABILITY
sk_on_official_named_program: NOT_CONFIRMED
commercial_status: NOT_APPLICABLE

reason_for_registration:
  - AI Researcher contains multiple battery-specific AI systems
  - Data spans experiments, processes and cell designs
  - Future reuse across R&D, manufacturing and operation requires common representation
  - No reviewed official source explicitly names an SK On Battery Foundation Model

potential_modalities:
  - Text and RFQ
  - Material composition
  - Experimental table
  - Time-series sensor data
  - Microscopy image
  - X-ray and CT image
  - Process recipe
  - Electrochemical curve
  - Patent and paper

potential_tasks:
  - Requirement understanding
  - Material-property prediction
  - Cell-design generation
  - Defect classification
  - Degradation prediction
  - Root-cause analysis
  - Technical question answering

evidence_basis:
  - SRC-SKON-D04-029
  - SRC-SKON-D04-030
  - SRC-SKON-D04-034

information_type: ANALYSIS
confidence:
  strategic_relevance: HIGH
  current_internal_implementation: UNCONFIRMED
```

검토한 SK온 공식 자료에는 `Battery Foundation Model`이라는 명칭의 플랫폼이 확인되지 않았다. 따라서 이 엔티티는 현재 보유기술이 아니라, AI Researcher·공정 AI·BaaS AI의 데이터와 모델을 공통 기반으로 연결할 수 있는 D17 후보역량으로만 등록한다. ([ASK Inno][1])

---

## TECH-SKON-D04-039 — AI Calendering Process Control

```yaml
technology_id: TECH-SKON-D04-039
canonical_name: AI Calendering Process Control
korean_name: AI 기반 캘린더링 공정제어

technology_category:
  - Manufacturing AI
  - Adaptive Process Control
  - Dry Electrode
  - Quality Optimization

technology_status: DEVELOPMENT_AND_PROCESS_APPLICATION_DISCLOSED
production_line: NOT_DISCLOSED

process_inputs:
  - Roll speed
  - Roll pressure
  - Roll temperature
  - Powder feed
  - Electrode thickness
  - Electrode density
  - Environmental condition
  - Historical quality data

ai_functions:
  - Real-time correlation analysis
  - Optimal set-point calculation
  - Condition-change response
  - Process-stability monitoring
  - Quality prediction

target_outputs:
  - Uniform thickness
  - Uniform density
  - Controlled porosity
  - Reduced defect
  - Improved production efficiency

principal_risks:
  - Sensor drift
  - Delayed feedback
  - Model instability
  - Equipment-to-equipment variation
  - Unseen material formulation
  - Unsafe autonomous set-point change

source_ids:
  - SRC-SKON-D04-030

confidence:
  technology_disclosure: VERY_HIGH
  production_scale: NOT_DISCLOSED
  quantitative_yield_effect: NOT_DISCLOSED
```

건식전극은 분말을 균일한 두께와 밀도로 압착하는 캘린더링이 품질과 양산성을 결정한다. SK온은 AI가 공정데이터를 실시간 분석하고 조건 변화에 맞춰 입력값을 조정하는 구조를 공개했지만, 인간 승인 없이 완전자율 제어하는지는 확인되지 않았다. ([ASK Inno][2])

### Closed-Loop Architecture

```text
Material and Equipment Data
    ↓
Sensor Validation
    ↓
AI Quality Prediction
    ↓
Optimal Set-Point Recommendation
    ↓
Safety and Constraint Check
    ↓
Equipment Input Adjustment
    ↓
Inline Quality Measurement
    └──────── Feedback ────────┘
```
