---
id: skes-d05-0-domain-boundary
title: Domain Boundary
summary: "SK E&S의 기술개발과 특허 포트폴리오를 관리하기 위해 어떤 기술과 권리를 포함할지, 어떻게 분류할지 정의하는 문서."
tags: [d05, rnd, core-candidate, schema, table, "xref:d04", "xref:d03", "xref:d17"]
keywords: [기술개발역량, 지식재산권, 특허포트폴리오, 권리귀속분류, 협력사기술, 자회사, FTO, 라이선스, 데이터권, 소프트웨어저작권]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001, ORG-SKI-LEGAL-000001]
priority: critical
domain: D05
section: 0
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1681
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# SK이노베이션 E&S AI Knowledge Database

## D05. R&D, Patents & Intellectual Property｜연구개발·특허·지식재산

**Version 1.0 / 기준일: 2026년 8월 4일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Parent after merger: `ORG-SKI-LEGAL-000001`
- Source namespace: `SRC-ENS-D05-*`
- R&D program namespace: `RDP-ENS-*`
- Patent family namespace: `PF-ENS-*`
- IP asset namespace: `IP-ENS-*`
- Research partner namespace: `RP-ENS-*`
- O/I Seed namespace: `SEED-ENS-D05-*`
- D04 inheritance: 10개 기술군, 61개 세부기술, 25개 적용 시나리오, 52개 O/I Seed

---

# 0. Domain Boundary

## 0.1 목적

D05는 SK이노베이션 E&S의 연구개발 역량과 지식재산을 단순 특허 건수로 평가하지 않는다. LNG·발전·도시가스·재생에너지·수소·ESS·EV 충전·CCS 사업에서 다음 질문에 답할 수 있는 관계형 데이터베이스를 구축한다.

1. 어떤 조직과 자회사가 기술을 개발·실증·운영하는가.
2. 기술은 자체개발, 공동개발, 인수, 라이선스, 벤더 도입 중 어느 경로로 확보되는가.
3. 공개 특허의 출원인·현재 권리자·발명자·우선일·법적 상태는 무엇인가.
4. 특허의 기술적 범위가 D03 제품과 D04 기술 중 어디에 연결되는가.
5. 특허가 없는 소프트웨어·데이터·운영 노하우는 어떤 방식으로 보호될 가능성이 높은가.
6. O/I 협력 시 공동성과·배경기술·데이터·개량발명의 권리를 어떻게 설계해야 하는가.
7. 공개자료만으로 답할 수 없는 권리·FTO·실시 여부는 무엇인가.

## 0.2 포함 범위

```yaml
included:
  corporate_rnd:
    - SK Innovation E&S CIC technology development and demonstration
    - historical SK E&S R&D programs and patent applications
  affiliates:
    - city-gas subsidiaries where technology is operationally relevant
    - Key Capture Energy proprietary software and operating know-how
    - EverCharge patents, software, firmware and charging hardware
    - SK Plug HyVerse joint-venture development where E&S linkage is explicit
  collaboration:
    - public research institutes
    - universities and technology ventures
    - global technology partners and licensors
  ip_forms:
    - patents and utility models
    - software copyright and trade-secret candidates
    - data rights and model artifacts
    - trademarks and product names when relevant to capability ownership
    - joint-development and license-right requirements
```

## 0.3 제외·유보 범위

```yaml
deferred_or_prohibited:
  - final freedom-to-operate opinion
  - infringement, invalidity or enforceability legal opinion
  - definitive ownership certification without official register and assignment packet
  - assertion that a patent is implemented in a product without claim-to-system evidence
  - complete worldwide patent portfolio claim
  - confidential R&D budget, headcount, laboratory inventory or invention register
  - confidential source code, model weights, training data or operating recipes
  - commercial license scope without contract review
  - internal background-IP and improvement-IP clauses not publicly disclosed
```

## 0.4 권리귀속 분류

| Code | 의미 | 예시 | D17 사용 규칙 |
|---|---|---|---|
| `OWNED_DIRECT` | 과거 SK E&S 또는 현재 E&S CIC가 직접 출원·보유한 것으로 공개 확인 | CO₂ 포집 흡수제 특허 | 내부 활용 가능성을 검토하되 실시 여부는 별도 확인 |
| `CO_OWNED` | E&S와 자회사·협력사가 공동 출원 | 정압기 제어, 도시가스 계량 | 공동권리자 동의·계약 확인 전 단독 활용 가정 금지 |
| `AFFILIATE_OWNED` | 연결 자회사 명의 IP | EverCharge EV 충전 특허 | 법인별 권리 경계와 내부 라이선스 확인 |
| `JV_CONTROLLED_OR_LICENSED` | JV 또는 파트너 기술을 계약으로 활용 | Plug Power PEM 기술 | E&S 자체 특허로 표현 금지 |
| `PARTNER_TECH` | 기술 파트너가 보유·제공 | Honeywell ASCC | PoC·라이선스·지역권·개량권 확인 |
| `PROPRIETARY_SOFTWARE` | 공개적으로 독자 개발은 확인되나 특허보다 소프트웨어·노하우 보호 가능성이 큼 | KCE MarketCapture | 소스·데이터·모델·재사용 권한을 별도 검토 |
| `PUBLIC_REFERENCE_ONLY` | 산업·학술 참고 기술 | NREL·DOE 기술 | E&S 보유기술로 오인 금지 |
| `UNVERIFIED` | 검색 히트만 있고 귀속·상태 미검증 | 유사 상호 출원 | D17 근거로 직접 사용 금지 |

## 0.5 증거수준

| Level | 근거 | 허용 표현 |
|---|---|---|
| `E1_REGISTER` | 특허청·USPTO·WIPO 등 공식 등록부 | 출원·등록·권리자·법적상태 |
| `E2_PATENT_AGGREGATOR` | Google Patents 등 등록정보 집계 | 초기 패밀리·검색 결과, 공식 재검증 필요 |
| `E3_COMPANY_OFFICIAL` | 회사 공식 보도자료·제품 페이지 | 개발·실증·협력·제품 기능 |
| `E4_PARTNER_OFFICIAL` | 연구기관·파트너 공식 자료 | 상대방 관점의 기술·계약 상태 |
| `E5_PUBLIC_SECONDARY` | 신뢰할 수 있는 보조자료 | 탐색용, 핵심 권리 판단 금지 |

---
