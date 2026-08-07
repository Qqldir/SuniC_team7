---
id: skon-d04-d04-011-011-storedot-sk온-적용-가치-6-6
title: 011 — StoreDot — SK온 적용 가치 (6)
summary: "SK온의 배터리 팩 안전성 및 냉각 기술(열전파 방지, On-Vent, CTP·S-Pack+, 액침냉각)의 개발 수준과 상용화 현황을 평가하는 벤치마크 문서"
tags: [d04, technology, schema]
keywords: [열전파 방지, On-Vent, 레이저 벤트, CTP, 액침냉각, 무선 BMS, 배터리 팩 안전, 각형 셀, S-Pack+, 열관리, 배터리 팩 구조, 냉각 시스템, 셀 안전성, 벤트 설계]
related: []
priority: normal
domain: D04
section: D04-011
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 011 — StoreDot
tokens: 3664
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 011 — StoreDot

## CH-SKON-D04-006 — Thermal Propagation Prevention

```yaml
chunk_id: CH-SKON-D04-006
title: 열전파 방지 통합기술
information_type: MIXED
evidence_scope: OFFICIAL_DIRECT
maturity_status: DEVELOPMENT_AND_PRODUCT_INTEGRATION
evidence_maturity_level: EML_8

chunk_text: >
  SK온의 열전파 방지기술은 셀 열안정성, 셀 간 단열, 대면적 냉각,
  방향성 벤트, 가스 경로와 팩 구조를 결합하는 시스템 기술이다.
  특정 소재 하나가 아니라 이상 셀의 열과 가스가 인접 셀과 팩으로
  확산되는 것을 지연하거나 차단하는 다층 구조로 봐야 한다.

primary_entity_ids:
  - TECH-SKON-D04-002
  - TECH-SKON-D04-026
  - TECH-SKON-D04-016

source_ids:
  - SRC-SKON-D04-004
  - SRC-SKON-D04-017
  - SRC-SKON-D04-022
  - SRC-SKON-D04-023

source_grades:
  - A

confidence: HIGH
claim_status: ANALYST_INFERENCE

embedding_tags:
  - 열전파
  - 단열
  - 가스 경로
  - 팩 안전
  - 냉각

exclusions:
  - 모든 안전요소가 하나의 양산팩에 통합됐다고 단정 금지
```

---

## CH-SKON-D04-007 — On-Vent

```yaml
chunk_id: CH-SKON-D04-007
title: On-Vent 각형 셀과 레이저 가공
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: PROTOTYPE_VALIDATION
evidence_maturity_level: EML_5

chunk_text: >
  On-Vent는 각형 알루미늄 캔에 레이저로 벤트 노치를 직접 형성해
  파열압력과 가스 배출 위치·방향을 설계하는 기술이다. SK온은
  6,000회 이상의 반복 압력시험 후 목표 파열압력을 만족했다는
  자체 시험결과를 공개했다. 양산수율과 차량 적용은 확인되지 않았다.

primary_entity_ids:
  - TECH-SKON-D04-006
  - TECH-SKON-D04-061

product_ids:
  - PROD-SKON-EV-009

source_ids:
  - SRC-SKON-D04-008
  - SRC-SKON-D04-037

source_grades:
  - A

confidence: VERY_HIGH
claim_status: MANUFACTURER_CLAIM

embedding_tags:
  - On-Vent
  - 각형 셀
  - 레이저 벤트
  - 파열압력
  - 방향성 배출

exclusions:
  - OEM 인증이나 양산 적용이 완료됐다고 표현 금지
```

---

## CH-SKON-D04-008 — CTP·S-Pack+

```yaml
chunk_id: CH-SKON-D04-008
title: CTP와 S-Pack+ 통합 팩 기술
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: DEVELOPMENT
evidence_maturity_level: EML_5

chunk_text: >
  CTP는 모듈 단계를 줄이고 셀을 팩 구조에 직접 통합해 공간효율과
  원가경쟁력을 높이는 기술이다. S-Pack과 S-Pack+는 열 차단,
  절연, 가스·분진 배출과 구조지지 기능을 팩에 통합하는 SK온의
  CTP 기술 개념이다. 고객차량 적용과 양산 재작업성은 공개되지 않았다.

primary_entity_ids:
  - TECH-SKON-D04-004
  - TECH-SKON-D04-024
  - TECH-SKON-D04-025
  - TECH-SKON-D04-062

source_ids:
  - SRC-SKON-D04-006
  - SRC-SKON-D04-022
  - SRC-SKON-D04-023

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - CTP
  - S-Pack
  - S-Pack+
  - 모듈리스
  - 팩 조립

exclusions:
  - 상용 양산차 적용기술로 일반화 금지
```

---

## CH-SKON-D04-009 — EV Immersion Cooling·Wireless BMS

```yaml
chunk_id: CH-SKON-D04-009
title: EV 액침냉각과 무선 BMS
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: JOINT_DEVELOPMENT
evidence_maturity_level: EML_5

chunk_text: >
  SK온과 SK엔무브는 절연성 플루이드가 셀과 직접 접촉하는 EV용
  액침냉각 기술을 개발하고 있다. SK온의 무선 BMS는 셀 탭의
  무선 칩과 모듈 안테나를 이용해 케이블을 줄이고 플루이드 유동과
  팩 공간을 개선하는 구조다. 차량 양산적용과 기능안전 인증은
  확인되지 않았다.

primary_entity_ids:
  - TECH-SKON-D04-028
  - TECH-SKON-D04-029

partner_ids:
  - PART-SK-ENMOVE

source_ids:
  - SRC-SKON-D04-024
  - SRC-SKON-D04-025

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - 액침냉각
  - 무선 BMS
  - 절연유
  - 열관리
  - 배터리 여권

exclusions:
  - 상용차 적용·사이버보안 인증 완료로 표현 금지
```

---

## CH-SKON-D04-010 — GRIDON Safety Intelligence

```yaml
chunk_id: CH-SKON-D04-010
title: GRIDON EIS 진단과 냉각수 안전기술
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: PRODUCT_INTEGRATED
evidence_maturity_level: EML_8

chunk_text: >
  GRIDON은 EIS 기반 BMS와 냉각수 침지·화재대응 기술을 결합한
  SK온의 ESS 솔루션이다. EIS는 주파수별 임피던스 응답을 이용해
  내부상태와 이상징후를 분석하며, 냉각수 기술은 위험 발생 시 열과
  화재확산을 억제하는 역할을 한다. 장기 필드 가동률과 오탐률은
  공개되지 않았다.

primary_entity_ids:
  - TECH-SKON-D04-008
  - TECH-SKON-D04-009
  - TECH-SKON-D04-030

product_ids:
  - PROD-SKON-ESS-002
  - PROD-SKON-ESS-003

source_ids:
  - SRC-SKON-D04-011
  - SRC-SKON-D04-012
  - SRC-SKON-D04-020

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - GRIDON
  - EIS
  - ESS 안전
  - 예지진단
  - 냉각수

exclusions:
  - 공개되지 않은 진단정확도·RTE·보증수명 추정 금지
```

---

## CH-SKON-D04-011 — BaaS Health Intelligence

```yaml
chunk_id: CH-SKON-D04-011
title: BaaS AI·SOH·RUL·잔존가치
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: PARTNER_APPLICATION
evidence_maturity_level: EML_7

chunk_text: >
  BaaS AI는 주행·충전·전압·전류·온도 이력을 활용해 배터리 상태,
  이상징후, 잔여수명과 잔존가치를 분석하는 기술이다. 중고 EV 평가,
  렌터카와 차량관리 서비스에 적용된 이력이 확인된다. 모델 정확도,
  활성고객 수와 현재 매출은 공개되지 않았다.

primary_entity_ids:
  - TECH-SKON-D04-018
  - TECH-SKON-D04-019
  - TECH-SKON-D04-045

source_ids:
  - SRC-SKON-D04-018
  - SRC-SKON-D04-019
  - SRC-SKON-D04-034

source_grades:
  - A
  - A_PLUS

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - BaaS
  - SOH
  - RUL
  - 잔존가치
  - 플릿 분석

exclusions:
  - 진단 정확도와 유료서비스 규모를 임의 추정 금지
```

---

## CH-SKON-D04-012 — AI Researcher

```yaml
chunk_id: CH-SKON-D04-012
title: AI Researcher 기반 배터리 설계 자동화
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: INTERNAL_OPERATION
evidence_maturity_level: EML_7

chunk_text: >
  SK온의 AI Researcher는 고객 RFQ를 구조화하고 설계후보 생성,
  성능예측, 원가계산과 보고서 작성을 연결하는 내부 R&D 플랫폼이다.
  최종 양산성·안전성·고객적합성은 연구자가 검토한다. 공개된 시간·비용
  개선수치는 회사 기대효과이며 독립적으로 검증된 실적이 아니다.

primary_entity_ids:
  - TECH-SKON-D04-032
  - TECH-SKON-D04-033
  - TECH-SKON-D04-034
  - TECH-SKON-D04-035
  - TECH-SKON-D04-036
  - TECH-SKON-D04-037

source_ids:
  - SRC-SKON-D04-013
  - SRC-SKON-D04-029

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - AI Researcher
  - RFQ 분석
  - 셀 설계 AI
  - 성능예측
  - 원가계산

exclusions:
  - 완전자율 연구시스템으로 표현 금지
  - 회사 기대효과를 실현성과로 표현 금지
```

---

## CH-SKON-D04-013 — Dry Electrode

```yaml
chunk_id: CH-SKON-D04-013
title: 건식전극과 AI 캘린더링
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: PILOT_AND_DEVELOPMENT
evidence_maturity_level: EML_5

chunk_text: >
  건식전극은 용매 없이 활물질·도전재·바인더를 혼합하고 집전체에
  분말층을 형성·압착하는 기술이다. 건조로와 용매 회수설비를 줄일
  가능성이 있지만, 분말 균일성, 집전체 접착, 균열과 캘린더링 수율이
  핵심 병목이다. SK온은 캘린더링 변수의 AI 제어를 공개했다.

primary_entity_ids:
  - TECH-SKON-D04-003
  - TECH-SKON-D04-048
  - TECH-SKON-D04-052
  - TECH-SKON-D04-039

source_ids:
  - SRC-SKON-D04-005
  - SRC-SKON-D04-030
  - SRC-SKON-D04-035

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - 건식전극
  - 캘린더링
  - 분말 혼합
  - 공정 AI
  - 원가절감

exclusions:
  - 상업 양산수율과 실제 원가절감률 추정 금지
```

---

## CH-SKON-D04-014 — Z-Folding

```yaml
chunk_id: CH-SKON-D04-014
title: Z-Folding 정밀 적층
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: COMMERCIALIZED
evidence_maturity_level: EML_9

chunk_text: >
  Z-Folding은 연속된 분리막을 양극과 음극 사이에 지그재그로 접으며
  전극을 적층하는 SK온의 셀 조립기술이다. 전극 가장자리 접촉과
  내부단락 가능성을 낮추는 것이 핵심이다. 실제 라인속도, 정렬오차와
  불량률은 공개되지 않았다.

primary_entity_ids:
  - TECH-SKON-D04-022

source_ids:
  - SRC-SKON-D04-021
  - SRC-SKON-D04-036

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - Z-Folding
  - 전극 적층
  - 분리막
  - 내부단락
  - 정렬

exclusions:
  - 공개되지 않은 생산속도·불량률 제시 금지
```

---

## CH-SKON-D04-015 — Formation & Aging

```yaml
chunk_id: CH-SKON-D04-015
title: 포메이션·가스제거·에이징
information_type: FACT
evidence_scope: GOVERNMENT_BASELINE
maturity_status: INDUSTRY_BASELINE
evidence_maturity_level: EML_9

chunk_text: >
  포메이션은 초기 충·방전으로 전극 계면을 형성하고 셀을 활성화하는
  제조단계다. 가스제거와 최종 밀봉 이후 에이징을 통해 자가방전,
  전압안정성과 잠재불량을 확인한다. 공정시간·에너지·설비채널과
  재공재고가 주요 비용요인이다. SK온의 실제 프로토콜은 공개되지 않았다.

primary_entity_ids:
  - TECH-SKON-D04-058
  - TECH-SKON-D04-059

source_ids:
  - SRC-SKON-D04-039
  - SRC-SKON-D04-040
  - SRC-SKON-D04-041

source_grades:
  - A_PLUS

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - 포메이션
  - 에이징
  - 셀 활성화
  - 가스 제거
  - 셀 선별

exclusions:
  - 과거 DOE 공정시간·비용을 현재 SK온 값으로 적용 금지
```

---

## CH-SKON-D04-016 — Nondestructive Inspection

```yaml
chunk_id: CH-SKON-D04-016
title: 고속 비파괴 셀 검사
information_type: ANALYSIS
evidence_scope: GOVERNMENT_BASELINE
maturity_status: REQUIRED_CAPABILITY
evidence_maturity_level: EML_NA

chunk_text: >
  셀 내부의 전극 오정렬, 버, 이물, 용접결함과 밀봉불량을 고속으로
  검출하려면 비전, X-Ray, CT, 초음파, 열화상과 전기검사를 조합할
  수 있다. SK온이 어떤 검사장비를 전수 적용하는지는 공개되지 않았다.
  On-Vent·Z-Folding·CTP 양산성 검증을 위한 핵심 외부역량 후보이다.

primary_entity_ids:
  - TECH-SKON-D04-060

source_ids:
  - SRC-SKON-D04-040
  - SRC-SKON-D04-036
  - SRC-SKON-D04-037

source_grades:
  - A
  - A_PLUS

confidence: HIGH
claim_status: ANALYST_INFERENCE

embedding_tags:
  - 비파괴검사
  - X-Ray
  - CT
  - 초음파
  - 내부결함

exclusions:
  - SK온이 모든 후보 검사법을 사용한다고 표현 금지
```

---

## CH-SKON-D04-017 — Smart Factory
