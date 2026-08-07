---
id: skon-d06-d06-25-formation-energy-inventory-throughput-pa
title: Formation Energy·Inventory·Throughput Pain Points
summary: "배터리 셀 Formation/Aging 공정의 에너지 소비, 처리량, 재고 병목을 분류하고 에너지·용량 드라이버를 정의한 문서"
tags: [d06, process, schema]
keywords: [에이징, WIP, 리드타임, 설비효율, 불량검출, 오검사, 등급분포, 데이터단편화, 충방전, 온도관리, Formation, Aging, 처리량, 에너지 효율, 장비 활용률, 불량 발견, 오판별, 등급 분포, 열 관리]
related: []
priority: normal
domain: D06
section: D06-25.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 932
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-25. Formation Energy·Inventory·Throughput Pain Points

## 25.1 Pain-Point Register

```yaml
cell_finishing_pain_points:

  - pain_point_id: PP-D06-008
    title: Long Formation and Aging Lead Time
    processes:
      - PROC-SKON-D06-015
      - PROC-SKON-D06-017
    impacts:
      - High WIP inventory
      - Large floor-space requirement
      - Slow upstream feedback
      - Long production lead time
    evidence_level: THIRD_PARTY_VERIFIED

  - pain_point_id: PP-D06-009
    title: Formation Equipment and Channel Utilization
    process:
      - PROC-SKON-D06-015
    causes:
      - Long recipes
      - Channel imbalance
      - Tray-loading delays
      - Retest cells
      - Equipment maintenance
    impacts:
      - Low throughput
      - High equipment count
    evidence_level: ANALYST_INFERENCE

  - pain_point_id: PP-D06-010
    title: Electrical Energy and Heat Management
    process:
      - PROC-SKON-D06-015
    causes:
      - Repeated charge-discharge
      - Conversion loss
      - Cooling requirement
    impacts:
      - Energy cost
      - Facility load
      - Temperature variation
    evidence_level: THIRD_PARTY_VERIFIED

  - pain_point_id: PP-D06-011
    title: Late Defect Discovery
    processes:
      - PROC-SKON-D06-015
      - PROC-SKON-D06-017
      - PROC-SKON-D06-018
    impacts:
      - Value-added scrap
      - Large affected population
      - Delayed root-cause containment
    evidence_level: THIRD_PARTY_VERIFIED

  - pain_point_id: PP-D06-012
    title: False Reject and Retest Burden
    processes:
      - PROC-SKON-D06-018A
      - PROC-SKON-D06-018B
      - PROC-SKON-D06-018C
    causes:
      - Sensor noise
      - Contact error
      - Conservative threshold
      - Model uncertainty
    impacts:
      - Retest queue
      - Good-cell scrap risk
    evidence_level: ANALYST_INFERENCE

  - pain_point_id: PP-D06-013
    title: Grade Distribution Instability
    process:
      - PROC-SKON-D06-018
    causes:
      - Material and upstream process shift
      - Tester bias
      - Recipe change
    impacts:
      - Module matching difficulty
      - Inventory imbalance
      - Customer allocation constraint
    evidence_level: ANALYST_INFERENCE

  - pain_point_id: PP-D06-014
    title: Fragmented Cell-Finishing Data
    processes:
      - PROC-SKON-D06-015
      - PROC-SKON-D06-016
      - PROC-SKON-D06-017
      - PROC-SKON-D06-018
    impacts:
      - Slow cause analysis
      - Weak model transfer
      - Incomplete genealogy
    evidence_level: HYPOTHESIS
```

---

## 25.2 Energy and Inventory Model

```yaml
cell_finishing_resource_model:

  formation:
    energy_drivers:
      - Charge-discharge energy
      - Power-conversion loss
      - Cooling and ventilation
      - Standby power

    capacity_drivers:
      - Number of channels
      - Recipe duration
      - Tray cycle time
      - Channel availability
      - Retest share

  aging:
    capacity_drivers:
      - Storage duration
      - Rack density
      - Measurement frequency
      - Temperature-controlled space
      - Hold and retest cells

  inspection:
    capacity_drivers:
      - Inspection takt
      - Image-acquisition time
      - False-reject rate
      - Retest queue
      - Manual engineering review

  prohibited_use:
    - Do not populate with SK On values without plant data
```

---
