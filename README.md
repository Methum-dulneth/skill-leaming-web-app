# Python — SkillForge learning repo

Your real, graded coding work. Each folder under `tasks/` is one task:

- `solution.py` — edit this to solve the task
- `test_solution.py` — the tests that grade it (don't edit)

## How grading works

1. Solve a task in its `solution.py`.
2. Commit and push.
3. GitHub Actions runs `scripts/grade.py` (all tests) and commits `results.json`.
4. In the SkillForge app, click **Sync from GitHub** — passing tasks award XP,
   tied to the commit that passed.

## Grade locally (no GitHub needed)

```bash
pip install -r requirements.txt
python scripts/grade.py
```

Then click **Grade locally** in the app.
