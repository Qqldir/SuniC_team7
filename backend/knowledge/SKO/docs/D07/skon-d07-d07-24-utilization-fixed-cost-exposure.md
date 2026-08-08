---
id: skon-d07-d07-24-utilization-fixed-cost-exposure
title: Utilization·Fixed-Cost Exposure
summary: "SK온 배터리 공장들의 고정비 부담도를 평가하기 위한 가동률 지표, 8개 거점의 고정비 노출 분류, 리스크 관리 스키마를 설명하는 문서."
tags: [d07, footprint, schema, table]
keywords: [가동률, utilization, 고정비, fixed-cost exposure, 생산거점, Ramp, GWh, 감가상각, 수율, 거점별 노출, fixed cost, 고정비 부담, battery plant, ESS, 제조원가, 공장 리스크]
related: []
priority: normal
domain: D07
section: D07-24.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 948
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-24. Utilization·Fixed-Cost Exposure

## 24.1 Utilization Boundary

```yaml
utilization_snapshot:

  consolidated_average:

    2024:
      value: 43.8_percent

    2025:
      value: 48.7_percent

    2026_Q1:
      value: 36.5_percent

  company_formula:
    utilization: load_time / operating_time

  unavailable:
    - Plant utilization
    - Line utilization
    - Product utilization
    - Customer utilization
    - EV versus ESS utilization
```

SK이노베이션 공시는 가동률을 `부하시간 ÷ 조업시간`으로 계산하며, 생산대기·자재부족·설비개조 등의 계획정지시간을 부하시간에서 제외한다. 따라서 일반적인 실제생산량/Nameplate Capacity와 같은 지표로 해석해서는 안 된다. ([KIND][11])

---

## 24.2 Fixed-Cost Exposure Model

```yaml
plant_fixed_cost_exposure:

  conceptual_formula: >
    plant_fixed_cost
    /
    customer_releasable_good_output

  fixed_cost_categories:
    - Depreciation
    - Salaried labor
    - Facility maintenance
    - Dry-room and HVAC base load
    - Property and local taxes
    - IT and OT systems
    - Security
    - Minimum utility charges
    - Financing and JV support cost where applicable

  exposure_multipliers:
    - Partial operation
    - Customer qualification delay
    - Material shortage
    - Low yield
    - Product-program cancellation
    - Line conversion
    - Retest and rework
```

---

## 24.3 Plant Exposure Classes

| 거점            | 공개상태              | Fixed-Cost Exposure 판정 |
| ------------- | ----------------- | ---------------------- |
| 서산            | 양산                | 공장별 가동률 미공개            |
| 코마롬 1·2       | 양산                | 고객·제품 Mix 미공개          |
| 이반차           | 30GWh 중 20GWh 반영  | Ramp 고정비 부담 가능성 높음     |
| 옌청 3          | 33GWh 중 2.8GWh 반영 | 초기 Ramp 부담 매우 높음       |
| SKBA Commerce | 양산                | 고객 Mix와 ESS 전환 여부 미확인  |
| HSBMA         | 2026년 SOP         | Ramp·고객승인 고정비 부담       |
| Tennessee     | 2028년 생산준비        | Pre-SOP 인력·시스템·유지비 부담  |
| Kentucky      | Ford 이전           | SK온 현재 고정비 범위에서 제외     |

Q2 배터리사업이 흑자전환했지만, 고객 보상금과 미국 세액공제 증가가 포함돼 있어 이를 모든 공장의 가동률·제조원가 정상화로 해석할 수 없다. ([ASK Inno][1])

---

## 24.4 Fixed-Cost Risk Record

```yaml
fixed_cost_risk_schema:

  risk_id: required
  plant_id: required

  capacity:
    - Installed GWh
    - Qualified GWh
    - Good-output GWh
    - Idle GWh

  cost:
    - Fixed manufacturing cost
    - Pre-SOP cost
    - Depreciation
    - Utility base load
    - Labor

  drivers:
    - Utilization
    - Yield
    - Customer allocation
    - Ramp delay
    - Conversion downtime

  mitigation:
    - Alternative customer
    - ESS conversion
    - Shift optimization
    - Temporary line shutdown
    - Asset transfer
    - Government support
```

---
