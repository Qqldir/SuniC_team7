---
id: skon-d03-10-2-chunk-retrieval-rules
title: Chunk Retrieval Rules
summary: "SK온 AI 지식 베이스에서 정보를 검색할 때 적용하는 사실 우선 검색, 상태 필터링, 출처 검증, 시간 연관성 등 8가지 규칙을 명시한다."
tags: [d03, product, schema]
keywords: [검색 우선순위, 출처 신뢰도, 상태 필터, COMMERCIAL, 프로토타입, temporal relevance, 사양 미공개, 경쟁사 주장, 사실 기반, 정보검색 규칙, 청크 필터링, 사실우선, 상태분류, 출처신뢰도, 시간연관성, 검증, source authority]
related: []
priority: normal
domain: D03
section: 10.2
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 499
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 10.2 Chunk Retrieval Rules

```yaml
retrieval_rules:

  rule_01:
    name: Fact-first retrieval
    instruction: >
      FACT 청크를 먼저 검색하고, ANALYSIS 청크는 사실관계를 보완하는
      용도로만 사용한다.

  rule_02:
    name: Commercial-status filter
    instruction: >
      사용자가 현재 판매제품을 질문하면 COMMERCIAL, CONTRACTED,
      APPLICATION_CONFIRMED 상태만 우선 반환한다.

  rule_03:
    name: Prototype warning
    instruction: >
      PROTOTYPE, R&D, CORPORATE_TARGET 청크에는 답변에서 상태표시를
      반드시 포함한다.

  rule_04:
    name: Source authority
    priority:
      - Official filing and report
      - Official product page
      - Official press release
      - Government or research institute
      - Reputable news
      - Analysis

  rule_05:
    name: Temporal relevance
    instruction: >
      최신 공식 자료와 과거 자료가 충돌하면 최신 자료를 우선하되
      과거 값은 삭제하지 않고 HISTORICAL_VALUE로 보존한다.

  rule_06:
    name: Measurement boundary
    instruction: >
      셀, 팩, 차량, 컨테이너 성능을 서로 직접 비교하지 않는다.

  rule_07:
    name: Competitor claim
    instruction: >
      경쟁사 제조사 주장은 MANUFACTURER_CLAIM 태그를 유지하고
      독립 검증값으로 바꾸지 않는다.

  rule_08:
    name: Missing specification
    instruction: >
      미공개 사양은 유사제품 데이터로 보완하지 않고 NOT_DISCLOSED를
      반환한다.
```

---
