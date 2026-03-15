"""Write structured episode records into the harness episodes directory."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Mapping

DEFAULT_EPISODES_DIR = Path(__file__).resolve().parent.parent / ".harness" / "episodes"
_IDENTIFIER_FIELDS = ("episode_id", "task_id", "timestamp")


def build_episode_filename(payload: Mapping[str, Any]) -> str:
    """Build a deterministic filename from stable payload fields."""
    identifier = _select_identifier(payload)
    slug = _slugify(identifier)
    if not slug:
        raise ValueError(
            "Episode identifier must contain at least one alphanumeric character."
        )
    return f"episode-{slug}.json"


def write_episode_record(
    payload: Mapping[str, Any],
    episodes_dir: Path | str | None = None,
) -> Path:
    """Serialize an episode record to disk and return the written path."""
    target_dir = Path(episodes_dir) if episodes_dir is not None else DEFAULT_EPISODES_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    target_path = target_dir / build_episode_filename(payload)
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
        "Episode payload must include a non-empty episode_id, task_id, or timestamp field."
    )


def _slugify(value: str) -> str:
    normalized = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", normalized)
    return slug.strip("-")
