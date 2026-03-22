"""
api/index.py — Vercel serverless entry point for the single-project deployment.

Adds backend/ to sys.path so FastAPI and services are importable,
then exposes `app` for Vercel's ASGI runtime.
"""

import sys
import os

# backend/ contains main.py and services/
_backend = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
sys.path.insert(0, _backend)

from main import app  # noqa: F401
