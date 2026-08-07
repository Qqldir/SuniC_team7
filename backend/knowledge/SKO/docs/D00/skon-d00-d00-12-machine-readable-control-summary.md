---
id: skon-d00-d00-12-machine-readable-control-summary
title: Machine-Readable Control Summary
summary: "D00 도메인의 정준 통제 항목별 완성도, 엔티티·소스·URL 정규화 현황, D17 연계 상태를 정의하는 메타데이터"
tags: [d00, governance, schema, "xref:d17"]
keywords: [D00, 기계 가독형 제어, YAML 형식, 스냅샷 통계, URL 정규화, 엔티티 스키마, 소스 스키마, D17 도메인, 릴리스 상태, 변경 이력, 정준화, 엔티티, D17, 메타데이터, 릴리스, 스냅샷, 데이터 품질]
related: []
priority: normal
domain: D00
section: D00-12
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 612
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-12 Machine-Readable Control Summary

```yaml
d00_control_summary:
  domain_id: D00
  canonical_name: Source, Entity, ID and Change-Log Master
  version: 1.2
  reference_date: 2026-08-03
  timezone: Asia/Seoul

  governed_domain_files: 17
  fact_source_domains: 16
  recommendation_domain: D17
  current_snapshot:
    total_lines: 69320
    total_bytes: 2276543
    url_occurrences: 839
    raw_unique_urls: 551
    normalized_unique_urls: 511
    D17_raw_seeds: 279
    D17_directly_referenced_unique_seeds: 166
    D17_deferred_seeds: 113
    D17_final_tasks: 60
    D17_priority_P0: 20
    D17_conditional_P1: 24
    D17_option_P2: 16

  canonical_controls:
    domain_master: COMPLETE_V1
    source_schema: COMPLETE_V1
    source_grade_and_evidence_level: COMPLETE_V1
    source_alias_and_url_normalization: COMPLETE_V1
    canonical_source_clusters: 20
    entity_schema: COMPLETE_V1
    entity_namespace: COMPLETE_V1
    high_risk_entity_aliases: 15
    fact_claim_relationship_schema: COMPLETE_V1
    scope_time_unit_unknown_standard: COMPLETE_V1
    ID_lifecycle_and_collision_rules: COMPLETE_V1
    change_event_schema: COMPLETE_V1
    initial_change_log: 12
    update_trigger_and_cadence: COMPLETE_V1
    automated_and_human_audit_rules: COMPLETE_V1
    current_integration_findings: 10
    resolved_findings: 8
    controlled_open_findings: 2
    D17_lineage_control: COMPLETE_V1

  current_release_state:
    D00_design_and_control_plane: COMPLETE_V1_2
    D01_to_D17_cross_domain_audit: COMPLETE
    canonical_source_crosswalk_full_population: COMPLETE_511_URL_IDENTITIES
    canonical_entity_crosswalk_full_population: COMPLETE_1491_IDENTIFIERS
    domain_patch_and_D17_gap_correction: COMPLETE
    integrated_freeze_and_submission_package: COMPLETE_PUBLIC_SNAPSHOT_WITH_INTERNAL_GATES
    snapshot_id: SKON-KB-20260803-v1.0
    snapshot_integrity: SHA256_MANIFEST_COMPLETE

  decision_boundaries:
    public_facts_only: true
    internal_metrics_estimated: false
    confidential_contract_terms_inferred: false
    legal_or_FTO_opinion_provided: false
    purchase_investment_or_partnership_approval: false
    autonomous_quality_safety_tax_legal_or_OT_authority: prohibited
```

---
