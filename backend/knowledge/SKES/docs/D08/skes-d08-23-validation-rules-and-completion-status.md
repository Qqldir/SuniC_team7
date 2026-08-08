---
id: skes-d08-23-validation-rules-and-completion-status
title: Validation Rules and Completion Status
summary: "공급망 데이터베이스 구축의 검증 결과, 완성도 수준, 미확보 정보 및 제약사항은?"
tags: [d08, supply-chain, table, "xref:d06", "xref:d07", "xref:d09", "xref:d17"]
keywords: [LNG 계약, 발전소 설비, 도시가스, 수소 충전, 공급사 관리, 데이터 검증, 메트릭, 미확보 정보, 공급망 DB, 제약사항]
related: []
priority: normal
domain: D08
section: 23
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 690
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 23. Validation Rules and Completion Status

## 23.1 Structural Validation

| Test | Result |
|---|---|
| production/offtake/tolling/TUA types separated | PASS |
| Freeport 2.2mtpa and Woodford 1.1mtpa not forced to match | PASS |
| Barossa equity/offtake/Darwin rights separated | PASS |
| Boryeong physical capacity and E&S TUA separated | PASS |
| operating/planned/historical relationships separated | PASS |
| KCE project-specific suppliers not generalized | PASS |
| undisclosed city-gas/power vendors not invented | PASS |
| nominal LH₂ capacity and actual flow separated | PASS |
| supplier ESG pool and actual assessments separated | PASS |
| D06 process and D07 asset handover included | PASS |
| confidential contract terms marked internal | PASS |
| O/I benefit attribution gate included | PASS |

## 23.2 Known Limitations

1. LNG 계약가격·월별 entitlement·take-or-pay·destination flexibility는 공개되지 않았다.
2. 3·4호 LNG선 실명·사양·용선조건은 내부확인이 필요하다.
3. 발전소별 OEM·LTSA·critical-spare 공급사 원장은 공개되지 않았다.
4. 도시가스 법인별 도매공급·자재·시공사 명단은 공개범위가 제한적이다.
5. Jeonnam OWF1 package vendor의 완전한 contract map은 확보되지 않았다.
6. KCE cell 제조공장·원산지·보증조항은 프로젝트별 내부자료가 필요하다.
7. EverCharge tier-2 BOM·AVL·SBOM은 공개되지 않았다.
8. 인천 LH₂ feed 계약·OEM·trailer/충전소별 물량은 공개되지 않았다.
9. CCS는 상용조달보다 기술협력·실증·계획 비중이 높다.

## 23.3 Completion Summary

| Metric | Count |
|---|---:|
| Source records | 37 |
| Public contract/right records | 12 |
| Material/service classes | 34 |
| End-to-end flow records | 16 |
| Supplier/partner nodes | 37 (named + controlled placeholders) |
| Supply-risk records | 32 |
| O/I Pain Points | 30 |
| O/I Seeds | 60 |
| P0 shortlist | 10 |
| Internal data requests | 28 |
| AI retrieval chunks | 14 |

**D08 status: COMPLETE / REPRESENTATIVE_COMPANY_DEEP_DB**

**Primary handoff:** D09 고객·offtake DB와 D17 O/I 과제 추천에서 `supplier_id`, `contract_id`, `material_id`, `flow_id`, `asset_id`, `process_id`, `risk_id`, `seed_id`를 공통키로 사용한다.
