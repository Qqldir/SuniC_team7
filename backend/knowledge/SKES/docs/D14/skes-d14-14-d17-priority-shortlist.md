---
id: skes-d14-14-d17-priority-shortlist
title: D17 Priority Shortlist
summary: 규제변화·세무인센티브·에너지사업 영역의 15개 AI 실증 프로젝트를 우선순위순으로 정렬하고 PoC 실행 제약조건을 정의한 가이드.
tags: [d14, policy, table, "xref:d17"]
keywords: [규제변화, 세무인센티브, AI 실증, 준법, 탄소배출권, 인허가, 공급사추적, 청정수소, 자산특정, 킬게이트]
related: [SEED-0001, SEED-0007, SEED-0026, SEED-0025, SEED-0015, SEED-0022, SEED-0034, SEED-0036, SEED-0043, SEED-0052, SEED-0050, SEED-0059, SEED-0058, SEED-0013, SEED-0060]
priority: normal
domain: D14
section: 14
source: SK이노베이션E&S_D14_Policy_Regulation_Incentives_and_Compliance.md
breadcrumb: ""
tokens: 662
updated: 2026-08-06
---

> SK이노베이션 E&S · D14 정책·규제·인센티브·컴플라이언스

# 14. D17 Priority Shortlist

## 14.1 P0 Candidates

| Rank | Seed | Why Now | 90-day PoC Target |
|---|---|---|---|
| 1 | `SEED-0001` temporal regulation KG | 2026 규제변화 다수 | 4관할 rule version 자동관리 |
| 2 | `SEED-0007` K-ETS position twin | 유상할당 15→50% | 발전소별 carbon position |
| 3 | `SEED-0026` PFE supplier graph | KCE tax eligibility | top BOM 공급사 ownership trace |
| 4 | `SEED-0025` 48E eligibility calculator | BESS 투자경제성 직접 영향 | 3개 project tax gate |
| 5 | `SEED-0015` offshore permit dependency | Jeonnam 2/3 | permit critical path |
| 6 | `SEED-0022` clean-H2 MRV | 9/18 제도변화 readiness | LH2 batch traceability |
| 7 | `SEED-0034` ERCOT rule change agent | rules high-frequency | protocol→config diff |
| 8 | `SEED-0036` interconnection predictor | KCE pipeline 8GW | milestone slip risk |
| 9 | `SEED-0043` Safeguard simulator | Barossa operating 2026 | baseline/carbon scenario |
| 10 | `SEED-0052` Quynh Lap 2031 Monte Carlo | deadline economics cliff | cutoff probability |
| 11 | `SEED-0050` bilingual permit extractor | Vietnam document load | permit obligations extraction |
| 12 | `SEED-0059` source-locked legal RAG | hallucination control | official-source-only Q&A |
| 13 | `SEED-0058` OT-safe AI gateway | operations AI prerequisite | read-only data path |
| 14 | `SEED-0013` PPA attribute validator | green claim integrity | 6 PPA cross-check |
| 15 | `SEED-0060` compliance gate scorer | D17 portfolio control | idea→PoC gate automation |

## 14.2 PoC Kill Gates

1. 규제 대상 법인/자산을 특정할 수 없으면 PoC 보류.
2. 공식 rule version/effective date가 없으면 자동 의사결정 금지.
3. 세무 인센티브는 Tax reviewer 없이 realized benefit으로 표시 금지.
4. OT write access가 필요한 실증은 별도 cyber/safety approval 전 금지.
5. 개인정보/시장기밀/계약기밀의 학습데이터 재사용 권리가 없으면 모델 학습 금지.
6. 규제기관 제출문서를 AI가 생성하더라도 담당자 서명·검토를 유지.
7. PoC KPI는 `정확도`만 아니라 회피한 비용·단축일·오류/위반 감소로 측정.

---
