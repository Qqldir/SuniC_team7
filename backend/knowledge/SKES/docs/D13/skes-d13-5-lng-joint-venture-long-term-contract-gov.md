---
id: skes-d13-5-lng-joint-venture-long-term-contract-gov
title: LNG Joint Venture & Long-term Contract Governance
summary: SK E&S의 LNG 프로젝트별 지분·계약 권리의무·거버넌스를 규정하고 소유권·운영권·사용권의 법적 경계를 명확히 하는 문서
tags: [d13, contract, table]
keywords: [Barossa, PRISM, 지분구조, JOA, TUA, Freeport, LTA, Darwin, Boryeong, 운영권]
related: []
priority: normal
domain: D13
section: 5
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 1285
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# 5. LNG Joint Venture & Long-term Contract Governance

## 5.1 Barossa Joint Operation

2026년 7월 Santos 공식자료 기준 Barossa는 Santos 50%·operator, PRISM Energy International Australia 37.5%, JERA Australia 12.5% 구조다. Santos는 2025 자료에서 PRISM을 `formerly SK E&S`로 설명했다. 따라서 D13은 과거 SK E&S 브랜드를 검색 alias로 남기되 최신 JV legal-party field에는 PRISM을 저장한다. `[SRC-ENS-D13-0007~0011]`

| Layer | 공개 확인 | 내부 확인 필요 |
|---|---|---|
| Ownership | 50/37.5/12.5 | direct legal holder registration |
| Operator | Santos | operator delegation limits |
| Production | 2026 operating | annual work program/budget approval |
| Lifting | LNG/condensate lifting | nomination·imbalance·under/overlift |
| Cash call | JV investment exists | call schedule·default remedy·security |
| Governance | JV partners | board/operating committee·reserved matters |
| Data | operator produces operating data | shareholder raw/derived/model rights |
| CCS | future/development linkage | JOA scope·new project consent·liability |

### Barossa decision graph

```text
Operator plan
→ JV work program / budget
→ partner approval thresholds
→ cash call / procurement
→ production / lifting schedule
→ cargo + condensate allocation
→ revenue / cost allocation
→ incident / claim / insurance
→ amendment / debottleneck / CCS decision
```

## 5.2 Darwin LNG Boundary

Darwin LNG는 Barossa와 같은 지분구조로 단순 복제하지 않는다. Santos의 공개자료에는 Darwin LNG 참여자와 지분이 별도로 제시되며, 과거 SK E&S는 25% 이해관계를 확보했다. Barossa upstream 37.5%와 Darwin LNG 25%는 서로 다른 interest다. `[SRC-ENS-D13-0010]`

`Barossa interest × production ≠ Darwin plant ownership × LNG output ≠ E&S actual lifting`을 강제 규칙으로 둔다.

## 5.3 Freeport LTA

Freeport는 2013 SK E&S LNG, LLC와 20년 LTA를 체결했고 base quantity 2.2Mt/y, use-or-pay tolling 구조가 공개됐다. Train 3 상업화의 장기수요 기반이었지만, D13에서는 이를 다음과 같이 분해한다. `[SRC-ENS-D13-0012~0014]`

| Right/Obligation | 공개 상태 | 내부 확인 |
|---|---|---|
| Liquefaction right | 2.2Mt/y base | daily/annual scheduling rights |
| Term | 20 years | 정확한 effective/expiry |
| Payment | use-or-pay | fixed/variable fee·credit |
| Feedgas | customer-supplied model | pipeline capacity·quality |
| Outage | plant dependency | planned/unplanned allocation |
| Cargo | loading access | slot window·demurrage |
| Parent support | historical guarantee disclosed | post-merger guarantor/succession |
| Assignment | not public | CoC/affiliate assignment consent |

## 5.4 Boryeong Sell-and-Retain-Right

보령은 D13의 대표적인 `equity exit ≠ contract exit` 사례다. 2025 지분매각 후 E&S는 3.5Mt/y 터미널 사용권을 유지한다. 따라서 법적 그래프에서 former equity ownership edge는 종료하고 TUA edge는 유지한다. `[SRC-ENS-D13-0015~0017]`

```text
Former equity interest --ENDED--> Boryeong LNG Terminal
E&S contractual TUA --ACTIVE--> 3.5Mt/y usage right
TUA --NOT_EQUAL_TO--> asset ownership
TUA --REQUIRES--> slot / fee / outage / data / nomination clauses
```

## 5.5 LNG Contract Control Questions

1. Barossa PRISM의 최신 법인등록명·지분 직접보유 주체는 무엇인가.
2. Barossa JOA에서 annual budget·major modification·shutdown·CCS의 승인 threshold는 무엇인가.
3. LNG와 condensate의 under/overlift 및 balancing 규칙은 무엇인가.
4. Darwin LNG 지분·processing agreement·Barossa processing entitlement는 어떻게 연결되는가.
5. Freeport LTA의 정확한 effective/expiry와 use-or-pay fee 구조는 무엇인가.
6. Freeport outage 때 fee relief·make-up right·alternative cargo 조건은 무엇인가.
7. SK E&S LNG LLC 관련 보증은 2024 합병 후 누가 법적으로 부담하는가.
8. 보령 TUA의 남은 term·capacity charge·slot·force majeure는 무엇인가.
9. 보령 지분매각 계약의 surviving indemnity·tax·environmental liability는 무엇인가.
10. LNG JV·TUA에서 AI/analytics를 위한 raw historian/cargo data 접근권은 누구에게 있는가.

---
