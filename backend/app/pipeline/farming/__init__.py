"""지식 파밍 layer — 크롤링 · PDF · LLM · 엔티티 추출.

구현 현황:
- crawler.py + dart.py / sec.py / news.py : 소스별 크롤러 (구현)
  watchlist.py 대상 → RawDoc 목록. DART 는 DART_API_KEY 필요, SEC/뉴스는 키 불필요.
- ingest.py : RawDoc → feed_item / feed_item_tag 적재 (구현, 요약은 naive)
- run.py    : 실행 CLI  (python -m app.pipeline.farming.run)
- pdf.py / llm.py / entity.py : 원문 본문 추출·LLM 요약·정밀 태깅 (스텁, 다음 단계)

흐름:  watchlist → crawler → (pdf·llm·entity) → ingest → feed_item
"""
