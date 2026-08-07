---
id: skon-d05-d05-dq-006-benchmark-method-source-grade-correc
title: 006. Benchmark Method & Source Grade Correction
summary: 특허 자료 출처의 신뢰도 등급 재정의와 기술영역 내 권리층 다양성을 측정하는 청구항 밀도의 정의 및 척도를 제시하는 방법론 문서.
tags: [d05, rnd, schema]
keywords: [source_grade, claim density, 학술논문, 특허 등록부, 신뢰도 등급, 특허족, KIPRIS, evidence level, 기술영역, 권리층, peer-reviewed paper, Google Patents, Claim Density, 청구항 밀도, 특허 출처]
related: [D05-DQ-004]
priority: normal
domain: D05
section: D05-DQ
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 737
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# SK온 D05 R&D, Patents & Intellectual Property

## Part 8. Competitor Patent Landscape·Claim-Density Benchmark·Design-Around Map

**문서 버전:** D05 v1.7
**기준일:** 2026-08-02
**이전 완료 지점:** `D05-48 IP Strategy OI Seeds`

---

# D05-DQ-006. Benchmark Method & Source Grade Correction

## 1. Peer-Reviewed Paper 등급 재정규화

기존 `D05-DQ-004`에서 학술논문의 `source_grade`를 A로 입력했으나, 프로젝트 공통 기준에 따라 다음과 같이 수정한다.

```yaml
source_grade_correction:

  peer_reviewed_paper:
    previous_source_grade: A
    corrected_source_grade: A_PLUS
    evidence_level: THIRD_PARTY_VERIFIED

  official_company_page:
    source_grade: A
    evidence_level: DIRECT_OFFICIAL

  patent_document_mirror:
    example:
      - Google Patents
    source_grade: A
    evidence_level: DOCUMENT_TEXT_REPRODUCTION

  official_patent_register:
    examples:
      - KIPRIS
      - USPTO Patent Center
      - European Patent Register
      - WIPO PATENTSCOPE
    source_grade: A_PLUS
    evidence_level: DIRECT_REGULATORY
```

Google Patents는 출원인·우선일·법적 상태가 법적 판단이 아니며 정확성을 보증하지 않는다고 각 문서에 명시한다. 따라서 이번 경쟁사 분석에서도 기술내용·청구항 탐색에는 사용하지만, 권리 존속과 현재 소유권은 공식 등록부 감사 전까지 확정하지 않는다. ([구글 특허][1])

---

## 2. Claim Density 정의

이번 D05의 `Claim Density`는 기업별 전체 특허 수를 뜻하지 않는다.

```yaml
sample_claim_density:

  definition: >
    이번 조사에서 확인한 대표 Patent Family가
    하나의 기술영역 안에서 얼마나 다양한 권리층을
    형성하는지를 나타내는 표본 기반 분석지표

  dimensions:
    - Material composition
    - Electrode or component structure
    - Manufacturing process
    - Equipment and process control
    - Cell or pack architecture
    - Diagnostics and software
    - Continuation or divisional breadth
    - Geographic family coverage

  scale:
    5: Very dense and multilayered
    4: Dense
    3: Moderate
    2: Limited in reviewed sample
    1: Single narrow archetype

  prohibited_interpretation:
    - Global patent-count ranking
    - Patent quality ranking
    - Legal strength ranking
    - Freedom-to-operate conclusion
```

---
