---
id: skon-d07-d07-03-capacity-reconciliation
title: Capacity Reconciliation
summary: SK온 2026년 1분기 연결 생산능력 97.4GWh의 거점별 구성과 설계 기준 대비 공시 기준 용량의 차이를 설명하는 문서
tags: [d07, footprint, schema, table]
keywords: [생산능력, 공시용량, 설계용량, GWh, 거점, 환산치, 공동기업, 연결재무, 부분가동, JV, 캐패시티, 연결통합, 설계기준, 공시기준, 환산]
related: []
priority: normal
domain: D07
section: D07-03.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 912
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-03. Capacity Reconciliation

## 03.1 2026년 1분기 연결 Capacity

```yaml
q1_2026_consolidated_capacity_bridge:

  korea:
    seosan: 4.7

  europe:
    komarom_1: 7.5
    komarom_2: 10.3
    ivancsa_partial: 20.0
    subtotal: 37.8

  china:
    yancheng_1: 10.0
    yancheng_2: 17.0
    yancheng_3_partial: 2.8
    subtotal: 29.8

  united_states:
    georgia_1: 10.3
    georgia_2: 11.7
    kentucky_1_partial_at_q1: 3.1
    subtotal: 25.1

  consolidated_total_gwh: 97.4
  reference_date: 2026-03-31
```

합계는 `4.7 + 37.8 + 29.8 + 25.1 = 97.4GWh`다. 이는 2026년 3월 말의 연결 공시 Snapshot으로, 5월 켄터키 이전 전 구조다. ([KIND][1])

---

## 03.2 연결 Capacity에 포함하지 않는 생산거점

```yaml
excluded_capacity_records:

  changzhou:
    reason:
      - Accounting treatment as joint venture
    historical_design_capacity_gwh: 7.5

  huizhou:
    reason:
      - Accounting treatment as joint venture
      - Stake disposal pending
    historical_design_capacity_gwh: 10.0

  hsbma:
    reason:
      - 50:50 joint venture
      - Commercial production began after Q1 reference date
    gross_design_capacity_gwh: 35.0

  tennessee:
    reason:
      - Mass production has not started
    current_counted_capacity_gwh: 0
    design_capacity_record:
      value_gwh: 45
      status: LEGACY_DESIGN_PLAN

  kentucky:
    reason:
      - Transferred to Ford
    current_sk_on_capacity_gwh: 0
```

SK이노베이션은 중국 창저우와 후이저우 공장을 실질적 생산거점으로 보지만 회계상 공동기업이어서 연결 생산능력 표에서 제외해왔다. HSBMA 역시 50:50 JV이므로 Gross Capacity와 SK온 연결 Capacity를 분리해야 한다. ([KIND][1])

---

## 03.3 Design Capacity와 공시 Capacity 차이

| 거점     | 설계·IR Capacity | 2026 Q1 공시 Capacity | 해석              |
| ------ | -------------: | ------------------: | --------------- |
| 서산 기존동 |         7.0GWh |              4.7GWh | 설계최대와 공시 환산치 분리 |
| 코마롬 2  |        약 10GWh |             10.3GWh | 공시 산식·설비환산 차이   |
| 이반차    |          30GWh |               20GWh | 전체의 66.7% 부분가동  |
| 조지아 1  |        약 10GWh |             10.3GWh | 환산 산식 차이        |
| 조지아 2  |        약 12GWh |             11.7GWh | 환산 산식 차이        |
| 옌청 3   |          33GWh |              2.8GWh | 전체의 8.33% 부분가동  |
| 테네시    |       45GWh 계획 |          0GWh 현재 반영 | 2028 생산개시 전망    |

SK이노베이션의 2025년 4분기 IR 자료는 설계·최대가동 기준 Capacity를 제시한 반면, 2026년 1분기 공시는 기준일 현재 생산가능 수준을 연간으로 환산했다. 따라서 두 수치를 오류로 병합하지 않고 `GROSS_DESIGN_CAPACITY`와 `REPORTED_NORMALIZED_CAPACITY`로 병렬 저장한다. ([파일SCS][2])

---
