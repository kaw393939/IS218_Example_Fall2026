Hello World

This minimal Python project demonstrates an `add` function and one pytest test.
Tested with Python 3.12.7.

## Setup

Prerequisites: Python 3 and Git installed, and this repository cloned locally.
Run all commands from the repository root.

Create and activate a virtual environment on macOS, Linux, or Ubuntu in WSL2:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell with native Windows Python:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

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
