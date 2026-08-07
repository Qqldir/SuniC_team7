---
id: skon-d05-d05-63-d17-handoff-correction
title: D17 Handoff Correction
summary: "D17 핸드오프 프로세스의 특허, FTO, IP 섹션 상태를 수정하고 각 게이트별 심사 진행 시 허용·금지 사항을 정의한 문서"
tags: [d05, rnd, schema, table, "xref:d17"]
keywords: [특허, FTO, 자유실시권, 지적재산권, Hard Gate, RIGHTS_GATE, 기술검토, 파트너, 비침해, 법무, D17 핸드오프, 특허 FTO, IP 권리, 지식재산권, 침해 판단, 상태 수정, 라이선싱, 게이트 통과, 내부 심사 기준]
related: []
priority: normal
domain: D05
section: D05-63.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 400
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-63. D17 Handoff Correction

```yaml
d17_handoff_correction:
  previous_gap_label:
    d05: INCOMPLETE_PATENT_FTO_IP_SECTION

  corrected_label:
    d05_public_db: COMPLETE_V2
    patent_family_master: COMPLETE_PROVISIONAL
    claim_element_pre_map: COMPLETE_V1
    fto_priority_gate_cards: COMPLETE_V1
    joint_ip_rights_schema: COMPLETE_V1
    official_status: RECURRENT_DECISION_DATE_REFRESH
    product_claim_implementation: BLOCKED_INTERNAL_DATA
    confidential_contract_rights: BLOCKED_INTERNAL_LEGAL_REVIEW
    legal_fto_opinion: OUT_OF_SCOPE

  recommendation_rule:
    - A high D17 score cannot bypass RIGHTS_GATE
    - A high D17 score cannot bypass DECISION_DATE_STATUS_PACKET
    - Product mapping remains technical relevance until internal evidence is attached
    - External partner selection requires background-IP and improvement-right review
```

| Hard Gate | 통과 전 허용 | 통과 전 금지 |
|---|---|---|
| `STATUS_PACKET_READY` | Landscape, 기술검토, 공개특허 비교 | 현재 유효권리라고 단정 |
| `PRODUCT_ELEMENT_MAP_READY` | 기술적 연관성 평가 | 실시·비침해 판단 |
| `RIGHTS_GATE_PASS` | 파트너 탐색·기술 PoC 설계 | 상업제품 적용·재라이선스 약속 |
| `COUNSEL_REVIEW_PASS` | 내부 가설·회피설계 후보 | 최종 FTO·침해·유효성 결론 |

---
