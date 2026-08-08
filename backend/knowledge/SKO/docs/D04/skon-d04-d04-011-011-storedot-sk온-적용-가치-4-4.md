---
id: skon-d04-d04-011-011-storedot-sk온-적용-가치-4-4
title: 011 — StoreDot — SK온 적용 가치 (4)
summary: "StoreDot 파트너 협력 현황을 직접 파트너, 연구 파트너, 협력 유형, 성숙도 지표(EML)로 체계화한 마스터 데이터."
tags: [d04, technology, schema, table]
keywords: [StoreDot, 전고체 배터리, 파트너 마스터, 협력 상태, 기술 이전, 공동 개발, 황화물 전해질, 연구 기관, EML, 기술 검증, 협력 관계, 공동개발, 성숙도 평가]
related: []
priority: normal
domain: D04
section: D04-011
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 011 — StoreDot
tokens: 3583
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 011 — StoreDot

```yaml
partner_status_vocabulary:

  ACTIVE_TECHNOLOGY_TRANSFER:
    definition: 설비·공정·라이선스 이전이 실제 진행됨

  ACTIVE_JOINT_DEVELOPMENT:
    definition: 공동 연구·개발 프로젝트가 공식 확인됨

  FEASIBILITY_MOU:
    definition: 기술·제조 가능성 평가를 위한 비구속 MOU

  AFFILIATE_COLLABORATION:
    definition: SK 계열사 역량과 연결

  RESEARCH_COLLABORATION:
    definition: 대학·연구기관과 학술·실험 연구

  BENCHMARK_ONLY:
    definition: 직접 협력은 확인되지 않고 비교대상으로만 사용
```

---

## 48.2 Direct Partner Master

| Partner ID           | 파트너            | 연결 기술            | 관계 상태                      | 핵심 역할        |
| -------------------- | -------------- | ---------------- | -------------------------- | ------------ |
| PART-SOLID-POWER     | Solid Power    | 황화물 전해질·전고체 셀 공정 | ACTIVE_TECHNOLOGY_TRANSFER | 파일럿 라인·설계·공정 |
| PART-FACTORIAL       | Factorial      | FEST 전고체         | FEASIBILITY_MOU            | 기존 라인 제조 적합성 |
| PART-SK-ENMOVE       | SK엔무브          | EV 액침냉각          | AFFILIATE_COLLABORATION    | 절연성 열관리 플루이드 |
| PART-SKIET           | SK아이이테크놀로지     | 세라믹 코팅 분리막       | AFFILIATE_TECHNOLOGY       | 분리막 소재       |
| PART-STANDARD-ENERGY | 스탠다드에너지        | VIB ESS          | ACTIVE_JOINT_DEVELOPMENT   | VIB 셀·전해질    |
| PART-SIEMENS-DISW    | Siemens DISW   | 제조 디지털 트윈        | ACTIVE_JOINT_DEVELOPMENT   | 공장·라인 시뮬레이션  |
| PART-BECKHOFF        | Beckhoff       | 생산설비 제어          | TECHNOLOGY_VALIDATION      | 제어기·자동화      |
| PART-CISCO           | Cisco          | 산업 네트워크          | TECHNOLOGY_VALIDATION      | 통신·보안        |
| PART-IFM             | IFM Electronic | 스마트 센서           | TECHNOLOGY_VALIDATION      | 설비상태 데이터     |
| PART-YASKAWA         | Yaskawa Korea  | 로봇·모션            | TECHNOLOGY_VALIDATION      | 자동화·로봇       |
| PART-WOOWON          | 우원기술           | 배터리 설비           | TECHNOLOGY_VALIDATION      | 조립설비         |

---

## 48.3 Research Partner Master

```yaml
research_partners:

  - partner_id: PART-SEOUL-NATIONAL-UNIV
    linked_technologies:
      - LMRO Single-Crystal Cathode
      - Ultrahigh-Nickel Large Single Crystal

  - partner_id: PART-HANYANG-UNIV
    linked_technologies:
      - Surface-Modified Lithium Interphase

  - partner_id: PART-YONSEI-UNIV
    linked_technologies:
      - GPE Curing and Residual-Monomer Control

  - partner_id: PART-DANKOOK-UNIV
    linked_technologies:
      - LLZO Oxide Solid Electrolyte

  - partner_id: PART-KICET
    linked_technologies:
      - Photonic Sintering
      - Garnet Electrolyte Scaffold

  - partner_id: PART-UT-RESEARCH
    linked_technologies:
      - Single-Ion Conducting Polymer Electrolyte
```

---

# D04-49. Evidence Maturity Normalization

공개자료만으로 공식 TRL 숫자를 확정하기 어렵기 때문에 D04에서는 `TRL` 대신 **Evidence Maturity Level, EML**을 사용한다.

## 49.1 EML Vocabulary

```yaml
evidence_maturity_level:

  EML_9:
    name: Commercial and Repeated Market Use
    requirement:
      - 실제 상용생산
      - 고객 또는 제품 적용
      - 반복적인 시장 공급

  EML_8:
    name: Product Integrated
    requirement:
      - 제품에 기술 통합
      - 생산 또는 고객적용 계획 확인
      - 상용실적은 제한적일 수 있음

  EML_7:
    name: Automotive or System Demonstration
    requirement:
      - 차량·ESS·시스템 수준 시연
      - 고객 검증 또는 실제 운전환경 시험

  EML_6:
    name: Pilot-Line Validation
    requirement:
      - 파일럿 설비
      - 공정 또는 대형셀 검증

  EML_5:
    name: Prototype Validation
    requirement:
      - 셀·팩·시제품 성능검증
      - 양산성 미확인

  EML_4:
    name: Integrated Laboratory Validation
    requirement:
      - 다층 연구셀
      - 논문·공동연구
      - 실제 작동 검증

  EML_3:
    name: Material or Component Validation
    requirement:
      - 소재 물성
      - 소형 시험셀
      - 개별 기능 검증

  EML_NA:
    name: Analytical Target
    requirement:
      - 현재 SK온 보유기술로 확인되지 않음
      - 전략·아키텍처 후보
```

---

## 49.2 Major Technology EML Map

| Technology                   |     EML | 근거 유형     | 해석           |
| ---------------------------- | ------: | --------- | ------------ |
| High-Nickel NCM              |   EML 9 | 차량·제품 상용  | 상용 핵심기술      |
| Z-Folding                    |   EML 9 | 양산 조립기술   | 고유 제조기술      |
| SF Fast Charging             |   EML 9 | 상용제품      | 제품 적용        |
| Magnetic Alignment           |   EML 8 | 제품 적용 공개  | 적용제품 확인      |
| EIS-Based BMS                |   EML 8 | GRIDON 통합 | 제품 통합        |
| ESS Coolant Immersion        |   EML 8 | GRIDON 기술 | 장기 필드실적 미공개  |
| BaaS AI                      |   EML 7 | 파트너 서비스   | 사업규모 미공개     |
| AI Researcher                |   EML 7 | 내부운영 플랫폼  | 외부제품 아님      |
| Hyper Fast·SUFast            |   EML 5 | 시제품 성능    | 양산·고객 미확인    |
| On-Vent                      |   EML 5 | 시제품·반복시험  | 양산 미확인       |
| Pouch-Integrated Prismatic   |   EML 5 | 전시·성능검증   | 고객 미확인       |
| S-Pack+                      |   EML 5 | 전시 시제품    | 양산차 미확인      |
| EV Immersion Cooling         |   EML 5 | 공동개발·전시   | 차량 적용 미확인    |
| Wireless BMS                 |   EML 5 | 시제품       | 인증 미확인       |
| Dry Electrode                | EML 5~6 | 개발·파일럿    | 양산수율 미공개     |
| Sulfide ASSB                 |   EML 6 | 파일럿 라인    | 상용셀 미확인      |
| Polymer–Oxide Composite      | EML 5~6 | 파일럿 개발    | 양산 미확인       |
| SIPE                         | EML 3~4 | 연구셀       | 대형셀 미검증      |
| LLZO                         | EML 3~4 | 소재·논문     | 상용공정 없음      |
| Surface-Modified Lithium     |   EML 4 | 연구셀 300회  | 특정 시험조건      |
| LMRO Single Crystal          | EML 3~4 | 논문        | 상업 셀 미확인     |
| Battery Foundation Model     | EML N/A | 분석목표      | 공식 보유기술 아님   |
| Manufacturing Digital Thread | EML N/A | 분석통합      | 완성 플랫폼 미확인   |
| Prelithiation                | EML N/A | 외부역량 후보   | SK온 프로그램 미확인 |

EML은 공개 증거를 정규화하기 위한 D04 내부 평가이며, 국제표준 TRL이나 SK온의 자체 기술평가 결과가 아니다.

---

# D04-50. FACT·ANALYSIS·HYPOTHESIS Separation

## 50.1 FACT Registry

```yaml
fact_registry:

  - fact_id: FACT-D04-001
    statement: SK온은 Cell Development AI Researcher를 구축했다.
    entity_ids:
      - TECH-SKON-D04-032
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - fact_id: FACT-D04-002
    statement: Materials Development AI Researcher는 공개 시점에 개발 중이었다.
    entity_ids:
      - TECH-SKON-D04-037
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - fact_id: FACT-D04-003
    statement: SK온은 건식전극과 AI 기반 캘린더링 제어를 개발하고 있다.
    entity_ids:
      - TECH-SKON-D04-003
      - TECH-SKON-D04-039
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - fact_id: FACT-D04-004
    statement: Solid Power는 SK온 파일럿 셀 라인의 현장인수시험 완료를 발표했다.
    entity_ids:
      - TECH-SKON-D04-001
      - TECH-SKON-D04-069
      - PART-SOLID-POWER
    evidence_type: PARTNER_CONFIRMED
    confidence: VERY_HIGH

  - fact_id: FACT-D04-005
    statement: SK온과 Factorial은 전고체 제조 타당성 검토 MOU를 체결했다.
    entity_ids:
      - PART-FACTORIAL
    evidence_type: PARTNER_CONFIRMED
    confidence: VERY_HIGH

  - fact_id: FACT-D04-006
    statement: On-Vent 기술은 각형 캔에 레이저로 벤트를 형성하는 기술이다.
    entity_ids:
      - TECH-SKON-D04-006
      - TECH-SKON-D04-061
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
```

---

## 50.2 ANALYSIS Registry

```yaml
analysis_registry:

  - analysis_id: ANA-D04-001
    statement: >
      Solid Power와 Factorial은 동일한 기술을 중복 도입하는 관계라기보다,
      황화물 전해질·셀 공정과 기존 라인 호환성이라는 서로 다른
      상용화 옵션을 제공한다.
    supporting_entities:
      - PART-SOLID-POWER
      - PART-FACTORIAL
    confidence: HIGH

  - analysis_id: ANA-D04-002
    statement: >
      건식전극 상용화의 핵심 병목은 소재의 존재보다 분말균일성,
      접착력, 캘린더링과 양산수율의 동시 확보다.
    supporting_entities:
      - TECH-SKON-D04-003
      - TECH-SKON-D04-048
      - TECH-SKON-D04-052
      - TECH-SKON-D04-039
    confidence: HIGH

  - analysis_id: ANA-D04-003
    statement: >
      Hyper Fast의 경쟁력을 실제 고객가치로 전환하려면 충전시간 외에
      저온성능, 반복 급속충전 수명, 충전기 통신과 차량 열관리 검증이 필요하다.
    supporting_entities:
      - TECH-SKON-D04-005
      - TECH-SKON-D04-043
      - TECH-SKON-D04-016
    confidence: HIGH

  - analysis_id: ANA-D04-004
    statement: >
      AI Researcher·공정 AI·BaaS AI를 공통 데이터모델로 연결하면
      설계-제조-필드 데이터를 잇는 장기 인텔리전스 구조가 가능하다.
    supporting_entities:
      - TECH-SKON-D04-032
      - TECH-SKON-D04-039
      - TECH-SKON-D04-018
      - TECH-SKON-D04-064
    confidence: MEDIUM_HIGH
```

---

## 50.3 HYPOTHESIS Registry

```yaml
hypothesis_registry:

  - hypothesis_id: HYP-D04-001
    statement: >
      SK온이 Solid Power와 Factorial 플랫폼을 공통 사양으로 비교하면
      2027년 이전에 주력 전고체 플랫폼을 축소 선정할 수 있다.
    validation_needed:
      - Common cell specification
      - Yield comparison
      - Equipment conversion cost
      - Automotive validation

  - hypothesis_id: HYP-D04-002
    statement: >
      배터리 파운데이션 모델은 SK온의 AI Researcher와 Materials AI를
      통합하는 기반이 될 수 있다.
    current_status:
      - No official SK On foundation model confirmed

  - hypothesis_id: HYP-D04-003
    statement: >
      EIS·가스·온도·음향 데이터를 결합하면 단일 센서보다 ESS 이상감지
      선행시간과 원인분류 성능을 개선할 수 있다.
    validation_needed:
      - Controlled abuse test
      - False-alarm comparison
      - Field data

  - hypothesis_id: HYP-D04-004
    statement: >
      재작업 가능한 접착기술과 로봇 셀 제거기술이 확보되면
      CTP의 수리성과 폐기비용 문제를 줄일 수 있다.
    validation_needed:
      - Pack structural test
      - Thermal propagation test
      - Automated rework trial
```

---

# D04-50.1 Canonical Triple Registry Extension
