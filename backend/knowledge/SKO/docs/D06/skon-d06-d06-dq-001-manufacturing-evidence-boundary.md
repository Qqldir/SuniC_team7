---
id: skon-d06-d06-dq-001-manufacturing-evidence-boundary
title: 001. Manufacturing Evidence Boundary
summary: "SK온의 배터리 제조공정에서 공개 가능한 정보와 기밀 정보의 경계를 명시하고, 공식 자료·산업 기준·비공개 항목을 분류하는 증거 정책 기준 문서다."
tags: [d06, process, schema]
keywords: [공개 정책, 비공개 정보, 공정 레시피, 산업표준, 설비 사양, 기밀 관리, 금지된 추론, 공식자료, 배터리 제조공정, 공개 기준, 기밀 정보, 레시피, 공정 기술, 리튬이온, 수율, OEE, 증거 등급, 양산 공정]
related: []
priority: normal
domain: D06
section: D06-DQ
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 479
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-DQ-001. Manufacturing Evidence Boundary

D06에서 가장 중요한 원칙은 **일반 배터리 제조공정과 SK온 실제 공정조건을 분리하는 것**이다.

```yaml
manufacturing_evidence_policy:

  sk_on_direct:
    definition: >
      SK온 공식자료에서 공정명·기술·적용방식이 직접 확인된 경우

    permitted_fields:
      - Process existence
      - Technology name
      - General operating principle
      - Partnership
      - Development or prototype status

    evidence_level: DIRECT_OFFICIAL
    source_grade: A

  industry_baseline:
    definition: >
      정부 연구소·학술자료에서 확인되는 일반적인 리튬이온
      배터리 제조공정

    permitted_fields:
      - Generic process flow
      - Generic equipment type
      - Typical control-variable category
      - Generic defect mechanism

    evidence_level: INDUSTRY_BASELINE
    source_grade: A_PLUS

  sk_on_not_disclosed:
    fields:
      - Actual recipe
      - Solids content
      - Mixing time
      - Coating speed
      - Oven temperature
      - Electrode loading
      - Electrode porosity
      - Line speed
      - Yield
      - Scrap rate
      - OEE
      - Formation protocol
      - Equipment vendor by plant

  prohibited_inference:
    - 산업 평균값을 SK온 공정값으로 저장
    - 특허 실시예를 실제 양산 Recipe로 저장
    - 파일럿 기술을 글로벌 전 공장 적용기술로 표현
    - 공개된 목표효과를 실제 수율개선 실적으로 표현
```

---
