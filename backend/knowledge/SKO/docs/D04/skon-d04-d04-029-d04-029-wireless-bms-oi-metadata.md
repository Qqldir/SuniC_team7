---
id: skon-d04-d04-029-d04-029-wireless-bms-oi-metadata
title: D04-029 — Wireless BMS — OI Metadata
summary: "무선 배터리 관리시스템의 기술 결점과 다계층 이상감지 기술(BaaS AI, EIS 기반)의 구현 현황 및 성능 지표 메타데이터."
tags: [d04, technology, schema]
keywords: [무선 BMS, 배터리 이상감지, EIS, 다계층 배터리 진단, BaaS AI, 조기 경고 시스템, 열 이벤트, 예측 유지보수, 배터리 상태 추정, 센서 데이터 융합, 임피던스 분석, 열 이벤트 예측, 센서 데이터, 무선 통신, 배터리 진단]
related: []
priority: normal
domain: D04
section: D04-029
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Safety & Thermal Technology Master > D04-029 — Wireless BMS
tokens: 931
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Safety & Thermal Technology Master > D04-029 — Wireless BMS

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  missing_capabilities:
    - Automotive-grade ultra-low-power wireless chipset
    - Deterministic wireless protocol
    - Functional-safety certification
    - Intrusion detection
    - Over-the-air security update
    - Fluid-environment RF propagation model
    - Cell-level secure identity
    - Battery-passport data connector

  poc_kpis:
    - Packet error rate
    - Communication latency
    - Power consumption per node
    - Synchronization error
    - RF availability
    - Cyberattack detection rate
    - Vibration durability
    - Harness mass reduction
```

---

## TECH-SKON-D04-030 — Multi-Layer Battery Abnormality Detection

```yaml
technology_id: TECH-SKON-D04-030
canonical_name: Multi-Layer Battery Abnormality Detection
korean_name: 다계층 배터리 이상감지 기술

technology_category:
  - Battery Diagnostics
  - Predictive Safety
  - BMS
  - BaaS

technology_status:
  ev_baas: PILOT_AND_PARTNER_APPLICATION
  ess_eis: PRODUCT_INTEGRATED
  wireless_bms: PROTOTYPE

detection_layers:
  conventional_bms:
    data:
      - Voltage
      - Current
      - Temperature
      - SOC
    purpose:
      - Threshold alarm
      - Cell balancing
      - Overcharge and overdischarge protection

  baas_ai:
    data:
      - Driving history
      - Charging history
      - Longitudinal operating data
    purpose:
      - Abnormality prediction
      - Lifetime assessment
      - Risk notification

  eis_based_bms:
    data:
      - Frequency-dependent impedance
    purpose:
      - Internal-condition diagnosis
      - Early anomaly detection
      - ESS predictive maintenance

  future_wireless_bms:
    data:
      - Distributed cell-level data
      - Lifecycle identity data
    purpose:
      - Higher-granularity monitoring
      - Reduced harness dependency

publicly_disclosed_early_warning:
  EIS:
    thermal_event_lead_time:
      value: at_least_30
      unit: minutes
      evidence_type: COMPANY_CLAIM

critical_model_requirements:
  - Low false-positive rate
  - Chemistry-specific model
  - Temperature and SOC compensation
  - Sensor-drift correction
  - Explainable diagnosis
  - Confidence score
  - Safe fallback logic

related_technologies:
  - TECH-SKON-D04-008
  - TECH-SKON-D04-018
  - TECH-SKON-D04-019
  - TECH-SKON-D04-029

source_ids:
  - SRC-SKON-D04-018
  - SRC-SKON-D04-019
  - SRC-SKON-D04-026

confidence:
  technology_layers: VERY_HIGH
  warning_time: HIGH_AS_COMPANY_CLAIM
  detailed_algorithm: NOT_DISCLOSED
```

SK온은 EV 영역에서 BaaS AI를 이용해 주행·충전 이력 기반 이상감지를 추진했고, ESS에서는 EIS를 활용한 내부상태 분석을 제품에 연결했다. 2026년 VIB 협력 발표에서 SK온은 EIS가 열 이벤트 발생 가능 시점보다 최소 30분 앞서 이상신호를 식별할 수 있다고 밝혔지만, 시험조건과 오탐률은 공개하지 않았다. ([ASK Inno][8])

### Detection Chain

```text
센서 데이터
→ 데이터 품질 검증
→ 상태 추정
→ 이상 점수
→ 원인 분류
→ 위험도 산정
→ 경고·출력 제한
→ 정비 또는 시스템 격리
```
