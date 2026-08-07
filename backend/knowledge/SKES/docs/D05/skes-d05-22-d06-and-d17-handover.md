---
id: skes-d05-22-d06-and-d17-handover
title: D06 and D17 Handover
summary: "D05에서 D06·D17로의 이관 요건을 정의하고, LNG·전력·도시가스·수소·ESS·CCS 등 기술 영역별 검증 프로세스와 D05 완료 현황을 기술한 이관 가이드"
tags: [d05, rnd, schema, "xref:d06", "xref:d17"]
keywords: [이관, LNG, 전력, 도시가스, 수소, ESS, CCS, IP 권리, 특허, 검증 프로세스]
related: []
priority: normal
domain: D05
section: 22
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 540
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 22. D06 and D17 Handover

## 22.1 D06 인계

```yaml
handover_id: HANDOVER-ENS-D05-D06-001
required_process_validation:
  LNG:
    - actual_control_and_data_architecture
    - BOG_and_inventory_workflow
  power:
    - OEM_boundary
    - performance_and_maintenance_process
    - capture_integration_point
  city_gas:
    - regulator_meter_pipeline_workflow
    - existing_patent_implementation
  hydrogen:
    - liquefaction_storage_delivery_and_station_process
    - JV_and_OEM_control_boundary
  ESS_EV:
    - MarketCapture_and_SmartPower_operating_flow
    - battery_warranty_and_charger_control
  CCS:
    - absorber_stripper_solvent_storage_and_MRV
```

## 22.2 D17 인계

```yaml
handover_id: HANDOVER-ENS-D05-D17-001
P0_seeds:
  - SEED-ENS-D05-001
  - SEED-ENS-D05-002
  - SEED-ENS-D05-003
  - SEED-ENS-D05-004
  - SEED-ENS-D05-005
  - SEED-ENS-D05-006
  - SEED-ENS-D05-007
  - SEED-ENS-D05-009
  - SEED-ENS-D05-011
  - SEED-ENS-D05-012
  - SEED-ENS-D05-013
  - SEED-ENS-D05-014
  - SEED-ENS-D05-016
  - SEED-ENS-D05-017
  - SEED-ENS-D05-020
  - SEED-ENS-D05-021
mandatory_rights_gate:
  - ownership_class
  - data_right
  - background_and_foreground_IP
  - affiliate_internal_license
  - official_legal_status_refresh
  - safety_and_cyber_boundary
```

---

# 23. D05 Completion Record

```yaml
domain: D05_RnD_Patents_and_Intellectual_Property
version: 1.0
depth_policy: representative_company_deep_database
source_records: 28
organization_nodes: 10
R&D_program_domains: 10
detailed_program_records: 15
patent_taxonomy_domains: 12
initial_patent_families: 15
inventor_records: 12
software_data_trade_secret_assets: 13
IP_risks: 15
white_spaces: 14
OI_seeds: 24
AI_chunks: 10
quality_status: COMPLETE_PUBLIC_DATA_TARGETED_LANDSCAPE
limitations:
  - not_complete_global_patent_portfolio
  - not_legal_FTO_opinion
  - internal_contract_and_implementation_validation_required
next_domain: D06_Manufacturing_Process_and_Operations
```
