---
id: skes-d17-d17-03-100-point-pre-screening-unified-hard-gat
title: 100-Point Pre-screening & Unified Hard Gates
summary: "오픈이노베이션 AI 과제의 100점 평가표와 Finance, Contract, Safety 등 6개 필수게이트를 통한 적격성 심사 기준을 정의한다."
tags: [d17, oi-portfolio, table, "xref:d12", "xref:d16"]
keywords: [평가표, 심사기준, PoC, Tier, 오픈이노베이션, 필수게이트, Finance, Contract, 데이터준비도, Compliance]
related: []
priority: normal
domain: D17
section: D17-03
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 1020
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-03 100-Point Pre-screening & Unified Hard Gates

## 1. 100점 사전심사

| 평가축 | 배점 | E&S 질문 |
|---|---:|---|
| Strategic Relevance | 15 | LNG·Power·City Gas·Renewable·BESS·H2·CCS의 핵심 경영문제를 직접 바꾸는가? |
| Quantified Value / Risk | 20 | KRW cash, KRW/MWh, GJ, downtime, demurrage, kg-H2, tCO2, 안전 Barrier 등으로 측정 가능한가? |
| Evidence & Problem Proof | 15 | Failure/Pain·분모·기간·Source·원인확신도가 있는가? |
| Data Readiness | 10 | Historian·SCADA·CMMS·Contract·Market·Finance 데이터와 권리가 있는가? |
| External Capability | 10 | 산업 실증·표준·기술근거가 있고 E&S Fit이 설명되는가? |
| Bounded PoC Feasibility | 10 | 6~24주 또는 합리적 운영주기 내 Shadow/Replay가 가능한가? |
| Scale & Cross-domain Reuse | 10 | 다자산·다자회사·다지역으로 확장 가능한가? |
| Governance & Reversibility | 10 | Owner·Human Approval·Rollback·Exit·Data/IP 통제가 명확한가? |
| **합계** | **100** | 공개자료 기반 점수는 승인점수가 아닌 사전심사값 |

## 2. Tier

| Tier | 점수 | 처리 |
|---|---:|---|
| `P0` | 85~100 | G0/G1 우선 착수. 내부 Evidence 없이는 Live/Scale 금지 |
| `P1` | 75~84 | Data·권리·Sponsor 선행조건을 닫은 뒤 PoC |
| `P2` | 60~74 | Option·기술실사·Observe 또는 좁은 연구형 PoC |
| `HOLD/NO-GO` | 0~59 또는 Hard Gate 위반 | 이번 Cycle 중단·재정의 |

## 3. Unified Hard Gate — D12~D16 통합

다음 중 하나라도 `FAIL`이면 점수와 무관하게 `HOLD/NO-GO`다.

### G-FIN Finance

1. Baseline과 분모가 없다.
2. 총 Project Value와 E&S net cash exposure가 분리되지 않는다.
3. Partner·Debt·Grant·Tax credit·Working capital·Exit cost가 중복/누락된다.
4. Vendor ROI만 있고 Finance가 검증할 Counterfactual이 없다.

### G-CON Contract / JV / Data Right

1. 법적 당사자·데이터 Owner·사용권이 `UNKNOWN` 상태다.
2. JV Reserved Matter·Lender consent·OEM warranty를 우회해야 한다.
3. 외부 Provider가 핵심 운영데이터를 무제한 학습·재사용하거나 Export/삭제를 거부한다.

### G-COM Compliance / Tax

1. 적용 법인·자산·관할·Rule Version·Effective Date가 없다.
2. AI가 세무·규제 적격성을 최종 판정하거나 규제기관 제출을 무검토 자동화한다.
3. 인센티브 최고율을 실제 수령액으로 표시한다.

### G-SHE Safety / OT

1. Safety Owner가 없거나 SIS/ESD/가스차단/보호계전의 독립성을 약화한다.
2. Shadow 검증 없이 OT Write 권한을 요구한다.
3. 고위험 False Negative/False Positive 허용치와 Stop Condition이 없다.

### G-CYB Cyber / AI

1. OT Asset/Zone/Remote Access 경계가 불명확하다.
2. Source-locked evidence·audit log·rollback·model version이 없다.
3. Prompt/Model이 계약·영업비밀·개인정보를 외부 학습에 노출한다.

### G-OI O/I Quality

1. Solution-first이며 재현된 Problem이 없다.
2. 책임 Owner/Operator가 없다.
3. 기존 시스템·과제와 Dedupe하지 않았다.
4. PoC 종료·Scale·Exit 기준이 없다.

---
