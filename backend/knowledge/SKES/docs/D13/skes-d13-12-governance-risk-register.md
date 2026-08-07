---
id: skes-d13-12-governance-risk-register
title: Governance Risk Register
summary: "SK E&S 거버넌스 리스크 27건의 노출 영역, 선행 지표, 통제 방안을 정의한 리스크 매트릭스"
tags: [d13, contract, table, "xref:d17", "xref:d11", "xref:d12"]
keywords: [JV, 거버넌스리스크, 선행지표, PPA, 소유권, 보증, BESS, LNG]
related: [GRSK-ENS-D13-0001, GRSK-ENS-D13-0002, GRSK-ENS-D13-0003, GRSK-ENS-D13-0004, GRSK-ENS-D13-0005, GRSK-ENS-D13-0006, GRSK-ENS-D13-0007, GRSK-ENS-D13-0008, GRSK-ENS-D13-0009, GRSK-ENS-D13-0010, GRSK-ENS-D13-0011, GRSK-ENS-D13-0012, GRSK-ENS-D13-0013, GRSK-ENS-D13-0014, GRSK-ENS-D13-0015, GRSK-ENS-D13-0016, GRSK-ENS-D13-0017, GRSK-ENS-D13-0018, GRSK-ENS-D13-0019, GRSK-ENS-D13-0020, GRSK-ENS-D13-0021, GRSK-ENS-D13-0022, GRSK-ENS-D13-0023, GRSK-ENS-D13-0024]
priority: normal
domain: D13
section: 12
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 1181
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# 12. Governance Risk Register

| Risk ID | Risk | 주요 노출 | Leading indicator | Control / D17 hook |
|---|---|---|---|---|
| `GRSK-ENS-D13-0001` | legal-party mismatch | all | invoice/contract/entity name mismatch | entity-resolution gate |
| `GRSK-ENS-D13-0002` | stale ownership | Hyverse/KCE/JV | source effective-date lag | ownership lineage |
| `GRSK-ENS-D13-0003` | JV reserved-matter breach | JV | approval missing | approval matrix |
| `GRSK-ENS-D13-0004` | partner veto/deadlock | JV | repeated deferred decisions | escalation workflow |
| `GRSK-ENS-D13-0005` | capital-call surprise | Barossa/JV | forecast vs call variance | cash-call predictor |
| `GRSK-ENS-D13-0006` | sponsor-support leakage | PF/JV | guarantee exposure growth | support ledger |
| `GRSK-ENS-D13-0007` | guarantee succession gap | merger/LTA | old guarantor name | succession audit |
| `GRSK-ENS-D13-0008` | use-or-pay underutilization | Freeport/Boryeong | right utilization | right optimizer |
| `GRSK-ENS-D13-0009` | lifting imbalance | Barossa | under/overlift | entitlement reconciler |
| `GRSK-ENS-D13-0010` | terminal-slot miss | LNG | slot change/demurrage | cargo-slot twin |
| `GRSK-ENS-D13-0011` | contract price leakage | LNG/PPA | unexplained true-up | clause-to-invoice reconcile |
| `GRSK-ENS-D13-0012` | PPA shortfall | renewables | meter vs obligation | PPA obligation monitor |
| `GRSK-ENS-D13-0013` | REC/evidence failure | PPA | unmatched MWh | evidence graph |
| `GRSK-ENS-D13-0014` | lender-consent breach | wind/BESS | restricted action | covenant workflow |
| `GRSK-ENS-D13-0015` | vendor warranty loss | KCE | warranty claim rejected | warranty-right ledger |
| `GRSK-ENS-D13-0016` | BESS vendor concentration | KCE | single-vendor MW share | contract concentration map |
| `GRSK-ENS-D13-0017` | LTSA performance gap | KCE | SLA/parts delay | SLA monitor |
| `GRSK-ENS-D13-0018` | site-host termination | EverCharge | churn/default | transition plan |
| `GRSK-ENS-D13-0019` | charging data-right conflict | EverCharge | consent/access mismatch | data-right registry |
| `GRSK-ENS-D13-0020` | technology-right loss after exit | Hyverse | license/supply change | survival-clause review |
| `GRSK-ENS-D13-0021` | ownership conflict | Hyverse | SEC vs registry mismatch | legal registry resolver |
| `GRSK-ENS-D13-0022` | MOU treated as firm demand | hydrogen | backlog includes MOU | commitment classifier |
| `GRSK-ENS-D13-0023` | H2 partner underdelivery | mobility | vehicle/site delay | ecosystem milestone graph |
| `GRSK-ENS-D13-0024` | subsidy-party mismatch | H2/wind | recipient vs operator | funding-right map |
| `GRSK-ENS-D13-0025` | Quynh Lap consortium deadlock | Vietnam | milestone approval delay | governance workflow |
| `GRSK-ENS-D13-0026` | concession/permit CP failure | Vietnam | CP approaching expiry | CP tracker |
| `GRSK-ENS-D13-0027` | EPC data handover omission | Vietnam | contract lacks data schedule | digital clause library |
| `GRSK-ENS-D13-0028` | cross-border data breach | global | transfer without basis | jurisdiction gate |
| `GRSK-ENS-D13-0029` | anti-bribery/sanction exposure | global | DD red flag | counterparty screening |
| `GRSK-ENS-D13-0030` | change-of-control consent miss | M&A/JV | transfer before consent | CoC checklist |
| `GRSK-ENS-D13-0031` | notice/time-bar loss | claims | late notice | deadline extractor |
| `GRSK-ENS-D13-0032` | amendment not propagated | all | operations uses old version | semantic diff |
| `GRSK-ENS-D13-0033` | side-letter invisibility | all | exception outside CLM | version lineage |
| `GRSK-ENS-D13-0034` | AI hallucinated obligation | all | clause without source | evidence-required RAG |
| `GRSK-ENS-D13-0035` | confidential data leakage | all | unauthorized prompt/export | redaction/access control |

## 12.1 Risk propagation examples

```text
Barossa operator outage
→ production/lifting change
→ partner entitlement mismatch
→ cargo/terminal reschedule
→ TUA/transport/demurrage economics
→ D11 margin
→ D12 cash recovery
```

```text
Quynh Lap permit or PPA delay
→ financing CP delay
→ EPC NTP delay
→ schedule/cost shift
→ LNG supply timing mismatch
→ terminal/power COD delay
→ D12 cost-to-complete and D17 opportunity reprioritization
```

---
