# IS218: Python Development Setup

Hello World

## Start here

We are setting up a professional development environment: a terminal workflow,
version control, secure GitHub access, an editor, and isolated Python dependencies.

Choose **one** setup assignment for your computer:

- **[Assignment 0 for Windows](assignments/assignment-0-windows.md)** — Set up Ubuntu under WSL2 and your development tools.
- **[Assignment 0 for Mac](assignments/assignment-0-mac.md)** — Set up Homebrew and your development tools in macOS Terminal.

After completing your platform's Assignment 0, everyone continues to
**[Assignment 1 — Python Project with GitHub Issues and pytest](assignments/assignment-1-python-pytest.md)**.
Complete four issues to build and verify your own minimal project.

Prerequisites for Assignment 1:

| Platform | Required environment |
| --- | --- |
| Windows | WSL2 with Ubuntu; Git and Python installed inside Ubuntu; Windows VS Code with the WSL extension |
| macOS | Homebrew; Git and Python installed through Homebrew; VS Code |
| Both | GitHub account, working SSH authentication, pyenv for Python version selection, and ability to open a project with `code .` |

Each Assignment 0 page includes its platform's prerequisites and links to its SSH
setup handout. Both use the [terminal and vi handout](handouts/terminal-and-vi.md).

## Example project

This minimal Python project demonstrates an `add` function and one pytest test.
Tested with Python 3.12.7.

This is the instructor's completed example. Complete assignment work in your own
assigned class repository; running this example alone does not complete the four
issues required by Assignment 1.

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

## Setup

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

Run `deactivate` when finished to leave the virtual environment.
