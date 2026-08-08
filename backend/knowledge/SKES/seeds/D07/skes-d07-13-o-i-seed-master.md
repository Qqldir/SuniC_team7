---
id: skes-d07-13-o-i-seed-master
title: O/I Seed Master
summary: "SK이노베이션의 LNG·발전소·도시가스 자산별 AI 개선 프로젝트 21개의 목표 KPI, 필요 데이터, 의존성, 우선순위를 담은 프로젝트 마스터"
tags: [d07, footprint, oi-seed, table, "xref:d06"]
keywords: [LNG 운송, 발전소 효율, 도시가스 공급, 재생에너지, BOG 최적화, 설비 진단, 수요 예측, 에너지 자산]
related: []
priority: normal
domain: D07
section: 13
source: SK이노베이션E&S_D07_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 2008
updated: 2026-08-06
---

> SK이노베이션 E&S · D07 터미널·발전소·배관 등 자산·용량

# 13. O/I Seed Master

| Seed ID | Asset | Use Case | D06 Join | Primary KPI | Minimum Data | Gate | Priority |
|---|---|---|---|---|---|---|---|
| SEED-ENS-D07-0001 | Barossa/Darwin | upstream-to-cargo availability forecast | D06 LNG upstream | delivery variance | production/train/cargo | JV data right | P0 |
| SEED-ENS-D07-0002 | LNG fleet | voyage ETA and BOG optimizer | D06 shipping | demurrage/BOR | AIS/weather/tank | vessel data | P0 |
| SEED-ENS-D07-0003 | Boryeong | tank inventory forecast | D06-011 | inventory error | tank/cargo/sendout | TUA access | P0 |
| SEED-ENS-D07-0004 | Boryeong | BOG compressor optimization | D06-013 | BOG energy/vent | pressure/load/event | operator approval | P0 |
| SEED-ENS-D07-0005 | LNG-power | integrated cargo-terminal-generation plan | D06-016 | balancing cost | cargo/tank/dispatch | cross-entity | P0 |
| SEED-ENS-D07-0006 | LNG portfolio | capacity/right semantic ledger | D06 common | reconciliation errors | asset/contract/event | master owner | P0 |
| SEED-ENS-D07-0007 | Gwangyang/Paju/Yeoju | fleet heat-rate diagnostics | D06-019 | heat rate | historian/ambient/fuel | OEM boundary | P0 |
| SEED-ENS-D07-0008 | power fleet | startup cost/emission recommender | D06 power | start fuel/time | event/fuel/emission | operator trust | P1 |
| SEED-ENS-D07-0009 | power fleet | outage-risk to LNG propagation | D06-026 | imbalance/EFOR | EAM/cargo/dispatch | causal validation | P0 |
| SEED-ENS-D07-0010 | Yeoju | commissioning baseline digital twin | D06 CCGT | degradation | acceptance/historian | warranty | P1 |
| SEED-ENS-D07-0011 | Paju | unit commitment under fuel constraints | D06 dispatch | margin | unit/cargo/price | dispatch approval | P0 |
| SEED-ENS-D07-0012 | Hanam/Wirye | power-heat co-optimizer | D06 CHP | total margin | heat/weather/price | heat SLA | P0 |
| SEED-ENS-D07-0013 | city gas | canonical GIS-EAM-SCADA asset graph | D06-034 | coverage | GIS/EAM/tag | data quality | P0 |
| SEED-ENS-D07-0014 | city gas | leak-risk segment ranking | D06-037 | high-risk hit rate | pipe/history/soil | safety validation | P0 |
| SEED-ENS-D07-0015 | city gas | regulator anomaly detection | D06 city gas | incident/MTBF | pressure/valve/work | false alarm | P1 |
| SEED-ENS-D07-0016 | city gas | UFG root-cause analytics | D06-041 | UFG | receipt/meter/billing | meter lineage | P0 |
| SEED-ENS-D07-0017 | city gas | emergency crew routing | D06 emergency | response time | alarm/crew/traffic | safety rule | P1 |
| SEED-ENS-D07-0018 | city gas | weather-demand forecast by region | D06 demand | MAPE | weather/customer/load | privacy | P0 |
| SEED-ENS-D07-0019 | renewable | project lifecycle master | D06 common | reporting accuracy | project/gate/COD | owner | P0 |
| SEED-ENS-D07-0020 | OWF1 | weather-window O&M optimizer | D06 renewable | lost MWh/MTTR | metocean/vessel/work | marine safety | P0 |
| SEED-ENS-D07-0021 | OWF1 | turbine power-curve anomaly | D06 renewable | availability | SCADA/weather | OEM data | P0 |
| SEED-ENS-D07-0022 | OWF1 | CMS failure prediction | D06 O&M | lead time | vibration/oil/work | labels | P1 |
| SEED-ENS-D07-0023 | OWF2/3 | phase-1 learning transfer | D06 development | LCOE/CAPEX | defects/yield/design | JV/EPC rights | P0 |
| SEED-ENS-D07-0024 | solar/wind | forecast and curtailment attribution | D06-044 | forecast error/lost MWh | forecast/meter/grid | curtailment label | P0 |
| SEED-ENS-D07-0025 | PPA | asset-meter-contract reconciliation | D06-050 | settlement exception | meter/PPA/REC | legal rule | P0 |
| SEED-ENS-D07-0026 | KCE | bid-degradation co-optimizer | D06-053 | lifetime margin | bid/dispatch/BMS | warranty | P0 |
| SEED-ENS-D07-0027 | KCE | cell-to-site thermal risk model | D06 ESS safety | early warning | cell/rack/HVAC | safety certification | P0 |
| SEED-ENS-D07-0028 | KCE | portfolio/project inclusion validator | D06 common | reporting errors | master/status | owner | P1 |
| SEED-ENS-D07-0029 | KCE | interconnection/congestion model | D06 market | captured spread | node/price/dispatch | ISO data | P1 |
| SEED-ENS-D07-0030 | KCE | warranty-aware SOH forecast | D06 ESS | SOH error | cycles/temp/SOC | vendor terms | P0 |
| SEED-ENS-D07-0031 | EverCharge | dynamic building load allocation | D06-058 | ports/service kW | building/session | local control | P0 |
| SEED-ENS-D07-0032 | EverCharge | charger fault triage | D06 EV | uptime/truck roll | fault/log/reset | remote access | P1 |
| SEED-ENS-D07-0033 | EverCharge | site expansion capacity recommender | D06 EV | CAPEX/ports | circuit/load/queue | engineering review | P1 |
| SEED-ENS-D07-0034 | Incheon LH2 | train load/SEC optimizer | D06-062 | kWh/kg | historian/purity/load | process safety | P0 |
| SEED-ENS-D07-0035 | Incheon LH2 | boil-off forecast/control | D06-063 | BOR/product loss | tank/pressure/dispatch | safety | P0 |
| SEED-ENS-D07-0036 | LH2 network | plant-tanker-station inventory optimizer | D06 hydrogen | stockout/loss | inventory/ETA/demand | partner data | P0 |
| SEED-ENS-D07-0037 | LH2 | predictive maintenance for liquefier | D06 hydrogen | availability | vibration/process/work | vendor | P1 |
| SEED-ENS-D07-0038 | CCS | project capacity and MRV readiness ledger | D06 CCS | gate completeness | design/permit/MRV | non-operating | P1 |
| SEED-ENS-D07-0039 | Bayu-Undan | storage injectivity uncertainty model | D06 CCS | capacity confidence | geology/well/model | partner/regulator | P2 |
| SEED-ENS-D07-0040 | Quynh Lap | EPC asset-data requirement library | D06 common | handover completeness | tag/doc/spec | contract timing | P0 |
| SEED-ENS-D07-0041 | Quynh Lap | terminal-power integrated design twin | D06 LNG/power | CAPEX/availability | design/load/grid | FEED data | P1 |
| SEED-ENS-D07-0042 | global | JV data-right registry | D06 common | accessible fields | contract/system | legal | P0 |
| SEED-ENS-D07-0043 | global | lifecycle event detector | D06 common | stale records | filings/news/master | human approval | P1 |
| SEED-ENS-D07-0044 | global | asset hierarchy/entity resolution | D06 common | duplicate rate | names/coords/entity | steward | P0 |
| SEED-ENS-D07-0045 | global | capacity unit and scope validator | D06 common | semantic errors | capacity/source | rule owner | P0 |

## 13.1 P0 Shortlist

| Rank group | Seed | Why now |
|---|---|---|
| A | 0003 Boryeong inventory | LNG-power chain foundation |
| A | 0005 integrated LNG-power plan | portfolio margin impact |
| A | 0007 fleet heat-rate | operating data and direct fuel value |
| A | 0012 CHP co-optimizer | E&S-specific multi-product operation |
| A | 0013 gas asset graph | safety analytics prerequisite |
| A | 0014 leak-risk ranking | safety and inspection productivity |
| A | 0020 offshore wind O&M | new operating asset, weather bottleneck |
| A | 0026 BESS bid-degradation | distinctive KCE capability |
| A | 0034 LH2 train optimizer | unique large operating asset |
| A | 0036 LH2 inventory optimizer | plant-to-network value chain |
| Foundation | 0006 rights ledger | prevents false capacity/ownership |
| Foundation | 0042 JV data-right registry | PoC feasibility |
| Foundation | 0044 asset entity resolution | cross-document join |
| Foundation | 0045 capacity validator | D07 data quality |

---
