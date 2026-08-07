---
id: skes-d05-19-knowledge-graph-and-query-templates
title: Knowledge Graph and Query Templates
summary: "특허군, 라이선스, 공동권리자, 발명자 네트워크 등 E&S 지식재산을 효율적으로 검색하고 관리하기 위한 그래프 구조와 쿼리 템플릿을 정의한다."
tags: [d05, rnd, schema, "xref:d04", "xref:d06"]
keywords: [특허군, 그래프 구조, 노드, 엣지, 발명자, 라이선스, 공동권리자, 지식재산]
related: []
priority: normal
domain: D05
section: 19
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 478
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 19. Knowledge Graph and Query Templates

## 19.1 Node Types

```yaml
nodes:
  - Organization
  - Affiliate
  - RnD_Program
  - Patent_Family
  - Patent_Publication
  - Inventor
  - Partner
  - Product
  - Technology
  - Data_Asset
  - Software
  - Facility
  - Contract
  - OI_Seed
  - Risk
```

## 19.2 Edge Types

```yaml
edges:
  - APPLIED_FOR
  - CURRENTLY_ASSIGNED_TO
  - CO_OWNED_BY
  - INVENTED_BY
  - DEVELOPED_IN
  - COLLABORATES_WITH
  - USES_PARTNER_TECH
  - LICENSED_UNDER
  - IMPLEMENTATION_UNCONFIRMED
  - SUPPORTS_PRODUCT
  - MAPS_TO_TECHNOLOGY
  - USES_DATA
  - CREATES_OI_SEED
  - BLOCKED_BY_RISK
  - REQUIRES_GATE
  - PRE_DATES_ACQUISITION
```

## 19.3 Query Templates

1. `E&S 또는 자회사 명의이면서 D04 P0 기술에 연결되는 active 특허군은?`
2. `인수 전 EverCharge 특허 중 한국 E&S 자산에 재사용할 후보는?`
3. `공동권리자 동의가 필요한 도시가스 과제는?`
4. `KCE 소프트웨어와 EverCharge 특허를 결합할 때 필요한 내부 라이선스는?`
5. `CO₂ 포집 특허와 Honeywell 배경IP가 동시에 연결되는 프로그램은?`
6. `발명자 네트워크가 2개 이상 특허군에 반복되는 기술은?`
7. `특허보다 데이터·영업비밀이 핵심인 P0 과제는?`
8. `공식 상태 갱신이 30일을 넘은 특허는?`
9. `파트너 기술 의존도가 높고 개량발명 조항이 필요한 과제는?`
10. `D06 공정데이터 없이는 구현 여부를 판정할 수 없는 특허는?`

---
