---
id: skes-d06-0-domain-boundary
title: Domain Boundary
summary: SK이노베이션 E&S의 LNG·전력·도시가스·재생에너지·ESS·수소 등 에너지 자산 전 단계에서 운영 프로세스·KPI·손실 포인트·데이터 요구사항을 정의하는 도메인 경계 설정 문서.
tags: [d06, process, core-candidate, schema, table, "xref:d02", "xref:d03", "xref:d04", "xref:d05"]
keywords: [LNG, 에너지 운영, KPI, 프로세스 구조화, 도시가스, ESS, 운전 데이터, 손실점, 재생에너지, 수소]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001, ORG-SKI-LEGAL-000001]
priority: critical
domain: D06
section: 0
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1644
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# SK이노베이션 E&S AI Knowledge Database

## D06. Energy Process & Operations｜에너지 공정·운영 프로세스

**Version 1.0 / 기준일: 2026년 8월 5일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Parent after merger: `ORG-SKI-LEGAL-000001`
- Source namespace: `SRC-ENS-D06-*`
- Process namespace: `PROC-ENS-D06-*`
- Equipment-class namespace: `EQC-ENS-D06-*`
- Process-event namespace: `EVT-ENS-D06-*`
- Failure-mode namespace: `FM-ENS-D06-*`
- KPI namespace: `KPI-ENS-D06-*`
- O/I Seed namespace: `SEED-ENS-D06-*`
- Inherited scope: D02 사업군, D03 29개 제품·솔루션/25개 적용 시나리오/52개 Seed, D04 61개 기술, D05 15개 연구프로그램/15개 표적 특허패밀리/24개 Seed

---

# 0. Domain Boundary

## 0.1 목적

D06은 SK이노베이션 E&S의 에너지 자산이 실제로 어떻게 계획·운전·감시·정비되고, 그 과정에서 어떤 데이터와 병목이 발생하는지를 O/I 과제 생성에 사용할 수 있는 수준으로 구조화한다. 제조기업의 D06이 원료에서 완제품까지의 생산 흐름을 다룬다면, E&S D06은 다음의 물리·상업 흐름을 동시에 다룬다.

1. 천연가스 생산·액화·해상운송·LNG 터미널·기화·송출
2. LNG 연료조달·복합화력·열병합·전력 및 열 판매
3. 도시가스 수급·정압·배관·안전·계량·고객서비스
4. 태양광·육상/해상풍력의 예측·발전·정비·PPA 정산
5. ESS의 시장입찰·충방전·열화·안전 및 EV 충전 부하관리
6. 부생수소 정제·액화·저장·탱크로리·충전소 공급
7. 계획·실증 단계 저탄소 LNG·블루수소·CCS의 포집·수송·저장·MRV
8. 자산군 전체의 통합 계획, 운전데이터, SHE, 정비, 변경관리

## 0.2 D06의 핵심 질문

```yaml
primary_questions:
  - 사업별 end_to_end process와 운영책임 경계는 무엇인가
  - 각 단계의 input output equipment control variable은 무엇인가
  - 수익과 안전에 직접 영향을 주는 KPI와 loss point는 무엇인가
  - 이상징후가 어느 센서 이벤트 작업이력 계약데이터에 남는가
  - 설비 고장 수요오차 가격오차 품질오차가 어떤 downstream 영향으로 전파되는가
  - 외부 솔루션으로 개선 가능한 문제와 내부 고유 운전영역은 무엇인가
  - PoC에 필요한 최소 데이터와 안전 cyber 승인 gate는 무엇인가
  - 공개자료로 확인된 E&S 사실과 산업 baseline을 어떻게 분리하는가
```

## 0.3 포함 범위

```yaml
included:
  LNG_upstream_midstream:
    - production nomination and gas conditioning interface
    - liquefaction entitlement and cargo planning
    - carrier voyage and cargo condition monitoring
    - terminal unloading storage BOG regasification sendout
  power_and_heat:
    - fuel nomination and dispatch planning
    - combined_cycle startup loading combustion steam cycle shutdown
    - CHP heat demand and network dispatch interface
    - emissions water chemistry and condition maintenance
  city_gas:
    - receipt odorization pressure regulation distribution
    - RBMS patrol drone leak survey integrity maintenance
    - metering billing customer move emergency response
  renewable_and_PPA:
    - forecasting generation control curtailment O&M
    - meter REC PPA allocation settlement
  energy_solution:
    - ESS bidding dispatch SOC SOH thermal safety
    - DERMS VPP aggregation where operational status is confirmed or planned
    - EV charging dynamic load management and availability
  hydrogen:
    - byproduct hydrogen intake purification liquefaction storage loading
    - tanker delivery station receiving and loss management
  CCS:
    - capture conditioning compression transport injection MRV as planned_or_pilot baseline
  common_operations:
    - control room alarm work order permit to work change management
    - asset performance energy water emissions and data lineage
```

## 0.4 후속 도메인으로 이관

| Domain | 이관 항목 | D06에서 유지하는 연결키 |
|---|---|---|
| `D07` | 사업장·플랜트·터미널·발전소·배관망·용량·가동 이벤트 | `asset_id`, `site_id`, `process_id` |
| `D08` | LNG 공급계약·원산지·선박·조달·재고·벤더 | `material_flow_id`, `supplier_id` |
| `D09` | 발전·열·도시가스·PPA·ESS 고객 및 계약수요 | `customer_segment_id`, `contract_id` |
| `D10` | 전력·가스·REC·보조서비스 시장 및 경쟁 | `market_id`, `bid_event_id` |
| `D11` | 연료비·효율·변동비·정비비·손실·마진 | `cost_driver_id`, `KPI_id` |
| `D12` | 증설·대정비·디지털 투자·CAPEX | `investment_event_id` |
| `D13` | JV·운영권·PPA·터미널 사용권·OEM 계약 | `rights_id`, `contract_id` |
| `D14` | 가스·전력·수소·CCS 규제와 허가 | `permit_id`, `compliance_record_id` |
| `D15` | 전사 위험·SHE·OT cyber·BCP·비상대응 | `risk_id`, `incident_id`, `barrier_id` |
| `D16` | 외부 솔루션·스타트업·벤더 | `provider_id`, `capability_id` |
| `D17` | 최종 O/I 과제·우선순위·PoC | `SEED-ENS-D06-*` |

---
