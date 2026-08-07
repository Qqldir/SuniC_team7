---
id: skes-d15-4-lng-value-chain-risk-failure-modes
title: LNG Value Chain Risk & Failure Modes
summary: LNG 공급망에서 가스 공급 중단을 초래하는 12개 실패 모드의 선행신호와 감시 지표를 정의한 문서
tags: [d15, risk, table]
keywords: [공급망 리스크, 실패모드, 선행신호, KRI, BOG, 선박 지연, 터미널 제약, 계약 미활용]
related: [FM-ENS-D15-001, FM-ENS-D15-002, FM-ENS-D15-003, FM-ENS-D15-004, FM-ENS-D15-005, FM-ENS-D15-006, FM-ENS-D15-007, FM-ENS-D15-008, FM-ENS-D15-009, FM-ENS-D15-010, FM-ENS-D15-011, FM-ENS-D15-012, KRI-ENS-D15-001, KRI-ENS-D15-002, KRI-ENS-D15-003, KRI-ENS-D15-004, KRI-ENS-D15-005, KRI-ENS-D15-006, KRI-ENS-D15-007, KRI-ENS-D15-008]
priority: normal
domain: D15
section: 4
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 905
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 4. LNG Value Chain Risk & Failure Modes

## 4.1 LNG Bow-tie

```text
Threats:
geopolitical closure / upstream outage / liquefaction outage / vessel delay / berth conflict /
tank constraint / quality-offspec / counterparty default / cyber / extreme weather
        ↓
Top Event: required gas volume is unavailable at required place/time/spec/cost
        ↓
Consequences:
spot replacement cost / cargo diversion / demurrage / terminal congestion /
power fuel shortage / dispatch loss / contract breach / cash and credit stress
```

## 4.2 LNG Failure Mode Register

| FM ID | Function | Failure Mode | Leading Signal | Consequence | Required Control/Data |
|---|---|---|---|---|---|
| `FM-ENS-D15-001` | upstream | expected production unavailable | field output/ramp variance | cargo entitlement shortfall | operator report·entitlement ledger |
| `FM-ENS-D15-002` | liquefaction | train outage / reduced rate | feedgas·maintenance notice | lifting delay | terminal/operator notice |
| `FM-ENS-D15-003` | route | route unavailable/unsafe | AIS·war-risk·closure | reroute/time/freight | route playbook·insurance |
| `FM-ENS-D15-004` | shipping | vessel ETA miss | ETA variance·port congestion | slot miss/demurrage | AIS·nomination twin |
| `FM-ENS-D15-005` | terminal | berth/slot conflict | schedule density | unload delay | slot optimization |
| `FM-ENS-D15-006` | storage | tank inventory constraint | heel/ullage forecast | cargo rejection/BOG | tank mass-balance twin |
| `FM-ENS-D15-007` | quality | LNG spec mismatch | composition/Wobbe | unload/use restriction | custody quality check |
| `FM-ENS-D15-008` | BOG | boil-off exceeds recovery | BOG rate/compressor | energy loss/pressure | BOG predictive control |
| `FM-ENS-D15-009` | contract | use-or-pay capacity underused | slot/volume mismatch | sunk capacity cost | TUA utilization optimizer |
| `FM-ENS-D15-010` | trading | physical/hedge basis mismatch | exposure by index/tenor | margin volatility | position reconciliation |
| `FM-ENS-D15-011` | counterparty | seller/buyer performance failure | credit/event trigger | replacement/receivable | credit+contract alerts |
| `FM-ENS-D15-012` | data | nomination mismatch | schedule/version delta | imbalance/penalty | versioned nomination workflow |

## 4.3 LNG KRIs

| KRI ID | 지표 | 산식/단위 | 방향 | Trigger 원칙 |
|---|---|---|---|---|
| `KRI-ENS-D15-001` | Route Disruption Exposure | at-risk cargo / next-N cargo | ↑ bad | route closure/warning + exposure |
| `KRI-ENS-D15-002` | ETA Variance | actual/latest ETA - plan | abs ↑ bad | berth tolerance 초과 |
| `KRI-ENS-D15-003` | Terminal Ullage Headroom | forecast ullage | ↓ bad | cargo unloading buffer 이하 |
| `KRI-ENS-D15-004` | Demurrage Risk Hours | expected waiting vs free time | ↑ bad | contract threshold 접근 |
| `KRI-ENS-D15-005` | BOG Loss Ratio | BOG unutilized / received | ↑ bad | asset baseline drift |
| `KRI-ENS-D15-006` | Portfolio Basis Gap | physical index exposure - hedge | abs ↑ bad | risk limit 내부값 |
| `KRI-ENS-D15-007` | Supplier Concentration | volume by source/counterparty | ↑ bad | threshold internal |
| `KRI-ENS-D15-008` | Fuel Cover Days | usable inventory / forecast burn | ↓ bad | plant/season specific |

---
