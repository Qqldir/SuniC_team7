---
id: skes-d05-17-joint-development-ip-playbook
title: Joint Development IP Playbook
summary: 공동개발 프로젝트의 지식재산권 계약에서 필요한 11개 필수 필드와 협력 유형별 권고 계약 구조를 정의한 실무 플레이북이다.
tags: [d05, rnd, schema, table]
keywords: [공동개발, 지식재산 계약, 배경기술, 성과기술, 개선기술, 라이선스, 협력모델, 발명권, 데이터 규약, 상용화]
related: []
priority: normal
domain: D05
section: 17
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 494
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 17. Joint Development IP Playbook

## 17.1 계약 필수 필드

| Field | 정의 | 최소 요구 |
|---|---|---|
| Background IP | 착수 전 각자 보유 | 목록·소유자·사용허락 |
| Foreground IP | 공동과제로 발생 | 발명기여 기반 귀속·비용 |
| Improvement IP | 배경기술 개량 | 소유·실시·제3자 라이선스 |
| Data | 원천·정제·라벨·파생 | 목적·보존·반출·재학습 |
| Model/Code | 코드·가중치·feature | repository·license·escrow |
| Inventorship | 법률상 발명자 | 기여기록·검토절차 |
| Publication | 논문·보도·데모 | 사전검토·출원유예 |
| Field/Region | 사업·지역·고객 | 독점·비독점·계열사 포함 |
| Commercialization | 구매·판매·SaaS | 가격·SLA·지원·보증 |
| Exit | 종료·파트너 부도 | 데이터반환·계속사용·escrow |
| Liability | 안전·성능·침해 | 책임·보험·면책 |

## 17.2 협력유형별 권고

```yaml
collaboration_models:
  startup_PoC:
    preferred: startup_background_IP_plus_E&S_site_data_plus_negotiated_foreground_license
    avoid: automatic_transfer_of_all_startup_IP
  public_institute:
    preferred: contribution_based_joint_or_field_license
    include: government_R&D_rules
  global_vendor:
    preferred: site_license_plus_integration_improvement_right
    include: performance_warranty_and_exit
  affiliate:
    preferred: documented_internal_license_and_data_processing_terms
    avoid: assuming_group_membership_equals_free_use
  consortium_CCS:
    preferred: project_IP_data_MRV_and_long_term_liability_schedule
```

---
