---
id: skon-d13-d13-01-contract-governance-data-model
title: Contract & Governance Data Model
summary: 계약·JV·거버넌스 관련 엔터티 구조와 계약 구속력 및 의무 이행 상태 분류를 정의하는 데이터 모델
tags: [d13, contract, schema, table]
keywords: [엔터티 설계, 계약 구속력, 의무 상태 추적, 거버넌스 의사결정, 자본금 호출, 권리 라이센스, 계약 변경 및 해지, 분쟁 클레임, 지급 트리거, 당사자 관계, 엔터티, 의무 상태, 거버넌스 모델, 계약 관리, LegalParty, AgreementFamily, 이행 추적, 권리의무]
related: []
priority: normal
domain: D13
section: D13-01
source: SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md
breadcrumb: "SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure"
tokens: 875
updated: 2026-08-03
---

> SK온 · D13 계약·JV·거버넌스·파트너십 · SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

## D13-01 Contract & Governance Data Model

### 1. 핵심 엔터티

| 엔터티 | 기본 키 | 최소 필드 |
|---|---|---|
| `LegalParty` | `legal_party_id` | 법인명·등록국·그룹·역할·보증관계·권한자 |
| `AgreementFamily` | `deal_id` | 사업목적·Master/JV/License/Supply/Finance 문서 묶음 |
| `AgreementVersion` | `agreement_id + version` | 체결일·효력일·만기·구속력·준거법·상위문서 |
| `Clause` | `clause_id + version` | 원문 위치·Clause Type·요약·기밀등급·Reviewer |
| `RightObligation` | `obligation_id` | obligor·beneficiary·행위·수량·기한·조건·상태 |
| `GovernanceBody` | `body_id` | Board·위원회·Working Group·구성·Quorum·권한 |
| `ReservedMatter` | `matter_id` | 의사결정 항목·승인 Threshold·Veto·Escalation |
| `CapitalCall` | `call_id` | 요청·납입기한·분담근거·미납·Remedy·보증 |
| `MilestoneAcceptance` | `milestone_id` | 기술·설비·납품 기준·증빙·승인·Payment Trigger |
| `IPDataRight` | `right_id` | Background/Foreground·Owner·License·Field·Territory·Data |
| `ChangeWaiver` | `change_id` | Amendment·Deviation·Waiver·영향·승인·유효기간 |
| `ClaimDispute` | `event_id` | 원인·Notice·Cure·금액·책임·상태·Resolution |
| `TransferExit` | `exit_id` | 양도·Change of Control·해지·자산·부채·사후의무 |
| `DecisionAudit` | `decision_id` | 입력문서 Version·승인자·반대의견·조건·사후검증 |

### 2. 계약 구속력 Vocabulary

```yaml
agreement_status:
  NON_BINDING_MOU:
    meaning: 협력방향 또는 협상범위만 공개, 확정 구매·투자 의무로 집계 금지
  CONDITIONAL_DEFINITIVE:
    meaning: 본계약이나 선행조건·기술검증·승인 충족 전
  ACTIVE_BINDING:
    meaning: 유효한 확정계약이 공개되었으나 세부 Call-off는 별도
  ACTIVE_PARTLY_OPTIONAL:
    meaning: 확정분과 Option·ROFO·우선협상 범위가 함께 존재
  ACTIVE_R_AND_D_ONLY:
    meaning: 연구·검증용 권리이며 상업생산권으로 확대 금지
  RESTRUCTURED:
    meaning: 당사자·자산·부채·권리의무가 변경됨
  TERMINATED_OR_EXPIRED:
    meaning: 해지·만료·청산으로 원 계약관계 종료
  NOT_DISCLOSED:
    meaning: 공개자료로 법적 상태·조항을 확정할 수 없음
```

### 3. 의무 상태와 증빙

```text
Proposed → Contracted → Conditional → Due → Performed → Accepted
                                      ↘ Disputed / Waived / Breached
Amended → Superseded → Transferred → Terminated → Surviving Obligation
```

`Performed`와 `Accepted`는 다르다. 설비 설치·Cell 납품·보고서 제출이 완료되어도 상대방 검수와 Payment Trigger가 충족됐는지 별도 증빙이 필요하다.

---
