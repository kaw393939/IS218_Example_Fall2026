# IS218: Python Development Setup

Hello World

## Start here

We are setting up a professional development environment: a terminal workflow,
version control, secure GitHub access, an editor, and isolated Python dependencies.

1. **[Assignment 0 — Environment Setup and Prerequisites](assignments/assignment-0-environment-setup.md):** Prepare your computer before starting project work.
2. **[Assignment 1 — Python Project with GitHub Issues and pytest](assignments/assignment-1-python-pytest.md):** Complete four issues to build and verify your own minimal project.

Prerequisites for Assignment 1:

| Platform | Required environment |
| --- | --- |
| Windows | WSL2 with Ubuntu; Git and Python installed inside Ubuntu; Windows VS Code with the WSL extension |
| macOS | Homebrew; Git and Python installed through Homebrew; VS Code |
| Both | GitHub account, working SSH authentication, pyenv for Python version selection, and ability to open a project with `code .` |

Assignment 0 walks through these prerequisites. Keep the
[GitHub SSH handout](handouts/github-ssh.md) and
[terminal and vi handout](handouts/terminal-and-vi.md) available as references.

## Example project

This minimal Python project demonstrates an `add` function and one pytest test.
Tested with Python 3.12.7.

## Setup

Prerequisites: complete Assignment 0 and clone this repository locally.
Run all commands from the repository root.

Create and activate a virtual environment on macOS, Linux, or Ubuntu in WSL2:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows students run these commands inside Ubuntu under WSL2.

Reactivate the environment when opening a new terminal. The local `.venv`
directory is ignored by Git.

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
