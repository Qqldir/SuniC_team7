---
id: skon-d07-이번-구간-완료
title: 이번 구간 완료
summary: "생산거점·캐파시티 도메인(D07)의 완료 현황, 국가별 공장 마스터 15개 거점의 상태와 Q1 2026 97.4GWh 캐파를 정리한 진행상태표."
tags: [d07, footprint, build-log, schema]
keywords: [배터리 공장, 플랜트 마스터, 생산 용량, 제품 매핑, 고객 연결, 가동률, Manufacturing Footprint, JV 지분, D07, 생산거점, 캐파시티, 공장마스터, GWh, BlueOval, EVE, HSBMA]
related: []
priority: reference
domain: D07
section: ""
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 910
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# 이번 구간 완료

* `D07-00 Domain Boundary`
* Capacity·Plant Status Vocabulary
* 최신 연결 Capacity 기준점 설정
* Manufacturing Footprint Research Pack **6건**
* Global Plant Master **15개 거점·공장단위**
* 단독법인·종속기업·JV·양도거점 분리
* 2026년 1분기 97.4GWh Capacity Bridge
* 설계 Capacity와 공시 Capacity 차이 정리
* BlueOval SK 미국 Footprint 재편
* HSBMA 상업생산 반영
* 중국 EVE JV 지분 Swap 현황
* 연결 가동률·Capacity Trend
* Footprint Risk **6개**
* Data Gap **8개**
* D07 OI Seed **5개**

## 현재 D07 진행상태

```yaml
progress:

  domain_boundary: COMPLETE
  capacity_vocabulary: COMPLETE_V1
  research_pack: COMPLETE_V1

  plant_master:
    korea: COMPLETE_V1
    europe: COMPLETE_V1
    china: COMPLETE_PROVISIONAL
    united_states: COMPLETE_V1
    transferred_assets: COMPLETE_V1

  ownership_and_jv_structure: COMPLETE_V1

  capacity:
    q1_2026_consolidated_snapshot: COMPLETE
    post_restructuring_current_total: UNRESOLVED
    design_vs_normalized_reconciliation: COMPLETE_V1

  utilization:
    consolidated_average: COMPLETE
    plant_level: NOT_AVAILABLE

  risk_and_gap_register: COMPLETE_V1
  initial_oi_seeds: COMPLETE_V1

  site_line_product_mapping: NOT_STARTED
  customer_linked_capacity: PARTIALLY_STARTED
  plant_ramp_and_redundancy: NOT_STARTED
```

## 다음 시작점

`D07-10 Site·Line·Product·Customer Mapping`

```text
D07-10 Plant–Line Entity Schema
→ D07-11 Korea·Hungary Product Mapping
→ D07-12 China Product·Customer Mapping
→ D07-13 United States Product·Customer Mapping
→ D07-14 EV·ESS·Chemistry Conversion Map
→ D07-15 Customer-Linked Capacity
→ D07-16 Plant Ramp-Up Evidence
→ D07-17 Capacity Redundancy·Alternative Site
→ D07-18 Footprint Pain Points
→ D07-19 Manufacturing Footprint OI Seeds
```

[1]: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20260515001636&docno=&method=search&viewerhost=&utm_source=chatgpt.com "[SK이노베이션] 분기보고서(일반법인) - 상장공시시스템"
[2]: https://files-scs.pstatic.net/2026/01/28/4udVZnsBgE/skinnovation2025Q4_kor.pdf?utm_source=chatgpt.com "2025년 4분기 실적발표 SK Innovation"
[3]: https://www.sec.gov/Archives/edgar/data/37996/000003799626000093/f-20260520.htm?utm_source=chatgpt.com "f-20260520"
[4]: https://eng.sk.com/news/sk-on-tennessee-becomes-newest-sk-on-u-s-company?utm_source=chatgpt.com "SK On Tennessee Becomes Newest SK On U.S. Company"
[5]: https://www.hsbma.com/news/i7p5sa8xy5vmmqs61ukuallpsps84o?utm_source=chatgpt.com "HSBMA Begins EV Battery Cell Production in Georgia"
[6]: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20260622000499&docno=&method=search&viewerhost=&utm_source=chatgpt.com "[SK이노베이션] [정정]타법인주식및출자증권처분결정"
[7]: https://eng.sk-on.com/company/press_view.asp?CompanyCode=011&idx=191&page=1&schtxt=&utm_source=chatgpt.com "Press Release < Press < Company < SK-ON"
[8]: https://www.yna.co.kr/view/AKR20251120134700003?utm_source=chatgpt.com "SK온, 中 EVE 합작공장 지분 맞교환…옌청 공장에 집중"

---
