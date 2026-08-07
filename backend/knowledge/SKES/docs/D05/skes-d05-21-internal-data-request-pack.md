---
id: skes-d05-21-internal-data-request-pack
title: Internal Data Request Pack
summary: "SK이노베이션 D05 부서의 내부 자료 10가지 유형별 요청 ID, 사용 목적, 필수 필드, 보안 등급을 정의한 표"
tags: [d05, rnd, table]
keywords: [특허, R&D과제, 라이선스, 지식재산, FTO, 공동개발계약, 데이터카탈로그, 발명기록, 보안등급]
related: [REQ-D05-001, REQ-D05-002, REQ-D05-003, REQ-D05-004, REQ-D05-005, REQ-D05-006, REQ-D05-007, REQ-D05-008, REQ-D05-009, REQ-D05-010]
priority: normal
domain: D05
section: 21
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 381
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 21. Internal Data Request Pack

| Request ID | 내부자료 | 목적 | 최소필드 | 보안 |
|---|---|---|---|---|
| `REQ-D05-001` | 발명·특허 대장 | 포트폴리오 완결 | family, owner, status, cost | Highly confidential |
| `REQ-D05-002` | R&D 과제대장 | 프로그램 검증 | owner, budget, stage, output | Confidential |
| `REQ-D05-003` | 공동개발 계약 | 권리경계 | background, foreground, license | Legal privileged |
| `REQ-D05-004` | 자회사 내부 라이선스 | 그룹 재사용 | entity, field, region, fee | Confidential |
| `REQ-D05-005` | 소프트웨어·모델 대장 | KCE·EverCharge·E&S | repo, owner, license, version | Restricted |
| `REQ-D05-006` | 데이터 카탈로그 | PoC 가능성 | owner, purpose, quality, rights | Restricted |
| `REQ-D05-007` | 특허–제품 실시표 | 구현검증 | claim element, system evidence | Legal privileged |
| `REQ-D05-008` | 연구시설·파일럿 목록 | 실증역량 | asset, location, owner, capacity | Confidential |
| `REQ-D05-009` | 발명자 기여기록 | 소유권·보상 | contribution, date, employer | Personal/confidential |
| `REQ-D05-010` | FTO·법률의견 | 상용 Gate | jurisdiction, claims, conclusion | Legal privileged |

---
