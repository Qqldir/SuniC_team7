---
id: skes-d12-7-cost-to-complete-construction-control
title: Cost-to-Complete & Construction Control
summary: "건설 프로젝트의 최종 예상 원가(EAC) 계산식, 공사비 통제 항목의 오류 패턴, 공사 지연이 수익성과 현금흐름에 미치는 영향을 설명하는 문서."
tags: [d12, capex, table]
keywords: [EAC, 공사비 초과, 공사 지연, 현금흐름, IDC, COD, 원가 예측, 불확실성 예비비]
related: []
priority: normal
domain: D12
section: 7
source: SK이노베이션E&S_D12_CAPEX_Investment_Funding_and_Financial_Structure.md
breadcrumb: ""
tokens: 519
updated: 2026-08-06
---

> SK이노베이션 E&S · D12 CAPEX·투자·자금조달

# 7. Cost-to-Complete & Construction Control

## 7.1 Required Formulae

```text
EAC = Actual Cost to Date + Forecast Cost to Complete
Remaining Commitment = Signed Commitment − Certified/Cancelled Amount
Net Sponsor Cash Need = Future CAPEX + WC + Debt Service + Required Reserves
                       − Undrawn Debt Eligible for Project
                       − Confirmed Grant/Tax Cash
                       − Partner Contributions

Forward Incremental Value
= Risk-adjusted Operating Cash Flow
+ Residual / Contract / Reuse Option Value
+ Probabilistic Policy Support
− Remaining CAPEX
− Ramp Working Capital
− Financing / Hedge / Guarantee Cost
− Exit / Remediation / Clawback Cost
```

## 7.2 EAC Control Fields

| Field | 의미 | 오류 |
|---|---|---|
| Approved budget | 승인 기준선 | 최신 EAC로 덮어쓰기 |
| Committed | 계약약정 | cash paid로 오인 |
| Change order | 범위변경 | 원인코드 누락 |
| Actual paid | 현금지급 | invoice와 혼합 |
| Accrued | 발생 미지급 | cash와 혼합 |
| Forecast | 미래 예상 | 확정약정으로 오인 |
| Contingency | 불확실성 예비비 | 무조건 소진 가정 |
| FX impact | 환율 | 공정 performance와 혼합 |
| Schedule impact | 지연비용 | EPC 원가와 중복 |
| IDC | 건설중 이자 | operating interest와 혼합 |

## 7.3 Delay-to-Cash Bridge

```text
Schedule Delay
→ EPC overhead / change order
→ later commissioning
→ later revenue / tax-credit recognition
→ extended IDC and working capital
→ covenant / long-stop risk
→ NPV and liquidity erosion
```

대형 LNG·해상풍력·수소·CCS는 `공사비 초과`만 보지 말고 `COD 1개월 지연의 cash cost`를 별도 KPI로 저장해야 한다.

---
