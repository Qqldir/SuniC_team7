---
id: skon-d07-d07-21-2024-2028-capacity-timeline
title: 2024–2028 Capacity Timeline
summary: 연결·비연결 기준으로 SK온의 2024~2028년 배터리 생산용량 변화추이와 주요 거점별 가동 일정을 정리한 표
tags: [d07, footprint, schema, table]
keywords: [배터리 생산 용량, Capacity Timeline, 연결 공시, GWh, 생산거점, HSBMA, Kentucky, Yancheng, Tennessee, JV Gross, 배터리 생산용량, 부분가동, 상업생산, Ramp-Up, 생산 로드맵, 설계용량]
related: []
priority: normal
domain: D07
section: D07-21.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 601
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-21. 2024–2028 Capacity Timeline

## 21.1 Three-Ledger Timeline

| 시점          | 연결 공시 Capacity |         JV Gross·비연결 Capacity | 주요 구조변화                      |
| ----------- | -------------: | ----------------------------: | ---------------------------- |
| 2024년 말     |        71.5GWh |                         별도 관리 | 이반차 부분가동                     |
| 2025년 말     |        94.6GWh |                         별도 관리 | Kentucky 1·Yancheng 3 부분가동   |
| 2026년 3월    |        97.4GWh |                  HSBMA 생산개시 전 | Kentucky 1의 3.1GWh 포함        |
| 2026년 5월 이후 |     공식 재작성표 없음 |          HSBMA 35GWh JV Gross | Kentucky 1·2 Ford 이전         |
| 2026년 6월 이후 |     공식 재작성표 없음 |            HSBMA 상업생산·Ramp-Up | 미국 ESS 생산목표 존재               |
| 2028년 목표    |            미확정 | Tennessee Legacy Design 45GWh | Tennessee SOP·Nissan 공급개시 목표 |

2024·2025·2026년 1분기 연결 Capacity와 가동률은 SK이노베이션 공시기준이며, 2026년 5월 이후의 현재 연결 Capacity는 아직 새 공시표로 확정되지 않았다. ([KIND][11])

---

## 21.2 Timeline Control

```yaml
capacity_timeline_control:

  parallel_ledgers:
    consolidated_capacity:
      purpose: Financial and consolidated operating scope

    jv_gross_capacity:
      purpose: Physical production footprint under joint ownership

    transferred_capacity:
      purpose: Historical comparison and restructuring analysis

    future_design_capacity:
      purpose: Construction and strategic-planning scenario

    customer_demand_commitment:
      purpose: Contract-linked future load

  prohibited:
    - Add all ledgers to one global number
    - Treat supply-contract total as annual capacity
    - Treat commercial-production start as full design utilization
    - Treat legacy design as commissioned 2028 output
```

---
