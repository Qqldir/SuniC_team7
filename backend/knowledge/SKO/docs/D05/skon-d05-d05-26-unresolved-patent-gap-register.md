---
id: skon-d05-d05-26-unresolved-patent-gap-register
title: Unresolved Patent Gap Register
summary: "기술 공개 이후에도 직접 대응하는 특허군이 확인되지 않은 사례들을 등록하고, 그 원인과 검색 전략, 그리고 결론 도출 시 준수할 원칙을 담은 문서."
tags: [d05, rnd, schema]
keywords: [특허 미확인, 배터리 기술, 특허 검색, 공동 출원, 영업 비밀, 특허 격차, EV 배터리, 기술 공개, 검색 거버넌스, 출원인 추적, 특허군, 미확인 기술, 공동출원, 영업비밀, 침지냉각, 무선BMS, 표면 코팅 리튬, 특허 검색 전략, 출원인 별칭]
related: []
priority: normal
domain: D05
section: D05-26.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 878
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-26. Unresolved Patent Gap Register

## 26.1 기술은 공개됐지만 직접 Patent Family가 확인되지 않은 영역

```yaml
unresolved_patent_gaps:

  - gap_id: GAP-D05-PAT-018
    technology: EV Immersion Cooling
    search_result:
      - No confirmed SK On-owned core family identified
      - GM immersion patent excluded as false positive
    possible_explanations:
      - Joint IP with SK Enmove
      - Unpublished application
      - Fluid formulation protected separately
      - Trade-secret pack design
    priority: VERY_HIGH

  - gap_id: GAP-D05-PAT-019
    technology: Wireless BMS
    search_result:
      - No direct SK On wireless cell-chip/antenna family confirmed
    required_search:
      - Wireless communication
      - Cell-tab transceiver
      - Module antenna
      - Battery passport identity
    priority: VERY_HIGH

  - gap_id: GAP-D05-PAT-020
    technology: Large-Surface Cooling
    search_result:
      - CTP thermal-contact patents identified
      - Exact large-surface cooling family not yet isolated
    priority: HIGH

  - gap_id: GAP-D05-PAT-021
    technology: Pouch-Integrated Prismatic
    search_result:
      - Pouch CTP and corner-lead patents identified
      - Aluminum outer-case integration family not confirmed
    priority: VERY_HIGH

  - gap_id: GAP-D05-PAT-022
    technology: GPE Curing Control
    search_result:
      - Peer-reviewed degradation study confirmed
      - Direct SK On curing-process family not confirmed
    priority: HIGH

  - gap_id: GAP-D05-PAT-023
    technology: Surface-Modified Lithium
    search_result:
      - Peer-reviewed paper confirmed
      - Joint Hanyang–SK On patent family requires targeted audit
    priority: VERY_HIGH

  - gap_id: GAP-D05-PAT-024
    technology: AI Researcher
    search_result:
      - No explicit RFQ/design/cost-AI family confirmed
      - Manufacturing and fault-detection AI families exist
    priority: VERY_HIGH
```

특허군이 확인되지 않았다는 결과는 해당 기술이 보호되지 않았다는 뜻이 아니다. 비공개 출원기간, 다른 명칭의 출원, 공동출원, 영업비밀 또는 장비·소재 파트너의 특허로 보호될 가능성을 각각 열어둬야 한다.

---

## 26.2 Search Gap Governance

```yaml
search_gap_governance:

  prohibited_conclusion:
    - "특허가 없다"
    - "자유롭게 실시할 수 있다"
    - "SK온이 영업비밀로 보호하고 있다"

  permitted_statement:
    - "검토한 공개자료에서 직접 대응하는 특허군을 확인하지 못했다"
    - "추가 출원인·발명자·IPC 검색이 필요하다"
    - "파트너 또는 계열사 보유 IP일 가능성을 확인해야 한다"

  next_search_dimensions:
    - Applicant aliases
    - Inventor names
    - Korean terminology variants
    - Joint applicants
    - Continuation and divisional chains
    - Unpublished application timing
    - Assignment history
```

---
