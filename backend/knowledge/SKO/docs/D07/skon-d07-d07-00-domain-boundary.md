---
id: skon-d07-d07-00-domain-boundary
title: Domain Boundary
summary: "SK온 배터리 공장의 위치, 법인 형태, 생산능력, 운영 상태를 정의하고 관련 도메인과의 관계를 명시한 마스터 문서"
tags: [d07, footprint, core-candidate, schema, "xref:d00", "xref:d06", "xref:d03", "xref:d04"]
keywords: [생산거점, 설계 생산능력, 공시 생산능력, 가동 상태, 법인 형태, 합작기업, GWh, 제조시설, 캐파, ESS 전환, 공장, 생산능력, Manufacturing Footprint, 법인 구조, 양산 상태, ESS, Capacity]
related: [ORG-SKON-000001, CO-SKON, COMP-SKON-001]
priority: critical
domain: D07
section: D07-00.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 670
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# SK온 D07 Manufacturing Footprint, Plants & Capacity

## Part 1. Global Plant Master·Ownership·Capacity Baseline·2026 Footprint Restructuring

**문서 버전:** D07 v1.3.1 — 누적 본문 v1.0~v1.3, D00 통합검수 Patch
**기준일:** 2026-08-02
**이전 완료 지점:** `D06 Manufacturing Process & Operations v1.6`
**Canonical company entity:** `ORG-SKON-000001` (`CO-SKON`, `COMP-SKON-001`은 Legacy Alias)

> 이번 D07에서는 **설계 생산능력, 공시상 환산 생산능력, JV 총생산능력, 실제 생산량과 목표 생산능력**을 분리한다. 서로 다른 기준의 GWh를 단순 합산하지 않는다.

---

# D07-00. Domain Boundary

```yaml
domain:
  domain_id: D07
  canonical_name: Manufacturing Footprint, Plants and Capacity
  company_id: CO-SKON
  company_name: SK On

primary_questions:
  - SK온의 배터리 생산거점은 어디에 있는가?
  - 각 거점은 SK온 단독법인·종속기업·합작기업 중 어디에 해당하는가?
  - 공장별 설계 생산능력과 현재 공시상 생산능력은 얼마인가?
  - 공장이 양산·부분가동·Ramp-Up·건설·양도 중 어느 단계인가?
  - 어느 생산능력이 SK온 연결 생산능력에 포함되는가?
  - 고객·제품·화학계·ESS 전환과 공장 간 관계는 무엇인가?
  - 생산거점 재편이 공급 안정성·가동률·고정비에 어떤 영향을 주는가?

relationship_to_previous_domains:
  D03:
    role: 제품·Cell·Module·Pack·ESS 정의

  D04:
    role: 공장에 적용될 수 있는 기술 정의

  D05:
    role: 공장·생산 관련 R&D와 특허 정의

  D06:
    role: 공장 내부 제조공정·설비·운영모델 정의

  D07:
    role: 공장의 위치·법인·Capacity·가동상태·고객 배치 정의

deferred_domains:
  D08: 원재료와 공급망
  D09: 고객·수주·OEM 관계
  D11: 공장별 원가와 고정비
  D12: CAPEX·투자·보조금
  D14: 환경·안전·인허가
  D15: 공장별 품질·보증
  D17: 생산거점 기반 OI 과제 추천
```

---
