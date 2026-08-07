---
id: skon-d07-d07-05-capacity-utilization-trend
title: Capacity·Utilization Trend
summary: "SK온 D07 생산거점의 2024-2026년 생산능력 및 평균 가동률 추이를 보여주는 표와, 신규 공장 추가가 용량 증가와 가동률 분리를 초래하는 원리를 설명한다."
tags: [d07, footprint, schema]
keywords: [용량활용, 생산능력, 평균가동률, 신규거점, Ramp-Up, 설계능력, 고객승인, 수율, GWh, 가동률, D07, 공시, Cell 생산, 평균 가동률, 연결 기준]
related: []
priority: normal
domain: D07
section: D07-05.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 538
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-05. Capacity·Utilization Trend

## 05.1 연결 기준 Trend

| 기간        | 공시상 최대 생산능력 | 평균 가동률 | 해석                        |
| --------- | ----------: | -----: | ------------------------- |
| 2024년     |     71.5GWh |  43.8% | 이반차 부분가동 반영               |
| 2025년     |     94.6GWh |  48.7% | 신규거점 Ramp-Up              |
| 2026년 1분기 |     97.4GWh |  36.5% | Capacity 증가와 가동률 하락 동시 발생 |

2026년 1분기 실제 생산실적은 4,336만6천 Cell로 공시됐다. 가동률 36.5%는 연결 종속 생산법인의 평균치이며, 특정 공장의 가동률로 배분할 수 없다. ([KIND][1])

```yaml
utilization_evidence_boundary:

  confirmed:
    - Consolidated average utilization
    - Consolidated cell-production volume
    - Company-defined operating-time methodology

  not_confirmed:
    - Plant-level utilization
    - Line-level utilization
    - Product-specific utilization
    - EV versus ESS utilization
    - Nameplate versus customer-qualified utilization

  prohibited:
    - Apply 36.5 percent equally to all plants
    - Estimate plant output by multiplying every plant capacity by 36.5 percent
```

---

## 05.2 Capacity Growth와 가동률의 분리

```text
New Plant Capacity Added
          ↓
Reported Maximum Capacity Increases
          ↓
Customer Qualification·Demand·Yield Ramp Needed
          ↓
Actual Production May Grow More Slowly
          ↓
Average Utilization Can Decline
```

따라서 `Capacity 증가 = 실제 생산·매출 증가`로 해석해서는 안 된다. 신규 공장은 부분가동·고객승인·수율 안정화 과정에서 설계능력보다 낮은 수준으로 운영될 수 있다.

---
