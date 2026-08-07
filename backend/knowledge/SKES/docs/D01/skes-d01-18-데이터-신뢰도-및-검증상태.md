---
id: skes-d01-18-데이터-신뢰도-및-검증상태
title: 데이터 신뢰도 및 검증상태
summary: "SK이노베이션 E&S의 기업정보 데이터에 대한 정보원별 신뢰도 등급 체계(S1A~S4)와 검증 현황을 정리한 문서로, 완료된 검증항목과 보완이 필요한 갭을 명시한다."
tags: [d01, identity, schema, table, "xref:d13", "xref:d07", "xref:d11", "xref:d12"]
keywords: [Source Tier, GAP ID, 조직 메타데이터, 2024년 합병, CIC, 신뢰도 분류, 검증 현황, 자회사, 임원, entity_id, 정보원 등급, 법정공시, 자회사 검증, CIC 전환, 조직도, 임원 목록, 데이터 품질]
related: [GAP-ENS-D01-001, GAP-ENS-D01-002, GAP-ENS-D01-003, GAP-ENS-D01-004, GAP-ENS-D01-005, GAP-ENS-D01-006]
priority: normal
domain: D01
section: 18
source: SK이노베이션E&S_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 841
updated: 2026-08-06
---

> SK이노베이션 E&S · D01 기업 기본정보·법인구조·연혁

# 18. 데이터 신뢰도 및 검증상태

## 18.1 Source Tier

| Tier | 기준 | 본 D01 적용 |
|---|---|---|
| `S1A` | 법정공시·등기·정부 원장 | 합병 법적효력 추가 감사 필요 |
| `S1B` | 회사 공식 홈페이지·공식 그룹 발표 | 주된 근거 |
| `S2A` | 정부·공공기관·거래소 | 후속 검증용 |
| `S2B` | 파트너사 공식자료 | 프로젝트 교차검증용 |
| `S3` | 신뢰도 높은 언론 | 공식자료 공백 보완용 |
| `S4` | 블로그·재인용·출처불명 | 사실근거로 사용 금지 |

## 18.2 검증 완료 항목

- 2024년 11월 1일 합병 및 CIC 전환
- 현재 공식 명칭과 본사 주소
- 1999년 설립, 2005년 사명변경 등 주요 연혁
- 공식 사업영역 5대 메뉴와 LNG·Power 통합 정체성
- 현재 공식 이사회상 추형욱의 E&S CIC 사장 지위
- 국내 도시가스·발전·수소 자회사 1차 목록
- 공식 해외 네트워크 1차 목록

## 18.3 후속 검증 필요 항목

| Gap ID | 항목 | 상태 | 인계 도메인 |
|---|---|---|---|
| `GAP-ENS-D01-001` | 2026년 최신 조직도와 세부 부문명 | `PENDING_INTERNAL_DATA` | D13 |
| `GAP-ENS-D01-002` | 모든 국내외 자회사 법적 상호·지분율 | `PENDING_PUBLIC_REGISTRY_AUDIT` | D07/D13 |
| `GAP-ENS-D01-003` | CIC 단위 손익·자산의 공시 Segment 경계 | `PENDING_FINANCIAL_AUDIT` | D11/D12 |
| `GAP-ENS-D01-004` | 최신 임원·자회사 대표 전수목록 | `PENDING_LATEST_DISCLOSURE` | D13 |
| `GAP-ENS-D01-005` | UK·Vietnam 거점의 법인·지점 여부 | `PENDING_ENTITY_AUDIT` | D07 |
| `GAP-ENS-D01-006` | 합병 전후 계약 당사자 승계 상세 | `PENDING_CONTRACT_REVIEW` | D13 |

---

# 19. D01 최종 요약 레코드

```yaml
domain: D01_Corporate_Identity
version: 1.0
as_of_date: 2026-08-03
canonical_target:
  entity_id: ORG-SKI-ENS-CIC-000001
  name_ko: SK이노베이션 E&S
  name_en: SK Innovation E&S
  entity_type: company_in_company
  separate_legal_entity: false
  parent_legal_entity: SK Innovation Co., Ltd.
historical_entity:
  entity_id: ORG-SKENS-LEGAL-000001
  name: SK E&S Co., Ltd.
  established_origin: 1999-01 SK-Enron Co., Ltd.
  renamed: 2005-10
  merged_into_parent: 2024-11-01
headquarters:
  address: 서울특별시 종로구 종로 26
leadership:
  ens_cic_president: 추형욱
business_identity:
  official_phrase: Sustainable Energy Solution Optimizer
  pillars:
    - LNG Value Chain
    - Power Generation and City Gas
    - Renewable Energy
    - Hydrogen and CCS
    - Energy Solution
data_status: PUBLIC_SOURCE_COMPLETE_V1
internal_validation_required: true
next_domain: D02_Business_Portfolio
```

---
