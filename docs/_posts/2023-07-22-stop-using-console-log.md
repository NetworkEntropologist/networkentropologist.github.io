---
layout: post
title: "Stop Using console.log for Debugging"
date: 2023-07-22 17:05:00 -0400
tags: [javascript, debugging, productivity, developer-experience]
---

`console.log` is fine. But leaning on it exclusively is leaving a lot of productivity on the table. Here are three better approaches I now use daily.

**1. The Node.js Debugger (and VS Code's Debug Panel)**

Most developers don't know Node ships with a built-in inspector. Run your script with `--inspect-brk` and attach VS Code's debugger, or open `chrome://inspect` in Chrome. You get breakpoints, watch expressions, call stacks, and the ability to step through code line by line. It sounds fancy but takes about 60 seconds to set up.

**2. `console.table`**

When you're logging arrays of objects, swap `console.log` for `console.table`. It renders a proper table in the terminal/console with columns for each key. Dramatically easier to scan than `[Object, Object, Object]`.

```js
console.table(users); // instead of console.log(users)
```

**3. Conditional Breakpoints**

In any modern browser or VS Code, you can right-click a breakpoint and add a condition. The debugger only pauses when the condition is true — invaluable when you're debugging something that only happens on the 500th iteration of a loop.

Logging has its place, but learning your debugger is one of the highest-leverage investments you can make as a developer.
