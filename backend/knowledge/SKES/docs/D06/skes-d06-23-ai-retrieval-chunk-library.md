---
id: skes-d06-23-ai-retrieval-chunk-library
title: AI Retrieval Chunk Library
summary: "SK이노베이션 E&S의 에너지자산 통합운영을 위한 12개 AI 청크로, LNG·발전·수소·CCS 등 도메인별 데이터 연결과 AI 배포 모델을 제시한다."
tags: [d06, process]
keywords: [LNG 통합운영, BOG (보일오프가스), 배관 RBMS, 발전 성능 최적화, 열병합발전 (CHP), ESS 입찰 최적화, CCS (탄소 포집), 액화수소, 드론 검사, OT AI 배포]
related: [CHUNK-ENS-D06-001, CHUNK-ENS-D06-002, CHUNK-ENS-D06-003, CHUNK-ENS-D06-004, CHUNK-ENS-D06-005, CHUNK-ENS-D06-006, CHUNK-ENS-D06-007, CHUNK-ENS-D06-008, CHUNK-ENS-D06-009, CHUNK-ENS-D06-010, CHUNK-ENS-D06-011, CHUNK-ENS-D06-012]
priority: normal
domain: D06
section: 23
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1385
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 23. AI Retrieval Chunk Library

## `CHUNK-ENS-D06-001` — LNG Integrated Operations

SK이노베이션 E&S의 LNG 운영은 가스전 권리, 액화설비 지분·사용계약, 전용선, Boryeong 터미널 운영권, 발전·도시가스 수요를 연결한다. O/I의 핵심은 각 자산을 보유했다고 나열하는 것이 아니라 계약권리·cargo ETA·tank inventory·BOG·sendout·발전급전을 같은 시계열과 ID로 연결하는 것이다.

## `CHUNK-ENS-D06-002` — Terminal BOG

LNG 터미널 BOG는 탱크 열유입, 하역, 배관·펌프 열유입과 운전 transient에서 발생할 수 있다. D06은 BOG flow, tank pressure, compressor/recondenser 상태, sendout demand, 회수·연료·flare/vent 경로를 요구한다. Boryeong의 실제 설비 구성은 내부검증 전 산업 baseline으로만 사용한다.

## `CHUNK-ENS-D06-003` — Power Performance

복합발전 O/I는 gas turbine만 보지 않고 GT–HRSG–steam turbine–condenser–cooling–CEMS–water chemistry를 함께 본다. ambient와 operating mode를 보정하지 않은 heat-rate 비교는 잘못된 결론을 만들 수 있다. Historian tag와 start/trip/work-order를 asset ID로 연결해야 원인과 효과를 구분할 수 있다.

## `CHUNK-ENS-D06-004` — CHP

CHP는 전력가격만 최적화할 수 없고 지역 열수요와 공급의무를 동시에 만족해야 한다. 날씨·달력·고객 heat meter, 공급/환수온도, plant availability, electric dispatch를 결합한 확률적 열수요 예측과 co-dispatch가 핵심 O/I 영역이다.

## `CHUNK-ENS-D06-005` — City-Gas RBMS

E&S는 도시가스 배관에 RBMS를 도입했다고 공개한다. RBMS의 핵심 데이터는 배관 재질·연령·접합·압력·부식·누출·수리·토양·굴착·인구·중요고객·데이터 불확실성이다. AI 점수는 설명가능성, incident backtest, missing-data penalty, 전문가 override를 포함해야 한다.

## `CHUNK-ENS-D06-006` — Drone and Leak Safety

드론·순회검사 데이터는 영상만 저장해서는 O/I 데이터가 되지 않는다. route coverage, sensor, 위치신뢰도, asset ID, anomaly confidence, 현장확인, work order, closure evidence를 연결해야 안전성과 생산성을 측정할 수 있다.

## `CHUNK-ENS-D06-007` — PPA Operations

직접 PPA 운영은 발전량 예측만의 문제가 아니다. interval meter, 계약 가격·배분·손실·curtailment 조항, REC 소유·이전·말소, 고객 RE100 evidence를 동일 lineage로 연결해야 자동정산과 감사가 가능하다.

## `CHUNK-ENS-D06-008` — ESS Bidding

KCE MarketCapture의 공개 기능은 AI 기반 입찰 최적화다. D06의 운영모델은 가격예측, bid/award, SOC/SOH, interconnection, warranty, degradation cost, dispatch telemetry, settlement를 연결한다. 안전제약은 언제나 시장수익보다 우선하고 모델 override는 기록해야 한다.

## `CHUNK-ENS-D06-009` — EV Dynamic Load

EverCharge SmartPower는 건물의 전력 한도 안에서 충전부하를 동적으로 배분하는 자회사 역량이다. site non-EV load, connected sessions, charger state, 요구에너지, 우선순위, tariff를 사용하되 공정한 배분, local fallback, overload protection을 검증해야 한다.

## `CHUNK-ENS-D06-010` — Liquid Hydrogen

인천 플랜트는 부생수소를 액화해 공급하는 운영자산으로 공개되었으나 실제 정제·액화 사이클과 성능값은 공개되지 않았다. O/I는 feed purity, liquefier power and process state, storage pressure/temperature/level, BOG, tanker loading, delivery mass balance에 집중한다.

## `CHUNK-ENS-D06-011` — CCS MRV

CCS의 gross capture는 net avoided CO₂와 다르다. source, capture, transport, injection, leakage/vent, 전력·steam penalty를 계량하고 calibration·missing-data substitution·uncertainty를 버전관리해야 MRV와 경제성을 함께 평가할 수 있다.

## `CHUNK-ENS-D06-012` — OT AI Deployment

E&S 공정의 외부 AI는 historical extract → offline validation → shadow mode → operator advisory → bounded closed-loop 순서로 승격한다. DCS·PLC·BMS·PCS·safety system에 대한 직접 write는 MOC, safety, cyber 승인 전 금지한다.

---
