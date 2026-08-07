---
id: skes-d05-15-preliminary-ip-risk-and-fto-scope
title: Preliminary IP Risk and FTO Scope
summary: "지식재산권 개발 프로젝트의 15개 리스크와 선행조치, 자유실시권 검토 범위를 규정한 IP 레지스터."
tags: [d05, rnd, schema, table]
keywords: [특허침해, 지식재산, 라이선스, 자유실시권, 권리귀속, 발명자, 개인정보, FTO, 공동특허]
related: [IPR-ENS-001, IPR-ENS-002, IPR-ENS-003, IPR-ENS-004, IPR-ENS-005, IPR-ENS-006, IPR-ENS-007, IPR-ENS-008, IPR-ENS-009, IPR-ENS-010, IPR-ENS-011, IPR-ENS-012, IPR-ENS-013, IPR-ENS-014, IPR-ENS-015]
priority: normal
domain: D05
section: 15
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 761
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 15. Preliminary IP Risk and FTO Scope

## 15.1 Risk Register

| Risk ID | 위험 | 영향 | 선행조치 | Gate |
|---|---|---|---|---|
| `IPR-ENS-001` | 합병 후 명의변경·승계 지연 | 권리자 혼동 | 공식 등록부·합병서류 | RIGHTS |
| `IPR-ENS-002` | 공동특허 단독실시 가정 | 계약분쟁 | 공동권리자·계약 검토 | RIGHTS |
| `IPR-ENS-003` | EverCharge IP를 E&S 직접발명으로 오기 | 데이터 왜곡 | acquisition timeline | ATTRIBUTION |
| `IPR-ENS-004` | KCE proprietary를 특허로 단정 | 보호전략 오류 | patent+copyright+trade-secret audit | IP_FORM |
| `IPR-ENS-005` | Honeywell·Plug 기술을 자체IP로 오기 | 라이선스 침해 | partner background-IP map | LICENSE |
| `IPR-ENS-006` | OEM 발전설비 데이터 사용 제한 | AI PoC 중단 | OEM data/cloud contract | DATA |
| `IPR-ENS-007` | 고객·AMI 데이터 목적 외 사용 | 개인정보·신뢰 | consent·de-identification | PRIVACY |
| `IPR-ENS-008` | 시장데이터 재배포·학습 제한 | KCE 모델 확장 제약 | vendor license | DATA |
| `IPR-ENS-009` | CCS 지하데이터·MRV 책임 불명확 | 허가·장기책임 | consortium terms | PROJECT |
| `IPR-ENS-010` | AI 추천이 안전제어로 전환 | 사고책임 | advisory boundary·MOC | SAFETY |
| `IPR-ENS-011` | 공동PoC 개선발명 귀속 미합의 | 상용화 지연 | foreground/improvement clause | COLLAB |
| `IPR-ENS-012` | 특허 공개 전 논문·보도 | 신규성 손실 | publication review | FILING |
| `IPR-ENS-013` | 발명자 기여기록 부족 | 소유권 취약 | lab notebook·commit·decision log | INVENTORSHIP |
| `IPR-ENS-014` | 특허만 있고 제품 실시증거 없음 | 과대평가 | claim-to-system map | IMPLEMENTATION |
| `IPR-ENS-015` | 타국 계속출원·경쟁사 특허 미반영 | FTO 위험 | approved-project landscape | FTO |

## 15.2 FTO 허용·금지

```yaml
permitted_in_D05:
  - targeted_landscape
  - family_and_assignee_normalization
  - preliminary_claim_theme
  - inventor_and_partner_network
  - white_space_hypothesis
  - identify_need_for_counsel
not_permitted:
  - final_noninfringement_conclusion
  - invalidity_or_enforceability_opinion
  - commercial_launch_clearance
  - license_need_conclusion_without_claim_chart
commercial_gate_requires:
  - final_product_or_process_spec
  - jurisdiction_and_launch_date
  - active_claim_set
  - counsel_review
  - design_around_or_license_decision
```

---
