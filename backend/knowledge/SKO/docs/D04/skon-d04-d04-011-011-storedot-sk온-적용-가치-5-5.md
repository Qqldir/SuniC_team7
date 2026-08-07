---
id: skon-d04-d04-011-011-storedot-sk온-적용-가치-5-5
title: 011 — StoreDot — SK온 적용 가치 (5)
summary: StoreDot 기술이 SK온 배터리 시스템에서 어떤 기술 컴포넌트들과 연결되고 제품을 가능하게 하는지 보여주는 기술 관계 메타데이터.
tags: [d04, technology, schema]
keywords: [StoreDot, 기술 컴포넌트, 지식그래프, 메타데이터, Solid Power, 기술 의존성, 배터리, 제품 연계]
related: []
priority: normal
domain: D04
section: D04-011
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 011 — StoreDot
tokens: 3816
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 011 — StoreDot

```yaml
canonical_triples:

  - triple_id: TR-D04-001
    subject: TECH-SKON-D04-032
    predicate: HAS_COMPONENT
    object: TECH-SKON-D04-033
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-002
    subject: TECH-SKON-D04-032
    predicate: HAS_COMPONENT
    object: TECH-SKON-D04-034
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-003
    subject: TECH-SKON-D04-034
    predicate: USES
    object: TECH-SKON-D04-035
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-004
    subject: TECH-SKON-D04-034
    predicate: USES
    object: TECH-SKON-D04-036
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-005
    subject: TECH-SKON-D04-003
    predicate: HAS_PROCESS_COMPONENT
    object: TECH-SKON-D04-048
    evidence_type: OFFICIAL_DIRECT
    confidence: HIGH

  - triple_id: TR-D04-006
    subject: TECH-SKON-D04-003
    predicate: HAS_PROCESS_COMPONENT
    object: TECH-SKON-D04-052
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-007
    subject: TECH-SKON-D04-052
    predicate: OPTIMIZED_BY
    object: TECH-SKON-D04-039
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-008
    subject: TECH-SKON-D04-005
    predicate: HAS_ALGORITHM_COMPONENT
    object: TECH-SKON-D04-043
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-009
    subject: PROD-SKON-EV-006
    predicate: ENABLED_BY
    object: TECH-SKON-D04-005
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-010
    subject: PROD-SKON-EV-009
    predicate: ENABLED_BY
    object: TECH-SKON-D04-006
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-011
    subject: TECH-SKON-D04-006
    predicate: USES_PROCESS
    object: TECH-SKON-D04-061
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-012
    subject: PROD-SKON-ESS-002
    predicate: USES
    object: TECH-SKON-D04-008
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-013
    subject: PROD-SKON-ESS-002
    predicate: USES
    object: TECH-SKON-D04-009
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-014
    subject: TECH-SKON-D04-001
    predicate: HAS_MATERIAL_COMPONENT
    object: TECH-SKON-D04-069
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-015
    subject: TECH-SKON-D04-001
    predicate: PILOT_TECHNOLOGY_PARTNER
    object: PART-SOLID-POWER
    evidence_type: PARTNER_CONFIRMED
    confidence: VERY_HIGH

  - triple_id: TR-D04-016
    subject: CO-SKON
    predicate: EXPLORES_MANUFACTURING_WITH
    object: PART-FACTORIAL
    evidence_type: PARTNER_CONFIRMED
    confidence: VERY_HIGH

  - triple_id: TR-D04-017
    subject: TECH-SKON-D04-028
    predicate: CO_DEVELOPED_WITH
    object: PART-SK-ENMOVE
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-018
    subject: TECH-SKON-D04-031
    predicate: CO_DEVELOPED_WITH
    object: PART-STANDARD-ENERGY
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D04-019
    subject: TECH-SKON-D04-040
    predicate: CO_DEVELOPED_WITH
    object: PART-SIEMENS-DISW
    evidence_type: OFFICIAL_DIRECT
    confidence: HIGH

  - triple_id: TR-D04-020
    subject: TECH-SKON-D04-038
    predicate: HAS_EVIDENCE_SCOPE
    object: ANALYTICAL_TARGET
    evidence_type: ANALYSIS
    confidence: VERY_HIGH
```

---

## 이번 구간 완료

* Source Grade Normalization v2
* 기존 `78개` Technology ID 중 중복 `3개` 병합
* 활성 Canonical Technology Entity `75개`
* 14개 기술 패밀리로 통합 분류
* Product–Technology–Process 연결
* Partner–Technology Master
* 공식 TRL 대신 공개근거 기반 `EML` 성숙도 체계 도입
* 주요 기술별 EML 분류
* FACT·ANALYSIS·HYPOTHESIS 레이어 분리
* Canonical Triple Registry 확장

## 다음 시작점

`D04-51 Technology Chunk Library`

```text
D04-51 Technology Chunk Library
→ D04-52 Graph Query Templates
→ D04-53 Human-Readable Technology Report
→ D04-54 Data Quality & Gap Register
→ D04-55 Canonical Source Index
→ D04 Final YAML
→ D04 완료
```

[1]: https://askinno.com/global/archives/154271?utm_source=chatgpt.com "[SK On Institute of Future Technology] SK On's AI Researcher"
[2]: https://askinno.com/global/archives/153845?utm_source=chatgpt.com "[Battery Deep Dive] Part 3: The Dry Electrode Process"
[3]: https://askinno.com/global/archives/154394?utm_source=chatgpt.com "[Battery Deep Dive] Part 6: On-vent Prismatic Cell"
[4]: https://www.solidpowerbattery.com/investor-relations/investor-news/news-details/2026/Solid-Power-Reports-First-Quarter-2026-Results/default.aspx?utm_source=chatgpt.com "Solid Power Reports First Quarter 2026 Results"
[5]: https://factorialenergy.com/?utm_source=chatgpt.com "Factorial Energy: High-Performing Solid-State Batteries"

---

# SK온 D04 Technology Taxonomy

## Part 9. Chunk Library·Graph Query·Human Report·Data Quality·Final YAML

**문서 버전:** D04 v1.8
**기준일:** 2026-08-02
**이전 완료 지점:** `D04-50.1 Canonical Triple Registry Extension`
**이번 구간 신규 외부자료:** 없음
**근거 범위:** 기존 등록 `SRC-SKON-D04-001~046`, `SRC-RES-D04-047~051`, `SRC-EXT-D04-052~063`

---

# D04-51. Technology Chunk Library

## 51.1 Canonical Chunk Schema

```yaml
technology_chunk_schema:

  chunk_id:
    type: canonical_string
    required: true

  title:
    type: string
    required: true

  domain:
    fixed_value: D04

  company_id:
    fixed_value: CO-SKON

  chunk_text:
    type: natural_language
    required: true

  primary_entity_ids:
    type: array

  related_entity_ids:
    type: array

  product_ids:
    type: array

  process_ids:
    type: array

  partner_ids:
    type: array

  information_type:
    allowed_values:
      - FACT
      - ANALYSIS
      - HYPOTHESIS
      - MIXED

  evidence_scope:
    allowed_values:
      - OFFICIAL_DIRECT
      - PARTNER_CONFIRMED
      - PEER_REVIEWED
      - GOVERNMENT_BASELINE
      - ANALYTICAL_INTEGRATION

  maturity_status:
    type: controlled_vocabulary

  evidence_maturity_level:
    allowed_values:
      - EML_9
      - EML_8
      - EML_7
      - EML_6
      - EML_5
      - EML_4
      - EML_3
      - EML_NA

  source_ids:
    type: array
    required: true

  source_grades:
    allowed_values:
      - A_PLUS
      - A
      - B_PLUS
      - B

  confidence:
    allowed_values:
      - VERY_HIGH
      - HIGH
      - MEDIUM
      - LOW

  claim_status:
    allowed_values:
      - VERIFIED_FACT
      - MANUFACTURER_CLAIM
      - CORPORATE_TARGET
      - ANALYST_INFERENCE
      - HYPOTHESIS

  embedding_tags:
    type: array

  exclusions:
    description: >
      해당 청크를 근거로 단정해서는 안 되는 내용
```

---

## CH-SKON-D04-001 — High-Nickel NCM

```yaml
chunk_id: CH-SKON-D04-001
title: SK온 하이니켈 NCM 기술 플랫폼
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: COMMERCIALIZED
evidence_maturity_level: EML_9

chunk_text: >
  SK온의 상용 전기차 배터리 기술 기반은 하이니켈 NCM 양극과
  파우치 셀 제조기술이다. NCM622, NCM811과 NCM9 계열을 거쳐
  니켈 비중을 높이는 방향으로 발전했으며, 높은 용량과 에너지밀도를
  장점으로 한다. 니켈 비중이 높아질수록 열안정성, 가스 발생,
  입자균열과 전해액 계면반응의 관리가 중요해진다.

primary_entity_ids:
  - TECH-SKON-D04-011
  - TECH-SKON-D04-075

product_ids:
  - PROD-SKON-EV-001
  - PROD-SKON-EV-002
  - PROD-SKON-EV-003

source_ids:
  - SRC-SKON-D04-015
  - SRC-RES-D04-051

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - 하이니켈
  - NCM
  - NCM9
  - 단결정 양극
  - 에너지밀도

exclusions:
  - 초고니켈 단결정 연구를 현재 양산기술로 표현 금지
  - 제품별 정확한 양극조성과 에너지밀도 추정 금지
```

---

## CH-SKON-D04-002 — High-Voltage Mid-Nickel

```yaml
chunk_id: CH-SKON-D04-002
title: 고전압 미드니켈 기술
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: PROTOTYPE
evidence_maturity_level: EML_5

chunk_text: >
  SK온의 고전압 미드니켈 기술은 니켈 함량을 약 50~70% 수준으로
  낮춰 원재료비와 열안정성을 개선하고, 높은 작동전압으로 에너지밀도
  감소를 보완하려는 접근이다. 단결정 양극, 도핑과 양극 계면 보호용
  전해액 첨가제가 핵심 보조기술로 공개됐다. 고객과 양산시점은
  확인되지 않았다.

primary_entity_ids:
  - TECH-SKON-D04-012
  - TECH-SKON-D04-076

product_ids:
  - PROD-SKON-EV-008

source_ids:
  - SRC-SKON-D04-014
  - SRC-SKON-D04-016

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - 미드니켈
  - 고전압
  - 저코발트
  - 전해액 첨가제

exclusions:
  - 상용 고객이 확보된 제품으로 표현 금지
  - 미드니켈 제품의 정확한 전압·용량 추정 금지
```

---

## CH-SKON-D04-003 — LFP Densification

```yaml
chunk_id: CH-SKON-D04-003
title: LFP 전극 고밀도화
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: DEVELOPMENT
evidence_maturity_level: EML_5

chunk_text: >
  SK온은 LFP 전극 고밀도화, 셀 내부 비활성 공간 축소와 셀 치수
  최적화를 통해 파우치형 LFP의 체적 에너지밀도와 출력을 높이는
  기술을 개발하고 있다. 공개된 500Wh/L 수준은 개발목표이며,
  상용 양산셀의 검증사양이 아니다. 고밀도화가 과도하면 이온이동과
  전해액 함침이 저하될 수 있어 수명·출력과의 균형이 필요하다.

primary_entity_ids:
  - TECH-SKON-D04-007

product_ids:
  - PROD-SKON-EV-007
  - PROD-SKON-ESS-001

source_ids:
  - SRC-SKON-D04-010

source_grades:
  - A

confidence: VERY_HIGH
claim_status: CORPORATE_TARGET

embedding_tags:
  - LFP
  - 전극 고밀도화
  - 500Wh/L
  - 저온성능
  - ESS

exclusions:
  - 500Wh/L를 양산 실적이나 고객 인증값으로 표현 금지
```

---

## CH-SKON-D04-004 — Silicon Anode Technology Chain

```yaml
chunk_id: CH-SKON-D04-004
title: 실리콘 음극·이중층 음극·자기정렬 기술
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: PRODUCT_TECHNOLOGY_DISCLOSED
evidence_maturity_level: EML_8

chunk_text: >
  SK온의 급속충전 기술에는 실리콘-흑연 복합 음극, 이중층 음극과
  자기정렬 공정이 포함된다. SF+는 고용량 실리콘층과 저저항
  흑연층을 결합하고, Advanced SF는 흑연 입자의 방향성을 제어해
  이온 이동경로를 줄이는 방식이다. 주요 과제는 실리콘 팽창,
  초기 리튬 손실, 층간 접착과 입자정렬의 공정균일성이다.

primary_entity_ids:
  - TECH-SKON-D04-013
  - TECH-SKON-D04-014
  - TECH-SKON-D04-015
  - TECH-SKON-D04-050

product_ids:
  - PROD-SKON-EV-004
  - PROD-SKON-EV-005

source_ids:
  - SRC-SKON-D04-007
  - SRC-SKON-D04-033

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - 실리콘 음극
  - 이중층 코팅
  - 자기정렬
  - SF+
  - Advanced SF

exclusions:
  - 실리콘 함량·바인더·프리리치에이션 적용 여부 추정 금지
```

---

## CH-SKON-D04-005 — SUFast

```yaml
chunk_id: CH-SKON-D04-005
title: SUFast와 7분 급속충전
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: PROTOTYPE
evidence_maturity_level: EML_5

chunk_text: >
  SUFast는 전극설계와 충전 프로토콜을 공동 최적화하는 SK온의
  초급속충전 기술이다. 다중물리 시뮬레이션으로 SOC별 음극전위와
  온도를 분석하고 전류조건을 조정해 리튬 도금과 열화를 줄이는
  방향이다. Hyper Fast Battery에서 10%에서 80%까지 7분 미만
  충전성능이 공개됐지만, 이는 기술 시제품 결과다.

primary_entity_ids:
  - TECH-SKON-D04-005
  - TECH-SKON-D04-043

product_ids:
  - PROD-SKON-EV-006

source_ids:
  - SRC-SKON-D04-007
  - SRC-SKON-D04-033

source_grades:
  - A

confidence: VERY_HIGH
claim_status: MANUFACTURER_CLAIM

embedding_tags:
  - SUFast
  - Hyper Fast
  - 7분 충전
  - 리튬 도금
  - 충전 프로토콜

exclusions:
  - 양산차의 확정 충전성능으로 표현 금지
  - 반복 급속충전 수명과 저온성능을 검증됐다고 표현 금지
```

---
