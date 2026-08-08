"""LLM provider 정책 회귀 테스트.

SK 사내망은 codex 만 허용한다. 그래서 지켜야 할 것이 셋이다.

1. 모든 LLM 호출이 `app.llm_client` 를 거친다 — SDK 를 직접 부르는 모듈이 있으면
   그 기능은 사내망에서 통째로 죽는다.
2. provider 기본값이 codex-cli 다.
3. codex 가 아닌 provider 는 `ready()` 가 거부한다 — 조용히 폴백하면
   "왜 요약이 전부 naive 인지" 를 추적할 수 없다.

셋 다 사람이 눈으로 지키기 어려운 종류라 테스트로 고정한다.

    cd backend && .venv/bin/python -m pytest tests/ -q
"""
import ast
import os
import re
import sys
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND))

# llm_client 는 provider 구현체라 SDK 를 직접 import 하는 것이 당연하다.
SDK_ALLOWED = {BACKEND / "app" / "llm_client.py"}
SDK_MODULES = {"anthropic", "openai"}


def _python_files():
    for root in ("app", "tools"):
        for path in (BACKEND / root).rglob("*.py"):
            if "__pycache__" not in path.parts:
                yield path


def test_llm_sdk_는_llm_client_밖에서_쓰이지_않는다():
    """LLM SDK 직접 import 를 금지한다 (llm_client 제외).

    사내망에서는 codex 만 허용되므로, SDK 를 직접 부르는 경로는 실행 자체가 불가능하다.
    새 기능을 붙일 때 습관적으로 `from anthropic import ...` 를 쓰는 것을 여기서 막는다.
    """
    offenders = []
    for path in _python_files():
        if path in SDK_ALLOWED:
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            mods = []
            if isinstance(node, ast.Import):
                mods = [a.name.split(".")[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                mods = [node.module.split(".")[0]]
            for m in mods:
                if m in SDK_MODULES:
                    offenders.append(f"{path.relative_to(BACKEND)}:{node.lineno} → {m}")
    assert not offenders, (
        "llm_client 를 우회해 LLM SDK 를 직접 씁니다. 사내망(codex 전용)에서 동작하지 않습니다:\n  "
        + "\n  ".join(offenders)
    )


def test_provider_기본값이_codex다():
    """.env 가 없는 환경에서도 codex 로 뜨는지."""
    src = (BACKEND / "app" / "config.py").read_text(encoding="utf-8")
    for name in ("OI_TASK_PROVIDER", "OI_LLM_PROVIDER"):
        m = re.search(rf'{name} = os\.getenv\("{name}", "([^"]+)"\)', src)
        assert m, f"{name} 기본값을 찾지 못했습니다"
        assert m.group(1) == "codex-cli", f"{name} 기본값이 {m.group(1)} 입니다"


def test_env_example_이_codex를_가리킨다():
    """새로 받은 사람이 .env.example 을 복사하면 바로 codex 로 뜬다."""
    env = (BACKEND / ".env.example").read_text(encoding="utf-8")
    for name in ("OI_TASK_PROVIDER", "OI_LLM_PROVIDER"):
        assert re.search(rf"^{name}=codex-cli\s*$", env, re.M), f"{name} 이 codex-cli 가 아닙니다"


@pytest.mark.parametrize("provider", ["claude-cli", "anthropic", "openai", "정체불명"])
def test_codex_아닌_provider_는_거부된다(provider):
    from app import llm_client

    ok, why = llm_client.ready(provider)
    assert ok is False
    assert "codex" in why, f"거부 사유에 정책 설명이 없습니다: {why}"


def test_정책_해제하면_사외에서_쓸_수_있다(monkeypatch):
    """OI_CODEX_ONLY=0 이면 사외 개발 환경에서 다른 provider 로 실험할 수 있어야 한다."""
    from app import llm_client

    monkeypatch.setattr(llm_client, "OI_CODEX_ONLY", False)
    monkeypatch.setattr(llm_client, "OPENAI_API_KEY", "sk-test")
    ok, _ = llm_client.ready("openai")
    assert ok is True


def test_codex만_스키마를_강제할_수_있다():
    from app import llm_client

    assert llm_client.supports_schema("codex-cli") is True
    for other in ("claude-cli", "anthropic", "openai"):
        assert llm_client.supports_schema(other) is False
