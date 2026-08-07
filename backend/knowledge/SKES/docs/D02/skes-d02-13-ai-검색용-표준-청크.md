---
id: skes-d02-13-ai-검색용-표준-청크
title: AI 검색용 표준 청크
summary: SK이노베이션 E&S의 LNG·도시가스·재생에너지·수소·에너지솔루션 등 각 사업 분야를 AI 검색을 위해 구조화한 청크 정의 및 데이터 갭 현황표.
tags: [d02, business, schema, table, "xref:d07", "xref:d13", "xref:d08", "xref:d11"]
keywords: [사업 포트폴리오, LNG, 도시가스, 재생에너지, 수소, 에너지솔루션, ESS, VPP, 메타데이터]
related: [GAP-ENS-D02-001, GAP-ENS-D02-002, GAP-ENS-D02-003, GAP-ENS-D02-004, GAP-ENS-D02-005, GAP-ENS-D02-006, GAP-ENS-D02-007]
priority: normal
domain: D02
section: 13
source: SK이노베이션E&S_D02_Business_Portfolio_v2_보강본.md
breadcrumb: ""
tokens: 1345
updated: 2026-08-06
---

> SK이노베이션 E&S · D02 사업 포트폴리오

# 13. AI 검색용 표준 청크

## Chunk D02-001｜전체 사업 포트폴리오

```yaml
chunk_id: CHUNK-ENS-D02-001
topic: business_portfolio_overview
answer: >
  SK이노베이션 E&S는 LNG 가스전·액화·운송·터미널·발전으로 이어지는 LNG Value Chain과
  도시가스, 재생에너지, 수소, ESS·VPP·DERMS·EV충전 등 Power Value Chain을 결합한다.
  기반사업은 LNG·발전·도시가스이고 성장사업은 재생에너지·수소·에너지솔루션·CCS다.
source_ids: [SRC-ENS-D02-0001, SRC-ENS-D02-0002]
```

## Chunk D02-002｜LNG 사업

```yaml
chunk_id: CHUNK-ENS-D02-002
topic: lng_value_chain
answer: >
  LNG 사업은 Barossa·Woodford·Tangguh의 자원과 조달, Darwin·Freeport 액화,
  전용 LNG선, 보령 터미널, 광양·파주·여주 발전 및 하남·위례 CHP를 연결한다.
  지분, 사용계약, 운영권, 직접운영은 서로 다른 권리다.
source_ids: [SRC-ENS-D02-0002]
```

## Chunk D02-003｜도시가스 사업

```yaml
chunk_id: CHUNK-ENS-D02-003
topic: city_gas
answer: >
  7개 도시가스 자회사가 8개 권역에서 약 510만 가구에 공급한다.
  공식 2023년 말 수치는 공급량 54억㎥, 국내 점유율 22.6%다.
  핵심 O/I 영역은 배관 위험도, 누출탐지, 수요예측, 원격검침, 정압기 예지보전이다.
source_ids: [SRC-ENS-D02-0003]
```

## Chunk D02-004｜재생에너지와 PPA

```yaml
chunk_id: CHUNK-ENS-D02-004
topic: renewable_energy
answer: >
  SK이노베이션 E&S는 태양광·육상풍력·해상풍력을 운영·개발하고 RE100 직접 PPA를 제공한다.
  약 5GW 파이프라인은 개발단계를 포함하며 상업운전 용량으로 보면 안 된다.
  전남 해상풍력 1단계는 2025년 운영을 시작했고 2·3단계는 개발계획이다.
source_ids: [SRC-ENS-D02-0004]
```

## Chunk D02-005｜수소 사업

```yaml
chunk_id: CHUNK-ENS-D02-005
topic: hydrogen
answer: >
  현재 상업화 핵심은 인천 연 3만 톤 액화수소플랜트와 공급망이다.
  보령 블루수소와 재생전력 기반 그린수소는 장기 개발·추진 단계이므로 현재 실적과 구분한다.
source_ids: [SRC-ENS-D02-0005]
```

## Chunk D02-006｜에너지솔루션

```yaml
chunk_id: CHUNK-ENS-D02-006
topic: energy_solution
answer: >
  에너지솔루션은 ESS, DERMS, VPP, 재생에너지 O&M, EV충전, 미국 KCE의 계통 ESS로 구성된다.
  주요 O/I 과제는 ESS 안전·입찰 AI, 분산자원 표준연동, VPP 예측·정산,
  충전기 고장예측과 충전부하 최적화다.
source_ids: [SRC-ENS-D02-0006]
```

---

# 14. 공개자료 Gap

| Gap ID | 미확정 정보 | 후속 도메인 | 처리상태 |
|---|---|---|---|
| `GAP-ENS-D02-001` | 자산별 소유지분·귀속용량·연결범위 | D07·D13 | `PENDING_PUBLIC_FILING_REVIEW` |
| `GAP-ENS-D02-002` | LNG 계약가격·기간·take-or-pay·hedge | D08·D13 | `PENDING_CONTRACT_DATA` |
| `GAP-ENS-D02-003` | 사업별 매출·EBITDA·CAPEX | D11·D12 | `PENDING_SEGMENT_DATA` |
| `GAP-ENS-D02-004` | 재생에너지 5GW의 운영·건설·개발 구분 | D07 | `PENDING_ASSET_BREAKDOWN` |
| `GAP-ENS-D02-005` | KCE 0.6GW의 운영·건설·개발 구분 | D07 | `PENDING_ASSET_BREAKDOWN` |
| `GAP-ENS-D02-006` | 수소 고객·장기 offtake·가동률 | D09·D13 | `PENDING_COMMERCIAL_DATA` |
| `GAP-ENS-D02-007` | CCS 포집률·저장허가·FID·상업개시 | D13·D14 | `PENDING_PROJECT_VALIDATION` |

---

# 15. D02 최종 요약 레코드

```yaml
domain: D02_Business_Portfolio
version: 1.0
as_of_date: 2026-08-04
target: ORG-SKI-ENS-CIC-000001
portfolio:
  base_cashflow:
    - BUS-ENS-01 LNG Value Chain
    - BUS-ENS-02 City Gas
    - BUS-ENS-03 Power and CHP
  growth:
    - BUS-ENS-04 Renewable Energy
    - BUS-ENS-05 Hydrogen
    - BUS-ENS-06 Energy Solution
    - BUS-ENS-07 CCS and Low-carbon LNG
priority_oi_domains:
  - integrated LNG demand inventory and generation optimization
  - asset reliability and predictive maintenance
  - pipeline and process safety
  - renewable forecasting and O&M
  - ESS VPP DERMS optimization
  - hydrogen liquefaction logistics and safety
  - emissions and CCS MRV
data_status: PUBLIC_SOURCE_COMPLETE_V1_COMPACT
next_domain: D03_Products_and_Solutions
```

---
