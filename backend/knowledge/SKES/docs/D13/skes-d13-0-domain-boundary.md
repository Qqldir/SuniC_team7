---
id: skes-d13-0-domain-boundary
title: Domain Boundary
summary: SK E&S의 JV·파트너십·계약을 법적·경제적 관계흐름으로 구조화하는 D13 도메인의 11가지 경계 규칙과 처리 범위를 정의한 문서다.
tags: [d13, contract, core-candidate, table, "xref:d01", "xref:d07", "xref:d08", "xref:d09"]
keywords: [JV·파트너십, 법적당사자·SPV, 의무·권리, 거버넌스·의사결정, LNG장기계약, 재생에너지·PPA, Hard Guardrails, Exit·Transfer, 도메인경계]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001]
priority: critical
domain: D13
section: 0
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 1607
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# SK이노베이션 E&S AI Knowledge Database

## D13. Joint Ventures, Partnerships, Contracts & Governance｜JV·파트너십·계약·거버넌스

**Version 1.0 / 기준일: 2026년 8월 6일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Agreement namespace: `AGR-ENS-D13-*`
- Party namespace: `PTY-ENS-D13-*`
- Governance namespace: `GOV-ENS-D13-*`
- Obligation namespace: `OBL-ENS-D13-*`
- Governance-risk namespace: `GRSK-ENS-D13-*`
- Pain-point namespace: `PAIN-ENS-D13-*`
- O/I Seed namespace: `SEED-ENS-D13-*`
- Data-request namespace: `DR-ENS-D13-*`
- Source namespace: `SRC-ENS-D13-*`
- 상속 도메인: `D01 Corporate Identity`, `D07 Footprint`, `D08 Supply Chain`, `D09 Customers`, `D11 Economics`, `D12 CAPEX/Funding`
- 작성 목적: E&S의 법인·JV·SPV·파트너·장기계약·사용권·의사결정권·Sponsor Support·Exit를 동일한 관계그래프로 연결하고 D17 O/I 과제로 전환

---

# 0. Domain Boundary

## 0.1 D13의 역할

D13은 파트너 이름이나 계약서 제목을 모으는 문서가 아니다. 하나의 사업관계를 아래의 법적·경제적 흐름으로 연결한다.

```text
Legal Party / Beneficial Group / SPV
→ MoU / JDA / Shareholders Agreement / TUA / LTA / PPA / EPC / LTSA / Finance
→ Right / Obligation / Condition Precedent / Milestone
→ Board / Reserved Matter / Veto / Capital Call / Sponsor Support
→ Asset·Data·Cash·Risk Attribution
→ Amendment / Waiver / Claim / Dispute / Change of Control
→ Transfer / Termination / Exit / Surviving Obligation
→ D17 Open-Innovation Opportunity
```

핵심 관리단위는 `계약 파일`이 아니라 **당사자–버전–조항–의무–권리–승인–이행증빙–경제적 귀속**이다.

## 0.2 Hard Guardrails

1. `SK그룹`, `SK이노베이션`, `E&S 사업/CIC`, `2024-11-01 이전 SK E&S`, `자회사`, `JV`, `Project SPV`를 별도 법적 Scope로 둔다.
2. 브랜드명이 같아도 실제 계약 당사자가 다르면 합치지 않는다. Barossa의 2026년 37.5% JV 당사자는 최신 Santos 자료의 `PRISM Energy International Australia`를 우선 저장하고 `formerly SK E&S` lineage를 보존한다.
3. 지분율은 Board 의석·Reserved Matter·Veto·Capital Call·보증·손익귀속을 자동 결정하지 않는다.
4. `MOU`, `LOI`, `developer designation`, `JDA`, `definitive agreement`, `FID`, `financial close`, `COD`, `운영`, `매각`을 분리한다.
5. `발표 총량`, `계약상 base quantity`, `option`, `nomination`, `firm call-off`, `actual lifting`, `settled quantity`를 동일 필드에 넣지 않는다.
6. TUA/LTA/PPA/시장참여권은 자산소유권이 아니다. Freeport 2.2Mt/y와 보령 3.5Mt/y 권리는 plant equity로 재분류하지 않는다.
7. JV 또는 사용권이 존재해도 raw data·derived data·AI model·cross-border transfer 권리가 자동 생기지 않는다.
8. 비공개 계약의 가격식·준거법·LD·indemnity·termination payment·deadlock·put/call은 추정하지 않는다.
9. `non-recourse PF`라는 공개표현을 sponsor support·completion support가 절대 없다는 의미로 확장하지 않는다.
10. 합병·사명변경·지분매각은 모든 계약·보증·IP·데이터·환경의무의 자동승계를 뜻하지 않는다.
11. 계약 AI 추출값은 원문 clause 위치와 Legal/Business reviewer 승인 전 `UNVERIFIED_EXTRACTION`이다.
12. D13 O/I 효과는 계약상 권리와 책임을 바꾸지 않으며, D17 채택 전 Legal·Security·Finance Gate를 통과해야 한다.

## 0.3 포함 범위

| 범위 | D13 처리 |
|---|---|
| Joint Operation/JV/SPV | 지분·운영사·이사회·Reserved Matter·추가출자·Exit |
| LNG 장기계약 | upstream right·LTA/TUA·운송·터미널·lifting rights |
| 재생에너지/PPA | 발전 SPV·공동개발·PF interface·offtake·정산·주민참여 |
| BESS/EV charging | 인수·자회사 지배구조·EPC/LTSA·utility/market 관계 |
| 수소 | JV·기술·충전소·정부/지자체·MOU·PF interface |
| 해외 개발 | consortium·developer designation·정부관계·EPC/PPA/data handover |
| 계약 운영 | amendment·waiver·claim·renewal·change of control·termination |
| O/I | contract intelligence·governance workflow·obligation monitoring·data-right controls |

## 0.4 다른 도메인의 원본과 경계

| 원본 | D13에서의 사용 |
|---|---|
| D01 legal entity | 당사자 canonical ID와 합병 lineage |
| D05 IP | 계약상 license·data right만 연결 |
| D07 asset/right | 어떤 JV·계약이 어느 자산을 지배/사용하는지 조인 |
| D08 supplier | 공급관계의 계약·warranty·LTSA clause 조인 |
| D09 customer | 수요·PPA의 commitment state를 계약으로 검증 |
| D11 economics | 조항이 margin/cash/KPI에 미치는 영향 |
| D12 finance | capital call·guarantee·PF·exit obligation 심화 |
| D14 regulation | 허가·보조금·clawback의 법적 원본 |
| D15 risk | 계약·JV 위험을 전사 risk register로 승격 |
| D16 external ecosystem | 파트너/벤더 후보 검증 |

---
