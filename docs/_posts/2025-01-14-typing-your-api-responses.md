---
layout: post
title: "The Case for Typing Your API Responses"
date: 2025-01-14 12:00:00 -0500
tags: [typescript, api, best-practices, backend]
---

One of the most common sources of runtime bugs in TypeScript projects is untyped API responses. You call `fetch`, get back `any`, and TypeScript goes quiet — right when you need it most.

The fix is straightforward: use a schema validation library to parse and type your responses at the boundary.

## Zod Makes This Easy

[Zod](https://zod.dev) lets you define a schema and parse unknown data against it. If the data doesn't match, it throws a descriptive error. If it does, you get a fully-typed object.

```ts
import { z } from 'zod';

const UserSchema = z.object({
  id: z.number(),
  name: z.string(),
  email: z.string().email(),
  role: z.enum(['admin', 'user', 'guest']),
  createdAt: z.string().datetime(),
});

type User = z.infer<typeof UserSchema>;

async function getUser(id: number): Promise<User> {
  const res = await fetch(`/api/users/${id}`);
  const data = await res.json();
  return UserSchema.parse(data); // throws if shape is wrong
}
```

Now `getUser` returns a proper `User` type and will surface API contract violations at runtime instead of silently propagating `undefined` through your UI.

## Why Not Just Cast?

```ts
const data = await res.json() as User; // don't do this
```

This compiles fine but proves nothing. If the API returns `null` for `email`, TypeScript won't notice — Zod will.

## Alternatives

- **Valibot** — similar to Zod but tree-shakeable and tiny.
- **Arktype** — very fast, ergonomic syntax.
- **TypeBox** — generates JSON Schema, great if you need runtime schema sharing.

Pick any of them. Just pick one. Your future self debugging a `Cannot read properties of undefined` error at 11pm will be grateful.
