---
id: skes-d09-0-domain-boundary
title: Domain Boundary
summary: SK이노베이션의 LNG·전력·도시가스·수소 등 에너지 사업에서 고객·계약·수요를 연결하는 도메인 경계와 사업별 수요 판정 기준을 정의한다.
tags: [d09, customer, core-candidate, table, "xref:d03", "xref:d06", "xref:d07", "xref:d08"]
keywords: [고객, 오프테이커, 계약수요, LNG, 도시가스, 전력시장, PPA, 액화수소]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001]
priority: critical
domain: D09
section: 0
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 1314
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# SK이노베이션 E&S AI Knowledge Database

## D09. Customers, Orders, Contract Demand & Relationships｜고객·수주·계약수요·관계

**Version 1.0 / 기준일: 2026년 8월 5일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Customer namespace: `CUS-ENS-D09-*`
- Relationship namespace: `REL-ENS-D09-*`
- Demand namespace: `DEM-ENS-D09-*`
- Contract namespace: `CTR-ENS-D09-*`
- Service-event namespace: `EVT-ENS-D09-*`
- Risk namespace: `RSK-ENS-D09-*`
- O/I Seed namespace: `SEED-ENS-D09-*`
- Source namespace: `SRC-ENS-D09-*`
- Inherited joins: D03 제품·솔루션 29개, D06 프로세스 45개, D07 자산 78개, D08 공급계약·권리 12개

---

# 0. Domain Boundary

## 0.1 목적

D09는 SK이노베이션 E&S의 에너지 사업에서 누가 고객이고, 어떤 계약·시장·서비스 관계를 통해 수요가 발생하며, 그 수요가 실제 공급·운영·정산으로 어떻게 변환되는지를 구조화한다. 단순 고객사 목록이 아니라 `고객–계약–수요–자산–운영–정산–서비스–관계위험`을 연결하는 의사결정 DB다.

D09가 답해야 하는 질문은 다음과 같다.

1. LNG·전력·열·도시가스·PPA·ESS·EV 충전·수소의 실제 수요자는 누구인가.
2. 최종 소비자, 오프테이커, 시장운영기관, 망사업자, 지자체, JV 파트너를 어떻게 구분하는가.
3. 계약상 최대물량·예상수요·확정 nomination·실제 사용량·정산량은 어떻게 다른가.
4. 장기 PPA와 대규모 인프라 사업에서 수요·가격·신용·운영위험은 어떻게 연결되는가.
5. 도시가스 약 510만 세대의 고객 Journey 중 비용·불편·안전 위험이 집중되는 지점은 어디인가.
6. KCE의 전력시장 수익과 EverCharge의 사이트·운전자 서비스는 일반 B2B 수주와 무엇이 다른가.
7. 액화수소처럼 시장 형성 단계인 사업에서 협약·충전소·차량도입계획을 실제 확정수요로 오인하지 않으려면 무엇이 필요한가.
8. O/I 과제 추천에 필요한 고객데이터를 개인정보·계약기밀·시장규칙을 지키면서 어떻게 사용할 것인가.

## 0.2 포함 범위

| 관계군 | 포함 항목 | 핵심 판정 단위 |
|---|---|---|
| LNG·발전 | 내부·외부 연료수요, 발전시장, 송전·정산 관계 | cargo·MMBtu·MWh·nomination |
| CHP·열 | 전력·열 동시수요, 지역난방·건물·산업체 | MWh·Gcal·시간대 수요 |
| 도시가스 | 가정·상업·업무·산업·열병합·수송 고객 | 고객전·계량점·사용량·서비스건 |
| 재생에너지 | 직접 PPA·V.PPA·REC·O&M 수요 | MW·MWh·계약기간·인증량 |
| KCE BESS | ERCOT·NYISO 등 전력시장 및 utility 계약 | MW·MWh·bid·award·dispatch |
| EverCharge | 공동주택·직장·경기장·렌터카 fleet 사이트 | EVSE·session·kWh·uptime |
| 액화수소 | 충전소·버스운송사·기업통근버스·지자체 | kg·차량대수·station throughput |
| CCS | CO2 배출원·운송·저장·정부·JV 관계 | tCO2·MRV·storage entitlement |

## 0.3 제외 및 후속 이관

| 후속 문서 | 이관 내용 | D09 연결키 |
|---|---|---|
| D10 | 시장규모·경쟁사·가격형성·수요전망 | `market_id`, `segment_id` |
| D11 | 고객별 매출·마진·원가·LTV·손익 | `customer_id`, `contract_id` |
| D12 | 고객 확보·설비 증설 CAPEX와 자금조달 | `asset_id`, `demand_case_id` |
| D13 | 계약조항·JV·거버넌스·변경권·해지권 | `contract_id`, `relationship_id` |
| D14 | 요금규제·전력시장규칙·개인정보·인증 | `regulation_id`, `data_class` |
| D15 | 고객안전·품질·신용·운영복원력 | `risk_id`, `incident_id` |
| D16 | CRM·forecast·contact-center·optimization 공급사 | `solution_id`, `provider_id` |
| D17 | 과제 추천·PoC·우선순위 | `seed_id`, `benefit_case_id` |

---
