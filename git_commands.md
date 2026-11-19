# Git Commands — Week 12 Day 4

Use these commands in Windows PowerShell. The folder and branch are separate for this internship day.

```powershell
cd "D:\Cynaris Internship"
mkdir "week-12-day-4-final-documentation-demo"
cd "week-12-day-4-final-documentation-demo"
```

Copy the contents of this prepared folder into the folder above, then run:

```powershell
git init
git checkout -b feature/week-12-day-4
git status
git add README.md docs demo git_commands.md
git status
git commit -m "docs: complete week-12-day-4 final documentation and demo preparation"
git remote add origin https://github.com/Aishwaryanaik123/sql-fundamentals.git
git push -u origin feature/week-12-day-4
```

If `origin` is already configured, do not add it again. Check it with:

```powershell
git remote -v
```

If the remote already exists, skip `git remote add origin ...` and run the push command.

Check the final commit and branch:

```powershell
git branch
git log -1 --oneline
git status
```

Keep this task on `feature/week-12-day-4`; do not merge it into `master` unless your mentor specifically instructs you to do so.
