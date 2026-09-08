# Assignment 1: Set Up a Python Project with GitHub Issues and pytest

## Purpose

Build a minimal Python project while practicing an issue-by-issue development workflow:

**Plan the work → make changes → verify the result → commit and push → close the issue.**

You will create **four GitHub issues** and complete them in order. Each issue must have at least one commit that references its issue number.

The finished project will contain one Python function, one automated test, and instructions that allow someone to set up the project from a fresh clone.

## Before you begin

Complete [Assignment 0: Environment Setup and Prerequisites](assignment-0-environment-setup.md) first. Use your existing class repository, with Git, Python 3, VS Code, and GitHub SSH access ready. This repository contains a completed example; do your assignment work in your own class repository.

Open a terminal in your repository’s root folder and open the project:

```bash
code .
```

For this exercise, work on your repository’s default branch. Creating branches and pull requests is outside the scope of this handout.

**Windows users:** Run project commands in Ubuntu under WSL2. macOS users run them in Terminal. Both platforms use the same commands below.

---

# Part 1: Plan Your Work in GitHub

## Create four issues

Before changing any project files, create these four issues in your repository.

| Order | Issue title                                         | Work covered                                                          |
| ----- | --------------------------------------------------- | --------------------------------------------------------------------- |
| 1     | Create the repository foundation                    | Add a README and Python ignore rules.                                 |
| 2     | Set up the Python environment and pytest            | Create a virtual environment, install pytest, and document setup.     |
| 3     | Add a Python function and automated test            | Write the function and test; demonstrate passing and failing results. |
| 4     | Complete the documentation and verify a fresh clone | Finish the README and confirm the project works in a new clone.       |

On GitHub, open your repository and select **Issues → New issue**. Choose a blank issue when available. Use the titles above and copy the corresponding issue descriptions from the following parts. Assign the issues to yourself when that option is available. ([GitHub Docs][1])

**GitHub assigns the issue numbers.** The examples below assume your issues are `#1`, `#2`, `#3`, and `#4`. Replace those numbers with the actual numbers in your repository.

For example, your first issue might be `#7`, not `#1`.

## Connect commits to issues using `#`

Include the relevant issue number **inside the quoted commit message**:

```bash
git commit -m "Create the repository foundation #1"
```

After you push the commit, GitHub can connect the issue reference to the issue in that repository. The issue explains the work you intended to do; the commit records the changes you made. ([GitHub Docs][2])

There is an important distinction:

| Commit message wording  | Effect                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ |
| `Add pytest #2`         | References the issue without automatically closing it.                                                       |
| `Add pytest. Closes #2` | References the issue and requests automatic closure when the commit reaches the repository’s default branch. |

A local commit alone does not close an issue on GitHub. Automatic closure depends on the commit reaching the default branch. ([GitHub Docs][3])

**For this handout, use plain references such as `#2` and close each issue manually after verifying its work.**

## Follow the same completion routine for every issue

Before committing, review `git status`. Use `git add` to select the files for that issue, `git commit` to record the changes locally, and `git push` to send the commits to GitHub. ([Git][4])

After pushing, reopen the issue on GitHub. Confirm that it references the correct commit, check off the completed tasks, add a brief comment describing what you verified, and close the issue.

**Complete one issue before moving to the next. Do not put the entire assignment into one commit.**

---

# Part 2: Issue — Create the Repository Foundation

## Issue description

Copy this into the first issue:

```markdown
Prepare the repository for a minimal Python project.

- [ ] README.md identifies the project and explains its purpose.
- [ ] .gitignore excludes the virtual environment and Python/pytest caches.
- [ ] The changes are committed and pushed with this issue's number.
```

## A. Create or update `README.md`

Start with a project title and a short explanation:

```markdown
# Python Project Setup

A minimal Python project for practicing GitHub issues, Git commits,
virtual environments, and automated testing with pytest.
```

Preserve any existing class information in the README.

## B. Create or update `.gitignore`

Add these entries:

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
```

These rules keep matching untracked files out of your commits. They do not remove files that Git is already tracking, which is why you are adding the rules before creating the environment. ([Git][5])

## C. Commit and push

Replace `#1` with this issue’s actual number.

```bash
git status
git add README.md .gitignore
git commit -m "Create the repository foundation #1"
git push
```

**Verify:** Open the repository on GitHub and confirm that the README and `.gitignore` contain your changes. Complete the issue’s checklist, add your verification comment, and close it.

---

# Part 3: Issue — Set Up the Python Environment and pytest

## Issue description

Copy this into the second issue:

```markdown
Create a local Python virtual environment and install pytest.

- [ ] A local .venv environment exists and runs pytest.
- [ ] requirements.txt lists pytest, and README.md documents setup.
- [ ] The setup files are committed and pushed with this issue's number;
      .venv is not committed.
```

## A. Create and activate a virtual environment

A virtual environment gives the project its own Python environment and installed packages. It is local to your computer and should be recreated—not committed to Git. ([Python documentation][6])

Run the commands for your platform **from the repository root**.

### macOS, Linux, or Ubuntu in WSL2

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Activation applies to the current terminal session. Activate the environment again when opening a new terminal. ([Python documentation][6])

Check which Python interpreter you are using:

```bash
python -c "import sys; print(sys.executable)"
```

The displayed path should point inside this project’s `.venv` folder.

## B. Create `requirements.txt`

Add this single line:

```text
pytest
```

Install the dependency from the file:

```bash
python -m pip install -r requirements.txt
```

The `-r` option tells pip to install the requirements listed in the named file. ([Pip][7])

Verify that pytest is available:

```bash
python -m pytest --version
```

You should see a pytest version number. You have not created a test yet; this checks the installation. ([pytest][8])

## C. Document your setup

Add a **Setup** section to `README.md` containing the commands to create and activate the environment and install dependencies.

Record the Python version you used:

```bash
python --version
```

**Commit the setup instructions and dependency list—not the `.venv` folder.**

## D. Commit and push

Replace `#2` with this issue’s actual number.

```bash
git status
git add requirements.txt README.md
git commit -m "Set up pytest and document the Python environment #2"
git push
```

**Verify:** Confirm that pytest reports its version and that GitHub contains `requirements.txt` and the updated README, but not `.venv`. Record your verification in the issue and close it.

---

# Part 4: Issue — Add a Python Function and Automated Test

## Issue description

Copy this into the third issue:

```markdown
Add a small Python function and verify it with pytest.

- [ ] app.py contains an add function, and tests/test_app.py tests it.
- [ ] The test passes, fails when its expected result is intentionally
      changed, and passes again after that change is restored.
- [ ] The final passing code is committed and pushed with this issue's number.
```

## A. Create `app.py`

Add the following code:

```python
def add(a: int, b: int) -> int:
    return a + b
```

## B. Create the test folder and file

Create the folder from the repository root:

```bash
mkdir tests
```

Inside it, create `test_app.py`:

```python
from app import add


def test_add():
    assert add(2, 3) == 5
```

The test imports your function and checks its result. Pytest recognizes test files and functions using naming conventions such as `test_app.py` and `test_add`. An assertion that is false causes the test to fail. ([pytest][8])

## C. Run the test

With the virtual environment active, run this command **from the repository root**, not from inside `tests`:

```bash
python -m pytest
```

Use `python -m pytest` throughout this project. This invocation includes the current directory in Python’s import path, allowing the test to import the root-level `app.py` without extra configuration. ([pytest][9])

For this minimal project, the result should include:

```text
1 passed
```

## D. Prove that the test detects a problem

Temporarily change the assertion to:

```python
assert add(2, 3) == 6
```

Save the file and run the tests again:

```bash
python -m pytest
```

The test should now fail. Read the output and locate the comparison between the actual and expected values.

Restore the expected result to `5`, save the file, and rerun the test. Confirm that it passes again.

**Do not commit the intentionally incorrect expectation.**

In your issue comment, explain briefly why the test failed and what you restored.

## E. Commit and push

Replace `#3` with this issue’s actual number.

```bash
git status
git add app.py tests/test_app.py
git commit -m "Add the addition function and its pytest test #3"
git push
```

**Verify:** Confirm the final test passes and the pushed commit references the correct issue. Complete the checklist and close the issue.

---

# Part 5: Issue — Complete the Documentation and Verify a Fresh Clone

## Issue description

Copy this into the fourth issue:

```markdown
Make the project usable from a fresh clone using only its README.

- [ ] README.md explains the project structure, setup, and test commands.
- [ ] A fresh clone works after creating a new environment and installing
      dependencies; pytest reports one passing test.
- [ ] Documentation changes are committed and pushed with this issue's
      number, and fresh-clone verification is recorded in the issue.
```

## A. Finish the README

Your README must include:

| Section          | Required information                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| Project overview | What this project demonstrates and the Python version you used.                                                    |
| File structure   | The five project files shown below and their purposes.                                                             |
| Setup            | Commands to create and activate `.venv` and install `requirements.txt`, using the shared macOS and Ubuntu/WSL2 commands. |
| Running tests    | `python -m pytest`, where to run it, and the expected `1 passed` result.                                           |
| Git tracking     | A brief explanation of why `.venv` and generated caches are not committed.                                         |

The final required structure is:

```text
your-repository/
├── README.md
├── .gitignore
├── requirements.txt
├── app.py
└── tests/
    └── test_app.py
```

Other existing class files may remain. No application framework, packaging configuration, or CI workflow is required.

## B. Commit and push the documentation

Push the completed README **before** checking the fresh clone so the new clone receives it.

Replace `#4` with this issue’s actual number.

```bash
git status
git add README.md
git commit -m "Complete project setup and testing documentation #4"
git push
```

**Leave this issue open until the fresh-clone check succeeds.**

## C. Verify a fresh clone

Use a terminal with no virtual environment active. Work from a folder **outside** your original repository.

Copy your repository’s clone URL from GitHub. Replace `YOUR_REPOSITORY_URL` below with that URL. Use a destination folder that does not already exist.

```bash
git clone YOUR_REPOSITORY_URL python-setup-check
cd python-setup-check
```

Cloning creates a separate local copy of the repository. ([Git][4])

Now use **only the README in that new clone** to create a new `.venv`, activate it, install dependencies, and run the test.

Do not copy the original `.venv` into the new clone. Virtual environments are intended to be recreated rather than moved between locations. ([Python documentation][6])

Confirm that the test reports:

```text
1 passed
```

Then check:

```bash
git status
```

The working tree should be clean; creating the environment and running tests should not require adding generated files to Git.

If a step is missing or unclear, return to the original repository, correct the README, and make another commit referencing the same issue. Push the correction and repeat the verification with the updated instructions.

## D. Record verification and close the issue

Add a comment using your actual results:

```text
Verified from a fresh clone.

Operating system:
Python version:
Test result:

I created a new virtual environment and installed the dependencies
using the README. The test passed, and git status showed a clean
working tree.
```

Complete the checklist and close the issue.

---

# Completion Check

You are finished when you have **four completed GitHub issues**, **at least four new commits—one or more per issue—and one test that passes from a fresh clone**.

Each issue should show what you planned, which commit completed the work, and how you verified it.

Be ready to explain why `.venv` is not committed, how pytest detects a failed expectation, and the difference between referencing an issue with `#3` and automatically closing it with `Closes #3`.

[1]: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue "Creating an issue - GitHub Docs"
[2]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls "Autolinked references and URLs - GitHub Docs"
[3]: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue "Linking a pull request to an issue - GitHub Docs"
[4]: https://git-scm.com/docs/gittutorial "Git - gittutorial Documentation"
[5]: https://git-scm.com/docs/gitignore "Git - gitignore Documentation"
[6]: https://docs.python.org/3/library/venv.html "venv — Creation of virtual environments — Python documentation"
[7]: https://pip.pypa.io/en/stable/user_guide/ "User Guide - pip documentation"
[8]: https://docs.pytest.org/en/stable/getting-started.html "Get Started - pytest documentation"
[9]: https://docs.pytest.org/en/stable/how-to/usage.html "How to invoke pytest - pytest documentation"
