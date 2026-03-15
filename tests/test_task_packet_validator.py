from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from src.task_packet_validator import validate_task_packet, validate_task_packet_file


class ValidateTaskPacketTests(unittest.TestCase):
    def test_accepts_minimal_valid_task_packet(self) -> None:
        payload = {
            "task_id": "task-003",
            "title": "Implement validator",
            "status": "ready",
            "brief": "docs/briefs/brief-003-task-packet-validator.md",
            "plan": "docs/exec-plans/plan-003-task-packet-validator.md",
            "priority": "low",
            "type": "feature",
            "created_at": "2026-03-10",
        }

        self.assertEqual(validate_task_packet(payload), payload)

    def test_rejects_missing_required_field(self) -> None:
        payload = {
            "task_id": "task-003",
            "title": "Implement validator",
            "status": "ready",
            "brief": "docs/briefs/brief-003-task-packet-validator.md",
            "plan": "docs/exec-plans/plan-003-task-packet-validator.md",
            "priority": "low",
            "type": "feature",
        }

        with self.assertRaises(ValueError):
            validate_task_packet(payload)

    def test_rejects_non_markdown_brief_or_plan(self) -> None:
        payload = {
            "task_id": "task-003",
            "title": "Implement validator",
            "status": "ready",
            "brief": "docs/briefs/brief-003-task-packet-validator.json",
            "plan": "docs/exec-plans/plan-003-task-packet-validator.md",
            "priority": "low",
            "type": "feature",
            "created_at": "2026-03-10",
        }

        with self.assertRaises(ValueError):
            validate_task_packet(payload)


class ValidateTaskPacketFileTests(unittest.TestCase):
    def test_loads_and_validates_task_packet_file(self) -> None:
        payload = {
            "task_id": "task-003",
            "title": "Implement minimal task packet validator",
            "status": "ready",
            "brief": "docs/briefs/brief-003-task-packet-validator.md",
            "plan": "docs/exec-plans/plan-003-task-packet-validator.md",
            "priority": "low",
            "type": "feature",
            "created_at": "2026-03-10",
        }

        # Create a valid directory structure for the test
        with tempfile.TemporaryDirectory() as temp_dir:
            tasks_dir = Path(temp_dir) / ".harness" / "tasks"
            tasks_dir.mkdir(parents=True, exist_ok=True)
            task_path = tasks_dir / "task-003.json"
            task_path.write_text(json.dumps(payload), encoding="utf-8")

            result = validate_task_packet_file(task_path)
            self.assertEqual(result, payload)

    def test_rejects_non_json_task_packet_path(self) -> None:
        with self.assertRaises(ValueError):
            validate_task_packet_file(".harness/tasks/task-003.txt")

    def test_rejects_task_packet_outside_harness_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            packet_path = Path(temp_dir) / "task-003.json"
            packet_path.write_text("{}", encoding="utf-8")

            with self.assertRaises(ValueError):
                validate_task_packet_file(packet_path)

    def test_rejects_paths_with_harness_segment_but_no_tasks_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            harness_dir = Path(temp_dir) / ".harness"
            harness_dir.mkdir(parents=True, exist_ok=True)
            packet_path = harness_dir / "task-003.json"
            packet_path.write_text("{}", encoding="utf-8")

            with self.assertRaises(ValueError):
                validate_task_packet_file(packet_path)

    def test_rejects_invalid_json(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            tasks_dir = Path(temp_dir) / ".harness" / "tasks"
            tasks_dir.mkdir(parents=True, exist_ok=True)
            packet_path = tasks_dir / "task-003.json"
            packet_path.write_text("{", encoding="utf-8")

            with self.assertRaises(ValueError):
                validate_task_packet_file(packet_path)

    def test_rejects_non_object_json(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            tasks_dir = Path(temp_dir) / ".harness" / "tasks"
            tasks_dir.mkdir(parents=True, exist_ok=True)
            packet_path = tasks_dir / "task-003.json"
            packet_path.write_text(json.dumps(["task-003"]), encoding="utf-8")

            with self.assertRaises(ValueError):
                validate_task_packet_file(packet_path)


if __name__ == "__main__":
    unittest.main()
