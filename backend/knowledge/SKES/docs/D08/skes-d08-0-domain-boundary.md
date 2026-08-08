---
id: skes-d08-0-domain-boundary
title: Domain Boundary
summary: 공급중단·가격변동이 자산·공정·손익에 전파되는 경로를 추적하는 LNG·발전·신재생 공급망 도메인의 경계와 11개 공급군 범위를 정의한다.
tags: [d08, supply-chain, core-candidate, table, "xref:d06", "xref:d07", "xref:d16", "xref:d09"]
keywords: [LNG 공급망, 공급망 도메인 설계, 원료·기자재·물류, 액화·선박·터미널, 신재생에너지·ESS·수소, 공급사 위험관리, 계약·사용권·지분, 공급중단 영향 추적, 협력사 실사·거버넌스]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001, ORG-SKI-LEGAL-000001]
priority: critical
domain: D08
section: 0
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 1417
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# SK이노베이션 E&S AI Knowledge Database

## D08. Supply Chain, Procurement, Raw Materials & Logistics｜공급망·조달·원료·물류

**Version 1.0 / 기준일: 2026년 8월 5일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Parent after merger: `ORG-SKI-LEGAL-000001`
- Source namespace: `SRC-ENS-D08-*`
- Supplier namespace: `SUP-ENS-D08-*`
- Supply-flow namespace: `FLOW-ENS-D08-*`
- Contract/right namespace: `CTR-ENS-D08-*`
- Material/service namespace: `MAT-ENS-D08-*`
- Logistics namespace: `LOG-ENS-D08-*`
- Risk namespace: `RSK-ENS-D08-*`
- O/I Seed namespace: `SEED-ENS-D08-*`
- Inherited scope: D06 45개 프로세스·D07 78개 자산과 `asset_id`, `right_id`, `supplier_id`, `material_flow_id`로 연결

---

# 0. Domain Boundary

## 0.1 목적

D08은 SK이노베이션 E&S의 사업을 움직이는 원료·기자재·서비스·물류·계약상 권리를 하나의 공급망 데이터 모델로 정리한다. 핵심은 단순 공급사 명단이 아니라, 공급중단이나 가격변동이 어느 자산·공정·고객·손익으로 전파되는지 추적할 수 있는 디지털 공급망 원장을 만드는 것이다.

D08은 다음 질문에 답하도록 설계한다.

1. LNG는 어느 원천에서 어떤 권리로 확보되고 어느 액화·선박·터미널 경로를 통과하는가.
2. 생산지분, 장기구매, 액화설비 사용권, 터미널 사용권, 현물구매는 어떻게 다른가.
3. 수요예측·cargo 일정·재고·발전 dispatch·시장가격이 어느 의사결정에서 결합되는가.
4. 공급자·OEM·EPC·O&M·물류사 의존도가 어느 자산에 집중되는가.
5. 공급사 품질·안전·ESG·사이버·재무 위험을 어떤 증빙과 지표로 관리해야 하는가.
6. 공개자료로 확인된 공급관계와 내부자료가 필요한 추정 영역을 어떻게 분리하는가.
7. 어떤 데이터와 외부 솔루션이 원가·안정성·재고·납기·탄소를 개선할 수 있는가.

## 0.2 포함 범위

| 공급망군 | 포함 항목 | 핵심 경계 |
|---|---|---|
| LNG upstream | 가스전 지분·생산·장기 도입·spot | 생산량·권리물량·실제 인도량 분리 |
| LNG liquefaction | Darwin 지분·Freeport tolling | equity와 use-or-pay 사용권 분리 |
| LNG shipping | 전용선·용선·voyage·연료·docking | 선박 소유·용선·운항관리 분리 |
| LNG terminal | Boryeong TUA·Ganyu 사용권 | 터미널 총능력과 E&S 계약권 분리 |
| Power/CHP | 발전연료·OEM 부품·정비·화학약품 | D16 솔루션 벤더와 구매 품목을 구분 |
| City gas | 도매가스·배관·밸브·정압·계량·시공 | 공개되지 않은 공급사명은 미확정 처리 |
| Renewable | 터빈·모듈·인버터·케이블·EPC·선박 | 프로젝트 공개 확인 범위만 확정 |
| ESS | cell·rack·PCS·EMS·EPC·LTSA | KCE 공개 프로젝트별 공급관계 연결 |
| EV charging | EVSE·통신·전기공사·부품·서비스 | EverCharge 자체 제조와 외부 부품 구분 |
| Liquid hydrogen | 부생수소·정제·액화·탱크·tank trailer | 명목능력과 실제 원료·출하량 분리 |
| CCS | 흡수제·압축·배관·주입·MRV 서비스 | 계획·실증과 상용 조달 분리 |
| Supplier governance | 등록·입찰·실사·품질·ESG·BCP | 협력사 약 100개 실사 pool과 전체 공급사 수 구분 |

## 0.3 제외 및 후속 이관

| 후속 문서 | 이관 항목 | D08 연결키 |
|---|---|---|
| D09 | 고객·offtake·PPA·전력/열/가스 수요 | `contract_id`, `customer_id` |
| D10 | LNG·SMP·REC·보조서비스 시장구조 | `market_id`, `price_index_id` |
| D11 | 연료비·용량요금·마진·운전자본 | `cost_id`, `flow_id` |
| D12 | 공급망 관련 CAPEX·재고금융 | `investment_event_id`, `asset_id` |
| D13 | JV·TUA·LTSA·EPC·PPA의 법적 조항 | `contract_id`, `right_id` |
| D14 | 수입·환경·안전·인허가·통상규정 | `compliance_id`, `origin_id` |
| D15 | 전사 위험·품질·안전·회복탄력성 | `risk_id`, `control_id` |
| D16 | 외부 디지털/설비 솔루션 벤더 후보 | `provider_id`, `use_case_id` |
| D17 | O/I 과제 추천·우선순위 | `seed_id`, `process_id`, `asset_id` |

---
