---
id: skes-d00-d00-01-domain-master
title: Domain Master
summary: "SK이노베이션 E&S의 데이터 영역을 17개 도메인으로 구분하고 각 도메인의 명칭, 소유 데이터 범위, 대표 참조키를 정리한 마스터 테이블."
tags: [d00, governance, table, "xref:d01", "xref:d02", "xref:d03", "xref:d04"]
keywords: [도메인 분류, 데이터 소유권, 참조키, 기업정보, 사업포트폴리오, 공급사, 고객계약, 자산, 스냅샷, 기준본, 데이터 도메인, canonical name, 마스터데이터, 엔티티, D00-D17, 도메인 정의, SK이노베이션]
related: []
priority: normal
domain: D00
section: D00-01
source: SK이노베이션E&S_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master"
tokens: 776
updated: 2026-08-06
---

> SK이노베이션 E&S · D00 소스·엔티티·ID·변경이력 마스터 · SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master

## D00-01 Domain Master

| Domain | Canonical Name | 원본으로 소유하는 데이터 | 대표 참조키 |
|---|---|---|---|
| D01 | Corporate Identity | 법인·조직·명칭·합병·지배관계 | `legal_entity_id`, `org_id` |
| D02 | Business Portfolio | LNG·발전·도시가스·재생·수소 등 사업영역 | `portfolio_id`, `business_model_id` |
| D03 | Products & Solutions | 전력·가스·PPA·BESS·EV충전·수소·CCS 서비스 | `product_id`, `solution_id` |
| D04 | Technology Taxonomy | 발전·가스·재생·저탄소·Digital 기술 | `technology_id`, `capability_id` |
| D05 | R&D, Patents & IP | R&D·특허·라이선스·기술권리 | `rnd_program_id`, `patent_family_id` |
| D06 | Process & Operations | Value Chain·공정·운영·의사결정 | `process_id`, `decision_id` |
| D07 | Footprint, Assets & Capacity | 터미널·발전소·배관·풍력·BESS·수소·해외자산 | `asset_id`, `capacity_event_id` |
| D08 | Supply Chain & Procurement | LNG·설비·EPC·부품·물류·공급사 | `supplier_id`, `supply_event_id` |
| D09 | Customers, Orders & Contracts | 고객·수요·PPA·도시가스·Offtake | `customer_id`, `contract_event_id` |
| D10 | Market & Competition | 시장·가격·규칙·경쟁사·전망 | `market_id`, `forecast_id` |
| D11 | Cost & Economics | 원가·마진·Unit Economics·민감도 | `economic_scope_id`, `cost_event_id` |
| D12 | CAPEX & Funding | 투자·PF·차입·보조금·Real Option | `project_id`, `funding_event_id` |
| D13 | JV, Contracts & Governance | JV·계약·권리·의무·의사결정·Exit | `agreement_id`, `clause_id` |
| D14 | Policy & Compliance | 법령·허가·시장제도·세액공제·보고의무 | `rule_id`, `obligation_id` |
| D15 | Risk & Resilience | Failure Mode·KRI·Control·BCP·복구 | `risk_id`, `control_id`, `scenario_id` |
| D16 | External Solution Ecosystem | 기술·벤더·실증·E&S Fit·PoC | `provider_id`, `evidence_id` |
| D17 | O/I Task Recommendation | 과제·우선순위·Gate·Roadmap | `oi_seed_id`, `oi_task_id` |

### 기준본 선택 규칙

- `_v2_보강본`은 비교·보존용 중간본이며 D00 Snapshot 집계에서는 제외한다.
- D02·D03의 Canonical 기준본은 보강 내용이 반영된 기본 파일이다.
- Domain 파일명·SHA-256·줄 수·URL 출현 수는 `SK이노베이션E&S_D00_Cross_Domain_Audit.json`을 권위 원장으로 사용한다.
- 향후 파일 내용이 바뀌면 Snapshot ID와 해시를 갱신하고 기존 Snapshot은 삭제하지 않는다.

---
