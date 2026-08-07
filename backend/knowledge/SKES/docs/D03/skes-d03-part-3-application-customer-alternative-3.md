---
id: skes-d03-part-3-application-customer-alternative-3
title: Part 3. Application·Customer·Alternative·Graph·Chunk 확장 — Application Taxonomy (2)
summary: "소규모 발전·ESS·충전 등 5개 에너지 애플리케이션별 기술 요구사항(최소데이터, 성공지표)과 문제정의를 명시한 사양서."
tags: [d03, product, core-candidate, schema]
keywords: [DER, 재생에너지 유지보수, 스마트충전, ESS, CCS, MRV, 기술사양, 성공지표]
related: [APP-ENS-022, APP-ENS-023, APP-ENS-024, APP-ENS-025]
priority: critical
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 3. Application·Customer·Alternative·Graph·Chunk 확장
tokens: 658
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 3. Application·Customer·Alternative·Graph·Chunk 확장

```yaml
problem_statement: >
  소규모 발전·ESS·부하 자원의 등록·예측·입찰·dispatch·정산 최소기능을 검증한다.
minimum_data:
  - asset_identity_consent
  - telemetry_and_baseline
  - market_rule_and_bid
  - dispatch_and_meter
success_metrics:
  - onboarded_controllable_capacity
  - forecast_and_dispatch_accuracy
  - settlement_completion
  - unit_economics
```

#### `APP-ENS-022` — Renewable fleet O&M

```yaml
problem_statement: >
  다수 발전자산의 alarm·영상·정비·부품을 통합해 발전손실 기준으로 작업 우선순위를 정한다.
minimum_data:
  - scada_alarm_weather
  - inspection_image
  - cmms_parts_crew
  - expected_generation_and_price
success_metrics:
  - recovered_MWh
  - MTTR
  - first_time_fix
  - avoided_visit
```

#### `APP-ENS-023` — Parking/fleet smart charging

```yaml
problem_statement: >
  제한된 부지전력 안에서 차량별 출발시간·필요에너지·우선순위를 반영해 충전전력을 배분한다.
minimum_data:
  - charger_status
  - session_vehicle_need_departure
  - building_load_and_limit
  - tariff_and_payment
success_metrics:
  - departure_target_success
  - charger_utilization
  - peak_and_upgrade_avoidance
  - customer_waiting
```

#### `APP-ENS-024` — Charging site BESS integration

```yaml
problem_statement: >
  충전수요·건물부하·계통제약을 ESS로 보완해 증설비용·피크비용과 서비스 품질을 함께 최적화한다.
minimum_data:
  - all_APP_ENS_023_data
  - battery_soc_soh_cost
  - solar_optional
  - grid_upgrade_cost_and_timeline
success_metrics:
  - net_present_cost
  - delayed_or_avoided_upgrade
  - charging_success
  - battery_safety_and_life
```

#### `APP-ENS-025` — CCS chain-of-custody MRV

```yaml
problem_statement: >
  포집·압축·운송·주입·저장 단계의 CO2 양과 품질을 추적해 감축·저장 주장을 검증한다.
minimum_data:
  - calibrated_meter_and_lab
  - custody_transfer
  - transport_and_injection
  - reservoir_monitoring
  - baseline_boundary_emission_factor
success_metrics:
  - mass_balance_reconciliation
  - data_completeness
  - verification_time
  - anomaly_and_leak_response
```

---
