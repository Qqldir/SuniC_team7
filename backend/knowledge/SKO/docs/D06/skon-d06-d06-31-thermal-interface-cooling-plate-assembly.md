---
id: skon-d06-d06-31-thermal-interface-cooling-plate-assembly
title: Thermal Interface·Cooling Plate Assembly
summary: "배터리 팩 냉각판 조립 공정의 단계, 핵심 파라미터, 품질 기준, 결함 모드, 검사 방법을 규정하는 제조 프로세스"
tags: [d06, process, schema, "xref:d04", "xref:d05"]
keywords: [열전도계면, 냉각판, CTP, 배터리셀, 공정파라미터, 품질속성, 검사방법, 냉매, 결함모드, 열응답균일성, 열전도 부재, 냉각판 조립, 열 인터페이스, 냉매채널, 셀 스택, 열접촉 검증, 공정 파라미터, 결함 모드, 냉각 성능]
related: []
priority: normal
domain: D06
section: D06-31.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 993
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-31. Thermal Interface·Cooling Plate Assembly

## 31.1 Thermal Assembly Flow

```text
Cell Stack or Cell Assembly
          ↓
Cooling Plate Surface Preparation
          ↓
Thermal Adhesive / Gap Filler Dispensing
          ↓
Cell or Assembly Placement
          ↓
Compression and Curing
          ↓
Coolant Connector Installation
          ↓
Leak and Flow Test
          ↓
Thermal Contact Verification
```

---

## PROC-SKON-D06-019D — Thermal Interface and Cooling Plate

```yaml
process_id: PROC-SKON-D06-019D
canonical_name: Thermal Interface and Cooling Plate Integration
korean_name: 열전도계면·냉각판 조립
process_layer: MODULE_PACK
ownership_scope: SK_ON_DEVELOPMENT

input_objects:
  - Cell stack or cell assembly
  - Cooling plate
  - Thermal adhesive
  - Gap filler or thermal pad
  - Coolant connector
  - Seal and gasket

output_object:
  - Thermally integrated module or pack subassembly

equipment_classes:
  - Surface-cleaning unit
  - Adhesive or gap-filler dispenser
  - Vision-guided placement robot
  - Compression or curing fixture
  - Leak-test unit
  - Coolant-flow tester
  - Thermal inspection system

critical_process_parameters:
  - Dispense mass
  - Bead position
  - Adhesive temperature
  - Mixing ratio
  - Working time
  - Cell-to-plate gap
  - Compression force
  - Cure time and temperature
  - Coolant-connector torque
  - Leak-test pressure
  - Coolant flow rate

critical_quality_attributes:
  - Thermal-interface coverage
  - Interface thickness
  - Void fraction
  - Adhesive cure
  - Cell-to-plate contact
  - Electrical insulation
  - Coolant leak absence
  - Pressure drop
  - Flow distribution
  - Thermal response uniformity

defect_modes:
  - Under-dispensing
  - Over-dispensing
  - Air void
  - Incomplete cure
  - Cell floating
  - Uneven interface thickness
  - Connector leakage
  - Cooling-channel blockage
  - Flow imbalance
  - Electrical-isolation failure

inspection_methods:
  - Dispense-weight monitoring
  - Bead vision
  - 3D surface inspection
  - Ultrasound or X-ray void inspection candidate
  - Cure-state sensing
  - Pressure-decay leak test
  - Coolant flow and pressure-drop test
  - Thermographic response test

technology_ids:
  - TECH-SKON-D04-016
  - TECH-SKON-D04-027
  - TECH-SKON-D04-028
  - TECH-SKON-D04-062

candidate_patent_family_ids:
  - PF-CAND-SKON-D05-011

source_ids:
  - SRC-SKON-D06-025
  - SRC-PAT-D06-027
  - SRC-PAT-D06-030

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-SKON-D06-025
  - SRC-PAT-D06-027
```

SK온의 공개 CTP 구조에는 셀과 팩 하부 사이의 열전도부재·냉매채널이 포함되며, 별도 출원에서는 냉각패널과 차단패널을 팩 내부에 배치하는 구조가 확인된다. LSC의 최대 3배 성능은 회사 주장으로만 관리한다. ([구글 특허][4])

---

## 31.2 Thermal Interface Record

```yaml
thermal_interface_record:

  assembly_identity:
    - Module or CTP assembly ID
    - Cooling-plate ID
    - Cell-stack ID

  material:
    - Thermal-interface material ID
    - Supplier lot
    - Mixing lot
    - Expiration and open time

  dispensing:
    - Dispenser ID
    - Nozzle ID
    - Recipe version
    - Actual mass
    - Bead coordinates
    - Dispense pressure

  assembly:
    - Placement force
    - Final gap
    - Cure profile
    - Fixture position

  quality:
    - Coverage estimate
    - Void estimate
    - Leak result
    - Flow result
    - Thermal-response result
```

---
