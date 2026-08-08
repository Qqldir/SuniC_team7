"""관심 종목 시세.

소스가 둘이고 **역할이 다르다.**
  1) 네이버 금융 (m.stock.naver.com) — 실시간 체결가. 키가 필요 없고 12종목 전부 즉시 온다.
     화면 티커가 보여 주는 값은 이쪽이다.
  2) 공공데이터포털 금융위원회_주식시세정보 — 공식 통계. 전일(정확히는 직전 영업일) 종가만
     주고 기준일 다음 영업일 13시 이후에 열린다. 그래서 티커의 주 소스로는 못 쓴다.
     네이버가 응답하지 않을 때의 폴백이자, 나중에 추세를 그릴 때 쓸 공식 원천이다.

★ 실패해도 예외를 올리지 않는다. 시세는 화면의 곁가지라 값이 없으면 숫자만 빠지고
  종목명·링크는 남는다. quote_daily 에 마지막 값을 남겨 두는 것도 같은 이유다 —
  두 소스가 모두 죽어도 티커가 비지 않는다.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import httpx

from app.config import DATA_GO_KR_SERVICE_KEY, QUOTE_TIMEOUT, QUOTE_TTL_SEC
from app.db.database import get_connection

_NAVER = "https://m.stock.naver.com/api/stock/{code}/basic"
_DATAGO = (
    "https://apis.data.go.kr/1160100/service"
    "/GetStockSecuritiesInfoService/getStockPriceInfo"
)
# 네이버 오픈 API 가 아니라 모바일 웹이 쓰는 경로다. 브라우저가 아닌 요청은 막힐 수 있어
# UA 를 명시한다. 이 값이 없으면 403 이 온다.
_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36"

# 관심 종목. sk=True 는 SK 계열이라 화면에서 굵게 표시된다.
# ★ 프론트 상수가 아니라 여기에 두는 이유: 화면 데이터는 서버가 준다는 이 프로젝트의 원칙을 따른다.
WATCH: List[Dict[str, Any]] = [
    {"code": "096770", "name": "SK이노베이션", "sk": True},
    {"code": "361610", "name": "SK아이이테크놀로지", "sk": True},
    {"code": "034730", "name": "SK", "sk": True},
    {"code": "011790", "name": "SKC", "sk": True},
    {"code": "011170", "name": "롯데케미칼", "sk": False},
    {"code": "010950", "name": "에쓰오일", "sk": False},
    {"code": "051910", "name": "LG화학", "sk": False},
    {"code": "011780", "name": "금호석유화학", "sk": False},
    {"code": "009830", "name": "한화솔루션", "sk": False},
    {"code": "006650", "name": "대한유화", "sk": False},
    {"code": "373220", "name": "LG에너지솔루션", "sk": False},
    {"code": "006400", "name": "삼성SDI", "sk": False},
]

QUOTE_URL = "https://finance.naver.com/item/main.naver?code={code}"


def _num(v: Any) -> Optional[float]:
    """'120,300' · '-1,000' · '.75' → float. 못 읽으면 None."""
    try:
        return float(str(v).replace(",", "").strip())
    except (TypeError, ValueError):
        return None


def _fetch_naver(client: httpx.Client, code: str) -> Optional[Dict[str, Any]]:
    """실시간 체결가. compareToPreviousPrice.code 로 등락 방향을 판정한다.

    ★ compareToPreviousClosePrice 는 하락일 때 이미 음수 문자열('-1,000')로 온다.
      부호를 또 뒤집으면 안 된다 — code(2=상승, 5=하락)는 검증용으로만 쓴다.
    """
    try:
        r = client.get(_NAVER.format(code=code), headers={"User-Agent": _UA})
        r.raise_for_status()
        d = r.json()
    except Exception:
        return None
    close = _num(d.get("closePrice"))
    if close is None:
        return None
    traded = str(d.get("localTradedAt") or "")
    return {
        "code": str(d.get("itemCode") or code),
        "name": (d.get("stockName") or "").strip(),
        "basDt": traded[:10].replace("-", ""),          # 'YYYY-MM-DDT..' → 'YYYYMMDD'
        "close": int(close),
        "diff": int(_num(d.get("compareToPreviousClosePrice")) or 0),
        "rate": _num(d.get("fluctuationsRatio")) or 0.0,
    }


def _fetch_datago(client: httpx.Client, code: str) -> Optional[Dict[str, Any]]:
    """직전 영업일 종가(공식). 네이버가 죽었을 때만 쓴다.

    basDt 를 지정하지 않는 것은 의도적이다 — 휴장일·연휴에는 '어제' 가 존재하지 않아
    날짜를 박으면 빈 응답이 온다. 지정하지 않으면 가장 최근 영업일이 알아서 온다.
    serviceKey 는 params 로 넘기므로 반드시 **Decoding 키(원문)** 여야 한다.
    """
    if not DATA_GO_KR_SERVICE_KEY:
        return None
    try:
        r = client.get(_DATAGO, params={
            "serviceKey": DATA_GO_KR_SERVICE_KEY, "resultType": "json",
            "numOfRows": 1, "pageNo": 1, "likeSrtnCd": code,
        })
        r.raise_for_status()
        items = ((r.json().get("response") or {}).get("body") or {}).get("items") or {}
        items = items.get("item")
    except Exception:
        return None
    if not items:
        return None
    it = items[0] if isinstance(items, list) else items
    close = _num(it.get("clpr"))
    if close is None:
        return None
    return {
        "code": str(it.get("srtnCd") or code),
        "name": (it.get("itmsNm") or "").strip(),
        "basDt": str(it.get("basDt") or ""),
        "close": int(close),
        "diff": int(_num(it.get("vs")) or 0),
        "rate": _num(it.get("fltRt")) or 0.0,
    }


def _fetch_one(client: httpx.Client, code: str) -> Optional[Dict[str, Any]]:
    """네이버 우선, 실패하면 공공데이터."""
    return _fetch_naver(client, code) or _fetch_datago(client, code)


_DDL = """
CREATE TABLE IF NOT EXISTS quote_daily (
    code       TEXT    NOT NULL,
    bas_dt     TEXT    NOT NULL,              -- 'YYYYMMDD' 체결일
    name       TEXT    NOT NULL,
    close      INTEGER NOT NULL,              -- 체결가(원)
    diff       INTEGER NOT NULL,              -- 전일 대비(원)
    rate       REAL    NOT NULL,              -- 등락률(%)
    fetched_at TEXT    NOT NULL,              -- 우리가 받아 온 시각(UTC ISO)
    PRIMARY KEY (code, bas_dt)
);
"""


def _ensure_table(conn) -> None:
    """schema.sql 을 다시 돌리지 않은 기존 DB 에서도 동작하게 한다(멱등)."""
    conn.executescript(_DDL)


def _save(rows: List[Dict[str, Any]]) -> None:
    """같은 날 값은 덮어쓴다(장중에는 계속 바뀐다). 날짜가 다르면 새 행으로 쌓인다."""
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    conn = get_connection()
    try:
        _ensure_table(conn)
        conn.executemany(
            """INSERT INTO quote_daily(code, bas_dt, name, close, diff, rate, fetched_at)
               VALUES(?,?,?,?,?,?,?)
               ON CONFLICT(code, bas_dt) DO UPDATE SET
                 name=excluded.name, close=excluded.close, diff=excluded.diff,
                 rate=excluded.rate, fetched_at=excluded.fetched_at""",
            [(r["code"], r["basDt"], r["name"], r["close"], r["diff"], r["rate"], now)
             for r in rows],
        )
        conn.commit()
    finally:
        conn.close()


def _cached() -> Dict[str, Dict[str, Any]]:
    """종목별 최신 기준일 1행. _fetch_one 과 **같은 키 이름**으로 맞춰 돌려준다."""
    conn = get_connection()
    try:
        _ensure_table(conn)
        rows = conn.execute(
            """SELECT q.* FROM quote_daily q
                WHERE q.bas_dt = (SELECT MAX(bas_dt) FROM quote_daily x WHERE x.code = q.code)"""
        ).fetchall()
    except Exception:
        return {}
    finally:
        conn.close()
    return {
        r["code"]: {
            "code": r["code"], "name": r["name"], "basDt": r["bas_dt"],
            "close": r["close"], "diff": r["diff"], "rate": r["rate"],
            "fetched_at": r["fetched_at"],
        }
        for r in rows
    }


def _fresh_enough(cache: Dict[str, Dict[str, Any]]) -> bool:
    """캐시가 TTL 안이고 관심 종목을 전부 덮고 있는가."""
    if len(cache) < len(WATCH):
        return False
    try:
        newest = max(datetime.fromisoformat(v["fetched_at"]) for v in cache.values())
    except Exception:
        return False
    return (datetime.now(timezone.utc) - newest).total_seconds() < QUOTE_TTL_SEC


def quotes(force: bool = False) -> Dict[str, Any]:
    """화면 티커용 시세 묶음.

      {"quotes": [{code,name,sk,url,close,diff,rate}], "at": "16:10"}

    close 가 None 인 원소는 값을 못 받은 종목이다 — 화면은 숫자 없이 이름과 링크만 그린다.
    """
    cache = _cached()
    fetched: List[Dict[str, Any]] = []
    if force or not _fresh_enough(cache):
        with httpx.Client(timeout=QUOTE_TIMEOUT) as client:
            with ThreadPoolExecutor(max_workers=6) as pool:
                fetched = [r for r in pool.map(
                    lambda w: _fetch_one(client, w["code"]), WATCH) if r]
        if fetched:
            _save(fetched)
            cache = _cached()

    got = {r["code"]: r for r in fetched}
    out: List[Dict[str, Any]] = []
    for w in WATCH:
        src = got.get(w["code"]) or cache.get(w["code"])
        out.append({
            "code": w["code"],
            # 표시 이름은 우리 목록을 우선한다 — 소스마다 'S-Oil'/'에쓰오일' 처럼 표기가 갈린다.
            "name": w["name"],
            "sk": w["sk"],
            "url": QUOTE_URL.format(code=w["code"]),
            "close": int(src["close"]) if src else None,
            "diff": int(src["diff"]) if src else None,
            "rate": float(src["rate"]) if src else None,
        })

    # 갱신 시각(HH:MM). 화면이 티커 옆에 조용히 붙이는 용도다.
    try:
        newest = max(datetime.fromisoformat(v["fetched_at"]) for v in cache.values())
        at = newest.astimezone().strftime("%H:%M")
    except Exception:
        at = ""
    return {"at": at, "quotes": out}
