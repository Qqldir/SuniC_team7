---
id: skes-d14-0-domain-boundary
title: Domain Boundary
summary: 규제 정책과 인센티브를 E&S 자산에 올바르게 연결하고 중복·오류를 피하기 위한 12가지 관리 원칙과 규제 상태 분류 기준
tags: [d14, policy, core-candidate, schema, table, "xref:d01", "xref:d06", "xref:d07", "xref:d09"]
keywords: [Hard Guardrails, 규제 상태 분류, 자산 매핑, 중복 계산, compliance, 허가 단계, 규제 의무, 인센티브, regulatory mapping, 규제 오류]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001]
priority: critical
domain: D14
section: 0
source: SK이노베이션E&S_D14_Policy_Regulation_Incentives_and_Compliance.md
breadcrumb: ""
tokens: 1759
updated: 2026-08-06
---

> SK이노베이션 E&S · D14 정책·규제·인센티브·컴플라이언스

# SK이노베이션 E&S AI Knowledge Database

## D14. Policy, Regulation, Incentives & Compliance｜정책·규제·인센티브·컴플라이언스

**Version 1.0 / 기준일: 2026년 8월 6일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Regulation namespace: `REG-ENS-D14-*`
- Obligation namespace: `OBL-ENS-D14-*`
- Incentive namespace: `INC-ENS-D14-*`
- Permit namespace: `PER-ENS-D14-*`
- Policy-event namespace: `EVT-ENS-D14-*`
- Compliance-risk namespace: `CRSK-ENS-D14-*`
- Pain-point namespace: `PAIN-ENS-D14-*`
- O/I Seed namespace: `SEED-ENS-D14-*`
- Data-request namespace: `DR-ENS-D14-*`
- Source namespace: `SRC-ENS-D14-*`
- 상속 도메인: `D01 Corporate Identity`, `D06 Process`, `D07 Footprint`, `D09 Customers`, `D10 Market`, `D11 Economics`, `D12 CAPEX`, `D13 Contracts/Governance`
- 작성 목적: E&S의 사업·자산·계약을 관할별 법령·시장규칙·허가·인센티브·보고의무와 연결하고, 규제변화가 원가·수익·가동·투자·데이터 사용에 미치는 영향을 D17 O/I 과제로 전환

---

# 0. Domain Boundary

## 0.1 D14의 역할

D14는 법령 제목을 모으는 문서가 아니다. 규제의 **시점·관할·적용주체·의무·증빙·경제적 효과**를 실제 E&S 자산과 연결한다.

```text
Jurisdiction / Regulator / Market Operator
→ Law / Rule / Permit / Auction / Tax Credit / Certification
→ Applicability Test
→ Obligation / Eligibility / Filing / Measurement / Deadline
→ Asset / Contract / Legal Entity / SPV
→ Evidence / Approval / Audit Trail
→ Revenue / Cost / CAPEX / Dispatch / Schedule Impact
→ Breach / Clawback / Penalty / Permit Delay / Lost Incentive
→ D17 Open-Innovation Opportunity
```

핵심 관리단위는 `법령명`이 아니라 **규칙 버전–효력일–적용조건–대상 자산–행동–기한–증빙–경제효과**다.

## 0.2 Hard Guardrails

1. `시행 중`, `공포됐으나 시행 전`, `입법예고/제안`, `정책목표`, `입찰공고`, `취소`, `종료`를 동일한 상태로 저장하지 않는다.
2. 기준일 2026-08-06 이후 시행 예정인 법은 현재 의무로 계산하지 않는다.
3. 정책목표·정부 발표를 허가 또는 보조금 수급 확정으로 해석하지 않는다.
4. 세액공제의 법정 최고율을 KCE 프로젝트의 실제 수령액으로 기록하지 않는다. 프로젝트별 placed-in-service, PWA, domestic content, PFE, basis, transfer 조건을 확인한다.
5. 미국 연방 인센티브와 New York/Texas/California 주·시장 제도를 합치지 않는다.
6. 한국 K-ETS의 발전부문 유상할당 비율은 발전 외 부문과 분리한다.
7. 청정수소 인증, 청정수소발전시장 낙찰, 실제 수소 판매량은 서로 다른 상태다.
8. 2025년 청정수소발전시장 경쟁입찰은 취소 사실을 보존하며 수주·매출 pipeline으로 계산하지 않는다.
9. 호주 Safeguard Mechanism의 facility baseline과 E&S의 경제적 지분율을 자동 곱하지 않는다. compliance entity는 operational control 기준으로 확인한다.
10. Vietnam PDP VIII 포함·개발자 선정은 투자허가·PPA·환경허가·COD를 의미하지 않는다.
11. 허가의 `신청`, `접수`, `승인`, `조건부 승인`, `조건 이행`, `운영승인`, `갱신`을 분리한다.
12. 재생에너지 인증서·PPA 환경가치를 중복 주장하지 않도록 attribute ownership을 계약별로 확인한다.
13. BESS 시장참여 자격은 계통연계·Resource registration·QSE/market participation·telemetry 요건을 별개로 관리한다.
14. AI/OI가 규제보고를 자동 생성해도 human sign-off와 원천증빙 lineage가 없으면 공식 제출본으로 취급하지 않는다.
15. 법률·세무 판단이 필요한 항목은 `LEGAL/TAX REVIEW REQUIRED`; 본 DB는 사실·의무·검증 포인트를 구조화하는 지식베이스다.

## 0.3 Regulation State Vocabulary

```yaml
regulatory_state:
  IN_FORCE: 기준일 현재 효력 있음
  ENACTED_FUTURE: 공포/확정됐으나 기준일 이후 시행
  AUCTION_OPEN: 입찰 또는 신청 접수 중
  AWARD_PENDING: 접수 종료, 결과/계약 미확정
  CANCELLED: 공고·입찰이 취소됨
  EXPIRED: 법정 또는 프로그램 기한 종료
  PROPOSED: 입법예고·초안·협의 단계
  POLICY_TARGET: 법적 개별 권리가 아닌 정책목표
  PROJECT_SPECIFIC: 특정 허가/협약/처분에만 적용
  INTERNAL_REQUIRED: 공개자료만으로 적용여부 확정 불가
```

## 0.4 Jurisdiction Map

| 관할 | 주요 노출 | D07 연결 |
|---|---|---|
| Korea | LNG 발전·CHP, 도시가스, PPA·재생, 해상풍력, 액화수소, 분산에너지 | `AST-ENS-D07-0014~0016`, `0020~0053`, `0071~0077` |
| United States—Federal | KCE BESS, EverCharge, Woodford/Freeport interface, 세액공제·전력시장 | `0006~0007`, `0054~0070` |
| New York | KCE BESS, NYISO, NYSERDA storage program | `0056~0057`, `0065` |
| Texas | KCE ERCOT BESS | `0058~0064` |
| California | EverCharge EV charging | `0066~0070` |
| Australia | Barossa/Darwin LNG, Safeguard Mechanism | `0001~0005` |
| Timor-Leste/Australia cross-border | Bayu-Undan CCS concept | `0005`, `0078` |
| Vietnam | 운영 재생 + Quynh Lap LNG-to-power | `0018~0019`, `0028`, `0047~0048` |
| China/Indonesia/global shipping | Ganyu usage plan, Tangguh, LNG shipping | `0017`, `0008~0013` |

---
