from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from src.run_log_writer import build_run_filename, write_run_record


class BuildRunFilenameTests(unittest.TestCase):
    def test_prefers_run_id_for_deterministic_name(self) -> None:
        payload = {"run_id": "Run 001", "task_id": "task-001"}

        self.assertEqual(build_run_filename(payload), "run-run-001.json")

    def test_falls_back_to_task_id_then_created_at(self) -> None:
        self.assertEqual(
            build_run_filename({"task_id": "task-001"}),
            "run-task-001.json",
        )
        self.assertEqual(
            build_run_filename({"created_at": "2026-03-10T12:30:00Z"}),
            "run-2026-03-10t12-30-00z.json",
        )

    def test_requires_stable_identifier_field(self) -> None:
        with self.assertRaises(ValueError):
            build_run_filename({"status": "running"})

    def test_rejects_identifier_without_alphanumeric_content(self) -> None:
        with self.assertRaises(ValueError):
            build_run_filename({"run_id": "!!!"})


class WriteRunRecordTests(unittest.TestCase):
    def test_writes_sorted_json_to_target_directory(self) -> None:
        payload = {
            "task_id": "task-001",
            "status": "running",
            "files_changed": [],
            "tests_run": [],
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            written_path = write_run_record(payload, runs_dir=temp_dir)

            self.assertEqual(written_path, Path(temp_dir) / "run-task-001.json")
            self.assertTrue(written_path.exists())

            written_payload = json.loads(written_path.read_text(encoding="utf-8"))
            self.assertEqual(written_payload, payload)

    def test_creates_missing_runs_directory(self) -> None:
        payload = {"run_id": "task-001"}

        with tempfile.TemporaryDirectory() as temp_dir:
            runs_dir = Path(temp_dir) / "nested" / "runs"

            written_path = write_run_record(payload, runs_dir=runs_dir)

            self.assertTrue(runs_dir.is_dir())
            self.assertEqual(written_path, runs_dir / "run-task-001.json")

    def test_preserves_existing_records_by_allocating_a_suffix(self) -> None:
        first_payload = {"task_id": "task-001", "status": "running"}
        second_payload = {"task_id": "task-001", "status": "passed"}

        with tempfile.TemporaryDirectory() as temp_dir:
            first_path = write_run_record(first_payload, runs_dir=temp_dir)
            second_path = write_run_record(second_payload, runs_dir=temp_dir)

            self.assertEqual(first_path, Path(temp_dir) / "run-task-001.json")
            self.assertEqual(second_path, Path(temp_dir) / "run-task-001-2.json")
            self.assertEqual(
                json.loads(first_path.read_text(encoding="utf-8")),
                first_payload,
            )
            self.assertEqual(
                json.loads(second_path.read_text(encoding="utf-8")),
                second_payload,
            )


if __name__ == "__main__":
    unittest.main()
