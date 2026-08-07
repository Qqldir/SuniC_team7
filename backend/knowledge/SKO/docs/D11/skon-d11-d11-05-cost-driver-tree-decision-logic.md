---
id: skon-d11-d11-05-cost-driver-tree-decision-logic
title: Cost Driver Tree & Decision Logic
summary: "배터리 제조 원가 최적화를 위해 소재, 수율, 이용률, 에너지 등 12가지 비용 드라이버별 측정변수, 핵심지표, 연결된 의사결정을 정의하는 원가 관리 프레임워크"
tags: [d11, cost, table]
keywords: [원가절감, 소재·금속지수, 수율·스크랩, 가동률, 에너지, 정비·MTBF, 품질·불량, 물류·운송, 마진누수, 선행KPI, 원가 드라이버, 수익성, 비용 최적화, Margin Leakage, KPI, 의사결정, 배터리 제조, Yield]
related: []
priority: normal
domain: D11
section: D11-05
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 600
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-05 Cost Driver Tree & Decision Logic

| Cost Driver | 주요 변수 | 선행 KPI | 연결 의사결정 |
|---|---|---|---|
| Active Material | Chemistry·Metal index·Loading·계약연동 | BOM variance, purchase price variance | 소재대체·계약·제품 Mix |
| Yield & Scrap | 공정별 FPY·불량원인·Scrap 회수율 | defect ppm, scrap kg/kWh | 공정조건·검사·재활용 |
| Utilization | 고객승인·Call-off·Downtime·Changeover | scheduled/qualified utilization | Line 배정·휴지·전환 |
| Energy | Dry room·Coating/Drying·Formation 부하·Tariff | kWh/accepted kWh, peak demand | 운전시간·설비개선·PPA |
| Labor | 자동화·교대·교육·Ramp | labor hour/kWh, overtime | 인력배치·자동화 |
| Maintenance | 고장·예방정비·부품 Lead time | MTBF, MTTR, lost GWh | 예지보전·Spare 최적화 |
| Quality | 검사비·Rework·Claim·출하보류 | cost of poor quality, hold days | 검사전략·원인제거 |
| Logistics | Inbound/Outbound·Expedite·Duty | freight/kWh, expedite ratio | Network·Mode·Safety stock |
| Warranty | Field failure·열화·Recall | expected loss/kWh, claim severity | 설계·BMS·Reserve |
| Fixed Cost | 감가·인건비·임차·Overhead | fixed cost/qualified kWh | 가동률·자산재편 |
| Policy | 45X·보조금·관세·PFE 적격 | eligible/recognized/cash credit | 시설·BOM·법인구조 |
| Working Capital | 재고·채권·채무·Slow-moving | DIO/DSO/DPO, cash conversion | 생산·구매·수금 |

### Margin Leakage 우선순위

```text
P0: Customer-accepted volume shortfall × high fixed cost
P0: Yield/Scrap loss on high-value active materials
P0: Unpriced engineering, expedite, quality and warranty cost
P0: Reported profit dependent on unquantified compensation or credit
P1: Metal/FX pass-through lag and inventory mismatch
P1: Energy peak and dry-room/formation inefficiency
P1: Excess inventory and customer program cancellation exposure
P2: Low-value manual reporting and reconciliation work
```

---
