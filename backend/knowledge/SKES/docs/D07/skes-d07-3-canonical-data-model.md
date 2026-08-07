---
id: skes-d07-3-canonical-data-model
title: Canonical Data Model
summary: 터미널·발전소·배관 등 에너지 자산을 거점·자산·용량·권리 차원에서 체계적으로 기록하기 위한 마스터 데이터 스키마 정의.
tags: [d07, footprint, table, "xref:d06"]
keywords: [거점, 자산, 용량, 권리, 마스터데이터, 스키마, 지분, 운영사, 라이프사이클, 에너지자산]
related: []
priority: normal
domain: D07
section: 3
source: SK이노베이션E&S_D07_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 646
updated: 2026-08-06
---

> SK이노베이션 E&S · D07 터미널·발전소·배관 등 자산·용량

# 3. Canonical Data Model

## 3.1 Site Master Schema

| Field | Type | 설명 |
|---|---|---|
| site_id | PK | 물리 거점 ID |
| site_name | text | 공개 명칭 |
| country | code | 국가 |
| region | text | 주·도·도시 |
| geo_precision | enum | exact_city, region_only, distributed |
| site_type | enum | field, plant, terminal, network, office, distributed |
| operator_entity_id | FK | 운영 주체 |
| ownership_state | enum | owned, JV, affiliate, contract_right, O&M, exited |
| lifecycle_state | enum | operating, commissioning, construction, development, planned, retired |
| effective_date | date | 상태 기준일 |
| source_id | FK | 근거 |

## 3.2 Asset Master Schema

| Field | Type | 설명 |
|---|---|---|
| asset_id | PK | 자산 ID |
| site_id | FK | 거점 |
| parent_asset_id | FK | 플랜트·포트폴리오 상위 ID |
| asset_class | enum | field, train, vessel, tank, CCGT, CHP, network, wind, solar, BESS, EVSE |
| asset_name | text | 공개 명칭 |
| unit_count | numeric | 설비 수 |
| equipment_configuration | text | 공개된 설비구성 |
| process_ids | array | D06 연결 |
| data_availability | enum | public_high, public_partial, internal_required |
| source_id | FK | 근거 |

## 3.3 Capacity Record Schema

| Field | Type | 설명 |
|---|---|---|
| capacity_id | PK | 능력 레코드 |
| asset_id | FK | 대상 자산 |
| capacity_type | enum | 1.2 vocabulary |
| measure | numeric/range | 공개값 |
| unit | text | MW, MWh, t/y, m3/y, Gcal/h |
| gross_or_net | enum | gross, equity, contract, unknown |
| status_scope | enum | operating, developing, mixed |
| period | date/year | 기준시점 |
| inclusion_parent | FK | 포트폴리오 포함관계 |
| source_id | FK | 근거 |

## 3.4 Rights and Ownership Schema

| Field | Type | 설명 |
|---|---|---|
| right_id | PK | 권리 ID |
| asset_id | FK | 대상 |
| right_type | enum | equity, operator, TUA, tolling, import, O&M, PPA, development |
| holder_entity_id | FK | 권리자 |
| share_or_volume | value | 지분 또는 계약량 |
| start_date | date | 시작 |
| end_date | date | 종료 |
| current_state | enum | active, sold, expired, planned |
| source_id | FK | 근거 |

---
