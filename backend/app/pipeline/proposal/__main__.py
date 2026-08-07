"""python -m app.pipeline.proposal — 제안서 문서 CLI.

`python -m <패키지>` 는 __init__.py 가 아니라 이 파일을 실행한다.
옛 POST /api/proposal/{build,markdown} 을 대신하는 진입점이므로 지우지 마라.
"""
from app.pipeline.proposal import _main

if __name__ == "__main__":
    _main()
