---
id: skes-d03-part-2-대표기업-심층-확장팩-renewable-re100-상세-ma-6
title: Part 2. 대표기업 심층 확장팩 — Renewable·RE100 상세 Master
summary: "재생에너지 발전 자산 상태 분류, 태양광·해상풍력 운영 및 의사결정, 기업 고객 직접 PPA 계약·정산·증빙의 전체 프로세스"
tags: [d03, product, schema, table]
keywords: [포트폴리오 상태, 태양광, 해상풍력, 직접 PPA, 발전 예측, 고객 부하 매칭, 계약 정산, SCADA, 기술 가용성]
related: [PS-ENS-REN-01, PS-ENS-REN-02]
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 2. 대표기업 심층 확장팩
tokens: 1417
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 2. 대표기업 심층 확장팩

## 18. Renewable·RE100 상세 Master

### 18.1 재생에너지 포트폴리오 상태 모델

| Status | DB 정의 | 용량 집계 규칙 |
|---|---|---|
| `OPERATING` | 상업운전이 공식 확인된 자산 | 운영용량에 포함 |
| `CONSTRUCTION` | 착공·건설 중 | 운영용량과 분리 |
| `DEVELOPMENT` | 인허가·부지·PPA·금융조달 단계 | 개발용량으로만 표시 |
| `PIPELINE` | 초기 후보 포함 가능 | 운영·개발과 합산 금지 |
| `OWNED_GROSS` | 프로젝트 총용량 | 지분귀속용량과 분리 |
| `ATTRIBUTABLE` | 지분율 반영 용량 | 지분율 출처 필요 |

공식 페이지의 태양광 `운영 및 개발 3.5GW`와 전체 `약 5GW pipeline`은 중복될 수 있으므로 총 8.5GW로 합산하지 않는다. 2025년 전남해상풍력 1단계 상업운전과 2·3단계 포함 약 900MW 계획도 상태별로 분리한다. ([SRC-ENS-D03-0009])

### 18.2 `PS-ENS-REN-01` — 태양광 전력

| Layer | 상세 내용 |
|---|---|
| Customer value | 재생전력·장기 가격가시성·RE100 이행 |
| Asset | 모듈, 인버터, 접속설비, 계량, 부지 |
| Data | irradiance, 기상, SCADA, 인버터, IV curve, 열화상, 오염·음영 |
| Decisions | 발전예측, 세척, 인버터 정비, 출력제한 대응, PPA 정산 |
| KPI | PR, availability, forecast error, degradation, curtailment, O&M cost |
| O/I | 위성·기상 보정, 드론 열화상, fault localization, 세척경제성, 예비품 최적화 |

### 18.3 `PS-ENS-REN-02` — 육상·해상풍력 전력

해상풍력은 터빈 데이터만으로 최적화되지 않는다. 접근선박·파고·풍속·인력·예비품·계통제약을 함께 봐야 한다.

```yaml
offshore_wind_maintenance_decision:
  asset_condition:
    - vibration_temperature_oil
    - SCADA_alarm_power_curve
    - blade_image_lightning_erosion
  access_window:
    - wind_wave_visibility
    - vessel_availability
    - technician_certification
  commercial_context:
    - expected_generation_loss
    - electricity_price
    - warranty_and_contract
  output:
    - failure_risk
    - optimal_visit_window
    - vessel_crew_parts_plan
    - defer_or_repair_recommendation
```

**주요 KPI**: capacity factor, technical availability, wake loss, downtime, forecast error, vessel day, MTTR, 안전사건.

### 18.4 `PS-ENS-REN-03~05` — 직접 PPA 통합 서비스

직접 PPA는 `영업상품`과 `운영서비스`를 분리한다.

| PPA layer | 제공 기능 | 입력 데이터 | 산출물 |
|---|---|---|---|
| Lead qualification | 고객 부하·RE100 목표 진단 | 월/시간대 사용량, 사업장, 목표연도 | 적합성·예상규모 |
| Asset matching | 발전자산과 고객부하 매칭 | 자산위치·기술·COD·발전곡선 | 후보 포트폴리오 |
| Commercial design | 기간·가격·물량·위험분담 | 가격전망, 신용, 계통비용 | 제안·시나리오 |
| Contracting | 계약·부속합의·조건선행 | 법률·계량·정산·보증 | 승인계약 |
| Forecasting | 발전·부하 예측 | 기상, 실적, 생산계획 | 일전·월간 예측 |
| Settlement | 사용·공급·부족/초과 대사 | 계량, 시장가격, 계약식 | 청구·정산 |
| Evidence | 재생전력 사용 증빙 | 계약·계량·인증정보 | 감사·공시자료 |
| Renewal | 성과·위험 재평가 | 비용, 감축, 오류, 민원 | 재계약·확장안 |

**공개 계약 예시**

| Customer entity | 공개 조건 | DB 상태 | 출처 |
|---|---|---|---|
| Amorepacific | 국내 최초 직접 PPA, 5MW, 20년, 대전사업장 공급 계획 | 계약별 공개사실 | SRC-ENS-D03-0017 |
| BASF Korea | 2025년부터 20년, 한국 전력수요 16%, 2045년까지 90만톤 감축 기대 | term sheet 공개 | SRC-ENS-D03-0016 |

**O/I 문제 구조**

- 고객부하 데이터 형식이 사업장마다 달라 제안분석 시간이 길 수 있다.
- 개발자산의 COD·발전량·계통접속 불확실성이 계약제안과 분리될 수 있다.
- 계량·계약·시장·인증 데이터 대사에 수작업이 존재할 수 있다.
- 발전량 부족·초과·출력제한의 비용이 계약별로 다르게 배분된다.
- 생성형 AI 계약검토는 법무 승인과 조항별 근거 추적 없이는 사용하지 않는다.

---
