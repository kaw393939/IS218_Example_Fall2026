# Assignment 2: Collaborate through a pull request

[Course index](../README.md) · [Previous: Assignment 1](assignment-1-python-pytest.md)

## Outcome and prerequisites

Extend your Assignment 1 Python project with a `subtract` function. Use an issue,
a feature branch, tests, a review, and a pull request instead of committing directly
to the default branch. Finish Assignment 1 first. The commands assume your default
branch is `main`; substitute its actual name if different.

## 1. Define the change

Create an issue titled `Add subtraction with tests`. Specify what the function
should return and at least two input/result examples. Include these criteria:

- [ ] `subtract(a, b)` returns the first integer minus the second.
- [ ] Two new tests cover distinct cases, including one you explain independently.
- [ ] Existing tests still pass.
- [ ] A reviewed pull request links this issue and includes test evidence.

Copy its actual number; `ISSUE-NUMBER` below is a placeholder.

## 2. Start from current main

From your Assignment 1 repository, activate `.venv` and verify a clean working tree:

```bash
git status
git switch main
git pull --ff-only origin main
git switch -c feature/subtract
source .venv/bin/activate
```

If your work is unfinished, commit it appropriately before switching. Do not
mix it into this feature. If the branch already exists, choose a new name.

## 3. Implement and test

In VS Code, add `subtract` to `app.py` and two tests to `tests/test_app.py`.
Write the expected results before running the implementation. Run:

```bash
python -m pytest
git diff
git add app.py tests/test_app.py
git diff --staged
git commit -m "Add subtraction and tests #ISSUE-NUMBER"
git push -u origin feature/subtract
```

Replace the issue placeholder in the commit message. Expect at least four passing
tests if Assignment 1 ended with two. Record the actual result.

## 4. Open and review the pull request

On GitHub, open a pull request with **base** `main` and **compare**
`feature/subtract`. Describe the problem, resulting behavior, and tests. Include
`Refs #ISSUE-NUMBER` with the real number. Close the issue manually after verification.

Ask a classmate or the instructor to review. A reviewer should inspect the diff,
check the two test cases, and leave one specific observation or actionable suggestion.
If no reviewer is available, use the instructor-approved self-review alternative:
leave a comment explaining one potential defect you checked and how you checked it.
Do not claim an independent review occurred when it did not.

Address feedback on the **same feature branch**. Retest, commit the follow-up with
the issue number, and run `git push`; the pull request updates automatically.

## 5. Merge and verify

Once the review is addressed and tests pass, merge using the repository's allowed
GitHub merge method. If blocked by permissions or branch rules, ask the maintainer
rather than bypassing them. Then locally:

```bash
git switch main
git pull --ff-only origin main
python -m pytest
git status
```

Expect the new function, passing tests, and a clean working tree. Record the pull
request URL and this verification in the issue, then close it. Local branch deletion
is optional: `git branch -d feature/subtract` works when Git recognizes it as merged.
After a squash merge it may refuse; keep the branch until you understand why.

## Completion evidence

Submit the repository, issue, and merged pull request links as directed. Include
actual test results and review evidence. Follow the [access checklist](../handouts/submission.md).

Next: [stash practice](../labs/stashes.md), [recovery practice](../labs/recovery.md),
and [staging shortcuts](../labs/staging-and-commits.md), then
[Assignment 3: Automated tests](assignment-3-automation.md).
