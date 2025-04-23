# Developer Guide – Bloom Assist Chatbot

Welcome to the Developer Guide for the **Bloom Assist Chatbot**, a capstone project designed to help social workers and individuals navigate affordable housing resources using a conversational AI interface.

This document is intended for contributors and team members working on the project. It covers everything you need to know to set up, develop, and contribute to the codebase.

---

## Overview

Bloom Assist is a single-turn RAG (Retrieval-Augmented Generation) chatbot designed to surface relevant, up-to-date housing information through a simple conversational interface.

---

## Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Frontend     | **Next.js** (sites/chatbot) |
| Backend      | **NestJS** (api/) |
| Microservice | **FastAPI** (python-llm-service/) |
| Database     | **ChromaDB** |
| Other        | Yarn, Markdown, Python 3.x |

---

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/glarerena/jtc-capstone-2025.git
cd jtc-capstone-2025
```
### 2. Start the Python Microservice

```bash
cd python-llm-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```
Leave this terminal running.

### 3. Start the NestJS BackEnd
```bash
cd api
yarn install
yarn start
```
Leave this terminal running.

### 4. Start the Next.js Frontend
```bash
cd sites/chatbot
yarn install
yarn dev
```
Visit: http://localhost:3000 to interact with the chatbot.

## Git Workflow

Main Branches:

main: Final production-ready version
merge: Capstone integration branch for tested code
Feature branches (e.g. frontend-ui, api-setup, etc.)

Guidelines:

Do not push directly to main or merge.
Create a branch from your assigned base (e.g., frontend-ui).
Submit a pull request for review.
Tag teammates for approval.
Merges are handled by the assigned lead.

## Project Structure

jtc-capstone-2025/
├── api/                    # NestJS backend
├── python-llm-service/     # FastAPI chatbot microservice
├── sites/chatbot/          # Next.js frontend
├── context/                # Markdown knowledge base for RAG
├── ethics_disclaimer.md
├── agile_plan.md
├── check_list.md
├── contributing.md
└── README.md

## Contribution Guidelines

### 1. Create New Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes
Write clean, well documented code and test before commiting.

```bash
git add .
git commit -m "Add [feature]: Short description"
```

### 3. Commit Changes
```bash
git add .
git commit -m "Add [feature]: Short description"
```

### 4. Push to GitHub
```bash
git push origin feature/your-feature-name
```

### 5. Open a Pull Request

Go to the GitHub repository
Click “Compare & Pull Request”
Add reviewers
Include a brief summary of changes

## Questions or Issues
Questions or Issues?
Open an issue on GitHub
Tag team members in your pull request for review
Use Slack for quick communication and feedback

## License
This project is licensed under the MIT License.

