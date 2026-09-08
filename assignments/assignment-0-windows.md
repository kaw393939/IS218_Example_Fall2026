# Assignment 0 for Windows: Environment Setup and Prerequisites

[Back to README](../README.md) · [Next: Assignment 1](assignment-1-python-pytest.md)

## Purpose

Prepare a professional development environment before writing project code.
You will use the terminal to navigate files, Git to record work, SSH to connect
to GitHub, VS Code to edit a project, and Python to run code. Learning these tools
now makes it easier to reproduce your work and collaborate later.

A terminal is the window where you type commands; a shell interprets them.
You will use Ubuntu under WSL2 with its Bash shell for class project work.
PowerShell is used only for the WSL installation and verification steps below.

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

## 1. Install WSL2, Ubuntu, and development tools

Use a Windows version supported by [Microsoft's WSL installation guide](https://learn.microsoft.com/en-us/windows/wsl/install).
Open **PowerShell as Administrator**, run the following, and restart if prompted:

```powershell
wsl --install -d Ubuntu
```

Open Ubuntu from the Start menu and create its Linux username and password.
Password characters do not appear while typing. In PowerShell, check:

```powershell
wsl --list --verbose
```

Ubuntu must show version `2`. If it shows `1`, run `wsl --set-version Ubuntu 2`
(substitute the listed distribution name if different).

**Use the Ubuntu terminal for all remaining project commands.** Install Git,
Python, vi's Vim implementation, SSH, and Python build dependencies:

```bash
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv vim openssh-client curl build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
git --version
python3 --version
```

The development libraries support building Python with pyenv; consult its
[build environment guide](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
if a build reports a missing library.

Install [VS Code on Windows and its WSL extension](https://code.visualstudio.com/docs/remote/wsl).
Keep class projects in Ubuntu's home directory, such as `~/projects`, and launch
the editor from Ubuntu using `code .`. The editor should indicate a WSL connection.

## 2. Select and change Python versions

We use pyenv to install additional Python versions and choose which one runs.
Keep Ubuntu's system Python in place.

Install pyenv once. If `~/.pyenv` already exists, check your
existing installation rather than cloning over it:

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
~/.pyenv/bin/pyenv init --install
```

Close and reopen your Ubuntu terminal, then run:

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

Run these in Ubuntu, replacing the sample identity with yours:

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

Complete the [GitHub SSH handout for Windows](../handouts/github-ssh-windows.md).
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

Confirm VS Code is connected to WSL and this terminal is Ubuntu. If `code` is
not found, check the Windows VS Code installation and WSL extension from section 1.
If pyenv is missing, reopen Ubuntu after its initialization.

## Completion and submission

Submit the following through your instructor's designated submission location.
Do not create the four Assignment 1 issues yet.

- [ ] Ubuntu shows WSL version 2.
- [ ] Git and Python version output from your development terminal.
- [ ] Output demonstrating Python 3.13 selected and then Python 3.12 restored.
- [ ] Successful GitHub SSH greeting showing your username. Never submit a private key.
- [ ] The saved vi practice file and a short explanation of normal and insert modes.
- [ ] Your class repository URL and a screenshot of it opened with `code .` showing the WSL connection.
- [ ] Two or three sentences explaining Git versus GitHub, and Python version selection versus a virtual environment.

You are ready for [Assignment 1](assignment-1-python-pytest.md) when these checks
are complete. That assignment verifies commits, pushes, and a passing pytest test.
