---
id: skes-d10-18-o-i-opportunity-seed-master
title: O/I Opportunity Seed Master
summary: LNG·전력·가스·재생에너지 등 SK이노베이션 E&S 전 사업의 AI 기회 60개를 경제성·데이터 접근성·PoC 가능성·의사결정 연결성으로 평가하고 우선순위를 정한 마스터 테이블
tags: [d10, market, oi-seed, schema, table, "xref:d17", "xref:d02", "xref:d06", "xref:d11"]
keywords: [기회 마스터, AI 세드, LNG 최적화, 전력 예측, 우선순위 평가, PoC 기간, 데이터 기반, 도시가스, 재생에너지, 경제성 평가]
related: [SEED-ENS-D10-001, SEED-ENS-D10-002, SEED-ENS-D10-003, SEED-ENS-D10-004, SEED-ENS-D10-005, SEED-ENS-D10-006, SEED-ENS-D10-007, SEED-ENS-D10-008, SEED-ENS-D10-009, SEED-ENS-D10-010, SEED-ENS-D10-011, SEED-ENS-D10-012, SEED-ENS-D10-013, SEED-ENS-D10-014, SEED-ENS-D10-015, SEED-ENS-D10-016, SEED-ENS-D10-017, SEED-ENS-D10-018, SEED-ENS-D10-019, SEED-ENS-D10-020, SEED-ENS-D10-021, SEED-ENS-D10-022, SEED-ENS-D10-023, SEED-ENS-D10-024]
priority: normal
domain: D10
section: 18
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 2600
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# 18. O/I Opportunity Seed Master

## 18.1 Scoring Rule

각 Seed는 `경제적 중요도`, `데이터 접근성`, `6~16주 PoC 가능성`, `현업 의사결정 연결성`, `외부 협업 필요성`을 1~5점으로 평가한다. 점수는 공개사실이 아니라 내부 선별용 분석값이다.

## 18.2 Seed Master — 60 Candidates

| Seed ID | 과제명 | Segment | Core data | Success KPI | PoC | Priority |
|---|---|---|---|---|---|---|
| `SEED-ENS-D10-001` | LNG market signal radar | LNG | price·flow·outage·weather | alert lead time | 8w | P0 |
| `SEED-ENS-D10-002` | portfolio cargo allocation twin | LNG | contract·cargo·terminal·power | margin uplift | 16w | P0 |
| `SEED-ENS-D10-003` | LNG basis exposure graph | LNG | HH·JKM·oil·FX·freight | explained exposure | 10w | P0 |
| `SEED-ENS-D10-004` | vessel ETA/disruption predictor | LNG | AIS·weather·port | ETA error | 10w | P1 |
| `SEED-ENS-D10-005` | terminal inventory/slot optimizer | LNG | tank·slot·BOG·cargo | congestion hours | 14w | P0 |
| `SEED-ENS-D10-006` | LNG demand weather normalizer | LNG | HDD/CDD·load | MAPE | 8w | P0 |
| `SEED-ENS-D10-007` | contract optionality valuation | LNG | clauses·prices·routes | option value captured | 16w | P1 |
| `SEED-ENS-D10-008` | methane/carbon cargo score | LNG | emissions·MRV·route | traceable cargo share | 12w | P2 |
| `SEED-ENS-D10-009` | fuel-to-SMP lag model | power | fuel·FX·SMP·dispatch | forecast error | 12w | P0 |
| `SEED-ENS-D10-010` | CCGT clean spark forecaster | power | heat rate·fuel·SMP | margin forecast | 12w | P0 |
| `SEED-ENS-D10-011` | CHP power-heat co-optimizer | CHP | heat load·SMP·fuel | joint margin | 16w | P0 |
| `SEED-ENS-D10-012` | start/ramp value estimator | power | start·ramp·price | flexibility value | 12w | P1 |
| `SEED-ENS-D10-013` | outage economic prioritizer | power | failure·margin·parts | avoided lost margin | 12w | P0 |
| `SEED-ENS-D10-014` | peak stress dispatch copilot | power | weather·reserve·units | decision lead time | 10w | P1 |
| `SEED-ENS-D10-015` | city-gas weather normalization | city gas | usage·weather·customer | structural forecast | 10w | P0 |
| `SEED-ENS-D10-016` | electrification cohort radar | city gas | building·usage·equipment | churn recall | 14w | P1 |
| `SEED-ENS-D10-017` | industrial fuel-switch simulator | city gas | fuel·carbon·process | qualified opportunity | 12w | P1 |
| `SEED-ENS-D10-018` | gas service cost-to-serve model | city gas | calls·visits·meter | cost/customer | 12w | P1 |
| `SEED-ENS-D10-019` | renewable pipeline probability engine | renewable | permit·grid·EPC·finance | forecast calibration | 12w | P0 |
| `SEED-ENS-D10-020` | grid queue/COD risk monitor | renewable | queue·milestone·network | delay lead time | 10w | P0 |
| `SEED-ENS-D10-021` | curtailment forecast | renewable | weather·grid·dispatch | lost MWh error | 12w | P1 |
| `SEED-ENS-D10-022` | offshore wind milestone graph | renewable | permit·survey·EPC | missed milestone | 12w | P0 |
| `SEED-ENS-D10-023` | PPA load-asset matcher | PPA | 15m load·generation | shape match | 14w | P0 |
| `SEED-ENS-D10-024` | PPA price/shape benchmark | PPA | bids·term·profile | quote cycle time | 12w | P1 |
| `SEED-ENS-D10-025` | PPA bankability scorer | PPA | credit·grid·asset·term | conversion | 10w | P0 |
| `SEED-ENS-D10-026` | 24/7 CFE portfolio optimizer | PPA | hourly load·gen·BESS | hourly coverage | 16w | P1 |
| `SEED-ENS-D10-027` | RE100 policy/evidence radar | PPA | rule·meter·REC | compliance lead time | 10w | P1 |
| `SEED-ENS-D10-028` | BESS market saturation monitor | BESS | operating MW·spread·revenue | margin warning | 10w | P0 |
| `SEED-ENS-D10-029` | MarketCapture counterfactual lab | BESS | bids·prices·SOC | risk-adjusted uplift | 16w | P0 |
| `SEED-ENS-D10-030` | degradation-aware bidding | BESS | SOH·cycle·price | lifecycle margin | 16w | P0 |
| `SEED-ENS-D10-031` | ancillary cannibalization model | BESS | awards·capacity·price | forecast error | 12w | P0 |
| `SEED-ENS-D10-032` | multi-market revenue stack engine | BESS | rules·prices·asset | option value | 16w | P1 |
| `SEED-ENS-D10-033` | BESS duration portfolio optimizer | BESS | load·price·CAPEX | risk return | 16w | P1 |
| `SEED-ENS-D10-034` | interconnection attrition predictor | BESS | queue·study·permit | conversion calibration | 12w | P0 |
| `SEED-ENS-D10-035` | competitor project graph | BESS | developer·supplier·COD | coverage | 10w | P1 |
| `SEED-ENS-D10-036` | charging site TAM qualifier | EV | panel·parking·EV·owner | install conversion | 10w | P0 |
| `SEED-ENS-D10-037` | constrained-kW capacity planner | EV | panel·sessions·dwell | served EV/kW | 12w | P0 |
| `SEED-ENS-D10-038` | port utilization forecast | EV | sessions·site·calendar | utilization MAPE | 10w | P0 |
| `SEED-ENS-D10-039` | fleet departure-SOC optimizer | EV | routes·arrival·SOC | SLA attainment | 14w | P1 |
| `SEED-ENS-D10-040` | charging fault triage | EV | alarm·ticket·parts | MTTR | 10w | P0 |
| `SEED-ENS-D10-041` | charging recurring-revenue cockpit | EV | port·subscription·service | ARR/port | 8w | P1 |
| `SEED-ENS-D10-042` | competitor pricing/offer monitor | EV | quote·hardware·SaaS | win-rate insight | 8w | P1 |
| `SEED-ENS-D10-043` | H2 commitment classifier | H2 | MOU·order·contract·sale | false backlog | 8w | P0 |
| `SEED-ENS-D10-044` | vehicle-station-fuel rollout twin | H2 | vehicle·station·plant·route | sold kg | 16w | P0 |
| `SEED-ENS-D10-045` | station throughput forecast | H2 | vehicle·route·kg·downtime | MAPE | 12w | P0 |
| `SEED-ENS-D10-046` | liquid-H2 logistics optimizer | H2 | tank·trailer·station | delivered cost/kg | 14w | P0 |
| `SEED-ENS-D10-047` | boil-off mass-balance monitor | H2 | production·storage·delivery | loss rate | 12w | P0 |
| `SEED-ENS-D10-048` | H2 subsidy/TCO stress simulator | H2 | vehicle·fuel·subsidy | parity gap | 12w | P1 |
| `SEED-ENS-D10-049` | fleet cluster prospecting | H2 | route·depot·vehicle | qualified kg/day | 12w | P1 |
| `SEED-ENS-D10-050` | CCS emitter qualification engine | CCS | emissions·quality·distance | qualified tCO2 | 12w | P0 |
| `SEED-ENS-D10-051` | capture-storage matching twin | CCS | capture·transport·storage | matched tCO2 | 16w | P0 |
| `SEED-ENS-D10-052` | CCS stage-gate probability model | CCS | permit·FID·contract | calibration | 12w | P0 |
| `SEED-ENS-D10-053` | injectivity uncertainty model | CCS | well·seismic·pressure | capacity confidence | 16w | P2 |
| `SEED-ENS-D10-054` | MRV evidence knowledge graph | CCS | meter·sample·model·report | completeness | 12w | P0 |
| `SEED-ENS-D10-055` | CCS full-chain cost simulator | CCS | capex·energy·transport | cost/tCO2 | 16w | P1 |
| `SEED-ENS-D10-056` | market forecast version registry | all | forecast·scope·date | overwrite errors | 8w | P0 |
| `SEED-ENS-D10-057` | competitor claim verification agent | all | source·metric·scope | false comparison | 10w | P0 |
| `SEED-ENS-D10-058` | market-to-asset exposure graph | all | market·asset·contract·KPI | mapping coverage | 14w | P0 |
| `SEED-ENS-D10-059` | scenario-to-P&L bridge | all | scenario·volume·price·cost | decision cycle | 16w | P0 |
| `SEED-ENS-D10-060` | market signal decision copilot | all | approved sources·owners·actions | adoption rate | 12w | P0 |

## 18.3 P0 Shortlist — D17 Handoff

| Rank | Seed | Why now | Minimum PoC | Stop condition |
|---:|---|---|---|---|
| 1 | 058 Market-to-Asset Exposure Graph | D02~D09를 시장신호와 연결 | LNG·KCE 2개 chain | mapping <80% |
| 2 | 002 Portfolio Cargo Allocation Twin | 2026 LNG volatility 직접 대응 | cargo 3건·발전 2기 | 의사결정 uplift 없음 |
| 3 | 011 CHP Power-Heat Co-optimizer | D06 중요공정·수익 직결 | CHP 1개 site 12개월 | joint margin 개선 없음 |
| 4 | 029 MarketCapture Counterfactual Lab | KCE 차별성 검증 | ERCOT assets subset | risk-adjusted alpha 없음 |
| 5 | 030 Degradation-aware Bidding | 성장·수익 동시관리 | BESS 1개 asset | lifecycle margin 악화 |
| 6 | 023 PPA Load-Asset Matcher | 고객·재생 portfolio 연결 | 고객 2·자산 3 | imbalance 개선 미미 |
| 7 | 019 Renewable Pipeline Probability | 5GW pipeline 과대평가 방지 | 20 projects | calibration 불량 |
| 8 | 036 Charging Site TAM Qualifier | EverCharge 영업효율 | 100 leads | conversion lift 없음 |
| 9 | 044 H2 Rollout Twin | capacity-demand mismatch 핵심 | 도시 1·fleet 1 | data sharing 불가 |
| 10 | 050 CCS Emitter Qualification | 상용화 전제 검증 | emitter 20 | firm interest 없음 |
| 11 | 056 Forecast Version Registry | 모든 시장 오류 통제 | D10 sources 47 | lineage 누락 |
| 12 | 059 Scenario-to-P&L Bridge | D11·D12 연결 | LNG/BESS/H2 | finance reconciliation 실패 |

## 18.4 Mandatory Seed Fields

```yaml
d17_seed_required:
  - seed_id
  - market_segment_and_geography
  - market_signal_and_as_of_date
  - fact_forecast_claim_status
  - affected_asset_process_customer_contract
  - quantified_problem_proxy
  - decision_owner
  - baseline_and_control
  - required_internal_data
  - data_right_and_security
  - external_partner_type
  - poc_duration
  - success_kpi
  - stop_condition
  - source_ids
  - human_approval_point
```

---
