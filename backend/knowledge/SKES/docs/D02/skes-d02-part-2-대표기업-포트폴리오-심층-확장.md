---
id: skes-d02-part-2-대표기업-포트폴리오-심층-확장
title: Part 2. 대표기업 포트폴리오 심층 확장
summary: "SK이노베이션 E&S의 사업을 계약형·규제·상품·성장 4가지 경제모델로 분류하고, 10개 계층의 사업역할·병목·데이터 연결을 정의한 포트폴리오 운영 모델 및 LNG 가치사슬 전략을 담은 문서."
tags: [d02, business, schema, table, "xref:d17", "xref:d03"]
keywords: [LNG 가치사슬, 경제모델 분류, 포트폴리오 계층, 현금흐름 동인, 병목 요소, ESS, 도시가스, 열병합발전, 해상풍력, CCS]
related: [PORT-ENS-UP-01, PORT-ENS-MID-01, PORT-ENS-MID-02, PORT-ENS-MID-03, PORT-ENS-DOWN-01, PORT-ENS-DOWN-02, PORT-ENS-GROW-01, PORT-ENS-GROW-02, PORT-ENS-GROW-03, PORT-ENS-GROW-04, BUS-ENS-01, BUS-ENS-03, BUS-ENS-02, BUS-ENS-04, BUS-ENS-05, BUS-ENS-06, BUS-ENS-07, VP-ENS-001, VP-ENS-002, VP-ENS-003, VP-ENS-004, VP-ENS-005, VP-ENS-006, VP-ENS-007]
priority: normal
domain: D02
section: ""
source: SK이노베이션E&S_D02_Business_Portfolio_v2_보강본.md
breadcrumb: ""
tokens: 3824
updated: 2026-08-06
---

> SK이노베이션 E&S · D02 사업 포트폴리오

# Part 2. 대표기업 포트폴리오 심층 확장

## 17. Portfolio Operating Model

### 17.1 사업을 네 가지 경제모델로 분리

| Economic Model | 포함 사업 | 현금흐름 동인 | 변동성 | O/I가 직접 개선할 수 있는 것 |
|---|---|---|---|---|
| `CONTRACTED_INFRASTRUCTURE` | LNG 장기계약·터미널·PPA·일부 ESS | 계약물량·가용성·정산 | 계약·가동·신용 | 가용성·일정·정산·예측 |
| `REGULATED_UTILITY` | 도시가스 | 공급량·규제요금·비용회수 | 기상·수요·규제 | 수요예측·안전·검침·현장생산성 |
| `MERCHANT_MARKET` | 발전·미국 ESS·일부 재생전력 | 시장가격·연료·입찰·가동률 | 가격·계통·설비 | 경제급전·입찰·열화·정비 |
| `DEVELOPMENT_GROWTH` | 해상풍력·DERMS·VPP·청정수소·CCS | 개발성공·PPA/offtake·금융조달 | 인허가·CAPEX·기술·수요 | 데이터룸·개발 Gate·MRV·시뮬레이션 |

> 같은 기술이라도 경제모델이 다르면 KPI가 달라진다. 예를 들어 ESS는 공장에서는 전기요금 절감, 재생연계에서는 예측오차·출력제한, KCE에서는 시장수익과 계통서비스가 핵심이다.

### 17.2 Portfolio Layer Master

| Layer ID | 사업역할 | 대표 자산/역량 | 다음 Layer에 제공 | 핵심 병목 |
|---|---|---|---|---|
| `PORT-ENS-UP-01` | 가스 생산·조달 | 가스전·계약·트레이딩 | feed gas/LNG | 가격·생산·계약 유연성 |
| `PORT-ENS-MID-01` | 액화 | 액화설비 사용권·프로젝트 | LNG cargo | 가동률·에너지·일정 |
| `PORT-ENS-MID-02` | 선박운송 | 전용선 | 국내 도착 cargo | ETA·BOG·기상 |
| `PORT-ENS-MID-03` | 터미널 | berth·탱크·기화·배관 | 기체가스 | 재고·BOG·send-out |
| `PORT-ENS-DOWN-01` | 발전·CHP | CCGT·열망·축열 | 전력·열 | heat rate·시장·정비 |
| `PORT-ENS-DOWN-02` | 도시가스 | 7개사·8개 권역 배관망 | 가정·산업 가스 | 수요·안전·고객운영 |
| `PORT-ENS-GROW-01` | 재생발전 | 태양광·육상/해상풍력 | 전력·인증·PPA | 개발·기상·O&M·계통 |
| `PORT-ENS-GROW-02` | 수소 | 액화플랜트·물류·충전연계 | 액화수소 | 원단위·BOG·수요·안전 |
| `PORT-ENS-GROW-03` | 에너지솔루션 | KCE·EverCharge·Ensolve·iPARKING | ESS·충전·분산자원 서비스 | 시장규칙·연동·열화·가동률 |
| `PORT-ENS-GROW-04` | CCS/저탄소 LNG | 프로젝트·MRV 계획 | 감축·저장 주장 | 허가·책임·탄소수지 |

## 18. Business Unit Deep Records

### 18.1 `BUS-ENS-01` LNG Value Chain

```yaml
business_id: BUS-ENS-01
role: base_cashflow_and_strategic_feedstock
value_chain:
  - upstream_gas
  - liquefaction_access
  - shipping
  - terminal
  - power_citygas_hydrogen_feed
customer_or_user:
  - internal_power_and_citygas
  - trading_counterparties
  - potential_external_terminal_or_lng_customer_not_publicly_confirmed
revenue_logic:
  disclosed: LNG linked business and downstream sales
  analysis: commodity_margin contract_margin asset_utilization
cost_drivers:
  - gas_and_lng_price
  - liquefaction_and_shipping
  - terminal_energy_and_maintenance
  - fx_and_financing
risk_drivers:
  - contract_rigidity
  - demand_and_price_volatility
  - project_and_geopolitical_risk
  - methane_and_carbon_regulation
oi_value_pool:
  - procurement_and_demand_scenario
  - vessel_terminal_inventory
  - bog_and_energy_efficiency
  - predictive_maintenance
  - methane_and_carbon_mrv
```

**대표기업 판단**

LNG는 다른 사업의 배경설명이 아니라 E&S 포트폴리오의 데이터 spine이다. 선박도착·터미널재고·발전계획·도시가스 수요·수소 원료·탄소데이터가 연결될수록 개별 최적화보다 통합 최적화 가치가 커진다. 다만 계약·가격·헤지 데이터의 보안 때문에 외부 SaaS보다 secure environment, anonymized constraint, human approval이 중요하다.

### 18.2 `BUS-ENS-03` Power and CHP

```yaml
business_id: BUS-ENS-03
economic_model: merchant_plus_infrastructure
products:
  - electricity
  - district_heat
inputs:
  - LNG_or_natural_gas
  - market_and_demand_signal
  - generation_and_heat_assets
revenue_drivers:
  - electricity_price_and_dispatch
  - heat_demand_and_tariff
  - availability_and_efficiency
cost_drivers:
  - fuel
  - start_stop_and_maintenance
  - emissions_and_compliance
oi_value_pool:
  - heat_rate_and_dispatch
  - outage_prediction
  - CHP_heat_power_storage_cooptimization
  - work_order_and_spare_parts
```

### 18.3 `BUS-ENS-02` City Gas

```yaml
business_id: BUS-ENS-02
economic_model: regulated_utility
scale_disclosed:
  subsidiaries: 7
  service_regions: 8
  households_approx: 5.1_million
  2023_supply: 5.4_billion_m3
  2023_market_share: 22.6_percent
service_chain:
  - demand_and_sendout
  - pressure_and_pipeline_operation
  - metering_and_billing
  - customer_service
  - inspection_and_emergency
oi_value_pool:
  - regional_demand_forecast
  - dynamic_RBMS
  - excavation_and_leak_detection
  - OCR_and_AMI_quality
  - move_in_out_field_routing
  - customer_contact_automation_with_safety_escalation
source_ids: [SRC-ENS-D02-0003]
```

**자회사 공통화와 개별화 원칙**

| 대상 | 공통화 후보 | 개별 유지가 필요한 것 |
|---|---|---|
| 데이터 모델 | 고객·계량기·배관·점검·민원 ID | 지역 GIS·레거시 코드 |
| AI 모델 | OCR·상담분류·위험 feature framework | 지역별 수요·배관·사고 baseline |
| 업무 | 전출입·검침·점검 표준 KPI | 규정·조직·현장동선 |
| 플랫폼 | MLOps·권한·감사·모니터링 | 자회사 운영시스템 연계 |

### 18.4 `BUS-ENS-04` Renewable Energy

```yaml
business_id: BUS-ENS-04
economic_models:
  - project_development
  - power_market_sales
  - corporate_direct_PPA
  - O&M_and_energy_solution_growth
status_boundary:
  operating: separately_identified_assets_only
  operating_and_developing: 3.5_GW_solar_disclosed_as_combined
  pipeline: approx_5_GW_not_additive
  offshore_wind_phase1: operating_2025
  offshore_wind_phase2_3: planned
value_drivers:
  - development_success_and_COD
  - capacity_factor_and_availability
  - PPA_price_and_credit
  - forecast_and_settlement
  - curtailment_and_grid_connection
oi_value_pool:
  - site_and_pipeline_data_room
  - generation_forecast
  - drone_and_condition_O&M
  - PPA_load_asset_matching
  - automated_settlement_and_evidence
```

### 18.5 `BUS-ENS-05` Hydrogen

```yaml
business_id: BUS-ENS-05
current_commercial_core:
  - byproduct_hydrogen_purification_and_liquefaction
  - liquid_hydrogen_storage_transport_supply
current_capacity_disclosed: 30000_tonnes_per_year
planned_or_considering:
  - blue_hydrogen
  - green_hydrogen
commercial_unknowns:
  - actual_production_and_sales
  - utilization
  - customer_and_offtake
  - price_and_unit_cost
oi_value_pool:
  - plant_energy_and_yield
  - cryogenic_reliability_and_boiloff
  - production_inventory_logistics_station_plan
  - safety_and_emergency_response
  - clean_hydrogen_economics_and_MRV
```

### 18.6 `BUS-ENS-06` Energy Solution

| Capability platform | 공개 확인 역할 | 경제모델 | 대표 데이터 | D17 우선 질문 |
|---|---|---|---|---|
| KCE | 미국 계통 ESS 개발·운영·AI 입찰 | merchant/contracted | market·BMS·bid·dispatch | 보유 AI의 타시장 이전성 |
| EverCharge | EVSE·SmartPower·mesh·턴키 서비스 | hardware+software+service | session·site load·charger | 국내/북미 확장과 ESS 결합 |
| PassKey | 북미 에너지전환 투자·통합 | portfolio/platform | 투자·자회사·project | 자회사 역량 시너지 |
| Ensolve | 배전망 기반 DERMS·ESS·VPP·O&M 추진 | regulated/development | topology·DER·meter | 현재 상용단계·데이터권리 |
| iPARKING | 국내 주차 네트워크 기반 충전 | service/network | parking·charging·payment | 부지부하·가동률·현장운영 |

### 18.7 `BUS-ENS-07` CCS and Low-carbon LNG

```yaml
business_id: BUS-ENS-07
economic_model: development_growth
product_claim_requires:
  - lifecycle_emission_boundary
  - capture_transport_storage_mass_balance
  - storage_integrity_and_liability
  - customer_allocation_and_verification
major_unknowns:
  - FID_and_schedule
  - permits_and_cross_border_rules
  - capture_rate_and_energy_penalty
  - storage_right_and_long_term_liability
  - offtake_and_price_premium
oi_value_pool:
  - project_data_room
  - carbon_mass_balance
  - meter_and_custody_data_lineage
  - anomaly_and_leak_monitoring
  - third_party_verification_package
```

## 19. Portfolio Synergy Graph

```text
BUS-ENS-01 LNG
  FEEDS -> BUS-ENS-03 Power/CHP
  FEEDS -> BUS-ENS-02 City Gas
  POTENTIALLY_FEEDS -> BUS-ENS-05 Hydrogen
  REQUIRES_DECARBONIZATION -> BUS-ENS-07 CCS

BUS-ENS-04 Renewable
  SELLS_THROUGH -> Direct PPA
  ENABLES -> BUS-ENS-05 Green Hydrogen
  CREATES_FLEXIBILITY_NEED -> BUS-ENS-06 ESS/DERMS/VPP

BUS-ENS-06 Energy Solution
  OPTIMIZES -> BUS-ENS-04 Renewable
  OPTIMIZES -> Corporate/Industrial Customer Load
  CONNECTS -> EV Charging and Distributed Energy

BUS-ENS-02 City Gas
  PROVIDES_NETWORK_OPERATING_DATA -> Safety/Demand AI
  PROVIDES_LOCAL_CUSTOMER_INTERFACE -> Future Energy Solution Optionality
```

### 19.1 Synergy를 과제로 전환하는 규칙

| Synergy claim | 과제화에 필요한 증거 | 잘못된 추천 예 |
|---|---|---|
| LNG–발전 통합 | cargo·재고·발전계획의 공통 owner·데이터 | 두 시스템이 있다는 이유만으로 통합플랫폼 구축 |
| 재생–ESS | curtailment·정산·열화의 경제적 baseline | ESS 설치만 추천 |
| 충전–ESS | 부지 전력제약·충전수요·증설비 | 모든 충전소에 ESS |
| PPA–재생 | 고객부하·자산발전·계약조건 | 단순 영업챗봇 |
| 수소–LNG/재생 | 원료·전력·수요·탄소강도 | 수소 생산설비 확대 |
| CCS–저탄소 LNG | 전과정 탄소수지·저장권리 | 센서 도입만으로 저탄소 인증 |

## 20. Portfolio Decision Matrix

| Business | 운영 성숙도 | 공개 데이터 풍부도 | 현장 데이터 발생 | O/I 단기성 | 기본 전략 |
|---|---:|---:|---:|---:|---|
| LNG 조달·선박·터미널 | 5 | 3 | 5 | 5 | 심층 탐색·secure PoC |
| 발전·CHP | 5 | 3 | 5 | 5 | 효율·신뢰도 우선 |
| 도시가스 | 5 | 4 | 5 | 5 | 자회사 공통화+현장화 |
| 태양광·풍력 | 4 | 4 | 5 | 5 | forecast/O&M/PPA |
| 액화수소 | 4 | 3 | 5 | 5 | 생산–물류–충전 통합 |
| KCE ESS | 5 | 4 | 5 | 5 | 보유역량 확장·통합 |
| EverCharge/충전 | 4 | 4 | 5 | 5 | load·uptime·BESS |
| DERMS/VPP | 2~3 | 3 | 3 | 3 | 최소기능·상용단계 확인 |
| 블루/그린수소 | 1~2 | 2 | 1~2 | 2 | 경제성·수요·MRV Gate |
| CCS/저탄소 LNG | 1~2 | 2 | 1~2 | 2 | 데이터룸·MRV PoC |

## 21. D02 to D17 Value Pool Handover

| Value Pool ID | 사업 | 개선 레버 | KPI | 연계 D03 Seed |
|---|---|---|---|---|
| `VP-ENS-001` | LNG | 수요·cargo·재고 통합 | 긴급조달·재고위반 | 001/022/023 |
| `VP-ENS-002` | 터미널 | BOG·설비·일정 | BOG·에너지·downtime | 002/024/025 |
| `VP-ENS-003` | 발전 | 효율·경제급전·정비 | heat rate·margin·outage | 003/026/027 |
| `VP-ENS-004` | CHP | 전력·열·축열 | 종합효율·열위반 | 004/028 |
| `VP-ENS-005` | 도시가스 | 수요·RBMS·검침·현장 | 누출·점검·처리시간 | 005~007/029~033 |
| `VP-ENS-006` | 재생 | 예측·O&M·해상접근 | forecast·downtime·MWh | 008/009/034/035 |
| `VP-ENS-007` | PPA | 자산매칭·정산·증빙 | 제안시간·오류·감사 | 010/011/036/037 |
| `VP-ENS-008` | 수소 | 원단위·신뢰도·물류 | kWh/kg·stockout·BOG | 012~014/038~040 |
| `VP-ENS-009` | ESS | 열화·입찰·안전 | net value·가용성 | 015~018/041~047 |
| `VP-ENS-010` | 충전 | 가동률·부하·ESS | 성공률·peak·MTTR | 019/020/048~050 |
| `VP-ENS-011` | CCS | 탄소수지·계보·검증 | 완전성·검증시간 | 021/051/052 |

## 22. D02 v2 Completion Record

```yaml
domain: D02_Business_Portfolio
version: 2.0
depth_policy: representative_company_deep_database
economic_models: 4
portfolio_layers: 10
business_deep_records: 7
owned_or_linked_solution_platforms: 5
portfolio_value_pools: 11
priority_rule:
  - operating cashflow and safety domains first
  - owned capability reuse before duplicate procurement
  - planned businesses require stage and demand gate
  - undisclosed contract and financial values remain gaps
D03_handover: completed_to_D03_v2
```
