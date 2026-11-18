# Lab Report

**Name:** Taha Amer  **Registration No:** FA23-BSE-180
**Course:** DevOps for Cloud Computing (CSC418) - Lab Assignment 4

## 1. Git vs GitHub; add, commit, push
Git is the version control tool that runs on my computer and records the history of my files.
GitHub is a website that hosts Git repositories online and adds teamwork features such as
Issues, Pull Requests and Actions. `git add` puts changes into the staging area, `git commit`
saves a snapshot of the staged changes with a message, and `git push` uploads my commits to GitHub.

## 2. Branches, Pull Requests and merge conflicts
Branches let me build a feature separately so the stable `main` branch is not broken. A Pull
Request lets others review the changes and discuss them before they are merged. A merge conflict
happens when two branches change the same lines of a file differently, so Git cannot decide which
version to keep and asks a person to choose.

## 3. fetch vs pull, merge vs rebase
`git fetch` only downloads new commits from the remote without changing my files, while `git pull`
fetches and then merges them into my current branch. `git merge` joins two branches and keeps both
histories with a merge commit. `git rebase` replays my commits on top of another branch, which gives
a straight, linear history but rewrites those commits.

## 4. Issues and Actions
GitHub Issues track tasks, bugs and ideas with labels, so the team knows what to work on and PRs can
be linked to them. GitHub Actions runs automated workflows, such as the unit tests, on every push
and pull request, so mistakes are found early and the team can trust what is merged.

## 5. A difficulty I faced
**WRITE THIS IN YOUR OWN WORDS before submitting.** For example: describe a real problem you hit
(a Git error, the merge conflict, or the failing test run) and how you solved it.
