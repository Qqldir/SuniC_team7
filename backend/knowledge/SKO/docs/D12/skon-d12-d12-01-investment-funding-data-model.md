---
id: skon-d12-d12-01-investment-funding-data-model
title: Investment & Funding Data Model
summary: "투자사업의 의사결정부터 상업운영까지 추적·관리하기 위한 핵심 데이터 엔터티 13개, 상태 8가지, 금액 워터폴을 정의한다."
tags: [d12, capex, schema, table]
keywords: [투자안, 자금조달, 자산범위, CAPEX, 건설진척, 투자상태, 금액워터폴, Decision Gate, Commercial Operation, JV, 투자안건, 의사결정, 자산화, 손상신호, 건설진행, 현금흐름, 합작투자, 상태관리]
related: []
priority: normal
domain: D12
section: D12-01
source: SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md
breadcrumb: "SK온 D12 — CAPEX, Investment, Funding & Financial Structure"
tokens: 813
updated: 2026-08-03
---

> SK온 · D12 CAPEX·투자·자금조달 · SK온 D12 — CAPEX, Investment, Funding & Financial Structure

## D12-01 Investment & Funding Data Model

### 1. 핵심 엔터티

| 엔터티 | 기본 키 | 최소 필드 |
|---|---|---|
| `InvestmentCase` | `investment_case_id + version` | 목적·대안·Sponsor·승인일·Decision Gate·경제성 |
| `AssetScope` | `entity_id + facility_id + line_id` | 소유권·연결범위·Capacity·제품·고객승인 |
| `CapexPackage` | `wbs_id + contract_id` | Budget·Commitment·PO·Change Order·검수·지급·자산화 |
| `ConstructionProgress` | `project_id + cut_off_date` | 물리진척·원가진척·Schedule·Critical Path·EAC |
| `FundingInstrument` | `instrument_id` | Equity·Debt·Grant·Tax·Lease·PRS·조건·만기·통화 |
| `PartnerContribution` | `jv_id + partner_id + call_id` | 약정·납입·미납·분담근거·Default Remedy |
| `GuaranteeSupport` | `support_id + obligation_id` | 보증인·수익자·최대 Exposure·기간·Release 조건 |
| `IncentiveCovenant` | `program_id + facility_id` | 고용·투자·생산·보고·유지기간·Clawback |
| `CashFlowForecast` | `case_id + period + scenario` | CAPEX·OPEX·운전자본·Credit·Debt service·FCF |
| `AssetOption` | `asset_id + option_id` | expand/hold/convert/mothball/sell·Trigger·Exit Cost |
| `ImpairmentSignal` | `cgu_id + test_date` | 수요·가동률·Margin·할인율·장부가·회수가능액 |
| `DecisionAudit` | `decision_id + gate` | 입력 Version·승인자·근거·조건·사후검증 |

### 2. 상태 Vocabulary

```yaml
investment_status:
  ANNOUNCED:
    meaning: 회사·정부가 계획을 발표했으나 확정집행과 다를 수 있음
  BOARD_APPROVED:
    meaning: 이사회 승인 또는 계약승인이 확인됨
  COMMITTED_NOT_DRAWN:
    meaning: 법적 약정·한도가 있으나 실제 인출·지급 미확인
  IN_EXECUTION:
    meaning: 발주·건설·설치·지급이 진행 중
  COMMERCIAL_OPERATION:
    meaning: 상업생산 개시가 확인됨
  RESTRUCTURED:
    meaning: 소유권·범위·자금의무가 변경됨
  CANCELLED_OR_EXITED:
    meaning: 취소·매각·JV 해소로 원안이 종료됨
  NOT_DISCLOSED:
    meaning: 공개자료로 상태 또는 금액을 확정할 수 없음
```

### 3. 금액 Waterfall

```text
Announced Gross Project Value
→ Board-approved Budget
→ Contracted Commitment
→ Purchase Order / Change Order
→ Invoice Certified
→ Cash Paid
→ Capitalized Asset
→ Asset in Commercial Operation
→ Recoverable Cash-generating Asset
```

각 단계의 금액은 같지 않다. 특히 공장 총투자액과 실제 CAPEX 지급액, 대출한도와 인출액, 자산화 금액과 회수가능가액을 분리해야 한다.

---
