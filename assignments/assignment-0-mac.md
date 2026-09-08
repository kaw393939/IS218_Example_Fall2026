# Assignment 0 for Mac: Environment Setup and Prerequisites

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

## 1. Install Homebrew and development tools

Open **Terminal** from Applications → Utilities, or find it with Spotlight
(Command+Space). Install Homebrew using the instructions at [brew.sh](https://brew.sh/).
Follow the installer's **Next steps** to put Homebrew on your shell's PATH.
PATH is the list of folders your shell searches for commands. Install Apple's
command line developer tools if the installer requests them. When prompted
for a password, use your Mac login password; characters will not appear while
typing. See [Homebrew's installation requirements](https://docs.brew.sh/Installation)
if your macOS version is unsupported.

```bash
brew --version
brew update
brew install git python pyenv openssl@3 readline sqlite3 xz zlib tcl-tk@8 libb2 zstd pkgconfig
git --version
python3 --version
```

`brew --version`, `git --version`, and `python3 --version` should each print a
version number. The initial Python version may differ from the course version;
select it in section 2.

Homebrew supplies Git, Python, and the tools needed for version management.
The additional libraries support Python builds.
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

Close and reopen your Terminal window. If an environment such as `(.venv)`
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

Run these in macOS Terminal, replacing the sample identity with yours:

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

Complete the [GitHub SSH handout for Mac](../handouts/github-ssh-mac.md).
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
Extensions view.
The extension provides Python editing and interpreter selection when you begin
creating Python files in Assignment 1. That assignment will select the project's
`.venv` once it exists. See [VS Code's Python environment guide](https://code.visualstudio.com/docs/python/environments).

**Checkpoint:** `pwd` points to your class repository, `git status` succeeds, and
`python3 --version` reports `3.12.x` (or your instructor's specified version).

## Completion and submission

Submit the following through the course submission location. **Submission receives
credit; there is no scored rubric.**
Do not create the four Assignment 1 issues yet.

- [ ] `brew --version` succeeds.
- [ ] Git and Python version output from your development terminal.
- [ ] Output demonstrating Python 3.13 selected and then Python 3.12 restored.
- [ ] Successful GitHub SSH greeting showing your username. Never submit a private key.
- [ ] The saved vi practice file and a short explanation of normal and insert modes.
- [ ] The Microsoft Python extension is installed in the project's VS Code window.
- [ ] Your class repository URL and a screenshot of it opened with `code .`.
- [ ] Two or three sentences explaining Git versus GitHub, and Python version selection versus a virtual environment.

You are ready for [Assignment 1](assignment-1-python-pytest.md) when these checks
are complete. That assignment verifies commits, pushes, and a passing pytest test.

## Troubleshooting

### Commands are missing

If `code` is not found, repeat the VS Code PATH command in section 1 and
restart Terminal. If `brew` is not found, complete Homebrew's installer Next
steps for your shell.

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
