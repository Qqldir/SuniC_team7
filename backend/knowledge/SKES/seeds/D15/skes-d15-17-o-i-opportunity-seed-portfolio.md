---
id: skes-d15-17-o-i-opportunity-seed-portfolio
title: O/I Opportunity Seed Portfolio
summary: "E&S 영역의 리스크·통증점을 해결하는 AI 기회 40개에 대한 레지스터 테이블로, 각 기회의 필요 데이터, KPI, 소유 부서를 기록한다."
tags: [d15, risk, oi-seed, table, "xref:d01", "xref:d13", "xref:d17"]
keywords: [E&S 기술 기회, LNG 거래, BESS 배터리, 신재생에너지, 도시가스, 해상풍력, 리스크 완화, 성공지표, AI 기반 최적화, 데이터 기반 의사결정]
related: [SEED-ENS-D15-001, SEED-ENS-D15-002, SEED-ENS-D15-003, SEED-ENS-D15-004, SEED-ENS-D15-005, SEED-ENS-D15-006, SEED-ENS-D15-007, SEED-ENS-D15-008, SEED-ENS-D15-009, SEED-ENS-D15-010, SEED-ENS-D15-011, SEED-ENS-D15-012, SEED-ENS-D15-013, SEED-ENS-D15-014, SEED-ENS-D15-015, SEED-ENS-D15-016, SEED-ENS-D15-017, SEED-ENS-D15-018, SEED-ENS-D15-019, SEED-ENS-D15-020, SEED-ENS-D15-021, SEED-ENS-D15-022, SEED-ENS-D15-023, SEED-ENS-D15-024]
priority: normal
domain: D15
section: 17
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 2646
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 17. O/I Opportunity Seed Portfolio

## 17.1 Seed Register 1–40

| Seed ID | Opportunity | Risk/Pain | Required Data | Success KPI | Gate |
|---|---|---|---|---|---|
| `SEED-ENS-D15-001` | LNG Geopolitical Flow Early-Warning | R001/P003 | AIS·loadings·news·cargo | alert lead time | Trading |
| `SEED-ENS-D15-002` | Cargo–Terminal–Power Resilience Twin | R001~009/P002 | cargo·tank·burn | replacement cost | Ops/Trading |
| `SEED-ENS-D15-003` | LNG ETA & Berth Conflict Optimizer | R004/P004 | AIS·slot·tank | demurrage hours | Ops |
| `SEED-ENS-D15-004` | TUA Utilization Option Engine | R006/P005 | TUA·cargo·slot | utilized capacity | Legal/Trading |
| `SEED-ENS-D15-005` | Physical–Hedge Basis Reconciler | R005 | positions·indices | unexplained exposure | Treasury |
| `SEED-ENS-D15-006` | Barossa Ramp Early Warning | R003 | operator production | ramp variance lead time | JV |
| `SEED-ENS-D15-007` | Turbine Trip Precursor AI | R007/P006 | vibration·temp·trip | avoided outage | SHE/Ops |
| `SEED-ENS-D15-008` | Heat-Rate Degradation Twin | R007/P006 | fuel·MWh·weather | heat-rate gap | Ops |
| `SEED-ENS-D15-009` | Scarcity-Aware Maintenance Scheduler | R007/P007 | CMMS·SMP·failure | outage margin | Ops/Market |
| `SEED-ENS-D15-010` | CHP Heat–Power Joint Risk Optimizer | R008/P008 | heat·power·fuel | joint margin | Ops |
| `SEED-ENS-D15-011` | City-Gas Pressure Anomaly Graph | R010/P009 | SCADA·GIS | detection lead | SHE |
| `SEED-ENS-D15-012` | Excavation-to-Pipeline Risk Geofence | R010 | work permit·GIS | third-party damage | SHE/Privacy |
| `SEED-ENS-D15-013` | Weather-normalized City-Gas Forecast | R011/P010 | weather·customer load | forecast error | Commercial |
| `SEED-ENS-D15-014` | Offshore Wind Marine Access Planner | R012/P011 | weather·vessel·work | MTTR | SHE/Ops |
| `SEED-ENS-D15-015` | Offshore Cable Health Analytics | R012/P012 | SCADA·condition | warning lead | Ops |
| `SEED-ENS-D15-016` | Curtailment Forecast & PPA Matcher | R013~014/P013 | grid·MWh·PPA | imbalance cost | Market/Legal |
| `SEED-ENS-D15-017` | Renewable Attribute Evidence Ledger | R014/P014 | meter·REC·PPA | evidence exception | Legal |
| `SEED-ENS-D15-018` | Offtaker Credit Early Warning | R015 | AR·rating·news | default lead | Finance |
| `SEED-ENS-D15-019` | BESS Thermal Anomaly Fusion | R016/P018 | BMS·weather·fault | false negative/lead | Safety |
| `SEED-ENS-D15-020` | BESS SOH Uncertainty Engine | R017/P015 | cycles·test·SOH | forecast error | Ops |
| `SEED-ENS-D15-021` | Degradation-Aware BESS Bidder | R017~019/P015 | SOH·price·dispatch | lifecycle net margin | Market/Safety |
| `SEED-ENS-D15-022` | BESS Market Saturation Radar | R018/P016 | operating MW·spread | revenue forecast | Market |
| `SEED-ENS-D15-023` | ERCOT/NYISO Rule Change Agent | R019/P017 | protocol·release | deployment latency | Legal/Market |
| `SEED-ENS-D15-024` | Bid Model Drift Monitor | R019 | bid·actual·regime | forecast calibration | Market |
| `SEED-ENS-D15-025` | Charger Self-Diagnostics | R021/P019 | fault·session | MTTR/uptime | Cyber |
| `SEED-ENS-D15-026` | Charging Site Power Headroom Twin | R020/P020 | panel·load·utility | site conversion | Utility |
| `SEED-ENS-D15-027` | Fleet Departure-SOC Predictor | R021 | session·route·SOC | SLA success | Privacy |
| `SEED-ENS-D15-028` | LH2 Mass-Balance Twin | R022~024/P021 | train·tank·trailer·station | unexplained kg loss | SHE |
| `SEED-ENS-D15-029` | LH2 Barrier Health Monitor | R022/P022 | detector·ESD·PSV | impairment hours | SHE |
| `SEED-ENS-D15-030` | LH2 BOG Predictive Control | R022 | temp·pressure·BOG | BOG ratio | SHE/Ops |
| `SEED-ENS-D15-031` | H2 Demand Confidence Engine | R024/P023 | vehicle·contract·paid kg | utilization error | Commercial |
| `SEED-ENS-D15-032` | H2 Trailer–Station Inventory Optimizer | R023/P024 | inventory·ETA·demand | stockout | SHE/Logistics |
| `SEED-ENS-D15-033` | H2 Station Reliability Network | R023 | faults·spares | uptime | SHE |
| `SEED-ENS-D15-034` | CCS FID Probability Graph | R025/P026 | emitter stage·contract | firm volume forecast | Legal/Finance |
| `SEED-ENS-D15-035` | CCS Storage Confidence Twin | R026/P025 | subsurface·permit | capacity confidence | Technical |
| `SEED-ENS-D15-036` | CCS Digital MRV Lineage | R026/P027 | meter·sample·rule | evidence completeness | Legal/MRV |
| `SEED-ENS-D15-037` | CCS Long-tail Liability Mapper | R040/P028 | contract·law·insurance | uncovered obligations | Legal |
| `SEED-ENS-D15-038` | Quynh Lap Deadline Monte Carlo | R028/P029 | schedule·permit·grid | deadline probability | Project/Legal |
| `SEED-ENS-D15-039` | Offshore Wind Permit Dependency AI | R027 | permit milestones | critical slack | Legal/Project |
| `SEED-ENS-D15-040` | Project EAC–Cash Call Early Warning | R029~030/P030 | WBS·invoice·JV | forecast error | Finance |

## 17.2 Seed Register 41–80

| Seed ID | Opportunity | Risk/Pain | Required Data | Success KPI | Gate |
|---|---|---|---|---|---|
| `SEED-ENS-D15-041` | JV Reserved-Matter Aging Agent | R031/P031 | agreement·decision | decision lead time | Legal |
| `SEED-ENS-D15-042` | Contract Obligation Knowledge Graph | R032/P032 | signed docs | missed deadline | Legal |
| `SEED-ENS-D15-043` | Counterparty Covenant Watch | R029·033 | financial/covenant | warning lead | Finance |
| `SEED-ENS-D15-044` | K-ETS Allocation-Position Twin | R034/P033 | emissions·allowance | carbon cost error | Trading/Legal |
| `SEED-ENS-D15-045` | PFE Supplier Evidence Graph | R035/P034 | supplier/BOM/origin | evidence completeness | Tax/Legal |
| `SEED-ENS-D15-046` | 48E Eligibility Evidence Calculator | R035 | tax basis/PWA/PFE | credit-at-risk | Tax |
| `SEED-ENS-D15-047` | Charging Incentive Economics Refresh | R036 | program·site economics | funnel forecast | Tax/Commercial |
| `SEED-ENS-D15-048` | Regulation Effective-Date Engine | R037~040/P035 | law/rule versions | stale-rule rate | Legal |
| `SEED-ENS-D15-049` | Source-Locked Legal RAG | R047~048/P041 | authoritative docs | citation coverage | Legal |
| `SEED-ENS-D15-050` | Permit Condition Compliance Agent | R027~028 | permit·evidence | overdue items | Legal |
| `SEED-ENS-D15-051` | Sanctions/ABAC Relationship Graph | R041 | party/UBO/country | false-negative/aging | Compliance |
| `SEED-ENS-D15-052` | Insurance Coverage Gap Mapper | R042/P043 | policy·asset·contract | uninsured exposure | Risk/Legal |
| `SEED-ENS-D15-053` | Claim Notification Deadline Agent | R042 | incident·policy | late notice | Legal/Risk |
| `SEED-ENS-D15-054` | OT Asset Discovery & Exposure Map | R043/P036 | network/device | unknown assets | CISO/SHE |
| `SEED-ENS-D15-055` | Vendor Remote Access JIT Gateway | R044/P037 | PAM/vendor | exception sessions | CISO |
| `SEED-ENS-D15-056` | OT Configuration Drift Monitor | R043~046 | config baseline | drift aging | CISO/Ops |
| `SEED-ENS-D15-057` | OT Safety-Cyber Correlation Engine | R043~046/P039 | cyber+barrier | triage time | CISO/SHE |
| `SEED-ENS-D15-058` | Immutable Backup Restore Orchestrator | R058/P038 | backup/restore | restore success/RTO | CISO |
| `SEED-ENS-D15-059` | BESS/Charger Edge Fallback Controller | R045~046 | cloud/local | service continuity | CISO/Safety |
| `SEED-ENS-D15-060` | AI Source Freshness Sentinel | R047/P035·041 | sources/version | stale ratio | Legal/Data |
| `SEED-ENS-D15-061` | AI Null-vs-Zero Guard | R047/P040 | schema/DQ | false certainty | Data |
| `SEED-ENS-D15-062` | Unit/Period Consistency Gate | R047 | metadata | unit errors | Data |
| `SEED-ENS-D15-063` | Entity-Lineage Contract Guard | R048 | D01/D13 | party error | Legal |
| `SEED-ENS-D15-064` | Human-in-Command Approval Layer | R049/P050 | workflow/roles | unauthorized action=0 | Safety/Legal |
| `SEED-ENS-D15-065` | Tail-Risk Scenario Workbench | R057/P042 | exposure/control | reverse-stress coverage | CRO/Finance |
| `SEED-ENS-D15-066` | Portfolio Correlation Stress Engine | R057/P049 | all assets/weather | correlated loss visibility | CRO |
| `SEED-ENS-D15-067` | Extreme-Weather Asset Resilience Twin | R051~053 | weather/asset | outage lead | SHE/Ops |
| `SEED-ENS-D15-068` | Critical Spare Network Optimizer | R054/P048 | BOM/spare/failure | downtime | Procurement |
| `SEED-ENS-D15-069` | Supplier Insolvency Early Warning | R054 | supplier financial | warning lead | Procurement |
| `SEED-ENS-D15-070` | Contractor Competence Risk Passport | R055 | training/work | overdue competence | SHE/Privacy |
| `SEED-ENS-D15-071` | Crisis Decision Log Copilot | R056 | incident/roles | decision traceability | Legal/SHE |
| `SEED-ENS-D15-072` | BCP Dependency Graph | R058 | service/app/vendor | untested dependency | CISO/Ops |
| `SEED-ENS-D15-073` | Automated Tabletop Scenario Generator | R057~058 | risk graph | scenario coverage | Safety |
| `SEED-ENS-D15-074` | Recovery RTO/RPO Evidence Dashboard | R058 | drill/restore | RTO achievement | CISO/Ops |
| `SEED-ENS-D15-075` | Incident-to-CAPA Closure Graph | R060/P046 | incident/CAPA | recurrence/aging | SHE |
| `SEED-ENS-D15-076` | Risk Acceptance Expiry Agent | R060/P047 | acceptance | overdue=0 | Risk |
| `SEED-ENS-D15-077` | External-Case Evidence Classifier | R047/P045 | sources | false incident mapping | Data |
| `SEED-ENS-D15-078` | D15 Risk-to-D17 Duplicate Detector | P001·050 | seed graph | duplicate rate | O/I |
| `SEED-ENS-D15-079` | O/I Safety-Legal Gate Scorer | P050 | seed/control/rule | unsafe PoC screened | EHS/Legal |
| `SEED-ENS-D15-080` | Enterprise Risk Knowledge Graph | R001~060 | D01~D15 IDs | cross-domain coverage | CRO/Data |

---
