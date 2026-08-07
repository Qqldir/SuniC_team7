---
id: skes-d09-18-open-innovation-seed-portfolio
title: Open-Innovation Seed Portfolio
summary: 혁신 씨드 평가 규칙과 60개 후보 프로젝트를 세그먼트·필요 데이터·성공 지표·PoC기간·우선순위별로 정리한 마스터.
tags: [d09, customer, oi-seed, schema, table, "xref:d17"]
keywords: [Seed Scoring Rule, Entity Resolution, Golden Thread, KPI, PoC, 수요 예측, 이상탐지, 조기경보, 계약 변경 영향, WAPE]
related: [SEED-ENS-D09-001, SEED-ENS-D09-002, SEED-ENS-D09-003, SEED-ENS-D09-004, SEED-ENS-D09-005, SEED-ENS-D09-006, SEED-ENS-D09-007, SEED-ENS-D09-008, SEED-ENS-D09-009, SEED-ENS-D09-010, SEED-ENS-D09-011, SEED-ENS-D09-012, SEED-ENS-D09-013, SEED-ENS-D09-014, SEED-ENS-D09-015, SEED-ENS-D09-016, SEED-ENS-D09-017, SEED-ENS-D09-018, SEED-ENS-D09-019, SEED-ENS-D09-020, SEED-ENS-D09-021, SEED-ENS-D09-022, SEED-ENS-D09-023, SEED-ENS-D09-024]
priority: normal
domain: D09
section: 18
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 2800
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 18. Open-Innovation Seed Portfolio

## 18.1 Seed Scoring Rule

각 Seed는 `Value 25 + Feasibility 20 + Data readiness 15 + Speed 15 + Strategic fit 15 + External leverage 10 - Risk penalty`로 100점 사전평가한다. 공개자료 점수는 후보선정용이며 내부 baseline·data right·process owner가 없으면 PoC 승인하지 않는다.

## 18.2 Seed Master — 60 Candidates

| Seed ID | Task | Segment | Required internal data | Success KPI | PoC | Priority |
|---|---|---|---|---|---|---|
| `SEED-ENS-D09-001` | 고객·파트너·시장기관 Entity Resolution | all | CRM·CLM·billing master | duplicate reduction | 8w | P0 |
| `SEED-ENS-D09-002` | 계약–수요–계량 Golden Thread | all | contract·forecast·meter | lineage coverage | 12w | P0 |
| `SEED-ENS-D09-003` | MOU/계약 commitment classifier | H2/PPA | documents·stage | false backlog rate | 6w | P0 |
| `SEED-ENS-D09-004` | 계약 변경영향 diff copilot | all | amendments·obligations | review lead time | 8w | P1 |
| `SEED-ENS-D09-005` | Clause-to-KPI obligation monitor | PPA/service | contract·KPI | missed obligation | 12w | P0 |
| `SEED-ENS-D09-006` | 고객신용 조기경보 | PPA/industrial | AR·rating·news | alert lead time | 10w | P1 |
| `SEED-ENS-D09-007` | 계약갱신 next-best-action | B2B | usage·issues·term | renewal uplift | 10w | P1 |
| `SEED-ENS-D09-008` | Account 360 evidence graph | B2B | CRM·case·contract | prep time | 8w | P1 |
| `SEED-ENS-D09-009` | 고객집중도 scenario monitor | all | volume·revenue·contract | exposure visibility | 6w | P1 |
| `SEED-ENS-D09-010` | LNG-to-power integrated demand forecast | LNG/power | market·plant·fuel | fuel WAPE | 12w | P0 |
| `SEED-ENS-D09-011` | 발전 nomination exception engine | power | schedule·nomination | exception lead time | 8w | P0 |
| `SEED-ENS-D09-012` | CHP heat-power co-optimization | CHP | heat·weather·SMP | total margin/SLA | 16w | P0 |
| `SEED-ENS-D09-013` | 산업고객 demand signal fusion | city gas | account load·calendar | WAPE | 10w | P1 |
| `SEED-ENS-D09-014` | 도시가스 cold-wave probabilistic forecast | city gas | AMI·weather | peak error | 10w | P0 |
| `SEED-ENS-D09-015` | 서비스포인트–계량기–계약 matching | city gas | CRM·GIS·billing | unmatched rate | 10w | P0 |
| `SEED-ENS-D09-016` | AMI 계량 이상탐지 | city gas | interval reads·work order | precision/recall | 12w | P0 |
| `SEED-ENS-D09-017` | 청구 전 bill anomaly guard | city gas | tariff·meter·invoice | bill error rate | 8w | P0 |
| `SEED-ENS-D09-018` | 전입·전출 방문 성공예측 | city gas | appointment·history | first-time success | 8w | P1 |
| `SEED-ENS-D09-019` | 공급가능 GIS self-service | city gas | pipe·address·plan | inquiry deflection | 12w | P1 |
| `SEED-ENS-D09-020` | 긴급신고 상담 triage assist | city gas | transcripts·dispatch | arrival/recall | 12w | P0 |
| `SEED-ENS-D09-021` | 현장기사 knowledge copilot | city gas | manuals·cases | fix rate | 8w | P1 |
| `SEED-ENS-D09-022` | 민원 root-cause clustering | city gas | cases·asset events | recurrence | 8w | P1 |
| `SEED-ENS-D09-023` | 체납상담 우선순위·지원 안내 | city gas | AR·consent·policy | cure/support rate | 10w | P1 |
| `SEED-ENS-D09-024` | 상담 음성 PII redaction | city gas | audio·policy | leakage rate | 6w | P0 |
| `SEED-ENS-D09-025` | 고객 Journey process mining | city gas | event logs | cycle time | 10w | P1 |
| `SEED-ENS-D09-026` | PPA load–generation matcher | PPA | interval load/gen | shape match | 12w | P0 |
| `SEED-ENS-D09-027` | PPA imbalance forecast | PPA | forecast·meter·price | imbalance cost | 12w | P0 |
| `SEED-ENS-D09-028` | Renewable COD risk monitor | PPA | EPC milestone·weather | delay alert | 10w | P0 |
| `SEED-ENS-D09-029` | RE100 evidence lineage graph | PPA | meter·REC·contract | completeness | 10w | P0 |
| `SEED-ENS-D09-030` | PPA contract VaR simulator | PPA | clause·price·profile | risk visibility | 14w | P1 |
| `SEED-ENS-D09-031` | PPA lead qualification scorer | PPA | load·credit·target | conversion | 8w | P1 |
| `SEED-ENS-D09-032` | 24/7 CFE portfolio simulator | PPA | hourly load/gen | hourly coverage | 16w | P1 |
| `SEED-ENS-D09-033` | privacy-preserving PPA optimizer | PPA | masked profiles | value vs baseline | 16w | P2 |
| `SEED-ENS-D09-034` | KCE bid feasibility pre-check | BESS | SOC·availability·rules | invalid bid | 8w | P0 |
| `SEED-ENS-D09-035` | warranty-aware bid optimizer | BESS | warranty·SOH·prices | lifecycle NPV | 16w | P0 |
| `SEED-ENS-D09-036` | bid-to-meter settlement reconciler | BESS | bid·award·meter·invoice | recovered leakage | 12w | P0 |
| `SEED-ENS-D09-037` | market rule change monitor | BESS | filings·rulebook·models | update lead time | 8w | P0 |
| `SEED-ENS-D09-038` | telemetry quality sentinel | BESS | SCADA·market telemetry | bad-data time | 8w | P0 |
| `SEED-ENS-D09-039` | NWA SLA predictor | BESS | feeder·availability | SLA compliance | 12w | P1 |
| `SEED-ENS-D09-040` | BESS community/permit CRM | BESS | stakeholder·milestone | permit lead time | 10w | P1 |
| `SEED-ENS-D09-041` | EV charging site demand forecast | charging | session·tenant·fleet | peak/session WAPE | 10w | P0 |
| `SEED-ENS-D09-042` | fleet departure-SOC scheduler | charging | routes·SOC·EVSE | departure success | 12w | P0 |
| `SEED-ENS-D09-043` | charger fault predictive support | charging | logs·tickets | MTTR | 10w | P0 |
| `SEED-ENS-D09-044` | session-to-payment reconciler | charging | session·payment | orphan rate | 8w | P1 |
| `SEED-ENS-D09-045` | site expansion trigger | charging | utilization·wait·capacity | timing/ROI | 10w | P1 |
| `SEED-ENS-D09-046` | driver onboarding copilot | charging | signup·support | activation | 6w | P2 |
| `SEED-ENS-D09-047` | infrastructure CAPEX avoided estimator | charging | one-line·load·design | estimate error | 10w | P1 |
| `SEED-ENS-D09-048` | multi-site customer health score | charging | uptime·tickets·usage | renewal | 10w | P1 |
| `SEED-ENS-D09-049` | hydrogen demand stage-gate model | hydrogen | MOU·vehicle·station·contract | forecast bias | 10w | P0 |
| `SEED-ENS-D09-050` | station–fleet–trailer control tower | hydrogen | inventory·ETA·schedule | stockout | 14w | P0 |
| `SEED-ENS-D09-051` | bus refueling slot optimizer | hydrogen | route·SOC·dispenser | queue time | 10w | P0 |
| `SEED-ENS-D09-052` | liquid-hydrogen loss allocation | hydrogen | load·delivery·dispense | unaccounted loss | 12w | P1 |
| `SEED-ENS-D09-053` | station ramp-up adoption forecast | hydrogen | active vehicles·sessions | utilization | 10w | P1 |
| `SEED-ENS-D09-054` | hydrogen SLA exception copilot | hydrogen | contract·delivery·downtime | recovery time | 8w | P1 |
| `SEED-ENS-D09-055` | CCS emitter qualification engine | CCS | emissions·quality·distance | qualified lead rate | 12w | P1 |
| `SEED-ENS-D09-056` | CCS volume–storage matching simulator | CCS | capture·transport·storage | feasible tCO2 | 16w | P1 |
| `SEED-ENS-D09-057` | MRV responsibility graph | CCS | contract·sensor·report | evidence coverage | 12w | P1 |
| `SEED-ENS-D09-058` | customer data-right registry | all | clauses·consent·systems | usable-data ratio | 8w | P0 |
| `SEED-ENS-D09-059` | PoC benefit baseline factory | all | historical KPI·control group | auditability | 8w | P0 |
| `SEED-ENS-D09-060` | human-approval decision gateway | all | model output·roles·audit | unauthorized actions | 8w | P0 |

## 18.3 P0 Shortlist

| Rank | Seed | Why now | Minimum dataset | Stop rule |
|---:|---|---|---|---|
| 1 | 002 계약–수요–계량 Golden Thread | 모든 D09 과제의 선행 기반 | 계약 1종·meter·settlement | join coverage <90% |
| 2 | 010 LNG-to-power forecast | 연료·발전 동시 가치 | 2개 발전소 1년 | baseline 미개선 |
| 3 | 012 CHP heat-power optimizer | 전력 단독최적화 오류 방지 | CHP 1곳·동절기 | SLA 위반 증가 |
| 4 | 015 도시가스 ID matching | 고객서비스·청구 공통 기반 | 1개 자회사 | false merge 허용치 초과 |
| 5 | 020 긴급신고 triage assist | 안전·고객가치 직접 | 비식별 신고·출동 | 고위험 recall 미달 |
| 6 | 026 PPA load-generation matcher | 공개 고객 확대와 직결 | 2 PPA·15분 data | imbalance 개선 미미 |
| 7 | 029 RE100 evidence graph | 신뢰·감사 자동화 | PPA 1건 월정산 | lineage 불완전 |
| 8 | 034 KCE bid feasibility | 빠른 시장운영 효과 | 자산 2개·90일 | invalid bid 미감소 |
| 9 | 036 KCE settlement reconciler | 현금효과 측정 용이 | 시장 1곳·6개월 | 회수액<비용 |
| 10 | 042 fleet SOC scheduler | 고객 SLA 명확 | fleet site 1곳 | 출차성공 악화 |
| 11 | 049 수소 stage-gate model | 계획수요 과대계상 차단 | 3지역 pipeline | status 정확도 미달 |
| 12 | 050 수소 control tower | station stockout·물류 개선 | station 2~3곳 | 안전·데이터권리 미확보 |
| 13 | 058 data-right registry | PoC 착수 실패 예방 | 계약 3종·시스템 5개 | 소유자 미지정 |
| 14 | 059 benefit baseline factory | 과제 ROI 비교 가능 | KPI 5개 | counterfactual 불가 |
| 15 | 060 human approval gateway | 고위험 자동결정 통제 | 과제 2개 | audit log 누락 |

## 18.4 Seed Mandatory Fields

모든 D17 인계 Seed는 다음 필드를 채운다.

```yaml
oi_seed_id: SEED-ENS-D09-000
customer_or_segment: string
quantified_problem_proxy: string
decision_owner: string
required_internal_data: []
potential_external_partner_type: string
poc_duration: string
success_kpi: []
baseline_period: string
human_approval_point: string
data_right_status: CONFIRMED | LIMITED | UNKNOWN
source_ids: []
```

---
