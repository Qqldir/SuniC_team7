---
id: skon-d14-d14-01-regulatory-incentive-data-model
title: Regulatory & Incentive Data Model
summary: 규제와 정책 인센티브의 적격성·신고·증빙·현금 관리를 위한 엔터티와 상태전이 데이터 모델
tags: [d14, policy, schema, table, "xref:d11", "xref:d12"]
keywords: [법적 규범 (Legal Regulation), 혜택 지원 (Benefit, Subsidy), 자격 판정 (Eligibility), 의무사항 (Obligation, Requirement), 근거 증빙 (Evidence), 자금 흐름 (Cash Flow), 법령 상태 (Legal Status), 컴플라이언스 (Compliance), 정책 시나리오 (Policy Scenario), 세무 의무 (Tax Obligation), 규제, 법령, 적격성, 신고, 증빙, 정책, Eligibility, 엔터티, 현금흐름, 상태분류]
related: []
priority: normal
domain: D14
section: D14-01
source: SK온_D14_Policy_Regulation_Incentives_Compliance.md
breadcrumb: "SK온 D14 — Policy, Regulation, Incentives & Compliance"
tokens: 773
updated: 2026-08-03
---

> SK온 · D14 정책·규제·인센티브·컴플라이언스 · SK온 D14 — Policy, Regulation, Incentives & Compliance

## D14-01 Regulatory & Incentive Data Model

### 1. 핵심 엔터티

| 엔터티 | 기본 키 | 최소 필드 |
|---|---|---|
| `LegalInstrument` | `instrument_id + version` | 관할·기관·법령·조항·발행일·효력일·폐지·상태 |
| `Requirement` | `requirement_id` | 의무/금지/혜택·적용대상·Threshold·전환기간·예외 |
| `ApplicabilityUnit` | `scope_id` | 법인·공장·Line·제품·Material·Shipment·거래·납세연도 |
| `EligibilityDecision` | `decision_id + version` | 입력·법적근거·산식·결론·Reviewer·유효기간 |
| `EvidenceObject` | `evidence_id` | PO·Invoice·COO·Lot·원가·시험·인증·신고·Hash |
| `PolicyCashEvent` | `cash_event_id` | Eligible·Claimed·Recognized·Received·Shared·Repaid |
| `Covenant` | `covenant_id` | 고용·투자·생산·보고·유지기간·Change of Control |
| `RegulatoryCalendar` | `event_id` | 원 법정일·조건부일·최신예상일·Owner·Lead Time |
| `SubmissionAudit` | `submission_id` | 신고버전·제출자·승인자·기관·Receipt·수정·조사 |
| `PolicyScenario` | `scenario_id` | Base·변경안·발효확률·가격/수요/현금/운영 영향 |

### 2. 법적 상태 Vocabulary

```yaml
legal_status:
  ENACTED_EFFECTIVE:
    meaning: 제정되어 현재 적용 중
  ENACTED_FUTURE_EFFECTIVE:
    meaning: 제정됐으나 미래 시행일 도래 전
  EFFECTIVE_CONDITIONAL_ON_SECONDARY_ACT:
    meaning: 기본법상 일정과 위임·시행법 발효 조건을 함께 확인해야 함
  PROPOSED_OR_CONSULTATION:
    meaning: 제안·협의 단계이며 확정 의무로 사용 금지
  GUIDANCE_OR_SAFE_HARBOR:
    meaning: 행정지침·잠정 Safe Harbor, 적용기간과 Reliance 조건 확인
  TERMINATED_WITH_TRANSITION:
    meaning: 신규 적용은 종료됐으나 기존 거래·신고의 경과규정 존재
  SUPERSEDED:
    meaning: 후속 법령·개정으로 이전 Version 대체
  NOT_VERIFIED:
    meaning: 공식 원문·적용관할·최신 Version 미확인
```

### 3. 혜택·의무의 상태 분리

```text
Potential → In Scope → Eligible → Applied → Awarded / Claimed
→ Recognized → Received / Monetized → Retained
                         ↘ Audited / Adjusted / Repaid / Clawed Back
```

`Eligible`, `Claimed`, `Recognized`, `Cash Received`는 동일하지 않다. D11 손익에는 회계 인식, D12 현금에는 실제 수령과 상환의무, D14에는 법적 적격성과 증빙을 저장한다.

---
