---
id: skon-d09-d09-07-d17-bridge
title: D17 Bridge
summary: "고객과 수주 정보가 제품기술, 공급능력, 규제, 재무 등 7개 도메인과 연결되는 방식을 정의한 표와, 의사결정 기준, D17 전달 규칙을 제시한 문서"
tags: [d09, customer, oi-seed, schema, table, "xref:d17", "xref:d03", "xref:d04", "xref:d06"]
keywords: [도메인 연결, 고객 용량, 계약 관리, 의사결정 체계, 전달 규칙, Forecast, Capacity 계획, Margin, OEM, OI 기회, 고객 Pain Point, Forecast-Capacity 연계, 도메인 통합, 용량 계획, Margin 검증, CAPEX 회수, 품질 탐지, 의사결정 기준]
related: []
priority: normal
domain: D09
section: D09-07
source: SK온_D09_Customers_Orders_OEM_Relationships.md
breadcrumb: "SK온 D09 — Customers, Orders & OEM Relationships"
tokens: 611
updated: 2026-08-03
---

> SK온 · D09 고객·수주·OEM 관계 · SK온 D09 — Customers, Orders & OEM Relationships

## D09-07 D17 Bridge

### 1. 다른 도메인과의 연결

| D09 정보 | 연결 도메인 | D17에서 사용할 질문 |
|---|---|---|
| 고객·Program·Cell Revision | D03·D04 | 어떤 제품·기술이 어느 고객 Pain Point를 해결하는가? |
| 고객수요·공장·Line·승인 | D06·D07 | 계약수요를 실제 공급 가능한 Capacity로 바꿀 수 있는가? |
| 고객 Program과 소재원산지 | D08 | 미국·EU 정책요건을 충족하는 공급경로인가? |
| 가격·보상·Margin | D11 | 수주 확대가 반복 가능한 이익으로 이어지는가? |
| 고객 Nomination과 CAPEX | D12 | 신규 Line·전환투자가 계약기간 안에 회수되는가? |
| Claim·Warranty | D15 | 고객 불만과 Field 품질을 조기에 탐지할 수 있는가? |
| 고객 Roadmap·경쟁사 | D16 | 고객의 다음 Platform을 선점할 기술은 무엇인가? |

### 2. D17 전달 규칙

```yaml
d17_handoff_rule:
  mandatory_fields:
    - oi_seed_id
    - customer_or_segment
    - quantified_problem_proxy
    - decision_owner
    - required_internal_data
    - potential_external_partner_type
    - poc_duration
    - success_kpi
    - source_ids
  gates:
    - remove_duplicates_with_D06_D07_D08
    - verify_internal_data_availability
    - estimate_ROI_and_change_management_cost
    - confirm_customer_data_and_contract_security
    - prohibit_autonomous_contract_decisions
```

### 3. 핵심 해석

SK온의 고객문제는 단순히 `신규 OEM을 더 확보하는 것`이 아니다. 공개자료상 기존 고객의 수요변동, Ford 관계 재편, Nissan·Slate의 미래 물량, Flatiron을 시작으로 한 ESS Pipeline이 동시에 존재한다. 따라서 가장 큰 O/I 기회는 영업 Lead 생성만이 아니라 **계약–Forecast–고객승인 Capacity–출하–수익성**을 하나의 의사결정 체계로 연결하는 데 있다.

---
