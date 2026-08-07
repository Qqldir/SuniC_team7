---
id: skon-d15-d15-11-o-i-opportunity-portfolio
title: O/I Opportunity Portfolio
summary: SK온 D15의 리스크·품질·안전 관련 15개 디지털 혁신 후보 프로젝트를 평가 점수(25점 만점)와 우선순위 PoC로 정리한 포트폴리오.
tags: [d15, risk, schema, table, "xref:d17"]
keywords: [혁신과제, 품질 관리, 리스크 분석, 안전 모니터링, 회복탄력성, Digital Twin, 현장 신호, PoC 평가, 사이버 보안, 점수 체계, 리스크 관리, 품질 보증, 안전 시스템, 평가 점수, PoC 우선순위, 디지털 트윈, CAPA, 공급망 복원력]
related: [OI-D15-01, OI-D15-02, OI-D15-03, OI-D15-04, OI-D15-05, OI-D15-06, OI-D15-07, OI-D15-08, OI-D15-09, OI-D15-10, OI-D15-11, OI-D15-12, OI-D15-13, OI-D15-14, OI-D15-15]
priority: normal
domain: D15
section: D15-11
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 1430
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-11 O/I Opportunity Portfolio

아래 점수는 공개사실이 아니라 D17 선별용 **분석 점수(1~5점, 총 25점)**다. 평가축은 `안전·현금 영향`, `내부 Data 필요성과 확보 가능성`, `6~12개월 PoC`, `의사결정 연결성`, `외부협업 필요성`이다.

| O/I ID | 후보과제 | 핵심 기능 | 외부 Partner 유형 | KPI | 점수 |
|---|---|---|---|---|---:|
| `OI-D15-01` | Enterprise Risk Knowledge Graph | 사건·Exposure·통제·손실·계약·Owner 연결 | GRC·Knowledge graph | risk linkage coverage | 24 |
| `OI-D15-02` | Process-to-Field Quality Digital Thread | 소재·공정·검사·BMS·보증·Return 연결 | Industrial data fabric·QualityTech | genealogy coverage, diagnosis time | 25 |
| `OI-D15-03` | Defect Population & Recall Scope Engine | 증거기반 포함/제외·Unknown Tail·Scenario | Graph analytics·Reliability AI | population precision/recall | 25 |
| `OI-D15-04` | Early Field Failure Signal Fusion | DTC·Telemetry·Complaint·Warranty·Text 이상탐지 | Connected vehicle·NLP·Anomaly AI | signal-to-triage time | 25 |
| `OI-D15-05` | Cross-Plant Common-Cause Detector | 공장·고객·Supplier의 유사 Failure Cluster | Causal AI·Federated analytics | common-cause lead time | 24 |
| `OI-D15-06` | CAPA Evidence & Effectiveness Agent | 원인·조치·변경·효과·수평전개 추적 | Quality workflow·Document AI | recurrence, closure quality | 24 |
| `OI-D15-07` | Safety-Critical Change Control Twin | Recipe·PLC·검사모델·BMS·설비 MOC | Configuration/ALM·Digital twin | unauthorized change, rollback time | 25 |
| `OI-D15-08` | Plant SHE Barrier Health Monitor | Gas·Thermal·HV·LOTO·Permit·Maintenance Leading KRI | Sensor analytics·EHSTech | impairment hours, HiPo closure | 24 |
| `OI-D15-09` | Battery Incident & Reignition Response Twin | 사고·SOC·열·격리·이송·보관 대응 | Fire SafetyTech·Digital twin | response time, reignition control | 23 |
| `OI-D15-10` | OT Cyber–Safety Guardrail | Asset·Zone·Access·Patch·Backup·Safety 독립성 | OT security·IEC62443 integrator | critical asset coverage, restore pass | 25 |
| `OI-D15-11` | Climate & Utility Resilience Twin | 홍수·폭염·전력·용수와 Plant/Supplier Criticality | Climate analytics·GIS·Resilience | downtime-at-risk, RTO pass | 23 |
| `OI-D15-12` | Alternative-Site Qualification Navigator | 제품·공정·고객승인·Tooling·Data의 이전 준비 | PLM·Qualification workflow | transfer lead time | 23 |
| `OI-D15-13` | Warranty & Tail-Risk Exposure Simulator | Population·Failure·Remedy·Cash·보험 Scenario | Actuarial·Reliability analytics | forecast calibration, tail coverage | 23 |
| `OI-D15-14` | Crisis Command & BCP Orchestrator | Decision Log·RTO/RPO·Stakeholder·Recovery Task | CrisisTech·Workflow | decision/RTO time, action closure | 24 |
| `OI-D15-15` | Risk-adjusted Portfolio Stress Engine | 수요·정책·원료·가동·CAPEX·유동성 복합 Stress | Decision intelligence·Optimization | loss avoided, trigger lead time | 24 |

### 우선 PoC 5개

| 우선순위 | 후보 | 6~12개월 PoC 범위 | 성공조건 |
|---:|---|---|---|
| 1 | `OI-D15-02 Process-to-Field Quality Digital Thread` | 미국 1개 공장·1개 OEM Program·과거 Return Sample | Material–Cell–Pack–VIN–Field–CAPA 재현 |
| 2 | `OI-D15-03 Defect Population & Recall Scope Engine` | 과거 1개 품질사건 Back-test | 포함·제외 근거, Unknown Tail, Reviewer 재현 가능 |
| 3 | `OI-D15-04 Early Field Failure Signal Fusion` | OEM 승인 Telemetry·Warranty·Complaint의 제한 Data | 기존 수동 Review보다 조기탐지, False Alarm 통제 |
| 4 | `OI-D15-10 OT Cyber–Safety Guardrail` | 1개 Line의 Critical Asset·Remote Access·Backup | 안전정지 독립성·Restore·변경승인 시험 통과 |
| 5 | `OI-D15-08 Plant SHE Barrier Health Monitor` | Formation/Aging 또는 전해액 영역 1개 | Barrier Impairment·HiPo Near Miss 조기경보와 종결률 개선 |

### PoC 공통 설계

```yaml
d15_poc_common_design:
  baseline:
    - one_event_or_failure_mode_one_program_one_plant
    - current_manual_signal_triage_population_containment_CAPA_and_recovery
    - known_denominator_genealogy_gap_and_control_test_history
  validation:
    - blinded_back_test_and_prospective_shadow_mode
    - false_negative_false_positive_and_unknown_tail
    - quality_SHE_cyber_legal_customer_and_plant_signoff
    - CAPA_recurrence_and_control_effectiveness_validation
  decision_safety:
    - no_autonomous_stop_start_release_recall_notification_or_root_cause_finalization
    - safety_interlocks_independent_from_AI_and_optimization
  security:
    - purpose_based_access_to_OEM_employee_supplier_contract_and_field_data
    - model_rule_input_output_action_reviewer_and_version_lineage
    - federated_or_minimum_necessary_data_for_cross_company_analysis
```

---
