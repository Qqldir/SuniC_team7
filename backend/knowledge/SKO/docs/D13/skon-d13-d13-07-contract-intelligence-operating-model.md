---
id: skon-d13-d13-07-contract-intelligence-operating-model
title: Contract Intelligence Operating Model
summary: 계약 조항 의무를 레코드로 기록하고 OCR/LLM 추출-법무검증-이행추적의 닫힌 루프로 자동 관리하는 모델.
tags: [d13, contract, schema]
keywords: [계약 의무, Clause Extraction, Closed-loop Review, 폐루프 검증, Obligation Record, 법무 검증, 데이터 스키마, 의무 추적, 기밀정보 관리, Master Agreement, 의무기록, 조항추출, OCR/LLM, 법무검증, Closed-loop, 이행추적, 기밀관리, 통제원칙, 권리포기]
related: []
priority: normal
domain: D13
section: D13-07
source: SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md
breadcrumb: "SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure"
tokens: 530
updated: 2026-08-03
---

> SK온 · D13 계약·JV·거버넌스·파트너십 · SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

## D13-07 Contract Intelligence Operating Model

### 1. Clause–Obligation Record

```yaml
contract_obligation_record:
  deal_id: DEAL-D13-...
  agreement_id: AGR-D13-...
  agreement_version: 1
  clause_id: CL-D13-...
  source_page_and_text_hash: null
  legal_parties: []
  obligor: null
  beneficiary: null
  obligation_type: PAYMENT|VOLUME|MILESTONE|CAPITAL_CALL|IP|REPORTING|COVENANT
  condition_precedent: []
  due_date_rule: null
  amount_or_quantity: null
  currency_or_unit: null
  evidence_required: []
  status: CONTRACTED|CONDITIONAL|DUE|PERFORMED|ACCEPTED|DISPUTED|WAIVED|TERMINATED
  economic_bearer: null
  asset_facility_program_links: []
  amendment_and_waiver_ids: []
  owner: null
  legal_reviewer: null
  confidentiality: RESTRICTED
  source_ids: []
```

### 2. 통제 원칙

- 원문·번역·AI 요약·법무확정본을 같은 필드에 덮어쓰지 않는다.
- OCR·LLM 추출에는 Clause 좌표·문서 Hash·Confidence·Reviewer를 남긴다.
- Master Agreement, JV Agreement, Supply Agreement, Financing, Incentive, Side Letter의 우선순위를 저장한다.
- 같은 의무가 여러 문서에 나타나면 중복 Count하지 않고 `governing_clause_id`를 정한다.
- 기밀 가격·IP·분쟁자료는 역할기반 접근과 Prompt/Model 학습 차단 정책을 적용한다.
- 외부 파트너와 공유하는 데이터는 Clean Room·필드 마스킹·목적제한을 적용한다.
- 계약 변경·통지·해지·권리포기는 자동 실행하지 않는다.

### 3. Closed-loop Review

```text
Clause Extraction
→ Legal Validation
→ Obligation Owner Assignment
→ Evidence / ERP·MES·Treasury Link
→ Alert / Decision / Approval
→ Performance and Leakage Measurement
→ Renewal·Renegotiation·Exit Learning
```

---
