---
id: skes-d00-d00-02-canonical-source-master
title: Canonical Source Master
summary: "정보 출처의 신뢰도를 S1A~S5 등급으로 평가하고 증거 수준을 E0~E4로 분류하며, 출처 기록 스키마와 URL 정규화 규칙을 규정한 데이터 품질 기준."
tags: [d00, governance, schema, table]
keywords: [신뢰도 등급, 증거 수준, 출처 검증, URL 정규화, 신뢰성 판정, 검증 상태, S1A/S1B/S2/S3/S4/S5, E0/E1/E2/E3/E4, 출처 신뢰도, 신뢰성 평가, "S1A, S1B, S2", E0~E4, 데이터 마스터, 원문 검증]
related: []
priority: normal
domain: D00
section: D00-02
source: SK이노베이션E&S_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master"
tokens: 794
updated: 2026-08-06
---

> SK이노베이션 E&S · D00 소스·엔티티·ID·변경이력 마스터 · SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master

## D00-02 Canonical Source Master

### Source Record Schema

```yaml
source_record:
  canonical_source_id: SRC-ENS-CAN-000001
  title: ""
  publisher_entity_id: ""
  source_type: LAW|REGULATOR|FILING|COMPANY_PRIMARY|STANDARD|RESEARCH|MEDIA|VENDOR_CLAIM
  original_url: ""
  canonical_url: ""
  publication_date: null
  effective_date: null
  access_date: null
  jurisdiction: ""
  reliability_grade: S1A|S1B|S2|S3|S4|S5
  evidence_level: E0|E1|E2|E3|E4
  validation_status: VERIFIED_CURRENT|VERIFIED_HISTORICAL|MOVED|BROKEN|NOT_REVALIDATED_D00
  used_by_domains: []
  supported_claim_ids: []
  supersedes_source_ids: []
  last_verified_at: null
  next_review_at: null
```

### 출처 신뢰도

| Grade | 유형 | 허용 용도 | 제한 |
|---|---|---|---|
| S1A | 법령·정부·규제기관·거래소·공식 등록부 | 시행일·의무·공시수치 | 비공개 적용사실은 확정 불가 |
| S1B | 당사자 공식 홈페이지·IR·보도자료·보고서 | 회사 발표·사업·목표·실적 | 독립검증과 구분 |
| S2 | 국제기구·학술·공공연구·표준기관 | 산업 Baseline·방법론 | E&S 내부 적용을 자동 확정하지 않음 |
| S3 | 신뢰 언론·통신사 | 사건·업계 맥락·교차검증 | 계약·권리 단독 확정 금지 |
| S4 | 전문매체·컨설팅·산업DB·벤더 사례 | 후보 탐색·Benchmark | 핵심 Fact는 S1/S2 보강 |
| S5 | 검색요약·블로그·출처불명 | 키워드 발견 | 사실 확정 금지 |

### Evidence Level

| Level | 의미 |
|---|---|
| E0 | 존재 또는 마케팅 주장만 확인 |
| E1 | 계획·MOU·목표·검토 발표 |
| E2 | 계약·발주·FID·금융종결·설치 등 실행 Event |
| E3 | 가동·상업운전·고객적용·운영 확인 |
| E4 | 독립검증 성과·감사·규제판정 |

### URL 정규화 규칙

1. scheme·host는 소문자로 통일한다.
2. 끝의 `/`와 문장부호를 제거한다.
3. `utm_*`, `gclid`, `fbclid`는 제거한다.
4. 법령번호·공시번호·DOI·특허번호가 있으면 URL보다 우선 식별자로 사용한다.
5. Redirect는 Source ID를 삭제하지 않고 Canonical URL과 변경이력을 갱신한다.
6. PDF와 HTML이 같은 원문이면 Alias로 묶되 내용·버전이 다르면 별도 Source Version으로 둔다.
7. 동적 페이지는 access date와 content hash 없이 같은 사실로 간주하지 않는다.

별도 원장: `SK이노베이션E&S_D00_Canonical_Source_Crosswalk.csv`

---
