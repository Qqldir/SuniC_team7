---
id: skes-d07-0-domain-boundary
title: Domain Boundary
summary: SK이노베이션 E&S의 LNG·발전·도시가스·재생에너지·ESS·EV충전·수소·CCS 11개 자산군의 포함·제외 범위와 다른 도메인으로의 이관 구조를 규정하는 데이터 모델 정의 문서
tags: [d07, footprint, core-candidate, table, "xref:d02", "xref:d05", "xref:d06", "xref:d08"]
keywords: [LNG 터미널, 발전소 용량, 도시가스 배관, 재생에너지 설비, ESS 저장시스템, 액화수소, CCS 탄소포집, EV 충전소, 자산 소유권, O&M 운영 수탁]
related: []
priority: critical
domain: D07
section: 0
source: SK이노베이션E&S_D07_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1249
updated: 2026-08-06
---

> SK이노베이션 E&S · D07 터미널·발전소·배관 등 자산·용량

# SK이노베이션 E&S AI Knowledge Database

## D07. Footprint, Plants, Equipment & Capacity｜사업장·플랜트·설비·생산능력

**Version 1.0 / 기준일: 2026년 8월 5일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: ORG-SKI-ENS-CIC-000001
- Historical legal entity: ORG-SKENS-LEGAL-000001
- Parent after merger: ORG-SKI-LEGAL-000001
- Source namespace: SRC-ENS-D07-*
- Site namespace: SITE-ENS-D07-*
- Asset namespace: AST-ENS-D07-*
- Capacity namespace: CAP-ENS-D07-*
- Right namespace: RGT-ENS-D07-*
- Status-event namespace: EVT-ENS-D07-*
- O/I Seed namespace: SEED-ENS-D07-*
- Inherited scope: D02~D05 대표기업 심층본 및 D06 45개 프로세스·29개 설비군·68개 O/I Seed

---

# 0. Domain Boundary

## 0.1 목적

D07은 SK이노베이션 E&S의 LNG·발전·도시가스·재생에너지·ESS·EV 충전·액화수소·CCS 관련 물리 거점과 계약 기반 사용권을 하나의 자산 데이터 모델로 정리한다. 핵심은 “회사가 소개하는 사업”을 “회사가 소유·운영·사용·개발하는 구체 자산”으로 변환하는 것이다.

D07은 다음 질문에 답하도록 설계한다.

1. 자산은 어디에 있고 누가 소유·운영하는가.
2. 공개된 능력은 설계능력, 계약권리, 실제 생산량, 개발 파이프라인 중 무엇인가.
3. 총능력과 지분귀속능력, 사용권, O&M 수탁범위가 어떻게 다른가.
4. 운영·건설·개발·계획·매각 상태가 언제 바뀌었는가.
5. D06 공정이 어느 현장·설비에서 실행되는가.
6. 자산 집중도와 병목은 어느 지점에서 발생하는가.
7. O/I 과제를 위해 필요한 태그·정비·상업 데이터는 어느 자산에서 확보해야 하는가.

## 0.2 포함 범위

| 자산군 | 포함 단위 | 핵심 경계 |
|---|---|---|
| LNG Upstream | 가스전·셰일가스 생산권 | 지분율·도입권·연간 설명물량 분리 |
| LNG Liquefaction | 액화플랜트·사용계약 | 지분과 tolling·사용권 분리 |
| LNG Shipping | LNG 운반선·선대 | 선박 실명과 공개되지 않은 선대 ID 분리 |
| LNG Terminal | 저장탱크·기화·송출·부두 | 터미널 총능력과 E&S 사용권 분리 |
| Power/CHP | 복합발전·열병합·O&M 수탁 | 발전 MW, 열 Gcal/h 또는 t/h를 별도 저장 |
| City Gas | 7개 법인·8개 권역·배관망 | 공급권역 통계와 미공개 설비수 분리 |
| Renewable | 태양광·육상/해상풍력 | 운영·개발·파이프라인 혼합값 금지 |
| ESS | KCE 운영·개발 BESS | MW와 MWh, 프로젝트와 포트폴리오 중복 금지 |
| EV Charging | EverCharge 설치사례·분산 충전기 | 설치 port, EV-ready circuit, 계획 port 분리 |
| Hydrogen | 액화플랜트·저장·물류·충전소 | 명목 생산능력과 실제 생산량 분리 |
| CCS | 포집·수송·저장 후보 | 계획·실증과 상용운영 분리 |

## 0.3 제외 및 후속 이관

| 후속 문서 | 이관 항목 | D07 연결키 |
|---|---|---|
| D08 | LNG 계약·공급자·선박 조달·연료·재고 | asset_id, right_id, supplier_id |
| D09 | 발전·도시가스·PPA·충전 고객 | site_id, customer_segment_id |
| D10 | 전력·가스·REC·보조서비스 시장 | asset_id, market_id |
| D11 | 자산별 매출·연료비·정비비·마진 | asset_id, cost_center_id |
| D12 | 신규 건설·증설·대정비 CAPEX | asset_id, investment_event_id |
| D13 | JV·TUA·PPA·O&M·LTSA 계약 | right_id, contract_id |
| D14 | 인허가·안전·환경·계통접속 | site_id, permit_id |
| D15 | 물리·운영·기후·지정학 위험 | asset_id, risk_id |
| D16 | OEM·EPC·디지털 솔루션 공급자 | equipment_id, provider_id |
| D17 | O/I 과제 및 PoC 우선순위 | seed_id, asset_id, process_id |

---
