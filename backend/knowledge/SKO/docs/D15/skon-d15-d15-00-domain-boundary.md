---
id: skon-d15-d15-00-domain-boundary
title: Domain Boundary
summary: "전사 리스크 도메인의 포함·제외 범위, 위험 사건 추적의 폐쇄형 관리 흐름, 리스크 판정의 10가지 핵심 원칙을 규정한 실무 지침"
tags: [d15, risk, core-candidate, table, "xref:d14", "xref:d17", "xref:d00", "xref:d03"]
keywords: [Risk Event, Exposure, Control, Hazard, CAPA, KRI, Incident, 근본원인, 리콜, Scenario, 전사 리스크 관리, 위험 사건 추적, 포함 제외 범위, 판정 원칙, 폐쇄형 제어, 리콜·보증]
related: []
priority: critical
domain: D15
section: D15-00
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 1256
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

# SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

- 문서 버전: **v1.0.1**
- 기준일: **2026-08-03 (KST)**
- 이전 완료 지점: `D14 Policy, Regulation, Incentives & Compliance v1.0`
- 작성 방식: **실무형 요약 DB** — 공개 사건·공식 제도·산업 표준과 내부 검증 필요 항목을 분리하고, 공개되지 않은 SK온의 불량률·보증충당금·사고빈도·보험한도를 추정하지 않음
- 상위 목적: 제품·공장·공급망·고객·재무·규제 위험을 사건 단위로 연결해 조기경보·Containment·복구·학습과 D17 O/I 과제 추천에 투입
- D00 통합검수: Domain-local Source/Entity ID를 보존하고 Canonical Alias는 D00 Crosswalk로 해석한다. 사건 Population·분모·기간·원인·통제상태가 없는 수치를 전사율로 승격하지 않는다.

---

## D15-00 Domain Boundary

### 1. 도메인 정의

D15는 위험요인을 나열하는 문서가 아니다. 다음의 폐쇄형 관리 흐름을 만드는 도메인이다.

```text
Hazard / Uncertainty / Weak Signal
→ Risk Event and Affected Population
→ Product / Lot / Line / Plant / Supplier / Customer / Legal Entity Exposure
→ Preventive / Detective / Corrective / Recovery Control
→ Incident / Near Miss / Claim / Complaint / Downtime / Financial Impact
→ Containment / Root Cause / CAPA / Recall-or-Service Decision
→ Recovery / Control Validation / Cross-plant Learning
→ Residual and Aggregated Risk
→ D17 Open-Innovation Seed
```

핵심 관리단위는 `위험명`이 아니라 **특정 시점의 사건 또는 시나리오가 어떤 개체에 노출되고, 어떤 통제가 작동했으며, 잔여위험과 복구상태가 무엇인지 재현할 수 있는 기록**이다.

### 2. 포함·제외 범위

| 포함 | 제외 또는 다른 도메인 원본 |
|---|---|
| 전사 Risk Taxonomy·Risk Event·Exposure·Control·KRI·Scenario | 제품 사양·안전기술 원본은 D03·D04 |
| 제조품질–필드고장–보증–리콜의 폐쇄형 추적 | 공정 Recipe·검사·설비 원본은 D06 |
| 공장 SHE·화재·폭발·화학·고전압·작업자 안전 | 공장·Line·생산능력 원본은 D07 |
| 공급·고객·가동률·현금·계약·정책 위험의 전파경로 | 각 원장은 D08~D14 |
| OT Cyber–Safety, BCP, Crisis Command, 기후·Utility 복원력 | 법적 의무·신고 판단 원본은 D14 |
| RiskTech·QualityTech·SafetyTech·Resilience O/I 후보 | 외부 Solution 기업 원장은 D16 |

### 3. 판정 원칙

1. `Hazard`, `Risk`, `Issue`, `Incident`, `Loss`, `Control Failure`를 분리한다.
2. 공개된 단일 리콜이나 사고를 SK온 전체 품질수준으로 일반화하지 않는다.
3. Complaint·Warranty·Field Report·리콜은 발생건수뿐 아니라 판매·가동 Population과 기간을 함께 본다.
4. 결함의 상관관계는 DoE·해체분석·재현시험·CAPA 재발방지 검증 전까지 확정 원인으로 쓰지 않는다.
5. Cell·Module·Pack·Vehicle·ESS Site의 Serial과 원료 Lot·공정·검사 Genealogy가 연결되지 않으면 영향범위를 자동 확정하지 않는다.
6. Severity×Likelihood 같은 점수는 정렬용이며 예상손실·Tail Scenario·법적 중대성을 대체하지 않는다.
7. 낮은 빈도의 화재·인명·대규모 리콜 Risk는 평균빈도만으로 우선순위를 낮추지 않는다.
8. 인증서와 시험합격은 현재 통제가 유효하다는 증거 중 하나일 뿐, 무사고 보증으로 사용하지 않는다.
9. AI는 안전정지·제품출하·리콜·규제신고·보험통지·근로자 징계·고객통보를 독자 결정하지 않는다.
10. D15의 O/I 점수와 Risk Scenario는 D17 선별용 분석이며 SK온의 공식 품질·안전·법률 판단이 아니다.

---
