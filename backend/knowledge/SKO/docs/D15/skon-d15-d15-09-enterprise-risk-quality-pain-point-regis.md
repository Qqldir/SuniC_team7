---
id: skon-d15-d15-09-enterprise-risk-quality-pain-point-regis
title: Enterprise Risk & Quality Pain-Point Register
summary: SK온의 전사 리스크·품질 이슈를 우선순위별로 정리하고 이들의 복합 확대 경로를 분석하는 문서
tags: [d15, risk, table, "xref:d10", "xref:d12"]
keywords: [genealogy, signal fusion, NHTSA, CAPA, 리콜, 배터리 안전, OT 보안, SHE, 데이터 통합, 위험 우선순위, Genealogy, Signal Fusion, Recall, OT보안, 배터리, 복합사건, 교차공장, 우선순위]
related: [PP-D15-01, PP-D15-02, PP-D15-03, PP-D15-04, PP-D15-05, PP-D15-06, PP-D15-07, PP-D15-08, PP-D15-09, PP-D15-10, PP-D15-11, PP-D15-12, PP-D15-13, PP-D15-14]
priority: normal
domain: D15
section: D15-09
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 855
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-09 Enterprise Risk & Quality Pain-Point Register

| Pain Point ID | 문제 | 공개 근거·징후 | 내부 확인 KPI | 우선순위 |
|---|---|---|---|---|
| `PP-D15-01` | Material–Cell–Pack–VIN/ESS Genealogy 단절 | 23V-168의 특정 VIN 추적성 사례 | genealogy coverage | P0 |
| `PP-D15-02` | 검사·BMS·Complaint·Warranty·Return Data가 분리 | NHTSA EWR의 다중 Signal 구조 | signal fusion coverage | P0 |
| `PP-D15-03` | 작은 리콜범위가 안전한 결과처럼 관리 | 18대 특정범위도 내부단락·화재 Risk 존재 | population precision + unknown tail | P0 |
| `PP-D15-04` | 공장별 사건을 공통 원인으로 늦게 연결 | LGES Multi-OEM Equipment Query | cross-plant detection time | P0 |
| `PP-D15-05` | Containment·원인·CAPA·효과검증 상태 혼합 | 리콜·공정변경 후 재발검증 필요 | CAPA effectiveness | P0 |
| `PP-D15-06` | 작업자 SHE가 Lagging 사고율 중심 | OSHA 제조·열폭주·화학 Hazard | barrier impairment / HiPo near miss | P0 |
| `PP-D15-07` | 비상훈련 횟수는 있으나 Scenario·후속조치 품질 불명 | 그룹 2022년 314회 훈련 공개 | drill coverage / action closure | P1 |
| `PP-D15-08` | 손상 Battery의 이송·보관·재점화가 복구범위에서 누락 | NTSB Stranded Energy | post-incident monitoring compliance | P0 |
| `PP-D15-09` | IT 보안체계와 공장 OT·Safety Control이 분리 | ISMS 공개, Site별 OT Coverage 미공개 | IEC62443 zone/asset coverage | P0 |
| `PP-D15-10` | Risk 점수 단순합으로 공통원인·Tail Risk가 사라짐 | 다공장·다제도 복합 Exposure | scenario aggregation coverage | P0 |
| `PP-D15-11` | 수요·가동률·현금압박이 품질·정비 Risk로 전파되는 경로 미관리 | D10~D12 교차 Risk | stress-to-control trigger | P1 |
| `PP-D15-12` | JV 분리 시 품질·보증·Data Custody 공백 가능 | BOSK 구조재편 | separation obligation closure | P0 |
| `PP-D15-13` | 기후·Utility 위험을 국가·공장 평균으로만 평가 | 글로벌 공장·Supplier 분산 | site hazard×criticality coverage | P1 |
| `PP-D15-14` | AI가 상관관계를 원인으로, 추천을 안전결정으로 승격 | 제조·필드 Data의 편향·접근제약 | causal validation / unauthorized action | P0 |

### 핵심 해석

SK온의 전사 Risk는 개별 위험의 수가 많다는 데 있지 않다. **동일 Cell과 소재가 여러 공장·고객·정책·계약·현금흐름에 연결되는데, Signal과 Genealogy가 늦게 합쳐지면 작은 공정편차가 품질·가동·재무·평판의 복합사건으로 확대될 수 있다는 것**이 핵심이다.

---
