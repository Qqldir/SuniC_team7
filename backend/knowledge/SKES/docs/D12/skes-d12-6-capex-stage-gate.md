---
id: skes-d12-6-capex-stage-gate
title: CAPEX Stage-Gate
summary: "대규모 투자사업의 10개 단계별 의사결정 관문, 각 단계의 심사질문과 통과조건, 그리고 사후 자산 최적화 옵션들을 체계화한 문서."
tags: [d12, capex, schema, table, "xref:d02", "xref:d10", "xref:d09", "xref:d06"]
keywords: [투자심사, 타당성검토, 의사결정, 오프테이크, 자금조달, 인허가, FEED, 리파이낸싱, 자산회수, 수익성]
related: []
priority: normal
domain: D12
section: 6
source: SK이노베이션E&S_D12_CAPEX_Investment_Funding_and_Financial_Structure.md
breadcrumb: ""
tokens: 641
updated: 2026-08-06
---

> SK이노베이션 E&S · D12 CAPEX·투자·자금조달

# 6. CAPEX Stage-Gate

| Gate | 질문 | 필수 증거 | 결정 |
|---|---|---|---|
| `G0 Strategic Fit` | D02/D10 방향과 맞는가 | 시장·portfolio | explore/stop |
| `G1 Concept` | build/buy/contract/digital 중 최적안인가 | 대안·capacity | study/stop |
| `G2 Commercial` | 고객·오프테이크가 투자규모를 지지하는가 | D09 계약상태 | proceed/resize |
| `G3 Technical` | 기술·부지·계통·공급망이 실행 가능한가 | D06~D08 | FEED/pilot |
| `G4 Regulatory` | 인허가·보조금 조건이 현실적인가 | D14 | conditional |
| `G5 Funding` | debt/equity/support가 확보됐는가 | term sheet·covenant | close/hold |
| `G6 FID` | downside에서도 증분가치가 양수인가 | NPV/IRR/ROIC range | FID/hold/exit |
| `G7 Build` | EAC·schedule·change order 통제되는가 | WBS·EPC | continue/replan |
| `G8 Commission` | 성능·안전·인수조건 충족하는가 | test·acceptance | COD/remediate |
| `G9 Operate` | 반복 cash ROIC가 목표인가 | D11 actual | hold/expand |
| `G10 Recycle` | refinance/sell/convert가 더 나은가 | forward cash | choose option |

## 6.1 Real Option Set

```yaml
options:
  EXPAND: 검증된 수요와 양의 증분현금이 있을 때 증설
  HOLD: 인허가/고객/가격 불확실성이 해소될 때까지 옵션 보존
  CONVERT: 기존 부지·계통·설비를 다른 에너지용도로 재사용
  REPOWER: 노후 발전/재생 설비의 효율·용량 개선
  REFINANCE: COD·운영 안정 후 자본비용/만기구조 개선
  SELL_PARTIAL: 지분 매각으로 현금회수하되 사용권/운영권 보존
  SELL_FULL: 자산과 위험을 함께 처분
  MOTHBALL: 재가동 옵션을 남기고 현금소모 축소
  EXIT: 구조적 음의 증분가치일 때 복구·clawback 포함 철수
```

보령 LNG터미널 사례처럼 `SELL_PARTIAL/SELL_EQUITY + RETAIN_USAGE_RIGHT`가 가능하므로 자산 매각을 사업철수와 동일시하지 않는다.

---
