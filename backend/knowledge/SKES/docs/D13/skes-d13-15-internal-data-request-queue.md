---
id: skes-d13-15-internal-data-request-queue
title: Internal Data Request Queue
summary: SK이노베이션 E&S D13 JV·계약·거버넌스 데이터 관리를 위해 우선순위별로 정의된 34개 데이터 수집 요청 큐.
tags: [d13, contract, table, "xref:d17"]
keywords: [데이터 수집, JV 계약, 거버넌스, 우선순위, 법인 정보, 의무 모니터링, 계약 추적, SK이노베이션]
related: [DR-ENS-D13-0001, DR-ENS-D13-0002, DR-ENS-D13-0003, DR-ENS-D13-0004, DR-ENS-D13-0005, DR-ENS-D13-0006, DR-ENS-D13-0007, DR-ENS-D13-0008, DR-ENS-D13-0009, DR-ENS-D13-0010, DR-ENS-D13-0011, DR-ENS-D13-0012, DR-ENS-D13-0013, DR-ENS-D13-0014, DR-ENS-D13-0015, DR-ENS-D13-0016, DR-ENS-D13-0017, DR-ENS-D13-0018, DR-ENS-D13-0019, DR-ENS-D13-0020, DR-ENS-D13-0021, DR-ENS-D13-0022, DR-ENS-D13-0023, DR-ENS-D13-0024]
priority: normal
domain: D13
section: 15
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 855
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# 15. Internal Data Request Queue

| ID | 데이터 | Grain | 목적 | Priority |
|---|---|---|---|---|
| `DR-ENS-D13-0001` | legal entity master | entity/effective date | party resolution | P0 |
| `DR-ENS-D13-0002` | subsidiary/JV cap table | entity/date | ownership | P0 |
| `DR-ENS-D13-0003` | corporate registry extracts | entity/version | legal verification | P0 |
| `DR-ENS-D13-0004` | board/committee delegation | body/version | governance | P0 |
| `DR-ENS-D13-0005` | shareholder/JV agreements | agreement/version | reserved matters | P0 |
| `DR-ENS-D13-0006` | contract master index | contract/version | CLM scope | P0 |
| `DR-ENS-D13-0007` | amendments/side letters | contract/version | lineage | P0 |
| `DR-ENS-D13-0008` | obligation register | clause/event | monitoring | P0 |
| `DR-ENS-D13-0009` | guarantees/support letters | support/version | exposure | P0 |
| `DR-ENS-D13-0010` | claim/dispute notices | event | time bar/learning | P0 |
| `DR-ENS-D13-0011` | merger succession notices | contract | successor check | P0 |
| `DR-ENS-D13-0012` | Barossa JOA | clause/version | JV governance | P0 |
| `DR-ENS-D13-0013` | Barossa lifting agreement | cargo/entitlement | LNG allocation | P0 |
| `DR-ENS-D13-0014` | Darwin processing agreements | right/version | upstream-downstream | P0 |
| `DR-ENS-D13-0015` | Freeport LTA | clause/version | right/fee/outage | P0 |
| `DR-ENS-D13-0016` | Freeport transport agreements | nomination/day | feedgas | P1 |
| `DR-ENS-D13-0017` | Boryeong sale agreement | version | surviving liability | P0 |
| `DR-ENS-D13-0018` | Boryeong TUA | clause/slot | right economics | P0 |
| `DR-ENS-D13-0019` | Jeonnam SHA | clause/version | JV governance | P0 |
| `DR-ENS-D13-0020` | Jeonnam PF covenants | facility/clause | lender consent | P0 |
| `DR-ENS-D13-0021` | PPA contracts | agreement/version | obligation/price | P0 |
| `DR-ENS-D13-0022` | REC/meter evidence | MWh/certificate | performance | P0 |
| `DR-ENS-D13-0023` | KCE SPV/legal map | project/entity | contract stack | P0 |
| `DR-ENS-D13-0024` | KCE vendor/EPC/LTSA | contract/site | warranty | P0 |
| `DR-ENS-D13-0025` | KCE market agreements | account/site | ISO obligations | P0 |
| `DR-ENS-D13-0026` | EverCharge site-host contracts | site/version | site/data rights | P0 |
| `DR-ENS-D13-0027` | EverCharge privacy/DPA | jurisdiction/version | data rights | P0 |
| `DR-ENS-D13-0028` | Hyverse shareholder ledger | holder/date | current ownership | P0 |
| `DR-ENS-D13-0029` | Hyverse transfer SPA | version | exit/survival | P0 |
| `DR-ENS-D13-0030` | Hyverse tech/license/supply | contract/version | continuity | P0 |
| `DR-ENS-D13-0031` | H2 MOU/firm contracts | project/version | commitment state | P0 |
| `DR-ENS-D13-0032` | Quynh Lap consortium/JV docs | agreement/version | governance | P0 |
| `DR-ENS-D13-0033` | Quynh Lap permit/CP register | CP/date | schedule | P0 |
| `DR-ENS-D13-0034` | Quynh Lap EPC data schedule | deliverable/tag | digital handover | P0 |
| `DR-ENS-D13-0035` | enterprise data-right catalog | dataset/contract | D17 feasibility | P0 |

---
