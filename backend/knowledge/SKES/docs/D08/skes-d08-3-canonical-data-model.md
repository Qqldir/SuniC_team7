---
id: skes-d08-3-canonical-data-model
title: Canonical Data Model
summary: "공급망 관리에서 공급자, 계약, 물자, 물량 이동, 성과를 기록하기 위한 표준 데이터 스키마들의 기술 명세"
tags: [d08, supply-chain, table, "xref:d07", "xref:d06"]
keywords: [공급자, 계약, 물자, 물량이동, 성과이벤트, 마스터스키마, 데이터표준, 조달, 공급망, 납품]
related: []
priority: normal
domain: D08
section: 3
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 1085
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 3. Canonical Data Model

## 3.1 Supplier Master Schema

| Field | Type | 설명 |
|---|---|---|
| `supplier_id` | PK | 공급자·파트너 식별자 |
| `legal_name` | text | 계약 법인명 |
| `brand_name` | text | 공개 브랜드명 |
| `supplier_role` | enum | producer, toller, carrier, terminal, OEM, EPC, O&M, software |
| `parent_entity_id` | FK | 모회사 |
| `country_of_incorporation` | code | 법인 국가 |
| `operating_countries` | array | 실제 사업 국가 |
| `relationship_state` | enum | active, historical, planned, under_review |
| `criticality` | enum | P0, P1, P2 |
| `single_source_flag` | boolean/unknown | 단일공급 여부 |
| `data_access_right` | enum | full, limited, aggregated, unknown |
| `source_ids` | array | 공개근거 |

## 3.2 Contract/Right Schema

| Field | Type | 설명 |
|---|---|---|
| `contract_id` | PK | 계약·권리 식별자 |
| `supplier_id` | FK | 상대방 |
| `right_type` | enum | 1.3 vocabulary |
| `commodity_or_service` | FK | 품목·서비스 |
| `asset_ids` | array | D07 자산 |
| `process_ids` | array | D06 공정 |
| `start_date` | date/unknown | 시작 |
| `end_date` | date/unknown | 종료 |
| `volume_or_capacity` | numeric/range | 공개 규모 |
| `unit` | enum | mtpa, MW, MWh, vessel, service |
| `pricing_index` | text/unknown | 공개된 경우에만 |
| `take_or_pay` | boolean/unknown | 미공개는 unknown |
| `destination_flexibility` | enum | disclosed, restricted, unknown |
| `service_level` | text/unknown | 납기·가동률·성능 |
| `data_right` | text/unknown | telemetry·audit 접근권 |
| `claim_status` | enum | 1.2 vocabulary |

## 3.3 Material/Service Master Schema

| Field | Type | 설명 |
|---|---|---|
| `material_id` | PK | 원료·부품·서비스 |
| `category` | enum | commodity, equipment, spare, chemical, logistics, digital |
| `specification_key` | array | 발열량·조성·압력·규격·화학계 등 |
| `quality_certificate` | array | CoA·검사·인증 |
| `hazard_class` | enum | cryogenic, flammable, pressure, electrical, chemical |
| `shelf_life` | duration/NA | 보관기한 |
| `substitution_rule` | text | 대체승인 조건 |
| `critical_spare_flag` | boolean | 장기납기 핵심품목 |
| `traceability_level` | enum | lot, serial, cargo, batch, project |

## 3.4 Supply-Flow Schema

| Field | Type | 설명 |
|---|---|---|
| `flow_id` | PK | 물량 이동 레코드 |
| `origin_node_id` | FK | 공급원 |
| `destination_node_id` | FK | 자산·창고·현장 |
| `contract_id` | FK | 근거 계약 |
| `material_id` | FK | 품목 |
| `planned_quantity` | numeric | 계획 |
| `actual_quantity` | numeric | 실적 |
| `quality_state` | enum | pending, accepted, quarantined, rejected |
| `incoterm_or_handover` | text/unknown | 위험이전 지점 |
| `planned_departure/arrival` | timestamp | 계획 |
| `actual_departure/arrival` | timestamp | 실적 |
| `inventory_impact` | numeric | 재고 증감 |
| `carbon_intensity` | numeric/unknown | 범위·방법론 포함 |
| `exception_code` | FK | 지연·품질·손실 사유 |

## 3.5 Supplier-Performance Event Schema

| Field | Type | 설명 |
|---|---|---|
| `event_id` | PK | 성과·이슈 이벤트 |
| `supplier_id` | FK | 대상 |
| `contract_id` | FK | 계약 |
| `event_type` | enum | delivery, defect, outage, safety, cyber, ESG, financial |
| `severity` | enum | S0~S4 |
| `detected_at` | timestamp | 탐지시각 |
| `affected_assets` | array | 영향자산 |
| `root_cause` | text/unknown | 원인 |
| `containment_action` | text | 즉시조치 |
| `corrective_action` | text | 시정조치 |
| `closure_evidence` | URI/hash | 종결증빙 |

---
