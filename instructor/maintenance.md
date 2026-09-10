# Maintain and validate the course

[Course index](../README.md)

## Scope and baseline

Keep the root Python example minimal: `add` and exactly one supplied pytest test.
Students design their second test in Assignment 1. Instructor tooling belongs in
`scripts/` and `.github/`; it must not inflate the student's expected test count.

The supported teaching baseline is Python 3.12.x with `pytest==8.4.2`. This pins
the direct teaching dependency, not the full transitive environment. Patch releases
of Python may vary; record the actual interpreter and package versions when validating.

## Local checks

From the repository root with a Python 3.12 environment activated:

```bash
python --version
python -m pip install -r requirements.txt
python -m pytest
python scripts/check_docs.py
git diff --check
```

Expect one passing sample test and no documentation errors. The documentation
checker validates local inline Markdown links and heading fragments, balanced code
fences, and shell-block syntax. It ignores external URLs; it is not a full Markdown
renderer. Do not execute setup blocks automatically on a maintainer's real account.

## Before releasing course changes

1. Run setup from a fresh macOS account and a fresh Ubuntu/WSL environment. Check
   editor integration, SSH authentication, and a new personal repository.
2. Walk through Assignment 1 using only the instructions and confirm its four-issue
   evidence and fresh-clone result. Keep the independently designed test unsupplied.
3. Replay the Git labs in temporary folders. Check each expected state, including
   the intentional conflict and untracked files.
4. Run the GitHub workflow after publishing and check both macOS and Linux jobs.
   A local successful run does not prove hosted CI or WSL setup has passed.
5. Verify external documentation links and the course submission/access policy.

The workflow is prepared to run on pushes and pull requests. Until changes are
published, hosted results are pending. Initial local validation details are in
[the implementation notes](implementation-notes.md).

## Update policy

Update pytest deliberately between teaching checkpoints. Change `requirements.txt`,
the Assignment 1 example, README baseline, and this guide together. Test with a fresh
environment and inspect upstream release notes. Review action versions and supported
Python versions each term. Do not silently change students' environment requirements
mid-assignment.

The README is the course index. Assignments define required work and evidence;
handouts explain concepts; labs provide disposable practice. Maintain one canonical
SSH handout per platform and link to it from other pages.
