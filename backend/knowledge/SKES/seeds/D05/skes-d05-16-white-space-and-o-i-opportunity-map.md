---
id: skes-d05-16-white-space-and-o-i-opportunity-map
title: White Space and O/I Opportunity Map
summary: "E&S 사업 전 영역(LNG, 수소, 도시가스, ESS 등)의 기술 혁신 공백과 그를 채우기 위한 구체적 개발 과제를 매핑한 기술 로드맵."
tags: [d05, rnd, oi-seed, schema, table]
keywords: [LNG, 수소, 도시가스, ESS, 신재생에너지, 기술 공백, 개발 과제, 혁신 로드맵, 개방형 혁신]
related: [WS-ENS-001, WS-ENS-002, WS-ENS-003, WS-ENS-004, WS-ENS-005, WS-ENS-006, WS-ENS-007, WS-ENS-008, WS-ENS-009, WS-ENS-010, WS-ENS-011, WS-ENS-012, WS-ENS-013, WS-ENS-014, SEED-ENS-D05-001, SEED-ENS-D05-002, SEED-ENS-D05-003, SEED-ENS-D05-004, SEED-ENS-D05-005, SEED-ENS-D05-006, SEED-ENS-D05-007, SEED-ENS-D05-008, SEED-ENS-D05-009, SEED-ENS-D05-010]
priority: normal
domain: D05
section: 16
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1562
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 16. White Space and O/I Opportunity Map

## 16.1 White Space

| White-space ID | 영역 | 현재 공개 IP | 공백 | O/I 방향 |
|---|---|---|---|---|
| `WS-ENS-001` | LNG 선박–터미널–발전 | 직접IP 미확인 | 통합 일정·재고·가격 | hybrid optimizer |
| `WS-ENS-002` | LNG BOG | 직접IP 미확인 | 예측·회수·운전 | physics+AI twin |
| `WS-ENS-003` | 발전+포집 | 파트너 기술 | 통합 열·증기·부하 | site integration IP |
| `WS-ENS-004` | 도시가스 RBMS | 전통 장치IP | 시계열·GIS·굴착 위험 | explainable risk model |
| `WS-ENS-005` | AMI | 계량·통신 특허 | 이상·품질·보안 | modern data platform |
| `WS-ENS-006` | 재생 O&M | 직접IP 미확인 | 결함–작업–발전손실 | loss attribution |
| `WS-ENS-007` | PPA 정산 | 직접IP 미확인 | 계약·계량·인증서 lineage | exception automation |
| `WS-ENS-008` | 액화수소 BOG | 공개IP 제한 | 극저온 손실·재액화 | advisory optimizer |
| `WS-ENS-009` | 수소 물류 | 공개IP 미확인 | 생산–재고–배송–충전 | supply-chain twin |
| `WS-ENS-010` | ESS bidding | KCE proprietary | 열화·보증·다시장 | cross-market engine |
| `WS-ENS-011` | DERMS/VPP | 공개IP Gap | 등록·제어·정산 | minimum viable platform |
| `WS-ENS-012` | EV charging+BESS | EverCharge 특허 강함 | 공동최적화·fleet SLA | affiliate combination |
| `WS-ENS-013` | CCS MRV | 포집특허 중심 | custody·mass balance·lineage | assurance data layer |
| `WS-ENS-014` | 다법인 기술이전 | 분산 IP | 관계사 재사용권 | internal license framework |

## 16.2 D05 O/I Seeds

| Seed ID | 과제 | 활용 자산 | 필요한 외부역량 | IP 설계 핵심 | 우선도 |
|---|---|---|---|---|---|
| `SEED-ENS-D05-001` | LNG선–터미널 일정 최적화 | 운영·AIS·재고 | OR solver | 알고리즘+상업데이터 | P0 |
| `SEED-ENS-D05-002` | BOG physics-AI twin | 탱크·기상·입출고 | 공정AI | 모델·튜닝·site data | P0 |
| `SEED-ENS-D05-003` | 발전 성능–포집 에너지 통합 | 발전OT·포집 | Honeywell/OEM | 배경IP·개량권 | P0 |
| `SEED-ENS-D05-004` | CO₂ 흡수제 상태·고체화 예측 | CCS-001/002 | 센서·AI | 특허개량·운전recipe | P0 |
| `SEED-ENS-D05-005` | 도시가스 RBMS 2.0 | 배관·사고·GIS | graph AI | 관계사 공동모델 | P0 |
| `SEED-ENS-D05-006` | 누출 다중센서 융합 | 센서·드론 | edge AI | 데이터·알람로직 | P0 |
| `SEED-ENS-D05-007` | AMI 품질·열량·과금 lineage | CG-003/004 | data quality | 기존특허+신규SW | P0 |
| `SEED-ENS-D05-008` | 배관 응급복구 로봇화 | CG-006 | robotics | 공동개량·안전검증 | P1 |
| `SEED-ENS-D05-009` | PPA 정산 exception engine | 계약·계량 | rules/AI | 고객데이터·정산로직 | P0 |
| `SEED-ENS-D05-010` | 해상풍력 O&M weather window | SCADA·기상 | offshore optimizer | 프로젝트 재사용권 | P1 |
| `SEED-ENS-D05-011` | 액화수소 공정 효율 advisor | 플랜트 OT | cryogenic AI | OEM·공정노하우 | P0 |
| `SEED-ENS-D05-012` | 수소 BOG 회수경로 최적화 | 저장·수요 | process integration | 개량발명·안전 | P0 |
| `SEED-ENS-D05-013` | 수소 생산–물류–충전 twin | 재고·차량·수요 | routing/twin | 다자 데이터권리 | P0 |
| `SEED-ENS-D05-014` | MarketCapture 열화비용 내재화 | KCE SW·BMS | degradation model | 코드·모델·vendor data | P0 |
| `SEED-ENS-D05-015` | KCE 신규시장 규칙 compiler | MarketCapture | market rules NLP | 파생코드·시장데이터 | P1 |
| `SEED-ENS-D05-016` | SmartPower+BESS 통합제어 | EverCharge+ESS | site EMS | 특허군·신규개량 | P0 |
| `SEED-ENS-D05-017` | Fleet departure-SLA charging | SmartPower | optimization | 고객·차량데이터 | P0 |
| `SEED-ENS-D05-018` | DERMS 자산등록·프로토콜 adapter | Ensolve 후보 | interoperability | connector IP·표준 | P1 |
| `SEED-ENS-D05-019` | VPP 성과측정·정산 | PPA·DER | M&V platform | 데이터·방법론 | P1 |
| `SEED-ENS-D05-020` | CCS MRV evidence graph | project data | lineage/assurance | 프로젝트·검증자 권리 | P0 |
| `SEED-ENS-D05-021` | 다법인 IP·데이터 재사용 카탈로그 | 전 자회사 | IP management | internal license | P0 |
| `SEED-ENS-D05-022` | 발명·코드·모델 provenance | R&D records | DevSecOps | inventorship evidence | P1 |
| `SEED-ENS-D05-023` | 안전 AI 검증 sandbox | OT·사고데이터 | simulation | 책임·테스트데이터 | P0 |
| `SEED-ENS-D05-024` | 파트너 기술 계약 clause copilot | 계약 metadata | legal tech | 기밀·human approval | P1 |

## 16.3 Seed Selection Rule

```yaml
priority_score:
  business_pain: 25
  data_readiness: 20
  owned_or_accessible_IP: 15
  measurable_KPI: 15
  cross_asset_reuse: 10
  safety_and_regulatory_feasibility: 10
  partner_availability: 5
penalty:
  unclear_data_rights: -20
  safety_closed_loop_without_gate: -30
  partner_core_IP_without_license_path: -20
  planned_business_without_asset_owner: -15
```

---
