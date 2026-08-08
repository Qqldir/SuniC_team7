---
id: skes-d09-7-lng-power-and-heat-customer-operating-mo
title: "LNG, Power and Heat Customer Operating Model"
summary: LNG 발전소의 전력시장 진입부터 정산까지의 수급 연계 운영 흐름과 열병합발전의 열·전력 동시 최적화 운영모델을 설명하는 문서.
tags: [d09, customer, table]
keywords: [LNG nomination, heat-rate, KPX 급전, CHP, unit commitment, 열수요, 발전계획, 계량정산, SMP, HHV]
related: []
priority: normal
domain: D09
section: 7
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 700
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 7. LNG, Power and Heat Customer Operating Model

## 7.1 LNG-to-Power Demand Chain

`KPX dispatch·가격 신호 → 발전소별 발전계획 → heat-rate 기반 연료수요 → LNG nomination → cargo/terminal inventory → 발전실적 → 계량·정산`

| Stage | Data | Decision | Failure mode | O/I opportunity |
|---|---|---|---|---|
| market forecast | SMP·수요·예비력·기상 | unit commitment | 가격·수요 오차 | 확률형 dispatch 시나리오 |
| plant plan | 가용용량·열효율·정비 | 발전량 배분 | 고장·derate | fleet allocation |
| fuel conversion | heat rate·HHV | LNG 소요량 | 단위·품질 오차 | 자동 mass/energy balance |
| nomination | 일·시간대 인수계획 | terminal sendout | late change | nomination exception engine |
| actual generation | MWh·연료·배출 | 차이분석 | 계량시각 불일치 | event-time alignment |
| settlement | market·fuel·환경비 | 수익성 검토 | settlement dispute | reconciliation copilot |

## 7.2 Power-Market Relationship Boundary

- KPX는 전력 구매고객이라기보다 시장운영·급전·정산 상대다.
- KEPCO 계통은 송배전 인터페이스이며 직접 PPA에서는 망 이용과 계량 데이터의 핵심 주체다.
- 발전소별 시장등록 단위, 계량점, 정산계정과 법인 매출계정을 연결해야 한다.
- AI 추천은 가격담합·시장조작 위험을 피하고 공개 시장정보와 자사 자산정보 범위에서 사용한다.

## 7.3 CHP Heat Demand

| Driver | Required data | Hard constraint |
|---|---|---|
| 외기온·체감온도 | 시간대 기온·풍속·습도 | 최소 열공급 의무 |
| 건물 부하 | 고객군·면적·요일 | 쾌적성·공급온도 |
| 산업 증기 | 생산계획·압력·품질 | 중단비용·계약우선순위 |
| 축열·네트워크 | 탱크 SOC·공급/환수온도 | 배관·펌프 한계 |
| 전력가격 | SMP·가동비 | 열수요 우선 제약 |

CHP O/I는 전력수익만 최대화하면 실패한다. 열수요 충족, 네트워크 수리학, 최소운전, 기동비, 고객 SLA를 동시에 반영해야 한다.

---
