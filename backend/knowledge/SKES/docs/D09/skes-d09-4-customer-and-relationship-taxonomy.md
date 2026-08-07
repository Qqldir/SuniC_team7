---
id: skes-d09-4-customer-and-relationship-taxonomy
title: Customer and Relationship Taxonomy
summary: "도시가스, 전력 거래에서 법인고객, 가정용, 산업용 등 거래처 12가지를 분류하고 각각의 경제역할, 계약유형, 핵심 데이터항목, 사업위험을 정의하는 분류체계."
tags: [d09, customer, core-candidate, table]
keywords: [계약분류, PPA, offtaker, 도시가스, 에너지거래, 정산, 충전, BESS, 거래처, 위험요소]
related: []
priority: critical
domain: D09
section: 4
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 722
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 4. Customer and Relationship Taxonomy

| Customer class | 경제적 역할 | 대표 계약 | 핵심 데이터 | 주요 위험 |
|---|---|---|---|---|
| Corporate offtaker | 장기 전력 구매 | 직접 PPA | 부하·발전·정산·인증 | 부하변동·신용·추가성 |
| Household | 규제 도시가스 소비 | 공급계약 | 계량·요금·민원·안전 | 체납·누출·민감정보 |
| Commercial | 상업용 가스·충전 | 요금·서비스 | 시간대 부하·SLA | 계절성·churn |
| Industrial | 대량 가스·전력·열 | 개별 공급 | 공정계획·최대수요 | 집중도·중단손실 |
| Market operator | 시장접수·dispatch·정산 | 참여규칙 | bid·award·telemetry | 규칙변경·정산오류 |
| Utility | NWA·계통·망서비스 | 서비스계약 | feeder·제약·가용성 | 성능벌점 |
| Site host | 충전·BESS 설치공간 | site agreement | 전기용량·접근·사용자 | 입주자 동의·공사 |
| Fleet operator | 반복 충전 수요 | charging service | 운행계획·SOC·회차 | 출차 실패 |
| Municipality | 인허가·부지·보조·수요촉진 | MOU·협약 | 차량계획·노선·보조 | 정책변경 |
| Internal affiliate | 그룹 내 에너지수요 | 내부 PPA·서비스 | 그룹 부하·이전가격 | 내부거래 경계 |
| JV partner | 공동 자산·사업 의사결정 | SHA/JV | 권한·데이터·배당 | 이해상충 |
| CO2 emitter | 잠재 포집·저장 수요 | future TSA | 배출량·순도·압력 | 책임·MRV |

## 4.1 Relationship Type Control

| 관계 | 고객 매출로 집계 | pipeline로 집계 | 예시 |
|---|---:|---:|---|
| `DISCLOSED_CONTRACT` | 조건부 가능 | 가능 | 아모레퍼시픽 PPA |
| `OPERATING_CASE` | 내부 매출 검증 후 | 가능 | Avis IAH 충전 |
| `MARKET_PARTICIPATION` | 시장정산 매출로만 | 불필요 | KCE–ERCOT |
| `MOU_OR_PLAN` | 금지 | 별도 비구속 pipeline | 천안 수소버스 협약 |
| `PARTNERSHIP` | 금지 | 기회관계로만 | Hyundai 협력 |
| `REGULATED_SUPPLY` | 계량·청구 실적으로 | 고객전 기반 | 도시가스 |
| `INTERNAL_TRANSFER` | 연결재무 제거여부 확인 | 별도 | 그룹 RE100 수요 |

---
