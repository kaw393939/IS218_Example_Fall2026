# Lab: Manage unfinished Python work with stashes

[Course index](../README.md) · [Git reference](../handouts/git-basics.md)

## Outcome and prerequisites

Save two tasks, inspect the correct stash, restore it, and clean up deliberately.
Complete Assignment 1 and configure your Git identity first. This is a disposable
local repository with no remote; its commits and stashes are practice only.
Commands are sequential unless labeled as a reference. Use a new folder name if
`stash-lab` exists. Do not run later commands after an unexpected failure.

## 1. Build the starting state

```bash
mkdir -p ~/terminal-practice
cd ~/terminal-practice
mkdir stash-lab
cd stash-lab
git init -b main
printf 'def add(a, b):\n    return a + b\n' > app.py
git add app.py
git commit -m "Start stash practice"
printf '\n# TODO: document integer examples\n' >> app.py
printf 'Try zero and negative numbers.\n' > test-ideas.txt
git status --short
```

Expect modified `app.py` and untracked `test-ideas.txt`.

## 2. Compare tracked-only and untracked behavior

```bash
git stash push -m "Document integer examples"
git status --short
```

The tracked edit is saved, but `test-ideas.txt` remains untracked. Now save it too:

```bash
git stash push -u -m "New test ideas"
git status --short
git stash list
git stash show -p -u 'stash@{0}'
git stash show -p 'stash@{1}'
```

Status should be empty. The newest entry contains the new file; the older one
contains the comment in `app.py`. `-u` includes untracked files, not ignored files.
Stashes belong to this local repository and ordinary pushes do not upload them.

## 3. Restore without deleting the saved entry

```bash
git stash apply 'stash@{1}'
git diff
git stash list
git add app.py
git commit -m "Document integer examples"
git stash drop 'stash@{1}'
```

`apply` keeps the entry. Drop it only after verifying and committing the restored
work. Now restore the remaining entry:

```bash
git stash pop 'stash@{0}'
cat test-ideas.txt
git add test-ideas.txt
git commit -m "Record test ideas"
git stash list
git status --short
```

Both final commands should print nothing. `pop` removes the entry only on success.
If it conflicts, the entry remains. Resolve and inspect the files; do not blindly
apply it a second time. Stash numbers change after entries are added or removed.

## 4. Recover on a branch at the original base

```bash
printf '\n# TODO: add subtraction later\n' >> app.py
git stash push -m "Subtraction plan"
git stash branch recover/subtraction 'stash@{0}'
git branch --show-current
git diff
git stash list
```

Expect branch `recover/subtraction`, the restored comment, and an empty stash list.
`stash branch` starts at the saved base and drops the entry after successful restore.
Commit the restored plan before finishing:

```bash
git add app.py
git commit -m "Record subtraction plan"
```

## Independent challenge and evidence

Create one staged change and one unstaged change. Save them, then restore with
`git stash apply --index` and inspect `git diff` and `git diff --staged`. Explain
how this differs from ordinary `apply`. Commit the restored work and drop the
verified entry. Keep status output and a short explanation if this lab is assigned.

`git stash clear` removes all entries; it is a reference command, not a lab step.
There is no simple undo for clearing or dropping stashes.

[Next: Recovery lab](recovery.md)
