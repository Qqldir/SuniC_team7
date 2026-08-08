---
id: skes-d08-d06-d08-d06-d08-process-asset-right-crosswalk
title: D06–D08 Process·Asset·Right Crosswalk
summary: "LNG 및 전력·도시가스 공급 기록이 어떤 프로세스, 자산, 권리와 연결되고 어떤 리스크를 가지는지 보여주는 매핑표."
tags: [d08, supply-chain, table, "xref:d06", "xref:d07", "xref:d11", "xref:d17"]
keywords: [LNG, 공급 기록, Barossa, 공급자, 리스크, 터미널, TUA, 연료 공급, Darwin, ID 대응]
related: [PROC-ENS-D06-LNG-002, RGT-ENS-D07-0001, SUP-ENS-D08-0008, CTR-ENS-D08-0004, AST-ENS-D07-0003, AST-ENS-D07-0004, RGT-ENS-D07-0002, PROC-ENS-D06-CCS-001, RGT-ENS-D07-0003, AST-ENS-D07-0006, SUP-ENS-D08-0010, CTR-ENS-D08-0002, AST-ENS-D07-0007, RGT-ENS-D07-0004, SUP-ENS-D08-0011, CTR-ENS-D08-0003, AST-ENS-D07-0008, RGT-ENS-D07-0005, SUP-ENS-D08-0012, CTR-ENS-D08-0001, AST-ENS-D07-0009, PROC-ENS-D06-LNG-007, AST-ENS-D07-0010, AST-ENS-D07-0011]
priority: normal
domain: D08
section: D06-D08
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 2967
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 21. D06–D08 Process·Asset·Right Crosswalk

## 21.1 LNG Crosswalk

| Supply Record | D06 Process ID | D07 Asset ID | D07 Right ID | Critical Supplier/Contract | Primary Risk |
|---|---|---|---|---|---|
| Barossa production | `PROC-ENS-D06-LNG-002` | `AST-ENS-D07-0001/0002` | `RGT-ENS-D07-0001` | `SUP-ENS-D08-0008`, `CTR-ENS-D08-0004` | upstream shortfall |
| Barossa GEP | `PROC-ENS-D06-LNG-002/003` | `AST-ENS-D07-0003` | `RGT-ENS-D07-0001` | Barossa JV/operator | pipeline availability |
| Darwin liquefaction | `PROC-ENS-D06-LNG-003/004/005` | `AST-ENS-D07-0004` | `RGT-ENS-D07-0002` | `CTR-ENS-D08-0005/0006` | brownfield outage |
| Bayu-Undan transition | `PROC-ENS-D06-CCS-001` | `AST-ENS-D07-0005/0078` | `RGT-ENS-D07-0003` | JV/storage counterparties | planned-right uncertainty |
| Woodford production | `PROC-ENS-D06-LNG-002` | `AST-ENS-D07-0006` | internal right | `SUP-ENS-D08-0010`, `CTR-ENS-D08-0002` | production/basis risk |
| Freeport tolling | `PROC-ENS-D06-LNG-003/004/005` | `AST-ENS-D07-0007` | `RGT-ENS-D07-0004` | `SUP-ENS-D08-0011`, `CTR-ENS-D08-0003` | outage/use-or-pay |
| Tangguh entitlement | `PROC-ENS-D06-LNG-001/005/006` | `AST-ENS-D07-0008` | `RGT-ENS-D07-0005` | `SUP-ENS-D08-0012`, `CTR-ENS-D08-0001` | delivery/quality |
| fleet aggregate | `PROC-ENS-D06-LNG-006/007` | `AST-ENS-D07-0009` | charter rights internal | `CTR-ENS-D08-0007/0008` | capacity/drydock |
| Prism Agility | `PROC-ENS-D06-LNG-007` | `AST-ENS-D07-0010` | charter internal | `SUP-ENS-D08-0015/0016/0017` | ETA/BOR/fuel |
| Prism Brilliance | `PROC-ENS-D06-LNG-007` | `AST-ENS-D07-0011` | charter internal | `SUP-ENS-D08-0015/0016/0017` | ETA/BOR/fuel |
| carrier ID gaps | `PROC-ENS-D06-LNG-007` | `AST-ENS-D07-0012/0013` | charter internal | identity required | master-data gap |
| Boryeong physical terminal | `PROC-ENS-D06-LNG-008/009/010/011` | `AST-ENS-D07-0014` | `RGT-ENS-D07-0006` inactive equity | terminal owner/operator | data access after sale |
| Boryeong E&S TUA | `PROC-ENS-D06-LNG-008/009/010/011` | `AST-ENS-D07-0015` | `RGT-ENS-D07-0007` | `SUP-ENS-D08-0013`, `CTR-ENS-D08-0009` | service/data-right |
| Ganyu usage plan | `PROC-ENS-D06-LNG-008/009/010/011` | `AST-ENS-D07-0017` | planned | `SUP-ENS-D08-0014`, `CTR-ENS-D08-0010` | project delay |
| Quynh Lap terminal/port | future LNG-008~011 | `AST-ENS-D07-0018/0019` | `RGT-ENS-D07-0012` | consortium/EPC future | development/interface |

## 21.2 Power, CHP and City-Gas Crosswalk

| Supply Record | D06 Process ID | D07 Asset ID | Supplier Layer | Required Internal Join |
|---|---|---|---|---|
| Gwangyang fuel/MRO | `PROC-ENS-D06-PWR-001/002/003/004/005/006/007/008` | `AST-ENS-D07-0020` | LNG route + GE interface | fuel contract·LTSA·BOM |
| Paju fuel/MRO | `PROC-ENS-D06-PWR-001/002/003/004/005/006/007/008` | `AST-ENS-D07-0021` | Freeport/Boryeong + Siemens | fuel allocation·LTSA·spares |
| Yeoju fuel/MRO | `PROC-ENS-D06-PWR-001/002/003/004/005/006/007/008` | `AST-ENS-D07-0022` | LNG route + Siemens | commissioning baseline·warranty |
| Hanam CHP | `PROC-ENS-D06-PWR-001/002/003/004/005/006/007/008`, `PROC-ENS-D06-CHP-001/002` | `AST-ENS-D07-0023` | gas + Doosan interface | heat demand·LTSA·chemicals |
| Wirye CHP | `PROC-ENS-D06-PWR-001/002/003/004/005/006/007/008`, `PROC-ENS-D06-CHP-001/002` | `AST-ENS-D07-0024` | gas + Siemens | heat demand·LTSA·chemicals |
| O&M-managed CHP | `PROC-ENS-D06-PWR-008`, `CHP-001/002` | `AST-ENS-D07-0025/0026` | owner/O&M/vendor split | data/stock ownership |
| Ko-one materials/gas | `PROC-ENS-D06-CG-001/002/003/004/005/006/007/008/009/010` | `AST-ENS-D07-0029` | `SUP-ENS-D08-0034/0035` | city-gate·PO·GIS·stock |
| Busan materials/gas | `PROC-ENS-D06-CG-001/002/003/004/005/006/007/008/009/010` | `AST-ENS-D07-0030` | same vendor pool | coastal/corrosion risk |
| Youngnam Gumi | `PROC-ENS-D06-CG-001/002/003/004/005/006/007/008/009/010` | `AST-ENS-D07-0031` | same vendor pool | industrial demand·stock |
| Youngnam Pohang | `PROC-ENS-D06-CG-001/002/003/004/005/006/007/008/009/010` | `AST-ENS-D07-0032` | same vendor pool | seismic/coastal risk |
| Chungcheong | `PROC-ENS-D06-CG-001/002/003/004/005/006/007/008/009/010` | `AST-ENS-D07-0033` | same vendor pool | wide-area logistics |
| Jeonnam | `PROC-ENS-D06-CG-001/002/003/004/005/006/007/008/009/010` | `AST-ENS-D07-0034` | same vendor pool | industrial-city mix |
| Jeonbuk | `PROC-ENS-D06-CG-001/002/003/004/005/006/007/008/009/010` | `AST-ENS-D07-0035` | same vendor pool | meter/UFG genealogy |
| Gangwon | `PROC-ENS-D06-CG-001/002/003/004/005/006/007/008/009/010` | `AST-ENS-D07-0036` | same vendor pool | cold-weather stock |

## 21.3 Renewable, ESS, EV, Hydrogen and CCS Crosswalk

| Supply Record | D06 Process ID | D07 Asset ID/Right | Public Supplier/Partner | O/I Gate |
|---|---|---|---|---|
| Jeonnam OWF1 | `PROC-ENS-D06-REN-001/003/004/005` | `AST-ENS-D07-0038`, `RGT-ENS-D07-0008` | `SUP-ENS-D08-0021`; package vendors internal | OEM/JV data-right |
| Jeonnam OWF2/3 | future REN-001~005 | `AST-ENS-D07-0039/0040` | project/EPC future | digital requirement before contract |
| solar portfolio | `PROC-ENS-D06-REN-001/002/004/005` | `AST-ENS-D07-0041~0051` | module/inverter/EPC internal | serial/as-built completeness |
| renewable aggregates | planning only | `AST-ENS-D07-0052/0053` | mixed | project de-duplication |
| KCE operating portfolio | `PROC-ENS-D06-ESS-001/002/003` | `AST-ENS-D07-0054`, `RGT-ENS-D07-0009` | mixed project suppliers | project inclusion map |
| KCE NY6 | `PROC-ENS-D06-ESS-001/002/003` | `AST-ENS-D07-0057` | Sungrow·Black & McDonald·National Grid | warranty/data access |
| KCE TX11/12/23 | `PROC-ENS-D06-ESS-001/002/003` | `AST-ENS-D07-0061/0062/0063` | Powin·Mitsubishi Power | current contract state |
| EverCharge factory | supply/EVC-001/002 | `AST-ENS-D07-0070`, `RGT-ENS-D07-0010` | `SUP-ENS-D08-0029` | BOM/AVL/SBOM |
| EverCharge sites | `PROC-ENS-D06-EVC-001/002` | `AST-ENS-D07-0066~0069` | installer/component vendors internal | site genealogy |
| Incheon LH₂ plant | `PROC-ENS-D06-H2-001/002/003` | `AST-ENS-D07-0071`, `RGT-ENS-D07-0011` | feed/OEM/logistics internal | safety/data-right |
| LH₂ trains/storage | `PROC-ENS-D06-H2-001/002` | `AST-ENS-D07-0072~0075` | `SUP-ENS-D08-0036` + OEM internal | train/tank serial |
| LH₂ delivery network | `PROC-ENS-D06-H2-003` | `AST-ENS-D07-0076` | `SUP-ENS-D08-0037` | route/station actuals |
| blue-H₂ concept | future H2/CCS | `AST-ENS-D07-0077` | Plug/other partners; status planned | no operating claim |
| Bayu-Undan CCS | `PROC-ENS-D06-CCS-001` | `AST-ENS-D07-0078`, `RGT-ENS-D07-0003` | Santos/JV/Honeywell/KIER/CE TECH by scope | right/MRV/interface |

## 21.4 Disruption-Propagation Paths

### Path A — Freeport Outage

```text
Freeport Train 3 outage
→ contracted tolling utilization loss
→ planned cargo cancellation/delay
→ dedicated vessel idle/reassignment
→ Boryeong inventory-cover decline
→ Paju/Yeoju/CHP fuel constraint
→ spot procurement or dispatch change
→ power margin and customer-supply impact
```

Required control: outage notice ingestion, cargo rescheduler, terminal inventory forecast, generation fuel constraint and D11 landed-cost scenario must share one event ID.

### Path B — Barossa Ramp-Up Shortfall

```text
well/FPSO shortfall
→ GEP/Darwin feed reduction
→ E&S lifting entitlement variance
→ cargo schedule and LNG quality change
→ Boryeong arrival/tank allocation change
→ Korean portfolio balancing need
```

Required control: JV/operator data latency and contract entitlement reconciliation must be modeled before automated recommendations.

### Path C — BESS Cell Defect

```text
cell-lot defect/recall
→ affected module/rack/container identification
→ KCE project availability restriction
→ MarketCapture dispatch constraint
→ warranty/OEM service/spares demand
→ market revenue and safety impact
```

Required control: cell-to-project genealogy, firmware state, warranty clause and work-order closure must be connected.

### Path D — City-Gas Pipe Lot Defect

```text
supplier lot NCR
→ warehouse/issued quantity reconciliation
→ fusion/weld/GIS segment identification
→ risk-based inspection or replacement
→ regional emergency stock transfer
→ customer notice and safety response
```

Required control: lot genealogy completeness must be quantified before risk ranking.

### Path E — LH₂ Feed Interruption

```text
byproduct-H₂ feed reduction
→ train production decline
→ storage drawdown
→ trailer allocation change
→ station stockout risk
→ bus/fleet fueling disruption
```

Required control: feed, production, storage, loaded, delivered and dispensed quantities must use consistent mass-balance periods.

## 21.5 Verification Queue

| Queue ID | 확인사항 | Owner Candidate | D08 Impact | Priority |
|---|---|---|---|---|
| `VQ-ENS-D08-001` | Tangguh 현재 SPA 법인·기간·ADP | LNG procurement/legal | contract master | P0 |
| `VQ-ENS-D08-002` | Woodford 실제 E&S entitlement와 feed-gas disposition | upstream/trading | volume balance | P0 |
| `VQ-ENS-D08-003` | Freeport Train allocation·contract expiry·make-up | LNG/legal | optimizer constraint | P0 |
| `VQ-ENS-D08-004` | Barossa 1.3Mt/y 권리 성격·20년 start date | JV/legal | double-count control | P0 |
| `VQ-ENS-D08-005` | Darwin LNG 25% 권리와 Barossa tolling 연결 | JV/legal | flow model | P0 |
| `VQ-ENS-D08-006` | LNG carrier 3·4 실명·IMO·charter | shipping | fleet scheduler | P0 |
| `VQ-ENS-D08-007` | Boryeong TUA service level·data right·2047 term | terminal/legal | terminal PoC | P0 |
| `VQ-ENS-D08-008` | Ganyu 2027 최신 construction/usage status | China business | lifecycle | P1 |
| `VQ-ENS-D08-009` | 발전소별 fuel allocation·OEM·LTSA | power procurement | spare/fuel models | P0 |
| `VQ-ENS-D08-010` | 7개 도시가스사 공통 material code | city gas procurement | inventory PoC | P0 |
| `VQ-ENS-D08-011` | pipe lot–GIS genealogy coverage | city gas safety | safety PoC | P0 |
| `VQ-ENS-D08-012` | Jeonnam OWF1 OEM/EPC/package map | renewable | warranty/schedule | P0 |
| `VQ-ENS-D08-013` | KCE project별 cell/BESS/EPC/LTSA current state | KCE | recall/warranty | P0 |
| `VQ-ENS-D08-014` | EverCharge tier-2 BOM/AVL/SBOM | EverCharge | EOL/cyber | P1 |
| `VQ-ENS-D08-015` | Incheon LH₂ feed supplier·contract·OEM | hydrogen | optimizer/spares | P0 |
| `VQ-ENS-D08-016` | supplier ESG 최신 연도 pool·실사·CAP | procurement ESG | score refresh | P1 |
| `VQ-ENS-D08-017` | AI/telemetry rights in active strategic contracts | legal/IT | D17 Gate | P0 |
| `VQ-ENS-D08-018` | supplier master canonical ownership after merger | procurement data | all domains | P0-foundation |

---
