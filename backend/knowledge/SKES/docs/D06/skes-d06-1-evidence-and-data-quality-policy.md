---
id: skes-d06-1-evidence-and-data-quality-policy
title: Evidence and Data-Quality Policy
summary: "E&S 사업 정보의 신뢰도를 E1~E5로 분류하고, 사업별 비공개 데이터 범위를 정의하며, 공개 수치를 실제 운영값으로 오용하지 않기 위한 10가지 강제 규칙을 제시하는 데이터 품질 정책."
tags: [d06, process, schema, table]
keywords: [증거수준, 신뢰도 분류, 비공개 데이터, 가드레일, LNG, 발전소, 도시가스, 재생에너지, CCS, 운영값]
related: []
priority: normal
domain: D06
section: 1
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1148
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 1. Evidence and Data-Quality Policy

## 1.1 증거수준

| Code | 의미 | 허용되는 저장 내용 | 금지되는 확대해석 |
|---|---|---|---|
| `E1_DIRECT_OFFICIAL` | E&S·SK이노베이션 공식 자료 | 사업 존재, 자산 역할, 공개 운영방식, 공개 실적 | 미공개 세부 운전값 추정 |
| `E2_PARTNER_OFFICIAL` | JV·운영사·기술파트너 공식 자료 | 파트너 관점의 공정·역할·기술 | E&S의 직접 보유·직접 운전으로 전환 |
| `E3_REGULATOR_STANDARD` | 정부·규제기관·국립연구소 | 산업 표준 공정, 안전·MRV·운영 변수 | E&S 현장에 실제 적용됐다고 단정 |
| `E4_ANALYST_PROCESS_MODEL` | E1~E3를 연결한 분석모델 | 데이터 요청안, 원인경로, O/I 가설 | 사실·실적·설비구성으로 표현 |
| `E5_INTERNAL_REQUIRED` | 내부자료가 있어야 확정 | 태그, setpoint, OEE, 고장률, 효율, vendor | 공개자료만으로 값 생성 |

## 1.2 공개되지 않은 핵심 필드

```yaml
not_publicly_disclosed:
  LNG:
    - cargo_schedule_and_inventory_by_day
    - tank_level_and_BOG_rate
    - compressor_train_configuration
    - regasifier_type_and_actual_efficiency
    - sendout_pressure_and_linepack
  power:
    - unit_heat_rate_and_degradation_curve
    - startup_time_fuel_and_emissions_by_mode
    - equivalent_operating_hours_and_forced_outage_rate
    - OEM_long_term_service_agreement_scope
    - control_logic_setpoints
  city_gas:
    - pipe_length_material_age_and_GIS_geometry
    - regulator_station_sensor_coverage
    - leak_history_and_risk_score_weights
    - meter_error_and_unaccounted_for_gas
  renewable:
    - plant_level_availability_curtailment_and_loss_tree
    - forecast_error_by_horizon
    - turbine_or_inverter_alarm_history
  ESS_EV:
    - cell_module_pack_vendor_and_warranty_terms
    - SOC_SOH_estimator_and_dispatch_constraints
    - charger_session_and_building_limit_data
  hydrogen:
    - liquefaction_process_vendor_and_train_configuration
    - specific_energy_consumption_purity_and_BOR
    - tanker_turnaround_and_delivery_loss
  CCS:
    - actual_capture_rate_solvent_recipe_and_energy_penalty
    - pipeline_specification_injection_profile_and_MRV_plan
```

## 1.3 Hard Guardrails

1. Boryeong LNG terminal의 공개 연간 처리능력 350만 톤은 실제 처리량이나 E&S 지분귀속량으로 사용하지 않는다.
2. Freeport 액화설비 연 220만 톤 사용계약은 실제 월별 생산·선적량으로 사용하지 않는다.
3. Barossa 약 130만 톤/년 도입 설명, Woodford 약 110만 톤/년 생산 설명, Tangguh 50~60만 톤/년 도입 설명은 서로 다른 권리·시점·물량 개념으로 분리한다.
4. 발전소 상업운전 연도는 운영 존재를 뜻할 뿐, 현재 설비효율·가동률·잔존수명을 뜻하지 않는다.
5. 도시가스 7개 자회사·8개 권역·약 510만 가구·2023년 54억㎥는 기준시점이 있는 공개 포트폴리오 수치이며 현 실시간 운영값이 아니다.
6. 재생에너지 3.5GW와 약 5GW pipeline은 운영·개발·계획 상태를 반드시 분리한다.
7. 인천 액화수소플랜트 연 3만 톤은 설계/명목 능력이고 실제 생산량·수율·가동률이 아니다.
8. VPP는 공식 페이지에서 검토 중으로 표현되므로 상용 대규모 운영을 가정하지 않는다.
9. CCS·블루수소는 계획·실증·개발 단계와 상용운전을 분리한다.
10. 산업 baseline의 수치·공정·설비를 E&S 실제 공정값으로 저장하지 않는다.

---
