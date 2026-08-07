---
id: skon-d16-d16-00-domain-boundary
title: Domain Boundary
summary: "SK온의 외부 기술·스타트업·벤더 평가 시 의사결정 흐름, 포함/제외 범위, 판정 원칙을 정의하는 D16 도메인의 경계 설정 기준"
tags: [d16, ecosystem, core-candidate, table, "xref:d15", "xref:d01", "xref:d00", "xref:d17"]
keywords: [외부솔루션, 스타트업, 벤더, PoC, 오픈이노베이션, 기술협력, MOU, Vendor Risk, Capability, 의사결정, 기술검증, Evidence Level, 협력사]
related: []
priority: critical
domain: D16
section: D16-00
source: SK온_D16_External_Solutions_Startups_Vendors_Open_Innovation_Ecosystem.md
breadcrumb: "SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem"
tokens: 1285
updated: 2026-08-03
---

> SK온 · D16 외부 솔루션·스타트업·벤더 생태계 · SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem

# SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem

- 문서 버전: **v1.0.1**
- 기준일: **2026-08-03 (KST)**
- 이전 완료 지점: `D15 Enterprise Risk, Quality, Safety & Resilience v1.0`
- 작성 방식: **실무형 외부역량 DB** — 제품 홍보, MOU, PoC, 생산 적용, 다사업장 확산을 분리하고 공개되지 않은 가격·계약조건·정확도·재무건전성을 추정하지 않음
- 상위 목적: D01~D15에서 확인된 Pain Point를 외부 기술·기업·레퍼런스·PoC 설계와 연결해 D17의 실행 가능한 O/I 과제 추천에 투입
- D00 통합검수: Domain-local Source/Entity ID를 보존하고 Canonical Alias는 D00 Crosswalk로 해석한다. Provider Claim·MOU·PoC·상용운영·다사업장 확산의 Evidence Level을 동일 실적으로 합치지 않는다.

---

## D16-00 Domain Boundary

### 1. 도메인 정의

D16은 스타트업·벤더 이름을 많이 나열하는 문서가 아니다. 다음 의사결정 흐름을 만드는 도메인이다.

```text
Verified Internal Pain Point from D01–D15
→ Required Capability and Non-negotiable Control
→ External Solution / Technology / Partner Universe
→ Evidence Level and Battery-domain Reference
→ Fit, Gap, Conflict, IP, Data, Cyber and Vendor Risk
→ Build / Buy / Partner / License / Invest / Observe Decision
→ Bounded PoC with Baseline, Control Group and Exit Criteria
→ Scale / Integrate / Re-negotiate / Stop
→ D17 Open-Innovation Task
```

핵심 관리단위는 `회사명`이 아니라 **특정 Pain Point를 해결하는 데 필요한 Capability, 이를 제공할 수 있다는 공개 증거, SK온 환경에서 검증할 가설, 접근해야 할 데이터·설비·IP, 실패·중단 조건을 함께 가진 후보 레코드**다.

### 2. 포함·제외 범위

| 포함 | 제외 또는 다른 도메인 원본 |
|---|---|
| 기존 SK온 기술협력·MOU·검증 생태계의 관계상태 | 계약상 권리·의무 원본은 D13 |
| 제조·품질·배터리 분석·DPP·공급망·OT·CLM·CAPEX 외부 솔루션 | SK온 공정·설비·데이터 원본은 D06·D07 |
| 차세대 배터리·재활용·순환경제 전략 탐색기업 | 핵심 기술 Benchmark 원본은 D04·D05 |
| Evidence Level, Partner Fit, Vendor Risk, PoC Gate | 개별 회사의 비공개 재무·가격·계약조건 추정 금지 |
| Build–Buy–Partner–License–Invest–Observe 판정 | D17 최종 과제 Portfolio 결정은 D17 |
| 외부사례에서 재사용 가능한 운영 Pattern | 경쟁사 사례의 성과를 SK온 성과로 복사 금지 |

### 3. 판정 원칙

1. `제품 존재`, `파트너십 발표`, `PoC`, `생산 적용`, `다사업장 확산`을 분리한다.
2. 공급사·고객사가 발표한 성과는 `COMPANY_REPORTED`로 표시하고 독립 검증값처럼 사용하지 않는다.
3. 경쟁사 적용사례는 Capability 증거일 뿐 SK온의 도입 가능성·가격·배타성·ROI를 증명하지 않는다.
4. SK그룹 계열사의 투자·JV·협력을 SK온의 직접 계약이나 사용권으로 간주하지 않는다.
5. 스타트업의 투자유치액·기업가치·직원수만으로 기술성숙도나 계속기업 능력을 판정하지 않는다.
6. SaaS Demo의 정확도를 실제 Line·Cell·ESS 성능으로 확대하지 않는다.
7. 공정 Recipe, 고객 Telemetry, 계약 Clause, 원산지 증빙, BMS·OT 접근권한은 PoC 이전에 목적·보관·파기·학습금지·재사용 범위를 정한다.
8. 안전·품질·출하·리콜·세금신고·통관·법률판단·설비제어는 외부 AI에 자율 위임하지 않는다.
9. 단일 공급사 Lock-in을 피하기 위해 Data Model·API·Feature·Label·Decision Log의 이식성을 검증한다.
10. D16의 후보와 점수는 D17 선별용이며 구매·투자·제휴 승인을 의미하지 않는다.

---
