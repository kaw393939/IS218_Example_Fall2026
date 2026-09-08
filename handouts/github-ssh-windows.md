# Handout: GitHub SSH for Windows

[Back to Assignment 0 for Windows](../assignments/assignment-0-windows.md)

## Why SSH?

SSH authenticates your computer to GitHub when you clone or push using an SSH URL.
A key pair has a **public key**, which you add to GitHub, and a **private key**,
which stays on your computer. A passphrase protects the private key; an SSH agent
can hold the unlocked key for use by Git. Git's configured name and email label
commits but do not authenticate you.

Use **Ubuntu under WSL2** throughout this handout. Create and use the keys inside
Ubuntu, where your class Git commands run.

## 1. Check for an existing key

```bash
ls -al ~/.ssh
```

If the directory is missing, continue. If `id_ed25519` and `id_ed25519.pub` already
exist, you can reuse that pair on this computer. Do not overwrite an existing key.
If it is already connected to GitHub, try the connection test below first.
If that identifies your intended account, save the greeting as evidence and
skip to section 6. If authentication fails and this is your own key, reuse the
existing pair starting at section 3; do not generate over it.

For a different account or a connection error, use [troubleshooting](#troubleshooting).

## 2. Generate a key if needed

Replace the example email with yours:

```bash
ssh-keygen -t ed25519 -C "YOUR_GITHUB_EMAIL"
```

Press Enter to accept the default location only if it is unused. Type a
passphrase and repeat it when prompted; characters will not appear while typing. If you
choose another filename, substitute that path throughout this handout.
The `.pub` file is public; the file without `.pub` is private.

## 3. Add the key to an agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Repeat these commands in a later session if no agent is available or your key
is no longer loaded. `ssh-add -l` lists loaded key fingerprints.

See [GitHub's key generation and agent guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

## 4. Add the public key to GitHub

Display the public key and copy the entire single line:

```bash
cat ~/.ssh/id_ed25519.pub
```

Open GitHub **Settings → SSH and GPG keys → New SSH key**. Give the key a
recognizable title such as “Class laptop — Ubuntu”, select
**Authentication Key**, paste the public key, and save. See
[GitHub's instructions for adding a key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

Never upload, paste, commit, or submit the private key.

## 5. Verify the connection

```bash
ssh -T git@github.com
```

On first connection, compare the displayed host fingerprint with
[GitHub's published SSH fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints)
before accepting it. If it matches, type `yes` and press Enter. This checks the
server's identity; the prompt normally appears only on the first connection.

Success is a greeting identifying your GitHub username and saying authentication
succeeded. GitHub does not provide shell access, so that message is normal;
the successful test can exit with status `1`. See
[GitHub's connection test guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection).

## 6. Use an SSH repository URL

Copy **Code → SSH** from your repository on GitHub, or choose SSH in its
**Quick setup** area if the repository is empty. An SSH URL looks like
`git@github.com:OWNER/REPOSITORY.git`.

**First-time setup:** return to Assignment 0 and complete its clone step.
The following remote-change commands are only for an existing clone.

From inside that existing repository folder, inspect its remote with `git remote -v`. If it uses HTTPS,
replace the placeholder below with the copied SSH URL:

```bash
git remote set-url origin YOUR_SSH_CLONE_URL
git remote -v
```

Use the repository owned by your personal GitHub account. Its SSH URL should
contain your username.

## Troubleshooting

If you see `Permission denied (publickey)`, check that the correct public key is
in your GitHub account and that `ssh-add -l` lists your loaded key. Confirm you are running the command inside Ubuntu.

If the greeting names a different account, resolve that account mismatch before
continuing. A public key already attached to another account cannot simply be
added to another account. Follow [GitHub's key-already-in-use guide](https://docs.github.com/en/authentication/troubleshooting-ssh/error-key-already-in-use)
before changing an existing account setup.
