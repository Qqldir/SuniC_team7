---
id: skon-d06-d06-03-raw-material-receiving-storage-dispensin
title: Raw Material Receiving·Storage·Dispensing
summary: "배터리 제조에서 원재료의 입고부터 저장, 계량 투입까지의 핵심 프로세스와 품질 관리 방법을 설명한다."
tags: [d06, process, schema]
keywords: [입고검사, 저장환경, 환경제어, 계량투입, 습도관리, 배치추적, FIFO, 공정계보, 교차오염, 원재료 입고검사, 저장 환경관리, 계량·투입, 로트추적, Receiving Inspection, 공정 계보, 품질속성]
related: []
priority: normal
domain: D06
section: D06-03.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 901
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-03. Raw Material Receiving·Storage·Dispensing

## 03.1 Process Chain

```text
Supplier Material Lot
        ↓
Receiving Inspection
        ↓
Identity·Specification Verification
        ↓
Moisture·Contamination Check
        ↓
Quarantine / Release Decision
        ↓
Controlled Storage
        ↓
Weighing·Dispensing
        ↓
Mixing Batch Assignment
```

---

## PROC-SKON-D06-001 — Raw Material Receiving

```yaml
process_id: PROC-SKON-D06-001
canonical_name: Raw Material Receiving and Incoming Inspection
korean_name: 원재료 입고 및 수입검사
process_layer: MATERIAL
ownership_scope: INDUSTRY_BASELINE

input_material_classes:
  - Cathode active material
  - Anode active material
  - Conductive additive
  - Binder
  - Solvent
  - Electrolyte
  - Separator
  - Aluminum foil
  - Copper foil
  - Pouch film

critical_quality_attributes:
  powder:
    - Chemical composition
    - Particle-size distribution
    - Moisture
    - Residual impurity
    - Tap density

  foil:
    - Thickness
    - Surface contamination
    - Roughness
    - Edge damage
    - Tensile properties

  liquid:
    - Purity
    - Moisture
    - Viscosity
    - Contaminant concentration

decision_status:
  - ACCEPT
  - CONDITIONAL_RELEASE
  - QUARANTINE
  - REJECT

sk_on_parameter_disclosure: NOT_DISCLOSED

source_ids:
  - SRC-BASE-D06-006
  - SRC-BASE-D06-007
```

---

## PROC-SKON-D06-002 — Controlled Material Storage

```yaml
process_id: PROC-SKON-D06-002
canonical_name: Controlled Material Storage
korean_name: 원재료 저장 및 환경관리
process_layer: MATERIAL
ownership_scope: INDUSTRY_BASELINE

environmental_controls:
  - Temperature
  - Relative humidity
  - Dew point where required
  - Inert atmosphere where required
  - Contamination control

critical_risks:
  - Moisture absorption
  - Powder agglomeration
  - Electrolyte contamination
  - Binder aging
  - Lot mixing
  - FIFO violation

required_data:
  - Supplier lot
  - Internal lot
  - Container ID
  - Storage location
  - Open time
  - Expiration date
  - Environmental exposure history

sk_on_parameter_disclosure: NOT_DISCLOSED
```

---

## PROC-SKON-D06-003 — Weighing & Dispensing

```yaml
process_id: PROC-SKON-D06-003
canonical_name: Weighing and Dispensing
korean_name: 계량 및 원료 투입
process_layer: MATERIAL
ownership_scope: INDUSTRY_BASELINE

critical_process_parameters:
  - Material mass
  - Addition sequence
  - Dispensing accuracy
  - Powder transfer time
  - Container cleanliness
  - Environmental exposure

defect_modes:
  - Wrong material
  - Incorrect ratio
  - Cross-contamination
  - Duplicate addition
  - Missing addition
  - Lot-traceability loss

recommended_controls:
  - Barcode or RFID validation
  - Electronic batch record
  - Interlocked scale
  - Material-container identity check
  - Recipe-version lock
```

### D06 분석

입고·저장·계량 단계의 불량은 후속 공정에서 수정하기 어렵고, 동일 원료 Lot가 여러 전극 Batch와 셀 Lot에 확산될 수 있다. 따라서 D06에서는 원재료를 단순 재고가 아니라 **공정 Genealogy의 시작 노드**로 저장한다.

---
