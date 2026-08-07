---
id: skes-d15-8-liquid-hydrogen-risk-safety
title: Liquid Hydrogen Risk & Safety
summary: 액화수소 생산·저장·운송·충전 전 단계의 12가지 실패 모드와 9가지 핵심 리스크 지표(KRI)로 안전성과 수요 연계를 관리하는 리스크 프레임워크
tags: [d15, risk, table]
keywords: [액화수소, 실패모드, 안전장벽, 핵심리스크지표, BOG, 극저온저장, 수소공급망, 가동률, 누수탐지, 증기회수]
related: [FM-ENS-D15-055, FM-ENS-D15-056, FM-ENS-D15-057, FM-ENS-D15-058, FM-ENS-D15-059, FM-ENS-D15-060, FM-ENS-D15-061, FM-ENS-D15-062, FM-ENS-D15-063, FM-ENS-D15-064, FM-ENS-D15-065, FM-ENS-D15-066, KRI-ENS-D15-037, KRI-ENS-D15-038, KRI-ENS-D15-039, KRI-ENS-D15-040, KRI-ENS-D15-041, KRI-ENS-D15-042, KRI-ENS-D15-043, KRI-ENS-D15-044, KRI-ENS-D15-045]
priority: normal
domain: D15
section: 8
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 723
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 8. Liquid Hydrogen Risk & Safety

## 8.1 LH2 Risk Thread

```text
feed / electricity
→ liquefaction train
→ cryogenic storage
→ transfer/loading
→ tanker trailer
→ station storage/pump/dispenser
→ vehicle
```

수소는 `생산능력`보다 **안전한 질량 흐름과 실제 판매량**을 같이 봐야 한다. 안전성이 나쁘면 가동률을 높일 수 없고, 수요가 약하면 정상가동 자체가 경제성을 보장하지 않는다.

## 8.2 Failure Modes

| FM ID | Failure Mode | Detection/Barrier | Consequence |
|---|---|---|---|
| `FM-ENS-D15-055` | cryogenic containment leak | gas detector·inspection·isolation | fire/explosion/asphyxiation/cold burn |
| `FM-ENS-D15-056` | overpressure / relief impairment | pressure·PSV test | vessel/piping hazard |
| `FM-ENS-D15-057` | vacuum insulation degradation | pressure/temp/evaporation | BOG·energy loss·pressure |
| `FM-ENS-D15-058` | liquefier trip | compressor/refrigeration alarms | production loss |
| `FM-ENS-D15-059` | BOG exceeds recovery | mass balance | product loss/pressure |
| `FM-ENS-D15-060` | transfer coupling/leak | detector/interlock | release during loading |
| `FM-ENS-D15-061` | trailer logistics delay | ETA/inventory | station stockout |
| `FM-ENS-D15-062` | station pump/dispenser failure | fault/MTTR | vehicle demand loss |
| `FM-ENS-D15-063` | ESD/interlock failure | proof test | escalation of release |
| `FM-ENS-D15-064` | certification/evidence gap | permit/certificate status | operation/sale restriction |
| `FM-ENS-D15-065` | vehicle rollout lag | active vehicles | plant/station underutilization |
| `FM-ENS-D15-066` | contracted demand fails to become paid kg | sold/paid kg | cash/payback stress |

## 8.3 LH2 KRIs

| KRI ID | 지표 | 의미 |
|---|---|---|
| `KRI-ENS-D15-037` | Train Availability | 3개 train 개별/전체 구분 |
| `KRI-ENS-D15-038` | BOG Ratio | 생산/저장/운송 구간별 |
| `KRI-ENS-D15-039` | Safety Barrier Impairment | detector/ESD/PSV 미가용 시간 |
| `KRI-ENS-D15-040` | Overdue Proof Test | safety-critical test 미완료 |
| `KRI-ENS-D15-041` | Sold kg / Produced kg | inventory 증가와 실제수요 구분 |
| `KRI-ENS-D15-042` | Paid kg / Delivered kg | 수금 포함 unit economics |
| `KRI-ENS-D15-043` | Station Availability | network demand enablement |
| `KRI-ENS-D15-044` | Active Vehicle Count | MOU/도입목표와 분리 |
| `KRI-ENS-D15-045` | Days of Station Inventory | 물류중단 resilience |

---
