---
id: skes-d09-9-direct-ppa-and-re100-relationship-db
title: Direct PPA and RE100 Relationship DB
summary: "PPA 고객별 계약 현황, 계약-정산 프로세스의 단계별 요구사항 및 의사결정자, 에너지·신용·이행도 추적 지표를 담은 재생에너지 직거래 포트폴리오 관리 DB."
tags: [d09, customer, table]
keywords: [PPA, 재생에너지, 직거래, Offtaker, 부하, 정산, RE100, COD, MWh, 포트폴리오]
related: [PPA-ENS-D09-001, PPA-ENS-D09-002, PPA-ENS-D09-003, PPA-ENS-D09-004, PPA-ENS-D09-005, PPA-ENS-D09-006]
priority: normal
domain: D09
section: 9
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 915
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 9. Direct PPA and RE100 Relationship DB

## 9.1 PPA Customer Master

| PPA ID | Offtaker | Public status | Public scale/term | Load site | Internal gaps |
|---|---|---|---|---|---|
| `PPA-ENS-D09-001` | Amorepacific | operating/contracted | 5MW·20년 | Daejeon Daily Beauty | actual COD·MWh·price·imbalance |
| `PPA-ENS-D09-002` | SK Specialty/materials | contracted | 50MW·2024~2044 | affiliate sites | legal entities·allocation·related party |
| `PPA-ENS-D09-003` | BASF | disclosed contract | 2025 demand 16% described | Korea sites | MW·term·source assets |
| `PPA-ENS-D09-004` | LG Innotek | disclosed relationship | undisclosed | site undisclosed here | all commercial fields |
| `PPA-ENS-D09-005` | AWS | disclosed relationship | undisclosed | data-center load | profile·site·additionality |
| `PPA-ENS-D09-006` | Iljin Global | disclosed relationship | undisclosed | industrial site | term·MW·COD |

## 9.2 Contract-to-Settlement Chain

`lead → load data NDA → preliminary pricing → renewable asset match → credit review → term sheet → PPA → grid/meter registration → supply commencement → monthly meter matching → RE100 evidence → invoice/settlement → renewal/change`

| Gate | Required data | Decision owner | Failure signal |
|---|---|---|---|
| qualification | contract demand·RE100 target | sales | insufficient eligible load |
| load analysis | 15/30-min load | solution/analytics | missing or poor data |
| asset matching | generation profile·COD | renewable business | profile mismatch |
| pricing | forward price·grid charge | commercial/finance | downside exposure |
| credit | rating·guarantee | risk/finance | long-term default |
| legal | change law·curtailment·FM | legal | ambiguous allocation |
| implementation | meter·KEPCO/KPX registration | operations | COD delay |
| evidence | generation·consumption·REC | ESG/settlement | double counting |

## 9.3 PPA Demand Metrics

| Metric | Formula/meaning |
|---|---|
| Contracted MW | 계약상 기준용량; 실제 에너지 아님 |
| Delivered MWh | 계량된 재생전력 |
| Load Coverage | eligible delivered MWh / eligible customer load |
| Shape Match | 동일 시간대 발전량과 부하의 일치도 |
| Curtailment Loss | 제한발전으로 미인도된 예상 MWh |
| Imbalance Cost | 계획과 계량 차이의 정산비용 |
| Evidence Completeness | MWh 중 인증·출처가 완결된 비율 |
| COD Slippage | 계약 공급개시 대비 실제 지연 |
| Credit Exposure | 미수·향후 의무·담보의 위험액 |
| Renewal Probability | 잔여기간·성과·고객전략 기반 승인용 예측 |

## 9.4 PPA O/I White Space

- 고객 부하와 복수 발전자산의 확률형 matching.
- 계약조항을 반영한 PPA value-at-risk simulator.
- 계량·REC·청구 증빙의 자동 lineage.
- 발전량 부족·COD 지연 조기경보.
- 고객별 RE100 이행 dashboard와 설명가능한 감축근거.
- 데이터센터처럼 24/7 CFE 수요가 큰 고객의 시간단위 matching.
- 고객 계약정보를 노출하지 않는 privacy-preserving portfolio optimizer.

---
