---
id: skon-d05-d05-11-applicant-assignee-normalization
title: Applicant·Assignee Normalization
summary: "SK온 및 그룹사의 배터리·분리막 특허를 올바르게 분류하기 위해 출원인을 정규화하고, 양도 이력을 추적하며, 공동 출원 특허의 권리 범위를 관리하는 규칙을 정의한 문서다."
tags: [d05, rnd, schema]
keywords: [배터리 특허, 출원인 정규화, 특허 양도, SK Innovation, 에스케이온, 공동출원, 실시권, 정준 명칭, SK이노베이션, SK온, 양수인, 권리자, IP 관리, 조건부 라이선스]
related: []
priority: normal
domain: D05
section: D05-11.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 978
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-11. Applicant·Assignee Normalization

## 11.1 Canonical Applicant Master

```yaml
applicant_master:

  - applicant_id: APP-SKI-001
    canonical_name: SK Innovation Co., Ltd.
    korean_name: 에스케이이노베이션 주식회사
    role:
      - Historical battery patent applicant
      - Group-level joint applicant
    aliases:
      - SK Innovation Co Ltd
      - SK INNOVATION CO., LTD.
      - 에스케이이노베이션(주)

  - applicant_id: APP-SKON-001
    canonical_name: SK On Co., Ltd.
    korean_name: 에스케이온 주식회사
    role:
      - Current battery company applicant
      - Current assignee of transferred battery patents
    aliases:
      - SK On Co Ltd
      - SK ON CO., LTD.
      - 에스케이온(주)

  - applicant_id: APP-SKIET-001
    canonical_name: SK IE Technology Co., Ltd.
    korean_name: 에스케이아이이테크놀로지 주식회사
    role:
      - Separator technology applicant
      - Group affiliate
    aliases:
      - SK IE Technology
      - SKIET

  - applicant_id: APP-POLYPLUS-001
    canonical_name: PolyPlus Battery Company
    role:
      - Joint applicant in lithium-metal solid-state technology
```

---

## 11.2 Transfer Normalization Rule

SK온 출범 전 출원된 배터리 특허는 최초 출원인이 SK이노베이션으로 표시되고 이후 SK온으로 이전된 사례가 존재한다. 급속충전 전극 특허는 최초 출원인이 SK이노베이션이지만 2022년 11월 SK온으로 양도된 기록이 있으며, BMS 특허 역시 SK이노베이션에서 SK온으로 이전된 이력이 확인된다. ([구글 특허][2])

```yaml
assignee_transfer_rule:

  original_applicant:
    definition: 출원 당시 명세서에 기록된 법인

  current_assignee:
    definition: 조사 기준일 현재 권리를 보유한 것으로 등록된 법인

  transfer_event:
    required_fields:
      - from_entity
      - to_entity
      - effective_date
      - record_date
      - jurisdiction
      - source

  prohibited_normalization:
    - SK Innovation 특허를 출원 시점부터 SK On 특허로 소급 표기
    - 현재 권리자를 확인하지 않고 최초 출원인만으로 소유권 확정
    - 발명자를 특허소유자로 간주
```

---

## 11.3 Joint Ownership Rule

배터리 이상감지 특허는 SK이노베이션과 SK온이 공동 권리자로 표시되고, 리튬메탈-유리 전해질 적층 특허는 SK온과 PolyPlus가 공동 출원인으로 기록돼 있다. 공동출원 특허는 SK온 단독 IP로 분류하지 않고, 실제 실시권·양도·개량발명 권리는 계약 검토 대상으로 남긴다. ([구글 특허][3])

```yaml
joint_ip_rule:

  ownership_scope:
    - SOLE_SK_ON
    - TRANSFERRED_TO_SK_ON
    - SK_GROUP_JOINT
    - EXTERNAL_JOINT
    - AFFILIATE_OWNED
    - OWNERSHIP_UNVERIFIED

  required_contract_questions:
    - 독자 실시 가능 여부
    - 제3자 라이선스 가능 여부
    - 개량발명 소유권
    - 국가별 비용부담
    - 권리유지 결정권
    - 분쟁 대응권
```

---
