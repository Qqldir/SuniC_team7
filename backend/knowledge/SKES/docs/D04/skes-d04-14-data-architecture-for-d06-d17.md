---
id: skes-d04-14-data-architecture-for-d06-d17
title: Data Architecture for D06~D17
summary: "SK이노베이션 E&S에서 데이터를 8개 계층으로 조직화하고, 이벤트를 표준화하며, AI 모델을 5단계 배포 체계로 관리하는 방법을 정의한 지식 아키텍처 문서."
tags: [d04, technology, schema, table, "xref:d06", "xref:d17", "xref:d00"]
keywords: [데이터 계층, 이벤트 표준화, 모델 배포 단계, DCS/SCADA/AMI/BMS, 자산 관리, 시계열 데이터, OT 운영, 데이터 거버넌스, 보안 분류]
related: []
priority: normal
domain: D04
section: 14
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: Part 2. 대표기업 기술체계 심층 확장
tokens: 633
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · Part 2. 대표기업 기술체계 심층 확장

## 14. Data Architecture for D06~D17

### 14.1 Common Data Layers

| Layer | Data products | 주요 owner | 대표 보안등급 |
|---|---|---|---|
| Asset Identity | asset hierarchy, GIS, serial, owner | 자산·설비 | Internal |
| Time Series | DCS/SCADA/AMI/BMS/charger | OT 운영 | Restricted |
| Event | alarm, trip, incident, near miss | 운영·SHE | Restricted |
| Work | inspection, work order, parts, labor | 정비 | Confidential |
| Commercial | contract, price, bid, settlement | 영업·트레이딩·재무 | Highly confidential |
| Customer | usage, billing, service, consent | 도시가스/PPA/충전 | Personal/confidential |
| External | weather, AIS, market, regulation | 외부 provider | Licensed/public |
| Evidence | source, model version, approval, audit | D00/governance | Internal |

### 14.2 Canonical Event Record

```yaml
event_id: UUID
event_time: source_timestamp
ingest_time: platform_timestamp
entity_id: canonical_asset_customer_contract
event_type: sensor_alarm_work_order_transaction_incident
source_system: system_id
value_payload: typed_fields
quality:
  completeness: 0_to_1
  validity: 0_to_1
  latency_seconds: number
  calibration_or_version: string
context:
  operating_mode: normal_startup_shutdown_maintenance_emergency
  location: controlled_geospatial_id
security:
  classification: public_internal_confidential_restricted
  consent_or_contract_basis: reference
lineage:
  raw_object_id: immutable
  transform_version: code_or_rule
```

### 14.3 Model Deployment Tiers

| Tier | 모델 역할 | 허용 출력 | 예시 | 승인 |
|---|---|---|---|---|
| `T0_OFFLINE` | 과거 데이터 분석 | 리포트 | 수요·고장 baseline | 데이터 owner |
| `T1_MONITOR` | 실시간 탐지 | 경보·설명 | 이상탐지·OCR 검토 | 운영 owner |
| `T2_ADVISORY` | 추천 | 일정·setpoint 후보 | LNG 일정·ESS 입찰 | 현업 승인 |
| `T3_GUARDED_AUTO` | 제한 자동화 | 사전승인 범위 제어 | 충전부하·시장입찰 | 안전·사이버·변경관리 |
| `T4_SAFETY_CONTROL` | 보호계통 | 본 DB 신규 AI 적용 제외 | SIS/ESD | 별도 법정/OEM 절차 |
