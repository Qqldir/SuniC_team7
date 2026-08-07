---
id: skon-d06-d06-02-manufacturing-process-entity-schema
title: Manufacturing Process Entity Schema
summary: "배터리 제조공정의 데이터 스키마 정의와 원재료 입고부터 등급분류까지 주요 18개 공정의 ID, 소유권, 공개 수준을 명시한 마스터 테이블."
tags: [d06, process, core-candidate, schema, table]
keywords: [공정 메타데이터, 배터리 제조공정, 스키마 정의, 전극 공정, 공개 수준, 공정 레이어, 소유권 범위, 공정 마스터, 제조공정 구조, 공정 파라미터, 품질 속성, 검사 방법, 배터리 공정, Process ID]
related: []
priority: critical
domain: D06
section: D06-02.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1162
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-02. Manufacturing Process Entity Schema

```yaml
manufacturing_process_schema:

  process_id:
    required: true

  canonical_name:
    required: true

  korean_name:
    required: true

  process_layer:
    allowed_values:
      - MATERIAL
      - ELECTRODE
      - CELL_ASSEMBLY
      - CELL_FINISHING
      - MODULE_PACK
      - DIGITAL_QUALITY

  ownership_scope:
    allowed_values:
      - SK_ON_CONFIRMED
      - SK_ON_DEVELOPMENT
      - INDUSTRY_BASELINE
      - ANALYTICAL_TARGET

  input_material_ids:
    type: array

  output_object_ids:
    type: array

  upstream_process_ids:
    type: array

  downstream_process_ids:
    type: array

  equipment_classes:
    type: array

  critical_process_parameters:
    type: array

  critical_quality_attributes:
    type: array

  defect_modes:
    type: array

  inspection_methods:
    type: array

  environmental_requirements:
    type: array

  data_tags:
    type: array

  technology_ids:
    type: array

  patent_family_ids:
    type: array

  source_ids:
    type: array
    required: true

  evidence_level:
    required: true

  sk_on_parameter_disclosure:
    allowed_values:
      - DISCLOSED
      - PARTIALLY_DISCLOSED
      - NOT_DISCLOSED

  confidence:
    allowed_values:
      - VERY_HIGH
      - HIGH
      - MEDIUM
      - LOW
```

---

## 02.1 Process Entity Master

| Process ID   | 공정                           | Ownership         | 공개 수준       |
| ------------ | ---------------------------- | ----------------- | ----------- |
| PROC-D06-001 | 원재료 입고·검수                    | INDUSTRY_BASELINE | SK온 조건 미공개  |
| PROC-D06-002 | 저장·환경관리                      | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-003 | 계량·투입                        | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-004 | 습식 혼합                        | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-005 | 건식 혼합                        | SK_ON_DEVELOPMENT | 일부 공개       |
| PROC-D06-006 | 습식 코팅                        | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-007 | 건조·용매회수                      | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-008 | 캘린더링                         | SK_ON_DEVELOPMENT | AI 기술 일부 공개 |
| PROC-D06-009 | 슬리팅·노칭                       | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-010 | 최종 전극건조                      | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-011 | Z-Folding                    | SK_ON_CONFIRMED   | 원리 공개       |
| PROC-D06-012 | 탭·집전체 접합                     | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-013 | 파우치 성형·삽입                    | SK_ON_CONFIRMED   | 제품형식 공개     |
| PROC-D06-014 | 전해액 주입·함침                    | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-015 | 포메이션                         | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-016 | 가스제거·최종실링                    | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-017 | 에이징                          | INDUSTRY_BASELINE | 미공개         |
| PROC-D06-018 | 등급분류·셀 검사                    | INDUSTRY_BASELINE | 일부 특허 확인    |
| PROC-D06-019 | 모듈 조립                        | SK_ON_CONFIRMED   | 일반 구조       |
| PROC-D06-020 | CTP 조립                       | SK_ON_DEVELOPMENT | 시제품 구조      |
| PROC-D06-021 | 팩 조립·EOL                     | SK_ON_CONFIRMED   | 세부조건 미공개    |
| PROC-D06-022 | 제조 디지털 트윈                    | SK_ON_DEVELOPMENT | 협력 확인       |
| PROC-D06-023 | 지능형 생산설비                     | SK_ON_DEVELOPMENT | 협력 확인       |
| PROC-D06-024 | Manufacturing Digital Thread | ANALYTICAL_TARGET | 통합 플랫폼 미확인  |

---
