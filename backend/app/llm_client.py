"""공용 LLM 호출 계층 — provider 를 갈아끼울 수 있게 감싼 얇은 래퍼.

단계마다 필요한 모델 급이 다르고(파밍 정제는 작은 모델로 충분하지만 과제 발굴은 강한
모델이 필요합니다), 상황에 따라 쓸 수 있는 인증 수단도 다릅니다. 그래서 호출부는 이
모듈만 보고, provider 선택은 설정으로 밀어냅니다.

    codex-cli   **기본이자 사내망에서 유일하게 허용되는 provider.**
                로컬 `codex exec` 서브프로세스. API 키가 아니라 ChatGPT 로그인을 씁니다.
                `--output-schema` 로 응답 JSON 형태를 서버측에서 강제할 수 있는 유일한
                provider 입니다(supports_schema=True). 호출당 10~15초.
    claude-cli  로컬 `claude -p` 서브프로세스. **API 키 불필요** — Claude Code 로그인을 씁니다.
                호출당 20~35초라 배치/비동기 경로 전용.
    anthropic   Anthropic SDK. ANTHROPIC_API_KEY 필요.
    openai      OpenAI SDK. OPENAI_API_KEY 필요.

**SK 사내망 정책상 codex 외 provider 는 쓸 수 없습니다.** 아래 셋은 사외 개발용으로만
남겨 두었고, `OI_CODEX_ONLY=1`(기본)이면 ready() 가 거부합니다.

모든 provider 가 같은 `call(user, system, model, provider, *, schema=None) -> str` 을 노출하므로
호출부는 어느 것이 쓰이는지 알 필요가 없습니다. `schema` 는 **키워드 전용**입니다 —
기존 4-positional 호출부를 그대로 두기 위해서입니다.
"""
import json
import os
import subprocess
import tempfile
import time
from typing import Callable, Dict, Optional

from app.config import (
    ANTHROPIC_API_KEY, OI_CODEX_BIN, OI_CODEX_EFFORT, OI_CODEX_IGNORE_USER_CONFIG,
    OI_CODEX_ONLY,
    OI_CODEX_MODEL,
    OI_CODEX_RETRY, OI_CODEX_TIMEOUT, OI_LLM_BASE_URL, OI_LLM_TIMEOUT, OPENAI_API_KEY,
)

MAX_TOKENS = 2000

# codex 실패 후 재시도 대기(초). 실측상 401 은 산발적이고 다음 호출에서 자동 회복됩니다.
_CODEX_BACKOFF = (1, 3)


def _with_schema_hint(system: str, schema: Optional[dict]) -> str:
    """스키마를 서버측에서 강제하지 못하는 provider 용 soft 강제.

    codex 외 provider 는 형태 보장이 없으므로 system 뒤에 '## 출력 형식' 블록을 덧붙여
    프롬프트로만 유도합니다. 호출부의 파싱 재시도·폴백은 그대로 남겨 두어야 합니다.
    """
    if not schema:
        return system
    block = (
        "## 출력 형식\n"
        "아래 JSON Schema 를 만족하는 JSON 만 출력한다. 코드펜스나 설명 문장을 붙이지 않는다.\n"
        + json.dumps(schema, ensure_ascii=False, indent=2)
    )
    return f"{system}\n\n{block}" if system else block


# ── codex-cli ───────────────────────────────────────────────────────────

def codex_cli_available() -> bool:
    """`codex login status` 의 rc 로 판정합니다.

    `--version` 만 보면 설치는 됐지만 로그아웃 상태인 경우를 놓칩니다(거짓 양성).
    인증은 CODEX_HOME 을 읽어야 성립하므로, 다른 사용자·docker·systemd 컨텍스트에서는
    설치돼 있어도 rc=1("Not logged in") 입니다.
    """
    try:
        proc = subprocess.run(
            [OI_CODEX_BIN, "login", "status"], capture_output=True, timeout=15,
        )
        return proc.returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def _call_codex_cli(user: str, system: str, model: str, schema: Optional[dict] = None) -> str:
    """codex exec 로 1회 호출. `model` 인자는 무시하고 OI_CODEX_MODEL 만 봅니다.

    (claude 모델 별칭이 `codex -m` 으로 흘러들어 호출이 깨지는 것을 막기 위해서입니다.)

    codex 에는 --system-prompt 가 없으므로 system 과 user 를 합쳐 stdin 으로 넣습니다.
    결과는 stdout 이 아니라 `-o` 파일에서 읽습니다 — 실패하면 파일이 아예 생기지 않아
    '파일 존재 = 성공' 이 결정적 판정이 되기 때문입니다.
    """
    prompt = f"{system}\n\n{user}" if system else user

    # aux: 스키마·출력 파일용. neutral_cwd: codex 작업 루트로 넘길 빈 디렉터리
    # (프로젝트의 AGENTS.md·git 상태가 딸려 들어가지 않게 분리합니다).
    with tempfile.TemporaryDirectory() as aux, tempfile.TemporaryDirectory() as neutral_cwd:
        out_path = os.path.join(aux, "last_message.txt")
        cmd = [
            OI_CODEX_BIN, "exec",
            "--ephemeral",              # 세션 파일을 디스크에 남기지 않음
            "--skip-git-repo-check",    # git 저장소 밖에서도 실행
            "-s", "read-only",          # 모델이 만든 명령의 파일/네트워크 접근 차단
            "-C", neutral_cwd,
        ]
        # 인증 정보가 user config 쪽에 얽혀 401 이 나는 사례가 보고돼 기본값은 끔.
        # 저장소 오염 방지는 --ephemeral + -C 빈 디렉터리로 이미 확보됩니다.
        if OI_CODEX_IGNORE_USER_CONFIG:
            cmd.append("--ignore-user-config")
        if OI_CODEX_MODEL:
            cmd += ["-m", OI_CODEX_MODEL]
        if OI_CODEX_EFFORT:
            # 기본 xhigh 는 한 건에 3분이 넘는다. 스키마가 형태를 강제하므로
            # 우리 용도에서는 추론 강도를 낮춰도 품질 차이가 없고 10배 이상 빠르다.
            cmd += ["-c", f"model_reasoning_effort={OI_CODEX_EFFORT}"]
        if schema:
            schema_path = os.path.join(aux, "schema.json")
            with open(schema_path, "w", encoding="utf-8") as f:
                json.dump(schema, f, ensure_ascii=False)
            # 최상위는 object 여야 합니다. type:"array" 는 provider 가 HTTP 400 으로 거절합니다.
            cmd += ["--output-schema", schema_path]
        cmd += ["-o", out_path, "-"]

        detail = "(사유 불명)"
        for attempt in range(OI_CODEX_RETRY + 1):
            if os.path.exists(out_path):
                os.remove(out_path)  # 이전 시도의 잔재를 성공으로 오인하지 않게

            try:
                proc = subprocess.run(
                    cmd, input=prompt, capture_output=True, text=True,
                    timeout=OI_CODEX_TIMEOUT, cwd=neutral_cwd,
                )
                rc = proc.returncode
                # stderr 는 성공해도 수 KB(모델 캐시 경고 + 프롬프트 에코) 나옵니다 —
                # 실패 신호로 쓰면 안 되고, 실패했을 때 꼬리만 잘라 씁니다.
                detail = (proc.stderr or "").strip()[-300:] or "(stderr 없음)"
            except subprocess.TimeoutExpired:
                rc, detail = -1, f"타임아웃({OI_CODEX_TIMEOUT}초)"
            except OSError as e:
                raise RuntimeError(f"codex 실행 실패: {e}") from e

            if rc == 0 and os.path.exists(out_path):
                with open(out_path, encoding="utf-8") as f:
                    return f.read().strip()
            if rc == 0:
                detail = f"rc=0 이지만 출력 파일이 없습니다 / {detail}"

            if attempt < OI_CODEX_RETRY:
                time.sleep(_CODEX_BACKOFF[min(attempt, len(_CODEX_BACKOFF) - 1)])

        raise RuntimeError(
            f"codex exec 실패({OI_CODEX_RETRY + 1}회 시도): {detail}"
        )


# ── claude-cli ──────────────────────────────────────────────────────────

def claude_cli_available() -> bool:
    try:
        subprocess.run(["claude", "--version"], capture_output=True, timeout=15, check=True)
        return True
    except (OSError, subprocess.SubprocessError):
        return False


def _call_claude_cli(user: str, system: str, model: str, schema: Optional[dict] = None) -> str:
    cmd = [
        "claude", "-p",
        "--output-format", "json",
        "--model", model,
        # 모든 툴을 막습니다 — 순수 텍스트 변환이라 파일·셸 접근이 필요 없습니다.
        "--allowed-tools", "",
    ]
    system = _with_schema_hint(system, schema)
    if system:
        # --system-prompt 로 기본 시스템 프롬프트를 **교체**하면 프롬프트 캐시가 깨져
        # 비용이 2.5배가 됩니다(실측). 덧붙이는 쪽(--append-system-prompt)이 맞습니다.
        cmd += ["--append-system-prompt", system]

    # ANTHROPIC_API_KEY 가 환경에 있으면 claude CLI 가 로그인 대신 그 키를 씁니다.
    # 키에 크레딧이 없으면 100% 실패하므로, 이 경로에서만 환경에서 걷어냅니다.
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}

    # 프롬프트는 stdin 으로 넣습니다(본문이 길면 argv 길이 제한에 걸립니다).
    # cwd 는 빈 임시 디렉터리 — 프로젝트의 CLAUDE.md·git 상태가 딸려 들어가지 않게 분리합니다.
    with tempfile.TemporaryDirectory() as neutral_cwd:
        proc = subprocess.run(
            cmd, input=user, capture_output=True, text=True,
            timeout=OI_LLM_TIMEOUT, cwd=neutral_cwd, env=env,
        )
    if proc.returncode != 0:
        # 이 CLI 는 에러를 stdout 으로 내보내는 경우가 있어 두 스트림을 다 봅니다.
        detail = (proc.stderr.strip() or proc.stdout.strip() or "(출력 없음)")[:300]
        raise RuntimeError(f"claude -p 실패(rc={proc.returncode}): {detail}")

    envelope = json.loads(proc.stdout)
    if envelope.get("is_error") or envelope.get("subtype") != "success":
        raise RuntimeError(f"claude -p 오류: {str(envelope.get('result'))[:200]}")
    return envelope.get("result") or ""


# ── anthropic SDK ───────────────────────────────────────────────────────

def _call_anthropic(user: str, system: str, model: str, schema: Optional[dict] = None) -> str:
    if not ANTHROPIC_API_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY 가 설정되지 않았습니다.")
    from anthropic import Anthropic

    resp = Anthropic(api_key=ANTHROPIC_API_KEY).messages.create(
        model=model, max_tokens=MAX_TOKENS,
        system=_with_schema_hint(system, schema) or "",
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in resp.content if b.type == "text")


# ── openai SDK ──────────────────────────────────────────────────────────

def _call_openai(user: str, system: str, model: str, schema: Optional[dict] = None) -> str:
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY 가 설정되지 않았습니다.")
    from openai import OpenAI

    kwargs = {"api_key": OPENAI_API_KEY}
    if OI_LLM_BASE_URL:
        kwargs["base_url"] = OI_LLM_BASE_URL

    messages = [{"role": "user", "content": user}]
    system = _with_schema_hint(system, schema)
    if system:
        messages.insert(0, {"role": "system", "content": system})
    resp = OpenAI(**kwargs).chat.completions.create(model=model, messages=messages)
    return resp.choices[0].message.content or ""


# 값 시그니처는 (user, system, model, schema) 4인자로 통일돼 있습니다.
PROVIDERS: Dict[str, Callable[[str, str, str, Optional[dict]], str]] = {
    "codex-cli": _call_codex_cli,
    "claude-cli": _call_claude_cli,
    "anthropic": _call_anthropic,
    "openai": _call_openai,
}

# 응답 형태를 서버측에서 강제할 수 있는 provider. 나머지는 프롬프트로만 유도합니다.
_SCHEMA_PROVIDERS = {"codex-cli"}


def supports_schema(provider: str) -> bool:
    """schema 가 '보장' 되는지 여부. False 면 호출부는 파싱 재시도를 유지해야 합니다."""
    return provider in _SCHEMA_PROVIDERS


# 사내망에서 허용되는 provider
ALLOWED_IN_HOUSE = {"codex-cli"}


def ready(provider: str) -> tuple[bool, str]:
    """provider 를 쓸 수 있는지와, 못 쓰면 그 사유."""
    if OI_CODEX_ONLY and provider not in ALLOWED_IN_HOUSE:
        return False, (
            f"'{provider}' 는 사내망 정책상 쓸 수 없습니다 (codex 만 허용). "
            f"OI_LLM_PROVIDER/OI_TASK_PROVIDER 를 codex-cli 로 두세요. "
            f"사외 개발 환경이라면 OI_CODEX_ONLY=0 으로 해제할 수 있습니다."
        )
    if provider == "codex-cli":
        if not codex_cli_available():
            return False, "codex CLI 를 쓸 수 없습니다 (설치 후 `codex login` 확인)"
        return True, ""
    if provider == "claude-cli":
        if not claude_cli_available():
            return False, "claude CLI 를 찾을 수 없습니다 (설치/로그인 확인)"
        return True, ""
    if provider == "anthropic":
        return (True, "") if ANTHROPIC_API_KEY else (False, "ANTHROPIC_API_KEY 미설정")
    if provider == "openai":
        return (True, "") if OPENAI_API_KEY else (False, "OPENAI_API_KEY 미설정")
    return False, f"알 수 없는 provider: {provider}"


def call(user: str, system: str, model: str, provider: str, *, schema: Optional[dict] = None) -> str:
    """provider 로 프롬프트를 돌리고 응답 텍스트를 돌려준다.

    `schema` 는 키워드 전용입니다 — 기존 4-positional 호출부가 무변경으로 돌아야 합니다.
    supports_schema(provider) 가 True 면 형태가 보장되고, False 면 프롬프트 유도에 그칩니다.
    """
    fn = PROVIDERS.get(provider)
    if fn is None:
        raise RuntimeError(f"알 수 없는 provider: {provider}")
    return fn(user, system, model, schema)
