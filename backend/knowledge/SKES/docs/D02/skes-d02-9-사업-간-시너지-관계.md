---
id: skes-d02-9-사업-간-시너지-관계
title: 사업 간 시너지 관계
summary: "LNG, 발전, 도시가스, 재생에너지, 수소 등 사업 간 시너지 관계와 각 사업의 성숙도, 현금창출 안정성, 재무 실적을 정리한 포트폴리오 매트릭스"
tags: [d02, business, schema, table, "xref:d17"]
keywords: [LNG Upstream, 도시가스, Renewable, 수소, ESS, VPP, 포트폴리오, 성숙도, 현금창출, 통합 운영]
related: [SRC-ENS-D02-0007, SRC-ENS-D02-0008]
priority: normal
domain: D02
section: 9
source: SK이노베이션E&S_D02_Business_Portfolio_v2_보강본.md
breadcrumb: ""
tokens: 1230
updated: 2026-08-06
---

> SK이노베이션 E&S · D02 사업 포트폴리오

# 9. 사업 간 시너지 관계

| From | 관계 | To | 의미 |
|---|---|---|---|
| LNG Upstream | 원료 공급 | Power / City Gas | 조달 안정성과 마진 연결 |
| LNG Midstream | 운송·저장 | Power / City Gas | 수요와 재고의 통합운영 |
| Gas Power | 조정가능 전원 | Renewable | 변동성 대응 |
| Renewable | 전력 공급 | Green Hydrogen | 수전해 전력원 |
| LNG + CCS | 원료·탄소저감 | Blue Hydrogen | 기존 자산 활용 |
| ESS / VPP / DERMS | 유연성 제공 | Renewable / Grid | 변동성·피크·계통 대응 |
| City Gas Network | 고객·현장 기반 | Energy Solution | 분산에너지·고객서비스 확장 |
| SK On interface | 배터리 기술 | ESS | 합병 시너지 후보, 거래·역할은 별도 검증 |

## 9.1 통합 O/I 문제정의

1. **통합 수요·재고·발전계획:** LNG 도입, 터미널 재고, 발전소 정비, 도시가스 수요를 하나의 계획계로 연결.
2. **설비 신뢰성:** 가스전부터 발전·배관·풍력·ESS·수소까지 위험기반 정비체계를 통합.
3. **에너지 효율:** 액화·기화·발전·수소액화·ESS 손실을 자산별로 측정하고 최적화.
4. **안전과 배출:** methane, CO2, 수소누출, 배터리 화재를 센서·AI·MRV로 통합 감시.
5. **Power Optimization:** 발전, 재생에너지, ESS, VPP, PPA를 가격·수요·계통제약에 맞춰 운영.

---

# 10. 포트폴리오 성숙도와 우선순위

| 사업 | 성숙도 | 현금창출 안정성 추정 | 디지털·외부기술 적용성 | D17 Seed 우선도 |
|---|---|---|---|---|
| City Gas | Mature | 높음·계절성 | 높음 | P0 |
| Gas Power / CHP | Mature | 중상·시장연동 | 높음 | P0 |
| LNG Midstream | Mature / Expanding | 중상·계약연동 | 높음 | P0 |
| LNG Upstream | Operating / Developing | 가격·생산연동 | 중상 | P1 |
| Renewable | Growth | 계약·시장연동 | 높음 | P0 |
| Energy Solution | Growth | 모델별 상이 | 매우 높음 | P0 |
| Liquefied Hydrogen | Early Commercial | 수요확대 필요 | 높음 | P1 |
| Blue/Green Hydrogen | Development | 미확정 | 중상 | P2 |
| CCS | Development | 미확정 | 높음 | P1 |

`현금창출 안정성`은 공개 사업구조에 기반한 정성분류이며 내부 회계실적이 아니다.

---

# 11. 포트폴리오 재무 경계

## 11.1 공개 분기 실적

| Reporting Period | E&S 매출 | E&S 영업이익 | 주요 설명 | Source |
|---|---:|---:|---|---|
| 2026 Q1 | 3.7조 원 | 2,832억 원 | 동절기 도시가스 판매 증가, SMP 상승 | `SRC-ENS-D02-0007` |
| 2026 Q2 | 2.60조 원 | 1,059억 원 | 도시가스 비수기, 발전소 계획정비 | `SRC-ENS-D02-0008` |

### 사용 규칙

- 위 실적은 SK이노베이션이 발표한 `SK Innovation E&S` 사업 단위 전체다.
- LNG·발전·도시가스·재생에너지·수소·솔루션별로 임의 배분하지 않는다.
- 합병 전 SK E&S 연결실적과 단순 시계열 비교하지 않는다.
- 수익성 상세 분석은 D11에서 원가·계절성·가격지표와 연결한다.

---

# 12. 핵심 Entity·Relation 레코드

```yaml
- subject: ORG-SKI-ENS-CIC-000001
  relation: OPERATES_PORTFOLIO
  object: BUS-ENS-01
  object_name: LNG_VALUE_CHAIN
- subject: BUS-ENS-01
  relation: FEEDS_FUEL_TO
  object: BUS-ENS-03
  object_name: POWER_AND_CHP
- subject: BUS-ENS-01
  relation: FEEDS_GAS_TO
  object: BUS-ENS-02
  object_name: CITY_GAS
- subject: BUS-ENS-04
  relation: CONNECTED_BY_FLEXIBILITY
  object: BUS-ENS-06
  object_name: ENERGY_SOLUTION
- subject: BUS-ENS-01
  relation: ENABLES_FEEDSTOCK
  object: BUS-ENS-05
  object_name: HYDROGEN
- subject: BUS-ENS-07
  relation: DECARBONIZES_CLAIMED
  object: BUS-ENS-01
  object_name: LNG_VALUE_CHAIN
  status: plan_requires_verification
```

---
