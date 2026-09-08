# Handout: GitHub SSH on macOS and Ubuntu under WSL2

[Back to Assignment 0](../assignments/assignment-0-environment-setup.md)

## Why SSH?

SSH authenticates your computer to GitHub when you clone or push using an SSH URL.
A key pair has a **public key**, which you add to GitHub, and a **private key**,
which stays on your computer. A passphrase protects the private key; an SSH agent
can hold the unlocked key for use by Git. Git's configured name and email label
commits but do not authenticate you.

Use **macOS Terminal** or **Ubuntu under WSL2** throughout this handout. On Windows,
create and use the keys inside Ubuntu, where your class Git commands run.

## 1. Check for an existing key

```bash
ls -al ~/.ssh
```

If the directory is missing, continue. If `id_ed25519` and `id_ed25519.pub` already
exist, you can reuse that pair on this computer. Do not overwrite an existing key.
If it is already connected to GitHub, try the connection test below first.

## 2. Generate a key if needed

Replace the example email with yours:

```bash
ssh-keygen -t ed25519 -C "YOUR_GITHUB_EMAIL"
```

Accept the default location only if it is unused. Choose a passphrase. If you
choose another filename, substitute that path throughout this handout.
The `.pub` file is public; the file without `.pub` is private.

## 3. Add the key to an agent

**Ubuntu under WSL2:**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Repeat these commands in a later session if no agent is available or your key
is no longer loaded. `ssh-add -l` lists loaded key fingerprints.

**macOS:**

```bash
eval "$(ssh-agent -s)"
touch ~/.ssh/config
vi ~/.ssh/config
```

Merge these settings into an existing `Host github.com` block, or add the block
if it does not exist. Preserve other configuration:

```sshconfig
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Save with `Esc`, `:wq`, Enter, then run Apple's SSH-add command:

```bash
/usr/bin/ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

If you created a key without a passphrase, omit `UseKeychain` and use
`/usr/bin/ssh-add ~/.ssh/id_ed25519` instead. These platform steps follow
[GitHub's key generation and agent guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

## 4. Add the public key to GitHub

On macOS, copy it to the clipboard:

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

On Ubuntu under WSL2, display it and copy the entire single line:

```bash
cat ~/.ssh/id_ed25519.pub
```

Open GitHub **Settings → SSH and GPG keys → New SSH key**. Give the key a
recognizable title such as “Class laptop — Ubuntu” or “Class laptop — Mac”, select
**Authentication Key**, paste the public key, and save. See
[GitHub's instructions for adding a key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

Never upload, paste, commit, or submit the private key.

## 5. Verify the connection

```bash
ssh -T git@github.com
```

On first connection, compare the displayed host fingerprint with
[GitHub's published SSH fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints)
before accepting it. This checks the server's identity.

Success is a greeting identifying your GitHub username and saying authentication
succeeded. GitHub does not provide shell access, so that message is normal;
the successful test can exit with status `1`. See
[GitHub's connection test guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection).

If you see `Permission denied (publickey)`, check that the correct public key is
in your GitHub account and that `ssh-add -l` lists your loaded key. Windows users
should confirm they are running the command inside Ubuntu.

## 6. Use an SSH repository URL

Copy **Code → SSH** from your repository on GitHub. An SSH URL looks like
`git@github.com:OWNER/REPOSITORY.git`.

For an existing clone, inspect its remote with `git remote -v`. If it uses HTTPS,
replace the placeholder below with the copied SSH URL:

```bash
git remote set-url origin YOUR_SSH_CLONE_URL
git remote -v
```

SSH authentication does not grant access to every repository. Accept your class
invitation and verify that your account has access to your assigned repository.
