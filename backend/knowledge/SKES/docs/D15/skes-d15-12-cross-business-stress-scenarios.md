---
id: skes-d15-12-cross-business-stress-scenarios
title: Cross-business Stress Scenarios
summary: "LNG·발전·수소·CCS 등 에너지사업 주요 영역의 외부충격을 시나리오로 등록하고 전파경로, 핵심성과지표, 대응도구를 매핑한 리스크 레지스터."
tags: [d15, risk, table, "xref:d17"]
keywords: [LNG, 발전, BESS, 수소, CCS, 파급효과, KRI, 외부충격, 공급망, 에너지비용]
related: [SCN-ENS-D15-001, SCN-ENS-D15-002, SCN-ENS-D15-003, SCN-ENS-D15-004, SCN-ENS-D15-005, SCN-ENS-D15-006, SCN-ENS-D15-007, SCN-ENS-D15-008, SCN-ENS-D15-009, SCN-ENS-D15-010, SCN-ENS-D15-011, SCN-ENS-D15-012, SCN-ENS-D15-013, SCN-ENS-D15-014, SCN-ENS-D15-015, SCN-ENS-D15-016, SCN-ENS-D15-017, SCN-ENS-D15-018, SCN-ENS-D15-019, SCN-ENS-D15-020, SCN-ENS-D15-021, SCN-ENS-D15-022, SCN-ENS-D15-023, SCN-ENS-D15-024]
priority: normal
domain: D15
section: 12
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 1173
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 12. Cross-business Stress Scenarios

## 12.1 Scenario Register

| Scenario ID | Shock | Propagation | Core KRI | D17 relevance |
|---|---|---|---|---|
| `SCN-ENS-D15-001` | Gulf LNG route disruption | cargo→replacement→terminal→power→cash | route exposure·fuel cover·basis | LNG resilience twin |
| `SCN-ENS-D15-002` | Freeport/liquefaction availability loss | US supply→cargo schedule→alternative sourcing | lifting delay·TUA usage | cargo reoptimizer |
| `SCN-ENS-D15-003` | Barossa ramp below plan | upstream→entitlement→portfolio supply | ramp variance | operator/JV early warning |
| `SCN-ENS-D15-004` | simultaneous LNG spike + low SMP | fuel cost↑ + revenue compression | clean spark spread | cross-commodity margin guard |
| `SCN-ENS-D15-005` | cold snap + plant forced outage | demand↑ + supply capacity↓ | reserve/fuel/trip | reliability/maintenance planner |
| `SCN-ENS-D15-006` | warm winter | city gas volume↓ | HDD-normalized demand | demand hedge/segment forecast |
| `SCN-ENS-D15-007` | offshore wind cable fault | generation↓ + marine access delay | fault·weather window | cable health + vessel planner |
| `SCN-ENS-D15-008` | PPA curtailment cluster | MWh shortfall→shape imbalance | curtailment·shape gap | portfolio matcher |
| `SCN-ENS-D15-009` | ERCOT BESS saturation | spread/ancillary revenue↓ | operating MW·spread | revenue diversification |
| `SCN-ENS-D15-010` | BESS thermal event | site shutdown→market/SLA/insurance | alarm·barrier | safety digital thread |
| `SCN-ENS-D15-011` | NY/Tx market rule change | optimizer stale→bid/credit error | rule deployment lag | rule-change agent |
| `SCN-ENS-D15-012` | EverCharge cloud/payment outage | sessions fail→SLA/churn | uptime·failed sessions | edge fallback |
| `SCN-ENS-D15-013` | LH2 plant train outage | production↓→station stockout→fleet impact | train availability·inventory | H2 network twin |
| `SCN-ENS-D15-014` | H2 demand ramp delayed 12m | paid kg↓→unit cost↑→PF/cash | sold kg·active vehicles | offtake confidence engine |
| `SCN-ENS-D15-015` | LH2 safety barrier impairment | operation restriction→production loss | overdue proof test | barrier health monitor |
| `SCN-ENS-D15-016` | CCS emitter FID delay | capture volume↓→storage utilization↓ | firm tCO2 | FID probability engine |
| `SCN-ENS-D15-017` | CCS injectivity underperformance | storage capacity↓→contract/liability | injectivity confidence | subsurface uncertainty twin |
| `SCN-ENS-D15-018` | Quynh Lap critical-path slip | permit/grid/PPA/finance→2031 cliff | schedule slack | Monte Carlo critical path |
| `SCN-ENS-D15-019` | K-ETS carbon cost escalation | power cost→dispatch/margin | allowance position | allocation-position twin |
| `SCN-ENS-D15-020` | 48E/PFE evidence failure | supplier→tax credit→PF cash | evidence completeness | PFE supplier graph |
| `SCN-ENS-D15-021` | OT ransomware | control visibility↓→safe shutdown→recovery | segmentation/backup | OT recovery orchestration |
| `SCN-ENS-D15-022` | extreme weather multi-asset | power+BESS+wind+citygas | weather exposure | portfolio resilience twin |
| `SCN-ENS-D15-023` | key vendor insolvency | spare/EPC/LTSA→downtime/COD | concentration/lead time | supplier early warning |
| `SCN-ENS-D15-024` | JV deadlock + capital call | schedule+liquidity | decision aging·cash call | governance obligation graph |

## 12.2 Scenario Quantification Boundary

각 시나리오는 최소 `Base / Moderate / Severe / Reverse Stress` 4개로 관리한다. 그러나 공개자료만으로 손실액을 만들지 않는다.

```text
Required internal inputs:
exposure quantity
contract/index formula
hedge/insurance
asset availability
duration
recovery curve
customer/market obligation
tax/accounting treatment

Output:
Volume-at-Risk
Margin-at-Risk
Cash-at-Risk
Downtime-at-Risk
Compliance-at-Risk
Safety consequence band
```

`Reverse Stress`는 “어떤 충격이 회사 전체를 망가뜨리는가” 같은 추상 질문이 아니라, `minimum liquidity`, `minimum service`, `permit/COD deadline`, `safety barrier`, `PF covenant` 등 실제 임계점을 처음 깨는 조건을 찾는 방식으로 정의한다.

---
