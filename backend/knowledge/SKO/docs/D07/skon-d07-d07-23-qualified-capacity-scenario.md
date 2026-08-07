---
id: skon-d07-d07-23-qualified-capacity-scenario
title: Qualified Capacity Scenario
summary: "SK온 배터리 생산 시설의 용량을 설계·설치·적격 단계별로 정의하는 체계와 2026년의 HSBMA, GRIDON 미국 생산, Tennessee 2028 가동 등 4가지 주요 시나리오를 담은 문서."
tags: [d07, footprint, schema]
keywords: [생산 거점, 배터리 캐파, HSBMA, GRIDON, Tennessee, 설계 용량, 고객 인증, ESS 국산화, 캐파시티 계층, 현대기아, ESS, SOP, GWh, 생산 시나리오, 로컬라이제이션]
related: []
priority: normal
domain: D07
section: D07-23.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 991
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-23. Qualified Capacity Scenario

## 23.1 Capacity Qualification Ladder

```text
Gross Design Capacity
        ↓
Installed Capacity
        ↓
Mechanically Available Capacity
        ↓
Process-Qualified Capacity
        ↓
Customer-Qualified Capacity
        ↓
Scheduled Capacity
        ↓
Good-Output Capacity
        ↓
Commercially Allocable Capacity
```

```yaml
qualified_capacity_layers:

  design_capacity:
    question: What was the facility designed to produce?

  installed_capacity:
    question: Which equipment has been installed and accepted?

  available_capacity:
    question: Which equipment can currently operate?

  process_qualified_capacity:
    question: Which lines have stable process capability?

  customer_qualified_capacity:
    question: Which lines and products have customer approval?

  good_output_capacity:
    question: How much customer-releasable output can be produced?

  commercially_allocable_capacity:
    question: >
      How much can be assigned after contracts, JVs, incentives,
      tariffs and local-content requirements?
```

---

## 23.2 2026 Scenario Set

### SCEN-D07-001 — Conservative Current Supply

```yaml
scenario_id: SCEN-D07-001
title: Conservative Current Consolidated Supply

starting_point:
  value_gwh: 94.3
  type: ANALYST_DERIVED_PRO_FORMA

included:
  - Q1 consolidated plants excluding transferred Kentucky 1

excluded:
  - HSBMA gross capacity
  - Tennessee legacy design
  - Unverified post-Q1 ramp

principal_uncertainty:
  - Plant-level customer-qualified capacity
  - Good-output capacity
```

### SCEN-D07-002 — HSBMA Ramp

```yaml
scenario_id: SCEN-D07-002
title: HSBMA Customer Ramp

physical_capacity:
  gross_design_gwh: 35

qualification:
  commercial_production_started: true
  full_design_output: NOT_CONFIRMED
  current_customer:
    - Hyundai_Motor_Group
  initial_model:
    - IONIQ_9

capacity_class:
  - JV_GROSS
  - CUSTOMER_LINKED
  - NOT_FREELY_ALLOCABLE
```

### SCEN-D07-003 — U.S. ESS Localization

```yaml
scenario_id: SCEN-D07-003
title: U.S. GRIDON Localization

official_target:
  - U.S. production of GRIDON Gen 1 during 2026

exact_site:
  status: UNRESOLVED

candidate_network:
  - SK_Battery_America
  - HSBMA
  - SK_On_Tennessee

constraints:
  - HSBMA partner and customer restrictions
  - Tennessee pre-SOP status
  - EV-to-ESS line qualification
  - Chemistry and module architecture
  - 45X and PFE eligibility
```

SK온은 2026년 중 GRIDON 1세대 미국 생산을 시작할 계획이며, 미국 제조 Network로 SKBA·HSBMA·Tennessee를 언급했다. 그러나 정확한 생산 Site는 공개하지 않았고 Tennessee는 2028년 생산개시를 준비하는 단계다. ([SK][12])

### SCEN-D07-004 — Tennessee 2028 Ramp

```yaml
scenario_id: SCEN-D07-004
title: Tennessee 2028 Start-Up

legacy_design_capacity_gwh: 45
actual_initial_qualified_capacity: UNRESOLVED

possible_demand:
  - Nissan supply beginning in 2028
  - Other U.S. EV programs
  - ESS optionality

prohibited_assumption:
  - Nissan contract equals Tennessee allocation
  - Full 45 GWh is available at SOP
```

### SCEN-D07-005 — Europe Ramp & Compliance

```yaml
scenario_id: SCEN-D07-005
title: Hungary Capacity and EU Compliance

capacity_opportunities:
  - Ivancsa ramp toward 30 GWh design level
  - Komarom process optimization

qualification_constraints:
  - Customer approval
  - EU battery carbon-footprint information
  - Battery-passport data
  - Material due diligence
  - Energy and water availability
```

---
