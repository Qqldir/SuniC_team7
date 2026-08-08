---
id: skes-d03-part-2-대표기업-심층-확장팩-hydrogen-상세-master-7
title: Part 2. 대표기업 심층 확장팩 — Hydrogen 상세 Master
summary: "SK이노베이션의 액화수소 생산·저장·충전부터 블루/그린수소까지, 공정 데이터·운영 KPI·최적화 기회를 단계별로 정의한 문서"
tags: [d03, product, schema, table, "xref:d17"]
keywords: [액화수소, 수소충전소, 블루수소, 그린수소, 탱크로리, BOG, 수전해, 공급망 최적화, 배송 경로, 탄소강도]
related: [PS-ENS-H2-01, PS-ENS-H2-02, PS-ENS-H2-03]
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 2. 대표기업 심층 확장팩
tokens: 1068
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 2. 대표기업 심층 확장팩

## 19. Hydrogen 상세 Master

### 19.1 `PS-ENS-H2-01` — 액화수소 생산

인천 액화수소플랜트는 SK인천석유화학 부생수소를 사용하며 공식 생산능력은 연 3만톤, 부지는 약 5만㎡다. 2024년부터 수도권을 포함한 전국 공급이 공개돼 있다. 생산능력은 실제 생산량·판매량·가동률이 아니다. ([SRC-ENS-D03-0012], [SRC-ENS-D03-0021])

```yaml
liquid_hydrogen_production:
  feed:
    - byproduct_hydrogen_flow
    - purity_and_impurities
    - pressure_temperature
  process:
    - purification
    - compression_and_precooling
    - liquefaction_at_cryogenic_temperature
    - storage_and_loading
  output:
    - liquid_hydrogen_quantity
    - product_purity
    - energy_intensity
    - boil_off_and_loss
  kpi:
    - kWh_per_kg_H2
    - yield
    - availability
    - off_spec_rate
    - safety_event
```

**O/I 우선기회**: 원료 조성 변동과 전력소비를 반영한 setpoint 추천, 극저온 회전기계 상태진단, BOG 발생 예측, 품질 이상 조기탐지, 생산–저장–출하 동기화.

### 19.2 `PS-ENS-H2-02` — 액화수소 저장·탱크로리 물류

| Decision | 데이터 | 제약 | KPI |
|---|---|---|---|
| 저장계획 | 탱크 레벨·압력·온도·입출고 | 안전재고·탱크용량 | 재고부족·BOG |
| 배차 | 주문·충전소 재고·차량·기사 | 운행시간·위험물 규정 | km/kg·정시율 |
| 경로 | 교통·기상·충전소 창구 | 안전·접근·휴게 | 배송시간·위험 |
| 회수·정비 | 탱크로리 상태·검사·고장 | 검사주기·부품 | 가동률·고장정지 |

**필수 Gate**: 극저온 안전, 고압가스 규정, 운전자 자격, 위치·고객데이터 보안, 비상대응, 추천경로의 human override.

### 19.3 `PS-ENS-H2-03` — 충전소 공급망 연계

액화수소 충전서비스의 제품가치는 충전소 숫자 자체가 아니라 `수소가 필요한 시간에 재고·설비·인력이 준비되어 차량을 처리하는 능력`이다.

| Data domain | 예시 | O/I 활용 |
|---|---|---|
| Demand | 차량유형, 버스노선, 예약, 시간대별 충전 | 단기수요 예측 |
| Inventory | 저장량, 압력, 온도, BOG | 재고·배송 트리거 |
| Equipment | 펌프, 압축, 디스펜서, 냉각, alarm | 고장예측·정비 |
| Operations | 충전시간, 성공·중단, 대기열 | throughput 최적화 |
| Logistics | 출하·차량·ETA·납품 | 생산–배송–충전 동기화 |

### 19.4 `PS-ENS-H2-04/05` — 블루·그린수소 계획

| 제품 | 공개 상태 | 제품성립 조건 | 데이터 Gap | 초기 O/I 형식 |
|---|---|---|---|---|
| 블루수소 | 장기적 검토 | LNG 원료·개질·포집·운송·저장·offtake | 탄소강도, 포집률, 저장권리, 원가 | 공정/탄소 시뮬레이션·MRV 설계 |
| 그린수소 | 추진계획 | 재생전력·수전해·물·저장·수요처 | 전력단가, 이용률, 물, 효율, 고객 | 전해조 운전·전력조달 최적화 PoC |

대규모 설비투자를 D17 과제로 바로 추천하지 않는다. 먼저 `가정관리–경제성–탄소 MRV–수요확약` 데이터룸을 구축하는 과제로 제한한다.

---
