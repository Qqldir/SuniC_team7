---
id: skes-d07-16-ai-retrieval-chunks
title: AI Retrieval Chunks
summary: "SK이노베이션 E&S의 LNG 터미널, 발전소, 도시가스, 액화수소, 재생에너지 자산에 대해 지분·용량·권리별로 어떻게 분류하고 합산하는지 정의하는 데이터 가이드."
tags: [d07, footprint]
keywords: [LNG 터미널, 발전소, 도시가스, 재생에너지, 액화수소, 지분구조, TUA, 용량 검증, 자산 분류, 권리 기반 분석]
related: []
priority: normal
domain: D07
section: 16
source: SK이노베이션E&S_D07_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1175
updated: 2026-08-06
---

> SK이노베이션 E&S · D07 터미널·발전소·배관 등 자산·용량

# 16. AI Retrieval Chunks

## CHUNK-ENS-D07-0001｜Boryeong ownership correction

보령 LNG터미널은 gross 7Mt/y, 7개 200,000kl LNG 탱크, 1,400t/h 송출능력을 가진 물리자산이다. 그러나 2025~2026 지분매각 이후 E&S는 equity owner로 분류하지 않는다. E&S 계열의 3.5Mt/y 사용권은 별도 TUA 레코드로 유지한다. 물리능력과 사용권은 합산하지 않는다.

## CHUNK-ENS-D07-0002｜Barossa operating transition

Barossa는 2026년 1월 첫 LNG 생산을 시작했고 첫 화물이 2026년 2월 보령에 도착했다. E&S 지분은 37.5%, 장기 도입 설명물량은 약 1.3Mt/y다. 이 값은 Barossa gross field capacity가 아니라 E&S offtake/equity-linked volume이다.

## CHUNK-ENS-D07-0003｜Freeport capacity meaning

Freeport 2.2Mt/y는 액화설비 사용계약이다. 공장 지분, 실제 생산량, 실제 한국 도입량으로 저장하지 않는다. O/I 분석은 계약 가용성, train outage, cargo window와 포트폴리오 balancing을 연결한다.

## CHUNK-ENS-D07-0004｜Power fleet

주요 공개 발전능력은 Gwangyang 1,126MW, Paju 1,800MW, Yeoju 1,000MW다. Hanam은 399MW와 263Gcal/h, Wirye는 450MW와 238Gcal/h로 전력과 열을 함께 생산한다. CHP는 전력효율만 최적화하면 안 된다.

## CHUNK-ENS-D07-0005｜City gas footprint

E&S 도시가스 포트폴리오는 7개 법인·8개 운영권역이다. 공개 snapshot은 2023년 5.4bn m3, 22.6% 점유율, 약 5.1m households다. 배관길이·재질·연령·정압기·계량기 수는 내부확인 항목이다.

## CHUNK-ENS-D07-0006｜Renewable status

재생에너지 3.5GW는 operating and developing의 혼합값이고 약 5GW는 pipeline이다. Jeonnam Offshore Wind 1의 96MW는 2025년 상업운전이 확인되며, 2·3단계 각 399MW는 2031 목표 개발자산이다.

## CHUNK-ENS-D07-0007｜KCE capacity

KCE 최신 공개 portfolio는 623MW operating과 8,000MW development다. NY6 20MW/45.6MWh 같은 개별 프로젝트는 623MW portfolio의 구성요소이므로 다시 더하지 않는다. MW와 MWh도 별도 차원이다.

## CHUNK-ENS-D07-0008｜EverCharge case counts

EverCharge 공개사례는 Oracle Park 50기 설치와 총 150기 계획, Sharon Park 64기, Legacy 80기와 67 EV-ready circuits다. ready circuit는 설치 충전기로 계산하지 않으며 이 사례 합계를 전사 설치대수로 확대하지 않는다.

## CHUNK-ENS-D07-0009｜Incheon LH2

인천 액화수소플랜트는 2024년 완공·운영을 시작했으며 명목 연 30,000t, 30t/day train 3개, 20t 저장설비 6개다. 90t/day×365와 30kt/y headline 차이는 추정 보정하지 않고 내부 가동일·availability로 검증한다.

## CHUNK-ENS-D07-0010｜Quynh Lap

Quynh Lap은 베트남 1,500MW LNG CCGT와 250,000m3 terminal, dedicated port를 포함하는 개발사업이다. 2027 construction, 2030 COD 목표이며 운영자산이 아니다. EPC 단계에서 asset hierarchy와 historian handover 요건을 계약에 넣는 것이 핵심 O/I 기회다.

## CHUNK-ENS-D07-0011｜Rights-aware analytics

JV 지분, TUA, tolling, O&M, site-host contract는 데이터 접근권을 자동 보장하지 않는다. 모든 O/I PoC는 asset ownership과 별도로 raw data, derived data, model deployment, cross-border transfer 권리를 확인해야 한다.

## CHUNK-ENS-D07-0012｜Capacity validation

NAMEPLATE_GROSS, EQUITY_ATTRIBUTABLE, CONTRACTED_RIGHT, ACTUAL_OUTPUT, OPERATING_PORTFOLIO, OPERATING_AND_DEVELOPING, DEVELOPMENT_PIPELINE, OAM_MANAGED를 분리한다. 단위가 같아도 capacity_type이 다르면 합산하지 않는다.

---
