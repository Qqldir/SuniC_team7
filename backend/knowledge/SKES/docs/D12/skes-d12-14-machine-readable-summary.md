---
id: skes-d12-14-machine-readable-summary
title: Machine-Readable Summary
summary: "Barossa, 액화수소 등 E&S 주요 에너지자산의 투자규모·금융구조·회수 현금흐름을 YAML데이터와 검증표로 구조화한 포트폴리오 문서."
tags: [d12, capex, schema, table, "xref:d11", "xref:d07", "xref:d17"]
keywords: [에너지자산 투자규모, CAPEX 자금조달 구조, 프로젝트 파이낸싱, Barossa, "액화수소, 해상풍력", 비상환금융 Non-recourse, 현금흐름 회수방식, YAML 기계가독형, 투자포트폴리오 검증]
related: []
priority: normal
domain: D12
section: 14
source: SK이노베이션E&S_D12_CAPEX_Investment_Funding_and_Financial_Structure.md
breadcrumb: ""
tokens: 1031
updated: 2026-08-06
---

> SK이노베이션 E&S · D12 CAPEX·투자·자금조달

# 14. Machine-Readable Summary

```yaml
domain: D12
entity: SK Innovation E&S
as_of: 2026-08-06
scope_rule: post_merger_ENS_CIC_with_historical_SK_ENS_time_separated
core_public_investments:
  barossa:
    gross_project_cost_usd_bn: 3.7
    ens_share_at_fid_pct: 37.5
    ens_public_investment_plan_usd_bn: 1.4
    status_2026: operating_transition
    caution: public_plan_not_equal_actual_cash_paid
  incheon_liquid_hydrogen:
    public_initial_plan_krw_bn: 500
    pf_agreement_krw_bn_approx: 360
    capacity_tpy: 30000
    completed: 2024
    caution: plan_pf_and_final_capex_are_different_states
  incheon_airport_h2_hub:
    gross_cost_krw_bn: 14.3
    central_government_krw_bn: 7.0
    incheon_city_krw_bn: 3.0
    hyverse_krw_bn: 4.3
    status: completed_2026
  jeonnam_offshore_wind_1:
    capacity_mw: 96
    ens_pct: 51
    cip_pct: 49
    financing: non_recourse_project_finance
    cod: 2025-05
  kce_texas_2021_financing:
    portfolio_mw: 230
    debt_usd_m: 93.3
    caution: not_current_total_kce_debt
  plug_power_2021:
    total_sk_investment_krw_trn: 1.6
    sk_ens_share_krw_bn: 800
    caution: historical_strategic_equity_investment
  rev_renewables:
    announced_max_investment_usd_m: 400
    caution: announced_max_not_equal_current_carrying_value
key_controls:
  - gross_vs_net_exposure
  - ownership_vs_contract_right
  - committed_vs_drawn_vs_paid
  - project_debt_vs_sponsor_debt
  - policy_eligibility_vs_cash
  - sunk_cost_vs_forward_cash
  - pipeline_vs_fid_vs_cod
counts:
  public_investment_records: 43
  financial_risks: 35
  pain_points: 35
  oi_seeds: 60
  d17_priority_candidates: 15
  internal_data_requests: 35
  sources: 36
```

---

# 15. Validation Checklist

| Check | Result |
|---|---|
| 현재 E&S CIC와 과거 SK E&S 법인 시간축 분리 | PASS |
| SK Innovation 연결재무와 E&S 사업손익 혼합 금지 | PASS |
| Barossa gross $3.7bn / E&S public $1.4bn 분리 | PASS |
| 인천 LH2 계획투자와 PF 약정 분리 | PASS |
| Hydrogen Hub gross 143억 / Hyverse 43억 분리 | PASS |
| KCE 2021 $93.3m debt와 현재 portfolio debt 혼동 금지 | PASS |
| Jeonnam 1 non-recourse PF를 무보증으로 확장하지 않음 | PASS |
| Boryeong equity sale와 TUA right 분리 | PASS |
| Freeport right를 plant ownership으로 처리하지 않음 | PASS |
| 개발 pipeline을 committed CAPEX로 처리하지 않음 | PASS |
| 공개되지 않은 WACC/IRR/DSCR 추정 금지 | PASS |
| Grant/ITC의 eligible-award-cash-clawback 분리 | PASS |
| D11 economics·D07 assets Crosswalk 반영 | PASS |
| D17 finance-verified benefit state 정의 | PASS |

---

# D12 완료 상태

`REPRESENTATIVE_COMPANY_DEEP_DB / READY_FOR_D13`

D12의 핵심은 E&S가 보유·운영·사용하는 에너지 자산의 투자금액 자체보다 **누가 얼마를 언제 실제 부담하고, 어떤 조건의 자금으로 조달하며, 어떤 현금흐름과 위험으로 회수하는지**를 구조화하는 것이다. 특히 Barossa, 인천 액화수소, 전남해상풍력, KCE BESS는 각각 `JV equity`, `PF`, `non-recourse renewable PF`, `merchant/storage debt + tax credit`라는 서로 다른 금융구조의 대표 학습셋으로 유지한다.

최종적으로 D17에 전달되는 O/I 아이디어는 기술적으로 매력적인지뿐 아니라 `scope → commitment → cash → support → downside → option → finance verification`의 전 과정을 통과해야 한다.
