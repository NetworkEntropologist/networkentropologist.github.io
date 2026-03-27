---
layout: post
title: "How I Set Up a New Mac for Development in 2024"
date: 2024-10-01 09:30:00 -0400
tags: [macos, setup, tooling, productivity, beginner]
---

Every time I set up a new Mac I tweak the process a little. Here's my current approach — opinionated but efficient.

## 1. Homebrew First

Everything flows from [Homebrew](https://brew.sh). Install it, then use a `Brewfile` to declaratively install everything else:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

My `Brewfile` includes: `git`, `gh`, `node`, `pnpm`, `python`, `postgresql`, `redis`, `httpie`, `bat`, `eza`, `fzf`, `ripgrep`, and a handful of Cask apps.

## 2. Zsh + Starship

I use Zsh (default on macOS) with [Starship](https://starship.rs) for the prompt. Starship is fast, written in Rust, and requires zero plugin manager overhead.

## 3. nvm for Node Versions

Even if pnpm is my package manager, I use `nvm` (or `fnm` — it's faster) to manage multiple Node versions across projects.

## 4. SSH Keys and Git Config

Generate an Ed25519 key, add it to GitHub, then set your global Git identity and a sensible `.gitconfig`:

```bash
ssh-keygen -t ed25519 -C "you@example.com"
gh ssh-key add ~/.ssh/id_ed25519.pub
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

## 5. macOS Defaults

A handful of `defaults write` commands make the OS more dev-friendly: show hidden files in Finder, enable key repeat, turn off autocorrect. I keep these in a `macos.sh` script in my dotfiles repo so I never have to remember them.

## 6. Dotfiles

Everything — `.zshrc`, `.gitconfig`, Starship config, VS Code settings — lives in a private GitHub repo. I clone it on day one and symlink with a small shell script. Day-two productivity unlocked.

The whole process takes about 30–45 minutes and results in an environment that's identical to my old machine.
