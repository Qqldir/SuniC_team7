---
id: skon-d05-d05-41-legal-status-audit-batch-1
title: Legal-Status Audit Batch 1
summary: SK온의 배터리 관련 특허 6개 패밀리에 대한 현재 법적 지위를 국제 특허청 공개 정보로 검증한 감사 결과 보고서.
tags: [d05, rnd, schema, table]
keywords: [특허감사, 법적지위, 존속권리, 분할출원, 국제특허패밀리, 배터리기술, US특허, EP특허, 공개대기, 등록특허, 분할 출원, 법적 지위 감사, 배터리 특허, 청구항 범위, 우선권, 국제 특허 가족, 특허 심사 상태, 등록권 확인, EIS-BMS, 급속충전 전극]
related: []
priority: normal
domain: D05
section: D05-41.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 2149
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-41. Legal-Status Audit Batch 1

## 41.1 감사 범위와 제한

```yaml
legal_status_audit_batch_1:

  families:
    - PF-SKON-D05-002 Fast-Charging Electrode
    - PF-SKON-D05-003 Dry Electrode Sheet
    - PF-SKON-D05-023 EIS-Based BMS
    - PF-SKON-D05-025 On-Vent Cross Notch
    - PF-SKON-D05-026 On-Vent H Pattern
    - PF-SKON-D05-027 Direct-to-Pack Pouch Cell

  audit_level:
    patent_document_reconciliation: COMPLETE
    family_member_reconciliation: PARTIAL
    official_register_confirmation: PENDING

  warning: >
    아래 상태는 특허공개문서와 Google Patents 법적 이벤트를
    대조한 결과이며 공식 법률의견이나 최종 존속권리 확인이 아니다.
```

---

## AUDIT-D05-001 — Fast-Charging Electrode

```yaml
audit_id: AUDIT-D05-001
patent_family_id: PF-SKON-D05-002

us_parent:
  application_number: US17/486032
  publication_number: US20220102727A1
  registration_number: US12100839B2
  grant_date: 2024-09-24
  snapshot_status: GRANTED_ACTIVE

us_divisionals:
  - application_number: US18/545091
    publication_number: US20240120485A1
    snapshot_status: PENDING

  - application_number: US18/545205
    publication_number: US20240154122A1
    snapshot_status: PENDING

country_members_identified:
  - KR102695826B1
  - CN114335413B
  - JP7801868B2
  - EP3975284A1

owner_snapshot:
  - SK On

audit_conclusion:
  - Parent US patent granted
  - Two US divisional applications remain open in snapshot
  - Claim-scope overlap among parent and divisionals requires review

official_register_status: PENDING
confidence: HIGH
```

미국 모출원은 2024년 등록됐고, 동일 우선권을 주장하는 두 건의 분할출원이 계류 중인 것으로 표시된다. 따라서 급속충전 전극의 미국 권리범위는 모특허 하나만이 아니라 분할출원의 향후 청구항까지 포함해 봐야 한다. ([구글 특허][4])

---

## AUDIT-D05-002 — Dry Electrode Sheet

```yaml
audit_id: AUDIT-D05-002
patent_family_id: PF-SKON-D05-003

ep_case:
  application_number: EP23174746.0
  publication_number: EP4283698A1
  priority_date: 2022-05-23
  snapshot_status: PUBLISHED_PENDING

inventors:
  - Young Jun Kim
  - Yong Hee Kang
  - Dong Hoon Lee
  - Hyo Sung Lim

owner_snapshot:
  - SK On

related_but_not_merged:
  - EP4283697A1
  - EP4276933A1

audit_conclusion:
  - EP4283698 remains pending in available snapshot
  - Similar titles do not prove a single family
  - Independent claims must be compared before consolidation

official_register_status: PENDING
confidence: MEDIUM_HIGH
```

EP4283698A1은 2022년 5월 우선권을 가지며 SK온 출원으로 나타나고, 공개자료상 심사 중인 상태다. `EP4283697A1`과 `EP4276933A1`은 제목이 유사하지만 별도 발명 또는 형제 출원일 수 있어 자동 병합하지 않는다. ([구글 특허][6])

---

## AUDIT-D05-003 — EIS-Based BMS

```yaml
audit_id: AUDIT-D05-003
patent_family_id: PF-SKON-D05-023

ep_case:
  application_number: EP24213157.1
  publication_number: EP4556923A1
  registration_number: EP4556923B1
  grant_publication_date: 2026-04-15
  snapshot_status: GRANTED_ACTIVE

other_members:
  us:
    publication_number: US20250164574A1
    snapshot_status: PENDING

  kr:
    publication_number: KR20250072203A
    snapshot_status: PENDING

  cn:
    publication_number: CN120015971A
    snapshot_status: PENDING

owner_snapshot:
  - SK On

audit_conclusion:
  - European case reached grant publication
  - US, KR and CN members remain application-stage in snapshot
  - EP grant does not establish enforceability in all designated states

official_register_status:
  ep_register: PENDING_DIRECT_CONFIRMATION
  national_validation: NOT_AUDITED

confidence: HIGH
```

EP4556923B1은 2026년 4월 15일 등록공개된 것으로 나타나며, 미국·한국·중국 대응문서는 여전히 출원공개 단계로 표시된다. 유럽 특허가 등록됐더라도 실제 국가별 유효화·연차료·무효절차는 별도 감사가 필요하다. ([구글 특허][7])

---

## AUDIT-D05-004 — On-Vent Cross-Notch

```yaml
audit_id: AUDIT-D05-004
patent_family_id: PF-SKON-D05-025

us_case:
  application_number: US18/331935
  publication_number: US20230411777A1
  registration_number: US11996579B2
  grant_date: 2024-05-28
  snapshot_status: GRANTED_ACTIVE

priority:
  earliest_date: 2022-06-15
  korean_improvement_application:
    - KR10-2023-0044246

owner_snapshot:
  - SK On

official_register_status: PENDING
confidence: HIGH
```

---

## AUDIT-D05-005 — On-Vent H-Pattern

```yaml
audit_id: AUDIT-D05-005
patent_family_id: PF-SKON-D05-026

us_case:
  application_number: US18/331998
  publication_number: US20230411778A1
  registration_number: US11990637B2
  grant_date: 2024-05-21
  snapshot_status: GRANTED_ACTIVE

priority:
  earliest_date: 2022-06-15
  korean_improvement_application:
    - KR10-2023-0043968

owner_snapshot:
  - SK On

official_register_status: PENDING
confidence: HIGH
```

두 On-Vent 미국 사건은 각각 별도의 한국 우선권·노치구조를 가지며, 2024년 5월 서로 다른 등록번호로 허여됐다. 동일 발명자와 우선일만으로 하나의 특허군으로 합칠 수 없다. ([구글 특허][5])

---

## AUDIT-D05-006 — Direct-to-Pack Pouch Cell

```yaml
audit_id: AUDIT-D05-006
patent_family_id: PF-SKON-D05-027

us_parent:
  application_number: US17/560536
  publication_number: US20220209325A1
  registration_number: US12113191B2
  grant_date: 2024-10-08
  snapshot_status: GRANTED_ACTIVE

us_continuation:
  application_number: US18/817808
  publication_number: US20240421375A1
  snapshot_status: PENDING

other_members:
  - EP4020690A1
  - KR102848976B1
  - CN114678641A

ownership_history:
  original_applicant:
    - SK Innovation
  current_owner_snapshot:
    - SK On

audit_conclusion:
  - US parent granted
  - US continuation remains pending
  - Korean member is shown as registered
  - EP and CN members require official status review

official_register_status: PENDING
confidence: HIGH
```

미국 모특허는 2024년 등록됐으며, 직접 팩 탑재·열교환면·가스채널과 관련된 후속 계속출원이 계류 중이다. 이 패밀리는 SK이노베이션 명의로 출원된 뒤 SK온으로 이전된 이력이 표시된다. ([구글 특허][8])

---

## 41.2 Batch 1 Status Matrix

| Family                  | US      | EP   | KR     | CN    | 최종 감사 |
| ----------------------- | ------- | ---- | ------ | ----- | ----- |
| Fast-Charging Electrode | 등록+분할계류 | 공개출원 | 등록표시   | 등록표시  | 미완료   |
| Dry Electrode           | 미확인     | 계류   | 추가 확인  | 추가 확인 | 미완료   |
| EIS BMS                 | 계류      | 등록공개 | 계류     | 계류    | 미완료   |
| On-Vent Cross           | 등록      | 미확인  | 우선권 확인 | 미확인   | 미완료   |
| On-Vent H               | 등록      | 미확인  | 우선권 확인 | 미확인   | 미완료   |
| Direct-to-Pack Pouch    | 등록+계속계류 | 계류표시 | 등록표시   | 계류표시  | 미완료   |

---
