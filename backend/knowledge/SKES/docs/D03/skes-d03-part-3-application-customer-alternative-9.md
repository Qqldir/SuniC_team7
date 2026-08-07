---
id: skes-d03-part-3-application-customer-alternative-9
title: Part 3. Application·Customer·Alternative·Graph·Chunk 확장 — Expanded AI Retrieval Chunk Library
summary: "LNG 조달, 발전 최적화, 안전 관리 등 SK이노베이션 E&S 주요 사업의 AI/O&I 의사결정 구조와 데이터 요구사항"
tags: [d03, product, schema, "xref:d17"]
keywords: [LNG 포트폴리오, 선박 터미널, 발전 수익, 열공급 네트워크, 도시가스 안전, 배관 위험도, 직접 PPA, 액화수소, BOG, 시나리오]
related: []
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 3. Application·Customer·Alternative·Graph·Chunk 확장
tokens: 2502
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 3. Application·Customer·Alternative·Graph·Chunk 확장

## 28. Expanded AI Retrieval Chunk Library

### Chunk D03-006｜LNG 조달 의사결정

```yaml
chunk_id: CHUNK-ENS-D03-006
topic: lng_procurement_portfolio_decision
answer: >
  E&S의 LNG 조달은 해외 가스전·액화설비 사용권·장기/현물 물량·선박·터미널·발전/도시가스 수요를
  연결하는 포트폴리오 문제다. 공개자료는 밸류체인 자산을 확인하지만 계약 가격식과 유연성은 미공개다.
  O/I는 비식별 계약제약을 사용한 시나리오 비교·재고경보·설명형 추천부터 검증해야 한다.
linked_ids: [PS-ENS-LNG-01, APP-ENS-001, SEED-ENS-D03-022]
source_ids: [SRC-ENS-D03-0018, SRC-ENS-D03-0022]
```

### Chunk D03-007｜선박–터미널 통합

```yaml
chunk_id: CHUNK-ENS-D03-007
topic: lng_vessel_terminal_integration
answer: >
  LNG 선박 ETA·기상·berth·탱크재고·send-out을 함께 사용해야 대기시간과 재고위반을 줄일 수 있다.
  BOG는 하역·조성·탱크열유입·송출·압축기 상태의 함수이므로 단일센서 예측보다 physics+data 접근이 적합하다.
linked_ids: [PS-ENS-LNG-03, PS-ENS-LNG-04, APP-ENS-002, APP-ENS-003]
source_ids: [SRC-ENS-D03-0022]
```

### Chunk D03-008｜복합화력·CHP

```yaml
chunk_id: CHUNK-ENS-D03-008
topic: power_and_chp_optimization
answer: >
  복합화력은 시장가격·연료비·heat rate·기동비·설비상태를, CHP는 여기에 열수요·축열·열네트워크를 더해
  최적화해야 한다. 과제 KPI는 단순 예측정확도가 아니라 순마진·연료원단위·강제정지·열공급 위반이다.
linked_ids: [PS-ENS-PWR-01, PS-ENS-PWR-02, APP-ENS-004, APP-ENS-005]
source_ids: [SRC-ENS-D03-0022]
```

### Chunk D03-009｜도시가스 고객 Journey

```yaml
chunk_id: CHUNK-ENS-D03-009
topic: city_gas_customer_journey
answer: >
  도시가스 디지털 서비스는 자가검침·요금·납부·전출입·안전신고로 분해한다.
  OCR은 계량기 유형·과거사용량·human correction으로 검증하고, 누출신고는 AI 단독종료를 금지한다.
linked_ids: [PS-ENS-CG-02, APP-ENS-009, APP-ENS-010]
source_ids: [SRC-ENS-D03-0007, SRC-ENS-D03-0008]
```

### Chunk D03-010｜도시가스 RBMS

```yaml
chunk_id: CHUNK-ENS-D03-010
topic: city_gas_dynamic_risk
answer: >
  E&S는 도시가스 배관에 RBMS와 드론 안전점검을 공개했다. 심층 O/I는 GIS·재질·매설연도·압력·부식·굴착·기상·민원·사고를
  결합한 동적 위험도와 점검동선에 있다. 모델은 법정점검을 대체하지 않고 우선순위를 보조해야 한다.
linked_ids: [PS-ENS-CG-03, APP-ENS-007, APP-ENS-008]
source_ids: [SRC-ENS-D03-0010]
```

### Chunk D03-011｜재생에너지 상태값

```yaml
chunk_id: CHUNK-ENS-D03-011
topic: renewable_capacity_status
answer: >
  E&S 공식 페이지는 2025년 5월 기준 태양광 운영·개발 3.5GW와 약 5GW pipeline을 제시한다.
  두 수치는 중복 가능하므로 합산하지 않는다. 전남해상풍력 1단계는 2025년 상업운전, 2·3단계는 계획으로 분리한다.
linked_ids: [PS-ENS-REN-01, PS-ENS-REN-02]
source_ids: [SRC-ENS-D03-0009]
```

### Chunk D03-012｜직접 PPA 서비스 구조

```yaml
chunk_id: CHUNK-ENS-D03-012
topic: direct_ppa_end_to_end
answer: >
  직접 PPA는 고객진단·자산매칭·상업조건·계약·발전/부하예측·정산·증빙의 연속서비스다.
  공개사례에는 Amorepacific 5MW·20년과 BASF Korea의 2025년부터 20년 term sheet가 있다.
  O/I는 제안 시나리오, 자동대사, 예외처리, 감사 가능한 데이터 계보다.
linked_ids: [PS-ENS-REN-03, PS-ENS-REN-04, PS-ENS-REN-05, APP-ENS-013, APP-ENS-014]
source_ids: [SRC-ENS-D03-0016, SRC-ENS-D03-0017]
```

### Chunk D03-013｜액화수소 생산

```yaml
chunk_id: CHUNK-ENS-D03-013
topic: liquid_hydrogen_production
answer: >
  인천 액화수소플랜트는 부생수소를 사용하고 연 3만톤 생산능력·약 5만㎡로 공개됐다.
  capacity는 실제 생산·판매·가동률이 아니다. O/I KPI는 kWh/kg-H2, 수율, off-spec, 가동률, BOG, 안전이다.
linked_ids: [PS-ENS-H2-01, APP-ENS-015]
source_ids: [SRC-ENS-D03-0012, SRC-ENS-D03-0021]
```

### Chunk D03-014｜액화수소 물류

```yaml
chunk_id: CHUNK-ENS-D03-014
topic: liquid_hydrogen_logistics
answer: >
  액화수소 물류는 플랜트 재고·탱크 압력/온도·탱크로리·충전소 재고/수요를 연결해야 한다.
  최적화 목표는 배송비뿐 아니라 stockout·BOG·안전·정시충족이다.
linked_ids: [PS-ENS-H2-02, PS-ENS-H2-03, APP-ENS-016]
source_ids: [SRC-ENS-D03-0012]
```

### Chunk D03-015｜KCE MarketCapture

```yaml
chunk_id: CHUNK-ENS-D03-015
topic: kce_marketcapture
answer: >
  KCE MarketCapture는 ERCOT의 계통형 ESS를 대상으로 day-ahead와 5분 실시간 최적화·입찰을 수행하는
  AI/ML 플랫폼으로 공개됐다. 신규 과제는 외부 입찰솔루션 재도입보다 이 보유역량의 타시장 규칙·데이터·배터리 제약 적합성을 먼저 검증한다.
linked_ids: [ORG-ENS-KCE, PS-ENS-ES-03, PS-ENS-MARKETCAPTURE, APP-ENS-019]
source_ids: [SRC-ENS-D03-0014, SRC-ENS-D03-0015]
```

### Chunk D03-016｜DERMS·VPP 상태

```yaml
chunk_id: CHUNK-ENS-D03-016
topic: derms_vpp_status
answer: >
  E&S 공식자료에서 Ensolve 기반 DERMS·ESS·재생 O&M은 추진계획, VPP는 검토 단계다.
  D17은 전면 플랫폼 구축보다 데이터 모델·연동·feeder forecast·자원등록·baseline·정산의 최소기능 PoC를 우선해야 한다.
linked_ids: [PS-ENS-ES-04, PS-ENS-ES-05, APP-ENS-020, APP-ENS-021]
source_ids: [SRC-ENS-D03-0011]
```

### Chunk D03-017｜EverCharge SmartPower

```yaml
chunk_id: CHUNK-ENS-D03-017
topic: evercharge_smart_charging
answer: >
  EverCharge는 EVSE 하드웨어·mesh network·SmartPower 동적부하관리·설치·운영·A/S를 결합한 턴키 솔루션이다.
  기존 대비 5배 설치 주장은 회사가 공개한 특정 조건의 값으로 일반화하지 않는다.
  핵심 적용은 공동주택·fleet·주차장에서 제한된 부지전력을 차량 요구에 배분하는 것이다.
linked_ids: [ORG-ENS-EVERCHARGE, PS-ENS-ES-07B, APP-ENS-023]
source_ids: [SRC-ENS-D03-0013]
```

### Chunk D03-018｜EV 충전+ESS

```yaml
chunk_id: CHUNK-ENS-D03-018
topic: ev_charging_bess_integration
answer: >
  PassKey와 EverCharge는 충전부지 전력용량 부족에 BESS를 결합하는 방향을 공개했다.
  과제는 건물부하·충전세션·계통한도·요금·SOC/SOH를 사용해 전력배분과 ESS dispatch, 증설시점을 함께 결정해야 한다.
linked_ids: [PS-ENS-ES-08, APP-ENS-024]
source_ids: [SRC-ENS-D03-0020]
```

### Chunk D03-019｜CCS MRV

```yaml
chunk_id: CHUNK-ENS-D03-019
topic: ccs_mrv_chain_of_custody
answer: >
  CCS 제품은 포집·압축·운송·주입·저장·모니터링 전 단계의 CO2 질량과 품질·권리·버전을 추적해야 한다.
  저탄소 LNG는 upstream methane·액화·해상운송·기화·최종사용 경계를 명시해야 하며 홍보표현만으로 감축률을 채우지 않는다.
linked_ids: [PS-ENS-CCS-01, PS-ENS-CCS-02, APP-ENS-025]
source_ids: [SRC-ENS-D03-0022]
```

### Chunk D03-020｜대표기업 D17 우선순위

```yaml
chunk_id: CHUNK-ENS-D03-020
topic: representative_company_oi_priority
answer: >
  E&S 대표기업 D17은 운영 중이고 데이터가 발생하는 LNG 선박/터미널, 발전/CHP, 도시가스 안전·고객업무,
  PPA 정산, 액화수소 생산·물류, KCE ESS, EverCharge 충전을 우선한다.
  블루·그린수소, DERMS/VPP, CCS는 사업단계와 데이터권리를 먼저 검증하는 소규모 PoC로 제한한다.
linked_seed_range: SEED-ENS-D03-001_to_052
```

---
