---
id: skon-d16-d16-01-external-capability-data-model
title: External Capability Data Model
summary: "외부 솔루션·공급업체 평가를 위한 13개 엔터티, 10개 Provider 유형, 5단계 Evidence 등급(E0-E4), 의사결정 상태의 통합 데이터 스키마."
tags: [d16, ecosystem, schema, table]
keywords: [벤더 평가, 솔루션 선정, 파트너십 의사결정, Evidence Level, PoC, 기술 due-diligence, 상용화 검증, 위험 평가, Provider 유형, 관계 상태, 외부솔루션평가, 공급업체선정, Evidence등급, Provider유형, 의사결정프레임, Fit Assessment, Build/Buy/Partner, PainPoint, 상용화검증, 엔터티]
related: []
priority: normal
domain: D16
section: D16-01
source: SK온_D16_External_Solutions_Startups_Vendors_Open_Innovation_Ecosystem.md
breadcrumb: "SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem"
tokens: 1235
updated: 2026-08-03
---

> SK온 · D16 외부 솔루션·스타트업·벤더 생태계 · SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem

## D16-01 External Capability Data Model

### 1. 핵심 엔터티

| 엔터티 | 기본 키 | 최소 필드 |
|---|---|---|
| `PainPoint` | `pain_point_id + version` | Domain·Owner·Baseline·영향단위·원인확신 |
| `Capability` | `capability_id` | 해결기능·필수입력·산출·통제·표준 Interface |
| `Provider` | `provider_id` | 법인명·국가·유형·Status·Conflict·Due-diligence 상태 |
| `Solution` | `solution_id + version` | 기능·배포형태·지원지역·Data/OT 요구·상호운용성 |
| `Evidence` | `evidence_id` | 출처·발표주체·날짜·고객·단계·성과·검증상태 |
| `Relationship` | `relationship_id` | 당사자·구속력·범위·시작·종료·IP·데이터·상태 |
| `ReferenceDeployment` | `deployment_id` | 고객·Site·공정·Scale·운영기간·성과·Claim Owner |
| `FitAssessment` | `assessment_id + date` | 문제적합·기술·통합·보안·사업·재무·Conflict |
| `PoC` | `poc_id` | 가설·범위·Baseline·Control·기간·KPI·Stop/Scale Gate |
| `CommercialModel` | `commercial_model_id` | License·Usage·Outcome·Hardware·Service·Exit Cost |
| `Risk` | `partner_risk_id` | 기술·재무·Cyber·IP·Data·규제·공급·Lock-in·평판 |
| `Decision` | `decision_id + version` | Build/Buy/Partner/License/Invest/Observe·승인·근거 |

### 2. Provider 유형

```yaml
provider_type:
  ENTERPRISE_PLATFORM: 대규모 IT_OT_data_workflow 통합
  INDUSTRIAL_AUTOMATION: 제어기_센서_로봇_MES_PLCSimulation
  BATTERY_VERTICAL_SOFTWARE: 배터리 RnD_제조_운영 특화 분석
  INSPECTION_AND_SENSOR: Xray_CT_ultrasound_vision_EIS_sensor
  REGTECH_AND_TRACEABILITY: DPP_LCA_due_diligence_trade_tax
  RISK_AND_DECISION_TECH: 공급망_계약_CAPEX_portfolio_risk
  OT_CYBER_AND_SAFETY: CPS_asset_remote_access_anomaly_safety
  MATERIALS_AND_PROCESS_STARTUP: 소재_전해질_건식_차세대공정
  CIRCULARITY_AND_RECYCLING: 회수_진단_재사용_전처리_정제_재생소재
  RESEARCH_INSTITUTE_OR_CONSORTIUM: 시험_표준_공동연구_data_space
```

### 3. Evidence Level

| Level | 공개 증거 | 허용되는 해석 |
|---|---|---|
| `E0` | 출처 불명·2차 인용만 존재 | 후보 등록 금지 또는 확인대기 |
| `E1` | 공식 제품·기술 페이지 | Capability 주장 존재, 실제 고객성과 미확인 |
| `E2` | 명명된 MOU·파트너십·Pilot·Grant | 공동검토 또는 실증, 상용성과 미확정 |
| `E3` | 명명된 고객·Site의 상용/운영 배포 | 실제 운영 Reference 존재, 범위·성과 검증 필요 |
| `E4` | 생산제품·다사업장·반복배포·검증 가능한 운영성과 | 확산성 높은 Reference, SK온 재현성은 별도 검증 |

`E4`는 기업 전체가 우수하다는 등급이 아니라 **특정 Solution–Use Case 조합의 공개 증거 수준**이다.

### 4. 관계·의사결정 상태

```yaml
relationship_status:
  PUBLIC_TECHNOLOGY_ONLY: 제품_기술만 확인
  UNDER_SCOUTING: 비구속적 탐색
  NON_BINDING_MOU: MOU_공동검토
  PILOT_OR_VALIDATION: 제한된 실증_검증
  ACTIVE_IMPLEMENTATION: 설치_통합_적용 중
  COMMERCIAL_OPERATION: 유상 또는 생산운영 확인
  STRATEGIC_PARTNERSHIP: 복수 프로젝트_장기협력
  LICENSE_OR_TECH_TRANSFER: 사용권_기술이전
  JV_OR_EQUITY_RELATION: JV_투자_지분관계
  PAUSED_TERMINATED_OR_EXITED: 중단_종료_분리

decision_posture:
  BUILD_CORE: 핵심 차별화_데이터_IP를 내부 구축
  BUY_CONFIGURE: 표준기능을 구매 후 설정
  CO_DEVELOP: 내부 도메인지식과 외부기술을 공동개발
  LICENSE_TRANSFER: 기술_공정_IP를 조건부 도입
  STRATEGIC_PARTNER: 장기공동사업_공급망_시장개척
  INVEST_OPTION: 소수지분_우선권_옵션 확보
  OBSERVE_BENCHMARK: 직접도입 없이 추적
  NO_GO: 규제_안전_IP_Conflict_재무 위험으로 제외
```

---
