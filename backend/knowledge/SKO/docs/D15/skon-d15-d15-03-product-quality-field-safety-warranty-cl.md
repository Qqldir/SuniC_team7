---
id: skon-d15-d15-03-product-quality-field-safety-warranty-cl
title: "Product Quality, Field Safety & Warranty Closed Loop"
summary: "배터리 제품의 결함을 공급자에서 필드까지 추적하고, 다양한 신호를 융합하여 영향 범위를 파악·리콜하며, CAPA 효과를 검증하는 폐쇄 루프 품질 관리 시스템."
tags: [d15, risk, schema, table]
keywords: [영향범위, 신호결합, CAPA, 계보추적, 텔레메트리, 원인분석, 리콜, 반품분석, NHTSA, 포함논리, Genealogy, BMS·Telemetry, 신호 융합, Complaint, Warranty Claim, Affected Population, Root Cause, Recall]
related: []
priority: normal
domain: D15
section: D15-03
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 1018
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-03 Product Quality, Field Safety & Warranty Closed Loop

### 1. End-to-end Quality Thread

```text
Supplier Material Lot / Certificate
→ Mixing Batch / Electrode Roll Coordinate
→ Cell Serial / Formation / Aging / Inspection
→ Module / Pack Serial / BMS Software-Calibrations
→ Customer Program / Vehicle VIN or ESS Site
→ Operating Context / SOC / Temperature / Charge Pattern
→ Complaint / DTC / Telemetry / Warranty / Field Report
→ Returned-part Quarantine / CT·X-ray·Teardown·Chemical Analysis
→ Defect Hypothesis / Affected Population / Containment
→ CAPA / Process or Design Change / Customer Approval
→ Field Remedy / Recall / Completion / Recurrence Monitoring
```

### 2. Affected Population Engine

```yaml
affected_population:
  trigger_signal_and_detection_time: null
  suspected_failure_mode: null
  cell_material_process_and_equipment_windows: []
  genealogy_keys:
    material_lot: []
    electrode_roll_coordinates: []
    cell_serials: []
    module_pack_serials: []
    vehicle_VIN_or_ESS_asset_IDs: []
  exposure_conditions:
    SOC_temperature_charge_discharge_profile: []
    storage_transport_damage_or_service_history: []
  inclusion_logic: null
  exclusion_logic_and_evidence: null
  potentially_affected_count: null
  confirmed_defective_count: null
  population_denominator_and_period: null
  confidence_and_unknown_tail: null
  quality_legal_customer_reviewers: []
```

리콜범위 최소화는 목표가 될 수 있지만 `작은 Population` 자체가 KPI가 되어서는 안 된다. 목표는 **증거로 포함·제외를 재현하고 Unknown Tail을 관리하는 것**이다.

### 3. Signal Fusion

| Signal | 장점 | 단독 사용 위험 | 결합 대상 |
|---|---|---|---|
| Inline·EoL 검사 | 출하 전 빠른 통제 | Field 조건과 다른 False Negative | Genealogy·환경·BMS |
| BMS·DTC·Telemetry | 운행 중 조기징후 | OEM 접근권한·Sampling·Calibration 차이 | Complaint·Warranty·기온·사용패턴 |
| Complaint | 고객경험을 빠르게 포착 | 중복·주관·노출량 미반영 | VIN·판매량·정비기록 |
| Warranty Claim | 비용·부품교환과 연결 | Coding 지연·No Trouble Found | Returned part·Dealer text |
| Field Report | 정성적 증거가 풍부 | 언어·보고편향 | NLP 분류·전문가 Review |
| Return Analysis | 물리적 원인 검증 | 표본편향·운송 후 손상 | 동일 Population 정상품 대조 |
| 외부 Recall·사고 | 유사 Failure Mode 조기경보 | 다른 설계·공정의 오적용 | BOM·공정·Supplier 유사성 Graph |

NHTSA EWR는 생산량, 사망·부상, 재산피해, Complaint, Warranty와 Field Report를 서로 다른 데이터형으로 다룬다. D15도 이를 하나의 `Incident Count`로 합치지 않는다. ([NHTSA EWR](https://www.nhtsa.gov/vehicle-manufacturers/early-warning-reporting))

### 4. CAPA 효과검증

```text
Containment 완료 ≠ Root Cause 확정
Root Cause 확정 ≠ CAPA 설치
CAPA 설치 ≠ 재발방지 검증
재발방지 검증 ≠ 유사 공장·제품 수평전개 완료
```

CAPA는 변경된 공정·설계·검사로 동일 Failure Mode가 감소했는지, 새로운 Failure Mode·Scrap·Throughput Loss를 만들지 않았는지, 적용대상 모든 공장과 공급사에서 유지되는지를 확인해야 종결한다.

---
