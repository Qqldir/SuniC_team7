"""회사 프로파일 — 계열사를 붙일 때 손대는 유일한 파일.

파이프라인(S0~S4)은 회사를 모른다. 회사마다 달라지는 것은 여기 다섯 가지뿐이다.

    slug          문서 id 접두사 (`skon-d08-…` / `skes-d08-…`)
    themes        도메인 라벨 — 같은 D06 이라도 SK온은 "제조공정", E&S 는 "운영 프로세스"다
    seed_marker   과제 후보 절의 제목 관례 (원본 DB 마다 다르다)
    glossary      계층 0 용어집 스텁 — 법인·약어가 회사마다 완전히 다르다
    rules         계층 0 절대 규칙 스텁 — **fact_status enum 부터가 다르다**
                  (SK온 official_fact/… vs E&S PUBLIC_CONFIRMED/…)

새 계열사는 `COMPANIES` 에 항목 하나를 추가하면 된다. 파이프라인 코드는 그대로다.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Pattern, Tuple

from tools.kb_build.common import DOMAIN_THEME


@dataclass(frozen=True)
class Company:
    code: str                       # knowledge/<code> · 계열사 코드 (config.AFFILIATE_CODES)
    name: str                       # 표시명 — 인덱스 제목과 문서 리드에 쓰인다
    slug: str                       # 문서 id 접두사
    src: Path                       # 원본 DB 디렉터리 (backend/ 기준 상대경로)
    updated: str                    # 원본 기준일 — frontmatter 의 updated
    seed_marker: Pattern
    theme_overrides: Dict[str, Tuple[str, str]] = field(default_factory=dict)
    glossary: str = ""
    rules: str = ""
    # 분할 레벨의 하위 절이 없는 상위 절을 별도 문서로 건질지 (restructure._orphans).
    # 켜면 청킹이 바뀌므로 **id 가 바뀌고 enrich 결과를 다시 만들어야 한다.**
    # 이미 보강이 끝난 KB 는 전면 재빌드를 잡을 때 함께 켠다.
    rescue_orphan_sections: bool = False

    @property
    def themes(self) -> Dict[str, Tuple[str, str]]:
        return {**DOMAIN_THEME, **self.theme_overrides}

    @property
    def lead_prefix(self) -> str:
        """문서 상단 리드 인용문의 접두사. coverage 가 대조에서 빼는 기준이기도 하다."""
        return f"> {self.name} ·"

    def theme(self, domain: str) -> Tuple[str, str]:
        return self.themes.get(domain, ("misc", domain))


# ── 공통 규칙 (회사 무관) ────────────────────────────────────────────────
# 답변 규칙은 검색 계층의 사용법이라 회사가 바뀌어도 같다. 회사별 rules 는
# 여기에 이어 붙는다 — fact_status·법인 시점처럼 **틀리면 위험한 것**만.

ANSWER_RULES = """## 답변 규칙

- 인덱스에 있는 주제는 반드시 문서를 열어 확인한 뒤 답한다. 기억으로 추측하지 않는다.
- 검색 결과가 비면 표현을 바꿔 1회 재시도하고, 그래도 없으면
  "지식 베이스에 없다"고 답한다. 지어내지 않는다.
- 답변에는 근거 문서 id 를 표기한다.
"""

_GLOSSARY_HEAD = """# 용어집

> 이 파일은 계층 0(항상 로드)이다. 시스템 프롬프트에 통째로 들어가므로
> **예산 안에서 사람이 직접 큐레이션한다.** 자동 생성 대상이 아니다.
> 후보 문서: `priority: critical` 인 문서 목록을 `validate.py` 가 출력한다.
"""

_RULES_HEAD = """# 절대 규칙

> 계층 0(항상 로드). 이 정보 없이 답하면 **위험한 답이 나오는 것**만 남긴다.
> 하나 추가할 때마다 계층 2 로 내릴 것이 없는지 함께 본다 (전략 §2.1).
"""


# ── SK온 ────────────────────────────────────────────────────────────────

SKO = Company(
    code="SKO",
    name="SK온",
    slug="skon",
    src=Path("../../DB_SK_ON"),
    updated="2026-08-03",
    # D04 한 파일에만 고아 절이 283개다(H3 분할·레코드형 파일). 켜면 문서가
    # 742 → 840건으로 재분할되고 id 가 바뀌어 보강된 summary 742건이 전부 날아간다.
    # 재보강 일정을 잡을 때 함께 켤 것.
    rescue_orphan_sections=False,
    # 원본은 `## OI Seed`, `## D17 Bridge` 처럼 절 제목에 표식이 있다.
    seed_marker=re.compile(
        r"OI\s*Seed|D17\s*Bridge|Seed Portfolio|Final Portfolio|Task Blueprint|"
        r"Recommendation Engine|O/I\s*후보|과제\s*후보|Seed Graph", re.I),
    glossary=_GLOSSARY_HEAD + """
## 법인·조직

| 약어 | 정식 명칭 | 비고 |
|---|---|---|
| SK온 | 에스케이온 주식회사 (SK On Co., Ltd.) | 2021-10-01 SK이노베이션 배터리사업 물적분할 |
| SKI | SK이노베이션 | SK온의 모회사 |
| SKIET | SK아이이테크놀로지 | 분리막 |
| SKTI | SK트레이딩인터내셔널 | 2025-02 SK온에 합병 |
| SK엔무브 | SK Enmove | 2025-11 SK온에 합병 (윤활기유·열관리) |

## 사업·기술

| 약어 | 뜻 |
|---|---|
| CTP | Cell to Pack — 모듈을 생략하고 셀을 팩에 직접 조립 |
| FPY | First Pass Yield — 초도 공정 합격률 |
| COPQ | Cost of Poor Quality — 품질 실패 비용 |
| SOP | Start of Production — 양산 개시 |
| O/I | Operation Improvement — 운영개선 과제 |
| DPP | Digital Product Passport — EU 배터리 여권 |
| PFE | Prohibited Foreign Entity (미국 IRA 관련) |
""",
    rules=_RULES_HEAD + """
## 사실 상태 (fact_status)

| 값 | 뜻 | 취급 |
|---|---|---|
| `official_fact` | 공시·공식발표로 확인된 사실 | 근거로 인용 가능 |
| `reported_claim` | 언론·3자 보도 | 출처를 함께 밝힌다 |
| `estimate` | 추정치 | 수치로 단정하지 않는다 |
| `plan` | 계획·목표 | 실적으로 말하지 않는다 |

## 시점 구분

- `target_date`(계획) 와 `actual_date`(완료)를 절대 섞지 않는다.
  계획일이 지났다는 이유로 완료 처리하지 않는다.
- 수치를 인용할 때는 반드시 기준일(`as_of`)을 함께 밝힌다.

## 법인 구분

- 합병 이전/이후 법인을 구분한다. 2025년 합병 전 SKTI·SK엔무브 실적을
  SK온 실적으로 합산하지 않는다.

""" + ANSWER_RULES + """- `build-log` 태그가 붙은 문서는 원본 집필 로그다. 사실 근거로 인용하지 않는다.
""",
)


# ── SK이노베이션 E&S ────────────────────────────────────────────────────
# 배터리 제조업(SK온)과 에너지 인프라 운영업(E&S)은 도메인 이름이 같아도
# 내용이 다르다. D06 은 제조공정이 아니라 LNG·발전·도시가스 운영이고,
# D07 은 셀 공장 캐파가 아니라 터미널·발전소·배관 자산이다.

SKES = Company(
    code="SKES",
    name="SK이노베이션 E&S",
    slug="skes",
    src=Path("../../DB_SK_E&S"),
    updated="2026-08-06",
    # E&S 원본은 `O/I Seed Master`, `Seed Registry`, `Open-Innovation Seed Portfolio`
    # 처럼 슬래시와 표기 변형이 많다. SK온 패턴 그대로면 시드 선반이 거의 빈다.
    seed_marker=re.compile(
        r"O/?I\s*Seed|Open-?Innovation\s*Seed|Seed\s*(?:Portfolio|Master|Registry|Register)|"
        r"O/?I\s*Opportunity\s*(?:Portfolio|Map)|"
        r"D17\s*Bridge|Final Portfolio|Task Blueprint|Recommendation Engine|"
        r"O/I\s*후보|과제\s*후보", re.I),
    # D04 는 H2 분할인데 `# 5. D04 직접 O/I Seed` 가 H1(하위는 H3뿐)이라
    # 시드 표가 옆 문서에 묻힌다. 고아 절은 6개뿐이라 켜도 부작용이 없다.
    rescue_orphan_sections=True,
    theme_overrides={
        "D06": ("process", "운영 프로세스·밸류체인 운전"),
        "D07": ("footprint", "터미널·발전소·배관 등 자산·용량"),
        "D08": ("supply-chain", "공급망·조달·설비·물류"),
        "D09": ("customer", "고객·수요·계약·Offtake"),
        "D13": ("contract", "JV·파트너십·계약·거버넌스"),
        "D15": ("risk", "리스크·실패모드·회복탄력성"),
        "D16": ("ecosystem", "외부 기술·솔루션·기업·스타트업"),
    },
    glossary=_GLOSSARY_HEAD + """
## 법인·조직

| 명칭 | 정식 명칭 | 비고 |
|---|---|---|
| SK이노베이션 E&S | SK Innovation E&S CIC | 2024-11-01 출범. SK이노베이션 내부 CIC — **독립 법인이 아니다** |
| SK E&S | 에스케이이엔에스 주식회사 (SK E&S Co., Ltd.) | 2005-10~2024-10-31 존재한 합병 전 법인. 검색 별칭으로만 쓴다 |
| SK-Enron | SK-Enron Co., Ltd. | 1999-01~2005-09 전신 |
| SKI | SK이노베이션 | 합병 존속법인 · E&S CIC 의 법적 귀속처 |
| KCE | Key Capture Energy | 미국 BESS 자회사 |
| EverCharge | EverCharge Inc. | 미국 EV 충전 자회사 |
| 도시가스 자회사군 | 부산도시가스·영남에너지서비스·코원에너지서비스·전남도시가스·충청에너지서비스·강원도시가스 | 지역 도시가스 공급 |

## 사업·기술

| 약어 | 뜻 |
|---|---|
| LNG | Liquefied Natural Gas — 액화천연가스. 도입·수송·터미널·발전으로 이어지는 밸류체인 |
| CHP | Combined Heat and Power — 열병합발전 |
| PPA | Power Purchase Agreement — 전력구매계약 (기업 PPA 포함) |
| BESS / ESS | Battery Energy Storage System — 계통 배터리 저장장치 |
| VPP | Virtual Power Plant — 분산자원을 묶어 계통에 입찰하는 가상발전소 |
| DER / DERMS | Distributed Energy Resource (Management System) — 분산에너지자원(관리시스템) |
| BOG | Boil-Off Gas — LNG 저장·수송 중 증발가스 |
| CCS / CCUS | Carbon Capture (Utilization and) Storage — 탄소 포집·저장 |
| SMP | System Marginal Price — 계통한계가격 |
| REC | Renewable Energy Certificate — 신재생에너지 공급인증서 |
| FID | Final Investment Decision — 최종투자결정 |
| EPC / O&M | 설계·조달·시공 / 운영·정비 |
| OT | Operational Technology — 발전·터미널 제어망(SCADA 등). IT 망과 구분한다 |
| O/I | Open Innovation — 외부 기술·기업을 활용하는 혁신과제 |
""",
    rules=_RULES_HEAD + """
## 사실 상태 (fact_status)

원본 D00 의 enum 을 그대로 쓴다. **SK온 DB 의 값(`official_fact` 등)과 다르다.**

| 값 | 뜻 | 취급 |
|---|---|---|
| `PUBLIC_CONFIRMED` | 공개 근거로 해당 범위의 사실이 확인됨 | 근거로 인용 가능 |
| `COMPANY_CLAIM` | 기업이 발표했으나 독립 검증과 구분 필요 | 발표 주체를 함께 밝힌다 |
| `EXTERNAL_SIGNAL` | 외부 시장·기술·위협 신호 | E&S 에서 일어난 일로 옮기지 않는다 |
| `INTERNAL_REQUIRED` | 내부 확인이 필요한 항목 | 추정으로 채우지 않는다 |
| `HYPOTHESIS` | 가설 | 사실로 말하지 않는다 |
| `PROPOSAL` | 제안 | 확정된 계획으로 말하지 않는다 |

D00 의 값이 정본이다. 원문에 `official_fact` 처럼 다른 표기가 드물게 남아 있으면
위 표에서 가장 가까운 값으로 읽되, 등급을 올려 잡지 않는다.

출처 등급은 `S1A`(법령·규제기관·공식 등록부) → `S5`(출처불명) 순이다.
`S4`·`S5` 만으로 계약·권리·수치를 확정하지 않는다.

## 법인·시점 구분

- 2024-11-01 이후 표준명은 `SK이노베이션 E&S CIC` 다. 현재의 법적 실체는
  SK이노베이션이며, E&S 를 별도 법인으로 서술하지 않는다.
- 합병 전 `SK E&S` 법인이 당사자인 계약·재무·지분·소송을 CIC 로 소급하지 않는다.
- 발표·MOU·계약·FID·착공·준공·가동·상업운전·현금효과는 서로 다른 사건이다.
  앞 단계가 있다는 이유로 뒤 단계를 단정하지 않는다.
- 수치를 인용할 때는 기준일과 적용 범위(자산·법인·지분 기준)를 함께 밝힌다.

## 과제 판단

- 외부사례의 ROI·효율·절감률을 E&S 기대효과로 그대로 옮기지 않는다.
- 안전·법률·세무·계약·Cyber·데이터 권리·경제성 Gate 가 막히면 점수와 무관하게 보류(HOLD)다.

""" + ANSWER_RULES + """- `build-log` 태그가 붙은 문서는 원본 집필 로그다. 사실 근거로 인용하지 않는다.
""",
)


COMPANIES: Dict[str, Company] = {c.code: c for c in (SKO, SKES)}
DEFAULT_CODE = SKO.code


def get(code: str) -> Company:
    try:
        return COMPANIES[code.upper()]
    except KeyError:
        raise SystemExit(
            f"알 수 없는 회사 코드: {code!r} — 등록된 코드: {', '.join(codes())}\n"
            f"새 계열사는 tools/kb_build/companies.py 에 항목을 추가하세요."
        )


def codes() -> List[str]:
    return list(COMPANIES)
