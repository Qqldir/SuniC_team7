---
id: skes-d04-12-owned-capability-registry
title: Owned Capability Registry
summary: "SK이노베이션 E&S의 12개 핵심 역량을 상태·우선순위별로 정리하고, 기술 재사용·자체개발·외부구매·협력 판단 기준을 제시하는 문서"
tags: [d04, technology, schema, table]
keywords: [기술 포트폴리오, 기술 재사용, LNG·가스·ESS·EV, 차별화 기술, Make-Buy-Partner, 데이터 권리, 사업 단계별 기술, RBMS·DERMS·VPP]
related: [CAP-ENS-001, CAP-ENS-002, CAP-ENS-003, CAP-ENS-004, CAP-ENS-005, CAP-ENS-006, CAP-ENS-007, CAP-ENS-008, CAP-ENS-009, CAP-ENS-010, CAP-ENS-011, CAP-ENS-012]
priority: normal
domain: D04
section: 12
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: Part 2. 대표기업 기술체계 심층 확장
tokens: 734
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · Part 2. 대표기업 기술체계 심층 확장

## 12. Owned Capability Registry

### 12.1 Capability Status

| CAP ID | 공개 확인 역량 | 보유/관계 | 기술 | 재사용 우선순위 | 제한 |
|---|---|---|---|---|---|
| `CAP-ENS-001` | LNG integrated value chain operations | E&S 직접 사업 | 수급·선박·터미널·발전 | P0 | 통합 SW 범위 미공개 |
| `CAP-ENS-002` | City-gas RBMS | E&S 도시가스 | 배관 위험관리 | P0 | 변수·성과 미공개 |
| `CAP-ENS-003` | Drone safety inspection | E&S 도시가스 | 원격 영상점검 | P0 | 적용범위 미공개 |
| `CAP-ENS-004` | Direct PPA commercial operation | E&S | 계약·공급·정산 | P0 | 자동화수준 미공개 |
| `CAP-ENS-005` | Incheon liquid-hydrogen operations | E&S | 정제·액화·저장·출하 | P0 | 실제 KPI 미공개 |
| `CAP-ENS-006` | MarketCapture | KCE | ESS AI 입찰·최적화 | P0 | IP·API·타시장성 미공개 |
| `CAP-ENS-007` | Grid ESS development/operation | KCE | BESS·시장·O&M | P0 | 자산별 기술구성 미공개 |
| `CAP-ENS-008` | SmartPower dynamic load | EverCharge | EV 충전부하 제어 | P0 | 국내표준 적합성 미확인 |
| `CAP-ENS-009` | Mesh charging network | EverCharge | 지하/주차 통신 | P0 | 네트워크·보안 상세 미공개 |
| `CAP-ENS-010` | EVSE turnkey lifecycle | EverCharge | 제조·설치·운영·A/S | P0 | E&S 국내 적용범위 미확인 |
| `CAP-ENS-011` | Distribution network base | Ensolve | DERMS·ESS·VPP 기반 | P1 | 상용 DERMS 상태 미확인 |
| `CAP-ENS-012` | Parking network interface | iPARKING | 주차·충전 고객접점 | P0 | 데이터/운영주체 미확인 |

### 12.2 Build–Buy–Partner Rule

```yaml
decision_rule:
  reuse_owned:
    when: disclosed capability meets 70_percent_plus requirements and data rights exist
    examples: KCE bidding EverCharge load management RBMS
  build:
    when: E&S proprietary operating data and workflow create durable differentiation
    examples: LNG integrated decision citygas risk PPA settlement lineage
  buy:
    when: function is standardized and not differentiating
    examples: OCR base engine generic CMMS connector weather data
  partner:
    when: safety-critical domain expertise or specialized hardware is required
    examples: LH2 rotating equipment offshore inspection CCS MRV
  research:
    when: business stage or data readiness is below PoC threshold
    examples: blue hydrogen large-scale CCS early VPP
```
