"""O/I Scout FastAPI 진입점."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import CORS_ORIGINS
from app.api import feed, tasks, discovery

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


@app.get("/api/health")
def health():
    return {"status": "ok"}
