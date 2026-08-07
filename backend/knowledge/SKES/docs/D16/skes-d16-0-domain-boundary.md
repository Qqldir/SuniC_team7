---
id: skes-d16-0-domain-boundary
title: Domain Boundary
summary: 외부 기술·벤더·솔루션을 E&S에 도입할 때 준수해야 할 검증 기준 20개(Hard Guardrail)와 근거 등급(Evidence State)을 정의한 D16 도메인의 경계·역할·규칙서.
tags: [d16, ecosystem, core-candidate, table, "xref:d01", "xref:d15", "xref:d06", "xref:d07"]
keywords: [벤더 검증, 기술 성숙도, 적용가능성 평가, Hard Guardrail, PoC·Pilot, OT 연결, 안전·사이버, Evidence State, BESS·수소, 배포 사례]
related: [ORG-SKI-ENS-CIC-000001]
priority: critical
domain: D16
section: 0
source: SK이노베이션E&S_D16_External_Technologies_Solutions_Companies_and_Startups.md
breadcrumb: ""
tokens: 1454
updated: 2026-08-06
---

> SK이노베이션 E&S · D16 외부 기술·솔루션·기업·스타트업

# SK이노베이션 E&S AI Knowledge Database

## D16. External Technologies, Solutions, Companies & Startups｜외부 기술·솔루션·기업·스타트업

**Version 1.0 / 기준일: 2026년 8월 6일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Technology namespace: `TECH-ENS-D16-*`
- Vendor namespace: `VEN-ENS-D16-*`
- Solution namespace: `SOL-ENS-D16-*`
- Evidence namespace: `EVD-ENS-D16-*`
- Fit namespace: `FIT-ENS-D16-*`
- Pain-point namespace: `PAIN-ENS-D16-*`
- O/I Seed namespace: `SEED-ENS-D16-*`
- PoC namespace: `POC-ENS-D16-*`
- Data-request namespace: `DR-ENS-D16-*`
- Source namespace: `SRC-ENS-D16-*`
- 상속 도메인: `D01~D15`; 특히 `D06 Process`, `D07 Assets`, `D08 Supply Chain`, `D10 Market`, `D11 Economics`, `D13 Governance`, `D14 Regulation`, `D15 Risk`
- 작성 목적: 외부 기술과 벤더를 단순 나열하지 않고 **검증사례–성숙도–E&S 적용점–통합조건–도입장벽–PoC–KPI**로 연결하여 D17의 O/I 과제 추천을 실행 가능한 수준으로 만든다.

---

# 0. Domain Boundary

## 0.1 D16의 역할

```text
D15 Failure Mode / Pain / Solution Need
→ External Technology Pattern
→ Vendor / Product / Service
→ External Deployment Evidence
→ Evidence Strength & Maturity
→ E&S Asset / Process Fit
→ Required Data / Integration / Safety-Cyber Gate
→ Build / Buy / Partner Decision
→ PoC KPI / Baseline / Stop Condition
→ D17 O/I Candidate
```

D16은 `시장에 존재하는 솔루션 DB`이면서 동시에 `E&S 적용 가능성 검증 DB`이다. 기술이 상용화됐다는 사실과 E&S에서 가치가 난다는 사실은 다르므로 둘을 분리한다.

## 0.2 Hard Guardrails

1. 벤더가 주장한 절감률·정확도·ROI를 SK이노베이션 E&S의 기대효과로 복사하지 않는다.
2. `Product capability`, `Vendor claim`, `Customer case`, `Independent standard/test`, `E&S internal validation`을 분리한다.
3. 외부 고객사 성공사례는 E&S의 성공을 보장하지 않는다.
4. `COMMERCIAL`, `DEPLOYED_CASE`, `PILOT`, `DEMO`, `R&D` 성숙도를 분리한다.
5. 제품 페이지가 존재한다고 실제 설치실적이 검증된 것으로 보지 않는다.
6. 고객사·벤더 공동자료는 실증근거로 사용할 수 있으나 독립 검증으로 승격하지 않는다.
7. Safety·SIS·ESD·가스차단·발전제어·BESS 보호계전·수소 emergency action은 AI가 독자 실행하지 않는다.
8. Market bidding·commodity trading·hedge·계약승인·규제신고 역시 Human Approval을 둔다.
9. OT 연결 솔루션은 `read-only shadow mode → isolated pilot → bounded write` 순서로 검증한다.
10. API·OPC UA·MQTT 지원 표기는 실제 E&S legacy system 호환성을 의미하지 않는다.
11. Cloud 가능과 Cloud 허용을 구분한다. 데이터 분류·국외이전·보안성 검토가 선행돼야 한다.
12. `OEM-specific`과 `OEM-agnostic`을 구분하고 vendor lock-in 비용을 평가한다.
13. BESS 최적화는 MW·MWh·SOH·warranty·degradation·market settlement를 동시에 검증한다.
14. 풍력 APM은 turbine OEM warranty 및 SCADA access 권한을 먼저 확인한다.
15. LNG digital twin은 process model의 물리적 타당성·calibration drift·operator override를 관리한다.
16. 액화수소 계측은 극저온 범위·방폭·SIL/기능안전·교정성·응답시간을 별도 검증한다.
17. CCS MMV는 storage capacity 추정과 regulatory-compliant monitoring을 동일시하지 않는다.
18. Cyber 제품의 보호 자산 수·탐지율 등 벤더 수치는 E&S 성능으로 변환하지 않는다.
19. 생성형 AI는 source freshness·effective date·access control·prompt injection·hallucination test를 통과해야 한다.
20. D16의 Fit/Score는 screening score이며 구매·투자·vendor endorsement가 아니다.

## 0.3 Evidence State

| State | 정의 | D17 사용원칙 |
|---|---|---|
| `E1_STANDARD` | 정부·표준·시험기관·시장운영기관 근거 | 안전/규제 Gate 근거 |
| `E2_CUSTOMER_CASE` | 고객사명과 적용내용이 공개된 벤더/고객 사례 | 실제 적용가능성 근거 |
| `E3_PRODUCT_CONFIRMED` | 공식 제품 기능만 확인 | 후보탐색 가능, 효과 확정 금지 |
| `E4_VENDOR_CLAIM` | 벤더가 효과수치 주장 | PoC baseline으로만 사용 금지 |
| `E5_HYPOTHESIS` | E&S 적용 분석가설 | 내부검증 전 사실 승격 금지 |
| `INT_VALIDATED` | E&S 내부 PoC/운영 데이터로 검증 | D17 승격 가능 |

---
