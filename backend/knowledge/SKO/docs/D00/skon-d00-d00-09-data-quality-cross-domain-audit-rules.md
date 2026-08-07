---
id: skon-d00-d00-09-data-quality-cross-domain-audit-rules
title: Data Quality & Cross-Domain Audit Rules
summary: "데이터 품질과 도메인 간 일관성을 검증하는 자동 검수, 7개 부서별 검수, 8단계 릴리스 게이트를 정의한다."
tags: [d00, governance, core-candidate, schema, table, "xref:d01", "xref:d17"]
keywords: [자동 검수, Release Gate, Entity, Lineage, Source, 도메인 감시, Scope, 품질 규칙, 데이터 검증, Cross-Domain, D00]
related: []
priority: critical
domain: D00
section: D00-09
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 641
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-09 Data Quality & Cross-Domain Audit Rules

### 1. 자동 검수

```yaml
automated_checks:
  markdown:
    - unclosed_code_fence
    - malformed_table_row
    - duplicate_heading_anchor
  identifiers:
    - duplicate_id
    - missing_referenced_id
    - invalid_namespace
    - orphan_alias
  sources:
    - duplicate_canonical_url
    - missing_original_url
    - missing_access_date
    - stale_source
    - broken_or_moved_url
  temporal:
    - future_event_marked_actual
    - expired_agreement_marked_active
    - superseded_rule_marked_current
    - overlapping_exclusive_status
  numeric:
    - mixed_currency_without_fx
    - capacity_scope_mismatch
    - gross_vs_attributable_mismatch
    - contract_option_included_as_firm
    - total_not_equal_to_components
  lineage:
    - claim_without_source
    - task_without_seed
    - seed_without_owner_domain
    - D17_source_id_not_found_in_domain
```

### 2. 사람 검수

| Review | 주 담당 | 확인사항 |
|---|---|---|
| Entity | 법무·재무·사업관리 | 법인·JV·CIC·공장·계약당사자 |
| Technical | R&D·제조·품질 | 제품 Revision·공정·불량·기술성숙도 |
| Commercial | 영업·SCM | Forecast·Call-off·가격·Option·공급경로 |
| Financial | Controller·Treasury | Scope·현금·원가·CAPEX·보증·Credit |
| Policy | 법무·세무·통상·ESG | 적용법령·Taxpayer·PFE·Passport·통관 |
| Safety | 품질·SHE·OT Security | Safety Barrier·Recall·Cyber·BCP |
| O/I | 현업 Owner·구매·IT·보안 | Pain Point·Data Right·PoC·Exit·ROI |

### 3. Release Gate

| Gate | 완료조건 |
|---|---|
| `G-D00-1 Inventory` | D01~D17 파일·Version·기준일 확인 |
| `G-D00-2 Source` | Source Alias·Canonical URL·등급·시점 연결 |
| `G-D00-3 Entity` | 고위험 법인·공장·JV·계약 Entity 중복 해소 |
| `G-D00-4 Fact` | Scope·단위·상태·Unknown 규칙 적용 |
| `G-D00-5 Lineage` | Claim→Source, D17 Task→Seed→Domain 연결 |
| `G-D00-6 Conflict` | 충돌·Stale·Superseded Queue 생성 |
| `G-D00-7 Domain Patch` | 발견된 불일치를 원본 도메인에 반영 |
| `G-D00-8 Freeze` | Snapshot·Change Log·검수결과 고정 |

---
