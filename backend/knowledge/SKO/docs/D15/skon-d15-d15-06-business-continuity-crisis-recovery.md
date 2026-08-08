---
id: skon-d15-d15-06-business-continuity-crisis-recovery
title: "Business Continuity, Crisis & Recovery"
summary: "서비스 중요도별 복구 목표를 정의한 BCP 티어 분류표와 위기 상황의 의사결정, 사건 종료 절차를 다룬 정책"
tags: [d15, risk, schema, table]
keywords: [BCP, Service Tier, RTO/RPO, 위기관리, 안전상태, 데이터무결성, 의사결정로그, 재해복구, 사업연속성, 서비스 티어, 위기 관리, 의사결정, 복구 절차, 데이터 무결성]
related: []
priority: normal
domain: D15
section: D15-06
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 489
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-06 Business Continuity, Crisis & Recovery

### 1. BCP Service Tier

| Tier | Critical Service | 목표 | 최소 Recovery Evidence |
|---|---|---|---|
| `T0` | 인명·화재·환경·HV Safety Control | 즉시 안전상태 | 독립 Interlock·비상전원·통신·Drill |
| `T1` | Serial Genealogy·출하보류·Recall Population | 안전·품질판정 지속 | Read-only Replica·Offline 조회·무결성검증 |
| `T2` | MES·LIMS·WMS·Supplier/Customer EDI | 제한 생산·자재·납품 | RTO/RPO·수동절차·복구시험 |
| `T3` | S&OP·원가·정책·계약·재무분석 | 의사결정 복구 | Data snapshot·우선순위·대체 Workflow |
| `T4` | 장기개선·BI·비핵심 Collaboration | 단계 복구 | Backlog·재처리·Data reconciliation |

### 2. Crisis Decision Log

```yaml
crisis_decision:
  incident_id: null
  timestamp_and_time_zone: null
  known_unknown_conflicting_facts: []
  safety_and_legal_thresholds: []
  decisions:
    - stop_line_hold_ship_notify_customer_or_regulator: null
      decision_owner_and_approvers: []
      evidence_snapshot: []
      next_review_time: null
  communications:
    employee_contractor_customer_regulator_community: []
  recovery:
    RTO_RPO_alternative_site_manual_workaround: []
  after_action:
    lessons_CAPA_horizontal_deployment: []
```

### 3. Recovery 종료조건

생산재개만으로 사건을 종료하지 않는다. `안전상태 → Data 무결성 → 제품격리·Release → 고객/규제 의무 → Backlog·재고 정합 → CAPA 효과 → 보험·법률·재무 반영 → 수평전개`까지 상태를 분리한다.

---
