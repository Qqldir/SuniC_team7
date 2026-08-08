---
id: skes-d10-19-internal-data-request-queue
title: Internal Data Request Queue
summary: "SK이노베이션 E&S의 주요 사업 데이터(LNG, 발전, 신재생, 수소, CCS)를 누가 소유하고 어느 정도의 기밀도로 관리하는가를 보여주는 데이터 카탈로그 테이블이다."
tags: [d10, market, table]
keywords: [데이터 카탈로그, 요청 ID, 민감도, LNG, 신재생에너지, 수소, CCS, BESS, 충전소, 데이터 소유자]
related: [REQ-ENS-D10-001, REQ-ENS-D10-002, REQ-ENS-D10-003, REQ-ENS-D10-004, REQ-ENS-D10-005, REQ-ENS-D10-006, REQ-ENS-D10-007, REQ-ENS-D10-008, REQ-ENS-D10-009, REQ-ENS-D10-010, REQ-ENS-D10-011, REQ-ENS-D10-012, REQ-ENS-D10-013, REQ-ENS-D10-014, REQ-ENS-D10-015, REQ-ENS-D10-016, REQ-ENS-D10-017, REQ-ENS-D10-018, REQ-ENS-D10-019, REQ-ENS-D10-020, REQ-ENS-D10-021, REQ-ENS-D10-022, REQ-ENS-D10-023, REQ-ENS-D10-024]
priority: normal
domain: D10
section: 19
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 1025
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# 19. Internal Data Request Queue

| Req ID | Dataset | Minimum fields | History | Owner | Sensitivity |
|---|---|---|---|---|---|
| `REQ-ENS-D10-001` | LNG contract exposure | volume·index·flex·term | contract life | trading/legal | confidential |
| `REQ-ENS-D10-002` | cargo ledger | origin·ETA·volume·cost | 36m | LNG ops | confidential |
| `REQ-ENS-D10-003` | vessel/terminal events | ETA·slot·tank·BOG | 24m | terminal | restricted |
| `REQ-ENS-D10-004` | generation bids | unit·price·award·dispatch | 24m | power | market-confidential |
| `REQ-ENS-D10-005` | plant economics | fuel·heat rate·start·O&M | 24m | finance/ops | confidential |
| `REQ-ENS-D10-006` | CHP heat demand | customer·hour·Gcal | 24m | CHP | confidential |
| `REQ-ENS-D10-007` | city-gas usage | masked customer·month·use | 36m | city gas | personal/restricted |
| `REQ-ENS-D10-008` | electrification features | building·equipment·event | current | city gas | personal |
| `REQ-ENS-D10-009` | renewable pipeline | stage·permit·grid·COD | history+plan | development | confidential |
| `REQ-ENS-D10-010` | renewable generation | site·interval·curtailment | 24m | O&M | internal |
| `REQ-ENS-D10-011` | PPA load | customer/site/15m | 24m | commercial | sensitive |
| `REQ-ENS-D10-012` | PPA commercial terms | price·term·imbalance | contract | legal | confidential |
| `REQ-ENS-D10-013` | KCE bids | asset·bid·award·price | 24m | market ops | market-confidential |
| `REQ-ENS-D10-014` | KCE telemetry | power·SOC·SOH·availability | 24m | asset ops | restricted |
| `REQ-ENS-D10-015` | KCE revenue | service·settlement·fees | 24m | finance | confidential |
| `REQ-ENS-D10-016` | BESS degradation | EFC·temp·SOH·warranty | life | engineering | restricted |
| `REQ-ENS-D10-017` | charging sites | panel·ports·parking·tariff | current | sales/ops | confidential |
| `REQ-ENS-D10-018` | charging sessions | port·kWh·time·error | 24m | platform | personal |
| `REQ-ENS-D10-019` | charging contracts | hardware·SaaS·SLA·term | life | commercial | confidential |
| `REQ-ENS-D10-020` | H2 production | feed·output·energy·loss | 24m | H2 ops | restricted |
| `REQ-ENS-D10-021` | H2 station | inventory·dispense·downtime | 24m | station ops | restricted |
| `REQ-ENS-D10-022` | H2 demand stages | MOU·order·delivery·contract | history+plan | BD | confidential |
| `REQ-ENS-D10-023` | H2 logistics | trailer·load·ETA·loss | 24m | logistics | internal |
| `REQ-ENS-D10-024` | CCS emitter leads | location·volume·quality·stage | current | CCS BD | confidential |
| `REQ-ENS-D10-025` | CCS storage | permit·capacity·injectivity | model versions | CCS/JV | restricted |
| `REQ-ENS-D10-026` | MRV evidence | meter·sample·model·audit | project life | ESG/ops | restricted |
| `REQ-ENS-D10-027` | competitor quotes | scope·price·term·win/loss | 24m | sales | confidential |
| `REQ-ENS-D10-028` | market forecasts | provider·version·scope·value | 5y | strategy | licensed |
| `REQ-ENS-D10-029` | decision log | signal·option·approval·result | 24m | PMO | internal |
| `REQ-ENS-D10-030` | PoC baseline | KPI·control·cost·owner | 12m | O/I PMO | internal |

## 19.1 Safe Sandbox Rules

- 시장입찰·계약가격·고객부하·개인정보를 외부 vendor에 원본 제공하지 않는다.
- licensed market data는 계약상 파생데이터·모델학습 권리를 확인한다.
- competitor 자료는 공개·허가된 범위만 사용한다.
- LNG hedge·BESS bid·PPA quote·고객 offer는 shadow mode 후 human approval을 거친다.
- PoC 종료 시 데이터 삭제·모델 보존·파생데이터 소유권을 기록한다.

---
