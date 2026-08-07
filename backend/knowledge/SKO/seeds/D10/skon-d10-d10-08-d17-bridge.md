---
id: skon-d10-d10-08-d17-bridge
title: D17 Bridge
summary: "시장정보 D10에서 전략의사결정 D17로 정보를 전달할 때 필요한 도메인 연결, 필수 필드, 검증 게이트 규칙을 정의한 가이드."
tags: [d10, market, oi-seed, schema, table, "xref:d17", "xref:d03", "xref:d04", "xref:d05"]
keywords: [D10-D17, 의사결정 매트릭스, 경쟁벤치마킹, 로드맵 결정, 공장투자, BOM 최적화, 시나리오, 마켓시그널, Time-to-SOP, Capacity, 시장신호, 도메인 정보 연결, 필수 전달 필드, 검증 게이트, 경쟁사 분석, 제품 포트폴리오, 시장세그먼트, 공장 투자 결정]
related: []
priority: normal
domain: D10
section: D10-08
source: SK온_D10_Market_Competition_Industry_Dynamics.md
breadcrumb: "SK온 D10 — Market, Competition & Industry Dynamics"
tokens: 687
updated: 2026-08-03
---

> SK온 · D10 시장·경쟁·산업동향 · SK온 D10 — Market, Competition & Industry Dynamics

## D10-08 D17 Bridge

### 1. 다른 도메인과의 연결

| D10 정보 | 연결 도메인 | D17에서 사용할 질문 |
|---|---|---|
| Chemistry·Form Factor 변화 | D03·D04 | 어느 제품·기술 Roadmap을 가속·중단해야 하는가? |
| 경쟁사 R&D·양산속도 | D05·D06 | 외부협력이 내부개발보다 Time-to-SOP를 줄이는가? |
| 시장수요와 공장구성 | D07·D09 | 실제 고객승인 Capacity로 성장시장을 Capture할 수 있는가? |
| 가격·소재·현지화 | D08·D11 | 경쟁가격과 규제적격성을 동시에 달성할 BOM은 무엇인가? |
| 공장전환·신규투자 | D12 | 전환 Option의 NPV와 중단조건은 무엇인가? |
| Solution Ecosystem | D13·D16 | 직접 구축할 역량과 Partner로 확보할 역량은 무엇인가? |
| 정책·시장 Risk | D14·D15 | 정책변화와 가격전쟁에 견디는 Scenario는 무엇인가? |

### 2. D17 전달 규칙

```yaml
d17_handoff_rule:
  mandatory_fields:
    - oi_seed_id
    - market_segment_and_geography
    - market_signal_and_as_of_date
    - competitor_reference_case
    - quantified_problem_proxy
    - affected_product_customer_and_plant
    - decision_owner
    - required_internal_data
    - external_partner_type
    - poc_duration
    - success_kpi
    - source_ids
  gates:
    - use_same_scope_period_and_unit_for_competitor_comparison
    - separate_actual_guidance_forecast_and_company_claim
    - remove_duplicates_with_D04_D06_D07_D09
    - verify_internal_cost_capacity_and_qualification_data
    - separate_recurring_profit_from_credit_and_one_time_items
    - require_human_approval_for_product_capacity_and_bid_decisions
```

### 3. 핵심 해석

D10이 D17에 넘기는 핵심은 `시장이 커진다`는 일반론이 아니다. **LFP·Prismatic·ESS·AI Data Center가 성장하는 동안 SK온의 High-Nickel Pouch, 글로벌 생산거점, 고객승인, 원가와 수익구조를 어떻게 재배치할 것인가**가 과제다. 외부 솔루션은 시장정보를 더 많이 보여주는 데 그치지 않고 제품·공장·수익성 의사결정을 실제로 바꾸는 데 사용돼야 한다.

---
