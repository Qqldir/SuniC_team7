---
id: skes-d06-16-kpi-dictionary
title: KPI Dictionary
summary: "LNG, 전력, 도시가스, 재생에너지 등 에너지 사업별 핵심성과지표의 정의, 측정 경계, 오용 방지 규칙을 정리한 관리 기준서"
tags: [d06, process, table]
keywords: [핵심성과지표, LNG 터미널, entitlement realization, net heat rate, 도시가스, 강제정지율, 재생에너지, 성과 측정, 운영 효율, 압력 준수율]
related: [KPI-ENS-D06-LNG-001, KPI-ENS-D06-LNG-002, KPI-ENS-D06-LNG-003, KPI-ENS-D06-LNG-004, KPI-ENS-D06-LNG-005, KPI-ENS-D06-LNG-006, KPI-ENS-D06-LNG-007, KPI-ENS-D06-PWR-001, KPI-ENS-D06-PWR-002, KPI-ENS-D06-PWR-003, KPI-ENS-D06-PWR-004, KPI-ENS-D06-PWR-005, KPI-ENS-D06-PWR-006, KPI-ENS-D06-PWR-007, KPI-ENS-D06-CHP-001, KPI-ENS-D06-CHP-002, KPI-ENS-D06-CG-001, KPI-ENS-D06-CG-002, KPI-ENS-D06-CG-003, KPI-ENS-D06-CG-004, KPI-ENS-D06-CG-005, KPI-ENS-D06-CG-006, KPI-ENS-D06-CG-007, KPI-ENS-D06-REN-001]
priority: normal
domain: D06
section: 16
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1573
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 16. KPI Dictionary

## 16.1 LNG and Terminal KPIs

| KPI ID | KPI | Definition boundary | Anti-misuse rule |
|---|---|---|---|
| `KPI-ENS-D06-LNG-001` | entitlement realization | actual available entitlement / planned entitlement | gross project production과 혼합 금지 |
| `KPI-ENS-D06-LNG-002` | cargo on-time arrival | arrival within approved window | schedule 변경 후 기준시점 기록 |
| `KPI-ENS-D06-LNG-003` | inventory reconciliation error | physical closing vs book closing | volume·mass·energy 기준 분리 |
| `KPI-ENS-D06-LNG-004` | BOG recovery ratio | recovered BOG / generated BOG | 생성량 계산방식 버전 필수 |
| `KPI-ENS-D06-LNG-005` | terminal sendout availability | available sendout capacity / required | 설계능력과 실제 수요 분리 |
| `KPI-ENS-D06-LNG-006` | unloading turnaround | all-fast to disconnect or agreed boundary | weather/port/terminal 지연 원인 분리 |
| `KPI-ENS-D06-LNG-007` | nomination accuracy | nominated vs actual energy | 표준상태·발열량 정합 필수 |

## 16.2 Power and CHP KPIs

| KPI ID | KPI | Definition boundary | Anti-misuse rule |
|---|---|---|---|
| `KPI-ENS-D06-PWR-001` | net heat rate | fuel energy / net MWh | HHV/LHV와 보정조건 고정 |
| `KPI-ENS-D06-PWR-002` | corrected output | ambient-corrected generation | 실제 판매전력과 혼동 금지 |
| `KPI-ENS-D06-PWR-003` | start reliability | successful starts / attempted starts | 모드별 cold/warm/hot 분리 |
| `KPI-ENS-D06-PWR-004` | forced outage factor | forced outage hours / applicable period | planned outage 분리 |
| `KPI-ENS-D06-PWR-005` | degradation index | actual vs clean/reference curve | OEM 기준과 내부 기준 버전 기록 |
| `KPI-ENS-D06-PWR-006` | dispatch adherence | actual vs instruction | ramp·reserve mode 분리 |
| `KPI-ENS-D06-PWR-007` | emissions intensity | valid emissions / net MWh | startup/shutdown 별도 표시 |
| `KPI-ENS-D06-CHP-001` | heat network loss | produced minus delivered heat | 계량 경계·시간정합 필수 |
| `KPI-ENS-D06-CHP-002` | return temperature performance | actual vs target return T | 고객·계절 조건 분리 |

## 16.3 City-Gas KPIs

| KPI ID | KPI | Definition boundary | Anti-misuse rule |
|---|---|---|---|
| `KPI-ENS-D06-CG-001` | pressure compliance | valid intervals within approved band | 센서 미수신을 정상으로 처리 금지 |
| `KPI-ENS-D06-CG-002` | risk inspection coverage | completed risk-weighted scope / plan | 단순 거리와 혼합 금지 |
| `KPI-ENS-D06-CG-003` | leak response time | verified call to safe state | 접수·출동·도착·차단을 분리 저장 |
| `KPI-ENS-D06-CG-004` | unaccounted-for gas | custody input minus billed/known use | 계량오차·시간차·실제손실 분리 |
| `KPI-ENS-D06-CG-005` | actual meter read rate | valid actual reads / due meters | 추정·대체값 제외 |
| `KPI-ENS-D06-CG-006` | regulator stability | pressure deviation/hunting metric | 설비별 정상운전 범위 내부확정 |
| `KPI-ENS-D06-CG-007` | work closure lead time | anomaly confirmed to verified close | 행정종결과 현장복구 분리 |

## 16.4 Renewable·ESS·EV KPIs

| KPI ID | KPI | Definition boundary | Anti-misuse rule |
|---|---|---|---|
| `KPI-ENS-D06-REN-001` | forecast error | market/horizon-specific metric | curtailment·고장 구간 label 분리 |
| `KPI-ENS-D06-REN-002` | energy availability | actual lost energy basis | 시간 availability와 혼합 금지 |
| `KPI-ENS-D06-REN-003` | performance ratio | normalized actual vs expected | 모델·센서 버전 기록 |
| `KPI-ENS-D06-REN-004` | curtailment loss | counterfactual expected energy | 추정치 불확실성 표시 |
| `KPI-ENS-D06-ESS-001` | dispatch tracking | actual vs instruction | safety override 별도 |
| `KPI-ENS-D06-ESS-002` | round-trip efficiency | discharged / charged energy | 경계·대기전력 정의 |
| `KPI-ENS-D06-ESS-003` | degradation per throughput | usable loss / energy throughput | 달력열화와 분리 |
| `KPI-ENS-D06-EVC-001` | successful session rate | energized valid sessions / attempts | 인증·결제·차량·충전기 원인 분리 |
| `KPI-ENS-D06-EVC-002` | port availability | usable ports / scheduled time | 통신미수신 상태 처리 규칙 필요 |

## 16.5 Hydrogen·CCS KPIs

| KPI ID | KPI | Definition boundary | Anti-misuse rule |
|---|---|---|---|
| `KPI-ENS-D06-H2-001` | liquefaction specific energy | net electricity / LH₂ produced | 보조설비 경계 명시 |
| `KPI-ENS-D06-H2-002` | hydrogen recovery | delivered product / accepted feed | purge·vent·BOG 경로 분리 |
| `KPI-ENS-D06-H2-003` | boil-off rate | defined loss / inventory and time | DOE 목표값을 E&S 실적으로 사용 금지 |
| `KPI-ENS-D06-H2-004` | delivery loss | loaded minus accepted mass | 계량불확실성 분리 |
| `KPI-ENS-D06-CCS-001` | capture rate | captured / source CO₂ | net avoided와 동일시 금지 |
| `KPI-ENS-D06-CCS-002` | net avoided CO₂ | baseline minus full-chain emissions | 경계·전력배출계수 버전 필수 |
| `KPI-ENS-D06-CCS-003` | capture energy penalty | incremental energy per CO₂ | 발전량 변화 정규화 |
| `KPI-ENS-D06-CCS-004` | MRV completeness | valid required records / due records | 추정대체값 별도 표시 |

---
