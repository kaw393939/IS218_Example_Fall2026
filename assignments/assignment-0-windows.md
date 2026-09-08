# Assignment 0 for Windows: Environment Setup and Prerequisites

[Back to README](../README.md) · [Next: Assignment 1](assignment-1-python-pytest.md)

## Purpose

This course assumes prior Python coursework and basic Git experience. Assignment
0 establishes a consistent professional workspace and checks your readiness.
Use VS Code for daily editing; vi is a short terminal-literacy exercise.

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

Complete the checkpoints in order. If a tool is already configured, verify its
checkpoint and reuse it; reinstalling is not a learning objective. Linked
handouts provide refresher instructions, and [troubleshooting](#troubleshooting)
is available at the end of this page. Run commands one
at a time and read their output. Do not type a shell prompt such as `$`.
Replace labels such as `YOUR_GITHUB_EMAIL` with your own information. Blocks marked
with a language show what belongs in a terminal or file; the backticks are not
part of the command. Wait for the prompt to return before running the next step.
If a command fails, resolve that error before continuing.

Save screenshots or copy the requested output as you finish each checkpoint;
you will submit this evidence at the end.

## 1. Install WSL2, Ubuntu, and development tools

Use a Windows version supported by [Microsoft's WSL installation guide](https://learn.microsoft.com/en-us/windows/wsl/install).
If you have used WSL before, check `wsl --list --verbose` in PowerShell:

- If Ubuntu shows version `2`, reuse it and continue with the Ubuntu tools below.
- If Ubuntu shows version `1`, run `wsl --set-version Ubuntu 2`, using the exact
  listed distribution name in place of `Ubuntu`, then check the version again.
- If Ubuntu is not installed, use the installation command below.

For a new installation, find PowerShell in Start, choose **Run as administrator**,
run this command, and restart if prompted:

```powershell
wsl --install -d Ubuntu
```

Open Ubuntu from the Start menu. On its first launch, create a Linux username
and password; an existing Ubuntu installation already has this account.
This is a Linux account; its password can differ from your Windows password.
Password characters do not appear while typing. `sudo` will ask for this Linux
password when installing tools. In PowerShell, check:

```powershell
wsl --list --verbose
```

Ubuntu must show version `2`. If it shows `1`, run `wsl --set-version Ubuntu 2`
(substitute the listed distribution name if different).

**Use the Ubuntu terminal for all remaining project commands.** Install Git,
Python, vi's Vim implementation, SSH, and Python build dependencies:

```bash
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv vim openssh-client curl build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libzstd-dev
git --version
python3 --version
```

`git --version` and `python3 --version` should each print a version number.
The initial Python version may differ from the course version; select it in section 2.

The development libraries support building Python with pyenv.

Install [VS Code on Windows and its WSL extension](https://code.visualstudio.com/docs/remote/wsl).
In the Windows installer, keep **Add to PATH** selected. Open VS Code, select
Extensions, search for **WSL**, and install the extension published by Microsoft.
Close and reopen Ubuntu afterward so it can find the `code` command.
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

Close and reopen your Ubuntu terminal. If an environment such as `(.venv)`
is already active, run `deactivate` first so it cannot override the version you
are selecting. Then run:

```bash
pyenv --version
pyenv install -s 3.12
pyenv global 3.12
python --version
python3 --version
```

`3.12` selects the latest patch available to your pyenv installation in that
series; record the full version printed on your machine. This example project
was tested with 3.12.7, but that exact patch is not required.

Installing Python can take several minutes while it builds. The `-s` option
skips installation if that exact version is already installed. For `BUILD FAILED`,
use [troubleshooting](#troubleshooting) before continuing.

Practice switching versions in a disposable folder. If your prompt shows an
active virtual environment such as `(.venv)`, run `deactivate` first:

```bash
mkdir -p ~/terminal-practice/python-versions
cd ~/terminal-practice/python-versions
pyenv install -s 3.13
pyenv local 3.13
python --version
pyenv local 3.12
python --version
pyenv versions
pyenv which python
```

`global` sets your user's default; `local` writes a `.python-version` file for
that folder and its descendants. The exercise leaves the practice folder on
3.12. Capture the two `python --version` results as your switching evidence.
See [pyenv's installation and usage guide](https://github.com/pyenv/pyenv).

A `.venv` uses the Python interpreter with which it was created. Changing the
selected version does not update an existing virtual environment. Assignment 1
will create your first project environment after you choose Python 3.12. For a
future version change, you will recreate the environment and reinstall its
requirements. No virtual environment commands are needed in Assignment 0.
See [Python's virtual environment documentation](https://docs.python.org/3/library/venv.html).

## 3. Practice the terminal and vi

Complete the exercise in the [terminal and vi handout](../handouts/terminal-and-vi.md).
Be able to explain your current directory, move between directories, and open,
edit, save, and exit vi. After this exercise, use VS Code for project files.

## 4. Configure Git and GitHub SSH access

Run these in Ubuntu, replacing the sample identity with yours:

```bash
git config --global user.name "Your Name"
git config --global user.email "YOUR_GITHUB_EMAIL"
git config --global core.editor "code --wait"
git config --global --get user.name
git config --global --get user.email
```

Git will open VS Code when it needs an editor. `--wait` keeps Git waiting until
you save and close that file's editor tab. These are user-wide settings. See
[VS Code's Git editor instructions](https://code.visualstudio.com/docs/sourcecontrol/overview).

Use an email associated with your GitHub account, or your GitHub-provided private
commit email from GitHub's email settings. This identity labels commits; SSH
authentication is a separate step.

Complete the [GitHub SSH handout for Windows](../handouts/github-ssh-windows.md).
Confirm `ssh -T git@github.com` identifies your GitHub username.

## 5. Clone your class repository and open VS Code

On GitHub, open your own assigned class repository, not the instructor's example.
Select **Code → SSH** and copy the URL. An empty repository instead shows an SSH
URL in **Quick setup**. If you already cloned your class repository, open its
existing folder with `cd` and skip the clone block. For example, if it is already
at the path used in this handout, run `cd ~/projects/class-project`.
Replace `YOUR_SSH_CLONE_URL` below with that complete URL. Use a destination name
that does not already exist:

```bash
mkdir -p ~/projects
cd ~/projects
git clone YOUR_SSH_CLONE_URL class-project
cd class-project
```

An empty repository can print `You appear to have cloned an empty repository.`
This is expected before your first commit. If cloning fails instead, fix the
error before continuing. From your new or existing repository folder, run:

```bash
pwd
git remote -v
git status
code .
```

The dot means the current directory. VS Code should show this repository's files;
an empty repository may have no visible project files yet. Its hidden `.git`
folder still stores repository information. Keep `~/projects/class-project` as
your working copy for Assignment 1. If you chose a different folder name, use
that name in later commands.
Open **Terminal → New Terminal** in VS Code and run:

```bash
pwd
git --version
python3 --version
```

For command or interpreter problems, use [troubleshooting](#troubleshooting).

Install the **Python** extension published by **Microsoft** from VS Code's
Extensions view. In this WSL window, choose **Install in WSL: Ubuntu** if offered.
The extension provides Python editing and interpreter selection when you begin
creating Python files in Assignment 1. That assignment will select the project's
`.venv` once it exists. See [VS Code's Python environment guide](https://code.visualstudio.com/docs/python/environments).

**Checkpoint:** `pwd` points to your class repository, `git status` succeeds, and
`python3 --version` reports `3.12.x` (or your instructor's specified version).

## Completion and submission

Submit the following through the course submission location. **Submission receives
credit; there is no scored rubric.**
Do not create the four Assignment 1 issues yet.

- [ ] Ubuntu shows WSL version 2.
- [ ] Git and Python version output from your development terminal.
- [ ] Output demonstrating Python 3.13 selected and then Python 3.12 restored.
- [ ] Successful GitHub SSH greeting showing your username. Never submit a private key.
- [ ] The saved vi practice file and a short explanation of normal and insert modes.
- [ ] The Microsoft Python extension is installed in the project's VS Code window.
- [ ] Your class repository URL and a screenshot of it opened with `code .` showing the WSL connection.
- [ ] Two or three sentences explaining Git versus GitHub, and Python version selection versus a virtual environment.

You are ready for [Assignment 1](assignment-1-python-pytest.md) when these checks
are complete. That assignment verifies commits, pushes, and a passing pytest test.

## Troubleshooting

### Commands are missing

If `code` is not found, check the Windows VS Code installation, Add to PATH
option, and Microsoft WSL extension, then reopen Ubuntu. Launch `code .` inside
Ubuntu and confirm the editor window shows a WSL connection.

If pyenv is missing, rerun its shell initialization from section 2 and reopen
the terminal. If a Python build fails, compare your installed libraries with
[pyenv's build environment guide](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
and read the reported build log before retrying.

### Python reports the wrong version

If a virtual environment is active, leave it with `deactivate`. Run
`pyenv version` and `pyenv which python` to inspect the selection. A repository's
`.python-version` can override your user default; follow any instructor-supplied
version requirement. Restart VS Code if its terminal retains an older environment.

### GitHub authentication or repository access fails

Use the troubleshooting section in your platform's SSH handout. GitHub login,
SSH authentication, and access to a particular repository are separate checks.
For project Git and pytest problems, use the
[project troubleshooting reference](../handouts/project-troubleshooting.md).
