# IS218: Introduction to Professional Programming

Learn a repeatable workflow: define a task, make a focused change, test it,
record it in Git, and verify the result on GitHub.

## Start here

Use VS Code and your own GitHub repository. Choose **one** setup route.
Windows students run project commands in Ubuntu under WSL2; Mac students use
macOS Terminal. Existing Linux users should check distribution-specific setup
with the instructor, then use the shared terminal and Python exercises.

| Order | Lesson | You are finished when… |
| --- | --- | --- |
| 0 | [Mac setup](assignments/assignment-0-mac.md) or [Windows/WSL setup](assignments/assignment-0-windows.md) | Python 3.12, Git, VS Code, SSH, and your own repository work. |
| 1 | [Issues, commits, and pytest](assignments/assignment-1-python-pytest.md) | Four issues have linked commits and verification; your fresh clone passes at least two tests. |
| 2 | [Branches and pull requests](assignments/assignment-2-collaboration.md) | A tested change is reviewed and merged through a pull request. |
| 3 | [Managing stashes](labs/stashes.md) | You can inspect, restore, and remove the correct saved work. |
| 4 | [Recovering from mistakes](labs/recovery.md) | You can unstage changes, resolve a conflict, and revert a shared commit. |
| 5 | [Staging and commit shortcuts](labs/staging-and-commits.md) | You can predict what a commit includes, including with `-am`. |
| 6 | [Automated tests](assignments/assignment-3-automation.md) | A pull request runs tests automatically and a deliberate failure is detected. |

Assignment 1 intentionally uses the default branch. Assignment 2 introduces
branches and pull requests. Later labs use disposable local repositories so
practice does not change your assignment history. Submit work where your
instructor directs; follow the [submission and access checklist](handouts/submission.md).

## Reference library

- [Terminal navigation and file operations](handouts/linux-macos-basics.md)
- [GitHub SSH for Mac](handouts/github-ssh-mac.md) · [GitHub SSH for Windows/WSL](handouts/github-ssh-windows.md)
- [Git commands and real-life examples](handouts/git-basics.md)
- [Troubleshooting](handouts/project-troubleshooting.md)
- [Optional terminal and vi practice](handouts/terminal-and-vi.md)
- [Optional Python version management](labs/python-versions.md)

## Instructor example

[Run the minimal Python example](handouts/run-example.md) to see `add` and one
supplied test. It is a demonstration, not your completed assignment. Assignment 1
requires your own second test and issue history. Keep the example small so the
workflow remains visible.

Course baseline: Python **3.12.x**, pytest **8.4.2**. Instructor automation is configured to test
Python 3.12 on Linux and macOS and check local documentation links.
[Maintenance and validation](instructor/maintenance.md) explains how to update it.
