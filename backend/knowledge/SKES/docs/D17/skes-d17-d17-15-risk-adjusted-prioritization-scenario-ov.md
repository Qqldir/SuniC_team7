---
id: skes-d17-d17-15-risk-adjusted-prioritization-scenario-ov
title: Risk-adjusted Prioritization & Scenario Overlay
summary: Urgency Overlay를 통해 스트레스 시나리오별로 포트폴리오 과제의 우선순위를 재조정하고 재검토 대상을 식별하는 프레임워크.
tags: [d17, oi-portfolio, table, "xref:d15"]
keywords: [Urgency Overlay, 스트레스 시나리오, D15, 우선순위 재검토, 트리거, 포트폴리오 위험, Hard Gate, 긴급도 평가]
related: []
priority: normal
domain: D17
section: D17-15
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 340
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-15 Risk-adjusted Prioritization & Scenario Overlay

100점 Score는 정적 사전심사다. D15 Stress Scenario가 활성화되면 **Score 자체를 임의로 고치지 않고 `Urgency Overlay`를 별도 필드로 부여**한다.

| Trigger | 우선 재검토 과제 | 이유 |
|---|---|---|
| LNG 공급/항로 충격 | 006·007·008·009·011 | 조달–재고–발전 파급 |
| 발전 forced outage / scarcity | 011·012·014 | lost-margin tail |
| 가스배관 safety signal | 016·017·019 | 공공안전 우선 |
| 해상풍력 cable/marine access | 021·022 | 긴 복구시간 |
| BESS thermal/market rule shock | 026·027·028·029 | 안전·수익 동시 영향 |
| H2 barrier impairment | 036·037·038 | SHE 우선, 경제최적화 후순위 |
| CCS emitter FID delay | 041·042·043·044 | sunk cost·bankability |
| K-ETS/Tax rule update | 002·046·047·048 | 현금·시장접근 |
| OT cyber advisory / incident | 056·057·058·060 | critical service resilience |
| Project/permit deadline slip | 052·053·055 | NPV·option value |

`Urgency`가 높아져도 Hard Gate를 우회하지 않는다.

---
