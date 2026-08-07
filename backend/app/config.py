"""환경변수 기반 설정."""
import os
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent  # backend/

# ── 과제 발굴 · 평가 · 제안 ──
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OI_MODEL = os.getenv("OI_MODEL", "claude-sonnet-4-6")
# 과제 발굴·평가·제안이 모두 쓰는 provider (app/llm_client.py).
# codex-cli / claude-cli 는 API 키가 필요 없습니다 — 평가·제안도 llm_client 를 경유하므로
# ANTHROPIC_API_KEY 없이 완주합니다(키가 없으면 규칙 채점·골격 폴백).
OI_TASK_PROVIDER = os.getenv("OI_TASK_PROVIDER", "codex-cli")

# ── 과제 평가(app/pipeline/evaluation) ──
# LLM 채점 1회에 넣는 과제 수. 수십 건을 한 번에 넣으면 응답이 길어져 중간에서
# 잘리고, 그러면 파싱이 통째로 실패해 배치 전부가 규칙 폴백으로 떨어진다.
# 8 은 실측 안전선이다 — 올리지 마라(anthropic 경로는 출력 상한 2000 토큰이라 더 빨리 잘린다).
OI_EVAL_BATCH = int(os.getenv("OI_EVAL_BATCH", "8"))

# ── 재생성(POST /api/proposals/regenerate) 의 LLM 발굴 ──
# 호출 수 = OI_REGEN_OCS 개(계열사당 정확히 1회). 기본 2회를 **동시에** 돌린다.
# 실측 소요: 단독 104초 / 동시 2건 155초(느린 쪽 기준). codex 는 동시 3건까지 안전하므로
# OCS 를 3 초과로 올리지 마세요 — 올리면 계정 쪽에서 밀려 전부 타임아웃합니다.
OI_REGEN_LLM = os.getenv("OI_REGEN_LLM", "1") == "1"   # 0 이면 항상 후보 풀 폴백
OI_REGEN_OCS = int(os.getenv("OI_REGEN_OCS", "2"))     # 한 번의 재생성에서 발굴할 계열사 수
OI_REGEN_TASKS = int(os.getenv("OI_REGEN_TASKS", "2"))  # 계열사당 과제 건수
# 계열사 1건의 발굴을 기다리는 상한(초). llm_client 의 자체 재시도(300초×3회)를 다 기다리면
# HTTP 요청이 15분을 넘기므로 여기서 먼저 끊는다. 끊긴 계열사만 버리고 나머지는 그대로 저장하며,
# 전부 끊기면 후보 풀 폴백으로 내려간다(최악 소요 ≈ 이 값 + 풀 저장 1초).
# HTTP 응답 대기 시간이 아니다 — 재생성은 비동기 작업이라 요청은 즉시 돌아온다(app/jobs.py).
OI_REGEN_TIMEOUT = int(os.getenv("OI_REGEN_TIMEOUT", "90"))

# ── 지식 파밍 정제 ──
# 파밍 단계만 별도 provider 를 씁니다. 분리해 두면 한쪽 크레딧이 떨어져도
# 다른 단계가 멈추지 않고, 설정 충돌도 생기지 않습니다.
#
#   codex-cli  : 로컬 `codex exec` 서브프로세스. API 키가 아니라 ChatGPT 로그인 사용.
#                응답 JSON 형태를 --output-schema 로 강제할 수 있는 유일한 provider.
#   claude-cli : 로컬 `claude -p` 서브프로세스. 별도 API 키 없이 Claude Code 로그인 사용.
#                호출당 20초 안팎 → 배치(파밍) 전용.
#   openai     : OpenAI API. OPENAI_API_KEY 필요.
OI_LLM_PROVIDER = os.getenv("OI_LLM_PROVIDER", "codex-cli")
# provider=claude-cli/anthropic/openai 일 때만 쓰입니다.
# codex-cli 는 이 값을 무시하고 아래 OI_CODEX_MODEL 만 봅니다.
OI_LLM_MODEL = os.getenv("OI_LLM_MODEL", "claude-haiku-4-5")
# 동시 실행 수. CLI provider 는 프로세스를 띄우므로 과하게 올리지 마세요.
OI_LLM_CONCURRENCY = int(os.getenv("OI_LLM_CONCURRENCY", "3"))
# 1건당 타임아웃(초). claude-cli 는 사고 시간이 있어 넉넉히 잡습니다.
OI_LLM_TIMEOUT = int(os.getenv("OI_LLM_TIMEOUT", "180"))

# ── LLM provider 정책 ──
# SK 사내망은 **codex 만 허용**한다. 다른 provider 를 설정하면 사내에서 통째로 죽으므로,
# 기본적으로 codex 계열이 아닌 provider 를 거부한다(조용한 폴백보다 큰 소리로 실패하는 편이 낫다).
# 사외 개발 환경에서 claude-cli/anthropic/openai 로 실험하려면 0 으로 두면 된다.
OI_CODEX_ONLY = os.getenv("OI_CODEX_ONLY", "1") == "1"

# ── codex-cli provider ──
# 인증은 API 키가 아니라 `codex login`(ChatGPT 계정)입니다. 인증 정보가 CODEX_HOME 에
# 있으므로 이를 읽을 수 없는 환경(다른 사용자·docker·systemd)에서는 항상 Not logged in 입니다.
OI_CODEX_BIN = os.getenv("OI_CODEX_BIN", "codex")
# **codex provider 는 OI_MODEL/OI_LLM_MODEL 을 무시하고 이 값만 봅니다.**
# 두 축(claude/codex)의 모델 설정이 서로 오염되지 않게 분리한 것입니다 —
# claude 모델 별칭(claude-haiku-4-5 등)을 `codex -m` 에 넘기면 호출이 깨집니다.
# 빈 값이면 -m 플래그를 아예 붙이지 않고 codex 기본 모델을 씁니다.
OI_CODEX_MODEL = os.getenv("OI_CODEX_MODEL", "")
# 추론 강도(low / medium / high / xhigh). codex 기본값은 xhigh 라 매우 느리다 —
# 실측: 발굴 프롬프트(4,573토큰) 1건이 xhigh 174~197초, medium 58~62초, low 38~41초.
# 우리 용도(정해진 스키마로 요약·초안 생성)에는 medium 이면 충분하다.
OI_CODEX_EFFORT = os.getenv("OI_CODEX_EFFORT", "medium")
# 1건당 타임아웃(초).
# 파밍 정제(프롬프트 300자)는 실측 9~15초지만, **과제 발굴은 다르다** —
# RAG 컨텍스트 6,000자 + 11필드×2건이라 단독 104초 / 동시 2건 155초가 실측이다.
# 120 으로 두면 발굴이 매번 타임아웃해 후보 풀 폴백으로만 떨어진다.
OI_CODEX_TIMEOUT = int(os.getenv("OI_CODEX_TIMEOUT", "300"))
# rc!=0 일 때 재시도 횟수(1s·3s 백오프). 401 이 산발적으로 났다가 자동 회복되는 사례가 있습니다.
OI_CODEX_RETRY = int(os.getenv("OI_CODEX_RETRY", "2"))
# 1이면 `--ignore-user-config` 를 붙입니다. 기본은 끔 —
# 이 플래그가 401 을 유발한다는 관측이 있고, 저장소 오염 방지는 --ephemeral + 빈 -C 로 이미 됩니다.
OI_CODEX_IGNORE_USER_CONFIG = os.getenv("OI_CODEX_IGNORE_USER_CONFIG", "0") == "1"

# ── RAG 프롬프트 토큰 예산 (app/pipeline/knowledge/prefetch.py) ──
# codex 는 단발 호출이라 툴 루프를 못 돕니다. 그래서 에이전트가 필요할 때 문서를 여는 대신
# 서버가 미리 골라 프롬프트에 실어 보냅니다(prefetch). 그 블록별 상한이 아래 값입니다.
# 합계 6,600 토큰 — 계층1 INDEX 전체(64,252토큰)를 매 호출 싣는 것의 1/10 입니다.
# est_tokens(tools/kb_build/common.py) 기준 근사치이며, 넘치면 블록을 뒤에서 잘라냅니다.
OI_RAG_ROLE_TOKENS = int(os.getenv("OI_RAG_ROLE_TOKENS", "400"))      # 역할·판단 규칙(SYSTEM)
OI_RAG_LEVER_TOKENS = int(os.getenv("OI_RAG_LEVER_TOKENS", "400"))    # 레버 체계 7행
OI_RAG_PROFILE_TOKENS = int(os.getenv("OI_RAG_PROFILE_TOKENS", "200"))  # 계열사 프로필
OI_RAG_KB_LIST_TOKENS = int(os.getenv("OI_RAG_KB_LIST_TOKENS", "1400"))  # 내부 지식 목록
OI_RAG_KB_BODY_TOKENS = int(os.getenv("OI_RAG_KB_BODY_TOKENS", "1300"))  # 내부 지식 본문 발췌
OI_RAG_UPLOAD_TOKENS = int(os.getenv("OI_RAG_UPLOAD_TOKENS", "800"))   # 업로드 자료 발췌
OI_RAG_CASE_TOKENS = int(os.getenv("OI_RAG_CASE_TOKENS", "800"))       # 검증된 혁신 사례
OI_RAG_FEED_TOKENS = int(os.getenv("OI_RAG_FEED_TOKENS", "1000"))      # 외부 동향
OI_RAG_NOTE_TOKENS = int(os.getenv("OI_RAG_NOTE_TOKENS", "300"))       # 사용자 메모
# 전체 상한. 블록 합계가 이 값을 넘으면 build_context 가 마지막에 한 번 더 잘라냅니다.
OI_RAG_TOTAL_TOKENS = int(os.getenv("OI_RAG_TOTAL_TOKENS", "6600"))
# 내부 지식 본문을 실제로 여는 문서 수와 문서당 절삭 글자 수.
# manifest 상 문서당 평균 939토큰 / 최대 3,822토큰이라 절삭 없이 2건을 열면 예산을 넘깁니다.
OI_RAG_KB_OPEN_DOCS = int(os.getenv("OI_RAG_KB_OPEN_DOCS", "2"))
OI_RAG_KB_DOC_CHARS = int(os.getenv("OI_RAG_KB_DOC_CHARS", "2500"))

# provider=openai 일 때만 사용
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
# OpenAI 호환 게이트웨이를 쓸 때만 지정 (미설정 시 공식 엔드포인트)
OI_LLM_BASE_URL = os.getenv("OI_LLM_BASE_URL", "")

# DB 경로: 상대경로면 backend/ 기준으로 해석
_db = os.getenv("OI_DB_PATH", "oi_scout.db")
DB_PATH = str(BASE_DIR / _db) if not os.path.isabs(_db) else _db

CORS_ORIGINS = [
    o.strip()
    for o in os.getenv("OI_CORS_ORIGINS", "http://localhost:5173").split(",")
    if o.strip()
]

# ── 인증 ──
# 로그인 토큰 서명용 비밀키. 운영에서는 반드시 OI_AUTH_SECRET 환경변수로 설정.
AUTH_SECRET = os.getenv("OI_AUTH_SECRET", "dev-insecure-secret-change-me")
# 토큰 유효기간(시간)
AUTH_TTL_HOURS = int(os.getenv("OI_AUTH_TTL_HOURS", str(24 * 7)))

# 빌드된 프론트(frontend/dist)를 FastAPI 가 직접 서빙할지 여부.
# 1이면 `uvicorn app.main:app` 하나로 화면까지 뜬다(운영/데모용).
# 0(기본)이면 API 만 서빙하고 화면은 Vite dev 서버(5173)가 담당한다.
SERVE_FRONTEND = os.getenv("OI_SERVE_FRONTEND", "0") == "1"
FRONTEND_DIST = Path(os.getenv("OI_FRONTEND_DIST", str(BASE_DIR.parent / "frontend" / "dist")))

# ── 지식 파밍(크롤러) ──
# OpenDART API 키 (https://opendart.fss.or.kr 발급). 없으면 DART 소스는 건너뜁니다.
DART_API_KEY = os.getenv("DART_API_KEY", "")
# SEC EDGAR 는 연락처가 포함된 User-Agent 를 요구합니다. (미설정 시 SEC 소스 skip)
SEC_USER_AGENT = os.getenv("SEC_USER_AGENT", "")
# 크롤 대상 기간(일). 뉴스 기준값입니다 —
# DART 정기보고서는 이 창에 구조적으로 걸리지 않으므로 dart.MIN_SINCE_DAYS 가 별도로 바닥을 깝니다.
CRAWL_SINCE_DAYS = int(os.getenv("CRAWL_SINCE_DAYS", "30"))

# 뉴스 본문 크롤 User-Agent.
# 로봇이 누구인지·어디로 연락하는지 밝히는 것이 예의이므로 SEC 용으로 이미 받아 둔
# 연락처를 재사용합니다(같은 팀·같은 수집기). 둘 다 비면 익명 봇 이름만 붙습니다.
NEWS_USER_AGENT = os.getenv("OI_NEWS_USER_AGENT", "") or (
    f"OIScoutBot/1.0 (+{SEC_USER_AGENT})" if SEC_USER_AGENT else "OIScoutBot/1.0"
)

# ⚠ Google News 진입 경로(RSS·기사 셸·batchexecute)는 news.google.com/robots.txt 의
#   `Disallow: /` 에 걸립니다 — /rss/ 는 Allow 목록에 없습니다.
#   지금은 **사내 검증 용도**라 기본값 0(현행 유지)이고, 사용자 판단으로 그렇게 뒀습니다.
#   1 로 두면 그 경로를 아예 타지 않습니다(뉴스 소스는 사실상 0건이 되고 DART·SEC 만 남음).
#   ★ 외부 배포·상시 운영 전에는 반드시 1 로 돌리거나 정식 뉴스 API 로 교체하십시오.
#   매체 기사 본문 요청은 이 값과 무관하게 항상 robots 를 지킵니다(news._robots_allows).
NEWS_ROBOTS_STRICT = os.getenv("OI_NEWS_ROBOTS_STRICT", "0") == "1"

# 캐시(코드/티커 매핑) 저장 디렉터리
DATA_DIR = BASE_DIR / "data"

# SK 계열사 코드 마스터 (db/seed_data.py AFFILIATES 와 동일).
# 정제 단계에서 LLM 이 뱉은 계열사 코드를 검증하는 화이트리스트로 씁니다.
AFFILIATE_CODES = ["SKE", "SKGC", "SKEN", "SKIPC", "SKTI", "SKEO", "SKO", "SKIET", "SKES"]

# 기준일 — 데모 시드(2026-06~07)와 정합을 맞추려고 고정돼 있습니다.
# 실제 크롤 데이터를 쓸 때는 .env 에 `OI_TODAY=` (빈 값)로 두어 오늘 날짜로 전환하세요.
# 고정값이면 오늘 수집한 항목이 discovery 의 최근 30일 창 밖으로 밀려 발굴에서 빠집니다.
TODAY = os.getenv("OI_TODAY", "2026-07-30") or date.today().isoformat()
