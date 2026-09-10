# Lab: Predict what Git will commit

[Course index](../README.md) · [Git reference](../handouts/git-basics.md)

## Outcome and prerequisites

Compare explicit staging, partial staging, and `git commit -am`. Complete Assignment
1 first and use a new disposable local folder. No remote is needed. If the folder
exists, choose a new name. Run the steps in order.

## 1. Build the starting state

```bash
mkdir -p ~/terminal-practice
cd ~/terminal-practice
mkdir staging-lab
cd staging-lab
git init -b main
printf 'def add(a, b):\n    return a + b\n' > app.py
printf '# Calculator\n' > README.md
python3 -c "from pathlib import Path; p = Path('app.py'); p.write_text(p.read_text() + chr(10) * 12)"
git add app.py README.md
git commit -m "Start staging practice"
printf '\nSupports integer addition.\n' >> README.md
printf 'Try negative inputs.\n' > test-plan.txt
```

## 2. Predict automatic staging

Before running the commit, predict whether `test-plan.txt` will be included:

```bash
git status --short
git commit --dry-run -a
git commit -am "Describe integer addition"
git show --stat HEAD
git status --short
```

Only the tracked README change is committed. Expect `?? test-plan.txt` afterward.
`-a` stages modifications and deletions of tracked files across the repository;
`-m` provides the message. Previously staged new files would also be committed.

Include the new file explicitly:

```bash
git add test-plan.txt
git diff --staged
git commit -m "Record a testing idea"
```

## 3. Stage one chunk at a time

Create two separated additions in the tracked Python file:

```bash
python3 - <<'PYCODE'
from pathlib import Path
p = Path('app.py')
p.write_text('# Integer arithmetic\n' + p.read_text() + '# TODO: add subtraction\n')
PYCODE
git add -p app.py
```

Use `y` for the first chunk and `n` for the second. If Git combines them, try `s`
to split the chunk. Inspect before committing:

```bash
git diff --staged
git diff
git commit -m "Label integer arithmetic"
git diff
```

The staged diff should contain only the first comment; the TODO should remain
unstaged afterward. Do not use `-am` here: it would stage the remaining tracked
edit too, defeating the selection.

## 4. Amend only an unshared commit

Suppose that TODO belongs with the latest local commit after all:

```bash
git add app.py
git diff --staged
git commit --amend --no-edit
git show HEAD
git status --short
```

The latest commit now contains both edits and has a different ID. The working tree
is clean. This repository has no remote; for shared commits, prefer a follow-up
commit instead of replacing published history.

## Independent challenge and evidence

Create a new file and delete a tracked one. Compare `git add -u` with `git add -A`
using `git status --short` and `git diff --staged` before committing. Explain which
command includes the new file. To reset your selection without losing edits, use
`git restore --staged .` from the repository root. Finish with a focused commit.

Summarize when you would use explicit filenames, `add -p`, `add -u`, `add -A`, or
`commit -am`. Save your prediction and observed file list if this lab is assigned.

[Next: Automated tests](../assignments/assignment-3-automation.md)
