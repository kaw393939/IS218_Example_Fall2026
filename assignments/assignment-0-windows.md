# Assignment 0 for Windows: Set Up Your Development Environment

[README](../README.md) · [Next: Assignment 1](assignment-1-python-pytest.md)

Prepare your computer for professional Python work. Use **VS Code** for editing,
Git for version history, and your **personal GitHub account** to store the project.
You will also practice basic terminal commands; vi is an optional extension.

You need internet access and permission to install software. Reuse tools that
already work. Run commands one at a time; replace placeholders with your details.

## 1. Install WSL2 and tools

For a new WSL installation, open **PowerShell as Administrator**:

```powershell
wsl --install -d Ubuntu
```

Restart if prompted. Open **Ubuntu** and create its Linux username and password.
Passwords do not appear as you type. Check in PowerShell:

```powershell
wsl --list --verbose
```

Ubuntu must show version `2`. If already installed, reuse it. If it shows `1`,
run `wsl --set-version Ubuntu 2`, substituting its listed name if different.
[Microsoft's WSL guide](https://learn.microsoft.com/en-us/windows/wsl/install).

**Run the remaining commands in Ubuntu, not PowerShell.**

```bash
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv vim openssh-client curl build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libzstd-dev
git --version
python3 --version
```

`sudo` asks for your Ubuntu password. The extra libraries support Python builds.

Install [VS Code on Windows](https://code.visualstudio.com/docs/remote/wsl), keep
**Add to PATH** selected, and install Microsoft's **WSL** extension. Reopen Ubuntu.
Keep projects in Ubuntu's home folder, as shown below.

## 2. Select the course Python version

Install pyenv once. If `~/.pyenv` already exists, reuse it and skip the clone:

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
~/.pyenv/bin/pyenv init --install
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

Complete the [SSH setup for Windows](../handouts/github-ssh-windows.md).
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
On the WSL connection, choose **Install in WSL: Ubuntu** if offered.

## 6. Check and turn it in

In VS Code's **Terminal → New Terminal**, run:

```bash
pwd
git --version
python3 --version
git status
```

Check that you are in `class-project`, Git runs, and Python reports `3.12.x`.
The VS Code window must show a WSL connection.
Submit **your repository's GitHub page URL and one screenshot of VS Code with
this terminal output**. Follow the [submission checklist](../handouts/submission.md), including access verification.
Submission receives credit. Then begin
[Assignment 1](assignment-1-python-pytest.md), where you create issues before code.

## Troubleshooting

- **`code` not found:** check Windows VS Code's Add to PATH option and WSL extension, then reopen Ubuntu.
- **pyenv missing:** repeat its initialization in step 2 and reopen the terminal.
- **Python build fails:** check [pyenv's build dependencies](https://github.com/pyenv/pyenv/wiki#suggested-build-environment).
- **Wrong Python version:** leave an active environment with `deactivate`, then inspect `pyenv version`. A folder's `.python-version` overrides the default.
- **SSH or Git errors:** use your SSH handout or the [project troubleshooting reference](../handouts/project-troubleshooting.md).
