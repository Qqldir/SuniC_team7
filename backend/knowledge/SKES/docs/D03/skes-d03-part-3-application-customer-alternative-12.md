---
id: skes-d03-part-3-application-customer-alternative-12
title: Part 3. Application·Customer·Alternative·Graph·Chunk 확장 — D03 v2 Completion Record
summary: "D03 제품·솔루션 데이터베이스 v2.0의 구성 규모, 포함된 주요 사업 영역, 데이터 정의 기준, 다음 단계를 정의한 완성 보고"
tags: [d03, product, schema, "xref:d02", "xref:d04", "xref:d05"]
keywords: [데이터베이스, LNG, 전력발전, 수소, 에너지저장, 신재생에너지, 도시가스, VPP, 고객니즈, 경쟁격차]
related: []
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 3. Application·Customer·Alternative·Graph·Chunk 확장
tokens: 341
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 3. Application·Customer·Alternative·Graph·Chunk 확장

## 31. D03 v2 Completion Record

```yaml
domain: D03_Products_and_Solutions
version: 2.0
as_of_date: 2026-08-04
target: ORG-SKI-ENS-CIC-000001
depth_policy: representative_company_deep_database
base_catalog_count: 29
application_count: 25
disclosed_customer_partner_records: 8
customer_need_records: 9
competitive_gap_records: 8
direct_oi_seed_count_total: 52
expanded_ai_chunk_count: 15
query_template_count: 12
expanded_gap_count: 14
status_model:
  - operating
  - active_service
  - construction
  - development
  - pipeline
  - planned
  - considering
core_depth_clusters:
  - LNG procurement shipping terminal
  - power and CHP
  - city gas supply customer safety
  - renewable direct PPA
  - liquid hydrogen production logistics charging
  - KCE ESS MarketCapture
  - Ensolve DERMS VPP O&M
  - iPARKING EverCharge charging and BESS
  - low-carbon LNG and CCS MRV
fact_boundary:
  - undisclosed price contract performance not inferred
  - capacity not treated as production or sales
  - operating development and pipeline not summed
  - subsidiary products not treated as universal domestic E&S products
next_action:
  - align D02 and D04 to representative_company_deep_database
  - proceed D05 with the same depth policy
```
