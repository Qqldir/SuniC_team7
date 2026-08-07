---
id: skon-d00-d00-10-current-integration-findings
title: Current Integration Findings
summary: "D01~D17 통합검수에서 발견된 10개 데이터 오류의 해결 현황과 자동검수 결과, 공개불가 항목을 정리한 표"
tags: [d00, governance, table, "xref:d01", "xref:d02", "xref:d03", "xref:d07"]
keywords: [통합검수, Source ID, Canonical URL, Crosswalk, 자동검수, 내부자료, FTO, 기준일, 검수 발견사항, 데이터 품질, Canonical URL Crosswalk, 공개제한, 오류 해결, 검증 현황]
related: [VAL-D00-000001, VAL-D00-000002, VAL-D00-000003, VAL-D00-000004, VAL-D00-000005, VAL-D00-000006, VAL-D00-000007, COMP-SKON-001, CO-SKON, ORG-SKON-000001, VAL-D00-000008, VAL-D00-000009, VAL-D00-000010]
priority: normal
domain: D00
section: D00-10
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 1158
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-10 Current Integration Findings

### 1. 통합검수 발견사항과 처리결과

| ID | 발견사항 | 처리결과 | 잔여 통제 | 상태 |
|---|---|---|---|---|
| `VAL-D00-000001` | D01·D02 Source ID 부재 | 번호 각주를 Legacy ID로 명시하고 Canonical URL Crosswalk 연결 | 번호형 ID를 재사용하지 않음 | `RESOLVED` |
| `VAL-D00-000002` | D03~D07 Header Version 불일치 | v1.5.1·v1.8.1·v2.0.1·v1.6.1·v1.3.1로 Header Patch | 누적 Part 내부 Version은 역사기록으로 보존 | `RESOLVED` |
| `VAL-D00-000003` | D08 Source Namespace 비표준 | Legacy Namespace로 선언·Canonical URL Crosswalk 연결 | 기존 ID 삭제·재발급 금지 | `RESOLVED` |
| `VAL-D00-000004` | D17의 D05 `OPEN_GAP` 불일치 | 공개 DB 완료·Decision-Date 내부/법률 Gate로 정정 | 최종 FTO·제품실시는 내부검증 전 금지 | `RESOLVED_WITH_GATE` |
| `VAL-D00-000005` | 동일 원문의 도메인별 Source ID 중복 | 839회 URL을 511개 Canonical URL로 통합 | Source 등급·발행일 상세필드는 점진 보강 | `RESOLVED_AT_URL_IDENTITY_LEVEL` |
| `VAL-D00-000006` | 511개 URL의 일괄 접근상태 미검수 | URL 문법·정규화·도메인 출현은 전수검수 | 외부 접근·Redirect·내용변경은 월간 Refresh Queue | `CONTROLLED_OPEN` |
| `VAL-D00-000007` | `COMP-SKON-001`·`CO-SKON` 혼재 | 둘 다 `ORG-SKON-000001` Alias로 연결 | 법인·Segment·CIC 구분 유지 | `RESOLVED` |
| `VAL-D00-000008` | 도메인별 상태·Evidence 용어 차이 | D08~D16 상단에 D00 해석규칙 추가 | Domain-local 상태값은 원문 호환성 때문에 보존 | `RESOLVED_BY_MAPPING` |
| `VAL-D00-000009` | Seed Lineage 분산 | D05 18개를 포함한 279개 Ledger 생성; 166개 직접참조·113개 `DEFERRED` | 보류 Seed 승격 시 Merge/Reject 사유 추가 | `RESOLVED_WITH_BACKLOG` |
| `VAL-D00-000010` | 기준일 7/29~8/3 혼재 | Domain 기준일과 8/3 통합검수일을 병기 | 최신성 높은 Event는 Trigger에 따라 재검수 | `RESOLVED_BY_BITEMPORAL_CONTROL` |

### 2. 자동검수 결과

| 검사 | 결과 |
|---|---|
| 대상 파일 | D01~D17 17개 전부 존재 |
| Markdown code fence | 전 파일 짝수·미종결 0개 |
| 번호형 각주 | D01 14개·D02 16개, 누락 정의 0개 |
| URL | 839회·Canonical 511개 |
| 식별자 | 고유 1,491개 Crosswalk 생성 |
| D17 과제 ID | `D17-OI-001~060` 누락·중복 0개 |
| Source Seed | 279개; D17 직접참조 고유 166개·보류 113개 |
| Markdown 표 | 열 수 불일치 0개 |

### 3. 공개자료로 닫을 수 없는 항목

| 범주 | 대표 내부자료 | D00 상태 |
|---|---|---|
| 제품·공정 | BOM, Recipe, Revision, 공정실적, Defect Library | `PENDING_INTERNAL_DATA` |
| 생산·수요 | Line별 승인 Capacity, Forecast, Call-off, Accepted GWh | `PENDING_INTERNAL_DATA` |
| 원가·현금 | Program Margin, Cost-to-Serve, CAPEX, Credit Cash | `PENDING_INTERNAL_DATA` |
| 계약·JV | 가격, Reserved Matter, Capital Call, 보증, Exit, Data/IP 조항 | `PENDING_INTERNAL_DATA` |
| 규제 | Taxpayer, PFE 원가, Shipment Chain, Passport Instance | `PENDING_INTERNAL_DATA` |
| IP | 제품 Element Map, 비공개 계약, 최종 FTO 의견 | `PENDING_LEGAL_REVIEW` |
| 품질·안전 | 전사 불량률, 보증, 사고·Near Miss, Barrier 상태 | `PENDING_INTERNAL_DATA` |
| Provider | 가격, 보안, 실제 KPI, 독점·경쟁관계, Vendor Health | `PENDING_DUE_DILIGENCE` |

공개자료로 닫을 수 없다는 것은 DB가 미완성이라는 뜻이 아니라, **공개 Fact와 내부 의사결정 Gate의 경계를 지켰다는 뜻**이다.

---
