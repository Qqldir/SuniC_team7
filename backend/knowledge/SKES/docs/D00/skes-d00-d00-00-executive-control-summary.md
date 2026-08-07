---
id: skes-d00-d00-00-executive-control-summary
title: Executive Control Summary
summary: "SK이노베이션 E&S 지식베이스의 D01~D17 통합 제어 현황과 데이터 품질 검증 결과를 보여주는 스냅샷 요약표, 출처·엔티티·ID·변경이력 정규화 기준 및 8가지 관리 원칙 수록"
tags: [d00, governance, table, "xref:d01", "xref:d17"]
keywords: [메타데이터 관리, URL 정규화, Lineage, Source Crosswalk, 교차검수, Snapshot, 도메인 통합, 엔티티 정규화, 데이터 통합 관리, 출처 정규화, 엔티티 중복제거, Lineage 추적, 변경이력 감사, 사실 검증, 스냅샷 제어]
related: []
priority: normal
domain: D00
section: D00-00
source: SK이노베이션E&S_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master"
tokens: 775
updated: 2026-08-06
---

> SK이노베이션 E&S · D00 소스·엔티티·ID·변경이력 마스터 · SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master

# SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master

- 문서 버전: **v1.0**
- 기준일: **2026-08-06 (KST)**
- 적용 범위: `D01~D17`
- Snapshot ID: `SKI-ENS-KB-20260806-D00-v1.0`
- 목적: D01~D17의 출처·엔티티·ID·시점·상태·변경·검증·D17 Lineage를 통합 관리하는 Knowledge Base Control Plane

---

## D00-00 Executive Control Summary

| 항목 | Snapshot | 판정 |
|---|---:|---|
| 입력 도메인 | D01~D17, 17개 파일 | 전부 존재 |
| 전체 규모 | 22,961줄·1,321,418 bytes | 기준본 Snapshot |
| URL 출현 | 523회 | 도메인 간 재사용 포함 |
| 정규화 고유 URL | 300개 | 추적 파라미터 제거 기준 |
| D17 최종 과제 | 60개 | P0 20·P1 24·P2 16 |
| 코드블록 오류 | 0개 | 자동검사 통과 |
| Source Crosswalk | 300개 Source | 별도 CSV 생성 |
| 교차검수 원장 | 1개 JSON | SHA-256 포함 |

> 300개는 현재 D01~D17에서 기계적으로 회수·정규화한 URL 수다. 모든 URL이 2026-08-06에 다시 열렸거나 현재 유효하다는 뜻은 아니다. 재검증 여부는 출처별 상태로 별도 관리한다.

### D00이 해결하는 문제

```text
Raw URL / Legacy Source ID / Entity Alias
→ Canonical Source / Canonical Entity / Time Slice
→ Claim / Scope / Fact Status / Evidence
→ Conflict / Supersession / Validation Queue
→ Domain Record / OI Seed / D17 Final Task
→ Change Event / Refresh Trigger / Audit Trail
```

### 최상위 원칙

1. 공개되지 않은 내부 수치·계약조항·공정조건·사고·권리를 추정하지 않는다.
2. 합병 전 `SK E&S`와 2024-11-01 이후 `SK이노베이션 E&S`를 동일 시점 기업으로 섞지 않는다.
3. 발표·MOU·계약·FID·착공·준공·가동·상업운전·현금효과를 서로 다른 Event로 보존한다.
4. 사실·기업 주장·외부 신호·분석·가설·제안을 같은 확실성으로 검색하지 못하게 한다.
5. 같은 URL·법인·자산·계약·프로젝트를 도메인마다 새 개체로 중복 생성하지 않는다.
6. 외부사례의 ROI·효율·절감률을 E&S 기대효과로 복사하지 않는다.
7. D17 과제는 D01~D16의 Pain·Risk·Evidence·Solution과 추적 가능한 Lineage를 가져야 한다.
8. 안전·법률·세무·계약·Cyber·Data Right·경제성 Gate가 막히면 점수와 무관하게 `HOLD`한다.

---
