# IS218: Introduction to Professional Programming

Hello World

## Start here

Build on your Python and Git experience using a repository in your **personal
GitHub account**. Assignment 0 shows you how to create it.

**Create an issue → make and test the change → commit with its issue number →
push → verify and close the issue.**

Use VS Code for daily work. The vi exercise is a short terminal introduction.
These are practice assignments: submit the requested work to receive credit.

Choose **one** setup assignment for your computer:

- **[Assignment 0 for Windows](assignments/assignment-0-windows.md)** — Set up Ubuntu under WSL2 and your development tools.
- **[Assignment 0 for Mac](assignments/assignment-0-mac.md)** — Set up Homebrew and your development tools in macOS Terminal.

After completing your platform's Assignment 0, everyone continues to
**[Assignment 1 — Python Project with GitHub Issues and pytest](assignments/assignment-1-python-pytest.md)**.
**Create four GitHub issues before coding. Each issue needs its own linked
commit(s) and verification comment before you close it.**

Assignment 0 covers Git, Python version selection, SSH, VS Code, and terminal
practice. If you get stuck, use the [troubleshooting reference](handouts/project-troubleshooting.md).

## Example project

This minimal Python project demonstrates an `add` function and one pytest test.
Tested with Python 3.12.7.

This is the instructor's baseline example, with one supplied test. Complete assignment work in your own
personal GitHub repository; running this example alone does not complete the four
issues required by Assignment 1. Your submission adds at least one independently
designed test, so its final result must be **at least two passing tests**. The
extra test is intentionally not supplied here.

```text
.
├── README.md          # Project overview and setup instructions
├── .gitignore         # Excludes local environments and generated caches
├── requirements.txt   # Project dependency: pytest
├── app.py             # The add function
└── tests/
    └── test_app.py    # One test of add
```

The `assignments/` and `handouts/` folders contain the course instructions.

## Run the example

Prerequisites: complete your platform's Assignment 0. To try this example, clone
it into a new folder from macOS Terminal or Ubuntu under WSL2:

```bash
mkdir -p ~/projects
cd ~/projects
git clone git@github.com:kaw393939/IS218_Example_Fall2026.git is218-example
cd is218-example
```

If already cloned, open that existing folder instead. The **repository root** is
the folder containing this README, `app.py`, and the hidden `.git` directory.
Run all remaining commands there.

Create and activate a virtual environment on macOS, Linux, or Ubuntu in WSL2:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows students run these commands inside Ubuntu under WSL2.

Reactivate the environment when opening a new terminal. The local `.venv`
directory is ignored by Git because each developer recreates it locally.
Python's `__pycache__/` and pytest's `.pytest_cache/` contain generated files
and are also ignored.

With the environment activated, install dependencies and run the test:

```bash
python -m pip install -r requirements.txt
python -m pytest
```

Expect `1 passed`. Use `python -m pytest` so the repository root is included in
Python's import path and the test can import `app.py` without extra configuration.

To check that the test detects an incorrect result, temporarily change the
expected value in `tests/test_app.py` from `5` to `6`, run the test and confirm it
fails, then restore `5` and run it again to confirm it passes.

To return to this example in a new terminal after setup, use its existing
folder and environment:

```bash
cd ~/projects/is218-example
source .venv/bin/activate
python -m pytest
```

Substitute your folder path if different. Run `deactivate` when finished to
leave the virtual environment.
