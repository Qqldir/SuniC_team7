---
id: skes-d13-16-d17-contract-feasibility-gate
title: D17 Contract Feasibility Gate
summary: 계약의 법적·재무·보안 타당성을 검증하는 11단계 게이트 프로세스와 데이터·IP 권리 등 판정 필드 구조.
tags: [d13, contract, schema, "xref:d17"]
keywords: [계약심사, 데이터권리, 지적재산권, 교차국경이전, 제3자동의, 보안게이트, 재무게이트, PoC, JV, 권리상태]
related: []
priority: normal
domain: D13
section: 16
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 363
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# 16. D17 Contract Feasibility Gate

## 16.1 Gate sequence

```text
O/I Seed
→ correct legal entity?
→ asset / contract in scope?
→ data ownership and access?
→ confidentiality / privacy / cross-border transfer allowed?
→ IP / model-output right allowed?
→ JV reserved-matter approval needed?
→ lender/customer/vendor consent needed?
→ cybersecurity deployment allowed?
→ liability / warranty / safety impact acceptable?
→ measurable economic KPI?
→ human owner and review path?
→ PoC approval
```

## 16.2 Gate fields

```yaml
d17_contract_gate:
  seed_id: required
  legal_entity_id: required
  agreement_ids: []
  asset_ids: []
  data_right: ALLOWED|RESTRICTED|UNKNOWN|PROHIBITED
  ip_right: ALLOWED|RESTRICTED|UNKNOWN|PROHIBITED
  cross_border: ALLOWED|REVIEW|PROHIBITED
  reserved_matter: YES|NO|UNKNOWN
  third_party_consent: REQUIRED|NOT_REQUIRED|UNKNOWN
  warranty_impact: NONE|REVIEW|MATERIAL
  safety_impact: NONE|REVIEW|MATERIAL
  finance_gate: PASS|REVIEW|FAIL
  legal_gate: PASS|REVIEW|FAIL
  security_gate: PASS|REVIEW|FAIL
  owner: required
  status: PROPOSED|PILOTABLE|BLOCKED|APPROVED
```

`UNKNOWN`은 `NO`가 아니다. 권리 미확인 상태에서는 D17이 PoC를 자동 추천할 수는 있어도 자동실행으로 승격할 수 없다.

---
