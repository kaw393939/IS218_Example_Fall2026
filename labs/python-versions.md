# Optional lab: Select Python versions

[Course index](../README.md)

## Outcome and prerequisites

After Assignment 1, practice switching interpreters without changing the assignment
environment. You need the pyenv installation from Assignment 0. Deactivate any active
virtual environment first. Use a new practice folder outside your repositories.

```bash
mkdir -p ~/terminal-practice
cd ~/terminal-practice
mkdir python-version-lab
cd python-version-lab
pyenv install -s 3.13
pyenv local 3.13
python3 --version
pyenv local 3.12
python3 --version
cat .python-version
```

Use a different folder name if it exists. Expect `3.13.x`, then `3.12.x`.
`pyenv local` writes `.python-version` for this directory and descendants;
`pyenv global` sets the user default. Confirm selection with `pyenv version`.
The existing Assignment 1 `.venv` still uses its original interpreter.

## Independent check

Leave this folder and inspect `python3 --version` and `pyenv version` again.
Explain which setting selected the interpreter. Do not change your assignment's
Python version merely to complete this lab.

See the [pyenv guide](https://github.com/pyenv/pyenv).
