---
id: skes-d15-1-enterprise-risk-data-model
title: Enterprise Risk Data Model
summary: 리스크·통제·실패모드 등 12개 엔티티의 데이터 구조와 리스크/이슈/인시던트/손실의 구분 기준을 정의하는 E&S 모델
tags: [d15, risk, schema, table]
keywords: [RiskEvent, FailureMode, KRI, 통제, LossEvent, 리스크-이슈-인시던트-손실, RecoveryPlan, 근접사건]
related: []
priority: normal
domain: D15
section: 1
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 742
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 1. Enterprise Risk Data Model

## 1.1 Core Entities

| Entity | Key | 최소 필드 |
|---|---|---|
| `RiskEvent` | `risk_event_id + version` | category·trigger·detected_at·state·owner·cause_confidence |
| `ExposureUnit` | `exposure_id` | legal entity·asset·contract·market·customer·route·jurisdiction |
| `FailureMode` | `fm_id` | function·failure·cause·local effect·end effect·detection·barrier |
| `Signal` | `signal_id` | source·timestamp·unit·baseline·threshold·quality·latency |
| `KRI` | `kri_id + version` | formula·direction·window·threshold·owner·action |
| `Control` | `control_id + version` | preventive/detective/corrective/recovery·owner·test·evidence |
| `Incident` | `incident_id` | start/end·severity·affected assets·notification·timeline |
| `LossEvent` | `loss_id` | safety·volume·downtime·margin·cash·legal·reputation·insured/uninsured |
| `Scenario` | `scenario_id` | shock·duration·dependencies·probability state·impact ranges |
| `RecoveryPlan` | `recovery_id` | critical service·RTO·RPO·minimum service·alternate·test result |
| `DecisionLog` | `decision_id` | time·input version·approver·action·reason·override·next review |
| `RiskAcceptance` | `acceptance_id` | residual risk·approver·expiry·conditions·reopen trigger |

## 1.2 Canonical Risk Record

```yaml
risk_id: RISK-ENS-D15-XXXX
title: string
category: operational|market|safety|financial|contract|regulatory|cyber|climate|strategic
exposure:
  legal_entity_id: string
  asset_ids: []
  contract_ids: []
  market_ids: []
  jurisdiction: []
trigger: string
kri_ids: []
failure_mode_ids: []
controls: []
control_evidence: []
inherent_risk: qualitative_or_internal
residual_risk: INTERNAL_REQUIRED
loss_path: []
recovery_id: string
owner: INTERNAL_REQUIRED
escalation_owner: INTERNAL_REQUIRED
source_ids: []
as_of: 2026-08-06
d17_seed_ids: []
```

## 1.3 Risk–Issue–Incident–Loss 구분

| 상태 | 의미 | 예시 |
|---|---|---|
| Risk | 미래 목표에 영향을 줄 불확실성 | LNG route disruption 가능성 |
| Issue | 이미 존재하는 문제, 손실범위 미확정 | 특정 compressor 진동 추세 악화 |
| Incident | 통제 또는 운영상태가 이탈한 사건 | compressor trip로 생산중단 |
| Near Miss | 손실은 회피했지만 동일 원인으로 중대사건 가능 | gas detector alarm 후 누출 전 isolation |
| Loss Event | 영향이 실현 | 미공급·정지·LD·repair·margin loss |
| Control Failure | 설계/운영 통제가 기대대로 작동하지 않음 | trip signal 미전달, stale rule 적용 |

---
