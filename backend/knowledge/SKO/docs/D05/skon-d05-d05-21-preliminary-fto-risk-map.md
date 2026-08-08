---
id: skon-d05-d05-21-preliminary-fto-risk-map
title: Preliminary FTO Risk Map
summary: "SK온 배터리 기술의 특허 침해 위험도를 영역별으로 평가하는 기준, 현황, 분석 절차를 제시한 자료입니다."
tags: [d05, rnd, schema, table]
keywords: [FTO, 특허침해 위험, 청구항 분석, 비침해설계, 실리콘 음극, 고전압 전해액, 건식전극, 배터리 IP 경쟁, 특허 회피, 라이선스 전략, 특허침해, 배터리기술, 실리콘음극, 고전압전해액, Claim Chart, 회피설계, 경쟁사특허, 기술평가]
related: []
priority: normal
domain: D05
section: D05-21.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1036
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-21. Preliminary FTO Risk Map

> 아래 내용은 법률의견이 아니라 공개 특허 기반의 기술적 사전 스크리닝이다.

## 21.1 FTO Risk Vocabulary

```yaml
fto_risk_level:

  VERY_HIGH:
    - 다수 경쟁사 핵심특허가 밀집
    - 제품 출시 전 청구항 차트 필수

  HIGH:
    - SK온 자체 특허가 있으나 경쟁사 유사특허도 다수 존재
    - 국가별 유효 청구항 비교 필요

  MEDIUM:
    - 상대적으로 차별화된 구조
    - 공정·소재 공급사 특허 검토 필요

  LOW:
    - 공개근거상 직접 중첩 가능성이 낮음
    - 완전한 비침해를 의미하지 않음
```

---

## 21.2 Risk Assessment

| 기술영역          | 잠정 FTO 위험 | 주요 이유                               |
| ------------- | --------: | ----------------------------------- |
| 실리콘 다층 음극     |     매우 높음 | LGES·Samsung·CATL 등 유사 다층·실리콘 IP 밀집 |
| 고전압 전해액       |     매우 높음 | 첨가제 조성·농도·계면층 청구가 광범위               |
| 건식전극          |     매우 높음 | 바인더 섬유화·건식필름·롤프레싱 특허 밀집             |
| 열전파 차단재       |        높음 | 에어로젤·내화시트·완충재 조합 경쟁 심화              |
| Z-Folding     |        높음 | 장비·전극 치수·정렬·권취 세부구조 특허 존재           |
| EIS 진단        |        높음 | 측정회로·운전 중 측정·ECM·이상판정 특허 중첩 가능      |
| 배터리 원장·여권     |        높음 | 데이터 객체·ID·블록체인·접근권한 특허 다수 가능        |
| On-Vent       |     중간~높음 | 레이저 노치와 파열압력 제어의 경쟁사 권리 검토 필요       |
| 리튬메탈 인공계면     |     매우 높음 | 소재·처리·적층·압력 관련 대학·스타트업 특허 밀집        |
| AI Researcher |        중간 | 핵심 데이터는 영업비밀 가능, 범용 AI 특허와 충돌 검토    |

---

## 21.3 FTO Analysis Workflow

```text
SK온 목표제품 정의
        ↓
제품·공정별 필수 기술요소 분해
        ↓
국가·생산지·판매지 결정
        ↓
경쟁사 유효 특허 검색
        ↓
독립청구항 요소별 Claim Chart
        ↓
비침해 설계 가능성 평가
        ↓
무효자료·선행기술 검토
        ↓
라이선스·공동개발·회피설계 결정
```

```yaml
priority_fto_projects:

  - project_id: FTO-D05-001
    technology: Hyper Fast Silicon Anode
    countries:
      - KR
      - US
      - EP
      - CN
    priority: VERY_HIGH

  - project_id: FTO-D05-002
    technology: Dry Electrode
    countries:
      - KR
      - US
      - EP
    priority: VERY_HIGH

  - project_id: FTO-D05-003
    technology: Sulfide ASSB
    countries:
      - KR
      - US
      - EP
      - JP
    priority: VERY_HIGH

  - project_id: FTO-D05-004
    technology: Thermal Propagation Barrier
    countries:
      - US
      - EP
      - KR
    priority: HIGH

  - project_id: FTO-D05-005
    technology: EIS-Based ESS Diagnostics
    countries:
      - US
      - EP
      - KR
    priority: HIGH
```

---
