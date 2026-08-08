---
id: skon-d06-d06-11-dry-room-material-transfer
title: Dry-Room & Material Transfer
summary: "배터리 셀 조립 드라이룸의 환경 제어 기준, 재료 이송 절차, 그리고 환경 편차·Lot 혼입·오염 입자 등 6가지 주요 운영 문제점을 정리한 표를 제시한다."
tags: [d06, process, schema, table]
keywords: [드라이룸, 이슬점, 습도 제어, 전극, 분리막, 재료 이동, 로트 관리, 환경편차, 상대습도, 환경 편차, Airlock, Lot 혼입, 오염 입자, 셀 조립, 수분 노출, 추적성]
related: []
priority: normal
domain: D06
section: D06-11.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 958
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-11. Dry-Room & Material Transfer

## 11.1 Dry-Room Boundary

```text
Final Electrode Vacuum Drying
          ↓
Dry-Room Entry Verification
          ↓
Electrode Lot Transfer
          ↓
Separator·Pouch Material Supply
          ↓
Z-Folding and Stack Assembly
          ↓
Tab Joining
          ↓
Pouch Insertion
          ↓
Electrolyte Filling
```

드라이룸은 전극·분리막·전해액과 셀 부품이 과도한 수분에 노출되는 것을 방지하기 위한 제조환경이다. 공개 연구에서는 낮은 이슬점 환경에서 셀 조립을 수행하지만, SK온 공장의 실제 이슬점·상대습도·노출 허용시간은 공개되지 않았다. ([OSTI][6])

---

## ENV-SKON-D06-001 — Dry-Room Environmental Control

```yaml
environment_id: ENV-SKON-D06-001
canonical_name: Battery Cell Assembly Dry Room
korean_name: 배터리 셀 조립 드라이룸

ownership_scope: INDUSTRY_BASELINE
evidence_level: THIRD_PARTY_VERIFIED

supported_process_ids:
  - PROC-SKON-D06-010
  - PROC-SKON-D06-011
  - PROC-SKON-D06-012
  - PROC-SKON-D06-013
  - PROC-SKON-D06-014

controlled_variables:
  - Dew point
  - Relative humidity
  - Temperature
  - Airflow
  - Differential pressure
  - Particle concentration
  - Door-open time
  - Material exposure time

operational_risks:
  - Moisture excursion
  - Excessive material exposure
  - Particle contamination
  - Lot-mixing during transfer
  - Airlock failure
  - Uncontrolled personnel movement

required_data:
  - Room-zone ID
  - Environmental time series
  - Material entry timestamp
  - Material exit timestamp
  - Container-open timestamp
  - Alarm and deviation record
  - Recovery and release decision

sk_on_parameter_disclosure: NOT_DISCLOSED

source_ids:
  - SRC-BASE-D06-012
```

---

## 11.2 Dry-Room Exposure Record

```yaml
dry_room_exposure_record:

  object_identity:
    - Electrode-lot ID
    - Separator-lot ID
    - Pouch-material lot
    - Cell-stack ID

  movement:
    - Origin zone
    - Destination zone
    - Entry timestamp
    - Exit timestamp
    - Transfer-container ID

  environmental_exposure:
    - Maximum dew point
    - Average dew point
    - Humidity excursion duration
    - Temperature
    - Exposure time outside sealed container

  deviation:
    - Alarm ID
    - Affected object IDs
    - Quarantine decision
    - Retest requirement
    - Release approval

  downstream_link:
    - Cell serial number
    - Formation batch
    - Gas-generation result
```

---

## 11.3 Dry-Room Pain Points

| Pain Point | 가능한 원인            | 잠재 영향         |
| ---------- | ----------------- | ------------- |
| 환경 편차      | 출입문·Airlock·공조 이상 | 전극·전해액 수분노출   |
| 장시간 노출     | 물류대기·라인 정지        | 공정 편차 증가      |
| Lot 혼입     | 수동 운반·라벨 오류       | 추적성 상실        |
| 오염 입자      | 작업자·설비마모·포장재      | 내부결함·단락위험     |
| 과도한 공조에너지  | 낮은 이슬점 유지·외기유입    | 제조 에너지 증가     |
| 국부 환경 미검출  | Room 평균센서 의존      | 특정 설비구역 편차 누락 |

---
