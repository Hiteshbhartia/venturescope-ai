# VentureScope AI - System Architecture v1

## Architecture Goals

The architecture must satisfy the following objectives:

1. Support startup intelligence workflows.
2. Enable collection of startup data from multiple public sources.
3. Support analytics, machine learning, graph analysis, and AI-driven insights.
4. Remain scalable enough to evolve beyond the MVP.
5. Use modern technologies commonly adopted by startups and technology companies.
6. Maintain clear separation between data collection, analytics, machine learning, APIs, and frontend systems.

## Architecture Philosophy

The MVP will follow a hybrid architecture:

* Startup-grade architecture
* Recruiter-friendly implementation scope
* Production-style system design
* MVP-sized deployment

This approach balances engineering depth with realistic execution.

## High-Level Architecture

```
                ┌──────────────────┐
                │   Data Sources   │
                └────────┬─────────┘
                         │
                         ▼

    ┌─────────────────────────────────────┐
    │      Data Collection Layer          │
    │                                     │
    │  YC Scraper                         │
    │  Product Hunt Collector             │
    │  GitHub Collector                   │
    │  News Collector                     │
    └───────────────┬─────────────────────┘
                    │
                    ▼

    ┌─────────────────────────────────────┐
    │       Data Processing Layer         │
    │                                     │
    │  Polars                            │
    │  Data Cleaning                     │
    │  Feature Engineering               │
    │  ETL Pipelines                     │
    └───────────────┬─────────────────────┘
                    │
                    ▼

    ┌─────────────────────────────────────┐
    │      Data Storage Layer             │
    │                                     │
    │ PostgreSQL                          │
    │ DuckDB                              │
    └──────┬─────────┬─────────┬──────────┘
           │         │         │
           ▼         ▼         ▼

 ┌────────────┐ ┌──────────┐ ┌─────────────┐
 │ Analytics  │ │ ML Layer │ │ Graph Layer │
 └─────┬──────┘ └────┬─────┘ └──────┬──────┘
       │             │              │
       └──────┬──────┴──────┬───────┘
              ▼             ▼

      ┌────────────────────────────┐
      │      AI Insight Layer      │
      │                            │
      │ Ollama                     │
      │ Qwen / DeepSeek            │
      │ RAG Pipeline               │
      └────────────┬───────────────┘
                   │
                   ▼

      ┌────────────────────────────┐
      │         FastAPI            │
      └────────────┬───────────────┘
                   │
                   ▼

      ┌────────────────────────────┐
      │          Next.js           │
      └────────────────────────────┘
```

## Core Components

### Component 1: Data Collection Layer

Responsibilities:

* Collect startup data
* Collect GitHub metrics
* Collect Product Hunt information
* Collect news signals

Technology:

* Python
* Requests
* BeautifulSoup
* Scheduled jobs

---

### Component 2: Data Processing Layer

Responsibilities:

* Data cleaning
* Feature generation
* Transformation

Technology:

* Polars
* DuckDB

---

### Component 3: Analytics Engine

Responsibilities:

* Growth Score
* Funding Score
* Ecosystem Score
* Failure Pattern Analysis

Technology:

* Python
* Statistical Analysis

---

### Component 4: Machine Learning Layer

Responsibilities:

* Funding Prediction
* Startup Classification
* Explainability

Technology:

* XGBoost
* SHAP
* Scikit-learn

---

### Component 5: Graph Intelligence Layer

Responsibilities:

* Startup relationship mapping
* Founder networks
* Industry clustering

Technology:

* NetworkX

---

### Component 6: AI Insight Layer

Responsibilities:

* Startup research assistant
* Natural language analysis
* Research generation

Technology:

* Ollama
* Qwen
* RAG

---

### Component 7: API Layer

Responsibilities:

* Serve startup data
* Serve predictions
* Serve analytics

Technology:

* FastAPI

---

### Component 8: Frontend Layer

Responsibilities:

* Startup Explorer
* Dashboard
* Startup Profiles
* Startup Galaxy

Technology:

* Next.js
* TypeScript
* Tailwind
* ShadCN
* Three.js

