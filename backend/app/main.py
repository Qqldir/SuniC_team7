"""O/I Scout FastAPI 진입점."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import CORS_ORIGINS
from app.api import feed, tasks, discovery, cases, auth, admin
from app.db.database import ensure_auth_columns

app = FastAPI(title="O/I Scout API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(feed.router)
app.include_router(tasks.router)
app.include_router(discovery.router)
app.include_router(cases.router)
app.include_router(auth.router)
app.include_router(admin.router)

ensure_auth_columns()  # 기존 DB에 신규 인증 컬럼(is_admin) 마이그레이션


@app.get("/api/health")
def health():
    return {"status": "ok"}
