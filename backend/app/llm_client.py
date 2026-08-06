"""Shared LLM call layer — a thin wrapper that lets providers be swapped out.

Each pipeline stage needs a different model tier (a small model is enough for
farming refinement, task discovery needs a stronger one), and which credentials
are usable varies by situation. So callers only ever see this module, and the
provider choice is pushed out into configuration.

    claude-cli  Local `claude -p` subprocess. **No API key needed** — it uses the
                Claude Code login. 20-35s per call, so batch/async paths only.
    anthropic   Anthropic SDK. Requires ANTHROPIC_API_KEY.
    openai      OpenAI SDK. Requires OPENAI_API_KEY.

Every provider exposes the same `call(user, system, model) -> str`, so callers
never need to know which one is in use.
"""
import json
import os
import subprocess
import tempfile
from typing import Callable, Dict

from app.config import (
    ANTHROPIC_API_KEY, OI_LLM_BASE_URL, OI_LLM_TIMEOUT, OPENAI_API_KEY,
)

MAX_TOKENS = 2000


# ── claude-cli ──────────────────────────────────────────────────────────

def claude_cli_available() -> bool:
    try:
        subprocess.run(["claude", "--version"], capture_output=True, timeout=15, check=True)
        return True
    except (OSError, subprocess.SubprocessError):
        return False


def _call_claude_cli(user: str, system: str, model: str) -> str:
    cmd = [
        "claude", "-p",
        "--output-format", "json",
        "--model", model,
        # Block every tool — this is a pure text transform, so no file/shell access is needed.
        "--allowed-tools", "",
    ]
    if system:
        # Replacing the default system prompt via --system-prompt breaks the prompt
        # cache and ends up 2.5x more expensive (measured). Appending is the right call.
        cmd += ["--append-system-prompt", system]

    # Strip Anthropic auth env vars — app.config loads .env (for the anthropic/openai
    # providers) which puts ANTHROPIC_API_KEY in this process's environment. The `claude`
    # CLI subprocess would inherit it and switch from the CLI login to that API key,
    # defeating the point of this provider (and failing outright if the key is unfunded).
    env = {k: v for k, v in os.environ.items() if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")}

    # Feed the prompt over stdin (a long body would hit the argv length limit).
    # Point cwd at an empty temp dir so the project's CLAUDE.md and git state
    # don't get pulled in.
    with tempfile.TemporaryDirectory() as neutral_cwd:
        proc = subprocess.run(
            cmd, input=user, capture_output=True, text=True,
            timeout=OI_LLM_TIMEOUT, cwd=neutral_cwd, env=env,
        )
    if proc.returncode != 0:
        # The CLI sometimes writes errors to stdout, so check both streams.
        detail = (proc.stderr.strip() or proc.stdout.strip() or "(출력 없음)")[:300]
        raise RuntimeError(f"claude -p 실패(rc={proc.returncode}): {detail}")

    envelope = json.loads(proc.stdout)
    if envelope.get("is_error") or envelope.get("subtype") != "success":
        raise RuntimeError(f"claude -p 오류: {str(envelope.get('result'))[:200]}")
    return envelope.get("result") or ""


# ── anthropic SDK ───────────────────────────────────────────────────────

def _call_anthropic(user: str, system: str, model: str) -> str:
    if not ANTHROPIC_API_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY 가 설정되지 않았습니다.")
    from anthropic import Anthropic

    resp = Anthropic(api_key=ANTHROPIC_API_KEY).messages.create(
        model=model, max_tokens=MAX_TOKENS,
        system=system or "",
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in resp.content if b.type == "text")


# ── openai SDK ──────────────────────────────────────────────────────────

def _call_openai(user: str, system: str, model: str) -> str:
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY 가 설정되지 않았습니다.")
    from openai import OpenAI

    kwargs = {"api_key": OPENAI_API_KEY}
    if OI_LLM_BASE_URL:
        kwargs["base_url"] = OI_LLM_BASE_URL

    messages = [{"role": "user", "content": user}]
    if system:
        messages.insert(0, {"role": "system", "content": system})
    resp = OpenAI(**kwargs).chat.completions.create(model=model, messages=messages)
    return resp.choices[0].message.content or ""


PROVIDERS: Dict[str, Callable[[str, str, str], str]] = {
    "claude-cli": _call_claude_cli,
    "anthropic": _call_anthropic,
    "openai": _call_openai,
}


def ready(provider: str) -> tuple[bool, str]:
    """Whether the provider is usable, and why not if it isn't."""
    if provider == "claude-cli":
        if not claude_cli_available():
            return False, "claude CLI 를 찾을 수 없습니다 (설치/로그인 확인)"
        return True, ""
    if provider == "anthropic":
        return (True, "") if ANTHROPIC_API_KEY else (False, "ANTHROPIC_API_KEY 미설정")
    if provider == "openai":
        return (True, "") if OPENAI_API_KEY else (False, "OPENAI_API_KEY 미설정")
    return False, f"알 수 없는 provider: {provider}"


def call(user: str, system: str, model: str, provider: str) -> str:
    """Run the prompt through the provider and return the response text."""
    fn = PROVIDERS.get(provider)
    if fn is None:
        raise RuntimeError(f"알 수 없는 provider: {provider}")
    return fn(user, system, model)
