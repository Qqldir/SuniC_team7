---
id: skes-d01-8-현재-cic-운영체계
title: 현재 CIC 운영체계
summary: "SK이노베이션 내 독립경영 단위 CIC의 법적 지위, 운영 구조, 그룹사와의 시너지 영역을 설명하는 문서"
tags: [d01, identity, schema, table]
keywords: [CIC, 독립경영 단위, LNG 조달, ESS, 재생에너지, 시너지 인터페이스, 수소, RE100, 저탄소 연료, 콘덴세이트, 정유화학, PPA, 합병]
related: [INTF-ENS-001, INTF-ENS-002, INTF-ENS-003, INTF-ENS-004, INTF-ENS-005]
priority: normal
domain: D01
section: 8
source: SK이노베이션E&S_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 481
updated: 2026-08-06
---

> SK이노베이션 E&S · D01 기업 기본정보·법인구조·연혁

# 8. 현재 CIC 운영체계

## 8.1 CIC의 의미

CIC는 별도 법인이 아니라 SK이노베이션 내부의 독립경영 단위다. 공식 합병 발표는 이 구조가 기존 E&S 사업의 민첩성과 경쟁력을 유지하면서 모회사 자원과 시너지를 활용하도록 설계됐다고 설명한다. ([SRC-ENS-D01-0001])

## 8.2 데이터베이스상 처리

```yaml
entity_id: ORG-SKI-ENS-CIC-000001
entity_class: operating_unit
legal_personality: false
can_own_assets_directly: false_as_separate_legal_person
asset_legal_owner_default: SK Innovation or relevant subsidiary
can_be_public_brand: true
can_have_business_leader: true
can_report_segment_information: true
requires_parent_entity_link: true
```

## 8.3 합병 후 시너지 인터페이스

| Interface ID | E&S 역량 | SK이노베이션 측 역량 | 잠재 결합영역 | 상태 |
|---|---|---|---|---|
| `INTF-ENS-001` | LNG 조달·발전 | 정유·화학 자가발전 수요 | LNG 직도입·전력비 최적화 | Official initiative |
| `INTF-ENS-002` | 가스전·LNG | 콘덴세이트 활용·트레이딩 | 원료·상품 최적화 | Official initiative |
| `INTF-ENS-003` | 분산전원·EMS | 배터리·ESS·R&D | 데이터센터·산업체 에너지패키지 | Official direction |
| `INTF-ENS-004` | 수소·CCS | 정유·화학 공정 | 저탄소 연료·탄소관리 | Official direction |
| `INTF-ENS-005` | 재생에너지·PPA | 그룹 전력수요 | RE100·전력조달 | Official direction |

---
