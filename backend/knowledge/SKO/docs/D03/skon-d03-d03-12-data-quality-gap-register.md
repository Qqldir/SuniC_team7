---
id: skon-d03-d03-12-data-quality-gap-register
title: Data Quality & Gap Register
summary: SK온 D03 배터리 제품의 데이터 품질 평가 결과(CONDITIONALLY_COMPLETE)와 원문중복·URL정규화·상용상태 혼동·사양누락·시험조건·제조사주장·고객계약 등 7가지 식별 이슈의 심각도·대응 통제 상태를 추적하는 레지스터.
tags: [d03, product, core-candidate, schema, table, "xref:d00", "xref:d05", "xref:d06", "xref:d07"]
keywords: [GRIDON, Hyper Fast Battery, 충전시간 비교, 상용화상태 분류, Source ID 중복, 배터리 스펙 누락, 제조사 클레임 독립성, URL 정규화, 차량충전 시험조건, 경쟁사 비교 조건, 데이터품질관리, 갭레지스터, SK온, D03, 배터리, 중복제거, 상용제품, 사양공개, 제조사클레임]
related: []
priority: critical
domain: D03
section: D03-12.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 2143
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03-12. Data Quality & Gap Register

## 12.1 Quality Status

```yaml
data_quality_summary:
  domain: D03
  overall_status: CONDITIONALLY_COMPLETE
  factual_core_quality: HIGH
  ai_structure_quality: HIGH
  source_traceability: MEDIUM_HIGH
  quantitative_spec_coverage: MEDIUM_LOW
  commercial_status_separation: HIGH
  competitor_claim_independence: MEDIUM
```

`CONDITIONALLY_COMPLETE`는 제품·서비스 구조와 핵심 사실이 완성됐지만, 미공개 사양과 계약정보가 남아 있다는 뜻이다.

---

## DQ-SKON-D03-001 — Source ID Duplication

```yaml
issue_id: DQ-SKON-D03-001
issue: 동일 원문이 여러 Source ID로 중복 등록됨
examples:
  - Hyper Fast article
  - GRIDON article
  - BaaS AI article
  - Solid-state pilot article
severity: MEDIUM
action:
  - D00 통합 시 canonical_source_id 하나만 유지
  - 나머지는 duplicate_of 필드로 연결
status: OPEN_FOR_D00_NORMALIZATION
```

---

## DQ-SKON-D03-002 — URL Canonicalization

```yaml
issue_id: DQ-SKON-D03-002
issue:
  - 일부 기존 URL에 utm_source 등 추적 파라미터 포함
  - 한국어·영문 페이지가 별도 원문으로 중복 등록
severity: LOW
action:
  - 추적 파라미터 제거
  - canonical_url과 alternate_language_url 분리
  - 접근일 기준 HTTP 상태 저장
status: OPEN
```

---

## DQ-SKON-D03-003 — Commercial Status Ambiguity

```yaml
issue_id: DQ-SKON-D03-003
affected_entities:
  - SF+ Battery
  - Hyper Fast Battery
  - LFP EV Platform
  - Prismatic Platform
  - Polymer-Oxide Composite Battery
  - Sulfide ASSB
issue: 공개 제품기술·시제품·R&D 목표가 상용제품과 혼동될 가능성
severity: VERY_HIGH
control:
  - commercial_status 필수
  - 답변 시 prototype/R&D 경고 표시
  - 고객계약과 기술공개 분리
status: CONTROL_IMPLEMENTED
```

---

## DQ-SKON-D03-004 — GRIDON Missing Specifications

```yaml
issue_id: DQ-SKON-D03-004
entity:
  - GRIDON Gen 1
  - GRIDON Gen 2
missing_fields:
  - Absolute MWh per container
  - Round-trip efficiency
  - Cycle life
  - Warranty period
  - Availability
  - Auxiliary power consumption
  - Operating temperature
  - PCS vendor
  - EMS architecture
severity: HIGH
handling: NOT_DISCLOSED
```

GRIDON의 공식 공개자료는 EIS, 냉각수 기반 안전기술, DC·AC 블록 지원 및 세대 간 용량 개선율을 제시하지만, 위 사양을 모두 공개하지는 않는다. ([ASK Inno][2])

---

## DQ-SKON-D03-005 — Fast-Charging Test Conditions

```yaml
issue_id: DQ-SKON-D03-005
affected_metrics:
  - Charging time
  - Driving range after charge
  - C-rate
  - Peak charging power
issue: 제품별 시험온도·전압·충전기·차량조건이 동일하지 않음
severity: VERY_HIGH
control:
  - 제품 순위 자동생성 금지
  - vehicle_range와 cell_performance 분리
  - manufacturer_claim 태그 유지
status: CONTROL_IMPLEMENTED
```

SK온 Hyper Fast와 CATL Shenxing의 충전 관련 수치는 서로 다른 제품·차량·시험조건에서 제시됐으므로 단순 수치만으로 우열을 결정하지 않는다. ([ASK Inno][18])

---

## DQ-SKON-D03-006 — Manufacturer Claim Independence

```yaml
issue_id: DQ-SKON-D03-006
affected_competitors:
  - CATL
  - Samsung SDI
  - LG Energy Solution
  - SK On
issue: 경쟁사 제품성능의 상당 부분이 제조사 자체 발표
severity: MEDIUM_HIGH
control:
  - MANUFACTURER_CLAIM 저장
  - 독립 시험·인증과 분리
  - D16에서 제3자 자료 추가
status: OPEN_FOR_D16
```

---

## DQ-SKON-D03-007 — Customer and Contract Granularity

```yaml
issue_id: DQ-SKON-D03-007
issue:
  - 동일 차종의 지역·연식·트림별 공급사 차이 가능
  - MOU와 공급계약의 혼동 가능
  - 우선협상권과 확정물량의 혼동 가능
severity: HIGH
control:
  - contract_status 필수
  - named_customer와 target_market 분리
  - historical/current 관계 분리
status: CONTROL_IMPLEMENTED
```

---

## DQ-SKON-D03-008 — BaaS Commercial Scale

```yaml
issue_id: DQ-SKON-D03-008
entity: PF-SKON-BAAS
confirmed:
  - 공식 사업영역
  - 모니터링·진단 기능
  - B2B/B2C 지향
  - 생태계 파트너 구조
not_confirmed:
  - Current paying customers
  - Annual revenue
  - Active monitored batteries
  - API transaction volume
  - Current geographic coverage
severity: HIGH
handling: SCALE_NOT_DISCLOSED
```

공식 BaaS 페이지는 서비스 방향과 파트너 유형을 설명하지만 사업 규모 수치를 제공하지 않는다. ([SK On][3])

---

## DQ-SKON-D03-009 — Solid-State Target Risk

```yaml
issue_id: DQ-SKON-D03-009
entity: PROD-SKON-NEXT-002
target:
  commercialization_year: 2029
  initial_energy_density: 800_Wh_per_L
  long_term_energy_density: 1000_Wh_per_L
risk:
  - Target schedule can change
  - Target density is not validated mass-production output
severity: VERY_HIGH
control:
  - CORPORATE_TARGET status
  - annual re-verification
status: CONTROL_IMPLEMENTED
```

SK온은 파일럿 플랜트 구축과 2029년 목표를 공식적으로 공개했으나, 이는 미래 계획이다. ([ASK Inno][4])

---

## DQ-SKON-D03-010 — Entity Count Reproducibility

```yaml
issue_id: DQ-SKON-D03-010
issue: 기존 178개 엔티티 집계는 서술형 작업 중 산출된 스냅샷
severity: MEDIUM
risk: 실제 JSON/YAML export 시 수량 차이 발생 가능
action:
  - D00~D03 통합 export 후 자동 카운트
  - orphan node와 duplicate entity 검사
canonical_status: PROVISIONAL_COUNT
```

따라서 최종 YAML에는 `178`을 확정 마스터 수량이 아니라 `provisional_entity_count`로 저장한다.

---

## 12.2 Missing Data Register

| Gap ID      | 미확보 정보            |   우선도 | 확보 대상          |
| ----------- | ----------------- | ----: | -------------- |
| GAP-D03-001 | 제품별 셀 용량·전압·중량    |    높음 | 고객 인증자료·제품 사양서 |
| GAP-D03-002 | GRIDON 절대 MWh·RTE | 매우 높음 | 제품 데이터시트·입찰자료  |
| GAP-D03-003 | Hyper Fast 양산일정   | 매우 높음 | IR·고객 발표       |
| GAP-D03-004 | EV LFP 실명 고객      | 매우 높음 | 공급계약·OEM 발표    |
| GAP-D03-005 | 각형 셀 양산공장         | 매우 높음 | 투자계획·고객 인증     |
| GAP-D03-006 | CTP 양산차 적용        |    높음 | OEM·모터쇼 자료     |
| GAP-D03-007 | BaaS 매출·활성고객      |    높음 | 사업보고서·인터뷰      |
| GAP-D03-008 | 전고체 파일럿 수율        | 매우 높음 | 기술발표·특허·고객 샘플  |
| GAP-D03-009 | 제품별 특허 연결         | 매우 높음 | D05 특허분석       |
| GAP-D03-010 | 제품별 공정·설비 연결      | 매우 높음 | D06·D07        |
| GAP-D03-011 | 원재료별 제품 노출도       |    높음 | D10            |
| GAP-D03-012 | 제품별 원가·마진         | 매우 높음 | D11·D12        |

---
