# ⚙️ CI/CD Pipeline with GitHub Actions

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-blue?logo=githubactions)
![Python](https://img.shields.io/badge/Python-3.10-yellow?logo=python)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![Status](https://img.shields.io/badge/All_Pipelines-Passing-brightgreen)

> 3 automated CI/CD pipelines built using GitHub Actions — triggering on every push to run Python scripts and Docker image builds.

---

## 📌 About This Project

This project contains 3 real GitHub Actions workflows built as part of my DevOps learning journey. Every time I push code to GitHub, all pipelines trigger automatically — no manual work needed.

**Skills practiced:** GitHub Actions, YAML, CI/CD, Docker, Python

---

## 📂 Project Structure

github-actions-cicd/
├── .github/
│   └── workflows/
│       ├── hello-world.yml       ← Pipeline 1
│       ├── python-runner.yml     ← Pipeline 2
│       └── docker-build.yml      ← Pipeline 3
├── scripts/
│   ├── hello.py
│   └── server-checker.py
├── Dockerfile
└── README.md

---

## 🚀 Pipelines Overview

| Pipeline | File | What It Does |
|----------|------|-------------|
| Hello World | `hello-world.yml` | Runs a Python script that prints timestamp and status |
| Python Runner | `python-runner.yml` | Installs requests library and runs server availability checker |
| Docker Build | `docker-build.yml` | Builds a Docker image of the Python app automatically |

---

## 🔧 How Each Pipeline Works

### Pipeline 1 — Hello World
- Triggers on every push
- Sets up Python 3.10 on Ubuntu
- Runs `hello.py` which prints timestamp and pipeline status

### Pipeline 2 — Python Script Runner
- Triggers on every push
- Sets up Python 3.10 and installs `requests` library
- Runs `server-checker.py` which monitors Google, GitHub and Python.org
- Reports each URL as UP or DOWN

### Pipeline 3 — Docker Build
- Triggers on every push
- Builds a Docker image using the Dockerfile
- Verifies the image was created successfully using `docker images`

---

## 🐳 Dockerfile

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY scripts/ .
RUN pip install requests
CMD ["python", "server-checker.py"]
```

---

## 📚 What I Learned

- How to write YAML workflow files for GitHub Actions
- How CI/CD pipelines trigger automatically on every push
- How to set up Python environment and install dependencies in a pipeline
- How Docker image builds integrate with CI/CD pipelines
- How to run and verify Docker containers inside GitHub Actions

---

## 👨‍💻 Author

**Akshat Dubey** — Aspiring DevOps/Cloud Engineer
- 📧 akshatautomates@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/akshatautomates/)
- 🐙 [GitHub](https://github.com/akshat20dubey)
