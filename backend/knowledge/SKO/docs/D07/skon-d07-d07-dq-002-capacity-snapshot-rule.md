---
id: skon-d07-d07-dq-002-capacity-snapshot-rule
title: 002. Capacity Snapshot Rule
summary: "SK온 배터리 생산 역량의 산정 기준과 2026년 말 목표 설정, 사업장 구조 변화에 따른 역량 재산정 과제를 설명한다."
tags: [d07, footprint, schema]
keywords: [배터리 생산능력, 연결 생산능력, GWh, 블루오벌, HSBMA, 자산이전, 구조개편, 2026년 목표, SK이노베이션, 배터리 캐파, 배터리 생산 역량, BlueOval SK, Tennessee, Kentucky, 연결 역량, 사업 구조 변화]
related: []
priority: normal
domain: D07
section: D07-DQ
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 361
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-DQ-002. Capacity Snapshot Rule

```yaml
capacity_snapshot_policy:

  latest_regulatory_snapshot:
    date: 2026-03-31
    consolidated_normalized_capacity_gwh: 97.4

  post_snapshot_events:
    - BlueOval SK dissolution and Kentucky asset transfer
    - SK On Tennessee standalone establishment
    - HSBMA commercial production start
    - China joint-venture stake-swap amendment

  current_exact_consolidated_capacity:
    status: UNRESOLVED
    reason:
      - No post-restructuring consolidated capacity table has been published
      - HSBMA is a 50:50 JV and should not be added as consolidated capacity
      - Tennessee is not yet in mass production
      - Kentucky capacity was included in Q1 but transferred in May 2026
      - China ownership restructuring remains pending

  year_end_2026_target:
    value_gwh: more_than_179
    status: CORPORATE_TARGET
```

SK이노베이션의 2026년 1분기 분기보고서는 3월 말 기준 연결 배터리 최대 생산능력을 연 97.4GWh로 공시했다. 같은 보고서에는 2026년 말까지 179GWh 이상의 연간 생산능력을 확보한다는 계획이 포함돼 있으나, 이는 달성 실적이 아닌 목표다. ([KIND][1])

---
