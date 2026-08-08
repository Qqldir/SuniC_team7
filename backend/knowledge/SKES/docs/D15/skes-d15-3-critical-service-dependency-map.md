---
id: skes-d15-3-critical-service-dependency-map
title: Critical Service & Dependency Map
summary: 발전·LNG·재생에너지·BESS·수소 사업의 중요 서비스를 T0~T3로 분류하고 각 계층별 복구목표·의존성을 정의하는 문서
tags: [d15, risk, table]
keywords: [T0/T1/T2/T3, 인명안전, RTO, LNG, 발전, BESS, 수소, EMS, 복구탄력성, 정산]
related: []
priority: normal
domain: D15
section: 3
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 598
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 3. Critical Service & Dependency Map

## 3.1 Service Tier

| Tier | Critical Service | 실패 영향 | 최소 복구목표 |
|---|---|---|---|
| `T0` | 인명·공정안전 보호, ESD, gas detection, fire protection | 인명·중대사고 | 즉시/Fail-safe; RTO 수치 내부정의 |
| `T0` | 도시가스 긴급차단·압력/공급 안전 | 공공안전·대규모 공급장애 | 안전상태 유지, 비상대응 연속성 |
| `T0` | LNG/LH2 containment·pressure relief | 화재·폭발·누출 | 독립 보호계층 유지 |
| `T1` | 발전/CHP 제어·black-start/계통 interface | 전력·열 공급, 매출 | 자산별 RTO·minimum stable load |
| `T1` | BESS EMS/BMS/PCS 안전제어 | 화재·시장불이행 | safe state + telemetry restoration |
| `T1` | trading/dispatch/market communication | 정산·입찰·노출 | deadline별 alternate submission |
| `T1` | LNG nomination·shipping·terminal scheduling | 연료공급·demurrage | cargo horizon별 대체절차 |
| `T2` | PPA metering/settlement·REC evidence | 청구·환경가치 | billing cycle 내 lineage 복구 |
| `T2` | EV charging network/payment | 고객 SLA·매출 | remote/local fallback |
| `T2` | H2 dispatch·station replenishment | 판매·fleet 운행 | station inventory buffer 기반 |
| `T2` | ERP·AP/AR·treasury | 현금·supplier/customer | payment calendar 기반 |
| `T3` | analytics/RAG/BI | 의사결정 지연 | 수동 판단 fallback |

## 3.2 Dependency Graph

```text
LNG contract → upstream/feedgas → liquefaction → vessel → terminal slot/tank
→ power/CHP fuel → dispatch → electricity/heat settlement → cash

Renewable asset → weather → grid connection → metering → PPA/REC allocation
→ customer claim → billing/cash

BESS → battery/PCS/BMS → site substation → EMS/optimizer → ISO telemetry
→ bid/dispatch → settlement → degradation/warranty → project cash

LH2 plant → electricity/feed → liquefaction/storage → trailer → station
→ vehicle demand → delivered/sold/paid kg → cash
```

---
