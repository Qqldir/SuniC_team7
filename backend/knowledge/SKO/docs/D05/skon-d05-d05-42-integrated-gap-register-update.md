---
id: skon-d05-d05-42-integrated-gap-register-update
title: Integrated Gap Register Update
summary: "SK온 D05의 특허·발명자 데이터 통합 구축 중 식별된 6개 갭(발명자 신원, 특허상태, 청구범위, AI발명 등)과 진행 현황을 정리한 감사 등록부다."
tags: [d05, rnd, schema]
keywords: [발명자 신원 검증, 특허 상태 감사, 공동연구 IP, 특허 패밀리, 연구자 네트워크, KIPRIS, USPTO, 청구범위 매핑, AI 보조 발명, 특허 감사, 발명자 신원, KIPRIS/USPTO, AI-assisted invention, 검증 등급, Patent Family, Legal-Status Audit]
related: []
priority: normal
domain: D05
section: D05-42.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1317
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-42. Integrated Gap Register Update

```yaml
integrated_gaps:

  - gap_id: GAP-D05-INT-001
    subject: Inventor identity
    gap:
      - Korean-name reconciliation
      - ORCID
      - Employment period
    priority: HIGH

  - gap_id: GAP-D05-INT-002
    subject: Official patent status
    gap:
      - Direct KIPRIS audit
      - Direct USPTO Patent Center audit
      - EP national-validation audit
      - CNIPA and J-PlatPat audit
    priority: VERY_HIGH

  - gap_id: GAP-D05-INT-003
    subject: Patent claim coverage
    gap:
      - Parent versus divisional claims
      - Continuation claims
      - Product implementation claim chart
    priority: VERY_HIGH

  - gap_id: GAP-D05-INT-004
    subject: Researcher capability continuity
    gap:
      - Key-person dependency
      - Technical successor
      - Tacit-knowledge capture
    priority: HIGH

  - gap_id: GAP-D05-INT-005
    subject: Joint research IP
    gap:
      - KICET photonic-sintering ownership
      - Dankook LLZO improvement rights
      - University publication-review clauses
    priority: VERY_HIGH

  - gap_id: GAP-D05-INT-006
    subject: AI-assisted invention
    gap:
      - Human contribution record
      - Model and prompt log
      - Vendor ownership
      - Customer-data confidentiality
    priority: VERY_HIGH
```

---

## 이번 구간 완료

* 연구자 Entity Master 확장
* 논문 저자–특허 발명자 교차검증
* `VERIFIED / PROBABLE / UNRESOLVED` 식별등급 적용
* 광소결 연구자의 논문–특허 연결 검증
* 초고니켈 연구자의 신규 양극 특허 후보 등록
* Patent Family–Inventor Network 구축
* 연구조직 Capability Map 구성
* 공동연구·논문·IP Governance 모델 작성
* Legal-Status Audit Batch 1

  * 급속충전 전극
  * 건식전극
  * EIS BMS
  * On-Vent 2개 패밀리
  * Direct-to-Pack CTP
* 공식 등록부 직접 감사는 `PENDING`으로 분리

## 현재 D05 진행상태

```yaml
progress:
  rnd_organization_and_facilities: COMPLETE_V1
  rnd_program_master: COMPLETE_V1

  patent_family_master:
    confirmed_initial_families: 33
    candidate_families: 4

  paper_master:
    verified_papers: 7
    candidate_papers: 1

  researcher_network:
    sk_on_paper_authors: 11
    cross_role_researchers_verified: 5
    cross_role_researchers_probable: 1
    patent_only_core_inventors_registered: 4

  legal_status_audit:
    batch_1_document_reconciliation: COMPLETE
    batch_1_official_register_confirmation: PENDING

  joint_research_ip_governance: COMPLETE_V1
  organization_capability_map: COMPLETE_V1
```

## 다음 시작점

`D05-43 Legal-Status Audit Batch 2 & Claim-Scope Mapping`

```text
D05-43 Legal-Status Audit Batch 2
├── Z-Folding Legacy & Modern
├── Thermal Barrier
├── Battery Ledger
├── AI Fault Detection
├── SOH Estimation
├── Solid-State Composite Cathode
├── Li-Metal–Glass Electrolyte
└── Photonic-Sintered Electrolyte

→ D05-44 Independent-Claim Element Map
→ D05-45 Product–Patent Claim Mapping
→ D05-46 Patent Expiry·Geographic Coverage Map
→ D05-47 IP White-Space Analysis
```

[1]: https://patents.google.com/patent/EP4350830A1/en "EP4350830A1 - Oxide-based thin film sintered body, oxide-based solid electrolyte sheet, and all-solid lithium secondary battery - Google Patents"
[2]: https://patents.google.com/patent/US20240222617A1/zh "US20240222617A1 - Cathode active material for lithium secondary battery and lithium secondary battery including the same - Google Patents"
[3]: https://patents.google.com/patent/EP4708394A1/de "EP4708394A1 - Kathodenaktivmaterial für lithiumsekundärbatterie, kathode für lithiumsekundärbatterie damit und lithiumsekundärbatterie - Google Patents"
[4]: https://patents.google.com/patent/US20220102727A1/en?utm_source=chatgpt.com "Electrode for Secondary Battery Having Improved Fast Charging ..."
[5]: https://patents.google.com/patent/US11990637B2?utm_source=chatgpt.com "US11990637B2 - Secondary battery cell - Google Patents"
[6]: https://patents.google.com/patent/EP4283698A1/zh?utm_source=chatgpt.com "EP4283698A1 - Method and apparatus for preparing dry electrode sheet for secondary battery, dry electrode sheet for secondary battery, electrode for secondary battery, and secondary battery - Google Patents"
[7]: https://patents.google.com/patent/EP4556923B1/de?utm_source=chatgpt.com "EP4556923B1 - Batterieverwaltungssystem und verfahren zur steuerung davon - Google Patents"
[8]: https://patents.google.com/patent/US20220209325A1/en?utm_source=chatgpt.com "US20220209325A1 - Pouch Type Battery Cell and Battery Pack Including the Same - Google Patents"

---
