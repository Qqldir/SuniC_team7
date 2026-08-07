---
id: skon-d06-d06-56-manufacturing-oi-prioritization
title: Manufacturing OI Prioritization
summary: 배터리 제조공정의 개선과제를 비즈니스 임팩트·기술성·데이터 준비도 등 6개 차원으로 우선순위 결정하는 평가 모델
tags: [d06, process, schema, table]
keywords: [OI 우선순위화, 가중치 공식, 스코어링, 수율 처리량, 안전 품질, 데이터 준비도, 포트폴리오 계층화, 기술 타당성, 경쟁 차별화, 공정 최적화, 우선순위평가, 사업영향도, 수율, 품질불량, 디지털스레드, 포트폴리오, 기술타당성, 데이터준비도]
related: []
priority: normal
domain: D06
section: D06-56.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1462
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-56. Manufacturing OI Prioritization

## 56.1 Prioritization Formula

```yaml
manufacturing_oi_priority_score:

  dimensions:

    business_impact:
      weight: 0.25
      criteria:
        - Yield
        - Throughput
        - Energy
        - Delivery
        - Value-added scrap

    safety_and_quality:
      weight: 0.20
      criteria:
        - Defect escape
        - Internal-short risk
        - Thermal risk
        - Warranty containment

    technical_feasibility:
      weight: 0.15
      criteria:
        - Sensor readiness
        - Data availability
        - Equipment compatibility
        - Pilot complexity

    data_readiness:
      weight: 0.10
      criteria:
        - Labels
        - Genealogy
        - Time synchronization
        - Measurement quality

    scale_reuse:
      weight: 0.15
      criteria:
        - Multi-line use
        - Multi-plant use
        - Multi-product use

    strategic_differentiation:
      weight: 0.15
      criteria:
        - SK On proprietary data
        - Patentability
        - Trade-secret value
        - Competitor differentiation

  scoring:
    each_dimension: 1_to_5
    final_score: weighted_sum

  control:
    - Missing baseline lowers data-readiness score
    - Unverified expected benefit is not treated as realized value
```

---

## 56.2 Top Priority OI Portfolio

| 순위 | OI Seed                                 | 핵심 가치            | 우선도   |
| -: | --------------------------------------- | ---------------- | ----- |
|  1 | D06-007 Material-to-Cell Digital Thread | 모든 분석의 데이터 기반    | 매우 높음 |
|  2 | D06-038 Yield Causal Knowledge Graph    | 후기불량의 상류원인 추적    | 매우 높음 |
|  3 | D06-039 Roll-to-Cell Coordinate Scrap   | 국부불량의 폐기범위 축소    | 매우 높음 |
|  4 | D06-016 Adaptive Formation              | 시간·에너지·품질 동시개선   | 매우 높음 |
|  5 | D06-021 Accelerated Aging               | WIP·공간·피드백 지연 축소 | 매우 높음 |
|  6 | D06-027 Busbar Weld Closed Loop         | 숨은 고저항 접합 예방     | 매우 높음 |
|  7 | D06-028 Thermal Interface Intelligence  | 냉각균일성·접착제 절감     | 매우 높음 |
|  8 | D06-037 Virtual Commissioning           | 신공장 Ramp-Up 위험감소 | 매우 높음 |
|  9 | D06-043 Finishing Bottleneck Optimizer  | 포메이션·에이징 처리량     | 매우 높음 |
| 10 | D06-047 Cross-Plant Recipe Transfer     | 해외공장 학습 재사용      | 매우 높음 |
| 11 | D06-042 Manufacturing AI Governance     | AI 확산의 품질·보안통제   | 매우 높음 |
| 12 | D06-030 Reworkable CTP                  | 고부가 Scrap·순환성 개선 | 매우 높음 |

---

## 56.3 Foundation–Optimization–Differentiation Portfolio

```yaml
oi_portfolio_layers:

  layer_1_foundation:
    purpose: 데이터와 추적성 확보
    seeds:
      - OI-SEED-D06-007
      - OI-SEED-D06-034
      - OI-SEED-D06-039
      - OI-SEED-D06-042

  layer_2_process_optimization:
    purpose: 수율·처리량·에너지 개선
    seeds:
      - OI-SEED-D06-005
      - OI-SEED-D06-016
      - OI-SEED-D06-021
      - OI-SEED-D06-027
      - OI-SEED-D06-028
      - OI-SEED-D06-043

  layer_3_scale_and_ramp:
    purpose: 신규 공장과 공장 간 학습확산
    seeds:
      - OI-SEED-D06-037
      - OI-SEED-D06-044
      - OI-SEED-D06-047
      - OI-SEED-D06-048
      - OI-SEED-D06-049

  layer_4_product_differentiation:
    purpose: CTP·신규 폼팩터 제조경쟁력
    seeds:
      - OI-SEED-D06-026
      - OI-SEED-D06-030
      - OI-SEED-D06-031
      - OI-SEED-D06-033
```

---

## 56.4 Recommended Execution Sequence

```text
Phase 1 — Data Foundation
Genealogy → Time Synchronization → Defect Ontology → KPI Standardization

Phase 2 — Visibility
Yield Waterfall → WIP → Bottleneck → Value-Added Scrap

Phase 3 — Prediction
Defect Prediction → Equipment Failure → Formation·Aging Risk

Phase 4 — Prescriptive Decision
Scheduling → Additional Inspection → Process Setting Recommendation

Phase 5 — Controlled Automation
Validated Closed Loop → Cross-Line Transfer → Cross-Plant Transfer
```

---

## 56.5 OI Project Gate

```yaml
manufacturing_oi_gate:

  G0_problem:
    required:
      - Quantified baseline
      - Process owner
      - Defect or loss definition

  G1_data:
    required:
      - Data source
      - Genealogy
      - Label quality
      - Sensor validation

  G2_poc:
    required:
      - Offline or shadow validation
      - Comparison baseline
      - Failure-mode analysis

  G3_pilot:
    required:
      - Production-line trial
      - Safe operating boundary
      - Operator workflow
      - Cybersecurity review

  G4_scale:
    required:
      - Reproducibility
      - Economic value
      - Multi-product applicability
      - Maintenance ownership

  G5_global_transfer:
    required:
      - Equipment normalization
      - Local validation
      - Model and recipe version control
```

---
