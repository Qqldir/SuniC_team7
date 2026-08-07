---
id: skes-d14-13-o-i-seed-master
title: O/I Seed Master
summary: "SK E&S의 규제·컴플라이언스·에너지 분야 AI 자동화 프로젝트 22개의 목표, 주요 KPI, 필요 데이터, 우선순위를 정리한 포트폴리오 현황표."
tags: [d14, policy, oi-seed, table, "xref:d17"]
keywords: [규제자동화, 컴플라이언스, 탄소관리, 인허가, KPI, 우선순위, 에너지, 디지털트윈, ESG, SEED]
related: [SEED-ENS-D14-0001, SEED-ENS-D14-0002, SEED-ENS-D14-0003, SEED-ENS-D14-0004, SEED-ENS-D14-0005, SEED-ENS-D14-0006, SEED-ENS-D14-0007, SEED-ENS-D14-0008, SEED-ENS-D14-0009, SEED-ENS-D14-0010, SEED-ENS-D14-0011, SEED-ENS-D14-0012, SEED-ENS-D14-0013, SEED-ENS-D14-0014, SEED-ENS-D14-0015, SEED-ENS-D14-0016, SEED-ENS-D14-0017, SEED-ENS-D14-0018, SEED-ENS-D14-0019, SEED-ENS-D14-0020, SEED-ENS-D14-0021, SEED-ENS-D14-0022, SEED-ENS-D14-0023, SEED-ENS-D14-0024]
priority: normal
domain: D14
section: 13
source: SK이노베이션E&S_D14_Policy_Regulation_Incentives_and_Compliance.md
breadcrumb: ""
tokens: 2168
updated: 2026-08-06
---

> SK이노베이션 E&S · D14 정책·규제·인센티브·컴플라이언스

# 13. O/I Seed Master

| SEED ID | O/I Idea | Target | Primary KPI | Required Data | Compliance Gate | Priority |
|---|---|---|---|---|---|---|
| `SEED-ENS-D14-0001` | temporal regulation knowledge graph | 전사 | stale-rule rate | law/version/effective date | Legal approval | P0 |
| `SEED-ENS-D14-0002` | law-diff impact mapper | 전사 | impact-review lead time | old/new text, asset map | source fidelity | P0 |
| `SEED-ENS-D14-0003` | regulatory applicability engine | 전사 | false applicability | entity/asset/rule | Legal sign-off | P0 |
| `SEED-ENS-D14-0004` | permit critical-path graph | Project | permit delay days | permits/CPM/dependency | PMO owner | P0 |
| `SEED-ENS-D14-0005` | regulator deadline copilot | Legal/EHS | missed deadlines | filings/notices/calendar | human submit | P1 |
| `SEED-ENS-D14-0006` | compliance evidence vault | 전사 | evidence retrieval time | certificates/logs | access control | P0 |
| `SEED-ENS-D14-0007` | K-ETS allocation-position twin | 발전 | KAU forecast error | emissions/allocation/bank | verified data | P0 |
| `SEED-ENS-D14-0008` | carbon-adjusted dispatch optimizer | 발전 | KRW/MWh margin | heat rate/SMP/KAU | market rules | P0 |
| `SEED-ENS-D14-0009` | K-MSR auction watcher | Treasury | procurement cost | notices/auction/position | trading limits | P1 |
| `SEED-ENS-D14-0010` | plant emissions anomaly detector | 발전 | tCO2 variance | CEMS/fuel/output | MRV method | P0 |
| `SEED-ENS-D14-0011` | verifier pre-check agent | ESG | findings count | emission package | auditor independence | P1 |
| `SEED-ENS-D14-0012` | 2026~30 carbon budget simulator | FP&A | EBITDA forecast | KAU scenarios/output | Finance review | P0 |
| `SEED-ENS-D14-0013` | PPA attribute ownership validator | Renewables | double claims | CLM/REC/meter | contract rights | P0 |
| `SEED-ENS-D14-0014` | REC issuance reconciliation | Renewables | missing REC | meter/registry | registry authority | P1 |
| `SEED-ENS-D14-0015` | offshore permit dependency AI | Jeonnam | schedule float | permits/conditions/CPM | official status | P0 |
| `SEED-ENS-D14-0016` | fisheries/community commitment tracker | Jeonnam | overdue commitment | meetings/contracts/payments | privacy/ABAC | P1 |
| `SEED-ENS-D14-0017` | marine condition monitoring twin | offshore wind | breach lead time | sensor/permit limits | regulator method | P1 |
| `SEED-ENS-D14-0018` | distributed-energy zone opportunity mapper | Ensolve | qualified sites | load/grid/zone rules | license boundary | P1 |
| `SEED-ENS-D14-0019` | city-gas safety inspection risk score | City gas | leak/overdue rate | CMMS/inspection | safety standard | P0 |
| `SEED-ENS-D14-0020` | gas supply compliance dashboard | City gas | outage/pressure | SCADA/customer | critical infra security | P1 |
| `SEED-ENS-D14-0021` | LH2 inspection digital twin | Incheon | unplanned stop | equipment/inspection | H2 safety | P0 |
| `SEED-ENS-D14-0022` | clean-H2 certification MRV engine | Hydrogen | certified kg | feedstock/power/emissions | certification rule | P0 |
| `SEED-ENS-D14-0023` | H2 law Sep-2026 readiness agent | Hydrogen | gaps closed | rule/control/process | Legal | P0 |
| `SEED-ENS-D14-0024` | H2 auction-state validator | Strategy | false demand=0 | KPX notices/contracts | authoritative source | P1 |
| `SEED-ENS-D14-0025` | 48E eligibility calculator | KCE | tax forecast error | PIS/basis/PWA | Tax counsel | P0 |
| `SEED-ENS-D14-0026` | PFE supplier graph | KCE | unverified spend | BOM/vendor ownership | tax/legal | P0 |
| `SEED-ENS-D14-0027` | domestic-content BOM tracer | KCE | bonus confidence | BOM/origin/cost | certification | P0 |
| `SEED-ENS-D14-0028` | PWA payroll compliance agent | KCE | payroll exceptions | payroll/apprentice | labor/tax | P1 |
| `SEED-ENS-D14-0029` | tax-basis invoice classifier | KCE | basis adjustment | invoices/EPC WBS | Tax approval | P1 |
| `SEED-ENS-D14-0030` | tax-credit transfer data room QA | KCE | buyer DD time | credit/docs | confidentiality | P1 |
| `SEED-ENS-D14-0031` | NYISO tariff diff-to-bid mapper | KCE NY | rule response time | tariff/bid config | market compliance | P0 |
| `SEED-ENS-D14-0032` | NY capacity accreditation forecaster | KCE NY | ICAP forecast | SOH/duration/rules | tariff version | P1 |
| `SEED-ENS-D14-0033` | NY ISC contract optimizer | KCE NY | risk-adjusted revenue | solicitation/market | award rules | P1 |
| `SEED-ENS-D14-0034` | ERCOT protocol change agent | KCE TX | config errors | NPRR/protocol/config | ops approval | P0 |
| `SEED-ENS-D14-0035` | ERCOT registration data validator | KCE TX | rejected fields | model/telemetry | ERCOT schema | P0 |
| `SEED-ENS-D14-0036` | interconnection milestone predictor | KCE | COD variance | queue/study/deposit | ISO confidentiality | P0 |
| `SEED-ENS-D14-0037` | BESS AHJ permit precedent engine | KCE | permit cycle time | local code/RFIs | engineer seal | P1 |
| `SEED-ENS-D14-0038` | BESS safety evidence graph | KCE | audit prep time | test/cert/BMS | safety code | P0 |
| `SEED-ENS-D14-0039` | incentive-aware project scheduler | KCE | lost-credit risk | CPM/PIS/tax rules | Tax/PMO | P0 |
| `SEED-ENS-D14-0040` | EverCharge date-aware incentive calculator | EV | quote error | site/PIS/program | tax disclaimer | P0 |
| `SEED-ENS-D14-0041` | utility energization permit tracker | EV | energization days | utility/permit/status | customer consent | P1 |
| `SEED-ENS-D14-0042` | EV site code pre-screen | EV | redesign rate | building/load/code | engineer review | P1 |
| `SEED-ENS-D14-0043` | Safeguard baseline simulator | Barossa/Darwin | baseline variance | production/emissions | operator data rights | P0 |
| `SEED-ENS-D14-0044` | operational-control compliance mapper | Australia | filer errors | JV/entity/control | Legal | P0 |
| `SEED-ENS-D14-0045` | Safeguard unit procurement optimizer | Australia | A$/t compliance | baseline/SMC/ACCU | trading policy | P1 |
| `SEED-ENS-D14-0046` | environmental condition digital twin | Australia | condition breaches | permits/sensors | regulator method | P0 |
| `SEED-ENS-D14-0047` | GO chain-of-custody engine | Australia | cert error | meter/product/emissions | GO rules | P1 |
| `SEED-ENS-D14-0048` | CCS permit-readiness score | Bayu-Undan | gate closure | title/MRV/subsurface | regulator | P0 |
| `SEED-ENS-D14-0049` | CCS MRV anomaly detection | CCS | stored-ton confidence | injection/pressure/model | approved MRV | P1 |
| `SEED-ENS-D14-0050` | Vietnam permit bilingual extractor | Quynh Lap | review time | VN/EN permits | certified translation | P0 |
| `SEED-ENS-D14-0051` | PDP/design consistency checker | Quynh Lap | rework | plan/design/version | authority confirmation | P0 |
| `SEED-ENS-D14-0052` | 2031 deadline Monte Carlo | Quynh Lap | cutoff probability | CPM/permit/EPC | PMO assumptions | P0 |
| `SEED-ENS-D14-0053` | PPA bankability clause tracker | Quynh Lap | open clauses | PPA/finance | Legal/Finance | P0 |
| `SEED-ENS-D14-0054` | permit-to-drawdown gate | Quynh Lap | premature spend | permits/PF | lender rules | P1 |
| `SEED-ENS-D14-0055` | sanctions continuous monitoring | Global | unresolved hits | parties/payments | Compliance | P0 |
| `SEED-ENS-D14-0056` | ABAC permit-interaction monitor | Global | high-risk events | meetings/agents/payments | privacy/Legal | P1 |
| `SEED-ENS-D14-0057` | regulated-data classifier | O/I platform | unclassified records | schema/source | Privacy/CISO | P0 |
| `SEED-ENS-D14-0058` | OT-safe AI gateway | Plants/BESS | unauthorized flows | OT tags/API/access | CISO/OT | P0 |
| `SEED-ENS-D14-0059` | source-locked legal RAG | Legal/OI | unsupported answer rate | official sources | human legal review | P0 |
| `SEED-ENS-D14-0060` | D17 compliance-gate scorer | Innovation | PoC kill rate late | all D14 gates | multi-function approval | P0 |

---
