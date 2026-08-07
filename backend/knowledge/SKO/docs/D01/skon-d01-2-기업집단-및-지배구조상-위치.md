---
id: skon-d01-2-기업집단-및-지배구조상-위치
title: 기업집단 및 지배구조상 위치
summary: SK온이 SK그룹의 어느 계층에 속하고 2025년 합병으로 어떤 법인관계가 형성되었는지 설명하는 계층도와 법인관계 표를 담은 문서다
tags: [d01, identity, table, "xref:d02"]
keywords: [SK온, SK이노베이션, SK Inc., 지배구조, 자회사, 합병, CIC, 배터리사업, 트레이딩, 법인관계, 계층 구조, 사업 통합]
related: []
priority: normal
domain: D01
section: 2
source: SK온_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 857
updated: 2026-08-03
---

> SK온 · D01 기업 기본정보·법인구조·연혁

# 2. 기업집단 및 지배구조상 위치

## 2.1 그룹 내 계층구조

```text
SK Inc.
  └─ SK Innovation
       └─ SK On
            ├─ Battery Business
            ├─ SK On Trading International CIC
            ├─ SK Enmove CIC
            ├─ Domestic R&D / Operating Sites
            └─ Overseas subsidiaries and production entities
```

SK Inc.는 SK그룹의 지주회사이며, SK이노베이션은 그룹 내 에너지사업 포트폴리오를 담당하는 주요 회사다. SK이노베이션은 공식 홈페이지에서 SK온을 전기차 배터리사업을 수행하는 핵심 자회사로 분류한다. ([SK 주식회사 (SK Inc.)][3])

2025년 SK온은 기존 배터리 단일사업 법인에서 트레이딩·탱크터미널·윤활기유 및 에너지효율화 사업을 포괄하는 통합 법인으로 확대됐다. SK온은 2025년 2월 SK트레이딩인터내셔널 및 SK엔텀과의 합병을 완료했고, 같은 해 11월 SK엔무브와의 합병을 완료했다고 공식 발표했다. 합병 이후 SK엔무브와 SK온 트레이딩인터내셔널은 통합 SK온 내 CIC 형태로 운영된다고 설명됐다. ([ASK Inno][4])

---

## 2.2 주요 법인관계

| Subject                     | Relation   | Object                   | 상태      | 근거 유형 |
| --------------------------- | ---------- | ------------------------ | ------- | ----- |
| SK Inc.                     | 지배구조상 상위회사 | SK Innovation            | Current | 공식    |
| SK Innovation               | 자회사로 보유    | SK On                    | Current | 공식    |
| SK On                       | 합병         | SK Trading International | 2025 완료 | 공식    |
| SK On                       | 합병         | SK Enterm                | 2025 완료 | 공식    |
| SK On                       | 합병         | SK Enmove                | 2025 완료 | 공식    |
| SK Enmove                   | CIC로 운영    | SK On                    | Current | 공식    |
| SK On Trading International | CIC로 운영    | SK On                    | Current | 공식    |

### 관계 트리플

```text
SK_INC — CONTROLS_GROUP_PORTFOLIO → SK_INNOVATION
SK_INNOVATION — HAS_SUBSIDIARY → SK_ON
SK_ON — MERGED_WITH → SK_TRADING_INTERNATIONAL
SK_ON — MERGED_WITH → SK_ENTERM
SK_ON — MERGED_WITH → SK_ENMOVE
SK_ENMOVE_CIC — OPERATES_WITHIN → SK_ON
SK_ON_TRADING_INTERNATIONAL_CIC — OPERATES_WITHIN → SK_ON
```

### Fact status

* SK온–SK이노베이션 관계: `official_fact`
* 2025년 3사 합병: `official_fact`
* 2025년 SK엔무브 합병: `official_fact`
* 합병 후 개별 사업 간 장기 시너지 효과: `analysis`, D02 및 D11에서 별도 관리

---
