# Implementation and validation notes

[Course index](../README.md) · [Maintenance](maintenance.md)

## Changes prepared

- Made the README a course index with a sequenced path and reference library.
- Integrated terminal and Git guides; retained platform-specific SSH handouts.
- Moved the example run instructions into a dedicated handout.
- Reduced initial setup to one required Python version; made version switching and vi extensions.
- Added private-repository access and submission evidence instructions.
- Added Assignment 2 for collaboration and Assignment 3 for automated testing.
- Added disposable stash, recovery, and staging labs with starting states and checkpoints.
- Selected pytest 8.4.2 as the direct dependency baseline and added instructor CI/documentation checks.

## Validation on September 10, 2026

Local checks use macOS and Python 3.12.14 with pytest 8.4.2. The root sample retains
one supplied test. Stash, recovery, and staging command sequences were replayed in
temporary repositories, including the deliberate conflict and partial staging.
All 20 Markdown pages passed local link, heading, fence, and shell-syntax checks.
The checker rejected deliberately broken fixtures. Instructor and student workflow
YAML parsed successfully. A clean copy of the Python example passed, failed with
an intentional wrong expectation, then passed after restoration.

Interactive review/editor actions were supplied by the validation harness; they
still need a student usability walkthrough.

Hosted GitHub Actions, actual GitHub invitations/reviews, fresh-machine Homebrew
installation, and Windows/WSL setup have not been executed in this change. The
workflow is configured for later hosted verification. External links are not
covered by the local documentation checker. These notes record local validation before publication; check GitHub Actions
for subsequent hosted results.
