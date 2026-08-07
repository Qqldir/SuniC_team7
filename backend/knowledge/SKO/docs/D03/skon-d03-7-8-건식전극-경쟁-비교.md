---
id: skon-d03-7-8-건식전극-경쟁-비교
title: 건식전극 경쟁 비교
summary: 건식전극 기술의 Tesla·SK온·LGES 개발 현황과 상용화 격차를 비교한 벤치마크 자료.
tags: [d03, product, schema, "xref:d17"]
keywords: [4680 배터리, 파일럿 라인, 상용화, dry electrode, 전극 균일성, 생산 수율, 롤투롤, 4680, 양극 음극, roll-to-roll, 코팅 균일성, 전극 부착, 스케일업, 벤치마크]
related: []
priority: normal
domain: D03
section: 7.8
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 515
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 7.8 건식전극 경쟁 비교

## COMP-MAP-DRY-001

```yaml
dry_electrode_competition:

  SK_On:
    status:
      - Pilot line completed in 2024
      - Commercialization development underway
    product_application: NOT_PUBLICLY_CONFIRMED

  Tesla:
    status:
      - Anode and cathode dry-electrode production in Austin
      - 4680 packs used in selected Model Y vehicles
    maturity: VEHICLE_PRODUCTION_APPLICATION

  LG_Energy_Solution:
    status:
      - Dry-electrode roadmap for LFP
      - Pilot line activation and mass-production capability development
    maturity: PILOT_AND_DEVELOPMENT

competitive_gap:
  - Continuous coating uniformity
  - Electrode adhesion
  - High-loading crack prevention
  - Powder handling
  - Roll-to-roll throughput
  - Production yield
```

Tesla는 4680 셀의 양극과 음극 모두에 건식전극을 적용해 차량용 생산을 시작했다고 발표했다. SK온과 LG에너지솔루션은 파일럿·상용화 개발단계로 공개돼 있어, 현재 공개근거 기준 Tesla가 실제 제품 적용에서 앞선 벤치마크다. ([Tesla][13])

### D17 연결 후보

```yaml
oi_candidate_id: OI-CAND-SKON-DRY-001
title: Dry Electrode Scale-Up Open Innovation Program

problem:
  - Pilot process has not been publicly validated at full commercial scale
  - Yield and electrode uniformity may become scale-up bottlenecks

external_technology_categories:
  - Dry powder dispersion
  - Electrostatic powder deposition
  - Fibrillation control
  - Inline thickness measurement
  - Machine-vision crack detection
  - Digital twin for calendering
  - Solvent-free binder technology

benchmark:
  - Tesla 4680 dry-electrode production
  - LGES LFP dry-electrode pilot

priority: VERY_HIGH
```

---
