---
id: skon-d05-d05-27-official-legal-status-audit-protocol
title: Official Legal-Status Audit Protocol
summary: 특허족의 법적 상태를 표준화된 값으로 분류하고 관할권별로 검증하는 감사 절차와 우선순위 큐
tags: [d05, rnd, schema, table]
keywords: [특허 법적 지위, 출원 상태, KIPRIS, USPTO, 등록 심사, 특허 패밀리, 국제단계 PCT, 존속기간, 소유권 이전, 청구항, 특허족, 상태값 표준, 우선순위 큐, 포트폴리오 스냅샷, 존속기간 관리, 출원상태 분류, 관할권 검증]
related: []
priority: normal
domain: D05
section: D05-27.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1055
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-27. Official Legal-Status Audit Protocol

## 27.1 상태값 표준

```yaml
official_legal_status_vocabulary:

  FILED_UNPUBLISHED:
    meaning: 출원됐으나 공개 전

  PUBLISHED_PENDING:
    meaning: 공개됐으며 심사 또는 등록절차 진행 중

  GRANTED_ACTIVE:
    meaning: 등록되고 존속 중

  GRANTED_LAPSED:
    meaning: 등록됐으나 연차료·기간·포기 등으로 소멸

  REJECTED_FINAL:
    meaning: 최종 거절 확정

  WITHDRAWN_OR_ABANDONED:
    meaning: 취하·포기·미응답 종료

  PCT_CEASED:
    meaning: PCT 국제단계 종료
    warning: 국가단계 권리와 별도

  EXPIRED:
    meaning: 존속기간 만료

  STATUS_UNVERIFIED:
    meaning: 공식 등록부 미검증
```

---

## 27.2 Jurisdiction Audit Workflow

```text
Patent Family
    ↓
Earliest Priority Application Verification
    ↓
PCT Publication and National-Phase List
    ↓
KR — KIPRIS
    ↓
US — Patent Center + Assignment
    ↓
EP — European Patent Register
    ↓
CN — CNIPA Record
    ↓
JP — J-PlatPat
    ↓
Current Assignee and Maintenance Status
    ↓
Remaining Claim Scope
    ↓
Canonical Family Status
```

---

## 27.3 Priority Audit Queue

| 우선순위 | Patent Family          | 감사 사유                 |
| ---- | ---------------------- | --------------------- |
| 1    | PF-D05-002 급속충전 전극     | Hyper Fast 핵심·분할출원 존재 |
| 2    | PF-D05-003 건식전극        | 양산전략 핵심·유사 패밀리 다수     |
| 3    | PF-D05-023 EIS BMS     | GRIDON 직접 연계          |
| 4    | PF-D05-025~026 On-Vent | 각형 신규사업 핵심            |
| 5    | PF-D05-027~029 CTP     | S-Pack+·멀티폼팩터 연계      |
| 6    | PF-D05-011~012 전고체     | 황화물·외부 공동 IP          |
| 7    | PF-D05-032~033 산화물 전고체 | 광소결·대학 공동출원           |
| 8    | PF-D05-030~031 X-ray   | 제조수율·검사장비 협업 연계       |

---

## 27.4 Family Audit Record Schema

```yaml
patent_legal_audit_record:

  audit_id: required
  patent_family_id: required
  jurisdiction: required

  application_number: required
  publication_number: required
  registration_number: optional

  official_status: required
  status_effective_date: required
  next_fee_date: optional
  expiration_date: optional

  original_applicant: required
  current_owner: required
  assignment_events: array

  claim_status:
    independent_claims_alive: optional
    amended_claim_summary: optional
    opposition_or_invalidity: optional

  official_register_source: required
  audited_at: required
  auditor_notes: optional
```

---

# D05-28. Updated Patent Portfolio Snapshot

```yaml
patent_portfolio_snapshot_v3:

  confirmed_initial_families:
    previous_total: 24
    newly_registered: 9
    current_total: 33

  candidate_families:
    count: 2
    ids:
      - PF-CAND-SKON-D05-001
      - PF-CAND-SKON-D05-002

  new_clusters_completed:
    - On-Vent Prismatic Cell
    - Direct-to-Pack Pouch Architecture
    - CTP and CTC Thermal Path
    - X-Ray Manufacturing Inspection
    - Photonic-Sintered Oxide Electrolyte
    - Joint LLZO Ceramic IP

  false_positive_patents_excluded:
    count: 3
    categories:
      - External CTP cooling
      - External immersion cooling
      - External multilayer separator

  official_status_audit:
    protocol: COMPLETE
    execution: NOT_STARTED

  portfolio_quality:
    technology_mapping: HIGH
    family_boundary_quality: MEDIUM_HIGH
    ownership_quality: MEDIUM_HIGH
    official_legal_status_quality: LOW_PENDING_AUDIT
```

---
