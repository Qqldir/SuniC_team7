---
id: skes-d05-13-technology-ip-product-crosswalk
title: Technology–IP–Product Crosswalk
summary: LNG·도시가스·수소 등 에너지기술별로 보유한 특허·노하우·파트너십의 권리상태와 사업 활용 현황을 정리한 기술자산 교차표
tags: [d05, rnd, schema, table, "xref:d04", "xref:d03"]
keywords: [LNG, 도시가스, 수소, CCS, 특허, 에너지저장, 권리상태, 노하우, 기술자산]
related: []
priority: normal
domain: D05
section: 13
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 767
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 13. Technology–IP–Product Crosswalk

| D04 Cluster | 핵심 IP·R&D 자산 | D03 연결 | 권리상태 | O/I 활용 |
|---|---|---|---|---|
| LNG 생산·액화 | Santos 공동연구·운영노하우 | LNG 조달·저탄소 LNG | 프로젝트·파트너 | 생산·메탄·CCS 데이터 공동개발 |
| LNG 선박·터미널 | 공개 직접특허 미확인 | 운송·터미널·송출 | 노하우·벤더 | 일정·BOG 최적화 알고리즘 |
| 발전·CHP | Honeywell 실증·OEM 기술 | 전력·열 | 파트너·OEM | 성능+포집 통합 twin |
| 도시가스 정압 | CG-001/005 | 도시가스 공급 | 직접·공동·자회사 | 센서·RBMS·정비추천 고도화 |
| 도시가스 계량 | CG-002/003/004 | 검침·고객서비스 | 직접·공동 | AMI·OCR·열량·과금 lineage |
| 도시가스 배관 | CG-006/008 | 안전관리 | 자회사·공동 | 로봇·영상·응급복구 |
| 재생에너지 | 공개 직접특허 미확인 | 태양광·풍력·PPA | 소프트웨어·계약 | 예측·O&M·정산 공동IP |
| 액화수소 | JV·파트너·운영노하우 | 생산·물류·충전 | 계약 중심 | BOG·물류 twin·안전데이터 |
| PEM 수전해 | Plug/JV 기술 | 그린수소 | JV·라이선스 | 현지화·운전 최적화 |
| ESS | MarketCapture | 시장입찰·계통서비스 | 자회사 proprietary | degradation-aware bidding |
| DERMS·VPP | 공개 IP Gap | 계획 서비스 | 미확인 | 상호운용·정산 IP 선점 |
| EV 충전 | EVC-001~005 | SmartPower·충전기 | 자회사 특허 | BESS·fleet·건물 통합 |
| CCS 포집 | CCS-001/002·Honeywell·CE TECH | 저탄소 LNG·블루수소 | 혼합 | 흡수제 운전·에너지 절감 |
| CCS MRV | 프로젝트 데이터·표준 | CCS 서비스 | 계약·데이터 | lineage·mass balance·assurance |

## 13.1 D04 61개 기술 처리 규칙

```yaml
mapping_rule:
  direct_patent_match:
    - CG_pressure_meter_pipeline
    - CCS_solvent_operation
    - EV_charging_load_and_hardware
  proprietary_software_match:
    - ESS_market_bidding
    - charging_control
  partner_license_match:
    - carbon_capture_core_process
    - PEM_electrolyzer_and_fuel_cell
  knowhow_data_match:
    - LNG_terminal
    - power_operations
    - renewable_PPA
    - hydrogen_logistics
    - CCS_MRV
  gap_for_new_OI_IP:
    - DERMS_VPP
    - cross_value_chain_optimization
    - multi_affiliate_city_gas_AI
    - hydrogen_supply_twin
```

---
