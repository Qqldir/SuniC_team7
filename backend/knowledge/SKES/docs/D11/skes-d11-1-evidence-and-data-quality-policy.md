---
id: skes-d11-1-evidence-and-data-quality-policy
title: Evidence and Data-Quality Policy
summary: "공시·계약·내부자료 등 정보원천의 신뢰도를 6단계로 분류하고, 재무·물량·시간·상태 데이터의 필수 단위·시점 필드를 규정."
tags: [d11, cost, schema, table]
keywords: [Evidence Tier, 신뢰도 등급, Claim Status, 정보원천 분류, 공시값, 내부 데이터, Unit Economics, 측정 제어, FID]
related: []
priority: normal
domain: D11
section: 1
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 617
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 1. Evidence and Data-Quality Policy

## 1.1 Evidence Tier

| Tier | 정의 | 사용 |
|---|---|---|
| `E1A` | 감사보고서·사업보고서·법령·규제기관·시장운영기관 | 회계값·법적 구조·시장정산 |
| `E1B` | 회사 공식 실적발표·공식 사업자료·자회사 공식자료 | 실적·사업경계·운영설명 |
| `E2` | 정부·국책기관·IEA·NREL·DOE 등 기술경제 자료 | 산업 Baseline·모델 구조 |
| `E3` | 신용평가·공식 거래상대방·공급사 자료 | 계약·자산·외부 사례 보완 |
| `E4` | 언론·분석자료 | 탐색용; 핵심 수치의 단독 근거로 사용 금지 |
| `INT` | 내부 ERP·계약·SCADA·EAM·세무·정산 데이터 | 실제 Unit Economics와 PoC 검증 |

## 1.2 Claim Status

```yaml
claim_status:
  REPORTED: 공시 또는 공식 실적발표의 수치
  DERIVED_FROM_REPORTED: 동일 Scope 공개값의 단순 산술
  COMPANY_EXPLANATION: 회사가 제시한 증감 사유
  INDUSTRY_BASELINE: 공공 기술·시장자료의 일반 구조
  CONTRACT_PUBLIC: 계약 당사자가 공개한 범위
  INTERNAL_REQUIRED: 내부 데이터가 있어야 계산 가능
  ANALYTICAL_SCENARIO: 의사결정용 가정이며 실적 아님
  NOT_DISCLOSED: 공개자료에서 값 미확인
  NOT_CALCULABLE: 분모·조정액·Scope 부족으로 산출 금지
```

## 1.3 필수 단위·시점 필드

```yaml
measurement_control:
  money:
    - currency
    - nominal_or_real
    - gross_or_net
    - accounting_or_cash
    - consolidated_or_equity_share
  volume:
    - physical_unit
    - gross_or_net_generation
    - nameplate_or_available_or_dispatched_or_sold
    - contracted_or_nominated_or_delivered_or_paid
  time:
    - trade_date
    - delivery_period
    - accounting_period
    - cash_settlement_date
  status:
    - planned
    - contracted
    - FID
    - construction
    - commissioning
    - operating
    - retired_or_sold
```

---
