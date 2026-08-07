---
id: skes-d05-4-r-d-operating-model
title: R&D Operating Model
summary: "R&D 조직 구조(5계층), 승인 게이트(7단계), 결과물 보호 전략을 정의한 SK이노베이션의 R&D 운영 체계"
tags: [d05, rnd, schema, table]
keywords: [governance gate, R&D 게이트, 도메인센터, 자산운영, 지식재산보호, 특허, POC, FTO, HAZOP, 영업비밀]
related: []
priority: normal
domain: D05
section: 4
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 890
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 4. R&D Operating Model

## 4.1 분산형 연구개발 구조

```yaml
rnd_model: DISTRIBUTED_BUSINESS_LED_AND_PARTNERED
layers:
  L1_corporate_strategy:
    owner: E&S_CIC_business_and_technology_leadership
    role: portfolio_priority_and_capital_gate
  L2_domain_center:
    confirmed_example: Net_Zero_Technology_Center
    role: decarbonization_technology_screening_and_demonstration
  L3_asset_operator:
    examples: LNG_power_city_gas_hydrogen_renewable_assets
    role: problem_definition_data_pilot_safety_acceptance
  L4_affiliate_technology:
    examples: KCE_EverCharge_SK_Plug_HyVerse
    role: software_hardware_market_and_hydrogen_capability
  L5_external_partner:
    examples: KIER_CE_TECH_Honeywell_Plug_Power_Santos
    role: core_technology_license_joint_development_and_scaleup
```

## 4.2 연구개발 Governance Gate

| Gate | 질문 | 필수 증거 | 실패 시 처리 |
|---|---|---|---|
| `G0_NEED` | 현장 문제와 KPI가 명확한가 | baseline·owner·손실 | 아이디어 보류 |
| `G1_TECH` | 기술 원리와 적용경계가 검증됐는가 | lab·reference·risk | 벤치/오프라인 검증 |
| `G2_DATA` | 데이터 접근·품질·권리가 있는가 | data catalog·consent·license | 데이터 계약 선행 |
| `G3_IP` | 배경IP·성과IP·개량권이 합의됐는가 | term sheet·inventorship process | 공동개발 착수 금지 |
| `G4_SAFETY` | 공정·전기·가스·수소·사이버 안전을 통과했는가 | HAZOP·MOC·cyber review | closed-loop 금지 |
| `G5_POC` | PoC가 baseline 대비 개선했는가 | KPI·통계·운영자 승인 | 종료 또는 재설계 |
| `G6_SCALE` | 타 자산·법인에 재사용할 권리가 있는가 | deployment license·data boundary | 한 사이트 한정 |
| `G7_COMMERCIAL` | 상용 FTO·책임·지원체계가 확보됐는가 | counsel·warranty·SLA | 구매·투자 보류 |

## 4.3 연구성과 보호 매트릭스

| 성과물 | 1차 보호수단 | 보조 보호 | 핵심 통제 |
|---|---|---|---|
| 공정 장치·제어 구성 | 특허 | 영업비밀 | 공개 전 출원 |
| 운전조건·튜닝값 | 영업비밀 | 접근통제 | 최소공개·현장분리 |
| AI 모델 구조 | 특허 또는 영업비밀 | 저작권 | 경쟁사 역설계 가능성 평가 |
| 소스코드 | 저작권·영업비밀 | 계약 | repository·SBOM·license scan |
| 학습·운영 데이터 | 계약·DB 권리 | 영업비밀 | 목적·보존·재사용 범위 |
| 모델 가중치·feature | 영업비밀 | 계약 | 반출·재학습·파생모델 규칙 |
| 보고서·도면 | 저작권 | 비밀유지 | 배포등급·워터마크 |
| 상표·서비스명 | 상표 | 도메인 | 지역·상품류 등록 |
| 현장 개선 아이디어 | 발명신고 | 노하우 | inventorship·기여기록 |

---
