---
id: skes-d16-12-priority-poc-portfolio
title: Priority PoC Portfolio
summary: "SK이노베이션 E&S의 디지털 트윈·센서 모니터링·설비 진단·수소·배터리 관련 21개 우선 PoC의 범위, 성공 KPI, 중단 기준, 검수 게이트를 정의하는 포트폴리오 표."
tags: [d16, ecosystem, table, "xref:d14"]
keywords: [PoC, 디지털 트윈, 센서 모니터링, 설비 진단, APM, BESS, 수소, CCS, KPI, 중단 기준]
related: [POC-ENS-D16-001, POC-ENS-D16-002, POC-ENS-D16-003, POC-ENS-D16-004, POC-ENS-D16-005, POC-ENS-D16-006, POC-ENS-D16-007, POC-ENS-D16-008, POC-ENS-D16-009, POC-ENS-D16-010, POC-ENS-D16-011, POC-ENS-D16-012, POC-ENS-D16-013, POC-ENS-D16-014, POC-ENS-D16-015, POC-ENS-D16-016, POC-ENS-D16-017, POC-ENS-D16-018, POC-ENS-D16-019, POC-ENS-D16-020, POC-ENS-D16-021, POC-ENS-D16-022, POC-ENS-D16-023, POC-ENS-D16-024]
priority: normal
domain: D16
section: 12
source: SK이노베이션E&S_D16_External_Technologies_Solutions_Companies_and_Startups.md
breadcrumb: ""
tokens: 1012
updated: 2026-08-06
---

> SK이노베이션 E&S · D16 외부 기술·솔루션·기업·스타트업

# 12. Priority PoC Portfolio

| PoC ID | 우선 PoC | 범위 | 성공 KPI | Stop Condition | Gate |
|---|---|---|---|---|---|
| `POC-ENS-D16-001` | Terminal Energy Digital Twin | 1 terminal process slice | baseline 대비 energy/unit 개선, constraint 0 | 물리제약 위반/모델 drift | Process Safety/MOC |
| `POC-ENS-D16-002` | GT Sensor Drift Monitor | 1 GT sensor family | false warning↓, failure precursor lead time | nuisance alert 악화 | Operations |
| `POC-ENS-D16-003` | Compressor APM | 1 equipment class | precision·lead time·avoided urgent WO | recall/precision 미달 | Maintenance |
| `POC-ENS-D16-004` | City Gas Network Truth | 1 service area | GIS-SCADA exception reduction | topology risk 증가 | Gas Safety |
| `POC-ENS-D16-005` | Offshore Weather Window | 1 wind stage | access success/plan stability | safety weather rule conflict | Marine/HSE |
| `POC-ENS-D16-006` | Wind Multi-OEM APM | selected turbines | actionable alert precision | warranty breach risk | OEM/HSE |
| `POC-ENS-D16-007` | Degradation-aware BESS Bid | 1 market/asset shadow | net margin after degradation | warranty/rule breach | Trading/Human |
| `POC-ENS-D16-008` | BESS Thermal Fusion | 1 site read-only | precursor lead time/false positive | safety alarm suppression | Fire/Safety |
| `POC-ENS-D16-009` | Charger Remote Fix | selected sites | remote fix↑, MTTR↓ | customer failure worsens | Customer/IT |
| `POC-ENS-D16-010` | Site Power Headroom Twin | 1 MUD/fleet site | overload 0, SLA 유지 | electrical limit breach | Electrical Safety |
| `POC-ENS-D16-011` | LH2 Barrier Health | selected barriers read-only | overdue proof-test/failed barrier detection | SIS dependency created | H2 Safety |
| `POC-ENS-D16-012` | LH2 Mass Balance | metering chain | unaccounted kg confidence band 축소 | meter uncertainty unbounded | Metrology/Safety |
| `POC-ENS-D16-013` | LH2 kWh/kg Twin | 1 train operating window | normalized kWh/kg improvement | safety envelope 접근 | Process Safety |
| `POC-ENS-D16-014` | CCS MMV Designer | 1 concept site | risk coverage/cost traceability | regulator requirement 누락 | Legal/Regulator |
| `POC-ENS-D16-015` | Emitter–Storage Matcher | CCS pipeline | firm/conditional status 정확도 | MOU를 firm으로 오분류 | Commercial |
| `POC-ENS-D16-016` | OT Asset Census | 1 isolated site | unknown asset↓, zero outage | active scan impact | CISO/OT |
| `POC-ENS-D16-017` | Contract Obligation Graph | 30~50 contracts | deadline/notice recall & precision | legal false-negative | Legal |
| `POC-ENS-D16-018` | Regulation Freshness AI | D14 source set | effective-date error≈0 | stale/uncited answer | Legal/Compliance |
| `POC-ENS-D16-019` | PFE Evidence Graph | 1 US BESS procurement | supplier evidence completeness | tax status hallucination | Tax/Legal |
| `POC-ENS-D16-020` | Project Monte Carlo | 1 development project | calibrated P50/P80 | garbage dependency graph | PMO/Finance |
| `POC-ENS-D16-021` | Source-Locked O&M Copilot | 1 equipment family | citation precision/answer usefulness | unsupported instruction | O&M/HSE |
| `POC-ENS-D16-022` | Alarm Rationalization | 1 plant subsystem | nuisance alarm↓, critical recall 유지 | critical miss 증가 | Operations |
| `POC-ENS-D16-023` | Risk Contagion Graph | LNG→power slice | dependency recall | false dependency overload | ERM |
| `POC-ENS-D16-024` | Common Vendor Benchmark | 2~3 tools same data | blind KPI comparison | data leakage | Procurement/CISO |
| `POC-ENS-D16-025` | AI Approval Router | 3 high-risk workflows | 100% auditable approval | bypass 가능 | Legal/CISO |

---
