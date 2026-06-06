# VentureScope AI - API Specification v1

## API Design Principles

The API must:

1. Be RESTful.
2. Support analytics workloads.
3. Support machine learning predictions.
4. Support AI-powered startup intelligence.
5. Remain extensible for future versions.

---

# Base URL

/api/v1

---

# Startup Discovery APIs

## Get All Startups

GET /api/v1/startups

Description:

Retrieve startups with filtering and pagination.

Query Parameters:

- industry
- country
- startup_stage
- page
- limit

Response:

200 OK

---

## Get Startup Details

GET /api/v1/startups/{startup_id}

Description:

Retrieve detailed startup profile.

Response:

200 OK

---

# Startup Intelligence APIs

## Get Startup Scores

GET /api/v1/startups/{startup_id}/scores

Description:

Retrieve VentureScope intelligence scores.

Response:

- Growth Score
- Funding Score
- Ecosystem Score
- Innovation Score

---

## Get Similar Startups

GET /api/v1/startups/{startup_id}/similar

Description:

Retrieve startups with similar characteristics.

Response:

List of related startups.

---

# Prediction APIs

## Get Funding Prediction

GET /api/v1/startups/{startup_id}/prediction

Description:

Retrieve funding probability prediction.

Response:

- Funding Probability
- Predicted Outcome
- Model Version

---

## Get Prediction Explanations

GET /api/v1/startups/{startup_id}/prediction/explanations

Description:

Retrieve explainable AI outputs.

Response:

- Feature Contributions
- Explanation Text

---

# Pattern Analysis APIs

## Get Failure Patterns

GET /api/v1/startups/{startup_id}/failure-patterns

Description:

Retrieve identified failure indicators.

---

## Get Success Patterns

GET /api/v1/startups/{startup_id}/success-patterns

Description:

Retrieve identified success indicators.

---

# Ecosystem APIs

## Startup Galaxy

GET /api/v1/ecosystem/galaxy

Description:

Retrieve startup ecosystem graph.

Response:

Nodes and edges.

---

## Startup Relationships

GET /api/v1/startups/{startup_id}/relationships

Description:

Retrieve startup graph connections.

---

# AI Intelligence APIs

## Analyze Startup

POST /api/v1/ai/analyze

Description:

Generate AI-powered startup analysis.

Request:

{
  "startup_id": "uuid"
}

Response:

{
  "analysis": "...",
  "insights": [...]
}

---

## Compare Startups

POST /api/v1/ai/compare

Description:

Compare multiple startups.

Request:

{
  "startup_ids": []
}

Response:

Comparative analysis.

---

# API Version

Version: 1.0

Status: Approved
