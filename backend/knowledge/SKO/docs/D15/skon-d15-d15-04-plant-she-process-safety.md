---
id: skon-d15-d15-04-plant-she-process-safety
title: Plant SHE & Process Safety
summary: 배터리 제조 전 공정에서 발생하는 화학·전기·열 위험 요소별로 예방 및 탐지 방어책을 정리한 Hazard Map과 리스크 관리 지표.
tags: [d15, risk, schema, table]
keywords: [배터리 제조 공정, 위험지도, 배리어, 열폭주, 리튬이온, 선행지표, Bow-tie, 저빈도 고중대 사건, 배터리 제조, Hazard Map, 공정 리스크, 방어 체계, LOTO, Leading indicator, Li-ion, Near miss, 변경관리]
related: []
priority: normal
domain: D15
section: D15-04
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 830
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-04 Plant SHE & Process Safety

### 1. Battery Manufacturing Hazard Map

| 공정/영역 | 주요 Hazard | 예방 Barrier | 탐지·완화 Barrier |
|---|---|---|---|
| 혼합·코팅·건조 | NMP·분진·정전기·가연성 Vapor | 밀폐·환기·접지·농도/점화원 관리 | Gas detection·Interlock·PPE·비상배기 |
| 압연·절단·적층 | 협착·절단·금속이물·분진 | Guard·LOTO·집진·이물관리 | Vision·Particle monitoring·Near miss |
| 전해액 주입 | 가연성·유해물질·누출 | Closed transfer·방폭·접지 | Leak·VOC detection·Spill response |
| Formation·Aging | 고전압·발열·Gas·열폭주 | Channel isolation·전류/온도 제한 | Thermal/gas monitoring·자동격리·소화/냉각 |
| Module·Pack | 중량물·용접·HV·냉각누설 | Robot cell·HV interlock·Torque/Weld control | EoL isolation·Leak test·Arc/fire response |
| 창고·물류 | SOC·충격·단락·손상품 혼입 | SOC/격리 기준·포장·구획 | 온도·연기·Gas 감지·Quarantine |
| 폐기·Rework | Stranded energy·손상 Cell·재점화 | 방전·상태표시·도구·격리 | 열감시·수조/냉각 등 승인절차·재점화 감시 |

OSHA는 Li-ion Battery의 제조·사용·비상대응·폐기·재활용에서 화학물질, 저장된 전기에너지, 열폭주로 인한 화재·폭발·화학 부산물을 Hazard로 제시한다. 이는 사업장별 위험성평가와 현지법을 대체하지 않지만 D15 Hazard Ontology의 공식 기준점이다. ([OSHA 2025 Fact Sheet](https://www.osha.gov/sites/default/files/publications/OSHA4480.pdf))

### 2. Bow-tie 기록

```yaml
bow_tie_event:
  top_event: control_of_energy_or_hazard_is_lost
  threats: []
  preventive_barriers:
    - barrier_id: null
      independent: null
      health_state: HEALTHY|DEGRADED|FAILED|UNKNOWN
  escalation_factors: []
  consequences: []
  mitigative_barriers: []
  emergency_actions_RTO: []
  evidence_and_last_test: []
  residual_risk_owner: null
```

### 3. Leading Indicator

- Barrier Bypass·Impairment 시간과 승인상태
- 고위험 작업 Permit·LOTO·Confined-space·Hot-work Audit 불일치
- Contractor Training·Competence·Supervision Gap
- High-potential Near Miss와 반복 Unsafe Condition
- Safety-critical Maintenance Overdue와 Spare 부족
- Gas·Thermal·Electrical Sensor Coverage와 Calibration Overdue
- Emergency Drill의 Scenario Coverage·의사결정시간·후속조치 종결률
- 변경관리(MOC) 미완료 상태에서의 생산·Recipe·Software 변경

재해율 같은 Lagging Indicator만으로는 저빈도·고중대 위험의 Barrier 약화를 조기에 보기 어렵다.

---
