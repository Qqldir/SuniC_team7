---
id: skon-d05-d05-38-patent-family-inventor-network
title: Patent Family–Inventor Network
summary: "SK온의 배터리 기술 특허 발명자들을 6개 기술 클러스터로 분류하고, 발명자 간 교량 역할과 특정 기술 분야의 인력 집중도 위험을 분석한 문서."
tags: [d05, rnd, schema]
keywords: [발명자 집중도, 배터리 기술, 양극 소재, 고체 전해질, 급속충전, 기술이전 위험, EIS 진단, 핵심인력 의존성, 산화물, 클러스터 분석, 발명자 클러스터, 전극·양극·고체전해질, 특허 포트폴리오, 기술이전 리스크, 인력 의존도, CTP·EIS, 기술사업화, 핵심인력 육성, 기술 네트워크]
related: []
priority: normal
domain: D05
section: D05-38.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 967
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-38. Patent Family–Inventor Network

## 38.1 Core Inventor Cluster Map

```text
SK On Patent Inventor Network
│
├── Electrode & Fast Charging Cluster
│   ├── Dong Hoon Lee
│   ├── Jae Youn Kim
│   ├── Jung Min Yang
│   ├── Young Jun Kim
│   ├── Yong Hee Kang
│   └── Hyo Sung Lim
│
├── Cathode Material Cluster
│   ├── Young-Uk Park
│   ├── Mincheol Beak
│   ├── Seung Hyun Kim
│   ├── Jae Young Choi
│   └── Je Nam Choi
│
├── Oxide Solid-State Cluster
│   ├── Eun Jeong Yi
│   ├── Kyeong Joon Kim
│   ├── Min Kyu Kim
│   ├── Ji Young Park
│   └── Do Kyeong Lee [related later filings]
│
├── EIS·Diagnostics Cluster
│   ├── Kyu Min Hwang
│   ├── Myeong Jae Go
│   ├── Won Hee Kim
│   ├── Yun Nyoung Lee
│   ├── So Yeon Choi
│   └── Dong Hwa Han
│
├── On-Vent Cluster
│   ├── Jae Sik Shin
│   ├── Seung Hoon Ju
│   ├── Ji Yong Park
│   ├── Jae Gyu Byun
│   └── Gi Jeong Seo
│
└── CTP·Pack Cluster
    ├── Jun Hee Jung
    ├── Jae Il Hwang
    ├── Bon Seok Ku
    ├── Jeong Hwan Lee
    └── Sei Hoon Cho
```

---

## 38.2 Cross-Cluster Bridge Analysis

```yaml
cross_cluster_bridges:

  - bridge_id: BRIDGE-D05-001
    researcher: Dong Hoon Lee
    connected_clusters:
      - Fast-Charging Electrode
      - Dry Electrode
    interpretation: >
      전극 계면저항·접착·급속충전 설계와 건식 제조공정 사이를
      연결하는 발명자 네트워크가 존재한다.
    information_type: ANALYSIS
    confidence: HIGH

  - bridge_id: BRIDGE-D05-002
    researchers:
      - Kyeong Joon Kim
      - Min Kyu Kim
      - Eun Jeong Yi
    connected_outputs:
      - Peer-reviewed photonic-sintering paper
      - Oxide-electrolyte patent family
    interpretation: >
      학술적 공정검증과 기업 특허화가 동일 연구자 집단을 통해
      연결된 대표 연구사업화 사례다.
    information_type: ANALYSIS
    confidence: VERY_HIGH

  - bridge_id: BRIDGE-D05-003
    researchers:
      - Young-Uk Park
      - Mincheol Beak
    connected_outputs:
      - Ultrahigh-nickel single-crystal paper
      - Single-particle and cathode-material patents
    interpretation: >
      차세대 양극 소재의 논문성과와 특허 포트폴리오가
      동일 연구자 네트워크에서 병행되고 있다.
    information_type: ANALYSIS
    confidence: HIGH
```

---

## 38.3 Concentration Risk

```yaml
inventor_concentration_risk:

  oxide_solid_state:
    observation:
      - Core paper and patent outputs rely on a relatively small researcher group
    potential_risk:
      - Key-person dependency
      - Tacit-knowledge concentration
      - Technology-transfer bottleneck
    mitigation:
      - Experiment protocol codification
      - Second-line inventor development
      - Pilot-line rotation
      - Research notebook and data genealogy

  on_vent:
    observation:
      - Same five inventors appear across sibling vent families
    potential_risk:
      - Narrow design-knowledge concentration
    mitigation:
      - Manufacturing engineer co-invention
      - Inspection and pack-integration patent expansion

  eis:
    observation:
      - Distinct six-person inventor group
    potential_risk:
      - Algorithm and hardware knowledge may remain separated from ESS field data
    mitigation:
      - GRIDON field-data feedback
      - BMS and ESS service-team integration
```

---
