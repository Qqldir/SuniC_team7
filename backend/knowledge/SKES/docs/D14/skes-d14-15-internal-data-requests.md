---
id: skes-d14-15-internal-data-requests
title: Internal Data Requests
summary: "SK이노베이션 E&S 각 부서의 필수 데이터셋, 최소 보관 기간, 사용 용도를 정의한 데이터 요청 마스터. 규제, ESG, 재무, 운영 등 전 부문의 데이터 요구사항을 조회할 수 있다."
tags: [d14, policy, table, "xref:d17"]
keywords: [데이터 요청 ID, 부서별 필수 데이터셋, 규제 컴플라이언스, ETS/배출권거래, REC/신재생에너지, H2/수소, PPA/계약, MRV/측정보고검증, NYISO/ERCOT, 데이터 보관 기간]
related: [DR-ENS-D14-0001, DR-ENS-D14-0002, DR-ENS-D14-0003, DR-ENS-D14-0004, DR-ENS-D14-0005, DR-ENS-D14-0006, DR-ENS-D14-0007, DR-ENS-D14-0008, DR-ENS-D14-0009, DR-ENS-D14-0010, DR-ENS-D14-0011, DR-ENS-D14-0012, DR-ENS-D14-0013, DR-ENS-D14-0014, DR-ENS-D14-0015, DR-ENS-D14-0016, DR-ENS-D14-0017, DR-ENS-D14-0018, DR-ENS-D14-0019, DR-ENS-D14-0020, DR-ENS-D14-0021, DR-ENS-D14-0022, DR-ENS-D14-0023, DR-ENS-D14-0024]
priority: normal
domain: D14
section: 15
source: SK이노베이션E&S_D14_Policy_Regulation_Incentives_and_Compliance.md
breadcrumb: ""
tokens: 1006
updated: 2026-08-06
---

> SK이노베이션 E&S · D14 정책·규제·인센티브·컴플라이언스

# 15. Internal Data Requests

| DR ID | Owner | Required Dataset | Minimum History | Key | Use |
|---|---|---|---|---|---|
| `DR-ENS-D14-0001` | Legal | 법령/규제 적용 매트릭스 | current+5y | rule/entity | applicability |
| `DR-ENS-D14-0002` | Legal | permit register | project life | permit_id | critical path |
| `DR-ENS-D14-0003` | Legal | regulator correspondence | 3y | permit/case | deadlines |
| `DR-ENS-D14-0004` | ESG | plant verified emissions | 5y | site/year | ETS model |
| `DR-ENS-D14-0005` | Treasury | KAU allocation/bank/purchase | 5y | vintage/entity | carbon position |
| `DR-ENS-D14-0006` | Plant | fuel/output/heat-rate | 24m | unit/time | carbon dispatch |
| `DR-ENS-D14-0007` | Renewable | REC registry | 5y | asset/vintage | attribute QA |
| `DR-ENS-D14-0008` | Legal | PPA attribute clauses | all active | contract | double-claim control |
| `DR-ENS-D14-0009` | Jeonnam PMO | permit CPM | project life | permit/milestone | schedule |
| `DR-ENS-D14-0010` | Jeonnam ESG | community/fisheries commitments | project life | commitment | social license |
| `DR-ENS-D14-0011` | City gas | safety inspection/work orders | 36m | asset/date | risk score |
| `DR-ENS-D14-0012` | IGE | LH2 equipment inspection | 24m | equipment/time | compliance twin |
| `DR-ENS-D14-0013` | H2 Business | H2 production batch/MRV | 24m | batch | certification |
| `DR-ENS-D14-0014` | KCE Tax | project PIS/tax basis | all projects | project | 48E |
| `DR-ENS-D14-0015` | KCE Procurement | full BOM/vendor hierarchy | active builds | component/vendor | PFE |
| `DR-ENS-D14-0016` | KCE Procurement | country-of-origin evidence | active builds | component | domestic content |
| `DR-ENS-D14-0017` | KCE EPC | payroll/apprenticeship | construction | worker/week | PWA |
| `DR-ENS-D14-0018` | KCE Finance | tax-credit transfer contracts | all | project/credit | realized value |
| `DR-ENS-D14-0019` | KCE NY | NYISO bids/qualification | 24m | site/interval | rule mapping |
| `DR-ENS-D14-0020` | KCE TX | ERCOT registration/model | current | site/resource | validation |
| `DR-ENS-D14-0021` | KCE Dev | interconnection queue history | 5y | project/milestone | delay model |
| `DR-ENS-D14-0022` | KCE EHS | local permits/AHJ RFIs | project life | project/permit | precedent |
| `DR-ENS-D14-0023` | EverCharge | site PIS/permit/utility | 24m | site | incentive/energization |
| `DR-ENS-D14-0024` | Australia JV | facility operational-control map | current | facility/entity | Safeguard |
| `DR-ENS-D14-0025` | Australia Operator | production/emissions/baseline | 5y | facility/year | Safeguard model |
| `DR-ENS-D14-0026` | Australia EHS | environmental conditions | permit life | condition | monitoring |
| `DR-ENS-D14-0027` | CCS Team | storage titles/permit/MRV | project life | permit/site | gate readiness |
| `DR-ENS-D14-0028` | Quynh Lap PMO | VN/EN permit dossier | project life | permit/version | extraction |
| `DR-ENS-D14-0029` | Quynh Lap PMO | integrated CPM schedule | current baseline | activity | 2031 Monte Carlo |
| `DR-ENS-D14-0030` | Quynh Lap Legal | PPA/grid/investment docs | latest | agreement | bankability |
| `DR-ENS-D14-0031` | Compliance | sanctions/third-party DD | 3y | party | screening |
| `DR-ENS-D14-0032` | Compliance | public-official interaction log | 3y | party/event | ABAC |
| `DR-ENS-D14-0033` | Privacy | data processing inventory | current | dataset/purpose | privacy |
| `DR-ENS-D14-0034` | CISO | OT/IT/API access matrix | current | system/role | AI gateway |
| `DR-ENS-D14-0035` | Innovation | D17 idea register | current | seed/project | compliance scoring |

---
