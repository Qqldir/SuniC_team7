---
id: skes-d08-d09-d17-d09-d17-handover
title: D09–D17 Handover
summary: 여러 도메인에서 공급망·조달·설비·물류 영역으로 전달되는 데이터의 용도와 D17 과제에 필요한 필수 필드를 정의한 핸드오버 명세.
tags: [d08, supply-chain, table, "xref:d09", "xref:d17", "xref:d10", "xref:d11"]
keywords: [도메인 연계, 데이터 핸드오버, 가치풀, PoC, 효과측정, 공정 영향도, 공급자 의존, 게이트, 샌드박스, 과제 추천]
related: []
priority: normal
domain: D08
section: D09-D17
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 347
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 22. D09–D17 Handover

## 22.1 Cross-Domain Handover

| Domain | 전달 필드 | 용도 |
|---|---|---|
| D09 | contract·delivery·customer allocation | 공급–수요 연결 |
| D10 | price index·market·competitor route | 시장/경쟁 분석 |
| D11 | landed cost·inventory·supplier spend | 경제성 |
| D12 | long-lead package·working capital | 투자·자금 |
| D13 | contract/right·data clause·liability | 법적 구조 |
| D14 | origin·permit·sanction·ESG evidence | 규제 |
| D15 | risk·control·BCP·supplier event | 회복탄력성 |
| D16 | unmet need·vendor category·interface | 외부솔루션 탐색 |
| D17 | seed·value·data readiness·gate | 과제 추천 |

## 22.2 D17 Required Fields

| Field | 설명 |
|---|---|
| `seed_id` | D08 후보 |
| `affected_process_ids` | D06 공정 |
| `affected_asset_ids` | D07 자산 |
| `supplier/contract dependency` | 외부 의존 |
| `value_pool` | 연료비·재고·가동·안전·CAPEX |
| `minimum_data_pack` | PoC 입력 |
| `confidentiality_class` | sandbox 요구 |
| `decision_right` | 승인자 |
| `baseline_method` | 효과측정 |
| `stop/go gate` | 권리·안전·데이터 조건 |

---
