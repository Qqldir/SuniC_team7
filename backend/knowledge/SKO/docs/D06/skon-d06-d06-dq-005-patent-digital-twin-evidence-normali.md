---
id: skon-d06-d06-dq-005-patent-digital-twin-evidence-normali
title: 005. Patent·Digital-Twin Evidence Normalization
summary: "SK온의 특허정보 신뢰도 기준과 디지털 트윈 구축 범위를 정정하는 문서로, 공개자료의 증거등급과 미확인 사항을 구분한다."
tags: [d06, process, schema, "xref:d05"]
keywords: [특허공보, Siemens Xcelerator, 스마트팩토리, 공식 등록부, 시뮬레이션, 협력 계획, 공개자료, 수율 개선, 특허정보 신뢰도, 법적 상태 검증, Google Patents, 디지털 트윈 범위, 제조공정 시뮬레이션, 공장 배포, 협력 현황]
related: []
priority: normal
domain: D06
section: D06-DQ
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 858
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# SK온 D06 Manufacturing Process & Operations

## Part 5. Smart Factory·OT·Digital Twin·OEE·Yield·Energy·Cybersecurity

**문서 버전:** D06 v1.4
**기준일:** 2026-08-02
**이전 완료 지점:** `D06-39 D05 Candidate Patent Backlog Update`

> 이번 구간은 SK온이 실제로 구축했다고 공개한 범위와, 향후 통합해야 할 제조 시스템 아키텍처를 분리한다. 시스템 구성·KPI·예지보전·에너지 최적화 항목 대부분은 `ANALYTICAL_TARGET`이며 SK온의 현재 전 공장 운영상태를 뜻하지 않는다.

---

# D06-DQ-005. Patent·Digital-Twin Evidence Normalization

## 1. 특허 미러 증거등급 정정

앞선 D06 Part 4에서 Google Patents를 통해 열람한 특허문서의 기술내용과 법적 상태가 동일한 증거수준으로 표현된 부분을 정정한다.

```yaml
patent_mirror_normalization:

  underlying_document:
    document_type: OFFICIAL_PATENT_PUBLICATION
    source_grade: A_PLUS
    technical_evidence_level: DIRECT_REGULATORY

  delivery_channel:
    value: PATENT_MIRROR
    example: Google Patents

  permitted_use:
    - Published applicant and inventor
    - Published description
    - Published claims
    - Priority and family discovery

  legal_status:
    official_register_verified: false
    permitted_status:
      - DOCUMENT_IDENTIFIED
      - GRANT_PUBLICATION_IDENTIFIED
      - APPLICATION_PUBLICATION_IDENTIFIED
      - OFFICIAL_STATUS_AUDIT_REQUIRED

  prohibited_status:
    - GRANTED_ACTIVE
    - CURRENT_OWNER_VERIFIED
    - EXACT_EXPIRATION_VERIFIED
```

즉 특허공보에 기재된 기술내용은 규제기관 공개문서에 근거하지만, 미러에 표시되는 현재 존속·연차료·양도정보는 공식 등록부 감사 전까지 확정하지 않는다.

---

## 2. Digital Twin 성과 경계

SK온은 2024년 Siemens Digital Industries Software와 스마트팩토리 구축 협력을 발표하고 Siemens Xcelerator의 디지털 트윈·시뮬레이션 기술을 활용할 계획이라고 밝혔다. 다만 공개자료는 협력과 활용계획을 확인할 뿐, 글로벌 전 공장 배포 완료나 수율·가동률 개선 수치를 제시하지 않는다. ([SK On][1])

```yaml
digital_twin_claim_boundary:

  confirmed:
    - SK On–Siemens DISW cooperation
    - Planned use of Xcelerator digital-twin software
    - Virtual production and process simulation objective

  not_confirmed:
    - Full global deployment
    - Factory-by-factory implementation
    - Quantified yield improvement
    - Quantified commissioning reduction
    - Quantified throughput improvement
    - Autonomous production control

  claim_status:
    cooperation: DIRECT_OFFICIAL
    expected_benefits: CORPORATE_TARGET
```

---
