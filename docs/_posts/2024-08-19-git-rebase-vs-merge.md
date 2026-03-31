---
layout: post
title: "Understanding Git Rebase vs Merge: When to Use Which"
date: 2024-08-19 10:00:00 -0400
categories: [git, version-control, workflow]
---

Few topics in software development spark more heated discussion than `git rebase` vs `git merge`. Both integrate changes from one branch into another — but they do it differently, and the choice matters.

## Merge

`git merge` creates a new "merge commit" that joins two branch histories. The full history of both branches is preserved, including exactly when they diverged and when they came back together.

```bash
git checkout main
git merge feature/my-feature
```

**Best for:** shared/public branches where preserving history is important. The audit trail is clear and non-destructive.

## Rebase

`git rebase` replays your commits on top of another branch, rewriting their history to appear as if they were always based on the latest code.

```bash
git checkout feature/my-feature
git rebase main
```

The result is a clean, linear history — easier to read with `git log`, and bisect with `git bisect`.

**Best for:** local/private branches you haven't pushed yet, or when your team values a clean linear history.

## The Golden Rule

Never rebase commits that exist on a remote branch others are working from. Rewriting shared history causes serious headaches for your teammates.

## My Workflow

I rebase locally to keep my feature branch current with `main` while I'm working, then use a merge (or a squash merge) when the feature is ready to land. Best of both worlds.
