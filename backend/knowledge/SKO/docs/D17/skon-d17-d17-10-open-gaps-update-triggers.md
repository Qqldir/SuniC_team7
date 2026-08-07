---
id: skon-d17-d17-10-open-gaps-update-triggers
title: Open Gaps & Update Triggers
summary: "D17 오픈이노베이션 과제 추진 시 해결해야 할 데이터 갭 10개(내부 통계, 현행 시스템, 권리, 마스터 데이터 등)와 각 갭별 필요 자료·영향 과제를 정리한 표, 그리고 정보 업데이트를 촉발하는 8가지 트리거 조건을 제시한다."
tags: [d17, oi-portfolio, schema, table, "xref:d05"]
keywords: [정보갭, 데이터결함, PoC 검증, 공급자통제, FTO, 권리검증, 업데이트기준, 규제준수, 품질인시던트, 계약검토, 정보 갭, GAP 분석, MES/QMS/ERP, PLM, RFI/RFP, 공급자 관리, IP 권리, SBOM, 의사결정 트리거]
related: [GAP-D17-01, GAP-D17-02, GAP-D17-03, GAP-D17-04, GAP-D17-05, GAP-D17-06, GAP-D17-07, GAP-D17-08, GAP-D17-09, GAP-D17-10]
priority: normal
domain: D17
section: D17-10
source: SK온_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation
tokens: 517
updated: 2026-08-03
---

> SK온 · D17 오픈이노베이션 과제 포트폴리오·AI 추천 · SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation

## D17-10 Open Gaps & Update Triggers

| Gap ID | 미확인 항목 | 필요한 자료 | 영향 과제 |
|---|---|---|---|
| `GAP-D17-01` | 내부 Pain Point Baseline·분모 | MES/QMS/ERP/Finance 추출 | 전체 P0 |
| `GAP-D17-02` | 현행 시스템·진행/실패 PoC | Architecture·PoC Archive·Interview | 001~005 |
| `GAP-D17-03` | D05 Decision-Date 권리·FTO 내부 Gate | 최신 공식 권리상태·제품 Element Map·비공개 계약·발명/영업비밀 원장·법률의견 | 030·048·051~055 |
| `GAP-D17-04` | Plant–Line–Product–Customer 승인 Master | PLM·QMS·S&OP·고객승인 | 011~015·021·024·026 |
| `GAP-D17-05` | Material Lot·Origin·Cost·Supplier Control | Supplier Portal·QMS·ERP·계약 | 031~040 |
| `GAP-D17-06` | Provider TCO·Battery Reference·Runway | RFI/RFP·Reference Call·NDA Pack | 002·004·060 및 외부협력 전부 |
| `GAP-D17-07` | Data/IP/Cyber/Export 권리 | 계약·Data Classification·SBOM | 외부 Provider 과제 전부 |
| `GAP-D17-08` | Warranty/OEM/BMS/Insurance 권리 | Data-sharing·보험·계약 | 016~020·025·055 |
| `GAP-D17-09` | 인센티브·대출·JV 원문 의무 | Agreement·Note·Guarantee·Consent | 036·041~050 |
| `GAP-D17-10` | 재활용 Yield·Spec·Permit·물류·원가 | Sample Qualification·TEA·Mass Balance | 035·054 |

```yaml
update_triggers:
  - new_internal_baseline_or_data_access
  - provider_RFI_RFP_reference_or_security_result
  - poc_gate_scale_stop_exit_or_PIR
  - new_customer_program_call_off_or_qualification
  - plant_ramp_conversion_shutdown_or_asset_transfer
  - regulation_delegated_act_tax_notice_tariff_or_enforcement_change
  - partnership_license_JV_investment_termination_or_provider_EoL
  - quality_incident_recall_field_signal_or_supplier_4M_change
```

---
