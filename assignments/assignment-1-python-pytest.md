# Assignment 1: Set Up a Python Project with GitHub Issues and pytest

[Back to README](../README.md)

## Purpose

Use your existing Python and Git knowledge to deliver a small project another
developer can understand, review, and run. The programming is deliberately small
so you can concentrate on the professional workflow:

**Define the task → implement → test → review the diff → commit and push → verify and close.**

Create **four GitHub issues** and complete them in order. Each needs at least
one coherent commit referencing its issue number. Four issues and four or more
commits are practice constraints for this assignment, not a universal measure
of productivity. Additional commits should reflect meaningful corrections.

The finished project contains one function, **at least two passing tests**,
and a README verified by you and a classmate. You will explain your test choice,
review what each commit contains, and record evidence that the project works.

## Before you begin

Complete **[Assignment 0 for Windows](assignment-0-windows.md)** or
**[Assignment 0 for Mac](assignment-0-mac.md)** first. Both paths join here for
Assignment 1. Use your own class repository from Assignment 0, with Git, Python 3,
VS Code, and GitHub SSH access ready. This instructor repository contains the supplied
baseline example; do your assignment work in your own assigned repository.
If your assigned starter already completes an issue's acceptance criteria,
confirm the intended starting point with your instructor. Do not manufacture
meaningless changes just to reach a commit count.

Open a terminal and return to the repository you cloned in Assignment 0. If you
chose a different folder name, substitute that path:

```bash
cd ~/projects/class-project
pwd
git status
code .
```

The **repository root** is this folder, which contains the hidden `.git`
directory. Run all project commands here. Open VS Code's **Terminal → New
Terminal** for a terminal in the project window.

Create and edit project files in VS Code. Use its Explorer **New File** action
when a new file is needed. Save each file before running commands.
Copy only the contents of a code block, not its backticks or language label.
Filenames must match exactly, including `.gitignore`'s leading dot; avoid extra
extensions such as `.txt`. Preserve Python indentation as shown.

For this assignment, work on the repository's default branch. This is an
introductory simplification that lets you practice issues, diffs, and verification
first. Branches and pull requests are the next workflow step in the course.

**Windows users:** Run project commands in Ubuntu under WSL2. macOS users run them in Terminal. Both platforms use the same commands below.

For failed checks, use the [project troubleshooting reference](../handouts/project-troubleshooting.md).

---

# Part 1: Plan Your Work in GitHub

## Create four issues

Before changing any project files, create these four issues in your repository.

| Order | Issue title                                         | Work covered                                                          |
| ----- | --------------------------------------------------- | --------------------------------------------------------------------- |
| 1     | Create the repository foundation                    | Add a README and Python ignore rules.                                 |
| 2     | Set up the Python environment and pytest            | Create a virtual environment, install pytest, and document setup.     |
| 3     | Add a Python function and automated test            | Write the function, verify a failure, and design an additional test. |
| 4     | Complete documentation and verify the handoff | Finish the README; verify a fresh clone and a classmate handoff.       |

On GitHub, open your repository and select **Issues → New issue**. Choose a blank issue when available. Use the titles above and copy the corresponding issue descriptions from the following parts. Assign the issues to yourself when that option is available. ([GitHub Docs][1])

If **Issues** is missing, check that you opened your assigned repository. Ask
the instructor or repository owner to enable issues if needed. Paste only the
issue-description checklist into each issue; the following lettered sections
are the instructions for carrying out that work.

**GitHub assigns the issue numbers.** The examples below assume your issues are `#1`, `#2`, `#3`, and `#4`. Replace those numbers with the actual numbers in your repository.

For example, your first issue might be `#7`, not `#1`.

## Connect commits to issues using `#`

Include the relevant issue number **inside the quoted commit message**. This is
a syntax example; run the actual commit commands in each issue's completion
section after saving and staging its files:

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

Before each commit, check `git status` and `git diff`, stage only that issue's
files, then read `git diff --staged`. The commit sections below include these
commands. Run them one at a time and inspect the output before committing.

- `git diff` shows unstaged changes to tracked files. New untracked files do not
  appear there; inspect them in VS Code and in the staged diff after `git add`.
- `git diff --staged` shows the proposed commit, including newly staged files.
  Check correctness, filenames, unrelated changes, and generated files.
- If you edit a file after staging, review it and stage it again before committing.
  If Git opens a pager, press `q` to return to the terminal.

See [Git's diff documentation](https://git-scm.com/docs/git-diff).

After pushing, inspect the commit on GitHub and record a short issue comment:

```text
Commit:
What changed and why:
Verification command or check:
Actual result:
What I checked in the staged diff:
```

Use your actual observations; “it works” alone is insufficient evidence. Check
all acceptance criteria before closing the issue. Issue 4 also requires a
classmate's verification record. Complete each issue before starting the next.

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
git diff
git add README.md .gitignore
git diff --staged
git commit -m "Create the repository foundation #1"
git push -u origin HEAD
```

This first push sets the upstream tracking branch, including when you cloned an
empty repository. `HEAD` refers to your current branch here, and `origin` is
the remote created by cloning. Later pushes can use `git push`. See
[Git's push documentation](https://git-scm.com/docs/git-push).

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

From the repository root, check `python3 --version`. Use the Python 3.12 version
selected in Assignment 0, unless your instructor specified another version.
Then run these shared commands.

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

The displayed path should point inside this project's `.venv` folder.

**When returning in a new terminal after this environment has been created,**
resume with these commands (substitute your folder name if different):

```bash
cd ~/projects/class-project
source .venv/bin/activate
python -c "import sys; print(sys.executable)"
git status
```

Reactivation uses the existing environment; you do not need to clone or create
it again. Continue with your next unfinished issue.

In VS Code, open the Command Palette (**View → Command Palette**), choose
**Python: Select Interpreter**, and select `.venv/bin/python` in this repository.
If it is missing from the list, use **Enter interpreter path** to choose it.
The Microsoft Python extension from Assignment 0 supplies this command. See
[VS Code's environment guide](https://code.visualstudio.com/docs/python/environments).
The terminal's activation and the editor's interpreter selection should point
to the same environment.

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

Check that Git ignores your environment:

```bash
git check-ignore .venv/
git ls-files .venv
```

The first command should print `.venv/`; the second should print nothing. For
unexpected output, use the [tracking recovery instructions](../handouts/project-troubleshooting.md#generated-files-are-tracked).

Commit the setup instructions and dependency list, with `.venv` excluded.

## D. Commit and push

Replace `#2` with this issue’s actual number.

```bash
git status
git diff
git add requirements.txt README.md
git diff --staged
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
- [ ] I designed at least one additional test and explained what it checks
      and why it adds coverage beyond the supplied example.
- [ ] At least two tests pass, and the reviewed code is committed and pushed
      with this issue's number.
```

## A. Create `app.py`

Add the following code:

```python
def add(a: int, b: int) -> int:
    return a + b
```

`app.py` defines a function; running it directly produces no output. The test
below calls that function and checks its return value.

## B. Create the test folder and file

Create the folder from the repository root:

```bash
mkdir -p tests
```

Create `tests/test_app.py` in VS Code while keeping your terminal at the
repository root. Paste this code into that file:

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

At this stage, with only the supplied test, the result should include:

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

If output seems to reflect an older saved version, use the
[test troubleshooting reference](../handouts/project-troubleshooting.md#test-output-does-not-match-the-saved-file).

**Do not commit the intentionally incorrect expectation.**

In your issue comment, explain briefly why the test failed and what you restored.

## E. Design an additional test

Add at least one new `test_` function in `tests/test_app.py`. Choose a case that
checks a behavior the supplied example does not establish. Use the integer
inputs described by the function signature and calculate the expected result
independently. A renamed copy of the supplied test is not sufficient.

Before writing the test, add a short comment to issue 3 explaining the behavior,
chosen inputs, expected result, and why the test adds useful coverage. Then
implement it and run `python -m pytest`. With exactly one additional test, expect
`2 passed`; with more tests, record the actual count. All tests must pass.

In your verification comment, explain what the intentional failure demonstrated
and one limitation of your tests. Passing examples do not prove every possible
input is correct. The additional test is intentionally not supplied here.

## F. Review, commit, and push

Replace `#3` with this issue’s actual number.

```bash
git status
git diff
git add app.py tests/test_app.py
git diff --staged
git commit -m "Add the function and reviewed pytest tests #3"
git push
```

**Verify:** Confirm at least two tests pass, your test rationale is recorded, and the pushed commit references the correct issue. Complete the checklist and close the issue.

---

# Part 5: Issue — Complete Documentation and Verify the Handoff

## Issue description

Copy this into the fourth issue:

```markdown
Make the project usable by another developer using only its README.

- [ ] README.md explains the project structure, setup, and test commands.
- [ ] A fresh clone works after creating a new environment and installing
      dependencies; pytest reports at least two passing tests.
- [ ] A classmate followed the README and recorded their verification
      method, result, and any unclear instructions.
- [ ] Feedback is addressed, the final handoff succeeds, and documentation
      corrections are reviewed, committed, and pushed with this issue's number.
```

## A. Finish the README

Your README must include:

| Section          | Required information                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| Project overview | What this project demonstrates and the Python version you used.                                                    |
| File structure   | The five project files shown below and their purposes.                                                             |
| Setup            | Commands to create and activate `.venv` and install `requirements.txt`, using the shared macOS and Ubuntu/WSL2 commands. |
| Running tests    | `python -m pytest`, where to run it, and the expected passing count (at least two tests).                                           |
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

Use your own repository URL and tested Python version in the README. If you
use the instructor README as a reference, adapt its example-clone instructions
to your repository. Include the reactivation commands for a returning session.

Other existing class files may remain. No application framework, packaging configuration, or CI workflow is required.

## B. Commit and push the documentation

Push the completed README **before** checking the fresh clone so the new clone receives it.

Replace `#4` with this issue’s actual number.

```bash
git status
git diff
git add README.md
git diff --staged
git commit -m "Complete project setup and testing documentation #4"
git push
```

**Leave this issue open until your fresh-clone check and the classmate handoff succeed.**

## C. Verify a fresh clone

Run `deactivate` if your virtual environment is active, then move outside your
original repository. If you opened a new terminal with no environment active,
skip `deactivate`.

Copy your own repository's **SSH** clone URL from GitHub. Replace
`YOUR_REPOSITORY_URL` below with it. Use a destination folder that does not
already exist; for a repeat attempt choose `python-setup-check-2` and update
both the clone destination and following `cd` command.

```bash
cd ~/projects
git clone YOUR_REPOSITORY_URL python-setup-check
cd python-setup-check
```

Cloning creates a separate local copy of the repository. ([Git][4])

Now use **only the README in that new clone** to create a new `.venv`, activate it, install dependencies, and run the test.

Do not copy the original `.venv` into the new clone. Virtual environments are intended to be recreated rather than moved between locations. ([Python documentation][6])

Confirm all tests pass: `2 passed` if you added one test, or the higher count
recorded in your README if you added more.

Then check:

```bash
git status
```

The working tree should be clean; creating the environment and running tests
should not require adding generated files to Git. A clean status alone does not
prove the original project excluded them. Check the tracked file list too:

```bash
git ls-files .venv __pycache__ tests/__pycache__ .pytest_cache
```

This command should print nothing. For listed files, use the
[tracking recovery instructions](../handouts/project-troubleshooting.md#generated-files-are-tracked)
in the original repository before repeating the check.

If a step is missing or unclear, return to the original repository, correct the README, and make another commit referencing the same issue. Push the correction and repeat the verification with the updated instructions.

## D. Record your verification

Add a comment using your actual results:

```text
Verified from a fresh clone.

Operating system:
Python version:
Test result:

I created a new virtual environment and installed the dependencies
using the README. All tests passed, and git status showed a clean
working tree.
```

Leave issue 4 open for the handoff below.

Run `deactivate` in the verification copy when finished. Return to your original
working copy with `cd ~/projects/class-project` (or your chosen path) for later
work; the fresh clone was a separate verification copy.

## E. Hand the project to a classmate

Arrange a reviewer who has completed Assignment 0. Give them the repository URL
and final commit ID (`git rev-parse --short HEAD`). They should follow the README
without extra setup instructions from you, create a fresh environment, run the
tests, and check Git status. This is a review exercise; each student still owns
their own implementation and test rationale.

For a private repository, use instructor-approved access. If that is unavailable,
a classmate can direct a supervised walkthrough in a fresh clone on your machine
using only the README while you operate the terminal. Record that method; it
checks the handoff instructions but does not verify another machine. Keep your
credentials private and retain the repository's assigned visibility.

Ask the reviewer to provide this record in issue 4. If they cannot comment there,
paste their feedback with their permission and identify them:

```text
Reviewer:
Commit reviewed:
Method: independent clone / supervised walkthrough
Operating system and Python version:
Commands run and actual test count:
Git status and tracked-cache check results:
Unclear or missing instructions (or none):
Final outcome: succeeded / needs correction
```

If the reviewer needs verbal help, record what was missing and improve the README.
Review and commit corrections with issue 4's number, push them, then have the
reviewer repeat the affected steps. Record the final commit and successful result.
A different supported operating system is welcome but not required.

Close issue 4 only after your self-check and the reviewed handoff both succeed.
If a reviewer is unavailable, request instructor coordination and leave this
criterion open; do not substitute an invented reviewer record.

---

# Completion Check

Submit your repository URL and links to the four closed issues through the
course submission location. Your repository must contain at least four coherent,
issue-linked commits and **at least two passing tests**. Issue 3 contains your
independent test rationale and failure explanation; issue 4 contains both your
fresh-clone evidence and the final classmate handoff record.

## Assessment rubric

| Area | Points | Evidence of completion |
| --- | ---: | --- |
| Defined work and traceability | 20 | Four issues with acceptance criteria, meaningful issue-linked commits, and accurate closure comments |
| Review and commit quality | 20 | Staged diffs reviewed, related changes grouped, no generated files, and comments describing actual review observations |
| Testing and reasoning | 25 | Supplied test plus an independent test, pass/fail/pass evidence, clear expected results, and an explanation of coverage and limitations |
| Documentation and self-verification | 20 | Accurate README, recorded versions and test count, and a successful clean fresh-clone check |
| Handoff and feedback | 15 | Identified reviewer and method, actionable observations, corrections where needed, and successful final verification |

Credit depends on the evidence and reasoning, not the number of screenshots or
commands copied. Unverified claims and missing criteria need revision. Additional
commits or tests earn value through useful work, not through their count alone.
Due dates, reviewer coordination, and submission location come from the course.

Be ready to explain what you staged, why your additional test matters, how a
virtual environment differs from version selection, and what your reviewer
could verify without your help.

[1]: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue "Creating an issue - GitHub Docs"
[2]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls "Autolinked references and URLs - GitHub Docs"
[3]: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue "Linking a pull request to an issue - GitHub Docs"
[4]: https://git-scm.com/docs/gittutorial "Git - gittutorial Documentation"
[5]: https://git-scm.com/docs/gitignore "Git - gitignore Documentation"
[6]: https://docs.python.org/3/library/venv.html "venv — Creation of virtual environments — Python documentation"
[7]: https://pip.pypa.io/en/stable/user_guide/ "User Guide - pip documentation"
[8]: https://docs.pytest.org/en/stable/getting-started.html "Get Started - pytest documentation"
[9]: https://docs.pytest.org/en/stable/how-to/usage.html "How to invoke pytest - pytest documentation"
