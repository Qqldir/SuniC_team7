---
id: skes-d11-13-ccs-economics
title: CCS Economics
summary: "CCS 프로젝트의 톤당 순수익 계산 공식, 경제성에 영향하는 10가지 드라이버와 6개 KPI, 포집-저장 물량 매칭의 중요성을 제시한다."
tags: [d11, cost, table]
keywords: [CCS 원가 구조, 톤당 순비용, 포집에너지 페널티, 저장가동률, Firm volume, 포집-저장 물량 불일치, MRV 검증, 장기책임]
related: [CST-ENS-D11-063, CST-ENS-D11-064, CST-ENS-D11-065, CST-ENS-D11-066, CST-ENS-D11-067, CST-ENS-D11-068, CST-ENS-D11-069, CST-ENS-D11-070, CST-ENS-D11-071, CST-ENS-D11-072, KPI-ENS-D11-047, KPI-ENS-D11-048, KPI-ENS-D11-049, KPI-ENS-D11-050, KPI-ENS-D11-051, KPI-ENS-D11-052]
priority: normal
domain: D11
section: 13
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 576
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 13. CCS Economics

## 13.1 Tonne Economics

```text
Net CCS revenue/tCO2
= capture service fee
+ transport and storage tariff
+ policy/carbon value contractually retained
− capture energy and solvent
− compression and dehydration
− shipping/pipeline and terminal
− injection, monitoring and verification
− long-tail liability and remediation reserve
− unutilized shared-infrastructure cost
```

## 13.2 CCS Driver and KPI

| ID | Driver | 경제성 영향 |
|---|---|---|
| `CST-ENS-D11-063` | Capture utilization | 공유인프라 가동률 |
| `CST-ENS-D11-064` | Capture energy penalty | OPEX·생산감소 |
| `CST-ENS-D11-065` | Solvent performance | 소모·부식·정비 |
| `CST-ENS-D11-066` | CO2 specification | 처리·수용성 |
| `CST-ENS-D11-067` | Shipping/pipeline | 운송비·Schedule |
| `CST-ENS-D11-068` | Storage injectivity | 처리량·Well CAPEX |
| `CST-ENS-D11-069` | MRV | 검증비·Credit 적격 |
| `CST-ENS-D11-070` | Long-tail liability | 충당·보험·WACC |
| `CST-ENS-D11-071` | Emitter default | 수요·Debt service |
| `CST-ENS-D11-072` | Capture-storage mismatch | Stranded capacity |

| KPI ID | KPI | 정의 |
|---|---|---|
| `KPI-ENS-D11-047` | Net Cost/tCO2 Stored | 총원가−지원/영구저장 t |
| `KPI-ENS-D11-048` | Firm Volume Coverage | Firm emitter t/경제가동 t |
| `KPI-ENS-D11-049` | Capture-to-Storage Match | 동시 COD·물량 적합도 |
| `KPI-ENS-D11-050` | Infrastructure Utilization | 실제 주입/가용능력 |
| `KPI-ENS-D11-051` | MRV Acceptance Rate | 검증 승인 t/보고 t |
| `KPI-ENS-D11-052` | Liability-adjusted NPV | 폐쇄후 책임 포함 NPV |

IEA는 2026년 Storage 개발과 Firm Capture 물량의 불일치가 확대될 수 있다고 지적한다. 따라서 Bayu-Undan 등 CCS 경제성은 발표된 저장용량이 아니라 `Firm emitter·동시 COD·운송계약·저장권·MRV·장기책임`을 Gate로 판단한다.

---
