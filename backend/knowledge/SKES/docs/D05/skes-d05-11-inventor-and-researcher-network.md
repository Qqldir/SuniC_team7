---
id: skes-d05-11-inventor-and-researcher-network
title: Inventor and Researcher Network
summary: "CO₂ 포집, 도시가스 계량, EV 충전 등 분야별 핵심 발명자 12명의 특허 이력과 SK E&S의 외부 협력 네트워크를 매핑한 마스터 테이블"
tags: [d05, rnd, schema, table]
keywords: [CO₂ 포집, CCS, 도시가스, 계량·검침, EV 충전, 특허 포트폴리오, 협력기관, 발명자]
related: [INV-ENS-001, INV-ENS-002, INV-ENS-003, INV-ENS-010, INV-ENS-011, INV-ENS-012, INV-ENS-013, INV-ENS-014, INV-ENS-020, INV-ENS-021, INV-ENS-022, INV-ENS-023]
priority: normal
domain: D05
section: 11
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 837
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 11. Inventor and Researcher Network

## 11.1 Inventor Master

| Person ID | 이름 | 확인된 특허군 | 기술축 | 네트워크 의미 |
|---|---|---|---|---|
| `INV-ENS-001` | 김순호 | CCS-001/002 | CO₂ 포집 | 최신 직접 출원 핵심 발명자군 |
| `INV-ENS-002` | 김정환 | CCS-001/002 | CO₂ 포집 | 동일 패밀리 공동발명 |
| `INV-ENS-003` | 오세영 | CCS-001/002 | CO₂ 포집 | 동일 패밀리 공동발명 |
| `INV-ENS-010` | 양기모 | CG-002/003 | 계량·온압보정 | 두 세대 계량기술 연결 |
| `INV-ENS-011` | 최순진 | CG-003/004 | 원격검침·열량 | 공동개발 연속성 |
| `INV-ENS-012` | 박찬호 | CG-003 | 원격검침 | 도담 협력군 |
| `INV-ENS-013` | 한상진 | CG-004 | 열량·부피환산 | 충청·도담 공동군 |
| `INV-ENS-014` | 김상우 | CG-004 | 열량·부피환산 | 충청·도담 공동군 |
| `INV-ENS-020` | Jason Appelbaum | EVC-001/002 및 관련 | EV 충전·부하 | EverCharge 핵심 발명자 |
| `INV-ENS-021` | Mario Landau-Holdsworth | EVC-001 | EV 충전분배 | 초기 SmartPower 계열 |
| `INV-ENS-022` | Amber Case | EVC-001 | EV 충전분배 | 초기 SmartPower 계열 |
| `INV-ENS-023` | John Loren Passmore | EVC-002 | 부하관리 | 후속 SmartPower 계열 |

## 11.2 Collaboration Graph

```yaml
edges:
  - [SK_E&S, CO2_capture_R&D, KIER]
  - [SK_E&S, CO2_capture_R&D, CE_TECH]
  - [SK_E&S, ASCC_demonstration, Honeywell_UOP]
  - [SK_E&S, CCS_feasibility, Santos]
  - [SK_E&S, hydrogen_JV, Plug_Power]
  - [SK_E&S, R&D_support, hydrogen_drone_startups]
  - [SK_E&S, acquired_capability, EverCharge]
  - [SK_E&S, acquired_capability, Key_Capture_Energy]
  - [SK_E&S, co_patent, Busan_City_Gas]
  - [SK_E&S, co_patent, Chungcheong_Energy_Service]
  - [SK_E&S, co_patent, Dodam_Energy_Systems]
```

## 11.3 Network Interpretation

- CO₂ 포집 발명자 3인은 2022년 동일 우선일의 두 특허에 공동으로 등장한다. 이는 단일 아이디어의 대체 실시형태 또는 병렬 보호전략일 가능성이 있으나, 내부 과제구조는 공개자료만으로 확정하지 않는다.
- 양기모·최순진이 계량·원격검침 관련 복수 특허군에 연결되어 있어 도시가스 디지털 계량 역량의 연속성을 시사한다.
- EverCharge의 Jason Appelbaum은 초기 에너지 분배 특허와 후속 스마트 부하관리 특허에 함께 나타나 제품 핵심기술의 발명 연속성을 보여준다.
- 발명자가 현재 재직 중이라는 의미는 아니며, 인력 유지·접근 가능성은 별도 확인해야 한다.

---
