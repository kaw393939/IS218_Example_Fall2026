# Lab: Recover from common Git mistakes

[Course index](../README.md) · [Git reference](../handouts/git-basics.md)

## Outcome and prerequisites

Practice unstaging, conflict resolution, and reverting shared history. Complete
Assignment 2 first. This lab creates its own repository and a local bare remote
that stands in for GitHub. Nothing is sent to a real server.

Use a new `recovery-lab` folder if it already exists. Stop and inspect unexpected
errors; the merge conflict in step 3 is intentional.

## 1. Build the starting state

```bash
mkdir -p ~/terminal-practice
cd ~/terminal-practice
mkdir recovery-lab
cd recovery-lab
git init --bare remote.git
git init -b main work
cd work
printf 'def add(a, b):\n    return a + b\n' > app.py
printf '# Python workflow practice\n\nCourse calculator.\n' > README.md
git add app.py README.md
git commit -m "Start recovery practice"
git remote add origin ../remote.git
git push -u origin main
```

## 2. Unstage an accidental addition

```bash
printf 'Personal practice notes\n' > notes.txt
git add notes.txt
git diff --staged
git restore --staged notes.txt
git status --short
cat notes.txt
```

Expect `?? notes.txt`; the file still exists. Keep this unrelated file untracked.
This demonstrates why reviewing the staged diff matters.

## 3. Resolve a realistic documentation conflict

Two branches change the same description:

```bash
git switch -c feature/description
printf '# Python workflow practice\n\nCalculator with integer examples.\n' > README.md
git add README.md
git commit -m "Describe integer examples"
git switch main
printf '# Python workflow practice\n\nCalculator with tested arithmetic.\n' > README.md
git add README.md
git commit -m "Describe tested arithmetic"
git merge feature/description
```

Expect a conflict and a nonzero exit from the merge. Run `git status` and open
`README.md` in VS Code. Replace the conflict block with a sentence preserving both
ideas, such as “Calculator with tested arithmetic and integer examples.” Remove
all conflict markers. Then:

```bash
git add README.md
git diff --staged
git commit -m "Combine calculator descriptions"
git push
```

Before resolving, `git merge --abort` can cancel this in-progress merge. If you use
it, retry the merge to complete the exercise. Do not run abort after the merge commit.

## 4. Reverse a bug that was already shared

Introduce an intentional implementation mistake and publish it to the local remote:

```bash
printf 'def add(a, b):\n    return a - b\n' > app.py
git add app.py
git commit -m "Introduce deliberate practice bug"
git push
git revert --no-edit HEAD
git push
git log --oneline -3
python3 -c 'from app import add; assert add(2, 3) == 5; print("Addition restored")'
```

Expect a new revert commit, the bug commit still in history, and `Addition restored`.
`HEAD` is appropriate here only because the deliberate bug is the latest commit.
For real work, inspect the history and identify the intended non-merge commit.

## Independent challenge and evidence

Modify `app.py` without staging it, inspect `git diff`, then use
`git restore -- app.py` only if you intend to discard that edit. Explain why this
is different from `restore --staged` and `revert`. Git cannot normally recover edits
it never recorded. Finish with `git status --short`: only `notes.txt` should remain
untracked. Save the merge/revert commit IDs and your explanation if assigned.

For wrong-folder, authentication, remote, or tracked-cache problems, use
[troubleshooting](../handouts/project-troubleshooting.md).

[Next: Staging and commit shortcuts](staging-and-commits.md)
