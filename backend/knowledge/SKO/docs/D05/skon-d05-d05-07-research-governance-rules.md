---
id: skon-d05-d05-07-research-governance-rules
title: Research Governance Rules
summary: "SK온의 R&D 데이터 관리에서 조직, 시설, 지식재산을 어떻게 정의·구분하고 추적해야 하는지 설명하는 지배 규칙 가이드."
tags: [d05, rnd, schema]
keywords: [특허, 지식재산, R&D, 기술이전, 공동연구, 거버넌스, 출원인, 성과 관리, 라이선스, MOU, 연구 거버넌스, 데이터 정의, 지식재산권, 특허 관리, 연구기관 분리, 시설 단계, IP 소유권, 연구결과 추적]
related: []
priority: normal
domain: D05
section: D05-07.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 482
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-07. Research Governance Rules

```yaml
research_governance_rules:

  organization_identity:
    - Future Technology Institute와 SK Innovation IEST를 분리한다.
    - 과거 Battery Research Institute는 시점별 별칭으로 저장한다.

  facility_status:
    - 계획, 건설, 완공, 파일럿 가동, 양산을 서로 구분한다.
    - 파일럿 플랜트를 상업생산 공장으로 표현하지 않는다.

  research_result:
    - 논문 연구셀 결과를 양산셀 성능으로 일반화하지 않는다.
    - 회사 내부 목표를 달성성과로 전환하지 않는다.

  partner_relation:
    - 공동연구, MOU, 라이선스, 기술이전과 공급계약을 분리한다.
    - 외부기술을 SK온 단독 보유기술로 등록하지 않는다.

  ip_ownership:
    - 특허의 출원인과 현재 권리자를 분리한다.
    - 공동발명자와 공동출원인을 구분한다.
    - 기술기사에 등장한다는 이유만으로 특허소유를 추정하지 않는다.

  temporal_data:
    - 연구기관 명칭 변경이력을 보존한다.
    - 로드맵 목표연도는 발표일별로 저장한다.
    - 최신 목표와 역사적 목표를 별도 필드로 관리한다.

  evidence_requirement:
    - 연구프로그램 FACT에는 source_id가 필요하다.
    - 분석 프로그램은 basis_program_ids 또는 basis_technology_ids가 필요하다.
```

---
