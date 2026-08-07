---
id: skes-d03-1-product-and-solution-master
title: Product and Solution Master
summary: SK이노베이션 E&S의 LNG·발전·도시가스·재생에너지 등 에너지 제품 및 서비스별 고객·공급방식·운영상태를 정리한 마스터 카탈로그.
tags: [d03, product, table, "xref:d17", "xref:d02"]
keywords: [LNG 조달, 도시가스 공급, 태양광발전, 풍력발전, PPA, 천연가스 발전, 운영상태, 고객가치, 밸류체인, 상업화 단계]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001, PS-ENS-LNG-01, PS-ENS-LNG-02, PS-ENS-LNG-03, PS-ENS-LNG-04, PS-ENS-PWR-01, PS-ENS-PWR-02, PS-ENS-CG-01, PS-ENS-CG-02, PS-ENS-CG-03, PS-ENS-REN-01, PS-ENS-REN-02, PS-ENS-REN-03, PS-ENS-REN-04, PS-ENS-REN-05, PS-ENS-REN-06, PS-ENS-H2-01, PS-ENS-H2-02, PS-ENS-H2-03, PS-ENS-H2-04, PS-ENS-H2-05, PS-ENS-ES-01, PS-ENS-ES-02]
priority: normal
domain: D03
section: 1
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: ""
tokens: 2659
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션

# SK이노베이션 E&S AI Knowledge Database

## D03. Products and Solutions｜제품·솔루션

**Version 2.0 / 기준일: 2026년 8월 4일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Source namespace: `SRC-ENS-D03-*`
- Product/Solution namespace: `PS-ENS-*`
- O/I Seed namespace: `SEED-ENS-D03-*`
- 작성 원칙: LNG·전력 비즈 대표기업용 심층 DB. D17 과제 생성에 필요한 고객가치·제공방식·운영데이터·Pain Point·외부기술 접점을 제품·서비스·계약·운영 단위까지 분해
- D02 상속 규칙: 2024년 11월 1일 이전 `SK E&S`, 이후 `SK이노베이션 E&S CIC`를 시점별로 구분

---

## 0. 도메인 정의

D03는 SK이노베이션 E&S가 고객에게 판매·공급하거나 자체 밸류체인에서 제공하는 에너지 제품, 인프라 서비스, 디지털 솔루션을 카탈로그 단위로 정리한다. 발전소·터미널·배관 같은 물리자산 자체는 D07에서, 세부 기술은 D04에서 다룬다.

### 0.1 데이터가 답해야 하는 질문

1. 무엇을 누구에게 제공하는가.
2. 거래·공급·운영 방식은 무엇인가.
3. 고객과 E&S가 얻는 측정 가능한 가치는 무엇인가.
4. 현재 상용운영인지, 개발·검토 단계인지.
5. 어떤 운영데이터와 Pain Point가 O/I 과제로 이어지는가.

### 0.2 상태값

| Status | 정의 | D17 사용 규칙 |
|---|---|---|
| `COMMERCIAL_OPERATING` | 생산·공급 또는 상업운전이 공식 확인됨 | 현장 적용·효율화 과제 우선 |
| `ACTIVE_SERVICE` | 고객 대상 계약·서비스가 공식 확인됨 | 고객가치·업무효율 과제 우선 |
| `OPERATING_AND_DEVELOPING` | 운영자산과 개발 파이프라인이 함께 존재 | 운영과 개발 데이터를 분리 |
| `PLANNED` | 추진계획은 있으나 상용운영이 확인되지 않음 | PoC·검증 과제로 제한 |
| `CONSIDERING` | 공식 표현이 검토·고려 단계 | 우선순위를 낮추고 내부수요 확인 |
| `INTERNAL_CAPABILITY` | 외부 판매보다 자체 운영기능 성격이 큼 | 내부 운영혁신 과제로 사용 |

### 0.3 해석 제한

- LNG 생산·액화·선박·터미널 기능을 모두 독립적인 외부 판매상품으로 단정하지 않는다.
- 전력·열·도시가스는 규제·시장정산·공급권역에 따라 판매구조가 다르므로 일반 소매제품처럼 해석하지 않는다.
- 직접 PPA는 재생전력 공급뿐 아니라 계약, 정산, 손해배상, 부족·초과전력 처리 역할을 포함한다. ([SRC-ENS-D03-0005])
- VPP는 공식 페이지가 `검토`로 표현하므로 상용 서비스로 표시하지 않는다.
- DERMS와 재생에너지 O&M은 공식 페이지가 신규사업 `추진계획`으로 설명하므로 계획 상태로 둔다.
- 블루수소·그린수소·저탄소 LNG·CCS는 현재 판매실적이 확인된 제품으로 취급하지 않는다.

---

# 1. Product and Solution Master

## 1.1 전체 카탈로그

| PS ID | 제품·솔루션 | 사업군 | 주요 고객·사용자 | 제공방식 | 상태 | O/I 우선도 |
|---|---|---|---|---|---|---|
| `PS-ENS-LNG-01` | 천연가스·LNG 조달물량 | LNG | 발전·도시가스·산업 수요처 | 장기조달·자체 밸류체인 투입·거래 | `COMMERCIAL_OPERATING` | P0 |
| `PS-ENS-LNG-02` | LNG 액화 연계 | LNG | 자체 LNG 체인·계약 상대방 | 지분·액화설비 사용계약 | `INTERNAL_CAPABILITY` | P1 |
| `PS-ENS-LNG-03` | LNG 해상운송 | LNG | 자체 LNG 체인 | 전용선 4척 운항 | `INTERNAL_CAPABILITY` | P0 |
| `PS-ENS-LNG-04` | LNG 터미널 처리 | LNG | 발전·가스 수요처 | 하역·저장·기화·송출 | `COMMERCIAL_OPERATING` | P0 |
| `PS-ENS-PWR-01` | 천연가스 발전 전력 | Power | 전력시장·전력수요자 | 시장 판매·정산 | `COMMERCIAL_OPERATING` | P0 |
| `PS-ENS-PWR-02` | CHP 전력·지역 열 | Power/CHP | 전력시장·지역 열수요처 | 전력 및 열 공급 | `COMMERCIAL_OPERATING` | P0 |
| `PS-ENS-CG-01` | 도시가스 공급 | City Gas | 가정·상업·산업 고객 | 지역 배관망·규제요금 | `COMMERCIAL_OPERATING` | P0 |
| `PS-ENS-CG-02` | 도시가스 디지털 고객서비스 | City Gas | 도시가스 고객 | 요금·검침·전출입·자동이체 등 비대면 채널 | `ACTIVE_SERVICE` | P0 |
| `PS-ENS-CG-03` | 도시가스 안전관리 서비스 | City Gas | 공급권역 고객·운영조직 | 배관 위험기반 관리·드론점검 | `INTERNAL_CAPABILITY` | P0 |
| `PS-ENS-REN-01` | 태양광 발전 전력 | Renewable | 전력시장·PPA 기업 | 발전·판매·PPA | `OPERATING_AND_DEVELOPING` | P0 |
| `PS-ENS-REN-02` | 육상·해상풍력 전력 | Renewable | 전력시장·PPA 기업 | 발전·판매·PPA | `OPERATING_AND_DEVELOPING` | P0 |
| `PS-ENS-REN-03` | 재생에너지 직접 PPA | RE100 | RE100 추진 기업 | 장기 전력공급계약 | `ACTIVE_SERVICE` | P0 |
| `PS-ENS-REN-04` | PPA 비용분석 | RE100 | PPA 검토 기업 | 온라인 사전분석·상담 | `ACTIVE_SERVICE` | P0 |
| `PS-ENS-REN-05` | PPA 계약·정산 운영 | RE100 | 발전사업자·전기사용자 | 계약·정산·부족/초과전력 처리 | `ACTIVE_SERVICE` | P0 |
| `PS-ENS-REN-06` | 해외 재생에너지·탄소크레딧 연계 | Renewable | 자체 사업·잠재 기업고객 | 해외 발전사업·탄소크레딧 확보 | `OPERATING_AND_DEVELOPING` | P1 |
| `PS-ENS-H2-01` | 부생수소 기반 액화수소 | Hydrogen | 수소충전·모빌리티 수요처 | 생산·탱크로리 공급 | `COMMERCIAL_OPERATING` | P0 |
| `PS-ENS-H2-02` | 액화수소 저장·운송 | Hydrogen | 전국 수소 수요처 | 극저온 저장·탱크로리 물류 | `COMMERCIAL_OPERATING` | P0 |
| `PS-ENS-H2-03` | 액화수소 충전 연계 | Hydrogen | 수소버스·상용차 등 모빌리티 | 충전소 공급망 연계 | `COMMERCIAL_OPERATING` | P0 |
| `PS-ENS-H2-04` | 블루수소 | Hydrogen/CCS | 산업·발전·모빌리티 잠재고객 | LNG 개질+탄소포집 계획 | `CONSIDERING` | P1 |
| `PS-ENS-H2-05` | 그린수소 | Hydrogen/Renewable | 산업·발전·모빌리티 잠재고객 | 재생전력+수전해 계획 | `PLANNED` | P2 |
| `PS-ENS-ES-01` | 수요관리 ESS | Energy Solution | 공장·대형 전기사용자 | 피크저감·전기요금 절감 | `ACTIVE_SERVICE` | P0 |
| `PS-ENS-ES-02` | 재생에너지 연계 ESS | Energy Solution | 재생에너지 발전사업자 | 변동성 완화·예측정확도 개선 | `ACTIVE_SERVICE` | P0 |
| `PS-ENS-ES-03` | 계통안정화 ESS | Energy Solution | 미국 전력망·시장 | KCE 개발·운영·AI 제어 | `OPERATING_AND_DEVELOPING` | P0 |
| `PS-ENS-ES-04` | DERMS | Energy Solution | 배전망·분산자원 운영자 | 분산자원 관제·망 최적화 | `PLANNED` | P1 |
| `PS-ENS-ES-05` | VPP·소규모전력중개 | Energy Solution | 소규모 발전·ESS 자원 | 자원 모집·전력/REC 중개 | `CONSIDERING` | P1 |
| `PS-ENS-ES-06` | 재생에너지 O&M | Energy Solution | 태양광·풍력 자산 보유자 | 발전설비 운영·정비 | `PLANNED` | P1 |
| `PS-ENS-ES-07` | EV 충전 서비스 | Energy Solution | 주차장 이용자·EV 운전자 | 주차시설 중심 충전 | `ACTIVE_SERVICE` | P0 |
| `PS-ENS-CCS-01` | 저탄소 LNG | LNG/CCS | 자체 발전·수소·잠재 구매자 | LNG 생산배출 CCS 연계 | `PLANNED` | P1 |
| `PS-ENS-CCS-02` | 국경간 CCS 밸류체인 | CCS | 자체 LNG 체인·잠재 배출원 | CO2 포집·운송·저장 연계 | `PLANNED` | P1 |

## 1.2 우선순위 해석

- `P0`: 이미 운영 중이며 비용·안전·생산성·고객경험 개선 데이터가 발생하는 영역.
- `P1`: 사업은 존재하거나 개발 중이지만 내부 수요·규제·상용단계를 확인해야 하는 영역.
- `P2`: 장기 계획 성격이 강해 외부사례 탐색보다 기술·경제성 검증이 먼저인 영역.

---
