---
id: skes-d04-16-d04-expanded-seed-crosswalk
title: D04 Expanded Seed Crosswalk
summary: "D03 기술을 D05-D16 도메인에 매핑한 크로스워크 테이블, D04 완성도, D05 이관 우선순위를 담은 기술체계 매핑 문서"
tags: [d04, technology, schema, table, "xref:d03", "xref:d05", "xref:d06", "xref:d07"]
keywords: [크로스워크, 씨앗기술, 도메인 매핑, Crosswalk, 기술 기회, 이관, 검색 우선순위, LNG 최적화, 에너지저장장치]
related: []
priority: normal
domain: D04
section: 16
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: Part 2. 대표기업 기술체계 심층 확장
tokens: 839
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · Part 2. 대표기업 기술체계 심층 확장

## 16. D04 Expanded Seed Crosswalk

| Technology Opportunity | D03 Seed 범위 | D05 검색 | D06 운영 | D07 자산 | D15 위험 | D16 외부솔루션 |
|---|---|---|---|---|---|---|
| LNG secure optimization | 001~003, 022~025 | 특허/내부역량 | 프로세스·시스템 | 선박·터미널 | 계약·OT | solver·AIS·hybrid model |
| Power health dispatch | 003~004, 026~028 | 발전 AI/특허 | 운전·정비 | 발전소·열망 | 안전·OEM | digital twin·APM |
| City-gas intelligence | 005~007, 029~033 | RBMS/OCR/AMI | 검침·점검·출동 | 배관·계량 | 가스안전·개인정보 | GIS·vision·FSM |
| Renewable/PPA | 008~011, 034~037 | forecast/PPA IP | 개발·O&M·정산 | 발전자산 | 계약·드론 | forecast·CMMS·lineage |
| Liquid hydrogen | 012~014, 038~040 | 액화·극저온 IP | 생산·물류 | 플랜트·차량·충전소 | 극저온·고압 | APM·routing·twin |
| ESS/KCE | 015~018, 041~047 | MarketCapture/ESS IP | 입찰·정비 | BESS | 화재·사이버 | MLOps·degradation |
| EV charging | 019~020, 048~050 | SmartPower/mesh IP | 설치·운영·A/S | charger·site ESS | 결제·전기안전 | FSM·smart charging |
| CCS MRV | 021, 051~052 | MRV/monitoring IP | project process | capture/transport/storage | 국제규제·책임 | meter·lineage·subsurface |

## 17. D04 v2 Completion Record

```yaml
domain: D04_Technology_Taxonomy
version: 2.0
depth_policy: representative_company_deep_database
base_technology_records: 61
application_crosswalk_records: 25
owned_capability_records: 12
detailed_priority_technology_cards: 10
data_architecture_layers: 8
model_deployment_tiers: 5
poc_cluster_designs: 13
D03_seed_crosswalk_total: 52
priority_rule:
  - reuse owned KCE EverCharge RBMS PPA LNG capability first
  - advisory before closed-loop automation
  - operating data domains before planned businesses
  - safety contract cyber and data-right gates are mandatory
next_domain: D05_RnD_Patents_and_Intellectual_Property
```

## 18. Revised D05 Handover

```yaml
handover_id: HANDOVER-ENS-D04-D05-002
source_domain_version: D04_v2.0
search_priority:
  P0:
    - SK E&S and city-gas subsidiaries RBMS drone AMI customer digital patents
    - KCE MarketCapture storage bidding software and grid ESS capability
    - EverCharge SmartPower mesh EVSE load-management patents
    - liquid-hydrogen purification liquefaction storage transport refueling
    - LNG terminal BOG efficiency vessel scheduling and power optimization
  P1:
    - renewable forecasting O&M direct-PPA settlement
    - DERMS VPP interoperability
    - CCS MRV capture transport storage
attribution_rule:
  - applicant owner assignee inventor affiliate relationship must be explicit
  - SK Group patent is not automatically E&S capability
  - acquisition date and capability ownership timeline must be preserved
  - academic paper without E&S commercialization link is reference only
```
