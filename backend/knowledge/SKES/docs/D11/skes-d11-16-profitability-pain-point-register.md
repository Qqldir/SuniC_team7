---
id: skes-d11-16-profitability-pain-point-register
title: Profitability Pain-Point Register
summary: SK이노베이션 E&S의 LNG·발전·신에너지 등 에너지 사업에서 발생하는 33개 수익성 이슈와 경제적 누수 원인을 정리한 매트릭스
tags: [d11, cost, table]
keywords: [LNG 마진, 수익성 누수, 열효율, 신에너지, 고객별 원가, 원가배부, PPA 최적화, 데이터 폐쇄]
related: [PAIN-ENS-D11-001, PAIN-ENS-D11-002, PAIN-ENS-D11-003, PAIN-ENS-D11-004, PAIN-ENS-D11-005, PAIN-ENS-D11-006, PAIN-ENS-D11-007, PAIN-ENS-D11-008, PAIN-ENS-D11-009, PAIN-ENS-D11-010, PAIN-ENS-D11-011, PAIN-ENS-D11-012, PAIN-ENS-D11-013, PAIN-ENS-D11-014, PAIN-ENS-D11-015, PAIN-ENS-D11-016, PAIN-ENS-D11-017, PAIN-ENS-D11-018, PAIN-ENS-D11-019, PAIN-ENS-D11-020, PAIN-ENS-D11-021, PAIN-ENS-D11-022, PAIN-ENS-D11-023, PAIN-ENS-D11-024]
priority: normal
domain: D11
section: 16
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 1293
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 16. Profitability Pain-Point Register

| Pain ID | 문제 | 경제적 누수 | 내부 확인 | Priority |
|---|---|---|---|---|
| `PAIN-ENS-D11-001` | 전사·Segment·법인·자산 Scope 혼합 | 잘못된 Margin·중복합산 | consolidation bridge | P0 |
| `PAIN-ENS-D11-002` | 계절성과 구조적 수익성 혼합 | Q1/Q3 과대해석 | weather/maintenance normalization | P0 |
| `PAIN-ENS-D11-003` | LNG 계약별 Margin 불투명 | 고정의무·옵션가치 누락 | contract/cargo P&L | P0 |
| `PAIN-ENS-D11-004` | Equity gas·장기계약·Spot 원가 혼합 | Portfolio 선택 왜곡 | source-specific landed cost | P0 |
| `PAIN-ENS-D11-005` | 액화·터미널 사용권 미활용 | use-or-pay 고정비 | reserved vs used capacity | P0 |
| `PAIN-ENS-D11-006` | Cargo ETA·Demurrage·BOG 분절 | 물류·재고 Margin 누수 | cargo event ledger | P1 |
| `PAIN-ENS-D11-007` | 내부 LNG Transfer Price와 외부이익 혼합 | 이익 중복 | elimination mapping | P0 |
| `PAIN-ENS-D11-008` | 발전 열효율과 연료원가 분리 | 원인 없는 Margin 변동 | heat-rate-to-P&L | P0 |
| `PAIN-ENS-D11-009` | 계획·비계획 정지 동일 처리 | 정비효과 오판 | outage counterfactual | P0 |
| `PAIN-ENS-D11-010` | CHP 전력·열 원가배부 불일치 | 사업별 수익성 왜곡 | joint-cost policy | P1 |
| `PAIN-ENS-D11-011` | 도시가스 기상효과 미분리 | 수요예측·예산오차 | customer weather model | P0 |
| `PAIN-ENS-D11-012` | 고객별 Cost-to-Serve 부재 | 저수익 고객 식별불가 | call/visit/meter ledger | P1 |
| `PAIN-ENS-D11-013` | 미계량·누출·계량오차 통합 | 손실원인 불명 | network mass balance | P0 |
| `PAIN-ENS-D11-014` | PPA MW와 실제 MWh 혼동 | 매출 과대계상 | interval settlement | P0 |
| `PAIN-ENS-D11-015` | PPA Shape·Curtailment 누락 | 계약 Margin 누수 | load-generation match | P0 |
| `PAIN-ENS-D11-016` | 개발 Pipeline을 확정 NPV로 처리 | 자산가치 과대평가 | stage probability | P0 |
| `PAIN-ENS-D11-017` | BESS Gross Revenue 중심 평가 | 열화·충전비·담보 누락 | lifecycle net margin | P0 |
| `PAIN-ENS-D11-018` | 입찰 AI의 Counterfactual 부재 | Uplift 검증불가 | shadow bid replay | P0 |
| `PAIN-ENS-D11-019` | BESS Revenue 집중도 미관리 | 시장포화 Tail Risk | product concentration | P1 |
| `PAIN-ENS-D11-020` | 충전 Port 수를 수익으로 간주 | 저가동 자산 확장 | session/port economics | P0 |
| `PAIN-ENS-D11-021` | Demand Charge 미최적화 | Site Margin 악화 | interval load | P0 |
| `PAIN-ENS-D11-022` | Truck Roll·설치초과비용 분절 | CTS 누락 | work-order-to-P&L | P1 |
| `PAIN-ENS-D11-023` | 수소 명목능력과 Paid kg 혼동 | 고정비/kg 과소평가 | production→paid waterfall | P0 |
| `PAIN-ENS-D11-024` | 차량·충전소 목표를 Firm 수요로 간주 | 가동률 과대추정 | offtake ladder | P0 |
| `PAIN-ENS-D11-025` | 액화에너지·BOG·배송 분절 | Delivered cost 누락 | kg mass/energy balance | P0 |
| `PAIN-ENS-D11-026` | CCS 발표용량을 계약물량으로 간주 | Stranded infra | firm emitter coverage | P0 |
| `PAIN-ENS-D11-027` | Capture·Storage COD 불일치 | 초기현금 Burn | synchronized milestone | P0 |
| `PAIN-ENS-D11-028` | MRV·장기책임 원가 누락 | NPV 과대 | liability reserve | P0 |
| `PAIN-ENS-D11-029` | Working Capital을 EBIT과 분리 | 현금위험 후행인지 | inventory/AR/collateral | P0 |
| `PAIN-ENS-D11-030` | 개선과제 편익 중복 | 과장된 Business Case | benefit dependency graph | P0 |
| `PAIN-ENS-D11-031` | 회피비용을 현금절감으로 보고 | 실적과제 오판 | benefit classification | P0 |
| `PAIN-ENS-D11-032` | 데이터 Close 지연 | 의사결정 후행 | close latency | P1 |
| `PAIN-ENS-D11-033` | 계약·OT·재무 ID 불일치 | 수작업 Reconciliation | master-data crosswalk | P0 |
| `PAIN-ENS-D11-034` | 안전제약 없는 최적화 | 사고·정지 Tail Loss | safety envelope | P0 |
| `PAIN-ENS-D11-035` | 자산매각 후 권리의 경제성 누락 | TUA 의무·옵션 왜곡 | ownership-rights bridge | P0 |

---
