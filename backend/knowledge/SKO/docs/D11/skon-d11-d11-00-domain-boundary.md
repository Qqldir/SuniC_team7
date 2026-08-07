---
id: skon-d11-d11-00-domain-boundary
title: Domain Boundary
summary: 배터리 제품의 단위경제성 분석 시 포함·제외할 항목과 고객 인수 기준 kWh 기반의 원가·수익성 판정 원칙을 정의하는 D11 도메인 경계 설정 문서
tags: [d11, cost, core-candidate, table, "xref:d10", "xref:d00", "xref:d17", "xref:d09"]
keywords: [배터리 세그먼트, Unit Economics, 원가·수익성, 합격 kWh, EBIT, 고정비 배분, 고객 인수, Cost-to-Serve, 운전자본, AMPC 조정, 합격kWh, 원가동인, 마진분석, AMPC, 반복이익, 고정비흡수]
related: []
priority: critical
domain: D11
section: D11-00
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 1222
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

# SK온 D11 — Cost, Profitability & Business Economics

- 문서 버전: **v1.0.1**
- 기준일: **2026-08-03 (KST)**
- 이전 완료 지점: `D10 Market, Competition & Industry Dynamics v1.0`
- 작성 방식: **실무형 요약 DB** — 공개 손익과 정책효과를 보존하고, 비공개 제품·고객·공장 원가는 임의 추정하지 않음
- 상위 목적: `판매 가능한 합격 kWh`의 경제성을 제품·고객·공장·기간 단위로 계산하고, 반복 가능한 이익 개선 과제를 D17로 전달
- D00 통합검수: Domain-local Source/Entity ID를 보존하고 Canonical Alias는 D00 Crosswalk로 해석한다. 금액·원가·세액공제는 Scope·단위·기간·gross/net을 필수 필드로 유지한다.

---

## D11-00 Domain Boundary

### 1. 도메인 정의

D11은 분기 실적을 요약하는 재무문서가 아니다. 시장·수주·생산·공급망 데이터가 실제 이익과 현금으로 바뀌는 과정을 연결한다.

```text
Customer Program / Product / Plant / Period
→ Accepted Sales Volume and Realized Price
→ Material·Conversion·Quality·Logistics·Warranty Cost
→ Fixed-cost Absorption and Ramp Cost
→ Policy Credit·Compensation·One-off Adjustment
→ Recurring EBIT / Cash Contribution / ROIC
→ Root Cause and Decision Lever
→ D17 Open-Innovation Seed
```

핵심 관리단위는 생산한 kWh가 아니라 **고객이 인수해 매출과 현금에 기여한 합격 kWh**다. 명목 생산능력, 실제 생산량, 합격량, 출하량, 고객 인수량을 분리해야 수율·재고·고정비·Credit의 경제적 효과가 정확히 드러난다.

### 2. 포함·제외 범위

| 포함 | 제외 또는 다른 도메인 원본 |
|---|---|
| Battery 세그먼트 공개 매출·영업손익·Margin | 시장수요·경쟁사 전략은 D10 |
| 제품·공장·고객·Program별 Unit Economics 스키마 | 고객계약·수주 상태는 D09 |
| 재료비·수율·가동률·에너지·물류·품질·Warranty Cost Driver | 상세 제조공정·설비 원본은 D06 |
| AMPC·고객보상·환입·손상차손 등 반복/비반복 구분 | 생산거점·명목 Capacity는 D07 |
| 견적–실적 Margin Bridge와 Cost-to-Serve | 공급사·원산지·구매계약은 D08 |
| 운전자본·현금기여·CAPEX 회수 연결 | 투자계획·보조금·재무조달 원본은 D12 |
| 외부사례와 D17 O/I 후보 | 계약·JV 구조는 D13, 규제판정은 D14 |
| 수익성 조기경보와 개선 우선순위 | 전사 Risk 원장은 D15, 후보기업 원장은 D16 |

### 3. 판정 원칙

1. `Battery segment` 손익과 SK온·SK온 Trading International·SK Enterm 등을 포함한 `consolidated entity` 손익을 합치지 않는다.
2. 보고영업이익, AMPC 포함 손익, AMPC 제외 단순 Proxy, 반복 EBIT, EBITDA, 영업현금흐름을 서로 다른 값으로 저장한다.
3. 고객보상·자산매각·충당금 환입·손상차손은 경제적 의미와 현금영향을 별도로 표시한다.
4. 공개되지 않은 출하 GWh가 없으면 `KRW/kWh`와 `EBIT/kWh`를 역산하지 않는다.
5. 명목 Capacity를 분모로 사용해 원가를 낮게 보이게 하지 않는다. 분모는 목적에 따라 `produced`, `good`, `shipped`, `customer-accepted kWh`를 명시한다.
6. 원료가격 연동·환율 Pass-through가 있더라도 시차·상하한·재고효과가 확인되지 않으면 완전 Hedge로 판정하지 않는다.
7. 공개자료에서 반복이익 조정금액을 알 수 없으면 `NOT_CALCULABLE_FROM_PUBLIC_DATA`로 둔다.
8. D11의 점수·목표치는 D17 선별용 분석값이며 회사의 공식 KPI나 실적이 아니다.

---
