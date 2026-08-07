---
id: skon-d14-d14-12-o-i-opportunity-portfolio
title: O/I Opportunity Portfolio
summary: "정책·규제·준수 영역에서 SK온이 추진하는 AI/디지털 기회과제 15개의 평가 점수, 외부 파트너 유형, 우선순위 PoC를 담은 포트폴리오."
tags: [d14, policy, schema, table, "xref:d17"]
keywords: [규제대응, 인센티브, 컴플라이언스, BOM, MACR, 탄소발자국, Battery Passport, 45X, PoC, 원산지, 규제준수, 공급망추적성, GRC, CBAM]
related: [OI-D14-01, OI-D14-02, OI-D14-03, OI-D14-04, OI-D14-05, OI-D14-06, OI-D14-07, OI-D14-08, OI-D14-09, OI-D14-10, OI-D14-11, OI-D14-12, OI-D14-13, OI-D14-14, OI-D14-15]
priority: normal
domain: D14
section: D14-12
source: SK온_D14_Policy_Regulation_Incentives_Compliance.md
breadcrumb: "SK온 D14 — Policy, Regulation, Incentives & Compliance"
tokens: 1427
updated: 2026-08-03
---

> SK온 · D14 정책·규제·인센티브·컴플라이언스 · SK온 D14 — Policy, Regulation, Incentives & Compliance

## D14-12 O/I Opportunity Portfolio

아래 점수는 공개사실이 아니라 D17 선별을 위한 **분석 점수(1~5점, 총 25점)**다. 평가축은 `현금·시장접근 영향`, `내부 데이터 확보 가능성`, `6~12개월 PoC`, `의사결정 연결성`, `외부 협업 필요성`이다.

| O/I ID | 후보과제 | 핵심 기능 | 외부 Partner 유형 | KPI | 점수 |
|---|---|---|---|---|---:|
| `OI-D14-01` | Regulatory Obligation Knowledge Graph | 법령 Version·의무·법인·제품·증빙·Owner 연결 | RegTech·Knowledge graph | obligation coverage, missed duty | 25 |
| `OI-D14-02` | Policy-to-BOM Eligibility Engine | BOM·시설·원산지·거래별 제도 적용판정 | Rules engine·TaxTech | eligibility accuracy | 24 |
| `OI-D14-03` | 45X Qualified-kWh Evidence Agent | 생산·시험·판매·신고·현금 Reconciliation | TaxTech·Manufacturing analytics | qualified-kWh, audit exceptions | 25 |
| `OI-D14-04` | PFE/MACR Compliance Engine | 소유·통제·계약·직접재료원가·Lot 판정 | Trade/Tax RegTech·Graph | MACR coverage, review lead time | 25 |
| `OI-D14-05` | UFLPA Pre-clearance Traceability Pack | Shipment 전 Upstream 문서수집·Gap 경보 | Supply-chain traceability·Document AI | detention rate, clearance time | 24 |
| `OI-D14-06` | EU Battery Passport Data Fabric | Model·개별 Battery·Lifecycle·Access API | DPP·Data space·Cybersecurity | passport completeness | 25 |
| `OI-D14-07` | Product Carbon-footprint Assurance Twin | Plant Energy·BOM·물류·수율 기반 LCA와 검증 | LCA SaaS·MRV·Digital twin | verified kgCO2e/kWh | 24 |
| `OI-D14-08` | Recycled-content Mass-balance Ledger | Scrap·Black Mass·재생소재·제품별 Co/Li/Ni 추적 | Circularity platform·Blockchain | mass-balance variance | 24 |
| `OI-D14-09` | Incentive Covenant & Clawback Monitor | 고용·투자·생산·보고·Consent·현금 연결 | Grant/TaxTech·Workflow | retained benefit, clawback-at-risk | 25 |
| `OI-D14-10` | Tariff–CBAM Landed-cost Simulator | HTSUS/CN·원산지·탄소·관세 Scenario | CustomsTech·Carbon analytics | landed-cost forecast error | 23 |
| `OI-D14-11` | Regulatory Change Impact Twin | 변경법령을 BOM·계약·공장·수요·현금에 전파 | Legal NLP·Decision intelligence | change-to-action lead time | 24 |
| `OI-D14-12` | Chemical Substitution & Approval Navigator | PFAS/NMP Scenario와 대체재·고객승인 경로 | ChemInformatics·EHSTech | substitution lead time | 22 |
| `OI-D14-13` | Multi-regime Audit Evidence Control Tower | Tax·Trade·DPP·ESG 증빙의 공통 Lineage | GRC·Audit analytics | first-pass rate, duplicate work | 24 |
| `OI-D14-14` | Public Funding Eligibility Radar | 시설·기술·지역·Stage별 Grant/Loan/Tax 기회 | Grant intelligence·FinTech | eligible funding captured | 21 |
| `OI-D14-15` | Policy-adjusted Plant & Product Allocator | 정책현금·관세·탄소·수요를 공장배정에 반영 | Optimization·S&OP analytics | contribution margin, compliance pass | 24 |

### 우선 PoC 5개

| 우선순위 | 후보 | 6~12개월 PoC 범위 | 성공조건 |
|---:|---|---|---|
| 1 | `OI-D14-04 PFE/MACR Compliance Engine` | 미국 1개 Cell·Module 제품군과 P0 소재 | 모든 구성재료의 PFE Cost·Lot·Certificate·Reviewer 연결 |
| 2 | `OI-D14-03 45X Qualified-kWh Evidence Agent` | 미국 1개 공장 3개월 생산·판매 | 생산~Claim~현금의 이중계상 0건, Audit Exception 감소 |
| 3 | `OI-D14-06 EU Battery Passport Data Fabric` | Hungary 1개 OEM Program·1개 Battery Model | Mandatory Field·Unique ID·권한·Update API 검증 |
| 4 | `OI-D14-09 Incentive Covenant & Clawback Monitor` | Georgia 또는 Tennessee 1개 Project | 모든 Covenant에 Owner·증빙·기한·Exposure 연결 |
| 5 | `OI-D14-01 Regulatory Obligation Knowledge Graph` | 미국·EU 핵심법령 10개와 2개 공장 | 법령변경이 영향 Product·Owner·Decision에 자동 전달 |

### PoC 공통 설계

```yaml
d14_poc_common_design:
  baseline:
    - official_legal_instrument_and_version
    - entity_facility_line_product_material_shipment_scope
    - current_manual_decision_and_evidence_pack
  validation:
    - tax_legal_trade_EHS_product_compliance_signoff
    - back_test_against_filed_claims_customs_entries_and_product_releases
    - reconcile_eligible_claimed_recognized_cash_and_clawback
    - preserve_unknown_and_conflicting_evidence
  decision_safety:
    - no_autonomous_tax_filing_origin_ruling_customs_declaration_or_product_release
    - no_supplier_blocking_or_contract_change_without_human_approval
  security:
    - role_based_access_for_tax_cost_contract_supplier_and_passport_data
    - source_clause_rule_version_input_snapshot_hash_and_reviewer_lineage
    - external_data_sharing_by_purpose_and_minimum_necessary_fields
```

---
