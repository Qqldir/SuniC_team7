"""O/I Scout FastAPI 진입점."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.config import CORS_ORIGINS, FRONTEND_DIST, SERVE_FRONTEND
from app.api import admin, auth, bootstrap, evaluation, feed, proposals, report

app = FastAPI(title="O/I Scout API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── 화면(O/I Spark)이 쓰는 API ──
app.include_router(auth.router)
app.include_router(bootstrap.router)
app.include_router(proposals.router)
app.include_router(admin.router)
app.include_router(report.router)

# ── 파이프라인 API ──
# 파이프라인에는 HTTP 진입점을 최소로 둔다. 화면이 안 부르는 것은 라우터가 아니라
# 다른 경로로 노출한다:
#   혁신 사례   → 시드(app/db/seed_data.INNOVATION_CASES)로만 관리하고,
#                읽기는 prefetch._case_block 이 kb_innovation_case 를 직접 조회한다.
#   과제 발굴   → 커스텀 생성 화면(POST /api/proposals/custom → store.create_custom_llm)이
#                'OC 지정 + note 주입' 을 담당한다. 엔진 discovery/agent.py 는 store 가
#                재생성·커스텀 두 경로에서 쓴다.
#   제안서 문서 → CLI: python -m app.pipeline.proposal --pid <id>
app.include_router(feed.router)
app.include_router(evaluation.router)


@app.get("/api/health")
def health():
    return {"status": "ok"}


# ── 빌드된 프론트 서빙 (OI_SERVE_FRONTEND=1) ──
# 개발 중에는 Vite dev 서버(5173)가 화면을, 여기서는 API 만 담당합니다.
if SERVE_FRONTEND and FRONTEND_DIST.is_dir():
    assets = FRONTEND_DIST / "assets"
    if assets.is_dir():
        app.mount("/assets", StaticFiles(directory=assets), name="assets")

    @app.get("/trendroom.html", include_in_schema=False)
    def trendroom():
        return FileResponse(FRONTEND_DIST / "trendroom.html")

    @app.get("/{path:path}", include_in_schema=False)
    def spa(path: str):
        """정적 파일이 있으면 그대로, 없으면 SPA 진입점(index.html).

        ★ /api/* 는 여기서 처리하지 않는다. 이 catch-all 이 API 경로까지 삼키면
          없는(또는 삭제된) 엔드포인트가 404 대신 **HTML 을 200 으로** 돌려준다.
          클라이언트는 JSON 을 기대하다 파싱 오류를 만나고, 원인이 서버인지
          클라이언트인지 구분되지 않는다.
        """
        if path.startswith("api/"):
            raise HTTPException(status_code=404, detail="존재하지 않는 API 경로입니다.")
        target = FRONTEND_DIST / path
        if path and target.is_file():
            return FileResponse(target)
        return FileResponse(FRONTEND_DIST / "index.html")
