---
id: skes-d01-1-기업-식별-마스터
title: 기업 식별 마스터
summary: SK이노베이션 E&S의 공식 정보(명칭·주소·웹사이트)와 2024년 합병 전후 법인 지위·조직 형태 변화를 명시한 기업정보표
tags: [d01, identity, schema, table]
keywords: [SK이노베이션, SK E&S, CIC, Company-in-Company, 합병, 법적 지위, SK-Enron, 도시가스, LNG, 에너지 사업, SK Innovation E&S, 2024년 합병, 법인정체성, LNG·발전·도시가스, 조직형태, 존속법인, Canonical Entity ID, 시간구간]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001, ORG-SKI-LEGAL-000001, TS-ENS-001, TS-ENS-002, TS-ENS-003, ALIAS-ENS-001, ALIAS-ENS-002, ALIAS-ENS-003, ALIAS-ENS-004, ALIAS-ENS-005, ALIAS-ENS-006, ALIAS-ENS-007, ALIAS-ENS-008, ALIAS-ENS-009, ALIAS-ENS-010]
priority: normal
domain: D01
section: 1
source: SK이노베이션E&S_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 2249
updated: 2026-08-06
---

> SK이노베이션 E&S · D01 기업 기본정보·법인구조·연혁

# SK이노베이션 E&S AI Knowledge Database

## D01. Corporate Identity｜기업 기본정보

**Version 1.0 / 기준일: 2026년 8월 3일 / 상태: PUBLIC_SOURCE_COMPLETE_V1**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Parent legal entity: `ORG-SKI-LEGAL-000001`
- Source namespace: `SRC-ENS-D01-*`
- Fact namespace: `FACT-ENS-D01-*`
- Event namespace: `EVT-ENS-D01-*`
- 본 문서는 처음부터 Canonical ID를 사용하며, 향후 D00에서 URL·엔티티·변경이력을 통합 관리한다.

---

## 0. 도메인 정의

D01 Corporate Identity는 SK이노베이션 E&S의 법적·조직적 정체성, 기업집단 내 위치, 공식 명칭, 설립과 합병의 역사, 현재 CIC 운영체계, 경영진, 공식 사업 정체성, 주요 거점과 기본 엔티티를 저장하는 도메인이다.

이 도메인의 핵심 목적은 AI가 다음 세 대상을 동일한 것으로 오인하지 않도록 하는 데 있다.

1. 1999년 설립되어 2024년까지 존속한 역사적 법인 `SK E&S Co., Ltd.`
2. 2024년 11월 1일 합병 후 SK이노베이션 내부에서 운영되는 `SK Innovation E&S CIC`
3. E&S CIC가 관리하거나 지분을 보유한 도시가스·발전·재생에너지·수소·에너지솔루션 자회사와 프로젝트 법인

### 0.1 기준 분석범위

```yaml
analysis_target:
  canonical_name: SK Innovation E&S CIC
  korean_name: SK이노베이션 E&S
  entity_type: company_in_company
  legal_personality: false
  parent_legal_entity: SK Innovation Co., Ltd.
  included_scope:
    - E&S CIC 본체의 LNG·발전·도시가스·재생에너지·수소·에너지솔루션 사업
    - E&S CIC 산하 연결·관계·프로젝트 법인
    - 2024-11-01 이전 SK E&S의 역사와 사업자료
  excluded_scope:
    - SK이노베이션 전체 석유·화학 사업
    - SK온 배터리 사업
    - SK어스온 E&P 사업 중 E&S 사업과 직접 연결되지 않는 범위
  boundary_rule: >
    과거 SK E&S와 현재 E&S CIC의 자료는 event_time과 reporting_entity를 함께 저장한다.
```

### 0.2 이번 기업에서 강화하는 데이터 규칙

- 발전설비는 `설비 총용량`, `지분귀속 용량`, `상업운전 용량`, `개발 파이프라인`을 분리한다.
- LNG는 `가스전 생산량`, `액화설비 사용계약량`, `선박 수송능력`, `터미널 처리능력`, `발전소 소비량`을 서로 다른 단위로 저장한다.
- 자회사와 사업장을 동일 엔티티로 병합하지 않는다.
- 과거 법인의 연결실적과 합병 후 SK이노베이션의 E&S 사업부문 실적을 그대로 시계열 연결하지 않는다.
- 공식자료가 CIC와 법인이라는 용어를 혼용할 때는 법적 지위보다 원문의 표현을 우선 보존하고 `normalized_entity_type`으로 정규화한다.

---

# 1. 기업 식별 마스터

## 1.1 현재 기준 식별정보

| 필드 | 데이터 | 상태 |
|---|---|---|
| Canonical Entity ID | `ORG-SKI-ENS-CIC-000001` | Current |
| 공식 사용 국문명 | SK이노베이션 E&S | Current |
| 공식 사용 영문명 | SK Innovation E&S | Current |
| 조직 형태 | SK이노베이션 내부 CIC(Company-in-Company) | Current |
| 독립 법인 여부 | 독립 법인이 아님 | Current |
| 법적 귀속 | SK이노베이션 주식회사 | Current |
| CIC 출범일 | 2024년 11월 1일 | Current |
| 전신 | 에스케이이엔에스 주식회사 / SK E&S Co., Ltd. | Historical |
| 최초 역사적 출발 | 1999년 1월 SK-Enron Co., Ltd. 설립 | Historical |
| 주요 산업 | LNG, 전력, 도시가스, 재생에너지, 수소, 에너지솔루션 | Current |
| 공식 사업 정체성 | Sustainable Energy Solution Optimizer | Current |
| 본사 사용 주소 | 서울특별시 종로구 종로 26 | Current |
| 대표번호 | 02-2121-3114 | Current |
| 공식 웹사이트 | `https://www.skens.com/` | Current |
| 기준일 | 2026-08-03 | Current |

SK E&S와 SK이노베이션의 합병은 2024년 11월 1일 완료됐다. 합병 후 존속법인은 SK이노베이션이며, 기존 SK E&S 사업은 `SK Innovation E&S`라는 CIC로 운영된다. 따라서 현재의 `SK이노베이션 E&S`는 브랜드와 독립경영 단위를 나타내지만 별도 법인으로 처리하면 안 된다. ([SRC-ENS-D01-0001])

## 1.2 법적·조직적 시간 구간

| Time Slice ID | 기간 | 명칭 | 유형 | 처리 규칙 |
|---|---|---|---|---|
| `TS-ENS-001` | 1999-01~2005-09 | SK-Enron Co., Ltd. | 역사적 독립법인 | SK E&S 전신 |
| `TS-ENS-002` | 2005-10~2024-10-31 | SK E&S Co., Ltd. | 역사적 독립법인 | 합병 전 법인실적 귀속 |
| `TS-ENS-003` | 2024-11-01~현재 | SK Innovation E&S CIC | SK이노베이션 내부 CIC | 현재 사업·조직 귀속 |

```yaml
event_id: EVT-ENS-D01-2024-001
event_type: merger
announcement_context: SK Innovation and SK E&S merger
effective_date: 2024-11-01
absorbing_entity: ORG-SKI-LEGAL-000001
absorbed_entity: ORG-SKENS-LEGAL-000001
successor_operating_unit: ORG-SKI-ENS-CIC-000001
legal_result: SK E&S standalone legal entity absorbed
operating_result: SK Innovation E&S retained as CIC
fact_status: official_fact
source_id: SRC-ENS-D01-0001
```

## 1.3 명칭 및 별칭 관리

| Alias ID | 명칭 | 언어 | 유형 | 유효기간·상태 |
|---|---|---|---|---|
| `ALIAS-ENS-001` | SK이노베이션 E&S | 한국어 | 현재 공식 사용명 | Current |
| `ALIAS-ENS-002` | SK Innovation E&S | 영어 | 현재 공식 사용명 | Current |
| `ALIAS-ENS-003` | SK이노베이션 E&S CIC | 한국어 | 조직형태 명시명 | Current Contextual |
| `ALIAS-ENS-004` | SK Innovation E&S CIC | 영어 | 조직형태 명시명 | Current Contextual |
| `ALIAS-ENS-005` | 에스케이이엔에스 주식회사 | 한국어 | 합병 전 법적 명칭 | Historical |
| `ALIAS-ENS-006` | SK E&S Co., Ltd. | 영어 | 합병 전 법적 명칭 | Historical |
| `ALIAS-ENS-007` | SK E&S | 한·영 혼용 | 합병 전 브랜드·통칭 | Historical / Search Alias |
| `ALIAS-ENS-008` | SK-Enron Co., Ltd. | 영어 | 1999~2005 전신명 | Historical |
| `ALIAS-ENS-009` | SK이엔에스 | 한국어 | 비표준 검색 별칭 | Search Alias Only |
| `ALIAS-ENS-010` | E&S CIC | 영어 | 내부·언론 축약 | Current Contextual |

### 명칭 처리 규칙

1. 기준일이 2024년 11월 1일 이후이면 기본 표준명은 `SK이노베이션 E&S CIC`로 저장한다.
2. 과거 계약·재무·지분·소송의 당사자가 SK E&S 법인이면 당사자를 CIC로 소급 변경하지 않는다.
3. 기사나 홈페이지가 `회사`, `기업`, `법인`으로 서술하더라도 현재 법적 실체는 SK이노베이션임을 별도 필드에 기록한다.
4. `SK E&S`는 검색 편의를 위한 Alias로 유지하되 Current Legal Entity로 사용하지 않는다.

---
