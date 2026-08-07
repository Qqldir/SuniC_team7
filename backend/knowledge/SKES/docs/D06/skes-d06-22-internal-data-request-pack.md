---
id: skes-d06-22-internal-data-request-pack
title: Internal Data Request Pack
summary: "SK이노베이션 E&S의 LNG·발전·도시가스·수소·재생에너지 등 20개 비즈니스 영역별 내부 데이터 요청 항목, 필드 정의, 보안 등급을 명시한 마스터 테이블."
tags: [d06, process, schema, table]
keywords: [LNG, 발전, 도시가스, SCADA, ESS, H2, CCS, 보안등급, 데이터마스터, 터미널]
related: [REQ-ENS-D06-001, REQ-ENS-D06-002, REQ-ENS-D06-003, REQ-ENS-D06-004, REQ-ENS-D06-005, REQ-ENS-D06-006, REQ-ENS-D06-007, REQ-ENS-D06-008, REQ-ENS-D06-009, REQ-ENS-D06-010, REQ-ENS-D06-011, REQ-ENS-D06-012, REQ-ENS-D06-013, REQ-ENS-D06-014, REQ-ENS-D06-015, REQ-ENS-D06-016, REQ-ENS-D06-017, REQ-ENS-D06-018, REQ-ENS-D06-019, REQ-ENS-D06-020]
priority: normal
domain: D06
section: 22
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 925
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 22. Internal Data Request Pack

| Request ID | 내부자료 | 최소필드 | 대상 과제 | 보안/주의 |
|---|---|---|---|---|
| `REQ-ENS-D06-001` | LNG 계약·권리 abstraction | source, entitlement, window, flexibility, penalty | LNG planning | Highly confidential |
| `REQ-ENS-D06-002` | cargo·선박·berth history | voyage, ETA, delay, cargo, terminal | ETA/berth | Confidential |
| `REQ-ENS-D06-003` | terminal historian extract | tag, unit, quality, tank, BOG, sendout | inventory/BOG | OT restricted |
| `REQ-ENS-D06-004` | terminal mass balance | receipts, stock, sendout, fuel, loss | reconciliation | Commercial restricted |
| `REQ-ENS-D06-005` | 발전 unit event history | mode, start, trip, load, fuel, ambient | startup/performance | OT restricted |
| `REQ-ENS-D06-006` | 발전 historian–EAM map | asset, tag, alarm, work, failure | predictive maintenance | OT restricted |
| `REQ-ENS-D06-007` | CEMS·수질 QA data | analyzer, calibration, valid flag, chemistry | environment | Compliance restricted |
| `REQ-ENS-D06-008` | CHP heat interval data | supply/return, flow, customer, weather | heat forecast | Customer aggregated |
| `REQ-ENS-D06-009` | 도시가스 GIS asset master | segment, material, age, depth, location | RBMS/excavation | Critical infrastructure |
| `REQ-ENS-D06-010` | 누출·검사·수리 history | location, method, severity, cause, closure | leak/RBMS | Safety sensitive |
| `REQ-ENS-D06-011` | 정압기 sensor/work data | P/flow/valve/alarm/work | condition | OT restricted |
| `REQ-ENS-D06-012` | custody·meter·billing data | interval, correction, exception, tariff | UFG/meter | Personal/commercial |
| `REQ-ENS-D06-013` | 재생 SCADA/forecast/work | asset, weather, forecast, actual, outage | forecast/O&M | Commercial |
| `REQ-ENS-D06-014` | PPA settlement rule and exception | contract, meter, allocation, REC, adjustment | settlement | Contract confidential |
| `REQ-ENS-D06-015` | ESS bid/BMS/warranty | bid, award, dispatch, SOC/SOH, constraint | KCE optimizer | Affiliate proprietary |
| `REQ-ENS-D06-016` | EV site/session/fault | site limit, load, session, fault, work | SmartPower/O&M | Privacy and affiliate IP |
| `REQ-ENS-D06-017` | H2 liquefier historian | process, power, product, tank, event | energy/BOR | OT/vendor restricted |
| `REQ-ENS-D06-018` | H2 logistics mass balance | load, tanker, route, delivery, loss | routing/transfer | Commercial/SHE |
| `REQ-ENS-D06-019` | CCS pilot/process design data | stream, solvent, utility, CO2, MRV | CCS seeds | Partner/JV confidential |
| `REQ-ENS-D06-020` | enterprise OT/IT architecture | source, owner, interface, cyber zone | all D06 | Highly restricted |

## 22.1 Safe Data-Sandbox Rule

```yaml
external_PoC_access:
  default: no_direct_OT_connection
  preferred:
    - deidentified historical extract
    - read_only replica
    - approved feature service
    - synthetic or replay environment
  prohibited_without_formal_approval:
    - write access to DCS PLC BMS PCS or safety system
    - customer PII export
    - raw critical_infrastructure geometry export
    - vendor confidential control logic
  promotion_path:
    - offline validation
    - shadow mode
    - operator advisory
    - bounded closed_loop only after MOC and safety/cyber approval
```

---
