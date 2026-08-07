---
id: skes-d08-18-d08-open-innovation-seed-portfolio
title: D08 Open-Innovation Seed Portfolio
summary: SK이노베이션 E&S가 추진하는 LNG·공급망·에너지 분야의 60개 AI·데이터 프로젝트를 평가 기준과 함께 제시한 문서.
tags: [d08, supply-chain, oi-seed, table, "xref:d11", "xref:d06"]
keywords: [LNG, 공급망, 데이터 레디니스, 터미널, 최적화, 에너지, 해운, 기술 혁신]
related: [SEED-ENS-D08-001, SEED-ENS-D08-002, SEED-ENS-D08-003, SEED-ENS-D08-004, SEED-ENS-D08-005, SEED-ENS-D08-006, SEED-ENS-D08-007, SEED-ENS-D08-008, SEED-ENS-D08-009, SEED-ENS-D08-010, SEED-ENS-D08-011, SEED-ENS-D08-012, SEED-ENS-D08-013, SEED-ENS-D08-014, SEED-ENS-D08-015, SEED-ENS-D08-016, SEED-ENS-D08-017, SEED-ENS-D08-018, SEED-ENS-D08-019, SEED-ENS-D08-020, SEED-ENS-D08-021, SEED-ENS-D08-022, SEED-ENS-D08-023, SEED-ENS-D08-024]
priority: normal
domain: D08
section: 18
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 2625
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 18. D08 Open-Innovation Seed Portfolio

## 18.1 Seed Scoring Rule

| 항목 | 가중치 | 질문 |
|---|---:|---|
| value | 25 | 원가·재고·가동률·안전 영향이 큰가 |
| data readiness | 20 | 6~12개월 데이터 확보가 가능한가 |
| feasibility | 15 | 기존 시스템과 제한적 PoC가 가능한가 |
| time to value | 15 | 6개월 이내 선행성과가 가능한가 |
| replicability | 10 | 발전·도시가스·자회사로 확산 가능한가 |
| safety/compliance | 10 | 위험·증빙을 개선하는가 |
| partner dependency | -5~5 | 외부 권리·인터페이스가 장애인가 |

## 18.2 Seed Master — 60 Candidates

| Seed ID | 과제 | 대상 | 핵심 데이터 | KPI | Gate |
|---|---|---|---|---|---|
| `SEED-ENS-D08-001` | LNG portfolio stochastic optimizer | LNG 전체 | demand·entitlement·price·inventory | landed cost·stockout | P0, confidential sandbox |
| `SEED-ENS-D08-002` | cargo-vessel-terminal scheduler | 선대/Boryeong | ETA·slot·ullage·sendout | demurrage·OTIF | P0 |
| `SEED-ENS-D08-003` | Freeport outage scenario engine | Freeport route | notice·inventory·spot·dispatch | replanning time | P0 |
| `SEED-ENS-D08-004` | Barossa ramp-up anomaly monitor | Barossa/Darwin | production·quality·outage | entitlement loss | JV data right |
| `SEED-ENS-D08-005` | LNG contract-right digital ledger | LNG contracts | clause·capacity·usage | utilization·audit | P0-foundation |
| `SEED-ENS-D08-006` | contract optionality valuation | LNG contracts | window·make-up·flexibility | option value | legal validation |
| `SEED-ENS-D08-007` | vessel ETA/weather predictor | LNG fleet | AIS·weather·port | ETA MAE | P0 |
| `SEED-ENS-D08-008` | voyage speed/fuel optimizer | LNG fleet | fuel curve·BOR·slot | fuel/t·cargo loss | safety approval |
| `SEED-ENS-D08-009` | LNG quality-to-heat-rate model | power fleet | CoA·lab·GT performance | heat rate | P1 |
| `SEED-ENS-D08-010` | tank ullage/BOG forecast | Boryeong | level·temp·receipt/sendout | BOG·slot conflict | historian access |
| `SEED-ENS-D08-011` | terminal quantity reconciliation | Boryeong | bill·tank·meter·ship | imbalance | metering governance |
| `SEED-ENS-D08-012` | fuel-dispatch co-optimizer | power/CHP | SMP·heat·heat rate·fuel | margin·fuel cover | P0 |
| `SEED-ENS-D08-013` | LNG landed-cost explainability | LNG finance | deal·flow·invoice·FX | variance closure | D11 link |
| `SEED-ENS-D08-014` | spot cargo decision copilot | trading | price·credit·inventory | decision lead time | human approval |
| `SEED-ENS-D08-015` | supplier/entity master resolution | enterprise | vendor master·contract·PO | duplicate rate | P0-foundation |
| `SEED-ENS-D08-016` | contract clause/data-right extractor | enterprise | contracts | review time·missed right | legal human review |
| `SEED-ENS-D08-017` | supplier control tower | enterprise | OTIF·quality·risk·ESG | disruption lead time | P0 |
| `SEED-ENS-D08-018` | supplier financial early warning | critical suppliers | rating·payment·news | warning precision | explainability |
| `SEED-ENS-D08-019` | multi-tier origin/BOM graph | BESS/EVSE/PV | BOM·AVL·origin | traceability | supplier participation |
| `SEED-ENS-D08-020` | PO lead-time predictor | MRO/project | PO·milestone·receipt | lead-time MAE | P1 |
| `SEED-ENS-D08-021` | expediting priority engine | projects | schedule·critical path·ETA | delay avoided | planner override |
| `SEED-ENS-D08-022` | invoice/GR anomaly detection | common | PO·GR·invoice | leakage·review time | finance validation |
| `SEED-ENS-D08-023` | critical-spare risk optimizer | power/LNG | failure·lead time·stock·outage cost | service level·inventory | P0 |
| `SEED-ENS-D08-024` | repairable-parts serial loop | power | serial·repair·warranty | turnaround·recovery | master data |
| `SEED-ENS-D08-025` | shared-spares marketplace | power fleet | compatibility·stock·location | avoided purchase | governance |
| `SEED-ENS-D08-026` | wrong-revision/counterfeit detector | MRO | BOM·photo·certificate | escape rate | inspection images |
| `SEED-ENS-D08-027` | contractor safety-quality score | all sites | permit·incident·NCR·rework | incident/rework | fairness review |
| `SEED-ENS-D08-028` | 7-city-gas multi-echelon inventory | city gas | demand·stock·transfer·lead time | fill rate·inventory | P0 |
| `SEED-ENS-D08-029` | pipe-lot GIS genealogy | city gas | lot·joint·segment·failure | recall time | P0 safety |
| `SEED-ENS-D08-030` | meter/regulator fleet recall engine | city gas | serial·model·site·event | affected units found | data completeness |
| `SEED-ENS-D08-031` | field-material demand forecast | city gas | work plan·failure·weather | stockout | P1 |
| `SEED-ENS-D08-032` | emergency-stock transfer recommender | city gas | regional stock·travel·incident | response time | emergency governance |
| `SEED-ENS-D08-033` | supplier CoA/document validation | common | CoA·spec·PO | review time·escape | human exception |
| `SEED-ENS-D08-034` | offshore package schedule twin | OWF2/3 | delivery·vessel·weather·critical path | COD risk | project data |
| `SEED-ENS-D08-035` | turbine/cable warranty claim miner | OWF1 | SCADA·work order·contract | recovery | OEM data right |
| `SEED-ENS-D08-036` | renewable digital-handover QA | renewable | as-built·tag·point list·punch | completeness | P0 by-design |
| `SEED-ENS-D08-037` | offshore spare/vessel co-planner | wind O&M | failure·weather·spare·vessel | downtime | P1 |
| `SEED-ENS-D08-038` | PV serial/degradation genealogy | solar | serial·flash·SCADA | warranty yield | P1 |
| `SEED-ENS-D08-039` | BESS vendor bankability radar | KCE | financial·recall·warranty | risk lead time | human review |
| `SEED-ENS-D08-040` | BESS serial genealogy/recall graph | KCE | cell/rack/container/project | recall time | OEM data right |
| `SEED-ENS-D08-041` | warranty-aware dispatch optimizer | KCE | market·SOH·warranty | net margin | safety/warranty |
| `SEED-ENS-D08-042` | BESS parts failure clustering | KCE | alarm·work order·lot | MTBF·repeat rate | label quality |
| `SEED-ENS-D08-043` | firmware/SBOM vulnerability monitor | KCE/EverCharge | SBOM·CVE·asset | exposure closure | cyber governance |
| `SEED-ENS-D08-044` | EPC punch-list closure predictor | KCE/renewable | punch·owner·evidence | aging | P1 |
| `SEED-ENS-D08-045` | BESS spares pooling optimizer | KCE | fleet BOM·stock·failure | service level | compatibility |
| `SEED-ENS-D08-046` | EVSE component EOL predictor | EverCharge | BOM·supplier notice·failure | shortage avoided | sub-tier data |
| `SEED-ENS-D08-047` | installer first-time-right analytics | EverCharge | visit·photo·test·ticket | first-time-fix | P1 |
| `SEED-ENS-D08-048` | EVSE warranty auto-triage | EverCharge | telemetry·lot·ticket | claim cycle | explainability |
| `SEED-ENS-D08-049` | LH₂ production-logistics optimizer | Incheon/network | feed·train·storage·station | yield·stockout | P0 |
| `SEED-ENS-D08-050` | trailer routing with safety windows | LH₂ | route·ETA·inventory·driver | OTIF·km/t | safety constraints |
| `SEED-ENS-D08-051` | LH₂ boil-off mass-balance analytics | LH₂ | meter·level·transfer | loss rate | metering QA |
| `SEED-ENS-D08-052` | cryogenic-spare risk inventory | LH₂ | condition·lead time·failure | availability | P0 |
| `SEED-ENS-D08-053` | H₂ purity deviation predictor | LH₂ | feed/after purification lab·sensor | off-spec | safety validation |
| `SEED-ENS-D08-054` | CCS supplier/evidence graph | CCS | equipment·calibration·MRV | evidence completeness | planned |
| `SEED-ENS-D08-055` | solvent degradation/makeup optimizer | capture pilot | composition·energy·capture | solvent/tCO₂ | pilot data |
| `SEED-ENS-D08-056` | low-carbon LNG chain-of-custody | LNG/CCS | cargo·energy·methane·MRV | traceability | methodology approval |
| `SEED-ENS-D08-057` | supplier ESG evidence copilot | suppliers | questionnaire·document·CAP | review time | no auto-rejection |
| `SEED-ENS-D08-058` | supplier CAP closure monitor | suppliers | finding·owner·evidence | on-time closure | P1 |
| `SEED-ENS-D08-059` | disruption network simulator | enterprise | supplier·flow·inventory·asset | recovery time | P0 |
| `SEED-ENS-D08-060` | O/I benefit measurement layer | all seeds | baseline·control·market factors | attributable value | mandatory |

## 18.3 P0 Shortlist

| Rank | Seed | 이유 | 첫 PoC |
|---:|---|---|---|
| 1 | 001 LNG portfolio optimizer | 연료비·공급안정 직접 영향 | 과거계획 replay |
| 2 | 002 cargo-vessel-terminal scheduler | D06 핵심 병목·데이터 명확 | 1개 route/terminal |
| 3 | 005 contract-right ledger | 모든 LNG 최적화 선행기반 | 5개 핵심 권리 |
| 4 | 023 critical-spare optimizer | 발전 outage 비용·복제성 | 1개 발전소 A1 품목 |
| 5 | 028 city-gas multi-echelon inventory | 7개사 시너지 | 2개 인접권역 |
| 6 | 029 pipe-lot GIS genealogy | 안전·recall 가치 | 1개 자재군 |
| 7 | 040 BESS recall graph | 화재·OEM 위험 | NY6 genealogy |
| 8 | 041 warranty-aware dispatch | 수익·열화 동시개선 | 1개 KCE site replay |
| 9 | 049 LH₂ production-logistics optimizer | 신사업 병목·재고 | 1 train+2 station |
| 10 | 059 disruption simulator | 전사 BCP 의사결정 | Freeport outage scenario |

---
