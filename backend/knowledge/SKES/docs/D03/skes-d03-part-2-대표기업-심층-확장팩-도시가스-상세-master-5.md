---
id: skes-d03-part-2-대표기업-심층-확장팩-도시가스-상세-master-5
title: Part 2. 대표기업 심층 확장팩 — 도시가스 상세 Master
summary: "E&S 도시가스 사업의 공급망 구조, 자회사·권역 맵핑, 제품솔루션, 고객여정을 정의한 기준 문서. 표로 정리한 서비스층별 오류와 KPI 포함."
tags: [d03, product, schema, table]
keywords: [공급망, 자회사, 권역, 고객여정, 제품솔루션, RBMS, 규제요금, 배관관리, 디지털서비스]
related: [ORG-ENS-CG-KOONE, ORG-ENS-CG-BUSAN, ORG-ENS-CG-YN-GUMI, ORG-ENS-CG-YN-POHANG, ORG-ENS-CG-CHUNGCHEONG, ORG-ENS-CG-JEONNAM, ORG-ENS-CG-JEONBUK, ORG-ENS-CG-GANGWON, PS-ENS-CG-01, PS-ENS-CG-02, CJ-CG-01, CJ-CG-02, CJ-CG-03, CJ-CG-04, CJ-CG-05, CJ-CG-06, CJ-CG-07, CJ-CG-08, PS-ENS-CG-03]
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 2. 대표기업 심층 확장팩
tokens: 1994
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 2. 대표기업 심층 확장팩

## 17. 도시가스 상세 Master

### 17.1 공급망 서비스 구조

도시가스는 `도입/도매가스 인수 → 압력조정 → 지역 배관망 → 계량 → 청구·수납 → 안전점검·민원`의 연속 서비스다. E&S는 7개 자회사, 8개 권역, 약 510만 가구에 공급하며 공식 페이지의 2023년 기준 공급량은 54억㎥, 국내 점유율은 22.6%다. ([SRC-ENS-D03-0010])

| Service layer | 주요 사용자 | 핵심 데이터 | 실패가 고객에게 보이는 방식 |
|---|---|---|---|
| 수급·송출 | 수급·관제조직 | 시간대별 수요, 압력, 온도, 공급계획 | 압력저하·공급불안 |
| 배관망 운영 | 관제·안전·정비 | GIS, 재질, 매설연도, 압력, 밸브 | 누출·공급중단 |
| 계량·검침 | 고객·검침조직 | 계량기, 사진, AMI, 검침주기 | 추정고지·오검침 |
| 청구·수납 | 고객센터·재무 | 사용량, 요금, 납부, 연체 | 청구오류·처리지연 |
| 전출입·계약 | 고객·현장기사 | 주소, 계량기, 예약, 계약상태 | 방문지연·재신청 |
| 안전점검 | 고객·안전조직 | 점검이력, 부적합, 민원, 누출 | 사고위험·반복방문 |

### 17.2 자회사·권역 Entity Mapping

| Entity ID | 자회사/사업장 | 공식 공급권역 요약 | D03 제품 연결 |
|---|---|---|---|
| `ORG-ENS-CG-KOONE` | 코원에너지서비스 | 서울 동남권 및 경기 동부·남부 일부 | CG-01/02/03 |
| `ORG-ENS-CG-BUSAN` | 부산도시가스 | 부산광역시 | CG-01/02/03 |
| `ORG-ENS-CG-YN-GUMI` | 영남에너지서비스 구미 | 경북 구미·김천·상주·문경 등 | CG-01/02/03 |
| `ORG-ENS-CG-YN-POHANG` | 영남에너지서비스 포항 | 포항·영덕·울진 | CG-01/02/03 |
| `ORG-ENS-CG-CHUNGCHEONG` | 충청에너지서비스 | 충북 다수 시·군 및 세종 일부 | CG-01/02/03 |
| `ORG-ENS-CG-JEONNAM` | 전남도시가스 | 순천·광양 및 전남 일부 | CG-01/02/03 |
| `ORG-ENS-CG-JEONBUK` | 전북에너지서비스 | 익산·정읍 | CG-01/02/03 |
| `ORG-ENS-CG-GANGWON` | 강원도시가스 | 춘천·태백 및 강원 일부 | CG-01/02/03 |

> 법인 수는 7개이지만 영남에너지서비스의 구미·포항 사업권역을 별도 운영 단위로 표시해 공식 페이지의 8개 권역과 정합성을 유지한다. ([SRC-ENS-D03-0010])

### 17.3 `PS-ENS-CG-01` — 도시가스 공급

```yaml
product_solution_id: PS-ENS-CG-01
canonical_name: Regulated City Gas Supply
lifecycle_status: commercial_operating
customer_segments:
  - residential
  - commercial
  - industrial
  - public_and_district_energy
value_proposition:
  - 안전하고 연속적인 가스공급
  - 규제요금 기반 사용량 정산
  - 지역생활·산업 인프라 제공
data_inputs:
  - 공급량·압력·온도
  - 시간대별·권역별 수요
  - 날씨·달력·고객군
  - 배관·정압기·밸브 상태
kpi:
  - 공급중단시간
  - 수요예측오차
  - 배관손실·미계량가스
  - 민원과 사고
source_ids: [SRC-ENS-D03-0010]
```

### 17.4 `PS-ENS-CG-02` — 고객 디지털 서비스

디지털 서비스는 단일 앱이 아니라 고객 journey를 기준으로 분해한다.

| Journey ID | 고객업무 | 자동화 후보 | 핵심 오류·위험 | KPI |
|---|---|---|---|---|
| `CJ-CG-01` | 신규 사용·명의변경 | 신청 분류·서류 확인·예약 | 주소/계량기 매칭 오류 | 처리시간·재방문 |
| `CJ-CG-02` | 전입·전출 | 일정추천·기사배정·상태알림 | 노쇼·중복예약 | 완료율·이동거리 |
| `CJ-CG-03` | 자가검침 | 이미지 OCR·범위검증 | 오입력·사진 품질 | 자동인식률·재처리 |
| `CJ-CG-04` | 요금조회·청구 | 설명형 청구서·이상알림 | 개인정보·오안내 | 문의감소·정확도 |
| `CJ-CG-05` | 납부·자동이체 | 실패원인 분류·재안내 | 결제·개인정보 | 납부성공률 |
| `CJ-CG-06` | 안전점검 예약 | 위험도·동선 기반 예약 | 고위험 고객 누락 | 점검완료율 |
| `CJ-CG-07` | 냄새·누출 신고 | 긴급도 분류·위치확인 | false negative | 출동시간·사고 |
| `CJ-CG-08` | 일반상담 | 검색형 답변·업무 라우팅 | 환각·규정오류 | 1회 해결률 |

**AI 적용 원칙**

- 누출·안전 신고는 생성형 AI 단독 종료를 금지하고 긴급 프로토콜로 연결한다.
- OCR 결과는 전월·계량기 최대값·사용패턴으로 검증한다.
- 고객 행동예측보다 목적 제한·최소수집·보존기간을 먼저 설계한다.
- 상담봇 정확도는 문장 유사도가 아니라 실제 업무완료율로 측정한다.

### 17.5 `PS-ENS-CG-03` — 배관·안전관리 서비스

공식 페이지는 드론 점검과 RBMS 도입을 확인한다. RBMS는 배관별 위험도를 정량화해 점검·보수 우선순위를 정하는 운영체계로 해석하되, E&S 내부 산식과 변수는 공개되지 않았다. ([SRC-ENS-D03-0010])

```yaml
pipeline_risk_record:
  asset:
    pipe_segment_id: canonical GIS segment
    material: steel | PE | other
    diameter_pressure: controlled
    installation_year: year
  hazard:
    corrosion: inspection and CP data
    excavation: permit and third_party_work
    ground: settlement flood landslide
    operational: pressure fluctuation leak_alarm
  consequence:
    population_density: geospatial
    critical_facility: school hospital transport
    isolation_complexity: valve topology
  evidence:
    inspection_history: date method result
    incident_near_miss: event labels
    uncertainty: missingness and freshness
```

**O/I 후보**

1. GIS·굴착신고·민원·기상·부식 데이터를 결합한 동적 위험도.
2. 드론/차량 영상의 침하·불법굴착·표지 이상 탐지.
3. 누출센서 경보와 압력패턴의 false alarm 감소.
4. 위험도 기반 점검주기·기사동선·부품배치 최적화.
5. 사고·near miss·작업허가 데이터의 원인 그래프.

---
