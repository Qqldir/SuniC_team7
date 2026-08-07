---
id: skes-d09-15-customer-and-contract-risk-register
title: Customer and Contract Risk Register
summary: "E&S 사업의 고객 신용, 계약 이행, 발전 수급, 청구 결산, 안전, 규제 등 28개 주요 위험 항목을 노출도·선행지표·관리방안으로 매칭한 위험 레지스터표."
tags: [d09, customer, table]
keywords: [PPA, offtaker, 신용리스크, 청구오류, 재생에너지, BESS, 수소충전소, 정산누수, 고객집중도, 예측모형]
related: [RSK-ENS-D09-001, RSK-ENS-D09-002, RSK-ENS-D09-003, RSK-ENS-D09-004, RSK-ENS-D09-005, RSK-ENS-D09-006, RSK-ENS-D09-007, RSK-ENS-D09-008, RSK-ENS-D09-009, RSK-ENS-D09-010, RSK-ENS-D09-011, RSK-ENS-D09-012, RSK-ENS-D09-013, RSK-ENS-D09-014, RSK-ENS-D09-015, RSK-ENS-D09-016, RSK-ENS-D09-017, RSK-ENS-D09-018, RSK-ENS-D09-019, RSK-ENS-D09-020, RSK-ENS-D09-021, RSK-ENS-D09-022, RSK-ENS-D09-023, RSK-ENS-D09-024]
priority: normal
domain: D09
section: 15
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 892
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 15. Customer and Contract Risk Register

| Risk ID | Risk | Exposure | Leading indicator | Control/OI |
|---|---|---|---|---|
| `RSK-ENS-D09-001` | PPA offtaker default | 장기 현금흐름 | rating·CDS·연체 | credit early warning |
| `RSK-ENS-D09-002` | PPA load decline | excess generation | load variance | portfolio rematching |
| `RSK-ENS-D09-003` | renewable COD delay | supply shortfall | EPC milestone | milestone risk model |
| `RSK-ENS-D09-004` | generation shape mismatch | imbalance cost | hourly mismatch | probabilistic matching |
| `RSK-ENS-D09-005` | REC/evidence defect | RE100 claim risk | missing lineage | evidence graph |
| `RSK-ENS-D09-006` | city-gas weather error | procurement imbalance | HDD error | ensemble forecast |
| `RSK-ENS-D09-007` | industrial customer shutdown | volume loss | production signal | account alert |
| `RSK-ENS-D09-008` | billing error | refund·trust | exception spike | bill anomaly detection |
| `RSK-ENS-D09-009` | meter failure | estimated billing | stale/flat read | meter health model |
| `RSK-ENS-D09-010` | emergency misclassification | safety | symptom mismatch | triage assist |
| `RSK-ENS-D09-011` | privacy leakage | regulatory/reputation | unusual access | data loss prevention |
| `RSK-ENS-D09-012` | unfair collection model | customer harm | segment disparity | human review/fairness |
| `RSK-ENS-D09-013` | heat forecast miss | SLA·fuel cost | temp/load error | CHP co-optimization |
| `RSK-ENS-D09-014` | KCE bid error | lost revenue/penalty | validation fail | pre-submit guardrail |
| `RSK-ENS-D09-015` | BESS non-performance | market penalty | SOC/availability | dispatch feasibility |
| `RSK-ENS-D09-016` | rule change | model invalidity | tariff/rule release | rule change monitor |
| `RSK-ENS-D09-017` | settlement leakage | revenue loss | bid-meter mismatch | automated reconciliation |
| `RSK-ENS-D09-018` | EverCharge session failure | churn | error code | predictive support |
| `RSK-ENS-D09-019` | fleet departure undercharged | operations failure | SOC shortfall | route-aware scheduler |
| `RSK-ENS-D09-020` | payment exception | leakage | orphan session | session-to-payment match |
| `RSK-ENS-D09-021` | site capacity saturation | poor UX | queue·peak | expansion trigger |
| `RSK-ENS-D09-022` | hydrogen station stockout | bus disruption | inventory/runout | logistics control tower |
| `RSK-ENS-D09-023` | hydrogen demand overestimate | stranded capacity | vehicle delay | stage-gated forecast |
| `RSK-ENS-D09-024` | trailer delay | supply failure | ETA/weather | dynamic routing |
| `RSK-ENS-D09-025` | MOU counted as backlog | forecast bias | status mismatch | commitment taxonomy |
| `RSK-ENS-D09-026` | customer concentration | earnings volatility | top-N share | portfolio limits |
| `RSK-ENS-D09-027` | internal/external mixing | reporting error | related-party flag | entity resolution |
| `RSK-ENS-D09-028` | contract clause loss | margin erosion | obligation breach | clause-to-KPI engine |
| `RSK-ENS-D09-029` | data-right restriction | PoC failure | missing consent | rights-first design |
| `RSK-ENS-D09-030` | AI automated adverse decision | legal/ethical | no human approval | approval workflow |

---
