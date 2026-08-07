---
id: skes-d07-17-d08-and-d17-handover
title: D08 and D17 Handover
summary: "D07 자산 DB에서 D08 공급망과 D17 혁신 과제로의 인수인계 시 필요한 데이터 충실화, 평가 차원, 포트폴리오 우선순위 매핑 현황."
tags: [d07, footprint, table, "xref:d08", "xref:d17", "xref:d06"]
keywords: [공급망, 자산인수인계, 데이터충실화, 포트폴리오, LNG, 재생에너지, 평가지표, 생명주기, 용량관리]
related: []
priority: normal
domain: D07
section: 17
source: SK이노베이션E&S_D07_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 767
updated: 2026-08-06
---

> SK이노베이션 E&S · D07 터미널·발전소·배관 등 자산·용량

# 17. D08 and D17 Handover

## 17.1 D08 Supply-Chain Handover

| D07 Asset | D08 Required Enrichment |
|---|---|
| Barossa | operator, lifting, condensate, cargo schedule, quality |
| Darwin/Freeport | tolling terms, train allocation, outage notices |
| LNG fleet | vessel IDs, charter, capacity, drydock, voyage |
| Boryeong TUA | nomination, service level, capacity charge, data right |
| power fleet | fuel contract, inventory cover, OEM/spares |
| city gas | KOGAS/city-gate supply and materials vendors |
| OWF1 | turbine OEM, vessel, spares, cable suppliers |
| KCE | cell/PCS/EPC/vendor and warranty |
| LH2 | feedstock, equipment vendor, tanker/station network |

## 17.2 D17 Scoring Inputs

| Scoring dimension | D07 field |
|---|---|
| operating maturity | lifecycle_state |
| value at scale | operating capacity + economic KPI |
| data availability | ownership/right + system |
| replicability | number of similar assets/regions |
| safety criticality | equipment/risk class |
| partner dependency | right_type/operator |
| implementation timing | operating vs development |
| double-count risk | capacity_type/inclusion_parent |

## 17.3 Recommended D17 Portfolio Shape

1. Operating-core P0: LNG terminal/power, city-gas safety, OWF1, KCE, Incheon LH2.
2. Data-foundation P0: asset hierarchy, rights registry, capacity validator.
3. Replication P1: fleet heat-rate, regional city-gas demand, BESS health, EV load.
4. Development-by-design P1: OWF2/3 and Quynh Lap digital handover.
5. Long-horizon P2: Bayu-Undan CCS injectivity/MRV.

---

# 18. Validation Checklist

| Test | Result |
|---|---|
| operating/development/planned states separated | PASS |
| Boryeong physical asset and TUA separated | PASS |
| equity-exited state reflected | PASS |
| gross/equity/contract/actual capacity taxonomy | PASS |
| MW/MWh/thermal units separated | PASS |
| KCE portfolio/project inclusion marked | PASS |
| renewable 3.5GW and 5GW status protected | PASS |
| LH2 nominal/actual distinction | PASS |
| EV chargers/ready circuits distinction | PASS |
| D06 process crosswalk included | PASS |
| internal data gaps not estimated | PASS |
| D08/D17 handover complete | PASS |

# 19. Completion Summary

| Metric | Count |
|---|---:|
| Source records | 28 |
| Asset records | 78 |
| Capacity ledger records | 23 |
| Rights records | 12 |
| Lifecycle events | 20 |
| Equipment classes | 23 |
| Risk records | 12 |
| Pain points | 30 |
| O/I Seeds | 45 |
| Internal data requests | 22 |
| AI retrieval chunks | 12 |

**D07 status: COMPLETE / REPRESENTATIVE_COMPANY_DEEP_DB**

**Primary handoff:** D08 공급망·조달 DB와 D17 O/I 과제 우선순위에서 asset_id, capacity_type, right_id, lifecycle_state를 공통키로 사용한다.
