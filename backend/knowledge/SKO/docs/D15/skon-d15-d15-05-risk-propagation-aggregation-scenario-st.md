---
id: skon-d15-d15-05-risk-propagation-aggregation-scenario-st
title: "Risk Propagation, Aggregation & Scenario Stress Test"
summary: "공급망 리스크가 현금·안전까지 파급되는 전파 경로와, 리스크를 5개 층위로 정량화하는 기준, SK온의 8개 핵심 시나리오를 보여준다."
tags: [d15, risk, table]
keywords: [인과 그래프, 공통 원인, 정량화 경계, 회복탄력성, 공급망, Cell Failure Mode, OT 침해, 현금 영향, 공급망 리스크, 연쇄 영향, 정량화 방법론, 우선순위 시나리오, 현금 충격]
related: [SCN-D15-01, SCN-D15-02, SCN-D15-03, SCN-D15-04, SCN-D15-05, SCN-D15-06, SCN-D15-07, SCN-D15-08]
priority: normal
domain: D15
section: D15-05
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 829
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-05 Risk Propagation, Aggregation & Scenario Stress Test

### 1. Cross-domain Propagation Graph

```text
Supplier Delay / Quality Drift
→ Material Substitution or Line Change
→ Customer Requalification / Ramp Loss
→ Lower Good-output and Utilization
→ Qualified-kWh / Revenue / 45X / Cash Change
→ Covenant or Liquidity Stress
→ Deferred Maintenance / Workforce Pressure
→ Higher Quality·SHE Residual Risk
```

위 흐름은 예시 시나리오이며 자동 인과로 확정하지 않는다. 각 Edge에는 `관찰·가설·재현·검증` 상태와 시간지연을 저장한다.

### 2. Risk Score와 정량화 경계

| 층 | 목적 | 허용 방식 | 금지 방식 |
|---|---|---|---|
| Screening | 빠른 우선순위 | Severity·Likelihood·Velocity·Detectability·Control weakness | RPN만으로 Safety Risk 종료 |
| Exposure | 영향범위 | Population·GWh·고객·법인·공장·계약 연결 | Scope 미확정 상태의 단일 금액 |
| Financial | 손익·현금 | 범위·기간·확률을 가진 Scenario | 비공개 Warranty/Recall Cost 추정치를 사실로 저장 |
| Tail Risk | 저빈도 고중대 | Stress·Reverse Stress·Bow-tie | 평균 Expected Loss로만 평가 |
| Aggregation | 전사 집중도 | 공통 원인·상관·동시발생 Scenario | 서로 다른 1~5점 점수 단순합산 |

### 3. Priority Scenarios

| Scenario ID | Trigger | 주요 전파 | 검증할 Resilience Option |
|---|---|---|---|
| `SCN-D15-01` | 공통 Cell Failure Mode의 Field Signal 급증 | Stop Ship→고객공장→Recall/Warranty→현금·평판 | Genealogy 기반 Population·대체공급·CAPA |
| `SCN-D15-02` | 미국 핵심 소재 PFE/MACR 부적격 | 45X→원가→제품배정→계약·현금 | 대체조달·BOM Requalification·가격조정 |
| `SCN-D15-03` | 주요 OEM Call-off 급감 | 가동률→고정비→재고→유동성 | EV↔ESS 전환·Line Flex·CAPEX Hold |
| `SCN-D15-04` | 신규공장 Ramp 품질정체 | Scrap·납기·고객승인→현금 | Golden Batch·Cross-plant 전문가·Stage Gate |
| `SCN-D15-05` | OT 침해 또는 MES/Genealogy 중단 | 생산정지·품질증빙 상실·안전통제 영향 | Segmentation·Offline Safe Mode·Immutable Backup |
| `SCN-D15-06` | 화재·폭발·대규모 Chemical Release | 인명·가동·규제·지역사회 | Incident Command·상호지원·대체 Site·공개소통 |
| `SCN-D15-07` | 홍수·폭염·전력/용수 중단 | Supplier·Plant·Logistics 동시영향 | Site hardening·Utility redundancy·Inventory Buffer |
| `SCN-D15-08` | JV·Partner 분리 또는 분쟁 | Data·품질·보증·차입·운영권 단절 | Separation Room·TSA·Record Custody·Exit Playbook |

---
