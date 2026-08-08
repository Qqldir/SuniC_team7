---
title: 기업 지식 베이스 재구성 플로우
version: 1.1
updated: 2026-08-06
strategy: ./llm-agent-knowledge-strategy.md
---

# 기업 지식 베이스 재구성 플로우

계열사 원본 DB 를 [LLM 에이전트 지식 베이스 설계 전략](./llm-agent-knowledge-strategy.md)에
맞춰 3계층 구조로 재구성하고, 과제 발굴 agent 에 연결하는 파이프라인.

> **원본 DB 는 사내 자산이라 저장소에 포함되지 않습니다.** 저장소에는 빌드 결과인
> `backend/knowledge/` 만 들어 있습니다. 아래 `tools.kb_build` 실행 절차는 원본
> (`../../DB_SK_ON` · `../../DB_SK_E&S`)을 가진 환경에서만 재현됩니다.

현재 두 계열사가 올라가 있다.

| 코드 | 회사 | 원본 | 문서 | 시드 | 커버리지 |
|---|---|---|---:|---:|---:|
| `SKO` | SK온 | `DB_SK_ON/` 18파일 · 69만 토큰 | 742 | 24 | 100.00% |
| `SKES` | SK이노베이션 E&S | `DB_SK_E&S/` 18파일 · 40만 토큰 | 378 | 18 | 100.00% |

파이프라인은 회사를 모른다. 회사마다 다른 값은 전부
[companies.py](../backend/tools/kb_build/companies.py) 의 프로파일에 모여 있고,
계열사를 추가할 때 손대는 파일도 그것 하나다 (§6).

---

## 1. 원본 진단 (SK온 기준)

| 항목 | 값 |
|---|---|
| 파일 | 18개 (D00~D17) |
| 분량 | 2.32M자 · 55,769줄 · 약 **69만 토큰** |
| 헤딩 | H1 422 / H2 1,545 / H3 621 |

전략을 그대로 적용할 수 없는 지점이 네 군데 있었다.

### 1.1 "H2 단위로 분할"이 통하지 않는다

파일마다 헤딩 사용법이 다르다.

| 계열 | 파일 | 구조 | 주제 단위 |
|---|---|---|---|
| A | D00, D09~D17 | H2가 도메인 절 (파일당 9~17개) | **H2** |
| B | D01~D03, D05~D07 | H1이 주제, H2는 레코드 마커 (D06은 H2가 356개) | **H1** |
| C | D04, D08 | H2 절이 3~15KB로 과대 | **H3** |

레벨을 고정하면 한쪽은 4,000토큰을 넘고 다른 쪽은 파편화된다.
→ **S0에서 파일별로 레벨을 자동 결정**한다.

추가로 D03~D07은 여러 파트가 이어붙은 파일이다(`이번 구간 완료` 마커 3~8개,
파일 제목 H1이 최대 10회 반복).

### 1.2 이미 RAG 자산이 들어 있다

`## Chunk D01-001` YAML 블록이 7개 파일에 29개. `chunk_id/title/content/entities/keywords`
구조로 frontmatter와 거의 1:1이다. 새로 만들지 않고 **승계**한다.

### 1.3 D00이 계층 0 그 자체다

Canonical Entity Master, fact_status enum, Scope/Time/Unit 표준, ID governance —
전략 §2.1이 요구하는 용어집·규칙·스키마가 이미 정리돼 있다.

### 1.4 과제 생성에는 계층이 하나 더 필요하다

`OI Seed` / `D17 Bridge` 섹션 29개, D17-04에 점수·KPI·Tier가 매겨진 최종 과제 60건.
이건 "검색해서 읽을 문서"가 아니라 **과제 발굴 agent가 직접 소비하는 후보 풀**이다.
일반 `docs/`에 섞으면 묻힌다. → `seeds/` 선반으로 분리.

### 1.5 두 번째 대상 — SK이노베이션 E&S

같은 팀이 같은 D00~D17 골격으로 쓴 DB라 파이프라인이 그대로 돌았다
(1.12M자 · 19,726줄 · 약 **40만 토큰**, H1 372 / H2 974 / H3 229).
S0가 D04만 H2, 나머지 17개를 H1로 잡았고 이어붙은 파트는 없다.
따로 대응한 차이는 세 가지다.

| 차이 | 결과 | 대응 |
|---|---|---|
| 시드 절 제목이 `O/I Seed Master` · `Seed Registry` 등으로 표기가 다양하다 | SK온 패턴으로는 6개 도메인 8건만 잡힘 (E&S 패턴 15개 도메인 18건) | 회사별 `seed_marker` |
| `fact_status` enum이 다르다 (`PUBLIC_CONFIRMED/COMPANY_CLAIM/…`) | SK온 규칙을 복사하면 계층 0이 통째로 거짓 | 회사별 `rules` |
| 같은 도메인 코드가 다른 주제다 (D06=제조공정 → 밸류체인 운전, D07=셀 캐파 → 터미널·발전소) | 인덱스 라벨이 오해를 부름 | 회사별 `theme_overrides` |

법인 성격도 다르다 — E&S는 독립 법인이 아니라 2024-11-01 출범한 SK이노베이션
내부 CIC다. 합병 전 `SK E&S` 법인과 섞지 않는 규칙을 계층 0에 넣었다.

---

## 2. 파이프라인

```
<원본 DB>/*.md  (계열사별 18파일)
   │
   ├─ S0  profile.py       파일별 분할 레벨 자동 결정 (H1/H2/H3), 파트 감지
   │
   ├─ S1  restructure.py   적응형 분할 + 결정적 frontmatter
   │                       · 표/코드블록 절대 미분할
   │                       · 서두(첫 헤딩 앞) 별도 문서로 보존
   │                       · 작은 형제 병합 / 상한 초과 재분할
   │                       · Chunk YAML에서 keywords·entities 승계
   │                                                 → build/segments/<코드>/
   │
   ├─ S2  build_index.py   계층 0 core/ + 계층 1 INDEX.md
   │                                                 → knowledge/<코드>/
   │
   ├─ S3  enrich.py        summary · keywords LLM 보강 (선택, 폴백 있음)
   │
   └─ S4  validate.py      원문 커버리지 + 전략 §3.6 점검
       └─ coverage.py      줄 단위 대조 — 자료 손실 검사
```

한 번에 실행 — 대상은 회사 코드 하나로 정한다. 원본 경로·산출 경로·기준일은
프로파일에서 오므로 따로 줄 필요가 없다.

```bash
cd backend
python -m tools.kb_build.run --company SKO       # SK온
python -m tools.kb_build.run --company SKES      # SK이노베이션 E&S
python -m tools.kb_build.run --company SKES --skip-enrich   # LLM 없이
```

### S0 — 분할 레벨 자동 결정

레벨별로 "목표 구간(500~2,000토큰) 적합도"를 채점해 파일마다 최적값을 고른다.
상한(4,000) 초과는 재분할로 구제되지만 그때 문맥이 상하므로 강하게 감점한다.

```
score = (목표구간_섹션수 - 1.5 × 상한초과 - 0.5 × 과소섹션) / 전체섹션수
```

### S1 — 분할에서 지키는 세 가지

1. **표와 코드블록을 절대 가르지 않는다.** 표 중간을 자르면 헤더 행이 사라져
   남은 조각이 해석 불가능해진다. 이 DB는 정보 대부분이 표에 있다.
2. **헤딩 경로를 문서에 남긴다.** H3로 자른 조각은 상위 문맥 없이는 의미가 없다
   (전략 §3.3 자기완결성). 모든 문서 상단에 `> SK온 · D08 원소재… · 상위경로` 리드를 붙인다.
3. **절 번호를 상위에서 물려받는다.** H3 조각의 `section_no`가 `2`(절 내 순번)면
   쓸모가 없다. 상위의 `D08-12`를 상속해야 id와 인덱스가 해석 가능해진다.

**고아 절 구제** (`rescue_orphan_sections`). 분할 레벨의 하위 절을 갖지 않는 상위
절은 분할 기준에 걸리지 않아 앞 구간에 통째로 흡수된다. E&S D04는 H2 분할인데
`# 5. D04 직접 O/I Seed`가 H1(하위는 H3뿐)이라 시드 표가 `공통 데이터·OT·SHE`
문서 안에 묻혔다 — 줄 커버리지는 100%인데 검색으로는 영영 안 나오는 손실이다.
E&S는 켜져 있고(고아 6개), SK온은 꺼져 있다 — D04 한 파일에만 고아가 283개라
켜면 742→840건으로 재분할되고 id가 바뀌어 보강된 summary가 전부 무효화된다.
재보강 일정을 잡을 때 함께 켤 것.

### S3 — LLM 보강

`summary`는 인덱스와 검색 결과에 그대로 노출된다. 에이전트가 **이 한 줄만 보고
문서를 열지 말지 판단**하므로(전략 §3.2) 제목 복사본이면 검색 단계가 무의미하다.

[farming/llm.py](../backend/app/pipeline/farming/llm.py)와 같은 규약을 따른다 —
provider 미설정·네트워크·파싱 실패는 전부 폴백으로 떨어지고 예외를 올리지 않는다.
설정이 없어도 빌드는 끝까지 돈다. 본문은 절대 수정하지 않고 frontmatter 두 필드만 덮어쓴다.

---

## 3. 산출 구조

```
backend/knowledge/
├── SKO/                  # SK온
│   ├── INDEX.md          # 계층 1 — 자동 생성, 문서 전량 수록
│   ├── manifest.json     # 검색용 색인 (id·title·summary·keywords·tags·tokens)
│   ├── core/             # 계층 0 — 항상 로드
│   │   ├── schema.md     #   자동 생성 (도메인 지도·id 규칙·태그 어휘)
│   │   ├── glossary.md   #   회사별 스텁 → 사람이 큐레이션
│   │   └── rules.md      #   회사별 스텁 → 사람이 큐레이션
│   ├── seeds/D##/        # 과제 후보 24건 — 과제 발굴 1차 소비 대상
│   └── docs/D##/         # 도메인 본문 718건
└── SKES/                 # SK이노베이션 E&S — 같은 구조, 시드 18 / 본문 360
```

### frontmatter

```yaml
---
id: skon-d08-d08-12-우선-o-i-후보-15개
title: 우선 O/I 후보 15개
summary: 원소재 공급망의 O/I 과제 후보 15건을 Pain Point·솔루션·KPI·우선도 표로 정리
tags: [d08, supply-chain, oi-seed, schema, table, "xref:d17"]
keywords: [공급망, 대사, PFE, 원산지, dual-source, ...]
related: [OI-D08-01, OI-D08-02, ...]
priority: normal
domain: D08
section: D08-12
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: SK온 D08 — Raw Materials… > D17 Bridge — Open Innovation Seed Portfolio
tokens: 1452
updated: 2026-08-03
---
```

`id`는 파일명과 일치한다. 한글 슬러그를 로마자로 바꾸지 않는다 — 에이전트도
사용자도 한국어로 질의하므로 로마자화는 정보만 잃고 재현율을 떨어뜨린다.

---

## 4. 자료 손실 검증

재구조화에서 가장 위험한 실패는 **조용한 누락**이다. 분할 기준 헤딩보다 앞의 서두,
필터에 걸린 구간, 재분할에서 흘린 블록은 전부 오류 없이 사라진다.
그래서 토큰 수가 아니라 **줄 단위 커버리지**를 신뢰 기준으로 삼는다.

```bash
python -m tools.kb_build.coverage --company SKO
python -m tools.kb_build.coverage --company SKES
```

원문 줄을 정규화해 멀티셋으로 만들고 산출물과 대조한다. 초기 구현에서 잡은 손실:

| 원인 | 손실 | 조치 |
|---|---|---|
| 분할 기준 헤딩 앞의 서두를 `_cut`이 폐기 (D04·D08은 파일 앞부분 통째) | 1,200줄+ | 서두를 별도 문서로 보존 |
| 집필 로그(`이번 구간 완료` 등)를 필터로 제거 | 300줄+ | 제거하지 않고 `build-log` 태그 + `priority: reference` |

**최종: SK온 55,769 / 55,769줄 · E&S 19,726 / 19,726줄 = 각 100.00%** (18개 파일 전부)

커버리지는 "줄이 어딘가에 남아 있는가"만 본다. 어느 문서에 들어갔는지는 보지
않으므로, §2 S1의 고아 절 문제처럼 **엉뚱한 제목 아래로 들어간 손실은 잡지 못한다.**
그건 시드 개수(도메인마다 후보 목록이 하나씩은 나와야 한다)로 교차 확인한다.

---

## 5. 호출 구조

전략 §4.1의 2단계 분리를 그대로 구현했다.

```
search_docs(query, shelf?, tags?, top_k)  → [{id, title, summary, matched_snippet}]  본문 없음
read_doc(id, section?)                    → 문서 전문 또는 지정 섹션
list_docs(domain?, section?, shelf?)      → 목록만 (검색어가 안 떠오를 때)
```

### 검색 엔진

전략 §5 권고대로 **파일 탐색형**으로 먼저 구현했다. 임베딩 인프라 없이
메타데이터 가중 일치 + 본문 BM25로 훑는다.

본문 역색인은 선택이 아니라 필수였다 — 메타데이터만 보면 제목이 영문인 문서를
한국어로 질의할 때 전부 놓친다(`"수율"` → `Yield-to-Margin Causal AI`).
회사당 400~750건 / 약 2MB라 메모리에 올리는 비용이 없다.

색인은 `load(company)` 단위로 캐시된다(`lru_cache`). 회사가 섞이지 않으므로
검색 결과에 다른 계열사 문서가 나올 일은 없다. 어떤 KB가 빌드돼 있는지는
`retriever.available()` 이 디렉터리에서 읽는다 — 목록을 코드에 적지 않는다.

### 프롬프트 배치와 캐싱 (전략 §4.3 · §6.1)

렌더 순서는 `tools` → `system` → `messages`이고 캐시는 접두사 일치다.
앞쪽이 1바이트만 달라져도 뒤가 전부 무효화된다.

```
tools       정렬 고정 (매 호출 동일 바이트)
system[0]   역할 정의        ┐
system[1]   계층 0 core/     ├ 고정 — 마지막 블록에 cache_control
system[2]   계층 1 INDEX     │   (툴 정의까지 함께 캐시된다)
system[3]   검색 사용 지침    ┘
messages    계열사·외부 동향·메모 — 매번 달라지는 것은 여기만
```

### 근거를 싣는 방식 — 지금은 사전 검색뿐이다

`OI_TASK_PROVIDER` 기본값은 `codex-cli`이고 `OI_CODEX_ONLY=1`이 나머지를 거부한다.
codex 는 단발 호출이라 **툴 루프가 돌지 않는다**. 그래서 서버가 먼저 검색해 결과를
프롬프트 본문에 싣는다.

| 경로 | 함수 | 동작 | 상태 |
|---|---|---|---|
| 사전 검색 | `prefetch.build_context()` | 서버가 먼저 검색해 결과를 본문에 주입 | **현재 유일한 경로** |
| 툴 루프 | — | 에이전트가 스스로 검색·열람 | 미구현. 툴 루프를 도는 provider 로 갈 때 |

두 경로는 같은 retriever 위에 올린다는 전제라, 전환해도 에이전트가 보는 근거는
동일하다. 차이는 "무엇을 열지"를 모델이 정하느냐 코드가 정하느냐뿐이다.

---

## 6. 계열사 추가하기

[companies.py](../backend/tools/kb_build/companies.py)에 항목 하나를 더한다.
파이프라인 코드는 건드리지 않는다.

```python
SKGC = Company(
    code="SKGC", name="SK지오센트릭", slug="skgc",
    src=Path("../../DB_SK_GC"), updated="2026-08-06",
    seed_marker=re.compile(...),      # 그 DB의 과제 후보 절 제목 관례
    theme_overrides={...},            # 같은 D06이라도 주제가 다르면
    glossary=..., rules=...,          # 계층 0 스텁
)
```

회사마다 반드시 다시 보는 것 두 가지.

1. **`rules`** — 여기 있는 값이 틀리면 항상 로드되는 계층 0이 통째로 거짓이 된다.
   `fact_status` enum부터 DB마다 다르다 (SK온 `official_fact/…`,
   E&S `PUBLIC_CONFIRMED/…`). 다른 회사 스텁을 복사해 두면 비워 두는 것보다 나쁘다.
2. **`seed_marker`** — 시드 선반이 과제 발굴의 1차 입력이다. 빌드 후
   도메인마다 후보 문서가 하나씩 잡혔는지 확인한다. E&S는 SK온 패턴
   그대로면 `O/I Seed Master` · `Seed Registry` 표기를 놓쳐 선반이 거의 비었다.

## 7. 남은 작업

- [ ] `core/glossary.md`, `core/rules.md` 사람 검토 — 지금은 스텁이다.
      `validate.py`가 `priority: critical` 문서를 승격 후보로 출력한다.
- [ ] 평가셋 구축 (전략 §8-4단계) — 실제 질문 30~50개와 정답 문서 id.
      이후 모든 개선의 판단 기준이 된다.
- [ ] 검색 실패 케이스 로깅 → 의미 검색이 실제로 필요한지 확인된 뒤에만 하이브리드 도입.
- [ ] SK온 `rescue_orphan_sections` 전환 — 재분할이라 전면 재보강이 함께 필요하다 (§2 S1).
- [ ] INDEX.md가 계층 1 예산(전략 1~4천 토큰)을 크게 넘는다 (SK온 6.4만 · E&S 3.4만).
      문서 전량 대신 절 단위 요약으로 줄이고 목록은 `list_docs`로 미룰 것.
