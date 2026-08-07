---
id: skon-d06-d06-dq-003-cell-finishing-evidence-boundary
title: 003. Cell Finishing Evidence Boundary
summary: 셀 마무리 공정 단계에서 SK온이 공개한 정보(특허 개발 중 기술)와 비공개 정보(Recipe·온도·합격기준)의 경계를 명시한 정책 문서다.
tags: [d06, process, schema]
keywords: [포메이션, 디개싱, 에이징, 공개 정책, 특허, 양산 공정, X-ray검사, 용량등급, 검사기준, 특허 개발, 셀 검사, 공개 정보, 비공개 정보, Recipe, 합격기준, 충방전]
related: []
priority: normal
domain: D06
section: D06-DQ
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 565
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# SK온 D06 Manufacturing Process & Operations

## Part 3. Formation·Degassing·Aging·Grading·End-of-Line Inspection

**문서 버전:** D06 v1.2
**기준일:** 2026-08-02
**이전 완료 지점:** `D06-18 Cell Assembly OI Seeds`

> 포메이션·디개싱·에이징의 세부 순서와 반복횟수는 셀 화학계·설계·제조사에 따라 달라질 수 있다. 아래 공정흐름은 공개 연구와 SK온 특허문서를 결합한 구조이며, SK온의 실제 충방전 Recipe·온도·시간·합격기준은 공개되지 않았다.

---

# D06-DQ-003. Cell Finishing Evidence Boundary

```yaml
cell_finishing_evidence_policy:

  sk_on_confirmed:
    permitted:
      - Formation process exists
      - Formation-stage defect detection is under patent development
      - Pre-charging and cell inspection systems are under patent development
      - X-ray, short, charging-resistance and appearance inspections are contemplated
      - Pouch insulation and thermographic inspection is under patent development
      - Seal inspection using pressure or tracer gas is under patent development

    not_permitted:
      - Patent application equals mass-production deployment
      - Patent example equals actual factory recipe
      - Patent inspection threshold equals commercial acceptance limit
      - Pending application equals enforceable patent right

  industry_baseline:
    permitted:
      - Generic formation purpose
      - Generic aging and retention-test role
      - Generic cell grading variables
      - Generic energy and inventory burden
      - Generic defect mechanisms

  sk_on_not_disclosed:
    - Initial charge current
    - Charge-voltage steps
    - Number of cycles
    - Rest duration
    - Formation temperature
    - Stack pressure during formation
    - Degassing timing
    - Aging temperature and duration
    - Capacity and resistance grade limits
    - Factory-specific yield
```

---
