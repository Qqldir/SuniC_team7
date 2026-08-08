---
id: skes-d10-0-domain-boundary
title: Domain Boundary
summary: "에너지·충전 8개 사업(LNG·전력·가스·재생에너지·BESS·EV충전·수소·CCS)의 시장 단위, 가격 메커니즘, 경쟁 분석 방식을 규정하는 도메인 경계 정의"
tags: [d10, market, core-candidate, table, "xref:d03", "xref:d06", "xref:d07", "xref:d08"]
keywords: [LNG, 전력시장, 도시가스, 재생에너지, BESS, EV충전, 수소, CCS, 가격메커니즘, 경쟁분석]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001]
priority: critical
domain: D10
section: 0
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 1312
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# SK이노베이션 E&S AI Knowledge Database

## D10. Market, Competition & Industry Dynamics｜시장·경쟁·산업동향

**Version 1.0 / 기준일: 2026년 8월 5일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Market namespace: `MKT-ENS-D10-*`
- Segment namespace: `SEG-ENS-D10-*`
- Competitor namespace: `COM-ENS-D10-*`
- Signal namespace: `SIG-ENS-D10-*`
- Scenario namespace: `SCN-ENS-D10-*`
- Risk namespace: `RSK-ENS-D10-*`
- Pain Point namespace: `PAIN-ENS-D10-*`
- O/I Seed namespace: `SEED-ENS-D10-*`
- Source namespace: `SRC-ENS-D10-*`
- Inherited joins: D03 제품·솔루션 29개, D06 운영 프로세스 45개, D07 자산 78개, D08 공급계약·권리 12개, D09 공개 고객·관계 34개

---

# 0. Domain Boundary

## 0.1 목적

D10은 SK이노베이션 E&S가 참여하는 LNG·전력·도시가스·재생에너지·ESS·EV 충전·수소·CCS 시장을 단순 통계집이 아니라 `시장–가격–정책–경쟁사–대체재–E&S 노출–의사결정–O/I 과제`로 연결하는 데이터베이스다.

D10이 답해야 하는 질문은 다음과 같다.

1. 각 사업의 실제 시장 단위와 가격 형성 메커니즘은 무엇인가.
2. 수요·설비·거래·파이프라인·정책목표를 어떻게 구분할 것인가.
3. LNG 가격·환율·SMP·REC·용량·보조서비스·충전 이용률·수소 판매량·CO2 저장료가 E&S 가치사슬에 어떤 경로로 전파되는가.
4. KOGAS·POSCO International·GS 계열 같은 통합에너지사와 Tesla·Wärtsilä·ChargePoint 같은 솔루션 경쟁사를 동일 순위표에 넣지 않고 어떻게 비교할 것인가.
5. 도시가스 전기화, LNG와 석탄의 연료전환, PPA와 REC의 대체, BESS와 가스발전의 유연성 경쟁은 어디에서 발생하는가.
6. KCE의 ERCOT·NYISO 노출과 EverCharge의 공동주택·직장·fleet 사업에서 성장률보다 더 중요한 병목은 무엇인가.
7. 수소·CCS의 발표 파이프라인을 확정수요로 과대평가하지 않으려면 어떤 stage gate가 필요한가.
8. D17이 추천할 과제를 시장 변화와 E&S 내부 자산·데이터에 어떻게 연결할 것인가.

## 0.2 포함 범위

| 시장군 | 포함 항목 | 핵심 측정 단위 | E&S 연결 |
|---|---|---|---|
| LNG | 생산·액화·장기도입·spot·선박·터미널·발전연료 | bcm, mtpa, cargo, MMBtu | Barossa·Freeport·Boryeong·발전 |
| 한국 전력 | 수요·발전믹스·SMP·정산·용량·계통 | MW, MWh, KRW/kWh | 발전·CHP·PPA |
| 도시가스 | 가정·상업·산업 수요·요금·전기화 | ㎥, 고객전, degree day | 7개 도시가스사 |
| 재생에너지 | 태양광·풍력·해상풍력·계통접속·출력제어 | MW, MWh, capacity factor | 3.5GW portfolio·5GW pipeline |
| PPA·RE100 | 직접 PPA·VPPA·REC·green premium·24/7 CFE | MW, MWh, REC, KRW/kWh | 공개 고객 6개 관계 |
| BESS | merchant·utility·capacity·ancillary·NWA | MW, MWh, spread, availability | KCE 623MW 운영·8GW 개발 |
| EV 충전 | 공동주택·직장·fleet·공공충전·SaaS | port, session, kWh, uptime | EverCharge |
| 수소 | 액화수소 생산·물류·충전·버스·상용차 | tpa, kg/day, vehicle, station | 인천 3만t/년 명목능력 |
| CCS | 포집·수송·저장·MRV·저장서비스 | tCO2, Mtpa, storage right | Bayu-Undan 개발 concept |

## 0.3 제외 및 후속 이관

| 후속 문서 | 이관 내용 | D10 연결키 |
|---|---|---|
| D11 | 사업별 원가·마진·현금흐름·민감도 | `market_id`, `price_driver_id` |
| D12 | CAPEX·투자·자금조달·NPV | `scenario_id`, `asset_id` |
| D13 | PPA·TUA·JV·LTSA·시장계약 조항 | `contract_id`, `competitor_id` |
| D14 | 전력시장·가스요금·수소·CCS 규제 | `policy_signal_id` |
| D15 | 전사 리스크·KRI·복원력 | `risk_id`, `scenario_id` |
| D16 | 외부 솔루션·startup·vendor | `solution_need_id` |
| D17 | 우선순위·PoC·AI 과제 추천 | `seed_id`, `benefit_case_id` |

---
