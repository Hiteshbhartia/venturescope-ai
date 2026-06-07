# VentureScope AI

VentureScope AI is an AI-powered startup intelligence platform designed to help investors, analysts, founders, and researchers discover, evaluate, and monitor high-potential startups. By aggregating fragmented startup data from multiple sources and transforming it into actionable intelligence through analytics, machine learning, graph analysis, and explainable AI, VentureScope AI provides unparalleled insights into the global startup ecosystem.

## Vision Statement
To build the **Bloomberg Terminal for Startup Intelligence**. VentureScope AI provides a unified platform to discover emerging startups, analyze startup ecosystems, evaluate growth potential, predict funding outcomes, identify market trends, and generate AI-powered research reports.

## Why VentureScope?
Existing startup platforms focus on static directories, funding databases, or news aggregation.

VentureScope aims to combine:
* Startup Discovery
* Growth Signal Detection
* Funding Prediction
* Ecosystem Graph Analysis
* AI-Powered Research

into a single intelligence platform.

## Project Stage
Current Stage: MVP+ Development

Progress:
███████░░░ 35%

Completed:
✓ Research
✓ PRD
✓ Architecture
✓ Database Design
✓ API Design
✓ Backend Foundation
✓ YC Collector

## MVP Status

### Completed
* System Architecture
* Database Design
* API Design
* Backend Foundation
* YC Startup Collector
* Automated Testing
* Initial Startup Dataset

### In Progress
* PostgreSQL Integration
* Feature Engineering Pipeline
* Startup Scoring Engine

### Planned
* Product Hunt Collector
* GitHub Collector
* Analytics Layer
* ML Prediction Layer
* Graph Intelligence Layer
* Frontend Dashboard

## Current Dataset

| Metric                | Value            |
| --------------------- | ---------------- |
| YC Startups Collected | 5,908            |
| Data Source           | YC-OSS           |
| Validation            | Pydantic         |
| Tests Passing         | 4                |
| Collector Status      | Production Ready |

## Architecture Overview
VentureScope AI follows a highly modular, hybrid architecture tailored for robust data science workflows and scalable deployments:
- **Data Collection (Implemented):** Python-based YC collector utilizing reliable JSON ingestion APIs.
- **Data Collection (Planned):** Extensible collectors for platforms like Product Hunt, GitHub, and News feeds.
- **Data Processing (Planned):** Polars and DuckDB for efficient ETL pipelines, data cleaning, and feature engineering.
- **Data Storage:** Backend foundation established using FastAPI, Pydantic v2, Alembic configuration, Docker setup, and PostgreSQL-ready architecture.
- **Intelligence Layers (Planned):** 
  - *Analytics:* Growth and funding scores via statistical analysis.
  - *Machine Learning:* Funding predictions and startup classification using XGBoost and SHAP.
  - *Graph Intelligence:* Ecosystem and relationship mapping using NetworkX.
  - *AI Insight Layer:* AI-powered startup research and explainability layer.
- **API & Frontend (Planned):** A high-performance FastAPI backend serving a modern Next.js, TypeScript, and Tailwind CSS web application.

## Repository Structure
```text
venturescope-ai/
├── backend/
│   ├── alembic/            # Database migration scripts
│   ├── app/
│   │   ├── analytics/      # Statistical scoring & ecosystem metrics (Planned)
│   │   ├── api/            # FastAPI v1 route definitions
│   │   ├── collectors/     # Data ingestion (YC implemented; GitHub, Product Hunt, News planned)
│   │   ├── core/           # Global configuration & security
│   │   └── database/       # PostgreSQL / SQLAlchemy session management
│   ├── tests/              # Pytest test suite
│   ├── Dockerfile          # Backend container configuration
│   ├── docker-compose.yml  # Local multi-container deployment setup
│   └── requirements.txt    # Python dependencies
├── data/                   # Raw datasets and processed exports
├── docs/                   # System architecture, schemas, PRD, and research
├── frontend/               # Frontend workspace (implementation pending)
└── README.md
```

## Documentation Links
Deep dive into the project's foundation by reviewing the documentation:
- [Product Requirements Document (PRD)](docs/prd/PRD-v1.md)
- [System Architecture](docs/architecture/system-architecture-v1.md)
- [Database Schema](docs/database/database-schema-v1.md)
- [API Specification](docs/api/api-specification-v1.md)
- [Data Sources Evaluation](docs/research/data-sources-v1.md)
- [Competitive Analysis](docs/research/competitor-analysis.md)

## Technology Stack
- **Backend:** Python 3.12, FastAPI, Pydantic v2, Alembic
- **Database Layer (Planned):** PostgreSQL, SQLAlchemy 2.0, DuckDB
- **Data Engineering & ML (Planned):** Polars, XGBoost, NetworkX, Scikit-learn, SHAP
- **Artificial Intelligence (Planned):** Ollama, Qwen/DeepSeek
- **Frontend (Planned):** Next.js, TypeScript, Tailwind CSS, ShadCN UI, Three.js
- **DevOps & Infrastructure:** Docker, Docker Compose

## Installation & Setup
Currently, the backend data collection foundation is active. Follow these steps to set up the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/Hiteshbhartia/venturescope-ai.git
cd venturescope-ai

# 2. Set up a Python virtual environment
python -m venv .venv

# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# 3. Install backend dependencies
pip install -r backend/requirements.txt

# 4. Run the Y Combinator Data Collector
# Ensures all modules are discovered correctly from the root directory
set PYTHONPATH=.;backend
python -m backend.app.collectors.yc.collector

# 5. Run the Test Suite
pytest backend/tests/ -v
```

## Future Work & Roadmap
- Complete PostgreSQL integration and persist collected datasets using SQLAlchemy models.
- Implement the GitHub and Product Hunt data collection pipelines.
- Build out the ML and Analytics layers to calculate and serve growth and funding scores.
- Expose startup intelligence via FastAPI endpoints.
- Construct the interactive Next.js frontend with ecosystem visualizations.
- Implement an AI-powered startup research and explainability layer.
