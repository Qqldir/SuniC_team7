---
id: skes-d17-d17-18-query-template-library
title: Query Template Library
summary: D17 오픈이노베이션 과제 포트폴리오의 상태·리스크·우선순위를 쿼리로 조회할 수 있는 12개 템플릿 정의표. ROI·규제·벤더·기술별 필터링과 의사결정 지원.
tags: [d17, oi-portfolio, table, "xref:d16"]
keywords: [포트폴리오 조회, 실행 준비도, ROI 검증, 규제 영향, 리스크 식별, 중복 과제, 우선순위 재계산, 벤더 관리, PoC 평가]
related: []
priority: normal
domain: D17
section: D17-18
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 439
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-18 Query Template Library

| Query ID | 질문 | 필수 Filter | 기대 출력 |
|---|---|---|---|
| `Q-D17-001` | 지금 바로 G0를 시작할 P0는? | Owner·Baseline·Hard Gate | READY/BLOCKED와 이유 |
| `Q-D17-002` | 같은 Pain을 중복 해결하는 Seed는? | pain/owner/data/denominator | Dedupe group |
| `Q-D17-003` | 외부벤더가 필요한 과제만 보여줘 | O/I mode·D16 evidence | Capability·벤더군·Evidence tier |
| `Q-D17-004` | Finance 검증이 끝나지 않은 ROI 주장은? | benefit_state | Hypothesis/Pilot/Verified 구분 |
| `Q-D17-005` | OT Write가 필요한 후보는? | cyber/SHE gate | NO-GO/approval path |
| `Q-D17-006` | LNG shock 시 우선순위를 재계산해줘 | scenario overlay | 006~013 urgency |
| `Q-D17-007` | BESS에서 수익·열화·안전 중복과제는? | BMS/EMS/bid/thermal | 026~030 dependency |
| `Q-D17-008` | LH2에서 생산량과 실제 판매량 차이는 어디서 생기나? | mass-balance boundary | 037~040 data gaps |
| `Q-D17-009` | CCS 중 firm volume 없는 후보는? | emitter stage/contract | HOLD/OBSERVE |
| `Q-D17-010` | 규정 Effective Date가 바뀌면 영향과제는? | jurisdiction/rule/version | 029·035·046~050·053 |
| `Q-D17-011` | Provider lock-in이 높은 과제는? | export·model/IP·EOL | re-negotiate/build option |
| `Q-D17-012` | Scale하지 말아야 할 PoC는? | G5/G6·TCO·guardrail | STOP/HOLD rationale |

---
