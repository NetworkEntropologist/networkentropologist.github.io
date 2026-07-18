---
layout: post
title: "Creating Jekyll blog on GitHub Pages"
subtitle: "Part 1: creating a GitHub Pages repository and publishing a basic site"
date: 2026-04-01 12:00:00 +0200
categories: [technology, jekyll, github, website, projects]
permalink: posts/jekyll-site-part-1
---

It might seem rather self-referential that the first official blog post on this site should be about how I actually built and published this site, but it also seems like a good first topic. In fact, this is going to be part 1 in a multi-part series of posts. Either way, let's jump right into this.

### Thinking and Reasoning

When I first started working on this site I was planning to do this in Flask, and was going to self-host this using Azure Container Apps (this might actually be a topic for a future post), and had even started working on a blog engine for this. Maybe I should write a post about this topic in the future.

But while I did know about GitHub Pages, it somehow never occurred to me to use this, until one day I started (as one does) randomly digging into using GitHub Pages to host a blog site, and discovered that Jekyll is not only a thing, but it already has all of the capabilities that I was building into the blog engine I was working on.

I should mention at this point, that I have never in the past made any secret of my disdain in documentation for some OSS projects, and while the documentation for both Jekyll and GitHub Pages can be a bit obtusse at times, both are nonetheless pretty well documented. Hopefully this series will help you avoid the same problems I faced in this.

For your referene, the GitHub Pages documentation is available at <a href="https://docs.github.com/en/pages" target="_blank">https://docs.github.com/en/pages</a>

Also please note that I followed this process on MacOS, so most of the instructions and code snippets will be aimed at this platform.

### Process Overview

This process can be roughly divided into the following steps:

#### 1. Sign up with GitHub

I'm going to assume that since you are here you already have a GitHub account. If you don't I'm afraid that is outside of the scope of this guide.

#### 2. Create a GitHub Pages repo

This is the tricky part, but we will go through this step by step.

#### 3. Setup a basic Jekyll site

This part I struggled with a bit, but hopefully my struggles and notes will help you.

At this point you should now have a working, albeit basic Jekyll site, and should be ready to publish it. So let's jump right in. _Sans attendre_ as they say in French...

### Start with a GitHub repo

Just like most other coding or development projects, it starts with creating a GitHub repo. I am not going to insult your intelligence by going over this process step-by-step, so instead I'm going to just highlight some caveats here.

##### Repo naming

Normally a GitHub Pages sire URL follows a specific format, namely:

`https://pages.github.io/username/repo_name`

This means that if I created a repo named My-Fancy-Site, the URL would be rendered as `https://pages.github.io/NetworkEntropologist/My-Fancy-Site`.

While this might be fine for most projects, if you are creating your personal site, or any user site for that matter, you would more than likely prefer a nicer looking URL, such as `https://networkentropologist.github.io`. This is entirely possible, but has a few additional requirements.

Firstly, you can only create one of these per user, and secondly, the repo name has to follow a very specific standard, namely `username.github.io`. For example:

<img class="img-fluid" src="https://docs.github.com/assets/cb-48480/images/help/pages/create-repository-name-pages.png" />

##### Repo structure

There are very little requirements in terms of the basic repo structure. However, since the convention is to place any documentation (including sites) for a GitHub repo in the `docs` folder, this is what I went ahead and did for this.

It is also very important to note that for GitHub Pages to work correctly, the repo has to be public, unless you are fortunate enough to have a GitHub Enterprise account. And if you do, lucky you. I am not jealous in the slightest...

##### Initialise the repo locally

Now that you have created your GitHub repo, you need to initialise it in your local development environment. There is very little to keep in mind here, so feel free to follow your usual workflow for this. Personally, I use [GitHub Desktop](https://github.com/apps/desktop) to clone the repo locally, and then switch to VS Code to edit and Commit.

You may also at this time want to create a branch specifically for this site, and in fact this is GitHub's recommendation, so let's do that now, and let's follow the recommendation of using the `gh-pages` branch:

```
git checkout --orphan gh-pages
```

If you used a different branch name, make a note of this, as you will need this information further down the line.

### Setup Ruby and Jekyll

Now we need to setup the Ruby environment and related packages, which I personally found to be a slightly tricky process, but still not very difficult.

Start by installing Ruby. For a comprehensive list of installation instructions for your particular development environment, feel free to navigate to <a href="https://www.ruby-lang.org/en/documentation/installation/" target="_blank">Installing Ruby</a>.

You can install any version that supports Jekyll, but since the highest version supported by GitHub Pages is v3.3.4, this is the version that I chose to install with this command:

```sh
brew install ruby@3.3.4
```

Another caveat - since MacOS ships with Ruby pre-installed (the so-called System Ruby), and this version is often older than the version you may install, it is necessary to change the version in use every time you use it. You can this with this simple command:

```sh
chruby 3.3.4
ruby -v
```

The output of this should look similar to this:

    ruby 3.3.4 (2024-07-09 revision be1089c8ec) [x86_64-darwin22]

Next we need to install and configure Jekyll. I would highly recommend using <a href="https://bundler.io" target="_blank">Bundler</a> here, so let's install that next.

Start by creating a `Gemfile` in your website root (in my case this was inside the docs directory, as this is my site root), with this content:

```ruby
source 'https://rubygems.org'
gem 'nokogiri'
gem 'rack', '~> 2.2.4'
gem 'rspec'
```

Now simply install this with this command:

```sh
bundle install
```
