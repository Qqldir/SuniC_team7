---
id: skes-d03-part-3-application-customer-alternative-8
title: Part 3. Application·Customer·Alternative·Graph·Chunk 확장 — Expanded D03 O/I Opportunity Seed Master
summary: "SK이노베이션 E&S D03 제품의 기존 21개에서 24개로 확장된 애플리케이션별 비즈니스 기회·이슈 과제 45개 Seed를 필수 데이터, KPI, Gate 조건, 우선순위와 함께 정리한 기회발굴 매트릭스."
tags: [d03, product, oi-seed, schema, table]
keywords: [D03, O/I Opportunity, Seed Master, 애플리케이션 확장, 비즈니스 기회과제, KPI 지표, Gate 제약조건, 상태모니터링, 이상탐지, 에너지최적화]
related: [SEED-ENS-D03-022, SEED-ENS-D03-023, SEED-ENS-D03-024, SEED-ENS-D03-025, SEED-ENS-D03-026, SEED-ENS-D03-027, SEED-ENS-D03-028, SEED-ENS-D03-029, SEED-ENS-D03-030, SEED-ENS-D03-031, SEED-ENS-D03-032, SEED-ENS-D03-033, SEED-ENS-D03-034, SEED-ENS-D03-035, SEED-ENS-D03-036, SEED-ENS-D03-037, SEED-ENS-D03-038, SEED-ENS-D03-039, SEED-ENS-D03-040, SEED-ENS-D03-041, SEED-ENS-D03-042, SEED-ENS-D03-043, SEED-ENS-D03-044, SEED-ENS-D03-045]
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 3. Application·Customer·Alternative·Graph·Chunk 확장
tokens: 2288
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 3. Application·Customer·Alternative·Graph·Chunk 확장

## 27. Expanded D03 O/I Opportunity Seed Master

기존 21개 Seed를 유지하면서 대표기업급 탐색을 위해 24개를 추가한다. 아래 Seed는 모두 `OI_HYPOTHESIS`이며 내부 KPI·데이터·Sponsor 확인 전 실행과제가 아니다.

| Seed ID | Application | 문제 가설 | 최소 데이터 | KPI | Gate | Priority |
|---|---|---|---|---|---|---|
| `SEED-ENS-D03-022` | APP-001 | 계약·수요·가격·일정 시나리오가 분리돼 cargo 포트폴리오 비교가 느림 | 비식별 계약제약·수요·가격 | 긴급조달·재고위반 | 계약기밀·거래통제 | P0 |
| `SEED-ENS-D03-023` | APP-002 | AIS ETA와 터미널 일정의 불일치 | AIS·기상·berth·재고 | 대기시간·재계획 | 선박/터미널 데이터권리 | P0 |
| `SEED-ENS-D03-024` | APP-003 | BOG 예측이 하역·조성·send-out을 충분히 반영하지 못함 | 탱크·BOG·cargo·send-out | BOG·에너지 | 공정안전·OT | P0 |
| `SEED-ENS-D03-025` | APP-003 | 터미널 alarm·정비 우선순위가 경제영향과 분리 | alarm·trip·CMMS·손실 | downtime·MTTR | OT·라벨품질 | P0 |
| `SEED-ENS-D03-026` | APP-004 | 발전경제성 모델에 상태·열화·기동비 반영 부족 | 시장·연료·효율·상태 | 순마진·heat rate | 운전승인 | P0 |
| `SEED-ENS-D03-027` | APP-004 | 이상탐지 경보가 조치·작업지시로 연결되지 않음 | historian·alarm·CMMS | lead time·precision | OEM/안전 | P0 |
| `SEED-ENS-D03-028` | APP-005 | 전력·열·축열 계획이 분리 | 가격·열수요·축열·설비 | 연료·열위반 | 공급신뢰도 | P0 |
| `SEED-ENS-D03-029` | APP-006 | 권역·고객군 단기 가스수요 예측오차 | 송출·기상·달력·고객군 | MAPE·압력위반 | 집계·개인정보 | P0 |
| `SEED-ENS-D03-030` | APP-007 | 정적 RBMS가 최신 굴착·기상·민원을 늦게 반영 | GIS·점검·굴착·기상 | 위험탐지·점검수율 | 법정점검·설명 | P0 |
| `SEED-ENS-D03-031` | APP-008 | 무단/근접굴착 조기탐지 부족 | 허가·GIS·영상·출동 | 탐지시간·precision | 드론·영상보안 | P0 |
| `SEED-ENS-D03-032` | APP-009 | 자가검침 OCR의 계량기 유형·촬영환경 편차 | 이미지·유형·수정라벨 | exact accuracy | 개인정보 | P0 |
| `SEED-ENS-D03-033` | APP-010 | 전출입 기사배정과 고객시간창 최적화 부족 | 예약·주소·기사·작업시간 | 완료율·이동 | 노동·안전 | P0 |
| `SEED-ENS-D03-034` | APP-011 | 태양광 발전손실 원인분해가 수작업 | 기상·SCADA·정비·curtailment | unexplained loss | 자산별 데이터 | P0 |
| `SEED-ENS-D03-035` | APP-012 | 해상풍력 정비에 고장·파고·선박·인력 통합 부족 | 상태·기상·선박·부품 | downtime·vessel day | 해상안전 | P0 |
| `SEED-ENS-D03-036` | APP-013 | PPA 고객부하–자산매칭 시나리오 생성시간 | 부하·자산·가격·신용 | proposal cycle | 계약·신용 | P0 |
| `SEED-ENS-D03-037` | APP-014 | 계량·계약·시장·인증 대사 예외처리 부담 | meter·formula·price·certificate | 정산시간·오류 | 회계·법무 | P0 |
| `SEED-ENS-D03-038` | APP-015 | 액화수소 원료변동·전력·생산계획 통합 부족 | feed·process·power·order | kWh/kg·yield | 극저온안전 | P0 |
| `SEED-ENS-D03-039` | APP-015 | 극저온 회전기계 이상 조기경보 부족 | 진동·온도·trip·정비 | lead time·MTBF | OEM·안전 | P0 |
| `SEED-ENS-D03-040` | APP-016 | 생산·탱크로리·충전소 재고계획 분리 | 생산·재고·차량·수요 | stockout·km/kg | 위험물·운전 | P0 |
| `SEED-ENS-D03-041` | APP-017 | ESS 절감제어가 열화·생산제약 미반영 | 부하·요금·SOC/SOH·생산 | net saving | 배터리안전 | P0 |
| `SEED-ENS-D03-042` | APP-018 | 재생연계 ESS가 PPA·curtailment·열화 동시반영 부족 | 발전·제약·계약·SOH | recovered MWh·net value | 시장·안전 | P0 |
| `SEED-ENS-D03-043` | APP-019 | MarketCapture의 신규시장 이전 시 규칙·데이터 Gap | market rule·price·asset | time-to-market·regret | IP·규제 | P0 |
| `SEED-ENS-D03-044` | APP-019 | ESS fleet의 입찰·안전·정비 데이터 분리 | bid·dispatch·BMS·CMMS | revenue·availability | 사이버·안전 | P0 |
| `SEED-ENS-D03-045` | APP-020 | DER 자산 데이터 모델·통신규격 불일치 | topology·telemetry·protocol | 연동시간·coverage | 사이버·제어권한 | P1 |
| `SEED-ENS-D03-046` | APP-021 | VPP 자원등록·baseline·정산 최소기능 미검증 | 자원·계량·시장·정산 | controllable MW·unit economics | 동의·규제 | P1 |
| `SEED-ENS-D03-047` | APP-022 | SCADA·영상·CMMS가 연결되지 않아 발전손실 기반 우선순위 부족 | SCADA·image·work order | recovered MWh·MTTR | 드론·데이터권리 | P0 |
| `SEED-ENS-D03-048` | APP-023 | 주차·충전·건물부하가 분리 | 세션·주차·건물·요금 | 성공률·peak | 개인정보·결제 | P0 |
| `SEED-ENS-D03-049` | APP-024 | EV 충전부지 ESS 용량·운전경제성 설계 부족 | 부하·충전·ESS·증설비 | NPV·증설회피 | 화재·전기안전 | P0 |
| `SEED-ENS-D03-050` | APP-023 | 충전기 고장·기사출동이 사후대응 중심 | charger log·parts·dispatch | MTTR·first fix | 원격제어보안 | P0 |
| `SEED-ENS-D03-051` | APP-025 | CCS 단계별 CO2 계량·소유권·버전 계보 불명확 | meter·lab·custody·storage | mass balance·audit time | 국제규제·책임 | P1 |
| `SEED-ENS-D03-052` | APP-025 | methane·액화·운송 포함 LNG 탄소강도 산정경계 불일치 | lifecycle activity data | carbon intensity | 방법론·검증 | P1 |

### 27.1 Seed Prioritization Fields

```yaml
seed_scoring_fields:
  business_relevance: 1_to_5
  pain_evidence: 1_to_5
  data_readiness: 1_to_5
  sponsor_readiness: 1_to_5
  expected_value: 1_to_5
  time_to_poc: 1_to_5
  safety_regulatory_risk: 1_to_5_negative
  duplication_with_owned_capability: 1_to_5_negative
  external_solution_fit: 1_to_5
  overall_status: screen | validate | poc | hold | reject
```

### 27.2 Immediate Validation Interview Questions

| Function | 질문 | 관련 Seed |
|---|---|---|
| LNG 수급 | 지난 12개월 수작업 재계획이 가장 잦았던 원인은 무엇인가 | 022~024 |
| 터미널 | BOG·재고·선박지연 중 비용과 안전에 가장 큰 변동요인은 무엇인가 | 023~025 |
| 발전 | heat rate 또는 강제정지 개선을 막는 데이터 단절은 무엇인가 | 026~028 |
| 도시가스 | RBMS가 사용 중인 데이터와 아직 연결되지 않은 데이터는 무엇인가 | 029~033 |
| 재생/PPA | 제안·정산·증빙에서 반복 수작업이 가장 많은 단계는 무엇인가 | 034~037 |
| 수소 | 생산·물류·충전소 중 병목과 재고손실이 가장 큰 구간은 어디인가 | 038~040 |
| 에너지솔루션 | KCE/EverCharge 보유기술을 국내에 적용할 때 가장 큰 규제·데이터 Gap은 무엇인가 | 041~050 |
| CCS | 누가 어떤 데이터의 owner이며 제3자 검증에 필요한 계보가 있는가 | 051~052 |

---
