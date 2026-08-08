---
id: skes-d07-15-knowledge-graph-and-relationship-triples
title: Knowledge Graph and Relationship Triples
summary: "SK이노베이션 주요 에너지 자산 간 공급·운영·권리 관계를 RDF 트리플로 정의하고, 지분 현황·장기사용권·자산 간 영향경로 등 경영 질문에 답할 수 있는 지식그래프이다."
tags: [d07, footprint, table]
keywords: [지분, TUA, LNG, 자산관계, 공급경로, 발전자산, 권리구조, 포트폴리오, 에너지자산, RDF]
related: []
priority: normal
domain: D07
section: 15
source: SK이노베이션E&S_D07_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 635
updated: 2026-08-06
---

> SK이노베이션 E&S · D07 터미널·발전소·배관 등 자산·용량

# 15. Knowledge Graph and Relationship Triples

## 15.1 Core Relations

| Subject | Predicate | Object |
|---|---|---|
| Barossa | supplies | Darwin LNG |
| Darwin LNG | loads | LNG cargo |
| LNG carrier fleet | delivers_to | Boryeong |
| Boryeong TUA | supports | Korean LNG-power portfolio |
| Paju | consumes | LNG |
| Hanam CHP | produces | electricity_and_heat |
| Ko-one | member_of | city_gas_portfolio |
| OWF1 | predecessor_learning_for | OWF2_and_3 |
| KCE NY6 | member_of | KCE operating portfolio |
| MarketCapture | optimizes | KCE market dispatch |
| SmartPower | allocates | EverCharge site power |
| Incheon LH2 plant | supplies | LH2 tanker network |
| Bayu-Undan | candidate_storage_for | CCS chain |
| Quynh Lap terminal | supplies | Quynh Lap CCGT |

## 15.2 Rights Relations

| Subject | Predicate | Object |
|---|---|---|
| E&S | holds_37.5_percent | Barossa |
| E&S | holds_25_percent | Darwin LNG |
| E&S | no_longer_equity_owner | Boryeong Terminal |
| E&S group | retains_3.5Mtpa_TUA | Boryeong Terminal |
| E&S | holds_51_percent | Jeonnam OWF1 |
| KCE | operates_portfolio | US BESS |
| IGE | operates | Incheon LH2 plant |

## 15.3 Example Retrieval Queries

1. 지분은 없지만 장기 사용권이 남아 있는 자산은 무엇인가.
2. 운영능력과 개발 pipeline이 한 수치로 소개되는 자산군은 무엇인가.
3. LNG 공급중단이 Paju 발전에 전파되는 경로는 무엇인가.
4. 전력 MW와 열능력을 동시에 가진 CHP는 무엇인가.
5. 2025년 이후 상업운전을 시작한 자산은 무엇인가.
6. 2030~2031년 목표 개발자산의 데이터 인프라 요구사항은 무엇인가.
7. KCE 623MW에 포함되어 중복합산하면 안 되는 개별 프로젝트는 무엇인가.
8. 내부 historian이 없으면 검증할 수 없는 P0 과제는 무엇인가.
9. JV 또는 TUA 때문에 데이터 접근권 확인이 선행되는 자산은 무엇인가.
10. 같은 설비를 물리자산과 계약권리 두 레코드로 저장한 사례는 무엇인가.

---
