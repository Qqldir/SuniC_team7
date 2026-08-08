---
id: skes-d04-2-10-공통-데이터-ot-she
title: 공통 데이터·OT·SHE
summary: "E&S 부문의 공통 기술 체계를 정의하는 마스터로, OT 데이터 표준화부터 안전 디지털화, 사이버보안까지 6가지 핵심 기술의 구성·상태·우선도를 나타내는 표를 담고 있다."
tags: [d04, technology, table]
keywords: [OT historian, 자산계층, Digital Thread, 사이버보안, 위험성평가 디지털화, 이상감지, SCADA, 설비 안전, 사고 재발방지, 모델 거버넌스]
related: [TECH-ENS-COM-01, TECH-ENS-COM-02, TECH-ENS-COM-03, TECH-ENS-COM-04, TECH-ENS-COM-05, TECH-ENS-COM-06]
priority: normal
domain: D04
section: 2.10
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: 세부 Technology Master
tokens: 549
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · 세부 Technology Master

## 2.10 공통 데이터·OT·SHE

E&S는 IRR 기반 위험 공유, 공정설비 안전관리, 환경·대기오염 실시간 관리를 포함한 SHE 체계를 운영한다. 공통 기술은 개별 현장 안전계통을 대체하지 않고 데이터 연결과 의사결정을 보조해야 한다. ([SRC-ENS-D04-0007])

| TECH ID | 기술 | Layer | 입력 데이터 | 출력·제어 | KPI | 상태 | O/I |
|---|---|---|---|---|---|---|---|
| `TECH-ENS-COM-01` | OT historian·시계열 데이터 표준화 | L2/L4 | DCS·SCADA·BMS·AMI·CMMS | 공통 태그·품질·계보 | 연결률, 결측률 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-COM-02` | 자산계층·Digital Thread | L4 | 설비ID, 도면, 작업, 부품, 센서 | 자산–데이터–정비 관계 | 매칭률, 검색시간 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-COM-03` | OT 사이버보안·접근통제 | L2/L5 | 자산목록, 로그, 네트워크, 계정 | 이상·격리·감사 | MTTD, 패치·계정준수 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-COM-04` | 작업허가·위험성평가 디지털화 | L4/L5 | 작업, 위험, 인력, 가스측정, 교육 | 승인·차단·현장확인 | 위반, 승인시간 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-COM-05` | 다중현장 이상·사고 지식검색 | L3/L4 | IRR, 사고, 정비, 매뉴얼, 변경관리 | 유사사례·조치·재발방지 | 검색시간, 재발률 | `OPERATING_CONFIRMED` | 높음 |
| `TECH-ENS-COM-06` | 운영 최적화 모델 거버넌스 | L5 | 모델, 학습데이터, 성능, 변경·승인 | 버전·한계·승인·rollback | drift, 승인준수 | `ENABLING_CANDIDATE` | 높음 |

---
