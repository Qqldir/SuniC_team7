---
id: skes-d12-1-evidence-data-quality-policy
title: Evidence & Data Quality Policy
summary: 증거 출처의 신뢰도 등급과 투자금액의 집행 단계별 상태를 분류하는 데이터 품질 기준
tags: [d12, capex, core-candidate, schema, table]
keywords: [증거등급, 출처신뢰도, Claim Status, 금액상태, 집행단계, 근거자료, 신뢰도, COD, PF, 품질기준]
related: []
priority: critical
domain: D12
section: 1
source: SK이노베이션E&S_D12_CAPEX_Investment_Funding_and_Financial_Structure.md
breadcrumb: ""
tokens: 471
updated: 2026-08-06
---

> SK이노베이션 E&S · D12 CAPEX·투자·자금조달

# 1. Evidence & Data Quality Policy

## 1.1 Evidence Tier

| Tier | 정의 | 사용 |
|---|---|---|
| `E1A` | 감사/사업보고서·거래소·정부·규제기관 | 법인·부채·보증·공시·정책 |
| `E1B` | SK Innovation/E&S·자회사 공식자료 | 투자·지분·COD·전략 |
| `E2` | JV 파트너·대주단·시장운영기관·공공기관 | 프로젝트 구조·금융·시장 |
| `E3` | 신용평가·공식 공급사·금융기관 | 재무구조·PF 보완 |
| `E4` | 언론·2차 분석 | 탐색용, 핵심 금액 단독근거 금지 |
| `INT` | ERP·Treasury·계약·EPC·세무·EAM | 실제 집행·잔액·수익률·covenant |

## 1.2 Claim Status

```yaml
claim_status:
  REPORTED: 공식자료의 직접 수치
  CONTRACT_PUBLIC: 계약당사자가 공개한 구조
  DERIVED: 동일 scope 공개값의 단순 산술
  HISTORICAL_PLAN: 과거 발표 당시 목표
  OPERATING_CONFIRMED: COD/운영 확인
  DEVELOPMENT: 개발단계이며 확정운영 아님
  INTERNAL_REQUIRED: 내부자료 필요
  NOT_DISCLOSED: 공개값 없음
  ANALYTICAL_SCENARIO: 의사결정 가정
```

## 1.3 Amount State

```text
Headline / Announced
→ Approved Budget
→ Committed Contract
→ PO / Change Order
→ Invoice Certified
→ Cash Paid
→ Capitalized
→ Asset Available for Use
→ Remaining Cost-to-Complete
→ Recoverable Cash-generating Asset
```

`같은 프로젝트의 금액`이라도 위 단계가 다르면 같은 숫자로 덮어쓰지 않는다.

---
