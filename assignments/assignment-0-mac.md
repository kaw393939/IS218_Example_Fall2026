# Assignment 0 for Mac: Set Up Your Development Environment

[README](../README.md) · [Next: Assignment 1](assignment-1-python-pytest.md)

Prepare your computer for professional Python work. Use **VS Code** for editing,
Git for version history, and your **personal GitHub account** to store the project.
You will also practice basic terminal commands; vi is an optional extension.

You need internet access and permission to install software. Reuse tools that
already work. Run commands one at a time; replace placeholders with your details.

## 1. Install tools

Open macOS **Terminal**. Install Homebrew from [brew.sh](https://brew.sh/) and
follow the installer's **Next steps**, including adding Homebrew to PATH.
Install Apple's command line tools if prompted. Passwords do not appear as you type.

```bash
brew --version
brew update
brew install git pyenv openssl@3 readline sqlite3 xz zlib tcl-tk@8 libb2 zstd pkgconfig
git --version
```

The extra libraries support Python builds. macOS already includes `vi`.

Install [VS Code](https://code.visualstudio.com/docs/setup/mac). In VS Code, press
**Command+Shift+P** and run **Shell Command: Install 'code' command in PATH**.
Open a new Terminal window afterward.

## 2. Select the course Python version

Homebrew installed pyenv, which selects your Python version. Initialize it:

```bash
pyenv init --install
```

Close and reopen your terminal. Run `deactivate` first if a virtual environment
is active. Install and select Python 3.12:

```bash
pyenv install -s 3.12
pyenv global 3.12
python3 --version
```

Expect `Python 3.12.x`. Installation can take several minutes; `-s` skips an
already installed version. This is the only Python version required for setup.
Check which interpreter was selected:

```bash
pyenv version
pyenv which python3
```

The optional [Python version-management lab](../labs/python-versions.md) covers
switching versions after Assignment 1. A `.venv` isolates project packages;
changing Python versions does not upgrade an existing environment.

## 3. Practice terminal essentials

Complete the [file operations practice](../handouts/linux-macos-basics.md#try-it-yourself).
Use VS Code for daily editing. The [vi exercise](../handouts/terminal-and-vi.md)
is an optional extension after your environment works.

## 4. Configure Git and SSH

Replace the name and email with yours. Use an email from your GitHub account's
email settings, including its private commit email if preferred:

```bash
git config --global user.name "Your Name"
git config --global user.email "YOUR_GITHUB_EMAIL"
git config --global core.editor "code --wait"
```

Git uses this identity on commits. `code --wait` opens VS Code for Git messages;
save and close the file's editor tab to continue.

Complete the [SSH setup for Mac](../handouts/github-ssh-mac.md).
Confirm `ssh -T git@github.com` greets you with your GitHub username.

## 5. Create your own repository

1. Sign in to GitHub and select **+ → New repository**.
2. Set **Owner** to your personal username.
3. Name it **is218-python-workflow** and choose Public or Private. For a private
   repository, follow the [submission-access instructions](../handouts/submission.md)
   so your instructor can review it.
4. Leave the README, `.gitignore`, and license options **unselected**. Create the repository.
5. In **Quick setup**, select **SSH** and copy the clone URL.

[GitHub's repository guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

Replace `YOUR_SSH_CLONE_URL` with that URL:

```bash
mkdir -p ~/projects
cd ~/projects
git clone YOUR_SSH_CLONE_URL class-project
cd class-project
code .
```

The empty-repository warning is expected. `class-project` is your local folder
name; use it throughout Assignment 1. If you already cloned this repository,
open that folder instead of cloning again. Use a fresh repository for this
exercise rather than a fork of the instructor's completed code.

Install Microsoft's **Python** extension in this VS Code window.

## 6. Check and turn it in

In VS Code's **Terminal → New Terminal**, run:

```bash
pwd
git --version
python3 --version
git status
```

Check that you are in `class-project`, Git runs, and Python reports `3.12.x`.
Submit **your repository's GitHub page URL and one screenshot of VS Code with
this terminal output**. Follow the [submission checklist](../handouts/submission.md), including access verification.
Submission receives credit. Then begin
[Assignment 1](assignment-1-python-pytest.md), where you create issues before code.

## Troubleshooting

- **`code` or `brew` not found:** complete the PATH setup in step 1 and reopen Terminal.
- **pyenv missing:** repeat its initialization in step 2 and reopen the terminal.
- **Python build fails:** check [pyenv's build dependencies](https://github.com/pyenv/pyenv/wiki#suggested-build-environment).
- **Wrong Python version:** leave an active environment with `deactivate`, then inspect `pyenv version`. A folder's `.python-version` overrides the default.
- **SSH or Git errors:** use your SSH handout or the [project troubleshooting reference](../handouts/project-troubleshooting.md).
