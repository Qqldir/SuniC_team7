---
id: skes-d15-5-power-chp-city-gas-risk
title: "Power, CHP & City Gas Risk"
summary: "발전·열병합·가스 시설의 운영상 실패 18개를 정의하고 감지 수단, 모니터링 지표 10개를 제시한 문서."
tags: [d15, risk, table]
keywords: [실패모드, 강제정지, 가스누출, 핵심위험지표, 열효율, SCADA, 수요예측, 발전마진]
related: [FM-ENS-D15-013, FM-ENS-D15-014, FM-ENS-D15-015, FM-ENS-D15-016, FM-ENS-D15-017, FM-ENS-D15-018, FM-ENS-D15-019, FM-ENS-D15-020, FM-ENS-D15-021, FM-ENS-D15-022, FM-ENS-D15-023, FM-ENS-D15-024, FM-ENS-D15-025, FM-ENS-D15-026, FM-ENS-D15-027, FM-ENS-D15-028, KRI-ENS-D15-009, KRI-ENS-D15-010, KRI-ENS-D15-011, KRI-ENS-D15-012, KRI-ENS-D15-013, KRI-ENS-D15-014, KRI-ENS-D15-015, KRI-ENS-D15-016]
priority: normal
domain: D15
section: 5
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 886
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 5. Power, CHP & City Gas Risk

## 5.1 Power/CHP Failure Modes

| FM ID | Failure Mode | KRI | Loss Path | O/I Hook |
|---|---|---|---|---|
| `FM-ENS-D15-013` | gas turbine forced trip | vibration·temp·trip precursors | lost MWh·restart·SLA | predictive maintenance |
| `FM-ENS-D15-014` | HRSG/steam limitation | pressure/temp anomaly | heat/power joint margin | heat-power digital twin |
| `FM-ENS-D15-015` | heat demand mismatch | heat load forecast error | CHP suboptimal dispatch | joint forecast |
| `FM-ENS-D15-016` | heat-rate deterioration | heat rate vs corrected baseline | fuel cost·CO2 | performance degradation AI |
| `FM-ENS-D15-017` | planned outage overrun | work package critical path | scarcity-hour lost margin | turnaround control tower |
| `FM-ENS-D15-018` | grid/dispatch constraint | dispatch instruction/constraint | curtailment·lost margin | grid-event co-pilot |
| `FM-ENS-D15-019` | fuel-to-SMP spread collapse | clean spark spread | negative/low generation margin | margin-aware dispatch |
| `FM-ENS-D15-020` | emissions/carbon position gap | tCO2·allowance position | carbon cash cost | K-ETS position twin |

## 5.2 City Gas Failure Modes

| FM ID | Failure Mode | Detection | Consequence | Required Barrier |
|---|---|---|---|---|
| `FM-ENS-D15-021` | network leakage | pressure/flow/gas detector | safety·loss·outage | isolation·dispatch·inspection |
| `FM-ENS-D15-022` | pressure excursion | SCADA pressure deviation | customer/safety impact | regulator/valve protection |
| `FM-ENS-D15-023` | odorization anomaly | concentration/QA | leak detectability | sampling/verification |
| `FM-ENS-D15-024` | meter/settlement error | balance exception | billing·UFG distortion | meter QA·reconciliation |
| `FM-ENS-D15-025` | peak demand forecast miss | HDD/load error | supply/pressure imbalance | weather-normalized forecast |
| `FM-ENS-D15-026` | third-party excavation damage | permit/work proximity | pipeline incident | one-call/GIS/field alert |
| `FM-ENS-D15-027` | customer-site incident | emergency call pattern | safety·reputation | response triage |
| `FM-ENS-D15-028` | SCADA/telemetry loss | heartbeat/data quality | blind operation | local safe mode·redundancy |

## 5.3 Power/City Gas KRIs

| KRI ID | 지표 | 의미 |
|---|---|---|
| `KRI-ENS-D15-009` | Forced Outage Rate | planned와 분리한 비계획 정지 |
| `KRI-ENS-D15-010` | Trip Precursors | 보호계전·진동·온도 abnormal events |
| `KRI-ENS-D15-011` | Corrected Heat-Rate Gap | 날씨/부하 보정 후 효율 저하 |
| `KRI-ENS-D15-012` | Maintenance Critical-Path Slack | outage completion 여유 |
| `KRI-ENS-D15-013` | Clean Spark Spread | fuel·carbon 반영 발전마진 신호 |
| `KRI-ENS-D15-014` | Gas Balance Error | input-output-metered imbalance |
| `KRI-ENS-D15-015` | Pressure Excursion Count | 기준범위 이탈 event |
| `KRI-ENS-D15-016` | Emergency Response Aging | 미종결 긴급조치 시간 |
| `KRI-ENS-D15-017` | Weather-normalized Demand Error | HDD/CDD 보정 예측오차 |
| `KRI-ENS-D15-018` | Customer Electrification Churn | 구조적 수요이탈 신호 |

---
