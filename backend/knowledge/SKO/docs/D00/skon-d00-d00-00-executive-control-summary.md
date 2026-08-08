---
id: skon-d00-d00-00-executive-control-summary
title: Executive Control Summary
summary: SK온 D01~D17 도메인의 사실·분석·과제가 같은 원문과 엔티티를 재사용하고 시점·변경·검증을 잃지 않도록 관리하는 메타데이터 제어층
tags: [d00, governance, table, "xref:d01", "xref:d17", "xref:d16", "xref:d03"]
keywords: [도메인 통합, 엔티티 중복제거, 소스 추적, 라인리지, 마스터 인덱스, URL 정규화, 교차검증, 변경이력, 거버넌스, 제어평면, 메타데이터 제어층, 엔티티 정규화, 출처 추적, O/I 과제, 사실 검증, 교차 참조]
related: []
priority: normal
domain: D00
section: D00-00
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 1041
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

# SK온 D00 — Source, Entity, ID & Change-Log Master

- 문서 버전: **v1.2**
- 기준일: **2026-08-03 (KST)**
- 적용 범위: `D01~D17`
- 작성 방식: **AI Knowledge Base Control Plane** — 도메인별 사실을 다시 서술하지 않고 출처·엔티티·ID·시점·상태·변경·검증을 통합 관리
- 상위 목적: D01~D17의 모든 사실·분석·가설·O/I 과제가 같은 개체와 같은 원문을 재사용하고, 시점·범위·권리·불확실성을 잃지 않도록 한다.

---

## D00-00 Executive Control Summary

### 1. 현재 통합 상태

| 항목 | 2026-08-03 Snapshot | D00 판정 |
|---|---:|---|
| 입력 도메인 | D01~D17, 17개 파일 | 전부 존재 |
| 원천 사실 도메인 | D01~D16, 16개 | D17의 근거 계층 |
| 최종 추천 도메인 | D17, 1개 | 60개 과제·12개 포트폴리오 |
| 전체 문서 규모 | 69,320줄·2,276,543 bytes | D01~D17 Patch 후 Snapshot |
| URL 출현 | 839회 | 도메인 간 재사용 포함 |
| Raw 고유 URL | 551개 | 추적 파라미터·표기 차이 포함 |
| 정규화 고유 URL | 511개 | `utm_source` 제거 기준 |
| D17 원천 O/I Seed | 279개 | D03~D16에서 식별; D05 v2.0의 18개 포함 |
| D17 최종 과제 | 60개 | P0 20·P1 24·P2 16 |
| 공개자료 기반 D05 | v2.0 완료 | 내부·법률 Gate는 별도 |
| 전체 교차검수 | 실행 완료 | 원본 Patch·Crosswalk·Seed Lineage 생성 |
| 최종 공개 Snapshot | `SKON-KB-20260803-v1.0` | D00~D17·Crosswalk·Audit·Manifest 동결 |

> `511개`는 현재 파일에서 정규화한 URL 수이며, 511개의 독립 사실이나 511개의 현재 유효성이 모두 재검증됐다는 의미가 아니다.

### 2. D00이 해결하는 문제

```text
Domain File / Legacy Source ID / Legacy Entity ID
→ Canonical Source / Canonical Entity / Alias
→ Fact or Claim / Scope / Time / Status / Evidence
→ Conflict / Supersession / Validation Queue
→ Domain Record / D17 Seed / Final OI Task
→ Change Event / Audit Trail / Refresh Trigger
```

D00의 핵심 관리단위는 문서가 아니라 **재현 가능한 주장**이다. 하나의 주장은 `누가·무엇을·언제·어느 범위에서·어떤 근거로·어떤 상태로 확인했는가`를 가져야 한다.

### 3. 최상위 원칙

1. 공개되지 않은 내부 수치·계약조항·공정조건·권리를 추정하지 않는다.
2. 같은 URL과 같은 법인·공장·계약·제품은 여러 도메인에서 새 개체로 만들지 않는다.
3. `발표`, `계약`, `투자결정`, `건설`, `가동`, `고객승인`, `출하`, `현금`을 서로 다른 Event로 보존한다.
4. 현재 사실과 역사 사실을 삭제로 구분하지 않고 `valid_from/valid_to/status`로 관리한다.
5. 사실·분석·가설·제안을 같은 확실성으로 검색하지 못하게 한다.
6. 지분율·생산능력·계약량·매출·세액공제·현금을 자동 결합하지 않는다.
7. 원문 Source ID와 D17 과제 ID 사이에 끊기지 않는 Lineage를 유지한다.
8. AI 추천은 사람의 투자·구매·법률·세무·품질·안전·OT 운영 승인을 대체하지 않는다.

---
