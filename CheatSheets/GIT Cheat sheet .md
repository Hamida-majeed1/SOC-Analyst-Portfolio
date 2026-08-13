# Git Cheat Sheet

## Repository Setup

```bash
git init
```

Initialize a new Git repository.

```bash
git clone <repository-url>
```

Clone an existing repository.

## Check Repository Status

```bash
git status
```

Check modified, staged, and untracked files.

## Add Files to Staging Area

```bash
git add <file>
```

Stage a specific file.

```bash
git add .
```

Stage all changed files.

## Commit Changes

```bash
git commit -m "message"
```

Save staged changes with a descriptive message.

## View Commit History

```bash
git log
```

Show commit history.

```bash
git log --oneline
```

Show a short version of commit history.

## Branches

```bash
git branch
```

List branches.

```bash
git branch <branch-name>
```

Create a new branch.

```bash
git switch <branch-name>
```

Switch to another branch.

```bash
git switch -c <branch-name>
```

Create and switch to a new branch.

## Merge

```bash
git merge <branch-name>
```

Merge another branch into the current branch.

## Remote Repository

```bash
git remote -v
```

Show connected remote repositories.

```bash
git push
```

Upload local commits to the remote repository.

```bash
git pull
```

Download and integrate changes from the remote repository.

```bash
git fetch
```

Download remote changes without merging them.

## Useful Commands

```bash
git diff
```

Show unstaged changes.

```bash
git diff --staged
```

Show staged changes.

```bash
git restore <file>
```

Discard unstaged changes in a file.

```bash
git rm <file>
```

Remove a file and stage the removal.

## Basic Git Workflow

```text
Working Directory
       ↓
   git add
       ↓
Staging Area
       ↓
  git commit
       ↓
 Local Repository
       ↓
   git push
       ↓
Remote Repository (GitHub)
```

## Quick Workflow

```bash
git init
git status
git add .
git commit -m "Initial commit"
git push
```
