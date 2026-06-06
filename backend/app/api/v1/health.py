# app/api/v1/health.py

"""Health‑check endpoint for API version 1.
GET /api/v1/health returns a simple JSON payload.
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check() -> dict:
    """Return basic service health.
    Future extensions may include DB ping, cache status, etc.
    """
    return {"status": "ok"}
