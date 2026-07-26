"""수집 원문의 LLM 요약 (스텁).

crawler/pdf 로 수집한 장문 원문을 feed_item.summary 수준으로 요약.
app.pipeline.discovery.agent 의 Claude 클라이언트를 재사용할 수 있음.
"""


def summarize(text: str, max_chars: int = 200) -> str:
    raise NotImplementedError("LLM 요약 미구현")
