---
id: skon-d05-d05-58-completion-boundary-reset
title: Completion Boundary Reset
summary: SK온 D05 IP 지식 데이터베이스의 완료 범위를 정의하고 공개정보 기반 기술 인텔리전스와 법률실사 대상을 구분하는 문서.
tags: [d05, rnd, schema]
keywords: [FTO, 법률실사, IP 인텔리전스, 공개정보, 특허 맵핑, 특허 유효성, 라이선싱, 오픈이노베이션, SK온, 자유실시권, 특허, 완료 경계, 공동 IP]
related: []
priority: normal
domain: D05
section: D05-58.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 822
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# SK온 D05 R&D, Patents & Intellectual Property

## Part 10. Public-Scope Closure·FTO Gate·Joint-IP Rights Register

**문서 버전:** D05 v2.0  
**기준일:** 2026-08-03  
**이전 완료 지점:** `D05-57 Human-Readable IP Strategy Report`  
**본 구간 역할:** 미해결 항목을 `공개자료 보완`, `주기적 갱신`, `SK온 내부자료 필요`, `법률전문가 판단 필요`로 분해하고 공개정보 DB의 완료 경계를 확정한다.

> 본 구간은 특허침해·유효성·FTO에 관한 법률의견이 아니다. 특허공보의 기술내용, 공식 등록부의 절차·권리상태, 제품·계약 내부자료로만 검증할 수 있는 사실을 서로 다른 필드로 유지한다.

---

# D05-58. Completion Boundary Reset

## 58.1 완료의 의미

```yaml
d05_completion_boundary_v2:

  public_evidence_intelligence_db:
    status: COMPLETE_V2
    completed_scope:
      - R&D organization, facilities and programs
      - 33 confirmed or provisional patent families
      - 4 candidate patent families
      - Independent-claim element pre-map
      - Product–patent technical-relevance map
      - Five priority FTO gate cards
      - Joint-IP and licensing-rights verification register
      - Paper, author and inventor network
      - Competitor sample benchmark
      - IP white-space and OI opportunity portfolio
      - Chunk library and graph-query templates

  legal_rights_closure:
    status: NOT_COMPLETE_AND_OUTSIDE_PUBLIC_DB_SCOPE
    requires:
      - Country-by-country official register extract at decision date
      - Current assignment and security-interest records
      - Prosecution history and amended independent claims
      - Opposition, invalidation and litigation review
      - Product BOM, process recipe and claim chart
      - Confidential license and joint-development agreements
      - Qualified patent-counsel opinion

  interpretation_rule: >
    D05를 기술·오픈이노베이션 탐색 DB로 사용하는 작업은 완료한다.
    다만 특정 제품의 실시자유, 침해, 특허유효성, 현재 소유권을 확정하는
    법률실사는 별도 프로젝트이며 D05 완료율에 포함하지 않는다.
```

기존 `CONDITIONALLY_COMPLETE`는 공개자료로 해결할 수 있는 작업과 내부 계약·제품자료가 필요한 작업을 한 상태값으로 묶어 전체 문서가 미완성처럼 보이게 했다. v2.0은 이를 분리한다. **공개자료 기반 기술·IP 인텔리전스 DB는 완료**, 개별 사업 의사결정 직전의 법률실사는 `Decision-Date FTO`로 남긴다.

---
