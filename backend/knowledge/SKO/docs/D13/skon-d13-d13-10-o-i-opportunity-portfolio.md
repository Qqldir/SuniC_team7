---
id: skon-d13-d13-10-o-i-opportunity-portfolio
title: O/I Opportunity Portfolio
summary: SK온 계약·JV·거버넌스 부문의 15개 디지털화 후보 과제를 평가 점수(1~25점)와 PoC 우선순위로 제시한 기획표
tags: [d13, contract, schema, table, "xref:d17"]
keywords: [계약 의무 추적, Knowledge Graph, JV 거버넌스, 경제적 귀속 분석, CLM, M&A 디지털실, 계약 누수 탐지, 우선순위 평가, PoC, 의사결정 자동화, 계약의무, JV거버넌스, 위험모니터링, 출자관리, 기한알림, 클레임회수, 데이터통제, 의사결정권한]
related: [OI-D13-01, OI-D13-02, OI-D13-03, OI-D13-04, OI-D13-05, OI-D13-06, OI-D13-07, OI-D13-08, OI-D13-09, OI-D13-10, OI-D13-11, OI-D13-12, OI-D13-13, OI-D13-14, OI-D13-15]
priority: normal
domain: D13
section: D13-10
source: SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md
breadcrumb: "SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure"
tokens: 1466
updated: 2026-08-03
---

> SK온 · D13 계약·JV·거버넌스·파트너십 · SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

## D13-10 O/I Opportunity Portfolio

아래 점수는 공개사실이 아니라 D17 선별을 위한 **분석 점수(1~5점, 총 25점)**다. 평가축은 `현금·법적 Risk 영향`, `내부 데이터 확보 가능성`, `6~12개월 PoC`, `의사결정 연결성`, `외부 협업 필요성`이다.

| O/I ID | 후보과제 | 핵심 기능 | 외부 Partner 유형 | KPI | 점수 |
|---|---|---|---|---|---:|
| `OI-D13-01` | Contract–JV Obligation Knowledge Graph | 법인·계약·Clause·의무·자산·공장·Program 연결 | LegalTech·Knowledge graph | obligation coverage, orphan count | 25 |
| `OI-D13-02` | Economic Attribution Engine | 비용·Credit·자산·부채·보증·수익의 법적/경제적 귀속 분리 | Legal-finance analytics | attributed exposure coverage | 25 |
| `OI-D13-03` | Contract-to-Call-off & Acceptance Bridge | 계약총량·Option·Forecast·PO·수락량 연결 | CLM·Supply-chain analytics | forecast-to-accepted accuracy | 24 |
| `OI-D13-04` | JV Reserved-Matter Decision Radar | Board·Veto·Quorum·승인기한·Escalation 추적 | Governance workflow | decision cycle, missed consent | 23 |
| `OI-D13-05` | Capital Call & Default-Remedy Monitor | 출자요청·미납·보증·Remedy·희석 경보 | Treasury·LegalTech | overdue calls, exposure at risk | 23 |
| `OI-D13-06` | Milestone Acceptance Evidence Agent | 기술·설비·납품 Milestone과 시험·검수·지급증빙 연결 | Document AI·Quality workflow | acceptance lead time, disputed value | 24 |
| `OI-D13-07` | IP Field-of-Use & Data-Rights Guardrail | R&D/상업·공장·지역·데이터 사용범위 통제 | IPTech·Data governance | unauthorized use, rights coverage | 24 |
| `OI-D13-08` | Amendment–Waiver Lineage Engine | 변경·Side Letter·Waiver를 운영 Baseline에 전파 | CLM·Process mining | propagation time, stale obligations | 23 |
| `OI-D13-09` | Cross-Agreement Dependency Mapper | JV·공급·대출·보증·지원·IP 계약의 선행조건 연결 | Knowledge graph·Rules engine | dependency coverage | 24 |
| `OI-D13-10` | Partner Risk & Renegotiation Early Warning | 수요·신용·기술·정책·분쟁 신호와 계약권리 연결 | Risk intelligence·NLP | warning lead time, avoided loss | 22 |
| `OI-D13-11` | Contract Leakage & Claim Recovery Analytics | 가격조정·LD·Rebate·Warranty·Reimbursement 누락 탐지 | Revenue assurance·Audit analytics | cash recovered, leakage rate | 23 |
| `OI-D13-12` | JV Exit & Separation Digital Room | Asset·Debt·Guarantee·IP·직원·IT·사후의무 Closing 관리 | M&A LegalTech·Virtual data room | zero orphan obligations | 25 |
| `OI-D13-13` | Deal-Term Scenario & Negotiation Copilot | Volume·가격·CAPEX·IP·Exit 조건의 Scenario 비교 | Negotiation analytics·Legal AI | downside exposure, review cycle | 22 |
| `OI-D13-14` | Notice–Cure–Renewal Calendar Agent | 통지·치유·갱신·Option 행사기간 자동 증빙·Escalation | Workflow automation·CLM | missed deadline count | 22 |
| `OI-D13-15` | Partnership Post-Deal Review Loop | 계약가정과 실제 수요·현금·기술·Decision 결과 학습 | Decision intelligence | review coverage, assumption bias | 23 |

### 우선 PoC 5개

| 우선순위 | 후보 | 6~12개월 PoC 범위 | 성공조건 |
|---:|---|---|---|
| 1 | `OI-D13-01 Contract–JV Obligation Knowledge Graph` | HSBMA 또는 BOSK 계약군 1개 | 핵심 의무 100% Clause·Owner·증빙·법인 연결 |
| 2 | `OI-D13-02 Economic Attribution Engine` | BOSK 분리 전후 자산·Debt·Guarantee·비용 | Finance·Legal 합의 Gross-to-Net Exposure |
| 3 | `OI-D13-12 JV Exit & Separation Digital Room` | Tennessee·Kentucky Closing 사후검증 | Orphan 자산·의무 0건, 미확인 Gap 전량 Owner 지정 |
| 4 | `OI-D13-03 Contract-to-Call-off & Acceptance Bridge` | Nissan·Slate·Flatiron 중 1개 Program | Base·Option·PO·Accepted Volume 중복 0건 |
| 5 | `OI-D13-06 Milestone Acceptance Evidence Agent` | Solid Power 3계약 또는 설비계약 1개 | 검수·Payment Trigger Cycle 단축과 분쟁금액 가시화 |

### PoC 공통 설계

```yaml
d13_poc_common_design:
  baseline:
    - executed_agreement_family_and_all_amendments
    - clause_level_right_obligation_and_evidence
    - legal_entity_asset_program_and_finance_links
  validation:
    - legal_business_finance_tax_IP_and_accounting_signoff
    - preserve_original_language_translation_and_AI_summary_separately
    - reconcile_binding_base_option_forecast_PO_and_acceptance
    - reconcile_legal_obligor_economic_bearer_and_accounting_scope
  decision_safety:
    - human_approval_for_notice_waiver_amendment_claim_dispute_and_termination
    - no_legal_conclusion_from_low_confidence_extraction
  security:
    - role_based_access_and_need_to_know
    - no_model_training_on_restricted_contract_or_IP_data
    - source_page_clause_hash_version_and_reviewer_lineage
    - controlled_external_data_room_and_clean_room
```

---
