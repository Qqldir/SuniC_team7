---
id: skes-d05-10-initial-patent-family-master
title: Initial Patent Family Master
summary: "SK E&S 특허 포트폴리오를 기술축(CCS·도시가스·EV충전)별로 정리한 마스터 테이블로, 각 특허 가족의 ID·우선권·상태를 조회할 수 있다."
tags: [d05, rnd, schema, table]
keywords: [특허 포트폴리오, CCS, 도시가스, EV충전, 탄소포집, Patent family, 우선권, 권리주체, 기술축, 흡수제]
related: [PF-ENS-CCS-001, PF-ENS-CCS-002, PF-ENS-CG-001, PF-ENS-CG-002, PF-ENS-CG-003, PF-ENS-CG-004, PF-ENS-CG-005, PF-ENS-CG-006, PF-ENS-CG-007, PF-ENS-CG-008, PF-ENS-EVC-001, PF-ENS-EVC-002, PF-ENS-EVC-003, PF-ENS-EVC-004, PF-ENS-EVC-005]
priority: normal
domain: D05
section: 10
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 2914
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 10. Initial Patent Family Master

## 10.1 Portfolio Summary

| Family ID | 대표 제목 | Priority | 권리주체 | 상태(공개DB) | 기술축 |
|---|---|---:|---|---|---|
| `PF-ENS-CCS-001` | 폐열을 이용한 흡수제 고체화 방지 | 2022-12-06 | SK E&S | KR 등록·active 표시 | CCS 열통합 |
| `PF-ENS-CCS-002` | CO₂를 이용한 흡수제 고체화 방지 | 2022-12-06 | SK E&S | KR 등록·active 표시 | CCS 흡수제 |
| `PF-ENS-CG-001` | 정압기 압력조절 시스템 | 2011-09-14 | SK E&S+부산도시가스 | PCT ceased 표시, 국가단계 별도 | 정압 |
| `PF-ENS-CG-002` | 온압 보정기 검사 장치·시스템·방법 | 2012-01-20 | SK E&S | PCT ceased 표시, 국가단계 별도 | 계량검사 |
| `PF-ENS-CG-003` | 무선통신·온압보정 자동검침 | 2014-06-10 | SK E&S+도담에너시스 | 국가별 확인 필요 | AMI |
| `PF-ENS-CG-004` | 열량변화 대응 가스부피 환산관리 | 2014-09-30 | SK E&S+도담+충청 | 국가별 확인 필요 | 계량·열량 |
| `PF-ENS-CG-005` | 도시가스 정압기용 압력설정장치 | 2009-08-11 | 충청에너지서비스 | KR active 표시 | 정압정비 |
| `PF-ENS-CG-006` | 가스공급관로 응급보수 | 2019-07-16 | 부산도시가스+파트너 | KR 등록 표시 | 배관안전 |
| `PF-ENS-CG-007` | 가스계량기 지지대 | 2010-03-25 | 부산도시가스 | KR 등록 표시 | 계량설치 |
| `PF-ENS-CG-008` | 밸브 유지관리 보수장치·방법 | 2012-05-31 | 부산도시가스 | KR 등록 표시 | 밸브정비 |
| `PF-ENS-EVC-001` | Smart energy distribution for EV charging | 2014-03-20 | EverCharge | US active 표시·다수 계속출원 | SmartPower |
| `PF-ENS-EVC-002` | Smart load management apparatus/system | 2018-03-14 | EverCharge | US active 표시 | 동적부하 |
| `PF-ENS-EVC-003` | EV electricity distribution/monitoring/billing | 2009-03-18 | EverCharge | US 등록 | 충전·과금 |
| `PF-ENS-EVC-004` | EVSE internal current overage protection | 2015-09-25 계열 | EverCharge | US active 표시 | 보호회로 |
| `PF-ENS-EVC-005` | Mixed-level EVSE | 2015-09-25 계열 | EverCharge | US 등록·계속출원 | 다중충전 |

## 10.2 Detailed Patent Cards

### `PF-ENS-CCS-001`

```yaml
family_id: PF-ENS-CCS-001
title_ko: 폐열을 이용한 흡수제 고체화 방지 시스템
priority_application: KR1020220168560A
earliest_priority: 2022-12-06
publication: KR20240084103A
grant: KR102815664B1
grant_date_reported: 2025-06-02
inventors: [김순호, 김정환, 오세영]
applicant_at_filing: SK_E&S_Co_Ltd
ownership_class: OWNED_DIRECT_HISTORICAL
legal_status_reported: ACTIVE
technical_problem:
  - amine_absorbent_can_solidify_in_storage_tank
  - separate_heater_increases_energy_and_complexity
solution_elements:
  - absorber_and_stripper
  - cooler_in_temperature_control_line
  - solvent_storage_tank
  - waste_heat_recovery_line_to_storage_tank
value_hypothesis:
  - prevent_solidification
  - reduce_auxiliary_heating_energy
  - improve_capture_process_availability
linked_tech: [TECH-ENS-CCS-01, TECH-ENS-PWR-03]
implementation_evidence: NOT_PUBLICLY_CONFIRMED
source_ids: [SRC-ENS-D05-0013]
```

### `PF-ENS-CCS-002`

```yaml
family_id: PF-ENS-CCS-002
title_ko: 이산화탄소를 이용한 흡수제 고체화 방지 시스템
priority_application: KR1020220168573A
earliest_priority: 2022-12-06
publication: KR20240084110A
grant: KR102815668B1
grant_date_reported: 2025-06-02
inventors: [김순호, 김정환, 오세영]
applicant_at_filing: SK_E&S_Co_Ltd
ownership_class: OWNED_DIRECT_HISTORICAL
legal_status_reported: ACTIVE
technical_problem:
  - stored_absorbent_solidification
solution_elements:
  - absorber_and_stripper
  - solvent_storage_tank
  - captured_CO2_supply_line_to_storage_tank
  - reduce_free_amine_concentration
linked_tech: [TECH-ENS-CCS-01]
implementation_evidence: NOT_PUBLICLY_CONFIRMED
source_ids: [SRC-ENS-D05-0014]
```

### `PF-ENS-CG-001`

```yaml
family_id: PF-ENS-CG-001
title_ko: 정압기 압력조절 시스템
representative_publication: WO2013039338A1
priority: 2011-09-14
applicants:
  - SK_E&S_Co_Ltd
  - Pusan_City_Gas_Co_Ltd
inventors:
  - 김종우
  - 송순섭
  - 이동찬
  - 이두홍
  - 김성태
  - 허영길
  - 김동준
  - 이용섭
ownership_class: CO_OWNED
PCT_status_reported: CEASED
national_stage_rule: VERIFY_SEPARATELY
linked_tech: [TECH-ENS-CG-01, TECH-ENS-CG-04]
implementation_evidence: NOT_PUBLICLY_CONFIRMED
source_ids: [SRC-ENS-D05-0015]
```

### `PF-ENS-CG-002`

```yaml
family_id: PF-ENS-CG-002
title_ko: 온압 보정기 검사 장치, 시스템 및 방법
representative_publication: WO2013108973A1
priority: 2012-01-20
applicant: SK_E&S_Co_Ltd
inventor: 양기모
ownership_class: OWNED_DIRECT_HISTORICAL
technical_problem:
  - portable_test_of_temperature_pressure_volume_corrector
linked_tech: [TECH-ENS-CG-05, TECH-ENS-CG-06]
PCT_status_reported: CEASED
national_stage_rule: VERIFY_SEPARATELY
source_ids: [SRC-ENS-D05-0016]
```

### `PF-ENS-CG-003`

```yaml
family_id: PF-ENS-CG-003
title_ko: 무선 통신 기능 및 온압 보정 기능을 갖는 자동 검침 장치
representative_publication: WO2015190625A1
priority: 2014-06-10
applicants:
  - SK_E&S_Co_Ltd
  - Dodam_Energy_Systems
inventors: [양기모, 최순진, 박찬호]
ownership_class: CO_OWNED
linked_tech: [TECH-ENS-CG-05, TECH-ENS-CG-06]
implementation_evidence: NOT_PUBLICLY_CONFIRMED
source_ids: [SRC-ENS-D05-0017]
```

### `PF-ENS-CG-004`

```yaml
family_id: PF-ENS-CG-004
title_ko: 도시가스 열량변화에 대응하는 가스부피 환산장치 관리 시스템 및 방법
representative_publication: WO2016052811A1
priority: 2014-09-30
applicants:
  - SK_E&S_Co_Ltd
  - Dodam_Energy_Systems
  - Chungcheong_Energy_Service
inventors: [최순진, 한상진, 김상우]
ownership_class: CO_OWNED
solution_elements:
  - gas_composition_analyzer
  - management_server
  - remote_metering_device
  - temperature_pressure_correction
  - customer_information_and_usage_database
  - authentication_and_data_validation
linked_tech: [TECH-ENS-CG-05, TECH-ENS-CG-07]
OI_relevance:
  - modern_AMI_data_platform
  - calorific_value_lineage
  - secure_device_identity
  - billing_anomaly_detection
source_ids: [SRC-ENS-D05-0018]
```

### `PF-ENS-CG-005`

```yaml
family_id: PF-ENS-CG-005
title_ko: 도시가스 정압기용 압력설정장치
grant: KR100981281B1
priority: 2009-08-11
applicant: Chungcheong_Energy_Service
ownership_class: AFFILIATE_OWNED
legal_status_reported: ACTIVE
linked_tech: [TECH-ENS-CG-01, TECH-ENS-CG-04]
source_ids: [SRC-ENS-D05-0020]
```

### `PF-ENS-CG-006`

```yaml
family_id: PF-ENS-CG-006
title_ko: 가스공급관로 응급 보수 장치 및 보수 방법
grant: KR102200861B1
priority: 2019-07-16
applicants:
  - Busan_City_Gas
  - MagSwitch_Technology_Korea
ownership_class: CO_OWNED_AFFILIATE
technical_value:
  - reduce_worker_direct_exposure
  - prevent_secondary_accident
linked_tech: [TECH-ENS-CG-01, TECH-ENS-CG-02, TECH-ENS-CG-03]
source_ids: [SRC-ENS-D05-0019]
```

### `PF-ENS-EVC-001`

```yaml
family_id: PF-ENS-EVC-001
title: Smart energy distribution methods and systems for electric vehicle charging
earliest_priority: 2014-03-20
representative_grant: US9685798B2
PCT: WO2015143250A1
selected_continuations:
  - US9362761B2
  - US10756549B1
  - US11316359B1
  - US12081055B1
inventors:
  - Jason_Appelbaum
  - Mario_Landau_Holdsworth
  - Amber_Case
assignee: EverCharge_Inc
ownership_class: AFFILIATE_OWNED
status_reported: ACTIVE
linked_tech: [TECH-ENS-EVERCHARGE-SMARTPOWER, TECH-ENS-EVC-03]
acquisition_timeline:
  priority_before_SK_acquisition: true
  implication: acquired_affiliate_IP_not_parent_originated_IP
source_ids: [SRC-ENS-D05-0021]
```

### `PF-ENS-EVC-002`

```yaml
family_id: PF-ENS-EVC-002
title: Smart load management apparatus and system for electric vehicle charging
priority: 2018-03-14
grant: US11091054B1
inventors:
  - John_Loren_Passmore
  - Jason_Appelbaum
assignee: EverCharge_Inc
ownership_class: AFFILIATE_OWNED
status_reported: ACTIVE
selected_related_filings:
  - US11211793B1
  - US11787304B1
  - US11728648B1
  - US12275308B1
claim_theme_preliminary:
  - dynamic_load_management
  - EVSE_control_based_on_power_values
  - network_capacity_response
linked_tech: [TECH-ENS-EVERCHARGE-SMARTPOWER, TECH-ENS-EVC-03]
source_ids: [SRC-ENS-D05-0022]
```

### `PF-ENS-EVC-003`

```yaml
family_id: PF-ENS-EVC-003
title: Method, system, and apparatus for distributing electricity to electric vehicles, monitoring the distribution thereof, and/or providing automated billing
priority: 2009-03-18
grant: US9751417B2
assignee: EverCharge_Inc
ownership_class: AFFILIATE_OWNED
linked_tech: [TECH-ENS-EVC-04, TECH-ENS-EVC-05]
source_ids: [SRC-ENS-D05-0023]
```

### `PF-ENS-EVC-004`

```yaml
family_id: PF-ENS-EVC-004
title: EVSE having internal current overage protection and associated charging methods
grant: US11046186B1
assignee: EverCharge_Inc
ownership_class: AFFILIATE_OWNED
linked_tech: [TECH-ENS-EVC-01, TECH-ENS-EVC-02]
source_ids: [SRC-ENS-D05-0024]
```

### `PF-ENS-EVC-005`

```yaml
family_id: PF-ENS-EVC-005
title: Mixed-level electric vehicle supply equipment and associated charging methods
grant: US10183586B1
assignee: EverCharge_Inc
ownership_class: AFFILIATE_OWNED
linked_tech: [TECH-ENS-EVC-01, TECH-ENS-EVC-02]
source_ids: [SRC-ENS-D05-0025]
```

## 10.3 Patent Count Guardrail

```yaml
counting_policy:
  invention_count: one_per_priority_family
  publication_count: separate_metric
  granted_active_count: official_register_refresh_required
  affiliate_count: separate_from_direct_E&S
  co_owned_count: separate_from_sole_owned
  pre_acquisition_IP: flagged
  continuation_divisional: linked_not_double_counted
current_initial_pack:
  direct_or_coowned_E&S_sample_families: 6
  city_gas_affiliate_sample_families: 4
  EverCharge_sample_families: 5
  completeness: INITIAL_TARGETED_LANDSCAPE_NOT_COMPLETE_PORTFOLIO
```

---
