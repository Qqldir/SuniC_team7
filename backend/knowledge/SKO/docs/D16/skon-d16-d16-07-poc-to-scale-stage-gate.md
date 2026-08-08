---
id: skon-d16-d16-07-poc-to-scale-stage-gate
title: PoC-to-Scale Stage Gate
summary: "PoC를 본운영으로 확대할 때 통과해야 할 8개 게이트와 각 단계별 필수 산출물, 통과 기준, 중단 조건을 규정한 표준 프로세스이다."
tags: [d16, ecosystem, schema, table]
keywords: [PoC, Stage Gate, 데이터보안, 백테스트, 섀도우모드, 독립검증, 상용화, 가드레일, TCO, 배포, 스케일링, 단계게이트, PoC검증, 오프라인백테스트, 롤아웃, AI안전성, Guardrail, KPI, 중단조건]
related: []
priority: normal
domain: D16
section: D16-07
source: SK온_D16_External_Solutions_Startups_Vendors_Open_Innovation_Ecosystem.md
breadcrumb: "SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem"
tokens: 838
updated: 2026-08-03
---

> SK온 · D16 외부 솔루션·스타트업·벤더 생태계 · SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem

## D16-07 PoC-to-Scale Stage Gate

### 1. Gate 구조

```text
G0 Problem Proof
→ G1 Data / Security / IP Readiness
→ G2 Offline Back-test
→ G3 Shadow Mode
→ G4 Bounded Live PoC
→ G5 Independent Outcome Validation
→ G6 Scale Architecture and Commercial Gate
→ G7 Multi-site Deployment
→ G8 Post-implementation Review / Exit
```

| Gate | 필수 산출물 | 통과 기준 | 중단 조건 |
|---|---|---|---|
| G0 | Pain Point·Owner·Baseline·금액/시간/안전 영향 | 문제와 KPI 재현 | Solution-first 과제 |
| G1 | Data Map·DPA·IP·Cyber·OT·법률 승인 | 최소권한·분리환경·파기조건 | 무제한 학습·Export 불가 |
| G2 | 과거 Data Back-test·Leakage Check | 기존 Rule/Model 대비 유의한 개선 | 미래정보 Leakage·불안정 결과 |
| G3 | 실제 운영 Shadow Prediction | Drift·Latency·False Alarm 허용 | 작업자 혼란·안전 Guardrail 미흡 |
| G4 | 한정 Line/Product/Site 적용 | Human Approval 하 KPI 개선 | 품질·안전·생산 악화 |
| G5 | Finance·Quality·SHE·Legal 독립검증 | 성과·부작용·재현성 승인 | Vendor 자체평가만 존재 |
| G6 | TCO·Support·Exit·Template | Scale Business Case 승인 | 통합비·변경비가 편익 초과 |
| G7 | 표준 Rollout·Training·Monitoring | Site별 성과와 Control 유지 | Local Exception 누적 |
| G8 | PIR·Model/Contract Update·Exit | 가정과 실제 차이를 다음 과제에 반영 | Zombie PoC 유지 |

### 2. PoC 공통 템플릿

```yaml
poc_record:
  pain_point_id_and_domain: null
  provider_solution_and_version: null
  internal_owner_and_operator: null
  hypothesis_and_counterfactual: null
  scope_site_line_product_period: null
  baseline_and_control_group: null
  data_fields_access_retention_and_training_rights: []
  safety_quality_cyber_legal_and_customer_constraints: []
  kpi_primary_secondary_and_guardrail: []
  evidence_level_before_and_after: null
  implementation_cost_internal_hours_and_TCO: null
  stop_scale_and_exit_criteria: []
  decision_log_and_approvers: []
```

### 3. AI·OT·Safety Guardrail

- 생산조건 추천은 먼저 Offline·Shadow Mode에서 검증하고 PLC Write 권한을 부여하지 않는다.
- Sensor/Inspection AI는 False Negative뿐 아니라 False Reject로 인한 Scrap·Throughput 손실도 함께 측정한다.
- Battery Health·Safety Alert는 OEM/BESS Operator의 Action Protocol과 연결하되 자동 Shutdown·Recall 판단은 별도 승인한다.
- DPP·PFE/MACR·UFLPA 시스템은 Evidence를 수집·정렬할 수 있지만 최종 적격·법률·세무판정은 담당자가 승인한다.
- Contract AI는 원문 Clause·Amendment·효력일을 보존하고 요약문만으로 의무를 실행하지 않는다.

---
