---
id: skes-d06-14-ccs-and-low-carbon-lng-operations
title: CCS and Low-Carbon LNG Operations
summary: "배가스와 공정가스에서 CO2를 포집·정제·수송·주입하는 CCS 프로세스와 발전소 통합 운영 포인트, MRV 모니터링 방법을 다룬다."
tags: [d06, process, schema, table]
keywords: [탄소포집, CCS, 배가스, 저탄소LNG, MRV, 솔벤트, CO2 수송, 주입저장, 발전 연계]
related: [PROC-ENS-D06-CCS-001]
priority: normal
domain: D06
section: 14
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1028
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 14. CCS and Low-Carbon LNG Operations

## 14.1 Lifecycle Status

Barossa–Darwin–Bayu-Undan 연계 저탄소 LNG와 국내 발전 배가스 포집은 공개된 계획·공동연구·실증 축이다. D06의 CCS 프로세스는 실증·상용 설계를 위한 데이터 모델이며 현재 E&S 전체 사업에 상용 적용된 공정으로 표현하지 않는다.

## 14.2 `PROC-ENS-D06-CCS-001` — Capture·Conditioning·Transport·Injection·MRV

```yaml
status: PLANNED_OR_PILOT_BASELINE
capture_source_candidates:
  - natural_gas_power_flue_gas
  - upstream_gas_CO2_removed_before_LNG
capture_sequence:
  - flue_or_process_gas pretreatment
  - absorber contact and CO2 removal
  - rich_solvent transfer
  - stripping and solvent regeneration
  - solvent reclaiming and makeup
conditioning:
  - CO2 cooling separation dehydration
  - compression to transport specification
transport_and_storage:
  - pipeline transport
  - injection well
  - reservoir pressure plume and integrity monitoring
MRV:
  - CO2 received produced captured transported injected
  - fugitive vent and other emissions
  - mass balance uncertainty
  - monitoring plan and annual record
critical_variables:
  - inlet and outlet CO2 concentration and flow
  - capture rate
  - solvent lean rich loading temperature degradation and loss
  - steam electricity cooling and water use
  - CO2 purity water and pressure
  - injection rate pressure and well integrity
failure_modes:
  - solvent foaming degradation or corrosion
  - excessive energy penalty
  - off_spec CO2
  - compressor trip or transport interruption
  - injection pressure or injectivity constraint
  - mass_balance or monitoring gap
KPIs:
  - captured_CO2
  - capture_rate
  - net_avoided_CO2
  - energy_per_CO2
  - solvent_makeup_and_emission
  - transport_injection_availability
  - MRV_data_completeness
OI_seeds: [SEED-ENS-D06-066, SEED-ENS-D06-067, SEED-ENS-D06-068]
```

## 14.3 Capture-Plant Integration Points

| Integration | Needed data | Operational conflict | O/I focus |
|---|---|---|---|
| Flue-gas interface | flow, CO₂, O₂, temperature, contaminants | unit load and startup variability | capture load-following control |
| Steam extraction | steam P/T/flow, turbine impact | net power and heat-rate penalty | steam/capture co-optimization |
| Cooling water | flow, temperature, seasonal capacity | condenser and water constraints | integrated cooling allocation |
| Electrical auxiliary | compressor/pump/fan power | export reduction and peak load | auxiliary efficiency |
| Solvent | inventory, loading, degradation, emissions | chemistry and corrosion | solvent health prediction |
| CO₂ compression | purity, dew point, pressure, trip | pipeline specification | conditioning optimizer |
| Transport/storage | nomination, linepack, injection | source-sink availability mismatch | buffer and chain scheduling |

## 14.4 MRV Digital Genealogy

```yaml
MRV_chain:
  source_meter:
    fields: [gas_flow, CO2_concentration, timestamp, quality_flag]
  capture_meter:
    fields: [captured_flow, purity, vent, calibration]
  transport_meter:
    fields: [custody_mass, pressure, composition, loss]
  injection_meter:
    fields: [received_mass, injected_mass, pressure, well]
  monitoring:
    fields: [plume, pressure, leakage_indicator, survey, anomaly]
  accounting:
    fields: [gross_captured, injected, stored, leakage, uncertainty, net_avoided]
hard_rules:
  - no_credit_without_meter_lineage
  - gross_capture_is_not_equal_to_net_avoided
  - model_estimate_and_meter_measurement_must_be_separate
  - calibration_and_missing_data_substitution_must_be_versioned
```

---
