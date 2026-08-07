---
id: skes-d06-5-process-and-equipment-master
title: Process and Equipment Master
summary: SK이노베이션 E&S의 LNG·발전·열병합·도시가스 밸류체인별 운영 프로세스 정의와 상태를 조회하는 마스터 데이터
tags: [d06, process, table]
keywords: [LNG, 발전, 도시가스, 열병합, 운영절차, 밸류체인, 액화천연가스, 터미널운영, 가스공급망, 상태관리]
related: [PROC-ENS-D06-LNG-001, PROC-ENS-D06-LNG-002, PROC-ENS-D06-LNG-003, PROC-ENS-D06-LNG-004, PROC-ENS-D06-LNG-005, PROC-ENS-D06-LNG-006, PROC-ENS-D06-LNG-007, PROC-ENS-D06-LNG-008, PROC-ENS-D06-LNG-009, PROC-ENS-D06-LNG-010, PROC-ENS-D06-LNG-011, PROC-ENS-D06-PWR-001, PROC-ENS-D06-PWR-002, PROC-ENS-D06-PWR-003, PROC-ENS-D06-PWR-004, PROC-ENS-D06-PWR-005, PROC-ENS-D06-PWR-006, PROC-ENS-D06-PWR-007, PROC-ENS-D06-PWR-008, PROC-ENS-D06-CHP-001, PROC-ENS-D06-CHP-002, PROC-ENS-D06-CG-001, PROC-ENS-D06-CG-002, PROC-ENS-D06-CG-003]
priority: normal
domain: D06
section: 5
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 2362
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 5. Process and Equipment Master

## 5.1 Process Master — 45 Records

| Process ID | Chain | Process | Status | Evidence |
|---|---|---|---|---|
| `PROC-ENS-D06-LNG-001` | LNG | Portfolio demand and entitlement planning | OPERATING | E1+E4 |
| `PROC-ENS-D06-LNG-002` | LNG | Upstream production and nomination interface | OPERATING | E1+E3 |
| `PROC-ENS-D06-LNG-003` | LNG | Feed-gas conditioning | INDUSTRY_BASELINE | E3 |
| `PROC-ENS-D06-LNG-004` | LNG | Gas liquefaction entitlement operation | OPERATING_INTERFACE | E1+E3 |
| `PROC-ENS-D06-LNG-005` | LNG | LNG storage and loading at export terminal | OPERATING_INTERFACE | E1+E3 |
| `PROC-ENS-D06-LNG-006` | LNG | Cargo and vessel scheduling | OPERATING | E1+E4 |
| `PROC-ENS-D06-LNG-007` | LNG | LNG carrier voyage and cargo management | OPERATING | E1+E3 |
| `PROC-ENS-D06-LNG-008` | LNG | Berthing and unloading | OPERATING | E1+E3 |
| `PROC-ENS-D06-LNG-009` | LNG | Terminal storage and inventory reconciliation | OPERATING | E1+E3 |
| `PROC-ENS-D06-LNG-010` | LNG | Boil-off gas management | INDUSTRY_BASELINE_FOR_ENS_ASSET | E3+E4 |
| `PROC-ENS-D06-LNG-011` | LNG | Regasification and sendout | OPERATING | E1+E3 |
| `PROC-ENS-D06-PWR-001` | PWR | Day-ahead dispatch and fuel nomination | OPERATING | E1+E4 |
| `PROC-ENS-D06-PWR-002` | PWR | Unit startup and synchronization | OPERATING_BASELINE | E1+E3 |
| `PROC-ENS-D06-PWR-003` | PWR | Gas turbine combustion and generation | OPERATING | E1+E3 |
| `PROC-ENS-D06-PWR-004` | PWR | HRSG steam generation | OPERATING_BASELINE | E1+E3 |
| `PROC-ENS-D06-PWR-005` | PWR | Steam turbine and condenser cycle | OPERATING_BASELINE | E1+E3 |
| `PROC-ENS-D06-PWR-006` | PWR | Load optimization and ancillary response | OPERATING_BASELINE | E1+E4 |
| `PROC-ENS-D06-PWR-007` | PWR | Emissions and water-chemistry control | OPERATING | E1+E3 |
| `PROC-ENS-D06-PWR-008` | PWR | Shutdown outage and condition maintenance | OPERATING_BASELINE | E1+E4 |
| `PROC-ENS-D06-CHP-001` | CHP | Heat-demand forecasting and co-dispatch | OPERATING | E1+E4 |
| `PROC-ENS-D06-CHP-002` | CHP | Heat production transfer and network supply | OPERATING | E1+E3 |
| `PROC-ENS-D06-CG-001` | CG | Wholesale gas receipt and city-gate custody transfer | OPERATING | E1+E3 |
| `PROC-ENS-D06-CG-002` | CG | Odorization and pressure regulation | OPERATING_BASELINE | E1+E3 |
| `PROC-ENS-D06-CG-003` | CG | Distribution pressure and linepack operation | OPERATING | E1+E3 |
| `PROC-ENS-D06-CG-004` | CG | RBMS integrity risk assessment | OPERATING_CONFIRMED | E1 |
| `PROC-ENS-D06-CG-005` | CG | Patrol drone and leak survey | OPERATING_CONFIRMED | E1 |
| `PROC-ENS-D06-CG-006` | CG | Excavation work and third-party damage prevention | OPERATING_BASELINE | E3+E4 |
| `PROC-ENS-D06-CG-007` | CG | Regulator and valve maintenance | OPERATING_BASELINE | E1+E3 |
| `PROC-ENS-D06-CG-008` | CG | Meter reading volume correction and billing | OPERATING | E1+E3 |
| `PROC-ENS-D06-CG-009` | CG | Customer service connection and move event | OPERATING | E1+E4 |
| `PROC-ENS-D06-CG-010` | CG | Leak report and emergency isolation | OPERATING | E1+E3 |
| `PROC-ENS-D06-REN-001` | REN | Weather and generation forecasting | OPERATING_BASELINE | E1+E3 |
| `PROC-ENS-D06-REN-002` | REN | Solar PV conversion and plant control | OPERATING | E1+E3 |
| `PROC-ENS-D06-REN-003` | REN | Wind turbine generation and plant control | OPERATING | E1+E3 |
| `PROC-ENS-D06-REN-004` | REN | Renewable O&M and loss accounting | OPERATING | E1+E3 |
| `PROC-ENS-D06-REN-005` | REN | Meter REC PPA allocation and settlement | OPERATING | E1+E4 |
| `PROC-ENS-D06-ESS-001` | ESS | Market forecasting and bid optimization | OPERATING_AFFILIATE | E1 |
| `PROC-ENS-D06-ESS-002` | ESS | Award-to-dispatch translation | OPERATING_BASELINE | E1+E3 |
| `PROC-ENS-D06-ESS-003` | ESS | Battery operation thermal safety and degradation | OPERATING_AFFILIATE | E1+E3 |
| `PROC-ENS-D06-EVC-001` | EVC | Site capacity and dynamic charging allocation | OPERATING_AFFILIATE | E1 |
| `PROC-ENS-D06-EVC-002` | EVC | Charging session billing and maintenance | OPERATING_AFFILIATE | E1+E4 |
| `PROC-ENS-D06-H2-001` | H2 | Byproduct hydrogen intake and purification | OPERATING_INTERFACE | E1+E3 |
| `PROC-ENS-D06-H2-002` | H2 | Hydrogen liquefaction and cryogenic storage | OPERATING | E1+E3 |
| `PROC-ENS-D06-H2-003` | H2 | Tanker loading delivery and station receiving | OPERATING | E1+E3 |
| `PROC-ENS-D06-CCS-001` | CCS | CO₂ capture conditioning transport injection and MRV | PLANNED_OR_PILOT | E1+E2+E3 |

## 5.2 Equipment-Class Master

| Equipment Class ID | Equipment class | Main chain | Critical measurements | Typical failure concerns |
|---|---|---|---|---|
| `EQC-ENS-D06-001` | well and subsea production system | LNG | pressure, rate, water/gas composition | flow assurance, integrity, availability |
| `EQC-ENS-D06-002` | feed-gas separator and treatment unit | LNG | composition, dew point, contaminant | off-spec feed, freeze, corrosion |
| `EQC-ENS-D06-003` | liquefaction compressor/refrigerant train | LNG | suction/discharge P/T, vibration, power | surge, trip, efficiency loss |
| `EQC-ENS-D06-004` | cryogenic heat exchanger | LNG/H2 | approach temperature, pressure drop | fouling, maldistribution, thermal stress |
| `EQC-ENS-D06-005` | LNG storage tank | LNG | level, pressure, temperature, density | rollover, overpressure, leak |
| `EQC-ENS-D06-006` | marine loading arm and jetty | LNG | flow, ESD status, movement | leak, disconnection, weather delay |
| `EQC-ENS-D06-007` | LNG carrier cargo containment | LNG | tank P/T/level, boil-off, engine fuel | BOR, sloshing, propulsion issue |
| `EQC-ENS-D06-008` | BOG compressor/recondenser | LNG | flow, suction P, vibration, availability | trip, flare/vent, inventory loss |
| `EQC-ENS-D06-009` | regasifier/vaporizer | LNG | inlet/outlet T/P, flow, heat source | icing, fouling, sendout constraint |
| `EQC-ENS-D06-010` | sendout pump and metering | LNG/CG | flow, pressure, composition | cavitation, meter bias, imbalance |
| `EQC-ENS-D06-011` | gas turbine | PWR | exhaust T spread, vibration, fuel flow | combustion dynamics, fouling, trip |
| `EQC-ENS-D06-012` | HRSG | PWR/CHP | steam P/T, drum level, stack T | tube leak, corrosion, thermal fatigue |
| `EQC-ENS-D06-013` | steam turbine generator | PWR/CHP | vibration, bearing T, efficiency | blade/bearing issue, trip |
| `EQC-ENS-D06-014` | condenser and cooling system | PWR/CHP | vacuum, cooling water T/flow, fouling | vacuum loss, biofouling, water use |
| `EQC-ENS-D06-015` | CEMS and water analyzer | PWR | NOx, O2, flow, pH, conductivity | drift, invalid data, compliance gap |
| `EQC-ENS-D06-016` | city gate/regulator station | CG | inlet/outlet P, flow, valve status | regulator hunting, over/underpressure |
| `EQC-ENS-D06-017` | distribution pipe and service line | CG | pressure, leak survey, GIS attributes | corrosion, joint leak, third-party damage |
| `EQC-ENS-D06-018` | odorization system | CG | injection rate, odorant inventory | under/over odorization, pump failure |
| `EQC-ENS-D06-019` | customer gas meter/volume corrector | CG | volume, T/P correction, communication | bias, battery loss, tamper |
| `EQC-ENS-D06-020` | PV module string inverter transformer | REN | irradiance, DC/AC power, temp, alarms | soiling, mismatch, inverter trip |
| `EQC-ENS-D06-021` | wind turbine and substation | REN | wind, power, vibration, oil, alarms | gearbox/bearing/blade/cable fault |
| `EQC-ENS-D06-022` | battery rack PCS HVAC fire system | ESS | V/I/T, SOC/SOH, insulation, gas/smoke | thermal event, imbalance, PCS trip |
| `EQC-ENS-D06-023` | EVSE and site controller | EVC | status, power, connector T, network | offline, overload, payment failure |
| `EQC-ENS-D06-024` | hydrogen purification system | H2 | purity, pressure, contaminant | off-spec, adsorbent saturation |
| `EQC-ENS-D06-025` | hydrogen liquefier | H2 | temperature profile, power, flow | trip, efficiency loss, contamination |
| `EQC-ENS-D06-026` | LH2 storage/loadout/tanker | H2 | P/T/level, BOR, mass transfer | boil-off, leak, transfer loss |
| `EQC-ENS-D06-027` | absorber/stripper/solvent system | CCS | CO2 in/out, solvent loading, T/P/flow | degradation, corrosion, foaming |
| `EQC-ENS-D06-028` | CO2 dehydration/compressor/pipeline | CCS | purity, water, pressure, flow | corrosion, phase issue, leak |
| `EQC-ENS-D06-029` | injection well and monitoring system | CCS | injection P/rate, plume, seismic | injectivity loss, migration, integrity |

---
