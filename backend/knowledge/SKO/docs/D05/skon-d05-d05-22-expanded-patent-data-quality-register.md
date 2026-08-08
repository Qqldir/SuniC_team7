---
id: skon-d05-d05-22-expanded-patent-data-quality-register
title: Expanded Patent Data Quality Register
summary: "배터리 특허의 조성 혼동, 중복 패밀리, 소유권 오류 등 9가지 데이터 품질 이슈와 각각의 제어·개선 방안을 정리한 레지스터입니다."
tags: [d05, rnd, core-candidate, schema]
keywords: [특허 데이터 혼동, 하이니켈 양극, 특허 패밀리 중복, 우선권 비교, 분리막 소유권, KIPRIS, 데이터 통제, 특허 검증, PCT 국가단계, 특허 이슈, 하이니켈, 음극재, 분리막, 중복 위험, 소유권, 전해액, EIS, 데이터 검증]
related: []
priority: critical
domain: D05
section: D05-22.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 655
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-22. Expanded Patent Data Quality Register

```yaml
patent_data_quality_extension:

  - issue_id: DQ-D05-PAT-009
    issue: 하이니켈 양극의 초기 조성특허와 2026 단결정 연구특허 혼동 위험
    severity: HIGH
    control:
      - Separate patent families
      - Separate inventors and priority dates
      - Separate product and research maturity

  - issue_id: DQ-D05-PAT-010
    issue: 고전압 전해액 특허를 미드니켈 제품 적용특허로 단정할 위험
    severity: VERY_HIGH
    control:
      - Use PATENT_POSSIBLY_SUPPORTS
      - Require product or inventor confirmation

  - issue_id: DQ-D05-PAT-011
    issue: 실리콘 음극 유사 특허가 다수 존재해 중복 패밀리 가능
    severity: VERY_HIGH
    action:
      - Independent claim clustering
      - Priority-number comparison
      - Continuation and divisional review

  - issue_id: DQ-D05-PAT-012
    issue: SK온 자체 분리막 IP와 SKIET 분리막 IP 소유주체 혼동
    severity: VERY_HIGH
    control:
      - Applicant-based separation
      - Affiliate relationship only

  - issue_id: DQ-D05-PAT-013
    issue: Flame Blocking 동일 제목 후속출원 경계 미확정
    severity: HIGH
    action:
      - Priority application audit
      - Continuation chain audit

  - issue_id: DQ-D05-PAT-014
    issue: PCT 공개 후 국가단계 진입 전후 상태가 혼재
    affected:
      - PF-SKON-D05-022
    severity: HIGH
    action:
      - PATENTSCOPE national phase review

  - issue_id: DQ-D05-PAT-015
    issue: EIS 특허와 GRIDON 실제 알고리즘 동일성 미확인
    severity: HIGH
    control:
      - PATENT_TECHNICALLY_LINKED only

  - issue_id: DQ-D05-PAT-016
    issue: AI Researcher 관련 특허 부재를 영업비밀 보유로 단정할 위험
    severity: HIGH
    control:
      - Mark as SEARCH_GAP
      - Do not infer IP protection method without evidence

  - issue_id: DQ-D05-PAT-017
    issue: Google Patents의 2026 등록상태는 공식 등록부 검증 전 스냅샷
    severity: VERY_HIGH
    action:
      - USPTO Patent Center audit
      - EP Register audit
      - KIPRIS audit
```

---
