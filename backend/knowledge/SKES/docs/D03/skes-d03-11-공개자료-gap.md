---
id: skes-d03-11-공개자료-gap
title: 공개자료 Gap
summary: "D03 제품·솔루션의 미확정 정보 현황과 데이터 상태를 추적하는 표로, 각 제품별 부족한 정보와 후속 도메인을 알 수 있다."
tags: [d03, product, schema, table, "xref:d09", "xref:d11", "xref:d13", "xref:d06"]
keywords: [미확정 정보, 데이터 확정, LNG 기능, 도시가스, 액화수소, ESS, EV 충전, 상용화 현황, PPA, O&M]
related: [GAP-ENS-D03-001, GAP-ENS-D03-002, GAP-ENS-D03-003, GAP-ENS-D03-004, GAP-ENS-D03-005, GAP-ENS-D03-006, GAP-ENS-D03-007, GAP-ENS-D03-008, GAP-ENS-D03-009]
priority: normal
domain: D03
section: 11
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: ""
tokens: 573
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션

# 11. 공개자료 Gap

| Gap ID | 미확정 정보 | 후속 도메인 | 상태 |
|---|---|---|---|
| `GAP-ENS-D03-001` | LNG 기능별 외부 고객·가격·독립 매출 | D09·D11·D13 | `PENDING_COMMERCIAL_DATA` |
| `GAP-ENS-D03-002` | 전력·열 판매량·고객·정산구조 | D09·D11 | `PENDING_SEGMENT_DATA` |
| `GAP-ENS-D03-003` | 도시가스 자회사별 앱·AMI·비대면 기능 보급률 | D06·D09 | `PENDING_OPERATING_DATA` |
| `GAP-ENS-D03-004` | PPA 계약별 용량·기간·가격·정산오류 | D09·D13 | `PENDING_CONTRACT_DATA` |
| `GAP-ENS-D03-005` | 액화수소 실제 생산·판매·가동률·고객 | D07·D09·D11 | `PENDING_COMMERCIAL_DATA` |
| `GAP-ENS-D03-006` | ESS 프로젝트별 운영용량·수익모델·화재안전 KPI | D07·D11·D15 | `PENDING_ASSET_BREAKDOWN` |
| `GAP-ENS-D03-007` | DERMS·VPP·O&M의 상용 고객·기능·매출 | D09·D11 | `PENDING_BUSINESS_VALIDATION` |
| `GAP-ENS-D03-008` | EV 충전기 수·이용률·서비스 권역·운영주체 | D07·D09 | `PENDING_ASSET_BREAKDOWN` |
| `GAP-ENS-D03-009` | 저탄소 LNG·CCS의 포집률·탄소강도·허가·고객 | D13·D14·D15 | `PENDING_PROJECT_VALIDATION` |

---

# 12. D03 최종 요약 레코드

```yaml
domain: D03_Products_and_Solutions
version: 1.0
as_of_date: 2026-08-04
target: ORG-SKI-ENS-CIC-000001
catalog_count: 29
commercial_or_active_focus:
  - LNG terminal shipping and power operations
  - electricity heat and city gas supply
  - city gas digital customer and safety services
  - renewable electricity direct PPA and cost analysis
  - liquid hydrogen production logistics and charging supply
  - demand renewable-linked and grid ESS
  - EV charging
planned_or_considering:
  - DERMS VPP renewable O&M
  - blue and green hydrogen
  - low-carbon LNG and cross-border CCS
direct_oi_seed_count: 21
data_status: PUBLIC_SOURCE_COMPLETE_V1_COMPACT
next_domain: D04_Technology_Taxonomy
```

---
