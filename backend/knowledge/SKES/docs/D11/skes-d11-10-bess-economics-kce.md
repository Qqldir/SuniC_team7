---
id: skes-d11-10-bess-economics-kce
title: BESS Economics — KCE
summary: "배터리 저장 시스템의 경제성 평가를 위한 생명주기 수익 구조, 경제성 드라이버 10개, KPI 6개와 시장 입찰 효과 검증 방식을 제시한다."
tags: [d11, cost, table]
keywords: [에너지 저장, 생명주기 수익, 경제성 드라이버, 에너지 차익거래, 충방전 스프레드, 배터리 열화, 전력시장, 입찰 전략, FERC Order 841, 마켓캡처]
related: [CST-ENS-D11-039, CST-ENS-D11-040, CST-ENS-D11-041, CST-ENS-D11-042, CST-ENS-D11-043, CST-ENS-D11-044, CST-ENS-D11-045, CST-ENS-D11-046, CST-ENS-D11-047, CST-ENS-D11-048, KPI-ENS-D11-029, KPI-ENS-D11-030, KPI-ENS-D11-031, KPI-ENS-D11-032, KPI-ENS-D11-033, KPI-ENS-D11-034]
priority: normal
domain: D11
section: 10
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 719
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 10. BESS Economics — KCE

## 10.1 Lifecycle Revenue Stack

```text
Gross market revenue
= energy arbitrage + ancillary services + capacity/resource adequacy
+ contracted availability or tolling revenue where applicable
− charging energy − market fee − imbalance/penalty
− degradation and augmentation reserve
− fixed O&M − LTSA − land − insurance − property tax
− interconnection and collateral carrying cost
```

## 10.2 BESS Driver Record

| ID | Driver | 경제성 질문 | 통제 |
|---|---|---|---|
| `CST-ENS-D11-039` | Price spread | 충·방전 Spread가 손실 포함 후 양수인가 | interval settlement |
| `CST-ENS-D11-040` | Ancillary price | 경쟁진입 후 가격잠식은 얼마인가 | market saturation |
| `CST-ENS-D11-041` | Bid quality | 실제 대비 Counterfactual Uplift | 동일 위험·제약 비교 |
| `CST-ENS-D11-042` | Round-trip efficiency | 구매전력 대비 판매전력 | meter boundary |
| `CST-ENS-D11-043` | Degradation | 현재 수익이 미래 용량을 소모하는가 | shadow cost/MWh |
| `CST-ENS-D11-044` | Augmentation | CAPEX·정지·잔존가치 | lifecycle plan |
| `CST-ENS-D11-045` | Availability | 미가동 수익·Penalty | warranty/LTSA |
| `CST-ENS-D11-046` | Interconnection delay | 개발비·IDC·Option value | queue probability |
| `CST-ENS-D11-047` | Collateral | 현금구속·금융비 | Treasury limit |
| `CST-ENS-D11-048` | Safety event | 중단·수리·보험·평판 | expected loss |

## 10.3 BESS KPI

| KPI ID | KPI | 정의 |
|---|---|---|
| `KPI-ENS-D11-029` | Net Revenue/MW-year | 모든 시장정산−변동비/MW |
| `KPI-ENS-D11-030` | Risk-adjusted Bid Uplift | 동일 SOC·위험 Counterfactual 대비 |
| `KPI-ENS-D11-031` | Degradation-adjusted Margin | 시장수익−열화 Shadow Cost |
| `KPI-ENS-D11-032` | Availability-adjusted Revenue | 실제/가능 수익 |
| `KPI-ENS-D11-033` | Revenue Concentration | 상위 시장상품 매출비중 |
| `KPI-ENS-D11-034` | Lifecycle IRR/NPV | Augmentation·잔존가치 포함 |

FERC Order 841은 Storage가 Wholesale energy와 ancillary-service 시장에 참여할 수 있는 구조를 제시한다. 그러나 시장참여 가능성을 확정수익으로 보아서는 안 되며, KCE의 MarketCapture 효과는 `실제 입찰`과 동일 제약조건의 `승인된 Counterfactual`을 비교해 검증해야 한다.

---
