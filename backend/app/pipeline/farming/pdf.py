"""PDF 텍스트 추출.

IR Presentation · 지속가능경영보고서 등 PDF 자료의 본문을 텍스트로 뽑습니다.

★ 지우지 마라 — 관리자 업로드 경로가 쓴다: app/api/admin.py 의
POST /api/admin/uploads/file 이 PDF 본문을 여기서 뽑아 upload_file.body 에 넣고,
그 본문이 prefetch._upload_block 을 거쳐 발굴 프롬프트로 들어간다.

크롤러 쪽에는 아직 소비처가 없습니다. DART 는 XML(dart.xml_to_text), SEC 는
HTML(sec.html_to_text)로 원문을 확보하기 때문입니다. SKI IR 자료·지속가능경영보고서를
소스로 붙이면 그때도 그대로 쓸 수 있게 인터페이스를 맞춰 두었습니다.

    from app.pipeline.farming import pdf
    text = pdf.extract_text("ir_2026q2.pdf")
    doc.body = text            # 이후는 dart/sec 와 동일하게 llm.enrich() 로 흐릅니다
"""
import io
import re
from pathlib import Path
from typing import Union

# 다른 소스와 동일한 정책 — 디스크·토큰 보호
MAX_CHARS = 300_000

_WS_RE = re.compile(r"[ \t]+")


def extract_text(src: Union[str, Path, bytes], max_chars: int = MAX_CHARS) -> str:
    """PDF(경로 또는 바이트) → 평문 텍스트.

    pypdf 가 없거나 파일이 깨졌으면 예외를 올립니다 — 호출 측(크롤러)이
    건 단위로 격리해 한 건 실패가 전체를 멈추지 않게 하세요.
    """
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(src) if isinstance(src, bytes) else str(src))
    pages, got = [], 0
    for page in reader.pages:
        try:
            chunk = page.extract_text() or ""
        except Exception:
            # 페이지 단위 격리 — 표/폰트 문제로 일부 페이지만 실패할 수 있습니다.
            continue
        pages.append(chunk)
        got += len(chunk)
        if got >= max_chars:
            # 어차피 뒤에서 잘라낼 분량이라 더 파싱하지 않습니다. 수백 페이지 스캔본에서
            # 전 페이지를 파싱하면 업로드 응답이 그만큼 늦어집니다.
            break

    text = _WS_RE.sub(" ", "\n".join(pages))
    lines = [ln.strip() for ln in text.split("\n")]
    return "\n".join(ln for ln in lines if ln)[:max_chars]
