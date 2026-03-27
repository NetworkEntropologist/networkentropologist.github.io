---
layout: post
title: "An Introduction to GitHub Actions for CI/CD"
date: 2023-09-15 11:00:00 -0400
tags: [github-actions, ci-cd, devops, automation]
---

GitHub Actions is one of the most developer-friendly CI/CD tools available today — mainly because it lives right where your code already does. No separate dashboard, no webhook setup, no third-party account.

## Core Concepts

- **Workflow**: A YAML file in `.github/workflows/` that defines your automation.
- **Event**: What triggers the workflow (push, pull request, schedule, etc.).
- **Job**: A group of steps that run on the same runner.
- **Step**: An individual task — either a shell command or a reusable Action.
- **Runner**: The virtual machine that executes your job (Ubuntu, Windows, macOS).

## A Basic CI Workflow

Here's a workflow that installs dependencies, runs tests, and checks types on every push to `main`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      - run: npm ci
      - run: npm test
      - run: npm run typecheck
```

## Secrets

Sensitive values (API keys, deploy tokens) go in **Settings → Secrets and variables → Actions**. Reference them in workflows as `${{ secrets.MY_SECRET }}`. They're never logged or exposed in output.

## Marketplace

The [GitHub Actions Marketplace](https://github.com/marketplace?type=actions) has thousands of pre-built actions for everything from Slack notifications to deploying to AWS. Before writing a custom step, check whether an action already exists.

## Tips

- Use `npm ci` instead of `npm install` in CI — it's faster and deterministic.
- Cache dependencies with `actions/cache` or the built-in cache option in `setup-node`.
- Use `concurrency` groups to cancel in-progress runs when a new push arrives on the same branch.

GitHub Actions has replaced Jenkinsfiles, CircleCI configs, and Travis YAML for most of my projects. The zero-setup experience and tight GitHub integration make it hard to beat.
