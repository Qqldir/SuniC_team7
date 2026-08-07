---
id: skon-d15-d15-01-enterprise-risk-data-model
title: Enterprise Risk Data Model
summary: 리스크 이벤트 추적 및 대응 관리를 위해 필요한 12개 핵심 엔터티의 기본 키·필드와 상태 분류 기준을 정의한 데이터 모델
tags: [d15, risk, schema, table]
keywords: [RiskEvent, CAPA, 근본원인, 통제, Incident, 상태분류, 영향범위, 손실사건, 회복계획, 원인확신도, 리스크추적, 원인분석, 격리조치, 복구계획, 손실이벤트, 신호탐지]
related: []
priority: normal
domain: D15
section: D15-01
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 848
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-01 Enterprise Risk Data Model

### 1. 핵심 엔터티

| 엔터티 | 기본 키 | 최소 필드 |
|---|---|---|
| `RiskEvent` | `event_id + version` | 분류·발견일·상태·Trigger·원인상태·Owner |
| `ExposureUnit` | `exposure_id` | 법인·공장·Line·제품·Lot·Serial·고객·지역·계약 |
| `AffectedPopulation` | `population_id` | 생산·출하·설치·운행·보증 Population과 포함/제외 논리 |
| `Control` | `control_id + version` | 예방/탐지/대응/복구·Owner·빈도·독립성·시험결과 |
| `Signal` | `signal_id` | 검사·MES·BMS·Complaint·Warranty·Field·SHE·Cyber·외부경보 |
| `Investigation` | `investigation_id` | 가설·증거·해체·시험·인과확신·검토자 |
| `ContainmentAction` | `action_id` | Hold·Stop Ship·Sorting·SOC 제한·교체·현장점검·완료상태 |
| `CAPA` | `capa_id` | 원인·시정·예방·적용범위·효과검증·재발여부 |
| `LossEvent` | `loss_id` | 인명·품질·가동·현금·법률·평판 영향과 보험·회수 |
| `Scenario` | `scenario_id` | 가정·전파경로·기간·확률범위·영향범위·대응 Option |
| `RecoveryPlan` | `plan_id` | BCP Tier·RTO·RPO·대체 Site·수동절차·복구시험 |
| `RiskAcceptance` | `acceptance_id` | 잔여위험·승인권자·만료일·조건·재검토 Trigger |

### 2. 상태 Vocabulary

```yaml
risk_event_status:
  WEAK_SIGNAL: 통계적 또는 정성적 이상징후, 사건 여부 미확정
  UNDER_TRIAGE: 중대성·영향범위·즉시조치 판단 중
  CONTAINED: 추가 노출을 제한했으나 원인·영구조치 미완료
  ROOT_CAUSE_PROVISIONAL: 주요 원인가설이 있으나 효과검증 전
  CAPA_IN_IMPLEMENTATION: 시정·예방조치 적용 중
  EFFECTIVENESS_VALIDATION: 재발방지와 통제유효성 검증 중
  CLOSED_WITH_RESIDUAL_RISK: 종결됐으나 잔여위험·Monitoring 존재
  REOPENED: 재발·신규증거·범위확대로 재개

cause_confidence:
  OBSERVED_ASSOCIATION: 동시발생 또는 상관관계만 확인
  PLAUSIBLE_MECHANISM: 물리·화학적 기전이 합리적
  REPRODUCED: 시험에서 재현
  VERIFIED_CAUSE: 증거·재현·CAPA 효과까지 검증
```

### 3. Risk–Issue–Incident 구분

```text
Risk: 미래 목표에 영향을 줄 불확실성
Issue: 이미 발생했으나 손실 또는 안전사건으로 확정되지 않은 문제
Incident: 안전·품질·보안·운영 통제가 이탈한 사건
Loss Event: 정량 또는 정성 영향이 실현된 사건
Near Miss: 손실은 회피됐으나 동일 원인으로 중대사건 가능성이 있었던 사건
```

---
