---
id: skes-d00-d00-08-refresh-validation-queue
title: Refresh & Validation Queue
summary: "SK이노베이션 E&S 마스터 데이터의 대상별 갱신 주기와 즉시 갱신 트리거, 우선 검증 항목을 정의하는 표."
tags: [d00, governance, table, "xref:d17", "xref:d01"]
keywords: [갱신주기, 즉시갱신, 데이터마스터, Canonical Source, Entity Crosswalk, LNG·전력·REC, 법령·세액공제, 우선검증큐, 마스터데이터, 법령제도, 에너지시장, 프로젝트자산, 계약관리, 데이터검증]
related: []
priority: normal
domain: D00
section: D00-08
source: SK이노베이션E&S_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master"
tokens: 385
updated: 2026-08-06
---

> SK이노베이션 E&S · D00 소스·엔티티·ID·변경이력 마스터 · SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master

## D00-08 Refresh & Validation Queue

| 대상 | 기본 갱신주기 | 즉시 갱신 Trigger |
|---|---|---|
| 법령·정책·세액공제 | 월 1회 | 개정·시행·가이던스·판결 |
| LNG·전력·REC·탄소시장 | 주 1회 또는 Event | 가격충격·시장규칙 변경 |
| 공시·재무·CAPEX | 분기 | 실적·투자결정·손상·자금조달 |
| 프로젝트·자산 | 월 1회 | FID·착공·준공·상업운전·지연·취소 |
| 계약·JV | Event | 체결·변경·종료·분쟁·Exit |
| 위험·사이버 | 주 1회 | 사고·취약점·규제 경보 |
| 외부기술·벤더 | 분기 | 제품종료·인수·신규 실증 |
| D17 과제 | Gate 시점 | Baseline·PoC 결과·Hard Gate 변경 |

### 우선 검증 큐

1. 300개 Canonical URL의 실제 접근성·발행일·유효성 재검증
2. D01~D17 내부 로컬 Source ID와 Canonical Source ID 매핑
3. 법인·JV·SPV·자산 Canonical Entity Crosswalk
4. D17 60개 과제의 Seed·Pain·Risk·Evidence 직접 Lineage 표
5. 동적 법령·시장제도·세액공제의 effective date 재검증
6. 비공개 계약·운영·원가·사고·가동률을 `INTERNAL_REQUIRED`로 확정 분리

---
