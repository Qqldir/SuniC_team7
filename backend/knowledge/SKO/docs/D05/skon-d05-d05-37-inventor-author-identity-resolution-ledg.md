---
id: skon-d05-d05-37-inventor-author-identity-resolution-ledg
title: Inventor–Author Identity Resolution Ledger
summary: SK온 D05 연구자의 논문 저자와 특허 발명자 신원 대응 결과를 정리하고 유사 이름 오식별을 방지하는 규칙을 제시한 문서
tags: [d05, rnd, schema, table]
keywords: [신원 검증, 저자명 매칭, 발명자 확인, 특허, 명의 통일, 중복 방지, 고체전해질, 인명 보정, 신원대응, 발명자확인, 논문저자, 특허발명자, 중복병합방지, 신원검증, 특허패밀리, 광소결, 인명정보]
related: [PF-SKON-D05-032]
priority: normal
domain: D05
section: D05-37.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 916
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-37. Inventor–Author Identity Resolution Ledger

## 37.1 Resolution Results

| Researcher      | Paper Author | Patent Inventor | 판정                 |
| --------------- | -----------: | --------------: | ------------------ |
| Kyeong Joon Kim |           확인 |              확인 | VERIFIED           |
| Min Kyu Kim     |           확인 |              확인 | VERIFIED           |
| Eun Jeong Yi    |           확인 |              확인 | VERIFIED           |
| Young-Uk Park   |           확인 |              확인 | VERIFIED           |
| Mincheol Beak   |           확인 |              유력 | PROBABLE           |
| Do Kyeong Lee   |           확인 |   다른 후속 특허에서 확인 | PARTIALLY VERIFIED |
| Jaehoon Choi    |           확인 |        유사 이름 존재 | UNRESOLVED         |
| Jeonghyun Ko    |           확인 |    직접 대응 특허 미확인 | UNRESOLVED         |
| Hansol Lee      |           확인 |    직접 대응 특허 미확인 | UNRESOLVED         |

---

## 37.2 Do Kyeong Lee 처리

광소결 논문에는 Do Kyeong Lee가 저자로 포함됐지만, `PF-SKON-D05-032`의 대표 EP 문서에는 발명자로 나타나지 않는다. 반면 2026년 공개된 다른 고체전해질 조성 특허에는 Kyeong Joon Kim·Min Kyu Kim·Do Kyeong Lee·Eun Jeong Yi가 공동 발명자로 나타난다. 따라서 Do Kyeong Lee를 `PF-D05-032 발명자`로 소급 등록하지 않고, 별도 후보 패밀리의 발명자로 관리한다. ([구글 특허][1])

```yaml
identity_correction:
  researcher_id: RES-SKON-D05-006
  canonical_name: Do Kyeong Lee

  paper_role:
    paper_id: PAPER-SKON-D05-002
    status: VERIFIED

  PF_D05_032_inventor_role:
    status: NOT_SUPPORTED_BY_REPRESENTATIVE_EP_DOCUMENT

  other_patent_activity:
    status: CONFIRMED_IN_LATER_SOLID_ELECTROLYTE_APPLICATIONS

  resolution:
    - Remove direct inventor edge to PF-SKON-D05-032
    - Retain solid-state patent-network membership
```

---

## 37.3 False-Merge Prevention

```yaml
identity_false_merge_rules:

  - rule_id: ID-RULE-D05-001
    rule: >
      Jaehoon Choi와 Jae Young Choi를 이름 유사성만으로
      동일 인물로 병합하지 않는다.

  - rule_id: ID-RULE-D05-002
    rule: >
      Jeonghyun Ko와 동일 영문 성명을 가진 다른 배터리
      연구자를 소속 확인 없이 병합하지 않는다.

  - rule_id: ID-RULE-D05-003
    rule: >
      Min Kyu Kim과 유사한 한글 성명을 가진 발명자는
      기술분야·공동발명자 네트워크를 함께 검증한다.

  - rule_id: ID-RULE-D05-004
    rule: >
      논문 소속이 대학으로만 표시된 저자를 SK온 직원으로
      자동 분류하지 않는다.

  - rule_id: ID-RULE-D05-005
    rule: >
      현재 SK온 소속이라고 해도 과거 SK이노베이션 명의 특허의
      출원 당시 고용관계를 임의 추정하지 않는다.
```

---
