---
id: skon-d07-d07-08-initial-data-gap-register
title: Initial Data Gap Register
summary: "SK온 배터리 생산거점의 용량, 가동률, 고객 계약 등 필수 데이터 격차 8건을 우선순위별로 정리한 레지스터."
tags: [d07, footprint, schema]
keywords: [생산 용량, 가동률, BlueOval, Seosan, Georgia, HSBMA, Tennessee, 고객-라인 매핑, 수율, OEM, 데이터 격차, Data Gap, 배터리 캐파, 생산거점, 미확인 정보]
related: []
priority: normal
domain: D07
section: D07-08.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 447
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-08. Initial Data Gap Register

```yaml
footprint_data_gaps:

  - gap_id: GAP-D07-001
    subject: Post-BlueOval consolidated capacity
    missing:
      - Restated total capacity after Kentucky transfer
    priority: CRITICAL

  - gap_id: GAP-D07-002
    subject: Plant-level utilization
    missing:
      - Actual production
      - Utilization
      - Yield
      - OEE
    priority: CRITICAL

  - gap_id: GAP-D07-003
    subject: Seosan capacity
    missing:
      - Reason for 7.0GWh design versus 4.7GWh regulatory capacity
      - Status of 14GWh third-plant plan
    priority: VERY_HIGH

  - gap_id: GAP-D07-004
    subject: Georgia SKBA configuration
    missing:
      - Current line allocation
      - EV and ESS product mix
      - Current workforce and operating pattern
    priority: VERY_HIGH

  - gap_id: GAP-D07-005
    subject: HSBMA ramp
    missing:
      - Current normalized production capacity
      - Yield and utilization
      - Ramp schedule to 35GWh
    priority: VERY_HIGH

  - gap_id: GAP-D07-006
    subject: Tennessee
    missing:
      - Product chemistry
      - Customer
      - Initial line capacity
      - Detailed 2028 SOP schedule
    priority: VERY_HIGH

  - gap_id: GAP-D07-007
    subject: China stake swap
    missing:
      - Actual closing confirmation
      - Consolidation-date treatment
      - Huizhou operational handover
    priority: HIGH

  - gap_id: GAP-D07-008
    subject: Customer-to-line mapping
    missing:
      - OEM
      - Vehicle program
      - Cell product
      - Contract volume
      - Alternative line
    priority: CRITICAL
```

---
