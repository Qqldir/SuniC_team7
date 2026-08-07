---
id: skon-d05-d05-59-official-register-operating-register
title: Official-Register Operating Register
summary: "국가별 공식 특허등록부(KIPRIS, USPTO, EPO)의 역할과 한계를 정의하고, 특허 법적 상태를 신뢰성 있게 기록하기 위한 패킷 스키마를 제시한다."
tags: [d05, rnd, schema, table]
keywords: [공식 정보원, KIPRIS, USPTO, EPO, 특허 권리상태, 정보원별 조회, 유지료, 권리이전, 특허 법적 상태, 공식 등록부, 지역별 정보원, 권리이전 기록, Decision-Date Status Packet, Patent Family, 절차 상태]
related: []
priority: normal
domain: D05
section: D05-59.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1087
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-59. Official-Register Operating Register

## 59.1 공식 정보원의 역할 분리

| 관할·정보원 | D05에서 확인할 내용 | 확인하지 않는 내용 | 갱신 Trigger |
|---|---|---|---|
| [KIPRIS](https://www.kipris.or.kr/) | 한국 출원·등록번호, 출원인, 공개·등록공보, 심판·권리상태 식별정보 | 실제 제품 실시 여부, 비공개 계약권리 | G1 진입, 고객 RFQ, 라이선스 협상 전 |
| [USPTO Patent Center](https://www.uspto.gov/patents/apply/patent-center) | 미국 출원 절차, 공개 File Wrapper, 청구항 변경 | 현재 권리자의 모든 계약상 제한 | G1·G3·상용화 승인 전 |
| [USPTO Assignment Search](https://www.uspto.gov/patents/maintain/patents-assignments-change-search-ownership) | 기록된 양도·권리이전 | 미기록 계약, 실질적 실시권 | 소유권·담보권 검토 시 |
| [USPTO Maintenance Fees](https://www.uspto.gov/patents/maintain) | 미국 등록특허의 수수료 납부 창과 납부이력 | 무효·비침해 결론 | 매 분기 및 거래 직전 |
| [European Patent Register](https://www.epo.org/en/searching-for-patents/legal/register) | EP 출원 절차, 허여, 이의신청, Unitary Patent 정보 | 허여 후 모든 국가의 최종 상태를 단일 EP 상태로 대체 | G1 진입 및 분기 갱신 |
| [EP Federated Register](https://register.epo.org/help?lng=en&topic=federated) | 참여국이 제공하는 허여 후 국가별 공식 상태 | 미참여국의 완전한 상태 | 유럽 생산·판매국 확정 후 |
| [EPO Publication Server](https://www.epo.org/en/searching-for-patents/technical/publication-server) | EPO가 발행한 A·B 공보의 명세서·청구항 | 현재 존속과 국가별 유효성 | Claim Map 작성·갱신 시 |
| [WIPO PATENTSCOPE](https://patentscope.wipo.int/) | PCT 공개문서·국제단계·우선권 탐색 | PCT 종료 이후 모든 국가단계 권리의 생존 여부 | Family 경계 감사 시 |

EPO는 European Patent Register를 유럽 출원의 절차·법적 정보원으로 설명하며, 허여 후 국가단계는 Federated Register와 각국 등록부로 이어진다. USPTO 역시 출원절차, 권리이전 기록, 유지료 정보를 서로 다른 시스템으로 운영한다. 따라서 D05의 `current_legal_status`는 하나의 검색화면이나 특허 미러만으로 확정하지 않는다.

## 59.2 Decision-Date Status Packet

```yaml
decision_date_status_packet:
  packet_id: required
  patent_family_id: required
  decision_date: required
  target_jurisdictions: required

  per_jurisdiction:
    publication_and_application_numbers: required
    official_register_url_or_extract: required
    procedural_status: required
    current_registered_owner: required
    independent_claim_version_date: required
    continuation_or_divisional_chain: required
    maintenance_or_renewal_status: required_if_granted
    opposition_or_invalidation_signal: required_if_available
    national_validation: required_for_conventional_ep

  evidence_controls:
    reviewer: IP_TEAM_OR_COUNSEL
    retrieval_timestamp: required
    source_grade: A_PLUS_OFFICIAL_REGISTER
    stale_after_days: 30

  prohibited_shortcuts:
    - Treating PCT cessation as national-right lapse
    - Treating a grant publication as proof of present enforceability
    - Treating applicant at filing as present owner
    - Treating one EP grant as active in every designated state
```

---
