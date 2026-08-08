---
id: skes-d06-8-natural-gas-power-and-chp-operations
title: Natural-Gas Power and CHP Operations
summary: "천연가스 발전소의 일일 급전 계획과 터빈 시동, 연소, 증기 생성 등 운영 전 프로세스를 설명한다."
tags: [d06, process, schema]
keywords: [천연가스 발전소, 열병합발전, CHP, Day-ahead dispatch, 급전, 연료 공급, 가스 터빈, HRSG, 터빈 시동]
related: [PROC-ENS-D06-PWR-001, PROC-ENS-D06-PWR-002, PROC-ENS-D06-PWR-003, PROC-ENS-D06-PWR-004, PROC-ENS-D06-PWR-005, PROC-ENS-D06-PWR-006, PROC-ENS-D06-PWR-007, PROC-ENS-D06-PWR-008]
priority: normal
domain: D06
section: 8
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 2138
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 8. Natural-Gas Power and CHP Operations

## 8.1 `PROC-ENS-D06-PWR-001` — Day-Ahead Dispatch and Fuel Nomination

```yaml
inputs:
  - market price and dispatch outlook
  - unit availability ramp and minimum_load
  - startup cost time and operating constraints
  - fuel price inventory nomination and pressure
  - heat demand for CHP
  - emission and water constraints
outputs:
  - unit commitment and generation schedule
  - gas nomination and terminal sendout request
  - reserve and flexibility offer
  - startup shutdown plan
failure_modes:
  - price or demand forecast error
  - gas power schedule mismatch
  - unavailable unit not reflected
  - startup duration uncertainty
  - heat obligation conflict
KPIs:
  - schedule_adherence
  - fuel_nomination_imbalance
  - start_success_rate
  - margin_after_variable_cost
  - dispatch_opportunity_loss
OI_seeds: [SEED-ENS-D06-016, SEED-ENS-D06-017]
```

## 8.2 `PROC-ENS-D06-PWR-002` — Unit Startup and Synchronization

```yaml
modes: [cold_start, warm_start, hot_start, restart_after_trip]
generic_sequence:
  - pre_start inspection and permissive check
  - auxiliary systems startup
  - purge and ignition
  - gas turbine acceleration
  - generator synchronization
  - HRSG warming and steam management
  - steam turbine roll and synchronization
  - combined_cycle loading
critical_data:
  - start classification and ambient condition
  - permissive state and alarm sequence
  - ignition attempts and flame status
  - rotor speed vibration and bearing temperature
  - thermal gradients and expansion
  - fuel use emissions and time by phase
failure_modes:
  - failed ignition
  - vibration or thermal stress alarm
  - steam chemistry not ready
  - valve or actuator response delay
  - grid synchronization failure
KPIs:
  - start_time_by_mode
  - start_reliability
  - startup_fuel_MMBtu_or_energy
  - startup_emissions
  - thermal_life_consumption_proxy
OI_seeds: [SEED-ENS-D06-018]
```

## 8.3 `PROC-ENS-D06-PWR-003` — Gas Turbine Combustion and Generation

```yaml
inputs: [natural_gas, combustion_air, dispatch_setpoint]
outputs: [electricity, hot_exhaust_gas, NOx_CO, operating_data]
control_variables:
  - load and ramp
  - fuel flow and fuel_quality
  - inlet_guide_vane or equivalent air control
  - combustion mode and temperature references
state_variables:
  - compressor pressure ratio
  - exhaust temperature average and spread
  - combustion dynamics
  - vibration bearing temperature
  - ambient temperature humidity pressure
failure_modes:
  - compressor fouling
  - combustor instability
  - hot section degradation
  - sensor bias
  - fuel quality variation
  - forced trip
KPIs:
  - corrected_output
  - heat_rate
  - availability_and_forced_outage
  - NOx_CO_by_load
  - degradation_from_clean_baseline
OI_seeds: [SEED-ENS-D06-019, SEED-ENS-D06-020]
```

## 8.4 `PROC-ENS-D06-PWR-004` — HRSG Steam Generation

```yaml
inputs: [gas_turbine_exhaust, feedwater, supplementary_fuel_if_any]
outputs: [HP_IP_LP_steam, stack_gas, blowdown]
critical_variables:
  - drum level and pressure
  - steam and metal temperature
  - feedwater flow and chemistry
  - stack temperature and pressure drop
  - tube leak indicators
failure_modes:
  - drum level excursion
  - thermal fatigue during cycling
  - tube leak
  - corrosion or deposition
  - attemperator malfunction
KPIs:
  - steam_generation_per_GT_exhaust
  - stack_loss_proxy
  - tube_leak_events
  - chemistry_excursion_hours
  - startup_thermal_stress_index
OI_seeds: [SEED-ENS-D06-021]
```

## 8.5 `PROC-ENS-D06-PWR-005` — Steam Turbine and Condenser Cycle

```yaml
inputs: [steam, cooling_water_or_air, vacuum_system]
outputs: [electricity, condensate, rejected_heat]
critical_variables:
  - inlet steam P/T/flow
  - turbine vibration and differential expansion
  - condenser vacuum
  - cooling water inlet outlet temperature
  - condensate conductivity and dissolved_oxygen
failure_modes:
  - condenser fouling or air ingress
  - turbine blade or bearing degradation
  - vacuum loss
  - cooling resource constraint
  - chemistry contamination
KPIs:
  - steam_cycle_efficiency
  - condenser_backpressure
  - cooling_system_auxiliary_power
  - water_consumption
  - availability
OI_seeds: [SEED-ENS-D06-022]
```

## 8.6 `PROC-ENS-D06-PWR-006` — Load Optimization and Ancillary Response

```yaml
decision_variables:
  - GT and ST load split
  - ramp trajectory
  - reserve headroom
  - auxiliary equipment staging
  - efficiency_vs_flexibility tradeoff
constraints:
  - dispatch instruction
  - minimum load and ramp
  - emissions envelope
  - equipment life and starts
  - gas pressure and fuel availability
  - HRSG and steam turbine thermal limits
KPIs:
  - dispatch_tracking_error
  - incremental_heat_rate
  - response_time
  - equivalent_start_or_life_consumption
  - reserve_availability
OI_seeds: [SEED-ENS-D06-023]
```

## 8.7 `PROC-ENS-D06-PWR-007` — Emissions and Water-Chemistry Control

```yaml
public_confirmation:
  - real_time air pollutant concentration tracking at power plants
  - integrated environmental permits for seven sites including Gwangyang
  - cooling water reuse review
air_data:
  - fuel flow and composition
  - stack flow O2 NOx CO and other permit parameters
  - CEMS calibration and quality flag
  - operating mode startup shutdown normal
water_data:
  - intake source and volume
  - cooling water cycles and treatment
  - boiler feedwater condensate chemistry
  - wastewater flow and quality
failure_modes:
  - CEMS analyzer drift or invalid interval
  - combustion emission excursion
  - chemistry excursion and corrosion risk
  - water constraint
  - permit limit proximity not visible to operator
OI_seeds: [SEED-ENS-D06-024, SEED-ENS-D06-025]
```

## 8.8 `PROC-ENS-D06-PWR-008` — Shutdown·Outage·Condition Maintenance

```yaml
maintenance_layers:
  - online condition monitoring
  - operator rounds and first_line maintenance
  - preventive maintenance by calendar or operating_hour
  - condition_based work order
  - planned inspection and overhaul
  - forced outage recovery
work_order_minimum_fields:
  - asset and functional_location
  - symptom alarm and operating_context
  - failure_mode and cause code
  - parts labor vendor and downtime
  - as_found as_left measurements
  - return_to_service and recurrence check
critical_integration:
  - DCS historian
  - vibration and condition system
  - EAM_CMMS
  - outage planning
  - OEM service bulletin and parts life
KPIs:
  - forced_outage_rate
  - mean_time_between_failure
  - mean_time_to_repair
  - planned_vs_unplanned_work
  - recurrence_rate
  - maintenance_schedule_compliance
OI_seeds: [SEED-ENS-D06-026, SEED-ENS-D06-027]
```

## 8.9 `PROC-ENS-D06-CHP-001/002` — CHP Heat Co-Dispatch and Supply

```yaml
public_confirmation:
  Hanam: electricity_and_heat_supply_since_2015
  Wirye: electricity_and_heat_supply_since_2017
operator: Narae_Energy_Service_affiliate
inputs:
  - hourly heat demand forecast
  - electricity dispatch and price
  - ambient temperature calendar occupancy
  - plant and heat network availability
  - storage or auxiliary boiler state if applicable
decisions:
  - cogeneration load
  - auxiliary heat source use
  - supply temperature and flow
  - network pressure and pump staging
outputs:
  - electricity
  - delivered heat
  - network loss and customer service state
critical_data:
  - supply return temperature and flow
  - customer heat meter
  - pressure differential
  - makeup water
  - forecast error
failure_modes:
  - heat demand forecast error
  - heat network leak or low differential pressure
  - electric dispatch conflict
  - return temperature degradation
  - peak heat shortage
OI_seeds: [SEED-ENS-D06-028, SEED-ENS-D06-029]
```

---
