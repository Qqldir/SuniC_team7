---
id: skes-d16-4-solution-master-registry
title: Solution Master Registry
summary: SK이노베이션 E&S D16에서 LNG·발전·회전기계 등 사업별 검토 중인 외부 상용솔루션의 공급사·기능·적용점·게이트 조건을 정리한 포트폴리오 평가 표다.
tags: [d16, ecosystem, table, "xref:d15"]
keywords: [D16, LNG·Shipping, 발전·CHP, 회전기계, Vendor, E&S적용, 기술게이트, 상용기술]
related: [SOL-ENS-D16-001, SOL-ENS-D16-002, SOL-ENS-D16-003, SOL-ENS-D16-004, SOL-ENS-D16-005, SOL-ENS-D16-006, SOL-ENS-D16-007, SOL-ENS-D16-008, SOL-ENS-D16-009, SOL-ENS-D16-010, SOL-ENS-D16-011, SOL-ENS-D16-012, SOL-ENS-D16-013, SOL-ENS-D16-014, SOL-ENS-D16-015, SOL-ENS-D16-016, SOL-ENS-D16-017, SOL-ENS-D16-018, SOL-ENS-D16-019, SOL-ENS-D16-020, SOL-ENS-D16-021, SOL-ENS-D16-022, SOL-ENS-D16-023, SOL-ENS-D16-024]
priority: normal
domain: D16
section: 4
source: SK이노베이션E&S_D16_External_Technologies_Solutions_Companies_and_Startups.md
breadcrumb: ""
tokens: 3451
updated: 2026-08-06
---

> SK이노베이션 E&S · D16 외부 기술·솔루션·기업·스타트업

# 4. Solution Master Registry

## 4.1 LNG·Shipping·Terminal

| Solution ID | Vendor/Product | 기능 | Evidence | E&S 적용점 | 핵심 Gate |
|---|---|---|---|---|---|
| `SOL-ENS-D16-001` | S&P LNG Market Insights | 가격·수급·outage·contract | E3 | cargo/portfolio view | license/API |
| `SOL-ENS-D16-002` | S&P MINT | real-time vessel tracking | E3 | LNG ETA/diversion | AIS quality |
| `SOL-ENS-D16-003` | S&P Commodities at Sea | trade-flow/fleet analytics | E3 | global flow shock | cargo inference |
| `SOL-ENS-D16-004` | Kongsberg Valid Voyage | weather routing | E3 | vessel ETA/fuel | ship interface |
| `SOL-ENS-D16-005` | Kongsberg Valid Performance | vessel digital fuel model | E3 | consumption deviation | vessel data rights |
| `SOL-ENS-D16-006` | AVEVA PI System | industrial historian/context | E2 | terminal data backbone | OT segmentation |
| `SOL-ENS-D16-007` | AVEVA Process Simulation | process twin | E2 | terminal energy optimization | model calibration |
| `SOL-ENS-D16-008` | AtkinsRéalis+AVEVA twin | live optimization | E2 | send-out/compression | operator approval |
| `SOL-ENS-D16-009` | Honeywell UniSim | first-principles simulation | E3 | LNG/H2 process what-if | model validation |
| `SOL-ENS-D16-010` | Emerson Tank Gauging | tank profile/rollover monitoring | E3 | LNG tank condition | instrument integrity |
| `SOL-ENS-D16-011` | Honeywell APC | multivariable optimization | E3 | process constraint control | MOC/SIS boundary |
| `SOL-ENS-D16-012` | ABB digital twin | control replica/training | E2 | terminal/control testing | DCS compatibility |

## 4.2 발전·CHP·Rotating Equipment

| Solution ID | Vendor/Product | 기능 | Evidence | E&S 적용점 | 핵심 Gate |
|---|---|---|---|---|---|
| `SOL-ENS-D16-013` | GE Vernova SmartSignal | predictive analytics | E2/E3 | GT/ST/HRSG auxiliaries | sensor coverage |
| `SOL-ENS-D16-014` | GE Vernova APM | fleet asset performance | E2 | 발전 fleet | OEM/non-OEM access |
| `SOL-ENS-D16-015` | Seeq Condition Monitoring | time-series predictive workflow | E2 | GT thermocouple/brush gear | alert validation |
| `SOL-ENS-D16-016` | C3 AI Reliability | ML predictive maintenance | E2 | pump/compressor/valve | failure labels |
| `SOL-ENS-D16-017` | Emerson AMS Optics | APM+CMMS workflow | E3 | plant auxiliaries | CMMS mapping |
| `SOL-ENS-D16-018` | Emerson Ovation | power control/optimization | E3 | CCGT/CHP | control authority |
| `SOL-ENS-D16-019` | Honeywell UniSim Twin | process what-if | E3 | heat rate/operating envelope | physics validation |
| `SOL-ENS-D16-020` | AspenTech APM | asset anomaly/RUL | E3 | rotating equipment | data availability |
| `SOL-ENS-D16-021` | IBM Maximo | EAM/condition-work order | E3 | maintenance execution | master-data quality |
| `SOL-ENS-D16-022` | SAP EAM | maintenance/parts/cost | E3 | work economics | ERP integration |
| `SOL-ENS-D16-023` | ABB 800xA analytics | control+asset monitoring | E3 | plant electrical/process | installed base |
| `SOL-ENS-D16-024` | Siemens Energy digital service | GT fleet diagnostics | E3 | turbine performance | OEM boundary |

## 4.3 도시가스·Pipeline·Methane

| Solution ID | Vendor/Product | 기능 | Evidence | E&S 적용점 | 핵심 Gate |
|---|---|---|---|---|---|
| `SOL-ENS-D16-025` | Esri ArcGIS Utility Network | network topology/GIS | E3 | pipeline asset graph | topology accuracy |
| `SOL-ENS-D16-026` | Urbint risk analytics | excavation/field risk | E3 | damage prevention | local model transfer |
| `SOL-ENS-D16-027` | Honeywell Signal Scout | methane leak sensor | E3 | stations/critical points | certification |
| `SOL-ENS-D16-028` | GHGSat monitoring | satellite methane | E3 | external emission screening | detection limits |
| `SOL-ENS-D16-029` | Kayrros methane analytics | satellite methane signals | E3 | network/upstream signal | attribution |
| `SOL-ENS-D16-030` | C3 AI utility reliability | asset failure risk | E2 | network asset prioritization | local failure data |
| `SOL-ENS-D16-031` | Neara network model | digital network modeling | E3 | network resilience | model completeness |
| `SOL-ENS-D16-032` | Percepto drone | autonomous inspection | E3 | stations/pipeline ROW | aviation/privacy |
| `SOL-ENS-D16-033` | ANYbotics robot | autonomous inspection | E3 | compressor/regulator site | hazardous-zone cert |
| `SOL-ENS-D16-034` | computer vision leak/zone | video anomaly pattern | E5 | selected unmanned site | false alarm/privacy |

## 4.4 해상풍력·재생·PPA

| Solution ID | Vendor/Product | 기능 | Evidence | E&S 적용점 | 핵심 Gate |
|---|---|---|---|---|---|
| `SOL-ENS-D16-035` | Vestas Digital Services | fleet data/diagnostics | E3 | wind turbines | OEM data rights |
| `SOL-ENS-D16-036` | Siemens Gamesa CMS | vibration+AI/ML detection | E3 | turbine drivetrain | warranty/interface |
| `SOL-ENS-D16-037` | Fluence Nispera Wind | multi-OEM APM | E2/E3 | wind portfolio | SCADA normalization |
| `SOL-ENS-D16-038` | SkySpecs inspection | drone blade inspection | E3 | blade O&M | offshore weather |
| `SOL-ENS-D16-039` | Kongsberg offshore data | marine/asset data | E3 | offshore ops | vessel integration |
| `SOL-ENS-D16-040` | Amperon forecasting | load/renewable forecast | E3 | PPA/dispatch | Korea data fit |
| `SOL-ENS-D16-041` | Pexapark analytics | PPA pricing/risk | E3 | PPA portfolio | market localization |
| `SOL-ENS-D16-042` | Seeq renewable analytics | performance/time-series | E3 | wind/solar RCA | historian access |
| `SOL-ENS-D16-043` | AVEVA PI | multi-asset historian | E3 | renewable fleet | tag harmonization |
| `SOL-ENS-D16-044` | weather-window optimizer | metocean scheduling | E5 | offshore O&M | forecast accuracy |

## 4.5 BESS / KCE

| Solution ID | Vendor/Product | 기능 | Evidence | E&S 적용점 | 핵심 Gate |
|---|---|---|---|---|---|
| `SOL-ENS-D16-045` | Fluence Nispera Storage | predictive APM | E3 | KCE fleet | OEM data access |
| `SOL-ENS-D16-046` | Fluence Mosaic | intelligent bidding | E3 | ERCOT/NYISO | market rule validation |
| `SOL-ENS-D16-047` | Wärtsilä GEMS | EMS/control optimization | E2/E3 | BESS/hybrid | controller integration |
| `SOL-ENS-D16-048` | UL 9540A testing | propagation test | E1 | design/fire plan | edition/AHJ |
| `SOL-ENS-D16-049` | UL large-scale fire test | installation fire behavior | E1 | site spacing/response | test applicability |
| `SOL-ENS-D16-050` | DNV storage assurance | technical due diligence | E3 | acquisition/project | scope-specific |
| `SOL-ENS-D16-051` | degradation-aware scheduler | SOH+warranty+price | E5 | lifecycle bidding | warranty data |
| `SOL-ENS-D16-052` | thermal anomaly fusion | BMS+EMS+ambient | E5 | early safety signal | safety non-bypass |
| `SOL-ENS-D16-053` | settlement reconciliation AI | bid→dispatch→meter→settle | E5 | revenue leakage | market data lineage |
| `SOL-ENS-D16-054` | augmentation optimizer | SOH→capacity plan | E5 | lifecycle CAPEX | vendor warranty |

## 4.6 EV Charging / EverCharge

| Solution ID | Vendor/Product | 기능 | Evidence | E&S 적용점 | 핵심 Gate |
|---|---|---|---|---|---|
| `SOL-ENS-D16-055` | ChargePoint platform | charger fleet management | E2/E3 | benchmark/partner | OCPP/API |
| `SOL-ENS-D16-056` | ChargePoint power mgmt | site power scheduling | E2/E3 | MUD/workplace/fleet | transformer limit |
| `SOL-ENS-D16-057` | WeaveGrid managed charging | grid-aware scheduling | E2/E3 | flexible load | OEM/customer consent |
| `SOL-ENS-D16-058` | remote diagnostics engine | failure classification | E5 | charger uptime | telemetry quality |
| `SOL-ENS-D16-059` | payment/session reconciliation | auth→energy→payment | E5 | revenue leakage | PCI/privacy |
| `SOL-ENS-D16-060` | site power digital twin | panel/transformer/ports | E5 | capacity planning | electrical model |
| `SOL-ENS-D16-061` | predictive truck roll | fault→remote fix probability | E5 | field service cost | technician labels |
| `SOL-ENS-D16-062` | spare-parts optimizer | failure/lead time inventory | E5 | uptime/cost | parts master |

## 4.7 액화수소 / Incheon LH2

| Solution ID | Vendor/Product | 기능 | Evidence | E&S 적용점 | 핵심 Gate |
|---|---|---|---|---|---|
| `SOL-ENS-D16-063` | H2scan HY-ALERTA | H2-specific fixed detection | E3 | leak barrier | hazardous area |
| `SOL-ENS-D16-064` | H2scan process analyzer | inline H2 concentration | E3 | process quality | calibration |
| `SOL-ENS-D16-065` | Emerson Micro Motion ELITE | ultra-cryogenic mass flow | E3 | LH2 custody/mass balance | -254°C config |
| `SOL-ENS-D16-066` | Emerson cryogenic valves | LH2/LNG flow control | E3 | cold box/transfer | leakage/SIL |
| `SOL-ENS-D16-067` | Emerson Fisher IC2 | top-entry cryogenic control | E3 | H2 liquefaction cold box | material/pressure |
| `SOL-ENS-D16-068` | Chart cryogenic storage | LH2 tanks | E3 | storage benchmark | interface/vendor |
| `SOL-ENS-D16-069` | Honeywell UniSim | liquefaction process twin | E3 | energy/yield optimization | first-principles fit |
| `SOL-ENS-D16-070` | barrier health monitor | detector/valve/ESD proof data | E5 | process safety | SIS independence |
| `SOL-ENS-D16-071` | LH2 mass-balance twin | train→tank→trailer→sold | E5 | loss/BOG/utilization | metering accuracy |
| `SOL-ENS-D16-072` | BOG optimizer | pressure/BOG routing | E5 | product loss/energy | control MOC |

## 4.8 CCS / CO2

| Solution ID | Vendor/Product | 기능 | Evidence | E&S 적용점 | 핵심 Gate |
|---|---|---|---|---|---|
| `SOL-ENS-D16-073` | SLB Sequestri Evaluation | capacity/injectivity/containment | E2/E3 | storage screening | geology data |
| `SOL-ENS-D16-074` | SLB MMV Planning | risk-based MMV | E2 | offshore CCS | jurisdiction rules |
| `SOL-ENS-D16-075` | SLB reservoir simulation | plume/injection model | E3 | storage design | uncertainty |
| `SOL-ENS-D16-076` | Baker Hughes CO2 compression | compression equipment | E2/E3 | transport/injection chain | equipment scope |
| `SOL-ENS-D16-077` | Baker Hughes monitoring | CCS monitoring package | E2/E3 | compressor/storage | project-specific |
| `SOL-ENS-D16-078` | digital MRV ledger | meter→chain→report lineage | E5 | cross-border CCS | regulator acceptance |
| `SOL-ENS-D16-079` | emitter-storage matcher | firm tCO2 vs injectivity | E5 | commercial/FID | contract status |
| `SOL-ENS-D16-080` | long-tail liability graph | well/plume/permit/liability | E5 | governance | legal interpretation |

## 4.9 OT Cyber·Enterprise Data·AI

| Solution ID | Vendor/Product | 기능 | Evidence | E&S 적용점 | 핵심 Gate |
|---|---|---|---|---|---|
| `SOL-ENS-D16-081` | Dragos Platform | passive asset visibility | E2/E3 | plant/grid OT | passive-first |
| `SOL-ENS-D16-082` | Dragos INSM | internal OT network monitoring | E2 | critical networks | network architecture |
| `SOL-ENS-D16-083` | Cognite Data Fusion | industrial contextualization | E3 | asset/process graph | source authority |
| `SOL-ENS-D16-084` | AVEVA CONNECT/PI | industrial data fabric | E3 | historian federation | data residency |
| `SOL-ENS-D16-085` | Databricks | governed analytics/ML | E3 | enterprise AI layer | OT isolation |
| `SOL-ENS-D16-086` | Palantir ontology | object/decision graph | E3 | risk/contract/asset | lock-in/export |
| `SOL-ENS-D16-087` | Icertis | contract intelligence | E3 | JV/PPA/EPC obligations | legal QA |
| `SOL-ENS-D16-088` | Ironclad | CLM/AI workflow | E3 | contract intake | template fit |
| `SOL-ENS-D16-089` | ServiceNow workflow | incident/work orchestration | E3 | risk/OT/IT workflow | CMDB quality |
| `SOL-ENS-D16-090` | OpenText content platform | controlled documents | E3 | manuals/P&ID/contracts | version authority |
| `SOL-ENS-D16-091` | source-locked RAG | cited answer/effective date | E5 | regulation/engineering | permission/freshness |
| `SOL-ENS-D16-092` | enterprise risk KG | risk→asset→contract→rule | E5 | D15 operationalization | graph stewardship |
| `SOL-ENS-D16-093` | project Monte Carlo | schedule/cost distributions | E5 | offshore/Quynh Lap/CCS | dependency quality |
| `SOL-ENS-D16-094` | supply-risk graph | supplier/entity/route/event | E5 | PFE/LNG/projects | entity resolution |
| `SOL-ENS-D16-095` | tax evidence engine | invoice/BOM/entity lineage | E5 | US BESS | tax counsel gate |
| `SOL-ENS-D16-096` | AI decision audit | input/version/approver/output | E5 | all high-stakes AI | immutable log |

---
