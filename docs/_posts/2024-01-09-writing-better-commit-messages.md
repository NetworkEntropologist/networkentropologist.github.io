---
layout: post
title: "Writing Better Commit Messages"
date: 2024-01-09 16:20:00 -0500
categories: [git, best-practices, workflow]
---

A good commit message is a gift to your future self. Here's the format I follow, loosely based on the [Conventional Commits](https://www.conventionalcommits.org/) spec:

```
<type>(<scope>): <short summary>

<optional body>

<optional footer>
```

**Types I use most:** `feat`, `fix`, `refactor`, `docs`, `chore`, `test`.

**Examples of bad vs good:**

| Bad | Good |
|-----|------|
| `fix stuff` | `fix(auth): handle expired JWT tokens gracefully` |
| `wip` | `refactor(api): extract pagination logic into helper` |
| `updated deps` | `chore: bump express from 4.18 to 4.19` |

Keep the summary line under 72 characters. Use the body to explain *why*, not *what* — the diff already shows what changed. Reference issue numbers in the footer.

It takes ten extra seconds to write a good message. Six months from now, `git log --oneline` will tell a coherent story instead of a wall of `fix`, `fix`, `fix`.
