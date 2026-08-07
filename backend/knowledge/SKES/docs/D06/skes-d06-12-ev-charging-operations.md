---
id: skes-d06-12-ev-charging-operations
title: EV Charging Operations
summary: "전기차 충전소의 실시간 전력 할당 알고리즘과 충전 세션 관리, 결제, 유지보수의 운영 프로세스 및 KPI를 정의한 문서."
tags: [d06, process, schema]
keywords: [동적 전력 할당, 사이트 용량, 세션 관리, 결제, 수요 피크 회피, 충전기 제어, 에너지 미터링, 유지보수]
related: [PROC-ENS-D06-EVC-001, PROC-ENS-D06-EVC-002]
priority: normal
domain: D06
section: 12
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 626
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 12. EV Charging Operations

## 12.1 `PROC-ENS-D06-EVC-001` — Site Capacity and Dynamic Charging Allocation

```yaml
operator_boundary: EverCharge_affiliate_capability
public_confirmation: SmartPower dynamically manages charging loads
inputs:
  - building or site power limit
  - real_time non_EV load
  - connected vehicle and charger state
  - requested energy departure or priority if available
  - tariff demand charge and time price
  - circuit panel and transformer constraints
decisions:
  - charger enable disable
  - power allocation by session
  - ramp and queue priority
  - demand_peak avoidance
outputs:
  - charger setpoint
  - session energy and unmet request
  - site demand profile
  - override and exception log
failure_modes:
  - stale building load
  - charger communication loss
  - unfair or unstable allocation
  - breaker or transformer overload risk
  - vehicle departure data unavailable
  - site controller cloud disconnect
KPIs:
  - simultaneous_active_ports
  - peak_demand_reduction
  - delivered_vs_requested_energy
  - session_success
  - load_limit_violation
OI_seeds: [SEED-ENS-D06-058, SEED-ENS-D06-059]
```

## 12.2 `PROC-ENS-D06-EVC-002` — Session·Billing·Maintenance

```yaml
session_sequence:
  - user authentication
  - connector and vehicle handshake
  - authorization and tariff confirmation
  - energization and meter intervals
  - stop reason and connector release
  - payment invoice and receipt
minimum_record:
  - station EVSE connector and firmware
  - user_or_contract pseudonymous ID
  - start end and timezone
  - meter start end and intervals
  - allocated power actual power and limit reason
  - stop and failure code
  - tariff version payment and refund
maintenance_workflow:
  - remote health and heartbeat
  - fault triage and remote action
  - field dispatch and part replacement
  - electrical safety and meter test
  - return_to_service
failure_modes:
  - authentication payment failure
  - handshake or connector fault
  - meter discrepancy
  - offline charger not detected
  - repeat failure without root cause
KPIs:
  - uptime_and_port_availability
  - successful_session_rate
  - mean_time_to_repair
  - payment_exception
  - energy_delivery_shortfall
OI_seeds: [SEED-ENS-D06-060]
```

---
