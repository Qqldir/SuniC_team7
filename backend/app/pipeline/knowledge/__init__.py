"""지식 기반 layer — 발굴 agent 에게 근거를 공급한다.

- retriever.py  : backend/knowledge/ 의 파일 KB 검색·열람
- prefetch.py   : 블록별 토큰 예산에 맞춰 발굴 프롬프트 컨텍스트를 조립(build_context)
- repository.py : feed_item 등 DB 조회

codex 는 단발 호출이라 툴 루프를 못 돈다. 그래서 에이전트가 필요할 때 문서를 여는 대신
서버가 미리 골라 프롬프트에 실어 보낸다 — 그 골라 담는 일을 prefetch 가 한다.
"""
