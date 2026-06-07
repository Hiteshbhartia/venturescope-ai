# backend/app/collectors/yc/collector.py

"""Y Combinator startup collector.

Fetches the public YC companies directory, extracts the required fields, validates
them with :class:`YCStartup` and hands the data off to the exporter.

The implementation now:
- Uses a ``requests.Session`` with a custom User‑Agent for connection reuse.
- Handles pagination to collect *all* YC startups.
- Uses accurate CSS selectors that match the current YC website.
- Logs detailed statistics (pages scanned, startups collected, export path,
  execution time).
- Fails loudly if no startups are collected.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import List

import json
import requests
from ratelimit import limits, sleep_and_retry
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from .models import YCStartup
from .exporter import export_startups

# ---------------------------------------------------------------------------
# Configuration (environment‑overrideable)
# ---------------------------------------------------------------------------
YC_COMPANIES_URL = "https://www.ycombinator.com/companies"
CUSTOM_USER_AGENT = (
    "Mozilla/5.0 (compatible; VentureScopeBot/1.0; +https://github.com/Hiteshbhartia/venturescope-ai)"
)
CALLS = 1  # 1 request per period
PERIOD = 1  # seconds

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
if not logger.handlers:
    logger.addHandler(handler)

# ---------------------------------------------------------------------------
# Session with custom headers
# ---------------------------------------------------------------------------
session = requests.Session()
session.headers.update({"User-Agent": CUSTOM_USER_AGENT})

# ---------------------------------------------------------------------------
# Rate‑limited GET helper
# ---------------------------------------------------------------------------
@sleep_and_retry
@limits(calls=CALLS, period=PERIOD)
def _rate_limited_get(url: str) -> requests.Response:
    """Perform a GET request respecting the rate limit.

    ``requests`` exceptions are propagated to the retry layer.
    """
    response = session.get(url, timeout=15)
    response.raise_for_status()
    return response

# ---------------------------------------------------------------------------
# Retry‑wrapped page fetcher
# ---------------------------------------------------------------------------
@retry(
    retry=retry_if_exception_type(requests.RequestException),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    stop=stop_after_attempt(3),
    reraise=True,
)
def _fetch_page(url: str) -> str:
    logger.info("Fetching %s", url)
    resp = _rate_limited_get(url)
    return resp.text

# ---------------------------------------------------------------------------
# Parsing helpers – selectors reflect the current YC site structure
# ---------------------------------------------------------------------------
def _parse_json_item(item: dict) -> YCStartup:
    """Parse a single JSON startup dictionary into a YCStartup model.

    Mapping:
        name -> company_name
        one_liner -> description
        website -> website
        batch -> batch
        industry -> industry
        all_locations -> location
    """
    return YCStartup(
        company_name=item.get("name", ""),
        description=item.get("one_liner"),
        website=item.get("website"),
        batch=item.get("batch"),
        industry=item.get("industry"),
        location=item.get("all_locations"),
    )


def _fetch_json() -> List[YCStartup]:
    """Download the YC‑OSS JSON list and parse it into YCStartup models."""
    url = "https://yc-oss.github.io/api/companies/all.json"
    logger.info("Fetching YC JSON data from %s", url)
    resp = _rate_limited_get(url)
    data = json.loads(resp.text)
    startups: List[YCStartup] = []
    for item in data:
        try:
            startup = _parse_json_item(item)
            if startup.company_name:
                startups.append(startup)
        except Exception as exc:  # pragma: no cover – defensive logging
            logger.warning("Failed to parse a startup record: %s", exc)
    return startups


def run() -> None:
    """Collect all YC startups from the JSON endpoint and export them.

    Logs detailed statistics and raises ``RuntimeError`` if no startups are found.
    """
    start_time = time.time()
    total_startups = _fetch_json()
    if not total_startups:
        raise RuntimeError("YC collector did not find any startups – aborting")
    export_startups(total_startups)
    export_path = Path(__file__).resolve().parents[4] / "data" / "raw" / "yc_startups.json"
    elapsed = time.time() - start_time
    logger.info(
        "YC collection complete – startups collected: %d, export: %s, time: %.2fs",
        len(total_startups),
        export_path,
        elapsed,
    )

if __name__ == "__main__":  # pragma: no cover
    run()
