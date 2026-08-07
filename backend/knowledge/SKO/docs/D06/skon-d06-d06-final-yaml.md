---
id: skon-d06-d06-final-yaml
title: D06 Final YAML
summary: 배터리 제조 전체 프로세스(재료부터 팩까지)의 구조와 각 단계별 프로세스 마스터를 정의하는 SK온의 도메인 문서이다.
tags: [d06, process, schema, "xref:d07"]
keywords: [전극 제조, Z-Folding, 셀투팩(CTP), 드라이 전극, 캘린더링, 디지털 트윈, OEE, 공정 표준화, 배터리 제조, 셀 조립, 전극, 팩, CTP, 모듈, 품질검사, 프로세스]
related: []
priority: normal
domain: D06
section: ""
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 2012
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06 Final YAML

```yaml
domain:
  domain_id: D06
  canonical_name: Manufacturing Process and Operations
  company_id: CO-SKON
  company_name: SK On
  version: 1.6
  reference_date: 2026-08-02
  status: CONDITIONALLY_COMPLETE

scope:
  included:
    - Raw material receiving and storage
    - Weighing and dispensing
    - Wet and dry electrode mixing
    - Coating and drying
    - Solvent recovery
    - Calendering
    - Slitting and notching
    - Final electrode drying
    - Dry-room operations
    - Z-Folding
    - Tab joining
    - Pouch forming
    - Electrolyte filling and wetting
    - Temporary sealing
    - Formation
    - Degassing and final sealing
    - Aging and retention
    - Grading and sorting
    - Cell multimodal inspection
    - Module assembly
    - Cell-to-pack assembly
    - Pouch-integrated prismatic assembly
    - Pack BMS and cooling integration
    - Pack end-of-line
    - Smart factory
    - Manufacturing digital twin
    - Predictive maintenance
    - OEE and downtime
    - Yield, scrap and rework
    - Energy
    - OT cybersecurity
    - Operations control tower
    - Ramp-up
    - Cross-plant transfer
    - Manufacturing OI opportunities

  excluded_or_deferred:
    - Plant-specific production capacity
    - Actual equipment layout
    - Confidential recipe
    - Actual yield and OEE
    - Actual energy consumption
    - Manufacturing cost
    - Plant environmental permits
    - Field failure and warranty data

registry:
  sources: 37

  processes:
    total_including_parent_aggregates: 42

    layers:
      - MATERIAL
      - ELECTRODE
      - CELL_ASSEMBLY
      - CELL_FINISHING
      - MODULE_PACK
      - DIGITAL_QUALITY

  defects:
    total: 20

  pain_points:
    total: 22

  oi_seeds:
    total: 49

  chunks:
    total: 25

  graph_queries:
    total: 20

  relationship_triples:
    total: 40

sk_on_confirmed_manufacturing_technologies:
  - Z-Folding
  - Dry Electrode Development
  - AI Calendering Development
  - Cell-to-Pack Development
  - Large-Surface Cooling
  - Pouch-Integrated Prismatic Prototype
  - Siemens Digital-Twin Cooperation

manufacturing_process_master:

  material:
    - Raw Material Receiving
    - Controlled Storage
    - Weighing and Dispensing

  electrode:
    - Wet Mixing
    - Dry Mixing
    - Wet Coating
    - Drying and Solvent Recovery
    - Calendering
    - Slitting and Notching
    - Final Vacuum Drying

  cell_assembly:
    - Z-Folding
    - Tab Joining
    - Pouch Forming
    - Electrolyte Filling
    - Temporary Sealing

  cell_finishing:
    - Formation
    - Degassing
    - Final Sealing
    - Aging
    - Grading
    - Electrical Inspection
    - Seal Inspection
    - X-Ray Inspection

  module_pack:
    - Cell Matching
    - Cell Stacking and Compression
    - Busbar Joining
    - Thermal Interface
    - Module Housing and Sensing
    - Direct CTP Installation
    - Pouch-Integrated Prismatic
    - Pack BMS and HV Integration
    - Cooling Circuit
    - Pack EoL

  digital_operations:
    - Manufacturing Digital Twin
    - Intelligent Equipment
    - Manufacturing Digital Thread

manufacturing_data_model:
  principal_objects:
    - Material Lot
    - Mixing Batch
    - Slurry Tank
    - Electrode Roll
    - Electrode Plate
    - Cell Stack
    - Cell Serial
    - Module Serial
    - Pack Serial
    - Equipment
    - Recipe
    - Process Event
    - Inspection Result
    - Defect
    - Disposition
    - Maintenance Event
    - Energy Record

  minimum_genealogy:
    - Material-to-Batch
    - Batch-to-Roll
    - Roll-to-Electrode
    - Electrode-to-Cell
    - Cell-to-Module
    - Cell-or-Module-to-Pack

smart_factory:
  architecture_reference:
    - ISA-95
    - ISO 22400
    - ISO 23247
    - NIST SP 800-82

  confirmed:
    - Siemens DISW cooperation
    - Digital-twin and simulation objective

  not_confirmed:
    - Global full deployment
    - Connected twin maturity
    - Autonomous control
    - Quantified performance improvement

operations_management:
  kpis:
    - OEE
    - First-Pass Yield
    - Rolled Throughput Yield
    - Scrap
    - Rework
    - Value-Added Scrap
    - WIP
    - Cycle Time
    - Energy per Accepted Cell
    - Schedule Adherence

  actual_sk_on_values:
    status: NOT_DISCLOSED

priority_oi_portfolio:

  foundation:
    - Material-to-Cell Digital Thread
    - Manufacturing Data Backbone
    - Roll-to-Cell Coordinate Genealogy
    - Manufacturing AI Governance

  process_optimization:
    - AI Calendering Closed Loop
    - Adaptive Formation
    - Accelerated Aging
    - Busbar Weld Closed Loop
    - Thermal Interface Intelligence
    - Formation–Aging Bottleneck Optimizer

  scale_and_ramp:
    - Virtual Commissioning
    - Ramp-Up Knowledge Graph
    - Cross-Plant Recipe Transfer
    - Golden Batch Library
    - Measurement-System Equivalence

  product_differentiation:
    - Compression Digital Twin
    - Reworkable CTP
    - Pouch-Integrated Prismatic Pilot Platform
    - Pack EoL Digital Passport

data_quality:

  overall:
    value: HIGH_FOR_PROCESS_INTELLIGENCE
    legal_or_operational_certification: NOT_SUITABLE

  strong:
    - End-to-end process coverage
    - Process–defect taxonomy
    - Manufacturing genealogy design
    - Smart-factory target architecture
    - OI opportunity generation

  weak:
    - Actual SK On process parameters
    - Plant-specific process routes
    - Actual yield and OEE
    - Production deployment evidence
    - Actual energy and cost
    - Field-quality linkage

  critical_open_items:
    - Plant-level routing
    - Actual operating KPI
    - Patent-to-production mapping
    - Digital-twin maturity
    - Material and equipment genealogy
    - Field feedback linkage

completion:
  domain_boundary: COMPLETE
  research_pack: COMPLETE_V5
  electrode_manufacturing: COMPLETE_V1
  cell_assembly: COMPLETE_V1
  cell_finishing: COMPLETE_V1
  module_pack_ctp: COMPLETE_V1
  smart_factory: COMPLETE_V1
  operations_control: COMPLETE_V1
  ramp_up_and_transfer: COMPLETE_V1
  chunk_library: COMPLETE_V1
  graph_queries: COMPLETE_V1
  relationship_graph: COMPLETE_V1
  final_quality_audit: COMPLETE
  human_readable_report: COMPLETE
  final_yaml: COMPLETE

next_domain:
  domain_id: D07
  canonical_name: Manufacturing Footprint, Plants and Capacity
```

---

# D06 완료 상태

**완료:** `SK온 D06 Manufacturing Process & Operations v1.6`

## 최종 산출물

* Canonical Source: **37건**
* Manufacturing Process Entity: **42개**
* Defect Entity: **20개**
* Pain Point: **22개**
* Manufacturing OI Seed: **49개**
* Manufacturing Chunk: **25개**
* Graph Query Template: **20개**
* Core Relationship Triple: **40개**

## 다음 시작점

`SK온 D07 Manufacturing Footprint, Plants & Capacity`

```text
D07-00 Domain Boundary
→ D07-01 Global Plant Master
→ D07-02 Plant Ownership·JV Structure
→ D07-03 Site·Line·Product Mapping
→ D07-04 Nominal Capacity
→ D07-05 Operating·Construction·Planned Status
→ D07-06 Capacity Timeline
→ D07-07 Customer-Linked Capacity
→ D07-08 Plant Ramp-Up·Utilization Evidence
→ D07-09 Equipment·Layout Inference Boundary
→ D07-10 Footprint Risk and Redundancy
→ D07-11 Capacity Pain Points
→ D07-12 Manufacturing Footprint OI Seeds
```
