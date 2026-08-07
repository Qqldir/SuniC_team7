---
id: skon-d04-d04-011-011-storedot-sk온-적용-가치-9-9
title: 011 — StoreDot — SK온 적용 가치 (9)
summary: StoreDot 벤치마킹 분석 중 발견된 SK온 기술 데이터의 8가지 품질 이슈와 각 이슈의 심각도 및 제어 현황을 정리한 마스터 데이터
tags: [d04, technology, schema, table, "xref:d03", "xref:d17", "xref:d05", "xref:d06"]
keywords: [데이터 품질, 벤치마크, 제조사 주장, 기술 분류, Solid-State, 기술-제품 경계, 소유권, 로드맵, Source ID 중복, 제조사 클레임, 산업 표준, 전고체 로드맵, Entity 무결성, Ownership Scope]
related: []
priority: normal
domain: D04
section: D04-011
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 011 — StoreDot
tokens: 2921
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 011 — StoreDot

```yaml
issue_id: DQ-D04-001
issue: 동일 원문이 복수 Source ID로 등록됨

examples:
  dry_electrode:
    - SRC-SKON-D04-005
    - SRC-SKON-D04-030
    - SRC-SKON-D04-035

  fast_charging:
    - SRC-SKON-D04-007
    - SRC-SKON-D04-033

  ai_researcher:
    - SRC-SKON-D04-013
    - SRC-SKON-D04-029

  z_folding:
    - SRC-SKON-D04-021
    - SRC-SKON-D04-036

severity: MEDIUM

action:
  - canonical_source_id 생성
  - 기존 ID는 duplicate_of 관계로 보존
  - 청크에서는 canonical_source_id 우선 사용

status: OPEN_FOR_D00_EXPORT
```

---

## DQ-D04-002 — Provisional Entity Count

```yaml
issue_id: DQ-D04-002
issue: 활성 Canonical Technology 75개는 수작업 통합 결과

severity: MEDIUM

required_audit:
  - ID uniqueness
  - Alias collision
  - Parent-child cycle
  - Duplicate relation
  - Orphan technology
  - Missing source
  - Retired ID redirection

status: MACHINE_AUDIT_REQUIRED
```

---

## DQ-D04-003 — Manufacturer Claim Contamination

```yaml
issue_id: DQ-D04-003

affected_metrics:
  - Hyper Fast seven-minute charging
  - On-Vent pressure-cycle result
  - Large-surface cooling improvement
  - GRIDON warning lead time
  - AI Researcher productivity effect
  - External benchmark performance

severity: VERY_HIGH

control:
  - MANUFACTURER_CLAIM 태그 유지
  - 시험경계 저장
  - 독립시험 여부 분리
  - 경쟁사와 절대순위 자동생성 금지

status: CONTROL_IMPLEMENTED
```

---

## DQ-D04-004 — Technology and Product Boundary

```yaml
issue_id: DQ-D04-004

examples:
  - Hyper Fast Battery는 D03 제품, SUFast는 D04 기술
  - GRIDON은 D03 솔루션, EIS BMS는 D04 기술
  - On-Vent Cell은 D03 시제품, Laser Vent는 D04 기술
  - S-Pack+는 제품개념과 기술 아키텍처가 혼재

severity: HIGH

control:
  - Product ID와 Technology ID 분리
  - ENABLED_BY·USES_TECHNOLOGY 관계 사용
  - 동일 이름이라도 entity_type 유지

status: CONTROL_IMPLEMENTED
```

---

## DQ-D04-005 — Industry Baseline vs SK온 고유기술

```yaml
issue_id: DQ-D04-005

affected_entities:
  - Mixing
  - Wet Coating
  - Electrolyte Filling
  - Formation
  - Cell Sorting
  - General Welding

severity: VERY_HIGH

control:
  - ownership_scope: INDUSTRY_BASELINE
  - SK온 실제 공정조건은 NOT_DISCLOSED
  - 정부·연구소 공정자료를 SK온 내부공정으로 변환 금지

status: CONTROL_IMPLEMENTED
```

---

## DQ-D04-006 — Analytical Target Leakage

```yaml
issue_id: DQ-D04-006

affected_entities:
  - Battery Foundation Model
  - Predictive Quality Intelligence
  - Battery Operational Digital Twin
  - Manufacturing Digital Thread
  - High-Pressure Stack Management
  - Prelithiation

severity: VERY_HIGH

control:
  - evidence_maturity_level: EML_NA
  - ownership_scope: ANALYTICAL_TARGET
  - 현재 보유기술 검색에서 기본 제외

status: CONTROL_IMPLEMENTED
```

---

## DQ-D04-007 — Solid-State Roadmap Variation

```yaml
issue_id: DQ-D04-007
issue: 발표시점에 따라 전고체 목표연도와 목표단계가 변경됨

severity: HIGH

control:
  - 발표일별 목표값 보존
  - 상업용 시제품과 양산·상용화 구분
  - 최신 공식 목표만 current_target에 기록
  - realized_result와 분리

status: CONTROL_IMPLEMENTED
```

---

## DQ-D04-008 — Partner Status Ambiguity

```yaml
issue_id: DQ-D04-008

examples:
  Solid_Power: ACTIVE_TECHNOLOGY_TRANSFER
  Factorial: FEASIBILITY_MOU
  Standard_Energy: ACTIVE_JOINT_DEVELOPMENT
  Siemens_DISW: DEVELOPMENT_PARTNERSHIP
  Equipment_partners: TECHNOLOGY_VALIDATION

severity: HIGH

control:
  - MOU·JDA·기술이전·공급계약 상태 분리
  - 계약 구속력 표시
  - 관계 유효기간과 최신 상태 정기 재검증

status: CONTROL_IMPLEMENTED
```

---

## DQ-D04-009 — Quantitative Manufacturing Data Gap

```yaml
issue_id: DQ-D04-009

missing_fields:
  - Line speed
  - First-pass yield
  - Scrap rate
  - Equipment utilization
  - Energy per cell
  - Dry-room energy
  - Formation time
  - Inspection coverage
  - Changeover time
  - Ramp-up curve

severity: VERY_HIGH
handling: NOT_DISCLOSED
```

---

## DQ-D04-010 — AI Performance Evidence Gap

```yaml
issue_id: DQ-D04-010

missing_fields:
  - RFQ extraction accuracy
  - Cell performance prediction error
  - Cost-estimation error
  - Researcher acceptance rate
  - Materials AI hit rate
  - AI calendering yield effect
  - Model uncertainty
  - Model drift

severity: VERY_HIGH
handling:
  - 회사 기대효과와 실제 운영성과 분리
  - D17 PoC KPI로 전환
```

---

## 54.2 Missing Data Register

| Gap ID           | 미확보 정보          | 연결 도메인  |   우선도 |
| ---------------- | --------------- | ------- | ----: |
| GAP-D04-DATA-001 | 기술별 담당 조직·인력    | D05     |    높음 |
| GAP-D04-DATA-002 | 기술별 특허군·권리범위    | D05     | 매우 높음 |
| GAP-D04-DATA-003 | 제품별 실제 적용기술 BOM | D03·D06 | 매우 높음 |
| GAP-D04-DATA-004 | 공정별 장비·공급사      | D06·D07 | 매우 높음 |
| GAP-D04-DATA-005 | 양산수율·불량률·공정속도   | D06     | 매우 높음 |
| GAP-D04-DATA-006 | 파일럿 규모·샘플 상태    | D05·D07 | 매우 높음 |
| GAP-D04-DATA-007 | 기술별 투자비·원가효과    | D11·D12 | 매우 높음 |
| GAP-D04-DATA-008 | 기술별 고객인증 단계     | D03·D09 | 매우 높음 |
| GAP-D04-DATA-009 | 파트너 계약조건·IP 귀속  | D13     | 매우 높음 |
| GAP-D04-DATA-010 | 규제·안전인증 상태      | D14     |    높음 |
| GAP-D04-DATA-011 | 필드고장·보증 데이터     | D15     | 매우 높음 |
| GAP-D04-DATA-012 | 기술별 외부 스타트업 후보  | D16·D17 | 매우 높음 |

---

# D04-55. Canonical Source Index

## 55.1 Source Statistics

```yaml
source_index_summary:

  raw_source_records:
    sk_on_and_group: 46
    peer_reviewed: 5
    external_benchmark: 12
    total: 63

  source_grade_distribution:
    A_PLUS:
      - Government publications
      - Annual and ESG reports
      - Regulatory or equivalent institutional documents

    A:
      - Official corporate sources
      - Official partner sources
      - Peer-reviewed papers

  canonicalization_status:
    duplicate_groups_identified: true
    final_canonical_count: PENDING_D00_MACHINE_EXPORT
```

---

## 55.2 Main Canonical Source Groups

| Canonical Group | 연결 Source ID      | 주요 내용                  |
| --------------- | ----------------- | ---------------------- |
| CAN-D04-001     | D04-001           | SK온 공식 R&D 범위          |
| CAN-D04-002     | D04-003, D04-042  | 전고체 기술·로드맵             |
| CAN-D04-003     | D04-004           | 열전파 방지                 |
| CAN-D04-004     | D04-005, 030, 035 | 건식전극·AI 캘린더링           |
| CAN-D04-005     | D04-006           | CTP                    |
| CAN-D04-006     | D04-007, 033      | SUFast·급속충전            |
| CAN-D04-007     | D04-008, 037      | On-Vent·레이저            |
| CAN-D04-008     | D04-009, 016      | 파우치 통합 각형              |
| CAN-D04-009     | D04-010           | LFP 고도화                |
| CAN-D04-010     | D04-011           | GRIDON·EIS             |
| CAN-D04-011     | D04-012           | ESS 냉각수 안전             |
| CAN-D04-012     | D04-013, 029      | AI Researcher          |
| CAN-D04-013     | D04-014           | 고전압 미드니켈               |
| CAN-D04-014     | D04-015, RES-051  | 초고니켈 단결정               |
| CAN-D04-015     | D04-018, 019, 034 | BaaS AI·플릿             |
| CAN-D04-016     | D04-020           | ESS DC·AC 블록           |
| CAN-D04-017     | D04-021, 036      | Z-Folding              |
| CAN-D04-018     | D04-022           | S-Pack                 |
| CAN-D04-019     | D04-023           | S-Pack+                |
| CAN-D04-020     | D04-024           | EV 액침냉각·무선 BMS         |
| CAN-D04-021     | D04-025           | InterBattery 2025 기술전시 |
| CAN-D04-022     | D04-026           | VIB 공동개발               |
| CAN-D04-023     | D04-028           | SKIET 세라믹 분리막          |
| CAN-D04-024     | D04-031           | 제조 디지털 트윈 협력           |
| CAN-D04-025     | D04-032, 038      | 생산설비 지능화               |
| CAN-D04-026     | D04-043           | SIPE                   |
| CAN-D04-027     | D04-044           | LLZO                   |
| CAN-D04-028     | D04-045           | 광소결·LMRO               |
| CAN-D04-029     | D04-046           | 리튬 표면·GPE              |
| CAN-D04-030     | EXT-052           | Solid Power–SK온        |
| CAN-D04-031     | EXT-053, 054      | Factorial·차량검증         |
| CAN-D04-032     | EXT-055           | QuantumScape           |
| CAN-D04-033     | EXT-056           | Toyota·Idemitsu        |
| CAN-D04-034     | EXT-057           | Samsung SDI            |
| CAN-D04-035     | EXT-058           | LG Energy Solution     |
| CAN-D04-036     | EXT-059           | CATL                   |
| CAN-D04-037     | EXT-060           | ProLogium              |
| CAN-D04-038     | EXT-061           | SES AI                 |
| CAN-D04-039     | EXT-062           | 24M                    |
| CAN-D04-040     | EXT-063           | StoreDot               |

---

## 55.3 Peer-Reviewed Canonical Sources

| Source ID       | 연구주제        | 연결 기술        |
| --------------- | ----------- | ------------ |
| SRC-RES-D04-047 | 표면개질 리튬메탈   | TECH-D04-071 |
| SRC-RES-D04-048 | 광소결 가넷 전해질  | TECH-D04-068 |
| SRC-RES-D04-049 | LMRO 단결정    | TECH-D04-074 |
| SRC-RES-D04-050 | GPE 잔류 모노머  | TECH-D04-077 |
| SRC-RES-D04-051 | 초고니켈 대형 단결정 | TECH-D04-075 |

---

# D04 Final YAML
