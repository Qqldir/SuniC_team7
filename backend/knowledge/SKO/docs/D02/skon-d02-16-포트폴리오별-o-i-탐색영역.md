---
id: skon-d02-16-포트폴리오별-o-i-탐색영역
title: 포트폴리오별 O/I 탐색영역
summary: "SK온의 주요 사업군(배터리, ESS, BaaS 등)에서 추진 가능한 AI·디지털 혁신 영역을 정리하고 비즈니스 엔티티 관계를 매핑한 마스터 자료."
tags: [d02, business]
keywords: [EV 배터리, 에너지 저장, 배터리 서비스, Manufacturing AI, 예측 유지보수, 디지털 트윈, 열관리, 공급망, 배터리 재사용, 거래 분석, 전기차 배터리, 에너지저장장치, Battery as a Service, SOC/SOH 추정, 공급망 최적화, 배터리 재활용]
related: []
priority: normal
domain: D02
section: 16
source: SK온_D02_Business_Portfolio.md
breadcrumb: ""
tokens: 727
updated: 2026-08-03
---

> SK온 · D02 사업 포트폴리오

# 16. 포트폴리오별 O/I 탐색영역

## 16.1 전기차 배터리

```text
Advanced Materials
Fast Charging
Battery Safety
Cell Design
Manufacturing AI
AI Vision Inspection
Predictive Maintenance
Digital Twin
Yield Optimization
Low-carbon Manufacturing
```

## 16.2 ESS

```text
Fire Detection and Suppression
Thermal Propagation Prevention
LFP Performance Optimization
VIB System Integration
ESS Management System
Lifetime Prediction
Grid Optimization
Cybersecurity
Container Thermal Management
```

## 16.3 BaaS

```text
SOC/SOH Estimation
Battery Digital Passport
Residual Value Assessment
Battery Data Platform
Predictive Diagnostics
Reuse Matching Platform
Collection Logistics
Recycling Traceability
Insurance and Finance Integration
```

## 16.4 트레이딩·공급망

```text
Commodity Price Forecasting
Supply Chain Risk Intelligence
Origin Traceability
Carbon Data Management
Shipping Optimization
Contract Intelligence
Trading Risk Analytics
```

## 16.5 열관리·에너지효율

```text
Immersion Cooling Fluid
Thermal Simulation
Leak Detection
Cooling Control
Heat Recovery
Data Center Cooling
Battery Pack Thermal Safety
Energy Optimization
```

이 목록은 공식 사업내용을 기반으로 한 O/I 탐색 분류이며, 실제 내부 수요 여부는 D15에서 검증한다.

---

# 17. Business Portfolio 엔티티 마스터

```text
BUS-SKON-EV-001          Electric Vehicle Battery
BUS-SKON-ESS-001         Energy Storage System
BUS-SKON-BAAS-001        Battery as a Service
BUS-SKON-THERMAL-001     Battery Thermal Management
BUS-SKON-TRADING-001     Global Trading
BUS-SKON-TERMINAL-001    Terminal and Logistics
BUS-SKON-LBO-001         Lube Base Oil
BUS-SKON-ENERGY-EFF-001  Energy Efficiency Solutions
```

---

# 18. 주요 관계 데이터

```text
SK_ON — OPERATES_BUSINESS → EV_BATTERY
SK_ON — OPERATES_BUSINESS → ESS
SK_ON — OPERATES_BUSINESS → BAAS

EV_BATTERY — PROVIDES → CELL
EV_BATTERY — PROVIDES → MODULE
EV_BATTERY — PROVIDES → PACK
EV_BATTERY — SERVES → AUTOMOTIVE_OEM

ESS — USES_CHEMISTRY → NCM
ESS — USES_CHEMISTRY → LFP
ESS — DEVELOPS_WITH_PARTNER → VIB
ESS — SERVES → BESS_DEVELOPER
ESS — INCLUDES → LIFESPAN_MANAGEMENT

BAAS — INCLUDES → RENTAL
BAAS — INCLUDES → CHARGING
BAAS — INCLUDES → DIAGNOSIS
BAAS — INCLUDES → REUSE
BAAS — INCLUDES → RECYCLING

SK_ON — OPERATES_CIC_BUSINESS → TRADING
SK_ON — OPERATES_CIC_BUSINESS → LUBE_BASE_OIL
SK_ON — EXPANDS_TO → THERMAL_MANAGEMENT

THERMAL_MANAGEMENT — APPLIES_TO → EV_BATTERY
THERMAL_MANAGEMENT — APPLIES_TO → ESS
```

---
