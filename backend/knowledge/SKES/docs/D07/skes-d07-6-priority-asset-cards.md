---
id: skes-d07-6-priority-asset-cards
title: Priority Asset Cards
summary: Barossa-Darwin LNG 공급망에서 SK이노베이션의 생산·액화·수입권 구성과 Boryeong 터미널 자산의 소유권·사용권 분리 현황을 정의한 자산 카드
tags: [d07, footprint, table, "xref:d06"]
keywords: [Barossa-Darwin LNG, 액화천연가스(LNG), 지분참여, 사용권, Boryeong 터미널, FPSO, LNG 공급망, 재기화(regas)]
related: []
priority: normal
domain: D07
section: 6
source: SK이노베이션E&S_D07_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 3616
updated: 2026-08-06
---

> SK이노베이션 E&S · D07 터미널·발전소·배관 등 자산·용량

# 6. Priority Asset Cards

## 6.1 Barossa–Darwin LNG Integrated Chain

### Public Fact Layer

- Barossa project reached first LNG production in January 2026.
- E&S interest is publicly described as 37.5%; Santos 50%; JERA 12.5%.
- E&S plans to bring approximately 1.3 million tonnes per year for 20 years.
- The first Barossa LNG cargo arrived at Boryeong in February 2026.
- E&S also has a 25% interest in Darwin LNG and Bayu-Undan according to partner disclosure.

### Physical and Commercial Boundary

| Layer | Asset | Right | D07 interpretation |
|---|---|---|---|
| production | Barossa field/FPSO | 37.5% JV interest | equity exposure |
| transport | subsea pipeline to Darwin | JV infrastructure | availability dependency |
| liquefaction | Darwin LNG | 25% interest | brownfield liquefaction exposure |
| shipping | E&S fleet/cargo charter | fleet/contract | cargo delivery interface |
| import | Boryeong TUA | 3.5Mt/y terminal right | Korean receipt capacity |

### Equipment and Data Required

| Area | Minimum asset data | O/I relevance |
|---|---|---|
| well/FPSO | well rate, pressure, water/condensate, downtime | production forecast |
| pipeline | pressure, flow, hydrate risk, pigging | availability |
| liquefaction | feed nomination, train rate, fuel, unplanned outage | cargo reliability |
| cargo | ETA, heel, boil-off, weather, demurrage | voyage optimization |
| terminal | berth, tank level, BOG, sendout | end-to-end scheduling |

### Primary O/I Hypotheses

1. Equity-production forecast and Korean demand forecast can be connected to reduce spot balancing.
2. FPSO/liquefaction outage probabilities can be propagated into cargo and power fuel risk.
3. Condensate and LNG co-product scheduling can share upstream constraints but must use separate commercial models.
4. Cargo ETA uncertainty can be joined with Boryeong tank capacity and power nominations.

### Internal Validation Gate

- Exact LNG entitlement formula and lifting schedule.
- Darwin LNG train capacity allocated to Barossa.
- Operator data access rights and latency.
- Cargo ownership transfer point.
- Field, liquefaction and vessel outage taxonomy.

## 6.2 Boryeong LNG Terminal—Ownership and Usage-Right Separation

### Current Asset State

| Item | Current record |
|---|---|
| Gross terminal capacity | 7Mt/y |
| Storage | 7 LNG tanks × 200,000kl |
| LPG storage | 45kt |
| Regas sendout | 1,400t/h |
| Expansion COD sequence | 2017, 2019, 2021, 2023; sendout expansion 2024 |
| Current equity | GS Energy 50.1%, Gaia Two 35.9%, Youngbo Green Hub 14.0% |
| E&S relationship | equity exited; 3.5Mt/y usage right retained |
| Contract horizon | disclosed rating context through 2047 |

### Data Model Rule

AST-ENS-D07-0014 is the physical terminal. AST-ENS-D07-0015 is the E&S usage-right layer. They share the same site but cannot be summed. A terminal optimization PoC must identify whether data access follows asset ownership, terminal operator service agreement, or TUA nomination rights.

### Equipment Tree

| Level | Equipment | Public count/capacity | Internal gap |
|---|---|---:|---|
| berth | LNG unloading berth | count not normalized | berth window, unloading arm count |
| storage | LNG tank | 7 × 200,000kl | tank type, usable volume, heel |
| BOG | compressor/recondenser | undisclosed | trains, turndown, reliability |
| regas | vaporizer/sendout | 1,400t/h aggregate | unit configuration |
| LPG | LPG tank | 45kt | commercial boundary |
| pipeline | sendout pipeline | undisclosed | pressure, destination, linepack |

### High-Value O/I Questions

1. Can cargo ETA, tank level and sendout forecasts lower BOG venting/recompression energy?
2. Can TUA nomination rights be optimized without accessing restricted operator data?
3. Can tank allocation and vessel berthing reduce demurrage and power fuel imbalance?
4. Can terminal maintenance windows be aligned with Paju/Yeoju/Gwangyang outage schedules?
5. Does post-sale data governance permit model deployment in terminal OT, or only decision support outside OT?

## 6.3 Freeport LNG Contracted Liquefaction Right

| Dimension | Record |
|---|---|
| Asset relationship | contracted tolling/liquefaction usage |
| Public volume | 2.2Mt/y |
| Import start | 2020 described |
| Capacity type | CONTRACTED_RIGHT |
| Not equivalent to | plant ownership, actual annual output, cargo delivered |
| Critical data | feed gas nomination, train availability, cargo window, force majeure, quality |
| O/I focus | cargo reliability forecast, schedule recovery, portfolio balancing |

## 6.4 Core LNG Power Plants

### Gwangyang

| Item | Record |
|---|---|
| Capacity | 1,126MW |
| Configuration | 4 GE F-class gas turbines + 2 steam turbines |
| Commercial operation | 2006 |
| D06 joins | fuel nomination, CCGT startup, combustion, HRSG, steam cycle, maintenance |
| Priority data | unit heat rate, start mode, EOH, emissions, trip history |
| O/I priority | fleet heat-rate diagnostics; start fuel/emission optimization |

### Paju

| Item | Record |
|---|---|
| Capacity | 1,800MW |
| Configuration | 4 Siemens H-class gas turbines + 2 steam turbines |
| Commercial operation | 2017 |
| D06 joins | dispatch, CCGT operation, condition maintenance |
| Priority data | GT/ST/HRSG unit hierarchy, LTSA, outage, ambient derate |
| O/I priority | unit commitment with LNG constraints; outage-risk propagation |

### Yeoju

| Item | Record |
|---|---|
| Capacity | 1,000MW |
| COD | 2023-07-05 |
| Configuration | 2 Siemens GT totaling 670MW, 1 ST 330MW, 2 HRSG |
| D06 joins | latest large CCGT operating baseline |
| Priority data | commissioning baseline, degradation, warranty, startup curves |
| O/I priority | clean-baseline digital twin; early anomaly detection |

### Hanam and Wirye CHP

| Plant | Electric | Heat | Configuration | O/I distinction |
|---|---:|---:|---|---|
| Hanam | 399MW | 263Gcal/h | 1 DHI G GT + 1 ST | electric/heat co-optimization |
| Wirye | 450MW | 238Gcal/h | 1 Siemens H GT + 1 ST | heat demand and thermal storage/network interface |

CHP optimization cannot maximize electric efficiency alone. Heat demand, network temperature, contract priority and weather must be included as hard constraints.

## 6.5 City-Gas Portfolio

### Portfolio Snapshot

- Seven city-gas companies operate eight geographic regions.
- The published snapshot reports 5.4 billion cubic metres supplied in 2023.
- Market share is described as 22.6%.
- Customer scale is approximately 5.1 million households.
- Youngnam Energy Service is split into Gumi and Pohang operating regions; this explains seven companies versus eight regions.

### Minimum Network Asset Tree

| Level | Required internal unit | Key fields |
|---|---|---|
| receipt | city gate | max flow, pressure, odorization, supplier |
| transmission | high-pressure main | diameter, material, age, GIS |
| distribution | medium/low-pressure pipe | segment, coating, leak history |
| regulation | district regulator | inlet/outlet, valve, monitor, inspection |
| customer | meter | type, age, AMI, calibration |
| safety | RBMS/drone/patrol zone | coverage, inspection date, anomaly |
| service | emergency center | dispatch, arrival, closure |

### Asset-Level O/I Readiness

| Region | First PoC | Why |
|---|---|---|
| Ko-one | demand/linepack + high-density leak risk | dense urban network |
| Busan | slope/coastal climate integrity model | geography and corrosion exposure |
| Youngnam Gumi | industrial load forecast | industrial demand |
| Youngnam Pohang | seismic/coastal integrity | hazard profile |
| Chungcheong | wide-area patrol routing | dispersed service area |
| Jeonnam | industrial-city demand segmentation | Gwangyang/Suncheon mix |
| Jeonbuk | meter/UFG diagnostic | manageable regional scope |
| Gangwon | cold-weather demand and response routing | weather sensitivity |

## 6.6 Jeonnam Offshore Wind 1–3

| Phase | Status | Capacity | Turbines | Ownership | Target |
|---|---|---:|---:|---|---|
| Phase 1 | operating since 2025-05 | 96MW | 10 | E&S 51%, CIP 49% | annual approx. 301.07GWh |
| Phase 2 | development | 399MW | TBD | project structure validate | completion target 2031 |
| Phase 3 | development | 399MW | TBD | project structure validate | completion target 2031 |

### Phase 1 Data Stack

| System | Data | O/I use |
|---|---|---|
| turbine SCADA | power, wind, pitch, yaw, temperature, alarms | power curve and anomaly |
| metocean | wind, wave, current, visibility | access and production forecast |
| CMS | vibration, oil/debris | drivetrain maintenance |
| offshore logistics | vessel, crew, weather window | maintenance scheduling |
| grid/PPA | meter, curtailment, imbalance | revenue-loss allocation |

### Development-Phase 2/3 Questions

1. Which phase-1 failure modes and weather-access statistics alter phase-2/3 spares and vessel design?
2. Can actual phase-1 wake and curtailment data improve layout and yield assumptions?
3. Which data-sharing rights survive the JV/OEM/O&M contract boundaries?
4. Is digital twin scope best fixed before EPC and turbine supply agreements?

## 6.7 KCE BESS Portfolio

### Portfolio Layers

| Layer | Scale | Status | Rule |
|---|---:|---|---|
| operating portfolio | 623MW | operating snapshot | do not add selected projects again |
| development pipeline | 8,000MW | development | probability-weight by gate |
| selected NY6 | 20MW/45.6MWh | operating | MW and MWh separate |
| selected Texas group | 200MW | project set | project COD/status validate |
| TX19+TX21 | 100MW combined | project set | individual split internal |

### BESS Asset Hierarchy

| Level | Unit | Critical attributes |
|---|---|---|
| site | interconnection/project | ISO, node, POI, max MW/MWh |
| block | container/PCS block | vendor, rating, warranty |
| pack | rack/module/pack | temperature, voltage, resistance |
| controls | BMS/EMS/PPC | setpoint, SOC, constraints |
| market | MarketCapture/bid stack | forecast, bid, award, dispatch |
| safety | fire detection/suppression | event, isolation, response |

### O/I Boundary

Market bidding optimization should not be separated from degradation and warranty constraints. Revenue models require dispatch, price and award data; asset-health models require cell-to-block telemetry. A joint model must prevent a revenue optimizer from creating hidden lifetime cost.

## 6.8 EverCharge Distributed Charging Footprint

| Case | Installed | Planned/ready | Interpretation |
|---|---:|---:|---|
| Oracle Park phase 1 | 50 chargers | 150 total plan | plan includes future rollout |
| Sharon Park | 64 chargers | 100% EV-ready description | expanded from 6 |
| Legacy | 80 chargers | 67 ready circuits | ready circuits are not chargers |

### Required Site Schema

| Field group | Fields |
|---|---|
| electrical | service limit, transformer, panel, circuit |
| charger | model, port, rated kW, firmware, connectivity |
| session | start/end, kWh, peak, interruption, user |
| building | non-EV load, demand charge, occupancy |
| SmartPower | allocation setpoint, queue, fairness, override |
| maintenance | fault, remote reset, truck roll, MTTR |

## 6.9 Incheon Liquid Hydrogen Plant

| Item | Public record |
|---|---|
| Site | inside SK Incheon Petrochemical complex |
| Area | approx. 50,000m2 |
| Annual nominal capacity | 30,000t/y |
| Liquefaction trains | 3 × 30t/day |
| Storage | 6 × 20t |
| Completion | 2024-05-08 |
| Operating affiliate | IGE |

### Reconciliation Note

Three trains at 30t/day imply 90t/day instantaneous nameplate. Multiplying by 365 gives 32,850t/y, while the official annual headline is approximately 30,000t/y. D07 does not “correct” either figure. The difference may reflect planned availability, rounding or operating days and requires internal confirmation.

### Priority Equipment/Data

| Stage | Equipment | Data |
|---|---|---|
| intake | by-product H2 interface | flow, purity, pressure |
| purification | purifier | impurity, regeneration |
| liquefaction | three trains | load, temperature, pressure, SEC |
| storage | six tanks | level, pressure, boil-off |
| loading | pumps/loading arm | batch, turnaround, loss |
| distribution | tankers/stations | ETA, inventory, demand |

## 6.10 Quynh Lap LNG-to-Power Development

| Dimension | Public record |
|---|---|
| Country | Vietnam |
| Development role | consortium selected as final developer |
| Planned power | 1,500MW |
| Planned terminal | 250,000m3 scale |
| Dedicated infrastructure | port |
| Investment context | approx. USD 2.3bn |
| Schedule | construction target 2027; completion/COD target 2030 |
| Current state | DEVELOPMENT, not operating |

### Front-End Digital Design Opportunities

1. Establish a canonical asset hierarchy before EPC data is fragmented.
2. Require tag, alarm, historian and document handover standards in contracts.
3. Model terminal–power–grid constraints before final equipment sizing.
4. Define multilingual work-order and operator knowledge structures.
5. Include cyber zones, remote support and model deployment in control-system specifications.

---
