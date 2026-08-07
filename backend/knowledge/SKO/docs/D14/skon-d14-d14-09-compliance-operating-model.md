---
id: skon-d14-d14-09-compliance-operating-model
title: Compliance Operating Model
summary: "규제·세무·무역 컴플라이언스 운영을 위한 폐쇄형 정책루프, 기능별 책임분담(RACI), 증빙 관리, KPI 지표를 정의한다."
tags: [d14, policy, table]
keywords: [규제 준수, RACI 책임분담, 증빙 추적, 세액공제, PFE/MACR, 관세 통관, EU Battery, 성과지표, Policy-to-Decision Closed Loop, UFLPA, CBAM, 증빙 관리, KPI, 원산지 확정, Clawback, 탄소발자국]
related: []
priority: normal
domain: D14
section: D14-09
source: SK온_D14_Policy_Regulation_Incentives_Compliance.md
breadcrumb: "SK온 D14 — Policy, Regulation, Incentives & Compliance"
tokens: 849
updated: 2026-08-03
---

> SK온 · D14 정책·규제·인센티브·컴플라이언스 · SK온 D14 — Policy, Regulation, Incentives & Compliance

## D14-09 Compliance Operating Model

### 1. Policy-to-Decision Closed Loop

```text
Official Source Ingestion
→ Version / Effective-date Parsing
→ Applicability Mapping
→ Evidence Request and Data Reconciliation
→ Tax·Legal·Trade·EHS Review
→ Claim / Certification / Filing / Product Release
→ Audit / Cash / Market-access Outcome
→ Rule and Model Feedback
```

### 2. RACI 최소구조

| 활동 | Accountable | Responsible | Consulted |
|---|---|---|---|
| 45X·한국 세액공제 | CFO/Tax Head | Tax·Plant Finance | Legal·Operations·IT |
| PFE/MACR | Tax·Legal 공동 | Procurement Compliance·Cost Accounting | Supplier·Trade·Audit |
| UFLPA·관세·CBAM | Trade Compliance Head | Customs·Logistics | Procurement·Legal·Finance |
| EU Battery Passport | EU Product Compliance Head | Product Data·Quality·IT | OEM·Plant·LCA·Cybersecurity |
| EU Due Diligence | Sustainability/Compliance Head | Procurement·ESG·Audit | Legal·Supplier·Notified Body |
| Chemical Regulation | EHS/Product Stewardship Head | EHS·R&D·Procurement | Plant·Quality·Legal |
| Incentive Covenant | CFO/Project Sponsor | Tax·HR·Plant Finance·Government Affairs | Legal·PMO·JV |

### 3. Evidence Control

- 법령 원문, 번역, AI 요약, 법무·세무 확정 Memo를 별도 저장한다.
- 신고와 제품출시에 사용된 Rule Version·입력 Snapshot·계산 Hash·승인자를 고정한다.
- Supplier Certificate는 만료·범위·서명권자·Reason-to-know 검사를 거친다.
- Passport 공개정보와 영업비밀·개인데이터의 Access Layer를 분리한다.
- Tax Credit, Tariff, Carbon Footprint, Recycled Content에서 동일 BOM을 쓰더라도 각 법적 산식과 범위는 별도 유지한다.
- 법령 변경이 Contract Change-in-law, 고객가격, Supplier Allocation, CAPEX Gate에 미치는 영향을 자동 배포한다.
- AI는 신고제출·원산지확정·Supplier 차단·세액공제 청구를 자율 실행하지 않는다.

### 4. 핵심 KPI

| KPI | 정의 |
|---|---|
| `regulatory_coverage` | 중요 의무 중 Owner·Scope·기한·증빙이 연결된 비율 |
| `eligibility_traceability` | Claim 금액 중 제품·공장·Lot·원문까지 추적 가능한 비율 |
| `evidence_first_pass_rate` | 첫 Review에서 보완 없이 통과한 증빙 비율 |
| `policy_change_lead_time` | 공식변경 감지부터 영향대상 Owner 통지까지 시간 |
| `clawback_at_risk` | 미충족 Covenant에 연결된 잠재 상환액 |
| `detention_and_hold_time` | 통관보류 건수·금액·해제 Lead Time |
| `passport_completeness` | Mandatory Field 중 검증된 최신값 비율 |
| `carbon_and_mass_balance_gap` | Plant Ledger와 Product Declaration 차이 |
| `credit_to_cash_reconciliation` | Eligible→Claimed→Recognized→Cash 차이 |

---
