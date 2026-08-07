---
id: skon-d06-d06-53-bottleneck-wip-scheduling-model
title: Bottleneck·WIP·Scheduling Model
summary: 배터리 제조의 병목 현상 유형과 포메이션·에이징 공정의 재공품 상태 및 생산 제약 조건 모델
tags: [d06, process, schema]
keywords: [생산 병목, 미완성품 관리, 포메이션 공정, 에이징, 전해액 함침, 공정 제약, 품질 홀드, 장시간 체류, 병목현상, 포메이션, 재공품관리, 생산제약, 품질병목, 전해액함침, 장시간체류]
related: []
priority: normal
domain: D06
section: D06-53.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1402
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-53. Bottleneck·WIP·Scheduling Model

## 53.1 Static vs Dynamic Bottleneck

```yaml
bottleneck_types:

  static_bottleneck:
    definition: >
      장기간 평균 처리능력이 가장 낮아 전체 생산량을 제한하는 공정

  dynamic_bottleneck:
    definition: >
      제품 Mix, 고장, Changeover, 품질 Hold와 WIP 상태에 따라
      시간대별로 바뀌는 병목

  quality_bottleneck:
    definition: >
      물리적 처리량은 충분하지만 검사·재검·승인 대기로 흐름을 제한

  utility_bottleneck:
    definition: >
      전력, 건조공기, 냉각, 진공 등 공용 Utility가 생산을 제한

  information_bottleneck:
    definition: >
      Release, 승인, 데이터 연결이나 시스템 지연이 물류흐름을 제한
```

---

## 53.2 Battery-Specific Long-Dwell Processes

전해액 함침, 포메이션과 에이징은 셀별 체류시간이 길고 많은 WIP·공간·충방전 채널을 요구할 수 있다. 포메이션 설비는 셀마다 개별 제어 채널을 필요로 하므로, Recipe 시간·재검 비율과 채널가동률이 공장 처리량에 직접적인 제약이 될 수 있다. ([Royal Society of Chemistry Publications][5])

```yaml
long_dwell_processes:

  electrolyte_wetting:
    capacity_drivers:
      - Soaking time
      - Vacuum-pressure cycle
      - Rack capacity

  formation:
    capacity_drivers:
      - Recipe duration
      - Number of channels
      - Tray logistics
      - Retest share
      - Channel availability

  aging:
    capacity_drivers:
      - Hold duration
      - Rack or warehouse capacity
      - Temperature zone
      - Measurement schedule

  quality_hold:
    capacity_drivers:
      - Engineering review
      - Additional inspection
      - Deviation approval
```

---

## 53.3 WIP State Model

```yaml
wip_state:

  object_id: required
  object_type:
    - Electrode roll
    - Cell stack
    - Unformed cell
    - Formation cell
    - Aged cell
    - Module
    - Pack

  current_process: required
  current_location: required

  status:
    - QUEUED
    - PROCESSING
    - WAITING_QUALITY
    - WAITING_MATERIAL
    - WAITING_EQUIPMENT
    - RETEST
    - REWORK
    - QUARANTINE
    - RELEASED

  timestamps:
    - Process arrival
    - Queue start
    - Processing start
    - Processing end
    - Release

  constraints:
    - Maximum exposure time
    - Maximum storage time
    - Temperature requirement
    - Grade requirement
    - Recipe compatibility

  value:
    - Material value
    - Accumulated conversion value
    - Energy capacity
```

---

## 53.4 Scheduling Constraint Model

```yaml
battery_production_scheduling_constraints:

  material:
    - Material-lot release
    - Expiry and open time
    - Supplier qualification
    - Product-specific formulation

  equipment:
    - Recipe capability
    - Tool availability
    - Maintenance window
    - Product changeover
    - Ramp-up restriction

  quality:
    - Hold and deviation
    - Inspection capacity
    - Retest queue
    - Grade availability

  process:
    - Wetting minimum time
    - Formation recipe
    - Aging duration
    - Adhesive curing
    - Dry-room exposure

  utility:
    - Peak power
    - Formation-energy recovery
    - Dry-room and oven load
    - Cooling capacity

  customer:
    - Product revision
    - Customer qualification
    - Shipping SOC
    - Delivery date
```

---

## 53.5 Dynamic Bottleneck Detection

```text
Equipment State + WIP + Cycle Time + Quality Hold
                       ↓
               Near-Term Capacity
                       ↓
     Predicted Starvation·Blocking·Queue Growth
                       ↓
                Bottleneck Ranking
                       ↓
        Schedule / Maintenance / Routing Action
```

```yaml
dynamic_bottleneck_score:

  components:
    - Queue-growth rate
    - Utilization
    - Cycle-time deviation
    - Downstream blocking
    - Upstream starvation
    - Failure probability
    - Quality-hold probability
    - Recovery time

  output:
    - Current bottleneck
    - Predicted bottleneck
    - Time to constraint
    - Recommended intervention

  control:
    - Do not rank solely by utilization
    - Separate failure, quality and flow causes
```

---

## 53.6 WIP·Bottleneck OI Seed

```yaml
seed_id: OI-SEED-D06-043
title: Formation–Aging Dynamic Bottleneck Optimizer

strategy:
  - Reduce cell-finishing lead time and WIP

target:
  - Wetting, formation, degassing, aging and grading

needed_capability:
  - Real-time WIP state
  - Formation-channel availability
  - Aging-rack capacity
  - Retest-risk prediction
  - Energy-aware tray assignment

expected_kpi:
  - Cell-finishing lead time
  - Formation-channel utilization
  - Aging WIP
  - Retest queue
  - Peak electricity demand

priority: VERY_HIGH
```

---
