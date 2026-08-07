---
id: skes-d17-d17-01-domain-boundary-evidence-rules
title: Domain Boundary & Evidence Rules
summary: "D17 프로젝트 평가를 위한 핵심 질문 10개, 데이터 상태 분류표, 그리고 E&S 평가에서 피해야 할 8가지 오해를 정의하는 기준문서다."
tags: [d17, oi-portfolio, core-candidate, table]
keywords: [검증 기준, Pain Point, Failure Mode, 데이터 상태분류, 가설 검증, E&S 익스포저, 프로젝트 평가, PoC, 금지 오류]
related: []
priority: critical
domain: D17
section: D17-01
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 884
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-01 Domain Boundary & Evidence Rules

## 1. D17이 반드시 답해야 하는 10개 질문

1. 어떤 Pain/Failure Mode가 실제 E&S Exposure와 연결되는가?
2. 문제의 분모는 `Cargo`, `MWh`, `GJ`, `customer`, `site`, `kg-H2`, `tCO2`, `KRW cash` 중 무엇인가?
3. 현재 의사결정자는 누구이며 어떤 시스템·Excel·계약·운전절차를 쓰는가?
4. 현재 Control이 있는데도 왜 Gap이 남는가?
5. 필요한 외부 Capability는 Tool·Sensor·Algorithm·Data·Engineering·Verification 중 무엇인가?
6. 무엇을 E&S 내부 Core로 남기고 무엇을 Buy/Partner/Co-develop할 것인가?
7. 가장 작은 검증범위에서 Baseline·Counterfactual을 어떻게 만들 것인가?
8. 안전·법률·세무·Cyber·JV·OEM Warranty 중 어떤 Hard Gate가 적용되는가?
9. 성공을 정확도 하나가 아니라 현금·원가·가동·안전·Lead time으로 어떻게 검증할 것인가?
10. Scale·Re-negotiate·Internalize·Stop 중 어떤 종료경로를 미리 확보할 것인가?

## 2. 사실·분석·가설 상태

| State | 의미 | 사용 규칙 |
|---|---|---|
| `VERIFIED_FACT` | 공식자료·내부 원장·검증된 실적 | 날짜·주체·Scope·Source 유지 |
| `EXTERNAL_REFERENCE` | 외부 고객사/벤더/표준의 공개사례 | Capability prior로만 사용; E&S ROI로 복사 금지 |
| `ANALYTICAL_DERIVATION` | 사실을 결합한 계산·점수·관계 | 산식·가정·분모·Version 저장 |
| `HYPOTHESIS` | PoC로 검증할 인과·가치가설 | realized benefit으로 표시 금지 |
| `INTERNAL_REQUIRED` | 공개자료에 없는 운전·손익·계약·권리 | 내부 Owner 확인 전 승인 금지 |
| `STALE_OR_CONFLICTED` | 시점 충돌·상반된 자료 | Human review 전 추천 차단 |

## 3. E&S에서 특히 금지하는 오해

- LNG 장기계약 물량, 터미널 사용권, Cargo 실인수량, 발전소 소비량을 같은 `LNG Capacity`로 합산하지 않는다.
- 발전소 명목용량을 실제 가용 MW·시장기여·열공급능력과 동일시하지 않는다.
- JV/SPV 총자산·총CAPEX를 E&S 단독 경제적 Exposure로 기록하지 않는다.
- BESS `pipeline MW`, `interconnection MW`, `operating MW`, `dispatchable MW`를 합산하지 않는다.
- 수소 MOU·정책목표·생산능력을 `firm paid kg`로 바꾸지 않는다.
- CCS 발표 저장용량·기술용량을 `firm contracted tCO2`로 바꾸지 않는다.
- 벤더의 절감률·정확도·ROI를 E&S 예상효과로 전이하지 않는다.
- AI가 단독으로 발전 Dispatch, BESS Bid, ESD/SIS, 가스차단, 계약·세무판정, CAPEX Commit을 실행하지 않는다.

---
