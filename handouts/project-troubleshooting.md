# Reference: Project Troubleshooting

[README](../README.md) · [Assignment 1](../assignments/assignment-1-python-pytest.md)

Use this reference when a checkpoint fails. Run project commands from your
repository root in macOS Terminal or Ubuntu under WSL2. Record the failing
command, actual output, and what you tried before asking for help.

For installation problems, use [Mac setup troubleshooting](../assignments/assignment-0-mac.md#troubleshooting)
or [Windows setup troubleshooting](../assignments/assignment-0-windows.md#troubleshooting).
For authentication, use the [Mac SSH handout](github-ssh-mac.md#troubleshooting)
or [Windows SSH handout](github-ssh-windows.md#troubleshooting).

## The environment or pytest is missing

Check `pwd` and `ls -la` first. If this project's `.venv` exists, activate it with
`source .venv/bin/activate`. Check `python -c "import sys; print(sys.executable)"`;
the path should be inside this repository's `.venv`. If pytest is missing from
that environment, run `python -m pip install -r requirements.txt`.

If the environment does not exist, return to Assignment 1's environment-creation
step. Switching Python versions does not change an existing `.venv`; recreate
it with the selected interpreter when a version change is intended. See
[Python's environment guide](https://docs.python.org/3/library/venv.html).

## Git says there is nothing to commit

Save your files in VS Code and confirm the terminal points to the same project.
`git status` lists changed and untracked files. `git diff` shows unstaged changes
to tracked files; new files appear in `git diff --staged` after you stage them.
Already committed work will not create another commit without new changes.

If an unrelated file is staged, use `git restore --staged -- PATH_TO_FILE` in a
repository with an existing commit, replacing the placeholder with that file.
This keeps its working copy. Before the first commit, use
`git rm --cached -- PATH_TO_FILE` for a newly staged file instead. Inspect status
and the staged diff again. See [Git's restore guide](https://git-scm.com/docs/git-restore)
and [Git's index-removal guide](https://git-scm.com/docs/git-rm).

## Generated files are tracked

From the repository root, inspect what Git tracks:

```bash
git ls-files .venv __pycache__ tests/__pycache__ .pytest_cache
```

This should print nothing. Ensure `.gitignore` contains the assignment's rules.
For each generated directory actually listed, stop tracking it while preserving
local files. For example, run this **only if `.venv` files were listed**:

```bash
git rm -r --cached -- .venv
```

Use the exact listed directory in place of `.venv` for a tracked cache. Review
`git diff --staged`, include the removal and ignore-rule correction in the
relevant issue's commit, and push. This changes future tracking; it does not
erase files from earlier commits. See [Git's ignore rules](https://git-scm.com/docs/gitignore).

## Tests are not discovered or app cannot be imported

Save the files. Confirm the paths are `app.py` and `tests/test_app.py`, with a
function name starting with `test_`. Run `python -m pytest` from the repository
root. Do not run it from inside `tests`, and do not add import-path configuration
to compensate for the wrong directory in this exercise. See
[pytest's invocation guide](https://docs.pytest.org/en/stable/how-to/usage.html).

## Test output does not match the saved file

First check the editor's folder, save the file, and rerun the test. If a very
rapid same-size edit and restore still shows the old expectation, delete only
the generated `tests/__pycache__` folder in VS Code and rerun. Python's timestamp
and size cache checks can miss edits within one timestamp interval. See
[Python's cache validation explanation](https://docs.python.org/3/reference/import.html#cached-bytecode-invalidation).

## Git is waiting for an editor or a pager

With `core.editor` set to `code --wait`, save and close the file's VS Code editor
tab to let Git continue. Closing the terminal is unnecessary. For read-only
output such as a diff displayed in a pager, press `q` to return to the prompt.

## The fresh-clone check needs another attempt

Deactivate the verification environment before returning to your original
working copy. Correct the README there, review the diff, commit with issue 4's
number, and push. Use a new destination such as `python-setup-check-2` for the
next clone. Record the corrected commit link and successful check in issue 4.

## You are on the wrong branch or remote

Run `pwd`, `git status`, `git branch --show-current`, and `git remote -v` before
changing anything. Compare the owner and repository with your assignment URL.
If the remote is wrong, copy the intended SSH URL and run
`git remote set-url origin YOUR_SSH_URL` from the correct repository. If `origin`
is missing, use `git remote add origin YOUR_SSH_URL` instead. Inspect again.

For uncommitted work on the wrong branch, a new branch at the same commit can keep
it with `git switch -c fix/my-task`; inspect status afterward. If commits already
landed on the wrong branch, stop and identify whether they were pushed before
choosing a recovery method. Do not reset shared history to make a screenshot clean.

## A pull refuses to fast-forward

Save your current work appropriately, then inspect `git fetch origin` and
`git log --oneline --graph --all -12`. Local and remote branches may both contain
new commits. Coordinate with the reviewer and follow the project's merge workflow;
a refused fast-forward is not a reason to force-push. The
[recovery lab](../labs/recovery.md) provides a disposable merge-conflict exercise.

## Applying a stash reports conflicts

Run `git status`, inspect the conflicted files, resolve the intended content, and
stage the resolved paths. A failed `stash pop` retains its stash entry. Do not pop
again onto the partially restored work. Review and commit the recovered change,
then inspect `git stash list` before dropping the verified entry. There is no
`git stash --abort`; do not discard working files without checking what was there
before the apply. Practice first in the [stash lab](../labs/stashes.md).
