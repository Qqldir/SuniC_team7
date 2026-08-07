---
id: skon-d05-d05-43-legal-status-audit-batch-2
title: Legal-Status Audit Batch 2
summary: "SK온의 배터리 기술 관련 특허 3건(Z-폴딩 적층방법 2건, 열차단 모듈 1건)에 대한 법적 지위 감사 결과 및 등록·유지 상태를 정리한 문서."
tags: [d05, rnd, schema]
keywords: [특허 법적 상태, Z-Folding, 배터리 모듈, 열차단, PCT, 우선권, 전극 적층, 미국 특허, 한국 특허, 등록 상태, Z-폴딩, 배터리 특허, 특허 감사, PCT 국제특허, 열차단 모듈, 특허 가족, 소유권 이전, 한국 특허권]
related: []
priority: normal
domain: D05
section: D05-43.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 3240
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-43. Legal-Status Audit Batch 2

## AUDIT-D05-007 — Legacy Z-Folding

```yaml
audit_id: AUDIT-D05-007
patent_family_id: PF-SKON-D05-001
canonical_name: Legacy Z-Folding Cell Stack

identified_documents:
  pct:
    publication_number: WO2014042424A1
    application_number: PCT/KR2013/008211
    priority_date: 2012-09-14
    document_event_snapshot: PCT_CEASED

  korea:
    publication_or_grant_number: KR101553542B1
    document_type: GRANT_DOCUMENT_IDENTIFIED

applicant_at_filing:
  - SK Innovation

claim_focus:
  - Continuous separator
  - Zigzag folding
  - Alternating positive and negative electrode plates
  - Stacked cell assembly manufacturing

audit_conclusion:
  - Korean grant document exists
  - PCT international phase ended
  - National rights must be assessed separately
  - Current maintenance status of Korean patent is not verified

official_register_confirmation: PENDING
legal_status_confidence: LOW_TO_MEDIUM
```

WO2014042424A1은 2012년 9월 14일 한국 우선권을 기초로 한 Z-Folding 적층방법을 다루며, 한국 등록문서 KR101553542B1이 연결된다. PCT의 `ceased` 표시는 국제단계 종료를 뜻하며 한국 등록권리의 소멸을 의미하지 않는다. ([구글 특허][2])

---

## AUDIT-D05-008 — Modern Z-Folding Electrode Assembly

```yaml
audit_id: AUDIT-D05-008
patent_family_id: PF-SKON-D05-024
canonical_name: Modern Z-Folding Electrode Assembly

us_document:
  application_number: US18/450403
  publication_number: US20240063424A1
  filing_date: 2023-08-16
  earliest_priority_date: 2022-08-17
  applicant:
    - SK On
  document_status: APPLICATION_PUBLICATION_IDENTIFIED

claim_focus:
  - Continuous separator folded in zigzag form
  - Alternating cathode and anode plates
  - Anode plates at upper and lower outer surfaces
  - Separator wrapping around the electrode stack
  - Dimensional relationship among electrode plates

relationship_to_legacy_family:
  relation: IMPROVEMENT_FAMILY
  merge_status: DO_NOT_MERGE
  reason:
    - Different priority application
    - Different claim limitations
    - Different applicant era

official_register_confirmation: PENDING
legal_status_confidence: LOW
```

현대 Z-Folding 패밀리는 2012년의 기본 적층방법과 달리 최상·최하부 음극판, 전극 치수와 분리막 외곽구조를 추가로 구체화한다. 검토된 자료에서는 미국 공개출원은 확인됐지만 등록 여부는 공식 등록부에서 재확인해야 한다. ([구글 특허][3])

---

## AUDIT-D05-009 — Thermal Barrier Module

```yaml
audit_id: AUDIT-D05-009
patent_family_id: PF-SKON-D05-020
canonical_name: Battery Module Comprising Thermal Barrier

identified_us_documents:
  application_publication: US20220069377A1
  grant_document: US12155053B2

ownership_event_snapshot:
  transfer_to:
    - SK On
  record_date: 2022-11-07

claim_focus:
  - Multiple battery-cell blocks
  - Thermal barrier between cell blocks
  - Module housing
  - Suppression of heat transfer to adjacent cells
  - Battery pack incorporating the module

document_conclusion:
  - US grant document identified
  - Assignment event to SK On is reproduced in document history
  - Current maintenance and enforceability not officially audited

official_register_confirmation: PENDING
legal_status_confidence: MEDIUM
```

이 패밀리는 복수 셀 블록 사이에 열 차단부재를 배치하는 모듈·팩 구조를 다루며, 미국 등록문서와 SK온으로의 권리이전 이벤트가 확인된다. 다만 현재 권리 존속은 USPTO 공식 기록의 수수료·권리이전 상태를 추가 확인해야 한다. ([구글 특허][4])

---

## AUDIT-D05-010 — Battery Ledger

```yaml
audit_id: AUDIT-D05-010
patent_family_id: PF-SKON-D05-006
canonical_name: Battery Ledger Management System

identified_documents:
  us:
    application_publication: US20230009714A1
    grant_document: US12567011B2

  europe:
    application_publication: EP4116142A1
    grant_document: EP4116142B1

applicant:
  - SK On

claim_focus:
  - Unique battery ID
  - Production-information registration
  - Battery-state information
  - Vehicle and usage information
  - Charging, maintenance and replacement history
  - Battery lifecycle management

document_conclusion:
  - US and EP grant documents identified
  - The family protects lifecycle data architecture rather than a physical battery component
  - EP national validation and US maintenance status remain unaudited

official_register_confirmation: PENDING
legal_status_confidence: MEDIUM_HIGH
```

Battery Ledger 패밀리는 배터리별 고유 ID를 생성하고 생산정보, 상태정보와 사용·정비이력을 연결하는 구조를 청구한다. 미국과 유럽 등록문서가 확인되며 BaaS·잔존가치·배터리 여권의 기반 IP로 기술적으로 연결할 수 있다. ([구글 특허][5])

---

## AUDIT-D05-011 — AI Battery Fault Detection

```yaml
audit_id: AUDIT-D05-011
patent_family_id: PF-SKON-D05-007
canonical_name: AI-Based Battery Abnormality Detection

identified_us_document:
  grant_number: US12517185B2
  issue_date: 2026-01-06
  assignee_snapshot:
    - SK Innovation
    - SK On

claim_focus:
  - Cell-data measurement over a time period
  - Two-dimensional data representation
  - Time axis
  - Battery-cell-index axis
  - Pre-trained abnormality-detection model
  - Identification of abnormal battery cell

ownership_scope: SK_GROUP_JOINT_SNAPSHOT

document_conclusion:
  - US grant document identified
  - Joint ownership is shown in reviewed records
  - Maintenance and assignment chain require official confirmation

official_register_confirmation: PENDING
legal_status_confidence: MEDIUM
```

이 패밀리는 셀별 시계열 데이터를 `시간 × 셀 인덱스`의 2차원 입력으로 변환해 사전학습 모델로 이상 셀을 식별하는 구조를 다룬다. 미국 특허번호 12,517,185는 2026년 1월 6일 발행된 것으로 확인된다. ([구글 특허][6])

---

## AUDIT-D05-012 — Battery SOH Estimation

```yaml
audit_id: AUDIT-D05-012
patent_family_id: PF-SKON-D05-005
canonical_name: Method for Estimating State of Health of Battery

identified_documents:
  korea:
    grant_number: KR102424165B1
    grant_publication_date: 2022-07-25

  united_states:
    publication_number: US20230132102A1
    document_status: APPLICATION_PUBLICATION_IDENTIFIED

applicant:
  - SK On

technology_scope:
  - Battery degradation estimation
  - State-of-health estimation
  - Battery measurement data
  - Lifecycle and maintenance decision support

document_conclusion:
  - Korean grant document identified
  - US application publication identified
  - US grant status not confirmed in reviewed records

official_register_confirmation: PENDING
legal_status_confidence: MEDIUM
```

한국 등록문서 KR102424165B1과 미국 공개출원 US20230132102A1이 동일 SOH 추정기술군으로 연결된다. 다만 미국 절차상태와 한국 특허의 현재 존속상태는 공식 등록부 감사 전까지 확정하지 않는다. ([구글 특허][7])

---

## AUDIT-D05-013 — Sulfide ASSB Composite Cathode

```yaml
audit_id: AUDIT-D05-013
patent_family_id: PF-SKON-D05-011
canonical_name: Composite Cathode for All-Solid-State Lithium Battery

identified_documents:
  pct:
    publication_number: WO2024210345A1

  europe:
    application_number: EP24785054.8
    publication_number: EP4651239A1
    publication_date: 2025-11-19
    applicant:
      - SK On
    document_status: APPLICATION_PUBLICATION_IDENTIFIED

earliest_priority_date: 2023-04-06

claim_focus:
  - Composite cathode for all-solid-state lithium battery
  - Cathode active material
  - Sulfide solid electrolyte
  - Binder and composite-cathode stability
  - All-solid-state battery including the cathode

document_conclusion:
  - Official EPO application publication identified
  - No EP grant document identified in the reviewed source set
  - Application status requires European Patent Register confirmation

official_register_confirmation: PENDING
legal_status_confidence: MEDIUM
```

EPO 공식 공개공보는 EP4651239A1의 출원인을 SK온으로 기재하며, 전고체 리튬이차전지용 복합양극을 대상으로 한다. 이번 조사에서는 등록공보가 아니라 출원공개문서가 확인됐다. ([EPO Data][8])

---

## AUDIT-D05-014 — Lithium-Metal·Glass Electrolyte Laminate

```yaml
audit_id: AUDIT-D05-014
patent_family_id: PF-SKON-D05-012
canonical_name: Lithium-Metal and Glass-Electrolyte Laminate

pct_document:
  publication_number: WO2024025344A1
  application_number: PCT/KR2023/010851
  filing_date: 2023-07-26
  earliest_priority_date: 2022-07-28
  applicants:
    - SK On
    - PolyPlus Battery Company
  pct_event_snapshot: CEASED

identified_national_phase_references:
  - Korea
  - China
  - Japan
  - Europe

claim_focus:
  - Lithium-containing metal foil
  - Sulfide-based glass electrolyte film
  - Direct lamination using temperature and pressure
  - Improved adhesion and lower interfacial resistance
  - All-solid-state cell incorporating the laminate

ownership_scope: EXTERNAL_JOINT

document_conclusion:
  - PCT publication and national-phase references identified
  - PCT cessation does not determine national-phase status
  - Joint ownership and improvement rights require contract review

official_register_confirmation: PENDING
legal_status_confidence: LOW_TO_MEDIUM
```

WO2024025344A1은 SK온과 PolyPlus의 공동출원으로, 리튬 함유 금속박과 유리계 고체전해질층의 적층체를 다룬다. PCT 기록에는 국제단계 종료가 표시되지만 한국·중국·일본·유럽 국가단계 문서가 연결돼 있다. ([구글 특허][9])

---

## AUDIT-D05-015 — Photonic-Sintered Electrolyte

```yaml
audit_id: AUDIT-D05-015
patent_family_id: PF-SKON-D05-032
canonical_name: Photonic-Sintered Oxide Electrolyte Sheet

previously_registered_publication:
  - EP4350830A1
  - KR20240047292A

current_batch_retrieval:
  official_document_retrieved: false
  exact_patent_record_retrieved: false

confirmed_technology_evidence:
  - SK On–KICET photonic-sintering research
  - ACS Energy Letters publication
  - Corporate statement that related patent applications were filed

audit_conclusion:
  - Patent publication number remains in the provisional master
  - Current batch could not independently re-retrieve the exact document
  - Claim and legal-status analysis is suspended pending direct retrieval

status: REQUIRES_RETRIEVAL
legal_status_confidence: UNCONFIRMED
```

SK온은 KICET와 산화물·고분자 복합 고체전해질의 광소결 연구를 진행했고 관련 연구결과에 대한 특허출원을 언급했다. 그러나 이번 배치에서는 기존 등록번호의 정확한 특허문서를 재확보하지 못했으므로 상태와 청구범위를 확정하지 않는다. ([SK][10])

---
