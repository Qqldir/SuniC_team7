---
id: skon-d07-이번-구간-완료-2
title: 이번 구간 완료 (2)
summary: "SK온 D07 프로젝트의 글로벌 용량·거점 정규화 완료 현황, 진행상태 체크리스트, 다음 작업 로드맵을 정리한 문서"
tags: [d07, footprint, build-log, schema]
keywords: [D07, 생산거점, 캐파시티, 진행 현황, 배터리 공장, 글로벌 맵핑, 고객 연계, Footprint, OI Seed, 확장 계획, 용량정규화, 고객연계, EV/ESS, 진행상태, 용량시나리오, 예비용량, OI]
related: []
priority: reference
domain: D07
section: ""
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 958
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# 이번 구간 완료

* Site–Product–Customer Evidence Level 정규화
* Plant·Line Entity Schema
* 미공개 Line의 임의 생성 방지규칙
* 서산·코마롬·이반차 제품 Mapping
* 중국 공장 고객·화학계 Mapping 경계
* SKBA–F-150 Lightning·ID.4 역사적 직접 Mapping
* HSBMA–현대·기아·제네시스 및 IONIQ 9 Mapping
* Tennessee EV·ESS 전략적 선택권과 2028 Pre-SOP 상태
* 미국 GRIDON 생산 Site 미확정 처리
* EV→ESS·Chemistry Conversion Matrix
* Customer-Linked Capacity Schema
* Plant Ramp-Up Stage·Snapshot
* Capacity Redundancy·Alternative Site Model
* Footprint Pain Point **10개**
* 신규 D07 OI Seed **8개**

## 현재 D07 진행상태

```yaml
progress:

  domain_boundary: COMPLETE
  capacity_vocabulary: COMPLETE_V1
  research_pack: COMPLETE_V2

  global_plant_master: COMPLETE_V1
  ownership_and_jv_structure: COMPLETE_V1

  site_line_product_mapping:
    schema: COMPLETE_V1
    korea: COMPLETE_WITH_DISCLOSURE_GAPS
    hungary: COMPLETE_WITH_DISCLOSURE_GAPS
    china: COMPLETE_PROVISIONAL
    united_states: COMPLETE_V1

  customer_linked_capacity:
    confirmed_records: 4
    dedicated_capacity_values: NOT_DISCLOSED
    europe_and_china_mapping: UNRESOLVED

  conversion_map:
    ev_to_ess: COMPLETE_PRELIMINARY
    chemistry_conversion: LOW_PUBLIC_VISIBILITY
    exact_gridon_site: UNRESOLVED

  ramp_up:
    maturity_framework: COMPLETE_V1
    plant_snapshot: COMPLETE_PROVISIONAL
    plant_level_yield: NOT_AVAILABLE

  redundancy:
    regional_assessment: COMPLETE_V1
    effective_qualified_capacity: NOT_AVAILABLE

  pain_points:
    total: 10

  oi_seeds:
    previous_total: 5
    newly_added: 8
    cumulative_total: 13
```

## 다음 시작점

`D07-20 Capacity Timeline·Scenario·Footprint Economics Boundary`

```text
D07-20 Plant Capacity Event Ledger
→ D07-21 2024–2028 Capacity Timeline
→ D07-22 Consolidated·JV·Transferred Capacity Bridge
→ D07-23 Qualified Capacity Scenario
→ D07-24 Utilization·Fixed-Cost Exposure
→ D07-25 Local Content·Tariff·Incentive Constraints
→ D07-26 Logistics·Customer Proximity
→ D07-27 Utility·Labor·Environmental Footprint Risk
→ D07-28 Capacity Scenario Graph
→ D07-29 Footprint OI Prioritization
```

[1]: https://www.skinnovation.com/company/history "History < About us < Company < SK Innovation"
[2]: https://eng.sk-on.com/company/press_view.asp?CompanyCode=011&idx=191&page=1&schtxt=&utm_source=chatgpt.com "Press Release < Press < Company < SK-ON"
[3]: https://gov.georgia.gov/press-releases/2023-01-26/gov-kemp-sk-battery-america-open-us-it-center-create-200-high-tech-jobs "Gov. Kemp: SK Battery America to Open U.S. IT Center, Create 200 High-Tech Jobs in Roswell | Governor Brian P. Kemp Office of the Governor"
[4]: https://www.hsbma.com/about "HSBMA"
[5]: https://eng.sk.com/news/sk-on-and-hyundai-motor-bolster-support-for-u-s-evs-with-georgia-battery-plant "SK On and Hyundai Partner on Georgia EV Battery Plant | News | SK"
[6]: https://eng.sk.com/news/sk-on-tennessee-becomes-newest-sk-on-u-s-company "SK On Tennessee Becomes Newest SK On U.S. Company | SK"
[7]: https://eng.sk.com/news/sk-on-expands-u-s-ess-push-at-acp-cleanpower-2026 "SK On Expands U.S. ESS Push at ACP CLEANPOWER 2026 | SK"
[8]: https://www.hyundainews.com/releases/4876?utm_source=chatgpt.com "HSBMA Begins EV Battery Cell Production in Georgia"

---
