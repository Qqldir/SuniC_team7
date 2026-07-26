"""환경변수 기반 설정."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent  # backend/

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OI_MODEL = os.getenv("OI_MODEL", "claude-sonnet-4-6")

# DB 경로: 상대경로면 backend/ 기준으로 해석
_db = os.getenv("OI_DB_PATH", "oi_scout.db")
DB_PATH = str(BASE_DIR / _db) if not os.path.isabs(_db) else _db

CORS_ORIGINS = [
    o.strip()
    for o in os.getenv("OI_CORS_ORIGINS", "http://localhost:5173").split(",")
    if o.strip()
]

# ── 지식 파밍(크롤러) ──
# OpenDART API 키 (https://opendart.fss.or.kr 발급). 없으면 DART 소스는 건너뜁니다.
DART_API_KEY = os.getenv("DART_API_KEY", "")
# SEC EDGAR 는 연락처가 포함된 User-Agent 를 요구합니다. (미설정 시 SEC 소스 skip)
SEC_USER_AGENT = os.getenv("SEC_USER_AGENT", "")
# 크롤 대상 기간(일)
CRAWL_SINCE_DAYS = int(os.getenv("CRAWL_SINCE_DAYS", "30"))

# 캐시(코드/티커 매핑) 저장 디렉터리
DATA_DIR = BASE_DIR / "data"

# 기준일 — 데모 데이터와 정합을 맞추기 위해 고정. 실서비스에서는 date.today() 사용.
TODAY = "2026-07-22"
