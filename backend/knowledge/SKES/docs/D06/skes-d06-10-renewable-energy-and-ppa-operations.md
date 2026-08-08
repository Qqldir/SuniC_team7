---
id: skes-d06-10-renewable-energy-and-ppa-operations
title: Renewable Energy and PPA Operations
summary: "태양광과 풍력 발전소의 발전량 예측, 제어 시스템, 손실 분석, 운영 유지보수 프로세스를 다루는 재생에너지 운영 가이드."
tags: [d06, process, schema]
keywords: [발전량 예측, 태양광 발전소, 풍력 발전소, SCADA, O&M, 손실회계, 커튼먼트, 가용성, 기상 예측, 인버터]
related: [PROC-ENS-D06-REN-001, PROC-ENS-D06-REN-002, PROC-ENS-D06-REN-003, PROC-ENS-D06-REN-004, PROC-ENS-D06-REN-005]
priority: normal
domain: D06
section: 10
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1136
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 10. Renewable Energy and PPA Operations

## 10.1 `PROC-ENS-D06-REN-001` — Weather and Generation Forecasting

```yaml
assets: [solar, onshore_wind, offshore_wind]
horizons: [month_ahead, day_ahead, intraday, very_short_term]
inputs:
  - numerical_weather_prediction
  - local met mast lidar irradiance and weather station
  - plant availability and planned outage
  - historical SCADA and curtailment
  - soiling snow wake and temperature factors
outputs:
  - P50_or_operational forecast
  - uncertainty interval
  - schedule and update
  - error attribution
failure_modes:
  - weather regime shift
  - unavailable asset treated as weather loss
  - curtailment contaminates training labels
  - missing or biased local sensor
  - portfolio correlation underestimated
KPIs:
  - MAE_RMSE_or_market_metric_by_horizon
  - bias
  - interval_coverage
  - error_cost
  - update_value
OI_seeds: [SEED-ENS-D06-044, SEED-ENS-D06-045]
```

## 10.2 `PROC-ENS-D06-REN-002` — Solar PV Plant Control

```yaml
flow: irradiance_to_DC_to_inverter_AC_to_transformer_to_grid_meter
critical_data:
  - irradiance module and ambient temperature
  - string current voltage and insulation
  - inverter power efficiency status and alarms
  - transformer and switchgear condition
  - meter and curtailment command
loss_tree:
  - resource_variance
  - temperature_loss
  - soiling_or_shading
  - mismatch_and_DC_fault
  - inverter_and_transformer_loss
  - availability_loss
  - curtailment
failure_modes:
  - string open circuit or ground fault
  - inverter derating or trip
  - sensor drift
  - vegetation soiling and shading
  - communication outage
OI_seeds: [SEED-ENS-D06-046]
```

## 10.3 `PROC-ENS-D06-REN-003` — Wind Plant Control

```yaml
flow: wind_to_rotor_to_drive_train_to_generator_converter_transformer_grid
critical_data:
  - wind speed direction turbulence and wake context
  - rotor speed pitch yaw power and curtailment
  - gearbox bearing generator vibration and temperature
  - oil condition
  - blade and tower inspection
  - offshore substation and export cable state
loss_tree:
  - resource_and_wake
  - aerodynamic_performance
  - electrical_loss
  - availability
  - environmental_or_grid_curtailment
failure_modes:
  - pitch_yaw fault
  - bearing_or_gearbox degradation
  - blade damage
  - converter_or_transformer fault
  - subsea cable or access constraint
OI_seeds: [SEED-ENS-D06-047, SEED-ENS-D06-048]
```

## 10.4 `PROC-ENS-D06-REN-004` — O&M and Loss Accounting

```yaml
workflow:
  - alarm and performance anomaly detection
  - remote diagnosis
  - work priority by energy_at_risk safety and access
  - crew part vessel or crane scheduling
  - repair and return_to_service
  - lost_energy and root_cause allocation
data_join:
  - SCADA alarms
  - weather and access window
  - EAM work order
  - spare part and warranty
  - meter and expected_generation model
KPIs:
  - technical_availability
  - energy_based_availability
  - mean_time_to_detect_and_repair
  - repeat_failure
  - lost_energy_by_cause
  - planned_vs_corrective_work
OI_seeds: [SEED-ENS-D06-049]
```

## 10.5 `PROC-ENS-D06-REN-005` — Meter·REC·Direct-PPA Allocation and Settlement

```yaml
public_confirmation: E&S signed Korea first direct renewable PPA with Amorepacific in 2022 and additional corporate PPAs
inputs:
  - settlement_meter_interval
  - generator and customer contract
  - PPA price shape and allocation rule
  - loss factor imbalance and fee
  - REC issuance ownership and retirement
  - curtailment force_majeure and outage clauses
outputs:
  - allocated renewable MWh
  - invoice and settlement statement
  - REC transfer_or_retirement record
  - exception dispute and adjustment
failure_modes:
  - meter and contract time granularity mismatch
  - missing interval data
  - duplicate allocation or REC claim
  - curtailment responsibility ambiguity
  - contract version not reflected in calculation
KPIs:
  - settlement_cycle_time
  - exception_rate
  - allocated_vs_generated_energy
  - customer_RE100_coverage
  - dispute_and_adjustment_value
OI_seeds: [SEED-ENS-D06-050, SEED-ENS-D06-051]
```

---
