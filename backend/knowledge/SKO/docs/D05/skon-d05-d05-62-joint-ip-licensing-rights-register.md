---
id: skon-d05-d05-62-joint-ip-licensing-rights-register
title: Joint-IP & Licensing Rights Register
summary: 협력기관과의 공동출원 및 라이선스 계약에서 실제 상업적 실시권을 확보하기 위해 필요한 내부 증거 문서와 권리 기록 표준을 설명한다.
tags: [d05, rnd, schema, table]
keywords: [공동출원, 기술이전, 실시권, Background IP, Foreground IP, 협력계약, 권리기록, 상용화, 개선발명, IP 관리, 기술라이선스, 배경지식재산, 계약권리, IP소유권, RIGHTS_GATE, 협력기관, 공동연구계약]
related: []
priority: normal
domain: D05
section: D05-62.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 854
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-62. Joint-IP & Licensing Rights Register

## 62.1 공개관계와 계약권리의 분리

| Relationship | 공개자료로 확인된 수준 | 공개자료만으로 확정 불가 | 필수 내부 Evidence |
|---|---|---|---|
| Solid Power | 기술 라이선스·파일럿 설비 및 R&D 협력 관계 | 상업생산 실시권, 고객·지역 범위, 개선발명, 제3자 소재 사용, 종료 후 권리 | 원계약·SOW·변경계약·Acceptance·IP Schedule |
| PolyPlus | 리튬메탈–유리전해질 적층 관련 공동출원 | 독자실시, 제3자 라이선스, 개량발명, 비용·집행 권한 | 공동출원·JDA·Prosecution Control 조항 |
| 단국대학교 산학협력단 | LLZO 관련 공동출원 | Field-of-use, 독점성, 개량발명과 상용화 수익배분 | 공동연구·기술이전·실시계약 |
| KICET | 광소결 공동연구·논문·관련 출원 언급 | 정확한 Family, 출원인, 개량공정 소유권, 장비사 실시권 | 과제협약·발명신고·출원명세·기관 간 계약 |
| 기타 대학 공동연구 | 공동논문·연구협력 | Publication Review, Background IP, Student IP, 후속발명 권리 | 연구계약·NDA·Data Management Plan |

## 62.2 Canonical Rights Record

```yaml
joint_ip_rights_record:
  relationship_id: required
  counterparty: required
  agreement_ids: required_internal
  effective_and_expiry_dates: required_internal

  background_ip:
    owner: required
    listed_assets: required
    license_scope: required
    field_of_use: required
    geography: required
    exclusivity: required
    sublicensing: required

  foreground_ip:
    inventorship_rule: required
    ownership_rule: required
    prosecution_control: required
    cost_allocation: required
    enforcement_control: required

  improvements:
    definition: required
    ownership: required
    grant_back: required
    post_termination_use: required

  data_and_knowhow:
    raw_data_owner: required
    model_and_derived_data_rights: required
    confidential_information: required
    trade_secret_marking: required
    retention_and_deletion: required

  commercialization:
    make_use_sell_import: required
    customer_program_scope: required
    third_party_material_right: required
    change_of_control: required

  verification_status:
    public_relationship_confirmed: required
    contract_reviewed_by_legal: required
    unresolved_restrictions: required
    next_decision_gate: required
```

`공동출원`, `기술이전`, `라이선스`라는 관계 라벨은 상업적 실시자유를 자동으로 증명하지 않는다. D17의 외부협력 과제는 기술적 적합성 점수와 별도로 `RIGHTS_GATE_PASS`가 있어야 G3 이후로 이동한다.

---
