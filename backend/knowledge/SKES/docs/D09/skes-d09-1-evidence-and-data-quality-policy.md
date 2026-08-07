---
id: skes-d09-1-evidence-and-data-quality-policy
title: Evidence and Data-Quality Policy
summary: "고객·계약·수요 정보의 신뢰도 등급(E1~E5), 상태 분류(DISCLOSED_CONTRACT 등), 데이터 취급 금지사항을 규정한 정책."
tags: [d09, customer, table]
keywords: [증거등급, 신뢰도, E1~E5, PPA, 계약상태, 공개여부, Hard Guardrails, 데이터검증]
related: []
priority: normal
domain: D09
section: 1
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 1058
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 1. Evidence and Data-Quality Policy

## 1.1 Evidence Tier

| Tier | 정의 | D09 허용 용도 |
|---|---|---|
| E1 | E&S·SK이노베이션·공시·공식 자회사 자료 | 고객·계약·규모·상태 확정 |
| E2 | 고객·상대방·시장운영기관 공식자료 | 관계·역할·시장규칙 교차확인 |
| E3 | 정부·공공기관·규제기관 | 수요·정산·보호의무 baseline |
| E4 | 신뢰도 높은 산업자료 | 비교·탐색·외부사례 |
| E5 | 검색 스니펫·미검증 2차자료 | 확정값 저장 금지 |

## 1.2 Claim Status

| Code | 정의 | 예시 |
|---|---|---|
| `DISCLOSED_CONTRACT` | 계약 당사자·기간·규모가 공개 | 아모레퍼시픽 20년·5MW PPA |
| `DISCLOSED_RELATIONSHIP` | 협력관계는 공개됐으나 상업조건 비공개 | AWS PPA 관계 |
| `MARKET_PARTICIPATION` | 고객이 아니라 시장 참여·정산 관계 | KCE–ERCOT |
| `MOU_OR_PLAN` | 협약·계획 단계 | 지자체 수소버스 전환 MOU |
| `OPERATING_CASE` | 설치·공급·운영이 공개 확인 | EverCharge Avis IAH 설치 |
| `PORTFOLIO_AGGREGATE` | 고객·지역 전체 합계 | 도시가스 약 510만 세대 |
| `STRUCTURAL_ANALYSIS` | 공개사실을 연결한 분석 | PPA 발전량 부족 시 정산위험 |
| `UNDISCLOSED_GAP` | 내부 확인 없이는 확정 불가 | 가격·take-or-pay·신용보강 |
| `OI_HYPOTHESIS` | 내부 데이터로 검증할 개선가설 | 수소 station 수요예측 |

## 1.3 Hard Guardrails

1. 계약전력 MW, 실제 공급 MWh, 발전설비 MW, 인증서 수량을 서로 합산하지 않는다.
2. 장기 PPA 총계약 규모와 연도별 실제 발전·소비·정산량을 분리한다.
3. MOU·업무협약·지자체 차량도입계획을 확정 발주나 최소구매의무로 표시하지 않는다.
4. KPX·KEPCO·ERCOT·NYISO는 일반 고객이 아니라 시장·망·정산 인터페이스로 분류한다.
5. KCE의 시장매출은 특정 단일 고객 매출로 배분하지 않는다.
6. 도시가스 공급세대수의 기준연도가 자회사별로 다르면 합산값에 기준일을 명시한다.
7. 고객전 수, 계량기 수, 가구 수, 계약계좌 수, 실사용 고객 수를 동일하게 취급하지 않는다.
8. 공개되지 않은 PPA 가격·에스컬레이션·불균형 부담·보증·해지조건을 추정하지 않는다.
9. PPA 고객명은 공개된 경우에만 기록하고, 그룹 내부 수요와 외부 고객을 구분한다.
10. EverCharge의 익명 사례는 고객명을 추정하지 않는다.
11. 충전기 설치대수와 동시충전 가능대수, 실제 활성 사용자 수를 구분한다.
12. 수소충전소 계획 수와 운영 수, 설계 처리량과 실제 판매량을 구분한다.
13. 고객 개인정보·결제정보·계량정보·차량정보는 목적별 최소필드만 사용한다.
14. AI는 가격·입찰·계약·고객차단을 자동 확정하지 않고 승인 가능한 추천만 제공한다.
15. 공개자료의 오래된 고객 수치는 최신값처럼 표기하지 않는다.

---
