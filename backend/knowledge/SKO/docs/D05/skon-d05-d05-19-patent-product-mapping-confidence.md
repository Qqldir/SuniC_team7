---
id: skon-d05-d05-19-patent-product-mapping-confidence
title: Patent–Product Mapping Confidence
summary: "SK온의 특허 포트폴리오가 배터리 제품(SF+, S-Pack, GRIDON 등)에 어떻게 기술 연계되는지 보여주는 특허-제품 매핑표와 확신도 평가 기준"
tags: [d05, rnd, schema, table]
keywords: [배터리 특허 포트폴리오, 제품 기술 매핑, SF+, S-Pack+, 하이니켈 NCM, 신뢰도 평가, GRIDON, 특허 활용, 고전압 셀, 음극 기술, 특허-제품 매핑, 배터리 기술, 하이니켈, 기술 연계, S-Pack, 파우치 셀, 지식재산 전략]
related: []
priority: normal
domain: D05
section: D05-19.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 524
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-19. Patent–Product Mapping Confidence

| Patent Family  | 연결 제품·서비스      | 관계             |   확신도 |
| -------------- | -------------- | -------------- | ----: |
| PF-D05-002     | SF+·Hyper Fast | 기술구조 유사        |    높음 |
| PF-D05-013     | 하이니켈 NCM 제품군   | 핵심 소재기술        |    높음 |
| PF-D05-014     | 고전압 셀 플랫폼      | 지원기술           |    중간 |
| PF-D05-015     | 미드니켈·하이니켈 후보   | 적용 가능성         | 낮음~중간 |
| PF-D05-017     | SF+            | 이중층 음극 직접 연계   |    높음 |
| PF-D05-020~022 | S-Pack·S-Pack+ | 안전기술군 연계       |    중간 |
| PF-D05-023     | GRIDON         | EIS 기능 직접 연계   | 매우 높음 |
| PF-D05-024     | 파우치 셀 제품군      | Z-Folding 개선기술 |    높음 |

```yaml
mapping_vocabulary:

  PATENT_APPLIED_TO_PRODUCT:
    requirement:
      - 제품문서나 특허문서가 실제 적용을 직접 확인

  PATENT_TECHNICALLY_LINKED:
    requirement:
      - 기술구조와 청구항이 직접 대응
      - 제품 적용은 별도 미확인

  PATENT_POSSIBLY_SUPPORTS:
    requirement:
      - 기술적 적용 가능성만 존재

  NO_PRODUCT_MAPPING:
    requirement:
      - 연구·기초 IP
      - 제품 연결근거 없음
```

현재 대부분의 공개 특허는 제품명을 직접 기재하지 않으므로, `SF+`, `S-Pack+`, `GRIDON`과의 연결은 제품기술 설명과 청구범위가 얼마나 직접 일치하는지를 기준으로 신뢰도를 부여해야 한다.

---
