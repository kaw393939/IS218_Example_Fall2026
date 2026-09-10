# Handout: Terminal and vi Basics

[Assignment 0 for Windows](../assignments/assignment-0-windows.md) ·
[Assignment 0 for Mac](../assignments/assignment-0-mac.md)

## Why practice these tools?

Terminal commands make your work repeatable: you can tell someone exactly how to
open a folder, run code, or verify a test. A terminal editor is useful on a server or whenever a graphical editor is
unavailable. This is a short introduction to vi, not a requirement to use it
for daily work. Use VS Code for project editing and Git messages.

Run these examples in macOS Terminal or Ubuntu under WSL2. Paths are relative to
your current directory unless they start with `/` or `~`. The symbol `~` means
your home directory, `.` means the current directory, and `..` means its parent.

## Essential terminal commands

| Command | Purpose |
| --- | --- |
| `pwd` | Print the current directory |
| `ls` | List files and folders |
| `ls -la` | Include hidden files and details |
| `cd ~/projects` | Move to your projects folder |
| `cd ..` | Move up one directory |
| `mkdir -p ~/terminal-practice` | Create a practice directory if needed |
| `cat practice.txt` | Display a text file |
| `cp practice.txt practice-copy.txt` | Copy a file |
| `mv practice-copy.txt renamed.txt` | Rename or move a file |
| `code .` | Open the current folder in VS Code |
| `git status` | Inspect a repository's working tree |

The table is a reference, not a sequence to paste. A folder must exist before
you can `cd` into it, and `git status` works only inside a repository. Use the
exercise below for your first practice session.

Copy and paste shortcuts differ from Ctrl+C, which interrupts a command. In
macOS Terminal, use Command+C and Command+V. In a Windows Terminal Ubuntu tab,
use Ctrl+Shift+C and Ctrl+Shift+V. See the
[Mac Terminal shortcuts](https://support.apple.com/guide/terminal/keyboard-shortcuts-trmlshtcts/mac)
and [Windows Terminal keybindings](https://learn.microsoft.com/en-us/windows/terminal/customize-settings/actions#copy).

Use Tab to complete paths, Up Arrow to recall commands, and Ctrl+C to interrupt
a running command. Quote paths containing spaces: `cd "my folder"`. Commands such
as `cp` and `mv` can replace existing destinations; check filenames first.

## vi modes and commands

Open a file with `vi practice.txt`. vi starts in **normal mode**, where keys are
commands. Press `i` to enter **insert mode** and type text. Press `Esc` to return
to normal mode. Commands starting with `:` finish when you press Enter.

| Keys in normal mode | Action |
| --- | --- |
| `i` | Enter insert mode before the cursor |
| `h`, `j`, `k`, `l` | Move left, down, up, right |
| `x` | Delete the character under the cursor |
| `dd` | Delete the current line |
| `u` | Undo the last change |
| `/word`, Enter | Search forward for `word` |
| `n` | Repeat the search |
| `:w`, Enter | Save |
| `:q`, Enter | Quit if there are no unsaved changes |
| `:wq`, Enter | Save and quit |
| `:q!`, Enter | Discard unsaved changes and quit |

If you feel stuck, press `Esc` first. Then use `:wq` to keep your edits or `:q!`
to discard them. If a swap-file warning appears, read it and check whether another
editor still has the file open before choosing recovery or deletion.

## Practice exercise

If you have done this exercise before, use a new filename such as
`practice-2.txt` in every command below to preserve your earlier work.

1. Create a practice folder outside your repository:

   ```bash
   mkdir -p ~/terminal-practice
   cd ~/terminal-practice
   pwd
   vi practice.txt
   ```

2. Press `i` and type two lines describing what a terminal and Git do.
3. Press `Esc`, type `:wq`, and press Enter.
4. Run `cat practice.txt` to verify the saved contents.
5. Reopen it with `vi practice.txt`, press `i`, and add an unwanted word.
6. Press `Esc`, type `:q!`, and press Enter. Run `cat practice.txt` again and
   confirm the unwanted edit was discarded.
7. Save this terminal output and your practice file if the extension is assigned. Run `code .`
   to open the same folder in VS Code. Locate your saved file.

Explain the difference between saving and quitting, and between normal and
insert modes. For more practice, run `vimtutor` if available or consult the
[official Vim learning resources](https://www.vim.org/docs.php).
