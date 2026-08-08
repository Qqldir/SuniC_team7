---
id: skon-d05-d05-60-final-gap-disposition-register
title: Final Gap Disposition Register
summary: "SK온 D05 특허지식재산 관리의 8가지 데이터 품질 이슈(DQ-D05-FINAL-001~008)를 v2.0 분류체계로 재정의하고 공개DB 처리 방식, 담당자, 종료 조건을 지정하는 최종 등록부."
tags: [d05, rnd, schema, table]
keywords: [특허 정보, 지식재산권 관리, 데이터 품질, 공개DB 처리, 기밀정보 구분, 발명자 검증, Freedom to Operate, 경쟁사 분석, 계약 관리, 특허, IP, 지식재산, DQ, 공개 데이터베이스, Gap Disposition, FTO, 내부 검증, 영업비밀]
related: []
priority: normal
domain: D05
section: D05-60.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 831
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-60. Final Gap Disposition Register

| 기존 Issue | v2.0 분류 | 공개 DB 처리 | 종료 조건·Owner |
|---|---|---|---|
| DQ-D05-FINAL-001 공식 등록부 감사 | `RECURRENT_PUBLIC_REFRESH` | 정보원·필드·갱신주기 확정. 개별 권리의 최신 Snapshot은 의사결정 시 생성 | IP팀, G1·G3 전 30일 이내 Status Packet |
| DQ-D05-FINAL-002 Family 경계 | `PUBLIC_RECONCILIATION_QUEUE` | 우선권·분할·계속·독립청구항 기준 유지 | Patent Analyst, Priority 5부터 정규화 |
| DQ-D05-FINAL-003 제품 적용증거 | `BLOCKED_INTERNAL` | 기술적 연관성까지만 허용, 직접 실시 0건 유지 | 제품설계·공정 Owner가 BOM/Recipe 제공 |
| DQ-D05-FINAL-004 공동 IP 계약 | `BLOCKED_CONFIDENTIAL_CONTRACT` | 공개 관계와 필요한 권리필드만 등록 | Legal/IP가 원계약·변경계약 검토 |
| DQ-D05-FINAL-005 발명자 식별 | `PUBLIC_PLUS_HR_VALIDATION` | VERIFIED/PROBABLE/UNRESOLVED 유지 | HR·IP 발명신고 DB 대조 |
| DQ-D05-FINAL-006 논문 성능경계 | `CONTROL_IMPLEMENTED` | 연구셀·조건·상용검증 필드 의무화 | 별도 종료 불필요, 계속 적용 |
| DQ-D05-FINAL-007 경쟁사 Landscape | `DECLARED_SAMPLE_BASED` | 표본 기반이라는 한계와 금지결론 명시 | 특정 FTO 프로젝트에서만 확장 |
| DQ-D05-FINAL-008 AI Researcher IP | `PUBLIC_NO-DIRECT-FAMILY-IDENTIFIED` | ‘미확인’을 ‘부존재’로 해석 금지 | 내부 발명신고·영업비밀 원장 대조 |

```yaml
d05_gap_routing:
  public_refreshable:
    - Official procedural status
    - Published claim amendments
    - Recorded ownership transfers
    - Maintenance-fee events
    - Opposition and public invalidation events
    - Public continuation and divisional members
    - Newly published competitor families

  internal_validation_required:
    - Product BOM and cell architecture
    - Manufacturing recipe and tolerances
    - Supplier material formulation
    - Customer-specific implementation
    - License field of use
    - Improvement-invention ownership
    - Sublicensing and third-party material rights
    - Post-termination rights
    - Trade-secret designation and access log

  counsel_judgment_required:
    - Claim construction
    - Infringement and doctrine-of-equivalents analysis
    - Validity and enforceability opinion
    - Design-around sufficiency
    - Final FTO opinion
```

내부자료가 공개되지 않았다는 이유로 D05 전체를 계속 미완료로 두지 않는다. 과제가 G1을 통과해 실제 PoC·제품·투자결정으로 이동할 때 필요한 자료와 승인자를 명확히 지정한다.

---
