---
id: skes-d15-7-bess-ev-charging-risk
title: BESS & EV Charging Risk
summary: BESS와 EV 충전기의 실패 모드 및 모니터링 지표를 정의한 운영 리스크 매뉴얼
tags: [d15, risk, table]
keywords: [실패 모드, 리스크 지표, SOH, BMS, 가용성, 충전기 운영, 수익 위험, 열 이상, 통신 손실, 예측 오류]
related: [FM-ENS-D15-039, FM-ENS-D15-040, FM-ENS-D15-041, FM-ENS-D15-042, FM-ENS-D15-043, FM-ENS-D15-044, FM-ENS-D15-045, FM-ENS-D15-046, FM-ENS-D15-047, FM-ENS-D15-048, FM-ENS-D15-049, FM-ENS-D15-050, FM-ENS-D15-051, FM-ENS-D15-052, FM-ENS-D15-053, FM-ENS-D15-054, KRI-ENS-D15-027, KRI-ENS-D15-028, KRI-ENS-D15-029, KRI-ENS-D15-030, KRI-ENS-D15-031, KRI-ENS-D15-032, KRI-ENS-D15-033, KRI-ENS-D15-034]
priority: normal
domain: D15
section: 7
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 711
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 7. BESS & EV Charging Risk

## 7.1 KCE BESS Failure Modes

| FM ID | Failure Mode | Safety/Commercial Effect | Required Evidence |
|---|---|---|---|
| `FM-ENS-D15-039` | cell/module thermal anomaly | safety·availability | BMS/temp/incident logs |
| `FM-ENS-D15-040` | PCS/inverter failure | MW unavailable | fault/repair/LTSA |
| `FM-ENS-D15-041` | HVAC degradation | thermal stress·degradation | HVAC telemetry |
| `FM-ENS-D15-042` | BMS sensor/data failure | unsafe/false limit | redundancy/calibration |
| `FM-ENS-D15-043` | SOH mis-estimation | bid/warranty/lifecycle error | capacity test·model error |
| `FM-ENS-D15-044` | optimizer/model drift | suboptimal bid | counterfactual/P&L attribution |
| `FM-ENS-D15-045` | telemetry/ISO communication loss | dispatch/non-performance | market telemetry logs |
| `FM-ENS-D15-046` | revenue cannibalization | margin compression | competing MW·spread |
| `FM-ENS-D15-047` | market rule not reflected | compliance/revenue | rule version·deployment log |
| `FM-ENS-D15-048` | PFE/ITC evidence gap | tax credit at risk | supplier origin·tax workpaper |

## 7.2 EverCharge Failure Modes

| FM ID | Failure Mode | KRI | Loss Path |
|---|---|---|---|
| `FM-ENS-D15-049` | charger offline | uptime/MTTR | session·SLA·churn |
| `FM-ENS-D15-050` | payment/session failure | failed transaction | lost revenue/customer |
| `FM-ENS-D15-051` | building peak overload | site kW headroom | utility charge/reliability |
| `FM-ENS-D15-052` | fleet departure SOC miss | SOC at departure | fleet SLA |
| `FM-ENS-D15-053` | low site utilization | kWh/port/session | payback/CAC |
| `FM-ENS-D15-054` | remote access compromise | cyber alert | service/safety/data |

## 7.3 BESS/Charging KRIs

| KRI ID | 지표 | 주의점 |
|---|---|---|
| `KRI-ENS-D15-027` | BESS Availability | registered capacity와 분리 |
| `KRI-ENS-D15-028` | Thermal Alarm Density | population/시간 분모 포함 |
| `KRI-ENS-D15-029` | SOH Forecast Error | test result 대비 model |
| `KRI-ENS-D15-030` | Degradation Cost/MWh | bid P&L에 반영 여부 |
| `KRI-ENS-D15-031` | Bid Forecast Error | market regime별 분리 |
| `KRI-ENS-D15-032` | Revenue Concentration | energy/ancillary/capacity 비중 |
| `KRI-ENS-D15-033` | Competitor Operating MW | pipeline와 운영 분리 |
| `KRI-ENS-D15-034` | Charger Uptime | port·site·network 정의 명시 |
| `KRI-ENS-D15-035` | Failed Session Rate | attempted session 분모 |
| `KRI-ENS-D15-036` | Site Peak Headroom | panel/transformer/utility constraint |

---
