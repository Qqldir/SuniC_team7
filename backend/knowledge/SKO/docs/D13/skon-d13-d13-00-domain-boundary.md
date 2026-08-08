---
id: skon-d13-d13-00-domain-boundary
title: Domain Boundary
summary: SK온 계약·JV·거버넌스 관리에서 D13 도메인의 범위를 정의하고 포함·제외 범위를 판정하는 원칙을 설명한다.
tags: [d13, contract, core-candidate, table, "xref:d12", "xref:d17", "xref:d00", "xref:d01"]
keywords: [계약 범위, JV 거버넌스, 파트너십 구조, 의무 귀속, Domain 경계, 포함 제외, MoU·JDA, Capital Call, IP 라이센싱, 자산 이전 규칙, 계약, 합작회사, 의사결정권, 경제귀속, MOU, 자본조달, 기술협력, Exit, 의무]
related: []
priority: critical
domain: D13
section: D13-00
source: SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md
breadcrumb: "SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure"
tokens: 1229
updated: 2026-08-03
---

> SK온 · D13 계약·JV·거버넌스·파트너십 · SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

# SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

- 문서 버전: **v1.0.1**
- 기준일: **2026-08-03 (KST)**
- 이전 완료 지점: `D12 CAPEX, Investment, Funding & Financial Structure v1.0`
- 작성 방식: **실무형 요약 DB** — 공개된 계약·공시 사실과 내부에서 확인해야 할 조항을 분리하고, 비공개 Reserved Matter·가격·해지·책임 조항을 추정하지 않음
- 상위 목적: 계약상 권리·의무와 JV의 법적·운영·경제적 귀속을 공장·고객·투자·IP·현금·Exit에 연결하고 D17 O/I 과제로 전달
- D00 통합검수: Domain-local Source/Entity ID를 보존하고 Canonical Alias는 D00 Crosswalk로 해석한다. MOU·계약·권리·의무·경제적 귀속은 서로 다른 Claim과 상태값으로 유지한다.

---

## D13-00 Domain Boundary

### 1. 도메인 정의

D13은 계약서 목록이나 파트너 명단이 아니다. 하나의 사업관계에 묶인 계약과 의사결정권을 다음 흐름으로 연결한다.

```text
Partner / Legal Entity / Beneficial Owner
→ MoU / JDA / License / Supply / JV / Financing / Incentive Agreement
→ Clause / Right / Obligation / Condition Precedent
→ Reserved Matter / Approval / Capital Call / Milestone / Call-off
→ Asset·Debt·Guarantee·IP·Data·Revenue·Cost Attribution
→ Performance / Change / Waiver / Claim / Dispute
→ Renewal / Transfer / Termination / Separation / Transition
→ D17 Open-Innovation Seed
```

핵심 관리단위는 `계약 파일`이 아니라 **법인·계약·조항·의무·증빙·경제적 귀속·의사결정 Event**다. 지분율, 이사회 의석, 운영통제, 회계 연결, 현금부담, 제품 구매의무는 서로 다른 사실로 보존한다.

### 2. 포함·제외 범위

| 포함 | 제외 또는 다른 도메인 원본 |
|---|---|
| JV 설립·운영·의사결정·Capital Call·Deadlock·Exit | 법인 기본정보·조직 원본은 D01 |
| 공급·개발·라이선스·MOU·JDA·Framework 계약 | 제품·기술 성능 원본은 D03~D05 |
| 자산·부채·보증·Credit·비용·수익의 계약상 귀속 | 투자금·자금조달 원본은 D12 |
| Forecast·Call-off·Option·우선협상권·고객수락 연결 | 고객·수주 원본은 D09 |
| Background/Foreground IP·Field of Use·Data Right | 특허·기술자산 원본은 D05 |
| 변경·면제·분쟁·해지·전환·사후의무 | 전사 Risk·품질·Recall 원본은 D15 |
| 계약지능·JV Governance O/I 후보 | 외부 솔루션 회사 원장은 D16 |

### 3. 판정 원칙

1. `50:50 지분`만으로 공동통제·동일 자본부담·동일 보증·동일 손익귀속을 확정하지 않는다.
2. MoU·의향서·우선협상권·Option은 Definitive Agreement·Firm Call-off·PO와 분리한다.
3. 발표된 총량·기간은 Take-or-pay·최소구매·연도별 확정수요를 뜻하지 않는다.
4. 계약 원문이 비공개면 가격식·Reserved Matter·Deadlock·Default Remedy·해지보상은 `NOT_DISCLOSED`로 둔다.
5. 계약의 법적 당사자와 상위 그룹·브랜드·운영회사·보증인을 분리한다.
6. 자산 이전은 관련 부채·보증·정부지원·고용·환경·품질·IP 의무의 자동이전을 뜻하지 않는다.
7. 기술협력은 Background IP, Foreground IP, 개선기술, 데이터, Field of Use, 상업생산권을 별도 저장한다.
8. Amendment·Side Letter·Waiver·회의록·PO가 Master Agreement의 실질을 바꿀 수 있으므로 Version Lineage를 유지한다.
9. AI 추출값은 원문 Clause와 Reviewer 승인 없이는 법적 의무로 승격하지 않는다.
10. D13의 우선순위·점수는 D17 선별용 분석값이며 SK온 공식 KPI나 법률의견이 아니다.

---
