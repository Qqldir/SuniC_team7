---
id: skes-d13-8-hydrogen-partnership-ownership-transitio
title: Hydrogen Partnership & Ownership Transition
summary: Plug Power가 2025년 49% 지분을 매각한 후 신규 보유자 규명과 Electrolyzer·Fuel cell 등 기술권 9개 항목별 존속 여부를 검증하는 내용이다.
tags: [d13, contract, schema, table]
keywords: [SK Plug Hyverse, 지분 구조 변경, 보유자 확인, 기술권 존속, Equipment supply, 라이센스 계약, 기업 등기, Change of Control, 비경쟁 약정, 수소 생태계]
related: []
priority: normal
domain: D13
section: 8
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 770
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# 8. Hydrogen Partnership & Ownership Transition

## 8.1 SK Plug Hyverse lineage

2021 JV 발표 기준 SK E&S와 Plug Power의 지분은 51:49였고, Board 의석수는 동수이며 material decision은 만장일치로 공개됐다. 따라서 **지분 51%인데도 특정 중대사항은 단독 통제가 아니었던 공개 사례**다. `[SRC-ENS-D13-0029]`

2025-12-31 Plug Power는 자신의 49% 지분 전량을 매각했고 $6.5m을 수취했다고 2025 10-K에 공시했다. D13 기준일 현재 Plug 49% ownership은 종료된 사실로 처리한다. `[SRC-ENS-D13-0030]`

```text
2021 JV announcement: SK E&S 51 / Plug 49
→ 2022 initial funding / operations
→ 2024~2025 hydrogen-market execution
→ 2025-12-31 Plug entire 49% sold
→ 2026 current 49% holder: registry/shareholder-ledger verification required
→ technology / supply / warranty survival: separate verification
```

## 8.2 Ownership Conflict Record

```yaml
claim_id: CNF-ENS-D13-0001
subject: SK_Plug_Hyverse_49pct_holder
source_E1A:
  source: Plug_Power_2025_10K
  fact: Plug sold entire 49% equity interest to SK Innovation on 2025-12-31
  cash_received_USD_million: 6.5
other_public_claim:
  fact: separate public reports describe a new SPC as 49% holder
resolution:
  required: Korean corporate registry + shareholder ledger + share purchase/assignment documents
  status: OPEN
prohibited:
  - treating Plug Power as current 49% shareholder
  - treating unverified buyer identity as canonical legal party
```

## 8.3 Technology-right survival

지분관계 종료는 Plug 기술 관련 모든 계약의 자동종료를 뜻하지 않는다. 다음을 독립적으로 확인한다.

| Right | 질문 |
|---|---|
| Equipment supply | 미인도 장비·spares·warranty 의무 존속 여부 |
| Electrolyzer | 기술사용·현지화·인증 권리 존속 여부 |
| Fuel cell | 상업판매·서비스·부품 권리 존속 여부 |
| Software/data | diagnostic·firmware·cloud access 존속 여부 |
| IP | Background/Foreground·improvement ownership |
| Trademark | Plug name/logo usage termination |
| Confidentiality | JV 종료 후 survival period |
| Non-compete | 시장/지역 제한의 존속 여부 |
| Change of Control | supplier/license consent 필요 여부 |

## 8.4 Hydrogen Public-Private Network

K-water, Korea South-East Power, KD운송그룹, 국토부·인천시 등은 모두 같은 종류의 파트너가 아니다. 기술 MOU·수요 생태계 MOU·정부지원·충전소 운영·PF를 분리한다.

---
