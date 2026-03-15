from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from src.episode_log_writer import build_episode_filename, write_episode_record


class BuildEpisodeFilenameTests(unittest.TestCase):
    def test_prefers_episode_id_for_deterministic_name(self) -> None:
        payload = {"episode_id": "Episode 001", "task_id": "task-002"}

        self.assertEqual(build_episode_filename(payload), "episode-episode-001.json")

    def test_falls_back_to_task_id_then_timestamp(self) -> None:
        self.assertEqual(
            build_episode_filename({"task_id": "task-002"}),
            "episode-task-002.json",
        )
        self.assertEqual(
            build_episode_filename({"timestamp": "2026-03-10T12:30:00Z"}),
            "episode-2026-03-10t12-30-00z.json",
        )

    def test_requires_stable_identifier_field(self) -> None:
        with self.assertRaises(ValueError):
            build_episode_filename({"result": "completed"})

    def test_rejects_identifier_without_alphanumeric_content(self) -> None:
        with self.assertRaises(ValueError):
            build_episode_filename({"episode_id": "!!!"})


class WriteEpisodeRecordTests(unittest.TestCase):
    def test_writes_sorted_json_to_target_directory(self) -> None:
        payload = {
            "task_id": "task-002",
            "result": "completed",
            "lesson": "Keep the writer pattern consistent.",
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            written_path = write_episode_record(payload, episodes_dir=temp_dir)

            self.assertEqual(
                written_path,
                Path(temp_dir) / "episode-task-002.json",
            )
            self.assertTrue(written_path.exists())

            written_payload = json.loads(written_path.read_text(encoding="utf-8"))
            self.assertEqual(written_payload, payload)

    def test_creates_missing_episodes_directory(self) -> None:
        payload = {"episode_id": "episode-002"}

        with tempfile.TemporaryDirectory() as temp_dir:
            episodes_dir = Path(temp_dir) / "nested" / "episodes"

            written_path = write_episode_record(payload, episodes_dir=episodes_dir)

            self.assertTrue(episodes_dir.is_dir())
            self.assertEqual(written_path, episodes_dir / "episode-episode-002.json")


if __name__ == "__main__":
    unittest.main()
