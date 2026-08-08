"""계열사 원본 DB → backend/knowledge/ 지식 베이스 빌드 (S0~S5).

절차는 docs/knowledge-base-flow.md, 이 패키지 주석의 '전략 §x.y' 는
docs/llm-agent-knowledge-strategy.md 의 절 번호다.

★ 이 패키지는 빌드 전용이 아니다 — app/pipeline/knowledge/prefetch.py 가
  tools.kb_build.common.est_tokens 를 런타임에 import 한다. 배포에서 빼지 마라.
"""
