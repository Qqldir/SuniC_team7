---
id: skon-d06-d06-47-energy-dry-room-formation-model
title: Energy·Dry-Room·Formation Model
summary: "배터리 제조의 드라이룸, 전극건조, 포메이션 등 주요 공정에서 에너지를 측정·할당하고 손실을 분류하기 위한 체계와 모델."
tags: [d06, process, schema]
keywords: [에너지 계량, 드라이룸, 전극건조, 용매회수, 에너지 손실 분류, 배터리 제조공정, 에너지 KPI, 조립공정, 배터리 제조 공정, 포메이션, 에너지 할당, 손실 분류, 공정 드라이버, 정규화 KPI, 용매 회수]
related: []
priority: normal
domain: D06
section: D06-47.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 777
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-47. Energy·Dry-Room·Formation Model

과거 Argonne 분석은 드라이룸, 전극건조·용매회수와 포메이션을 배터리 제조의 주요 에너지 사용영역으로 다뤘으며, 2025년에는 조립공정 에너지 모델이 최근 자료에 맞춰 갱신됐다. 모델의 수치를 SK온 공장에 직접 적용해서는 안 된다. ([Greet][8])

## 47.1 Energy Meter Hierarchy

```text
Plant Main Meter
      ↓
Utility System
      ├── Electricity
      ├── Natural Gas or Heat
      ├── Chilled Water
      ├── Cooling Water
      ├── Compressed Air
      ├── Vacuum
      └── Dry Air
              ↓
Production Area
              ↓
Line
              ↓
Equipment
              ↓
Product·Batch·Cell Allocation
```

---

## 47.2 Energy Entity Schema

```yaml
manufacturing_energy_record:

  meter:
    - Meter ID
    - Utility type
    - Location
    - Measurement interval
    - Calibration

  consumption:
    - Start reading
    - End reading
    - Actual consumption
    - Peak demand
    - Power factor where applicable

  operating_context:
    - Equipment state
    - Product
    - Recipe
    - Output count
    - Good output
    - Environmental condition

  allocation:
    - Direct consumption
    - Shared utility allocation
    - Standby allocation
    - Rework allocation

  normalized_kpis:
    - Energy per good cell
    - Energy per electrode area
    - Energy per accepted kWh
    - Dry-room energy per assembly-hour
    - Formation net energy per good cell
```

---

## 47.3 Process Energy Drivers

```yaml
energy_driver_master:

  mixing:
    - Motor load
    - Mixing time
    - Vacuum
    - Temperature control

  coating_drying:
    - Oven heat
    - Exhaust air
    - Line speed
    - Solvent load
    - Solvent recovery

  dry_room:
    - Outdoor humidity
    - Air infiltration
    - Door opening
    - Personnel
    - Exhaust makeup air
    - Target dew point

  formation:
    - Charging and discharging
    - Power-conversion efficiency
    - Energy recovery
    - Cooling
    - Channel utilization

  module_pack:
    - Adhesive curing
    - Welding
    - Leak testing
    - Thermal validation
```

---

## 47.4 Energy Loss Taxonomy

```yaml
energy_loss_taxonomy:

  productive:
    - Energy used while producing accepted product

  quality_loss:
    - Energy applied to scrapped product
    - Rework energy
    - Retest energy

  operating_loss:
    - Idle
    - Warm-up
    - Start-up
    - Changeover
    - Shutdown

  utility_loss:
    - Leakage
    - Excess pressure
    - Overcooling
    - Overdrying
    - Unbalanced flow

  scheduling_loss:
    - Peak demand
    - Poor formation energy recovery
    - Uncoordinated utility operation
```

---
