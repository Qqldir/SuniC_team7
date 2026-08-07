---
id: skes-d12-3-investment-funding-data-model
title: Investment & Funding Data Model
summary: "프로젝트 투자의 의사결정·자금조달·운영 전 단계에서 추적·관리해야 할 데이터 엔티티와 상태, 재원 구성을 정의하는 모델"
tags: [d12, capex, schema, table]
keywords: [투자케이스, 자본지출, 투자상태, 재원구조, FID, SPV, 금융악기, 의사결정게이트]
related: []
priority: normal
domain: D12
section: 3
source: SK이노베이션E&S_D12_CAPEX_Investment_Funding_and_Financial_Structure.md
breadcrumb: ""
tokens: 588
updated: 2026-08-06
---

> SK이노베이션 E&S · D12 CAPEX·투자·자금조달

# 3. Investment & Funding Data Model

## 3.1 Core Entities

| Entity | Key | 필수 필드 |
|---|---|---|
| `InvestmentCase` | case_id + version | 목적·대안·Sponsor·Gate·approval·economics |
| `ProjectSPV` | legal_entity_id | 지분·연결여부·partner·governance |
| `AssetScope` | asset_id | 위치·capacity·ownership·COD·status |
| `CapexPackage` | WBS + contract_id | budget·commitment·change·invoice·cash·EAC |
| `FundingInstrument` | instrument_id | debt/equity/PF/grant/tax·currency·maturity |
| `SponsorSupport` | obligation_id | guarantee·completion support·equity call·cap |
| `PolicySupport` | program_id | eligibility·award·cash·clawback |
| `CashForecast` | case+period+scenario | capex·WC·debt service·cash contribution |
| `InvestmentOption` | asset+option | expand/hold/convert/refinance/sell/exit |
| `DecisionAudit` | decision+gate | input version·approver·condition·evidence |

## 3.2 Status Vocabulary

```yaml
investment_status:
  ANNOUNCED: 발표, 집행확정 아님
  FEASIBILITY: 타당성 검토
  PERMITTED: 핵심 인허가 확보
  FID: 최종투자결정
  FINANCIAL_CLOSE: 자금조달 종결
  CONSTRUCTION: 건설/설치 중
  COMMISSIONING: 시운전
  COMMERCIAL_OPERATION: 상업운전
  REFINANCING: 운영 후 재조달
  RESTRUCTURED: 범위/소유권/의무 변경
  SOLD: 지분/자산 처분
  CANCELLED: 취소
  NOT_DISCLOSED: 공개 확인 불가
```

## 3.3 Funding Stack

```yaml
funding_stack:
  sponsor_equity:
    fields: [committed, called, paid, returned]
  partner_equity:
    fields: [partner, share, contribution, default_remedy]
  project_debt:
    fields: [lender, limit, drawn, outstanding, maturity, amortization]
  corporate_debt:
    fields: [borrower, parent_scope, currency, purpose]
  public_support:
    fields: [grant, subsidy, tax_credit, concessional_loan, clawback]
  contract_financing:
    fields: [prepayment, vendor_credit, lease, receivable_financing]
  risk_support:
    fields: [guarantee, completion_support, DSRA, LC, hedge]
```

---
