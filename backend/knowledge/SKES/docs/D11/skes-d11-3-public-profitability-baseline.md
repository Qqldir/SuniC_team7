---
id: skes-d11-3-public-profitability-baseline
title: Public Profitability Baseline
summary: "SK이노베이션 E&S 사업의 분기별 매출, 영업이익, 수익성 실적(2025~2026)을 제시하고, 공개 손익 해석 시 계절성·정비·SMP 변동·사업별 내역 공개 부족을 고려해야 함을 설명한다."
tags: [d11, cost, schema, table]
keywords: [영업이익률, 수익성, 도시가스, LNG, SMP, 발전소 가동률, 계절성, 공개 재무정보, 사업별 손익, 정산조정]
related: []
priority: normal
domain: D11
section: 3
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 1155
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 3. Public Profitability Baseline

## 3.1 E&S 사업 공개 손익

단위는 억 원이며 영업이익률은 `영업이익 ÷ 매출`의 단순 산술값이다.

| 기간 | 매출 | 영업이익 | 단순 영업이익률 | 공식 설명 | 상태·출처 |
|---|---:|---:|---:|---|---|
| 2025 Q1 | 37,521 | 1,931 | 5.15% | 동절기 난방수요에 따른 도시가스 판매 증가 | `REPORTED`, D11-0001 |
| 2025 Q2 | 25,453 | 1,150 | 4.52% | 계절 비수기 구간; 공식 발표 실적 | `REPORTED`, D11-0002 |
| 2025 Q3 | 25,278 | 2,554 | 10.10% | 하절기 Cargo 도입 경쟁력과 발전소 높은 가동률 | `REPORTED`, D11-0003 |
| 2025 Q4 | 30,379 | 1,176 | 3.87% | 유가 하락, 간절기 전력수요·SMP 하락, 발전소 정비 | `REPORTED`, D11-0004 |
| 2025 FY | 118,631 | 6,811 | 5.74% | E&S 사업 연간 실적 | `REPORTED/DERIVED_MARGIN`, D11-0004 |
| 2026 Q1 | 36,961 | 2,832 | 7.66% | 동절기 도시가스 판매 증가와 SMP 상승 | `REPORTED`, D11-0005 |
| 2026 Q2 | 25,961 | 1,059 | 4.08% | 도시가스 비수기와 하절기 전 발전소 계획정비 | `REPORTED`, D11-0006 |
| 2026 H1 | 62,922 | 3,891 | 6.18% | Q1+Q2 단순 합산 | `DERIVED_FROM_REPORTED` |

## 3.2 공개값에서 계산 가능한 변화

| 지표 | 산식 | 결과 | 해석 제한 |
|---|---|---:|---|
| 2026 Q2 매출 QoQ | `(25,961-36,961)/36,961` | -29.76% | 계절성·사업 Mix가 함께 작용 |
| 2026 Q2 영업이익 QoQ | `(1,059-2,832)/2,832` | -62.61% | 비수기·정비·SMP 영향; 사업별 배분 불가 |
| 2026 Q2 영업이익 YoY | `(1,059-1,150)/1,150` | -7.91% | 동일 Segment 공시이나 내부 Scope 변화 확인 필요 |
| 2025 Q3 vs Q2 이익증가 | `2,554-1,150` | +1,404억 원 | 회사가 발전소 가동률·Cargo 경쟁력을 설명 |
| 2025 Q4 vs Q3 이익감소 | `1,176-2,554` | -1,378억 원 | 회사가 SMP 하락·정비를 설명 |
| 2026 Q1 vs 2025 Q4 증가 | `2,832-1,176` | +1,656억 원 | 동절기·SMP 상승 효과 |
| 2026 Q2 vs Q1 감소 | `1,059-2,832` | -1,773억 원 | 비수기·계획정비 효과 |

## 3.3 공개 손익의 판정

1. 2025년 Q3의 10.10%와 Q4의 3.87% 차이는 E&S의 이익이 단일 안정형 Utility Margin이 아니라 LNG 조달경쟁력·발전가동률·SMP·도시가스 계절성·정비 일정의 결합이라는 신호다.
2. Q1과 Q2 차이를 그대로 구조적 수익성 변화로 해석하면 안 된다. 도시가스 난방수요와 계획정비의 계절 패턴을 정상화해야 한다.
3. 공개자료는 E&S 사업 전체 손익만 제공하므로 LNG Upstream, 발전, 도시가스, 재생, BESS, 충전, 수소, CCS별 영업이익은 `NOT_DISCLOSED`다.
4. 반복 EBIT을 계산하려면 파생상품·재고평가·환율·일회성 정산·개발비·지분법·자산매각 등 조정액과 Scope가 필요하다.
5. 따라서 공개 손익은 Top-down Control Total이며, 사업별 Bottom-up Economics와 합계 조정해야 한다.

## 3.4 Scope Bridge

```yaml
scope_bridge:
  consolidated_SK_Innovation:
    use: group_total_and_elimination_control
  disclosed_ENS_business_segment:
    use: quarterly_revenue_and_operating_profit_control_total
  ENS_CIC_management_view:
    use: organization_and_business_owner_view
    public_status: PARTIALLY_DISCLOSED
  subsidiary_legal_entity:
    use: city_gas_KCE_EverCharge_project_company_financials
  JV_or_equity_method:
    use: equity_share_cash_distribution_and_commitment
  asset_contract_route:
    use: LNG_cargo_terminal_power_PPA_BESS_unit_economics
  rule: do_not_sum_or_compare_without_elimination_and_ownership_bridge
```

---
