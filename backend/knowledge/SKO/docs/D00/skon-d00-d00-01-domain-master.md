---
id: skon-d00-d00-01-domain-master
title: Domain Master
summary: SK온 데이터의 17개 도메인별 소유권과 엔티티 간 참조 ID 규칙을 정의하는 마스터 구조.
tags: [d00, governance, table, "xref:d01", "xref:d02", "xref:d03", "xref:d04"]
keywords: [데이터 도메인, 도메인 소유권, D01~D17, 캐노니컬명, 참조 아이디, entity, source, 크로스도메인, 엔티티 ID, 데이터 아키텍처, D01-D17, 참조 관계, Corporate Identity, 마스터 데이터, Canonical Name]
related: []
priority: normal
domain: D00
section: D00-01
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 1998
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-01 Domain Master

### 1. 도메인 소유권

| Domain | Canonical Name | 원본으로 소유하는 데이터 | 다른 도메인이 참조하는 방식 |
|---|---|---|---|
| `D01` | Corporate Identity | 법인·조직·명칭·지배관계·경영체계 | `legal_entity_id`, `org_id` |
| `D02` | Business Portfolio | 사업영역·제공가치·수익모델·성숙도 | `portfolio_id`, `business_model_id` |
| `D03` | Products & Solutions | Cell·Module·Pack·ESS·BaaS 제품/서비스 | `product_id`, `solution_id`, `revision_id` |
| `D04` | Technology Taxonomy | 소재·Cell·Pack·진단·제조 기술 | `technology_id`, `capability_id` |
| `D05` | R&D, Patents & IP | R&D 조직·시설·프로그램·논문·특허·권리 | `rnd_program_id`, `patent_family_id`, `rights_id` |
| `D06` | Manufacturing Process & Operations | 공정·설비역할·변수·불량·검사·운영 | `process_id`, `equipment_class_id`, `defect_id` |
| `D07` | Footprint, Plants & Capacity | 법인–공장–Line–Capacity–가동 Event | `plant_id`, `line_id`, `capacity_event_id` |
| `D08` | Raw Materials & Supply Chain | 소재·공급사·시설·원산지·공급계약·Lot 경로 | `material_id`, `supplier_id`, `origin_path_id` |
| `D09` | Customers, Orders & OEM | 고객·Program·Nomination·Call-off·수락 | `customer_id`, `program_id`, `order_event_id` |
| `D10` | Market & Competition | 시장 Snapshot·전망·경쟁사·Battlefield | `market_id`, `forecast_id`, `competitor_event_id` |
| `D11` | Cost & Profitability | Unit Economics·손익 Bridge·원가·현금 기여 | `economic_scope_id`, `cost_event_id` |
| `D12` | CAPEX & Funding | 투자안·자산·차입·보증·지원·Real Option | `project_id`, `funding_event_id`, `obligation_id` |
| `D13` | Contracts & JV Governance | 계약군·조항·권리·의무·의사결정·Exit | `agreement_id`, `clause_id`, `governance_event_id` |
| `D14` | Policy & Compliance | 법령·버전·적격성·의무·증빙·Clawback | `rule_id`, `obligation_id`, `eligibility_event_id` |
| `D15` | Enterprise Risk & Resilience | Risk Event·Exposure·Control·CAPA·복구 | `risk_event_id`, `control_id`, `scenario_id` |
| `D16` | External Solution Ecosystem | Provider·Capability·Evidence·Fit·PoC Gate | `provider_id`, `solution_id`, `evidence_id` |
| `D17` | O/I Opportunity & AI Recommendation | 통합 과제·우선순위·Dependency·Stage Gate | `oi_seed_id`, `oi_task_id`, `portfolio_id` |

### 2. 문서 Manifest

| Domain | 파일 | 유효 버전 | 기준일 | 공개자료 상태 | D00 주의사항 |
|---|---|---:|---|---|---|
| D01 | `SK온_D01_Corporate_Identity.md` | v1.0.1 | 2026-07-29 | 완료 | 번호 링크 14개를 Legacy Source로 보존·Canonical URL 연결 |
| D02 | `SK온_D02_Business_Portfolio.md` | v1.0.1 | 2026-07-29 | 완료 | 번호 링크 16개를 Legacy Source로 보존·Canonical URL 연결 |
| D03 | `SK온_D03_Products_and_Solutions.md` | v1.5.1 | 2026-07-30 | 완료 | 누적 본문과 Header Version 일치 |
| D04 | `SK온_D04_Technology_Taxonomy.md` | v1.8.1 | 2026-07-30 | 완료 | 누적 본문과 Header Version 일치 |
| D05 | `SK온_D05_RnD_Patents_and_Intellectual_Property.md` | v2.0.1 | 2026-08-03 | 공개 DB 완료 | Decision-Date FTO/권리검증 Gate 유지 |
| D06 | `SK온_D06_Manufacturing_Process_and_Operations.md` | v1.6.1 | 2026-08-02 | 완료 | 누적 본문과 Header Version 일치 |
| D07 | `SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md` | v1.3.1 | 2026-08-02 | 완료 | 누적 본문과 Header Version 일치 |
| D08 | `SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md` | v1.0.1 | 2026-08-02 | 완료 | Legacy Namespace를 명시하고 Canonical URL 연결 |
| D09 | `SK온_D09_Customers_Orders_OEM_Relationships.md` | v1.0.1 | 2026-08-03 | 공개자료 Gap 포함 완료 | D00 상태·Alias 규칙 적용 |
| D10 | `SK온_D10_Market_Competition_Industry_Dynamics.md` | v1.0.1 | 2026-08-03 | Scope 제한 포함 완료 | D00 상태·Alias 규칙 적용 |
| D11 | `SK온_D11_Cost_Profitability_Business_Economics.md` | v1.0.1 | 2026-08-03 | 내부 원가 Gap 포함 완료 | D00 Scope·단위 규칙 적용 |
| D12 | `SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md` | v1.0.1 | 2026-08-03 | 법인별 금액 Gap 포함 완료 | D00 Scope·단위 규칙 적용 |
| D13 | `SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md` | v1.0.1 | 2026-08-03 | 비공개 조항 Gap 포함 완료 | D00 Claim·상태 규칙 적용 |
| D14 | `SK온_D14_Policy_Regulation_Incentives_Compliance.md` | v1.0.1 | 2026-08-03 | 시행규칙·내부증빙 Gap 포함 완료 | D00 Time·상태 규칙 적용 |
| D15 | `SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md` | v1.0.1 | 2026-08-03 | 공개 Signal 기반 완료 | D00 Population·분모 규칙 적용 |
| D16 | `SK온_D16_External_Solutions_Startups_Vendors_Open_Innovation_Ecosystem.md` | v1.0.1 | 2026-08-03 | Provider 공개증거 기반 완료 | D00 Evidence Level 적용 |
| D17 | `SK온_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md` | v1.1 | 2026-08-03 | 내부검증 필요 | D05 v2.0·279개 Seed 반영 완료 |

### 3. 전수 Crosswalk 산출물

| 산출물 | 행 수 | 역할 |
|---|---:|---|
| `SK온_D00_Canonical_Source_Crosswalk.csv` | 511 Source + Header | 839개 URL 출현을 추적 파라미터 제거 기준 511개 Canonical URL로 연결 |
| `SK온_D00_ID_Entity_Crosswalk.csv` | 1,491 ID + Header | Source·Entity·Event·OI ID의 도메인·출현·Alias 해석 |
| `SK온_D00_D17_Seed_Lineage.csv` | 279 Seed + Header | 166개 직접참조 Seed와 113개 보류 Seed의 Disposition·과제 연결 |
| `SK온_D00_Cross_Domain_Audit.json` | 1 Snapshot | 파일·버전·URL·식별자·코드블록·각주·D17 연속성 검사결과 |

### 4. 도메인 상태 코드

| 상태 | 의미 |
|---|---|
| `COMPLETE_PUBLIC_V1` | 공개자료로 정의한 범위의 v1 완료 |
| `COMPLETE_PUBLIC_WITH_GAPS` | 공개자료 DB는 완료됐으나 내부 사실이 필요한 Gap 존재 |
| `COMPLETE_DECISION_LOGIC` | 실제 운영값이 아니라 의사결정 규칙·스키마 완료 |
| `REFRESH_REQUIRED` | 기준일 이후 변경 가능성이 높아 갱신 필요 |
| `INTERNAL_VALIDATION_REQUIRED` | 내부 원장·계약·BOM·실적 없이는 확정 불가 |
| `LEGAL_TAX_REVIEW_REQUIRED` | 법률·세무·규제 전문가의 시점별 검토 필요 |
| `SUPERSEDED` | 후속 Event/Version이 기존 레코드를 대체 |
| `HISTORICAL_ONLY` | 현재 유효성을 뜻하지 않는 역사 레코드 |

---
