---
id: skon-d15-d15-08-governance-raci-kpi
title: "Governance, RACI & KPI"
summary: "기업 리스크 관리의 3선 조직모델, 중대사건 보고 기준, 그리고 12개의 품질·안전 성과KPI를 정의하는 거버넌스 체계"
tags: [d15, risk, table]
keywords: [Three-line model, Risk escalation, Signal to triage, Genealogy coverage, CAPA effectiveness, Near miss, Barrier impairment, Field failure rate, Risk Owner, Escalation Trigger, CAPA, Near Miss, 원인분석, 성과KPI, BCP, 중대사건, Containment]
related: []
priority: normal
domain: D15
section: D15-08
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 836
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-08 Governance, RACI & KPI

### 1. Three-line Operating Model

| Line | 역할 | D15 책임 |
|---|---|---|
| 1선 | Plant·Product·Program·Procurement·IT/OT Owner | Risk 소유, 통제운영, 사건보고, Containment·CAPA |
| 2선 | Quality·SHE·ERM·Cyber·Compliance·Legal·Finance | 정책·방법론·Challenge·Aggregation·Escalation |
| 3선 | Internal Audit·독립 Assurance | 통제설계·운영효과·Data Lineage 독립검증 |
| Board/Executive | Risk Appetite·중대사건·자본배분 | Tail Risk·Acceptance·Recovery 투자 승인 |

SK이노베이션은 Audit and Corporate Compliance Committee를 Compliance와 Business Risk의 Control Tower로 공개한다. D15는 이 상위구조와 SK온의 법인·공장·제품 Risk Owner를 연결하되, 공개되지 않은 내부 위원회 상세를 임의 구성하지 않는다. ([SK이노베이션 Governance](https://www.skinnovation.com/esg/governance))

### 2. Escalation Trigger 예시

- 인명·화재·폭발·환경방출 또는 잠재 중대 Near Miss
- 동일/유사 Failure Mode의 여러 공장·고객·국가 출현
- Affected Population 또는 원인범위의 불확실성이 확대
- Safety-critical Barrier·Genealogy·Field Monitoring의 장시간 불능
- 고객 Stop Ship·Line Stop·규제기관 조사·리콜 가능성
- 보험·계약 통지기한 또는 법정 신고기한 임박
- Liquidity·Covenant·Clawback과 연결되는 복합 Risk

### 3. KPI Dictionary

| KPI | 정의 |
|---|---|
| `signal_to_triage_time` | 최초 Signal부터 책임자·중대성·즉시조치 결정까지 |
| `genealogy_coverage` | 출하품 중 Material–Cell–Pack–Customer까지 재현 가능한 비율 |
| `population_precision_recall` | 확인 불량 포함률과 정상품 과잉포함률을 함께 측정 |
| `containment_lead_time` | Trigger부터 Line/Shipment/Field 노출 차단까지 |
| `root_cause_confidence` | Association→Mechanism→Reproduced→Verified 분포 |
| `CAPA_effectiveness_and_recurrence` | 효과검증 완료율·동일/유사 Failure 재발률 |
| `field_failure_rate_by_exposure` | 판매·운행·kWh·시간 등 적절한 분모 기반 Field Rate |
| `barrier_impairment_hours` | Safety-critical Barrier가 저하·우회된 누적시간 |
| `high_potential_near_miss_closure` | 중대 잠재 Near Miss의 원인·조치·효과검증 완료율 |
| `BCP_RTO_RPO_test_pass` | 복구시험에서 목표시간·Data 손실기준 통과율 |
| `cross_plant_learning_latency` | 검증된 CAPA부터 영향 Site 적용완료까지 |
| `residual_risk_acceptance_overdue` | 만료 또는 조건위반 Risk Acceptance 수·Exposure |

---
