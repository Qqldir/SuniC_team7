---
id: skes-d13-1-evidence-state-policy
title: Evidence & State Policy
summary: "계약정보의 신뢰도를 E1A~INT 6단계로 분류하고, 계약·의무의 생명주기 상태를 정의하며, 공개자료 충돌을 처리하는 원칙을 제시한 정책기준"
tags: [d13, contract, schema, table]
keywords: [신뢰도등급, E1A~INT, Agreement State, 계약상태, Obligation State, 의무추적, 공개자료충돌, conflict_record, 정보검증, JV계약정보]
related: []
priority: normal
domain: D13
section: 1
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 845
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# 1. Evidence & State Policy

## 1.1 Evidence Tier

| Tier | 정의 | 사용 원칙 |
|---|---|---|
| `E1A` | 법정공시·거래소·정부·규제기관 | 소유권·재무·법인·공식 의사결정 |
| `E1B` | SK Innovation/E&S·자회사 공식자료 | 사업관계·지분·운영·전략 |
| `E2` | JV 상대방·계약상대·시장기관 공식자료 | 상대방 기준 관계·계약 구조 |
| `E3` | 신용평가·금융기관·공식 공급사 | PF·TUA·공급계약 보완 |
| `E4` | 신뢰 언론·2차 분석 | 탐색/충돌감지, 핵심 권리 단독근거 금지 |
| `INT` | CLM·전자결재·법무·이사회·ERP·Treasury·data catalog | 비공개 조항·실제 의무·승인·이행 |

## 1.2 Agreement State Vocabulary

```yaml
agreement_state:
  NON_BINDING_MOU: 방향·협력의사; 확정 투자/수요 집계 금지
  DEVELOPMENT_CONSORTIUM: 공동개발/사업자선정 단계
  CONDITIONAL_BINDING: 본계약이나 CP 충족 전
  ACTIVE_BINDING: 유효한 구속계약
  ACTIVE_RIGHT: TUA/LTA/license 등 권리 사용 중
  OPERATING_JV: JV/SPV가 상업운영 중
  RESTRUCTURED: 당사자·지분·자산·의무 구조 변경
  TRANSFERRED: 권리/지분이 제3자 또는 관계사로 이전
  TERMINATED_OR_EXPIRED: 종료·만료·청산
  STATUS_CONFLICT: 공개자료 간 현재 당사자/상태 불일치
  INTERNAL_REQUIRED: 공개자료로 법적 상태 확정 불가
```

## 1.3 Obligation State

```text
Proposed → Signed → Effective → Conditional → Due → Performed → Accepted → Settled
                                  ↘ Waived / Disputed / Breached / Cured
Amended → Superseded → Assigned → Terminated → Surviving Obligation
```

`Performed`와 `Accepted`, `Accepted`와 `Settled`는 각각 다른 상태다.

## 1.4 공개자료 충돌 처리

동일 사실에 최신 공식자료가 충돌하면 자동 병합하지 않는다.

```yaml
conflict_record:
  claim_id: required
  source_a: required
  source_b: required
  effective_date_a: required
  effective_date_b: required
  legal_party_a: required
  legal_party_b: required
  likely_explanation: hypothesis_only
  resolver: Legal_or_CorporateRegistry
  status: OPEN
```

대표 사례는 SK Plug Hyverse다. Plug Power의 2025 10-K는 2025-12-31 Plug가 보유하던 49% 전량을 SK Innovation에 매각하고 현금 $6.5m을 수취했다고 공시한다. 별도 2차 공개자료에는 신규 SPC가 49%를 취득했다는 설명도 존재하므로, D13은 **Plug Power의 49% 보유 종료는 E1A 사실**, 최종 현행 49% 명의주주는 한국 법인등기/주주명부 확인 전 `OPEN_CONFLICT`로 둔다.

---
