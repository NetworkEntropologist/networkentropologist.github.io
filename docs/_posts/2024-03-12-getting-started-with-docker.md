---
layout: post
title: "Getting Started with Docker: A Practical Introduction"
date: 2024-03-12 09:15:00 -0500
tags: [docker, devops, containers, beginner]
---

If you've been hearing about Docker for a while but haven't taken the plunge, this post is for you. Docker is a platform that lets you package your application and all its dependencies into a standardised unit called a **container**. Containers are lightweight, portable, and consistent — which means if it runs on your machine, it'll run anywhere.

## Why Bother?

The classic "it works on my machine" problem is real. Docker eliminates it by bundling everything your app needs — runtime, libraries, environment variables, config files — into a single image.

## Installing Docker

Head to [docs.docker.com](https://docs.docker.com) and grab Docker Desktop for your OS. Once installed, verify it's working:

```bash
docker --version
docker run hello-world
```

## Your First Dockerfile

Here's a minimal Dockerfile for a Node.js app:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
```

Build and run it:

```bash
docker build -t my-app .
docker run -p 3000:3000 my-app
```

That's it. Your app is now running in a container. From here, look into Docker Compose for multi-service setups — it's where things get really powerful.
