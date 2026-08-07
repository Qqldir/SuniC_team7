"""레버 표기 정규화 — LLM·혁신사례가 쓰는 변형 표기를 lever 마스터 정식명으로.

왜 필요한가
-----------
`proposal.lever` 는 `lever(name)` FK 이고 커넥션마다 `PRAGMA foreign_keys = ON` 이라
'정비·TA'(가운뎃점) · '간접비/가동률' · '기타' 같은 표기는 INSERT 자체가
FOREIGN KEY constraint failed 로 실패한다. 저장 직전 반드시 여기를 거쳐야 한다.

★ 정규화에 실패하면 **None 을 돌려준다. 임의 레버로 떨어뜨리지 않는다.**
  화면의 `LOGIC[lever].calc` 가 레버별로 고정된 계산식이라, 틀린 레버를 붙이면
  과제가 저장되기는 해도 화면이 **틀린 금액**을 계산해 보여 준다.
  조용히 틀린 숫자를 내는 것보다 그 과제 1건을 버리는 쪽이 낫다.
  호출부(discovery/persist.py)는 None 이면 그 과제를 건너뛴다.
"""
import re
from typing import Dict, Optional, Tuple

from app.db.database import get_connection

# 공백과 구분기호(·, /, (, ), -, —, ~, ., ,)를 지운다.
# '정비 · TA' / '정비/TA' / '정비-TA' 가 전부 같은 키('정비ta')로 모이게 하기 위함.
_SQUASH_RE = re.compile(r"[\s·/()\-—–~.,\[\]]+")


def squash(s: str) -> str:
    """비교용 키 — 공백·구분기호 제거 후 소문자."""
    return _SQUASH_RE.sub("", (s or "")).lower()


def _tables(conn) -> Tuple[Dict[str, str], Dict[str, str], Dict[str, str]]:
    """(정식명 집합, 별칭→정식명, 압축키→정식명) 세 표를 만든다."""
    levers = {r["name"]: r["name"] for r in conn.execute("SELECT name FROM lever")}
    aliases = {
        r["alias"]: r["lever"]
        for r in conn.execute("SELECT alias, lever FROM lever_alias")
    }
    # 압축키 표는 정식명이 우선이다 — 별칭이 정식명을 덮지 않게 정식명을 나중에 넣는다.
    squashed: Dict[str, str] = {}
    for alias, lever in aliases.items():
        squashed.setdefault(squash(alias), lever)
    for name in levers:
        squashed[squash(name)] = name
    return levers, aliases, squashed


def normalize_lever(raw: Optional[str], conn=None) -> Optional[str]:
    """레버 표기 하나를 lever 마스터 정식명으로 바꾼다. 실패하면 None.

    순서: (1) lever 정확 일치 → (2) lever_alias 조회 → (3) 압축키(공백·구분기호 제거) 재조회.
    conn 을 넘기면 그 커넥션을 쓰고, 안 넘기면 여기서 열고 닫는다(루프에서는 넘겨라).
    """
    if not raw or not str(raw).strip():
        return None
    text = str(raw).strip()

    own = conn is None
    if own:
        conn = get_connection()
    try:
        levers, aliases, squashed = _tables(conn)
        if text in levers:            # (1) 정식명 그대로
            return levers[text]
        if text in aliases:           # (2) 등록된 별칭
            return aliases[text]
        return squashed.get(squash(text))  # (3) 압축키. 없으면 None
    finally:
        if own:
            conn.close()


def known_levers(conn=None):
    """lever 마스터 정식명 목록(sort_order 순). 발굴 스키마의 enum 원본."""
    own = conn is None
    if own:
        conn = get_connection()
    try:
        return [r["name"] for r in conn.execute("SELECT name FROM lever ORDER BY sort_order, name")]
    finally:
        if own:
            conn.close()
