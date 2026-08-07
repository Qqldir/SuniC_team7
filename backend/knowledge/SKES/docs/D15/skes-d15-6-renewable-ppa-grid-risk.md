---
id: skes-d15-6-renewable-ppa-grid-risk
title: "Renewable, PPA & Grid Risk"
summary: 재생에너지 PPA 사업의 발전·그리드·신용 분야 실패모드 카탈로그 및 핵심리스크지표(KRI) 정의표.
tags: [d15, risk, table]
keywords: [신재생에너지, 풍력, 태양광, 해상풍력, Power Purchase Agreement, 실패모드, KRI, 커튼먼트, 전력구매자신용]
related: [FM-ENS-D15-029, FM-ENS-D15-030, FM-ENS-D15-031, FM-ENS-D15-032, FM-ENS-D15-033, FM-ENS-D15-034, FM-ENS-D15-035, FM-ENS-D15-036, FM-ENS-D15-037, FM-ENS-D15-038, KRI-ENS-D15-019, KRI-ENS-D15-020, KRI-ENS-D15-021, KRI-ENS-D15-022, KRI-ENS-D15-023, KRI-ENS-D15-024, KRI-ENS-D15-025, KRI-ENS-D15-026]
priority: normal
domain: D15
section: 6
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 537
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 6. Renewable, PPA & Grid Risk

## 6.1 Failure Modes

| FM ID | Failure Mode | Exposure | Loss Path | O/I Hook |
|---|---|---|---|---|
| `FM-ENS-D15-029` | wind/solar resource underperformance | renewable asset | MWh shortfall | weather/yield ensemble |
| `FM-ENS-D15-030` | turbine/inverter outage | operating asset | availability/revenue | condition monitoring |
| `FM-ENS-D15-031` | offshore access delayed | Jeonnam OW | MTTR↑ | marine weather route planner |
| `FM-ENS-D15-032` | subsea/export cable fault | offshore wind | long outage | cable risk analytics |
| `FM-ENS-D15-033` | grid congestion/curtailment | renewable | lost MWh/PPA gap | congestion forecast |
| `FM-ENS-D15-034` | PPA generation-load shape mismatch | customer portfolio | imbalance cost | portfolio matcher |
| `FM-ENS-D15-035` | meter/REC attribution error | PPA/RE100 | claim/billing risk | attribute ledger |
| `FM-ENS-D15-036` | offtaker credit deterioration | long PPA | AR/cash/default | credit early warning |
| `FM-ENS-D15-037` | grid connection delay | pipeline project | COD/PF delay | permit-grid critical path |
| `FM-ENS-D15-038` | offshore permit milestone slip | Jeonnam 2/3 | FID/COD delay | permit dependency AI |

## 6.2 KRIs

| KRI ID | 지표 | 최소 정의 |
|---|---|---|
| `KRI-ENS-D15-019` | Availability | available hours / scheduled hours |
| `KRI-ENS-D15-020` | Curtailment Rate | curtailed MWh / available MWh |
| `KRI-ENS-D15-021` | Yield Gap | weather-adjusted actual - expected |
| `KRI-ENS-D15-022` | PPA Shape Gap | hourly generation - contracted/load profile |
| `KRI-ENS-D15-023` | Attribute Exception Rate | REC/GO/measurement unmatched records |
| `KRI-ENS-D15-024` | Permit Critical-path Slack | milestone deadline - forecast completion |
| `KRI-ENS-D15-025` | Grid Queue Aging | stage duration vs benchmark |
| `KRI-ENS-D15-026` | Offtaker Credit Watch | rating/AR/covenant composite; 내부 threshold |

---
