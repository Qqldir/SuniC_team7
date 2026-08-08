---
id: skon-d10-d10-00-domain-boundary
title: Domain Boundary
summary: "시장·경쟁 정보(D10)의 범위, 포함제외 기준, 공개자료 해석 원칙을 규정하는 도메인 경계 정의서."
tags: [d10, market, core-candidate, table, "xref:d09", "xref:d17", "xref:d00", "xref:d03"]
keywords: [EV·배터리·ESS, 경쟁사 분석, 시장구조, Form Factor, 화학계, D10 정의, 공개자료 기준, 시장노출도, 경쟁격차, Technology Scouting, 시장세분화, 경쟁사동향, 제품형태, 공개자료판정, 자료해석기준, 노출도, 시장점유율]
related: []
priority: critical
domain: D10
section: D10-00
source: SK온_D10_Market_Competition_Industry_Dynamics.md
breadcrumb: "SK온 D10 — Market, Competition & Industry Dynamics"
tokens: 1078
updated: 2026-08-03
---

> SK온 · D10 시장·경쟁·산업동향 · SK온 D10 — Market, Competition & Industry Dynamics

# SK온 D10 — Market, Competition & Industry Dynamics

- 문서 버전: **v1.0.1**
- 기준일: **2026-08-03 (KST)**
- 이전 완료 지점: `D09 Customers, Orders & OEM Relationships v1.0`
- 작성 방식: **실무형 요약 DB** — 시장구조·경쟁 포지션·Pain Point·외부 사례·O/I 기회를 유지하고, 유료 시장자료의 수치를 임의 보간하지 않음
- 상위 목적: 글로벌 EV·배터리·ESS 시장의 변화와 경쟁사 대응을 SK온의 제품·고객·생산거점에 연결하고 D17 O/I 과제 추천에 투입
- D00 통합검수: Domain-local Source/Entity ID를 보존하고 Canonical Alias는 D00 Crosswalk로 해석한다. 전망·계획·실적은 D00의 Time·Fact Class Standard에 따라 분리한다.

---

## D10-00 Domain Boundary

### 1. 도메인 정의

D10은 시장규모 전망을 모아두는 통계 문서가 아니다. 다음의 변화가 SK온의 어떤 의사결정에 영향을 주는지 연결하는 도메인이다.

```text
Market Segment / Geography
→ Demand Driver / Policy / Price Signal
→ Chemistry·Form-factor·Solution Shift
→ Competitor Move
→ SK온 Product·Customer·Plant Exposure
→ Strategic Gap / Response Option
→ D17 Open-Innovation Seed
```

핵심 질문은 `시장이 성장하는가`보다 `어느 지역·용도·화학계·제품형태가 성장하며, SK온의 현재 자산과 고객승인 범위가 그 변화에 얼마나 빠르게 대응할 수 있는가`다.

### 2. 포함·제외 범위

| 포함 | 제외 또는 다른 도메인 원본 |
|---|---|
| EV·EV Battery·ESS 시장 Snapshot과 전망 | 개별 고객·수주·Call-off는 D09 |
| 지역·화학계·Form Factor·Application별 구조 변화 | 제품사양·기술성능 원본은 D03~D04 |
| CATL·LGES·Samsung SDI·BYD·Panasonic 등 경쟁사 전략 | 특허·R&D Program 원본은 D05 |
| 경쟁 가격·규모·수익성·현지화의 공개 Proxy | 제조원가·공장별 손익은 D11 |
| 시장–제품–공장 Exposure와 Scenario | CAPEX·보조금·투자회수는 D12 |
| 외부사례와 D17 O/I 후보 | 계약·JV·파트너 구조는 D13 |
| 산업정책의 시장효과 | 법규 준수 판단 원본은 D14 |
| 경쟁격차와 전략적 Pain Point | 전사 Risk 원본은 D15 |
| Technology·Startup Scouting 대상 정의 | 개별 후보기업 원장은 D16 |

### 3. 공개자료 판정 원칙

1. 시장전망, 실제 판매, 설치량, 생산능력과 출하량을 서로 다른 값으로 보존한다.
2. 시장점유율은 조사기관의 지역·기간·집계기준이 다르면 직접 연결하거나 합산하지 않는다.
3. 경쟁사의 `생산능력`을 `판매량`, `수주`, `가동률`로 바꾸지 않는다.
4. 기업이 발표한 기술성능은 해당 기업의 공식 Claim으로 저장하며 독립 검증치로 취급하지 않는다.
5. 세액공제·고객보상·일회성 환입이 포함된 영업이익을 구조적 수익성으로 자동 분류하지 않는다.
6. 2026년 전망은 기준일 현재 전망치이며 Actual이 들어오면 Version을 추가한다.
7. 공개되지 않은 SK온의 고객별 Margin·제품별 원가·현재 시장점유율은 `NOT_DISCLOSED`로 둔다.

---
