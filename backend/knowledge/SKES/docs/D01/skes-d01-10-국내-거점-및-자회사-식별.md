---
id: skes-d01-10-국내-거점-및-자회사-식별
title: 국내 거점 및 자회사 식별
summary: SK이노베이션 E&S의 본사·거점과 도시가스·발전·수소 자회사 7개씩을 Entity ID로 분류해 국내 조직구조와 각 법인의 사업 기능을 파악하는 참조목록이다.
tags: [d01, identity, table]
keywords: [도시가스, 발전사업, 에너지솔루션, 수소, LNG, 집단에너지, 코원에너지, 광양, 발전, 자회사, LNG 복합화력, Entity ID]
related: [SITE-ENS-KR-001, SITE-ENS-KR-002, ORG-ENS-CG-001, ORG-ENS-CG-002, ORG-ENS-CG-003, ORG-ENS-CG-004, ORG-ENS-CG-005, ORG-ENS-CG-006, ORG-ENS-CG-007, ORG-ENS-PWR-001, ORG-ENS-PWR-002, ORG-ENS-PWR-003, ORG-ENS-SOL-001, ORG-ENS-H2-001, ORG-ENS-H2-002, ORG-ENS-H2-003]
priority: normal
domain: D01
section: 10
source: SK이노베이션E&S_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 790
updated: 2026-08-06
---

> SK이노베이션 E&S · D01 기업 기본정보·법인구조·연혁

# 10. 국내 거점 및 자회사 식별

## 10.1 본체·직접 거점

| Site ID | 명칭 | 위치 | 유형 | 상태 |
|---|---|---|---|---|
| `SITE-ENS-KR-001` | SK이노베이션 E&S 본사 | 서울 종로구 종로 26 | CIC Headquarters | Current |
| `SITE-ENS-KR-002` | 광양 천연가스발전소 | 전남 광양시 제철로 일대 | Gas Power Site | Current official listing |

## 10.2 도시가스 자회사군

| Entity ID | 공식 명칭 | 대표 권역·거점 | 유형 |
|---|---|---|---|
| `ORG-ENS-CG-001` | 코원에너지서비스 | 서울·수도권 일부 | City Gas Subsidiary |
| `ORG-ENS-CG-002` | 부산도시가스 | 부산 | City Gas Subsidiary |
| `ORG-ENS-CG-003` | 영남에너지서비스 | 구미·포항 운영권역 | City Gas Subsidiary |
| `ORG-ENS-CG-004` | 충청에너지서비스 | 충북권 | City Gas Subsidiary |
| `ORG-ENS-CG-005` | 전남도시가스 | 전남권 | City Gas Subsidiary |
| `ORG-ENS-CG-006` | 강원도시가스 | 강원권 | City Gas Subsidiary |
| `ORG-ENS-CG-007` | 전북에너지서비스 | 전북권 | City Gas Subsidiary |

공식 홈페이지는 7개 도시가스 자회사가 전국 8개 권역에서 약 510만 가구에 도시가스를 공급한다고 설명한다. 영남에너지서비스는 구미와 포항 거점이 별도로 표시되므로 `자회사 수`와 `운영권역 수`를 혼동하면 안 된다. ([SRC-ENS-D01-0008], [SRC-ENS-D01-0009])

## 10.3 발전·에너지솔루션·수소 자회사군

| Entity ID | 명칭 | 구분 | 대표 기능 |
|---|---|---|---|
| `ORG-ENS-PWR-001` | 파주에너지서비스 | 발전 | LNG 복합화력 |
| `ORG-ENS-PWR-002` | 여주에너지서비스 | 발전 | LNG 복합화력 |
| `ORG-ENS-PWR-003` | 나래에너지서비스 | 발전·집단에너지 | 하남·위례 CHP 및 O&M |
| `ORG-ENS-SOL-001` | 엔솔브 | 에너지솔루션·집단에너지 | 분산전원·전력망 운영 기반 |
| `ORG-ENS-H2-001` | 아이지이(IGE) | 수소 | 인천 액화수소 관련 |
| `ORG-ENS-H2-002` | SK Plug Hyverse | 수소 | 수소사업 JV·운영 |
| `ORG-ENS-H2-003` | Boryeong BlueHy | 수소 | 보령 블루수소 프로젝트 |

위 목록은 공식 네트워크 페이지의 사업군 분류를 따른 1차 식별목록이다. 지분율, 연결여부, 법적 상호, 지배력은 D13에서 법인별로 재검증한다. ([SRC-ENS-D01-0009])

---
