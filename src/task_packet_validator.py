"""Validate task packet JSON files stored in the harness tasks directory."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DEFAULT_TASKS_DIR = Path(__file__).resolve().parent.parent / ".harness" / "tasks"
REQUIRED_FIELDS = (
    "task_id",
    "title",
    "status",
    "brief",
    "plan",
    "priority",
    "type",
    "created_at",
)


def validate_task_packet(payload: dict[str, Any]) -> dict[str, Any]:
    """Validate a parsed task packet and return it when valid."""
    for field in REQUIRED_FIELDS:
        value = payload.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Task packet must include a non-empty {field} field.")

    if not payload["brief"].endswith(".md"):
        raise ValueError("Task packet brief must point to a Markdown file.")
    if not payload["plan"].endswith(".md"):
        raise ValueError("Task packet plan must point to a Markdown file.")

    return payload


def validate_task_packet_file(task_packet_path: Path | str) -> dict[str, Any]:
    """Load and validate a task packet file from the harness tasks directory."""
    path = Path(task_packet_path)

    if path.suffix != ".json":
        raise ValueError("Task packet path must end with .json.")
    if not _is_harness_tasks_path(path):
        raise ValueError("Task packet path must be inside .harness/tasks.")

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError("Task packet file must contain valid JSON.") from exc

    if not isinstance(payload, dict):
        raise ValueError("Task packet JSON must decode to an object.")

    return validate_task_packet(payload)


def _is_harness_tasks_path(path: Path) -> bool:
    parts = path.parent.parts
    for index, part in enumerate(parts[:-1]):
        if part == ".harness" and parts[index + 1] == "tasks":
            return True
    return False
