---
id: skes-d01-2-기업집단-및-지배구조상-위치
title: 기업집단 및 지배구조상 위치
summary: "SK이노베이션 그룹 내에서 E&S 부문의 조직적 위치와 CIC 구조, 관리하는 자회사 및 사업 부문의 계층관계를 설명하는 문서입니다."
tags: [d01, identity, table]
keywords: [SK Inc., SK Innovation, E&S CIC, 자회사, 조직도, 흡수합병, 도시가스, LNG, 재생에너지, 그룹 포트폴리오, 도시가스 자회사, 발전, 자회사 관리체계]
related: []
priority: normal
domain: D01
section: 2
source: SK이노베이션E&S_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 606
updated: 2026-08-06
---

> SK이노베이션 E&S · D01 기업 기본정보·법인구조·연혁

# 2. 기업집단 및 지배구조상 위치

## 2.1 그룹 내 계층구조

```text
SK Inc.
  └─ SK Innovation Co., Ltd.  [존속 법인]
       ├─ SK Innovation E&S CIC
       │    ├─ LNG Value Chain
       │    ├─ Power Generation / CHP
       │    ├─ City Gas Subsidiaries
       │    ├─ Renewable Energy
       │    ├─ Hydrogen / CCS
       │    └─ Energy Solution / ESS / VPP / DERMS
       ├─ SK Energy
       ├─ SK Geo Centric
       ├─ SK Incheon Petrochem
       ├─ SK Earthon
       └─ SK On and other affiliates
```

현재 E&S CIC는 SK이노베이션 내부의 독립경영 단위다. CIC 구조는 기존 사업의 경쟁력과 의사결정 민첩성을 유지하면서도 SK이노베이션의 석유·화학·배터리·연구개발·트레이딩 역량과 시너지를 만들기 위한 조직 설계로 설명된다. ([SRC-ENS-D01-0001])

## 2.2 핵심 관계

| Subject | Relation | Object | 시점 | 근거상태 |
|---|---|---|---|---|
| SK Inc. | 그룹 지배구조상 상위회사 | SK Innovation | Current | Official |
| SK Innovation | 내부 CIC로 운영 | SK Innovation E&S | 2024-11-01~ | Official |
| SK E&S Co., Ltd. | 흡수합병됨 | SK Innovation | 2024-11-01 | Official |
| SK Innovation E&S CIC | 관리·연결 | 도시가스 자회사군 | Current | Official |
| SK Innovation E&S CIC | 관리·연결 | 발전 자회사군 | Current | Official |
| SK Innovation E&S CIC | 관리·연결 | 재생에너지·수소·솔루션 법인군 | Current | Official / Entity-level audit required |

### 관계 트리플

```text
SK_INC — CONTROLS_GROUP_PORTFOLIO → SK_INNOVATION
SK_INNOVATION — OPERATES_CIC → SK_INNOVATION_ENS_CIC
SK_ENS_LEGAL — MERGED_INTO → SK_INNOVATION
SK_INNOVATION_ENS_CIC — SUCCEEDS_BUSINESS_OF → SK_ENS_LEGAL
SK_INNOVATION_ENS_CIC — MANAGES_BUSINESS_CLUSTER → LNG_VALUE_CHAIN
SK_INNOVATION_ENS_CIC — MANAGES_BUSINESS_CLUSTER → POWER_VALUE_CHAIN
SK_INNOVATION_ENS_CIC — MANAGES_SUBSIDIARY_CLUSTER → CITY_GAS_SUBSIDIARIES
```

---
