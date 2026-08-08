---
id: skon-d05-d05-dq-003-patent-search-reconciliation
title: 003. Patent Search Reconciliation
summary: SK온 특허 포트폴리오 구성 시 제외되어야 할 타사 특허들을 식별하고 제외하는 기준과 사례를 정리한 문서
tags: [d05, rnd, schema]
keywords: [오탐 제거, 특허 권리자, Assignee verification, 포트폴리오 정제, 액침냉각, 고체전해질, Patent family, 법적 상태, FTO, 경쟁 벤치마크, 검색 오탐 제거, 특허 포트폴리오, 권리자 확인, FTO 벤치마크, 경쟁사 분석, 특허 가족, KIPRIS, 지식재산 관리]
related: []
priority: normal
domain: D05
section: D05-DQ
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 625
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# SK온 D05 R&D, Patents & Intellectual Property

## Part 4. Architecture·Inspection·Solid-State Patent Family Expansion

**문서 버전:** D05 v1.3
**기준일:** 2026-08-02
**이전 완료 지점:** `D05-23 Patent Portfolio Snapshot v2`

> 아래 법적 상태는 특허문서 탐색 시점의 스냅샷이다. 등록·존속·권리자 상태는 KIPRIS, USPTO Patent Center, EP Register 등 관할 특허청에서 최종 재검증해야 한다.

---

# D05-DQ-003. Patent Search Reconciliation

## 검색 오탐 제거

```yaml
false_positive_exclusion:

  - publication: EP4228060A1
    title: Battery Module
    actual_assignee: Prime Planet Energy and Solutions
    exclusion_reason:
      - SK On patent citations에서 발견되었으나 SK온 출원이 아님
      - CTP·냉각 벤치마크 문서로만 사용

  - publication: US20230369708A1
    title: Immersion Cooling System for Battery Systems of Electric Vehicles
    actual_assignee: GM Global Technology Operations
    exclusion_reason:
      - SK온 EV 액침냉각 특허로 오인 가능
      - SK온 Patent Family Master에서 제외

  - publication: US20220407183A1
    title: Multi-Layer Solid Electrolyte Separator
    actual_assignee:
      original: Global Graphene Group
      current_snapshot: Honeycomb Battery Company
    exclusion_reason:
      - 검색 결과에 SK온 후속 특허가 인용됐을 뿐 SK온 출원이 아님
```

EP4228060A1은 Prime Planet Energy and Solutions가 출원한 냉각판·열전도부재 기술이며, SK온 소유 특허가 아니다. US20230369708A1 역시 GM 소유 액침냉각 특허다. 따라서 두 문서는 경쟁·FTO 벤치마크로는 활용할 수 있지만 SK온의 보유 IP로 등록하지 않는다. ([구글 특허][1])

다층 고체전해질 분리막 문서 US20220407183A1도 Global Graphene Group에서 Honeycomb Battery Company로 이전된 특허로 확인돼 SK온 포트폴리오에서 제외한다. ([구글 특허][2])

---
