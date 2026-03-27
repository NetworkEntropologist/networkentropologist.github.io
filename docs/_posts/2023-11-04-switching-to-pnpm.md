---
layout: post
title: "Why I Switched from npm to pnpm"
date: 2023-11-04 14:30:00 -0500
tags: [javascript, tooling, npm, pnpm]
---

After years of using npm (and a brief stint with Yarn), I switched to pnpm on all my projects about six months ago. Here's the short version of why I'm not going back.

**Disk space.** pnpm uses a global content-addressable store, so packages are never duplicated across projects. If ten projects depend on `lodash@4.17.21`, there's exactly one copy on disk. My SSD thanks me daily.

**Speed.** Installation is noticeably faster, especially on CI where cache hits are common.

**Strict by default.** npm and Yarn hoist packages in a way that lets you silently depend on things you never declared. pnpm's isolated `node_modules` structure catches these phantom dependencies immediately, which surfaces real bugs early.

Switching is straightforward:

```bash
npm install -g pnpm
pnpm import   # converts existing package-lock.json
pnpm install
```

The CLI is nearly identical to npm, so the learning curve is basically zero. Give it a try on your next project.
