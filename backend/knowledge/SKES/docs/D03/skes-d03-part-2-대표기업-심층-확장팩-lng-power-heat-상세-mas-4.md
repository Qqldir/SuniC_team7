---
id: skes-d03-part-2-대표기업-심층-확장팩-lng-power-heat-상세-mas-4
title: Part 2. 대표기업 심층 확장팩 — LNG·Power·Heat 상세 Master
summary: "천연가스 조달부터 최종 송출까지 LNG 사업 전체 가치사슬의 운영 데이터, 성과지표, AI 개선 기회를 종합하는 문서."
tags: [d03, product, schema, table, "xref:d17"]
keywords: [천연가스 조달, 액화설비 운영, 해상운송, LNG 터미널, BOG 처리, 기화 (regasification), cargo 배정, 재고 최적화]
related: [PS-ENS-LNG-01, PS-ENS-LNG-02, PS-ENS-LNG-03, PS-ENS-LNG-04, PS-ENS-LNG-04A, PS-ENS-LNG-04B, PS-ENS-LNG-04C, PS-ENS-LNG-04D, PS-ENS-PWR-01, PS-ENS-PWR-02]
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 2. 대표기업 심층 확장팩
tokens: 2573
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 2. 대표기업 심층 확장팩

## 16. LNG·Power·Heat 상세 Master

### 16.1 `PS-ENS-LNG-01` — 천연가스·LNG 조달 포트폴리오

**Human-readable description**

E&S의 LNG 제공가치는 단순 현물 구매가 아니라 해외 가스전·액화설비 사용권·장기계약·선박·국내 터미널·발전 수요를 연결하는 포트폴리오 운영에 있다. 공개자료는 인도네시아·호주·미국 가스전과 미국 Freeport LNG 터미널 사용권을 확인하지만, 계약별 가격식·take-or-pay·목적지 제한·헤지 조건은 공개하지 않는다. ([SRC-ENS-D03-0018], [SRC-ENS-D03-0022])

```yaml
product_solution_id: PS-ENS-LNG-01
canonical_name: Natural Gas and LNG Procurement Portfolio
lifecycle_status: commercial_operating
user_customer:
  - E&S 발전운영 조직
  - 도시가스 자회사
  - LNG 트레이딩·수급 조직
delivery_mechanism:
  - 지분가스 및 장기 LNG 도입
  - 액화설비 사용권 기반 물량 확보
  - 선박·터미널을 통한 국내 반입
value_proposition:
  - 연료 안정성
  - 공급원 다변화
  - 수요·가격 변동 대응
data_inputs:
  - 계약물량과 인도창
  - 유가·가스가격·환율
  - 발전·도시가스 수요예측
  - 선박 ETA와 터미널 재고
decision_outputs:
  - 월·주·일 도입계획
  - cargo 배정과 재판매/대체조달 후보
  - 재고·수요 불균형 경보
kpi:
  - delivered LNG cost
  - 공급부족·과잉 물량
  - 긴급조달 비용
  - 계약 유연성 활용률
governance_gates:
  - 계약기밀
  - 시장조작·거래통제
  - 신용·환율·가격위험
source_ids: [SRC-ENS-D03-0018, SRC-ENS-D03-0022]
```

**O/I 검증 질문**

- 수요예측·cargo 일정·재고·가격이 하나의 의사결정 화면에서 연결되는가.
- 계약조건을 공개형 AI에 노출하지 않고 최적화할 수 있는가.
- 추천 결과가 트레이더 판단을 설명할 수 있고 audit trail을 남기는가.
- `절감액`을 시장가격 변동효과와 알고리즘 효과로 분리할 수 있는가.

### 16.2 `PS-ENS-LNG-02` — LNG 액화설비 연계

액화는 천연가스를 장거리 해상운송 가능한 LNG로 전환하는 기능이다. E&S의 공개자료는 Freeport LNG 사용권과 호주 LNG 프로젝트 연계를 보여주지만 개별 Train의 E&S 운영권·에너지 원단위·downtime은 공개하지 않는다. 따라서 D17에서는 액화공정 자체 제어보다 `계약 물량·가동상태·선적계획 연계`를 우선 탐색한다. ([SRC-ENS-D03-0018], [SRC-ENS-D03-0022])

| Dimension | DB 값 |
|---|---|
| Value | LNG 변환능력과 선적 유연성 확보 |
| Core data | feed gas, nomination, Train availability, cargo window, 품질, 에너지소비 |
| KPI | 액화가용성, 지연시간, 계약물량 충족률, 에너지 원단위 |
| Pain hypothesis | 설비상태와 cargo 일정의 정보지연, outage 영향 시나리오 부족 |
| O/I interface | outage 영향 예측, cargo rescheduling, 품질·에너지 이상탐지 |
| Gate | JV 데이터권리, 설비제어 권한, 계약조건, OT 보안 |

### 16.3 `PS-ENS-LNG-03` — LNG 해상운송

전용선 운송은 생산·액화와 국내 터미널 사이의 시간차를 흡수한다. 제품은 선박운송 자체가 아니라 `안전한 정시 인도와 재고 안정성`이다.

| Data layer | 세부 데이터 | 사용 결정 |
|---|---|---|
| Voyage | 위치, 속력, ETA, 항로, 기상·해상 | 항로·속력·도착창 조정 |
| Cargo | 적재량, 온도·압력, 조성, BOG | 손실·품질·연료관리 |
| Terminal | berth window, 탱크 여유, send-out | 대기·접안·하역계획 |
| Demand | 발전계획, 도시가스 수요, 재고 | cargo 우선순위·도입시점 |
| Cost | 연료, 용선, 항만, 지연비용 | 경제속도·대안비교 |

**성과지표**: ETA 오차, berth 대기시간, BOG 손실, 연료원단위, schedule change 횟수, 안전사건.

**O/I Seed 확장**: 기상·AIS·터미널·수요 데이터를 결합한 ETA/도착창 추천, BOG 원인분해, 선박–터미널–발전 통합 시뮬레이션.

### 16.4 `PS-ENS-LNG-04` — LNG 터미널 하역·저장·기화·송출

터미널 서비스는 하나의 제품이 아니라 네 개의 연속 서비스로 분해한다.

| Sub-service ID | 기능 | 입력 | 출력 | 대표 KPI |
|---|---|---|---|---|
| `PS-ENS-LNG-04A` | Berthing & Unloading | 선박 ETA, berth, 하역설비 | LNG 탱크 이송 | 대기·하역시간 |
| `PS-ENS-LNG-04B` | Storage & Inventory | 탱크 레벨, 온도, 조성 | 사용가능 재고 | heel, 가용용량, stratification |
| `PS-ENS-LNG-04C` | BOG Handling | 압력, BOG 유량, 압축기 | 재액화·연료·처리 | BOG 원단위, flare/vent |
| `PS-ENS-LNG-04D` | Regasification & Send-out | 수요, 기화설비, 배관압력 | 기체가스 송출 | send-out 신뢰도·에너지 |

**운영 데이터 모델**

```yaml
terminal_event:
  timestamp: ISO-8601
  asset_id: tank | pump | compressor | vaporizer | pipeline | berth
  operating_state: running | standby | maintenance | trip
  process_values: temperature pressure flow level composition vibration
  schedule_context: cargo_id unloading_window demand_plan
  alarm_context: alarm_code severity acknowledgement recovery
  maintenance_context: work_order failure_mode parts labor
```

**O/I 우선순위**

1. 탱크재고·선박 ETA·send-out 동시예측.
2. BOG 발생량 예측과 압축기 운전 최적화.
3. 펌프·압축기·기화기 예지보전.
4. alarm flood와 비정상상태 조기탐지.
5. 작업허가·점검·정비기록의 디지털 계보.

### 16.5 `PS-ENS-PWR-01` — LNG 복합화력 전력

복합화력 제품은 전력시장에 판매되는 전력이지만, 운영 의사결정은 연료비·SMP·기동정지·heat rate·배출·설비수명 간의 균형이다.

| Decision horizon | 핵심 의사결정 | 입력 데이터 | KPI |
|---|---|---|---|
| 월·주 | 연료·정비·가동계획 | 계약연료, 정비창, 가격전망 | availability, margin |
| 일전 | 발전계획·시장 대응 | 수요·SMP·기상·효율곡선 | contribution margin |
| 실시간 | 부하추종·효율·배출 | 출력, 온도, 진동, 배출 | heat rate, ramp, emissions |
| 정비 | 검사·부품·outage | 운전시간, start count, 상태 | forced outage, MTBF, MTTR |

**Pain Point hypothesis**

- 설비상태 모델과 시장수익 모델이 분리되어 있을 수 있다.
- 부분부하·기동정지 비용·설비열화가 경제급전에 충분히 반영되지 않을 수 있다.
- 이상탐지는 많지만 조치 우선순위와 경제적 영향이 연결되지 않을 수 있다.

**D17 전환조건**: 실제 DCS/PI historian 접근, 열성능 기준선, 과거 trip·work order 라벨, 운전원 승인체계.

### 16.6 `PS-ENS-PWR-02` — CHP 전력·지역열

CHP는 전력과 열을 동시에 생산하므로 단일 목적 최적화가 부적합하다. 열수요는 외기온·시간·건물유형에 좌우되고, 전력수익은 시장가격과 설비제약에 좌우된다.

```yaml
multi_objective_dispatch:
  objectives:
    - 전력수익 최대화
    - 열공급 신뢰도 유지
    - 연료·배출·기동비용 최소화
    - 설비운전 제약 준수
  constraints:
    - 열수요와 공급온도
    - 축열조 용량
    - 발전기 최소출력·ramp
    - 배관압력·온도·안전
  outputs:
    - 전력·열 생산계획
    - 축열 충방전 계획
    - 이상수요·누수 후보
```

**O/I 기회**: 단기 열수요 예측, 공급온도 최적화, 열네트워크 누수·열손실 추정, 전력·열·축열 동시 최적화, 고객 민원·설비상태 연계.

---
