---
id: skes-d15-13-control-barrier-register
title: Control & Barrier Register
summary: "에너지 설비 운영 중 LNG, 가스, BESS, 수소 등 주요 위험을 관리하는 통제항목 26개를 정의하고 각 통제의 유형, 증거, 대상 리스크를 매칭한 통제 등록부 표이다."
tags: [d15, risk, schema, table]
keywords: [리스크 통제, 위험 관리, 예방통제, 탐지통제, 회복탄력성, LNG 공급, BESS, 가스안전, 수소, HAZOP]
related: [CTRL-ENS-D15-001, CTRL-ENS-D15-002, CTRL-ENS-D15-003, CTRL-ENS-D15-004, CTRL-ENS-D15-005, CTRL-ENS-D15-006, CTRL-ENS-D15-007, CTRL-ENS-D15-008, CTRL-ENS-D15-009, CTRL-ENS-D15-010, CTRL-ENS-D15-011, CTRL-ENS-D15-012, CTRL-ENS-D15-013, CTRL-ENS-D15-014, CTRL-ENS-D15-015, CTRL-ENS-D15-016, CTRL-ENS-D15-017, CTRL-ENS-D15-018, CTRL-ENS-D15-019, CTRL-ENS-D15-020, CTRL-ENS-D15-021, CTRL-ENS-D15-022, CTRL-ENS-D15-023, CTRL-ENS-D15-024]
priority: normal
domain: D15
section: 13
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 1639
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 13. Control & Barrier Register

## 13.1 Control Design Rule

통제는 `문서 존재`가 아니라 **설계–실행–증빙–시험–예외–복구**의 연속체로 관리한다.

```text
Control Design
→ Owner & Frequency
→ Data / Sensor / Procedure
→ Execution Evidence
→ Exception
→ Independent Test
→ Failure / Override
→ Corrective Action
→ Retest
```

## 13.2 Control Register

| Control ID | Type | Control | Primary Risk | Evidence |
|---|---|---|---|---|
| `CTRL-ENS-D15-001` | Preventive | LNG source/route diversification rule | 001~003 | contract·cargo portfolio |
| `CTRL-ENS-D15-002` | Detective | AIS/ETA disruption alert | 001·003 | AIS·port notice |
| `CTRL-ENS-D15-003` | Preventive | minimum fuel/inventory buffer | 001·004 | inventory plan |
| `CTRL-ENS-D15-004` | Corrective | alternate cargo/route playbook | 001·003 | executed scenario/decision log |
| `CTRL-ENS-D15-005` | Preventive | physical-vs-hedge position reconciliation | 002 | position ledger |
| `CTRL-ENS-D15-006` | Detective | terminal tank/slot constraint forecast | 003 | tank·schedule model |
| `CTRL-ENS-D15-007` | Preventive | critical equipment maintenance strategy | 004 | CMMS/inspection |
| `CTRL-ENS-D15-008` | Detective | turbine/rotating equipment anomaly detection | 004 | historian/vibration |
| `CTRL-ENS-D15-009` | Corrective | forced-outage rapid diagnostic workflow | 004 | incident timeline |
| `CTRL-ENS-D15-010` | Recovery | spare/field-service mobilization | 004·024 | spare inventory·LTSA |
| `CTRL-ENS-D15-011` | Preventive | gas network integrity/inspection | 006 | inspection record |
| `CTRL-ENS-D15-012` | Detective | pressure/flow/gas alarm monitoring | 006 | SCADA/alarm log |
| `CTRL-ENS-D15-013` | Recovery | emergency isolation/dispatch | 006 | drill/incident log |
| `CTRL-ENS-D15-014` | Preventive | renewable preventive maintenance | 008 | work orders |
| `CTRL-ENS-D15-015` | Detective | yield/availability normalization | 008·009 | SCADA/weather |
| `CTRL-ENS-D15-016` | Corrective | curtailment-aware dispatch/contract action | 009·010 | market/PPA log |
| `CTRL-ENS-D15-017` | Preventive | PPA attribute ownership ledger | 010·020 | contract/REC evidence |
| `CTRL-ENS-D15-018` | Preventive | BESS operating envelope | 011 | BMS/EMS configuration |
| `CTRL-ENS-D15-019` | Detective | BESS thermal/voltage anomaly monitor | 011 | BMS alarms |
| `CTRL-ENS-D15-020` | Corrective | BESS safe-state/ESD procedure | 011 | ESD test/incident |
| `CTRL-ENS-D15-021` | Preventive | degradation-aware bid constraint | 011·012 | SOH/economic model |
| `CTRL-ENS-D15-022` | Detective | optimizer drift/counterfactual validation | 012 | model monitoring |
| `CTRL-ENS-D15-023` | Preventive | market-rule version gate | 012·020 | rule/change log |
| `CTRL-ENS-D15-024` | Recovery | charger local/edge fallback | 013·021 | failover drill |
| `CTRL-ENS-D15-025` | Preventive | LH2 HAZOP/LOPA/MOC controlled workflow | 014 | approved studies/MOC |
| `CTRL-ENS-D15-026` | Detective | LH2 gas/pressure/temp/BOG monitoring | 014 | sensor historian |
| `CTRL-ENS-D15-027` | Preventive | safety-critical proof-test schedule | 014 | PSV/ESD/detector tests |
| `CTRL-ENS-D15-028` | Corrective | LH2 leak/isolation emergency response | 014 | drill/response log |
| `CTRL-ENS-D15-029` | Preventive | H2 demand-to-production gate | 015 | firm order·sold kg |
| `CTRL-ENS-D15-030` | Detective | H2 plant-station-vehicle network balance | 015 | mass balance/inventory |
| `CTRL-ENS-D15-031` | Preventive | CCS stage/FID gating | 016·017 | FID/permit/offtake |
| `CTRL-ENS-D15-032` | Detective | CCS digital MRV lineage | 016·020 | meter/sampling/source |
| `CTRL-ENS-D15-033` | Preventive | project critical-path dependency register | 017·018 | schedule/permit |
| `CTRL-ENS-D15-034` | Detective | EAC/contingency/cash-call early warning | 018 | project controls |
| `CTRL-ENS-D15-035` | Preventive | CLM obligation/deadline register | 019 | signed contract/source |
| `CTRL-ENS-D15-036` | Detective | counterparty/covenant monitoring | 018·019·025 | rating·financial·covenant |
| `CTRL-ENS-D15-037` | Preventive | rule applicability + effective-date gate | 020 | authoritative source |
| `CTRL-ENS-D15-038` | Preventive | PFE/tax evidence graph | 020·024 | supplier/tax evidence |
| `CTRL-ENS-D15-039` | Preventive | OT asset inventory/network segmentation | 021 | asset/network map |
| `CTRL-ENS-D15-040` | Preventive | MFA/JIT vendor remote access | 021 | PAM/session log |
| `CTRL-ENS-D15-041` | Detective | OT configuration/vulnerability drift | 021 | scan/config baseline |
| `CTRL-ENS-D15-042` | Recovery | immutable backup + restore drill | 021·022 | restore evidence |
| `CTRL-ENS-D15-043` | Preventive | source-locked AI retrieval | 022 | source hash/version |
| `CTRL-ENS-D15-044` | Preventive | human approval for safety/legal/trading | 020~022 | approval log |
| `CTRL-ENS-D15-045` | Detective | data lineage/unit/state validation | 022 | DQ exception log |
| `CTRL-ENS-D15-046` | Preventive | supplier concentration/spare gate | 024 | vendor/spare map |
| `CTRL-ENS-D15-047` | Detective | sanctions/ABAC screening refresh | 026 | screening evidence |
| `CTRL-ENS-D15-048` | Recovery | insurance notice/claim protocol | 029 | policy/claim log |
| `CTRL-ENS-D15-049` | Recovery | cross-business crisis command | 030 | decision log |
| `CTRL-ENS-D15-050` | Detective | resilience exercise/lessons closure | 023·030 | drill/action closure |

## 13.3 Barrier Health

Safety-critical barrier는 `GREEN/AMBER/RED`의 단순 상태만 저장하지 않는다.

```yaml
barrier_health:
  design_basis: required
  last_test_at: required
  test_result: PASS|PARTIAL|FAIL|NOT_TESTED
  impairment_start: datetime|null
  compensating_measure: string|null
  owner: required
  next_test_due: date
  override_authority: role
  evidence_uri: required
```

---
