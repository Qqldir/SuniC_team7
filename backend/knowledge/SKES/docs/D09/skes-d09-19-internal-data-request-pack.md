---
id: skes-d09-19-internal-data-request-pack
title: Internal Data Request Pack
summary: "SK이노베이션 E&S의 내부 데이터 28개 요청별 ID, 담당자, 시간범위, 개인정보보호 레벨 카탈로그."
tags: [d09, customer, table]
keywords: [데이터요청, 카탈로그, REQ-ENS-D09, 개인정보보호, 오프테이크, 고객마스터, 계약, 수요예측, 시간범위, 데이터소유자]
related: [REQ-ENS-D09-001, REQ-ENS-D09-002, REQ-ENS-D09-003, REQ-ENS-D09-004, REQ-ENS-D09-005, REQ-ENS-D09-006, REQ-ENS-D09-007, REQ-ENS-D09-008, REQ-ENS-D09-009, REQ-ENS-D09-010, REQ-ENS-D09-011, REQ-ENS-D09-012, REQ-ENS-D09-013, REQ-ENS-D09-014, REQ-ENS-D09-015, REQ-ENS-D09-016, REQ-ENS-D09-017, REQ-ENS-D09-018, REQ-ENS-D09-019, REQ-ENS-D09-020, REQ-ENS-D09-021, REQ-ENS-D09-022, REQ-ENS-D09-023, REQ-ENS-D09-024]
priority: normal
domain: D09
section: 19
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 985
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 19. Internal Data Request Pack

| Request ID | Dataset | Minimum fields | Time range | Owner candidate | Privacy |
|---|---|---|---|---|---|
| `REQ-ENS-D09-001` | customer master | legal ID·segment·parent·status | current+history | sales ops | internal |
| `REQ-ENS-D09-002` | relationship master | type·owner·state·evidence | full history | strategy | internal |
| `REQ-ENS-D09-003` | contract header | term·volume basis·delivery | active+5y | legal/CLM | confidential |
| `REQ-ENS-D09-004` | obligation table | clause·KPI·deadline·remedy | active | legal/ops | confidential |
| `REQ-ENS-D09-005` | demand versions | forecast·nomination·firm·actual | 24m | S&OP | internal |
| `REQ-ENS-D09-006` | billing/settlement | meter·invoice·adjustment | 24m | finance | confidential |
| `REQ-ENS-D09-007` | PPA interval load | customer/site/15min | 12~24m | PPA ops | sensitive |
| `REQ-ENS-D09-008` | renewable generation | plant/15min·curtailment | 12~24m | renewable ops | internal |
| `REQ-ENS-D09-009` | REC/evidence | certificate·MWh·retirement | 24m | ESG | confidential |
| `REQ-ENS-D09-010` | city-gas CRM | pseudonymous account·Journey | 24m | city gas CX | personal |
| `REQ-ENS-D09-011` | AMI reads | service point·timestamp·quality | 24m | metering | sensitive |
| `REQ-ENS-D09-012` | contact-center cases | reason·channel·resolution | 12m | CX | personal |
| `REQ-ENS-D09-013` | emergency dispatch | symptom·priority·arrival | 24m | safety | sensitive |
| `REQ-ENS-D09-014` | field work order | asset·task·visit·result | 24m | operations | internal |
| `REQ-ENS-D09-015` | CHP demand | heat·power·weather·SLA | 24m | plant ops | internal |
| `REQ-ENS-D09-016` | KCE bid/award | market·product·price·MW | 12m | market ops | confidential |
| `REQ-ENS-D09-017` | KCE telemetry | SOC·power·availability | 12m | asset ops | restricted |
| `REQ-ENS-D09-018` | KCE settlement | award·meter·charge·true-up | 12m | finance | confidential |
| `REQ-ENS-D09-019` | EverCharge site | panel·EVSE·capacity·SLA | 12m | customer success | confidential |
| `REQ-ENS-D09-020` | charging sessions | masked driver·kWh·error | 12m | platform | personal |
| `REQ-ENS-D09-021` | fleet schedules | vehicle·route·departure SOC | 6m | customer/fleet | sensitive |
| `REQ-ENS-D09-022` | hydrogen station | tank·dispense·downtime | 12m | H2 ops | restricted |
| `REQ-ENS-D09-023` | trailer logistics | load·ETA·delivery·loss | 12m | logistics | internal |
| `REQ-ENS-D09-024` | vehicle rollout | ordered·delivered·active | history+plan | business dev | confidential |
| `REQ-ENS-D09-025` | customer credit | rating·AR·security | 24m | finance | restricted |
| `REQ-ENS-D09-026` | amendments | redline·effective date | 5y | legal | confidential |
| `REQ-ENS-D09-027` | access/consent | purpose·scope·retention | current | privacy | restricted |
| `REQ-ENS-D09-028` | PoC baseline | KPI·control group·cost | 12m | O/I PMO | internal |

## 19.1 Safe Sandbox Rule

- 원본 계약서·PII·시장입찰 데이터를 외부 벤더에 직접 제공하지 않는다.
- 가명화·필드 최소화·기간 제한·read-only sandbox를 기본으로 한다.
- 고객별 가격·신용·계약조항은 합성데이터로 기능검증 후 제한 접근한다.
- 안전·시장입찰·가격·계약 의사결정은 shadow mode에서 검증한다.
- PoC 종료 후 데이터 삭제·모델 보존·파생데이터 권리를 계약에 명시한다.

---
