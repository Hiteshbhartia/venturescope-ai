# backend/app/collectors/yc/exporter.py

"""Exporter for Y Combinator collector.

Writes a list of :class:`YCStartup` objects to ``data/raw/yc_startups.json``
using UTF‑8 encoding and pretty‑printed JSON.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .models import YCStartup


def export_startups(startups: Iterable[YCStartup], *, output_path: str | None = None) -> None:
    """Serialize *startups* to a JSON file.

    Parameters
    ----------
    startups:
        Iterable of :class:`YCStartup` instances.
    output_path:
        Optional custom path. When ``None`` the default location
        ``data/raw/yc_startups.json`` relative to the repository root is used.
    """
    # Resolve default location – we assume this module lives under
    # ``backend/app/collectors/yc``; the repository root is two levels up.
    if output_path is None:
        repo_root = Path(__file__).resolve().parents[4]  # /backend
        output_path = repo_root / "data" / "raw" / "yc_startups.json"
    else:
        output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert Pydantic models to plain dicts for JSON serialisation.
    data = [startup.model_dump(mode='json', exclude_none=True) for startup in startups]

    with output_path.open("w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)

    # No return value – callers can log success themselves.
