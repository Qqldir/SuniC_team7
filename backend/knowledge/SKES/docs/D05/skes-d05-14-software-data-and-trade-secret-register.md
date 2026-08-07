---
id: skes-d05-14-software-data-and-trade-secret-register
title: "Software, Data and Trade-Secret Register"
summary: "SK이노베이션 E&S의 소프트웨어·데이터·AI모델 자산을 소유권, 보호형태, 권리제약별로 정의하는 자산마스터 및 오픈소스 소프트웨어 도입 기준"
tags: [d05, rnd, schema, table]
keywords: [자산마스터, 영업비밀, 저작권, 데이터권리, 지식재산, SBOM, 오픈소스라이선스, 개인정보, AI모델, 수출통제]
related: [IP-ENS-SW-001, IP-ENS-SW-002, IP-ENS-SW-003, IP-ENS-DATA-001, IP-ENS-DATA-002, IP-ENS-DATA-003, IP-ENS-DATA-004, IP-ENS-DATA-005, IP-ENS-DATA-006, IP-ENS-DATA-007, IP-ENS-DATA-008, IP-ENS-MODEL-001, IP-ENS-MODEL-002, IP-ENS-MODEL-003]
priority: normal
domain: D05
section: 14
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 816
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 14. Software, Data and Trade-Secret Register

## 14.1 Initial Asset Master

| Asset ID | 자산 | 추정 보호형태 | Owner | 공개수준 | 핵심 권리질문 |
|---|---|---|---|---|---|
| `IP-ENS-SW-001` | KCE MarketCapture | 저작권·영업비밀·상표 가능 | KCE | 기능 공개 | 지역·계열사 재사용 |
| `IP-ENS-SW-002` | KCE WattBot | 저작권·영업비밀 | KCE | 명칭 제한공개 | 기능·owner·API |
| `IP-ENS-SW-003` | EverCharge SmartPower software | 특허+저작권+영업비밀 | EverCharge | 기능 공개 | 특허–코드–펌웨어 경계 |
| `IP-ENS-DATA-001` | ESS bidding data | 계약·영업비밀 | KCE/market vendor | 비공개 | 재학습·보존·파생데이터 |
| `IP-ENS-DATA-002` | Charger telemetry | 계약·DB·개인정보 | EverCharge/customer | 비공개 | 고객·차량·site 권리 |
| `IP-ENS-DATA-003` | City-gas AMI and customer usage | 개인정보·계약·영업비밀 | 각 도시가스사 | 비공개 | 목적·동의·계열사 공유 |
| `IP-ENS-DATA-004` | LNG commercial/operational data | 계약·영업비밀 | 프로젝트·E&S | 비공개 | JV·선박·터미널 권리 |
| `IP-ENS-DATA-005` | Power plant OT and maintenance | 영업비밀·OEM 계약 | 발전법인·E&S | 비공개 | OEM cloud·모델 재사용 |
| `IP-ENS-DATA-006` | PPA customer load/settlement | 계약·영업비밀 | E&S/customer | 비공개 | 목적 외 사용·모델 학습 |
| `IP-ENS-DATA-007` | Hydrogen plant/logistics data | 영업비밀·안전정보 | 사업법인·partners | 비공개 | JV·OEM·운송사 공유 |
| `IP-ENS-DATA-008` | CCS subsurface/MRV data | 프로젝트 계약·규제자료 | consortium | 비공개/규제공개 | 장기책임·검증자 접근 |
| `IP-ENS-MODEL-001` | LNG schedule optimizer candidate | 신규 공동IP | 미정 | 미개발 | solver·constraint·data rights |
| `IP-ENS-MODEL-002` | City-gas risk model candidate | 신규 공동IP | 미정 | 미개발 | 설명가능성·사고책임 |
| `IP-ENS-MODEL-003` | H2 supply twin candidate | 신규 공동IP | 미정 | 미개발 | 물류사·충전소 데이터 |

## 14.2 Open-source and Third-party Software Gate

```yaml
software_gate:
  required:
    - SBOM
    - open_source_license_scan
    - model_and_dataset_license
    - cloud_API_terms
    - export_control_and_sanctions
    - vulnerability_and_patch_SLA
    - escrow_or_exit_plan_for_critical_OT
  prohibited:
    - copy_partner_code_without_license
    - train_on_customer_or_market_data_without_right
    - deploy_AGPL_or_restrictive_component_without_review
    - place_safety_critical_control_in_unapproved_cloud_service
```

---
