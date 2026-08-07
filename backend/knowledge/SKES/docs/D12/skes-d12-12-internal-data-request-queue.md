---
id: skes-d12-12-internal-data-request-queue
title: Internal Data Request Queue
summary: "SK이노베이션 E&S의 투자·자금 관리에 필요한 35건의 데이터 요청을 ID, 데이터명, 수집 기간, 용도, 우선순위별로 정리한 마스터 테이블."
tags: [d12, capex, table]
keywords: [CAPEX, 투자관리, 채무, 현금흐름, SPV, 자금조달, 허들율, 데이터 카탈로그, 우선순위, 사후검토]
related: [DR-ENS-D12-0001, DR-ENS-D12-0002, DR-ENS-D12-0003, DR-ENS-D12-0004, DR-ENS-D12-0005, DR-ENS-D12-0006, DR-ENS-D12-0007, DR-ENS-D12-0008, DR-ENS-D12-0009, DR-ENS-D12-0010, DR-ENS-D12-0011, DR-ENS-D12-0012, DR-ENS-D12-0013, DR-ENS-D12-0014, DR-ENS-D12-0015, DR-ENS-D12-0016, DR-ENS-D12-0017, DR-ENS-D12-0018, DR-ENS-D12-0019, DR-ENS-D12-0020, DR-ENS-D12-0021, DR-ENS-D12-0022, DR-ENS-D12-0023, DR-ENS-D12-0024]
priority: normal
domain: D12
section: 12
source: SK이노베이션E&S_D12_CAPEX_Investment_Funding_and_Financial_Structure.md
breadcrumb: ""
tokens: 806
updated: 2026-08-06
---

> SK이노베이션 E&S · D12 CAPEX·투자·자금조달

# 12. Internal Data Request Queue

| ID | 데이터 | Grain | 기간 | 목적 | Priority |
|---|---|---|---|---|---|
| `DR-ENS-D12-0001` | Investment committee cases | case/version | 5y | 승인논리 학습 | P0 |
| `DR-ENS-D12-0002` | Legal entity/SPV master | entity | current | scope | P0 |
| `DR-ENS-D12-0003` | Asset-right ownership master | asset/right | current | 소유권 통제 | P0 |
| `DR-ENS-D12-0004` | CAPEX budget baseline | WBS/month | 5y | budget | P0 |
| `DR-ENS-D12-0005` | PO/commitment | contract/PO | 5y | commitment | P0 |
| `DR-ENS-D12-0006` | invoice/AP/payment | invoice | 5y | cash | P0 |
| `DR-ENS-D12-0007` | Change orders | CO | 5y | overrun | P0 |
| `DR-ENS-D12-0008` | physical progress | WBS/week | projects | EAC | P0 |
| `DR-ENS-D12-0009` | project schedule | activity/week | projects | delay | P0 |
| `DR-ENS-D12-0010` | debt facilities | facility | life | debt | P0 |
| `DR-ENS-D12-0011` | drawdown/outstanding | facility/day | life | liquidity | P0 |
| `DR-ENS-D12-0012` | covenant definitions | clause | current | compliance | P0 |
| `DR-ENS-D12-0013` | guarantee/support | obligation | current | contingent risk | P0 |
| `DR-ENS-D12-0014` | equity calls | JV/call | life | sponsor cash | P0 |
| `DR-ENS-D12-0015` | grant/subsidy | program | life | support | P0 |
| `DR-ENS-D12-0016` | tax credits | project/taxyear | life | ITC | P0 |
| `DR-ENS-D12-0017` | hedge book | instrument/day | 3y | FX/rate | P1 |
| `DR-ENS-D12-0018` | insurance | asset/policy | current | risk | P1 |
| `DR-ENS-D12-0019` | impairment tests | CGU/test | 5y | trigger | P0 |
| `DR-ENS-D12-0020` | disposal/exit cases | asset/deal | 5y | option learning | P1 |
| `DR-ENS-D12-0021` | Barossa cash calls | JV/month | project life | LNG | P0 |
| `DR-ENS-D12-0022` | Barossa cargo cash | cargo | 24m | recovery | P0 |
| `DR-ENS-D12-0023` | Boryeong TUA | slot/month | 24m | right value | P0 |
| `DR-ENS-D12-0024` | Freeport right utilization | cargo/month | 24m | right value | P0 |
| `DR-ENS-D12-0025` | power major maintenance | asset/event | 5y | CAPEX priority | P0 |
| `DR-ENS-D12-0026` | Jeonnam PF waterfall | SPV/month | life | PF twin | P0 |
| `DR-ENS-D12-0027` | KCE project debt | site/month | life | BESS PF | P0 |
| `DR-ENS-D12-0028` | KCE ITC ledger | project/taxyear | life | credit cash | P0 |
| `DR-ENS-D12-0029` | KCE BMS/market cash | site/interval | 24m | DSCR | P0 |
| `DR-ENS-D12-0030` | IGE PF waterfall | month | life | H2 | P0 |
| `DR-ENS-D12-0031` | IGE production/sales | kg/day | 24m | H2 cash | P0 |
| `DR-ENS-D12-0032` | Hyverse station economics | station/day | 24m | right-size | P0 |
| `DR-ENS-D12-0033` | CCS development spend | workpackage/month | life | stage gate | P1 |
| `DR-ENS-D12-0034` | hurdle rates | policy/version | 5y | comparable cases | P0 |
| `DR-ENS-D12-0035` | post-investment reviews | case | 5y | learning | P0 |

---
