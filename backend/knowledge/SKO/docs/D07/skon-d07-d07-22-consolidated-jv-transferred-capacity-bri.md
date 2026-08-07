---
id: skon-d07-d07-22-consolidated-jv-transferred-capacity-bri
title: Consolidated·JV·Transferred Capacity Bridge
summary: SK온 Q1 2026 공식 연결 용량 97.4GWh에서 Kentucky 1 이전(3.1GWh)을 반영하고 JV와 이전 용량을 제외한 Pro Forma 기준 생산 능력 분석
tags: [d07, footprint, schema]
keywords: [배터리 생산 용량, Q1 2026, Pro Forma, 캐파 이관, JV 지분, Kentucky 1, GWh, 구조적 조정, 통합 기준, 캐파시티 조정, 연결 생산 능력, 프로포마, 용량 이전, HSBMA, 합작회사, 램프업, 용량 폭포]
related: []
priority: normal
domain: D07
section: D07-22.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 486
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-22. Consolidated·JV·Transferred Capacity Bridge

## 22.1 Post-Restructuring Analytical Bridge

```yaml
post_restructuring_capacity_bridge:

  official_q1_2026_consolidated_capacity_gwh: 97.4

  known_structural_adjustment:
    kentucky_1_capacity_transferred_gwh: -3.1

  derived_known_scope_baseline_gwh: 94.3

  classification:
    value_type: ANALYST_DERIVED_PRO_FORMA
    official_company_restatement: false

  excluded_from_derived_total:
    hsbma:
      gross_design_capacity_gwh: 35
      reason: 50_50_JV

    tennessee:
      counted_current_capacity_gwh: 0
      reason: PRE_SOP

    kentucky_2:
      counted_q1_capacity_gwh: 0
      reason: NOT_INCLUDED_IN_Q1_CAPACITY

    changzhou_and_huizhou:
      reason: JV_AND_EQUITY_METHOD_CAPACITY

  unresolved_changes:
    - Additional Ivancsa ramp after Q1
    - Additional Yancheng 3 ramp after Q1
    - Q2 plant normalization
    - China ownership-closing treatment
```

**94.3GWh는 공식 SK온 수치가 아니다.** Q1 97.4GWh에서 당시 포함됐던 Kentucky 1의 3.1GWh만 제거한 구조적 Pro Forma다. HSBMA의 35GWh를 더하지 않으며, Q2 중 다른 공장의 증설·Ramp-Up이 있었는지는 다음 반기보고서가 필요하다. ([KIND][11])

---

## 22.2 Capacity Waterfall

```text
2026 Q1 Official Consolidated Capacity
97.4 GWh
        ↓
Kentucky 1 Transferred to Ford
−3.1 GWh
        ↓
Known-Scope Pro Forma
94.3 GWh
        ↓
Plus: Additional Ramp After Q1
UNKNOWN
        ↓
Current Official Consolidated Capacity
UNRESOLVED
```

```text
Separate Physical Footprint
HSBMA 35 GWh JV Gross
+
Tennessee 45 GWh Legacy Design Reference
+
China JV Sites
≠
SK On Consolidated Capacity
```

---
