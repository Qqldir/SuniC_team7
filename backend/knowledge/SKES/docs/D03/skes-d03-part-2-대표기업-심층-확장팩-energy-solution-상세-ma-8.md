---
id: skes-d03-part-2-대표기업-심층-확장팩-energy-solution-상세-ma-8
title: Part 2. 대표기업 심층 확장팩 — Energy Solution 상세 Master
summary: "5가지 에너지솔루션(수요관리·재생·계통형 ESS, DERMS, VPP)의 운영 로직·KPI·비용을 기술한 사양서"
tags: [d03, product, schema, table]
keywords: [수요관리, ESS, 재생에너지, 배터리열화, DERMS, 분산자원, VPP, MarketCapture, 예측]
related: [PS-ENS-ES-01, PS-ENS-ES-02, PS-ENS-ES-03, PS-ENS-ES-04, PS-ENS-ES-05, PS-ENS-ES-06, PS-ENS-ES-07A, PS-ENS-ES-07B, PS-ENS-ES-08]
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 2. 대표기업 심층 확장팩
tokens: 2329
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 2. 대표기업 심층 확장팩

## 20. Energy Solution 상세 Master

### 20.1 `PS-ENS-ES-01` — 수요관리 ESS

```yaml
demand_management_ess:
  customer: factory_or_large_commercial_site
  objectives:
    - maximum_demand_reduction
    - tariff_cost_saving
    - resilience_optional
  inputs:
    - interval_load
    - tariff_and_demand_charge
    - battery_soc_soh_temperature
    - production_schedule
    - demand_response_signal
  decisions:
    - charge_discharge_schedule
    - peak_event_reserve
    - operating_limit
  economics:
    - gross_saving
    - degradation_cost
    - efficiency_loss
    - maintenance_and_financing
```

**O/I 검증**: 절감액만 최대화하지 말고 열화비용·안전여유·생산중단 위험을 포함한다.

### 20.2 `PS-ENS-ES-02` — 재생에너지 연계 ESS

재생연계 ESS의 목적은 발전량을 단순 저장하는 것이 아니라 예측오차·출력제한·정산·PPA 공급패턴·배터리 열화를 함께 관리하는 것이다.

| Objective | 핵심 입력 | KPI | 상충관계 |
|---|---|---|---|
| 출력 평탄화 | 실시간 발전·기상 | ramp, 변동성 | 배터리 cycle 증가 |
| 예측오차 완화 | 일전예측·실측 | forecast/settlement error | SOC 여유 필요 |
| 출력제한 회피 | 계통제약·curtailment | 회수에너지 | 가격·열화 |
| PPA 이행 | 고객부하·계약곡선 | 공급부족·초과 | 시장매매 비용 |
| 시장수익 | 가격·보조서비스 | 순수익 | 안전·가용성 |

### 20.3 `PS-ENS-ES-03` — KCE 계통형 ESS와 MarketCapture

KCE는 뉴욕·텍사스 중심 계통형 ESS를 개발·운영한다. E&S 공식 페이지는 약 0.6GW, KCE의 2025년 발표는 200MW 추가 프로젝트 후 운영 포트폴리오 620MW 이상을 제시한다. 수치 기준일과 범위가 달라 별도 레코드로 보존한다. ([SRC-ENS-D03-0011], [SRC-ENS-D03-0015])

MarketCapture는 ERCOT에서 day-ahead와 5분 실시간 최적화·입찰을 수행하고 보고를 자동화하는 AI/ML 플랫폼으로 공개됐다. ([SRC-ENS-D03-0014])

```yaml
marketcapture_service:
  geography: ERCOT disclosed; NYISO rollout was planned in 2023
  asset: standalone_battery_energy_storage
  decisions:
    - day_ahead_bid
    - real_time_5_minute_bid
    - charge_discharge_dispatch
  reporting:
    - daily_weekly_monthly
    - revenue_vs_perfect_foresight_benchmark
  model_inputs_hypothesis:
    - market_price_and_grid_signal
    - battery_state_and_limit
    - outage_and_availability
  fact_boundary:
    - 세부 모델·수익개선율·고객별 성과는 미공개
source_ids: [SRC-ENS-D03-0014]
```

**대표기업 O/I 관점**

- 외부 솔루션 탐색보다 이미 보유한 MarketCapture의 국내·타시장 적용가능성과 데이터·규제 Gap을 먼저 본다.
- AI 입찰은 모델 정확도 외에 시장규칙 변경, 배터리 보증, degradation, cyber security, trader override를 검증한다.
- `완벽한 미래정보(perfect foresight)` 대비 벤치마크와 실제 달성가능 벤치마크를 구분한다.

### 20.4 `PS-ENS-ES-04` — DERMS

DERMS는 배전망과 분산자원 정보를 연결하는 운영체계다. E&S 공식자료는 Ensolve 인수 후 추진계획으로 설명하므로 상용 고객·기능은 확정하지 않는다. ([SRC-ENS-D03-0011])

| Capability layer | 필요 기능 | 핵심 데이터 | 초기 PoC |
|---|---|---|---|
| Visibility | DER 자산·상태·출력 가시화 | topology, meter, inverter, ESS | 데이터 모델·연동률 |
| Forecast | 부하·태양광·풍력·EV 예측 | interval data, weather | feeder forecast |
| Constraint | 전압·혼잡·역송 제약 분석 | network model, limits | violation prediction |
| Dispatch | ESS·인버터·부하 제어 | control interface | closed-loop sandbox |
| Settlement | 자원 성과·보상 | baseline, dispatch, meter | performance verification |

### 20.5 `PS-ENS-ES-05` — VPP·소규모전력중개

VPP는 공식적으로 `검토` 단계다. 따라서 후보 과제는 플랫폼 전면구축이 아니라 최소기능 검증으로 제한한다.

```yaml
vpp_minimum_viable_scope:
  resource_onboarding:
    - asset_identity
    - ownership_and_consent
    - telemetry_quality
  forecast:
    - baseline
    - generation_load_soc
  market:
    - bid_rule
    - dispatch
    - REC_and_power_transaction
  settlement:
    - measured_performance
    - allocation_and_payment
  exit_criteria:
    - insufficient_resource_pool
    - unreliable_telemetry
    - negative_unit_economics
    - regulatory_blocker
```

### 20.6 `PS-ENS-ES-06` — 재생에너지 O&M

| O&M module | 입력 | 분석·결정 | KPI |
|---|---|---|---|
| Remote monitoring | SCADA, alarm, weather | 이상탐지·우선순위 | detection lead time |
| Visual inspection | drone, thermal, RGB | 결함분류·위치화 | precision/recall |
| Work management | CMMS, crew, parts | 작업계획·배정 | MTTR, first-time fix |
| Performance | expected vs actual generation | loss attribution | recovered MWh |
| Warranty | serial, contract, event | 청구증빙 | recovery value |

### 20.7 `PS-ENS-ES-07A` — 국내 주차장 중심 EV 충전

국내 공식 페이지는 iPARKING 네트워크를 중심으로 다양한 충전서비스 확대 방향을 제시한다. 충전기 수·가동률·운영주체는 공개자료 Gap이다. ([SRC-ENS-D03-0011])

### 20.8 `PS-ENS-ES-07B` — EverCharge 북미 턴키 EV 충전

EverCharge는 하드웨어·소프트웨어·설치·서비스·A/S를 결합한 턴키 솔루션이며 공동주택과 fleet의 고밀도 설치에 초점을 둔다. 자체 mesh network와 동적부하관리로 기존 전력인프라의 제약을 완화한다고 공개한다. `기존 대비 5배 설치`는 특정 조건의 회사 주장으로 저장하며 보편적 성능값으로 사용하지 않는다. ([SRC-ENS-D03-0013])

| Product layer | 공개 기능 | 고객가치 | O/I·통합 접점 |
|---|---|---|---|
| EVSE hardware | 충전기 제조 | 설치·운영 표준화 | 원격진단·부품예측 |
| SmartPower | 동적부하관리 | 전력증설 없이 설치확대 | 건물부하·ESS 공동제어 |
| Mesh network | 지하주차장 연결성 | 통신신뢰도 | 장애탐지·self-healing |
| Turnkey install | 설계·설치·commissioning | 도입기간·복잡성 감소 | site survey 자동화 |
| Operations/A/S | 운영·유지보수 | 가동률·고객경험 | 예지보전·기사배정 |
| Fleet/Multi-family | 고밀도 charging | 다수차량 전력배분 | 예약·우선순위·정산 |

### 20.9 `PS-ENS-ES-08` — EV 충전+ESS 통합

EverCharge와 PassKey는 충전부지의 전력용량 부족을 해결하기 위해 BESS 결합을 공개했다. 이는 D17에서 `충전기 증설`보다 `부지 전력제약·수요·배터리 경제성` 문제로 전환해야 한다. ([SRC-ENS-D03-0020])

```yaml
charging_bess_site_optimizer:
  inputs:
    - grid_connection_limit
    - building_base_load
    - charger_sessions_and_reservations
    - tariff_demand_charge
    - battery_soc_soh
    - onsite_solar_optional
  objectives:
    - charging_success_and_departure_target
    - demand_charge_reduction
    - avoid_or_defer_grid_upgrade
    - battery_life_and_safety
  outputs:
    - charger_power_allocation
    - battery_dispatch
    - site_capacity_upgrade_trigger
```

---
