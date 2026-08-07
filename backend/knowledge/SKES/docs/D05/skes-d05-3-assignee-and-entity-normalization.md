---
id: skes-d05-3-assignee-and-entity-normalization
title: Assignee and Entity Normalization
summary: "SK이노베이션 E&S 그룹사의 표준 권리자명, 관계 분류, IP 귀속 기본값을 정리하고 2024년 합병 후 특허 소유권 처리 규칙을 제시한다."
tags: [d05, rnd, schema, table]
keywords: [권리자정규화, 법인표준명, IP귀속, 합병승계, SK이노베이션, 도시가스, 자회사, 특허권리자]
related: [ASG-ENS-0001, ASG-ENS-0002, ASG-ENS-0003, ASG-ENS-0101, ASG-ENS-0102, ASG-ENS-0103, ASG-ENS-0104, ASG-ENS-0105, ASG-ENS-0106, ASG-ENS-0201, ASG-ENS-0202, ASG-ENS-0203, ASG-ENS-0301, ASG-ENS-0302, ASG-ENS-0303, ASG-ENS-0304, ASG-ENS-0305]
priority: normal
domain: D05
section: 3
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 989
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 3. Assignee and Entity Normalization

## 3.1 Canonical Assignee Master

| Assignee ID | Canonical name | 변형·과거명 | 관계 | IP 귀속 기본값 |
|---|---|---|---|---|
| `ASG-ENS-0001` | SK E&S Co., Ltd. | 에스케이이엔에스 주식회사, SK E&S Co Ltd | 2024-11-01 이전 법인 | `OWNED_DIRECT_HISTORICAL` |
| `ASG-ENS-0002` | SK Innovation Co., Ltd. | SK이노베이션 주식회사 | 합병 존속법인 | 승계 여부 공식 등록 확인 |
| `ASG-ENS-0003` | SK Innovation E&S CIC | SK이노베이션 E&S | 사내회사·브랜드 | 별도 법인 assignee로 자동 간주 금지 |
| `ASG-ENS-0101` | Busan City Gas Co., Ltd. | 부산도시가스, Pusan City Gas | 도시가스 관계사 | `AFFILIATE_OR_CO_OWNED` |
| `ASG-ENS-0102` | Chungcheong Energy Service Co., Ltd. | 충청에너지서비스 | 도시가스 관계사 | `AFFILIATE_OR_CO_OWNED` |
| `ASG-ENS-0103` | Ko-one Energy Service Co., Ltd. | 코원에너지서비스 | 도시가스 관계사 | 검색 별도 수행 |
| `ASG-ENS-0104` | Jeonbuk Energy Service Co., Ltd. | 전북에너지서비스 | 도시가스 관계사 | 검색 별도 수행 |
| `ASG-ENS-0105` | Gangwon City Gas Co., Ltd. | 강원도시가스 | 도시가스 관계사 | 검색 별도 수행 |
| `ASG-ENS-0106` | Yeongnam Energy Service Co., Ltd. | 영남에너지서비스 | 도시가스 관계사 | 검색 별도 수행 |
| `ASG-ENS-0201` | EverCharge, Inc. | Evercharge Inc, GreenIT! Inc | E&S 인수 자회사 | `AFFILIATE_OWNED` |
| `ASG-ENS-0202` | Key Capture Energy, LLC | KCE | E&S 에너지솔루션 자회사 | `AFFILIATE_PROPRIETARY` |
| `ASG-ENS-0203` | SK Plug HyVerse Co., Ltd. | SK Plug Hyverse | Plug Power JV | `JV_CONTROLLED_OR_LICENSED` |
| `ASG-ENS-0301` | CE TECH Co., Ltd. | 씨이텍 | CO₂ 포집 파트너 | `PARTNER_TECH_OR_JOINT` |
| `ASG-ENS-0302` | Korea Institute of Energy Research | 한국에너지기술연구원, KIER | 연구기관 | `PARTNER_OR_JOINT` |
| `ASG-ENS-0303` | Honeywell UOP | Honeywell | 포집기술 파트너 | `PARTNER_TECH` |
| `ASG-ENS-0304` | Plug Power Inc. | Plug | 수소기술 파트너 | `PARTNER_TECH_JV_LICENSE` |
| `ASG-ENS-0305` | Santos Ltd. | Santos | Barossa·CCS 파트너 | `PROJECT_JOINT_RIGHTS` |

## 3.2 합병 후 특허 승계 처리

```yaml
merger_event:
  effective_date: 2024-11-01
  absorbed_entity: ASG-ENS-0001
  surviving_entity: ASG-ENS-0002
  operating_identity: ASG-ENS-0003
rules:
  - Historical filings retain filing-time applicant name.
  - Current ownership must be refreshed in the official register.
  - CIC name is not assumed to be a separate legal assignee.
  - Assignment lag after merger is recorded as REGISTRY_LAG, not ownership denial.
  - Security interest, pledge, exclusive license and co-owner consent are separate fields.
```

## 3.3 검색 제외어

```yaml
false_positive_controls:
  - exclude SK hynix, SK telecom, SK on and SK geo centric unless co-assignee is explicit
  - exclude similar acronym ENS unrelated to SK
  - exclude citations merely mentioning an SK E&S patent
  - exclude a technology partner patent unless contract or E&S collaboration is explicit
  - do not count national-stage publications as separate inventions
  - group continuation, divisional and family members before counting
```

---
