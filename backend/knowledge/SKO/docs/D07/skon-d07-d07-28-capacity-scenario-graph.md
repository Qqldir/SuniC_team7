---
id: skon-d07-d07-28-capacity-scenario-graph
title: Capacity Scenario Graph
summary: D07 생산 거점의 수요·인증·경제성·위험을 고려한 배터리 용량 할당 시나리오를 평가하고 최적 공장 배분을 도출하는 의사결정 프레임워크
tags: [d07, footprint, schema]
keywords: [배터리 캐파시티, 공장 할당, 시나리오 분석, Footprint Scenario, 45X 세제, 고객 수요, 설비 인증, 생산 리스크, 생산 용량, 공급 계획, HSBMA, Tennessee, 45X, ESS 전환, 공장 배분, 수요 변동, 경제성 분석, JV 운영]
related: []
priority: normal
domain: D07
section: D07-28.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 915
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-28. Capacity Scenario Graph

## 28.1 Scenario Nodes

```yaml
capacity_scenario_nodes:

  demand:
    - Existing EV customer demand
    - Slate contract
    - Nissan contract
    - HMG demand
    - GRIDON ESS demand

  physical_capacity:
    - SKBA Commerce
    - HSBMA
    - Tennessee
    - Hungary
    - Yancheng

  qualification:
    - Customer approval
    - Product approval
    - Chemistry approval
    - Regulatory compliance

  economics:
    - Fixed cost
    - 45X eligibility
    - Tariff
    - Logistics
    - Conversion CAPEX
    - Incentive covenant

  risk:
    - Ramp delay
    - Customer cancellation
    - PFE exposure
    - Utility shortage
    - Ownership restriction
```

---

## 28.2 Scenario Relationship Graph

```text
Customer Contract
        ↓
Required Product·Origin·Timing
        ↓
Technically Compatible Plants
        ↓
Customer-Qualified Plants
        ↓
Policy-Eligible Plants
        ↓
JV·Contractually Available Plants
        ↓
Utility·Labor Available Capacity
        ↓
Expected Good Output
        ↓
Economic Plant Allocation
```

---

## 28.3 Major Scenarios

```yaml
footprint_scenarios:

  - scenario_id: FSC-D07-001
    title: HSBMA Ramp Slower than HMG Demand
    effects:
      - Cell inventory shortage
      - Vehicle production disruption
      - Emergency alternative sourcing
    required_data:
      - HMG build schedule
      - HSBMA qualified output
      - Alternative HMG-qualified site

  - scenario_id: FSC-D07-002
    title: SKBA EV Demand Decline
    effects:
      - Idle capacity
      - Fixed-cost increase
      - ESS conversion pressure
    required_data:
      - Current Ford and Volkswagen allocation
      - Slate allocation
      - GRIDON conversion readiness

  - scenario_id: FSC-D07-003
    title: Tennessee 2028 Ramp Delay
    effects:
      - Nissan-supply risk if allocated there
      - Continued pre-SOP cost
      - Alternative-site qualification need
    control:
      - Nissan-to-Tennessee relationship remains hypothetical

  - scenario_id: FSC-D07-004
    title: 45X PFE Eligibility Loss
    effects:
      - Lower tax-credit recognition
      - Supplier replacement
      - Margin and allocation change
    required_data:
      - Material-assistance cost ratio
      - Supplier ownership
      - Origin traceability

  - scenario_id: FSC-D07-005
    title: EU Carbon and Energy Cost Pressure
    effects:
      - Hungary competitiveness decline
      - Customer allocation shift
      - Renewable-power investment need

  - scenario_id: FSC-D07-006
    title: China Stake-Swap Delay
    effects:
      - Ownership ambiguity
      - Capacity-governance delay
      - JV and consolidated reporting mismatch
```

---

## 28.4 Scenario Output Schema

```yaml
capacity_scenario_output:

  capacity:
    - Physical GWh
    - Qualified GWh
    - Good-output GWh
    - Commercially available GWh
    - Recoverable alternative GWh

  finance:
    - Fixed-cost absorption
    - Incentive and tax credit
    - Conversion CAPEX
    - Logistics
    - Revenue at risk

  customer:
    - Unserved demand
    - Delay
    - Alternative-site status

  operations:
    - Utilization
    - Ramp requirement
    - Workforce
    - Utility

  confidence:
    - Evidence level
    - Missing inputs
    - Scenario probability
```

---
