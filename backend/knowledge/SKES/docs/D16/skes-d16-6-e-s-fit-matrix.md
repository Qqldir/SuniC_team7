---
id: skes-d16-6-e-s-fit-matrix
title: E&S Fit Matrix
summary: "SK이노베이션의 각 사업 영역(LNG, 발전, 가스 등)에서 데이터와 AI 기술로 해결할 수 있는 운영 과제와 검증 지표를 정리한 기술 적합도 매트릭스이다."
tags: [d16, ecosystem, table, "xref:d15", "xref:d01"]
keywords: [LNG, 발전, 도시가스, 신재생에너지, BESS, 설비 진단, 예측정비, PoC]
related: [FIT-ENS-D16-001, FIT-ENS-D16-002, FIT-ENS-D16-003, FIT-ENS-D16-004, FIT-ENS-D16-005, FIT-ENS-D16-006, FIT-ENS-D16-007, FIT-ENS-D16-008, FIT-ENS-D16-009, FIT-ENS-D16-010, FIT-ENS-D16-011, FIT-ENS-D16-012, FIT-ENS-D16-013, FIT-ENS-D16-014, FIT-ENS-D16-015, FIT-ENS-D16-016, FIT-ENS-D16-017, FIT-ENS-D16-018, FIT-ENS-D16-019, FIT-ENS-D16-020, FIT-ENS-D16-021, FIT-ENS-D16-022, FIT-ENS-D16-023, FIT-ENS-D16-024]
priority: normal
domain: D16
section: 6
source: SK이노베이션E&S_D16_External_Technologies_Solutions_Companies_and_Startups.md
breadcrumb: ""
tokens: 1862
updated: 2026-08-06
---

> SK이노베이션 E&S · D16 외부 기술·솔루션·기업·스타트업

# 6. E&S Fit Matrix

## 6.1 LNG Value Chain Fit

| Fit ID | D15 Need | 후보 솔루션 | 필요한 E&S 데이터 | PoC KPI | 우선도 |
|---|---|---|---|---|---|
| `FIT-ENS-D16-001` | Cargo/route shock 조기탐지 | 001~005 | contract cargo·ETA·slot·inventory | signal lead time·ETA error | A |
| `FIT-ENS-D16-002` | Terminal energy optimization | 006~011 | PI tags·compressor·pump·send-out | MWh/MMSCF·constraint violation | A |
| `FIT-ENS-D16-003` | Demurrage/slot risk | 001~005 | berth·vessel·tank·weather | demurrage risk recall | B |
| `FIT-ENS-D16-004` | LNG quality/operating envelope | 007/009 | composition·pressure·temperature | off-spec avoidance | B |
| `FIT-ENS-D16-005` | rotating equipment failure | 013/016/017 | vibration·temperature·CMMS | lead time·precision | A |

## 6.2 Power/CHP Fit

| Fit ID | D15 Need | 후보 솔루션 | 필요한 E&S 데이터 | PoC KPI | 우선도 |
|---|---|---|---|---|---|
| `FIT-ENS-D16-006` | GT trip precursor | 013~020 | startup·thermocouple·vibration·alarm | false trip↓·lead time | A |
| `FIT-ENS-D16-007` | Heat Rate drift | 015/019/020 | fuel·MW·ambient·steam | heat-rate residual | A |
| `FIT-ENS-D16-008` | maintenance work prioritization | 017/021/022 | CMMS·criticality·parts | overdue critical WO | B |
| `FIT-ENS-D16-009` | CHP power/heat co-opt | 007/018/019 | heat demand·SMP·fuel·constraints | contribution margin proxy | B |
| `FIT-ENS-D16-010` | outage planning | 014/021/093 | outage scope·parts·crew | schedule variance | B |

## 6.3 City Gas Fit

| Fit ID | D15 Need | 후보 솔루션 | 필요한 E&S 데이터 | PoC KPI | 우선도 |
|---|---|---|---|---|---|
| `FIT-ENS-D16-011` | leak/anomaly localization | 025~034 | GIS·SCADA·alarm·work | localization time | A |
| `FIT-ENS-D16-012` | excavation damage risk | 025/026 | permit·ticket·asset·contractor | high-risk hit rate | A |
| `FIT-ENS-D16-013` | methane source screening | 027~029 | sensor/site/wind | verified alert precision | B |
| `FIT-ENS-D16-014` | regulator station inspection | 032/033 | route·images·alarm | inspection hours↓ | B |
| `FIT-ENS-D16-015` | network topology truth | 025/031 | GIS·valve·customer | topology exception rate | A |

## 6.4 Renewable/PPA Fit

| Fit ID | D15 Need | 후보 솔루션 | 필요한 E&S 데이터 | PoC KPI | 우선도 |
|---|---|---|---|---|---|
| `FIT-ENS-D16-016` | turbine failure warning | 035~037 | SCADA·CMS·WO | alert precision/lead time | A |
| `FIT-ENS-D16-017` | offshore access | 038/039/044 | metocean·CTV/SOV·crew | lost weather window↓ | A |
| `FIT-ENS-D16-018` | generation forecast | 040/042 | weather·actual generation | MAE/RMSE | A |
| `FIT-ENS-D16-019` | PPA shape/imbalance | 040/041 | hourly contract/load/gen | imbalance cost | A |
| `FIT-ENS-D16-020` | blade inspection | 038 | image·defect·repair | inspection cycle time | B |

## 6.5 KCE BESS Fit

| Fit ID | D15 Need | 후보 솔루션 | 필요한 E&S 데이터 | PoC KPI | 우선도 |
|---|---|---|---|---|---|
| `FIT-ENS-D16-021` | SOH/degradation | 045/047/051 | cell/rack/BMS/cycle | SOH error·warranty adherence | A |
| `FIT-ENS-D16-022` | thermal early warning | 045/048/049/052 | temperature·gas·alarm | lead time/false alarm | A |
| `FIT-ENS-D16-023` | bid margin erosion | 046/051 | price·bid·dispatch·SOH | degradation-adjusted margin | A |
| `FIT-ENS-D16-024` | settlement leakage | 053 | bid·dispatch·meter·invoice | unresolved variance | B |
| `FIT-ENS-D16-025` | augmentation timing | 047/054 | capacity test·SOH·forecast | NPV under scenarios | B |

## 6.6 EverCharge Fit

| Fit ID | D15 Need | 후보 솔루션 | 필요한 E&S 데이터 | PoC KPI | 우선도 |
|---|---|---|---|---|---|
| `FIT-ENS-D16-026` | charger downtime | 055/058/061 | heartbeat·error code·WO | MTTR·remote fix rate | A |
| `FIT-ENS-D16-027` | site power constraint | 056/057/060 | panel/transformer/load | overload events | A |
| `FIT-ENS-D16-028` | failed sessions | 055/058/059 | auth·meter·payment·error | session success rate | A |
| `FIT-ENS-D16-029` | truck-roll cost | 058/061/062 | fault·visit·parts | avoidable visits | B |
| `FIT-ENS-D16-030` | managed charging | 057/060 | EV availability·tariff·grid | peak kW/customer SLA | B |

## 6.7 LH2 Fit

| Fit ID | D15 Need | 후보 솔루션 | 필요한 E&S 데이터 | PoC KPI | 우선도 |
|---|---|---|---|---|---|
| `FIT-ENS-D16-031` | leak/barrier health | 063/064/070 | detector·proof-test·ESD | bad-actor barrier rate | A |
| `FIT-ENS-D16-032` | mass-balance loss | 065/071 | train/tank/trailer/station meters | unaccounted kg | A |
| `FIT-ENS-D16-033` | cryogenic valve leak | 066/067 | valve position·pressure·temp | leakage/maintenance | A |
| `FIT-ENS-D16-034` | BOG/product loss | 065/069/072 | tank P/T·BOG·vent/recycle | BOG kg/kg handled | A |
| `FIT-ENS-D16-035` | liquefaction energy | 069 | power·feed·yield·ambient | kWh/kg good product | A |

## 6.8 CCS Fit

| Fit ID | D15 Need | 후보 솔루션 | 필요한 E&S 데이터 | PoC KPI | 우선도 |
|---|---|---|---|---|---|
| `FIT-ENS-D16-036` | capacity/injectivity uncertainty | 073/075 | wells·seismic·pressure | uncertainty range | A |
| `FIT-ENS-D16-037` | risk-based MMV | 074/078 | risk·regulation·monitoring | risk coverage/cost | A |
| `FIT-ENS-D16-038` | emitter-storage mismatch | 079 | firm contracts·FID·injectivity | matched firm tCO2 | A |
| `FIT-ENS-D16-039` | compressor reliability | 076/077 | vibration·process·WO | availability/efficiency | B |
| `FIT-ENS-D16-040` | long-tail liability | 078/080 | permit·well·plume·closure | evidence completeness | B |

## 6.9 Enterprise/OT Fit

| Fit ID | D15 Need | 후보 솔루션 | 필요한 E&S 데이터 | PoC KPI | 우선도 |
|---|---|---|---|---|---|
| `FIT-ENS-D16-041` | OT asset visibility | 081/082 | SPAN/TAP·asset inventory | unknown asset rate | A |
| `FIT-ENS-D16-042` | risk knowledge graph | 083/086/092 | D01~D15 IDs | orphan link rate | A |
| `FIT-ENS-D16-043` | contract deadline | 087/088 | contracts·notices·entities | missed obligation recall | A |
| `FIT-ENS-D16-044` | regulation freshness | 090/091 | authoritative sources·effective date | stale answer rate | A |
| `FIT-ENS-D16-045` | project schedule risk | 093 | CPM·permit·EPC·JV | P50/P80 calibration | A |
| `FIT-ENS-D16-046` | PFE/tax evidence | 094/095 | BOM·supplier·ownership·invoice | unresolved evidence | A |
| `FIT-ENS-D16-047` | GenAI hallucination | 091/096 | prompts·sources·answers | unsupported claim rate | A |
| `FIT-ENS-D16-048` | crisis/incident orchestration | 089/092 | incidents·dependency·BCP | escalation latency | B |

---
