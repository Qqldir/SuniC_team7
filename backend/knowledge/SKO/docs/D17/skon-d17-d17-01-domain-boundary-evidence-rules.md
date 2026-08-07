---
id: skon-d17-d17-01-domain-boundary-evidence-rules
title: Domain Boundary & Evidence Rules
summary: "D17 오픈이노베이션 과제를 추천할 때 사실·분석·가설을 구분하는 검증 상태와 정보 격차를 정의하며, 내부 Pain Point 재현부터 기술 가치화까지의 의사결정 기준을 제시한다."
tags: [d17, oi-portfolio, core-candidate, table, "xref:d05", "xref:d16"]
keywords: [Pain Point, Capability, FTO, PoC, 검증사실, 정보공백, 정보공개 제약, 신뢰성 상태, D17, 오픈이노베이션, 검증 기준, 상태 분류, 기술 가치화, 내재화, 정보 격차]
related: []
priority: critical
domain: D17
section: D17-01
source: SK온_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation
tokens: 732
updated: 2026-08-03
---

> SK온 · D17 오픈이노베이션 과제 포트폴리오·AI 추천 · SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation

## D17-01 Domain Boundary & Evidence Rules

### 1. D17이 답해야 하는 질문

1. 어떤 내부 Pain Point가 실제 손실·시간·안전·시장접근 문제로 재현되는가?
2. 기존 시스템·협력·과제와 중복되지 않는 필요한 Capability는 무엇인가?
3. Core를 내부에 남기고 외부에서 확보할 Tool·Sensor·Data·IP는 무엇인가?
4. 어느 Site·Line·Product·Customer·Supplier·기간에서 안전하게 검증할 것인가?
5. 무엇을 기준으로 PoC를 중단·확장·재협상·내재화할 것인가?
6. 기술성과가 실제 `KRW/accepted-kWh`, 현금, 안전, Lead time, 시장접근으로 이어졌는가?

### 2. 사실·분석·가설 상태

| 상태 | 의미 | D17 사용 규칙 |
|---|---|---|
| `VERIFIED_FACT` | 공식문서·계약·실적·내부 시스템으로 검증 | 근거 날짜·Scope·Source를 보존 |
| `ANALYTICAL_DERIVATION` | 사실을 결합해 만든 계산·관계·점수 | 산식·가정·분모를 공개 |
| `HYPOTHESIS` | PoC로 확인해야 할 인과·효과 가설 | 실현편익으로 계산 금지 |
| `NOT_DISCLOSED` | 공개자료에 없음 | 평균값·경쟁사 수치로 대체 금지 |
| `STALE_OR_CONFLICTED` | 시점 불일치·상충 | Human review 전 추천 차단 |

### 3. 중요 Evidence Gap

- D05 공개자료 DB는 v2.0으로 완료됐으며 Patent Family 33개, Claim 사전 Map, 우선 FTO Gate 5개, 공동 IP 권리원장을 포함한다. 다만 공식 권리상태는 Decision Date 30일 이내 갱신하고, 제품 BOM·공정 Recipe·비공개 계약·최종 FTO 의견은 내부·법률 Gate가 닫히기 전 확정하지 않는다.
- Plant별 수율·원가·가동률·불량률·에너지·고객승인 Capacity는 공개되지 않았다.
- Provider별 가격·Integration·Support TCO, Startup Runway, Data/IP 조건, 실제 SK온 배포성과는 D16 Longlist만으로 확정할 수 없다.
- 고객 Forecast·Call-off·계약원문·Warranty·보험·JV Reserved Matter는 내부 승인이 필요한 제한 데이터다.

R&D·IP·License·투자 과제는 위 Gap이 닫히기 전 `P0 실행`이 아니라 `G0/G1 검증` 또는 `P2 Option`으로만 취급한다.

---
