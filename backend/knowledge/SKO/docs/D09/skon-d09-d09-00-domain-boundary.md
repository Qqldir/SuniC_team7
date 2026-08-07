---
id: skon-d09-d09-00-domain-boundary
title: Domain Boundary
summary: SK온 D09 도메인의 경계를 정의하여 고객·프로그램·계약·주문 간 관계 연계 방법과 공개 범위 판정 원칙을 제시한다.
tags: [d09, customer, core-candidate, table, "xref:d08", "xref:d17", "xref:d00", "xref:d07"]
keywords: [고객·OEM, Vehicle Program, 공급계약, Call-off·Forecast, GWh, 포함·제외범위, 공개원칙, D09, ESS프로젝트, Nomination, 고객 마스터, OEM, 차종 프로그램, ESS, 콜오프, 도메인 범위, 공개 판정, 고객집중도]
related: []
priority: critical
domain: D09
section: D09-00
source: SK온_D09_Customers_Orders_OEM_Relationships.md
breadcrumb: "SK온 D09 — Customers, Orders & OEM Relationships"
tokens: 899
updated: 2026-08-03
---

> SK온 · D09 고객·수주·OEM 관계 · SK온 D09 — Customers, Orders & OEM Relationships

# SK온 D09 — Customers, Orders & OEM Relationships

- 문서 버전: **v1.0.1**
- 기준일: **2026-08-03 (KST)**
- 이전 완료 지점: `D08 Raw Materials, Suppliers & Supply Chain v1.0`
- 작성 방식: **실무형 요약 DB** — 핵심 사실·Pain Point·외부 사례·O/I 기회는 유지하고, 비공개 계약조건의 과도한 추정은 배제
- 상위 목적: SK온의 고객·차종/프로그램·공급계약·수요·생산거점 관계를 연결하고 D17 O/I 과제 추천에 투입
- D00 통합검수: Domain-local Source/Entity ID를 보존하고 Canonical Alias는 D00 Crosswalk로 해석한다. 기존 상태값은 D00의 Fact Class·Evidence·Unknown Standard와 함께 사용한다.

---

## D09-00 Domain Boundary

### 1. 도메인 정의

D09는 SK온의 고객을 단순 명단으로 관리하지 않고 다음 흐름을 연결한다.

```text
Customer / OEM
→ Vehicle·ESS Program
→ Agreement / Nomination
→ Forecast / Call-off / Purchase Order
→ Cell·Chemistry·Revision
→ Qualified Plant·Line
→ Shipment / Customer Acceptance
→ Claim·Compensation·Program Change
```

이 구조를 사용해야 장기계약의 총 GWh, 실제 연도별 주문, 공장별 고객승인 Capacity, 실제 출하량을 서로 다른 값으로 보존할 수 있다.

### 2. 포함·제외 범위

| 포함 | 제외 또는 다른 도메인 원본 |
|---|---|
| OEM·ESS 고객 Master | 공장·Capacity 원본은 D07 |
| 차종·플랫폼·ESS 프로젝트 | 제품 성능·Chemistry 원본은 D03~D04 |
| 공급계약·JV·미래 수주·관계 상태 | 소재·원산지·PFE 원본은 D08 |
| Forecast·Call-off·Nomination·고객승인 스키마 | 제조공정 원본은 D06 |
| 고객집중·프로그램 지연·취소·수요변동 Risk | 원가·계약 수익성은 D11 |
| 고객 대응·수요계획 O/I 과제 | 품질·보증·리콜 원본은 D15 |

### 3. 공개자료 판정 원칙

1. `주요 고객`이라는 보도와 `특정 차종·공장에 현재 공급`을 분리한다.
2. 장기계약 총 GWh를 연간 수요나 공장 Capacity로 바꾸지 않는다.
3. `최대`, `option`, `right of first offer`, `preferential negotiation right`는 확정 주문과 분리한다.
4. 과거 탑재차종은 현재 양산·공급이 재확인되지 않으면 `HISTORICAL_CONFIRMED`로 둔다.
5. JV Capacity는 파트너 고객 전용범위와 SK온이 자유롭게 배분 가능한 Capacity를 구분한다.
6. 고객 보상금은 고객·사유·반복가능성이 공개되지 않으면 개별 고객 관계에 귀속하지 않는다.
7. 매체의 고객 추정은 보조근거로만 사용하고 당사자 발표·공시와 같은 등급으로 올리지 않는다.

---
