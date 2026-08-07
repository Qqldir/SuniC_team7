---
id: skes-d15-19-internal-data-request-register
title: Internal Data Request Register
summary: "SK이노베이션 E&S의 LNG, 발전, 수소, ESS 등 사업 영역에서 요구하는 33개 데이터 요청항목의 목적, 담당자, 민감도 수준을 정리한 표."
tags: [d15, risk, table]
keywords: [LNG, 데이터 거버넌스, 민감도, SCADA, 수소, ESS, CCS, 재생에너지, 리스크, 회복탄력성]
related: [DR-ENS-D15-001, DR-ENS-D15-002, DR-ENS-D15-003, DR-ENS-D15-004, DR-ENS-D15-005, DR-ENS-D15-006, DR-ENS-D15-007, DR-ENS-D15-008, DR-ENS-D15-009, DR-ENS-D15-010, DR-ENS-D15-011, DR-ENS-D15-012, DR-ENS-D15-013, DR-ENS-D15-014, DR-ENS-D15-015, DR-ENS-D15-016, DR-ENS-D15-017, DR-ENS-D15-018, DR-ENS-D15-019, DR-ENS-D15-020, DR-ENS-D15-021, DR-ENS-D15-022, DR-ENS-D15-023, DR-ENS-D15-024]
priority: normal
domain: D15
section: 19
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 1130
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 19. Internal Data Request Register

| DR ID | 요청 데이터 | 목적 | Owner 후보 | Sensitivity |
|---|---|---|---|---|
| `DR-ENS-D15-001` | cargo schedule/entitlement | LNG exposure | LNG Ops | HIGH |
| `DR-ENS-D15-002` | LNG contract index/option summary | basis stress | Trading/Legal | RESTRICTED |
| `DR-ENS-D15-003` | hedge position/limits | net exposure | Treasury | RESTRICTED |
| `DR-ENS-D15-004` | terminal tank/slot/BOG history | logistics resilience | Ops | HIGH |
| `DR-ENS-D15-005` | demurrage actual | KPI baseline | Ops/Finance | HIGH |
| `DR-ENS-D15-006` | power plant trip/outage log | reliability | Plant | HIGH |
| `DR-ENS-D15-007` | turbine historian | predictive PoC | Plant | RESTRICTED_OT |
| `DR-ENS-D15-008` | heat-rate corrected baseline | economics | Plant | HIGH |
| `DR-ENS-D15-009` | maintenance backlog/critical path | outage risk | CMMS | HIGH |
| `DR-ENS-D15-010` | city gas SCADA alarm/event | safety | City Gas | RESTRICTED_OT |
| `DR-ENS-D15-011` | pipeline GIS/work permit | third-party damage | City Gas | HIGH |
| `DR-ENS-D15-012` | emergency response/drill log | BCP | SHE | HIGH |
| `DR-ENS-D15-013` | renewable SCADA/weather | availability | Renewable Ops | HIGH |
| `DR-ENS-D15-014` | offshore cable condition | tail risk | Offshore Ops | HIGH |
| `DR-ENS-D15-015` | curtailment/meter/REC | PPA risk | Market/Commercial | HIGH |
| `DR-ENS-D15-016` | PPA hourly obligation | shape risk | Legal/Commercial | RESTRICTED |
| `DR-ENS-D15-017` | KCE BMS/PCS/EMS events | BESS reliability | KCE | RESTRICTED_OT |
| `DR-ENS-D15-018` | BESS SOH/cycle/capacity test | degradation | KCE | HIGH |
| `DR-ENS-D15-019` | KCE bid/settlement history | model drift | KCE Market | RESTRICTED |
| `DR-ENS-D15-020` | optimizer versions/features | model governance | KCE | RESTRICTED |
| `DR-ENS-D15-021` | charger fault/session logs | uptime | EverCharge | HIGH/PRIVACY |
| `DR-ENS-D15-022` | site power/utility limits | site risk | EverCharge | HIGH |
| `DR-ENS-D15-023` | LH2 train historian | process safety | IGE/H2 Ops | RESTRICTED_OT |
| `DR-ENS-D15-024` | LH2 detector/ESD/PSV test | barrier health | SHE | RESTRICTED |
| `DR-ENS-D15-025` | produced/stored/loaded/sold/paid kg | H2 mass balance | H2 Ops/Finance | HIGH |
| `DR-ENS-D15-026` | station inventory/uptime | H2 logistics | H2 Mobility | HIGH |
| `DR-ENS-D15-027` | active vehicle/offtake contract | demand confidence | Commercial | RESTRICTED |
| `DR-ENS-D15-028` | CCS emitter stage/contract | firm volume | CCS BD | RESTRICTED |
| `DR-ENS-D15-029` | subsurface/injectivity data | storage risk | CCS Technical | RESTRICTED |
| `DR-ENS-D15-030` | CCS MRV measurement plan | compliance | CCS/MRV | RESTRICTED |
| `DR-ENS-D15-031` | Quynh Lap integrated schedule | 2031 stress | Project | RESTRICTED |
| `DR-ENS-D15-032` | permit condition register | schedule/compliance | Legal/Project | HIGH |
| `DR-ENS-D15-033` | project EAC/contingency | cash risk | Finance/Project | RESTRICTED |
| `DR-ENS-D15-034` | PF covenant/DSCR/DSRA | finance risk | Treasury | RESTRICTED |
| `DR-ENS-D15-035` | JV reserved matters/decision log | governance | Legal | RESTRICTED |
| `DR-ENS-D15-036` | CLM obligation/notice | contract risk | Legal | RESTRICTED |
| `DR-ENS-D15-037` | K-ETS emissions/allocation/position | carbon risk | Environment/Trading | RESTRICTED |
| `DR-ENS-D15-038` | PFE supplier origin evidence | tax credit | Procurement/Tax | RESTRICTED |
| `DR-ENS-D15-039` | OT asset/network inventory | cyber | CISO | RESTRICTED_SECURITY |
| `DR-ENS-D15-040` | vendor remote access log | cyber | CISO | RESTRICTED_SECURITY |
| `DR-ENS-D15-041` | backup/restore drill | resilience | CISO/IT | RESTRICTED_SECURITY |
| `DR-ENS-D15-042` | insurance policy/claim register | recovery | Risk/Legal | RESTRICTED |
| `DR-ENS-D15-043` | incident/near-miss/CAPA | learning | SHE/Risk | RESTRICTED |
| `DR-ENS-D15-044` | risk acceptance register | residual risk | ERM | RESTRICTED |
| `DR-ENS-D15-045` | BCP RTO/RPO/dependency/test | recovery | BCM/CISO | RESTRICTED_SECURITY |

---
