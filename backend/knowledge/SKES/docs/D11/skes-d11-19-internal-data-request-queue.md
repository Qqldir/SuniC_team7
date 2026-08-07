---
id: skes-d11-19-internal-data-request-queue
title: Internal Data Request Queue
summary: SK이노베이션 E&S의 원가·수익성 분석에 필요한 35개 데이터 요청사항을 우선순위별로 정의하고 소유팀을 명시한 마스터 테이블.
tags: [d11, cost, table]
keywords: [원가계산, Margin 분석, Unit Economics, LNG 경제성, 발전원가, 데이터 거버넌스, 사업경제성, 비용배부]
related: [REQ-ENS-D11-001, REQ-ENS-D11-002, REQ-ENS-D11-003, REQ-ENS-D11-004, REQ-ENS-D11-005, REQ-ENS-D11-006, REQ-ENS-D11-007, REQ-ENS-D11-008, REQ-ENS-D11-009, REQ-ENS-D11-010, REQ-ENS-D11-011, REQ-ENS-D11-012, REQ-ENS-D11-013, REQ-ENS-D11-014, REQ-ENS-D11-015, REQ-ENS-D11-016, REQ-ENS-D11-017, REQ-ENS-D11-018, REQ-ENS-D11-019, REQ-ENS-D11-020, REQ-ENS-D11-021, REQ-ENS-D11-022, REQ-ENS-D11-023, REQ-ENS-D11-024]
priority: normal
domain: D11
section: 19
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 1002
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 19. Internal Data Request Queue

| Request ID | 데이터 | Owner 후보 | 용도 | Priority |
|---|---|---|---|---|
| `REQ-ENS-D11-001` | E&S Segment→법인→자산 연결조정 | 회계 | Scope Bridge | P0 |
| `REQ-ENS-D11-002` | 분기 손익 One-off·Timing Bridge | FP&A | 반복 EBIT | P0 |
| `REQ-ENS-D11-003` | 사업별 매출·변동비·고정비 | 관리회계 | Unit Economics | P0 |
| `REQ-ENS-D11-004` | 계약별 가격공식·물량·옵션·의무 | 법무·Trading | Contract Margin | P0 |
| `REQ-ENS-D11-005` | Cargo별 Landed Cost Ledger | LNG·SCM | LNG Economics | P0 |
| `REQ-ENS-D11-006` | 액화·터미널 권리 예약/실사용 | LNG | 고정비 흡수 | P0 |
| `REQ-ENS-D11-007` | 탱크 재고·BOG·기화·송출 | Terminal | Mass Balance | P0 |
| `REQ-ENS-D11-008` | Commodity·FX Exposure/Hedge | Treasury | Margin-at-Risk | P0 |
| `REQ-ENS-D11-009` | Unit별 Fuel·Net MWh·Heat Rate | 발전·OT | 발전원가 | P0 |
| `REQ-ENS-D11-010` | 정비·고장·Derating·Lost Margin | 발전·EAM | Reliability ROI | P0 |
| `REQ-ENS-D11-011` | CHP 전력·열 원가배부 | CHP·Finance | Joint Margin | P0 |
| `REQ-ENS-D11-012` | 도시가스 고객·날씨·요금·청구 | 도시가스 | 정상화 Margin | P0 |
| `REQ-ENS-D11-013` | 배관 Input·계량·운영사용·누출 | 도시가스·안전 | Mass Balance | P0 |
| `REQ-ENS-D11-014` | 콜·출동·부품·재방문 비용 | CS·현장 | Cost-to-Serve | P1 |
| `REQ-ENS-D11-015` | 재생 발전·Curtailment·정산 | 재생 O&M | Captured Price | P0 |
| `REQ-ENS-D11-016` | PPA Load·Generation·REC·Imbalance | PPA | Shape Margin | P0 |
| `REQ-ENS-D11-017` | 개발 Milestone·확률·지출·Exit | 사업개발 | Pipeline NPV | P0 |
| `REQ-ENS-D11-018` | KCE Bid·Award·Dispatch·정산 | KCE | Counterfactual | P0 |
| `REQ-ENS-D11-019` | BESS SOC/SOH·효율·Cycle·Warranty | KCE·OEM | Lifecycle Margin | P0 |
| `REQ-ENS-D11-020` | BESS O&M·LTSA·보험·담보 | KCE·Finance | Net Revenue | P0 |
| `REQ-ENS-D11-021` | EverCharge Site·Port·Session | EverCharge | Utilization | P0 |
| `REQ-ENS-D11-022` | 충전 전력비·Demand Charge·Host Share | EverCharge | Site Margin | P0 |
| `REQ-ENS-D11-023` | 충전 설치 Quote·BOM·Actual | EverCharge | Project Margin | P1 |
| `REQ-ENS-D11-024` | 수소 생산·액화·저장 kg Balance | 수소 | Paid-kg Cost | P0 |
| `REQ-ENS-D11-025` | 액화전력·Utility·Boil-off | 수소·Plant | Efficiency | P0 |
| `REQ-ENS-D11-026` | Tanker·Station Route·Fill·Delivery | 수소물류 | Cost/kg | P0 |
| `REQ-ENS-D11-027` | 수소 Firm Offtake·가격·신용 | 영업·법무 | Bankability | P0 |
| `REQ-ENS-D11-028` | CCS Emitter FID·Volume·COD | CCS BD | Match Gate | P0 |
| `REQ-ENS-D11-029` | Capture·Transport·Storage Cost | CCS Engineering | Cost/tCO2 | P0 |
| `REQ-ENS-D11-030` | MRV·저장권·장기책임 | CCS·법무 | Liability NPV | P0 |
| `REQ-ENS-D11-031` | 재고·AR·AP·담보·Margin Call | Treasury | Cash Twin | P0 |
| `REQ-ENS-D11-032` | O/I 과제 Baseline·편익·투자비 | O/I·Finance | Benefit Ledger | P0 |
| `REQ-ENS-D11-033` | Asset/Contract/Customer Master ID | Data Office | Cross-domain Join | P0 |
| `REQ-ENS-D11-034` | 데이터 권한·보존·Lineage | IT·보안 | Auditability | P0 |
| `REQ-ENS-D11-035` | 안전·환경·시장 운영제약 | HSE·법무·Trading | Optimization Guardrail | P0 |

---
