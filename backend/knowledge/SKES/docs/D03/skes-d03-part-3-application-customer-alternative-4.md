---
id: skes-d03-part-3-application-customer-alternative-4
title: Part 3. Application·Customer·Alternative·Graph·Chunk 확장 — Customer and User Mapping
summary: "SK이노베이션 E&S 전개 고객을 14개 클래스로 분류하고, 실제 파트너·고객을 매핑하며, 9가지 고객 니즈에 대한 데이터·기술 솔루션을 제시한 고객 전략 맵."
tags: [d03, product, table]
keywords: [고객 클래스, LNG, 전력시장, 도시가스, PPA, 재생에너지, 수소, ESS, EV]
related: [CUST-INTERNAL-SUPPLY, CUST-POWER-MARKET, CUST-HEAT, CUST-CITY-RES, CUST-CITY-CI, CUST-RE100, CUST-RE-DEVELOPER, CUST-H2-MOBILITY, CUST-INDUSTRIAL-ESS, CUST-GRID-ESS, CUST-DER, CUST-EV-MF, CUST-EV-FLEET, CUST-CCS, CUST-ENS-PPA-AMORE, CUST-ENS-PPA-BASF, ORG-ENS-KCE, ORG-ENS-EVERCHARGE, ORG-ENS-PASSKEY, ORG-ENS-ENSOLVE, ORG-ENS-IPARKING, ORG-ENS-SKIPC, NEED-ENS-001, NEED-ENS-002]
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 3. Application·Customer·Alternative·Graph·Chunk 확장
tokens: 1333
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 3. Application·Customer·Alternative·Graph·Chunk 확장

## 23. Customer and User Mapping

### 23.1 Customer Class

| CUST Class | 설명 | 대표 PS | 구매·사용 기준 |
|---|---|---|---|
| `CUST-INTERNAL-SUPPLY` | E&S 수급·트레이딩·터미널 | LNG-01~04 | 안정·비용·유연성 |
| `CUST-POWER-MARKET` | 전력시장·계통운영 | PWR-01/02, ES-03 | 가용성·규칙·가격 |
| `CUST-HEAT` | 지역난방 열수요처 | PWR-02 | 신뢰도·온도·요금 |
| `CUST-CITY-RES` | 도시가스 가정고객 | CG-01/02/03 | 안전·편의·정확성 |
| `CUST-CITY-CI` | 상업·산업 도시가스 고객 | CG-01/02/03 | 공급신뢰·비용·현장지원 |
| `CUST-RE100` | RE100 추진 기업 | REN-03~05 | 가격·기간·감축·증빙 |
| `CUST-RE-DEVELOPER` | 재생발전 사업자·자산주 | REN-01/02, ES-06 | 개발·판매·O&M |
| `CUST-H2-MOBILITY` | 버스·상용차·충전사업 | H2-01~03 | 물량·가격·가동률 |
| `CUST-INDUSTRIAL-ESS` | 공장·대형 전기사용자 | ES-01 | 절감·안전·보증 |
| `CUST-GRID-ESS` | 미국 전력시장·ESS 고객 | ES-03 | 수익·가용성·규칙 |
| `CUST-DER` | 분산자원 보유자·운영자 | ES-04/05 | 연동·제어·정산 |
| `CUST-EV-MF` | 공동주택·주차장 | ES-07/08 | 설치밀도·편의·비용 |
| `CUST-EV-FLEET` | fleet·상용차 운영자 | ES-07/08 | 출차보장·총비용 |
| `CUST-CCS` | 배출원·LNG/수소 내부조직 | CCS-01/02 | 탄소강도·책임·검증 |

### 23.2 Disclosed Customer/Partner Records

| Entity ID | 조직 | 관계 | 연결 PS/APP | 공개상태 | Source |
|---|---|---|---|---|---|
| `CUST-ENS-PPA-AMORE` | Amorepacific | 직접 PPA 고객 | REN-03~05 / APP-013~014 | 5MW·20년 공개 | SRC-ENS-D03-0017 |
| `CUST-ENS-PPA-BASF` | BASF Korea | PPA term sheet 상대방 | REN-03~05 / APP-013~014 | 2025~20년·16% 공개 | SRC-ENS-D03-0016 |
| `ORG-ENS-KCE` | Key Capture Energy | 미국 ESS 자회사/플랫폼 | ES-03 / APP-019 | 개발·운영·MarketCapture | SRC-ENS-D03-0011/14/15 |
| `ORG-ENS-EVERCHARGE` | EverCharge | 북미 EV 충전 자회사 | ES-07/08 / APP-023~024 | 턴키·SmartPower | SRC-ENS-D03-0013/20 |
| `ORG-ENS-PASSKEY` | PassKey | 북미 에너지전환 투자/통합 | ES-03/07/08 | KCE·EverCharge 등 포트폴리오 | SRC-ENS-D03-0019 |
| `ORG-ENS-ENSOLVE` | Ensolve | 국내 분산에너지 기반 | ES-04~06 | DERMS·ESS·VPP·O&M 추진 | SRC-ENS-D03-0011 |
| `ORG-ENS-IPARKING` | iPARKING | 국내 주차 네트워크 | ES-07 | 주차장 중심 충전 확대 | SRC-ENS-D03-0011 |
| `ORG-ENS-SKIPC` | SK Incheon Petrochemical | 부생수소 공급원 | H2-01 | 원료연계 공개 | SRC-ENS-D03-0012 |

### 23.3 Customer Need Map

| Need ID | 고객 질문 | 필요한 답 | 연결 데이터 | O/I 적용 |
|---|---|---|---|---|
| `NEED-ENS-001` | 우리 LNG 수요를 더 낮은 위험으로 충족할 수 있는가 | 조달·재고·가격 시나리오 | 계약·수요·선박·터미널 | 최적화·설명형 의사결정 |
| `NEED-ENS-002` | 전력·열을 안정적으로 공급받는가 | 고장·수요·효율 전망 | 설비·시장·기상 | 예지보전·동시최적화 |
| `NEED-ENS-003` | 가스요금과 검침이 정확한가 | 검침 근거·이상 원인 | 계량·사진·청구 | OCR·이상탐지 |
| `NEED-ENS-004` | 누출·배관 위험이 통제되는가 | 위험구간·조치이력 | GIS·점검·굴착 | 위험예측·동선 |
| `NEED-ENS-005` | PPA가 비용·감축목표에 맞는가 | 시나리오·계약·증빙 | 부하·자산·가격 | 자산매칭·정산자동화 |
| `NEED-ENS-006` | 액화수소가 제때 공급되는가 | 재고·배송·충전 가용성 | 생산·물류·충전소 | 수요·배차·예지보전 |
| `NEED-ENS-007` | ESS가 열화비용 이후에도 가치가 있는가 | 순수익·보증·안전 | SOC/SOH·시장·요금 | 제어·입찰·진단 |
| `NEED-ENS-008` | 제한전력에서 더 많은 EV를 충전할 수 있는가 | 차량·부하·ESS 계획 | 세션·건물·배터리 | 동적부하관리 |
| `NEED-ENS-009` | 저탄소 주장을 감사할 수 있는가 | 탄소수지·계보·검증 | meter·계약·저장 | MRV 데이터 플랫폼 |

---
