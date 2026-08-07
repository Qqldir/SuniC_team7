"""지식 파밍 layer — 크롤링 · PDF · LLM · 엔티티 추출.

모듈:
- crawler.py + dart.py / sec.py / news.py : 소스별 크롤러.
  watchlist.py 대상 → RawDoc 목록. DART 는 DART_API_KEY 필요, SEC/뉴스는 키 불필요.
- llm.py / entity.py / classify.py : LLM 요약·지표 추출, 계열사 태깅, 규칙 표시값.
- ingest.py : llm.enrich → classify → entity.tag_affiliates → feed_item 적재.
              LLM 정제가 실패하면 naive 절삭 요약으로 떨어진다.
- pdf.py    : PDF 본문 추출. 크롤러가 아니라 관리자 업로드(api/admin.py)가 쓴다.
- run.py    : 실행 CLI  (python -m app.pipeline.farming.run)

흐름:  watchlist → crawler → ingest(llm·classify·entity) → feed_item
"""
