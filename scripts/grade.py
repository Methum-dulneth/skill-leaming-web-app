#!/usr/bin/env python3
"""Run every task's pytest suite and write results.json.

Used identically by GitHub Actions and by the app's local grader, so a pass is
a pass whether it ran in CI or on your machine.
"""
import json
import os
import subprocess
import sys
import datetime
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
tasks_dir = root / "tasks"

results = {}
for task in sorted(p for p in tasks_dir.iterdir() if p.is_dir()):
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(task)],
        cwd=root,
        capture_output=True,
        text=True,
    )
    results[task.name] = {"passed": proc.returncode == 0}
    print(f"{task.name}: {'PASS' if proc.returncode == 0 else 'FAIL'}")

sha = os.environ.get("GITHUB_SHA")
if not sha:
    try:
        sha = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True
        ).stdout.strip() or None
    except Exception:
        sha = None

out = {
    "commit": sha,
    "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "results": results,
}
(root / "results.json").write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
