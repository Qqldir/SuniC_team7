---
id: skes-d17-d17-12-decision-ready-internal-data-request-pac
title: Decision-Ready Internal Data Request Pack
summary: 에너지·유틸리티 전역 AI 시스템 개발에 필요한 데이터 요청사항과 민감도를 정리한 의사결정용 마스터 목록이다.
tags: [d17, oi-portfolio, table]
keywords: [데이터 마스터, 에너지 포트폴리오, 민감도 분류, LNG·전력·도시가스, 운영 데이터, AI 거버넌스, 자산 정보, SCADA·BMS·EAM]
related: [DR-D17-001, DR-D17-002, DR-D17-003, DR-D17-004, DR-D17-005, DR-D17-006, DR-D17-007, DR-D17-008, DR-D17-009, DR-D17-010, DR-D17-011, DR-D17-012, DR-D17-013, DR-D17-014, DR-D17-015, DR-D17-016, DR-D17-017, DR-D17-018, DR-D17-019, DR-D17-020, DR-D17-021, DR-D17-022, DR-D17-023, DR-D17-024]
priority: normal
domain: D17
section: D17-12
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 1492
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-12 Decision-Ready Internal Data Request Pack

## 1. Enterprise Foundation

| Request ID | 내부 데이터 | Grain | 핵심 과제 | Owner 후보 |
|---|---|---|---|---|
| `DR-D17-001` | legal entity/JV/SPV master | entity/effective date | 047·051·053·054 | Legal/Corp |
| `DR-D17-002` | asset/site/equipment hierarchy | asset/equipment/history | 006·011·012·016·056 | Asset/Data |
| `DR-D17-003` | contract/right master + amendments | clause/right/version | 006·007·023·047·051 | Legal |
| `DR-D17-004` | existing O/I/AI/PoC archive | project/gate/result | 001~005 | O/I |
| `DR-D17-005` | benefit baseline/PIR ledger | task/KPI/cash | 003·005·전체 | FP&A |
| `DR-D17-006` | data catalog/owner/classification | dataset/field | 전체 | Data/CISO |
| `DR-D17-007` | vendor/license/SLA/EOL | product/version/term | 004·015·026·056 | Procurement/IT |
| `DR-D17-008` | AI approval/audit/model registry | model/version/action | 002·003·060 | AI Governance |

## 2. LNG / Power / City Gas

| Request ID | 내부 데이터 | Grain / Period | 핵심 과제 | Sensitivity |
|---|---|---|---|---|
| `DR-D17-009` | LNG contract entitlement/option/index | cargo/contract 3y | 006·007 | RESTRICTED |
| `DR-D17-010` | cargo/vessel/AIS/ETA/berth | voyage 2y | 006·009 | HIGH |
| `DR-D17-011` | terminal tank/BOG/send-out | tag 1~5min 12m+ | 006·008 | RESTRICTED_OT |
| `DR-D17-012` | LNG invoice/toll/freight/FX | cargo 3y | 007 | RESTRICTED |
| `DR-D17-013` | power fuel/net MWh/heat rate/ambient | unit 5~60min 24m | 006·011·046 | RESTRICTED_OT |
| `DR-D17-014` | trip/start/alarm/historian | unit/event 5y | 012 | RESTRICTED_OT |
| `DR-D17-015` | EAM work/failure/spare/lead time | equipment/work 5y | 012·014 | HIGH |
| `DR-D17-016` | CHP heat/weather/price/SLA | interval 24m | 013 | HIGH |
| `DR-D17-017` | city-gas GIS/pipe/regulator | segment/history | 016·017 | CRITICAL_INFRA |
| `DR-D17-018` | leak/inspection/excavation/work | segment/event 5y | 016·017 | SAFETY |
| `DR-D17-019` | receipt/meter/billing/correction | meter/interval 24m | 018 | PRIVACY_COMMERCIAL |
| `DR-D17-020` | emergency call/crew/arrival/SOP | incident 24m | 019 | SAFETY_PRIVACY |

## 3. Renewable / BESS / EV

| Request ID | 내부 데이터 | Grain / Period | 핵심 과제 | Sensitivity |
|---|---|---|---|---|
| `DR-D17-021` | wind SCADA/CMS/metocean | turbine 10min 12m+ | 021·022 | HIGH |
| `DR-D17-022` | cable condition/marine logs/parts | asset/event 5y | 021 | HIGH |
| `DR-D17-023` | renewable forecast/actual/curtailment | asset/interval 24m | 022·025 | HIGH |
| `DR-D17-024` | PPA load/gen/meter/REC/settlement | 15m~monthly 24m | 023·024 | RESTRICTED |
| `DR-D17-025` | KCE BMS/PCS/EMS/SOC/SOH | site/block/interval 24m | 026·027·028 | RESTRICTED_OT |
| `DR-D17-026` | BESS warranty/throughput/LTSA/insurance | contract/site | 026·027 | RESTRICTED |
| `DR-D17-027` | bid/award/dispatch/price/settlement | interval/site 24m | 026·028·029 | RESTRICTED |
| `DR-D17-028` | optimizer model/version/override | deployment/event | 026·028·029 | RESTRICTED_IP |
| `DR-D17-029` | BESS alarm/incident/response | event 5y | 027 | SAFETY |
| `DR-D17-030` | interconnection/permit/study/milestone | project/version | 030·047 | RESTRICTED |
| `DR-D17-031` | charger heartbeat/error/session/payment | port/session 12m+ | 031·033 | PRIVACY |
| `DR-D17-032` | site one-line/panel/transformer/utility limit | site/current | 032·034 | CRITICAL_ELECTRICAL |
| `DR-D17-033` | truck roll/repair/parts | work/site 24m | 031·033 | HIGH |
| `DR-D17-034` | fleet departure SOC/request | vehicle/session | 034 | PRIVACY |

## 4. Hydrogen / CCS / Regulation / Projects

| Request ID | 내부 데이터 | Grain / Period | 핵심 과제 | Sensitivity |
|---|---|---|---|---|
| `DR-D17-035` | LH2 train historian/feed/power/product | tag/interval 24m | 036·037·038 | RESTRICTED_OT |
| `DR-D17-036` | detector/ESD/PSV/proof-test/bypass | barrier/event | 036 | SAFETY_CRITICAL |
| `DR-D17-037` | produced/stored/loaded/delivered/sold/paid kg | meter/event/day | 037·039 | HIGH |
| `DR-D17-038` | LH2 meter calibration/uncertainty | meter/version | 037 | METROLOGY |
| `DR-D17-039` | station inventory/uptime/tanker route | station/route/day | 039 | HIGH |
| `DR-D17-040` | H2 offtake/vehicle/stage/price/credit | contract/project | 040·050 | RESTRICTED |
| `DR-D17-041` | CCS emitter FID/volume/COD/contract | emitter/project | 041·042 | RESTRICTED |
| `DR-D17-042` | subsurface/injectivity/model ensemble | model/well/version | 041·043 | RESTRICTED_TECH |
| `DR-D17-043` | CCS MMV/permit/closure/liability | obligation/version | 041·044 | RESTRICTED_LEGAL |
| `DR-D17-044` | K-ETS emissions/allocation/position | facility/day-year | 046 | RESTRICTED |
| `DR-D17-045` | KCE tax basis/PIS/PWA/BOM ownership | project/component | 047 | TAX_RESTRICTED |
| `DR-D17-046` | current rule/source/owner/effective date | rule/version | 002·029·035·046~050 | LEGAL |
| `DR-D17-047` | project CPM/permit/EPC/JV milestone | activity/week | 052·053 | RESTRICTED |
| `DR-D17-048` | budget/commitment/invoice/EAC/cash | WBS/month | 052·054·055 | FINANCE_RESTRICTED |
| `DR-D17-049` | debt/covenant/guarantee/support | facility/clause | 054·055 | FINANCE_RESTRICTED |
| `DR-D17-050` | OT network/asset/remote access/backup/RTO | zone/asset/event | 056~060 | SECURITY_CRITICAL |

---
