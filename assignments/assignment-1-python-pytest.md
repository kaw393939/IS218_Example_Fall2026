# Assignment 1: Connect GitHub Issues to Your Commits

[README](../README.md) · [Troubleshooting](../handouts/project-troubleshooting.md)

**Create an issue → make and test the change → commit with its issue number → push → verify and close the issue.**

Practice this workflow four times using a small Python project. Your finished
repository must have **four closed issues, at least one linked commit per issue,
and at least two passing tests**. Do not put all the work into one commit.

## Before starting

Complete [Assignment 0 for Windows](assignment-0-windows.md) or
[Assignment 0 for Mac](assignment-0-mac.md). Use your own assigned repository.
Edit in VS Code; run commands from its root in macOS Terminal or Ubuntu under WSL2:

```bash
cd ~/projects/class-project
code .
```

Substitute your folder path if different. Use the default branch for this
introductory exercise; branches and pull requests come next. If your starter
already completes these tasks, confirm the intended starting point with your instructor.

## 1. Create the four issues FIRST

On **your repository's GitHub page**, select **Issues → New issue**. Create all
four issues before changing files. Use these titles and copy the checklists
from the matching sections below into their descriptions. Assign them to yourself
if available. [GitHub's issue instructions](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue).

| Work order | Issue title | Your actual issue number |
| --- | --- | --- |
| 1 | Create the repository foundation | #___ |
| 2 | Set up the Python environment and pytest | #___ |
| 3 | Add the function and tests | #___ |
| 4 | Document and verify the handoff | #___ |

**GitHub assigns the numbers. Replace `#1`, `#2`, `#3`, and `#4` in every example
with your actual numbers.** Work order 1 might be issue `#7`.

## 2. Connect EACH commit to its issue

Put the issue number **inside the quoted commit message**. For example, if your
foundation issue is `#7`, its commit message is:

```text
Create the repository foundation #7
```

The commit records your changes; the issue records the task and verification.
After pushing, GitHub turns the issue reference into a link.
[GitHub's reference guide](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls).

For **every issue**:

1. Make and verify only that issue's changes.
2. Review `git diff`, stage its files, and review `git diff --staged`.
3. Commit with its issue number, then push.
4. Open the pushed commit on GitHub. Click its `#number` and confirm it opens the correct issue.
5. Paste the **commit URL** and your verification result into that issue, check its checklist, and close it.

Use this short comment format with your actual results:

```text
Commit: [paste the GitHub commit URL]
Verified: [command/check and actual result]
Reviewed: [what you checked in the staged changes]
```

**Use plain `#number` references and close issues manually after verification.**
`Closes #number` can automatically close an issue when the commit reaches the
default branch, so do not use it in this exercise.
[GitHub's closing-keyword guide](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).

`git diff` omits new untracked files; they appear in the staged diff after
`git add`. If you edit again, stage again. Press `q` to leave a diff pager.
[Git's diff guide](https://git-scm.com/docs/git-diff).

## Issue 1 — Create the repository foundation

**Paste into this issue:**

```markdown
- [ ] README.md explains the project; existing class information is preserved.
- [ ] .gitignore excludes the environment and generated caches.
- [ ] My pushed commit references this issue; its URL and verification are recorded here.
```

Create or update `README.md` with a title and short project description.
Add these entries to `.gitignore`:

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
```

**Review, commit, and push. Replace `#1` with your foundation issue number:**

```bash
git status
git diff
git add README.md .gitignore
git diff --staged
git commit -m "Create the repository foundation #1"
git push -u origin HEAD
```

The first push sets the tracking branch; later pushes use `git push`.
Verify the files on GitHub, check the commit's issue link, add the commit URL and
verification comment to the issue, and close it **before starting issue 2**.

## Issue 2 — Set up the Python environment and pytest

**Paste into this issue:**

```markdown
- [ ] A local .venv has pytest installed; requirements.txt contains only pytest.
- [ ] README.md records the Python version and setup commands; .venv is not tracked.
- [ ] My pushed commit references this issue; its URL and verification are recorded here.
```

Check `python3 --version` matches Assignment 0's Python 3.12 selection, unless
your instructor specified another version. Create the local environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -c "import sys; print(sys.executable)"
```

The interpreter path must be inside this project's `.venv`. In VS Code, use
**Python: Select Interpreter** to select `.venv/bin/python`.

Create `requirements.txt` containing:

```text
pytest
```

Install and verify:

```bash
python -m pip install -r requirements.txt
python -m pytest --version
python --version
git check-ignore .venv/
git ls-files .venv
```

Expect version output, then `.venv/` from `check-ignore`, and nothing from
`ls-files`. Record your Python version and setup commands in the README.
For a later terminal session, return to this folder and run
`source .venv/bin/activate`; do not recreate the environment.
[Python's environment guide](https://docs.python.org/3/library/venv.html).

**Review, commit, and push. Replace `#2` with your environment issue number:**

```bash
git status
git diff
git add requirements.txt README.md
git diff --staged
git commit -m "Set up pytest and document the environment #2"
git push
```

Check the commit's issue link. Add its URL, pytest version, and tracking-check
results to the issue. Close it **before starting issue 3**.

## Issue 3 — Add the function and tests

**Paste into this issue:**

```markdown
- [ ] app.py contains add; tests/test_app.py contains the supplied test.
- [ ] I verified pass → intentional failure → restored pass.
- [ ] I designed another test, explained its purpose, and at least two tests pass.
- [ ] My pushed commit references this issue; its URL and verification are recorded here.
```

Create `app.py`:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Run `mkdir -p tests`, then create `tests/test_app.py` in VS Code:

```python
from app import add


def test_add():
    assert add(2, 3) == 5
```

With `.venv` active, run from the repository root:

```bash
python -m pytest
```

Expect `1 passed`. Temporarily change the expected `5` to `6`, save, and run
again: it must fail. Restore `5`, save, and confirm it passes. Do not commit
the intentional failure. Use `python -m pytest` so `app.py` can be imported
from the root. [pytest's invocation guide](https://docs.pytest.org/en/stable/how-to/usage.html).

**Design one additional test yourself.** Before writing it, comment on this
issue with your chosen integer inputs, expected result, and why the case adds
coverage. Add a distinct `test_` function, then run the tests. Expect **at least
`2 passed`**. Explain the intentional failure and one limitation of your tests
in your verification comment.

**Review, commit, and push. Replace `#3` with your testing issue number:**

```bash
git status
git diff
git add app.py tests/test_app.py
git diff --staged
git commit -m "Add the function and tests #3"
git push
```

Check the commit's issue link. Add its URL and your actual test results to the
issue, finish the checklist, and close it **before starting issue 4**.

## Issue 4 — Document and verify the handoff

**Paste into this issue:**

```markdown
- [ ] README.md describes the files, Python version, setup, reactivation, tests, and ignored files.
- [ ] My fresh clone passes at least two tests and has a clean working tree with no tracked caches.
- [ ] A classmate followed the README; feedback and successful final verification are recorded.
- [ ] My pushed documentation commit references this issue; its URL is recorded here.
```

Finish the README using **your repository URL**, tested Python version, and
actual passing-test count. Describe `README.md`, `.gitignore`, `requirements.txt`,
`app.py`, and `tests/test_app.py`. Keep existing class files. No framework,
packaging configuration, or CI is required.

**Review and push the README before verification. Replace `#4` with your handoff issue number:**

```bash
git status
git diff
git add README.md
git diff --staged
git commit -m "Document setup and testing #4"
git push
```

Check the commit's issue link and add its URL to the issue. **Keep this issue open.**

### Verify a fresh clone

Run `deactivate` if an environment is active. Replace the URL below with your
own SSH clone URL; use a new destination folder:

```bash
cd ~/projects
git clone YOUR_REPOSITORY_URL python-setup-check
cd python-setup-check
```

Follow **only that clone's README** to create a new environment, install
requirements, and run all tests. Expect at least two passing tests, then check:

```bash
git status
git ls-files .venv __pycache__ tests/__pycache__ .pytest_cache
```

Expect a clean working tree and no tracked-file output. Record the OS, Python
version, actual test count, and Git checks in **this issue**.

### Have a classmate verify the handoff

Give a classmate the repository URL and commit ID (`git rev-parse --short HEAD`).
They must follow the README in a fresh clone and record:

```text
Reviewer and commit reviewed:
Method: independent clone / supervised walkthrough
OS and Python version:
Test count and Git check results:
Unclear instructions, corrections, and final outcome:
```

For private repositories, use instructor-approved access or a classmate-directed
walkthrough in a fresh clone on your machine. Record the method; a walkthrough
does not verify another machine. Keep credentials private. If they cannot
comment in the issue, paste their feedback with permission. Ask the instructor
to coordinate a reviewer if needed.

Fix unclear instructions in your original working copy. Review, commit with
**the same issue number**, and push corrections; record each commit URL and have
the reviewer repeat affected steps. Close issue 4 only after both checks succeed.
Run `deactivate` before leaving the verification copy and returning to your
original project folder.

## Submit the issue-to-commit record

Submit your repository URL and this completed table through the course submission
location. **Every issue must show its linked commit(s) and verification before closure.**

| Issue URL | GitHub commit URL(s) | Verification result |
| --- | --- | --- |
| Foundation | | |
| Environment | | |
| Function and tests | | |
| Documentation and handoff | | |

Four issues and at least four coherent commits are required for practice.
Commit count alone does not demonstrate good work.

| Assessment | Points |
| --- | ---: |
| Issues, linked commits, and verification comments | 20 |
| Reviewed, focused commits with no generated files | 20 |
| Two or more passing tests, independent rationale, and failure explanation | 25 |
| Accurate README and fresh-clone evidence | 20 |
| Classmate handoff and addressed feedback | 15 |
