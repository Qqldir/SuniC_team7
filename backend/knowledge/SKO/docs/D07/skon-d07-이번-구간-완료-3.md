---
id: skon-d07-이번-구간-완료-3
title: 이번 구간 완료 (3)
summary: "배터리 생산거점·생산능력 데이터 구축(D07)의 진행현황 문서로, 완료/미완료 작업 현황과 다음 단계(청크·그래프·감사)를 제시한다."
tags: [d07, footprint, build-log, schema]
keywords: [배터리 캐파시티, 생산거점, Pro Forma, 45X, PFE, 관세, EU 배터리 규제, 가동률, 정책 리스크, 프로젝트 진행, 배터리 생산능력, ESS 생산, 공장, D07, 생산 용량, Capacity Ledger, Footprint]
related: []
priority: reference
domain: D07
section: ""
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1627
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# 이번 구간 완료

* 최신 Q2 사업 업데이트와 Q1 Capacity 기준일 분리
* Capacity Event Ledger
* 2024–2028 Three-Ledger Timeline
* Kentucky 이전 후 **94.3GWh Pro Forma** 산출
* HSBMA 35GWh JV Gross 분리
* Tennessee 45GWh Legacy Design 경계
* Design→Qualified→Good-Output Capacity Ladder
* HSBMA·GRIDON·Tennessee·EU Scenario
* 가동률·Fixed-Cost Exposure Model
* 미국 45X·PFE·Battery Ledger 구조
* 중국산 EV·ESS Battery 관세
* EU Battery Regulation·Battery Booster
* Logistics·Customer Proximity Model
* Utility·Labor·Environmental Risk
* Capacity Scenario Graph
* Footprint Economics Boundary
* 신규 D07 OI Seed **8개**

## 현재 D07 진행상태

```yaml
progress:

  domain_boundary: COMPLETE
  capacity_vocabulary: COMPLETE_V1
  research_pack: COMPLETE_V3

  global_plant_master: COMPLETE_V1
  ownership_and_jv_structure: COMPLETE_V1

  capacity_timeline:
    event_ledger: COMPLETE_V1
    2024_to_2028_timeline: COMPLETE_V1
    official_q1_2026_capacity: 97.4
    post_kentucky_pro_forma: 94.3
    current_official_restatement: UNRESOLVED

  qualified_capacity:
    qualification_ladder: COMPLETE_V1
    actual_plant_values: NOT_AVAILABLE

  utilization_and_fixed_cost:
    consolidated_utilization: COMPLETE
    plant_level_utilization: NOT_AVAILABLE
    fixed_cost_model: COMPLETE_V1

  policy:
    section_45x: COMPLETE_V1
    pfe_restriction: COMPLETE_V1
    section_301_tariff: COMPLETE_V1
    us_battery_ledger: COMPLETE_V1
    eu_battery_regulation: COMPLETE_V1

  footprint_risk:
    logistics: COMPLETE_V1
    utility_and_labor: COMPLETE_PRELIMINARY
    environmental: COMPLETE_PRELIMINARY

  oi_seeds:
    previous_total: 13
    newly_added: 8
    cumulative_total: 21

  chunk_library: NOT_STARTED
  graph_queries: PARTIALLY_STARTED
  final_quality_audit: NOT_STARTED
```

## 다음 시작점

`D07-32 Footprint Chunk Library·Graph Query·Final Audit`

```text
D07-32 Manufacturing Footprint Chunk Library
→ D07-33 Plant·Capacity Graph Query Templates
→ D07-34 Plant–Customer–Policy Relationship Graph
→ D07-35 Capacity Data Quality Audit
→ D07-36 Human-Readable Footprint Strategy
→ D07 Final YAML
→ D07 완료
```

[1]: https://askinno.com/global/archives/156625?utm_source=chatgpt.com "[SK Innovation's Q2 2026 Financial Results] Recording ..."
[2]: https://www.federalregister.gov/documents/2024/10/28/2024-24840/advanced-manufacturing-production-credit "Federal Register :: Advanced Manufacturing Production Credit"
[3]: https://www.irs.gov/newsroom/treasury-irs-provide-guidance-for-certain-energy-tax-credits-regarding-material-assistance-provided-by-prohibited-foreign-entities-under-the-one-big-beautiful-bill "Treasury, IRS provide guidance for certain energy tax credits regarding material assistance provided by prohibited foreign entities under the One, Big, Beautiful Bill | Internal Revenue Service"
[4]: https://ustr.gov/about-us/policy-offices/press-office/press-releases/2024/may/us-trade-representative-katherine-tai-take-further-action-china-tariffs-after-releasing-statutory "U.S. Trade Representative Katherine Tai to Take Further Action on China Tariffs After Releasing Statutory Four-Year Review | United States Trade Representative"
[5]: https://www.irs.gov/credits-deductions/clean-vehicle-credit-qualified-manufacturer-requirements "Clean vehicle credit qualified manufacturer requirements | Internal Revenue Service"
[6]: https://eur-lex.europa.eu/eli/reg/2023/1542/oj?eliuri=eli%3Areg%3A2023%3A1542%3Aoj&locale=en&utm_source=chatgpt.com "Regulation - 2023/1542 - EN - Batteries Regulation - EUR-Lex"
[7]: https://climate.ec.europa.eu/eu-action/eu-funding-climate-action/innovation-fund/battery-booster-facility_en?utm_source=chatgpt.com "Battery Booster Facility - Climate Action - European Commission"
[8]: https://eng.sk.com/news/sk-on-signs-battery-supply-agreement-with-nissan?utm_source=chatgpt.com "SK On Signs Battery Supply Agreement with Nissan"
[9]: https://eng.sk.com/news/sk-on-selected-as-battery-supplier-for-u-s-ev-startup-slate?utm_source=chatgpt.com "SK On Selected as Battery Supplier for U.S. EV Startup Slate"
[10]: https://www.energy.gov/sites/default/files/2023-03/2023_03_02_LPO-BlueOvalSK_EAv6.0_signed.pdf?utm_source=chatgpt.com "Report"
[11]: https://kind.krx.co.kr/external/2026/05/15/001636/20260515003618/11013.htm "kind.krx.co.kr"
[12]: https://eng.sk.com/news/sk-on-expands-u-s-ess-push-at-acp-cleanpower-2026 "SK On Expands U.S. ESS Push at ACP CLEANPOWER 2026 | SK"
[13]: https://www.irs.gov/credits-deductions/advanced-manufacturing-production-credit "Advanced Manufacturing Production Credit | Internal Revenue Service"
[14]: https://gov.georgia.gov/press-releases/2023-01-26/gov-kemp-sk-battery-america-open-us-it-center-create-200-high-tech-jobs?utm_source=chatgpt.com "Gov. Kemp: SK Battery America to Open U.S. IT Center, Create 200 High-Tech Jobs in Roswell | Governor Brian P. Kemp Office of the Governor"
[15]: https://eng.sk.com/news/sk-on-and-hyundai-motor-bolster-support-for-u-s-evs-with-georgia-battery-plant?utm_source=chatgpt.com "SK On and Hyundai Partner on Georgia EV Battery Plant"
[16]: https://corporate.ford.com/articles/electrification/blue-oval-city/?utm_source=chatgpt.com "BlueOval City | Articles | Ford Motor Company"
[17]: https://economy-finance.ec.europa.eu/economic-surveillance-eu-member-states/country-pages-including-country-reports/country-report-hungary_en?utm_source=chatgpt.com "Country report - Hungary - Economy and Finance - European Commission"
[18]: https://gov.georgia.gov/press-releases/2023-01-30/gov-kemp-sk-battery-america-exceeds-hiring-goal-track-reach-3000-workers?utm_source=chatgpt.com "Gov. Kemp: SK Battery America Exceeds Hiring Goal, On Track to Reach 3,000 Workers | Governor Brian P. Kemp Office of the Governor"

---
