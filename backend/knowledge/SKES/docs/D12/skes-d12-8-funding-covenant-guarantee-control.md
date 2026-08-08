---
id: skes-d12-8-funding-covenant-guarantee-control
title: "Funding, Covenant & Guarantee Control"
summary: "기업·프로젝트 차입금, 지분, 보조금 등 8가지 자금조달 수단의 등록 필드와 DSCR 악화, 공사 지연, 비용초과 등 9가지 협약 위반 신호에 대한 조기 경보 및 대응 조치를 정의하는 문서."
tags: [d12, capex, table]
keywords: [자금조달 수단, DSCR, 협약 조기경보, 부채 관리, 현금흐름, 환위험 헤지, 금리리스크, 프로젝트파이낸싱, 유동성 위험]
related: []
priority: normal
domain: D12
section: 8
source: SK이노베이션E&S_D12_CAPEX_Investment_Funding_and_Financial_Structure.md
breadcrumb: ""
tokens: 384
updated: 2026-08-06
---

> SK이노베이션 E&S · D12 CAPEX·투자·자금조달

# 8. Funding, Covenant & Guarantee Control

## 8.1 Funding Instrument Register Schema

| 구분 | 필드 |
|---|---|
| Corporate debt | borrower·currency·principal·rate·maturity·purpose |
| Project debt | SPV·lender·limit·drawn·amortization·DSCR·security |
| Equity | investor·class·ownership·call·paid·distribution |
| Grant | program·eligible cost·award·cash·milestone·clawback |
| Tax credit | statute·eligible basis·generated·transfer·cash·recapture |
| Lease | lessor·asset·term·payment·purchase option |
| Guarantee | guarantor·beneficiary·cap·expiry·release trigger |
| Hedge | commodity/FX/rate·notional·maturity·collateral·MtM |

## 8.2 Covenant Early Warning

| Signal | 데이터 | 조치 |
|---|---|---|
| DSCR headroom 축소 | CFADS·debt service | downside cash forecast |
| construction long-stop 접근 | schedule·critical path | cure plan |
| cost overrun | EAC vs budget | contingency/partner call |
| volume shortfall | actual vs P50/P90 | reserve/hedge/offtake review |
| price/spread collapse | realized margin | curtail/rebid/recontract |
| interest-rate rise | floating debt | hedge/refinance review |
| FX mismatch | debt vs cash currency | natural/financial hedge |
| tax-credit delay | eligibility/transfer | bridge liquidity |
| grant milestone miss | KPI/evidence | clawback reserve |
| major outage | availability | insurance/debt cure |

---
