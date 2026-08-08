---
id: skon-d04-d04-018-d04-018-baas-ai-platform-oi-metadata
title: D04-018 — BaaS AI Platform — OI Metadata
summary: "배터리의 현재 상태(SOH), 잔여수명(RUL), 잔존가치를 예측하는 AI 기술의 기술 스펙, 모델 구조, 입력변수, 불확실성 요소를 설명하는 문서."
tags: [d04, technology, schema]
keywords: [SOH, RUL, 배터리 진단, 잔존가치, 중고차 평가, 건강상태, 수명 예측, 머신러닝, 중고 EV 평가, 배터리 여권, 상태 진단, 잔여수명]
related: []
priority: normal
domain: D04
section: D04-018
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Detailed Technology Master > D04-018 — BaaS AI Platform
tokens: 797
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Detailed Technology Master > D04-018 — BaaS AI Platform

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: HIGH

  missing_capabilities:
    - Cross-OEM data standard
    - Data-access consent framework
    - Cloud-edge hybrid diagnostics
    - Explainable battery diagnosis
    - Fraud-resistant battery history
    - Federated learning
    - Digital battery passport integration

  poc_kpis:
    - Detection accuracy
    - Warning lead time
    - SOH error
    - Data transmission cost
    - Model transferability
    - User adoption
```

---

## TECH-SKON-D04-019 — SOH·RUL·Residual Value Prediction

```yaml
technology_id: TECH-SKON-D04-019
canonical_name: Battery Health and Residual-Value Prediction
korean_name: 배터리 건강상태·잔여수명·잔존가치 예측

technology_category:
  - Battery Diagnostics
  - Predictive Analytics
  - Asset Valuation

technology_status: PILOT_AND_STANDARDIZATION

core_outputs:
  SOH:
    full_name: State of Health
    purpose: Current performance relative to reference condition

  RUL:
    full_name: Remaining Useful Life
    purpose: Predicted operating time or cycles before threshold

  residual_value:
    purpose:
      - Used-EV valuation
      - Warranty decision
      - Reuse screening
      - Recycling routing

model_inputs:
  - Capacity trend
  - Internal resistance trend
  - Temperature exposure
  - Fast-charging history
  - Depth of discharge
  - Storage duration
  - Driving load
  - Abnormal-event history

model_classes:
  - Empirical model
  - Electrochemical model
  - Machine-learning model
  - Hybrid physics-informed model

principal_uncertainties:
  - Hidden vehicle history
  - Battery-model variation
  - Sensor error
  - Temperature variation
  - Sparse aging data
  - Future usage pattern
  - End-of-life threshold definition

related_technologies:
  - BaaS AI
  - EIS-Based BMS
  - Battery Passport
  - Fleet Analytics

source_ids:
  - SRC-SKON-D04-018
  - SRC-SKON-D04-019

confidence:
  capability_existence: VERY_HIGH
  exact_algorithm: NOT_DISCLOSED
  accuracy: NOT_DISCLOSED
```

SK온은 미래 수명과 잔존가치 예측을 BaaS AI의 공식 기능으로 제시하고 중고 EV 평가와 표준개발에 활용했다. 다만 공개자료에는 SOH 오차율, RUL 신뢰구간, 진단시간 및 차량모델별 정확도가 제공되지 않았다. ([ASK Inno][10])

### Analysis Layer

```yaml
analysis:
  value_chain_effect:
    - Increase trust in used-EV transaction
    - Reduce fleet-maintenance uncertainty
    - Improve battery-warranty pricing
    - Support reuse-versus-recycle decision
    - Create battery-backed finance products

  critical_requirement:
    - Prediction result must include uncertainty
    - Models must be chemistry and vehicle aware
    - Historical data integrity must be verifiable
```
