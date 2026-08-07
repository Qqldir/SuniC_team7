---
id: skes-d09-21-ai-retrieval-chunks
title: AI Retrieval Chunks
summary: "고객 정의부터 PPA 가치평가, 도시가스·수소 수요 신뢰도, 계약 이행 추적까지 E&S 비즈니스 핵심 14개 관리 원칙을 정리한 참고자료다."
tags: [d09, customer]
keywords: [고객 구분, PPA 가치평가, 도시가스 포트폴리오, 수소 수요 신뢰도, CHP 최적화, 계약-KPI 연계, 데이터 권리, 고객 여정, LNG-to-power, 시장 정산]
related: [CHUNK-ENS-D09-0001, CHUNK-ENS-D09-0002, CHUNK-ENS-D09-0003, CHUNK-ENS-D09-0004, CHUNK-ENS-D09-0005, CHUNK-ENS-D09-0006, CHUNK-ENS-D09-0007, CHUNK-ENS-D09-0008, CHUNK-ENS-D09-0009, CHUNK-ENS-D09-0010, CHUNK-ENS-D09-0011, CHUNK-ENS-D09-0012, CHUNK-ENS-D09-0013, CHUNK-ENS-D09-0014]
priority: normal
domain: D09
section: 21
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 1208
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 21. AI Retrieval Chunks

## `CHUNK-ENS-D09-0001` — Customer Is Not Every Counterparty

KPX·ERCOT·NYISO는 시장운영기관, 지자체는 정책·인허가·수요촉진 주체, JV사는 공동사업 파트너다. 이들을 최종 구매고객과 합치면 고객집중도·매출·수주가 왜곡된다.

## `CHUNK-ENS-D09-0002` — Demand States Must Stay Separate

계약상 상한, forecast, nomination, firm order, dispatch, 계량, 정산은 서로 다른 상태다. 같은 값으로 덮어쓰지 않고 version lineage를 보존한다.

## `CHUNK-ENS-D09-0003` — Public PPA Customers

공개자료에서 아모레퍼시픽, SK Specialty, BASF, LG이노텍, AWS, Iljin Global 등과의 PPA 관계가 확인된다. 아모레퍼시픽은 5MW·20년, SK Specialty 관련 계약은 50MW·2024~2044가 공개됐으며 나머지 상업조건은 내부확인이 필요하다.

## `CHUNK-ENS-D09-0004` — PPA Value Chain

PPA 가치는 계약 MW가 아니라 시간대별 고객부하·발전량·curtailment·망비용·불균형·REC 증빙·신용을 함께 보아야 한다.

## `CHUNK-ENS-D09-0005` — City-Gas Scale

E&S 도시가스 포트폴리오는 7개사·8개 권역, 약 510만 가구, 2023년 약 54억㎥, 22.6% 시장점유율로 공개된다. 개별사 수치의 기준연도는 달라 단순 합산 검증이 필요하다.

## `CHUNK-ENS-D09-0006` — City-Gas Journey

공급조회, 신청, 전입, 전출, 검침, 청구, 납부, 상담, 안전신고, 현장출동의 event log를 연결하면 고객노력·방문성공·청구오류·안전응답 개선 과제를 만들 수 있다.

## `CHUNK-ENS-D09-0007` — CHP Constraint

CHP는 전력가격만 보고 최적화할 수 없다. 열수요·공급온도·네트워크·축열·고객 SLA가 hard constraint다.

## `CHUNK-ENS-D09-0008` — KCE Market Relationship

KCE는 ERCOT·NYISO 시장에서 bid·award·dispatch·settlement 관계를 가진다. ISO/RTO를 단일 고객으로 매출 배분하지 않으며 utility NWA 계약은 별도 관계로 둔다.

## `CHUNK-ENS-D09-0009` — EverCharge Customer Value

EverCharge는 공동주택·직장·fleet 고객에게 동적 부하관리로 기존 전기용량 내 충전 확대, 인프라 CAPEX 회피, session 운영을 제공한다. 설치대수·EV-ready·활성사용자·동시충전은 분리한다.

## `CHUNK-ENS-D09-0010` — Hydrogen Demand Discipline

수소버스 목표나 MOU는 확정수요가 아니다. 차량 발주·등록, 충전소 준공, 연료계약, 실제 dispensed kg 순으로 수요 신뢰도를 높인다.

## `CHUNK-ENS-D09-0011` — Icheon Hydrogen Case

이천 액화수소충전소는 SK hynix 통근버스에 공급하며 하루 최대 120대 충전 가능으로 공개됐다. 이 값은 실제 하루 수요가 아니라 설계 가능량이다.

## `CHUNK-ENS-D09-0012` — Contract-to-KPI

계약조항을 운영 KPI와 연결하지 않으면 공급은 했지만 SLA·증빙·정산·변경통지 의무를 놓칠 수 있다. Clause-to-KPI monitor는 추천과 경보만 제공하고 법적 판단은 사람이 승인한다.

## `CHUNK-ENS-D09-0013` — Data Rights First

고객 부하·계량·결제·차량·시장입찰 데이터는 가치가 높지만 기밀·개인정보·시장규칙 제약이 있다. PoC 전에 목적·필드·보유기간·접근권·파생데이터 권리를 확인한다.

## `CHUNK-ENS-D09-0014` — P0 Portfolio

D09 우선 과제는 Golden Thread, LNG-to-power forecast, CHP co-optimization, 도시가스 ID matching·긴급 triage, PPA matching·증빙, KCE 입찰·정산, fleet SOC, 수소 stage-gate·control tower, data-right registry다.

---
