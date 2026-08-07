---
id: skes-d14-1-evidence-temporal-policy
title: Evidence & Temporal Policy
summary: "규제·정부·회사 자료 등 증거자료의 6단계 신뢰도 등급과 법령의 공포·시행·적용일 구분, 인센티브 수령 단계를 분류하는 정책 기준."
tags: [d14, policy, schema, table]
keywords: [증거등급, 신뢰도, 시행일, 공포일, 적용일, 경제효과상태, 인센티브, 규제, 보조금, E1A]
related: []
priority: normal
domain: D14
section: 1
source: SK이노베이션E&S_D14_Policy_Regulation_Incentives_and_Compliance.md
breadcrumb: ""
tokens: 542
updated: 2026-08-06
---

> SK이노베이션 E&S · D14 정책·규제·인센티브·컴플라이언스

# 1. Evidence & Temporal Policy

## 1.1 Evidence Tier

| Tier | 정의 | 사용 원칙 |
|---|---|---|
| `E1A` | 법령·정부·규제기관·세무당국 | 시행일·의무·공고·세액공제 원본 |
| `E1B` | 시장운영기관·공공기관 | 입찰·시장참여·계통·인증 절차 |
| `E2` | SK Innovation/E&S 및 자회사 공식자료 | 실제 사업·자산·신청/참여 상태 |
| `E3` | JV 상대방·프로젝트 파트너 공식자료 | 공동사업 관할·허가 상태 보완 |
| `E4` | 신뢰 2차자료 | 탐색·충돌감지용, 핵심 의무 단독 근거 금지 |
| `INT` | Legal, Tax, EHS, EMS, Permit register, ERP, CLM, 시장정산 | 실제 적용·신고·수령·위반·증빙 |

## 1.2 Effective-Date Rule

```text
publication_date != enactment_date != effective_date != compliance_deadline
```

- 기준일 이전 `effective_date`만 `IN_FORCE`로 본다.
- 공포되었더라도 시행 전이면 `ENACTED_FUTURE`다.
- 입찰 공고 후 취소되면 최종상태는 `CANCELLED`; 과거 공고 기록은 삭제하지 않는다.
- 매년 변경되는 경매비율·시장규칙·세액공제 guidance는 `effective_year`를 반드시 가진다.

## 1.3 경제효과 상태

```yaml
economic_effect_state:
  STATUTORY_MAX: 법정 최대 인센티브
  ELIGIBLE_UNVERIFIED: 적용 가능성 있으나 요건 검증 전
  QUALIFIED: 요건 검증 완료
  CLAIMED: 신고/신청 완료
  AWARDED: 보조금/계약 선정
  RECEIVED: 현금/세액/인증서 실제 수령
  TRANSFERRED: 세액공제/인증서 양도
  CLAWBACK_EXPOSED: 사후 환수 위험 존재
  NOT_ELIGIBLE: 불충족 확인
```

---
