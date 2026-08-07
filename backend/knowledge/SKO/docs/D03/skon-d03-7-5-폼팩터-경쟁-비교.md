---
id: skon-d03-7-5-폼팩터-경쟁-비교
title: 폼팩터 경쟁 비교
summary: 프리즈매틱·원통형 등 배터리 폼팩터별 SK온의 개발 단계와 경쟁사의 상용화 현황을 비교 분석한 자료
tags: [d03, product, schema]
keywords: [배터리 셀, Pouch, Prismatic, Cylindrical, 상용화 수준, 기술격차, LG에너지솔루션, CATL, BYD, 생산기반, 원통형, 프리즈매틱, 삼성SDI, 대량생산, 4680, 2170, CTP]
related: []
priority: normal
domain: D03
section: 7.5
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 532
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 7.5 폼팩터 경쟁 비교

## COMP-MAP-FORM-001

```text
SK On
├─ Pouch → Commercial core
├─ Prismatic → Prototype / Pre-commercial
└─ Cylindrical → Exploratory

LG Energy Solution
├─ Pouch → Commercial
├─ Cylindrical 2170 → Commercial
├─ Cylindrical 46-Series → Commercializing
└─ Prismatic → Development / Conversion plans

Samsung SDI
├─ Prismatic → Commercial core
├─ Cylindrical 21700 → Commercial
└─ 46-Series → Development and customer expansion

Panasonic Energy
├─ 2170 → Large-scale commercial
└─ 4680 → Product program

CATL
├─ Prismatic → Commercial core
├─ CTP / Module-free → Commercial
└─ Multiple chemistry-system architectures

BYD
└─ Long Blade Prismatic / CTP → Commercial core
```

SK온의 각형 시제품 공개는 폼팩터 다변화가 실제 개발단계에 진입했음을 보여주지만, 경쟁사들은 이미 고객계약과 대량생산 경험을 보유한다. 원통형은 SK온이 검토 수준인 반면 LG에너지솔루션·Panasonic·삼성SDI는 상용 제품 및 생산기반을 확보하고 있다. ([삼성SDI][10])

### 폼팩터 격차

```yaml
gap_id: GAP-SKON-D03-FORM-001

prismatic:
  sk_on_status: PRE_COMMERCIAL
  benchmark:
    - Samsung SDI PRiMX
    - CATL prismatic CTP
    - BYD Blade
  gap:
    - Mass-production yield
    - Can and sealing technology
    - Vent design validation
    - Customer platform integration
    - Pack-level thermal propagation control

cylindrical:
  sk_on_status: EXPLORATORY
  benchmark:
    - LGES 46-Series
    - Panasonic 2170
    - Tesla 4680
  gap:
    - Cell design platform
    - Tabless current collection
    - High-speed winding
    - Can manufacturing ecosystem
    - Cell-to-pack thermal management
    - Customer reference

d17_priority:
  prismatic: VERY_HIGH
  cylindrical: MEDIUM
```

---
