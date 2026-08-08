---
id: skes-d17-d17-17-open-gaps-update-triggers
title: Open Gaps & Update Triggers
summary: D17 오픈이노베이션 과제에서 수집해야 할 미확인 정보 15개 항목과 프로젝트 갱신을 유발하는 이벤트 조건들을 정리한 위험 관리 문서.
tags: [d17, oi-portfolio, schema, table]
keywords: [정보갭, 미확인항목, 위험레지스터, 트리거조건, KPI baseline, LNG 계약권, 자산데이터권리, 규제준수, 포트폴리오]
related: [GAP-D17-01, GAP-D17-02, GAP-D17-03, GAP-D17-04, GAP-D17-05, GAP-D17-06, GAP-D17-07, GAP-D17-08, GAP-D17-09, GAP-D17-10, GAP-D17-11, GAP-D17-12, GAP-D17-13, GAP-D17-14, GAP-D17-15]
priority: normal
domain: D17
section: D17-17
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 718
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-17 Open Gaps & Update Triggers

## 1. Open Gap Register

| Gap ID | 미확인 항목 | 필요한 내부자료 | 영향 과제 |
|---|---|---|---|
| `GAP-D17-01` | 실제 Pain Baseline/분모 | KPI·loss·event baseline | 전체 P0 |
| `GAP-D17-02` | 현행 O/I·AI·Digital 과제 중복 | portfolio archive·architecture | 001~005·전체 |
| `GAP-D17-03` | LNG contract option/right exact scope | LTA/TUA/entitlement | 006~010 |
| `GAP-D17-04` | Terminal/Power canonical asset-tag mapping | historian/EAM map | 006·008·011·012 |
| `GAP-D17-05` | 도시가스 자회사간 RBMS/data model 차이 | GIS·risk model·inspection | 016~019 |
| `GAP-D17-06` | Offshore OEM/cable data right | warranty·SCADA/CMS terms | 021·022 |
| `GAP-D17-07` | KCE MarketCapture/BMS/warranty 권리 | software/IP/OEM agreements | 026~030 |
| `GAP-D17-08` | EverCharge site/port/session economics | session·utility·host contracts | 031~035 |
| `GAP-D17-09` | LH2 actual utilization·meter uncertainty·paid kg | plant/logistics/sales/finance | 036~040 |
| `GAP-D17-10` | CCS firm emitter/storage/permit/MMV | counterparty·subsurface·regulatory | 041~045 |
| `GAP-D17-11` | K-ETS/48E/PFE actual entity/project inputs | compliance/tax/procurement | 046~050 |
| `GAP-D17-12` | JV/PF/guarantee/Quynh Lap confidential obligations | agreements·schedule·finance | 051~055 |
| `GAP-D17-13` | OT authoritative inventory/zone/remote access | CISO/OT inventory | 056~060 |
| `GAP-D17-14` | Provider TCO/SLA/reference health | RFI/RFP/reference calls | 외부 Provider 과제 전부 |
| `GAP-D17-15` | Data/IP/training/export/deletion rights | contract + data classification | 외부 AI 과제 전부 |

## 2. Update Triggers

```yaml
update_triggers:
  - new_internal_baseline_or_loss_event
  - new_cargo_LNG_contract_right_terminal_outage_or_supply_shock
  - power_trip_major_outage_LTSA_or_heat_rate_baseline_change
  - city_gas_incident_RBMS_model_or_regulatory_change
  - offshore_wind_COD_cable_failure_or_OEM_data_right_change
  - KCE_new_market_project_rule_tax_or_optimizer_version
  - EverCharge_site_contract_power_limit_or_incentive_change
  - LH2_utilization_incident_meter_recalibration_or_offtake_change
  - CCS_emitter_FID_permit_injectivity_MMV_or_liability_change
  - ETS_IRS_PFE_48E_Safeguard_hydrogen_rule_effective_date_change
  - Quynh_Lap_permit_PPA_EPC_JV_schedule_change
  - OT_advisory_incident_remote_access_or_backup_restore_result
  - provider_RFI_RFP_reference_security_TCO_or_EoL_result
  - poc_gate_scale_stop_exit_or_PIR
```

---
