---
id: skon-d06-d06-35-pack-structure-bms-cooling-eol
title: Pack Structure·BMS·Cooling·EoL
summary: "배터리 팩의 구조 조립과 BMS·고전압 부품 통합 공정에서 요구하는 공정 파라미터, 품질 기준, 결함 유형, 검사 방법을 명시한 문서."
tags: [d06, process, schema, "xref:d04"]
keywords: [팩 조립, BMS 마스터, 고전압 통합, 셀 센싱, 컨택터, 토크, 채널 설정, 펌웨어, 절연, 압력 테스트, 배터리 팩 조립, BMS 통합, 고전압 부품, 구조조립, 셀 모니터링, 접점기, 품질 속성, 결함 모드]
related: []
priority: normal
domain: D06
section: D06-35.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1861
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-35. Pack Structure·BMS·Cooling·EoL

## PROC-SKON-D06-021A — Pack Structural Assembly

```yaml
process_id: PROC-SKON-D06-021A
canonical_name: Battery Pack Structural Assembly
korean_name: 배터리 팩 구조조립
process_layer: MODULE_PACK
ownership_scope: SK_ON_CONFIRMED

input_objects:
  - Pack lower housing
  - Modules or CTP cell assemblies
  - Center beams and partitions
  - Thermal barriers
  - High-voltage components
  - Pack upper cover
  - Gaskets and seals
  - Crash and mounting structures

critical_process_parameters:
  - Module or CTP position
  - Fastening torque and angle
  - Structural-adhesive amount
  - Seal or gasket compression
  - Partition position
  - Cover alignment
  - Mounting-interface dimensions

critical_quality_attributes:
  - Pack dimensions
  - Structural fastening
  - Water and dust sealing
  - Electrical clearance
  - Gas-path continuity
  - Crash-structure position
  - Service-disconnect access
  - Pack-floor flatness

defect_modes:
  - Missing fastener
  - Torque deviation
  - Structural-adhesive void
  - Gasket folding
  - Cover deformation
  - Module or CTP misposition
  - Gas-path blockage
  - Housing damage

inspection_methods:
  - Torque trace
  - Vision and presence check
  - 3D metrology
  - Seal inspection
  - Pack pressure-decay test
  - Electrical isolation

technology_ids:
  - TECH-SKON-D04-024
  - TECH-SKON-D04-025
  - TECH-SKON-D04-026
  - TECH-SKON-D04-062

source_ids:
  - SRC-PAT-D06-027
  - SRC-PAT-D06-030

evidence_level: ANALYST_INFERENCE
```

---

## PROC-SKON-D06-021B — BMS·High-Voltage Integration

```yaml
process_id: PROC-SKON-D06-021B
canonical_name: BMS and High-Voltage Component Integration
korean_name: BMS·고전압부품 통합
process_layer: MODULE_PACK
ownership_scope: INDUSTRY_BASELINE

components:
  - BMS master controller
  - Cell-monitoring units
  - Contactors
  - Fuse
  - Current sensor
  - Service disconnect
  - High-voltage busbar and cable
  - Low-voltage communication harness
  - Temperature sensors
  - Wireless BMS components where applicable

assembly_functions:
  - Controller installation
  - Sensing-channel connection
  - High-voltage routing
  - Contactor and fuse connection
  - Communication-network configuration
  - Firmware and calibration loading

critical_quality_attributes:
  - Channel mapping
  - Sensor accuracy
  - Communication integrity
  - Contactor operation
  - Current-sensor direction
  - Fuse and disconnect installation
  - HV insulation
  - Firmware and calibration version

defect_modes:
  - Connector not fully seated
  - Swapped sensing channel
  - Incorrect firmware
  - Contactor wiring error
  - Current-sensor reversal
  - Harness pinching
  - Communication failure
  - Insulation defect

inspection_methods:
  - Network communication test
  - Channel simulation
  - Contactor activation
  - Current-sensor calibration
  - HV isolation
  - Firmware checksum
  - Connector-presence vision

technology_ids:
  - TECH-SKON-D04-029
  - TECH-SKON-D04-030
  - TECH-SKON-D04-046
  - TECH-SKON-D04-062

evidence_level: ANALYST_INFERENCE
source_ids:
  - SRC-PAT-D06-028
```

---

## PROC-SKON-D06-021C — Pack Cooling-Circuit Integration

```yaml
process_id: PROC-SKON-D06-021C
canonical_name: Pack Cooling-Circuit Integration
korean_name: 팩 냉각회로 통합
process_layer: MODULE_PACK
ownership_scope: SK_ON_DEVELOPMENT

components:
  - Cooling plates
  - Coolant manifolds
  - Inlet and outlet connectors
  - Hoses or internal channels
  - Gaskets and seals
  - Temperature and leak sensors

critical_quality_attributes:
  - Leak absence
  - Pressure drop
  - Flow distribution
  - Connector retention
  - Air removal
  - Electrical isolation
  - Thermal-response uniformity

inspection_methods:
  - Pressure-decay test
  - Vacuum filling test
  - Coolant-flow test
  - Pressure-drop test
  - Thermal imaging
  - Connector-force or torque trace

technology_ids:
  - TECH-SKON-D04-016
  - TECH-SKON-D04-027
  - TECH-SKON-D04-028

source_ids:
  - SRC-SKON-D06-025
  - SRC-PAT-D06-030

evidence_level: ANALYST_INFERENCE
```

---

## PROC-SKON-D06-021D — Pack End-of-Line Test

```yaml
process_id: PROC-SKON-D06-021D
canonical_name: Battery Pack End-of-Line Test
korean_name: 배터리 팩 출하검사
process_layer: MODULE_PACK
ownership_scope: INDUSTRY_BASELINE

test_groups:

  identity_and_configuration:
    - Pack serial
    - Product revision
    - Module or cell serial mapping
    - Firmware version
    - Calibration version

  electrical:
    - Pack voltage
    - Module and cell voltage channels
    - Insulation resistance
    - Contactor operation
    - Pre-charge function
    - Current-sensor direction
    - HVIL continuity

  communication:
    - CAN or applicable network
    - Diagnostic communication
    - BMS fault-code test
    - Sensor plausibility

  thermal:
    - Temperature-channel function
    - Coolant flow
    - Pressure drop
    - Thermal response

  sealing:
    - Pack enclosure leakage
    - Coolant leakage
    - Connector sealing

  safety:
    - Service disconnect
    - Fuse configuration
    - Interlock
    - Emergency fault response

  final:
    - Software release
    - Manufacturing genealogy upload
    - Shipping SOC
    - Final disposition

defect_modes:
  - Incorrect electrical topology
  - Isolation failure
  - Communication fault
  - Cooling leak
  - Sensor-channel error
  - Firmware mismatch
  - Contactor fault
  - Pack-enclosure leak
  - Serial genealogy mismatch

technology_ids:
  - TECH-SKON-D04-030
  - TECH-SKON-D04-040
  - TECH-SKON-D04-046
  - TECH-SKON-D04-062
  - TECH-SKON-D04-064

source_ids:
  - SRC-PAT-D06-027
  - SRC-PAT-D06-028
  - SRC-PAT-D06-030

evidence_level: ANALYST_INFERENCE
sk_on_parameter_disclosure: NOT_DISCLOSED
```

---

## 35.1 Pack EoL Record

```yaml
pack_eol_record:

  pack_identity:
    - Pack serial number
    - Product revision
    - Customer configuration
    - Manufacturing plant and line

  genealogy:
    - Cell serial numbers
    - Module serial numbers
    - CTP assembly IDs
    - Busbar and joint records
    - Cooling-plate IDs
    - BMS hardware ID

  software:
    - BMS software version
    - Calibration version
    - Security certificate
    - Flash result

  electrical_results:
    - Pack voltage
    - Channel consistency
    - Isolation
    - Contactor function
    - Current-sensor calibration

  thermal_results:
    - Coolant leak
    - Flow rate
    - Pressure drop
    - Temperature-channel response

  structural_results:
    - Pack leak
    - Fastener completeness
    - Dimensions
    - Weight

  final_decision:
    - Release
    - Repair
    - Retest
    - Engineering review
    - Scrap
```

---
