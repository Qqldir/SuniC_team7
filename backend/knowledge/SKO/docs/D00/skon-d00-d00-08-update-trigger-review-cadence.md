---
id: skon-d00-d00-08-update-trigger-review-cadence
title: Update Trigger & Review Cadence
summary: "SK온 내 비즈니스 이벤트(실적발표·합병·계약·공장·리콜·특허·공급업체 등) 발생 시 데이터 도메인별 업데이트 주기, SLA, 필수 조치를 정의하는 마스터 테이블."
tags: [d00, governance, table, "xref:d01", "xref:d02", "xref:d07", "xref:d09"]
keywords: [이벤트 기반, SLA, 실적공시, M&A, 공급계약, 리콜, 특허, 공급자, 데이터 동기화, 갱신 주기, 이벤트 트리거, 계약관리, 리콜 관리, 공급업체]
related: []
priority: normal
domain: D00
section: D00-08
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 426
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-08 Update Trigger & Review Cadence

| Trigger | 영향 Domain | SLA/주기 | 필수 조치 |
|---|---|---|---|
| 실적발표·사업보고서·10-Q/10-K | D01·D02·D07·D09~D12 | 발표 후 5영업일 | Scope·기간·Segment·법인 재대조 |
| 합병·분할·JV 설립/해소·자산양도 | D01·D07·D12·D13 | Event 후 3영업일 | Entity·Ownership·Debt·Guarantee Version 생성 |
| 공급계약·MOU·해지·정정공시 | D08·D09·D13 | Event 후 5영업일 | Binding 상태·물량·기간·당사자 갱신 |
| 공장 착공·Ramp·SOP·전환·휴지 | D06·D07·D11·D12 | Event 후 5영업일 | Capacity Event와 고객승인 범위 분리 |
| 법령·가이던스·위임법령 | D08·D11·D14 | 주간/발효 전 30일 | Version·시행일·적용대상·증빙 재판정 |
| 리콜·사고·품질 Signal | D06·D09·D15 | 24시간 Triage | Population·원인·Containment·Source 보존 |
| 특허 상태·Continuation·분할출원 | D05 | 분기·Decision Date 30일 이내 | Official Register Packet 갱신 |
| Provider 인수·파산·제품종료·보안사고 | D16 | 월간/Event | Vendor 상태·Exit·Lock-in 재평가 |
| PoC Gate·Scale·Stop 결정 | D16·D17 | 즉시 | Decision Evidence·KPI·비용·학습 기록 |
| URL 이동·접근불가 | 전 도메인 | 월간 | Archive/대체 원문·접근상태 갱신 |

---
