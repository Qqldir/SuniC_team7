---
id: skes-d01-11-해외-네트워크-식별
title: 해외 네트워크 식별
summary: SK이노베이션 E&S의 해외 자회사 및 거점을 Entity ID로 매핑한 조직 현황표와 엔티티 관리 규칙
tags: [d01, identity, table, "xref:d02"]
keywords: [PRISM Energy, LNG Americas, PassKey, 자회사, 지역사무소, 해외거점, CCS, 아시아사업, 분산에너지, SK이노베이션, Entity ID, 국제 사업, 트레이딩]
related: [ORG-ENS-OV-001, ORG-ENS-OV-002, ORG-ENS-OV-003, ORG-ENS-OV-004, ORG-ENS-OV-005, ORG-ENS-OV-006, SITE-ENS-OV-001, SITE-ENS-OV-002]
priority: normal
domain: D01
section: 11
source: SK이노베이션E&S_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 470
updated: 2026-08-06
---

> SK이노베이션 E&S · D01 기업 기본정보·법인구조·연혁

# 11. 해외 네트워크 식별

| Entity ID | 명칭 | 국가·도시 | 대표 기능 추정 | 검증상태 |
|---|---|---|---|---|
| `ORG-ENS-OV-001` | LNG Americas, Inc. | 미국 휴스턴 | 북미 LNG 사업 | Official listing |
| `ORG-ENS-OV-002` | PRISM Energy International China Ltd. | 중국 베이징 | 중국 사업 | Official listing |
| `ORG-ENS-OV-003` | PRISM Energy International Australia Pty. Ltd. | 호주 퍼스 | 호주 가스·CCS 사업 | Official listing |
| `ORG-ENS-OV-004` | PRISM Energy International Pte. Ltd. | 싱가포르 | 아시아 사업·트레이딩 | Official listing |
| `ORG-ENS-OV-005` | PT. PRISM Nusantara International | 인도네시아 자카르타 | 인도네시아 사업 | Official listing |
| `ORG-ENS-OV-006` | PassKey, Inc. | 미국 뉴욕 | 분산에너지·솔루션 | Official listing |
| `SITE-ENS-OV-001` | UK Office | 영국 런던 | 해외 거점 | Legal entity not shown |
| `SITE-ENS-OV-002` | Vietnam Office | 베트남 호찌민 | 해외 거점 | Legal entity not shown |

### 해외 엔티티 처리 규칙

- 홈페이지가 주소만 제시하고 법인명을 제시하지 않으면 `Site`로 저장한다.
- PRISM 계열 명칭은 국가별 별도 법인으로 유지한다.
- 프로젝트 지분법인과 지역사무소를 동일 법인으로 추정하지 않는다.
- KCE 등 주요 해외 투자자산은 D02·D13에서 별도 Entity Master로 확장한다.

([SRC-ENS-D01-0010])

---
