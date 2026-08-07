---
id: skes-d10-15-scenario-library
title: Scenario Library
summary: "LNG, 전력, BESS, 수소, CCS 등 사업 영역별 시장 시나리오 13개와 각 시나리오의 트리거, 시장영향, 경영 대응 방안을 정의한 시나리오 매트릭스 표."
tags: [d10, market, schema, table]
keywords: [시나리오 매트릭스, LNG, 전력, BESS, 수소, CCS, PPA, 신재생에너지, 트리거 임계값, EV충전]
related: [SCN-ENS-D10-001, SCN-ENS-D10-002, SCN-ENS-D10-003, SCN-ENS-D10-004, SCN-ENS-D10-005, SCN-ENS-D10-006, SCN-ENS-D10-007, SCN-ENS-D10-008, SCN-ENS-D10-009, SCN-ENS-D10-010, SCN-ENS-D10-011, SCN-ENS-D10-012, SCN-ENS-D10-013]
priority: normal
domain: D10
section: 15
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 678
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# 15. Scenario Library

## 15.1 Scenario Matrix

| Scenario ID | Name | Trigger | Market effect | E&S exposure | Decision |
|---|---|---|---|---|---|
| `SCN-ENS-D10-001` | LNG_TIGHT_HIGH_PRICE | Gulf recovery delay | JKM/freight up | procurement·power margin | hedge·cargo allocation |
| `SCN-ENS-D10-002` | LNG_SUPPLY_WAVE | non-Gulf ramp/on-time | prices ease | upstream margin vs downstream benefit | portfolio rebalance |
| `SCN-ENS-D10-003` | KOREA_LOW_SMP | mild weather·low fuel | generation margin down | CCGT/CHP | maintenance·dispatch |
| `SCN-ENS-D10-004` | KOREA_PEAK_STRESS | heatwave·outage | peak price/reliability up | generation·BESS | availability priority |
| `SCN-ENS-D10-005` | RENEWABLE_CURTAILMENT | grid delay·solar growth | captured price down | renewable/PPA | storage·grid tech |
| `SCN-ENS-D10-006` | PPA_DEMAND_ACCELERATION | RE100/data center | bankable offtake up | PPA pipeline | asset matching |
| `SCN-ENS-D10-007` | ERCOT_SPREAD_COMPRESSION | BESS saturation | merchant margin down | KCE | duration·market diversify |
| `SCN-ENS-D10-008` | ERCOT_VOLATILITY | weather/grid shock | scarcity events up | KCE | risk-adjusted bids |
| `SCN-ENS-D10-009` | EV_CHARGING_UTILIZATION_UP | EV stock grows | session/port up | EverCharge | service scale |
| `SCN-ENS-D10-010` | H2_DEMAND_DELAY | vehicle/station delay | plant utilization low | liquid H2 | staged production |
| `SCN-ENS-D10-011` | H2_FLEET_CLUSTER | buses+stations align | local kg demand up | liquid H2 | cluster contract |
| `SCN-ENS-D10-012` | CCS_STORAGE_WITHOUT_CAPTURE | storage FID, emitter delay | underutilized infra | Bayu-Undan | no-FID gate |
| `SCN-ENS-D10-013` | CCS_HUB_BANKABLE | firm emitters+permit | contracted tCO2 up | CCS | partner/invest |

## 15.2 Scenario Trigger Thresholds

Threshold는 내부 Risk Committee가 승인하며 공개자료만으로 자동 설정하지 않는다.

```yaml
trigger_candidates:
  LNG:
    - JKM_vs_contract_slope
    - freight_rate
    - Gulf_export_recovery
    - terminal_inventory_days
  POWER:
    - SMP_percentile
    - clean_spark_spread
    - reserve_margin
    - weather_load_deviation
  BESS:
    - ancillary_price_decay
    - energy_spread
    - operating_BESS_MW
    - degradation_cost
  H2:
    - paid_kg_per_day
    - active_vehicle_count
    - station_availability
  CCS:
    - firm_emitter_tCO2
    - permitted_storage
    - injectivity_confidence
```

---
