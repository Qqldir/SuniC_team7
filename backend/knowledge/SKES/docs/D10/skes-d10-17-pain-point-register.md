---
id: skes-d10-17-pain-point-register
title: Pain Point Register
summary: "LNG, 전력, 도시가스, 재생에너지 등 에너지 사업 전체에서 식별된 30개 pain point의 ID, 근본원인, 영향 KPI, 우선순위를 정리한 관리 표다."
tags: [d10, market, table, "xref:d11"]
keywords: [LNG, 근본원인, 우선순위, BESS, 재생에너지, 도시가스, PPA, 문제점]
related: [PAIN-ENS-D10-001, PAIN-ENS-D10-002, PAIN-ENS-D10-003, PAIN-ENS-D10-004, PAIN-ENS-D10-005, PAIN-ENS-D10-006, PAIN-ENS-D10-007, PAIN-ENS-D10-008, PAIN-ENS-D10-009, PAIN-ENS-D10-010, PAIN-ENS-D10-011, PAIN-ENS-D10-012, PAIN-ENS-D10-013, PAIN-ENS-D10-014, PAIN-ENS-D10-015, PAIN-ENS-D10-016, PAIN-ENS-D10-017, PAIN-ENS-D10-018, PAIN-ENS-D10-019, PAIN-ENS-D10-020, PAIN-ENS-D10-021, PAIN-ENS-D10-022, PAIN-ENS-D10-023, PAIN-ENS-D10-024]
priority: normal
domain: D10
section: 17
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 1327
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# 17. Pain Point Register

| Pain ID | Pain Point | Segment | Root cause | KPI affected | Priority |
|---|---|---|---|---|---|
| `PAIN-ENS-D10-001` | LNG exposure가 계약별 silo | LNG | IDs 불일치 | portfolio cost | P0 |
| `PAIN-ENS-D10-002` | cargo optionality 수기평가 | LNG | scenario engine 부재 | option value | P0 |
| `PAIN-ENS-D10-003` | freight·route shock 반영 지연 | LNG | event data 단절 | delivered cost | P1 |
| `PAIN-ENS-D10-004` | terminal inventory와 trading 분리 | LNG | system interface | demurrage/BOG | P0 |
| `PAIN-ENS-D10-005` | fuel price→SMP 전파 설명 부족 | power | lag model 부재 | margin forecast | P0 |
| `PAIN-ENS-D10-006` | CHP 전력·열 공동손익 미흡 | CHP | separate optimization | joint margin | P0 |
| `PAIN-ENS-D10-007` | flexibility 가치 미계량 | power | energy-only KPI | asset value | P1 |
| `PAIN-ENS-D10-008` | 도시가스 기상·구조수요 혼합 | city gas | normalization 부족 | forecast error | P0 |
| `PAIN-ENS-D10-009` | 전기화 churn signal 부재 | city gas | customer/building data 단절 | volume retention | P1 |
| `PAIN-ENS-D10-010` | 산업고객 fuel-switch 경제성 수기 | city gas | price/carbon data 단절 | sales conversion | P1 |
| `PAIN-ENS-D10-011` | 재생 pipeline MW 과대집계 | renewable | stage probability 없음 | forecast accuracy | P0 |
| `PAIN-ENS-D10-012` | grid queue/COD 위험 분산 | renewable | permit·grid IDs 단절 | COD | P0 |
| `PAIN-ENS-D10-013` | curtailment-adjusted yield 부족 | renewable | congestion data 부족 | revenue | P1 |
| `PAIN-ENS-D10-014` | PPA load·generation shape 불일치 | PPA | interval data silo | imbalance | P0 |
| `PAIN-ENS-D10-015` | PPA lead의 bankability 불명 | PPA | credit/site gate 부족 | conversion | P1 |
| `PAIN-ENS-D10-016` | 24/7 CFE portfolio 수기 | PPA | optimization 부재 | hourly coverage | P1 |
| `PAIN-ENS-D10-017` | BESS pipeline와 운영 혼합 | BESS | status taxonomy 오류 | market share | P0 |
| `PAIN-ENS-D10-018` | merchant alpha 검증 어려움 | BESS | control/counterfactual 부족 | margin uplift | P0 |
| `PAIN-ENS-D10-019` | degradation cost bid 미반영 | BESS | SOH-economic bridge 없음 | lifecycle margin | P0 |
| `PAIN-ENS-D10-020` | rule change 반영 지연 | BESS | manual interpretation | compliance/margin | P1 |
| `PAIN-ENS-D10-021` | 충전 site TAM 과대평가 | EV | power/parking gate 없음 | conversion | P0 |
| `PAIN-ENS-D10-022` | port 수와 활성 이용 혼합 | EV | metric definition | ARR/port | P0 |
| `PAIN-ENS-D10-023` | fleet departure SOC 예측 부족 | EV | route·session data 단절 | SLA | P1 |
| `PAIN-ENS-D10-024` | H2 MOU를 수요로 오인 | H2 | stage discipline 부족 | utilization | P0 |
| `PAIN-ENS-D10-025` | 차량·station·fuel rollout 불일치 | H2 | multi-party schedule | sold kg | P0 |
| `PAIN-ENS-D10-026` | boil-off 포함 원가 불명 | H2 | mass balance 단절 | cost/kg | P1 |
| `PAIN-ENS-D10-027` | CCS 발표·확정 capacity 혼합 | CCS | stage taxonomy 부족 | pipeline value | P0 |
| `PAIN-ENS-D10-028` | emitter와 storage matching 부재 | CCS | cross-border data gap | contracted tCO2 | P0 |
| `PAIN-ENS-D10-029` | MRV 책임·증빙 단절 | CCS | contract/sensor 분리 | verification | P1 |
| `PAIN-ENS-D10-030` | 경쟁사 signal이 action과 미연결 | all | news collection 중심 | decision lead time | P0 |
| `PAIN-ENS-D10-031` | 전망 version이 overwrite됨 | all | lineage 부재 | forecast audit | P0 |
| `PAIN-ENS-D10-032` | 단위·기간 다른 수치 비교 | all | metadata 누락 | decision quality | P0 |
| `PAIN-ENS-D10-033` | market signal owner 불명 | all | workflow 부재 | response time | P1 |
| `PAIN-ENS-D10-034` | 외부자료와 내부 KPI 연결 부족 | all | entity crosswalk 없음 | adoption | P0 |
| `PAIN-ENS-D10-035` | scenario별 손익 연결 없음 | all | D10-D11 bridge 부족 | capital decision | P0 |
| `PAIN-ENS-D10-036` | 경쟁사 claim 검증 부족 | all | source tier 미적용 | benchmark error | P1 |
| `PAIN-ENS-D10-037` | policy target를 demand로 간주 | all | claim status 오류 | TAM | P0 |
| `PAIN-ENS-D10-038` | project attrition 미반영 | all | probability model 없음 | pipeline value | P0 |
| `PAIN-ENS-D10-039` | human override 학습 미흡 | all | decision log 부재 | model adoption | P1 |
| `PAIN-ENS-D10-040` | 데이터권리 미확인 | all | contract registry 부족 | PoC feasibility | P0 |

---
