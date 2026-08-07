---
id: skes-d11-12-liquid-hydrogen-economics
title: Liquid-Hydrogen Economics
summary: "액화수소 사업의 원가 구조(생산부터 배송까지), 경제성을 좌우하는 8개 드라이버와 6개 KPI, 정책수요의 확률 평가 방식을 설명한다."
tags: [d11, cost, table]
keywords: [액화수소 원가, 가치사슬, 경제성 드라이버, KPI, 보일오프, Offtake, 정책지원, 피드스톡]
related: [CST-ENS-D11-055, CST-ENS-D11-056, CST-ENS-D11-057, CST-ENS-D11-058, CST-ENS-D11-059, CST-ENS-D11-060, CST-ENS-D11-061, CST-ENS-D11-062, KPI-ENS-D11-041, KPI-ENS-D11-042, KPI-ENS-D11-043, KPI-ENS-D11-044, KPI-ENS-D11-045, KPI-ENS-D11-046]
priority: normal
domain: D11
section: 12
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 634
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 12. Liquid-Hydrogen Economics

## 12.1 Delivered Cost per Paid kg

```text
Delivered liquid-H2 cost/kg
= feedstock and hydrogen production
+ purification and compression
+ liquefaction electricity and utility
+ storage and boil-off loss
+ loading, tanker and station delivery
+ dispensing and station energy
+ fixed plant, maintenance, safety and depreciation
− by-product or policy value actually realized

Recurring contribution/kg
= realized sale price/kg
− delivered cost per paid kg
− expected contract and credit loss/kg
```

DOE 자료는 액화설비 비용이 규모에 크게 좌우되고 액화·배송이 별도 Cost Layer임을 보여준다. 이를 인천 액화수소플랜트의 실제 원가로 복사하지 않고 내부 모델의 누락항목과 규모 민감도를 확인하는 Baseline으로만 사용한다.

## 12.2 Hydrogen Driver and KPI

| ID | Driver | 경제성 영향 |
|---|---|---|
| `CST-ENS-D11-055` | Feedstock H2 cost | 원료원가 |
| `CST-ENS-D11-056` | Liquefaction energy | 전력비·효율 |
| `CST-ENS-D11-057` | Plant utilization | 고정비/kg |
| `CST-ENS-D11-058` | Boil-off | 판매가능 kg·안전 |
| `CST-ENS-D11-059` | Tanker fill and route | 배송원가/kg |
| `CST-ENS-D11-060` | Station demand | 재고회전·BOG |
| `CST-ENS-D11-061` | Offtake firmness | 가동률·Bankability |
| `CST-ENS-D11-062` | Policy support | 조건부 Revenue |

| KPI ID | KPI | 정의 |
|---|---|---|
| `KPI-ENS-D11-041` | Paid kg/Nameplate kg | 실제 판매/명목능력 |
| `KPI-ENS-D11-042` | Liquefaction kWh/kg | 액화공정 전력효율 |
| `KPI-ENS-D11-043` | BOG Loss % | 생산·입고 대비 손실 |
| `KPI-ENS-D11-044` | Delivered Cost/Paid kg | 전 Value Chain 원가 |
| `KPI-ENS-D11-045` | Contracted Demand Coverage | Firm kg/경제가동 kg |
| `KPI-ENS-D11-046` | Route Cost/kg-km | 배송경로 효율 |

정책상 차량·충전소 목표나 MOU는 Firm Offtake가 아니다. `차량 등록→충전소 가동→연료계약→일별 인수→대금회수` 단계로 확률을 적용해야 한다.

---
