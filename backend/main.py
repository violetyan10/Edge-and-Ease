"""
main.py — FastAPI application entry point.

Endpoints:
  GET  /health      — liveness check
  POST /api/tip     — returns a coach tip for the given user input

Run locally:
  uvicorn main:app --reload --port 8000

On Vercel this module is imported by api/index.py which exposes `app`
as the ASGI entry point.
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from services.tip_service import retrieve_tip

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Edge & Ease API",
    description="Backend for the Edge & Ease wellness platform.",
    version="0.1.0",
)

# ---------------------------------------------------------------------------
# CORS
# Reads ALLOWED_ORIGINS from the environment so you can set the production
# Vercel frontend URL in the Vercel dashboard without touching code.
#
# Local default:  http://localhost:5173
# Production:     set ALLOWED_ORIGINS="https://your-frontend.vercel.app"
#                 (comma-separated for multiple origins)
# ---------------------------------------------------------------------------
_raw_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173")
allowed_origins = [o.strip() for o in _raw_origins.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Request / Response schemas
# ---------------------------------------------------------------------------
class TipRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="User's free-text input describing how they feel or what they need.",
    )


class TipResponse(BaseModel):
    coach: str
    suggestion: str


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.get("/health", tags=["system"])
def health_check():
    """Simple liveness probe."""
    return {"status": "ok"}


@app.post("/api/tip", response_model=TipResponse, tags=["tips"])
def get_tip(payload: TipRequest):
    """
    Accept a user query and return a personalised coach tip.

    Currently powered by mock data in services/tip_service.py.
    Swap retrieve_tip() for real RAG logic without changing this route.
    """
    try:
        result = retrieve_tip(payload.query)
        return TipResponse(**result)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
