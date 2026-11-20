# Git Commands — Week 12 Day 5

Run these commands from the project folder in PowerShell. They create a separate branch and commit this day's work without merging it into another task.

```powershell
git status
git switch -c feature/week-12-day-5
git add README.md app.py analyst_engine.py requirements.txt data/ docs/ demo/ git_commands.md
git commit -m "feat: build week-12-day-5 AI data analyst platform demo"
git push -u origin feature/week-12-day-5
```

If the branch already exists locally, use:
```powershell
git switch feature/week-12-day-5
```

If Git reports that the remote branch already exists, fetch and inspect before pushing:
```powershell
git fetch origin
git status
```

Create a pull request from `feature/week-12-day-5` into the repository's required base branch when instructed by the internship.
