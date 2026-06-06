# VentureScope AI – Backend Foundation

This repository contains the initial FastAPI backend scaffold for **VentureScope AI**.

## Project Structure
```
backend/
├── app/                # FastAPI application package
│   ├── api/            # API routers (versioned)
│   ├── collectors/    # Data collector placeholders (yc, github, producthunt, news)
│   ├── core/          # Configuration (Pydantic Settings v2)
│   ├── database/      # SQLAlchemy base and async session
│   ├── analytics/     # Placeholder for analytics utilities
│   ├── ml/            # Placeholder for ML orchestration
│   ├── graph/         # Placeholder for graph utilities
│   ├── ai/            # Placeholder for AI helpers
│   └── main.py        # FastAPI entry point
├── alembic/            # Database migration scripts
│   ├── env.py          # Alembic environment configuration (async)
│   └── versions/       # Migration versions
│       └── 0001_initial.py  # Initial empty migration
├── tests/              # Pytest suite (health check example)
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables for PostgreSQL
├── Dockerfile          # Multi‑stage Docker build for the API
├── docker-compose.yml  # Local development stack (API + PostgreSQL)
└── README.md           # This file
```

## Quick Start (Docker)
```bash
cd backend
docker compose up --build
```
The API will be reachable at `http://localhost:8000/api/v1/health`.

## Development (without Docker)
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Database Migrations
```bash
# Initialise the database (first run)
alembic upgrade head
```

More detailed documentation, additional endpoints, and business logic will be added in subsequent sprints.
