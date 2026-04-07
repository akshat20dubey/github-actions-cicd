# ⚙️ CI/CD Pipeline with GitHub Actions

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-blue?logo=githubactions)
![Python](https://img.shields.io/badge/Python-3.10-yellow?logo=python)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![Status](https://img.shields.io/badge/Pipeline-Passing-brightgreen)

> Automated CI/CD pipelines built using GitHub Actions — triggering builds, tests, and Docker deployments on every push.

---

## 📌 About This Project

This project contains 3 real GitHub Actions workflows I built as part of my DevOps learning journey. Every time I push code, the pipelines automatically run — no manual work needed.

**Skills practiced:** GitHub Actions, YAML, CI/CD, Docker, Python

---

## 📂 Project Structure

---

## 🚀 Pipelines Overview

| Pipeline | Trigger | What it does |
|----------|---------|-------------|
| `hello-world.yml` | Every push | Runs a simple Python script |
| `python-runner.yml` | Every push | Sets up Python, installs libraries, runs script |
| `docker-build.yml` | Every push | Builds a Docker image automatically |

---

## 🔧 How CI/CD Works Here

1. I write code and run `git push`
2. GitHub Actions **automatically detects** the push
3. It spins up a **fresh Ubuntu machine** in the cloud
4. Runs all the steps — setup, install, execute
5. Shows ✅ green tick if everything passed

---

## 📚 What I Learned

- How to write YAML workflow files for GitHub Actions
- How CI/CD pipelines trigger automatically on every push
- How to set up Python environment inside a pipeline
- How Docker image builds integrate with CI/CD

---

## 👨‍💻 Author

**Akshat Dubey** — Aspiring DevOps/Cloud Engineer

- 📧 akshatautomates@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/akshatautomates/)
- 🐙 [GitHub](https://github.com/akshat20dubey)
