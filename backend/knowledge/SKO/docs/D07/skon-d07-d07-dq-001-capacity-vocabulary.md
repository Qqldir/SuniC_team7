---
id: skon-d07-d07-dq-001-capacity-vocabulary
title: 001. Capacity Vocabulary
summary: "배터리 생산능력의 6가지 유형(설계용량, 정규화용량, 합작용량 등)과 공장의 10가지 상태(운영, 건설, 램프업 등)를 정의한 SK온 캐파시티 데이터 기준 문서"
tags: [d07, footprint, schema]
keywords: [캐파, 생산능력, 설계능력, 정규화능력, 공장상태, OPERATIONAL, RAMPING, 가동률, 배터리, 생산량, 캐파시티, 생산용량, 설계용량, 정규화용량, 운영상태, 램프업, 합작공장, UTILIZATION]
related: []
priority: normal
domain: D07
section: D07-DQ
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 849
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-DQ-001. Capacity Vocabulary

## 1. Capacity 유형

```yaml
capacity_types:

  GROSS_DESIGN_CAPACITY:
    definition: >
      공장 설계 또는 투자계획에서 제시된 최대 연간 생산능력
    warning:
      - 실제 가동 가능한 생산능력과 다를 수 있음
      - 건설·Ramp-Up·고객승인 전 Capacity가 포함될 수 있음

  REPORTED_NORMALIZED_CAPACITY:
    definition: >
      공시 기준일 현재 설비상태와 가동가능일수 등을 반영해
      회사가 연간 기준으로 환산한 최대 생산능력
    preferred_for:
      - 연결 생산능력 Snapshot
      - 연도별 공시 비교

  JV_GROSS_CAPACITY:
    definition: >
      합작공장 전체의 설계 또는 가동능력
    warning:
      - SK온 지분율만큼의 연결 Capacity를 뜻하지 않음
      - 연결 또는 지분법 회계처리와 별도 관리

  CURRENT_PRODUCTION_OUTPUT:
    definition: >
      특정 기간 실제 생산한 Cell·GWh·수량
    warning:
      - 연간 Capacity와 다른 개념

  UTILIZATION:
    definition: >
      회사가 정의한 생산가능시간 또는 생산능력 대비 실제 가동수준
    warning:
      - 산식과 포함법인이 같을 때만 비교 가능

  CORPORATE_TARGET:
    definition: >
      향후 확보하겠다고 발표한 목표 생산능력
    claim_status: CORPORATE_TARGET
    prohibited_use:
      - 현재 보유 Capacity로 합산 금지
```

## 2. 공장 상태 Vocabulary

```yaml
plant_status:

  OPERATIONAL:
    definition: 상업생산 중

  PARTIAL_OPERATION:
    definition: 전체 설계능력 중 일부 라인만 가동

  RAMPING:
    definition: 생산량·수율·고객승인을 높이는 단계

  COMMERCIAL_PRODUCTION_STARTED:
    definition: 상업생산 개시가 공식 확인됐으나 정상 Capacity 도달 여부는 미확인

  COMPLETED_PRE_SOP:
    definition: 건물·설비는 완성됐으나 상업생산 전

  PREPARING_FOR_MASS_PRODUCTION:
    definition: 운영체계·인력·설비를 준비 중

  UNDER_CONSTRUCTION:
    definition: 건설·설비투자 진행 중

  RECONFIGURING:
    definition: 제품·고객·화학계 또는 라인용도 전환 중

  DISPOSAL_PENDING:
    definition: 지분 또는 자산 매각계약이 체결됐지만 종결 전

  TRANSFERRED:
    definition: 소유권이 다른 기업으로 이전돼 SK온 Footprint에서 제외

  DEFERRED:
    definition: 생산개시 또는 투자가 연기됨

  STATUS_UNRESOLVED:
    definition: 최신 공개자료만으로 상태를 판단할 수 없음
```

---
