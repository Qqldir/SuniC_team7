---
id: skon-d04-d04-060-d04-060-nondestructive-cell-inspection-o-1
title: D04-060 — Nondestructive Cell Inspection — OI Metadata
summary: "배터리 셀 비파괴 검사 기술의 성능 요구사항(POC KPI), 레이저 가공 플랫폼의 On-Vent 벤트 형성 기술 상태, 모듈·팩·CTP 조립기술의 개발 단계와 핵심 공정을 정의하는 기술 마스터 문서"
tags: [d04, technology, schema, table, "xref:d06", "xref:d07", "xref:d15"]
keywords: [비파괴 검사, 셀 검사, X-Ray, 레이저 가공, On-Vent, 탭 용접, CTP, 모듈 조립, 불량 검출, 제조 기술, X선 이미징, 결함 검출율, 위음성율, On-Vent 벤트, 모듈 팩 조립, 셀 정렬, 버스바 용접]
related: []
priority: normal
domain: D04
section: D04-060
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Manufacturing Technology Master > D04-060 — Nondestructive Cell Inspection
tokens: 3625
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Manufacturing Technology Master > D04-060 — Nondestructive Cell Inspection

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  external_capability_needs:
    - High-speed X-Ray inspection
    - Sparse-view CT reconstruction
    - Ultrasound cell imaging
    - Multimodal defect fusion
    - Synthetic defect-data generation
    - Explainable anomaly detection
    - Inline inspection digital twin

  poc_kpis:
    - Defect detection rate
    - False reject rate
    - Inspection time per cell
    - Minimum detectable defect
    - Cost per inspected cell
    - Field defect escape rate
```

---

## TECH-SKON-D04-061 — Laser Processing Platform

```yaml
technology_id: TECH-SKON-D04-061
canonical_name: Battery Laser Processing Platform
korean_name: 배터리 레이저 가공 플랫폼

technology_category:
  - Precision Manufacturing
  - Cutting
  - Welding
  - Structural Safety

technology_status:
  on_vent: PROTOTYPE_VALIDATION_CONFIRMED
  other_laser_operations: PRODUCT_SPECIFIC_DETAILS_NOT_DISCLOSED

confirmed_sk_on_application:
  - On-Vent laser engraving

potential_battery_applications:
  - Electrode notching
  - Tab welding
  - Busbar welding
  - Can and cap welding
  - Pack joining
  - Surface cleaning
  - Traceability marking

on_vent_control_parameters:
  - Laser power
  - Scan speed
  - Pulse condition
  - Notch depth
  - Notch geometry
  - Heat-affected region
  - Position accuracy

on_vent_quality_attributes:
  - Rupture-pressure distribution
  - Mechanical strength
  - Repeatability
  - No unintended can damage
  - Directional gas release

source_ids:
  - SRC-SKON-D04-037

confidence:
  on_vent_application: VERY_HIGH
  broader_sk_on_platform: PARTIALLY_INFERRED
```

SK온이 명확히 공개한 독자 레이저 기술은 On-Vent 가공이다. 레이저 노치 깊이를 조정해 파열압력을 제어하고, 캔 상·측·하부 등 원하는 위치에 벤트를 형성할 수 있다. 전극 노칭·탭·버스바 용접 등 다른 레이저 응용은 산업적으로 일반적이지만 SK온의 구체적 적용범위는 별도 근거가 필요하다. ([ASK Inno][8])

---

## TECH-SKON-D04-062 — Module, Pack & CTP Assembly

```yaml
technology_id: TECH-SKON-D04-062
canonical_name: Module, Pack and Cell-to-Pack Assembly
korean_name: 모듈·팩·CTP 조립기술

technology_category:
  - System Integration
  - Mechanical Assembly
  - Electrical Assembly
  - Thermal Integration

technology_status:
  conventional_module_pack: COMMERCIAL_PLATFORM
  pouch_ctp: DEVELOPMENT
  s_pack_plus: EXHIBITION_PROTOTYPE

principal_operations:
  - Cell inspection and matching
  - Cell positioning
  - Compression and fixation
  - Busbar connection
  - Voltage and temperature sensing
  - BMS integration
  - Cooling-plate installation
  - Thermal-interface application
  - Housing assembly
  - Pack sealing
  - Electrical and leak testing

ctp_specific_requirements:
  - Higher cell-placement precision
  - Pack-level structural load support
  - Swelling accommodation
  - Thermal propagation barrier
  - Rework strategy
  - Large-area cooling integration

critical_quality_attributes:
  - Cell alignment
  - Electrical connection resistance
  - Compression uniformity
  - Cooling contact
  - Insulation resistance
  - Water and gas sealing
  - Structural strength

source_ids:
  - SRC-SKON-D04-006
  - SRC-SKON-D04-022
  - SRC-SKON-D04-023
  - SRC-SKON-D04-039

confidence:
  general_assembly: VERY_HIGH
  sk_on_ctp_process_detail: NOT_DISCLOSED
```

모듈·팩 조립에서는 셀을 전기적으로 연결하고 BMS·냉각·하우징을 통합한다. CTP에서는 기존 모듈이 담당하던 고정·절연·열차단 기능을 팩 조립단계가 직접 수행해야 하므로 셀 배치정밀도, 접착·압축, 냉각판 접촉과 재작업 가능성이 더욱 중요해진다. ([energy.gov][5])

---

## TECH-SKON-D04-063 — Intelligent Equipment & OT Infrastructure

```yaml
technology_id: TECH-SKON-D04-063
canonical_name: Intelligent Equipment and OT Infrastructure
korean_name: 지능형 생산설비·OT 인프라

technology_category:
  - Smart Factory
  - Industrial Automation
  - Industrial Network
  - Equipment Intelligence

technology_status: MULTILATERAL_VALIDATION

core_components:
  - PLC and equipment controller
  - Servo and motion controller
  - Robot
  - Smart sensor
  - Industrial network
  - Edge computing
  - Power monitoring
  - Remote maintenance interface

operational_functions:
  - Equipment-state collection
  - Error detection
  - Motion optimization
  - Cycle-time monitoring
  - Predictive maintenance
  - Remote troubleshooting
  - Network security
  - Production-data redundancy

principal_interoperability_needs:
  - Common equipment tag
  - Time synchronization
  - Standard communication protocol
  - Equipment-data ontology
  - Vendor-independent historian
  - Secure remote access
  - Legacy-equipment connector

source_ids:
  - SRC-SKON-D04-038

confidence:
  partnership_and_validation: VERY_HIGH
  plantwide_deployment: NOT_CONFIRMED
```

SK온은 Beckhoff·Cisco·IFM·Yaskawa·Woowon Technology와 제어기·센서·네트워크·로봇·배터리 조립설비의 지능화를 검증하기로 했다. 이 구조는 개별 장비 최적화보다 설비 상태와 품질데이터를 공통 OT 인프라에 연결하는 것이 핵심이다. ([ASK Inno][4])

---

## TECH-SKON-D04-064 — Manufacturing Digital Thread

```yaml
technology_id: TECH-SKON-D04-064
canonical_name: Battery Manufacturing Digital Thread
korean_name: 배터리 제조 디지털 스레드

technology_category:
  - Data Architecture
  - Traceability
  - Process-to-Quality Intelligence

technology_status: ANALYTICAL_INTEGRATION_LAYER
official_named_sk_on_platform: NOT_CONFIRMED

data_chain:
  - Raw-material lot
  - Mixing batch
  - Coated electrode roll
  - Slit and notched electrode
  - Cell stack
  - Electrolyte filling
  - Formation record
  - Cell grade
  - Module and pack assembly
  - Field operation and warranty

required_identifiers:
  - Material lot ID
  - Electrode roll ID
  - Cell serial number
  - Module ID
  - Pack ID
  - Equipment ID
  - Process recipe version
  - Inspection result ID

potential_functions:
  - Defect root-cause tracing
  - Recall-scope minimization
  - Material-process correlation
  - Warranty analysis
  - Process-to-field learning
  - Battery-passport data supply

confirmed_building_blocks:
  - Intelligent equipment
  - Manufacturing digital twin partnership
  - BaaS AI
  - Battery passport concept

information_type: ANALYSIS

source_ids:
  - SRC-SKON-D04-038
  - SRC-SKON-D04-031
  - SRC-SKON-D04-034

confidence:
  strategic_need: VERY_HIGH
  complete_sk_on_implementation: UNCONFIRMED
```

공식 자료에서는 설비 지능화, 제조 디지털 트윈 협력과 BaaS 데이터 기술이 각각 확인되지만, 원재료부터 필드운영까지 연결된 `Manufacturing Digital Thread`라는 단일 SK온 플랫폼은 확인되지 않는다. 이 엔티티는 D06·D07·D15·D17을 연결하기 위한 분석 아키텍처다. ([ASK Inno][4])

---

# D04-26. Process–Technology Relationship Graph

```text
Material Lot
  ↓
Wet Mixing / Dry Powder Mixing
  ↓
Wet Coating / Dry Coating / Dual-Layer Coating
  ↓
Drying and Solvent Recovery [Wet Only]
  ↓
Calendering
  ↓
Slitting and Notching
  ↓
Electrode Edge Inspection
  ↓
Z-Folding / Stacking / Jelly-Roll Assembly
  ↓
Tab and Current-Collector Joining
  ↓
Pouch Forming or Can Insertion
  ↓
Electrolyte Filling and Wetting
  ↓
Initial Sealing
  ↓
Formation
  ↓
Degassing and Final Sealing
  ↓
Aging
  ↓
Cell Inspection, Grading and Sorting
  ↓
Module / Pack / CTP Assembly
  ↓
Cooling, BMS and Safety Integration
  ↓
Final Electrical, Leakage and Functional Testing
```

이 흐름은 DOE가 제시한 셀 제조·팩 통합의 공통 단계와 SK온이 공개한 습식·건식전극, Z-Folding, On-Vent 및 CTP 기술을 통합한 D04 기준모델이다. SK온 실제 공장의 장비배치와 세부 공정순서는 D06에서 공장·제품별로 재검증한다. ([energy.gov][5])

---

# D04-27. Critical Parameter–Quality Map

| 공정        | 핵심 관리변수      | 핵심 품질속성   | 대표 결함       |
| --------- | ------------ | --------- | ----------- |
| 혼합        | 속도·시간·점도·고형분 | 분산·균일성    | 응집·침전·기포    |
| 습식 코팅     | 유량·웹속도·갭     | 로딩·두께·표면  | 스트릭·핀홀·엣지비드 |
| 건식 코팅     | 분말공급·압착      | 밀도·접착·두께  | 분리·균열·불균일   |
| 건조        | 온도·풍량·체류시간   | 잔류용매·접착   | 바인더 이동·균열   |
| 캘린더링      | 압력·갭·온도·속도   | 밀도·기공률    | 크랙·과압착      |
| 슬리팅·노칭    | 절단위치·공구상태    | 치수·버·분진   | 금속버·엣지 파손   |
| Z-Folding | 장력·피치·배치     | 정렬·분리막 피복 | 주름·전극 노출    |
| 탭 접합      | 에너지·압력·위치    | 강도·저항     | 미용접·스패터     |
| 전해액 주입    | 양·진공·시간      | 함침·잔류가스   | 건조영역·누액     |
| 포메이션      | 전류·전압·온도     | 초기효율·저항   | 가스·이상발열     |
| 에이징       | 시간·온도·측정주기   | 자가방전·안정성  | 잠재불량 미검출    |
| 셀 검사      | 해상도·검출모델     | 결함 검출률    | 오탐·미검       |
| 팩 조립      | 위치·압축·접합     | 절연·냉각·강성  | 접촉저항·누설     |

표에 제시한 변수·결함은 산업 공통 제조모델이며, SK온의 내부 허용범위나 실제 불량원인 통계를 의미하지 않는다. 전극 제조와 포메이션·셀 조립이 원가와 품질에 큰 영향을 준다는 점은 DOE와 Argonne 공개자료에서도 공통적으로 확인된다. ([energy.gov][6])

---

# D04-28. Manufacturing Technology Maturity Map

| Technology  | SK온 공개 상태  | D04 성숙도                  | 비공개 핵심정보    |
| ----------- | ---------- | ------------------------ | ----------- |
| 습식 혼합·코팅    | 공정개념 공개    | COMMERCIAL_BASELINE      | 배합·라인속도·수율  |
| 건식 분말 혼합    | 개발 공개      | DEVELOPMENT              | 바인더·장비·균일도  |
| 건식 코팅       | 복수 방식 개발   | DEVELOPMENT              | 파일럿 수율·양산규모 |
| 건조·용매회수     | 기존공정 설명    | COMMERCIAL_BASELINE      | 에너지·회수율     |
| 캘린더링        | 기존·건식 핵심공정 | COMMERCIAL / DEVELOPMENT | 허용범위·수율     |
| AI 캘린더링     | 적용기술 공개    | DEVELOPMENT_APPLICATION  | 양산라인·개선폭    |
| 슬리팅·노칭      | 산업 필수공정    | BASELINE                 | SK온 방식·불량률  |
| Z-Folding   | 고유기술 적용    | COMMERCIALIZED           | 라인속도·정렬오차   |
| 탭 접합        | 산업 필수공정    | BASELINE                 | 용접방식·검사     |
| On-Vent 레이저 | 시제품 검증     | PROTOTYPE_VALIDATION     | 양산 수율·고객    |
| 전해액 주입      | 산업 필수공정    | BASELINE                 | 주입·함침 조건    |
| 포메이션·에이징    | 산업 필수공정    | BASELINE                 | 시간·프로토콜     |
| 비파괴검사       | 필요기술       | PARTIALLY_DISCLOSED      | 장비·전수범위     |
| CTP 조립      | 기술 개발      | DEVELOPMENT              | 양산차·재작업     |
| 설비 지능화      | 다자 검증      | VALIDATION               | 글로벌 배포범위    |
| 제조 디지털 스레드  | 공식 통합 미확인  | ANALYTICAL_LAYER         | 플랫폼·데이터범위   |

---

# D04-29. Manufacturing Technology Gap Register
