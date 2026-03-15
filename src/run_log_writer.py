"""Write structured run records into the harness runs directory."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Mapping

DEFAULT_RUNS_DIR = Path(__file__).resolve().parent.parent / ".harness" / "runs"
_IDENTIFIER_FIELDS = ("run_id", "task_id", "created_at")


def build_run_filename(payload: Mapping[str, Any]) -> str:
    """Build a deterministic filename from stable payload fields."""
    identifier = _select_identifier(payload)
    slug = _slugify(identifier)
    if not slug:
        raise ValueError("Run identifier must contain at least one alphanumeric character.")
    return f"run-{slug}.json"


def write_run_record(
    payload: Mapping[str, Any],
    runs_dir: Path | str | None = None,
) -> Path:
    """Serialize a run record to disk and return the written path."""
    target_dir = Path(runs_dir) if runs_dir is not None else DEFAULT_RUNS_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    target_path = _select_available_path(target_dir, build_run_filename(payload))
    target_path.write_text(
        json.dumps(dict(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target_path


def _select_identifier(payload: Mapping[str, Any]) -> str:
    for field in _IDENTIFIER_FIELDS:
        value = payload.get(field)
        if isinstance(value, str) and value.strip():
            return value
    raise ValueError(
        "Run payload must include a non-empty run_id, task_id, or created_at field."
    )


def _slugify(value: str) -> str:
    normalized = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", normalized)
    return slug.strip("-")


def _select_available_path(target_dir: Path, filename: str) -> Path:
    candidate = target_dir / filename
    if not candidate.exists():
        return candidate

    stem = candidate.stem
    suffix = candidate.suffix
    attempt = 2

    while True:
        candidate = target_dir / f"{stem}-{attempt}{suffix}"
        if not candidate.exists():
            return candidate
        attempt += 1
