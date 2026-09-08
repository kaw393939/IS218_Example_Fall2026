# Assignment 0 for Mac: Environment Setup and Prerequisites

[Back to README](../README.md) · [Next: Assignment 1](assignment-1-python-pytest.md)

## Purpose

Prepare a professional development environment before writing project code.
You will use the terminal to navigate files, Git to record work, SSH to connect
to GitHub, VS Code to edit a project, and Python to run code. Learning these tools
now makes it easier to reproduce your work and collaborate later.

A terminal is the window where you type commands; a shell interprets them.
You will use macOS Terminal with its usual zsh shell for class project work.

Git stores local version history. GitHub hosts repositories and issues online.
Python runs your code. A version manager chooses a Python interpreter; a virtual
environment isolates a project's packages. Assignment 1 introduces those packages
and automated testing after this setup is complete.

## Before starting

Have a GitHub account, internet access, permission to install software, and your
instructor's class repository invitation or URL. Accept the invitation first if
one was provided. Use your own assigned repository for submissions. If you have
not received one, complete the local exercises while obtaining it from your instructor.

Complete this page in order, including its linked handouts. Run commands one
at a time and read their output. Do not type a shell prompt such as `$`.

## 1. Install Homebrew and development tools

Open Terminal. Install Homebrew using the instructions at [brew.sh](https://brew.sh/).
Follow the installer's **Next steps** to put Homebrew on your shell's PATH.
PATH is the list of folders your shell searches for commands. Install Apple's
command line developer tools if the installer requests them.

```bash
brew --version
brew install git python pyenv openssl@3 readline sqlite3 xz zlib tcl-tk@8 libb2 zstd
git --version
python3 --version
```

Homebrew supplies Git, Python, and the tools needed for version management.
The additional libraries support Python builds; see the
[pyenv build environment guide](https://github.com/pyenv/pyenv/wiki#suggested-build-environment).
macOS already provides a `vi` command.

Install [VS Code for macOS](https://code.visualstudio.com/docs/setup/mac) and move it
to Applications. Open its Command Palette with **Command+Shift+P**, run
**Shell Command: Install 'code' command in PATH**, then open a new terminal.

## 2. Select and change Python versions

We use pyenv to install additional Python versions and choose which one runs.
Homebrew's Python remains available.

Pyenv was installed through Homebrew above. Configure your shell:

```bash
pyenv init --install
```

Close and reopen your Terminal window, then run:

```bash
pyenv --version
pyenv install 3.12
pyenv global 3.12
python --version
python3 --version
```

`3.12` selects the latest patch available to your pyenv installation in that
series; record the full version printed on your machine. This example project
was tested with 3.12.7, but that exact patch is not required.

Practice switching versions in a disposable folder, with no virtual environment active:

```bash
mkdir -p ~/terminal-practice/python-versions
cd ~/terminal-practice/python-versions
pyenv install 3.13
pyenv local 3.13
python --version
pyenv local 3.12
python --version
pyenv versions
pyenv which python
```

`global` sets your user's default; `local` writes a `.python-version` file for
that folder and its descendants. The exercise leaves the practice folder on
3.12. See [pyenv's installation and usage guide](https://github.com/pyenv/pyenv).

A `.venv` uses the interpreter with which it was created. Switching pyenv does
not change an existing environment. For a later project version change, run
`deactivate` if active, select the new version, and recreate `.venv` before
reinstalling requirements. You can preserve the old environment temporarily:

```bash
mv .venv .venv-backup
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

This later-project example requires an existing `.venv` and `requirements.txt`;
skip it for Assignment 0. Keep `.venv-backup/` out of commits by adding it to
`.git/info/exclude` if you use this approach. See
[Python's virtual environment documentation](https://docs.python.org/3/library/venv.html).

## 3. Configure Git and GitHub SSH access

Run these in macOS Terminal, replacing the sample identity with yours:

```bash
git config --global user.name "Your Name"
git config --global user.email "YOUR_GITHUB_EMAIL"
git config --global core.editor "vi"
git config --global --get user.name
git config --global --get user.email
```

Use an email associated with your GitHub account, or your GitHub-provided private
commit email from GitHub's email settings. This identity labels commits; SSH
authentication is a separate step.

Complete the [GitHub SSH handout for Mac](../handouts/github-ssh-mac.md).
Confirm `ssh -T git@github.com` identifies your GitHub username.

## 4. Practice the terminal and vi

Complete the exercise in the [terminal and vi handout](../handouts/terminal-and-vi.md).
Be able to explain your current directory, move between directories, edit and
save a file with vi, and quit without saving an unwanted change.

## 5. Clone your class repository and open VS Code

On GitHub, open your own class repository and select **Code → SSH**. Copy the URL.
Replace `YOUR_SSH_CLONE_URL` below with that complete URL. Use a destination name
that does not already exist:

```bash
mkdir -p ~/projects
cd ~/projects
git clone YOUR_SSH_CLONE_URL class-project
cd class-project
pwd
git remote -v
git status
code .
```

The dot means the current directory. VS Code should show this repository's files.
Open **Terminal → New Terminal** in VS Code and run:

```bash
pwd
git --version
python3 --version
```

If `code` is not found, repeat the PATH command from section 1 and restart
Terminal. If pyenv is missing, reopen the shell after its initialization.

## Completion and submission

Submit the following through your instructor's designated submission location.
Do not create the four Assignment 1 issues yet.

- [ ] `brew --version` succeeds.
- [ ] Git and Python version output from your development terminal.
- [ ] Output demonstrating Python 3.13 selected and then Python 3.12 restored.
- [ ] Successful GitHub SSH greeting showing your username. Never submit a private key.
- [ ] The saved vi practice file and a short explanation of normal and insert modes.
- [ ] Your class repository URL and a screenshot of it opened with `code .`.
- [ ] Two or three sentences explaining Git versus GitHub, and Python version selection versus a virtual environment.

You are ready for [Assignment 1](assignment-1-python-pytest.md) when these checks
are complete. That assignment verifies commits, pushes, and a passing pytest test.
