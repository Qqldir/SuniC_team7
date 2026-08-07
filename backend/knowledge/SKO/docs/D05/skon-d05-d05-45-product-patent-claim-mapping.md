---
id: skon-d05-d05-45-product-patent-claim-mapping
title: Product–Patent Claim Mapping
summary: SK온 배터리 제품과 특허 기술의 기술적 연결 관계를 5단계로 평가하는 매핑 프레임워크 및 제품별 현황표.
tags: [d05, rnd, schema, table]
keywords: [특허-제품 매핑, 기술적 대응, SF+, 전고체 배터리, CTP, BaaS, GRIDON, 급속충전, 배터리 여권, 청구항 실시, 기술 연계, 청구요소, Z-Folding, 전고체]
related: []
priority: normal
domain: D05
section: D05-45.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 976
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-45. Product–Patent Claim Mapping

## 45.1 Mapping Status Vocabulary

```yaml
product_patent_mapping_status:

  DIRECT_PUBLIC_IMPLEMENTATION:
    definition: >
      제품문서 또는 특허문서가 실제 특허기술 적용을 명시

  STRONG_TECHNICAL_MATCH:
    definition: >
      공개 제품구조와 특허 청구요소가 직접 대응하나
      실제 실시 증거는 없음

  SUPPORTING_PLATFORM_IP:
    definition: >
      제품의 기반기술을 보호할 가능성이 있지만
      제품별 적용이 확인되지 않음

  RESEARCH_IP_ONLY:
    definition: >
      연구·파일럿 기술과 연결되며 제품 적용근거 없음

  NO_MAPPING:
    definition: >
      공개 제품과 연결할 근거가 없음
```

---

## 45.2 Mapping Matrix

| Product·Platform | Patent Family        | 관계등급                   | 판단                 |
| ---------------- | -------------------- | ---------------------- | ------------------ |
| SF+              | PF-D05-002 급속충전 전극   | STRONG_TECHNICAL_MATCH | 전극 저항·급속충전 구조 연계   |
| SF+              | PF-D05-017 다층 실리콘 음극 | STRONG_TECHNICAL_MATCH | 고용량층·저저항층 개념 연계    |
| Hyper Fast       | PF-D05-002           | SUPPORTING_PLATFORM_IP | SUFast 전체 알고리즘은 별도 |
| 파우치 셀            | PF-D05-001·024       | STRONG_TECHNICAL_MATCH | Z-Folding 적층구조     |
| S-Pack·S-Pack+   | PF-D05-020~022       | SUPPORTING_PLATFORM_IP | 열 차단·난연·완충 기술군     |
| CTP              | PF-D05-027~029       | STRONG_TECHNICAL_MATCH | 직접 팩 탑재·열경로·가스채널   |
| GRIDON           | PF-D05-023           | STRONG_TECHNICAL_MATCH | EIS 진단 기능과 직접 연계   |
| GRIDON           | PF-D05-007           | SUPPORTING_PLATFORM_IP | AI 이상감지 적용은 미확인    |
| BaaS             | PF-D05-005·006       | STRONG_TECHNICAL_MATCH | SOH·배터리 원장 기능 연계   |
| Battery Passport | PF-D05-006           | STRONG_TECHNICAL_MATCH | 생애주기 ID·데이터 구조     |
| 황화물 전고체          | PF-D05-011·012       | RESEARCH_IP_ONLY       | 파일럿·공동연구 단계        |
| 산화물 전고체          | PF-D05-032·033       | RESEARCH_IP_ONLY       | 광소결·LLZO 연구단계      |

```yaml
mapping_control:

  confirmed_direct_product_implementation:
    count: 0
    reason:
      - Public product documents do not cite patent numbers directly

  strong_technical_matches:
    - Z-Folding
    - Multilayer silicon anode
    - EIS diagnostics
    - Battery ledger
    - Direct-to-pack architecture

  output_rule:
    - "특허 적용 제품" 대신 "기술적으로 연결되는 특허군"으로 표현
    - Claim chart와 BOM 증거가 확보되기 전 DIRECT_PUBLIC_IMPLEMENTATION 금지
```

특허 명세서와 제품자료의 기능이 일치해도 제품이 실제로 해당 독립청구항의 모든 요소를 실시한다는 뜻은 아니다. 따라서 현재 D05에는 `DIRECT_PUBLIC_IMPLEMENTATION` 관계를 부여하지 않는다.

---
