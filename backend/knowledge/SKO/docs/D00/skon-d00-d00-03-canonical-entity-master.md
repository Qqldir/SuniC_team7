---
id: skon-d00-d00-03-canonical-entity-master
title: Canonical Entity Master
summary: SK온 마스터 데이터의 모든 엔티티(법인·조직·제품·기술·계약 등)에 대해 canonical ID로 유일하게 식별하고 분류하는 체계를 정의합니다.
tags: [d00, governance, core-candidate, schema, table, "xref:d01", "xref:d02", "xref:d03", "xref:d04"]
keywords: [정준 엔티티, 엔티티 ID, 엔티티 타입, ID 규칙, canonical_entity_id, 엔티티 마스터, 별칭 분리, Owner Domain, 레거시 ID, ID 명명 규칙, 법인 분류, alias·legacy ID, D00 도메인, 마스터 데이터, entity_record]
related: [ORG-SKON-000001, COMP-SKON-001, CO-SKON, ORG-SKI-000001, ORGUNIT-SKON-ENMOVE, ORGUNIT-SKON-TRADING, ORG-HSBMA-000001, ORG-BOSK-000001, ORG-SKOTN-000001, ORG-SKBA-000001, ORG-SOLIDPOWER-000001, ORG-FACTORIAL-000001, ORG-EXXON-000001, ORG-FORD-000001, ORG-HMG-000001, ORG-NISSAN-000001, ORG-FLATIRON-000001]
priority: critical
domain: D00
section: D00-03
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 1584
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-03 Canonical Entity Master

### 1. Entity Record Schema

```yaml
entity_record:
  canonical_entity_id: ORG-SKON-000001
  entity_type: LEGAL_ENTITY
  canonical_name: SK On Co., Ltd.
  names:
    ko: 에스케이온 주식회사
    en: SK On Co., Ltd.
  aliases: [SK온, SK On]
  legacy_entity_ids: [COMP-SKON-001, CO-SKON]
  parent_entity_id: ORG-SKI-000001
  jurisdiction: KR
  legal_form: CORPORATION
  valid_from: 2021-10-01
  valid_to: null
  status: ACTIVE
  owner_domain: D01
  source_ids: []
  last_verified_at: 2026-08-03
  confidence: CONFIRMED_SINGLE|CONFIRMED_MULTI|INDICATED|HYPOTHESIS|CONFLICTED
```

### 2. Entity Type와 Canonical ID

| Type | Prefix | 기본키 구성 | Owner Domain |
|---|---|---|---|
| 법인·기관·회사 | `ORG-` | 법적 실체+관할+기간 | D01 |
| 내부 조직·CIC | `ORGUNIT-` | 법인+조직명+유효기간 | D01 |
| 사업 포트폴리오 | `BIZ-` | 회사+사업영역 | D02 |
| 제품·서비스 | `PROD-`, `SERV-` | Family+Form+Revision | D03 |
| 기술·Capability | `TECH-`, `CAP-` | 기술 정의+버전 | D04 |
| R&D Program | `RND-` | Program+Phase | D05 |
| 특허 Family·권리 | `PF-`, `RIGHT-` | Family+Jurisdiction/Right | D05 |
| 제조공정·불량 | `PROC-`, `DEF-` | 공정단계/불량정의 | D06 |
| 공장·Line·Capacity Event | `PLANT-`, `LINE-`, `CAPEVT-` | 소유법인+Site+기간 | D07 |
| 소재·Grade·Lot | `MAT-`, `GRADE-`, `LOT-` | 물질+규격+Lot | D08 |
| 공급사 시설·Origin Path | `FAC-`, `ORIGIN-` | 법인+위치+공정 | D08 |
| 고객·Program·Order Event | `CUST-`, `PRG-`, `ORD-` | 고객법인+Program+기간 | D09 |
| 시장·전망·경쟁 Event | `MKT-`, `FCST-`, `CEVT-` | 범위+지역+기간+버전 | D10 |
| 경제성 Scope·Cost Event | `ECON-`, `COST-` | 법인+Plant+Product+Customer+기간 | D11 |
| 투자·Funding Event | `PROJ-`, `FUND-` | Project+법인+Stage+기간 | D12 |
| 계약·조항·의무 | `AGR-`, `CLAUSE-`, `OBL-` | 계약군+Version+당사자 | D13 |
| 법령·규제의무 | `RULE-`, `REGO-` | 관할+Instrument+Version | D14 |
| Risk Event·Control | `RISK-`, `CTRL-` | 사건/시나리오+Population+기간 | D15 |
| 외부 Provider·Solution | `PROV-`, `SOL-` | 법인+제품 Version | D16 |
| O/I Seed·Task | `OI-SEED-`, `D17-OI-` | 원천 도메인/최종 Serial | D17 |

### 3. 고위험 Entity Alias Register

| Canonical Entity | Alias·Legacy | 반드시 분리할 대상 | 판정 |
|---|---|---|---|
| `ORG-SKON-000001` SK On Co., Ltd. | `COMP-SKON-001`, `CO-SKON`, SK온 | SK Innovation 연결·Battery Segment | 법인·Segment·그룹연결 분리 |
| `ORG-SKI-000001` SK Innovation Co., Ltd. | SK이노베이션 | SK온 단독 | 모회사 연결수치를 SK온 단독으로 사용 금지 |
| `ORGUNIT-SKON-ENMOVE` | SK엔무브 CIC | 합병 전 SK Enmove 법인 | 법인/내부조직을 시점으로 분리 |
| `ORGUNIT-SKON-TRADING` | SK트레이딩인터내셔널 CIC | 합병 전 SK Trading International 법인 | 시점·법적 의무 분리 |
| `ORG-HSBMA-000001` | HMG–SK Battery America | Georgia 공장·HMG 전체 | 50:50 지분과 통제·부담 분리 |
| `ORG-BOSK-000001` | BlueOval SK | Ford·SK온·Kentucky·Tennessee | 2026 분리 전후 자산·차입·보증 분리 |
| `ORG-SKOTN-000001` | SK On Tennessee | BlueOval SK Tennessee | 분리 후 법인·2028 준비상태 보존 |
| `ORG-SKBA-000001` | SK Battery America | Georgia Site/Plant | 법인과 공장 분리 |
| `ORG-SOLIDPOWER-000001` | Solid Power | Sulfide electrolyte·Pilot Line | 회사·기술·R&D License·상업 License 분리 |
| `ORG-FACTORIAL-000001` | Factorial Energy | FEST·Solstice | MOU와 양산권리 분리 |
| `ORG-EXXON-000001` | ExxonMobil | Arkansas Lithium Project | MOU와 확정 Offtake 분리 |
| `ORG-FORD-000001` | Ford Motor Company | Ford–CATL LFP model·BOSK | 고객·JV Partner·외부사례 역할 분리 |
| `ORG-HMG-000001` | Hyundai Motor Group | Hyundai Motor·Kia·HSBMA | 그룹과 계약당사 법인 분리 |
| `ORG-NISSAN-000001` | Nissan | 개별 차량 Program | 총 계약과 연도별 Call-off 분리 |
| `ORG-FLATIRON-000001` | Flatiron Energy | 1GWh 계약·6.2GWh 우선협상 | 확정량과 Pipeline 분리 |

### 4. Entity Resolution Rule

1. 회사명 일치만으로 같은 법인으로 합치지 않는다. 관할·법인등록명·기간·지배관계를 확인한다.
2. `공장`, `Site`, `법인`, `JV`, `Line`은 각각 별도 Entity다.
3. 합병·분할·양도는 이름 수정이 아니라 `corporate_action_event`와 전후 Entity 관계로 기록한다.
4. 제품 Family와 고객승인 Revision을 구분한다.
5. 공급사 이름과 실제 생산시설을 분리한다.
6. 특허 출원인·현재 권리자·라이선시·실시주체를 분리한다.
7. 고객그룹과 구매계약 당사 법인을 분리한다.
8. 규제상 Taxpayer, Economic Operator, Importer, Manufacturer를 회사그룹명으로 대체하지 않는다.
9. Provider 회사와 제품·서비스 Version을 분리한다.
10. Alias 충돌이 해소되지 않으면 합치지 않고 `POSSIBLE_SAME_AS`로 둔다.

---
