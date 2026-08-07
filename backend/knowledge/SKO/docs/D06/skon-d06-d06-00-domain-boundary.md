---
id: skon-d06-d06-00-domain-boundary
title: Domain Boundary
summary: "배터리 제조공정의 순서, 변수, 품질특성, 불량역추적, 병목 분석 등을 다루는 SK온 D06 도메인의 경계와 핵심 질문을 정의한 문서."
tags: [d06, process, core-candidate, schema, "xref:d00", "xref:d05", "xref:d03", "xref:d04"]
keywords: [제조공정, 배터리 셀, 공정변수, 품질특성, 수율, 불량, 병목, 가동률, 역추적, 설비, 배터리 제조공정, 공정순서, 불량역추적, pain point]
related: [ORG-SKON-000001, CO-SKON, COMP-SKON-001]
priority: critical
domain: D06
section: D06-00.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 507
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# SK온 D06 Manufacturing Process & Operations

## Part 1. End-to-End Process·Electrode Manufacturing·Process Data Model

**문서 버전:** D06 v1.6.1 — 누적 본문 v1.0~v1.6, D00 통합검수 Patch
**기준일:** 2026-08-02
**이전 완료 지점:** `D05 R&D, Patents & Intellectual Property v2.0`
**Canonical company entity:** `ORG-SKON-000001` (`CO-SKON`, `COMP-SKON-001`은 Legacy Alias)

---

# D06-00. Domain Boundary

```yaml
domain:
  domain_id: D06
  canonical_name: Manufacturing Process and Operations
  company_id: CO-SKON
  company_name: SK On

primary_questions:
  - 배터리 셀·모듈·팩은 어떤 공정순서로 제조되는가?
  - 각 공정의 투입물·산출물·설비·공정변수는 무엇인가?
  - 공정별 핵심 품질특성과 불량유형은 무엇인가?
  - 불량을 소재 Lot·설비·Recipe·작업조건까지 역추적할 수 있는가?
  - 수율·스크랩·에너지·가동률을 저하시키는 병목은 무엇인가?
  - 외부기술로 해결할 수 있는 제조 Pain Point는 무엇인가?

relationship_to_previous_domains:
  D03:
    role: 제품·폼팩터·솔루션 정의

  D04:
    role: 제조기술·공정기술 엔티티 정의

  D05:
    role: 제조 관련 특허·연구·IP 정의

  D06:
    role: 실제 공정흐름·공정변수·품질·운영 Pain Point 구조화

deferred_domains:
  D07: 공장·생산능력·설비배치
  D08: 원재료·공급망
  D11: 제조원가
  D12: 투자·CAPEX
  D14: 환경·안전·규제
  D15: 품질·보증·필드불량
  D17: 최종 OI 과제추천
```

---
