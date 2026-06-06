"""Backend FastAPI application entry point.

Imports the API versioned router and creates the FastAPI app.
"""

from fastapi import FastAPI
from app.api.v1 import health

app = FastAPI(title="VentureScope AI Backend", version="0.1.0")
app.include_router(health.router, prefix="/api/v1")
