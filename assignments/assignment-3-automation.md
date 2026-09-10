# Assignment 3: Run tests automatically

[Course index](../README.md) · [Previous: Assignment 2](assignment-2-collaboration.md)

## Outcome and prerequisites

Use GitHub Actions to run your Python tests on pushes and pull requests. Complete
Assignment 2 first. Work in your personal Python repository, with its existing tests
and `requirements.txt`. The instructor repository's workflow is an example, not a
substitute for adding one to your own project. CI is not required for Assignment 1.

## 1. Plan and branch

Create an issue titled `Run pytest with GitHub Actions`. Record these criteria:

- [ ] Pushes and pull requests trigger tests on Python 3.12.
- [ ] A deliberate failing test produces a failed workflow run.
- [ ] Restoring the test produces a passing run before merge.

From a clean working tree, switch to your default branch, pull with `--ff-only`,
and create `ci/python-tests`. Substitute the default branch name if not `main`.

## 2. Add the workflow

Create `.github/workflows/tests.yml` in VS Code:

```yaml
name: Python tests
on: [push, pull_request]
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: python -m pip install -r requirements.txt
      - run: python -m pytest
```

Run your tests locally. Review and stage only the workflow, commit with your actual
issue number, and push the feature branch with `-u`. Open a pull request targeting
the default branch. In **Actions**, inspect the run and its pytest output. If your
repository requires approval to run workflows, ask the maintainer to approve it.

The runner is a fresh machine. Checkout obtains your files; setup-python chooses
the interpreter; pip installs dependencies; pytest verifies behavior. See
[GitHub's Python automation guide](https://docs.github.com/en/actions/tutorials/build-and-test-code/python).

## 3. Demonstrate failure and recovery

On this unmerged feature branch only, change the supplied test's expected `5` to
`6`. Run pytest locally and confirm failure. Commit this intentional exercise change
with the issue number and push. Record the failed workflow URL and the relevant
assertion output. Do not merge this state.

Restore the correct expected result, verify locally, commit the correction, and
push again. Record the passing workflow URL. This differs from Assignment 1's local
failure demonstration: here the temporary failure is committed to the feature
branch specifically to prove CI detects it.

## 4. Review and finish

Request review using Assignment 2's process. Merge only the corrected passing
version, update your local default branch, and rerun tests. In the issue, record
both workflow URLs and the merged pull request link, then close it.

## Independent check and submission

Explain whether a green run proves that every possible bug is absent. Identify
one behavior your tests do not cover. Submit the links through the course channel
and follow the [access checklist](../handouts/submission.md).

A failed run may indicate installation trouble rather than a failing assertion;
read the failing step before changing code. If no run appears, check Actions is
enabled and the workflow path, indentation, and trigger names.
