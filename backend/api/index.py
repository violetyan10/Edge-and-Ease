"""
api/index.py — Vercel serverless entry point.

Vercel's Python runtime discovers this file and serves `app` as an ASGI
application. All routing is handled by FastAPI; vercel.json rewrites every
request to this handler.

Nothing here should change when you add features — extend main.py instead.
"""

import sys
import os

# Make the backend root importable so `from services.tip_service import ...` works.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app  # noqa: F401  (Vercel picks up `app` automatically)
