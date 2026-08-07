---
id: skes-d03-part-3-application-customer-alternative-5
title: Part 3. Application·Customer·Alternative·Graph·Chunk 확장 — Competitive and Alternative Solution Mapping
summary: LNG·발전·도시가스·수소·ESS 등 주요 사업 영역별로 고객의 문제해결 방식과 E&S의 차별화 자산을 비교하는 대안 매핑 표
tags: [d03, product, table, "xref:d16"]
keywords: [대체솔루션, 경쟁력분석, LNG, 발전, 도시가스, 수소, ESS, 예지보전, 데이터권리, 차별화자산]
related: [CGAP-ENS-001, CGAP-ENS-002, CGAP-ENS-003, CGAP-ENS-004, CGAP-ENS-005, CGAP-ENS-006, CGAP-ENS-007, CGAP-ENS-008]
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 3. Application·Customer·Alternative·Graph·Chunk 확장
tokens: 1701
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 3. Application·Customer·Alternative·Graph·Chunk 확장

## 24. Competitive and Alternative Solution Mapping

### 24.1 비교 원칙

- 경쟁사는 회사명 나열보다 고객이 동일 문제를 해결하는 `대체 방식`을 비교한다.
- 공개되지 않은 가격·성능·시장점유율을 임의로 채우지 않는다.
- E&S가 이미 가진 자회사 역량과 외부 도입이 필요한 영역을 구분한다.
- 외부 솔루션은 D16에서 회사·제품 단위로 확장하고, D03에서는 기능요건만 정의한다.

### 24.2 LNG 운영 대안

| 문제 | 현재/전통 방식 | 디지털 대안 | E&S 차별화 자산 | Gap |
|---|---|---|---|---|
| 수요·조달계획 | spreadsheet·담당자 판단 | stochastic portfolio optimization | 가스–선박–터미널–발전 연결 | 계약 데이터권리 |
| ETA·berth | 선사 ETA·수동조정 | AIS·기상 ML + terminal constraint | 전용선·터미널·수요 | 실시간 통합 여부 |
| BOG | 경험기반 운전 | physics+ML 예측·최적화 | 탱크·send-out 운영데이터 | 센서·라벨 품질 |
| 정비 | 주기·alarm 중심 | condition/prescriptive maintenance | 다수 유사설비 | failure label |

### 24.3 발전·CHP 대안

| 문제 | 대안 A | 대안 B | 선정기준 |
|---|---|---|---|
| 발전계획 | 시장경제급전 | 설비상태 포함 경제급전 | 순마진·고장·설명가능성 |
| 효율진단 | OEM curve | digital twin/ML baseline | drift 탐지·정확도·현장신뢰 |
| 예지보전 | 단일센서 alarm | 다변량 anomaly + work order | lead time·precision·회수액 |
| 열수요 | 기온회귀 | 건물군·달력·실시간 수요 모델 | horizon별 오차·공급위반 |

### 24.4 도시가스 대안

| 문제 | 대체방식 | 장점 | 한계/Gate |
|---|---|---|---|
| 검침 | 방문검침 | 현장확인 | 비용·접근·주기 |
| 검침 | 자가검침 OCR | 편의·자동화 | 이미지·오입력·개인정보 |
| 검침 | AMI | 고빈도·원격 | CAPEX·통신·보안 |
| 누출 | 순회·민원 | 단순·현장성 | 탐지주기 |
| 누출 | 고정센서/압력분석 | 연속감시 | false alarm·커버리지 |
| 누출 | 차량/드론·위성 | 넓은 영역 | 해상도·기상·규제 |
| 배관위험 | 정기점검 | 규정충족 | 동적위험 반영 부족 |
| 배관위험 | RBMS/AI | 우선순위화 | 라벨편향·설명·법정점검 |

### 24.5 PPA·RE100 대안

| 고객목표 | 대안 | 데이터 요구 | 위험 |
|---|---|---|---|
| 재생전력 조달 | 직접 PPA | 부하·자산·계약·정산 | 장기 가격·발전위험 |
| 재생전력 조달 | 녹색프리미엄/인증서 등 | 사용량·인증 | 추가성·가격·정책 |
| 비용안정 | 고정/혼합 가격구조 | 가격전망·신용 | basis·불균형 |
| 시간일치 | ESS·portfolio matching | 시간대별 부하·발전 | 열화·CAPEX |
| 증빙 | 수작업 문서 | 계량·계약·인증 | 오류·감사비용 |
| 증빙 | 데이터 계보 플랫폼 | 원천 연동·권한 | 표준·법적 인정 |

### 24.6 수소 대안

| 기능 | 대안 | 비교축 |
|---|---|---|
| 저장·운송 | 기체수소 | 압력, 부피, 거리, 설비 |
| 저장·운송 | 액화수소 | 액화에너지, BOG, 처리량 |
| 생산 | 부생수소 | 원료가용성, 탄소강도 |
| 생산 | 천연가스+CCS | 포집률, methane, 저장 |
| 생산 | 수전해 | 전력단가, 이용률, 물, 효율 |
| 배송 | 정적 주기배송 | 단순성, 재고안전 |
| 배송 | 수요예측 동적배차 | 데이터, 최적화, 복원력 |

### 24.7 ESS·DERMS·VPP 대안

| Capability | Internal/owned baseline | External alternative need | Build/Buy 판단축 |
|---|---|---|---|
| 계통 ESS 입찰 | KCE MarketCapture | 타시장 rule engine·MLOps | 규칙적합·성과·IP |
| EV 동적부하 | EverCharge SmartPower | 국내표준·결제·로밍 | 현지화·HW 연동 |
| DERMS | Ensolve 기반 추진 | network model·ADMS 연계 | 배전데이터·사이버 |
| VPP | 검토 단계 | onboarding·forecast·settlement | 자원규모·규제·단위경제 |
| 재생 O&M | 추진 단계 | image AI·CMMS·field service | 발전회수·정비성과 |
| ESS 안전 | 자산별 BMS/EMS | 통합 fleet risk analytics | 데이터접근·책임·보험 |

### 24.8 Competitive Gap Summary

| Gap ID | E&S의 공개 확인 역량 | 아직 확인되지 않은 부분 | D16 탐색 우선순위 |
|---|---|---|---|
| `CGAP-ENS-001` | LNG 전 밸류체인 | 통합 의사결정 플랫폼의 범위 | P0 |
| `CGAP-ENS-002` | 도시가스 RBMS·드론 | 자회사 공통 데이터·실시간성 | P0 |
| `CGAP-ENS-003` | 직접 PPA 선도계약 | 자동정산·시간단위 매칭 수준 | P0 |
| `CGAP-ENS-004` | 액화수소 생산·물류 인프라 | 실제 가동률·BOG·수요예측 | P0 |
| `CGAP-ENS-005` | KCE AI 입찰 | 국내/타시장 이전 가능성 | P0 |
| `CGAP-ENS-006` | EverCharge 동적부하 | 국내 충전·주차·ESS 통합 | P0 |
| `CGAP-ENS-007` | Ensolve 배전망 기반 | DERMS/VPP 상용운영 실적 | P1 |
| `CGAP-ENS-008` | CCS 계획 | MRV·허가·고객·검증탄소강도 | P1 |

---
