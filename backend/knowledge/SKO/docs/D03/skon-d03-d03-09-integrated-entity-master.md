---
id: skon-d03-d03-09-integrated-entity-master
title: Integrated Entity Master
summary: SK온의 배터리·에너지저장장치·차세대 제품 등 178개 엔티티를 ID·분류·상태별로 관리하는 마스터 데이터베이스.
tags: [d03, product, core-candidate, schema, table]
keywords: [SK온 배터리, 제품 분류, 고-니켈 포우치, LFP, ESS, GRIDON, 차세대 배터리, 포트폴리오, 엔티티 마스터, 배터리 포트폴리오, 상태 관리, 고니켈 파우치, ASSB]
related: []
priority: critical
domain: D03
section: D03-09.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 2344
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03-09. Integrated Entity Master

## 9.1 Entity Count

```yaml
entity_count_snapshot:

  company: 7
  product_family: 5
  sk_on_product: 18
  sk_on_service: 5
  technology: 26
  chemistry: 5
  form_factor: 3
  architecture: 10
  application: 14
  customer_and_partner: 18
  competitor_product: 15
  pain_point: 31
  oi_seed: 8
  source: 63

  total_registered_entities: 178
```

`total_registered_entities`는 D03 내부에서 생성한 엔티티와 외부 벤치마크·분석 엔티티를 합친 값이며, 원천문서 수와 동일하지 않다.

---

## 9.2 SK온 Product Entity Master

| Entity ID          | Canonical Name                  | Class                | Status                   | Parent             |
| ------------------ | ------------------------------- | -------------------- | ------------------------ | ------------------ |
| PROD-SKON-EV-001   | High-Nickel Pouch Battery       | Product Family       | Commercial               | EV Battery         |
| PROD-SKON-EV-002   | NCM9+ Battery                   | Product Technology   | Commercial               | High-Nickel Pouch  |
| PROD-SKON-EV-003   | SF Battery                      | Named Product        | Commercial               | High-Nickel Pouch  |
| PROD-SKON-EV-004   | Advanced SF Battery             | Named Product        | Application Confirmed    | SF Family          |
| PROD-SKON-EV-005   | SF+ Battery                     | Named Product        | Disclosed Technology     | SF Family          |
| PROD-SKON-EV-006   | Hyper Fast Battery              | Prototype            | Technology Demonstration | Fast-Charge Family |
| PROD-SKON-EV-007   | LFP EV Platform                 | Product Platform     | Pre-commercial           | EV Battery         |
| PROD-SKON-EV-008   | Pouch-Integrated Prismatic      | Prototype            | Exhibition Prototype     | Prismatic Platform |
| PROD-SKON-EV-009   | On-Vent Prismatic Cell          | Prototype            | Exhibition Prototype     | Prismatic Platform |
| PROD-SKON-EV-010   | Prismatic Battery Platform      | Form-Factor Platform | Pre-commercial           | EV Battery         |
| PROD-SKON-EV-011   | Cylindrical Battery Platform    | Form-Factor Platform | Exploratory              | EV Battery         |
| PROD-SKON-ESS-001  | LFP ESS Battery                 | Battery Product      | Contracted               | ESS                |
| PROD-SKON-ESS-002  | GRIDON Gen 1                    | ESS Solution         | Production Planned       | ESS                |
| PROD-SKON-ESS-003  | GRIDON Gen 2                    | ESS Solution         | Under Development        | GRIDON             |
| PROD-SKON-ESS-004  | DC Block                        | ESS Component        | Supported                | GRIDON             |
| PROD-SKON-ESS-005  | AC Block Configuration          | ESS Architecture     | Under Development        | GRIDON Gen 2       |
| PROD-SKON-NEXT-001 | Polymer-Oxide Composite Battery | Next-Gen Product     | Pilot Development        | Solid-State        |
| PROD-SKON-NEXT-002 | Sulfide ASSB                    | Next-Gen Product     | R&D                      | Solid-State        |

---

## 9.3 Service Entity Master

| Entity ID          | Canonical Name             | Status                | Primary Function                     |
| ------------------ | -------------------------- | --------------------- | ------------------------------------ |
| SERV-SKON-BAAS-001 | Battery Diagnosis Service  | Pilot/Partner Service | 상태·이상 진단                             |
| SERV-SKON-BAAS-002 | Battery Monitoring Service | Partner Service       | 주행·충전 데이터 분석                         |
| SERV-SKON-BAAS-003 | Residual Value Assessment  | Partnership           | 잔여수명·잔존가치 평가                         |
| SERV-SKON-BAAS-004 | Reuse Decision Support     | Strategic Capability  | 재사용·재활용 분기                           |
| SERV-SKON-BAAS-005 | 5R Lifecycle Platform      | Strategic Framework   | Rental·Recharge·Repair·Reuse·Recycle |

---

## 9.4 Technology Entity Master

```yaml
technology_entities:

  - technology_id: TECH-SKON-HIGH-NICKEL
    name: High-Nickel Cathode Technology
    category: MATERIAL

  - technology_id: TECH-SKON-DUAL-LAYER-ANODE
    name: Dual-Layer Silicon-Graphite Anode
    category: ELECTRODE

  - technology_id: TECH-SKON-MAGNETIC-ALIGNMENT
    name: Magnetic Alignment Process
    category: MANUFACTURING

  - technology_id: TECH-SKON-SUFAST
    name: SUFast
    category: CELL_AND_CHARGING_CO_DESIGN

  - technology_id: TECH-SKON-CONFIGURABLE-VENT
    name: Configurable On-Vent
    category: CELL_SAFETY

  - technology_id: TECH-SKON-LASER-VENT
    name: Laser Vent Processing
    category: MANUFACTURING

  - technology_id: TECH-SKON-CTP
    name: Pouch-Type Cell-to-Pack
    category: PACK_ARCHITECTURE

  - technology_id: TECH-SKON-EIS-BMS
    name: EIS-Based Battery Management System
    category: DIAGNOSTICS

  - technology_id: TECH-SKON-COOLANT-IMMERSION
    name: Coolant Immersion Technology
    category: THERMAL_MANAGEMENT

  - technology_id: TECH-SKON-COOLANT-FIRE-SUPPRESSION
    name: Coolant-Based Fire Suppression
    category: ESS_SAFETY

  - technology_id: TECH-SKON-BAAS-AI
    name: BaaS AI
    category: BATTERY_ANALYTICS

  - technology_id: TECH-SKON-SULFIDE-ELECTROLYTE
    name: Sulfide Solid Electrolyte
    category: SOLID_STATE

  - technology_id: TECH-SKON-POLYMER-OXIDE
    name: Polymer-Oxide Composite Electrolyte
    category: SOLID_STATE

  - technology_id: TECH-SKON-LITHIUM-METAL
    name: Lithium-Metal Anode
    category: NEXT_GENERATION_ANODE
```

---

## 9.5 Status Vocabulary

```yaml
commercial_status_vocabulary:

  COMMERCIAL:
    definition: 실제 판매 또는 차량 적용이 공식적으로 확인됨

  CONTRACTED:
    definition: 공급계약은 확인됐으나 전체 공급 또는 양산이 완료되지 않음

  PRODUCTION_PLANNED:
    definition: 생산개시 계획이 공식 발표됐으나 생산실적은 아직 확인되지 않음

  APPLICATION_CONFIRMED:
    definition: 특정 차량·장비 적용이 확인됐으나 전체 판매규모는 공개되지 않음

  PRODUCT_TECHNOLOGY_DISCLOSED:
    definition: 명명된 제품 또는 기술이 공개됐으나 고객·양산이 확인되지 않음

  PRE_COMMERCIAL:
    definition: 기술 또는 시제품이 존재하며 상용화 이전 단계

  EXHIBITION_PROTOTYPE:
    definition: 전시 또는 기술시연 목적으로 공개된 시제품

  PILOT_DEVELOPMENT:
    definition: 파일럿 라인 또는 시험생산 단계

  R_AND_D:
    definition: 연구개발 단계

  EXPLORATORY:
    definition: 개발 검토 또는 시장 탐색단계

  CORPORATE_TARGET:
    definition: 회사가 발표한 미래 목표로 실제 성과가 아님

  HISTORICAL:
    definition: 과거에는 확인됐으나 현재 상태가 재확인되지 않음

  UNCONFIRMED:
    definition: 공개근거가 부족함
```

---

## 9.6 Alias Dictionary

```yaml
alias_dictionary:

  NCM9+:
    canonical_entity: PROD-SKON-EV-002
    aliases:
      - NCM 9 Plus
      - NCM9 Plus
      - 90%+ Nickel Battery

  SF_Battery:
    canonical_entity: PROD-SKON-EV-003
    aliases:
      - Super Fast Battery
      - SF 배터리

  Advanced_SF:
    canonical_entity: PROD-SKON-EV-004
    aliases:
      - Advanced Super Fast Battery
      - 어드밴스드 SF 배터리

  Hyper_Fast:
    canonical_entity: PROD-SKON-EV-006
    aliases:
      - Hyper Fast Battery
      - HYPER FAST
      - 7-Minute Battery
      - 7분 급속충전 배터리

  GRIDON:
    canonical_entity: PROD-SKON-ESS-002
    aliases:
      - SK On GRIDON
      - 그리드온
      - GRID ON

  BaaS_AI:
    canonical_entity: TECH-SKON-BAAS-AI
    aliases:
      - Battery as a Service AI
      - 배터리 진단 AI

  Sulfide_ASSB:
    canonical_entity: PROD-SKON-NEXT-002
    aliases:
      - Sulfide All-Solid-State Battery
      - 황화물계 전고체 배터리
      - 황화물 전고체
```

---
