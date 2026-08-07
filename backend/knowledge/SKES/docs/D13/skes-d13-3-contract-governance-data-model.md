---
id: skes-d13-3-contract-governance-data-model
title: Contract & Governance Data Model
summary: 계약 당사자·의무·거버넌스 의사결정을 추적하는 15개 엔티티의 데이터 모델과 11개 조항 분류 체계를 정의한 스키마
tags: [d13, contract, schema, table, "xref:d01", "xref:d12", "xref:d08", "xref:d09"]
keywords: [JV 계약, 거버넌스, 데이터 모델, 엔티티, 조항 분류, 의무 관리, 법적 당사자, 지분, 계약 변경]
related: []
priority: normal
domain: D13
section: 3
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 912
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# 3. Contract & Governance Data Model

## 3.1 Core Entities

| Entity | Key | 최소 필드 |
|---|---|---|
| `LegalParty` | `party_id` | legal_name·jurisdiction·registration·group·role·effective_dates |
| `AgreementFamily` | `deal_id` | purpose·documents·parties·assets·business_line |
| `AgreementVersion` | `agreement_id/version` | signed·effective·expiry·binding_state·governing_law·supersedes |
| `Clause` | `clause_id/version` | type·source_location·plain_summary·confidentiality·review_status |
| `RightObligation` | `obligation_id` | obligor·beneficiary·action·quantity·deadline·condition·state |
| `JVInterest` | `interest_id` | holder·pct·direct/indirect·start/end·operator·source |
| `GovernanceBody` | `body_id` | board/committee·seats·quorum·authority·delegation |
| `ReservedMatter` | `matter_id` | subject·threshold·veto·escalation·deadlock |
| `SponsorSupport` | `support_id` | guarantor·beneficiary·type·cap·expiry·trigger |
| `DataRight` | `data_right_id` | dataset·owner·controller·access·purpose·region·retention |
| `Milestone` | `milestone_id` | deliverable·acceptance·evidence·payment/CP link |
| `ChangeWaiver` | `change_id` | amendment/waiver·approval·economic impact·expiry |
| `ClaimDispute` | `claim_id` | notice·cure·liability·amount·status·resolution |
| `TransferExit` | `exit_id` | assignment·CoC·ROFR/ROFO·put/call·termination·survival |
| `DecisionAudit` | `decision_id` | input versions·approver·conditions·decision·review date |

## 3.2 Legal Party vs Group Alias

```yaml
party_resolution:
  legal_name: exact_registered_name
  brand_name: optional
  parent_group: optional
  contract_capacity: shareholder|operator|guarantor|offtaker|supplier|lender|regulator
  valid_from: date
  valid_to: nullable
  predecessor: nullable
  successor: nullable
  do_not_merge_on_brand_only: true
```

## 3.3 Governance Decision Record

```yaml
decision:
  entity_or_jv_id: required
  meeting_body: required
  reserved_matter: true|false|unknown
  quorum_met: true|false|unknown
  vote_threshold: unanimous|majority|special|unknown
  conflicted_party_recusal: yes|no|unknown
  supporting_documents: []
  capital_commitment_change: amount_or_none
  contract_change_ids: []
  implementation_owner: required
  evidence_of_completion: []
```

## 3.4 Clause Taxonomy

| Clause family | 필수 추출값 | 연결 도메인 |
|---|---|---|
| Ownership | holder·pct·dilution·pledge | D01/D12 |
| Governance | board·quorum·veto·reserved matter | D13 |
| Capital | contribution·call·default remedy | D12 |
| Volume | min/max·option·nomination·take/use-or-pay | D08/D09 |
| Price | index·FX·pass-through·true-up | D11 |
| Capacity | right·slot·priority·reservation | D07/D11 |
| Performance | SLA·availability·acceptance·LD | D06/D15 |
| Warranty | scope·duration·exclusion·remedy | D08/D15 |
| IP/Data | background·foreground·license·data right | D05/D16 |
| Security | guarantee·LC·parent support·collateral | D12 |
| Change | law·scope·engineering·change order | D12/D14 |
| Compliance | permit·sanction·ABC·ESG | D14 |
| Liability | cap·indemnity·consequential loss | D15 |
| Termination | cause/convenience·cure·payment·transition | D12/D15 |
| Transfer | assignment·CoC·ROFR/ROFO·consent | D01/D12 |
| Dispute | notice·escalation·law·forum | D15 |

---
