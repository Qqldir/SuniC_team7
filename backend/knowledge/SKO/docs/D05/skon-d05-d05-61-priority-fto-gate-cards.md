---
id: skon-d05-d05-61-priority-fto-gate-cards
title: Priority FTO Gate Cards
summary: 배터리 핵심 기술 5개 분야별 특허침해 위험요소와 설계우회 전략을 정의하는 FTO 검토 프로세스 및 우선순위
tags: [d05, rnd, schema, table]
keywords: [FTO, 특허 침해 위험, 게이트 심사, 회피설계, 건식전극, 고체전지, 청구항 분석, 우선순위 프로젝트, 특허검토, 드라이전극, 전고체전지, 실리콘음극, 설계우회, 청구항, EIS, 배터리셀]
related: []
priority: normal
domain: D05
section: D05-61.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 839
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-61. Priority FTO Gate Cards

## 61.1 Gate 공통규칙

```yaml
fto_gate_rule:
  G0_landscape:
    output: Problem-specific applicant and patent-family universe
    decision: CONTINUE_OR_STOP_SEARCH
  G1_claim_screen:
    output: Current independent claims in target jurisdictions
    decision: LOW_CONCERN_OR_FULL_CHART_REQUIRED
  G2_internal_mapping:
    output: Confidential product and process element map
    decision: NO_MATCH_OR_POTENTIAL_MATCH
  G3_counsel_review:
    output: Counsel-reviewed claim chart and status packet
    decision: PROCEED_DESIGN_AROUND_LICENSE_OR_STOP
  G4_change_control:
    output: Frozen design baseline and monitoring list
    decision: LAUNCH_OR_REOPEN_FTO
```

## 61.2 Priority Project Master

| ID | 영역·자체 Reference Family | 핵심 FTO 위험요소 | G1 최소 산출물 | Design-Around 중심 |
|---|---|---|---|---|
| FTO-D05-001 | Hyper Fast Silicon Anode · PF-002/016/017 | 실리콘 구조, 다층배열, 두께·로딩, 기공률·밀도, 급속충전 Protocol 결합 | 미국 모출원·2개 분할 Claim Tree, 소재공급사 권리, 제품요소표 | 전극구조와 충전제어 분리, 공정·진단 IP |
| FTO-D05-002 | Dry Electrode · PF-003 | Binder 섬유화, 건식혼합, Free-standing Film, Lamination·Roll Pressing | EP4283698A1·EP4283697A1·EP4276933A1의 Priority·독립청구항 비교 | Inline 인장·기공률·접착 센싱, Closed-loop Calendering |
| FTO-D05-003 | Sulfide ASSB · PF-011/012 | 황화물 조성·합성, 복합양극 Binder, 리튬계면, 압력, Pilot 개량발명 | 국가별 핵심청구항, Solid Power·PolyPlus 권리 Matrix | Interface NDI, 압력센싱, 결함–수명예측 |
| FTO-D05-004 | Thermal Propagation · PF-020/021/022/025/026 | Barrier 적층, Aerogel·난연 조합, Vent·파열압력, Gas/Flame Path, Laser Notch | 소재·모듈·벤트 Claim Layer Map, Cross/H Family 분리 | Closed-loop Laser, 파열압력예측, Reworkable Pack |
| FTO-D05-005 | EIS ESS Diagnostics · PF-004/005/023 | 측정회로, Online EIS, 주파수, ECM, Z-score, 이상판정·제어 | EP 허여청구항과 US·KR·CN 계류청구항 비교, 실행위치 정의 | Multi-signal Fusion, Fleet Drift, Explainable Fault Isolation |

## 61.3 우선순위

1. **Dry Electrode** — 공정·소재·장비 권리가 겹치고 Pilot 전환투자와 직접 연결
2. **Sulfide ASSB** — 자체 IP와 Partner Background IP·공동개량이 중첩
3. **Hyper Fast Silicon Anode** — 소재 공급사 권리와 셀·충전기술 분리 필요
4. **Thermal Propagation Barrier** — 안전성능과 회피설계를 함께 검증
5. **EIS ESS Diagnostics** — 소프트웨어 실행위치와 진단로직이 권리범위에 영향

---
