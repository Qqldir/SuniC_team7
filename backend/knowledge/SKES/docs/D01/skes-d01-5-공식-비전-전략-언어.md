---
id: skes-d01-5-공식-비전-전략-언어
title: 공식 비전·전략 언어
summary: "E&S 공식 기업정체성, 성장축, 솔루션축을 정의하는 6개의 비전 표현과 목표값·파이프라인·실적을 구분하는 저장 규칙을 기술하는 표와 가이드"
tags: [d01, identity, schema, table]
keywords: [Sustainable Energy Solution Optimizer, LNG 가치사슬 확대, Net Zero 2040, 분산전원 솔루션, 저탄소 전원 믹스, 에너지 솔루션 패키지, SKMS, SUPEX, CIC 독립성, 전력 가치사슬 통합, LNG Value Chain Expansion, Energy Solution Package, 목표값·파이프라인·실적 구분, 재생에너지 파이프라인, 저탄소 전원, SKMS SUPEX, CIC]
related: [VISION-ENS-001, VISION-ENS-002, VISION-ENS-003, VISION-ENS-004, VISION-ENS-005, VISION-ENS-006]
priority: normal
domain: D01
section: 5
source: SK이노베이션E&S_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 783
updated: 2026-08-06
---

> SK이노베이션 E&S · D01 기업 기본정보·법인구조·연혁

# 5. 공식 비전·전략 언어

## 5.1 핵심 공식 표현

| ID | 공식·준공식 표현 | 유형 | 저장 규칙 |
|---|---|---|---|
| `VISION-ENS-001` | Sustainable Energy Solution Optimizer | 공식 기업 정체성 | Exact phrase |
| `VISION-ENS-002` | LNG Value Chain Expansion | 핵심 성장축 | Official concept |
| `VISION-ENS-003` | Global Power Value Chain Integration Solution | 핵심 솔루션축 | Official concept |
| `VISION-ENS-004` | Energy Solution Package | 합병 시너지 표현 | Official concept |
| `VISION-ENS-005` | Low-carbon LNG | 전환 전략 | Official concept |
| `VISION-ENS-006` | Net Zero 2040 | E&S 기후목표 | Official target; boundary check required |

## 5.2 비전 구조

```text
LNG Value Chain
  + Diverse Low-carbon Power Mix
  + Global Power Value Chain Integration
  + Customer/Region-specific Distributed Energy Package
  = Sustainable Energy Solution Optimizer
```

공식 기업소개는 LNG, 재생에너지, 수소 등 다양한 저탄소 전원과 송배전·ESS·소프트웨어·EV 관련 역량을 연결해 지역과 고객 특성에 맞는 분산전원 솔루션을 제공하는 구조를 제시한다. 이는 현재 E&S CIC의 사업영역을 정의하는 최상위 Ontology로 사용한다. ([SRC-ENS-D01-0002])

## 5.3 목표와 사실의 구분

- `5GW 재생에너지 파이프라인`: 특정 기준일의 공식 발표값이며 운영용량이 아니다.
- `매년 약 1GW 파이프라인 추가`: 회사의 계획·방향이며 확정 CAPEX나 준공실적이 아니다.
- `10GW 성장 목표`: 목표값으로 저장하고 현재 보유·운영량과 구분한다.
- `Net Zero 2040`: 목표 경계가 E&S 사업, 연결 자회사, Scope 1+2 중 어디까지인지 원문 단위로 확인한다.

---

# 6. 경영철학과 SKMS

E&S CIC는 SK그룹과 SK이노베이션의 경영철학인 SKMS와 SUPEX 추구체계 안에서 운영된다. 합병 공식 발표에서도 독립 CIC 구조를 통한 기존 경쟁력 유지와 함께 `One Team`, 고객 기반 확대, 에너지 솔루션 패키지 개발이 강조됐다. ([SRC-ENS-D01-0001])

```yaml
management_system:
  group_philosophy: SKMS
  key_behavioral_concept: SUPEX
  operating_principles:
    - CIC autonomy
    - shared resource utilization
    - portfolio synergy
    - customer-specific solution
    - stability and growth
fact_status: official_and_structured_analysis
```

---
